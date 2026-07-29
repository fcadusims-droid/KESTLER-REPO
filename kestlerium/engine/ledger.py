"""Verdade, crença e a distância entre as duas — Fase 2.

A regra que sustenta o resto do projeto: **nenhum agente lê `fact`.** Toda
leitura passa por `belief`. Um fato pode ser verdadeiro e ninguém saber; pode
ser sabido por três pessoas em três versões diferentes; pode chegar até quem
ele condena numa forma que não o condena mais. Sem essa separação não existe
segredo, e sem segredo não existe drama.

Três mecanismos:

1. **Testemunho.** Quem está presente forma crença em primeira mão. Um nativo
   que vê o impossível racionaliza: não crê "ele é um vampiro", crê "foi
   truque". A versão fiel e a racionalizada competem pela mesma aresta.

2. **Fofoca.** No encontro, com probabilidade dependente de confiança e
   saliência, um agente transmite uma crença. A confiança degrada a cada salto
   e a distorção pode crescer. É aqui que informação errada nasce sozinha,
   sem ninguém mentir.

3. **Corrosão da racionalização.** Testemunhar a mesma anomalia de novo derruba
   a distorção. Uma explicação boba aguenta um episódio; não aguenta três.
   É esse acúmulo que produz exposição.
"""

from __future__ import annotations

import json
import sqlite3
from random import Random

# --- fofoca -----------------------------------------------------------------
GOSSIP_BASE_P = 0.22        # chance por encontro de haver transmissão
CONFIDENCE_DECAY = 0.85     # degradação por salto, conforme o plano
DISTORTION_P = 0.28         # chance de a versão piorar ao ser repassada
SALIENCE_TO_GOSSIP = 0.25   # abaixo disso a crença não é interessante o bastante

# --- saliência --------------------------------------------------------------
SALIENCE_DAILY_DECAY = 0.97
SALIENCE_ON_REACTIVATION = 0.28

# --- relação ----------------------------------------------------------------
TRUST_ON_CONTACT = 0.010
AFFECT_ON_CONTACT = 0.006
TENSION_DAILY_GROWTH = 0.004    # tensão sobe sozinha onde há fio aberto
TENSION_DISCHARGE = 0.45        # ralo simbólico: confronto sem LLM
TENSION_CONFRONT_THRESHOLD = 0.55

# --- eventos endógenos ------------------------------------------------------
# O mundo precisa produzir fatos próprios, senão esfria assim que os fatos
# plantados terminam de circular. Confronto e vínculo são as duas coisas que
# a dinâmica de relação já sabe detectar sem precisar de LLM nenhum.
BOND_AFFECT = 0.35
BOND_TRUST = 0.62

# Racionalizações por anomalia: o que uma pessoa comum conclui ao ver o
# impossível. Índice = nível de distorção.
RATIONALIZATIONS = {
    "sangue": ["truque_de_luz", "estava_drogada", "ele_e_enfermeiro"],
    "ressonancia": ["foi_o_vento", "ouvi_coisas", "cansaco"],
    "corpo_de_maquina": ["protese", "figurino", "vi_errado"],
    "esfera": ["reflexo", "brinquedo", "nao_vi_direito"],
    "rede": ["coincidencia", "vazamento_comum", "propaganda_dirigida"],
}
DEFAULT_RATIONALIZATION = ["mal_entendido", "boato", "engano"]


def pair(a: str, b: str) -> tuple[str, str]:
    return (a, b) if a < b else (b, a)


class Ledger:
    """Guarda a verdade e distribui crenças a partir dela."""

    def __init__(self, conn: sqlite3.Connection, rng: Random, agents: dict) -> None:
        self.conn = conn
        self.rng = rng
        self.agents = agents
        # cache em memória; o banco é escrito em lote
        self.facts: dict[int, dict] = {}
        self.beliefs: dict[tuple[str, int], dict] = {}
        self.relations: dict[tuple[str, str], dict] = {}
        # Recursos e burocracia: o mínimo para que adquirir_recurso e
        # estabelecer_identidade deixem de ser rótulos inertes.
        self.resources: dict[str, float] = {}
        self.paperwork: dict[str, int] = {}

    # -- verdade ------------------------------------------------------------

    def add_fact(self, tick, subject, predicate, obj, visibility, witnesses) -> int:
        cur = self.conn.execute(
            "INSERT INTO fact (tick, subject, predicate, object, visibility, witnesses_json)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (tick, subject, predicate, obj, visibility, json.dumps(sorted(witnesses))),
        )
        fact_id = cur.lastrowid
        self.facts[fact_id] = {
            "id": fact_id, "tick": tick, "subject": subject,
            "predicate": predicate, "object": obj,
            "visibility": visibility, "witnesses": set(witnesses),
        }
        return fact_id

    # -- crença -------------------------------------------------------------

    def _is_mundane(self, agent_id: str) -> bool:
        """Sem anomalia própria: não tem vocabulário para o impossível."""
        agent = self.agents.get(agent_id)
        return agent is None or agent.anomaly is None

    def witness(self, agent_id: str, fact_id: int, tick: int) -> None:
        """Crença de primeira mão. Anomalia vista por gente comum já nasce torta."""
        fact = self.facts[fact_id]
        key = (agent_id, fact_id)

        anomalous = fact["predicate"] == "usou_anomalia"
        rationalizes = anomalous and self._is_mundane(agent_id)

        existing = self.beliefs.get(key)
        if existing:
            # Ver de novo corrói a racionalização: uma explicação boba aguenta
            # um episódio, não aguenta três.
            if existing["distortion"] > 0:
                existing["distortion"] -= 1
                existing["distorted_object"] = self._rationalization(
                    fact, existing["distortion"]
                )
            existing["confidence"] = min(1.0, existing["confidence"] + 0.18)
            existing["salience"] = min(1.0, existing["salience"] + SALIENCE_ON_REACTIVATION)
            return

        distortion = 1 if rationalizes else 0
        self.beliefs[key] = {
            "agent_id": agent_id, "fact_id": fact_id,
            "confidence": 0.72 if rationalizes else 0.95,
            "distortion": distortion,
            "distorted_object": self._rationalization(fact, distortion),
            "source_agent_id": None,
            "salience": 0.85,
            "acquired_tick": tick,
        }

    def _rationalization(self, fact: dict, distortion: int) -> str | None:
        if distortion <= 0:
            return None
        anomaly = None
        subject = self.agents.get(fact["subject"])
        if subject is not None:
            anomaly = subject.anomaly
        table = RATIONALIZATIONS.get(anomaly, DEFAULT_RATIONALIZATION)
        return table[min(distortion - 1, len(table) - 1)]

    # -- fofoca -------------------------------------------------------------

    def _transmittable(self, speaker: str) -> list[tuple[int, dict]]:
        # Entidade não fofoca. Suomynona não comenta com a vizinha o que
        # descobriu — ela acumula e publica. Deixá-la repassar boato a
        # transformava no maior vetor de fofoca do distrito, que é o oposto
        # do que ela é. Ela recebe (detecta) e retém.
        agent = self.agents.get(speaker)
        if agent is not None and not agent.embodied:
            return []

        out = []
        for (agent_id, fact_id), belief in self.beliefs.items():
            if agent_id != speaker or belief["salience"] < SALIENCE_TO_GOSSIP:
                continue
            fact = self.facts[fact_id]
            # Ninguém entrega o próprio segredo. É isso que faz ocultar_anomalia
            # ser um objetivo com custo em vez de um rótulo.
            if fact["subject"] == speaker and fact["visibility"] != "publico":
                continue
            out.append((fact_id, belief))
        return out

    def gossip(self, speaker: str, listener: str, tick: int) -> tuple[int, float] | None:
        rel = self.relation(speaker, listener)
        candidates = self._transmittable(speaker)
        if not candidates:
            return None

        p = GOSSIP_BASE_P * (0.4 + rel["trust"])
        if self.rng.random() >= p:
            return None

        # Mais saliente, mais provável de ser dito.
        weights = [b["salience"] for _, b in candidates]
        fact_id, source_belief = self.rng.choices(candidates, weights=weights, k=1)[0]

        key = (listener, fact_id)
        heard_confidence = source_belief["confidence"] * CONFIDENCE_DECAY
        distortion = source_belief["distortion"]
        if self.rng.random() < DISTORTION_P:
            distortion += 1

        existing = self.beliefs.get(key)
        if existing:
            # Ouvir de novo reforça o que já se acredita; não converte.
            before = existing["confidence"]
            existing["confidence"] = min(
                1.0, max(existing["confidence"], heard_confidence * 0.9)
            )
            delta = existing["confidence"] - before
            existing["salience"] = min(1.0, existing["salience"] + SALIENCE_ON_REACTIVATION)
        else:
            fact = self.facts[fact_id]
            delta = heard_confidence   # crença nova: de zero ao que ouviu
            self.beliefs[key] = {
                "agent_id": listener, "fact_id": fact_id,
                "confidence": heard_confidence,
                "distortion": distortion,
                "distorted_object": self._rationalization(fact, distortion),
                "source_agent_id": speaker,
                "salience": 0.6,
                "acquired_tick": tick,
            }

        source_belief["salience"] = min(
            1.0, source_belief["salience"] + SALIENCE_ON_REACTIVATION * 0.5
        )
        return fact_id, delta

    # -- relações -----------------------------------------------------------

    def relation(self, a: str, b: str) -> dict:
        key = pair(a, b)
        rel = self.relations.get(key)
        if rel is None:
            rel = {"agent_a": key[0], "agent_b": key[1], "affect": 0.0,
                   "trust": 0.30, "tension": 0.0, "last_contact_tick": None}
            self.relations[key] = rel
        return rel

    def on_encounter(self, a: str, b: str, tick: int,
                     present: list[str] | None = None) -> list[int]:
        """Atualiza a relação e devolve fatos que o próprio mundo gerou."""
        rel = self.relation(a, b)
        rel["trust"] = min(1.0, rel["trust"] + TRUST_ON_CONTACT)
        rel["affect"] = max(-1.0, min(1.0, rel["affect"] + AFFECT_ON_CONTACT))
        rel["last_contact_tick"] = tick
        born: list[int] = []
        witnesses = sorted(set(present or []) | {a, b})

        # Ralo simbólico de tensão. O portão da Fase 3 exige tensão oscilando,
        # mas antes do LLM nada a reduz — sem isto o critério é inalcançável por
        # falha de projeto, não por defeito do mundo.
        if rel["tension"] >= TENSION_CONFRONT_THRESHOLD:
            rel["tension"] *= (1.0 - TENSION_DISCHARGE)
            rel["affect"] = max(-1.0, rel["affect"] - 0.05)
            # O confronto deixa marca: quem viu, viu.
            fid = self.add_fact(tick, a, "brigou_com", b, "privado", witnesses)
            for w in witnesses:
                self.witness(w, fid, tick)
            born.append(fid)

        # Vínculo que se firma também é fato, e uma única vez.
        if (not rel.get("bonded") and rel["affect"] >= BOND_AFFECT
                and rel["trust"] >= BOND_TRUST):
            rel["bonded"] = True
            fid = self.add_fact(tick, a, "ama", b, "privado", [a, b])
            for w in (a, b):
                self.witness(w, fid, tick)
            born.append(fid)

        return born

    def on_activity(self, agent_id: str, activity: str, location_id: str | None,
                    tick: int) -> int | None:
        """O trabalho paga, a vida gasta, e o cartório é lento."""
        if activity == "trabalhar":
            self.resources[agent_id] = self.resources.get(agent_id, 0.0) + 1.2
        elif activity in ("comer", "compras", "beber"):
            self.resources[agent_id] = max(0.0, self.resources.get(agent_id, 0.0) - 2.5)

        if location_id == "registro" and activity not in ("dormir", "em_transito"):
            n = self.paperwork.get(agent_id, 0) + 1
            self.paperwork[agent_id] = n
            if n == 8:
                fid = self.add_fact(tick, agent_id, "possui_documento",
                                    "registro_civil", "publico", [agent_id])
                self.witness(agent_id, fid, tick)
                return fid
        return None

    def daily_upkeep(self, tick: int) -> None:
        for belief in self.beliefs.values():
            belief["salience"] *= SALIENCE_DAILY_DECAY
        for rel in self.relations.values():
            # Só cresce onde há fio aberto: gente que já se conhece.
            if rel["last_contact_tick"] is not None:
                rel["tension"] = min(1.0, rel["tension"] + TENSION_DAILY_GROWTH)

    # -- persistência -------------------------------------------------------

    def flush(self) -> None:
        self.conn.executemany(
            "INSERT OR REPLACE INTO belief (agent_id, fact_id, confidence, distortion,"
            " distorted_object, source_agent_id, salience, acquired_tick)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [
                (b["agent_id"], b["fact_id"], b["confidence"], b["distortion"],
                 b["distorted_object"], b["source_agent_id"], b["salience"],
                 b["acquired_tick"])
                for b in self.beliefs.values()
            ],
        )
        self.conn.executemany(
            "INSERT OR REPLACE INTO relation (agent_a, agent_b, affect, trust,"
            " tension, last_contact_tick) VALUES (?, ?, ?, ?, ?, ?)",
            [
                (r["agent_a"], r["agent_b"], r["affect"], r["trust"],
                 r["tension"], r["last_contact_tick"])
                for r in self.relations.values()
            ],
        )
        self.conn.commit()
