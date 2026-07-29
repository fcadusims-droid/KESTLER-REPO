"""O laço de tempo do Kestlerium.

Um tick de 30 minutos: cada agente decide onde estar e o que fazer, os que se
cruzam formam encontros, e sobre os encontros se apoiam as camadas seguintes —
crença e fofoca (`ledger`), conhecimento e ensino (`knowing`), pressão
(`pressure`). Este módulo é a espinha; as camadas são chamadas daqui.

Determinismo: um único `random.Random(seed)`, injetado. O módulo `random`
global nunca é usado — se fosse, duas execuções com a mesma seed divergiriam e
a reprodutibilidade morreria junto.
"""

from __future__ import annotations

import json
import pathlib
import sqlite3
import time
from dataclasses import dataclass, field
from datetime import datetime
from random import Random

from . import clock as clockmod
from .knowing import Knowledge
from .ledger import Ledger
from .pressure import PressureDetector
from .world import Agent, World

TICKS_PER_DAY = clockmod.TICKS_PER_DAY

# --- necessidades -----------------------------------------------------------
# Semântica de pressão: 0 = saciado, 1 = crítico. Sobem sozinhas, caem ao serem
# atendidas. Servem para desviar o agente da rotina — é daí que vem boa parte
# da variedade de encontro.
HUNGER_RATE = 1.0 / 30      # fome plena em ~15h sem comer
SLEEP_RATE = 1.0 / 34       # sono pleno em ~17h acordado
ENERGY_RATE = 1.0 / 40

HUNGER_CRITICAL = 0.78
SLEEP_CRITICAL = 0.86

DEVIATION_P = 0.055         # chance por tick de sair da rotina sem motivo
NETWORK_USE_P = 0.012       # chance por tick de a entidade RESOLVER um rastro
                            # (não é "usou o celular": é detecção significativa.
                            #  Se fosse frequente, Suomynona exporia o elenco
                            #  inteiro na semana 1 e não sobraria segredo nenhum.)
# Contato por tick entre um par específico no mesmo local = CONTACT_K / capacidade.
# Café pequeno: provável. Metrô de 40 lugares: raro. Moradia tem regra própria:
# lá o padrão não é a sala, é a unidade privada.
CONTACT_K = 2.0
PRIVATE_CONTACT_P = 0.012   # cruzar com vizinho em área comum do prédio

@dataclass
class Runtime:
    """Estado vivo de um agente durante a simulação."""
    agent: Agent
    location: str | None = None
    activity: str = "ausente"
    travel_until: int = -1
    destination: str | None = None
    needs: dict[str, float] = field(
        default_factory=lambda: {"fome": 0.15, "sono": 0.15, "energia": 0.15}
    )

    @property
    def traveling(self) -> bool:
        return self.destination is not None


class Simulation:
    def __init__(
        self,
        conn: sqlite3.Connection,
        world: World,
        seed: int = 20260729,
        record_states: bool = True,
        world_name: str = "distrito",
    ) -> None:
        self.conn = conn
        self.world = world
        self.rng = Random(seed)
        self.seed = seed
        self.record_states = record_states
        self.connected = world.connected_locations()
        self.private = world.private_locations()
        self.food = world.food_locations()
        self.contact_p = {
            lid: (PRIVATE_CONTACT_P if lid in self.private
                  else min(1.0, CONTACT_K / max(1, row['capacity'])))
            for lid, row in world.locations.items()
        }

        self.runtime: dict[str, Runtime] = {
            agent_id: Runtime(agent=agent) for agent_id, agent in world.agents.items()
        }
        # co-presença do tick anterior, para emitir encontro só na transição
        self._previous_pairs: set[tuple[str, str]] = set()
        # pares já em contato, para o encontro não piscar a cada tick
        self._contact_active: set[tuple[str, str]] = set()

        self._state_buffer: list[tuple] = []
        self._encounter_buffer: list[tuple] = []

        self.ledger = Ledger(conn, self.rng, world.agents)
        self.knowing = Knowledge(conn, self.rng, world.agents)
        self.ledger.knowing = self.knowing   # compreender_mundo lê daqui
        self._endowed: set[str] = set()
        self.world_name = world_name
        self._pending_seeds = self._load_seed_facts()
        self.detector: PressureDetector | None = None
        # Objetivos nascem com os fatos: ninguém tem o objetivo de ocultar
        # antes de existir algo a ocultar.
        self.on_new_facts = None

    def _load_seed_facts(self) -> dict[int, list[dict]]:
        """Fatos plantados, indexados pelo tick em que entram no mundo."""
        path = (pathlib.Path(__file__).resolve().parent.parent / "data"
                / self.world_name / "seed_facts.json")
        if not path.exists():
            return {}
        doc = json.loads(path.read_text(encoding="utf-8"))
        by_tick: dict[int, list[dict]] = {}
        for spec in doc.get("facts", []):
            by_tick.setdefault(spec["day"] * TICKS_PER_DAY, []).append(spec)
        return by_tick

    def _plant_facts(self, tick: int) -> None:
        planted = self._pending_seeds.pop(tick, [])
        for spec in planted:
            fact_id = self.ledger.add_fact(
                tick, spec["subject"], spec["predicate"], spec.get("object"),
                spec["visibility"], spec["witnesses"],
            )
            for witness in spec["witnesses"]:
                # Só testemunha quem já chegou ao Kestlerium.
                agent = self.world.agents.get(witness)
                if agent is not None and tick >= agent.arrival_tick:
                    self.ledger.witness(witness, fact_id, tick)
        if planted and self.on_new_facts is not None:
            self.on_new_facts()

    # -- movimento ----------------------------------------------------------

    def _target_for(self, rt: Runtime, tick: int) -> tuple[str, str]:
        """Para onde o agente quer ir neste tick, e fazendo o quê.

        Conhecimento entra aqui: quem não sabe o que é emprego não vai
        trabalhar, quem não sabe o que é dinheiro não compra, e quem não sabe
        o que é transporte não sai da vizinhança. O recém-chegado fica perto de
        onde chegou até alguém explicar — que é exatamente a experiência de
        aterrissar num lugar sem entender nada.
        """
        agent = rt.agent
        home = agent.home

        # 1. Necessidade crítica sobrescreve a rotina.
        if rt.needs["sono"] >= SLEEP_CRITICAL and home:
            return home, "dormir"
        if rt.needs["fome"] >= HUNGER_CRITICAL:
            current = rt.location or home
            # Vai ao mais perto — e entre os igualmente perto, sorteia.
            #
            # Sem o sorteio, o desempate caía na ordem da lista, e trocar
            # ("mercado","cafe") por ("cafe","mercado") bastava para reprovar as
            # Fases 2 e 3. Resultado que depende de ordenação alfabética é
            # acidente de implementação, não propriedade do mundo. O sorteio
            # também é mais verdadeiro: ninguém almoça no mesmo lugar sempre.
            distances = {
                lid: self.world.travel_ticks(current or lid, lid) for lid in self.food
            }
            nearest = min(distances.values())
            tied = sorted(lid for lid, d in distances.items() if d == nearest)
            return self.rng.choice(tied), "comer"

        # 2. Rotina da hora do dia.
        tod = clockmod.time_of_day(tick)
        planned = agent.schedule.get(tod)

        # 3. Desvio: pequeno, mas é o que impede o mundo de virar um relógio.
        if planned and self.rng.random() < DEVIATION_P:
            public = self.world.locations_of_kind("social") + self.world.locations_of_kind("servico")
            return self.rng.choice(public), "deriva"

        if planned:
            destino, atividade = planned
            if not self.knowing.can(agent.id, atividade):
                # Não sabe fazer isso ainda. Fica por perto, observando.
                perto = home or rt.location
                return (perto, "perdido") if perto else (None, "perdido")
            if (rt.location and destino != rt.location
                    and self.world.travel_ticks(rt.location, destino) > 1
                    and not self.knowing.can_travel_far(agent.id)):
                # Longe demais para quem não sabe pegar transporte.
                return (rt.location, "perdido")
            return destino, atividade
        return (home, "casa") if home else (None, "ocioso")

    def _step_agent(self, rt: Runtime, tick: int) -> None:
        agent = rt.agent

        # Entidades não têm corpo nem lugar: encontram pelo canal de rede.
        if not agent.embodied:
            rt.location = None
            rt.activity = "latente"
            return

        # Chegou ao destino?
        if rt.traveling:
            if tick >= rt.travel_until:
                rt.location = rt.destination
                rt.destination = None
                rt.activity = "chegou"
            else:
                rt.activity = "em_transito"
                return

        target, activity = self._target_for(rt, tick)

        if target is None:
            rt.activity = "ocioso"
            return

        if rt.location is None:
            # Primeira aparição no mundo: materializa no destino.
            rt.location = target
            rt.activity = activity
        elif target != rt.location:
            cost = self.world.travel_ticks(rt.location, target)
            if cost <= 0:
                rt.location = target
                rt.activity = activity
            else:
                rt.destination = target
                rt.travel_until = tick + cost
                rt.location = None
                rt.activity = "em_transito"
                return
        else:
            rt.activity = activity

        self._apply_needs(rt)

    def _apply_needs(self, rt: Runtime) -> None:
        needs = rt.needs
        activity = rt.activity

        needs["fome"] = min(1.0, needs["fome"] + HUNGER_RATE)
        if activity == "dormir":
            needs["sono"] = max(0.0, needs["sono"] - SLEEP_RATE * 2.4)
            needs["energia"] = max(0.0, needs["energia"] - ENERGY_RATE * 2.0)
        else:
            needs["sono"] = min(1.0, needs["sono"] + SLEEP_RATE)
            needs["energia"] = min(1.0, needs["energia"] + ENERGY_RATE)

        if activity in ("comer", "descansar", "beber"):
            needs["fome"] = max(0.0, needs["fome"] - 0.55)
            needs["energia"] = max(0.0, needs["energia"] - 0.15)

    # -- encontros ----------------------------------------------------------

    def _detect_encounters(self, tick: int, active: list[Runtime]) -> list[tuple[str, str]]:
        by_location: dict[str, list[str]] = {}
        for rt in active:
            if rt.location is not None:
                by_location.setdefault(rt.location, []).append(rt.agent.id)

        current: set[tuple[str, str]] = set()
        fresh: list[tuple[str, str, str]] = []

        for location_id, occupants in by_location.items():
            occupants.sort()
            for i, a in enumerate(occupants):
                for b in occupants[i + 1:]:
                    pair = (a, b)

                    # Estar no mesmo local não é estar na mesma conversa. Num
                    # prédio cada um tem sua unidade; num parque de 25 lugares
                    # dois ocupantes podem nunca se ver. O contato é provável na
                    # razão inversa do tamanho do lugar.
                    # Uma vez cruzados, o par continua junto enquanto ambos
                    # ficarem — senão o encontro pisca e infla a contagem.
                    if pair not in self._contact_active:
                        if self.rng.random() >= self.contact_p[location_id]:
                            continue
                        self._contact_active.add(pair)
                    current.add(pair)

                    if pair not in self._previous_pairs:
                        self._encounter_buffer.append(
                            (tick, location_id, "presencial", a, b)
                        )
                        fresh.append((*pair, "presencial"))

        # Contato terminou quando o par se desfez.
        self._contact_active &= current

        # Rede: entidades sem corpo alcançam quem usa dispositivo em local conectado.
        entities = [rt.agent.id for rt in active if not rt.agent.embodied]
        if entities:
            for rt in active:
                if not rt.agent.embodied or rt.location not in self.connected:
                    continue
                if self.rng.random() >= NETWORK_USE_P:
                    continue
                for entity_id in entities:
                    pair = tuple(sorted((entity_id, rt.agent.id)))
                    current.add(pair)
                    if pair not in self._previous_pairs:
                        self._encounter_buffer.append(
                            (tick, rt.location, "rede", pair[0], pair[1])
                        )
                        fresh.append((*pair, "rede"))

        self._previous_pairs = current
        return fresh

    # -- laço ---------------------------------------------------------------

    def run(self, from_tick: int, to_tick: int, mode: str = "rapido") -> dict:
        """Avança o mundo de `from_tick` (inclusive) até `to_tick` (exclusive)."""
        started = time.perf_counter()

        for tick in range(from_tick, to_tick):
            self._plant_facts(tick)

            active = [
                rt for rt in self.runtime.values()
                if tick >= rt.agent.arrival_tick
            ]
            for rt in active:
                if rt.agent.id not in self._endowed:
                    self.knowing.endow(rt.agent.id, tick)
                    self._endowed.add(rt.agent.id)
            for rt in active:
                self._step_agent(rt, tick)
                self.knowing.practise(rt.agent.id, rt.activity)
                got = self.ledger.on_activity(
                    rt.agent.id, rt.activity, rt.location, tick)
                if got is not None and self.on_new_facts is not None:
                    self.on_new_facts()
                if self.record_states:
                    self._state_buffer.append(
                        (rt.agent.id, tick, rt.location, rt.activity,
                         json.dumps(rt.needs))
                    )

            here = {}
            for rt in active:
                if rt.location:
                    here.setdefault(rt.location, []).append(rt.agent.id)

            for a, b, channel in self._detect_encounters(tick, active):
                loc_a = self.runtime[a].location
                # Lido ANTES do encontro: depois dele o intervalo seria zero.
                previous_contact = self.ledger.relation(a, b)["last_contact_tick"]
                born = self.ledger.on_encounter(a, b, tick, here.get(loc_a, []))
                if born and self.on_new_facts is not None:
                    self.on_new_facts()
                # Conversa tem dois lados: cada um pode contar ao outro.
                trust = self.ledger.relation(a, b)["trust"]
                self.knowing.teach(a, b, tick, trust)
                self.knowing.teach(b, a, tick, trust)

                deltas = []
                for speaker, listener in ((a, b), (b, a)):
                    told = self.ledger.gossip(speaker, listener, tick)
                    if told:
                        deltas.append(told)
                if self.detector is not None:
                    loc = self.runtime[a].location or self.runtime[b].location
                    self.detector.score(tick, a, b, loc, channel, deltas,
                                        previous_contact, here.get(loc_a, []))

            if tick % TICKS_PER_DAY == 0:
                self.ledger.daily_upkeep(tick)

            if len(self._state_buffer) > 40_000:
                self._flush()

        self._flush()
        self.ledger.flush()
        self.knowing.flush()
        if self.detector is not None:
            self.detector.flush(self.conn)
        elapsed = time.perf_counter() - started

        self.conn.execute(
            "INSERT INTO run (started_at, mode, seed, from_tick, to_tick,"
            " ticks_per_day, params_json, wall_seconds)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                datetime.now(clockmod.TZ).isoformat(), mode, self.seed,
                from_tick, to_tick, TICKS_PER_DAY,
                json.dumps({
                    "deviation_p": DEVIATION_P,
                    "network_use_p": NETWORK_USE_P,
                    "hunger_critical": HUNGER_CRITICAL,
                    "sleep_critical": SLEEP_CRITICAL,
                }),
                round(elapsed, 3),
            ),
        )
        self.conn.execute(
            "INSERT INTO world_clock (id, epoch_iso, last_tick, mode)"
            " VALUES (1, ?, ?, ?)"
            " ON CONFLICT(id) DO UPDATE SET last_tick = excluded.last_tick,"
            " mode = excluded.mode",
            (clockmod.EPOCH.isoformat(), to_tick, mode),
        )
        self.conn.commit()

        return {"from_tick": from_tick, "to_tick": to_tick, "wall_seconds": elapsed}

    def _flush(self) -> None:
        if self._state_buffer:
            self.conn.executemany(
                "INSERT OR REPLACE INTO agent_state"
                " (agent_id, tick, location_id, activity, needs_json)"
                " VALUES (?, ?, ?, ?, ?)",
                self._state_buffer,
            )
            self._state_buffer.clear()
        if self._encounter_buffer:
            self.conn.executemany(
                "INSERT INTO encounter (tick, location_id, channel, agent_a, agent_b)"
                " VALUES (?, ?, ?, ?, ?)",
                self._encounter_buffer,
            )
            self._encounter_buffer.clear()
