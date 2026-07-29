"""Governador de ritmo — Fase 4. Ainda zero LLM.

O detector de pressão diz o que *poderia* ser contado. Este módulo decide o que
*será* — e, mais importante, o que fica esperando.

Existe por três razões, e nenhuma é economia de dinheiro:

1. **Orçamento.** Sem teto, a narração das fases seguintes gasta sem critério e
   conta tudo com a mesma importância. Um mundo em que tudo é cena não tem cena
   nenhuma.

2. **Descanso por personagem.** Sem isso aparece o protagonista acidental: quem
   entra em duas cenas seguidas vira o centro da história por acidente
   estatístico, não por escolha. O descanso força o elenco a circular.

3. **Fila com bônus de espera.** Tensão adiada é estrutura, não desperdício. Um
   evento que perdeu a vez volta mais forte — e se continuar perdendo, ganha
   força até que ignorá-lo fique impossível. É assim que um fio esquecido
   cobra a própria resolução.

Toda decisão é registrada: o que passou, o que caiu, e por qual pontuação.
Sem esse registro, um cronograma ruim é impossível de explicar depois.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field

from . import clock as clockmod

# Orçamento por semana simulada.
BUDGET_SCENE = 2      # cenas encenadas (L2): caras, raras, decisivas
BUDGET_BEAT = 15      # beats narrados (L1): baratos, frequentes

# Um agente não entra em duas cenas encenadas em menos que isto.
COOLDOWN_SCENE_DAYS = 6
COOLDOWN_BEAT_DAYS = 1

# Quanto um evento ganha por semana esperando na fila.
WAIT_BONUS = 0.06
MAX_WAIT_DAYS = 42    # depois disso o assunto esfriou de vez

# Cena encenada é o pico, e o pico é o mesmo que o detector já reconhece como
# tal. Com o piso mais baixo, quase todo evento virava cena e o cronograma
# saía invertido — mais cenas caras que beats baratos, que é o oposto do que
# o orçamento existe para fazer.
SCENE_FLOOR = 0.70


@dataclass
class Scheduled:
    tick: int
    day: int
    kind: str            # 'cena' | 'beat'
    participants: list
    facts: list
    pressure: float
    score: float
    reason: str


@dataclass
class Governor:
    ticks_per_day: int = clockmod.TICKS_PER_DAY
    fila: list = field(default_factory=list)
    agenda: list = field(default_factory=list)
    descartes: list = field(default_factory=list)
    _last_scene: dict = field(default_factory=dict)
    _last_beat: dict = field(default_factory=dict)

    # -- fila ---------------------------------------------------------------

    def offer(self, event) -> None:
        """Um evento de pressão entra na disputa."""
        self.fila.append({
            "tick": event.tick, "day": event.day,
            "participants": list(event.participants) or [event.agent_a, event.agent_b],
            "facts": list(event.facts),
            "pressure": event.value,
            "a": event.agent_a, "b": event.agent_b,
        })

    def _score(self, item: dict, day: int) -> float:
        """Pressão mais o que a espera acrescentou."""
        esperou = max(0, day - item["day"])
        bonus = WAIT_BONUS * (esperou / 7.0)
        return item["pressure"] + bonus

    def _rested(self, item: dict, kind: str) -> bool:
        """Descanso medido contra o dia em que o evento ACONTECEU.

        Medir contra o dia do fechamento fazia o primeiro beat da semana cansar
        o elenco inteiro e bloquear todos os outros: dezessete beats agendados
        onde cabiam cento e oitenta. O evento de terça e o de sábado são dias
        diferentes, mesmo que a decisão sobre os dois seja tomada de uma vez.
        """
        registro = self._last_scene if kind == "cena" else self._last_beat
        limite = COOLDOWN_SCENE_DAYS if kind == "cena" else COOLDOWN_BEAT_DAYS
        for agente in item["participants"]:
            visto = registro.get(agente)
            if visto is not None and item["day"] - visto < limite:
                return False
        return True

    # -- decisão ------------------------------------------------------------

    def close_week(self, day: int) -> list[Scheduled]:
        """Fecha a semana: escolhe o que se conta e o que continua esperando."""
        # Descarta o que esfriou demais.
        vivos, frios = [], []
        for item in self.fila:
            (frios if day - item["day"] > MAX_WAIT_DAYS else vivos).append(item)
        for item in frios:
            self.descartes.append({**item, "motivo": "esfriou na fila"})
        self.fila = vivos

        candidatos = sorted(self.fila, key=lambda i: (-self._score(i, day), i["day"]))
        escolhidos: list[Scheduled] = []
        restantes: list[dict] = []
        cenas = beats = 0

        for item in candidatos:
            score = self._score(item, day)

            # O piso é testado contra a pressão CRUA, não contra o score.
            # A espera dá prioridade na fila; não dá importância. Um assunto que
            # ninguém achou grave por seis semanas não vira clímax por ter
            # esperado — sem esta distinção, cenas decisivas saíam com pressão
            # 0.41 enquanto o piso declarado era 0.70.
            if (cenas < BUDGET_SCENE and item["pressure"] >= SCENE_FLOOR
                    and self._rested(item, "cena")):
                cenas += 1
                for a in item["participants"]:
                    self._last_scene[a] = item["day"]
                    self._last_beat[a] = item["day"]
                escolhidos.append(Scheduled(
                    item["tick"], item["day"], "cena", item["participants"],
                    item["facts"], item["pressure"], score,
                    "maior pressão da semana"))
                continue

            if beats < BUDGET_BEAT and self._rested(item, "beat"):
                beats += 1
                for a in item["participants"]:
                    self._last_beat[a] = item["day"]
                escolhidos.append(Scheduled(
                    item["tick"], item["day"], "beat", item["participants"],
                    item["facts"], item["pressure"], score,
                    "dentro do orçamento de beats"))
                continue

            # Perdeu a vez: volta à fila e cobra juros.
            motivo = ("orçamento esgotado" if (cenas >= BUDGET_SCENE and beats >= BUDGET_BEAT)
                      else "personagem ainda descansando")
            item["ultimo_motivo"] = motivo
            restantes.append(item)

        self.fila = restantes
        self.agenda.extend(escolhidos)
        return escolhidos

    # -- persistência -------------------------------------------------------

    def load(self, conn: sqlite3.Connection) -> None:
        """Retoma fila e descanso de onde a execução anterior parou.

        No modo real cada execução avança meia hora de mundo e termina. Sem
        isto o governador renasceria vazio a cada 30 minutos: a fila nunca
        acumularia espera, o bônus jamais chegaria a valer nada, e o descanso
        por personagem — que é o que impede o protagonista acidental — não
        atravessaria nem um dia.
        """
        self.fila = [
            {"tick": r["tick"], "day": r["day"],
             "participants": json.loads(r["participants_json"]),
             "facts": json.loads(r["facts_json"]),
             "pressure": r["pressure"], "a": r["agent_a"], "b": r["agent_b"]}
            for r in conn.execute("SELECT * FROM queued ORDER BY id")
        ]
        for r in conn.execute("SELECT * FROM rest"):
            alvo = self._last_scene if r["kind"] == "cena" else self._last_beat
            alvo[r["agent_id"]] = r["last_day"]

    def flush(self, conn: sqlite3.Connection) -> None:
        conn.execute("DELETE FROM queued")
        conn.executemany(
            "INSERT INTO queued (tick, day, participants_json, facts_json,"
            " pressure, agent_a, agent_b) VALUES (?, ?, ?, ?, ?, ?, ?)",
            [(i["tick"], i["day"], json.dumps(i["participants"]),
              json.dumps(i["facts"]), i["pressure"], i["a"], i["b"])
             for i in self.fila],
        )
        conn.executemany(
            "INSERT OR REPLACE INTO rest (agent_id, kind, last_day) VALUES (?, ?, ?)",
            [(a, "cena", d) for a, d in self._last_scene.items()]
            + [(a, "beat", d) for a, d in self._last_beat.items()],
        )
        conn.executemany(
            "INSERT INTO scheduled (tick, day, kind, participants_json,"
            " facts_json, pressure, score, reason)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [(s.tick, s.day, s.kind, json.dumps(s.participants),
              json.dumps(s.facts), s.pressure, s.score, s.reason)
             for s in self.agenda],
        )
        conn.commit()
