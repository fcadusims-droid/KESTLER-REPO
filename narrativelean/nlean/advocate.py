"""Advogado do diabo: o código roteia, o operador julga (seção 6.5).

O código só DETECTA e ROTEIA — decidir se uma lente é a certa para uma cena é
interpretação, e torná-la determinística daria a ela autoridade falsa. São
marcados para revisão:

- dois ou mais diagnósticos sobre o mesmo trecho ou o mesmo elemento;
- diagnósticos de lentes com tensão conhecida (lens_conflicts.yaml);
- todo diagnóstico com ação NOVO_CONTEUDO (é o que mais custa ao autor);
- diagnósticos em documentos cuja classificação de tipo não foi declarada.

O pacote de cada caso leva o diagnóstico e as evidências, mas NÃO as notas do
verificador — o advogado não pode herdar o mesmo erro de leitura. E as regras
do parecer são impostas na ingestão: nunca apaga, nunca sobe para ERROR, e
argumento sem citação ancorada no texto é descartado.
"""

from __future__ import annotations

from .extraction import _render
from .grounding import ancorar, sobrepoe
from .io import RAIZ, ErroDeProjeto, carregar_yaml, ler_obra, projeto, salvar_yaml, sha

VEREDITOS = ("MANTER", "REENQUADRAR", "REBAIXAR", "CONTESTAR")
ORDEM = {"SUGGESTION": 0, "WARNING": 1, "ERROR": 2}
PENDENTES = RAIZ / "work" / "advogado" / "pendentes"
RESPOSTAS = RAIZ / "work" / "advogado" / "respostas"


def _spans(d: dict) -> list[tuple[str, int, int]]:
    return [(e["arquivo"], e["linha_inicio"], e["linha_fim"]) for e in d["evidencias"]
            if e.get("fonte") == "obra"]


def rotear(relatorio: dict) -> list[dict]:
    diags = [d for d in relatorio["diagnosticos"] if not d.get("suprimido")]
    conflitos = (carregar_yaml(RAIZ / "lens_conflicts.yaml", {}) or {}).get("tensoes") or []
    pares_lente = {frozenset((t["lente"], t["com"].split(":", 1)[1])) for t in conflitos
                   if str(t.get("com", "")).startswith("lente:")}
    intencoes = carregar_yaml(RAIZ / "canon" / "intencoes.yaml", {}) or {}
    docs_incertos = {doc for doc, r in relatorio["documentos"].items()
                     if (r.get("classificacao") or {}).get("fonte") != "declarado"}

    motivos: dict[str, set[str]] = {d["impressao"]: set() for d in diags}
    grupos: list[set[str]] = []
    for i, a in enumerate(diags):
        if a["acao"] == "NOVO_CONTEUDO":
            motivos[a["impressao"]].add("ação NOVO_CONTEUDO")
        if any(s[0] in docs_incertos for s in _spans(a)):
            motivos[a["impressao"]].add("tipo de documento não declarado pelo autor")
        for t in conflitos:
            alvo = str(t.get("com", ""))
            if t["lente"] == a["verificador"] and alvo.startswith("intencao:"):
                chave = alvo.split(":", 1)[1].split("=")[0]
                if chave in intencoes:
                    motivos[a["impressao"]].add(f"tensão com intenção declarada: {alvo}")
        for b in diags[i + 1:]:
            mesmo_trecho = any(sa[0] == sb[0] and sobrepoe(sa[1:], sb[1:])
                               for sa in _spans(a) for sb in _spans(b))
            mesmo_elemento = bool(set(map(str, (a.get("chave") or {}).values()))
                                  & set(map(str, (b.get("chave") or {}).values())))
            if not (mesmo_trecho or mesmo_elemento):
                continue
            motivo = "dois diagnósticos sobre o mesmo trecho" if mesmo_trecho \
                else "dois diagnósticos sobre o mesmo elemento"
            if frozenset((a["verificador"], b["verificador"])) in pares_lente:
                motivo = f"lentes em tensão: {a['verificador']} × {b['verificador']}"
            motivos[a["impressao"]].add(motivo)
            motivos[b["impressao"]].add(motivo)
            grupos.append({a["impressao"], b["impressao"]})

    # Junta grupos que se tocam: o advogado vê os casos relacionados juntos.
    juntos: list[set[str]] = []
    for g in grupos + [{k} for k, v in motivos.items() if v]:
        for j in juntos:
            if j & g:
                j |= g
                break
        else:
            juntos.append(set(g))
    por_imp = {d["impressao"]: d for d in diags}
    casos = []
    for g in juntos:
        membros = [por_imp[i] for i in sorted(g) if motivos.get(i)]
        if not membros:
            continue
        casos.append({"id": "RV-" + sha("|".join(sorted(g)), 8), "diagnosticos": membros,
                      "motivos": sorted(set().union(*(motivos[m["impressao"]] for m in membros)))})
    return casos


def preparar(relatorio: dict) -> int:
    versao = (projeto().get("prompts") or {}).get("advogado")
    modelo = (RAIZ / "prompts" / f"{versao}.md").read_text(encoding="utf-8")
    intencoes = (RAIZ / "canon" / "intencoes.yaml").read_text(encoding="utf-8") \
        if (RAIZ / "canon" / "intencoes.yaml").exists() else "(vazio)"
    PENDENTES.mkdir(parents=True, exist_ok=True)
    n = 0
    for caso in rotear(relatorio):
        blocos, arquivos = [], set()
        for d in caso["diagnosticos"]:
            ev = "\n".join(f"  - {e['arquivo']} l.{e['linha_inicio']}–{e['linha_fim']}: \"{e['citacao']}\""
                           if e.get("fonte") == "obra" else f"  - {e['arquivo']}: {e['citacao']}"
                           for e in d["evidencias"])
            # Sem `notas` nem `pergunta`: o raciocínio do verificador fica de fora.
            blocos.append(f"### {d['impressao']}\n- {d['nivel']} · {d['verificador']} "
                          f"({d['camada']}) · método: {d['metodo']} · ação: {d['acao']}\n"
                          f"- Afirmação: {d['titulo']}\n- {d['conflito']}\n- Evidências:\n{ev}")
            arquivos |= {s[0] for s in _spans(d)}
        trechos = []
        for arquivo in sorted(arquivos):
            linhas = ler_obra(arquivo).split("\n")
            usadas = sorted({ln for d in caso["diagnosticos"] for (a, i, f) in _spans(d) if a == arquivo
                             for ln in range(max(1, i - 15), min(len(linhas), f + 15) + 1)})
            trechos.append(f"#### {arquivo}\n" + "\n".join(f"{ln:>5}| {linhas[ln - 1]}" for ln in usadas))
        texto = _render(modelo, {"CASO": caso["id"], "MOTIVOS": "\n".join(f"- {m}" for m in caso["motivos"]),
                                 "DIAGNOSTICOS": "\n\n".join(blocos), "INTENCOES": intencoes,
                                 "TRECHOS": "\n\n".join(trechos)})
        (PENDENTES / f"{caso['id']}.md").write_text(texto, encoding="utf-8")
        n += 1
    return n


def ingerir(relatorio: dict) -> dict:
    from .extraction import extrair_yaml
    por_imp = {d["impressao"]: d for d in relatorio["diagnosticos"]}
    resumo = {"pareceres": 0, "argumentos_descartados": 0, "recusados": []}
    for resp in sorted(RESPOSTAS.glob("*")) if RESPOSTAS.exists() else []:
        dados = extrair_yaml(resp.read_text(encoding="utf-8"))
        for p in dados.get("pareceres") or []:
            d = por_imp.get(p.get("impressao"))
            if not d:
                resumo["recusados"].append(f"{resp.name}: impressão desconhecida {p.get('impressao')}")
                continue
            v = str(p.get("veredito", "")).upper()
            if v not in VEREDITOS:
                resumo["recusados"].append(f"{p['impressao']}: veredito inválido {v}")
                continue
            novo = p.get("novo_nivel")
            if novo and (novo == "ERROR" or ORDEM.get(novo, 9) > ORDEM[d["nivel"]]):
                # Nunca sobe um diagnóstico, muito menos para ERROR (seção 6.5).
                resumo["recusados"].append(f"{p['impressao']}: tentou subir o nível para {novo}")
                novo = None
            validos = []
            for arg in p.get("argumentos") or []:
                arquivo = arg.get("arquivo")
                try:
                    ok = arquivo and ancorar(arg.get("citacao", ""), ler_obra(arquivo))["ok"]
                except ErroDeProjeto:
                    ok = False
                if ok:
                    validos.append(arg)
                else:
                    resumo["argumentos_descartados"] += 1   # argumento sem citação não vale
            salvar_yaml(RAIZ / "reviews" / f"{p['impressao']}.yaml", {
                "impressao": p["impressao"], "veredito": v, "resumo": p.get("resumo", ""),
                "novo_nivel": novo, "argumentos": validos, "arquivo_resposta": resp.name,
            })
            resumo["pareceres"] += 1
    return resumo
