"""O canon do autor: a única parte do sistema com autoridade (seção 4).

Duas marcas controlam essa autoridade, e é aqui que elas são aplicadas:

`proposto_por: claude` num item do canon — o Claude escreveu, o autor ainda não
confirmou. O item vale como referência, com a força de uma regra derivada
(FLEXIBLE): pode gerar WARNING, nunca ERROR. O autor aprova apagando a marca, ou
com `nl.py canon aprovar`.

`formalizacao` numa regra do mundo — a descrição é do autor, mas a forma
estruturada (aplica_a, exige, excecoes) foi traduzida pelo Claude. A seção 5 diz
que uma regra traduzida só entra no solver depois que o autor aprova as
consequências. Aqui isso vale para TODOS os verificadores formais, não só para
regra×regra: uma tradução errada produziria ERROR com a mesma certeza de uma
certa. A aprovação guarda o hash da forma; se a forma mudar depois, a aprovação
cai sozinha.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .io import RAIZ, ErroDeProjeto, carregar_yaml, normalizar_nome, sha_estavel
from .schema import RIGIDEZ

ARQUIVOS = ("characters", "world_rules", "entidades", "timeline", "locations", "intencoes")


def caminho(nome: str):
    return RAIZ / "canon" / f"{nome}.yaml"


def carregar(nome: str) -> dict:
    return carregar_yaml(caminho(nome), {}) or {}


def hash_formal(regra: dict) -> str:
    """Hash só da parte formal de uma regra — o que o solver de fato usa."""
    return sha_estavel({
        "aplica_a": regra.get("aplica_a") or {},
        "exige": regra.get("exige") or {},
        "proibido": bool(regra.get("proibido", False)),
        "excecoes": regra.get("excecoes") or [],
    })


def autoridade(item: dict, arquivo: dict, e_regra: bool = False) -> dict:
    """Rigidez efetiva de um item do canon e o motivo, para o relatório."""
    if str(item.get("proposto_por", "")).casefold() == "claude":
        return {"rigidez": "FLEXIBLE", "autoritativo": False,
                "motivo": "proposto pelo Claude, aguardando aprovação do autor"}
    if e_regra:
        forma = item.get("formalizacao")
        if forma and str(forma.get("proposta_por", "")).casefold() == "claude":
            if forma.get("aprovada_hash") != hash_formal(item):
                motivo = ("formalização alterada depois da aprovação"
                          if forma.get("aprovada_hash") else
                          "formalização do Claude ainda não aprovada pelo autor")
                return {"rigidez": "FLEXIBLE", "autoritativo": False, "motivo": motivo}
    rigidez = item.get("rigidez") or arquivo.get("rigidez_padrao")
    if rigidez not in RIGIDEZ:
        # O sistema nunca escolhe a rigidez: ela é do autor (seção 5).
        return {"rigidez": "FLEXIBLE", "autoritativo": False,
                "motivo": "rigidez não declarada pelo autor"}
    return {"rigidez": rigidez, "autoritativo": True, "motivo": "canon do autor"}


# ---------------------------------------------------------------------------
# Pessoas
# ---------------------------------------------------------------------------

@dataclass
class Pessoa:
    nome: str
    aliases: list[str]
    tipos: list[str]
    nascimento: dict | None
    morte: dict | None
    atributos: dict
    travas: list
    autoridade: dict
    origem: str = "canon"   # canon | fato


class Pessoas:
    def __init__(self, personagens: dict):
        self.por_chave: dict[str, Pessoa] = {}
        self.lista: list[Pessoa] = []
        for item in personagens.get("personagens", []) or []:
            nome = item.get("nome")
            if not nome:
                continue
            p = Pessoa(
                nome=nome,
                aliases=list(item.get("aliases") or []),
                tipos=list(item.get("tipos") or []),
                nascimento=_data(item.get("nascimento")),
                morte=_data(item.get("morte")),
                atributos=dict(item.get("atributos") or {}),
                travas=list(item.get("travas") or []),
                autoridade=autoridade(item, personagens),
            )
            self.lista.append(p)
            for chave in [nome, *p.aliases]:
                self.por_chave[normalizar_nome(chave)] = p

    def resolver(self, nome) -> Pessoa | None:
        return self.por_chave.get(normalizar_nome(nome))

    def canonico(self, nome) -> str:
        p = self.resolver(nome)
        return p.nome if p else str(nome or "").strip()


def _data(valor) -> dict | None:
    if valor in (None, "", {}):
        return None
    if isinstance(valor, int):
        return {"ano": valor, "mes": None, "dia": None}
    if isinstance(valor, str):
        partes = valor.split("-")
        try:
            numeros = [int(p) for p in partes if p]
        except ValueError as erro:
            raise ErroDeProjeto(f"data inválida no canon: {valor!r}") from erro
        return {"ano": numeros[0],
                "mes": numeros[1] if len(numeros) > 1 else None,
                "dia": numeros[2] if len(numeros) > 2 else None}
    if isinstance(valor, dict):
        return {"ano": valor.get("ano"), "mes": valor.get("mes"), "dia": valor.get("dia")}
    raise ErroDeProjeto(f"data inválida no canon: {valor!r}")


# ---------------------------------------------------------------------------
# Hierarquia é_um (seção 5, "Hierarquia de entidades e exceções")
# ---------------------------------------------------------------------------

@dataclass
class Hierarquia:
    pais: dict[str, set[str]] = field(default_factory=dict)
    rotulo: dict[str, str] = field(default_factory=dict)   # normalizado → como o autor escreveu

    @classmethod
    def do_canon(cls, entidades: dict, pessoas: Pessoas | None = None) -> "Hierarquia":
        h = cls()
        for filho, pais in (entidades.get("e_um") or {}).items():
            for pai in (pais if isinstance(pais, list) else [pais]):
                h.ligar(filho, pai)
        for inst, classes in (entidades.get("instancias") or {}).items():
            for c in (classes if isinstance(classes, list) else [classes]):
                h.ligar(inst, c)
        if pessoas:
            for p in pessoas.lista:
                for t in p.tipos:
                    h.ligar(p.nome, t)
                for a in p.aliases:
                    h.ligar(a, p.nome)
        return h

    def _chave(self, x) -> str:
        # Mesma forma de normalizar_predicado: "usa poder", "usa-poder" e
        # "usa_poder" são o mesmo nó.
        k = normalizar_nome(x).replace(" ", "_").replace("-", "_")
        self.rotulo.setdefault(k, str(x))
        return k

    def ligar(self, filho, pai) -> None:
        f, p = self._chave(filho), self._chave(pai)
        self.pais.setdefault(f, set()).add(p)
        self.pais.setdefault(p, set())

    def ancestrais(self, x) -> set[str]:
        inicio = self._chave(x)
        vistos = {inicio}
        pilha = [inicio]
        while pilha:
            for pai in self.pais.get(pilha.pop(), ()):
                if pai not in vistos:
                    vistos.add(pai)
                    pilha.append(pai)
        return vistos

    def e_um(self, x, y) -> bool:
        if x is None or y is None:
            return False
        return self._chave(y) in self.ancestrais(x)

    def descendentes(self, y) -> set[str]:
        """Inclui o próprio y, mesmo que ele não apareça na hierarquia."""
        alvo = self._chave(y)
        return {x for x in self.pais if alvo in self.ancestrais(x)} | {alvo}

    def filhos_diretos(self, y) -> set[str]:
        alvo = self._chave(y)
        return {x for x, pais in self.pais.items() if alvo in pais}

    def ciclos(self) -> list[list[str]]:
        encontrados = []
        for x in self.pais:
            for pai in self.pais[x]:
                if x in self.ancestrais(pai):
                    encontrados.append([self.rotulo.get(x, x), self.rotulo.get(pai, pai)])
        return encontrados

    def nome(self, chave: str) -> str:
        return self.rotulo.get(chave, chave)


@dataclass
class Canon:
    personagens: dict
    regras: dict
    entidades: dict
    timeline: dict
    lugares: dict
    intencoes: dict
    pessoas: Pessoas
    hierarquia: Hierarquia

    @classmethod
    def carregar(cls) -> "Canon":
        personagens = carregar("characters")
        entidades = carregar("entidades")
        pessoas = Pessoas(personagens)
        return cls(
            personagens=personagens,
            regras=carregar("world_rules"),
            entidades=entidades,
            timeline=carregar("timeline"),
            lugares=carregar("locations"),
            intencoes=carregar("intencoes"),
            pessoas=pessoas,
            hierarquia=Hierarquia.do_canon(entidades, pessoas),
        )

    def lista_regras(self) -> list[dict]:
        return list(self.regras.get("regras") or [])

    def autoridade_regra(self, regra: dict) -> dict:
        return autoridade(regra, self.regras, e_regra=True)
