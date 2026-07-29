"""Chegada de personagens — a obra vira gente. Ainda zero LLM.

Este é o ponto onde o Kestlerium deixa de ser um mundo com moradores e passa a
ser um hub das obras: **toda obra nova que entrar no repositório pode virar um
personagem vivo aqui.** A chegada é contínua — um de cada vez, no tick em que
foi declarada — e não um elenco despejado de uma vez.

Três regras, e nenhuma é detalhe de implementação:

**Só o front matter é lido. O corpo da obra, nunca.** Um personagem sabe apenas
o que viveu dentro da história dele; a obra inteira é conhecimento do autor, não
da criatura. Se este módulo lesse o texto para "enriquecer" o personagem, ele
saberia o próprio final — e a distinção que sustenta o projeto acabaria numa
conveniência. O autor declara o que o personagem sabe; o motor não adivinha.

**O arquivo da obra nunca é alterado.** Este módulo só lê. Os `.md` são do
autor, ficam onde estão e do jeito que estão.

**Entidades não chegam.** Suomynona e The Continuity não são personagens do
mesmo jeito que Severin ou James Revex: não têm corpo, não dormem, e não
*chegam* — se manifestam onde há substrato. Uma declaração `tipo: entidade` é
recusada com essa explicação, em vez de virar um morador com pernas.

O bloco declarado numa obra:

    ---
    title: "One Blood"
    kestlerium:
      - id: severin
        nome: "Severin Sângelună"
        constituicao: "Nascido duas vezes. Não pergunta o que é permitido."
        casa: pensao
        trabalho: bar
        traz: [sangue, noite, juramento]
    ---

`traz` é o que ele traz de casa, e é a única coisa que ele já entende ao
chegar. Tudo o mais deste mundo — dinheiro, ônibus, turno de trabalho — ele
aprende com quem já mora aqui, ou não aprende.
"""

from __future__ import annotations

import json
import pathlib
import sqlite3

from . import clock as clockmod

# Rotina de quem acabou de chegar sem entender nada. Curta de propósito: ele
# ainda não tem emprego, não sabe o que é um turno, e o mundo é que vai
# ensinar. Faixas [inicio, fim, local, atividade] em ticks do dia.
ROTINA_RECEM_CHEGADO = [
    [0, 14, "__casa__", "dormir"],
    [15, 23, "__casa__", "descansar"],
    [24, 33, "__praca__", "andar"],
    [34, 41, "__trabalho__", "trabalhar"],
    [42, 47, "__casa__", "casa"],
]


class DeclaracaoInvalida(Exception):
    """A declaração não fecha. Sempre diz o quê, para o autor poder corrigir."""


def front_matter(texto: str) -> dict:
    """Lê o bloco entre as duas linhas de `---`, e só ele.

    Não é um parser de YAML completo, e não finge ser: aceita `chave: valor`,
    listas com `- ` e listas em linha `[a, b]`, que é a forma documentada do
    bloco `kestlerium`. Uma construção fora disso é recusada com o número da
    linha, e não interpretada por adivinhação — adivinhar aqui produziria um
    personagem sutilmente errado, que é pior que um erro na cara.
    """
    linhas = texto.splitlines()
    if not linhas or linhas[0].strip() != "---":
        return {}
    try:
        fim = next(i for i in range(1, len(linhas)) if linhas[i].strip() == "---")
    except StopIteration:
        return {}

    raiz: dict = {}
    pilha_item: dict | None = None
    chave_lista: str | None = None

    for n in range(1, fim):
        linha = linhas[n]
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        recuo = len(linha) - len(linha.lstrip())
        corpo = linha.strip()

        if recuo == 0:
            pilha_item = None
            chave_lista = None
            if ":" not in corpo:
                continue
            chave, _, valor = corpo.partition(":")
            valor = valor.strip()
            if valor == "":
                raiz[chave.strip()] = []
                chave_lista = chave.strip()
            else:
                raiz[chave.strip()] = _escalar(valor)
            continue

        if chave_lista is None:
            continue

        if corpo.startswith("- "):
            pilha_item = {}
            raiz[chave_lista].append(pilha_item)
            corpo = corpo[2:].strip()
            if not corpo:
                continue

        if pilha_item is None or ":" not in corpo:
            continue
        chave, _, valor = corpo.partition(":")
        pilha_item[chave.strip()] = _escalar(valor.strip())

    return raiz


def _escalar(valor: str):
    valor = valor.strip()
    if valor.startswith("[") and valor.endswith("]"):
        dentro = valor[1:-1].strip()
        return [_escalar(p) for p in dentro.split(",")] if dentro else []
    if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
        return valor[1:-1]
    if valor.lower() in ("true", "false"):
        return valor.lower() == "true"
    return valor


def declaracoes(raiz: pathlib.Path) -> list[dict]:
    """Varre as obras na raiz do repositório e devolve o que foi declarado.

    Só a raiz, como no site: subpasta é privada. E só o front matter — o corpo
    da obra não é aberto em momento nenhum.
    """
    achadas = []
    for caminho in sorted(raiz.glob("*.md")):
        try:
            texto = caminho.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        fm = front_matter(texto)
        for bruto in fm.get("kestlerium") or []:
            if not isinstance(bruto, dict):
                continue
            bruto = dict(bruto)
            bruto["_obra"] = fm.get("title") or caminho.stem
            bruto["_arquivo"] = caminho.name
            achadas.append(bruto)
    return achadas


def validar(d: dict, locais: set) -> dict:
    """Recusa cedo e com motivo. Um personagem malformado é pior que nenhum."""
    for campo in ("id", "nome", "constituicao"):
        if not d.get(campo):
            raise DeclaracaoInvalida(
                f"{d.get('_arquivo', '?')}: falta '{campo}'")

    if str(d.get("tipo", "personagem")).lower() == "entidade":
        raise DeclaracaoInvalida(
            f"{d['_arquivo']}: '{d['id']}' foi declarado como entidade. "
            "Entidades não chegam — se manifestam onde há substrato, e ainda "
            "não têm desenho próprio. Só personagens encarnados entram por aqui.")

    for campo in ("casa", "trabalho"):
        alvo = d.get(campo)
        if alvo and alvo not in locais:
            raise DeclaracaoInvalida(
                f"{d['_arquivo']}: '{d['id']}' aponta para o local '{alvo}',"
                f" que não existe neste mundo.")

    traz = d.get("traz") or []
    if isinstance(traz, str):
        traz = [t.strip() for t in traz.split(",") if t.strip()]
    d["traz"] = [str(t) for t in traz]
    return d


def chegar(conn: sqlite3.Connection, d: dict, tick: int,
           casa_padrao: str, trabalho_padrao: str) -> bool:
    """Insere o personagem no mundo. Devolve False se ele já estava aqui.

    `arrival_tick` é o agora: antes dele o agente não existe no mundo, e é isso
    que faz a chegada ser contínua em vez de um elenco despejado de uma vez.
    """
    ja = conn.execute("SELECT 1 FROM agent WHERE id = ?", (d["id"],)).fetchone()
    if ja:
        return False

    casa = d.get("casa") or casa_padrao
    trabalho = d.get("trabalho") or trabalho_padrao

    conn.execute(
        "INSERT INTO agent (id, name, origin, kind, arrival_tick,"
        " home_location_id, constitution_json) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (d["id"], d["nome"], d["_obra"], "encarnado", tick, casa,
         json.dumps(d["constituicao"], ensure_ascii=False)))

    for inicio, fim, alvo, atividade in ROTINA_RECEM_CHEGADO:
        local = {"__casa__": casa, "__trabalho__": trabalho,
                 "__praca__": trabalho}.get(alvo, alvo)
        conn.execute(
            "INSERT INTO routine (agent_id, start_tod, end_tod, location_id,"
            " activity) VALUES (?, ?, ?, ?, ?)",
            (d["id"], inicio, fim, local, atividade))

    # O que ele traz de casa: domínio pleno, sem professor. É tudo o que ele
    # entende ao chegar — o resto deste mundo ele aprende aqui, ou não aprende.
    for conceito in d["traz"]:
        conn.execute(
            "INSERT OR IGNORE INTO knowledge (agent_id, concept, grasp,"
            " learned_tick, taught_by) VALUES (?, ?, 1.0, ?, NULL)",
            (d["id"], conceito, tick))

    conn.commit()
    return True


def relatorio(entradas: list, recusas: list, tick: int) -> str:
    linhas = [f"Chegadas em {clockmod.label(tick)}:"]
    if not entradas and not recusas:
        linhas.append("  Nenhuma obra declara personagem ainda.")
    for d in entradas:
        traz = ", ".join(d["traz"]) or "nada"
        linhas.append(f"  + {d['nome']} ({d['_obra']}) — traz: {traz}")
    for motivo in recusas:
        linhas.append(f"  ! {motivo}")
    return "\n".join(linhas)
