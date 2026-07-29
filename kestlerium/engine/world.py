"""Carga do mundo: locais, grafo de deslocamento, elenco e rotinas.

Tudo que é conteúdo vive em data/*.json. Este módulo só traduz para o banco e
oferece as consultas que o laço de tempo precisa.
"""

from __future__ import annotations

import json
import sqlite3
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path

from . import clock as clockmod

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Um mundo é uma pasta de dados. `distrito` é a bancada de teste (15 pessoas,
# 12 locais, portões medindo distribuições); `vila` é a produção. Mesmo motor,
# configurações diferentes — foi para isto que o conteúdo saiu do código.
DEFAULT_WORLD = "distrito"

# Vem do relógio, nunca cravado aqui: com 48 escrito à mão, mudar TICK_MINUTES
# quebraria em silêncio as chegadas e as rotinas.
TICKS_PER_DAY = clockmod.TICKS_PER_DAY


@dataclass
class Agent:
    id: str
    name: str
    origin: str
    kind: str  # 'encarnado' | 'entidade'
    arrival_tick: int
    home: str | None
    anomaly: str | None
    constitution: str
    # rotina indexada por hora-do-dia: tod -> (location_id, activity)
    schedule: dict[int, tuple[str, str]] = field(default_factory=dict)

    @property
    def embodied(self) -> bool:
        return self.kind == "encarnado"


@dataclass
class World:
    locations: dict[str, sqlite3.Row]
    neighbors: dict[str, dict[str, int]]  # from -> {to: travel_ticks}
    agents: dict[str, Agent]
    _dist: dict[str, dict[str, int]] = field(default_factory=dict)

    def connected_locations(self) -> set[str]:
        return {lid for lid, row in self.locations.items() if row["connected"]}

    def private_locations(self) -> set[str]:
        """Moradias. Co-presença ali não é automática: cada um tem sua unidade."""
        return {lid for lid, row in self.locations.items() if not row["shared"]}

    def travel_ticks(self, origin: str, destination: str) -> int:
        """Menor tempo de deslocamento. BFS ponderado simples, cacheado.

        O grafo tem 12 nós; Dijkstra completo por origem é instantâneo e roda
        uma vez só por local.
        """
        if origin == destination:
            return 0
        if origin not in self._dist:
            self._dist[origin] = self._shortest_from(origin)
        return self._dist[origin].get(destination, 3)

    def _shortest_from(self, source: str) -> dict[str, int]:
        dist = {source: 0}
        queue: deque[str] = deque([source])
        while queue:
            node = queue.popleft()
            for neighbor, cost in self.neighbors.get(node, {}).items():
                candidate = dist[node] + cost
                if candidate < dist.get(neighbor, 1_000_000):
                    dist[neighbor] = candidate
                    queue.append(neighbor)
        return dist

    def food_locations(self) -> list[str]:
        """Onde se come. Vem dos dados: com os IDs cravados no motor,
        trocar de mundo deixaria todo mundo com fome."""
        out = [lid for lid, row in self.locations.items() if row["food"]]
        return sorted(out) or sorted(self.locations)

    def locations_of_kind(self, kind: str) -> list[str]:
        return sorted(lid for lid, row in self.locations.items() if row["kind"] == kind)


def _expand_schedule(routine: list) -> dict[int, tuple[str, str]]:
    """Converte faixas [start, end, local, atividade] em mapa tod -> destino."""
    schedule: dict[int, tuple[str, str]] = {}
    for start, end, location_id, activity in routine:
        for tod in range(start, end + 1):
            schedule[tod % TICKS_PER_DAY] = (location_id, activity)
    return schedule


def load(conn: sqlite3.Connection, world_name: str = DEFAULT_WORLD) -> World:
    """Lê os JSON, grava no banco e devolve o mundo em memória."""
    src = DATA / world_name
    locations_doc = json.loads((src / "locations.json").read_text(encoding="utf-8"))
    cast_doc = json.loads((src / "cast.json").read_text(encoding="utf-8"))

    conn.executemany(
        "INSERT OR REPLACE INTO location (id, name, kind, capacity, connected, shared, food)"
        " VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            (loc["id"], loc["name"], loc["kind"], loc["capacity"],
             loc["connected"], loc["shared"], loc.get("food", 0))
            for loc in locations_doc["locations"]
        ],
    )

    edges: list[tuple[str, str, int]] = []
    for a, b, cost in locations_doc["edges"]:
        edges.append((a, b, cost))
        edges.append((b, a, cost))  # grafo não-direcionado, gravado nos dois sentidos
    conn.executemany(
        "INSERT OR REPLACE INTO location_edge (from_id, to_id, travel_ticks) VALUES (?, ?, ?)",
        edges,
    )

    agents: dict[str, Agent] = {}
    agent_rows, routine_rows = [], []

    for spec in cast_doc["agents"]:
        agent = Agent(
            id=spec["id"],
            name=spec["name"],
            origin=spec["origin"],
            kind=spec["kind"],
            arrival_tick=spec["arrival_day"] * TICKS_PER_DAY,
            home=spec.get("home"),
            anomaly=spec.get("anomaly"),
            constitution=spec["constitution"],
            schedule=_expand_schedule(spec.get("routine", [])),
        )
        agents[agent.id] = agent

        constitution_json = json.dumps(
            {
                "text": agent.constitution,
                "anomaly": agent.anomaly,
                "origin": agent.origin,
            },
            ensure_ascii=False,
        )
        agent_rows.append(
            (agent.id, agent.name, agent.origin, agent.kind,
             agent.arrival_tick, agent.home, constitution_json)
        )
        for start, end, location_id, activity in spec.get("routine", []):
            routine_rows.append((agent.id, start, end, location_id, activity))

    conn.executemany(
        "INSERT OR REPLACE INTO agent"
        " (id, name, origin, kind, arrival_tick, home_location_id, constitution_json)"
        " VALUES (?, ?, ?, ?, ?, ?, ?)",
        agent_rows,
    )
    conn.execute("DELETE FROM routine")
    conn.executemany(
        "INSERT INTO routine (agent_id, start_tod, end_tod, location_id, activity)"
        " VALUES (?, ?, ?, ?, ?)",
        routine_rows,
    )
    conn.commit()

    locations = {row["id"]: row for row in conn.execute("SELECT * FROM location")}
    neighbors: dict[str, dict[str, int]] = {}
    for row in conn.execute("SELECT * FROM location_edge"):
        neighbors.setdefault(row["from_id"], {})[row["to_id"]] = row["travel_ticks"]

    return World(locations=locations, neighbors=neighbors, agents=agents)
