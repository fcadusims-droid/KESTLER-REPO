"""Verificador formal: timeline e idades (seção 6.1; o verificador da Fase 1).

Três checagens, todas determinísticas:

1. IDADE × NASCIMENTO. Com dados só de ano, "N anos no ano Y" é compatível com
   nascimento em Y−N−1 ou Y−N: depende de o aniversário já ter passado. O
   exemplo TL-003 do documento ("1987 + 20 = 2007 ≠ 2001") acerta o caso dele,
   mas a mesma conta acusaria como ERROR "nascido em 1987, 20 anos em 2008", que
   é perfeitamente possível. Um ERROR falso com cara de certeza é o pior modo de
   falha do sistema (seção 2); por isso a janela de um ano. Com data completa, a
   conta é exata.

2. AGIR ANTES DE NASCER OU DEPOIS DE MORRER, com datas absolutas.

3. REDE DE RESTRIÇÕES TEMPORAIS (Simple Temporal Network, Dechter, Meiri &
   Pearl, 1991) para tudo o que é relativo: "três dias depois", "onze anos
   antes", eventos do canon encadeados. Cada restrição vira uma aresta; a rede é
   inconsistente exatamente quando existe um ciclo de peso negativo, e esse
   ciclo É o conjunto de restrições em conflito — cada aresta aponta a citação
   ou o item de canon de onde veio. Data que não dá para resolver vira
   "indeterminada", nunca erro.

Só fatos com modo `narrador` entram no mundo (seção 4.2). O que um personagem
diz ou acredita não restringe a timeline — mas uma idade dita por alguém que
contradiz o canon ainda aparece, como WARNING, com o modo explícito.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..canon import Canon, _data, autoridade
from ..diagnostics import Diagnostico, Evidencia, nivel_por_evidencia
from ..io import normalizar_nome
from ..schema import menor_confianca, normalizar_unidade

INF = float("inf")
DIAS_POR_UNIDADE = {"dias": (1, 1), "semanas": (7, 7), "meses": (28, 31), "anos": (365, 366)}


def dias(ano: int, mes: int = 1, dia: int = 1) -> int:
    """Dias desde 1970-01-01, calendário gregoriano proléptico, qualquer ano inteiro."""
    y = ano - (1 if mes <= 2 else 0)
    era = (y if y >= 0 else y - 399) // 400
    yoe = y - era * 400
    doy = (153 * (mes + (-3 if mes > 2 else 9)) + 2) // 5 + dia - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe - 719468


def _ultimo_dia(ano: int, mes: int) -> int:
    proximo = dias(ano + (mes == 12), 1 if mes == 12 else mes + 1, 1)
    return proximo - dias(ano, mes, 1)


def intervalo_data(data: dict) -> tuple[int, int] | None:
    """Intervalo [primeiro dia, último dia] que uma data de precisão parcial cobre."""
    if not data or data.get("ano") is None:
        return None
    a, m, d = data["ano"], data.get("mes"), data.get("dia")
    if m is None:
        return dias(a, 1, 1), dias(a, 12, 31)
    if d is None:
        return dias(a, m, 1), dias(a, m, _ultimo_dia(a, m))
    return dias(a, m, d), dias(a, m, d)


def intervalo_desvio(desvio: dict) -> tuple[int, int]:
    lo_mult, hi_mult = DIAS_POR_UNIDADE[desvio["unidade"]]
    lo, hi = desvio["min"] * lo_mult, desvio["max"] * hi_mult
    if desvio.get("sentido") == "antes":
        lo, hi = -hi, -lo
    return int(lo), int(hi)


def formatar_data(data: dict) -> str:
    partes = [str(data["ano"])]
    if data.get("mes"):
        partes.append(f"{data['mes']:02d}")
    if data.get("dia"):
        partes.append(f"{data['dia']:02d}")
    return "-".join(partes)


# ---------------------------------------------------------------------------
# Proveniência: de onde vem cada restrição
# ---------------------------------------------------------------------------

@dataclass
class Origem:
    """Uma restrição carrega o fato ou o item de canon que a sustenta."""
    tipo: str                         # fato | canon | axioma
    descricao: str
    fato: dict | None = None
    canon_ref: str | None = None
    autoridade: dict | None = None

    def evidencia(self) -> Evidencia:
        if self.tipo == "canon":
            return Evidencia(arquivo=self.canon_ref or "canon", linha_inicio=0, linha_fim=0,
                             citacao=self.descricao, fonte="canon")
        f = self.fato
        return Evidencia(arquivo=f["local"]["arquivo"], linha_inicio=f["local"]["linha_inicio"],
                         linha_fim=f["local"]["linha_fim"], citacao=f["citacao"],
                         unidade=f["local"].get("unidade"), fato=f["id"], modo=f["modo"],
                         confianca=f.get("confianca_extracao"))


@dataclass
class Aresta:
    de: int
    para: int
    peso: float
    origem: Origem
    texto: str


@dataclass
class Rede:
    """t[para] − t[de] ≤ peso. O nó 0 é a origem do tempo."""
    nomes: list[str] = field(default_factory=lambda: ["origem"])
    rotulos: dict[str, str] = field(default_factory=dict)
    arestas: list[Aresta] = field(default_factory=list)

    def no(self, nome: str, rotulo: str | None = None) -> int:
        if nome not in self.nomes:
            self.nomes.append(nome)
        if rotulo:
            self.rotulos.setdefault(nome, rotulo)
        return self.nomes.index(nome)

    def rotulo(self, i: int) -> str:
        nome = self.nomes[i]
        return self.rotulos.get(nome, nome)

    def absoluta(self, nome: str, lo: int, hi: int, origem: Origem, texto: str) -> None:
        i = self.no(nome)
        self.arestas.append(Aresta(0, i, hi, origem, texto))
        self.arestas.append(Aresta(i, 0, -lo, origem, texto))

    def relativa(self, a: str, b: str, lo: float, hi: float, origem: Origem, texto: str) -> None:
        """t[b] − t[a] ∈ [lo, hi]."""
        ia, ib = self.no(a), self.no(b)
        if hi != INF:
            self.arestas.append(Aresta(ia, ib, hi, origem, texto))
        if lo != -INF:
            self.arestas.append(Aresta(ib, ia, -lo, origem, texto))

    def ciclo_negativo(self, ignorar: set[int]) -> list[Aresta] | None:
        """Bellman-Ford a partir de uma fonte virtual ligada a todos os nós."""
        n = len(self.nomes)
        dist = [0.0] * n
        pred: list[int | None] = [None] * n   # índice da aresta
        ativas = [(k, a) for k, a in enumerate(self.arestas) if k not in ignorar]
        x = None
        for _ in range(n):
            x = None
            for k, a in ativas:
                if dist[a.de] + a.peso < dist[a.para]:
                    dist[a.para] = dist[a.de] + a.peso
                    pred[a.para] = k
                    x = a.para
            if x is None:
                return None
        # x foi relaxado na n-ésima rodada: andar n vezes para trás cai no ciclo.
        for _ in range(n):
            x = self.arestas[pred[x]].de
        ciclo, v = [], x
        while True:
            a = self.arestas[pred[v]]
            ciclo.append(a)
            v = a.de
            if v == x:
                break
        ciclo.reverse()
        return ciclo


# ---------------------------------------------------------------------------
# Verificador
# ---------------------------------------------------------------------------

def _pessoa(canon: Canon, nome) -> str:
    return canon.pessoas.canonico(nome)


def _no_fato(f: dict) -> str:
    return f"ref:{normalizar_nome(f['ref'])}" if f.get("ref") else f"fato:{f['id']}"


def _rotulo_fato(f: dict) -> str:
    obj = f" {f['objeto']}" if f.get("objeto") not in (None, "") else ""
    return f"{f['sujeito']} {f['predicado']}{obj}"


def _padrao(f: dict) -> bool:
    cal = (f.get("tempo") or {}).get("calendario")
    return cal in (None, "", "padrao", "padrão")


def verificar(fatos_por_doc: dict[str, dict], canon: Canon) -> tuple[list[Diagnostico], list[dict]]:
    todos = [f for doc in fatos_por_doc.values() for f in doc.get("fatos", [])]
    diagnosticos: list[Diagnostico] = []
    indeterminadas: list[dict] = []

    for f in todos:
        t = f.get("tempo") or {}
        if t and not _padrao(f):
            indeterminadas.append({"fato": f["id"], "motivo": f"calendário '{t.get('calendario')}' sem conversão declarada",
                                   "citacao": f["citacao"], "local": f["local"]})
        rel = t.get("relativo_a") if t else None
        if rel and not rel.get("resolvido"):
            indeterminadas.append({"fato": f["id"], "motivo": "âncora de tempo relativo não resolvida",
                                   "citacao": f["citacao"], "local": f["local"]})

    diagnosticos += _idades(todos, canon)
    diagnosticos += _antes_de_nascer(todos, canon)
    diagnosticos += _rede(todos, canon)
    return diagnosticos, indeterminadas


# -- nascimentos conhecidos ------------------------------------------------

def _nascimentos(todos, canon) -> dict[str, list[tuple[dict, Origem]]]:
    """pessoa → [(data, origem)], do canon e de fatos narrador."""
    saida: dict[str, list[tuple[dict, Origem]]] = {}
    for p in canon.pessoas.lista:
        if p.nascimento and p.nascimento.get("ano") is not None:
            saida.setdefault(p.nome, []).append((p.nascimento, Origem(
                "canon", f"{p.nome}.nascimento = {formatar_data(p.nascimento)}",
                canon_ref="canon/characters.yaml", autoridade=p.autoridade)))
    for f in todos:
        if f["predicado"] == "nasce_em" and f["modo"] == "narrador" and _padrao(f):
            t = f.get("tempo") or {}
            if t.get("ano") is not None:
                saida.setdefault(_pessoa(canon, f["sujeito"]), []).append(
                    (t, Origem("fato", _rotulo_fato(f), fato=f)))
    return saida


def _mortes(todos, canon) -> dict[str, list[tuple[dict, Origem]]]:
    saida: dict[str, list[tuple[dict, Origem]]] = {}
    for p in canon.pessoas.lista:
        if p.morte and p.morte.get("ano") is not None:
            saida.setdefault(p.nome, []).append((p.morte, Origem(
                "canon", f"{p.nome}.morte = {formatar_data(p.morte)}",
                canon_ref="canon/characters.yaml", autoridade=p.autoridade)))
    for f in todos:
        if f["predicado"] == "morre_em" and f["modo"] == "narrador" and _padrao(f):
            t = f.get("tempo") or {}
            if t.get("ano") is not None:
                saida.setdefault(_pessoa(canon, f["sujeito"]), []).append(
                    (t, Origem("fato", _rotulo_fato(f), fato=f)))
    return saida


def _nivel(origens: list[Origem]) -> tuple[str, list[str], str | None]:
    """Nível de um conflito a partir das origens envolvidas.

    Com canon autoritativo STRICT e fatos narrador → o fato está errado: ERROR.
    Sem canon → contradição interna da obra: WARNING, com pergunta ao autor.
    """
    canons = [o for o in origens if o.tipo == "canon"]
    fatos = [o.fato for o in origens if o.tipo == "fato"]
    if not fatos:
        return "WARNING", ["só itens do canon estão envolvidos: o próprio canon se contradiz"], \
            "qual dos itens do canon vale?"
    if not canons:
        return "WARNING", ["contradição interna da obra, sem canon envolvido"], \
            "qual dos trechos está certo?"
    rigidez = "STRICT" if all(o.autoridade["rigidez"] == "STRICT" for o in canons) else "FLEXIBLE"
    autoritativo = all(o.autoridade["autoritativo"] for o in canons)
    nivel, notas = nivel_por_evidencia(rigidez, autoritativo, [f["modo"] for f in fatos],
                                       [f.get("confianca_extracao") for f in fatos])
    for o in canons:
        if not o.autoridade["autoritativo"]:
            notas.append(f"{o.descricao}: {o.autoridade['motivo']}")
    return nivel, notas, None


def _acao(origens: list[Origem]) -> str:
    # Contradição em bíblia, ficha ou cronologia: nunca edição automática de
    # conteúdo (seção 4.3). A troca pontual só vem depois da resposta do autor.
    return "REVISAO"


def _idades(todos, canon) -> list[Diagnostico]:
    saida = []
    nasc = _nascimentos(todos, canon)
    idades = [f for f in todos if f["predicado"] == "tem_idade" and _padrao(f)
              and (f.get("tempo") or {}).get("ano") is not None
              and isinstance(f.get("objeto"), int)]

    for f in idades:
        pessoa = _pessoa(canon, f["sujeito"])
        n, t = f["objeto"], f["tempo"]
        for data_nasc, origem in nasc.get(pessoa, []):
            if origem.tipo == "fato" and origem.fato["id"] == f["id"]:
                continue
            idade_min, idade_max = _idade_possivel(data_nasc, t)
            if idade_min <= n <= idade_max:
                continue
            origens = [origem, Origem("fato", _rotulo_fato(f), fato=f)]
            nivel, notas, pergunta = _nivel(origens)
            b = data_nasc["ano"]
            if idade_min == idade_max:
                esperado = f"{idade_min}"
            else:
                esperado = f"{idade_min} ou {idade_max}"
            conflito = (f"nascimento em {formatar_data(data_nasc)} → em {formatar_data(t)} a idade seria "
                        f"{esperado}; o texto diz {n}.\n"
                        f"Para ter {n} anos em {t['ano']}, o nascimento seria em {t['ano'] - n - 1} ou "
                        f"{t['ano'] - n} (não em {b}).")
            saida.append(Diagnostico(
                prefixo="TL", nivel=nivel, verificador="timeline", camada="formal",
                metodo="timeline", titulo=f"Idade de {pessoa} incompatível com o nascimento",
                regra=origem.descricao if origem.tipo == "canon" else "consistência interna (idade × nascimento)",
                evidencias=[o.evidencia() for o in origens], conflito=conflito,
                acao=_acao(origens),
                pergunta=pergunta or f"mudar a idade ({n} → {esperado}) ou o ano ({t['ano']} → "
                                     f"{b + n}–{b + n + 1})?",
                confianca=menor_confianca(*(o.fato.get("confianca_extracao") for o in origens if o.fato)),
                notas=notas, chave={"tipo": "idade", "pessoa": normalizar_nome(pessoa),
                                    "fatos": sorted(o.fato["id"] for o in origens if o.fato)},
            ))

    # Idades entre si, sem nascimento conhecido: "20 em 2001" e "29 em 2005"
    # implicam nascimentos que não se cruzam.
    por_pessoa: dict[str, list[dict]] = {}
    for f in idades:
        if f["modo"] == "narrador":
            por_pessoa.setdefault(_pessoa(canon, f["sujeito"]), []).append(f)
    relativas = _pessoas_com_idade_relativa(todos, canon)
    for pessoa, lista in por_pessoa.items():
        if pessoa in nasc or pessoa in relativas:
            continue      # já comparadas contra o nascimento, ou cobertas pela rede
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                a, b = lista[i], lista[j]
                ra = (a["tempo"]["ano"] - a["objeto"] - 1, a["tempo"]["ano"] - a["objeto"])
                rb = (b["tempo"]["ano"] - b["objeto"] - 1, b["tempo"]["ano"] - b["objeto"])
                if ra[0] <= rb[1] and rb[0] <= ra[1]:
                    continue
                origens = [Origem("fato", _rotulo_fato(a), fato=a), Origem("fato", _rotulo_fato(b), fato=b)]
                saida.append(Diagnostico(
                    prefixo="TL", nivel="WARNING", verificador="timeline", camada="formal",
                    metodo="timeline", titulo=f"Duas idades de {pessoa} que não fecham entre si",
                    regra="consistência interna (idade × idade)",
                    evidencias=[o.evidencia() for o in origens],
                    conflito=(f"{a['objeto']} anos em {a['tempo']['ano']} → nascimento em {ra[0]}–{ra[1]};\n"
                              f"{b['objeto']} anos em {b['tempo']['ano']} → nascimento em {rb[0]}–{rb[1]}.\n"
                              f"Os intervalos não se cruzam."),
                    acao="REVISAO", pergunta="qual das duas idades (ou dos dois anos) está certa?",
                    confianca=menor_confianca(a.get("confianca_extracao"), b.get("confianca_extracao")),
                    notas=["contradição interna da obra, sem canon envolvido"],
                    chave={"tipo": "idade-idade", "pessoa": normalizar_nome(pessoa),
                           "fatos": sorted([a["id"], b["id"]])},
                ))
    return saida


def _pessoas_com_idade_relativa(todos, canon) -> set[str]:
    """Pessoas sem nascimento conhecido que têm alguma idade em tempo relativo."""
    nasc = _nascimentos(todos, canon)
    return {_pessoa(canon, f["sujeito"]) for f in todos
            if f["predicado"] == "tem_idade" and f["modo"] == "narrador" and _padrao(f)
            and isinstance(f.get("objeto"), int) and (f.get("tempo") or {}).get("relativo_a")
            and _pessoa(canon, f["sujeito"]) not in nasc}


def _idade_possivel(nasc: dict, t: dict) -> tuple[int, int]:
    """Idades possíveis de quem nasceu em `nasc`, no momento `t`."""
    base = t["ano"] - nasc["ano"]
    if nasc.get("mes") and nasc.get("dia") and t.get("mes") and t.get("dia"):
        ja_fez = (t["mes"], t["dia"]) >= (nasc["mes"], nasc["dia"])
        exata = base if ja_fez else base - 1
        return exata, exata
    if nasc.get("mes") and t.get("mes") and nasc["mes"] != t["mes"]:
        exata = base if t["mes"] > nasc["mes"] else base - 1
        return exata, exata
    return base - 1, base


def _antes_de_nascer(todos, canon) -> list[Diagnostico]:
    saida = []
    nasc, mortes = _nascimentos(todos, canon), _mortes(todos, canon)
    for f in todos:
        if f["tipo"] != "evento" or f["modo"] != "narrador" or not _padrao(f):
            continue
        if f["predicado"] in ("nasce_em", "morre_em"):
            continue
        t = f.get("tempo") or {}
        if t.get("ano") is None:
            continue
        pessoa = _pessoa(canon, f["sujeito"])
        for data, origem in nasc.get(pessoa, []):
            if t["ano"] < data["ano"]:
                origens = [origem, Origem("fato", _rotulo_fato(f), fato=f)]
                nivel, notas, pergunta = _nivel(origens)
                saida.append(_diag_vida(pessoa, "antes de nascer", origens, nivel, notas, pergunta,
                                        f"{pessoa} age em {t['ano']}, mas nasce em {formatar_data(data)}."))
        for data, origem in mortes.get(pessoa, []):
            if t["ano"] > data["ano"]:
                origens = [origem, Origem("fato", _rotulo_fato(f), fato=f)]
                nivel, notas, pergunta = _nivel(origens)
                saida.append(_diag_vida(pessoa, "depois de morrer", origens, nivel, notas, pergunta,
                                        f"{pessoa} age em {t['ano']}, mas morre em {formatar_data(data)}.\n"
                                        f"Se a morte for só o que alguém acredita, o fato de morte "
                                        f"deveria ter modo `pensamento` ou `fala`, não `narrador`."))
    return saida


def _diag_vida(pessoa, quando, origens, nivel, notas, pergunta, conflito) -> Diagnostico:
    return Diagnostico(
        prefixo="TL", nivel=nivel, verificador="timeline", camada="formal", metodo="timeline",
        titulo=f"{pessoa} age {quando}",
        regra=origens[0].descricao if origens[0].tipo == "canon" else "consistência interna (vida × ação)",
        evidencias=[o.evidencia() for o in origens], conflito=conflito, acao="REVISAO",
        pergunta=pergunta or "o ano do acontecimento ou a data de nascimento/morte está errado?",
        confianca=menor_confianca(*(o.fato.get("confianca_extracao") for o in origens if o.fato)),
        notas=notas,
        chave={"tipo": quando, "pessoa": normalizar_nome(pessoa),
               "fatos": sorted(o.fato["id"] for o in origens if o.fato)},
    )


# -- rede de restrições ---------------------------------------------------

def _montar_rede(todos, canon) -> Rede:
    r = Rede()
    aut_tl = canon.timeline
    for ev in canon.timeline.get("eventos") or []:
        if not ev.get("id"):
            continue
        aut = autoridade(ev, aut_tl)
        nome = f"ev:{ev['id']}"
        r.no(nome, f"{ev['id']} ({ev.get('descricao', '')})")
        data = _data(ev.get("data"))      # aceita 1961, "2036-03-09" ou {ano, mes, dia}
        iv = intervalo_data(data) if data else None
        if iv:
            r.absoluta(nome, iv[0], iv[1], Origem("canon", f"{ev['id']}: {formatar_data(data)}",
                                                  canon_ref="canon/timeline.yaml", autoridade=aut),
                       f"{ev['id']} em {formatar_data(data)}")
        dep = ev.get("depois_de")
        if dep and dep.get("evento") and dep.get("desvio"):
            desvio = dict(dep["desvio"])
            desvio["unidade"] = normalizar_unidade(desvio.get("unidade")) or "dias"
            desvio.setdefault("min", desvio.get("valor", 0))
            desvio.setdefault("max", desvio.get("valor", desvio["min"]))
            lo, hi = intervalo_desvio(desvio)
            r.relativa(f"ev:{dep['evento']}", nome, lo, hi,
                       Origem("canon", f"{ev['id']} depois de {dep['evento']}",
                              canon_ref="canon/timeline.yaml", autoridade=aut),
                       f"{ev['id']} {desvio['min']}–{desvio['max']} {desvio['unidade']} depois de {dep['evento']}")

    nasc, mortes = _nascimentos(todos, canon), _mortes(todos, canon)
    for pessoa, lista in nasc.items():
        nome = f"nasc:{normalizar_nome(pessoa)}"
        r.no(nome, f"nascimento de {pessoa}")
        for data, origem in lista:
            iv = intervalo_data(data)
            r.absoluta(nome, iv[0], iv[1], origem, f"nascimento de {pessoa} em {formatar_data(data)}")
    for pessoa, lista in mortes.items():
        nome = f"morte:{normalizar_nome(pessoa)}"
        r.no(nome, f"morte de {pessoa}")
        for data, origem in lista:
            iv = intervalo_data(data)
            r.absoluta(nome, iv[0], iv[1], origem, f"morte de {pessoa} em {formatar_data(data)}")
        if pessoa in nasc:
            r.relativa(f"nasc:{normalizar_nome(pessoa)}", nome, 0, INF,
                       Origem("axioma", "ninguém morre antes de nascer"), f"{pessoa} nasce antes de morrer")

    # Quem não tem nascimento conhecido mas tem idade em tempo relativo ganha um
    # nascimento VIRTUAL, sem data: basta para duas idades se checarem entre si
    # ("12 anos em 2034" e "12 anos quatro anos depois de 2037" não fecham).
    virtuais = _pessoas_com_idade_relativa(todos, canon)
    for pessoa in virtuais:
        r.no(f"nasc:{normalizar_nome(pessoa)}", f"nascimento (desconhecido) de {pessoa}")

    for f in todos:
        if f["modo"] != "narrador" or not _padrao(f) or f["predicado"] in ("nasce_em", "morre_em"):
            continue
        t = f.get("tempo") or {}
        if not t:
            continue
        rel = t.get("relativo_a")
        # Idade com ano absoluto já foi checada acima; só entra na rede se
        # relativa — ou se a pessoa tem nascimento virtual.
        if f["predicado"] == "tem_idade" and not rel and _pessoa(canon, f["sujeito"]) not in virtuais:
            continue
        nome = _no_fato(f)
        r.no(nome, _rotulo_fato(f))
        origem = Origem("fato", _rotulo_fato(f), fato=f)
        if t.get("ano") is not None:
            iv = intervalo_data(t)
            r.absoluta(nome, iv[0], iv[1], origem, f"{_rotulo_fato(f)} em {formatar_data(t)}")
        if rel and rel.get("resolvido") and rel.get("desvio"):
            ancora = None
            if rel.get("fato"):
                alvo = next((g for g in todos if g["id"] == rel["fato"]), None)
                ancora = _no_fato(alvo) if alvo else None
            elif rel.get("evento"):
                ancora = f"ev:{rel['evento']}"
            if ancora:
                lo, hi = intervalo_desvio(rel["desvio"])
                d = rel["desvio"]
                r.relativa(ancora, nome, lo, hi, origem,
                           f"{_rotulo_fato(f)}: {d['min']:g}–{d['max']:g} {d['unidade']} "
                           f"{d['sentido']} de {r.rotulos.get(ancora, ancora)}")
        pessoa = _pessoa(canon, f["sujeito"])
        chave_nasc = f"nasc:{normalizar_nome(pessoa)}"
        idade_na_rede = rel or pessoa in virtuais
        if f["predicado"] == "tem_idade" and idade_na_rede and isinstance(f.get("objeto"), int) \
                and chave_nasc in r.nomes:
            n = f["objeto"]
            r.relativa(chave_nasc, nome, n * 365, (n + 1) * 366 - 1, origem,
                       f"{pessoa} tem {n} anos em: {_rotulo_fato(f)}")
        elif f["tipo"] == "evento" and rel and chave_nasc in r.nomes:
            r.relativa(chave_nasc, nome, 0, INF, origem, f"{pessoa} já nasceu quando: {_rotulo_fato(f)}")
    return r


def _rede(todos, canon) -> list[Diagnostico]:
    r = _montar_rede(todos, canon)
    saida, ignorar = [], set()
    for _ in range(50):     # no máximo 50 conflitos distintos por rodada
        ciclo = r.ciclo_negativo(ignorar)
        if not ciclo:
            break
        origens: list[Origem] = []
        vistos = set()
        for a in ciclo:
            chave = (a.origem.tipo, a.origem.fato["id"] if a.origem.fato else a.origem.descricao)
            if chave not in vistos:
                vistos.add(chave)
                origens.append(a.origem)
        # Idade/nascimento com ano absoluto já é coberta por `_idades`: não duplicar.
        total = sum(a.peso for a in ciclo)
        nivel, notas, pergunta = _nivel(origens)
        conflito = "Estas restrições não podem valer ao mesmo tempo:\n" + "\n".join(
            f"- {a.texto}" for a in _unicas(ciclo)) + \
            f"\nJuntas, elas exigem um intervalo impossível (faltam {abs(int(total))} dia(s))."
        saida.append(Diagnostico(
            prefixo="TL", nivel=nivel, verificador="timeline", camada="formal", metodo="timeline",
            titulo="Restrições de tempo em conflito",
            regra=", ".join(o.descricao for o in origens if o.tipo == "canon") or
                  "consistência interna (rede de tempo)",
            evidencias=[o.evidencia() for o in origens if o.tipo != "axioma"], conflito=conflito,
            acao="REVISAO", pergunta=pergunta or "qual destas datas ou intervalos está errado?",
            confianca=menor_confianca(*(o.fato.get("confianca_extracao") for o in origens if o.fato)),
            notas=notas,
            chave={"tipo": "rede", "origens": sorted(
                (o.fato["id"] if o.fato else o.descricao) for o in origens)},
        ))
        # Remove do próximo passo a aresta de fato de menor confiança do ciclo
        # (o canon é a última coisa a sair), para achar os conflitos seguintes.
        indices = [k for k, a in enumerate(r.arestas) if a in ciclo]
        de_fato = [k for k in indices if r.arestas[k].origem.tipo == "fato"]
        escolha = min(de_fato or indices, key=lambda k: _peso_conf(r.arestas[k].origem))
        ignorar |= {k for k, a in enumerate(r.arestas) if a.origem is r.arestas[escolha].origem}
    return saida


def _peso_conf(o: Origem) -> int:
    if o.fato is None:
        return 9
    return {"baixa": 0, "media": 1, "alta": 2}.get(o.fato.get("confianca_extracao"), 1)


def _unicas(ciclo: list[Aresta]) -> list[Aresta]:
    vistos, saida = set(), []
    for a in ciclo:
        if a.texto not in vistos:
            vistos.add(a.texto)
            saida.append(a)
    return saida
