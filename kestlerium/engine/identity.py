"""Deriva de identidade — Fase 7. Ainda zero LLM.

Duas coisas que um personagem tem, e que precisam ser separadas com força:

**A constituição é imutável.** É quem ele é: o texto que veio da obra. Nada no
mundo a reescreve — nem fofoca, nem tempo, nem o que ele aprendeu aqui. Se a
constituição pudesse mudar, "Severin" viraria um rótulo colado num estado
qualquer, e depois de seis meses de simulação não haveria como dizer se o
sujeito no bar ainda é o personagem que chegou.

**A trajetória é mutável.** É o que aconteceu com ele *aqui*: o que passou a
saber, no que passou a acreditar. Ela deriva, e deve derivar — um personagem
que atravessa meses sem mudar nada não está vivendo, está em exibição.

A regra que amarra as duas: **toda mudança cita a causa.** Uma crença nova cita
o `fact_id` que a originou; um conceito aprendido cita quem ensinou. Deriva sem
causa citada não é desenvolvimento — é o estado escorregando, e é assim que um
personagem vira outro sem ninguém conseguir apontar quando.

A medição é reconstruída do banco, não gravada durante a corrida, e isso é de
propósito: `acquired_tick` e `learned_tick` são históricos e imutáveis, então a
trajetória é derivável a qualquer momento e não pode divergir do que de fato
aconteceu. Confiança e distorção ficam de fora justamente por serem valores
correntes — usá-los descreveria o passado com o que só se soube depois.
"""

from __future__ import annotations

import hashlib
import sqlite3

from . import clock as clockmod

def assinatura(constitution_json: str) -> str:
    """A constituição é imutável; o hash é como se prova isso depois."""
    return hashlib.sha256(constitution_json.encode("utf-8")).hexdigest()[:16]


def trajetoria(conn: sqlite3.Connection, agent_id: str) -> list[dict]:
    """Cada passo que este agente deu, com a causa colada nele.

    Só dados históricos entram: `acquired_tick` de uma crença e `learned_tick`
    de um conceito nunca mudam depois de escritos. Por isso a trajetória
    reconstruída hoje é a mesma que seria reconstruída daqui a um ano.
    """
    passos: list[dict] = []

    for b in conn.execute(
            "SELECT fact_id, acquired_tick, source_agent_id FROM belief"
            " WHERE agent_id = ? ORDER BY acquired_tick", (agent_id,)):
        passos.append({
            "tick": b["acquired_tick"],
            "dia": b["acquired_tick"] // clockmod.TICKS_PER_DAY,
            "dimensao": "crenca",
            "causa": f"fato:{b['fact_id']}",
            "fonte": b["source_agent_id"] or "testemunhou",
        })

    for k in conn.execute(
            "SELECT concept, learned_tick, taught_by FROM knowledge"
            " WHERE agent_id = ? ORDER BY learned_tick", (agent_id,)):
        passos.append({
            "tick": k["learned_tick"],
            "dia": k["learned_tick"] // clockmod.TICKS_PER_DAY,
            "dimensao": "conhecimento",
            "causa": f"conceito:{k['concept']}",
            "fonte": k["taught_by"] or "trouxe de casa",
        })

    passos.sort(key=lambda p: (p["tick"], p["dimensao"], p["causa"]))
    return passos


def deriva(conn: sqlite3.Connection, agent_id: str, chegada: int) -> dict:
    """Quanto este agente se afastou de quem chegou.

    Não é uma nota de qualidade: é uma contagem de passos dados depois da
    chegada. O que veio de casa não conta — trazer o próprio mundo na cabeça
    não é ter mudado.
    """
    passos = [p for p in trajetoria(conn, agent_id) if p["tick"] > chegada]
    crencas = [p for p in passos if p["dimensao"] == "crenca"]
    conceitos = [p for p in passos if p["dimensao"] == "conhecimento"]
    sem_causa = [p for p in passos if not p["causa"]]
    ensinados = [p for p in conceitos if p["fonte"] != "trouxe de casa"]
    return {
        "passos": len(passos),
        "crencas": len(crencas),
        "conceitos": len(conceitos),
        "aprendeu_com_alguem": len(ensinados),
        "sem_causa": len(sem_causa),
        "primeiro_dia": min((p["dia"] for p in passos), default=None),
        "ultimo_dia": max((p["dia"] for p in passos), default=None),
    }


def gravar(conn: sqlite3.Connection) -> int:
    """Persiste a trajetória e a âncora de identidade de cada agente."""
    cur = conn.cursor()
    cur.execute("DELETE FROM trajectory")
    total = 0
    for a in conn.execute("SELECT id, constitution_json, arrival_tick FROM agent"):
        # IGNORE, jamais REPLACE. A âncora vale porque foi escrita UMA vez:
        # regravá-la a cada execução faria o portão comparar o valor com ele
        # mesmo e passar para sempre, inclusive depois de alguém ser reescrito.
        cur.execute(
            "INSERT OR IGNORE INTO identity_anchor (agent_id, constitution_hash,"
            " arrival_tick) VALUES (?, ?, ?)",
            (a["id"], assinatura(a["constitution_json"]), a["arrival_tick"]))
        passos = trajetoria(conn, a["id"])
        cur.executemany(
            "INSERT INTO trajectory (agent_id, tick, day, dimension, cause,"
            " source) VALUES (?, ?, ?, ?, ?, ?)",
            [(a["id"], p["tick"], p["dia"], p["dimensao"], p["causa"],
              p["fonte"]) for p in passos])
        total += len(passos)
    conn.commit()
    return total


def constituicoes_intactas(conn: sqlite3.Connection) -> list:
    """A prova de que ninguém foi reescrito.

    Vazia é o resultado esperado, e um resultado esperado que nunca poderia
    falhar seria inútil — por isso a âncora é gravada na primeira execução e
    conferida em todas as seguintes, e não recalculada na hora.
    """
    quebradas = []
    for row in conn.execute(
            "SELECT a.id, a.constitution_json, i.constitution_hash"
            " FROM agent a JOIN identity_anchor i ON i.agent_id = a.id"):
        if assinatura(row["constitution_json"]) != row["constitution_hash"]:
            quebradas.append(row["id"])
    return quebradas
