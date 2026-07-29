"""Conhecimento: o que um agente sabe sobre COMO O MUNDO FUNCIONA.

Separado de `belief`, que guarda o que ele sabe sobre PESSOAS. Aqui é sobre
coisas: o que é dinheiro, o que é um ônibus, o que é um turno de trabalho.

**A regra do autor.** Um personagem conhece apenas o que viveu dentro da
história dele — nunca a obra. Severin sabe o que é linhagem e juramento porque
atravessou os dois; não sabe o enredo de *One Blood*, não sabe o que aconteceu
longe da vista dele, não sabe que é personagem de coisa alguma. Essa fronteira
pertence ao autor e não atravessa para cá.

**A consequência que dá verdade ao mundo.** Sem o conceito, a atividade não
acontece. Quem não sabe o que é emprego não vai trabalhar; quem não sabe o que
é dinheiro não compra comida; quem não sabe o que é transporte fica preso onde
chegou. É isto que faz `compreender_mundo` deixar de ser rótulo e virar
pré-requisito de sobrevivência — e é isto que torna o NPC necessário, porque
alguém precisa explicar.

A troca é nos dois sentidos, e a de volta é distorcida: o morador da vila ouve
falar de juramento de sangue e arquiva como história de doido — a mesma
racionalização que faz Clara ver o impossível e concluir "truque de luz".
"""

from __future__ import annotations

import json
import pathlib
import sqlite3
from random import Random

DATA = pathlib.Path(__file__).resolve().parent.parent / "data"

USABLE = 0.55          # abaixo disto o conceito não sustenta uma atividade
TEACH_P = 0.30         # chance por encontro de haver ensino
NATIVE_TEACH_BONUS = 2.2  # quem é daqui explica como as coisas são daqui
GRASP_ON_TEACH = 0.34  # o quanto se aprende por conversa; ninguém aprende de uma vez
GRASP_ON_USE = 0.05    # praticar consolida
FOREIGN_GRASP = 0.22   # o que um local retém de um conceito de outro mundo


class Knowledge:
    def __init__(self, conn: sqlite3.Connection, rng: Random, agents: dict) -> None:
        self.conn = conn
        self.rng = rng
        self.agents = agents
        doc = json.loads((DATA / "knowledge.json").read_text(encoding="utf-8"))
        self.world_concepts = [k for k in doc["mundo"] if not k.startswith("_")]
        self.requirements = doc["requisitos"]
        self.origin_concepts = {
            k: [c for c in v if not c.startswith("_")]
            for k, v in doc["origem"].items() if not k.startswith("_")
        }
        # agent_id -> {concept: grasp}
        self.known: dict[str, dict[str, float]] = {}
        self._source: dict[tuple[str, str], str | None] = {}
        self._when: dict[tuple[str, str], int] = {}

    # -- dotação inicial ----------------------------------------------------

    def endow(self, agent_id: str, tick: int) -> None:
        """O que este agente traz consigo ao entrar no mundo."""
        agent = self.agents[agent_id]
        mine: dict[str, float] = {}

        if agent.origin == "nativo":
            # Nasceu aqui: o mundo moderno é óbvio para ele.
            for concept in self.world_concepts:
                mine[concept] = 1.0
        else:
            # Chegou de outro lugar. Traz o que viveu — e nada daqui.
            for concept in self.origin_concepts.get(agent.origin, []):
                mine[concept] = 1.0

        self.known[agent_id] = mine
        for concept in mine:
            self._source[(agent_id, concept)] = None
            self._when[(agent_id, concept)] = tick

    # -- consulta -----------------------------------------------------------

    def grasp(self, agent_id: str, concept: str) -> float:
        return self.known.get(agent_id, {}).get(concept, 0.0)

    def can(self, agent_id: str, activity: str) -> bool:
        """Sabe o bastante para fazer isto?"""
        for concept in self.requirements.get(activity, ()):
            if self.grasp(agent_id, concept) < USABLE:
                return False
        return True

    def can_travel_far(self, agent_id: str) -> bool:
        return self.grasp(agent_id, "transporte") >= USABLE

    def world_grasp(self, agent_id: str) -> float:
        """Fração do mundo moderno que este agente já domina. 0..1."""
        if not self.world_concepts:
            return 1.0
        total = sum(
            min(1.0, self.grasp(agent_id, c) / USABLE) for c in self.world_concepts
        )
        return total / len(self.world_concepts)

    # -- prática ------------------------------------------------------------

    def practise(self, agent_id: str, activity: str) -> None:
        for concept in self.requirements.get(activity, ()):
            current = self.known.setdefault(agent_id, {}).get(concept, 0.0)
            if 0.0 < current < 1.0:
                self.known[agent_id][concept] = min(1.0, current + GRASP_ON_USE)

    # -- ensino -------------------------------------------------------------

    def teach(self, teacher: str, student: str, tick: int, trust: float) -> str | None:
        """Uma conversa em que alguém explica como as coisas são aqui.

        O aprendiz não sai sabendo: sai sabendo um pouco. Conceito se firma por
        repetição e uso, que é o que faz o recém-chegado depender de conviver e
        não de um único encontro providencial.
        """
        # Quem é do lugar ensina o lugar. É esse o papel do morador comum
        # diante de alguém que acabou de chegar sem entender nada — e sem
        # ele o aprendizado fica ao acaso do encontro, o que trava o
        # deslocado e esfria o mundo inteiro.
        chance = TEACH_P * (0.4 + trust)
        if self.agents[teacher].origin == "nativo":
            chance *= NATIVE_TEACH_BONUS
        if self.rng.random() >= chance:
            return None

        mine = self.known.get(teacher, {})
        theirs = self.known.setdefault(student, {})

        # O que eu domino e o outro ainda não.
        gaps = [
            c for c, g in mine.items()
            if g >= USABLE and theirs.get(c, 0.0) < 1.0
        ]
        if not gaps:
            return None
        concept = self.rng.choice(sorted(gaps))

        foreign = concept not in self.world_concepts
        student_native = self.agents[student].origin == "nativo"

        gain = GRASP_ON_TEACH
        if foreign and student_native:
            # Conceito de outro mundo, ouvido por quem mora aqui: fica como
            # curiosidade, não como ferramenta. História de doido.
            gain = FOREIGN_GRASP * 0.5

        before = theirs.get(concept, 0.0)
        theirs[concept] = min(1.0, before + gain)
        if before == 0.0:
            self._source[(student, concept)] = teacher
            self._when[(student, concept)] = tick
        return concept

    # -- persistência -------------------------------------------------------

    def flush(self) -> None:
        rows = []
        for agent_id, concepts in self.known.items():
            for concept, grasp in concepts.items():
                rows.append((
                    agent_id, concept, grasp,
                    self._when.get((agent_id, concept), 0),
                    self._source.get((agent_id, concept)),
                ))
        self.conn.executemany(
            "INSERT OR REPLACE INTO knowledge"
            " (agent_id, concept, grasp, learned_tick, taught_by)"
            " VALUES (?, ?, ?, ?, ?)",
            rows,
        )
        self.conn.commit()
