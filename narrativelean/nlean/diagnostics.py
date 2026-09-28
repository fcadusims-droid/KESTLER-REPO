"""Diagnósticos, no formato obrigatório da seção 7, e supressões (seção 8).

As regras de nível estão aqui, num lugar só, e são verificadas na construção:
um diagnóstico que as viole não chega a existir. Isso importa mais do que
parece — se cada verificador aplicasse as regras por conta própria, bastaria um
esquecimento para um verificador semântico emitir ERROR.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone

from .io import RAIZ, carregar_yaml, salvar_yaml, sha, sha_estavel
from .schema import ACOES, CAMADAS, NIVEIS, menor_confianca


class DiagnosticoInvalido(Exception):
    pass


@dataclass
class Evidencia:
    arquivo: str
    linha_inicio: int
    linha_fim: int
    citacao: str
    unidade: str | None = None
    fato: str | None = None           # id do fato, quando a evidência vem de um
    modo: str | None = None
    fonte: str = "obra"               # obra | canon
    confianca: str | None = None      # confiança da extração do fato citado


@dataclass
class Diagnostico:
    prefixo: str                      # TL, RM, AT, RR, REF...
    nivel: str
    verificador: str
    camada: str
    metodo: str
    titulo: str
    regra: str                        # de onde vem a autoridade: canon/… ou método
    evidencias: list[Evidencia]
    conflito: str
    acao: str
    pergunta: str | None = None
    confianca: str = "alta"
    notas: list[str] = field(default_factory=list)
    chave: dict = field(default_factory=dict)   # o que identifica este problema entre versões
    id: str = ""                      # atribuído pelo relatório (TL-001, ...)
    suprimido: bool = False
    supressao: dict | None = None
    revisao: dict | None = None       # parecer do advogado do diabo, se houver

    def __post_init__(self) -> None:
        if self.nivel not in NIVEIS:
            raise DiagnosticoInvalido(f"nível inválido: {self.nivel}")
        if self.camada not in CAMADAS:
            raise DiagnosticoInvalido(f"camada inválida: {self.camada}")
        if self.acao not in ACOES:
            raise DiagnosticoInvalido(f"ação inválida: {self.acao}")
        # Seção 6.2: verificadores semânticos emitem no máximo WARNING.
        if self.camada == "semantica" and self.nivel == "ERROR":
            raise DiagnosticoInvalido(
                f"{self.verificador}: verificador semântico não pode emitir ERROR")
        # Seção 6.4: sem método publicado, no máximo SUGGESTION.
        if self.camada == "semantica" and self.metodo == "proprio" and self.nivel != "SUGGESTION":
            raise DiagnosticoInvalido(
                f"{self.verificador}: método próprio fica limitado a SUGGESTION")
        # Seção 7: a confiança do diagnóstico nunca passa a da extração que o
        # sustenta. Imposto aqui, e não em cada verificador.
        confs = [self.confianca] + [ev.confianca for ev in self.evidencias if ev.confianca]
        self.confianca = menor_confianca(*confs)

    @property
    def impressao(self) -> str:
        """Identidade estável do problema, para supressões e regressão."""
        return sha_estavel({"v": self.verificador, "r": self.regra, "k": self.chave})

    def trecho_hash(self) -> str:
        """Hash do que está citado. Supressão vale enquanto o trecho não mudar."""
        return sha("\n".join(sorted(f"{e.arquivo}:{e.citacao}" for e in self.evidencias
                                   if e.fonte == "obra")))

    def formatar(self) -> str:
        linhas = [f"{self.nivel} {self.id}  —  {self.titulo}"]
        linhas.append(f"Verificador: {self.verificador} ({self.camada})")
        if self.metodo and self.metodo != self.verificador:
            linhas.append(f"Método: {self.metodo}")
        linhas.append(f"Regra: {self.regra}")
        linhas.append("Evidência:")
        for ev in self.evidencias:
            if ev.fonte == "canon":
                linhas.append(f"  {ev.arquivo} — {ev.citacao}")
                continue
            local = f"{ev.arquivo}, l.{ev.linha_inicio}"
            if ev.linha_fim != ev.linha_inicio:
                local += f"–{ev.linha_fim}"
            extra = f" [modo: {ev.modo}]" if ev.modo and ev.modo != "narrador" else ""
            linhas.append(f"  {local} — \"{ev.citacao}\"{extra}")
        linhas.append("Conflito:")
        for parte in self.conflito.split("\n"):
            linhas.append(f"  {parte}")
        linhas.append(f"Confiança da extração: {self.confianca}")
        acao = self.acao if not self.pergunta else f"{self.acao} após pergunta ao autor: {self.pergunta}"
        linhas.append(f"Ação: {acao}")
        for nota in self.notas:
            linhas.append(f"Nota: {nota}")
        if self.revisao:
            linhas.append(f"Advogado do diabo: {self.revisao.get('veredito')} — "
                          f"{self.revisao.get('resumo', '')}")
        linhas.append("Verifique: a citação sustenta o fato extraído?")
        linhas.append(f"Impressão: {self.impressao}")
        return "\n".join(linhas)

    def para_json(self) -> dict:
        d = asdict(self)
        d["impressao"] = self.impressao
        d["trecho_hash"] = self.trecho_hash()
        return d


def nivel_por_evidencia(rigidez: str, autoritativo: bool, modos: list[str],
                        confiancas: list[str]) -> tuple[str, list[str]]:
    """A regra de nível da seção 7, aplicada igual por todos os verificadores formais.

    ERROR só quando: regra STRICT do canon do autor (autoritativa), TODOS os fatos
    envolvidos com modo `narrador` e nenhuma extração de confiança baixa.
    Qualquer outra coisa é WARNING, e a nota diz por quê.
    """
    notas = []
    if not autoritativo:
        notas.append("a regra do canon não tem autoridade plena (ver motivo no canon)")
    if rigidez != "STRICT":
        notas.append("regra FLEXIBLE ou derivada: vira WARNING")
    nao_narrador = sorted({m for m in modos if m != "narrador"})
    if nao_narrador:
        notas.append("fato com modo " + ", ".join(nao_narrador)
                     + ": registra o que alguém disse ou acredita, não um fato do mundo")
    if "baixa" in confiancas:
        notas.append("extração de confiança baixa")
    erro = autoritativo and rigidez == "STRICT" and not nao_narrador and "baixa" not in confiancas
    return ("ERROR" if erro else "WARNING"), notas


# ---------------------------------------------------------------------------
# Supressões — o `# noqa` da obra
# ---------------------------------------------------------------------------

CAMINHO_SUPRESSOES = RAIZ / "suppressions.yaml"


def carregar_supressoes() -> list[dict]:
    dados = carregar_yaml(CAMINHO_SUPRESSOES, {}) or {}
    return list(dados.get("supressoes") or [])


def aplicar_supressoes(diagnosticos: list[Diagnostico]) -> list[dict]:
    """Marca os suprimidos. Devolve as supressões expiradas (o trecho mudou)."""
    por_impressao = {s.get("impressao"): s for s in carregar_supressoes()}
    expiradas = []
    for d in diagnosticos:
        s = por_impressao.get(d.impressao)
        if not s:
            continue
        if s.get("trecho_hash") == d.trecho_hash():
            d.suprimido = True
            d.supressao = s
        else:
            expiradas.append({**s, "diagnostico": d.titulo})
    return expiradas


def suprimir(diagnostico_json: dict, motivo: str) -> dict:
    dados = carregar_yaml(CAMINHO_SUPRESSOES, {}) or {}
    lista = list(dados.get("supressoes") or [])
    lista = [s for s in lista if s.get("impressao") != diagnostico_json["impressao"]]
    entrada = {
        "impressao": diagnostico_json["impressao"],
        "trecho_hash": diagnostico_json["trecho_hash"],
        "verificador": diagnostico_json["verificador"],
        "titulo": diagnostico_json["titulo"],
        "motivo": motivo,
        "criado_em": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }
    lista.append(entrada)
    salvar_yaml(CAMINHO_SUPRESSOES, {**dados, "supressoes": lista})
    return entrada
