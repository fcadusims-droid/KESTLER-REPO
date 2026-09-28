"""Apoio dos testes: canon e fatos construídos em memória, sem tocar nos
arquivos reais do projeto."""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))

from nlean.canon import Canon, Hierarquia, Pessoas  # noqa: E402


def canon_de(personagens=None, regras=None, entidades=None, timeline=None, intencoes=None) -> Canon:
    personagens = personagens or {}
    entidades = entidades or {}
    pessoas = Pessoas(personagens)
    return Canon(personagens=personagens, regras=regras or {}, entidades=entidades,
                 timeline=timeline or {}, lugares={}, intencoes=intencoes or {},
                 pessoas=pessoas, hierarquia=Hierarquia.do_canon(entidades, pessoas))


_n = [0]


def fato(sujeito, predicado, objeto=None, ano=None, modo="narrador", tipo=None, confianca="alta",
         linha=None, arquivo="obra.md", tempo=None, qualificadores=None, ref=None, citacao=None,
         tipo_documento="prosa"):
    _n[0] += 1
    n = _n[0]
    linha = linha or n
    if tempo is None and ano is not None:
        tempo = {"ano": ano, "mes": None, "dia": None, "relativo_a": None, "flashback": False,
                 "calendario": None}
    if tipo is None:
        tipo = "atributo" if predicado in ("tem_idade", "nasce_em", "tem_atributo") else "evento"
    return {
        "id": f"F-{n:04d}", "tipo": tipo, "sujeito": sujeito, "predicado": predicado,
        "objeto": objeto, "qualificadores": qualificadores or {}, "tempo": tempo, "modo": modo,
        "ref": ref, "tipo_documento": tipo_documento,
        "citacao": citacao or f"trecho {n} de {sujeito} {predicado}",
        "local": {"arquivo": arquivo, "unidade": "obra#x", "linha_inicio": linha, "linha_fim": linha},
        "confianca_extracao": confianca, "origem_extracao": "aberta",
    }


def docs(*fatos):
    return {"obra.md": {"fatos": list(fatos)}}
