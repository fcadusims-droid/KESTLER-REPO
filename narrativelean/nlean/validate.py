"""`nl.py validar`: confere tudo o que o autor edita, antes de qualquer rodada.

Erro de configuração descoberto no meio de uma extração custa chamadas; aqui
ele custa zero. ERRO impede a rodada; AVISO só informa.
"""

from __future__ import annotations

from . import contracts
from .canon import Canon, carregar
from .io import RAIZ, ErroDeProjeto, caminho_obra, carregar_yaml, normalizar_nome, projeto
from .schema import RIGIDEZ, TIPOS_DOCUMENTO, TIPOS_FATO, predicados_registrados

OBJETOS = {"texto", "pessoa", "lugar", "inteiro", "evento", "nenhum"}
ESTADOS_LENTE = {"sim", "nao", "adaptada"}
CHAVES_EXCECAO = {"sujeito_e_um", "predicado_e_um", "qualificador"}


def validar() -> tuple[list[str], list[str]]:
    erros: list[str] = []
    avisos: list[str] = []

    try:
        p = projeto()
    except ErroDeProjeto as e:
        return [str(e)], []
    for nome, versao in (p.get("prompts") or {}).items():
        if not (RAIZ / "prompts" / f"{versao}.md").exists():
            erros.append(f"project.yaml: prompts.{nome} → prompts/{versao}.md não existe")
    for chave in ("aberta", "dirigida", "baseline", "retrotraducao", "advogado"):
        if chave not in (p.get("prompts") or {}):
            erros.append(f"project.yaml: falta prompts.{chave}")
    if not (RAIZ / "schema" / "VERSION").exists():
        erros.append("schema/VERSION não existe")

    try:
        vocab = carregar_yaml(RAIZ / "schema" / "predicados.yaml", {}) or {}
        if not isinstance(vocab.get("versao"), int):
            erros.append("schema/predicados.yaml: `versao` precisa ser um inteiro")
        for nome, info in (vocab.get("predicados") or {}).items():
            info = info or {}
            if info.get("tipo") not in TIPOS_FATO:
                erros.append(f"predicado {nome}: tipo inválido {info.get('tipo')!r}")
            if info.get("objeto", "texto") not in OBJETOS:
                erros.append(f"predicado {nome}: objeto inválido {info.get('objeto')!r}")
        registrados = predicados_registrados(vocab)
    except ErroDeProjeto as e:
        erros.append(str(e))
        registrados = {}

    # doctypes
    for d in (carregar_yaml(RAIZ / "doctypes.yaml", {}) or {}).get("documentos") or []:
        arq = d.get("arquivo")
        if not arq:
            erros.append("doctypes.yaml: documento sem `arquivo`")
            continue
        if not caminho_obra(arq).exists():
            erros.append(f"doctypes.yaml: {arq} não existe")
        if d.get("tipo") and d["tipo"] not in TIPOS_DOCUMENTO:
            erros.append(f"doctypes.yaml: {arq}: tipo inválido {d['tipo']}")
        if d.get("canon") and d.get("rigidez") not in RIGIDEZ:
            erros.append(f"doctypes.yaml: {arq} promovida a canon sem rigidez STRICT/FLEXIBLE")
        for s in d.get("secoes") or []:
            if s.get("tipo") not in TIPOS_DOCUMENTO:
                erros.append(f"doctypes.yaml: {arq}: seção com tipo inválido {s.get('tipo')}")

    # canon
    try:
        canon = Canon.carregar()
    except ErroDeProjeto as e:
        return erros + [str(e)], avisos

    pers = carregar("characters")
    if pers.get("personagens") and pers.get("rigidez_padrao") not in RIGIDEZ:
        erros.append("canon/characters.yaml: declare `rigidez_padrao: STRICT` ou `FLEXIBLE` "
                     "(a rigidez é decisão do autor, o sistema não escolhe)")
    nomes = [normalizar_nome(x.get("nome")) for x in pers.get("personagens") or []]
    for n in {n for n in nomes if nomes.count(n) > 1}:
        erros.append(f"canon/characters.yaml: personagem repetido: {n}")

    regras = carregar("world_rules")
    if regras.get("regras") and regras.get("rigidez_padrao") not in RIGIDEZ:
        erros.append("canon/world_rules.yaml: declare `rigidez_padrao`")
    ids = [r.get("id") for r in regras.get("regras") or []]
    for i in {i for i in ids if ids.count(i) > 1}:
        erros.append(f"canon/world_rules.yaml: id repetido: {i}")
    for r in regras.get("regras") or []:
        rid = r.get("id") or "?"
        if not r.get("id"):
            erros.append("canon/world_rules.yaml: regra sem id")
        if r.get("rigidez") and r["rigidez"] not in RIGIDEZ:
            erros.append(f"{rid}: rigidez inválida {r['rigidez']}")
        pred = (r.get("aplica_a") or {}).get("predicado")
        if not pred:
            erros.append(f"{rid}: aplica_a.predicado é obrigatório")
        elif pred.replace("-", "_") not in registrados and not canon.hierarquia.descendentes(pred) - {pred}:
            avisos.append(f"{rid}: o predicado {pred!r} não está no vocabulário — rode `nl.py vocab sincronizar`")
        if not isinstance(r.get("exige") or {}, dict):
            erros.append(f"{rid}: `exige` precisa ser um mapa")
        if not r.get("exige") and not r.get("proibido"):
            avisos.append(f"{rid}: sem `exige` nem `proibido`, a regra nunca dispara")
        for exc in r.get("excecoes") or []:
            if not isinstance(exc, dict) or not set(exc) <= CHAVES_EXCECAO or not exc:
                erros.append(f"{rid}: exceção inválida {exc!r} (use {sorted(CHAVES_EXCECAO)})")
        aut = canon.autoridade_regra(r)
        if not aut["autoritativo"]:
            avisos.append(f"{rid}: {aut['motivo']} — vale como FLEXIBLE até o autor aprovar")

    for ciclo in canon.hierarquia.ciclos():
        erros.append(f"canon/entidades.yaml: ciclo na hierarquia é_um envolvendo {ciclo}")

    tl = carregar("timeline")
    eids = [e.get("id") for e in tl.get("eventos") or []]
    if tl.get("eventos") and tl.get("rigidez_padrao") not in RIGIDEZ:
        erros.append("canon/timeline.yaml: declare `rigidez_padrao`")
    for e in tl.get("eventos") or []:
        dep = (e.get("depois_de") or {}).get("evento")
        if dep and dep not in eids:
            erros.append(f"canon/timeline.yaml: {e.get('id')} depende de evento inexistente {dep}")

    for bloco in (pers, regras, tl):
        for item in (bloco.get("personagens") or bloco.get("regras") or bloco.get("eventos") or []):
            if str(item.get("proposto_por", "")).casefold() == "claude":
                avisos.append(f"canon: {item.get('nome') or item.get('id')} proposto pelo Claude, "
                              f"aguardando aprovação do autor")

    # lentes e contratos
    lentes = (carregar_yaml(RAIZ / "lenses.yaml", {}) or {}).get("lentes") or {}
    todos_contratos = contracts.carregar()
    for lente, cfg in lentes.items():
        for tipo, estado in (cfg or {}).items():
            if tipo not in TIPOS_DOCUMENTO:
                erros.append(f"lenses.yaml: {lente}: tipo desconhecido {tipo}")
            if estado not in ESTADOS_LENTE:
                erros.append(f"lenses.yaml: {lente}.{tipo}: estado {estado!r} (use sim, nao ou adaptada)")
        c = todos_contratos.get(lente)
        if c and c.get("estado") != "implementado" and any(v != "nao" for v in (cfg or {}).values()):
            avisos.append(f"lenses.yaml: a lente {lente} está ativa mas ainda não foi implementada "
                          f"(estado: {c.get('estado')}) — não roda")
    erros += contracts.validar(todos_contratos)

    for s in (carregar_yaml(RAIZ / "suppressions.yaml", {}) or {}).get("supressoes") or []:
        if not s.get("motivo"):
            erros.append(f"suppressions.yaml: supressão {s.get('impressao')} sem motivo")
        if not s.get("trecho_hash"):
            erros.append(f"suppressions.yaml: supressão {s.get('impressao')} sem trecho_hash")
    return erros, avisos
