"""Ancoragem de citações: a citação existe mesmo no texto?

O documento de design pede "Verifique: a citação sustenta o fato extraído?" mas
nunca checa se a citação sequer EXISTE. Um modelo de linguagem inventa citações
e números de linha com a mesma fluência com que acerta — e um fato ancorado numa
citação inventada é exatamente o "erro com cara de certeza" da seção 2.

Por isso esta checagem é mecânica e vem antes de tudo:

- a citação precisa aparecer literalmente na unidade (após normalizar espaços,
  aspas tipográficas, travessões e marcação Markdown);
- trechos pulados só com " ... ", e os pedaços precisam aparecer em ordem;
- a localização (linhas) é CALCULADA aqui, nunca aceita do extrator.

Um fato cuja citação não é encontrada é rejeitado e contado. A taxa de rejeição
é, ela mesma, uma medida de quanto o extrator alucina.
"""

from __future__ import annotations

import re

MIN_CARACTERES = 12   # "1961" ancora em qualquer lugar e não prova nada

_TROCAS = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
    "–": "-", "—": "-", "‒": "-", "−": "-",
    "…": "...", " ": " ",
}
_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_ELIPSE = re.compile(r"\s*(?:\.\.\.|…|\[\.\.\.\]|\(\.\.\.\))\s*")


def _normalizar_caractere(c: str) -> str:
    return _TROCAS.get(c, c)


def _mapa_normalizado(texto: str, linha_base: int = 1) -> tuple[str, list[int]]:
    """Texto normalizado + a linha de origem de cada caractere normalizado."""
    texto = _LINK.sub(r"\1", texto)
    saida: list[str] = []
    linhas: list[int] = []
    linha = linha_base
    em_espaco = True
    for c in texto:
        if c == "\n":
            linha += 1
        c = _normalizar_caractere(c)
        # Marcação Markdown não é texto, e aspas o extrator costuma omitir ou
        # trocar: somem dos dois lados da comparação.
        if c in "*`|#>":
            c = " "
        elif c in "\"'":
            continue
        for ch in c:
            if ch.isspace():
                if not em_espaco:
                    saida.append(" ")
                    linhas.append(linha)
                em_espaco = True
            else:
                # casefold pode virar mais de um caractere ("ß" → "ss"): cada
                # um carrega a linha, para o mapa continuar alinhado.
                for x in ch.casefold():
                    saida.append(x)
                    linhas.append(linha)
                em_espaco = False
    while saida and saida[-1] == " ":
        saida.pop()
        linhas.pop()
    return "".join(saida), linhas


def normalizar(texto: str) -> str:
    return _mapa_normalizado(texto)[0]


def ancorar(citacao: str, texto_unidade: str, linha_base: int = 1) -> dict:
    """Procura a citação na unidade.

    Devolve {ok, linha_inicio, linha_fim, motivo, ocorrencias}.
    """
    if not citacao or not str(citacao).strip():
        return {"ok": False, "motivo": "citação vazia"}
    citacao = str(citacao).strip().strip('"').strip("'").strip()

    pedacos = [p for p in _ELIPSE.split(citacao) if p.strip()]
    pedacos_norm = [normalizar(p).strip(" .,;:") for p in pedacos]
    pedacos_norm = [p for p in pedacos_norm if p]
    if not pedacos_norm:
        return {"ok": False, "motivo": "citação só com reticências"}
    if sum(len(p) for p in pedacos_norm) < MIN_CARACTERES:
        return {"ok": False, "motivo": f"citação curta demais (mínimo {MIN_CARACTERES} caracteres)"}

    alvo, mapa = _mapa_normalizado(texto_unidade, linha_base)
    posicao = 0
    inicio_primeiro = None
    fim_ultimo = None
    for p in pedacos_norm:
        achado = alvo.find(p, posicao)
        if achado < 0:
            motivo = "citação não encontrada no texto" if inicio_primeiro is None \
                else f"trecho depois das reticências não encontrado: {p[:60]!r}"
            return {"ok": False, "motivo": motivo}
        if inicio_primeiro is None:
            inicio_primeiro = achado
        fim_ultimo = achado + len(p) - 1
        posicao = achado + len(p)

    ocorrencias = alvo.count(pedacos_norm[0])
    return {
        "ok": True,
        "linha_inicio": mapa[inicio_primeiro],
        "linha_fim": mapa[fim_ultimo],
        "ocorrencias": ocorrencias,
        "motivo": None,
    }


def sobrepoe(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] <= b[1] and b[0] <= a[1]
