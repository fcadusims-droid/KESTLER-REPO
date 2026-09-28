"""Unidades de análise e classificação do tipo de documento (seção 4.3).

A unidade muda com o tipo: cena na prosa, verbete na bíblia, entrada datada na
cronologia. O id de cada unidade vem do título dela, não da posição — inserir
uma seção nova no começo não pode mudar o id de todas as seguintes, senão cada
supressão e cada entrada de cache seriam invalidadas por uma edição que não
tocou nelas.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .io import sha, slug

TITULO = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
QUEBRA_CENA = re.compile(r"^\s*(\*\s*\*\s*\*|-{3,}|_{3,}|#{3,}\s*$)\s*$")
CABECALHO_ROTEIRO = re.compile(r"^\s*(INT\.|EXT\.|INT/EXT\.|I/E\.)\s", re.I)


@dataclass
class Unidade:
    id: str
    arquivo: str
    titulo: str
    linha_inicio: int          # 1-based, inclusivo, no arquivo real
    linha_fim: int
    linhas: list[str] = field(repr=False)
    tipo: str = "biblia"

    @property
    def texto(self) -> str:
        return "\n".join(self.linhas)

    @property
    def hash(self) -> str:
        # O tipo entra no hash: o mesmo texto extraído como bíblia ou como prosa
        # produz fatos diferentes.
        return sha(self.tipo + "\n" + self.texto, 24)


def fim_do_front_matter(linhas: list[str]) -> int:
    """Índice (0-based) da primeira linha depois do front matter YAML."""
    if linhas and linhas[0].strip() == "---":
        for i in range(1, len(linhas)):
            if linhas[i].strip() == "---":
                return i + 1
    return 0


def segmentar(arquivo: str, texto: str, tipo: str, nivel_max: int = 3) -> list[Unidade]:
    """Divide um documento em unidades conforme o tipo.

    Bíblia, ficha e cronologia: por título até `nivel_max` (verbete ou seção).
    Prosa e ramificado: por título e por quebra de cena (`---`, `* * *`).
    Roteiro: por cabeçalho de cena (INT./EXT.) e por título.
    """
    linhas = texto.split("\n")
    inicio = fim_do_front_matter(linhas)
    base = slug(arquivo.rsplit("/", 1)[-1].removesuffix(".md"))

    cortes: list[tuple[int, str]] = []   # (índice 0-based, título)
    for i in range(inicio, len(linhas)):
        linha = linhas[i]
        m = TITULO.match(linha)
        if m and len(m.group(1)) <= nivel_max:
            cortes.append((i, m.group(2).strip() or f"secao-{i + 1}"))
            continue
        if tipo in ("prosa", "ramificado") and QUEBRA_CENA.match(linha):
            cortes.append((i, ""))
            continue
        if tipo == "roteiro" and CABECALHO_ROTEIRO.match(linha):
            cortes.append((i, linha.strip()))

    if not cortes or cortes[0][0] > inicio:
        cortes.insert(0, (inicio, "preambulo"))

    unidades: list[Unidade] = []
    vistos: dict[str, int] = {}
    ultimo_titulo = "preambulo"
    for n, (i, titulo) in enumerate(cortes):
        fim = cortes[n + 1][0] if n + 1 < len(cortes) else len(linhas)
        bloco = linhas[i:fim]
        if not any(l.strip() for l in bloco):
            continue
        # Uma quebra de cena sem título herda o título anterior, numerada.
        if titulo:
            ultimo_titulo = titulo
            chave = slug(titulo)
        else:
            chave = slug(ultimo_titulo) + "-cena"
        vistos[chave] = vistos.get(chave, 0) + 1
        if vistos[chave] > 1:
            chave = f"{chave}-{vistos[chave]}"
        # Pula uma linha em branco/quebra só de separador no fim.
        while bloco and not bloco[-1].strip():
            bloco = bloco[:-1]
            fim -= 1
        unidades.append(Unidade(
            id=f"{base}#{chave}",
            arquivo=arquivo,
            titulo=titulo or ultimo_titulo,
            linha_inicio=i + 1,
            linha_fim=i + len(bloco),
            linhas=bloco,
            tipo=tipo,
        ))
    return unidades


# ---------------------------------------------------------------------------
# Classificação automática do tipo (usada só quando doctypes.yaml não declara)
# ---------------------------------------------------------------------------

_SINAIS_TITULO = {
    "biblia": re.compile(r"\b(bible|b[ií]blia|worldbuilding|codex|compendium|encyclop|glossary|gloss[aá]rio|lore|reference|systems)\b", re.I),
    "ficha": re.compile(r"\b(character bible|ficha|dossier|dossi[eê]|profile|perfil)\b", re.I),
    "cronologia": re.compile(r"\b(timeline|chronolog|cronologia|linha do tempo|annals|anais)\b", re.I),
    "roteiro": re.compile(r"\b(screenplay|roteiro|script|teleplay)\b", re.I),
    "ramificado": re.compile(r"\b(campaign|campanha|branching|interactive fiction|choose your)\b", re.I),
}
# A categoria que o autor já escreveu no front matter do site é evidência forte.
_CATEGORIA = {
    "worldbuilding": "biblia", "worldbuilding reference": "biblia",
    "fiction": "prosa", "ficcao": "prosa", "ficção": "prosa",
}


def _front_matter(linhas: list[str]) -> dict:
    fim = fim_do_front_matter(linhas)
    dados = {}
    for l in linhas[1:max(1, fim - 1)]:
        m = re.match(r"^(\w+):\s*\"?(.*?)\"?\s*$", l)
        if m:
            dados[m.group(1).lower()] = m.group(2)
    return dados


def classificar(texto: str) -> dict:
    """Classifica o tipo do documento e CITA o que motivou a classificação.

    Heurística determinística e deliberadamente conservadora: confiança `alta`
    só com evidência declarada (título ou categoria do front matter) E margem
    folgada. Sem isso, no máximo `media` — e `baixa` vira pergunta ao autor antes
    de qualquer verificação (seção 4.3). Um tipo errado muda todos os
    diagnósticos; errar para o lado de perguntar é barato.
    """
    linhas = texto.split("\n")
    fm = _front_matter(linhas)
    corpo = linhas[fim_do_front_matter(linhas):]
    ne = [l for l in corpo if l.strip()] or [""]
    n = len(ne)

    pontos = {t: 0.0 for t in ("prosa", "roteiro", "biblia", "ficha", "cronologia", "ramificado")}
    evidencias: dict[str, list[str]] = {t: [] for t in pontos}
    declarado: set[str] = set()

    def marcar(tipo: str, peso: float, linha: str, decl: bool = False) -> None:
        if peso <= 0:
            return
        pontos[tipo] += peso
        if decl:
            declarado.add(tipo)
        if len(evidencias[tipo]) < 3 and linha.strip():
            evidencias[tipo].append(linha.strip()[:160])

    cat = (fm.get("category") or "").strip().casefold()
    if cat in _CATEGORIA:
        marcar(_CATEGORIA[cat], 4.0, f"category: {fm['category']}", decl=True)
    for linha in [l for l in ne if TITULO.match(l)][:6] + [fm.get("title", "")]:
        for tipo, rx in _SINAIS_TITULO.items():
            if linha and rx.search(linha):
                marcar(tipo, 3.0, linha, decl=True)

    tab = [l for l in ne if l.lstrip().startswith("|")]
    lst = [l for l in ne if re.match(r"\s*([-*+]|\d+[.)])\s", l)]
    neg = [l for l in ne if re.match(r"\s*([-*+]\s+)?\*\*[^*]+\*\*", l)]
    dlg = [l for l in ne if re.search(r"(^|\s)[\"“]\S", l)]
    rot = [l for l in ne if CABECALHO_ROTEIRO.match(l)]
    ano = [l for l in ne if re.match(r"^\s*[-*|]?\s*\**\s*\d{3,4}\b", l)]
    par = [l for l in ne if not l.lstrip().startswith(("#", "|", "-", "*", ">")) and len(l) > 200]
    palavras = sum(len(l.split()) for l in par) or 1
    eu = sum(len(re.findall(r"\b(I|me|my|eu|meu|minha)\b", l)) for l in par)

    marcar("biblia", 12.0 * (len(tab) + len(lst) + len(neg)) / n, (tab or lst or neg or [""])[0])
    marcar("ficha", 6.0 * len(neg) / n, (neg or [""])[0])
    marcar("prosa", 30.0 * len(dlg) / n, (dlg or [""])[0])
    marcar("prosa", min(3.0, (1000.0 * eu / palavras) / 15.0), (par or [""])[0])
    marcar("roteiro", 30.0 * len(rot) / n, (rot or [""])[0])
    marcar("cronologia", 15.0 * len(ano) / n, (ano or [""])[0])

    ordem = sorted(pontos, key=lambda t: -pontos[t])
    melhor, segundo = ordem[0], ordem[1]
    margem = pontos[melhor] - pontos[segundo]
    if pontos[melhor] < 2.0 or margem < 1.5:
        confianca = "baixa"
    elif melhor in declarado and margem >= 3.0:
        confianca = "alta"
    else:
        confianca = "media"
    return {
        "tipo": melhor,
        "confianca": confianca,
        "evidencias": evidencias[melhor] or [ne[0].strip()[:160]],
        "pontos": {t: round(v, 2) for t, v in pontos.items()},
    }
