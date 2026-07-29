"""Infraestrutura de narração — Fase 5. O primeiro lugar onde um LLM entra.

**Nada aqui chama modelo pago.** A restrição é do projeto e não é detalhe de
custo: ela muda a arquitetura, e é melhor construir sabendo disso do que
descobrir depois.

Três consequências, e cada uma virou código neste arquivo:

**A narração não roda no agendador.** O runner do GitHub Actions não tem GPU e
tem teto de tempo. O laço se divide: o mundo avança na nuvem, que é só
aritmética; a narração roda em outro lugar — máquina local com Ollama ou
llama.cpp, ou camada gratuita — e o texto volta como commit. Por isso o
adaptador fala com um endpoint qualquer compatível com OpenAI e não sabe qual
modelo está do outro lado.

**O contrato estrito fica mais importante, não menos.** Modelo pequeno erra
formato com mais frequência que modelo grande. Validar o delta contra limites,
rejeitar com uma re-tentativa e cair no delta neutro deixa de ser precaução e
vira caminho normal — é assim que a maioria das saídas ruins vai ser tratada,
não a minoria.

**O cache é obrigatório desde o primeiro dia.** Com geração medida em minutos
por beat em CPU, reprocessar é inviável, e sem cache o replay determinístico
morre junto: o mundo deixaria de ser função da seed.

O que este módulo NÃO faz é escolher o modelo. Essa decisão se toma medindo
**taxa de saída válida no contrato**, não qualidade de prosa: se o JSON não
fecha, a prosa não importa. Até lá, o stub determinístico exercita todo o
caminho — e é ele que os portões usam.

REGRA INVIOLÁVEL, que aqui é onde mais corre risco: o pacote que vai para o
modelo é montado a partir de `belief`, nunca de `fact`. Um modelo que recebe a
verdade escreve personagens que sabem o que não deveriam saber, e o segredo —
que é a coisa que este motor inteiro existe para representar — evapora sem
deixar rastro no log.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from dataclasses import dataclass, field

# Limites do delta que um beat pode pedir. Um beat é um momento pequeno: ele
# move o mundo um pouco. Sem teto, um modelo que alucina "eles brigaram feio"
# reescreve uma relação de anos numa frase — e o estado do mundo passa a ser
# ditado pela prosa, que é exatamente a inversão que este projeto recusa.
LIMITES = {
    "affect": 0.15,
    "trust": 0.10,
    "tension": 0.20,
    "confidence": 0.25,
    "salience": 0.30,
}

# Campos obrigatórios da resposta. Nada além disto é aceito: um modelo que
# inventa chave nova está inventando mecânica.
CAMPOS = {"texto", "deltas"}
CAMPOS_DELTA = {"tipo", "a", "b", "valor"}

MAX_TEXTO = 900          # um beat é curto por definição
TENTATIVAS = 2           # a original e uma re-tentativa; depois, delta neutro


class ContratoQuebrado(Exception):
    """A saída não fecha o contrato. Sempre carrega o motivo — o motivo é o
    dado que decide qual modelo aberto usar mais tarde."""


@dataclass
class Beat:
    """O pedido: um momento agendado, com o pacote de cada participante."""
    tick: int
    day: int
    kind: str
    participants: list
    location: str | None
    pacotes: dict = field(default_factory=dict)   # agente -> o que ELE acredita

    def prompt(self) -> str:
        """Texto estável: mesma entrada, mesma string, mesmo hash, mesmo cache."""
        return json.dumps({
            "instante": {"tick": self.tick, "dia": self.day,
                         "local": self.location, "tipo": self.kind},
            "presentes": sorted(self.participants),
            "cabecas": {k: self.pacotes[k] for k in sorted(self.pacotes)},
        }, ensure_ascii=False, sort_keys=True)

    def hash(self) -> str:
        return hashlib.sha256(self.prompt().encode("utf-8")).hexdigest()


@dataclass
class Resposta:
    texto: str
    deltas: list
    origem: str            # 'modelo' | 'cache' | 'neutro'
    tentativas: int = 1
    rejeicoes: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Contrato
# ---------------------------------------------------------------------------

def validar(bruto: str, beat: Beat) -> Resposta:
    """Aceita ou explica por que recusou. Nunca conserta silenciosamente.

    Consertar por conta própria seria pior que rejeitar: o portão passaria a
    medir a minha tolerância em vez da taxa de acerto do modelo, e a escolha do
    modelo aberto ficaria cega.
    """
    try:
        dado = json.loads(bruto)
    except (json.JSONDecodeError, TypeError) as erro:
        raise ContratoQuebrado(f"não é JSON: {erro}") from erro

    if not isinstance(dado, dict):
        raise ContratoQuebrado("a raiz não é um objeto")
    if set(dado) != CAMPOS:
        raise ContratoQuebrado(f"campos {sorted(set(dado))}, esperado {sorted(CAMPOS)}")

    texto = dado["texto"]
    if not isinstance(texto, str) or not texto.strip():
        raise ContratoQuebrado("texto vazio")
    if len(texto) > MAX_TEXTO:
        raise ContratoQuebrado(f"texto com {len(texto)} caracteres, teto {MAX_TEXTO}")

    deltas = dado["deltas"]
    if not isinstance(deltas, list):
        raise ContratoQuebrado("deltas não é lista")

    presentes = set(beat.participants)
    limpos = []
    for d in deltas:
        if not isinstance(d, dict) or set(d) != CAMPOS_DELTA:
            raise ContratoQuebrado(f"delta malformado: {d}")
        tipo = d["tipo"]
        if tipo not in LIMITES:
            raise ContratoQuebrado(f"tipo de delta desconhecido: {tipo}")
        # Um beat só mexe em quem estava lá. Sem isto, um momento entre duas
        # pessoas no café altera a relação de outras duas do outro lado da
        # vila — e nada no estado registraria de onde veio.
        if d["a"] not in presentes or d["b"] not in presentes:
            raise ContratoQuebrado(f"delta sobre quem não estava presente: {d}")
        if d["a"] == d["b"]:
            raise ContratoQuebrado("delta de alguém consigo mesmo")
        valor = d["valor"]
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ContratoQuebrado(f"valor não numérico: {valor!r}")
        if abs(valor) > LIMITES[tipo]:
            raise ContratoQuebrado(
                f"{tipo} {valor:+.3f} fora do limite ±{LIMITES[tipo]}")
        limpos.append({"tipo": tipo, "a": d["a"], "b": d["b"],
                       "valor": float(valor)})

    return Resposta(texto=texto.strip(), deltas=limpos, origem="modelo")


def neutro(motivos: list) -> Resposta:
    """O fracasso tem forma: o momento existiu, o mundo não mudou.

    Não escrever nada seria apagar o beat que o governador escolheu; aceitar
    qualquer coisa seria deixar o modelo governar o estado. O meio-termo
    honesto é registrar o momento sem delta e guardar por que falhou.
    """
    return Resposta(
        texto="", deltas=[], origem="neutro",
        tentativas=TENTATIVAS, rejeicoes=list(motivos))


# ---------------------------------------------------------------------------
# Modelos
# ---------------------------------------------------------------------------

class StubModel:
    """Modelo determinístico. Não imita prosa — imita o CONTRATO.

    Existe para que todo o caminho (validação, re-tentativa, delta neutro,
    cache) seja exercitável e testável sem GPU, sem rede e sem centavo. Os
    portões da Fase 5 rodam contra ele.
    """

    def __init__(self, falhas: dict | None = None) -> None:
        # hash do beat -> lista de saídas ruins a devolver antes da boa.
        self.falhas = falhas or {}
        self.chamadas = 0

    def complete(self, prompt: str, beat: Beat) -> str:
        self.chamadas += 1
        roteiro = self.falhas.get(beat.hash())
        if roteiro:
            return roteiro.pop(0)
        quem = sorted(beat.participants)
        par = quem[:2]
        deltas = []
        if len(par) == 2:
            # Determinístico e dentro dos limites: derivado do hash, não de
            # sorteio. Duas execuções da mesma entrada dão o mesmo delta.
            n = int(beat.hash()[:8], 16) % 21 - 10
            deltas.append({"tipo": "affect", "a": par[0], "b": par[1],
                           "valor": round(n / 100.0, 3)})
        return json.dumps({
            "texto": f"Dia {beat.day}: {', '.join(quem)} se cruzam"
                     f"{' em ' + beat.location if beat.location else ''}.",
            "deltas": deltas,
        }, ensure_ascii=False)


class OpenAICompatModel:
    """Adaptador para qualquer endpoint compatível com OpenAI.

    Serve Ollama, llama.cpp, vLLM e camadas gratuitas sem mudar uma linha —
    é por isso que o adaptador não conhece o nome do modelo, só a URL. A
    escolha do modelo aberto é decisão de medição, não de código.

    Sem dependência externa: `urllib` basta, e o motor continua rodando com
    Python puro.
    """

    def __init__(self, base_url: str, model: str, timeout: int = 300) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout
        self.chamadas = 0

    def complete(self, prompt: str, beat: Beat) -> str:
        import urllib.request

        self.chamadas += 1
        corpo = json.dumps({
            "model": self.model,
            "messages": [
                {"role": "system", "content": SISTEMA},
                {"role": "user", "content": prompt},
            ],
            # Determinismo primeiro: o mundo é função da seed, e uma narração
            # com temperatura alta quebraria isso mesmo com cache — bastaria
            # um cache frio para o passado mudar.
            "temperature": 0,
            "response_format": {"type": "json_object"},
        }).encode("utf-8")
        req = urllib.request.Request(
            f"{self.base_url}/chat/completions", data=corpo,
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            dado = json.loads(r.read().decode("utf-8"))
        return dado["choices"][0]["message"]["content"]


SISTEMA = (
    "Você escreve um momento curto de uma vila. Responda APENAS um objeto JSON "
    'com exatamente duas chaves: "texto" (string, até 900 caracteres) e '
    '"deltas" (lista). Cada delta é um objeto com "tipo" (affect, trust, '
    'tension, confidence ou salience), "a", "b" (dois presentes, diferentes) e '
    '"valor" (número pequeno). Escreva só o que os presentes poderiam saber: '
    "o que cada um acredita está no pacote, e não há mais nada."
)


# ---------------------------------------------------------------------------
# Cache e execução
# ---------------------------------------------------------------------------

class Narrator:
    def __init__(self, conn: sqlite3.Connection, model) -> None:
        self.conn = conn
        self.model = model
        self.acertos_de_cache = 0

    def _do_cache(self, chave: str) -> Resposta | None:
        row = self.conn.execute(
            "SELECT texto, deltas_json FROM narration_cache WHERE hash = ?",
            (chave,)).fetchone()
        if row is None:
            return None
        self.acertos_de_cache += 1
        return Resposta(texto=row["texto"],
                        deltas=json.loads(row["deltas_json"]),
                        origem="cache")

    def _guardar(self, chave: str, beat: Beat, r: Resposta) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO narration_cache (hash, tick, day, texto,"
            " deltas_json, origem, tentativas, rejeicoes_json)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (chave, beat.tick, beat.day, r.texto, json.dumps(r.deltas),
             r.origem, r.tentativas, json.dumps(r.rejeicoes)))
        self.conn.commit()

    def narrate(self, beat: Beat) -> Resposta:
        """Uma chamada por beat, no máximo duas tentativas, sempre cacheada."""
        chave = beat.hash()
        guardada = self._do_cache(chave)
        if guardada is not None:
            return guardada

        motivos: list[str] = []
        for tentativa in range(1, TENTATIVAS + 1):
            bruto = self.model.complete(beat.prompt(), beat)
            try:
                r = validar(bruto, beat)
            except ContratoQuebrado as erro:
                motivos.append(str(erro))
                continue
            r.tentativas = tentativa
            r.rejeicoes = motivos
            self._guardar(chave, beat, r)
            return r

        r = neutro(motivos)
        self._guardar(chave, beat, r)
        return r


# ---------------------------------------------------------------------------
# O pacote de cada cabeça
# ---------------------------------------------------------------------------

def pacote(conn: sqlite3.Connection, agent_id: str, tick: int) -> dict:
    """O que ESTE agente sabe — lido de `belief`, jamais de `fact`.

    Este é o ponto do motor com mais risco de vazamento, porque `fact` está a
    um JOIN de distância e o texto sairia mais bonito com ele. Sairia errado:
    um modelo que recebe a verdade escreve gente que sabe o que não deveria, e
    o segredo desaparece sem deixar rastro em lugar nenhum.

    Por isso o objeto que vai daqui carrega `acredita`, e nunca `verdade`.
    """
    crencas = []
    for b in conn.execute(
            "SELECT b.*, f.subject, f.predicate, f.object FROM belief b"
            " JOIN fact f ON f.id = b.fact_id"
            " WHERE b.agent_id = ? AND b.acquired_tick <= ?"
            " ORDER BY b.salience DESC LIMIT 12", (agent_id, tick)):
        crencas.append({
            "sobre": b["subject"],
            "que": b["predicate"],
            # A versão DELE, e só ela. Se distorceu, vai a distorção; se não
            # distorceu, ele acredita no que de fato aconteceu e é isso que
            # vai — não porque seja a verdade, mas porque é a crença dele, e
            # as duas coincidem neste caso.
            #
            # Mandar None para crença fiel, como esta função fazia antes,
            # esvaziava o pacote: o modelo receberia doze crenças sem
            # conteúdo nenhum e teria de inventar o que cada um sabe.
            "acredita": b["distorted_object"] if b["distortion"] else b["object"],
            "confianca": round(b["confidence"], 2),
            "de_ouvir": bool(b["source_agent_id"]),
        })

    sabe = [r["concept"] for r in conn.execute(
        "SELECT concept FROM knowledge WHERE agent_id = ? AND grasp >= 0.55"
        " ORDER BY concept", (agent_id,))]
    nao_sabe = [r["concept"] for r in conn.execute(
        "SELECT concept FROM knowledge WHERE agent_id = ? AND grasp < 0.55"
        " ORDER BY concept", (agent_id,))]

    return {"crencas": crencas, "entende": sabe, "nao_entende": nao_sabe}


def vazou(pacotes: dict, conn: sqlite3.Connection) -> list:
    """Procura verdade no pacote. Um portão, não um comentário.

    A comparação é POR CAMPO, não por substring do pacote inteiro. Buscar a
    string solta acusava vazamento toda vez que o objeto secreto de um fato
    era o nome de alguém: "nuno ama sano" fazia qualquer pacote que
    mencionasse Sano por outro motivo parecer vazado. Saber que Sano existe
    não é saber que Nuno o ama.

    O que de fato vaza é o objeto de um fato aparecer como CONTEÚDO de crença
    de quem não crê nele fielmente — e vazamento silencioso é o modo mais
    provável de este projeto falhar sem ninguém perceber.
    """
    fatos = {}
    for f in conn.execute(
            "SELECT id, subject, predicate, object FROM fact"
            " WHERE visibility != 'publico'"):
        if f["object"]:
            fatos[f["id"]] = (f["subject"], f["predicate"], str(f["object"]))

    achados = []
    for agente, p in pacotes.items():
        fieis = {r["fact_id"] for r in conn.execute(
            "SELECT fact_id FROM belief WHERE agent_id = ? AND distortion = 0",
            (agente,))}
        tem = {(c["sobre"], c["que"], str(c["acredita"]))
               for c in p.get("crencas", [])}
        for fid, assinatura in fatos.items():
            if fid not in fieis and assinatura in tem:
                achados.append((agente, fid, assinatura[2]))
    return achados


def montar(conn: sqlite3.Connection, linha) -> Beat:
    """Um beat agendado vira pedido de narração."""
    quem = json.loads(linha["participants_json"])
    local = conn.execute(
        "SELECT location_id FROM agent_state WHERE agent_id = ? AND tick = ?",
        (quem[0], linha["tick"])).fetchone()
    return Beat(
        tick=linha["tick"], day=linha["day"], kind=linha["kind"],
        participants=quem,
        location=local["location_id"] if local else None,
        pacotes={a: pacote(conn, a, linha["tick"]) for a in quem},
    )
