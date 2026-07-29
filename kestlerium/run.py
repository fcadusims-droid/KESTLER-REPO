#!/usr/bin/env python3
"""Kestlerium — ponto de entrada.

    python run.py validar            # 90 dias em segundos, banco descartável
    python run.py avancar            # avança o mundo real até agora (Brasília)
    python run.py agora              # onde está cada um neste instante

O modo real nunca usa o banco de validação e vice-versa.
"""

from __future__ import annotations

import argparse
import pathlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from engine import clock as clockmod
from engine import db, goals as goalmod, report, world
from engine.sim import Simulation

OUT = Path(__file__).resolve().parent / "out"
REAL_DB = OUT / "kestlerium.db"
TEST_DB = OUT / "validacao.db"


def _bind_epoch(conn) -> int:
    """Lê a época gravada, ou cria o mundo agora. Devolve o último tick simulado.

    A época viver no banco é o que mantém a numeração dos ticks estável entre
    execuções — e portanto as datas de chegada dos personagens.
    """
    from datetime import datetime
    row = conn.execute("SELECT epoch_iso, last_tick FROM world_clock WHERE id = 1").fetchone()
    if row:
        clockmod.set_epoch(datetime.fromisoformat(row["epoch_iso"]))
        return row["last_tick"]
    epoch = clockmod.default_epoch()
    clockmod.set_epoch(epoch)
    conn.execute(
        "INSERT INTO world_clock (id, epoch_iso, last_tick, mode) VALUES (1, ?, 0, 'real')",
        (epoch.isoformat(),),
    )
    conn.commit()
    print(f"Kestlerium nasce em {epoch.strftime('%d/%m/%Y %H:%M')} (horário de Brasília).")
    return 0


def cmd_validar(args: argparse.Namespace) -> int:
    """Modo rápido: queima os erros de design antes do mundo viver de verdade."""
    conn = db.connect(OUT / f"validacao_{args.mundo}.db", fresh=True)
    w = world.load(conn, args.mundo)
    total_ticks = args.dias * clockmod.TICKS_PER_DAY

    sim = Simulation(conn, w, seed=args.seed, world_name=args.mundo)
    from engine.pressure import PressureDetector

    # Os fatos entram no mundo no tick deles — plantar tudo de véspera faria
    # todas as saliências decaírem juntas e a fofoca morrer no meio da run.
    # Os objetivos são reconstruídos quando fatos novos aparecem.
    def rebuild_goals():
        goal_list = goalmod.instantiate(conn, w.agents, sim.ledger.facts, sim.ledger)
        if sim.detector is None:
            sim.detector = PressureDetector(sim.ledger, goal_list, clockmod.TICKS_PER_DAY)
        else:
            sim.detector.rebuild(goal_list)

    sim.on_new_facts = rebuild_goals
    rebuild_goals()

    result = sim.run(0, total_ticks, mode="rapido")

    metrics = report.collect(conn, 0, total_ticks)
    text, passed = report.render(metrics, result["wall_seconds"])
    print(text)

    import json as _json
    spec = _json.loads(
        (pathlib.Path(__file__).resolve().parent / "data" / args.mundo /
         "seed_facts.json").read_text(encoding="utf-8"))
    gates = spec.get("gates", ["1", "2", "3"])

    passed2 = passed3 = True
    if "2" in gates:
        m2 = report.collect_phase2(conn, total_ticks, args.mundo)
        text2, passed2 = report.render_phase2(m2)
        print(); print(text2)
        (OUT / f"fase2_{args.mundo}.txt").write_text(text2, encoding="utf-8")
    else:
        print()
        print(f"  Fases 2 e 3 nao se aplicam a '{args.mundo}':")
        print(f"  {spec.get('_gates_nota','')}")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"fase1_{args.mundo}.txt").write_text(text, encoding="utf-8")
    if "3" in gates:
        m3 = report.collect_phase3(conn, total_ticks)
        text3, passed3 = report.render_phase3(m3)
        print(); print(text3)
        (OUT / f"fase3_{args.mundo}.txt").write_text(text3, encoding="utf-8")
    passed = passed and passed2 and passed3
    conn.close()
    return 0 if passed else 1


def cmd_avancar(args: argparse.Namespace) -> int:
    """Modo real: leva o mundo até o instante atual de Brasília."""
    conn = db.connect(OUT / f"mundo_{args.mundo}.db")
    w = world.load(conn, args.mundo)
    from_tick = _bind_epoch(conn)
    to_tick = clockmod.RealClock().current_tick()

    if to_tick <= from_tick:
        print(f"Kestlerium já está em {clockmod.label(from_tick)}. Nada a avançar.")
        conn.close()
        return 0

    behind = to_tick - from_tick
    print(f"Kestlerium: {clockmod.label(from_tick)} → {clockmod.label(to_tick)}")
    print(f"Recuperando {behind} tick(s) = {behind * clockmod.TICK_MINUTES / 60:.1f}h de mundo.")

    sim = Simulation(conn, w, seed=args.seed, world_name=args.mundo)
    result = sim.run(from_tick, to_tick, mode="real")
    print(f"Feito em {result['wall_seconds']:.2f}s.")
    conn.close()
    return 0


def cmd_agora(args: argparse.Namespace) -> int:
    """Fotografia do instante: quem está onde, agora."""
    conn = db.connect(OUT / f"mundo_{args.mundo}.db")
    last = _bind_epoch(conn)
    tick = clockmod.RealClock().current_tick()
    if last <= 0:
        print("O mundo ainda não foi iniciado. Rode: python run.py avancar")
        conn.close()
        return 1

    shown = min(tick, last - 1)
    noite = "noite" if clockmod.is_night(shown) else "dia"
    print(f"KESTLERIUM — {clockmod.label(shown)} ({noite}, horário de Brasília)")
    print("-" * 58)

    rows = conn.execute(
        "SELECT s.agent_id, a.name, s.location_id, s.activity"
        " FROM agent_state s JOIN agent a ON a.id = s.agent_id"
        " WHERE s.tick = ? ORDER BY s.location_id IS NULL, s.location_id, a.name",
        (shown,),
    ).fetchall()

    if not rows:
        print("  (sem estado gravado para este tick)")
    for r in rows:
        place = r["location_id"] or "—"
        print(f"  {r['name']:<24} {place:<16} {r['activity']}")
    conn.close()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="kestlerium")
    sub = parser.add_subparsers(dest="cmd", required=True)

    def add_common(sp):
        sp.add_argument("--seed", type=int, default=20260729)
        sp.add_argument("--mundo", default="distrito",
                        help="distrito (bancada) ou vila (produção)")
        return sp

    p = add_common(sub.add_parser("validar", help="roda N dias rápido e mede a Fase 1"))
    p.add_argument("--dias", type=int, default=90)
    p.set_defaults(func=cmd_validar)

    p = add_common(sub.add_parser("avancar", help="avança o mundo real até agora"))
    p.set_defaults(func=cmd_avancar)

    p = add_common(sub.add_parser("agora", help="mostra o estado do instante atual"))
    p.set_defaults(func=cmd_agora)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
