"""Os portões de validação — Fases 1, 2 e 3.

O produto destas fases não é a simulação: é a medição dela. Um mundo onde todos
se encontram todo dia faz o drama virar ruído; um segredo que nunca se move não
é segredo; uma distribuição de pressão sem cauda pesada é um mundo onde nada
importa. Cada portão existe para detectar uma dessas falhas, e a regra é sempre
a mesma — quando um reprova, conserta-se o modelo, nunca o número do portão.
"""

from __future__ import annotations

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
