"""O cronista — Fase 8. Ainda zero LLM.

Todas as fases anteriores produzem números. Esta produz a única coisa que um
humano de fato consome: **texto legível**.

O objeto central é o **fio**. Até aqui o mundo produzia momentos soltos — um
pico na terça, outro no mês seguinte, sem nada dizendo que são a mesma história.
O fio é o que amarra: nasce num fato, atravessa os momentos que mexeram naquele
fato, e termina quando o assunto se resolve ou esfria.

Duas decisões de projeto merecem registro:

**O fio é tabela, não consulta.** `agent_state` e `pressure_event` são podados a
cada publicação para o banco caber no repositório. O que o mundo já contou não
pode depender de dados que serão apagados amanhã — memória e rastro são coisas
diferentes.

**A prosa sai do estado, sem modelo nenhum.** Não é literatura, e não tenta ser:
é um relatório em português que diz o que aconteceu, quem viu, e — a parte que
interessa — *em que versão do fato cada um acredita*. Quando a Fase 5 trouxer um
modelo aberto, ele substitui a camada de frase e encontra os fios já prontos.
Construir o fio depois do modelo seria construir na ordem errada: o modelo
escreve melhor, mas não sabe o que é uma história continuada.

O cronista é o único lugar do motor que pode ler `fact` diretamente. Ele não é
um agente: é o autor olhando de fora. A regra inviolável — nenhum *agente* lê
`fact` — continua valendo, e por isso todo texto que descreve o que alguém acha
passa por `belief`, nunca pela verdade.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field

from . import clock as clockmod

# Quantos dias sem nenhum momento agendado até um fio ser dado por adormecido.
SLEEP_DAYS = 30

# Como cada predicado vira frase. O objeto entra cru quando não há forma
# melhor: inventar detalhe que o mundo não tem seria mentira, não estilo.
FRASE = {
    "deve_a": "{s} deve a {o}.",
    "prometeu_a": "{s} fez uma promessa a {o}.",
    "mentiu_sobre": "{s} mentiu sobre {o}.",
    "teme": "{s} teme {o}.",
    "ama": "{s} ama {o}.",
    "usou_anomalia": "{s} usou o que trouxe de casa: {o}.",
    "é_de_origem": "{s} não é daqui — veio de {o}.",
    "trabalha_para": "{s} passou a trabalhar em {o}.",
    "possui_documento": "{s} finalmente tem {o}.",
}

VISIBILIDADE = {
    "publico": "à vista de todos",
    "privado": "sem alarde",
    "oculto": "e ninguém deveria ter visto",
}


@dataclass
class Thread:
    root_fact_id: int
    title: str
    opened_day: int
    last_day: int
    status: str
    entries: list = field(default_factory=list)


class Chronicler:
    """Lê o mundo já simulado e devolve fios com texto."""

    def __init__(self, conn: sqlite3.Connection, world_name: str) -> None:
        self.conn = conn
        self.world = world_name
        self.agents = {r["id"]: dict(r) for r in conn.execute("SELECT * FROM agent")}
        self.facts = {r["id"]: dict(r) for r in conn.execute("SELECT * FROM fact")}
        self.locations = {r["id"]: dict(r) for r in
                          conn.execute("SELECT * FROM location")}

    # -- vocabulário --------------------------------------------------------

    def nome(self, agent_id: str) -> str:
        a = self.agents.get(agent_id)
        return a["name"] if a else agent_id

    def _termo(self, valor) -> str:
        """Um objeto de fato pode ser outra pessoa, um lugar ou um rótulo."""
        if valor is None:
            return "algo que não ficou claro"
        if valor in self.agents:
            return self.nome(valor)
        if valor in self.locations:
            return self.locations[valor]["name"]
        return str(valor).replace("_", " ")

    def frase_do_fato(self, fact: dict) -> str:
        modelo = FRASE.get(fact["predicate"])
        if modelo is None:
            return (f"{self.nome(fact['subject'])} — {fact['predicate']}"
                    f" {self._termo(fact['object'])}.")
        return modelo.format(s=self.nome(fact["subject"]),
                             o=self._termo(fact["object"]))

    # -- o que se acredita --------------------------------------------------

    def crencas(self, fact_id: int) -> list[dict]:
        return [dict(r) for r in self.conn.execute(
            "SELECT * FROM belief WHERE fact_id = ? ORDER BY acquired_tick",
            (fact_id,))]

    def quantos_sabiam(self, fact_id: int, tick: int) -> str:
        """Quantos já sabiam disto NAQUELE dia.

        Só `acquired_tick` é histórico: uma crença, uma vez adquirida, não
        desadquire. `confidence` e `distortion` são valores CORRENTES — a
        racionalização se corrói com testemunho repetido, a confiança decai —
        e a tabela guarda um estado, não uma série temporal.

        Escrever "8 delas numa versão errada" num dia de dois meses atrás seria
        inventar passado a partir do presente. Então a entrada do meio diz só o
        que é datável, e o retrato completo — quem acredita em quê, hoje —
        aparece uma vez por fio, marcado como hoje.
        """
        sabiam = [b for b in self.crencas(fact_id) if b["acquired_tick"] <= tick]
        if not sabiam:
            return "Ninguém sabia disso ainda."
        de_ouvir = sum(1 for b in sabiam if b["source_agent_id"])
        plural = "s" if len(sabiam) > 1 else ""
        frase = (f"Nesse dia {len(sabiam)} pessoa{plural} já sabia{plural and 'm'}"
                 f" de alguma versão disto")
        if de_ouvir:
            frase += f", {de_ouvir} por ter ouvido de outra pessoa"
        return frase + "."

    def _estado_das_cabecas(self, fact_id: int) -> str:
        """A parte que só este projeto pode escrever — o retrato de hoje.

        Um resumo comum diria o que aconteceu. Aqui interessa o desencontro:
        quantos sabem, quantos sabem torto, e com que firmeza — que é a única
        coisa que a separação entre verdade e crença existe para produzir.
        """
        bs = self.crencas(fact_id)
        if not bs:
            return "Ninguém sabe disso."
        tortos = [b for b in bs if b["distortion"]]
        conf = sum(b["confidence"] for b in bs) / len(bs)
        partes = [f"{len(bs)} pessoa{'s' if len(bs) > 1 else ''} sabe"
                  f"{'m' if len(bs) > 1 else ''} de alguma versão disto"
                  f" (confiança média {conf:.2f})"]
        if tortos:
            versoes = sorted({self._termo(b["distorted_object"]) for b in tortos})
            partes.append(f"{len(tortos)} dela{'s' if len(tortos) > 1 else ''}"
                          f" numa versão errada: {', '.join(versoes)}")
        de_ouvir = [b for b in bs if b["source_agent_id"]]
        if de_ouvir:
            partes.append(f"{len(de_ouvir)} por ter ouvido de outra pessoa")
        return "; ".join(partes) + "."

    # -- construção dos fios ------------------------------------------------

    def build(self, until_day: int | None = None) -> list[Thread]:
        agendados = [dict(r) for r in self.conn.execute(
            "SELECT * FROM scheduled ORDER BY day, id")]
        if until_day is None:
            until_day = max((s["day"] for s in agendados), default=0)

        por_fato: dict[int, list[dict]] = {}
        self.sem_fio = 0
        for s in agendados:
            fatos = json.loads(s["facts_json"] or "[]")
            if not fatos:
                # Momento movido por objetivo, não por informação. Não pertence
                # a fio nenhum, e forçá-lo a um seria inventar continuidade.
                self.sem_fio += 1
                continue
            for fid in fatos:
                por_fato.setdefault(fid, []).append(s)

        fios: list[Thread] = []
        for fid, momentos in sorted(por_fato.items()):
            fato = self.facts.get(fid)
            if fato is None:
                continue
            abertura = fato["tick"] // clockmod.TICKS_PER_DAY
            ultimo = max(m["day"] for m in momentos)

            fio = Thread(
                root_fact_id=fid,
                title=self.frase_do_fato(fato).rstrip("."),
                opened_day=abertura,
                last_day=ultimo,
                status=self._status(fid, ultimo, until_day),
            )

            fio.entries.append({
                "day": abertura, "tick": fato["tick"], "kind": "abertura",
                "participants": json.loads(fato["witnesses_json"]),
                "pressure": 0.0,
                "text": (f"{self.frase_do_fato(fato)} Aconteceu"
                         f" {VISIBILIDADE.get(fato['visibility'], '')}."),
            })

            for m in momentos:
                quem = json.loads(m["participants_json"])
                nomes = ", ".join(sorted(self.nome(a) for a in quem))
                onde = "" if m["kind"] == "beat" else " Foi diante de todos."
                fio.entries.append({
                    "day": m["day"], "tick": m["tick"], "kind": m["kind"],
                    "participants": quem, "pressure": m["pressure"],
                    "text": (f"O assunto voltou entre {nomes}."
                             f"{onde} {self.quantos_sabiam(fid, m['tick'])}"),
                })

            if fio.status != "aberto":
                # O fecho é o ÚLTIMO acontecimento do último dia, não o
                # primeiro. Ancorá-lo no início do dia fazia "o assunto se
                # encerrou" sair antes da conversa que o encerrou.
                fio.entries.append({
                    "day": ultimo,
                    "tick": max(m["tick"] for m in momentos) + 1,
                    "kind": "fecho", "participants": [], "pressure": 0.0,
                    "text": self._fecho(fid, fio.status),
                })

            fio.entries.sort(key=lambda e: (e["day"], e["tick"]))
            fios.append(fio)

        fios.sort(key=lambda f: (f.opened_day, f.root_fact_id))
        return fios

    def _status(self, fact_id: int, ultimo: int, hoje: int) -> str:
        """Resolvido, adormecido ou aberto — derivado, nunca declarado.

        Um fio se resolve quando nenhum objetivo que dependia daquele fato
        continua ativo: alguém conseguiu o que queria, ou desistiu. Se ainda há
        objetivo de pé e o assunto simplesmente parou de aparecer, ele não
        acabou — adormeceu, que é outra coisa e pode acordar.
        """
        vivos = 0
        for row in self.conn.execute("SELECT depends_on_facts_json, status FROM goal"):
            if fact_id in json.loads(row["depends_on_facts_json"] or "[]"):
                if row["status"] == "ativo":
                    vivos += 1
        if vivos == 0:
            return "resolvido"
        return "adormecido" if hoje - ultimo > SLEEP_DAYS else "aberto"

    def _fecho(self, fact_id: int, status: str) -> str:
        if status == "resolvido":
            return ("O assunto se encerrou: ninguém mais persegue nada que"
                    " dependa disto. " + self._estado_das_cabecas(fact_id))
        return ("O assunto parou de aparecer, mas não se resolveu — há quem"
                " ainda dependa dele. " + self._estado_das_cabecas(fact_id))

    # -- persistência -------------------------------------------------------

    def save(self, fios: list[Thread]) -> None:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM thread_entry")
        cur.execute("DELETE FROM thread")
        for fio in fios:
            cur.execute(
                "INSERT INTO thread (root_fact_id, title, opened_day, last_day,"
                " status) VALUES (?, ?, ?, ?, ?)",
                (fio.root_fact_id, fio.title, fio.opened_day, fio.last_day,
                 fio.status))
            tid = cur.lastrowid
            cur.executemany(
                "INSERT INTO thread_entry (thread_id, day, tick, kind,"
                " participants_json, pressure, text) VALUES (?, ?, ?, ?, ?, ?, ?)",
                [(tid, e["day"], e["tick"], e["kind"],
                  json.dumps(e["participants"]), e["pressure"], e["text"])
                 for e in fio.entries])
        self.conn.commit()

    # -- saída legível ------------------------------------------------------

    def markdown(self, fios: list[Thread], hoje: int) -> str:
        ordem = {"aberto": 0, "adormecido": 1, "resolvido": 2}
        linhas = [
            f"# Crônica de {self.world.capitalize()}",
            "",
            f"Dia {hoje} do mundo. {len(fios)} fio"
            f"{'s' if len(fios) != 1 else ''} de história"
            f" — {sum(1 for f in fios if f.status == 'aberto')} ainda de pé.",
            "",
            "Nada aqui foi escrito por um modelo de linguagem. Cada frase sai do",
            "estado do mundo: o que aconteceu, quem viu, e em que versão cada um",
            "acredita.",
            "",
        ]
        for fio in sorted(fios, key=lambda f: (ordem[f.status], f.opened_day)):
            linhas.append(f"## {fio.title}")
            linhas.append("")
            linhas.append(f"*Dia {fio.opened_day} — {fio.status}*")
            linhas.append("")
            # O retrato de hoje aparece uma vez, marcado como hoje. Repeti-lo
            # em cada entrada era o que fazia a crônica descrever o dia 32 com
            # o que só se soube no dia 90.
            linhas.append(f"**Hoje.** {self._estado_das_cabecas(fio.root_fact_id)}")
            linhas.append("")
            for e in fio.entries:
                linhas.append(f"**Dia {e['day']}.** {e['text']}")
                linhas.append("")
        if getattr(self, "sem_fio", 0):
            linhas.append("---")
            linhas.append("")
            linhas.append(
                f"Outros {self.sem_fio} momentos deste período não pertencem a"
                " fio nenhum: foram movidos por objetivo, não por informação."
                " Ficam registrados sem virar história.")
            linhas.append("")
        return "\n".join(linhas)
