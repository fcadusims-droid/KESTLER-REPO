"""Os portões de validação — Fases 1, 2 e 3.

O produto destas fases não é a simulação: é a medição dela. Um mundo onde todos
se encontram todo dia faz o drama virar ruído; um segredo que nunca se move não
é segredo; uma distribuição de pressão sem cauda pesada é um mundo onde nada
importa. Cada portão existe para detectar uma dessas falhas, e a regra é sempre
a mesma — quando um reprova, conserta-se o modelo, nunca o número do portão.
"""

from __future__ import annotations

import json
import pathlib
import sqlite3
from collections import Counter
from itertools import combinations

from . import clock as clockmod


def collect(conn: sqlite3.Connection, from_tick: int, to_tick: int) -> dict:
    agents = {row["id"]: row for row in conn.execute("SELECT * FROM agent")}
    total_ticks = max(1, to_tick - from_tick)
    days = max(1, total_ticks / clockmod.TICKS_PER_DAY)

    encounters = list(
        conn.execute(
            "SELECT tick, location_id, channel, agent_a, agent_b FROM encounter"
            " WHERE tick >= ? AND tick < ?",
            (from_tick, to_tick),
        )
    )

    pair_counts = Counter((row["agent_a"], row["agent_b"]) for row in encounters)
    per_agent = Counter()
    for row in encounters:
        per_agent[row["agent_a"]] += 1
        per_agent[row["agent_b"]] += 1

    # Pares possíveis considera só quem coexiste: dois agentes que nunca
    # estiveram no mundo ao mesmo tempo não são um par perdido.
    possible = 0
    for a, b in combinations(sorted(agents), 2):
        overlap_start = max(agents[a]["arrival_tick"], agents[b]["arrival_tick"], from_tick)
        if overlap_start < to_tick:
            possible += 1

    # Saturação diária: fração dos pares possíveis que se encontram num dia médio.
    by_day: dict[int, set] = {}
    for row in encounters:
        day = row["tick"] // clockmod.TICKS_PER_DAY
        by_day.setdefault(day, set()).add((row["agent_a"], row["agent_b"]))
    daily_saturation = (
        sum(len(pairs) for pairs in by_day.values()) / len(by_day) / possible
        if by_day and possible else 0.0
    )

    total = len(encounters)
    top_pair_share = (pair_counts.most_common(1)[0][1] / total) if total else 0.0

    active_agents = [
        aid for aid, row in agents.items() if row["arrival_tick"] < to_tick
    ]
    isolates = [aid for aid in active_agents if per_agent[aid] == 0]

    return {
        "days": days,
        "agents_active": len(active_agents),
        "encounters": total,
        "encounters_per_day": total / days,
        "pairs_met": len(pair_counts),
        "pairs_possible": possible,
        "pair_coverage": len(pair_counts) / possible if possible else 0.0,
        "daily_saturation": daily_saturation,
        "top_pair_share": top_pair_share,
        "top_pairs": pair_counts.most_common(6),
        "isolates": isolates,
        "per_agent": per_agent,
        "by_channel": Counter(row["channel"] for row in encounters),
        "by_location": Counter(row["location_id"] for row in encounters),
        "agents": agents,
    }


# Critérios de saída da Fase 1. Cada um existe por um motivo declarado.
GATES = [
    ("tempo de execução < 10s", lambda m, w: w < 10.0),
    ("nenhum agente isolado", lambda m, w: not m["isolates"]),
    ("saturação diária < 20%", lambda m, w: m["daily_saturation"] < 0.20),
    ("nenhum par domina (< 12%)", lambda m, w: m["top_pair_share"] < 0.12),
    ("cobertura de pares > 50%", lambda m, w: m["pair_coverage"] > 0.50),
]


def render(metrics: dict, wall_seconds: float) -> tuple[str, bool]:
    m = metrics
    lines: list[str] = []
    add = lines.append

    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA FASE 1")
    add("=" * 62)
    add(f"  dias simulados        {m['days']:.0f}")
    add(f"  agentes ativos        {m['agents_active']}")
    add(f"  tempo de execução     {wall_seconds:.2f}s")
    add("")
    add(f"  encontros             {m['encounters']} ({m['encounters_per_day']:.1f}/dia)")
    add(f"  pares distintos       {m['pairs_met']} de {m['pairs_possible']} possíveis")
    add(f"  cobertura de pares    {m['pair_coverage']:.1%}")
    add(f"  saturação diária      {m['daily_saturation']:.1%}")
    add(f"  fatia do maior par    {m['top_pair_share']:.1%}")
    add("")

    add("  canais")
    for channel, count in m["by_channel"].most_common():
        add(f"    {channel:<14} {count}")
    add("")

    add("  pares mais frequentes")
    for (a, b), count in m["top_pairs"]:
        na = m["agents"][a]["name"]
        nb = m["agents"][b]["name"]
        add(f"    {count:>5}  {na} × {nb}")
    add("")

    add("  encontros por agente")
    for aid, row in sorted(m["agents"].items(), key=lambda kv: -m["per_agent"][kv[0]]):
        if row["arrival_tick"] >= 0:
            count = m["per_agent"][aid]
            arrival_day = row["arrival_tick"] // clockmod.TICKS_PER_DAY
            mark = "  ← isolado" if count == 0 else ""
            add(f"    {count:>5}  {row['name']:<24} (chegou dia {arrival_day}){mark}")
    add("")

    add("  locais mais movimentados")
    for location_id, count in m["by_location"].most_common(5):
        add(f"    {count:>5}  {location_id}")
    add("")

    add("-" * 62)
    all_passed = True
    for label_text, check in GATES:
        passed = check(m, wall_seconds)
        all_passed &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    add("  FASE 1 APROVADA" if all_passed else "  FASE 1 REPROVADA — ajustar rotinas/grafo, não os pesos")
    add("=" * 62)

    return "\n".join(lines), all_passed


# ===========================================================================
# FASE 2 — difusão de crença
# ===========================================================================

def collect_phase2(conn: sqlite3.Connection, to_tick: int,
                   world_name: str = "distrito") -> dict:
    agents = {row["id"]: row for row in conn.execute("SELECT * FROM agent")}
    facts = {row["id"]: row for row in conn.execute("SELECT * FROM fact")}

    beliefs = list(conn.execute("SELECT * FROM belief"))
    by_fact: dict[int, list] = {}
    for b in beliefs:
        by_fact.setdefault(b["fact_id"], []).append(b)

    # O segredo do portão vem DECLARADO nos dados do mundo. Procurá-lo por nome
    # de personagem cravado aqui acoplava o instrumento a um mundo só: na vila
    # não existe Severin, e o portão passava em branco sem medir nada.
    import json as _json
    spec_path = (pathlib.Path(__file__).resolve().parent.parent / "data"
                 / world_name / "seed_facts.json")
    spec = {}
    if spec_path.exists():
        spec = _json.loads(spec_path.read_text(encoding="utf-8")).get("gate_secret", {})
    secret_id = next(
        (fid for fid, f in facts.items()
         if f["subject"] == spec.get("subject")
         and f["predicate"] == spec.get("predicate")),
        None,
    ) if spec else None
    holders = by_fact.get(secret_id, []) if secret_id else []
    # Quem sabe além do sujeito e da testemunha original.
    original = set()
    if secret_id:
        import json as _json
        original = set(_json.loads(facts[secret_id]["witnesses_json"]))

    # O critério do plano é temporal: "difusão parcial e distorcida em ~30-60
    # dias". Medir no fim de uma execução de qualquer duração mede outra coisa —
    # uma run mais longa reprovaria só por ter continuado a rodar. A janela de
    # avaliação é fixa em 60 dias (ou o fim, se a run for mais curta).
    GATE_DAY = 60
    gate_tick = min(to_tick, GATE_DAY * clockmod.TICKS_PER_DAY)
    at_gate = [b for b in holders if b["acquired_tick"] < gate_tick]

    curve = []
    for day in (10, 20, 30, 45, 60, 90):
        t = day * clockmod.TICKS_PER_DAY
        if t > to_tick:
            break
        curve.append((day, sum(1 for b in holders if b["acquired_tick"] < t)))

    spread = [b for b in holders if b["agent_id"] not in original]
    distorted = [b for b in holders if b["distortion"] > 0]
    secondhand = [b for b in holders if b["source_agent_id"] is not None]
    firsthand = [b for b in holders if b["source_agent_id"] is None]

    out_of_bounds = [
        b for b in beliefs
        if not (0.0 <= b["confidence"] <= 1.0) or not (0.0 <= b["salience"] <= 1.0)
    ]

    relations = list(conn.execute("SELECT * FROM relation"))
    saturated = [r for r in relations if r["tension"] >= 0.99]

    # O sujeito do segredo nunca pode ser a fonte de ninguém.
    leaked_by_subject = [
        b for b in holders if b["source_agent_id"] == facts[secret_id]["subject"]
    ] if secret_id else []

    return {
        "agents": agents,
        "facts": facts,
        "beliefs": beliefs,
        "secret_id": secret_id,
        "secret_holders": holders,
        "secret_spread": spread,
        "secret_reach": len(at_gate) / max(1, len(agents)),
        "secret_reach_final": len(holders) / max(1, len(agents)),
        "gate_day": GATE_DAY,
        "curve": curve,
        "distorted_share": len(distorted) / max(1, len(holders)),
        "conf_firsthand": (sum(b["confidence"] for b in firsthand) / len(firsthand)) if firsthand else 0.0,
        "conf_secondhand": (sum(b["confidence"] for b in secondhand) / len(secondhand)) if secondhand else 0.0,
        "out_of_bounds": out_of_bounds,
        "leaked_by_subject": leaked_by_subject,
        "relations": relations,
        "tension_saturated": saturated,
        "tension_mean": (sum(r["tension"] for r in relations) / len(relations)) if relations else 0.0,
        "by_fact": by_fact,
    }


GATES_P2 = [
    ("segredo escapou do círculo original", lambda m: len(m["secret_spread"]) > 0),
    ("difusão parcial em 60 dias (15%-70%)", lambda m: 0.15 <= m["secret_reach"] <= 0.70),
    ("informação degrada ao circular", lambda m: m["distorted_share"] > 0.0),
    ("segunda mão < primeira mão", lambda m: m["conf_secondhand"] < m["conf_firsthand"]),
    ("crenças dentro dos limites", lambda m: not m["out_of_bounds"]),
    ("sujeito nunca vaza o próprio segredo", lambda m: not m["leaked_by_subject"]),
    ("tensão não satura", lambda m: not m["tension_saturated"]),
]


def render_phase2(m: dict) -> tuple[str, bool]:
    lines: list[str] = []
    add = lines.append

    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA FASE 2 (verdade vs. crença)")
    add("=" * 62)
    add(f"  fatos no mundo        {len(m['facts'])}")
    add(f"  crenças formadas      {len(m['beliefs'])}")
    add("")

    if m["secret_id"] is None:
        add("  SEM SEGREDO PLANTADO — o portão não pode ser avaliado")
        add("=" * 62)
        return "\n".join(lines), False

    secret = m["facts"][m["secret_id"]]
    add(f"  O SEGREDO: {secret['subject']} · {secret['predicate']} · {secret['object']}")
    add(f"  visibilidade: {secret['visibility']}")
    add("")
    add(f"  sabem em {m['gate_day']} dias      {m['secret_reach']:.0%} do elenco   <- portão")
    add(f"  sabem no fim          {len(m['secret_holders'])} de {len(m['agents'])}"
        f"  ({m['secret_reach_final']:.0%})")
    if m["curve"]:
        traco = "  ".join(f"d{d}:{n}" for d, n in m["curve"])
        add(f"  curva de difusão      {traco}")
    add(f"  fora do círculo       {len(m['secret_spread'])}")
    add(f"  versão distorcida     {m['distorted_share']:.0%} de quem sabe")
    add(f"  confiança 1ª mão      {m['conf_firsthand']:.2f}")
    add(f"  confiança 2ª mão      {m['conf_secondhand']:.2f}")
    add("")
    add("  quem acredita em quê")
    for b in sorted(m["secret_holders"], key=lambda x: -x["confidence"]):
        name = m["agents"][b["agent_id"]]["name"]
        crenca = b["distorted_object"] or secret["object"]
        via = m["agents"][b["source_agent_id"]]["name"] if b["source_agent_id"] else "viu"
        add(f"    {name:<22} {crenca:<26} conf {b['confidence']:.2f}"
            f"  d{b['distortion']}  ({via})")
    add("")
    add(f"  tensão média por aresta  {m['tension_mean']:.3f}"
        f"   saturadas: {len(m['tension_saturated'])}")
    add("")

    add("-" * 62)
    ok = True
    for label_text, check in GATES_P2:
        passed = check(m)
        ok &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    add("  FASE 2 APROVADA" if ok else "  FASE 2 REPROVADA — ajustar propagação, não o portão")
    add("=" * 62)
    return "\n".join(lines), ok


# ===========================================================================
# FASE 3 — o portão de verdade
# ===========================================================================

def _kurtosis(xs: list[float]) -> float:
    """Curtose de Fisher. > 0 = cauda mais pesada que a normal."""
    n = len(xs)
    if n < 4:
        return 0.0
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    if var <= 1e-12:
        return 0.0
    m4 = sum((x - mean) ** 4 for x in xs) / n
    return m4 / (var * var) - 3.0


def _autocorr(xs: list[float], lag: int) -> float:
    n = len(xs)
    if n <= lag + 2:
        return 0.0
    mean = sum(xs) / n
    num = sum((xs[i] - mean) * (xs[i + lag] - mean) for i in range(n - lag))
    den = sum((x - mean) ** 2 for x in xs)
    return num / den if den > 1e-12 else 0.0


PEAK = 0.70


def collect_phase3(conn: sqlite3.Connection, to_tick: int) -> dict:
    agents = {row["id"]: row for row in conn.execute("SELECT * FROM agent")}
    events = list(conn.execute("SELECT * FROM pressure_event ORDER BY tick"))
    days = max(1, to_tick // clockmod.TICKS_PER_DAY)

    values = [e["value"] for e in events]
    daily_max = [0.0] * days
    for e in events:
        if e["day"] < days:
            daily_max[e["day"]] = max(daily_max[e["day"]], e["value"])

    peaks = [e for e in events if e["value"] >= PEAK]
    peak_days = sorted({e["day"] for e in peaks})
    in_peak = set()
    for e in peaks:
        in_peak |= {e["agent_a"], e["agent_b"]}
        if e["participants_json"]:
            import json as _j
            in_peak |= set(_j.loads(e["participants_json"]))

    # Quem está em coma narrativo: pressão máxima que o agente já atingiu.
    best: dict[str, float] = {a: 0.0 for a in agents}
    for e in events:
        best[e["agent_a"]] = max(best.get(e["agent_a"], 0.0), e["value"])
        best[e["agent_b"]] = max(best.get(e["agent_b"], 0.0), e["value"])

    active = [a for a, r in agents.items() if r["arrival_tick"] < to_tick]

    # Contribuição média de cada componente: mostra se algum termo domina.
    parts = {}
    for key in ("de", "co", "cr", "re", "ta"):
        parts[key] = sum(e[key] for e in events) / len(events) if events else 0.0

    relations = list(conn.execute("SELECT * FROM relation"))

    return {
        "agents": agents, "active": active, "days": days,
        "events": len(events), "values": values,
        "daily_max": daily_max,
        "peaks": len(peaks),
        "peak_day_share": len(peak_days) / days if days else 0.0,
        "cast_in_peak": len(in_peak & set(active)) / max(1, len(active)),
        "kurtosis": _kurtosis(values),
        "autocorr": [(lag, _autocorr(daily_max, lag)) for lag in (1, 2, 3, 5)],
        "best_per_agent": best,
        "parts": parts,
        "mean": sum(values) / len(values) if values else 0.0,
        "tension_mean": (sum(r["tension"] for r in relations) / len(relations)) if relations else 0.0,
        "tension_saturated": [r for r in relations if r["tension"] >= 0.99],
    }


GATES_P3 = [
    ("distribuição com cauda pesada (curtose > 0)", lambda m: m["kurtosis"] > 0.0),
    ("dias com pico entre 2% e 8%", lambda m: 0.02 <= m["peak_day_share"] <= 0.08),
    ("mais de 60% do elenco em algum pico", lambda m: m["cast_in_peak"] > 0.60),
    ("picos correlacionados mas não em cascata", lambda m: any(0.0 < v < 0.6 for _, v in m["autocorr"])),
    ("tensão não satura", lambda m: not m["tension_saturated"]),
]


def _spark(xs: list[float], width: int = 56) -> str:
    if not xs:
        return ""
    blocks = " ▁▂▃▄▅▆▇█"
    step = max(1, len(xs) // width)
    sampled = [max(xs[i:i + step]) for i in range(0, len(xs), step)][:width]
    hi = max(sampled) or 1.0
    return "".join(blocks[min(8, int(v / hi * 8))] for v in sampled)


def render_phase3(m: dict) -> tuple[str, bool]:
    lines: list[str] = []
    add = lines.append
    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA FASE 3 (o portão de verdade)")
    add("=" * 62)
    add(f"  eventos avaliados     {m['events']}")
    add(f"  pressão média         {m['mean']:.3f}")
    add(f"  curtose               {m['kurtosis']:+.2f}   (>0 = cauda pesada)")
    add(f"  picos (>= {PEAK})       {m['peaks']}")
    add(f"  dias com pico         {m['peak_day_share']:.1%}   (alvo 2%-8%)")
    add(f"  elenco em algum pico  {m['cast_in_peak']:.0%}   (alvo > 60%)")
    add("")
    add("  pressão máxima por dia")
    add(f"    {_spark(m['daily_max'])}")
    add("")
    add("  contribuição média por componente")
    rotulos = {"de": "epistêmico", "co": "conflito de objetivo",
               "cr": "carga relacional", "re": "raridade", "ta": "tensão"}
    for key, value in sorted(m["parts"].items(), key=lambda kv: -kv[1]):
        add(f"    {rotulos[key]:<24} {value:.4f}")
    add("")
    add("  autocorrelação dos picos")
    for lag, value in m["autocorr"]:
        add(f"    lag {lag}d  {value:+.3f}")
    add("")
    add("  pressão máxima já atingida por personagem")
    for aid, value in sorted(m["best_per_agent"].items(), key=lambda kv: -kv[1]):
        if aid not in m["active"]:
            continue
        mark = "   <- coma narrativo" if value < 0.30 else ""
        add(f"    {value:.2f}  {m['agents'][aid]['name']}{mark}")
    add("")
    add(f"  tensão média por aresta  {m['tension_mean']:.3f}"
        f"   saturadas: {len(m['tension_saturated'])}")
    add("")
    add("-" * 62)
    ok = True
    for label_text, check in GATES_P3:
        passed = check(m)
        ok &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    if ok:
        add("  FASE 3 APROVADA — o mundo gera estrutura sozinho")
    else:
        add("  FASE 3 REPROVADA — ajustar ontologia e densidade social,")
        add("                     NÃO os pesos do detector")
    add("=" * 62)
    return "\n".join(lines), ok


# ===========================================================================
# FASE 4 — governador de ritmo
# ===========================================================================
# O que se mede aqui não é o mundo: é a *edição* dele. O detector já disse o
# que poderia ser contado; o portão da Fase 4 pergunta se a escolha do que
# será contado tem forma de história — pico raro, elenco circulando, e nada
# escolhido por baixo do próprio piso declarado.


def collect_phase4(conn: sqlite3.Connection, to_tick: int) -> dict:
    import json as _j

    agents = {row["id"]: row for row in conn.execute("SELECT * FROM agent")}
    rows = list(conn.execute("SELECT * FROM scheduled ORDER BY day, id"))
    days = max(1, to_tick // clockmod.TICKS_PER_DAY)
    semanas = max(1, days // 7)

    cenas = [r for r in rows if r["kind"] == "cena"]
    beats = [r for r in rows if r["kind"] == "beat"]

    # Aparições por agente, contadas separadamente: o protagonista acidental
    # nasce das cenas, não dos beats.
    apar_cena: Counter = Counter()
    apar_beat: Counter = Counter()
    for r in rows:
        alvo = apar_cena if r["kind"] == "cena" else apar_beat
        for aid in _j.loads(r["participants_json"]):
            alvo[aid] += 1

    # Descanso: menor intervalo observado entre duas cenas do mesmo agente.
    dias_de_cena: dict[str, list[int]] = {}
    for r in cenas:
        for aid in _j.loads(r["participants_json"]):
            dias_de_cena.setdefault(aid, []).append(r["day"])
    menor_intervalo = min(
        (b - a for lista in dias_de_cena.values()
         for a, b in zip(sorted(lista), sorted(lista)[1:])),
        default=None,
    )

    ativos = [a for a, r in agents.items() if r["arrival_tick"] < to_tick]
    elenco_em_cena = len(set(apar_cena) & set(ativos)) / max(1, len(ativos))
    pico_cena = max(apar_cena.values(), default=0)

    return {
        "agents": agents, "ativos": ativos,
        "dias": days, "semanas": semanas,
        "cenas": cenas, "beats": beats,
        "por_semana_cena": len(cenas) / semanas,
        "por_semana_beat": len(beats) / semanas,
        "menor_pressao_cena": min((r["pressure"] for r in cenas), default=None),
        "menor_pressao_beat": min((r["pressure"] for r in beats), default=None),
        "apar_cena": apar_cena, "apar_beat": apar_beat,
        "menor_intervalo_cena": menor_intervalo,
        "elenco_em_cena": elenco_em_cena,
        "concentracao_cena": pico_cena / max(1, len(cenas)),
        "espera_maxima": max((r["score"] - r["pressure"] for r in rows), default=0.0),
    }


GATES_P4 = [
    # Cena cara é cena rara. Se o orçamento estourar, quem escolheu foi o
    # acaso do laço, não o governador.
    ("orçamento de cena respeitado (<= 2/semana)",
     lambda m: m["por_semana_cena"] <= 2.0),
    ("orçamento de beat respeitado (<= 15/semana)",
     lambda m: m["por_semana_beat"] <= 15.0),
    # O piso é medido contra a pressão crua. Um clímax que só chegou lá pelo
    # bônus de espera não é clímax; é fila.
    ("nenhuma cena abaixo do piso de pressão",
     lambda m: m["menor_pressao_cena"] is None or m["menor_pressao_cena"] >= 0.70),
    ("beats existem (o barato não foi esquecido)", lambda m: len(m["beats"]) > 0),
    # Protagonista acidental: ninguém deve concentrar as cenas.
    ("sem protagonista acidental (< 60% das cenas)",
     lambda m: m["concentracao_cena"] < 0.60),
    ("descanso entre cenas respeitado (>= 6 dias)",
     lambda m: m["menor_intervalo_cena"] is None or m["menor_intervalo_cena"] >= 6),
    ("mais de um terço do elenco em alguma cena",
     lambda m: m["elenco_em_cena"] > 0.33),
]


def render_phase4(m: dict) -> tuple[str, bool]:
    import json as _j

    lines: list[str] = []
    add = lines.append
    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA FASE 4 (ritmo)")
    add("=" * 62)
    add(f"  semanas simuladas     {m['semanas']}")
    add(f"  cenas encenadas       {len(m['cenas'])}   ({m['por_semana_cena']:.2f}/semana)")
    add(f"  beats narrados        {len(m['beats'])}   ({m['por_semana_beat']:.2f}/semana)")
    if m["menor_pressao_cena"] is not None:
        add(f"  menor pressão em cena {m['menor_pressao_cena']:.3f}   (piso 0.70)")
    add(f"  maior bônus de espera {m['espera_maxima']:+.3f}")
    add("")
    add("  cenas agendadas")
    for r in m["cenas"]:
        nomes = ", ".join(sorted(
            m["agents"][a]["name"] for a in _j.loads(r["participants_json"])
            if a in m["agents"]))
        add(f"    dia {r['day']:>4}  pressão {r['pressure']:.3f}  {nomes}")
    add("")
    add("  aparições em cena por personagem")
    if m["apar_cena"]:
        for aid, n in m["apar_cena"].most_common():
            add(f"    {n:>2}x  {m['agents'][aid]['name']}")
    else:
        add("    nenhuma")
    add("")
    add("-" * 62)
    ok = True
    for label_text, check in GATES_P4:
        passed = check(m)
        ok &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    if ok:
        add("  FASE 4 APROVADA — o mundo escolhe o que contar")
    else:
        add("  FASE 4 REPROVADA — ajustar orçamento/descanso, não o piso")
    add("=" * 62)
    return "\n".join(lines), ok


# ===========================================================================
# FASE 8 — o cronista
# ===========================================================================
# O que se mede aqui não é prosa — é se existe história. Um fio precisa de
# começo, de meio e de gente diferente passando por ele; e o texto precisa
# falar de crença, porque um resumo que só conta o que aconteceu joga fora a
# única coisa que este motor tem de próprio.


def collect_phase8(conn: sqlite3.Connection, fios: list, sem_fio: int) -> dict:
    import json as _j

    entradas = [e for f in fios for e in f.entries]
    com_meio = [f for f in fios if any(e["kind"] in ("cena", "beat")
                                       for e in f.entries)]
    elenco: set = set()
    for e in entradas:
        elenco |= set(e["participants"])

    # Toda entrada de meio tem de dizer quantos já sabiam naquele dia: é o
    # que diferencia uma crônica deste mundo de um log de eventos — e tem de
    # ser o número DAQUELE dia, não o de hoje.
    meio = [e for e in entradas if e["kind"] in ("cena", "beat")]
    sem_crenca = [e for e in meio if "sabia" not in e["text"]]

    fora_de_ordem = [f for f in fios
                     if [e["day"] for e in f.entries]
                     != sorted(e["day"] for e in f.entries)]

    agendados = sem_fio + len({(e["tick"], tuple(e["participants"]))
                               for e in meio})
    # Contagem extraída do próprio texto: se a frase disser um número que
    # diminui com o tempo, ela está lendo o estado de hoje, não o de então.
    import re as _re
    anacronismos = []
    for f in fios:
        visto = 0
        for e in f.entries:
            achou = _re.search(r"Nesse dia (\d+) pessoa", e["text"])
            if not achou:
                continue
            n = int(achou.group(1))
            if n < visto:
                anacronismos.append((f.root_fact_id, e["day"], n, visto))
            visto = n

    return {
        "fios": fios, "entradas": entradas,
        "anacronismos": anacronismos,
        "com_meio": com_meio,
        "abertos": [f for f in fios if f.status == "aberto"],
        "resolvidos": [f for f in fios if f.status == "resolvido"],
        "adormecidos": [f for f in fios if f.status == "adormecido"],
        "elenco": elenco,
        "sem_crenca": sem_crenca,
        "fora_de_ordem": fora_de_ordem,
        "sem_fio": sem_fio,
        "cobertura": (agendados - sem_fio) / max(1, agendados),
        "maior": max((len(f.entries) for f in fios), default=0),
    }


GATES_P8 = [
    ("existem fios", lambda m: len(m["fios"]) > 0),
    # Um fato que aparece uma vez e some não é fio: é anotação.
    ("a maioria dos fios tem meio, não só abertura",
     lambda m: len(m["com_meio"]) > len(m["fios"]) / 2),
    # Estados derivados de verdade, não decorativos: os três precisam existir
    # em algum momento, senão a regra que os separa nunca foi exercida.
    ("os fios terminam de alguma forma",
     lambda m: len(m["resolvidos"]) + len(m["adormecidos"]) > 0),
    ("nenhum fio fora de ordem cronológica", lambda m: not m["fora_de_ordem"]),
    ("toda entrada de meio diz quantos sabiam naquele dia",
     lambda m: not m["sem_crenca"]),
    # Anacronismo: um dia não pode ter mais gente sabendo que o dia seguinte.
    ("nenhuma entrada sabe do futuro", lambda m: not m["anacronismos"]),
    ("a maior parte dos momentos vira história (> 50%)",
     lambda m: m["cobertura"] > 0.50),
    ("mais de um terço do elenco aparece na crônica",
     lambda m: len(m["elenco"]) > 4),
]


def render_phase8(m: dict) -> tuple[str, bool]:
    lines: list[str] = []
    add = lines.append
    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA FASE 8 (o cronista)")
    add("=" * 62)
    add(f"  fios                  {len(m['fios'])}")
    add(f"    abertos             {len(m['abertos'])}")
    add(f"    adormecidos         {len(m['adormecidos'])}")
    add(f"    resolvidos          {len(m['resolvidos'])}")
    add(f"  entradas escritas     {len(m['entradas'])}")
    add(f"  maior fio             {m['maior']} entradas")
    add(f"  momentos sem fio      {m['sem_fio']}   (movidos por objetivo)")
    add(f"  cobertura             {m['cobertura']:.0%}")
    add(f"  elenco na crônica     {len(m['elenco'])}")
    add("")
    add("  fios abertos")
    for f in sorted(m["abertos"], key=lambda f: f.opened_day)[:8]:
        add(f"    dia {f.opened_day:>4}  {f.title}")
    add("")
    add("-" * 62)
    ok = True
    for label_text, check in GATES_P8:
        passed = check(m)
        ok &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    if ok:
        add("  FASE 8 APROVADA — o mundo se conta")
    else:
        add("  FASE 8 REPROVADA — ajustar a construção do fio, não o texto")
    add("=" * 62)
    return "\n".join(lines), ok


# ===========================================================================
# FASE 5 — infraestrutura de narração
# ===========================================================================
# O portão desta fase não mede prosa. Mede se o caminho aguenta um modelo que
# erra — porque modelo pequeno erra formato com frequência, e a restrição de
# só usar modelo aberto torna o caminho do erro o caminho normal.


def collect_phase5(conn: sqlite3.Connection) -> dict:
    import json as _j
    from . import narrate

    agendados = [dict(r) for r in conn.execute(
        "SELECT * FROM scheduled ORDER BY day, id LIMIT 12")]
    beats = [narrate.montar(conn, r) for r in agendados]
    resultados = {}

    # 1. Saída boa passa.
    limpo = narrate.StubModel()
    n1 = narrate.Narrator(conn, limpo)
    conn.execute("DELETE FROM narration_cache")
    aceitos = [n1.narrate(b) for b in beats]
    resultados["aceitos"] = sum(1 for r in aceitos if r.origem == "modelo")

    # 2. Cache: repetir os mesmos beats não chama o modelo de novo.
    chamadas_antes = limpo.chamadas
    repetidos = [n1.narrate(b) for b in beats]
    resultados["chamadas_extras"] = limpo.chamadas - chamadas_antes
    resultados["cache_igual"] = all(
        a.texto == b.texto and a.deltas == b.deltas
        for a, b in zip(aceitos, repetidos))

    # 3. Uma saída malformada seguida de uma boa: a re-tentativa salva o beat.
    if beats:
        alvo = beats[0]
        conn.execute("DELETE FROM narration_cache")
        remendo = narrate.StubModel(falhas={alvo.hash(): ["{isso não é json"]})
        r = narrate.Narrator(conn, remendo).narrate(alvo)
        resultados["retentativa"] = (r.origem == "modelo" and r.tentativas == 2)

        # 4. Duas saídas ruins: delta neutro, e o motivo fica registrado.
        conn.execute("DELETE FROM narration_cache")
        ruim = narrate.StubModel(falhas={alvo.hash(): ["{", "também não"]})
        r = narrate.Narrator(conn, ruim).narrate(alvo)
        resultados["neutro"] = (r.origem == "neutro" and not r.deltas
                                and len(r.rejeicoes) == 2)

        # 5. Delta fora dos limites é recusado, não aparado.
        estouro = _j.dumps({"texto": "x", "deltas": [
            {"tipo": "affect", "a": alvo.participants[0],
             "b": alvo.participants[-1], "valor": 0.9}]})
        try:
            narrate.validar(estouro, alvo)
            resultados["limite"] = False
        except narrate.ContratoQuebrado as erro:
            resultados["limite"] = "limite" in str(erro)

        # 6. Delta sobre quem não estava presente é recusado.
        de_fora = [a for a in
                   (r["id"] for r in conn.execute("SELECT id FROM agent"))
                   if a not in alvo.participants]
        if de_fora and len(alvo.participants) >= 1:
            intruso = _j.dumps({"texto": "x", "deltas": [
                {"tipo": "trust", "a": alvo.participants[0],
                 "b": de_fora[0], "valor": 0.01}]})
            try:
                narrate.validar(intruso, alvo)
                resultados["ausente"] = False
            except narrate.ContratoQuebrado:
                resultados["ausente"] = True
        else:
            resultados["ausente"] = True

        # 7. Chave inventada é recusada: campo novo é mecânica nova.
        inventado = _j.dumps({"texto": "x", "deltas": [], "morte": True})
        try:
            narrate.validar(inventado, alvo)
            resultados["campo_extra"] = False
        except narrate.ContratoQuebrado:
            resultados["campo_extra"] = True
    else:
        resultados.update(retentativa=False, neutro=False, limite=False,
                          ausente=False, campo_extra=False)

    # 8. Vazamento: a verdade de um fato oculto não pode estar no pacote de
    #    quem não acredita nela.
    pacotes = {}
    for b in beats:
        pacotes.update(b.pacotes)
    resultados["vazamentos"] = narrate.vazou(pacotes, conn)

    # 9. Replay determinístico: mesmo beat, novo narrador, mesmo hash.
    resultados["hash_estavel"] = all(b.hash() == b.hash() for b in beats) and (
        len({b.hash() for b in beats}) == len(beats))

    conn.execute("DELETE FROM narration_cache")
    conn.commit()
    resultados["beats"] = len(beats)
    return resultados


GATES_P5 = [
    ("saída válida é aceita", lambda m: m["aceitos"] == m["beats"] and m["beats"] > 0),
    ("cache evita a segunda chamada", lambda m: m["chamadas_extras"] == 0),
    ("cache devolve exatamente o mesmo", lambda m: m["cache_igual"]),
    ("uma re-tentativa salva a saída malformada", lambda m: m["retentativa"]),
    ("duas falhas viram delta neutro com motivo", lambda m: m["neutro"]),
    ("delta fora do limite é recusado, não aparado", lambda m: m["limite"]),
    ("delta sobre ausente é recusado", lambda m: m["ausente"]),
    ("campo inventado é recusado", lambda m: m["campo_extra"]),
    ("o pacote não vaza verdade", lambda m: not m["vazamentos"]),
    ("o hash do pedido é estável e distingue beats",
     lambda m: m["hash_estavel"]),
]


def render_phase5(m: dict) -> tuple[str, bool]:
    lines: list[str] = []
    add = lines.append
    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA FASE 5 (contrato, cache, vazamento)")
    add("=" * 62)
    add(f"  beats montados        {m['beats']}")
    add(f"  aceitos de primeira   {m['aceitos']}")
    add(f"  chamadas extras       {m['chamadas_extras']}   (cache: alvo 0)")
    add(f"  vazamentos            {len(m['vazamentos'])}")
    for agente, fid, valor in m["vazamentos"][:5]:
        add(f"    {agente} recebeu a verdade do fato {fid}: {valor}")
    add("")
    add("  Nenhum modelo pago participa disto. O stub determinístico não imita")
    add("  prosa — imita o CONTRATO — e é contra ele que os portões rodam.")
    add("")
    add("-" * 62)
    ok = True
    for label_text, check in GATES_P5:
        passed = check(m)
        ok &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    if ok:
        add("  FASE 5 APROVADA — a infraestrutura aguenta um modelo que erra")
    else:
        add("  FASE 5 REPROVADA — consertar o contrato, nunca afrouxá-lo")
    add("=" * 62)
    return "\n".join(lines), ok


# ===========================================================================
# FASE 7 — deriva de identidade
# ===========================================================================


def collect_phase7(conn: sqlite3.Connection, to_tick: int) -> dict:
    from . import identity

    identity.gravar(conn)
    agents = {r["id"]: dict(r) for r in conn.execute("SELECT * FROM agent")}
    ativos = {a: r for a, r in agents.items() if r["arrival_tick"] < to_tick}

    # A âncora é escrita uma vez só, então numa base nova o teste de
    # constituição passaria por construção — instrumento que não pode falhar
    # não mede nada. Aqui ele é exercitado de verdade: reescreve-se uma
    # constituição, confere-se que o portão acusa, e desfaz-se.
    vitima = next(iter(ativos), None)
    pega_reescrita = False
    if vitima is not None:
        original = agents[vitima]["constitution_json"]
        conn.execute("UPDATE agent SET constitution_json = ? WHERE id = ?",
                     (original + " (reescrito)", vitima))
        pega_reescrita = vitima in identity.constituicoes_intactas(conn)
        conn.execute("UPDATE agent SET constitution_json = ? WHERE id = ?",
                     (original, vitima))
        conn.commit()

    derivas = {a: identity.deriva(conn, a, r["arrival_tick"])
               for a, r in ativos.items()}
    parados = [a for a, d in derivas.items() if d["passos"] == 0]
    sem_causa = sum(d["sem_causa"] for d in derivas.values())

    deslocados = [a for a, r in ativos.items() if r["origin"] != "nativo"]
    nativos = [a for a, r in ativos.items() if r["origin"] == "nativo"]

    def media(quem, campo):
        vals = [derivas[a][campo] for a in quem]
        return sum(vals) / len(vals) if vals else 0.0

    return {
        "agents": agents, "ativos": ativos, "derivas": derivas,
        "parados": parados,
        "sem_causa": sem_causa,
        "constituicoes_quebradas": identity.constituicoes_intactas(conn),
        "pega_reescrita": pega_reescrita,
        "deslocados": deslocados, "nativos": nativos,
        "media_deslocado": media(deslocados, "conceitos"),
        "media_nativo": media(nativos, "conceitos"),
        "ensinados": sum(d["aprendeu_com_alguem"] for d in derivas.values()),
        "total_passos": sum(d["passos"] for d in derivas.values()),
    }


GATES_P7 = [
    ("nenhuma constituição foi reescrita",
     lambda m: not m["constituicoes_quebradas"]),
    # O portão acima só vale se puder reprovar. Este confere que ele reprova.
    ("o teste de constituição detecta uma reescrita",
     lambda m: m["pega_reescrita"]),
    ("toda mudança cita a causa", lambda m: m["sem_causa"] == 0),
    # Um mundo onde ninguém deriva é um mundo em exibição, não vivo.
    ("todo mundo derivou alguma coisa", lambda m: not m["parados"]),
    # A previsão falsificável desta fase: quem chegou de outra obra tem mais o
    # que aprender do que quem sempre morou aqui. Se não for verdade, a camada
    # de conhecimento não está fazendo o que diz fazer.
    ("deslocado aprende mais que nativo",
     lambda m: not m["deslocados"] or not m["nativos"]
     or m["media_deslocado"] > m["media_nativo"]),
    # Só se aplica quando há quem ensinar. Ensinar existe para socorrer quem
    # chegou sem entender nada; na vila da base todos já sabem como o mundo
    # funciona, e cobrar aula ali reprovaria um mundo por não ter o problema
    # que a aula resolve — o mesmo erro que a P27 registrou.
    ("alguém aprendeu com outra pessoa (se há quem ensinar)",
     lambda m: not m["deslocados"] or m["ensinados"] > 0),
]


def render_phase7(m: dict) -> tuple[str, bool]:
    lines: list[str] = []
    add = lines.append
    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA FASE 7 (deriva de identidade)")
    add("=" * 62)
    add(f"  passos registrados    {m['total_passos']}")
    add(f"  sem causa citada      {m['sem_causa']}   (alvo 0)")
    add(f"  constituições intactas {len(m['ativos']) - len(m['constituicoes_quebradas'])}"
        f"/{len(m['ativos'])}")
    add(f"  conceitos aprendidos por deslocado  {m['media_deslocado']:.1f}")
    add(f"  conceitos aprendidos por nativo     {m['media_nativo']:.1f}")
    add("")
    add("  quanto cada um se afastou de quem chegou")
    for aid, d in sorted(m["derivas"].items(), key=lambda kv: -kv[1]["passos"])[:14]:
        origem = m["agents"][aid]["origin"]
        marca = "" if d["passos"] else "   <- parado"
        add(f"    {d['passos']:>3} passos  {m['agents'][aid]['name']:<22}"
            f" {origem}{marca}")
    add("")
    add("-" * 62)
    ok = True
    for label_text, check in GATES_P7:
        passed = check(m)
        ok &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    if ok:
        add("  FASE 7 APROVADA — a trajetória muda, a constituição não")
    else:
        add("  FASE 7 REPROVADA — ajustar o que causa a mudança, não o registro")
    add("=" * 62)
    return "\n".join(lines), ok


# ===========================================================================
# FASE 6 — cenas encenadas
# ===========================================================================


def collect_phase6(conn: sqlite3.Connection) -> dict:
    from . import narrate, staging

    cenas = [dict(r) for r in conn.execute(
        "SELECT * FROM scheduled WHERE kind = 'cena' ORDER BY day")]
    if not cenas:
        cenas = [dict(r) for r in conn.execute(
            "SELECT * FROM scheduled ORDER BY day LIMIT 3")]
    beats = [narrate.montar(conn, r) for r in cenas]

    conn.execute("DELETE FROM narration_cache")
    modelo = narrate.StubModel()
    narrador = narrate.Narrator(conn, modelo)

    encenadas = [staging.encenar(narrador, b) for b in beats]
    vazamentos = []
    for b, e in zip(beats, encenadas):
        vazamentos += staging.vazamento_entre_atores(b, e["prompts"])

    # O portão acima só vale se puder reprovar: planta-se a cabeça do vizinho
    # no prompt de alguém e confere-se que o detector acusa.
    pega_plantado = True
    if beats and len(beats[0].participants) >= 2:
        b = beats[0]
        a1, a2 = sorted(b.participants)[:2]
        envenenado = _j_loads(staging.turno_prompt(b, a1, []))
        envenenado["sua_cabeca"] = b.pacotes[a2]
        pega_plantado = bool(staging.vazamento_entre_atores(
            b, {a1: [__import__("json").dumps(envenenado)]}))

    # Um turno nunca pode receber mais de uma cabeça.
    cabecas_por_turno = set()
    for e in encenadas:
        for lista in e["prompts"].values():
            for p in lista:
                cabecas_por_turno.add(
                    len(_j_loads(p)["sua_cabeca"].get("crencas", [])) >= 0)

    turnos = [e["turnos"] for e in encenadas]
    conn.execute("DELETE FROM narration_cache")
    conn.commit()
    return {
        "cenas": len(beats),
        "turnos": turnos,
        "max_turnos": max(turnos, default=0),
        "vazamentos": vazamentos,
        "pega_plantado": pega_plantado,
        "ordem_estavel": all(
            staging.ordem(b) == staging.ordem(b) for b in beats),
        "um_por_prompt": all(
            "sua_cabeca" in _j_loads(p) and "cabecas" not in _j_loads(p)
            for e in encenadas for lista in e["prompts"].values() for p in lista),
        "elenco": [sorted(b.participants) for b in beats],
    }


def _j_loads(s):
    import json as _j
    return _j.loads(s)


GATES_P6 = [
    ("existem cenas para encenar", lambda m: m["cenas"] > 0),
    ("o teto de turnos é respeitado",
     lambda m: m["max_turnos"] <= 6),
    ("todo turno recebe uma cabeça só", lambda m: m["um_por_prompt"]),
    # O bug mais provável desta fase, e o motivo de ela existir em código
    # separado em vez de um prompt maior.
    ("nenhum ator recebe a cabeça de outro", lambda m: not m["vazamentos"]),
    ("o teste de vazamento detecta um plantado", lambda m: m["pega_plantado"]),
    ("a ordem dos turnos é determinística", lambda m: m["ordem_estavel"]),
]


def render_phase6(m: dict) -> tuple[str, bool]:
    lines: list[str] = []
    add = lines.append
    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA FASE 6 (cenas, e o vazamento)")
    add("=" * 62)
    add(f"  cenas encenadas       {m['cenas']}")
    add(f"  turnos por cena       {m['turnos']}   (teto 6)")
    add(f"  vazamentos entre atores {len(m['vazamentos'])}")
    for ator, o_que in m["vazamentos"][:5]:
        add(f"    {ator} recebeu: {o_que}")
    add("")
    add("  Um turno = um ator = o pacote dele. O que os outros disseram em voz")
    add("  alta atravessa; o que os outros PENSAM, nunca.")
    add("")
    add("-" * 62)
    ok = True
    for label_text, check in GATES_P6:
        passed = check(m)
        ok &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    if ok:
        add("  FASE 6 APROVADA — cada ator só sabe o que é dele")
    else:
        add("  FASE 6 REPROVADA — separar os pacotes, não filtrar a saída")
    add("=" * 62)
    return "\n".join(lines), ok


# ===========================================================================
# FASE 9 — a obra vira gente (só a prova de que funciona)
# ===========================================================================
# ESTE PORTÃO NÃO COLOCA NINGUÉM NO MUNDO PUBLICADO. A versão estável do
# Kestlerium é a vila com NPCs e mais nada: os personagens do autor entram
# quando ele decidir, um a um. O que se mede aqui é só se um personagem
# FUNCIONARIA — porque descobrir que não funciona depois de colocá-lo no mundo
# em produção seria descobrir tarde.
#
# A prova roda num banco descartável, com um personagem de teste que não
# pertence a obra nenhuma.

FIXTURE = '''---
title: "Obra de Teste"
kestlerium:
  - id: forasteiro
    nome: "O Forasteiro"
    constituicao: "Chegou sem entender nada. Aprende olhando."
    casa: pensao
    trabalho: bar
    traz: [juramento, linhagem]
  - id: coisa
    nome: "A Coisa"
    tipo: entidade
    constituicao: "Não tem corpo."
---

# Corpo da obra

Este texto NUNCA deve ser lido pelo motor. Se um personagem soubesse o que
está escrito aqui, saberia a própria obra — e isso é do autor, não dele.
'''


def collect_phase9(mundo_base: str = "vila", dias: int = 30,
                   seed: int = 20260729) -> dict:
    import pathlib as _p

    from . import arrival, db as dbmod, world as worldmod
    from .sim import Simulation

    out = _p.Path(__file__).resolve().parent.parent / "out"
    conn = dbmod.connect(out / "chegada_teste.db", fresh=True)
    w = worldmod.load(conn, mundo_base)
    locais = {r["id"] for r in conn.execute("SELECT id FROM location")}

    # 1. O front matter é lido, e só ele.
    fm = arrival.front_matter(FIXTURE)
    declaradas = [dict(d, _obra=fm["title"], _arquivo="fixture.md")
                  for d in fm.get("kestlerium", [])]
    leu_corpo = any("NUNCA" in json.dumps(d, ensure_ascii=False)
                    for d in declaradas)

    aceitos, recusas = [], []
    for d in declaradas:
        try:
            aceitos.append(arrival.validar(d, locais))
        except arrival.DeclaracaoInvalida as erro:
            recusas.append(str(erro))

    # 2. O personagem chega no dia 3 — depois do mundo já estar andando.
    chegada_tick = 3 * clockmod.TICKS_PER_DAY
    entrou = False
    for d in aceitos:
        entrou |= arrival.chegar(conn, d, chegada_tick, "pensao", "bar")

    # 3. O mundo roda com ele dentro.
    w = worldmod.load(conn, mundo_base)
    sim = Simulation(conn, w, seed=seed, world_name=mundo_base)
    sim.run(0, dias * clockmod.TICKS_PER_DAY, mode="rapido")

    novo = "forasteiro"
    antes = conn.execute(
        "SELECT count(*) c FROM agent_state WHERE agent_id = ? AND tick < ?",
        (novo, chegada_tick)).fetchone()["c"]
    depois = conn.execute(
        "SELECT count(*) c FROM agent_state WHERE agent_id = ? AND tick >= ?",
        (novo, chegada_tick)).fetchone()["c"]

    conheceu = {r["agent_a"] if r["agent_b"] == novo else r["agent_b"]
                for r in conn.execute(
                    "SELECT agent_a, agent_b FROM encounter"
                    " WHERE agent_a = ? OR agent_b = ?", (novo, novo))}

    trouxe = {r["concept"] for r in conn.execute(
        "SELECT concept FROM knowledge WHERE agent_id = ? AND taught_by IS NULL",
        (novo,))}
    aprendeu = [dict(r) for r in conn.execute(
        "SELECT concept, grasp, taught_by FROM knowledge"
        " WHERE agent_id = ? AND taught_by IS NOT NULL", (novo,))]

    # 4. Ao chegar ele NÃO pode saber o que é daqui. Um deslocado que já
    #    entende dinheiro e ônibus não é um deslocado.
    do_mundo = set(sim.knowing.world_concepts)
    sabia_de_ante_mao = trouxe & do_mundo

    locais_visitados = {r["location_id"] for r in conn.execute(
        "SELECT DISTINCT location_id FROM agent_state WHERE agent_id = ?"
        " AND location_id IS NOT NULL", (novo,))}

    residentes = conn.execute(
        "SELECT count(*) c FROM agent WHERE origin = 'nativo'").fetchone()["c"]
    conn.close()

    return {
        "declaradas": declaradas, "aceitos": aceitos, "recusas": recusas,
        "leu_corpo": leu_corpo, "entrou": entrou,
        "estados_antes": antes, "estados_depois": depois,
        "conheceu": conheceu, "trouxe": trouxe, "aprendeu": aprendeu,
        "sabia_de_ante_mao": sabia_de_ante_mao,
        "locais": locais_visitados, "residentes": residentes, "dias": dias,
    }


GATES_P9 = [
    ("a declaração da obra é lida", lambda m: len(m["declaradas"]) == 2),
    # A regra do autor, virada portão: o motor lê o bloco, nunca o texto.
    ("o corpo da obra não é lido", lambda m: not m["leu_corpo"]),
    ("entidade é recusada com explicação",
     lambda m: len(m["recusas"]) == 1 and "manifestam" in m["recusas"][0]),
    ("o personagem entra no mundo", lambda m: m["entrou"]),
    # Chegada contínua: antes do tick dele, ele não existe.
    ("não existe antes de chegar", lambda m: m["estados_antes"] == 0),
    ("existe e se move depois de chegar",
     lambda m: m["estados_depois"] > 0 and len(m["locais"]) >= 2),
    ("conhece parte dos moradores",
     lambda m: len(m["conheceu"]) >= max(2, m["residentes"] // 3)),
    ("chega sem entender este mundo", lambda m: not m["sabia_de_ante_mao"]),
    # E o motivo de os NPCs existirem: alguém tem de ensiná-lo.
    ("aprende com quem já morava aqui", lambda m: len(m["aprendeu"]) >= 3),
]


def render_phase9(m: dict) -> tuple[str, bool]:
    lines: list[str] = []
    add = lines.append
    add("=" * 62)
    add("KESTLERIUM — VALIDAÇÃO DA CHEGADA (um personagem funciona?)")
    add("=" * 62)
    add("  Este teste NÃO coloca ninguém no mundo publicado. A versão estável")
    add("  do Kestlerium é a vila com NPCs e mais nada. Aqui só se verifica")
    add("  que um personagem funcionaria quando o autor decidir mandar um.")
    add("")
    add(f"  declarações lidas     {len(m['declaradas'])}")
    add(f"  aceitas               {len(m['aceitos'])}")
    for r in m["recusas"]:
        add(f"    recusada: {r}")
    add("")
    add(f"  dias simulados        {m['dias']}   (chegou no dia 3)")
    add(f"  estados antes         {m['estados_antes']}   (alvo 0)")
    add(f"  estados depois        {m['estados_depois']}")
    add(f"  locais que frequentou {len(m['locais'])}")
    add(f"  moradores que conheceu {len(m['conheceu'])} de {m['residentes']}")
    add(f"  trouxe de casa        {', '.join(sorted(m['trouxe'])) or '—'}")
    add("")
    add("  o que aprendeu aqui, e com quem")
    for k in sorted(m["aprendeu"], key=lambda k: -k["grasp"])[:10]:
        add(f"    {k['concept']:<16} domínio {k['grasp']:.2f}"
            f"   com {k['taught_by']}")
    if not m["aprendeu"]:
        add("    nada")
    add("")
    add("-" * 62)
    ok = True
    for label_text, check in GATES_P9:
        passed = check(m)
        ok &= passed
        add(f"  [{'ok' if passed else 'FALHOU'}] {label_text}")
    add("-" * 62)
    if ok:
        add("  CHEGADA APROVADA — um personagem viveria aqui")
        add("  (e continua fora do mundo publicado, de propósito)")
    else:
        add("  CHEGADA REPROVADA — consertar antes de mandar alguém de verdade")
    add("=" * 62)
    return "\n".join(lines), ok
