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
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from engine import clock as clockmod
from engine import db, goals as goalmod, report, viewer, world
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


def cmd_publicar(args: argparse.Namespace) -> int:
    """Avança o mundo até agora e escreve a janela do terrário.

    A página é estática e o snapshot é pequeno: o agendador roda isto a cada
    30 min — a duração de um tick — então o que se publica é sempre o tick
    corrente. Quem abre a página vê o agora sem iniciar nada.
    """
    conn = db.connect(OUT / f"mundo_{args.mundo}.db")
    w = world.load(conn, args.mundo)
    from_tick = _bind_epoch(conn)
    to_tick = clockmod.RealClock().current_tick()

    if to_tick > from_tick:
        sim = Simulation(conn, w, seed=args.seed, world_name=args.mundo)
        sim.run(from_tick, to_tick, mode="real")
        print(f"Avancou {to_tick - from_tick} tick(s) ate {clockmod.label(to_tick)}.")
    else:
        print(f"Ja estava em {clockmod.label(from_tick)}.")

    tick = max(0, min(to_tick, from_tick if to_tick <= from_tick else to_tick) - 1)
    snap = viewer.snapshot(conn, tick, args.mundo)

    destino = Path(args.saida) if args.saida else (
        Path(__file__).resolve().parent.parent / "public" / "kestlerium")
    destino.mkdir(parents=True, exist_ok=True)
    (destino / "index.html").write_text(viewer.render(snap), encoding="utf-8")
    (destino / "snapshot.json").write_text(
        json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")

    _podar(conn, tick)
    conn.close()
    print(f"Publicado em {destino}/index.html ({snap['quando']}).")
    return 0


def _podar(conn, tick: int, dias_rastro: int = 3) -> None:
    """Versiona-se o ESTADO do mundo, não o histórico dele.

    Medido em 90 dias de vila: o banco completo passa de 5,8 MB, dos quais
    43.200 linhas são `agent_state` — rastro de posição a cada meia hora, que
    não serve para nada depois de passar. Fatos, crenças, relações e
    conhecimento, que são o mundo de verdade, somam 132 KB e **não crescem**.

    Como o agendador commita a cada 30 minutos, um banco que cresce sem limite
    inviabilizaria o repositório em semanas. Então guarda-se o estado inteiro,
    o instante corrente (que o snapshot precisa) e alguns dias de rastro para
    diagnóstico. O resto é reproduzível pela seed.
    """
    conn.execute("DELETE FROM agent_state WHERE tick < ?", (tick,))
    corte = tick - dias_rastro * clockmod.TICKS_PER_DAY
    if corte > 0:
        conn.execute("DELETE FROM encounter WHERE tick < ?", (corte,))
        conn.execute("DELETE FROM pressure_event WHERE tick < ?", (corte,))
    conn.execute("DELETE FROM run WHERE id NOT IN"
                 " (SELECT id FROM run ORDER BY id DESC LIMIT 50)")
    conn.commit()
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.execute("VACUUM")


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

    p = add_common(sub.add_parser("publicar", help="avança e escreve a janela do terrário"))
    p.add_argument("--saida", default=None)
    p.set_defaults(func=cmd_publicar)

    p = add_common(sub.add_parser("agora", help="mostra o estado do instante atual"))
    p.set_defaults(func=cmd_agora)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
