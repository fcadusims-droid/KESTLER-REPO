"""Verificador formal: atributos fixos (seção 6.1).

Dois casos:

1. CANON × OBRA. `canon/characters.yaml` diz que os olhos de Ana são verdes; um
   fato narrador diz azuis. Com o canon autoritativo e STRICT, é ERROR.

2. OBRA × OBRA. Sem canon, o mesmo atributo funcional aparece com dois valores.
   Não dá para saber qual lado está certo: WARNING com pergunta ao autor, e o
   relatório conta quantos trechos sustentam cada valor — a "maioria clara" que
   a seção 5.2 exige antes de qualquer troca pontual.
"""

from __future__ import annotations

from collections import defaultdict

from ..canon import Canon
from ..diagnostics import Diagnostico, Evidencia, nivel_por_evidencia
from ..io import normalizar_nome
from ..schema import menor_confianca, predicados_registrados


def _evidencia(f: dict) -> Evidencia:
    return Evidencia(arquivo=f["local"]["arquivo"], linha_inicio=f["local"]["linha_inicio"],
                     linha_fim=f["local"]["linha_fim"], citacao=f["citacao"],
                     unidade=f["local"].get("unidade"), fato=f["id"], modo=f["modo"],
                     confianca=f.get("confianca_extracao"))


def _atributo(f: dict) -> str | None:
    """Nome do atributo de um fato: `tem_atributo` usa o qualificador."""
    if f["predicado"] == "tem_atributo":
        nome = (f.get("qualificadores") or {}).get("atributo")
        return normalizar_nome(nome) if nome else None
    return f["predicado"]


def verificar(fatos_por_doc: dict[str, dict], canon: Canon) -> list[Diagnostico]:
    registrados = predicados_registrados()
    funcionais = {p for p, info in registrados.items() if info.get("funcional")} | {"tem_atributo"}
    # Datas de nascimento/morte são da timeline, não deste verificador.
    funcionais -= {"nasce_em", "morre_em"}
    todos = [f for doc in fatos_por_doc.values() for f in doc.get("fatos", [])
             if f["predicado"] in funcionais and f.get("objeto") not in (None, "")]
    saida: list[Diagnostico] = []

    # 1. canon × obra
    for f in todos:
        pessoa = canon.pessoas.resolver(f["sujeito"])
        attr = _atributo(f)
        if not pessoa or not attr:
            continue
        travados = {normalizar_nome(k): v for k, v in pessoa.atributos.items()}
        if attr not in travados:
            continue
        if normalizar_nome(travados[attr]) == normalizar_nome(f["objeto"]):
            continue
        aut = pessoa.autoridade
        nivel, notas = nivel_por_evidencia(aut["rigidez"], aut["autoritativo"], [f["modo"]],
                                           [f.get("confianca_extracao")])
        if not aut["autoritativo"]:
            notas.append(aut["motivo"])
        saida.append(Diagnostico(
            prefixo="AT", nivel=nivel, verificador="atributos", camada="formal", metodo="atributos",
            titulo=f"{pessoa.nome}: {attr} diferente do canon",
            regra=f"canon/characters.yaml → {pessoa.nome}.{attr} = {travados[attr]}",
            evidencias=[Evidencia(arquivo="canon/characters.yaml", linha_inicio=0, linha_fim=0,
                                  citacao=f"{pessoa.nome}.{attr} = {travados[attr]}", fonte="canon"),
                        _evidencia(f)],
            conflito=f"canon: {travados[attr]}; o trecho: {f['objeto']}",
            acao="REVISAO", pergunta=f"trocar '{f['objeto']}' por '{travados[attr]}' neste trecho?",
            confianca=f.get("confianca_extracao", "media"), notas=notas,
            chave={"pessoa": normalizar_nome(pessoa.nome), "atributo": attr, "fato": f["id"]},
        ))

    # 2. obra × obra (só fatos do mundo)
    grupos: dict[tuple, list[dict]] = defaultdict(list)
    for f in todos:
        if f["modo"] != "narrador":
            continue
        attr = _atributo(f)
        if not attr:
            continue
        pessoa = canon.pessoas.resolver(f["sujeito"])
        if pessoa and attr in {normalizar_nome(k) for k in pessoa.atributos}:
            continue      # o canon já decide; tratado acima
        chave_sujeito = normalizar_nome(pessoa.nome if pessoa else f["sujeito"])
        grupos[(chave_sujeito, attr)].append(f)
    for (sujeito, attr), fatos in grupos.items():
        valores: dict[str, list[dict]] = defaultdict(list)
        for f in fatos:
            valores[normalizar_nome(f["objeto"])].append(f)
        if len(valores) < 2:
            continue
        contagem = sorted(((len(v), k) for k, v in valores.items()), reverse=True)
        maioria = contagem[0][0] >= 2 * contagem[1][0] and contagem[0][0] >= 3
        exemplos = [v[0] for _, v in sorted(valores.items())]
        saida.append(Diagnostico(
            prefixo="AT", nivel="WARNING", verificador="atributos", camada="formal", metodo="atributos",
            titulo=f"{fatos[0]['sujeito']}: {attr} com valores diferentes na obra",
            regra="consistência interna (atributo funcional)",
            evidencias=[_evidencia(f) for f in exemplos],
            conflito="; ".join(f"'{valores[k][0]['objeto']}' em {n} trecho(s)" for n, k in contagem)
                     + ("\nHá maioria clara." if maioria else "\nSem maioria clara."),
            acao="REVISAO", pergunta="qual valor vale? (a troca pontual só depois da resposta)",
            confianca=menor_confianca(*(f.get("confianca_extracao") for f in exemplos)),
            notas=["contradição interna da obra, sem canon envolvido"],
            chave={"sujeito": sujeito, "atributo": attr,
                   "fatos": sorted(f["id"] for f in fatos)},
        ))
    return saida
