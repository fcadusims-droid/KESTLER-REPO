"""Verificadores formais: regras do mundo e regra × regra (seções 5 e 6.1).

Uma regra do canon tem esta forma:

    - id: R-MAGIA-03
      descricao: toda magia exige um objeto-âncora     # palavras do autor
      aplica_a: { predicado: usa_poder, sujeito_e_um: null }
      exige: { ancora: true }        # qualificador que o fato precisa ter
      proibido: false                # true = o próprio ato é proibido no escopo
      excecoes:
        - { sujeito_e_um: sacerdote }
      rigidez: STRICT

A hierarquia é_um vem de canon/entidades.yaml: se "cura é_um usa_poder", a
regra acima vale para cura. As exceções tiram casos do escopo. Isso é o que o
documento pede ao ASP/Datalog — herança e exceção —, implementado direto em
Python, sem dependência, porque a forma das regras é simples o bastante para
que o conflito entre duas delas se decida enumerando os casos da hierarquia.

Nada aqui interpreta texto. Um fato viola a regra quando o qualificador exigido
foi extraído com o valor contrário; quando o qualificador simplesmente não foi
extraído, isso não é violação — é uma LACUNA de extração, contada à parte,
porque é exatamente o falso negativo silencioso que a seção 2 descreve.
"""

from __future__ import annotations

import itertools

from ..canon import Canon, hash_formal
from ..diagnostics import Diagnostico, Evidencia, nivel_por_evidencia
from ..io import normalizar_nome
from ..schema import normalizar_predicado

QUALQUER = "(qualquer)"


def _valor(v):
    """Normaliza valores de qualificador: 'sim'/'true'/True → True etc."""
    if isinstance(v, bool):
        return v
    if v is None:
        return None
    s = normalizar_nome(v)
    if s in ("true", "sim", "yes", "verdadeiro", "cumprida", "cumprido"):
        return True
    if s in ("false", "nao", "no", "falso", "violada", "violado"):
        return False
    if s in ("desconhecido", "indeterminado", "nao da para saber", "?", "unknown"):
        return None
    return s


def aplica(regra: dict, predicado: str, sujeito, canon: Canon) -> bool:
    alvo = regra.get("aplica_a") or {}
    h = canon.hierarquia
    p = alvo.get("predicado")
    if p and not h.e_um(predicado, normalizar_predicado(p)):
        return False
    s = alvo.get("sujeito_e_um")
    if s and (sujeito in (None, QUALQUER) or not h.e_um(sujeito, s)):
        return False
    return True


def excecao(regra: dict, predicado: str, sujeito, qualificadores: dict, canon: Canon) -> dict | None:
    h = canon.hierarquia
    for exc in regra.get("excecoes") or []:
        ok = True
        if exc.get("sujeito_e_um"):
            ok &= sujeito not in (None, QUALQUER) and h.e_um(sujeito, exc["sujeito_e_um"])
        if exc.get("predicado_e_um"):
            ok &= h.e_um(predicado, normalizar_predicado(exc["predicado_e_um"]))
        for k, v in (exc.get("qualificador") or {}).items():
            ok &= _valor(qualificadores.get(k)) == _valor(v)
        if ok and exc:
            return exc
    return None


def _evidencia(f: dict) -> Evidencia:
    return Evidencia(arquivo=f["local"]["arquivo"], linha_inicio=f["local"]["linha_inicio"],
                     linha_fim=f["local"]["linha_fim"], citacao=f["citacao"],
                     unidade=f["local"].get("unidade"), fato=f["id"], modo=f["modo"],
                     confianca=f.get("confianca_extracao"))


def verificar_regras(fatos_por_doc: dict[str, dict], canon: Canon) -> tuple[list[Diagnostico], list[dict]]:
    """Fatos contra as regras do mundo. Devolve (diagnósticos, lacunas)."""
    todos = [f for doc in fatos_por_doc.values() for f in doc.get("fatos", [])]
    saida, lacunas = [], []
    for regra in canon.lista_regras():
        aut = canon.autoridade_regra(regra)
        for f in todos:
            if not aplica(regra, f["predicado"], f["sujeito"], canon):
                continue
            if excecao(regra, f["predicado"], f["sujeito"], f.get("qualificadores") or {}, canon):
                continue
            violacoes = []
            if regra.get("proibido"):
                violacoes.append("o ato é proibido neste escopo")
            for k, esperado in (regra.get("exige") or {}).items():
                obtido = _valor((f.get("qualificadores") or {}).get(k))
                if obtido is None:
                    lacunas.append({"regra": regra["id"], "fato": f["id"], "qualificador": k,
                                    "citacao": f["citacao"], "local": f["local"]})
                elif obtido != _valor(esperado):
                    violacoes.append(f"{k}: exigido {esperado!r}, o trecho mostra {obtido!r}")
            if not violacoes:
                continue
            nivel, notas = nivel_por_evidencia(aut["rigidez"], aut["autoritativo"], [f["modo"]],
                                               [f.get("confianca_extracao")])
            if not aut["autoritativo"]:
                notas.append(aut["motivo"])
            saida.append(Diagnostico(
                prefixo="RM", nivel=nivel, verificador="regras_do_mundo", camada="formal",
                metodo="regras_do_mundo", titulo=f"Regra {regra['id']} violada",
                regra=f"canon/world_rules.yaml → {regra['id']}: {regra.get('descricao', '').strip()}",
                evidencias=[_evidencia(f)],
                conflito="\n".join(violacoes),
                # Troca pontual se couber; se não couber, conteúdo novo (seção 5.2).
                acao="REVISAO", pergunta="a troca pontual resolve, ou é preciso conteúdo novo (fluxo 5.3)?",
                confianca=f.get("confianca_extracao", "media"), notas=notas,
                chave={"regra": regra["id"], "fato": f["id"]},
            ))
    return saida, lacunas


# ---------------------------------------------------------------------------
# Regra × regra
# ---------------------------------------------------------------------------

def _escopo(regra: dict, canon: Canon) -> tuple[set[str], set[str] | None]:
    alvo = regra.get("aplica_a") or {}
    h = canon.hierarquia
    p = alvo.get("predicado")
    preds = h.descendentes(normalizar_predicado(p)) if p else set(h.pais) or {QUALQUER}
    s = alvo.get("sujeito_e_um")
    sujs = h.descendentes(s) if s else None      # None = qualquer sujeito
    return preds, sujs


def _testemunhas_sujeito(a: set | None, b: set | None) -> list:
    if a is None and b is None:
        return [QUALQUER]
    if a is None:
        return sorted(b)
    if b is None:
        return sorted(a)
    return sorted(a & b)


def regra_x_regra(canon: Canon, somente_aprovadas: bool = True) -> tuple[list[Diagnostico], list[str]]:
    """Duas regras que não podem valer ao mesmo tempo.

    Conflito = existe um caso concreto (um predicado e um sujeito da hierarquia)
    em que as duas regras se aplicam, nenhuma exceção o tira, e elas exigem
    valores diferentes do mesmo qualificador. O caso encontrado é a prova: vai
    no diagnóstico, junto com a cadeia é_um que o liga às duas regras.
    """
    regras = canon.lista_regras()
    ignoradas = []
    usaveis = []
    for r in regras:
        aut = canon.autoridade_regra(r)
        if somente_aprovadas and not aut["autoritativo"]:
            ignoradas.append(f"{r['id']}: {aut['motivo']}")
            continue
        usaveis.append(r)

    h = canon.hierarquia
    saida = []
    for a, b in itertools.combinations(usaveis, 2):
        comuns = set(a.get("exige") or {}) & set(b.get("exige") or {})
        opostos = [k for k in comuns if _valor(a["exige"][k]) != _valor(b["exige"][k])]
        if not opostos:
            continue
        pa, sa = _escopo(a, canon)
        pb, sb = _escopo(b, canon)
        # Prefere como prova as classes que as regras declaram (legível para o
        # autor) antes de instâncias individuais.
        declarados = {h._chave(v) for r in (a, b) for v in (r.get("aplica_a") or {}).values() if v}
        ordem = lambda x: (x not in declarados, bool(h.filhos_diretos(x)) is False, x)  # noqa: E731
        testemunha = None
        for p in sorted(pa & pb, key=ordem):
            for s in sorted(_testemunhas_sujeito(sa, sb), key=ordem):
                if excecao(a, p, s, {}, canon) or excecao(b, p, s, {}, canon):
                    continue
                testemunha = (p, s)
                break
            if testemunha:
                break
        if not testemunha:
            continue
        p, s = testemunha
        ev = [
            Evidencia(arquivo="canon/world_rules.yaml", linha_inicio=0, linha_fim=0, fonte="canon",
                      citacao=f"{r['id']}: {r.get('descricao', '').strip()} — exige "
                              f"{ {k: r['exige'][k] for k in opostos} }")
            for r in (a, b)
        ]
        cadeia = []
        for alvo_regra in (a, b):
            pred_regra = (alvo_regra.get("aplica_a") or {}).get("predicado")
            if pred_regra and normalizar_predicado(pred_regra) != p:
                cadeia.append(f"{h.nome(p)} é_um {pred_regra}")
        nivel = "ERROR" if all(canon.autoridade_regra(r)["rigidez"] == "STRICT" for r in (a, b)) \
            else "WARNING"
        saida.append(Diagnostico(
            prefixo="RR", nivel=nivel, verificador="regra_x_regra", camada="formal",
            metodo="regra_x_regra", titulo=f"{a['id']} e {b['id']} não podem valer juntas",
            regra=f"canon/world_rules.yaml → {a['id']}, {b['id']}",
            evidencias=ev,
            conflito=(f"Caso concreto: sujeito {h.nome(s) if s != QUALQUER else 'qualquer'} fazendo "
                      f"{h.nome(p)}.\n"
                      + (f"Cadeia: {'; '.join(sorted(set(cadeia)))}.\n" if cadeia else "")
                      + "; ".join(f"{a['id']} exige {k}={a['exige'][k]!r}, {b['id']} exige "
                                  f"{k}={b['exige'][k]!r}" for k in opostos)
                      + ".\nNenhuma exceção cobre este caso."),
            acao="RELATORIO",
            pergunta="acrescentar uma exceção a uma das regras, ou uma delas está errada?",
            notas=["contradição dentro do canon: o sistema pergunta, nunca troca regra sozinho"],
            chave={"regras": sorted([a["id"], b["id"]]), "qualificadores": sorted(opostos)},
        ))
    return saida, ignoradas


# ---------------------------------------------------------------------------
# Bateria de casos para aprovação pelas consequências (seção 5)
# ---------------------------------------------------------------------------

def veredito(canon: Canon, predicado: str, sujeito, qualificadores: dict,
             regras: list[dict] | None = None) -> list[str]:
    """Quais regras um caso concreto viola. Lista vazia = permitido."""
    violadas = []
    for r in regras if regras is not None else canon.lista_regras():
        if not aplica(r, predicado, sujeito, canon):
            continue
        if excecao(r, predicado, sujeito, qualificadores, canon):
            continue
        if r.get("proibido"):
            violadas.append(r["id"])
            continue
        for k, esperado in (r.get("exige") or {}).items():
            if k in qualificadores and _valor(qualificadores[k]) != _valor(esperado):
                violadas.append(r["id"])
                break
    return violadas


def bateria(canon: Canon, regra: dict) -> list[dict]:
    """Casos gerados MECANICAMENTE da hierarquia e das exceções, não escolhidos.

    Um caso para cada tipo filho na hierarquia é_um e um para cada exceção, dos
    dois lados da fronteira. Se o Claude escolhesse os casos, tenderia a escolher
    os que a própria tradução acerta.
    """
    h = canon.hierarquia
    alvo = regra.get("aplica_a") or {}
    pred = normalizar_predicado(alvo["predicado"]) if alvo.get("predicado") else None
    predicados = [pred] + sorted(h.filhos_diretos(pred) | (h.descendentes(pred) - {pred})) if pred else [QUALQUER]
    suj_regra = alvo.get("sujeito_e_um")
    sujeitos = [suj_regra or QUALQUER]
    if suj_regra:
        sujeitos += sorted(h.descendentes(suj_regra) - {h._chave(suj_regra)})
    # Os dois lados de cada exceção: o tipo excetuado, e do lado de fora a
    # classe-pai (um clérigo qualquer não é necessariamente sacerdote) e os irmãos.
    for exc in regra.get("excecoes") or []:
        s = exc.get("sujeito_e_um")
        if s:
            sujeitos.append(h._chave(s))
            pais = h.pais.get(h._chave(s), set())
            irmaos = set()
            for pai in pais:
                irmaos |= h.filhos_diretos(pai)
            irmaos -= {h._chave(s)}
            sujeitos += sorted(pais) + sorted(irmaos)[:2] + [QUALQUER]
        p = exc.get("predicado_e_um")
        if p:
            predicados.append(normalizar_predicado(p))

    exige = regra.get("exige") or {}
    combinacoes = [{}]
    for k, v in exige.items():
        combinacoes = [{**c, k: val} for c in combinacoes for val in (v, _oposto(v))]
    casos, vistos = [], set()
    for p in dict.fromkeys(predicados):
        for s in dict.fromkeys(sujeitos):
            for q in combinacoes:
                chave = (p, s, tuple(sorted(q.items())))
                if chave in vistos:
                    continue
                vistos.add(chave)
                violadas = veredito(canon, p, s, q)
                casos.append({
                    "predicado": h.nome(p) if p != QUALQUER else "qualquer ato",
                    "sujeito": h.nome(s) if s != QUALQUER else "qualquer um",
                    "qualificadores": q, "violadas": violadas,
                    "texto": _frase(h.nome(p) if p != QUALQUER else "qualquer ato",
                                    h.nome(s) if s != QUALQUER else "qualquer um", q, violadas),
                })
    return casos


def _oposto(v):
    if isinstance(v, bool):
        return not v
    return f"não {v}"


def _frase(pred, suj, q, violadas) -> str:
    partes = ", ".join(f"{k} = {v}" for k, v in q.items()) or "sem qualificador"
    resultado = "violação (" + ", ".join(violadas) + ")" if violadas else "permitido"
    return f"{suj} realizando {pred} com {partes}: {resultado}"


def aprovar(regra: dict) -> dict:
    """Marca a formalização como aprovada pelo AUTOR (nunca chamado pelo Claude)."""
    forma = dict(regra.get("formalizacao") or {"proposta_por": "claude"})
    forma["aprovada_hash"] = hash_formal(regra)
    return {**regra, "formalizacao": forma}
