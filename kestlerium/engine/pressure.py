"""Detector de pressão — Fase 3. Ainda zero LLM.

Esta fase decide se o projeto continua. Ela responde à única pergunta que pode
matá-lo: **o modelo de mundo gera estrutura narrativa sozinho?** Se a resposta
for não, o problema está na ontologia e no grafo social — não no LLM que ainda
nem entrou.

Nenhum componente aqui interpreta significado. Pressão é aritmética sobre o
estado: quantos objetivos dependem de um fato cuja confiança mudou, quantos
objetivos se atropelam, há quanto tempo duas pessoas com carga afetiva não se
falam, quão raro é o que acabou de acontecer, quanta tensão a aresta acumulou.

O produto real da fase não é o número — é a instrumentação. Uma distribuição de
pressão sem cauda pesada significa um mundo onde nada importa, e isso é
diagnóstico, não detalhe.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

# Pesos iniciais todos 1.0, conforme o plano.
#
# Mas peso só é interpretável se os componentes forem comparáveis, e medidos
# eles NÃO eram: dE vivia em [0, 0.18] e CO em [0, 1.76]. Somados com peso 1,
# CO dominava sempre e o detector virou um medidor de conflito de objetivo com
# quatro enfeites — varrer os pesos apenas trocava qual componente mandava.
# Calibragem não conserta unidade errada.
#
# Cada componente passa por x/(x+k), que satura suave em 1 e é ~linear perto de
# zero. Os k saem dos percentis medidos (p99 de cada um mapeia para ~0.65), de
# modo que todos contribuem na mesma ordem de grandeza. Só depois disso os
# pesos passam a significar importância relativa de verdade.
# Valores derivados de varredura sobre os dados, não escolhidos a priori.
# Substância (ep/co) controla QUANTOS picos; plateia controla QUEM participa.
# Reajustados quando compreender_mundo deixou de ser inerte: conhecimento sendo
# aprendido move objetivo, e o mundo passou a ter mais coisa acontecendo.
# Separar esses dois botões foi o que destravou o portão: antes, reduzir picos
# custava cobertura de elenco, e nenhuma combinação satisfazia os dois.
W_EPISTEMIC = 0.62
W_CONFLICT = 0.50
W_RELATIONAL = 1.25
W_RARITY = 0.82
W_TENSION = 0.40
W_AUDIENCE = 2.3

K_EPISTEMIC = 0.05    # p99 medido 0.096
K_CONFLICT = 0.50     # p99 medido 0.975
K_RELATIONAL = 0.10
K_TENSION = 0.20      # p99 medido 0.344
K_AUDIENCE = 2.0      # plateia além do par


def _norm(x: float, k: float) -> float:
    """Satura em 1, linear perto de zero. Torna escalas comparáveis."""
    return x / (x + k) if x > 0 else 0.0

# Escala do "há quanto tempo não se falam". O plano sugeriu 180 dias, mas
# medido neste mundo o termo saía SEMPRE zero: as pessoas se cruzam a cada
# poucos dias e 1-exp(-2/180) ~ 0.01 apaga a componente inteira. Três semanas
# é a escala em que um reencontro é notável aqui.
TAU_DAYS = 21.0


@dataclass
class PressureEvent:
    tick: int
    day: int
    agent_a: str
    agent_b: str
    location_id: str | None
    channel: str
    value: float
    parts: dict = field(default_factory=dict)
    participants: list = field(default_factory=list)


class PressureDetector:
    def __init__(self, ledger, goals: list[dict], ticks_per_day: int) -> None:
        self.ledger = ledger
        self.ticks_per_day = ticks_per_day
        self.goals_by_agent: dict[str, list[dict]] = {}
        for goal in goals:
            self.goals_by_agent.setdefault(goal["agent_id"], []).append(goal)

        from .goals import GoalTracker, leverage
        self.leverage = leverage(goals, ledger.relations)
        self.tracker = GoalTracker(goals, ledger.agents)

        # Assinaturas já vistas, para medir raridade estrutural.
        self._seen: dict[tuple, int] = {}
        self.events: list[PressureEvent] = []

    def rebuild(self, goals: list[dict]) -> None:
        """Objetivos mudaram (fato novo no mundo). Preserva raridade e eventos."""
        from .goals import GoalTracker, leverage
        self.goals_by_agent = {}
        for goal in goals:
            self.goals_by_agent.setdefault(goal["agent_id"], []).append(goal)
        self.leverage = leverage(goals, self.ledger.relations)
        previous = self.tracker._last if hasattr(self, "tracker") else {}
        self.tracker = GoalTracker(goals, self.ledger.agents)
        self.tracker._last.update(previous)

    # -- componentes --------------------------------------------------------

    def _holders(self, fact_id: int) -> int:
        return sum(1 for (_, f) in self.ledger.beliefs if f == fact_id)

    def epistemic_delta(self, deltas: list[tuple[int, float]]) -> float:
        """Σ alavancagem(fato) × |Δconfiança| ÷ quantos já sabem.

        Alavancagem é grau de saída: quantos objetivos dependem daquele fato.
        Uma fofoca sobre coisa que não sustenta objetivo nenhum vale zero, por
        mais escandalosa que soe.

        A divisão pelo número de portadores é o que impede que todo mundo
        descobrindo o mesmo segredo produza vinte picos iguais: **o valor
        dramático de uma informação é inverso a quantos já a possuem.** O
        primeiro a saber muda o mundo; o décimo confirma o que a rua comenta.
        Informação que dez pessoas têm deixou de ser informação.
        """
        total = 0.0
        for fid, d in deltas:
            spread = self._holders(fid)
            total += self.leverage.get(fid, 0.0) * abs(d) / (1.0 + spread)
        return total

    def goal_conflict(self, a: str, b: str) -> float:
        """Objetivos bloqueados ou avançados por este evento.

        Mede MUDANÇA, não incompatibilidade. Dois inimigos declarados que se
        cruzam sem nada mudar pontuam zero — o que é correto: não aconteceu
        nada. O potencial de conflito vira pressão quando ele se move.
        """
        moved = self.tracker.delta_for((a, b), self.ledger)
        if moved <= 0.0:
            return 0.0
        from .goals import conflict_score
        # A incompatibilidade estrutural amplifica a mudança, não a substitui.
        rivalry = conflict_score(
            self.goals_by_agent.get(a, []), self.goals_by_agent.get(b, []), a, b
        )
        return moved * (1.0 + rivalry)

    def relational_charge(self, a: str, b: str, tick: int,
                          last_contact: int | None) -> float:
        """|afeto| × raridade do contato.

        Duas pessoas que se odeiam e se veem todo dia não geram evento. As
        mesmas duas depois de meses sem se falar, geram.

        `last_contact` vem de FORA porque quem trata o encontro já atualizou o
        registro antes de o detector rodar — lendo do ledger, o intervalo seria
        sempre zero e esta componente morreria por ordem de chamada.
        """
        rel = self.ledger.relation(a, b)
        if last_contact is None:
            gap_days = TAU_DAYS
        else:
            gap_days = (tick - last_contact) / self.ticks_per_day
        return abs(rel["affect"]) * (1.0 - math.exp(-gap_days / TAU_DAYS))

    def structural_rarity(self, signature: tuple) -> float:
        count = self._seen.get(signature, 0)
        self._seen[signature] = count + 1
        return 1.0 / (1.0 + count)

    def accumulated_tension(self, a: str, b: str) -> float:
        return self.ledger.relation(a, b)["tension"]

    # -- pressão ------------------------------------------------------------

    def score(self, tick, a, b, location_id, channel,
              deltas: list[tuple[int, float]],
              last_contact: int | None = None,
              present: list | None = None) -> PressureEvent:
        dE = self.epistemic_delta(deltas)
        CO = self.goal_conflict(a, b)
        CR = self.relational_charge(a, b, tick, last_contact)
        RE = self.structural_rarity((a, b, channel))
        TA = self.accumulated_tension(a, b)

        # DESVIO CONSCIENTE DO PLANO, registrado em VALIDATION.md (P10).
        #
        # O plano soma os cinco termos. A soma tem um defeito estrutural: dois
        # deles existem mesmo quando nada aconteceu. Todo primeiro encontro de
        # um par tem RE = 1.0, e a maioria dos primeiros encontros é banal —
        # duas pessoas se cruzam no café, nada muda, e a soma marca pressão
        # alta porque nunca tinham se cruzado.
        #
        # Substância é o que de fato mudou neste evento: crença e objetivo.
        # Raridade, carga relacional e tensão não geram drama sozinhas — elas
        # amplificam. "Fazia meses que não se viam" só importa se algo acontece
        # no reencontro; tensão acumulada só vira pressão quando descarrega.
        # Plateia: um segredo revelado diante de cinco pessoas pesa mais que
        # diante de uma. O ledger já trata testemunha assim; o detector não
        # tratava, e por isso os picos caíam em salas vazias e cobriam pouco
        # elenco. Cena cheia é cena que importa.
        audience = max(0, len(set(present or [])) - 2)
        substance = (W_EPISTEMIC * _norm(dE, K_EPISTEMIC)
                     + W_CONFLICT * _norm(CO, K_CONFLICT))
        amplifier = (1.0 + W_RELATIONAL * _norm(CR, K_RELATIONAL)
                     + W_RARITY * RE + W_TENSION * _norm(TA, K_TENSION)
                     + W_AUDIENCE * _norm(audience, K_AUDIENCE))
        raw = substance * amplifier
        value = 1.0 - math.exp(-raw)   # achata para 0..1

        event = PressureEvent(
            tick=tick, day=tick // self.ticks_per_day,
            agent_a=a, agent_b=b, location_id=location_id, channel=channel,
            value=value,
            parts={"dE": dE, "CO": CO, "CR": CR, "RE": RE, "TA": TA},
            # Um momento dramático não acontece entre duas pessoas isoladas:
            # acontece numa sala. Quem estava presente participou da cena, e é
            # por isso que sete picos podem envolver o elenco inteiro em vez de
            # exigirem setenta.
            participants=sorted(set(present or []) | {a, b}),
        )
        self.events.append(event)
        return event

    def flush(self, conn) -> None:
        conn.executemany(
            "INSERT INTO pressure_event (tick, day, agent_a, agent_b, location_id,"
            " channel, value, de, co, cr, re, ta, participants_json)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            [
                (e.tick, e.day, e.agent_a, e.agent_b, e.location_id, e.channel,
                 e.value, e.parts["dE"], e.parts["CO"], e.parts["CR"],
                 e.parts["RE"], e.parts["TA"], __import__("json").dumps(e.participants))
                for e in self.events
            ],
        )
        conn.commit()
