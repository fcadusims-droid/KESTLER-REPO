"""O formato comum. Nenhum verificador é escrito antes dele (seção 5).

Todo fato, regra e diagnóstico passa por aqui. Se cada verificador inventasse o
próprio formato, a regressão entre versões ficaria impossível.
"""

from __future__ import annotations

from .io import RAIZ, ErroDeProjeto, carregar_yaml, normalizar_nome

TIPOS_FATO = ("evento", "atributo", "relacao", "conhecimento", "localizacao")
MODOS = ("narrador", "fala", "pensamento", "hipotetico", "documento_interno")
CONFIANCAS = ("alta", "media", "baixa")
TIPOS_DOCUMENTO = ("prosa", "roteiro", "biblia", "ficha", "cronologia", "ramificado")
RIGIDEZ = ("STRICT", "FLEXIBLE")
NIVEIS = ("ERROR", "WARNING", "SUGGESTION")
ACOES = ("REVISAO", "NOVO_CONTEUDO", "RELATORIO")
CAMADAS = ("formal", "semantica")
UNIDADES_TEMPO = ("dias", "semanas", "meses", "anos")

# Grafias que o extrator costuma produzir e que significam a mesma coisa.
_ALIAS_MODO = {
    "hipotético": "hipotetico",
    "documento interno": "documento_interno",
    "documento-interno": "documento_interno",
    "narração": "narrador",
    "narracao": "narrador",
}
_ALIAS_CONFIANCA = {"média": "media", "high": "alta", "medium": "media", "low": "baixa"}
_ALIAS_UNIDADE = {
    "dia": "dias", "semana": "semanas", "mes": "meses", "mês": "meses",
    "ano": "anos", "days": "dias", "day": "dias", "weeks": "semanas",
    "week": "semanas", "months": "meses", "month": "meses",
    "years": "anos", "year": "anos",
}

ORDEM_CONFIANCA = {"baixa": 0, "media": 1, "alta": 2}


def versao_schema() -> str:
    return (RAIZ / "schema" / "VERSION").read_text(encoding="utf-8").strip()


def normalizar_modo(valor) -> str | None:
    if valor is None:
        return None
    v = str(valor).strip().casefold()
    v = _ALIAS_MODO.get(v, v)
    return v if v in MODOS else None


def normalizar_confianca(valor) -> str | None:
    if valor is None:
        return None
    v = str(valor).strip().casefold()
    v = _ALIAS_CONFIANCA.get(v, v)
    return v if v in CONFIANCAS else None


def normalizar_unidade(valor) -> str | None:
    if valor is None:
        return None
    v = str(valor).strip().casefold()
    v = _ALIAS_UNIDADE.get(v, v)
    return v if v in UNIDADES_TEMPO else None


def menor_confianca(*valores: str) -> str:
    """A confiança do diagnóstico nunca é maior que a da extração (seção 7)."""
    validos = [v for v in valores if v in ORDEM_CONFIANCA]
    if not validos:
        return "baixa"
    return min(validos, key=lambda v: ORDEM_CONFIANCA[v])


# ---------------------------------------------------------------------------
# Vocabulário fechado de predicados
# ---------------------------------------------------------------------------

def carregar_vocabulario() -> dict:
    dados = carregar_yaml(RAIZ / "schema" / "predicados.yaml")
    if not dados or "predicados" not in dados:
        raise ErroDeProjeto("schema/predicados.yaml sem a chave `predicados`")
    return dados


def predicados_registrados(vocab: dict | None = None) -> dict:
    vocab = vocab or carregar_vocabulario()
    return {normalizar_nome(k).replace(" ", "_"): (v or {}) for k, v in vocab["predicados"].items()}


def normalizar_predicado(valor) -> str:
    return normalizar_nome(valor).replace(" ", "_").replace("-", "_")


# ---------------------------------------------------------------------------
# Tempo
# ---------------------------------------------------------------------------

def validar_tempo(tempo) -> tuple[dict | None, list[str]]:
    """Normaliza o campo `tempo` de um fato. Devolve (tempo, problemas)."""
    problemas: list[str] = []
    if tempo in (None, {}, ""):
        return None, problemas
    if not isinstance(tempo, dict):
        return None, ["tempo não é um mapa"]

    saida: dict = {
        "ano": None, "mes": None, "dia": None,
        "relativo_a": None, "flashback": bool(tempo.get("flashback", False)),
        "calendario": tempo.get("calendario") or None,
    }
    for campo in ("ano", "mes", "dia"):
        v = tempo.get(campo)
        if v in (None, ""):
            continue
        try:
            saida[campo] = int(v)
        except (TypeError, ValueError):
            problemas.append(f"tempo.{campo} não é inteiro: {v!r}")
    if saida["mes"] is not None and not 1 <= saida["mes"] <= 12:
        problemas.append(f"tempo.mes fora de 1..12: {saida['mes']}")
        saida["mes"] = None
    if saida["dia"] is not None and not 1 <= saida["dia"] <= 31:
        problemas.append(f"tempo.dia fora de 1..31: {saida['dia']}")
        saida["dia"] = None

    rel = tempo.get("relativo_a")
    if rel:
        if not isinstance(rel, dict):
            problemas.append("tempo.relativo_a não é um mapa")
        else:
            desvio = rel.get("desvio") or {}
            unidade = normalizar_unidade(desvio.get("unidade"))
            sentido = str(desvio.get("sentido", "depois")).casefold()
            if sentido not in ("depois", "antes"):
                problemas.append(f"tempo.relativo_a.desvio.sentido inválido: {sentido}")
                sentido = "depois"
            try:
                valor = desvio.get("valor")
                vmin = desvio.get("min", valor)
                vmax = desvio.get("max", valor)
                vmin = None if vmin is None else float(vmin)
                vmax = None if vmax is None else float(vmax)
            except (TypeError, ValueError):
                problemas.append("tempo.relativo_a.desvio com número inválido")
                vmin = vmax = None
            if vmin is None or vmax is None or unidade is None:
                problemas.append("tempo.relativo_a sem desvio completo (min/max/unidade)")
            saida["relativo_a"] = {
                "ref": rel.get("ref"),
                "evento": rel.get("evento"),
                "descricao": rel.get("descricao"),
                "desvio": None if unidade is None or vmin is None or vmax is None
                else {"min": min(vmin, vmax), "max": max(vmin, vmax),
                      "unidade": unidade, "sentido": sentido},
            }
    return saida, problemas


def tem_tempo(fato: dict) -> bool:
    t = fato.get("tempo")
    return bool(t) and (t.get("ano") is not None or t.get("relativo_a") is not None)
