"""Objetivos — os 10 tipos fixados na Fase 0.

Cada tipo tem condição de satisfação verificável em código. Não há semântica
aqui: um objetivo é satisfeito, bloqueado ou não conforme o estado do ledger,
sem ninguém interpretar nada.

Objetivos existem por duas razões. Primeiro, dar `leverage` aos fatos: um fato
do qual muitos objetivos dependem vale mais quando a confiança nele muda — é
isso que faz o detector de pressão distinguir uma fofoca qualquer de uma
revelação. Segundo, produzir conflito: dois objetivos que não podem ser
satisfeitos ao mesmo tempo são a definição operacional de drama.
"""

from __future__ import annotations

import json
import sqlite3

# Pares de tipos que não podem ser satisfeitos ao mesmo tempo sobre o mesmo
# alvo. É a tabela de conflito — a única fonte de `goal_conflict`.
CONFLICTING = {
    frozenset({"ocultar_anomalia", "expor_verdade"}),
    frozenset({"ocultar_anomalia", "obter_informacao"}),
    frozenset({"proteger_pessoa", "remover_obstaculo"}),
    frozenset({"proteger_pessoa", "vingar"}),
    frozenset({"estabelecer_identidade", "expor_verdade"}),
    frozenset({"elevar_status", "remover_obstaculo"}),
}


# Tipos que alguém pode atrapalhar. Só estes viram pressão de conflito.
CONTESTABLE = {t for par in CONFLICTING for t in par}


def instantiate(conn: sqlite3.Connection, agents: dict, facts: dict,
                ledger=None) -> list[dict]:
    """Dá a cada agente os objetivos que a situação dele implica.

    Nada aqui é escolha de personalidade — é consequência da posição. Quem tem
    anomalia precisa ocultá-la; quem chegou de fora precisa entender o mundo;
    quem existe para publicar identidades quer expor.
    """
    goals: list[dict] = []

    def add(agent_id, gtype, target, priority, depends=()):
        goals.append({
            "agent_id": agent_id, "type": gtype, "target_id": target,
            "priority": priority, "status": "ativo",
            "depends_on_facts": list(depends),
        })

    # Fatos que revelam alguém: base de ocultar / expor.
    exposing = {}
    for fid, f in facts.items():
        if f["predicate"] in ("usou_anomalia", "é_de_origem", "mentiu_sobre"):
            exposing.setdefault(f["subject"], []).append(fid)

    def knows(agent_id: str, fact_id: int) -> bool:
        """REGRA CENTRAL: objetivo se apoia em CRENÇA, nunca na verdade.

        Um agente não pode querer expor o que não detectou, nem proteger o que
        não sabe que existe. Construir objetivo lendo `fact` seria dar ao agente
        acesso à verdade pelas costas — exatamente o que a Fase 2 proíbe.
        """
        if ledger is None:
            return True
        return (agent_id, fact_id) in ledger.beliefs

    for agent_id, agent in agents.items():
        deslocado = agent.origin != "nativo"
        segredos = exposing.get(agent_id, [])

        if agent.anomaly and agent.embodied:
            add(agent_id, "ocultar_anomalia", None, 0.9, segredos)
        if segredos and not agent.anomaly:
            add(agent_id, "ocultar_anomalia", None, 0.7, segredos)

        if deslocado and agent.embodied:
            add(agent_id, "compreender_mundo", None, 0.75)
            add(agent_id, "estabelecer_identidade", None, 0.6)
            # Quase nunca satisfazível — fonte permanente de tensão, por projeto.
            add(agent_id, "retornar_origem", None, 0.5)

        if not agent.embodied:
            # A compulsão, limitada ao que ela de fato detectou.
            for subject, fids in exposing.items():
                detected = [f for f in fids if knows(agent_id, f)]
                if detected:
                    add(agent_id, "expor_verdade", subject, 0.95, detected)
            continue

        if not deslocado:
            add(agent_id, "adquirir_recurso", None, 0.55)
            add(agent_id, "elevar_status", None, 0.4)

        add(agent_id, "formar_vinculo", None, 0.45)

        # Proteger nasce do vínculo, não do nada.
        if ledger is not None:
            for (a, b), rel in ledger.relations.items():
                if agent_id in (a, b) and rel.get("bonded"):
                    outro = b if a == agent_id else a
                    add(agent_id, "proteger_pessoa", outro, 0.8)

    conn.execute("DELETE FROM goal")
    conn.executemany(
        "INSERT INTO goal (agent_id, type, target_id, priority, status,"
        " depends_on_facts_json) VALUES (?, ?, ?, ?, ?, ?)",
        [(g["agent_id"], g["type"], g["target_id"], g["priority"], g["status"],
          json.dumps(g["depends_on_facts"])) for g in goals],
    )
    conn.commit()

    for row, goal in zip(conn.execute("SELECT id FROM goal ORDER BY id"), goals):
        goal["id"] = row["id"]
    return goals


def leverage(goals: list[dict], relations: dict) -> dict[int, float]:
    """Quantos objetivos e relações dependem de cada fato.

    Grau de saída no grafo. Nenhuma semântica envolvida — é contagem. Um fato
    do qual três objetivos dependem move três vezes mais o mundo quando a
    confiança nele muda.
    """
    lev: dict[int, float] = {}
    for goal in goals:
        weight = goal["priority"]
        for fid in goal["depends_on_facts"]:
            lev[fid] = lev.get(fid, 0.0) + weight
    return lev


def conflict_score(goals_a: list[dict], goals_b: list[dict],
                   a_id: str, b_id: str) -> float:
    """Quanto os objetivos destes dois se atropelam.

    Conta pares de tipos conflitantes, ponderados pela prioridade dos dois
    lados. Objetivo direcionado ao outro (`target_id`) pesa mais: é conflito
    pessoal, não estrutural.
    """
    total = 0.0
    for ga in goals_a:
        for gb in goals_b:
            if frozenset({ga["type"], gb["type"]}) not in CONFLICTING:
                continue
            weight = ga["priority"] * gb["priority"]
            if ga.get("target_id") == b_id or gb.get("target_id") == a_id:
                weight *= 2.0
            # Conflito só é real se disputam o mesmo fato, ou se um deles mira
            # diretamente o outro.
            shared = set(ga["depends_on_facts"]) & set(gb["depends_on_facts"])
            if shared or ga.get("target_id") == b_id or gb.get("target_id") == a_id:
                total += weight
    return total


# ===========================================================================
# Avaliação de progresso — o que torna o conflito dinâmico
# ===========================================================================

def progress(goal: dict, ledger, agents: dict) -> float:
    """Quão perto este objetivo está de ser satisfeito, 0..1.

    Sem semântica: é leitura de estado do ledger. O valor importa menos que a
    variação dele — é a MUDANÇA de progresso que gera pressão. Dois inimigos
    que se cruzam sem nada mudar não são um evento; são duas pessoas passando
    uma pela outra.
    """
    gtype = goal["type"]
    deps = goal["depends_on_facts"]

    if gtype == "ocultar_anomalia":
        # Erode conforme gente comum passa a crer na versão FIEL. A crença
        # distorcida não ameaça: é justamente o disfarce funcionando.
        worst = 0.0
        for fid in deps:
            for (agent_id, f), belief in ledger.beliefs.items():
                if f != fid or agent_id == goal["agent_id"]:
                    continue
                if belief["distortion"] == 0:
                    worst = max(worst, belief["confidence"])
        return 1.0 - worst

    if gtype == "expor_verdade":
        # Avança conforme a verdade fiel se espalha.
        faithful = 0
        total = max(1, len(agents))
        for fid in deps:
            for (_, f), belief in ledger.beliefs.items():
                if f == fid and belief["distortion"] == 0 and belief["confidence"] > 0.5:
                    faithful += 1
        return min(1.0, faithful / total)

    if gtype == "formar_vinculo":
        best = 0.0
        for (a, b), rel in ledger.relations.items():
            if goal["agent_id"] not in (a, b):
                continue
            best = max(best, (max(0.0, rel["affect"]) + rel["trust"]) / 2.0)
        return best

    if gtype == "adquirir_recurso":
        return min(1.0, ledger.resources.get(goal["agent_id"], 0.0) / 100.0)

    if gtype == "elevar_status":
        # Reputação = quantos confiam nele. Não é cargo; é quantas portas abrem.
        trusted = sum(
            1 for (a, b), rel in ledger.relations.items()
            if goal["agent_id"] in (a, b) and rel["trust"] > 0.5
        )
        return min(1.0, trusted / 6.0)

    if gtype == "proteger_pessoa":
        # Erode quando o protegido se machuca ou entra em conflito.
        alvo = goal.get("target_id")
        if not alvo:
            return 1.0
        danos = sum(
            1 for f in ledger.facts.values()
            if f["predicate"] in ("brigou_com", "feriu", "matou")
            and alvo in (f["subject"], f["object"])
        )
        return max(0.0, 1.0 - danos * 0.25)

    if gtype == "estabelecer_identidade":
        for f in ledger.facts.values():
            if f["subject"] == goal["agent_id"] and f["predicate"] == "possui_documento":
                return 1.0
        return min(0.9, ledger.paperwork.get(goal["agent_id"], 0) / 8.0)

    if gtype == "compreender_mundo":
        knowing = getattr(ledger, "knowing", None)
        return knowing.world_grasp(goal["agent_id"]) if knowing else 0.0

    if gtype == "remover_obstaculo":
        return 0.0

    if gtype == "retornar_origem":
        return 0.0   # por projeto, quase nunca satisfazível

    return 0.0


class GoalTracker:
    """Guarda o progresso anterior para poder medir a variação."""

    def __init__(self, goals: list[dict], agents: dict) -> None:
        self.goals = goals
        self.agents = agents
        self.by_agent: dict[str, list[dict]] = {}
        for goal in goals:
            self.by_agent.setdefault(goal["agent_id"], []).append(goal)
        self._last: dict[int, float] = {}

    def delta_for(self, agent_ids, ledger) -> float:
        """Mudança de progresso em objetivos DISPUTÁVEIS.

        O plano chama isto de 'objetivos bloqueados/avançados'. A palavra que
        importa é *bloqueado*: pressão vem de objetivo que alguém pode
        atrapalhar. Aprender o que é um ônibus move `compreender_mundo`, mas
        ninguém se opõe a isso — é cotidiano, não drama, e contá-lo como
        conflito fazia o mundo alternar entre "todos aprendendo" (pressão em
        todo lugar) e "todos já sabem" (pressão nenhuma), sem meio-termo.

        Objetivo que não aparece em CONFLICTING continua real e continua
        governando comportamento; só não gera pressão de conflito.
        """
        total = 0.0
        for agent_id in agent_ids:
            for goal in self.by_agent.get(agent_id, []):
                gid = id(goal)
                now = progress(goal, ledger, self.agents)
                before = self._last.get(gid)
                if (before is not None and abs(now - before) > 1e-9
                        and goal["type"] in CONTESTABLE):
                    total += abs(now - before) * goal["priority"]
                self._last[gid] = now
        return total
