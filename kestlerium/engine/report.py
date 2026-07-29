"""Validação da Fase 1.

O produto desta fase não é a simulação — é a medição dela. O plano é explícito:
se todo mundo encontra todo mundo todo dia, as rotinas estão frouxas e o drama
das fases seguintes vira ruído. Estes números decidem se a Fase 2 pode começar.
"""

from __future__ import annotations

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
