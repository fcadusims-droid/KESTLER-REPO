"""Roda os verificadores ativos e escreve o relatório (seções 4.3 e 7).

O topo do relatório é o que mais importa conferir e o que menos se confere:
a classificação de cada documento (um tipo errado muda todos os diagnósticos),
as unidades que NÃO foram extraídas, as citações rejeitadas e as divergências
entre extração aberta e dirigida. Um relatório sem diagnósticos é "nenhuma
violação detectada contra o canon atual, nas unidades extraídas" — e o topo diz
quais eram essas unidades.
"""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone

from .canon import Canon
from .diagnostics import Diagnostico, aplicar_supressoes
from .extraction import carregar_fatos, documentos_declarados, unidades_do_documento
from .io import RAIZ, ErroDeProjeto, carregar_yaml, salvar_json, slug, versao_atual
from .verifiers import attributes, references, rules, timeline

ORDEM_NIVEL = {"ERROR": 0, "WARNING": 1, "SUGGESTION": 2}
ORDEM_VEREDITO = {None: 0, "MANTER": 0, "REENQUADRAR": 1, "REBAIXAR": 2, "CONTESTAR": 3}


def lentes() -> dict:
    return (carregar_yaml(RAIZ / "lenses.yaml", {}) or {}).get("lentes") or {}


def tipos_ativos(lente: str) -> set[str]:
    """Tipos de documento em que a lente roda. `adaptada` conta como ativa só
    onde a adaptação existe; em `ramificado` a verificação por estado ainda não
    foi construída, então fica de fora — e o relatório diz isso."""
    cfg = lentes().get(lente) or {}
    ativos = set()
    for tipo, estado in cfg.items():
        if estado in ("sim", True) or (estado == "adaptada" and tipo != "ramificado"):
            ativos.add(tipo)
    return ativos


def _filtrar(fatos_por_doc: dict, tipos: set[str]) -> dict:
    return {doc: {**d, "fatos": [f for f in d.get("fatos", []) if f.get("tipo_documento") in tipos]}
            for doc, d in fatos_por_doc.items()}


def gerar(versao: str | None = None, documentos: list[str] | None = None) -> dict:
    """Relatório de uma versão. Sem `documentos`, verifica todos os declarados
    exceto os de experimento (cópias com erros plantados), que só rodam quando
    pedidos pelo nome — misturá-los com a obra real poria a cópia e o original
    a se contradizerem um ao outro."""
    versao = versao or versao_atual()
    canon = Canon.carregar()
    if documentos:
        declarados = list(documentos)
    else:
        declarados = [d["arquivo"] for d in documentos_declarados() if not d.get("experimento")]
    if not declarados:
        raise ErroDeProjeto("doctypes.yaml não declara nenhum documento")
    fatos = {k: v for k, v in carregar_fatos(versao).items() if k in declarados}

    avisos = []
    diags: list[Diagnostico] = []

    tl, indeterminadas = timeline.verificar(_filtrar(fatos, tipos_ativos("timeline")), canon)
    diags += tl
    rm, lacunas = rules.verificar_regras(_filtrar(fatos, tipos_ativos("regras_do_mundo")), canon)
    diags += rm
    diags += attributes.verificar(_filtrar(fatos, tipos_ativos("atributos")), canon)
    rr, regras_ignoradas = rules.regra_x_regra(canon)
    diags += rr

    unidades_por_doc = {}
    for arquivo in declarados:
        try:
            unidades_por_doc[arquivo], _ = unidades_do_documento(arquivo)
        except ErroDeProjeto as erro:
            avisos.append(str(erro))
    ref_tipos = tipos_ativos("referencia_sem_definicao")
    if ref_tipos:
        diags += references.verificar(unidades_por_doc, canon, tuple(ref_tipos))

    for d in declarados:
        if d not in fatos:
            avisos.append(f"{d}: sem fatos extraídos na versão {versao} — nada deste documento foi "
                          f"verificado pelos verificadores que dependem de extração.")
    if any(f.get("tipo_documento") == "ramificado" for doc in fatos.values() for f in doc.get("fatos", [])):
        avisos.append("documentos ramificados: a verificação por estado alcançável ainda não existe; "
                      "os fatos deles ficaram fora dos verificadores formais.")

    _anexar_revisoes(diags)
    expiradas = aplicar_supressoes(diags)
    diags.sort(key=lambda d: (d.suprimido, ORDEM_NIVEL[d.nivel],
                              ORDEM_VEREDITO.get((d.revisao or {}).get("veredito"), 0),
                              d.verificador, d.evidencias[0].arquivo if d.evidencias else "",
                              d.evidencias[0].linha_inicio if d.evidencias else 0))
    contadores: Counter = Counter()
    for d in diags:
        contadores[d.prefixo] += 1
        d.id = f"{d.prefixo}-{contadores[d.prefixo]:03d}"

    relatorio = {
        "versao": versao, "gerado_em": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "documentos": {doc: _resumo_doc(dados) for doc, dados in fatos.items()},
        "avisos": avisos,
        "diagnosticos": [d.para_json() for d in diags],
        "indeterminadas": indeterminadas,
        "lacunas": lacunas,
        "regras_fora_do_solver": regras_ignoradas,
        "supressoes_expiradas": expiradas,
        "contagem": dict(Counter(d.nivel for d in diags if not d.suprimido)),
    }
    nome = "relatorio" if not documentos else "relatorio-" + "-".join(
        slug(d.removesuffix(".md")) for d in documentos)[:80]
    pasta = RAIZ / "reports" / versao
    relatorio["arquivo"] = f"reports/{versao}/{nome}.md"
    salvar_json(pasta / f"{nome}.json", relatorio)
    (pasta / f"{nome}.md").write_text(_markdown(relatorio, diags), encoding="utf-8")
    return relatorio


def _resumo_doc(dados: dict) -> dict:
    motivos = Counter(r.get("motivo", "?") for r in dados.get("rejeitados", []))
    return {
        "classificacao": dados.get("classificacao"),
        "unidades": dados.get("unidades"),
        "nao_extraidas": dados.get("nao_extraidas", []),
        "fatos": len(dados.get("fatos", [])),
        "por_modo": dict(Counter(f["modo"] for f in dados.get("fatos", []))),
        "predicado_livre": [{"predicado": p.get("predicado_original"), "citacao": p.get("citacao"),
                             "local": p.get("local")} for p in dados.get("predicado_livre", [])],
        "rejeitados": len(dados.get("rejeitados", [])),
        "rejeitados_por_motivo": dict(motivos),
        "divergencias": dados.get("divergencias", []),
        "estabilidade": dados.get("estabilidade", []),
    }


def _anexar_revisoes(diags: list[Diagnostico]) -> None:
    pasta = RAIZ / "reviews"
    for d in diags:
        r = carregar_yaml(pasta / f"{d.impressao}.yaml")
        if r:
            d.revisao = r


def _markdown(rel: dict, diags: list[Diagnostico]) -> str:
    L = [f"# Relatório NarrativeLean — {rel['versao']}", "",
         f"Gerado em {rel['gerado_em']}.", ""]
    L += ["## 1. Classificação dos documentos (confira primeiro)", "",
          "| Documento | Tipo | Fonte | Confiança | Unidades | Não extraídas | Fatos |",
          "|---|---|---|---|---|---|---|"]
    for doc, r in rel["documentos"].items():
        c = r["classificacao"] or {}
        L.append(f"| {doc} | {c.get('tipo')} | {c.get('fonte')} | {c.get('confianca')} | "
                 f"{r['unidades']} | {len(r['nao_extraidas'])} | {r['fatos']} |")
    L.append("")
    if rel["avisos"]:
        L += ["**Avisos:**", ""] + [f"- {a}" for a in rel["avisos"]] + [""]

    L += ["## 2. Qualidade da extração", ""]
    for doc, r in rel["documentos"].items():
        L.append(f"### {doc}")
        L.append(f"- Fatos por modo: {r['por_modo'] or '—'}")
        L.append(f"- Citações rejeitadas (não encontradas no texto ou inválidas): {r['rejeitados']}"
                 + (f" — {r['rejeitados_por_motivo']}" if r["rejeitados"] else ""))
        L.append(f"- Divergências entre extração aberta e dirigida: {len(r['divergencias'])}")
        for dv in r["divergencias"][:15]:
            L.append(f"  - {dv['unidade']} · {dv['pergunta']} · {dv['tipo']}"
                     + (f" · l.{dv['linha']}: \"{dv.get('citacao', '')}\"" if dv.get("linha") else ""))
        if r["nao_extraidas"]:
            L.append(f"- **Unidades sem extração ({len(r['nao_extraidas'])}) — NÃO verificadas:**")
            for n in r["nao_extraidas"][:20]:
                L.append(f"  - {n['unidade']} (l.{n['linhas'][0]}–{n['linhas'][1]}): falta {n['falta']}")
        if r["predicado_livre"]:
            L.append(f"- `predicado_livre` ({len(r['predicado_livre'])}) — candidatos ao vocabulário:")
            contagem = Counter(p["predicado"] for p in r["predicado_livre"])
            for p, n in contagem.most_common(20):
                L.append(f"  - `{p}` × {n}")
        if r["estabilidade"]:
            L.append("- Reextração da amostra (concordância com o cache):")
            for e in r["estabilidade"]:
                L.append(f"  - {e['unidade']}: jaccard {e['jaccard']} ({e['em_comum']} de "
                         f"{max(e['cache'], e['nova'])})")
        L.append("")
    if rel["lacunas"]:
        L += [f"**Lacunas ({len(rel['lacunas'])}):** fatos a que uma regra se aplica, mas sem o "
              f"qualificador que ela exige. Não é violação — é extração incompleta:", ""]
        for lac in rel["lacunas"][:20]:
            L.append(f"- {lac['regra']} · `{lac['qualificador']}` · {lac['local']['arquivo']} "
                     f"l.{lac['local']['linha_inicio']}: \"{lac['citacao']}\"")
        L.append("")
    if rel["indeterminadas"]:
        L += [f"**Datas indeterminadas ({len(rel['indeterminadas'])})** — nunca erro:", ""]
        for i in rel["indeterminadas"][:20]:
            L.append(f"- {i['local']['arquivo']} l.{i['local']['linha_inicio']}: {i['motivo']} — "
                     f"\"{i['citacao']}\"")
        L.append("")
    if rel["regras_fora_do_solver"]:
        L += ["**Regras fora do regra×regra** (aguardando aprovação do autor):", ""]
        L += [f"- {r}" for r in rel["regras_fora_do_solver"]] + [""]

    ativos = [d for d in diags if not d.suprimido]
    c = rel["contagem"]
    L += ["## 3. Diagnósticos", "",
          f"ERROR: {c.get('ERROR', 0)} · WARNING: {c.get('WARNING', 0)} · "
          f"SUGGESTION: {c.get('SUGGESTION', 0)}", "",
          "Não existe meta de zerar esta lista (seção 8). Um diagnóstico é um indício para o "
          "autor avaliar, não uma ordem de correção.", ""]
    if not ativos:
        L += ["Nenhuma violação detectada contra o canon atual, nas unidades extraídas. "
              "Isso NÃO significa que a obra é consistente: ver seção 1 e 2 acima.", ""]
    for d in ativos:
        L += ["```text", d.formatar(), "```", ""]

    suprimidos = [d for d in diags if d.suprimido]
    if suprimidos or rel["supressoes_expiradas"]:
        L += ["## 4. Supressões", ""]
        for d in suprimidos:
            L.append(f"- {d.id} {d.titulo} — suprimido: {d.supressao.get('motivo')}")
        for s in rel["supressoes_expiradas"]:
            L.append(f"- EXPIRADA (o trecho mudou, o diagnóstico voltou): {s.get('titulo')} — "
                     f"motivo antigo: {s.get('motivo')}")
        L.append("")
    return "\n".join(L)
