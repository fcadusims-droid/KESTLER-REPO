"""Referências sem definição, para bíblias (seção 4.3, "Lentes por tipo").

A lente "Informação não estabelecida", adaptada ao tipo `biblia`: um termo,
lugar ou facção citado num verbete e nunca definido em nenhum.

É método PRÓPRIO — não há fonte publicada que o sustente —, então a regra do
contrato vale: no máximo SUGGESTION (seção 6.4). A implementação é
determinística e não precisa de extração: procura termos cunhados (sequências
com maiúscula e siglas) e confere se cada um
aparece em algum lugar que DEFINE: um título, um termo em negrito (a convenção
de introduzir um termo), a primeira coluna de uma tabela, ou o canon.

Vai ter ruído — nomes do mundo real, por exemplo. O remédio é declarar em
`canon/entidades.yaml`, na lista `termos_conhecidos`, os termos que não precisam
de definição; ou suprimir o diagnóstico com um motivo.
"""

from __future__ import annotations

import re
from collections import defaultdict

from ..canon import Canon
from ..diagnostics import Diagnostico, Evidencia
from ..io import normalizar_nome
from ..segment import TITULO, Unidade

CONECTORES = {"of", "the", "and", "de", "da", "do", "das", "dos", "e", "von", "van", "del", "la", "le"}

# Palavras com maiúscula que não são termos cunhados.
COMUNS = set("""
a an the and or but if then when while with without within into onto from for of on in at by to as is are was
were be been being it its this that these those there here he she they we you i me my our your their his her
him them who whom whose what which where why how not no yes all any some each every one two three four five
six seven eight nine ten first second third last next new old part chapter section book volume act scene
note notes appendix index table figure fig see also ii iii iv v vi vii viii ix x xi xii xiii xiv xv xvi xvii
xviii xix xx january february march april may june july august september october november december monday
tuesday wednesday thursday friday saturday sunday o os as um uma uns umas e ou mas se entao quando com sem
para por pelo pela no na nos nas em ao aos do da dos das que quem qual onde como nao sim capitulo parte secao
mr mrs ms dr st
""".split())

TERMO_MULTI = re.compile(
    r"\b([A-ZÀ-Ý][\w'’-]+(?:\s+(?:(?:of|the|and|de|da|do|das|dos|e|von|van|del|la|le)\s+)?[A-ZÀ-Ý][\w'’-]+)+)")
SIGLA = re.compile(r"\b([A-Z]{2,6})\b")
NEGRITO = re.compile(r"\*\*([^*\n]{2,60})\*\*")
NEGRITO_ABRINDO = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)?\*\*([^*\n]{2,60})\*\*")
LINHA_TABELA = re.compile(r"^\s*\|\s*([^|]+?)\s*\|")
NUMERACAO = re.compile(r"^(?:[IVXLC]+|\d+(?:\.\d+)*|§\s*\d+)[.):]?\s+", re.I)


def _limpo(termo: str) -> str:
    termo = re.sub(r"[*_`]", "", termo).strip(" .,:;—–-")
    termo = re.sub(r"['’]s$", "", termo)          # possessivo: "Reiter's" é "Reiter"
    return NUMERACAO.sub("", termo).strip()


def definicoes(unidades: list[Unidade], canon: Canon) -> set[str]:
    """Todos os textos que definem alguma coisa, normalizados."""
    defs: set[str] = set()
    for u in unidades:
        for linha in u.linhas:
            m = TITULO.match(linha)
            if m:
                defs.add(normalizar_nome(_limpo(m.group(2))))
                continue
            # Termo em negrito é o autor dizendo "isto é um termo" — em bíblias,
            # a convenção é negritar o termo onde ele é introduzido e explicado.
            # Medido no piloto: 5 de 7 sugestões eram termos assim ("It reads
            # **structured signal**"). Negrito conta como definição.
            for m in NEGRITO.finditer(linha):
                defs.add(normalizar_nome(_limpo(m.group(1))))
            m = LINHA_TABELA.match(linha)
            if m and not re.match(r"^[-:\s]+$", m.group(1)):
                defs.add(normalizar_nome(_limpo(m.group(1))))
    for p in canon.pessoas.lista:
        defs.add(normalizar_nome(p.nome))
        defs |= {normalizar_nome(a) for a in p.aliases}
    for chave in canon.hierarquia.pais:
        defs.add(normalizar_nome(canon.hierarquia.nome(chave)))
    for lugar in canon.lugares.get("lugares") or []:
        if isinstance(lugar, dict) and lugar.get("nome"):
            defs.add(normalizar_nome(lugar["nome"]))
    for termo in canon.entidades.get("termos_conhecidos") or []:
        defs.add(normalizar_nome(termo))
    return {d for d in defs if d}


def _definido(termo_norm: str, defs: set[str]) -> bool:
    if termo_norm in defs:
        return True
    padrao = re.compile(r"(^|\W)" + re.escape(termo_norm) + r"($|\W)")
    return any(padrao.search(d) for d in defs)


def _candidatos(linha: str) -> list[str]:
    achados = []
    for m in TERMO_MULTI.finditer(linha):
        palavras = m.group(1).split()
        while palavras and normalizar_nome(palavras[0]) in COMUNS:
            palavras = palavras[1:]
        while palavras and normalizar_nome(palavras[-1]) in CONECTORES:
            palavras = palavras[:-1]
        if len([p for p in palavras if normalizar_nome(p) not in CONECTORES]) >= 2:
            achados.append(" ".join(palavras))
    for m in SIGLA.finditer(linha):
        if normalizar_nome(m.group(1)) not in COMUNS:
            achados.append(m.group(1))
    return [_limpo(a) for a in achados if _limpo(a)]


def _janela(linha: str, termo: str, folga: int = 70) -> str:
    """O termo com ~folga caracteres de cada lado, sem cortar palavra no meio."""
    pos = max(0, linha.find(termo))
    ini, fim = max(0, pos - folga), min(len(linha), pos + len(termo) + folga)
    if ini > 0:
        espaco = linha.find(" ", ini, pos)
        ini = espaco + 1 if espaco >= 0 else pos
    if fim < len(linha):
        espaco = linha.rfind(" ", pos + len(termo), fim)
        fim = espaco if espaco >= 0 else pos + len(termo)
    return linha[ini:fim].strip()


def verificar(unidades_por_doc: dict[str, list[Unidade]], canon: Canon,
              tipos_ativos: tuple[str, ...] = ("biblia",)) -> list[Diagnostico]:
    todas = [u for us in unidades_por_doc.values() for u in us]
    defs = definicoes(todas, canon)
    ocorrencias: dict[str, list[tuple[Unidade, int, str, str]]] = defaultdict(list)
    for u in todas:
        if u.tipo not in tipos_ativos:
            continue
        for i, linha in enumerate(u.linhas):
            if TITULO.match(linha):
                continue
            for termo in _candidatos(linha):
                norm = normalizar_nome(termo)
                if len(norm) < 3 or norm in COMUNS:
                    continue
                ocorrencias[norm].append((u, u.linha_inicio + i, linha, termo))

    saida = []
    for norm, lista in sorted(ocorrencias.items()):
        if _definido(norm, defs):
            continue
        evidencias = []
        for u, n, linha, termo in lista[:3]:
            trecho = _janela(linha, termo)
            evidencias.append(Evidencia(arquivo=u.arquivo, linha_inicio=n, linha_fim=n,
                                        citacao=trecho, unidade=u.id))
        exemplo = lista[0][3]
        saida.append(Diagnostico(
            prefixo="REF", nivel="SUGGESTION", verificador="referencia_sem_definicao",
            camada="semantica", metodo="proprio",
            titulo=f"'{exemplo}' é citado e nunca definido",
            regra="lente: informação não estabelecida, adaptada a bíblia (método próprio, seção 6.4)",
            evidencias=evidencias,
            conflito=(f"'{exemplo}' aparece {len(lista)} vez(es) e não há verbete, título, termo "
                      f"em negrito, primeira coluna de tabela ou item do canon que o defina."),
            acao="NOVO_CONTEUDO",
            pergunta="definir o termo num verbete, ou declará-lo em canon/entidades.yaml → termos_conhecidos?",
            notas=["método próprio (sem fonte publicada): limitado a SUGGESTION"],
            chave={"termo": norm},
        ))
    return saida
