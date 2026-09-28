"""Protocolo de extração (seções 5 e 9).

A extração é a única etapa que exige ler linguagem, e é feita por um operador —
o Claude Code, ou qualquer modelo gratuito rodando localmente. Este módulo não
chama modelo nenhum. Ele:

1. prepara PACOTES: um arquivo por tarefa, com exatamente o que o operador pode
   ver (o texto da unidade, o vocabulário, as perguntas) e nada além;
2. recebe as RESPOSTAS e as valida mecanicamente (formato, vocabulário fechado,
   citação literal, linhas calculadas pelo código);
3. guarda o resultado num CACHE cuja chave torna impossível reaproveitar uma
   extração feita com outro texto, outro schema ou outro prompt.

Um pacote por processo é o que torna reais as "sessões separadas" da seção 9:
cada pacote chega a um operador que não viu relatório, edição ou outra unidade.

Duas decisões que divergem do documento, de propósito:

- A chave do cache NÃO inclui a versão do vocabulário. Se incluísse, qualquer
  predicado novo esvaziaria o cache inteiro e obrigaria a reextrair a obra —
  o contrário do que a própria seção 5 pede. A entrada do cache registra quais
  predicados cobriu, e um predicado novo gera só um pacote de complemento.
- A chave inclui o hash do TEXTO do prompt, não só o número da versão. Editar
  o prompt sem subir a versão invalidaria nada; assim, invalida sempre.
"""

from __future__ import annotations

import json
import random
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

import yaml

from . import grounding
from .canon import Canon
from .io import (RAIZ, ErroDeProjeto, carregar_yaml, ler_obra, normalizar_nome, projeto,
                 salvar_json, salvar_yaml, sha, sha_estavel, slug, versao_atual)
from .schema import (MODOS, TIPOS_DOCUMENTO, TIPOS_FATO, carregar_vocabulario,
                     normalizar_confianca, normalizar_modo, normalizar_predicado,
                     predicados_registrados, validar_tempo, versao_schema)
from .segment import Unidade, classificar, segmentar

TRABALHO = RAIZ / "work"
PENDENTES = TRABALHO / "pendentes"
RESPOSTAS = TRABALHO / "respostas"
PROCESSADOS = TRABALHO / "processados"
CACHE = RAIZ / "cache"


class ClassificacaoPendente(ErroDeProjeto):
    """Tipo do documento incerto: pergunta ao autor antes de verificar (seção 4.3)."""


# ---------------------------------------------------------------------------
# Documentos e unidades
# ---------------------------------------------------------------------------

def documentos_declarados() -> list[dict]:
    dados = carregar_yaml(RAIZ / "doctypes.yaml", {}) or {}
    return list(dados.get("documentos") or [])


def entrada_documento(arquivo: str) -> dict:
    for d in documentos_declarados():
        if d.get("arquivo") == arquivo:
            return d
    return {"arquivo": arquivo}


def tipo_do_documento(entrada: dict, texto: str) -> dict:
    """Tipo declarado pelo autor, ou classificado com evidência citada."""
    if entrada.get("tipo"):
        if entrada["tipo"] not in TIPOS_DOCUMENTO:
            raise ErroDeProjeto(f"doctypes.yaml: tipo inválido para {entrada['arquivo']}: "
                                f"{entrada['tipo']}")
        return {"tipo": entrada["tipo"], "fonte": "declarado", "confianca": "alta",
                "evidencias": ["declarado em doctypes.yaml"]}
    c = classificar(texto)
    c["fonte"] = "automatico"
    if c["confianca"] == "baixa":
        raise ClassificacaoPendente(
            f"{entrada['arquivo']}: classificação automática incerta "
            f"(melhor palpite: {c['tipo']}; pontos: {c['pontos']}). "
            f"Declare o tipo em doctypes.yaml antes de verificar.")
    return c


def unidades_do_documento(arquivo: str) -> tuple[list[Unidade], dict]:
    entrada = entrada_documento(arquivo)
    texto = ler_obra(arquivo)
    classe = tipo_do_documento(entrada, texto)
    unidades = segmentar(arquivo, texto, classe["tipo"], int(entrada.get("nivel_titulo", 3)))
    # Documento misto: seções com tipo próprio (seção 4.3).
    for regra in entrada.get("secoes") or []:
        rx = re.compile(regra.get("titulo", "$^"), re.I)
        for u in unidades:
            if rx.search(u.titulo) and regra.get("tipo") in TIPOS_DOCUMENTO:
                u.tipo = regra["tipo"]
    return unidades, classe


# ---------------------------------------------------------------------------
# Perguntas dirigidas e pré-filtro
# ---------------------------------------------------------------------------

def perguntas_ativas(canon: Canon) -> list[dict]:
    base = carregar_yaml(RAIZ / "schema" / "perguntas_base.yaml", {}) or {}
    perguntas = []
    for q in base.get("perguntas") or []:
        perguntas.append({
            "id": q["id"], "grupo": q.get("grupo", "geral"), "pergunta": q["pergunta"].strip(),
            "predicados": list(q.get("predicados") or []),
            "sinais": list(q.get("sinais_regex") or []),
        })
    # Cada regra STRICT do canon gera a sua pergunta estreita (seção 5).
    for r in canon.lista_regras():
        if canon.autoridade_regra(r)["rigidez"] != "STRICT" and not r.get("perguntar_sempre"):
            continue
        texto = r.get("pergunta") or (
            f"Há neste trecho alguma instância do que a regra {r['id']} regula "
            f"({r.get('descricao', '').strip()})? Para cada uma, registre o fato e, nos "
            f"qualificadores, se a exigência {json.dumps(r.get('exige') or {}, ensure_ascii=False)}"
            f" é cumprida, violada ou não dá para saber.")
        pred = (r.get("aplica_a") or {}).get("predicado")
        sinais = [re.escape(s) for s in (r.get("sinais") or [])]
        perguntas.append({
            "id": f"Q-{r['id']}", "grupo": r.get("grupo", "regras"), "pergunta": texto,
            "predicados": [pred] if pred else [], "sinais": sinais,
        })
    for q in perguntas:
        q["hash"] = sha_estavel({k: q[k] for k in ("pergunta", "predicados")})
    return perguntas


def tem_sinal(unidade: Unidade, pergunta: dict) -> bool:
    for padrao in pergunta.get("sinais") or []:
        try:
            if re.search(padrao, unidade.texto, re.I):
                return True
        except re.error:
            continue
    return False


def agrupar_perguntas(unidade: Unidade, perguntas: list[dict], tamanho: int) -> list[list[dict]]:
    """Pré-filtro decide a GRANULARIDADE, nunca a inclusão (seção 5).

    Pergunta com sinal na unidade → pacote só dela (pergunta estreita).
    As demais → checklist agrupado por afinidade, no máximo `tamanho` por pacote.
    Nenhuma pergunta sai da unidade: um filtro que excluísse seria mais uma fonte
    de falso negativo silencioso.
    """
    estreitas = [[q] for q in perguntas if tem_sinal(unidade, q)]
    resto: dict[str, list[dict]] = {}
    for q in perguntas:
        if not tem_sinal(unidade, q):
            resto.setdefault(q["grupo"], []).append(q)
    grupos = []
    for lista in resto.values():
        for i in range(0, len(lista), max(1, tamanho)):
            grupos.append(lista[i:i + tamanho])
    return estreitas + grupos


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

def _prompt(nome: str) -> tuple[str, str]:
    versao = (projeto().get("prompts") or {}).get(nome)
    if not versao:
        raise ErroDeProjeto(f"project.yaml: prompts.{nome} não definido")
    caminho = RAIZ / "prompts" / f"{versao}.md"
    if not caminho.exists():
        raise ErroDeProjeto(f"prompt não encontrado: {caminho}")
    texto = caminho.read_text(encoding="utf-8")
    return texto, f"{versao}@{sha(texto, 8)}"


def chave_aberta(unidade: Unidade) -> str:
    _, prompt_id = _prompt("aberta")
    return sha(f"aberta|{unidade.hash}|schema{versao_schema()}|{prompt_id}", 24)


def chave_dirigida(unidade: Unidade, pergunta: dict) -> str:
    _, prompt_id = _prompt("dirigida")
    return sha(f"dirigida|{unidade.hash}|schema{versao_schema()}|{prompt_id}|{pergunta['id']}|"
               f"{pergunta['hash']}", 24)


def ler_cache(tipo: str, chave: str) -> dict | None:
    return carregar_yaml(CACHE / tipo / f"{chave}.yaml")


def gravar_cache(tipo: str, chave: str, dados: dict) -> None:
    salvar_yaml(CACHE / tipo / f"{chave}.yaml", dados)


# ---------------------------------------------------------------------------
# Pacotes
# ---------------------------------------------------------------------------

ORIENTACAO_TIPO = {
    "prosa": "Prosa narrativa. Extraia eventos, falas e atributos, cada um com o `modo` certo. "
             "Fala de personagem é `fala`; o que ele acredita é `pensamento`; sonho, plano ou "
             "suposição é `hipotetico`. Só a afirmação direta do narrador é `narrador`.",
    "roteiro": "Roteiro. Ação e rubrica contam como `narrador`. Falas são `fala`, com o "
               "personagem em `falante`.",
    "biblia": "Bíblia de mundo. Extraia proposições sobre o mundo: entidades, regras, relações e "
              "datas. Afirmação direta da bíblia é `narrador`. Lendas, crônicas, cartas, registros "
              "e textos escritos por gente do mundo são `documento_interno` — inclusive quando o "
              "documento inteiro é narrado por um personagem.",
    "ficha": "Ficha. Extraia atributos estruturados, com o mínimo de interpretação.",
    "cronologia": "Cronologia. Extraia cada evento com a sua data em `tempo`.",
    "ramificado": "Narrativa ramificada. Todo fato leva em `condicao` o estado (flags, escolhas) "
                  "em que ele vale; fatos que valem em qualquer caminho levam `condicao: null`.",
}


def _texto_vocabulario(vocab: dict, somente: list[str] | None = None) -> str:
    linhas = []
    for nome, info in vocab["predicados"].items():
        if somente and normalizar_predicado(nome) not in somente:
            continue
        info = info or {}
        linhas.append(f"- `{nome}` ({info.get('tipo', '?')}; objeto: {info.get('objeto', 'texto')})"
                      f" — {str(info.get('descricao', '')).strip()}")
    return "\n".join(linhas)


def _eventos_canon(canon: Canon) -> str:
    eventos = canon.timeline.get("eventos") or []
    if not eventos:
        return "(nenhum)"
    return "\n".join(f"- `{e['id']}`: {e.get('descricao', '')}" for e in eventos if e.get("id"))


def _id_pacote(tipo: str, unidade: Unidade, extra: str = "") -> str:
    return f"{tipo}-{slug(unidade.id)[:40]}-{sha(unidade.id + extra, 6)}"


def _gravar_pacote(pacote_id: str, texto: str, meta: dict) -> None:
    PENDENTES.mkdir(parents=True, exist_ok=True)
    (PENDENTES / f"{pacote_id}.md").write_text(texto, encoding="utf-8")
    salvar_json(PENDENTES / f"{pacote_id}.json", meta)


def _render(modelo: str, campos: dict) -> str:
    for chave, valor in campos.items():
        modelo = modelo.replace("{{" + chave + "}}", str(valor))
    return modelo


def preparar(arquivos: list[str] | None = None, forcar: bool = False, amostra: float = 0.0,
             semente: int | None = None, vizinhas: bool = True) -> dict:
    """Gera os pacotes que faltam. Devolve um resumo por documento."""
    canon = Canon.carregar()
    vocab = carregar_vocabulario()
    registrados = set(predicados_registrados(vocab))
    perguntas = perguntas_ativas(canon)
    tamanho = int(projeto().get("checklist_tamanho_grupo", 7))
    modelo_aberta, _ = _prompt("aberta")
    modelo_dirigida, _ = _prompt("dirigida")
    rng = random.Random(semente)

    # Cópias com erros plantados (experimento: true) só entram quando pedidas
    # pelo nome, como no `verificar`: não gastam o operador por acidente.
    arquivos = arquivos or [d["arquivo"] for d in documentos_declarados() if not d.get("experimento")]
    resumo = {}
    for arquivo in arquivos:
        unidades, classe = unidades_do_documento(arquivo)
        # Unidades cujo texto mudou (cache ausente) puxam as vizinhas: o sentido
        # de uma cena depende das anteriores — "ele" pode mudar de referente.
        alteradas = {i for i, u in enumerate(unidades) if ler_cache("aberta", chave_aberta(u)) is None}
        motivo: dict[int, str] = {}
        if vizinhas and alteradas and len(alteradas) < len(unidades):
            for i in alteradas:
                for j in (i - 1, i + 1):
                    if 0 <= j < len(unidades) and j not in alteradas:
                        motivo[j] = "vizinha"
        # Amostra aleatória das inalteradas, reextraída do zero (seção 9).
        inalteradas = [i for i in range(len(unidades)) if i not in alteradas and i not in motivo]
        if amostra > 0 and inalteradas:
            k = max(1, round(len(inalteradas) * amostra))
            for j in rng.sample(inalteradas, min(k, len(inalteradas))):
                motivo[j] = "amostra"

        contagem = {"unidades": len(unidades), "aberta": 0, "complemento": 0, "dirigida": 0,
                    "vizinha": 0, "amostra": 0}
        for i, u in enumerate(unidades):
            chave = chave_aberta(u)
            atual = ler_cache("aberta", chave)
            reextrair = forcar or (i in motivo and atual is not None)
            faltam = None
            if atual is not None and not reextrair:
                cobertos = set(atual.get("predicados_cobertos") or [])
                faltam = sorted(registrados - cobertos)
            if atual is None or reextrair or faltam:
                somente = faltam if (atual is not None and not reextrair and faltam) else None
                pid = _id_pacote("aberta", u, "complemento" if somente else "")
                texto = _render(modelo_aberta, {
                    "ARQUIVO": u.arquivo, "UNIDADE": u.id, "TITULO": u.titulo,
                    "TIPO_DOCUMENTO": u.tipo, "ORIENTACAO_TIPO": ORIENTACAO_TIPO[u.tipo],
                    "VOCABULARIO": _texto_vocabulario(vocab, somente),
                    "SOMENTE": ("Esta é uma extração de COMPLEMENTO: registre apenas fatos com os "
                                "predicados listados acima, que entraram no vocabulário depois da "
                                "extração anterior." if somente else ""),
                    "EVENTOS_CANON": _eventos_canon(canon),
                    "TEXTO": u.texto,
                })
                _gravar_pacote(pid, texto, {
                    "pacote": pid, "tipo": "aberta", "chave": chave, "arquivo": u.arquivo,
                    "unidade": u.id, "unidade_hash": u.hash, "tipo_documento": u.tipo,
                    "somente_predicados": somente,
                    "reextracao": (motivo.get(i, "forcada") if reextrair and atual else None),
                    "vocabulario_versao": vocab.get("versao"),
                    "criado_em": _agora(),
                })
                if somente:
                    contagem["complemento"] += 1
                elif reextrair and atual:
                    contagem[motivo.get(i, "amostra")] += 1
                else:
                    contagem["aberta"] += 1

            faltando = [q for q in perguntas if forcar or ler_cache("dirigida", chave_dirigida(u, q)) is None]
            for grupo in agrupar_perguntas(u, faltando, tamanho):
                ids = [q["id"] for q in grupo]
                pid = _id_pacote("dirigida", u, "|".join(ids))
                blocos = "\n\n".join(f"### {q['id']}\n{q['pergunta']}\n"
                                     f"Predicados esperados: {', '.join(q['predicados']) or 'qualquer'}"
                                     for q in grupo)
                texto = _render(modelo_dirigida, {
                    "ARQUIVO": u.arquivo, "UNIDADE": u.id, "TITULO": u.titulo,
                    "TIPO_DOCUMENTO": u.tipo, "ORIENTACAO_TIPO": ORIENTACAO_TIPO[u.tipo],
                    "PERGUNTAS": blocos, "IDS": ", ".join(ids),
                    "VOCABULARIO": _texto_vocabulario(vocab),
                    "EVENTOS_CANON": _eventos_canon(canon),
                    "TEXTO": u.texto,
                })
                _gravar_pacote(pid, texto, {
                    "pacote": pid, "tipo": "dirigida", "arquivo": u.arquivo, "unidade": u.id,
                    "unidade_hash": u.hash, "tipo_documento": u.tipo,
                    "perguntas": [{"id": q["id"], "hash": q["hash"],
                                   "chave": chave_dirigida(u, q),
                                   "predicados": q["predicados"]} for q in grupo],
                    "estreita": len(grupo) == 1 and tem_sinal(u, grupo[0]),
                    "criado_em": _agora(),
                })
                contagem["dirigida"] += 1
        resumo[arquivo] = {"classificacao": classe, **contagem}
    return resumo


def _agora() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Ingestão
# ---------------------------------------------------------------------------

def extrair_yaml(texto: str):
    """Aceita YAML puro ou dentro de um bloco ```yaml (operadores costumam cercar)."""
    blocos = re.findall(r"```(?:yaml|yml)?\s*\n(.*?)```", texto, re.S)
    candidatos = blocos or [texto]
    ultimo_erro = None
    for bloco in candidatos:
        try:
            dados = yaml.safe_load(bloco)
        except yaml.YAMLError as erro:
            ultimo_erro = erro
            continue
        if isinstance(dados, dict):
            return dados
    raise ErroDeProjeto(f"resposta sem YAML válido ({ultimo_erro})")


def validar_fato(bruto: dict, unidade: Unidade, registrados: dict, origem: str) -> tuple[dict | None, dict | None, dict | None]:
    """Devolve (fato, predicado_livre, rejeitado). Exatamente um não é None."""
    if not isinstance(bruto, dict):
        return None, None, {"motivo": "fato não é um mapa", "bruto": str(bruto)[:200]}

    def rejeitar(motivo: str):
        return None, None, {"motivo": motivo, "citacao": bruto.get("citacao"),
                            "predicado": bruto.get("predicado"), "sujeito": bruto.get("sujeito")}

    for campo in ("tipo", "sujeito", "predicado", "citacao", "modo"):
        if bruto.get(campo) in (None, ""):
            return rejeitar(f"campo obrigatório ausente: {campo}")
    tipo = str(bruto["tipo"]).strip().casefold()
    if tipo not in TIPOS_FATO:
        return rejeitar(f"tipo inválido: {bruto['tipo']}")
    modo = normalizar_modo(bruto["modo"])
    if modo is None:
        return rejeitar(f"modo inválido: {bruto['modo']} (válidos: {', '.join(MODOS)})")
    confianca = normalizar_confianca(bruto.get("confianca_extracao", bruto.get("confianca"))) or "media"

    ancora = grounding.ancorar(bruto["citacao"], unidade.texto, unidade.linha_inicio)
    if not ancora["ok"]:
        return rejeitar(ancora["motivo"])

    tempo, problemas_tempo = validar_tempo(bruto.get("tempo"))
    qualificadores = bruto.get("qualificadores") or {}
    if not isinstance(qualificadores, dict):
        qualificadores = {}

    predicado = normalizar_predicado(bruto["predicado"])
    # Linhas guardadas também RELATIVAS à unidade: o cache é por conteúdo, e o
    # mesmo trecho pode reaparecer noutro arquivo ou deslocado (a cópia com
    # erros plantados, uma seção acrescentada acima). Ver `_relocalizar`.
    local = {"arquivo": unidade.arquivo, "unidade": unidade.id,
             "linha_inicio": ancora["linha_inicio"], "linha_fim": ancora["linha_fim"],
             "rel_inicio": ancora["linha_inicio"] - unidade.linha_inicio,
             "rel_fim": ancora["linha_fim"] - unidade.linha_inicio}
    base = {
        "tipo": tipo, "sujeito": str(bruto["sujeito"]).strip(), "predicado": predicado,
        "objeto": bruto.get("objeto"), "qualificadores": qualificadores, "tempo": tempo,
        "modo": modo, "falante": bruto.get("falante"), "ref": bruto.get("ref"),
        "tipo_documento": unidade.tipo, "condicao": bruto.get("condicao"),
        "citacao": str(bruto["citacao"]).strip(), "local": local,
        "confianca_extracao": confianca, "origem_extracao": origem,
    }
    if bruto.get("responde_a"):
        r = bruto["responde_a"]
        base["responde_a"] = r if isinstance(r, list) else [r]

    if predicado not in registrados:
        base["predicado_original"] = bruto["predicado"]
        return None, base, None

    info = registrados[predicado]
    if info.get("objeto") == "inteiro" and base["objeto"] is not None:
        try:
            base["objeto"] = int(str(base["objeto"]).strip())
        except ValueError:
            return rejeitar(f"objeto de {predicado} precisa ser inteiro: {base['objeto']!r}")
    if problemas_tempo:
        base["problemas"] = problemas_tempo
    base["id"] = "F-" + sha("|".join([unidade.id, tipo, normalizar_nome(base["sujeito"]), predicado,
                                      normalizar_nome(base["objeto"]), grounding.normalizar(base["citacao"])]), 12)
    return base, None, None


def _lista_fatos(dados: dict, chave: str = "fatos") -> list:
    lista = dados.get(chave)
    if lista is None:
        return []
    if not isinstance(lista, list):
        raise ErroDeProjeto(f"`{chave}` precisa ser uma lista")
    return lista


def _unidade_por_id(arquivo: str, unidade_id: str, unidade_hash: str) -> Unidade | None:
    unidades, _ = unidades_do_documento(arquivo)
    for u in unidades:
        if u.id == unidade_id:
            return u if u.hash == unidade_hash else None
    return None


def ingerir(operador: str = "manual") -> dict:
    """Valida todas as respostas disponíveis e grava no cache."""
    registrados = predicados_registrados()
    resumo = {"ingeridos": 0, "sem_resposta": 0, "obsoletos": 0, "fatos": 0,
              "rejeitados": 0, "predicado_livre": 0, "erros": []}
    afetados: set[str] = set()
    for meta_path in sorted(PENDENTES.glob("*.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        pid = meta["pacote"]
        resposta = next((p for p in (RESPOSTAS / f"{pid}.yaml", RESPOSTAS / f"{pid}.md",
                                     RESPOSTAS / f"{pid}.txt") if p.exists()), None)
        if resposta is None:
            resumo["sem_resposta"] += 1
            continue
        unidade = _unidade_por_id(meta["arquivo"], meta["unidade"], meta["unidade_hash"])
        if unidade is None:
            # O texto mudou depois que o pacote foi gerado: a resposta fala de
            # outro texto e não pode ser aceita.
            resumo["obsoletos"] += 1
            _arquivar(meta_path, resposta, "obsoleto")
            continue
        try:
            dados = extrair_yaml(resposta.read_text(encoding="utf-8"))
            if meta["tipo"] == "aberta":
                n = _ingerir_aberta(meta, dados, unidade, registrados, operador)
            else:
                n = _ingerir_dirigida(meta, dados, unidade, registrados, operador)
        except ErroDeProjeto as erro:
            resumo["erros"].append(f"{pid}: {erro}")
            continue
        for k in ("fatos", "rejeitados", "predicado_livre"):
            resumo[k] += n[k]
        resumo["ingeridos"] += 1
        afetados.add(meta["arquivo"])
        _arquivar(meta_path, resposta, "processado")
    for arquivo in sorted(afetados):
        montar_fatos(arquivo)
    resumo["documentos"] = sorted(afetados)
    return resumo


def _arquivar(meta_path: Path, resposta: Path, sufixo: str) -> None:
    PROCESSADOS.mkdir(parents=True, exist_ok=True)
    pid = meta_path.stem
    for origem in (meta_path, PENDENTES / f"{pid}.md", resposta):
        if origem.exists():
            shutil.move(str(origem), str(PROCESSADOS / f"{pid}.{sufixo}{origem.suffix}"))


def _validar_lista(brutos, unidade, registrados, origem):
    fatos, livres, rejeitados = [], [], []
    for bruto in brutos:
        f, livre, rej = validar_fato(bruto, unidade, registrados, origem)
        if f:
            fatos.append(f)
        elif livre:
            livres.append(livre)
        else:
            rejeitados.append(rej)
    return fatos, livres, rejeitados


def _ingerir_aberta(meta, dados, unidade, registrados, operador) -> dict:
    fatos, livres, rejeitados = _validar_lista(_lista_fatos(dados), unidade, registrados, "aberta")
    anterior = ler_cache("aberta", meta["chave"])
    somente = meta.get("somente_predicados")
    if somente and anterior:
        # Complemento: junta ao que já estava, sem refazer.
        vistos = {f["id"] for f in anterior.get("fatos", [])}
        fatos = anterior.get("fatos", []) + [f for f in fatos if f["id"] not in vistos]
        livres = anterior.get("predicado_livre", []) + livres
        rejeitados = anterior.get("rejeitados", []) + rejeitados
        cobertos = sorted(set(anterior.get("predicados_cobertos") or []) | set(somente))
    else:
        cobertos = sorted(registrados)
    entrada = {
        "chave": meta["chave"], "arquivo": meta["arquivo"], "unidade": meta["unidade"],
        "unidade_hash": meta["unidade_hash"], "tipo_documento": meta["tipo_documento"],
        "schema": versao_schema(), "predicados_cobertos": cobertos,
        "extraido_em": _agora(), "operador": operador,
        "fatos": fatos, "predicado_livre": livres, "rejeitados": rejeitados,
    }
    if meta.get("reextracao") and anterior:
        # Reextraída do zero (vizinha ou amostra): quanto concorda com o cache
        # mede o ruído normal da extração (seção 9).
        entrada["estabilidade"] = {"motivo": meta["reextracao"],
                                   **_estabilidade(anterior.get("fatos", []), fatos)}
    gravar_cache("aberta", meta["chave"], entrada)
    return {"fatos": len(fatos), "rejeitados": len(rejeitados), "predicado_livre": len(livres)}


def _assinatura(f: dict) -> tuple:
    return (normalizar_nome(f["sujeito"]), f["predicado"], normalizar_nome(f.get("objeto")), f["modo"])


def _estabilidade(antes: list, depois: list) -> dict:
    """Quanto a mesma unidade, reextraída do zero, concorda com o cache (seção 9)."""
    a = {_assinatura(f) for f in antes}
    b = {_assinatura(f) for f in depois}
    uniao = a | b
    return {"cache": len(a), "nova": len(b), "em_comum": len(a & b),
            "jaccard": round(len(a & b) / len(uniao), 3) if uniao else 1.0}


def _ingerir_dirigida(meta, dados, unidade, registrados, operador) -> dict:
    checklist = dados.get("checklist") or {}
    instancias = _lista_fatos(dados, "instancias")
    fatos, livres, rejeitados = _validar_lista(instancias, unidade, registrados, "dirigida")
    perguntas = meta["perguntas"]
    respostas = {}
    for q in perguntas:
        r = str(checklist.get(q["id"], "")).strip().casefold()
        if r not in ("sim", "nao", "não"):
            raise ErroDeProjeto(f"checklist sem resposta sim/nao para {q['id']}")
        respostas[q["id"]] = "nao" if r in ("nao", "não") else "sim"

    def dono(f: dict) -> list[str]:
        """A que pergunta(s) do pacote uma instância responde."""
        if len(perguntas) == 1:
            return [perguntas[0]["id"]]
        marcadas = [i for i in (f.get("responde_a") or []) if i in respostas]
        if marcadas:
            return marcadas
        pelo_predicado = [q["id"] for q in perguntas
                          if f["predicado"] in {normalizar_predicado(p) for p in q["predicados"]}]
        return pelo_predicado or [perguntas[0]["id"]]

    for n, q in enumerate(perguntas):
        gravar_cache("dirigida", q["chave"], {
            "chave": q["chave"], "arquivo": meta["arquivo"], "unidade": meta["unidade"],
            "unidade_hash": meta["unidade_hash"], "pergunta": q["id"], "pergunta_hash": q["hash"],
            "estreita": meta.get("estreita", False),
            "resposta": respostas[q["id"]],
            "instancias": [f for f in fatos if q["id"] in dono(f)],
            # Livres e rejeitados do pacote ficam registrados uma vez só.
            "predicado_livre": livres if n == 0 else [],
            "rejeitados": rejeitados if n == 0 else [],
            "extraido_em": _agora(), "operador": operador,
        })
    return {"fatos": len(fatos), "rejeitados": len(rejeitados), "predicado_livre": len(livres)}


# ---------------------------------------------------------------------------
# Fatos do documento (a partir do cache)
# ---------------------------------------------------------------------------

def caminho_fatos(arquivo: str, versao: str | None = None) -> Path:
    return RAIZ / "facts" / (versao or versao_atual()) / f"{slug(arquivo.removesuffix('.md'))}.yaml"


def montar_fatos(arquivo: str) -> dict:
    """Junta, a partir do cache, os fatos de TODAS as unidades atuais do documento.

    Unidade sem extração não some em silêncio: fica listada como não verificada.
    Um relatório limpo sobre metade da obra não pode parecer limpo sobre a obra.
    """
    canon = Canon.carregar()
    perguntas = perguntas_ativas(canon)
    unidades, classe = unidades_do_documento(arquivo)

    fatos: list[dict] = []
    livres, rejeitados, divergencias, nao_extraidas, estabilidade = [], [], [], [], []
    for u in unidades:
        aberta = ler_cache("aberta", chave_aberta(u))
        if aberta is None:
            nao_extraidas.append({"unidade": u.id, "linhas": [u.linha_inicio, u.linha_fim],
                                  "falta": "extração aberta"})
            abertos = []
        else:
            abertos = [_relocalizar(f, u) for f in aberta.get("fatos") or []]
            livres += aberta.get("predicado_livre") or []
            rejeitados += aberta.get("rejeitados") or []
            if aberta.get("estabilidade"):
                estabilidade.append({"unidade": u.id, **aberta["estabilidade"]})
        fatos += abertos

        for q in perguntas:
            d = ler_cache("dirigida", chave_dirigida(u, q))
            if d is None:
                nao_extraidas.append({"unidade": u.id, "linhas": [u.linha_inicio, u.linha_fim],
                                      "falta": f"pergunta dirigida {q['id']}"})
                continue
            livres += d.get("predicado_livre") or []
            rejeitados += d.get("rejeitados") or []
            insts = [_relocalizar(f, u) for f in d.get("instancias") or []]
            if d.get("resposta") == "sim" and not insts:
                divergencias.append({"unidade": u.id, "pergunta": q["id"],
                                     "tipo": "resposta 'sim' sem instância citada"})
            for inst in insts:
                par = _par_aberto(inst, abertos)
                if par is None:
                    # A pergunta estreita achou o que a extração aberta não registrou:
                    # falha de extração (seção 5). O fato entra, e a falha aparece.
                    divergencias.append({"unidade": u.id, "pergunta": q["id"],
                                         "tipo": "achado só pela pergunta dirigida",
                                         "fato": inst["id"], "citacao": inst["citacao"],
                                         "linha": inst["local"]["linha_inicio"]})
                    fatos.append(inst)
                else:
                    par.setdefault("confirmado_por", [])
                    if q["id"] not in par["confirmado_por"]:
                        par["confirmado_por"].append(q["id"])
            if d.get("resposta") == "nao" and q["predicados"]:
                preds = {normalizar_predicado(p) for p in q["predicados"]}
                for f in abertos:
                    if f["predicado"] in preds:
                        divergencias.append({"unidade": u.id, "pergunta": q["id"],
                                             "tipo": "pergunta dirigida respondeu 'não', mas a "
                                                     "extração aberta registrou",
                                             "fato": f["id"], "citacao": f["citacao"],
                                             "linha": f["local"]["linha_inicio"]})

    fatos = _dedupe(fatos)
    _resolver_refs(fatos)
    saida = {
        "documento": arquivo, "classificacao": classe, "versao": versao_atual(),
        "schema": versao_schema(), "montado_em": _agora(),
        "unidades": len(unidades), "nao_extraidas": nao_extraidas,
        "fatos": fatos, "predicado_livre": livres, "rejeitados": rejeitados,
        "divergencias": divergencias, "estabilidade": estabilidade,
    }
    salvar_yaml(caminho_fatos(arquivo), saida)
    return saida


def _relocalizar(f: dict, u: Unidade) -> dict:
    """Fato do cache, reposicionado na unidade atual (arquivo, linhas e id)."""
    f = {**f, "local": dict(f["local"]), "tempo": _copia(f.get("tempo"))}
    rel_i = f["local"].get("rel_inicio", 0)
    rel_f = f["local"].get("rel_fim", rel_i)
    f["local"].update({"arquivo": u.arquivo, "unidade": u.id,
                       "linha_inicio": u.linha_inicio + rel_i, "linha_fim": u.linha_inicio + rel_f})
    f["id"] = "F-" + sha("|".join([u.id, f["tipo"], normalizar_nome(f["sujeito"]), f["predicado"],
                                   normalizar_nome(f.get("objeto")),
                                   grounding.normalizar(f["citacao"])]), 12)
    return f


def _copia(x):
    return json.loads(json.dumps(x)) if x is not None else None


def _par_aberto(inst: dict, abertos: list[dict]) -> dict | None:
    for f in abertos:
        if (f["predicado"] == inst["predicado"]
                and normalizar_nome(f["sujeito"]) == normalizar_nome(inst["sujeito"])
                and grounding.sobrepoe((f["local"]["linha_inicio"], f["local"]["linha_fim"]),
                                       (inst["local"]["linha_inicio"], inst["local"]["linha_fim"]))):
            return f
    return None


def _dedupe(fatos: list[dict]) -> list[dict]:
    vistos, saida = set(), []
    for f in fatos:
        if f["id"] in vistos:
            continue
        vistos.add(f["id"])
        saida.append(f)
    return saida


def _resolver_refs(fatos: list[dict]) -> None:
    refs = {}
    for f in fatos:
        if f.get("ref"):
            refs.setdefault(normalizar_nome(f["ref"]), f["id"])
    for f in fatos:
        rel = (f.get("tempo") or {}).get("relativo_a")
        if not rel:
            continue
        if rel.get("ref"):
            alvo = refs.get(normalizar_nome(rel["ref"]))
            rel["fato"] = alvo
            rel["resolvido"] = alvo is not None
        elif rel.get("evento"):
            rel["resolvido"] = True
        else:
            rel["resolvido"] = False


def carregar_fatos(versao: str | None = None) -> dict[str, dict]:
    pasta = RAIZ / "facts" / (versao or versao_atual())
    saida = {}
    for p in sorted(pasta.glob("*.yaml")):
        dados = carregar_yaml(p, {}) or {}
        if dados.get("documento"):
            saida[dados["documento"]] = dados
    return saida


def status() -> list[dict]:
    canon = Canon.carregar()
    perguntas = perguntas_ativas(canon)
    linhas = []
    pendentes = {json.loads(p.read_text())["arquivo"] for p in PENDENTES.glob("*.json")} \
        if PENDENTES.exists() else set()
    for d in documentos_declarados():
        try:
            unidades, classe = unidades_do_documento(d["arquivo"])
        except ErroDeProjeto as erro:
            linhas.append({"arquivo": d["arquivo"], "erro": str(erro)})
            continue
        abertas = sum(1 for u in unidades if ler_cache("aberta", chave_aberta(u)))
        dirigidas = sum(1 for u in unidades for q in perguntas if ler_cache("dirigida", chave_dirigida(u, q)))
        linhas.append({
            "arquivo": d["arquivo"], "tipo": classe["tipo"], "unidades": len(unidades),
            "aberta_ok": abertas, "dirigidas_ok": dirigidas,
            "dirigidas_total": len(unidades) * len(perguntas),
            "pacotes_pendentes": d["arquivo"] in pendentes,
        })
    return linhas
