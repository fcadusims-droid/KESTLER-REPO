"""Medição: é aqui que a Fase 1 produz números (seção 11).

Sem isto, o sistema seria só uma opinião bem formatada. Quatro instrumentos:

- GOLDEN SET de extração: trechos difíceis com a resposta escrita pelo autor.
  Mede precisão, recall e — o mais importante — o erro de `modo` (mentira
  registrada como fato).
- ERROS PLANTADOS: uma cópia da obra com contradições conhecidas. Mede o que o
  sistema deixa passar.
- GABARITO POR POOLING (como no TREC): a união do que acharam o pipeline, o
  prompt simples e a leitura manual do autor numa amostra. Mede recall sobre
  erros naturais.
- BASELINE: a obra inteira num contexto longo, "liste as contradições e cite".

Todo recall sai com intervalo de confiança de Wilson. Os números do próprio
documento batem com Wilson (59 de 60 → limite inferior ≥ 90%; 55 de 60 → ≥ 80%;
18 de 20 → ~70% a 97%) e estão fixados nos testes. O critério de parada usa o
LIMITE INFERIOR, não o valor observado.
"""

from __future__ import annotations

import math
import random
import re
from collections import defaultdict
from pathlib import Path

from . import grounding
from .io import (RAIZ, ErroDeProjeto, carregar_yaml, ler_obra, normalizar_nome, projeto,
                 salvar_yaml, slug)
from .schema import normalizar_modo, normalizar_predicado


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Intervalo de confiança de Wilson (95% por padrão) para k sucessos em n."""
    if n == 0:
        return 0.0, 1.0
    p = k / n
    centro = (p + z * z / (2 * n)) / (1 + z * z / n)
    margem = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, centro - margem), min(1.0, centro + margem)


def taxa(k: int, n: int) -> dict:
    lo, hi = wilson(k, n)
    return {"k": k, "n": n, "valor": round(k / n, 3) if n else None,
            "ic95": [round(lo, 3), round(hi, 3)]}


def criterio(nome: str) -> float | None:
    return (projeto().get("criterios_parada") or {}).get(nome)


# ---------------------------------------------------------------------------
# Golden set de extração
# ---------------------------------------------------------------------------

PASTA_GOLDEN = RAIZ / "tests" / "golden_extraction"


def carregar_golden() -> list[dict]:
    itens = []
    for p in sorted(PASTA_GOLDEN.glob("*.yaml")):
        dados = carregar_yaml(p, {}) or {}
        if dados.get("id") and dados.get("texto"):
            dados["_arquivo"] = p.name
            itens.append(dados)
    return itens


def _mesmo_nome(a, b) -> bool:
    a, b = normalizar_nome(a), normalizar_nome(b)
    if not a or not b:
        return a == b
    if a == b:
        return True
    # "Reiter" ~ "Anselm Reiter": um contém o outro como palavras inteiras.
    pa, pb = set(a.split()), set(b.split())
    return pa <= pb or pb <= pa


def casa(esperado: dict, extraido: dict) -> bool:
    if normalizar_predicado(esperado["predicado"]) != extraido["predicado"]:
        return False
    if not _mesmo_nome(esperado["sujeito"], extraido["sujeito"]):
        return False
    oe, ox = esperado.get("objeto"), extraido.get("objeto")
    if oe is None:
        return True
    if isinstance(oe, int) or isinstance(ox, int):
        return str(oe).strip() == str(ox).strip()
    return _mesmo_nome(oe, ox)


def pontuar_golden(extraidos_por_item: dict[str, list[dict]], itens: list[dict]) -> dict:
    """Precisão, recall e erros de modo, no total e por dificuldade/origem."""
    total_esp = total_ext = acertos_esp = acertos_ext = 0
    modo_certo = modo_total = 0
    graves: list[dict] = []
    por_grupo: dict[str, dict] = defaultdict(lambda: {"esp": 0, "ok": 0})
    for item in itens:
        extraidos = extraidos_por_item.get(item["id"], [])
        esperados = item.get("fatos_esperados") or []
        usados = set()
        for e in esperados:
            total_esp += 1
            grupo_d = f"dificuldade:{item.get('dificuldade', '?')}"
            grupo_o = f"origem:{item.get('origem', '?')}"
            for g in (grupo_d, grupo_o):
                por_grupo[g]["esp"] += 1
            par = next((i for i, x in enumerate(extraidos) if i not in usados and casa(e, x)), None)
            if par is None:
                continue
            usados.add(par)
            acertos_esp += 1
            for g in (grupo_d, grupo_o):
                por_grupo[g]["ok"] += 1
            me = normalizar_modo(e.get("modo", "narrador"))
            mx = extraidos[par]["modo"]
            modo_total += 1
            if me == mx:
                modo_certo += 1
            elif mx == "narrador":
                graves.append({"item": item["id"], "esperado": e, "citacao": extraidos[par]["citacao"],
                               "erro": f"registrado como narrador, mas é {me}"})
        total_ext += len(extraidos)
        acertos_ext += len(usados)
        for proibido in item.get("nao_deve_extrair") or []:
            for x in extraidos:
                if casa(proibido, x) and x["modo"] == normalizar_modo(proibido.get("modo", "narrador")):
                    graves.append({"item": item["id"], "esperado": proibido, "citacao": x["citacao"],
                                   "erro": "extraiu um fato que não deveria existir"})
    rec, prec = taxa(acertos_esp, total_esp), taxa(acertos_ext, total_ext)
    return {
        "recall": rec, "precisao": prec, "modo": taxa(modo_certo, modo_total),
        "erros_graves": graves,
        "por_grupo": {g: taxa(v["ok"], v["esp"]) for g, v in sorted(por_grupo.items())},
        "parada": _parada({"recall": (rec, criterio("extracao_recall_min_li")),
                           "precisao": (prec, criterio("extracao_precisao_min_li"))}),
    }


def _parada(medidas: dict) -> dict:
    saida = {}
    for nome, (t, limite) in medidas.items():
        if limite is None or t["n"] == 0:
            saida[nome] = "sem critério ou sem dados"
            continue
        saida[nome] = ("PASSA" if t["ic95"][0] >= limite else "PARE") + \
            f" (limite inferior {t['ic95'][0]:.3f} vs mínimo {limite})"
    return saida


# ---------------------------------------------------------------------------
# Erros plantados
# ---------------------------------------------------------------------------

PASTA_PLANTIO = RAIZ / "tests" / "seeded_errors"
DIFICEIS = {"distante", "relativo", "heranca", "implicito"}


def _plantio(nome: str) -> tuple[dict, Path]:
    pasta = PASTA_PLANTIO / nome
    dados = carregar_yaml(pasta / "plantio.yaml")
    if not dados:
        raise ErroDeProjeto(f"{pasta}/plantio.yaml não encontrado")
    return dados, pasta


def status_plantio(nome: str) -> dict:
    dados, _ = _plantio(nome)
    erros = dados.get("erros") or []
    minimo = int(criterio("plantados_minimo") or 60)
    quota = float(criterio("quota_dificeis_min") or 0.3)
    dificeis = sum(1 for e in erros if e.get("dificuldade") in DIFICEIS)
    por_origem = defaultdict(int)
    for e in erros:
        por_origem[e.get("origem", "?")] += 1
    problemas = []
    if len(erros) < minimo:
        problemas.append(f"só {len(erros)} erros; o mínimo é {minimo} (com menos, o intervalo de "
                         f"confiança não permite decidir nada)")
    if erros and dificeis / len(erros) < quota:
        problemas.append(f"só {dificeis} erros difíceis ({dificeis / len(erros):.0%}); a cota é {quota:.0%}")
    if por_origem.get("autor", 0) == 0 and erros:
        problemas.append("nenhum erro plantado pelo autor: o recall medido só com erros do Claude sai "
                         "otimista (o Claude planta o tipo de erro que ele mesmo detecta)")
    return {"erros": len(erros), "dificeis": dificeis, "por_origem": dict(por_origem),
            "problemas": problemas, "pronto": not problemas}


def aplicar_plantio(nome: str) -> dict:
    """Gera a cópia com os erros e o gabarito com as linhas de cada um."""
    dados, pasta = _plantio(nome)
    fonte = dados["fonte"]
    texto = ler_obra(fonte)
    erros = dados.get("erros") or []
    for e in erros:
        n = texto.count(e["localizar"])
        if n != 1:
            raise ErroDeProjeto(f"{e['id']}: `localizar` aparece {n} vez(es) no texto (precisa ser 1)")
        texto = texto.replace(e["localizar"], e["substituir"], 1)
    gabarito = []
    for e in erros:
        n = texto.count(e["substituir"])
        if n != 1:
            raise ErroDeProjeto(f"{e['id']}: `substituir` aparece {n} vez(es) na cópia (precisa ser 1 "
                                f"para localizar o erro)")
        pos = texto.index(e["substituir"])
        ini = texto.count("\n", 0, pos) + 1
        fim = ini + e["substituir"].count("\n")
        gabarito.append({"id": e["id"], "categoria": e.get("categoria"), "dificuldade": e.get("dificuldade"),
                         "origem": e.get("origem"), "linha_inicio": ini, "linha_fim": fim,
                         "descricao": e.get("descricao")})
    copia = pasta / "obra_plantada.md"
    copia.write_text(texto, encoding="utf-8")
    salvar_yaml(pasta / "gabarito_plantado.yaml", {"fonte": fonte, "copia": _relativo(copia),
                                                  "erros": gabarito})
    return {"copia": _relativo(copia), "erros": len(gabarito)}


def _relativo(caminho: Path) -> str:
    from .io import raiz_obras
    return str(caminho.resolve().relative_to(raiz_obras()))


def pontuar_plantio(nome: str, relatorio: dict) -> dict:
    _, pasta = _plantio(nome)
    gab = carregar_yaml(pasta / "gabarito_plantado.yaml")
    if not gab:
        raise ErroDeProjeto("rode `plantar aplicar` antes de pontuar")
    copia = gab["copia"]
    diags = [d for d in relatorio["diagnosticos"] if not d.get("suprimido")]
    spans = []
    for d in diags:
        for ev in d["evidencias"]:
            if ev.get("fonte") == "obra" and ev["arquivo"] == copia:
                spans.append((ev["linha_inicio"], ev["linha_fim"], d["id"]))
    achados, grupos = 0, defaultdict(lambda: [0, 0])
    detalhes = []
    usados = set()
    for e in gab["erros"]:
        alvo = (e["linha_inicio"], e["linha_fim"])
        quem = [sid for (a, b, sid) in spans if grounding.sobrepoe(alvo, (a, b))]
        ok = bool(quem)
        usados |= set(quem)
        achados += ok
        for g in (f"categoria:{e.get('categoria')}", f"dificuldade:{e.get('dificuldade')}",
                  f"origem:{e.get('origem')}"):
            grupos[g][0] += ok
            grupos[g][1] += 1
        detalhes.append({"id": e["id"], "achado": ok, "por": quem, "descricao": e.get("descricao")})
    fora = sorted({sid for (_, _, sid) in spans} - usados)
    rec = taxa(achados, len(gab["erros"]))
    return {
        "recall": rec,
        "por_grupo": {g: taxa(k, n) for g, (k, n) in sorted(grupos.items())},
        "detalhes": detalhes,
        "diagnosticos_fora_dos_plantados": fora,
        "nota": ("recall em erros plantados é um TETO: o valor real é menor. Diagnósticos fora dos "
                 "plantados são erros naturais ou falsos positivos — vão para o gabarito por pooling."),
        "parada": _parada({"recall": (rec, criterio("plantados_recall_min_li"))}),
    }


# ---------------------------------------------------------------------------
# Gabarito por pooling
# ---------------------------------------------------------------------------

def pasta_gabarito(arquivo: str) -> Path:
    return RAIZ / "tests" / "gabarito" / slug(arquivo.removesuffix(".md"))


def amostrar(arquivo: str, n: int, semente: int, unidades: list) -> dict:
    rng = random.Random(semente)
    escolhidas = sorted(rng.sample(range(len(unidades)), min(n, len(unidades))))
    dados = {
        "documento": arquivo, "semente": semente,
        "instrucoes": ("Leia SÓ estas unidades, sem olhar o relatório, e anote em achados_manuais "
                       "cada contradição ou problema real que encontrar (linha_inicio, linha_fim, "
                       "descricao). A amostra é aleatória de propósito."),
        "unidades": [{"id": unidades[i].id, "linhas": [unidades[i].linha_inicio, unidades[i].linha_fim]}
                     for i in escolhidas],
        "achados_manuais": [],
    }
    destino = pasta_gabarito(arquivo) / "amostra.yaml"
    if destino.exists():
        antigo = carregar_yaml(destino, {}) or {}
        dados["achados_manuais"] = antigo.get("achados_manuais") or []
    salvar_yaml(destino, dados)
    return dados


def juntar(arquivo: str, relatorio: dict) -> dict:
    pasta = pasta_gabarito(arquivo)
    candidatos: list[dict] = []

    def adicionar(fonte: str, ini: int, fim: int, descricao: str) -> None:
        for c in candidatos:
            if grounding.sobrepoe((ini, fim), tuple(c["linhas"])):
                if fonte not in c["fontes"]:
                    c["fontes"].append(fonte)
                c["descricoes"].append(f"[{fonte}] {descricao}")
                c["linhas"] = [min(c["linhas"][0], ini), max(c["linhas"][1], fim)]
                return
        candidatos.append({"linhas": [ini, fim], "fontes": [fonte],
                           "descricoes": [f"[{fonte}] {descricao}"], "real": None})

    for d in relatorio["diagnosticos"]:
        if d.get("suprimido"):
            continue
        for ev in d["evidencias"]:
            if ev.get("fonte") == "obra" and ev["arquivo"] == arquivo:
                adicionar("pipeline", ev["linha_inicio"], ev["linha_fim"], f"{d['id']} {d['titulo']}")
    base = carregar_yaml(pasta / "baseline.yaml", {}) or {}
    for achado in base.get("achados") or []:
        for c in achado.get("citacoes_ancoradas") or []:
            adicionar("baseline", c["linha_inicio"], c["linha_fim"], achado.get("descricao", ""))
    amostra = carregar_yaml(pasta / "amostra.yaml", {}) or {}
    for m in amostra.get("achados_manuais") or []:
        adicionar("manual", int(m["linha_inicio"]), int(m.get("linha_fim", m["linha_inicio"])),
                  m.get("descricao", ""))

    antigo = carregar_yaml(pasta / "pool.yaml", {}) or {}
    for c in candidatos:   # preserva os rótulos que o autor já deu
        for a in antigo.get("candidatos") or []:
            if a.get("real") is not None and grounding.sobrepoe(tuple(a["linhas"]), tuple(c["linhas"])):
                c["real"] = a["real"]
                c["nota_autor"] = a.get("nota_autor")
    candidatos.sort(key=lambda c: c["linhas"][0])
    for i, c in enumerate(candidatos, 1):
        c["id"] = f"P-{i:03d}"
    dados = {"documento": arquivo,
             "instrucoes": "Marque `real: true` ou `real: false` em cada candidato.",
             "candidatos": candidatos}
    salvar_yaml(pasta / "pool.yaml", dados)
    return {"candidatos": len(candidatos)}


def pontuar_pool(arquivo: str) -> dict:
    dados = carregar_yaml(pasta_gabarito(arquivo) / "pool.yaml", {}) or {}
    cands = dados.get("candidatos") or []
    rotulados = [c for c in cands if c.get("real") is not None]
    reais = [c for c in rotulados if c["real"]]
    fontes = ("pipeline", "baseline", "manual")
    rec = {f: taxa(sum(1 for c in reais if f in c["fontes"]), len(reais)) for f in fontes}
    prec = {f: taxa(sum(1 for c in reais if f in c["fontes"]),
                    sum(1 for c in rotulados if f in c["fontes"])) for f in fontes}
    so_p = sum(1 for c in reais if "pipeline" in c["fontes"] and "baseline" not in c["fontes"])
    so_b = sum(1 for c in reais if "baseline" in c["fontes"] and "pipeline" not in c["fontes"])
    ambos = sum(1 for c in reais if "pipeline" in c["fontes"] and "baseline" in c["fontes"])
    return {
        "candidatos": len(cands), "rotulados": len(rotulados), "reais": len(reais),
        "recall_por_fonte": rec, "precisao_por_fonte": prec,
        "comparacao_baseline": {"so_pipeline": so_p, "so_baseline": so_b, "ambos": ambos},
        "nota": ("recall por pooling é um TETO: um erro que nenhuma das três fontes achou não entra "
                 "no gabarito. O valor real é menor."),
    }


# ---------------------------------------------------------------------------
# Baseline: a obra inteira num prompt
# ---------------------------------------------------------------------------

def ingerir_baseline(arquivo: str, dados: dict) -> dict:
    texto = ler_obra(arquivo)
    achados, rejeitadas = [], 0
    for c in dados.get("contradicoes") or []:
        ancoradas = []
        for cit in c.get("citacoes") or []:
            a = grounding.ancorar(cit, texto, 1)
            if a["ok"]:
                ancoradas.append({"citacao": cit, "linha_inicio": a["linha_inicio"],
                                  "linha_fim": a["linha_fim"]})
            else:
                rejeitadas += 1
        achados.append({"descricao": c.get("descricao"), "citacoes_ancoradas": ancoradas,
                        "sem_ancora": not ancoradas})
    saida = {"documento": arquivo, "achados": achados, "citacoes_rejeitadas": rejeitadas}
    salvar_yaml(pasta_gabarito(arquivo) / "baseline.yaml", saida)
    return {"achados": len(achados), "citacoes_rejeitadas": rejeitadas,
            "sem_ancora": sum(1 for a in achados if a["sem_ancora"])}


def linhas_numeradas(texto: str) -> str:
    return "\n".join(f"{i:>5}| {l}" for i, l in enumerate(texto.split("\n"), 1))


_ = re  # usado por módulos que importam daqui
