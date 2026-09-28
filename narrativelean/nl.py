#!/usr/bin/env python3
"""NarrativeLean — verificadores para documentos narrativos.

    python narrativelean/nl.py validar
    python narrativelean/nl.py extrair preparar            # pacotes para o operador
    python narrativelean/nl.py extrair rodar --comando "claude -p"
    python narrativelean/nl.py extrair ingerir
    python narrativelean/nl.py verificar                   # relatório em reports/<versão>/

Ver narrativelean/README.md para o fluxo completo e CLAUDE.md para as regras
de operação.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from nlean import advocate, contracts, extraction, metrics, operator, report  # noqa: E402
from nlean.canon import Canon, caminho as caminho_canon, carregar as carregar_canon  # noqa: E402
from nlean.extraction import extrair_yaml  # noqa: E402
from nlean.io import (RAIZ, ErroDeProjeto, carregar_yaml, ler_obra, projeto,  # noqa: E402
                      salvar_yaml, slug, versao_atual)
from nlean.schema import carregar_vocabulario, normalizar_predicado  # noqa: E402
from nlean.segment import Unidade, classificar  # noqa: E402
from nlean.validate import validar  # noqa: E402
from nlean.verifiers import rules  # noqa: E402

FILAS = {
    "principal": (extraction.PENDENTES, extraction.RESPOSTAS),
    "golden": (RAIZ / "work" / "golden" / "pendentes", RAIZ / "work" / "golden" / "respostas"),
    "advogado": (advocate.PENDENTES, advocate.RESPOSTAS),
    "baseline": (RAIZ / "work" / "baseline" / "pendentes", RAIZ / "work" / "baseline" / "respostas"),
    "retrotraducao": (RAIZ / "work" / "retrotraducao" / "pendentes",
                      RAIZ / "work" / "retrotraducao" / "respostas"),
}


def mostrar(dados) -> None:
    print(json.dumps(dados, ensure_ascii=False, indent=2, default=str))


def relatorio_json(versao: str | None, nome: str = "relatorio") -> dict:
    p = RAIZ / "reports" / (versao or versao_atual()) / f"{nome}.json"
    if not p.exists():
        raise ErroDeProjeto(f"{p} não existe — rode `nl.py verificar` antes")
    return json.loads(p.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------

def cmd_validar(a) -> int:
    erros, avisos = validar()
    for e in erros:
        print(f"ERRO   {e}")
    for w in avisos:
        print(f"aviso  {w}")
    print(f"\n{len(erros)} erro(s), {len(avisos)} aviso(s).")
    return 1 if erros else 0


def cmd_classificar(a) -> int:
    alvos = a.arquivos or ([p.name for p in sorted((RAIZ / "..").resolve().glob("*.md"))
                            if p.name not in ("index.md", "README.md")] if a.todos else [])
    if not alvos:
        print("informe arquivos ou --todos")
        return 1
    for arq in alvos:
        c = classificar(ler_obra(arq))
        pergunta = "  ← declare em doctypes.yaml" if c["confianca"] == "baixa" else ""
        print(f"{arq:45} {c['tipo']:11} {c['confianca']:6}{pergunta}")
        print(f"{'':45} evidência: {c['evidencias'][0]!r}")
    return 0


def cmd_unidades(a) -> int:
    unidades, classe = extraction.unidades_do_documento(a.arquivo)
    print(f"{a.arquivo}: {classe['tipo']} ({classe['fonte']}), {len(unidades)} unidades")
    for u in unidades:
        print(f"  {u.id:60} l.{u.linha_inicio}–{u.linha_fim}  [{u.tipo}]")
    return 0


def cmd_vocab_sincronizar(a) -> int:
    """Acrescenta ao vocabulário os predicados que as regras do canon citam."""
    vocab = carregar_vocabulario()
    registrados = {normalizar_predicado(k) for k in vocab["predicados"]}
    novos = []
    for r in Canon.carregar().lista_regras():
        pred = (r.get("aplica_a") or {}).get("predicado")
        if pred and normalizar_predicado(pred) not in registrados:
            vocab["predicados"][normalizar_predicado(pred)] = {
                "tipo": "evento", "objeto": "texto",
                "descricao": f"(da regra {r['id']}) {r.get('descricao', '')}".strip()}
            registrados.add(normalizar_predicado(pred))
            novos.append(pred)
    if novos:
        vocab["versao"] = int(vocab.get("versao", 1)) + 1
        caminho = RAIZ / "schema" / "predicados.yaml"
        cabecalho = caminho.read_text(encoding="utf-8").split("\nversao:")[0]
        import yaml
        caminho.write_text(cabecalho + "\n" + yaml.safe_dump(vocab, allow_unicode=True,
                                                             sort_keys=False, width=100),
                           encoding="utf-8")
    print(f"predicados novos: {novos or 'nenhum'}; versão do vocabulário: {vocab['versao']}")
    if novos:
        print("A próxima `extrair preparar` gera só pacotes de complemento para eles.")
    return 0


def cmd_extrair_preparar(a) -> int:
    resumo = extraction.preparar(a.arquivos or None, forcar=a.forcar, amostra=a.amostra,
                                 semente=a.semente, vizinhas=not a.sem_vizinhas)
    mostrar(resumo)
    print(f"\nPacotes em {extraction.PENDENTES.relative_to(RAIZ)}/. Rode `extrair rodar` ou "
          f"responda à mão em work/respostas/<pacote>.yaml (ver CLAUDE.md).")
    return 0


def cmd_rodar(a) -> int:
    pasta, respostas = FILAS[a.fila]
    comando = a.comando or projeto().get("operador_padrao")
    if not comando:
        print("informe --comando (ex.: \"claude -p\" ou \"ollama run qwen2.5:14b\")")
        return 1
    mostrar(operator.rodar(comando, a.limite, a.tempo, pasta, respostas))
    return 0


def cmd_extrair_ingerir(a) -> int:
    r = extraction.ingerir(a.operador)
    mostrar(r)
    return 1 if r["erros"] else 0


def cmd_extrair_status(a) -> int:
    for linha in extraction.status():
        mostrar(linha)
    return 0


def cmd_verificar(a) -> int:
    for arq in a.documentos or [d["arquivo"] for d in extraction.documentos_declarados()
                                if not d.get("experimento")]:
        try:
            extraction.montar_fatos(arq)
        except ErroDeProjeto as e:
            print(f"aviso: {e}")
    r = report.gerar(a.versao, a.documentos or None)
    print(f"Relatório: narrativelean/{r['arquivo']}")
    print(f"Contagem: {r['contagem'] or 'nenhum diagnóstico'}")
    for aviso in r["avisos"]:
        print(f"aviso: {aviso}")
    return 0


def cmd_regras_bateria(a) -> int:
    canon = Canon.carregar()
    retro = RAIZ / "reviews" / "retrotraducao"
    for r in canon.lista_regras():
        if a.id and r["id"] != a.id:
            continue
        aut = canon.autoridade_regra(r)
        print(f"\n== {r['id']} — {aut['rigidez']} ({aut['motivo']})")
        print(f"   Texto do autor:   {r.get('descricao', '').strip()}")
        volta = carregar_yaml(retro / f"{r['id']}.yaml")
        if volta:
            print(f"   Tradução de volta: {volta.get('retrotraducao')}")
            if volta.get("estranhezas"):
                print(f"   Estranhezas:      {volta['estranhezas']}")
        for caso in rules.bateria(canon, r):
            print(f"   - {caso['texto']}")
    print("\nSe as consequências estiverem certas, o AUTOR roda `nl.py regras aprovar <ID>`.")
    return 0


def cmd_regras_aprovar(a) -> int:
    dados = carregar_canon("world_rules")
    for i, r in enumerate(dados.get("regras") or []):
        if r.get("id") == a.id:
            dados["regras"][i] = rules.aprovar(r)
            salvar_yaml(caminho_canon("world_rules"), dados)
            print(f"{a.id}: formalização aprovada (hash {dados['regras'][i]['formalizacao']['aprovada_hash']}). "
                  f"Se a forma mudar, a aprovação cai sozinha.")
            return 0
    print(f"regra {a.id} não encontrada")
    return 1


def cmd_regras_retro_preparar(a) -> int:
    canon = Canon.carregar()
    pasta, _ = FILAS["retrotraducao"]
    pasta.mkdir(parents=True, exist_ok=True)
    versao = (projeto().get("prompts") or {}).get("retrotraducao")
    modelo = (RAIZ / "prompts" / f"{versao}.md").read_text(encoding="utf-8")
    import yaml
    n = 0
    for r in canon.lista_regras():
        forma = {k: r.get(k) for k in ("aplica_a", "exige", "proibido", "excecoes") if r.get(k) is not None}
        conceitos = {str(v) for v in (r.get("aplica_a") or {}).values() if v}
        for exc in r.get("excecoes") or []:
            conceitos |= {str(v) for v in exc.values() if isinstance(v, str)}
        linhas = []
        for c in sorted(conceitos):
            for anc in sorted(canon.hierarquia.ancestrais(c) - {canon.hierarquia._chave(c)}):
                linhas.append(f"- {c} é_um {canon.hierarquia.nome(anc)}")
            for des in sorted(canon.hierarquia.descendentes(c) - {canon.hierarquia._chave(c)}):
                linhas.append(f"- {canon.hierarquia.nome(des)} é_um {c}")
        texto = extraction._render(modelo, {
            "REGRA": r["id"], "FORMA": yaml.safe_dump(forma, allow_unicode=True, sort_keys=False).strip(),
            "HIERARQUIA": "\n".join(linhas) or "(nenhuma)"})
        (pasta / f"retro-{r['id']}.md").write_text(texto, encoding="utf-8")
        n += 1
    print(f"{n} pacote(s) de tradução de volta. Cada um vai para uma sessão que NÃO viu o texto original.")
    return 0


def cmd_regras_retro_ingerir(a) -> int:
    _, respostas = FILAS["retrotraducao"]
    n = 0
    for p in sorted(respostas.glob("retro-*")) if respostas.exists() else []:
        rid = p.stem.removeprefix("retro-")
        dados = extrair_yaml(p.read_text(encoding="utf-8"))
        salvar_yaml(RAIZ / "reviews" / "retrotraducao" / f"{rid}.yaml",
                    {"regra": rid, "retrotraducao": dados.get("retrotraducao"),
                     "estranhezas": dados.get("estranhezas")})
        n += 1
    print(f"{n} tradução(ões) de volta registradas. Compare em `nl.py regras bateria`.")
    return 0


def cmd_canon_aprovar(a) -> int:
    dados = carregar_canon(a.arquivo)
    for chave in ("personagens", "regras", "eventos"):
        for item in dados.get(chave) or []:
            if a.item in (item.get("id"), item.get("nome")):
                item.pop("proposto_por", None)
                salvar_yaml(caminho_canon(a.arquivo), dados)
                print(f"{a.item}: agora é canon do autor.")
                return 0
    print(f"{a.item} não encontrado em canon/{a.arquivo}.yaml")
    return 1


def cmd_suprimir(a) -> int:
    from nlean.diagnostics import suprimir
    rel = relatorio_json(a.versao)
    for d in rel["diagnosticos"]:
        if d["impressao"] == a.impressao or d["id"] == a.impressao:
            e = suprimir(d, a.motivo)
            print(f"suprimido: {e['titulo']} — enquanto o trecho citado não mudar.")
            return 0
    print("diagnóstico não encontrado no último relatório")
    return 1


def cmd_advogado_preparar(a) -> int:
    n = advocate.preparar(relatorio_json(a.versao))
    print(f"{n} caso(s) para o advogado do diabo em {advocate.PENDENTES.relative_to(RAIZ)}/")
    return 0


def cmd_advogado_ingerir(a) -> int:
    mostrar(advocate.ingerir(relatorio_json(a.versao)))
    print("Rode `nl.py verificar` para ver os pareceres no relatório.")
    return 0


def cmd_golden_preparar(a) -> int:
    pasta, _ = FILAS["golden"]
    pasta.mkdir(parents=True, exist_ok=True)
    modelo, _ = extraction._prompt("aberta")
    vocab = carregar_vocabulario()
    n = 0
    for item in metrics.carregar_golden():
        tipo = item.get("tipo_documento", "prosa")
        texto = extraction._render(modelo, {
            "ARQUIVO": f"golden/{item['_arquivo']}", "UNIDADE": item["id"], "TITULO": item["id"],
            "TIPO_DOCUMENTO": tipo, "ORIENTACAO_TIPO": extraction.ORIENTACAO_TIPO[tipo],
            "VOCABULARIO": extraction._texto_vocabulario(vocab), "SOMENTE": "",
            "EVENTOS_CANON": "(nenhum)", "TEXTO": item["texto"].rstrip("\n")})
        (pasta / f"{item['id']}.md").write_text(texto, encoding="utf-8")
        n += 1
    print(f"{n} pacote(s) do golden set. O prompt é o MESMO da produção: mede-se o que roda.")
    return 0


def cmd_golden_pontuar(a) -> int:
    from nlean.schema import predicados_registrados
    _, respostas = FILAS["golden"]
    registrados = predicados_registrados()
    extraidos, rejeitados = {}, 0
    itens = metrics.carregar_golden()
    for item in itens:
        resp = next((p for p in (respostas / f"{item['id']}.yaml", respostas / f"{item['id']}.md")
                     if p.exists()), None)
        if not resp:
            continue
        linhas = item["texto"].rstrip("\n").split("\n")
        u = Unidade(id=item["id"], arquivo=f"golden/{item['_arquivo']}", titulo=item["id"],
                    linha_inicio=1, linha_fim=len(linhas), linhas=linhas,
                    tipo=item.get("tipo_documento", "prosa"))
        fatos = []
        for bruto in extrair_yaml(resp.read_text(encoding="utf-8")).get("fatos") or []:
            f, livre, rej = extraction.validar_fato(bruto, u, registrados, "aberta")
            fatos += [f] if f else ([livre] if livre else [])
            rejeitados += bool(rej)
        extraidos[item["id"]] = fatos
    respondidos = [i for i in itens if i["id"] in extraidos]
    r = metrics.pontuar_golden(extraidos, respondidos)
    r["itens"] = len(itens)
    r["respondidos"] = len(respondidos)
    r["citacoes_rejeitadas"] = rejeitados
    if len(itens) < 30:
        r["aviso"] = f"o golden set tem {len(itens)} itens; a Fase 0 pede cerca de 30, escritos pelo autor"
    salvar_yaml(RAIZ / "reports" / "golden.yaml", r)
    mostrar(r)
    return 0


def cmd_plantar(a) -> int:
    if a.acao == "status":
        mostrar(metrics.status_plantio(a.nome))
    elif a.acao == "aplicar":
        r = metrics.aplicar_plantio(a.nome)
        mostrar(r)
        print(f"\nDeclare a cópia em doctypes.yaml com o mesmo tipo da fonte e `experimento: true`,\n"
              f"depois: extrair preparar {r['copia']} → rodar → ingerir → "
              f"verificar --documentos {r['copia']} → plantar pontuar {a.nome}")
    else:
        dados, _ = metrics._plantio(a.nome)
        gab = carregar_yaml(RAIZ / "tests" / "seeded_errors" / a.nome / "gabarito_plantado.yaml", {})
        nome = "relatorio-" + slug(gab["copia"].removesuffix(".md"))[:80]
        r = metrics.pontuar_plantio(a.nome, relatorio_json(a.versao, nome))
        salvar_yaml(RAIZ / "reports" / f"plantio-{a.nome}.yaml", r)
        mostrar(r)
    return 0


def cmd_gabarito(a) -> int:
    if a.acao == "amostrar":
        unidades, _ = extraction.unidades_do_documento(a.arquivo)
        r = metrics.amostrar(a.arquivo, a.n, a.semente, unidades)
        print(f"{len(r['unidades'])} unidades sorteadas em "
              f"{metrics.pasta_gabarito(a.arquivo).relative_to(RAIZ)}/amostra.yaml")
    elif a.acao == "juntar":
        mostrar(metrics.juntar(a.arquivo, relatorio_json(a.versao)))
    else:
        r = metrics.pontuar_pool(a.arquivo)
        salvar_yaml(metrics.pasta_gabarito(a.arquivo) / "resultado.yaml", r)
        mostrar(r)
    return 0


def cmd_baseline(a) -> int:
    pasta, respostas = FILAS["baseline"]
    nome = slug(a.arquivo.removesuffix(".md"))
    if a.acao == "preparar":
        pasta.mkdir(parents=True, exist_ok=True)
        versao = (projeto().get("prompts") or {}).get("baseline")
        modelo = (RAIZ / "prompts" / f"{versao}.md").read_text(encoding="utf-8")
        texto = extraction._render(modelo, {"ARQUIVO": a.arquivo, "TEXTO": ler_obra(a.arquivo)})
        (pasta / f"{nome}.md").write_text(texto, encoding="utf-8")
        print(f"pacote do baseline: {(pasta / f'{nome}.md').relative_to(RAIZ)}")
    else:
        resp = next((p for p in (respostas / f"{nome}.yaml", respostas / f"{nome}.md") if p.exists()), None)
        if not resp:
            print("sem resposta do baseline")
            return 1
        mostrar(metrics.ingerir_baseline(a.arquivo, extrair_yaml(resp.read_text(encoding="utf-8"))))
    return 0


def cmd_contratos(a) -> int:
    problemas = contracts.validar()
    dados = contracts.gerar_conflitos()
    for p in problemas:
        print(f"ERRO   {p}")
    print(f"lens_conflicts.yaml gerado com {len(dados['tensoes'])} tensão(ões).")
    return 1 if problemas else 0


# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="nl.py", description="NarrativeLean")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("validar").set_defaults(f=cmd_validar)
    p = sub.add_parser("classificar")
    p.add_argument("arquivos", nargs="*")
    p.add_argument("--todos", action="store_true")
    p.set_defaults(f=cmd_classificar)
    p = sub.add_parser("unidades")
    p.add_argument("arquivo")
    p.set_defaults(f=cmd_unidades)

    v = sub.add_parser("vocab").add_subparsers(dest="sub", required=True)
    v.add_parser("sincronizar").set_defaults(f=cmd_vocab_sincronizar)

    e = sub.add_parser("extrair").add_subparsers(dest="sub", required=True)
    p = e.add_parser("preparar")
    p.add_argument("arquivos", nargs="*")
    p.add_argument("--forcar", action="store_true")
    p.add_argument("--amostra", type=float, default=0.0,
                   help="fração das unidades inalteradas reextraída do zero (seção 9)")
    p.add_argument("--semente", type=int, default=None)
    p.add_argument("--sem-vizinhas", action="store_true")
    p.set_defaults(f=cmd_extrair_preparar)
    p = e.add_parser("rodar")
    p.add_argument("--comando")
    p.add_argument("--fila", choices=sorted(FILAS), default="principal")
    p.add_argument("--limite", type=int)
    p.add_argument("--tempo", type=int, default=900)
    p.set_defaults(f=cmd_rodar)
    p = e.add_parser("ingerir")
    p.add_argument("--operador", default="manual")
    p.set_defaults(f=cmd_extrair_ingerir)
    e.add_parser("status").set_defaults(f=cmd_extrair_status)

    p = sub.add_parser("verificar")
    p.add_argument("--versao")
    p.add_argument("--documentos", nargs="*")
    p.set_defaults(f=cmd_verificar)

    r = sub.add_parser("regras").add_subparsers(dest="sub", required=True)
    p = r.add_parser("bateria")
    p.add_argument("id", nargs="?")
    p.set_defaults(f=cmd_regras_bateria)
    p = r.add_parser("aprovar", help="SÓ O AUTOR roda isto")
    p.add_argument("id")
    p.set_defaults(f=cmd_regras_aprovar)
    rt = r.add_parser("retrotraduzir").add_subparsers(dest="acao", required=True)
    rt.add_parser("preparar").set_defaults(f=cmd_regras_retro_preparar)
    rt.add_parser("ingerir").set_defaults(f=cmd_regras_retro_ingerir)

    c = sub.add_parser("canon").add_subparsers(dest="sub", required=True)
    p = c.add_parser("aprovar", help="SÓ O AUTOR roda isto")
    p.add_argument("arquivo", choices=["characters", "world_rules", "timeline"])
    p.add_argument("item")
    p.set_defaults(f=cmd_canon_aprovar)

    p = sub.add_parser("suprimir")
    p.add_argument("impressao", help="impressão ou id (TL-001) do diagnóstico")
    p.add_argument("--motivo", required=True)
    p.add_argument("--versao")
    p.set_defaults(f=cmd_suprimir)

    ad = sub.add_parser("advogado").add_subparsers(dest="sub", required=True)
    for nome, f in (("preparar", cmd_advogado_preparar), ("ingerir", cmd_advogado_ingerir)):
        p = ad.add_parser(nome)
        p.add_argument("--versao")
        p.set_defaults(f=f)

    g = sub.add_parser("golden").add_subparsers(dest="sub", required=True)
    g.add_parser("preparar").set_defaults(f=cmd_golden_preparar)
    g.add_parser("pontuar").set_defaults(f=cmd_golden_pontuar)

    p = sub.add_parser("plantar")
    p.add_argument("acao", choices=["status", "aplicar", "pontuar"])
    p.add_argument("nome")
    p.add_argument("--versao")
    p.set_defaults(f=cmd_plantar)

    p = sub.add_parser("gabarito")
    p.add_argument("acao", choices=["amostrar", "juntar", "pontuar"])
    p.add_argument("arquivo")
    p.add_argument("--n", type=int, default=5)
    p.add_argument("--semente", type=int, default=1)
    p.add_argument("--versao")
    p.set_defaults(f=cmd_gabarito)

    p = sub.add_parser("baseline")
    p.add_argument("acao", choices=["preparar", "ingerir"])
    p.add_argument("arquivo")
    p.set_defaults(f=cmd_baseline)

    sub.add_parser("contratos").set_defaults(f=cmd_contratos)

    a = ap.parse_args(argv)
    try:
        return a.f(a)
    except ErroDeProjeto as erro:
        print(f"ERRO: {erro}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
