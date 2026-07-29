"""Cenas encenadas — Fase 6. Infraestrutura; o modelo entra depois.

Um beat é um momento resumido. Uma cena é um diálogo: vários atores, um turno
de cada vez. É o caso mais caro e mais frágil do projeto inteiro, e por isso
vem depois dos beats — e por isso o governador da Fase 4 racionou cenas antes
de existir uma única.

O bug mais provável desta fase tem nome: **vazamento entre atores.** É fácil
montar um prompt com o estado da sala e mandar o modelo escrever todo mundo. O
resultado passa em qualquer teste de formato, lê bem, e destrói o projeto em
silêncio: os personagens passam a saber o que só o outro sabia, o segredo
deixa de existir, e nada no log registra o momento em que isso aconteceu.

A defesa é estrutural, não uma checagem no fim: **um turno = um ator = o pacote
dele.** O prompt de cada turno é montado do zero com uma cabeça só. O que os
outros disseram em voz alta entra — foi dito na frente dele; o que os outros
*pensam*, não entra nunca.

Nada aqui chama modelo pago: o `StubModel` da Fase 5 fecha o mesmo contrato e é
contra ele que o portão roda.
"""

from __future__ import annotations

import json

from . import narrate

# Teto duro de turnos. Não é economia: é forma. Uma cena que não fecha em seis
# turnos não é uma cena, é uma conversa sem foco — e sem teto o custo de uma
# única cena fica ilimitado, o que com modelo aberto em CPU trava o laço.
MAX_TURNOS = 6


class Fala:
    """O que foi dito em voz alta. É a única coisa que atravessa atores."""

    def __init__(self, ator: str, texto: str) -> None:
        self.ator = ator
        self.texto = texto

    def __repr__(self) -> str:
        return f"{self.ator}: {self.texto}"


def turno_prompt(beat: narrate.Beat, ator: str, ditas: list) -> str:
    """O prompt de UM turno: uma cabeça, mais o que se disse em voz alta.

    Montado do zero a cada turno, e não recortado de um prompt geral. A
    diferença importa: recortar deixa o pacote dos outros a um descuido de
    distância, e o descuido não apareceria em teste nenhum de formato.
    """
    if ator not in beat.pacotes:
        raise KeyError(f"{ator} não está nesta cena")
    return json.dumps({
        "instante": {"tick": beat.tick, "dia": beat.day, "local": beat.location},
        "voce": ator,
        "presentes": sorted(beat.participants),
        # Só a cabeça dele. Uma, e nenhuma outra.
        "sua_cabeca": beat.pacotes[ator],
        "dito_em_voz_alta": [{"quem": f.ator, "disse": f.texto} for f in ditas],
    }, ensure_ascii=False, sort_keys=True)


def ordem(beat: narrate.Beat) -> list:
    """Quem fala quando. Determinística, como tudo o mais no motor."""
    quem = sorted(beat.participants)
    saida = []
    for i in range(MAX_TURNOS):
        saida.append(quem[i % len(quem)])
    return saida


def encenar(narrador: narrate.Narrator, beat: narrate.Beat,
            max_turnos: int = MAX_TURNOS) -> dict:
    """Roda a cena turno a turno. Devolve as falas e os prompts usados.

    Os prompts voltam de propósito: é neles que o vazamento apareceria, e um
    portão que não pode inspecionar o que foi enviado só consegue medir o que
    voltou.
    """
    ditas: list[Fala] = []
    prompts: dict[str, list] = {}
    deltas: list = []
    neutros = 0

    for ator in ordem(beat)[:max_turnos]:
        prompt = turno_prompt(beat, ator, ditas)
        prompts.setdefault(ator, []).append(prompt)

        turno = narrate.Beat(
            tick=beat.tick + len(ditas), day=beat.day, kind="cena",
            participants=beat.participants, location=beat.location,
            pacotes={ator: beat.pacotes[ator]},
        )
        r = narrador.narrate(turno)
        if r.origem == "neutro":
            neutros += 1
            continue
        ditas.append(Fala(ator, r.texto))
        deltas.extend(r.deltas)

    return {"falas": ditas, "prompts": prompts, "deltas": deltas,
            "neutros": neutros, "turnos": len(ditas)}


def vazamento_entre_atores(beat: narrate.Beat, prompts: dict) -> list:
    """O portão desta fase.

    Para cada prompt, confere que nenhuma crença que pertence SÓ a outro ator
    aparece nele. Comparação por campo, nunca por substring: mencionar o nome
    de alguém não é saber o que essa pessoa pensa.
    """
    def assinaturas(pacote: dict) -> set:
        return {(c["sobre"], c["que"], str(c["acredita"]))
                for c in pacote.get("crencas", [])}

    minhas = {a: assinaturas(p) for a, p in beat.pacotes.items()}
    achados = []
    for ator, lista in prompts.items():
        alheias = set()
        for outro, sig in minhas.items():
            if outro != ator:
                alheias |= sig
        so_do_outro = alheias - minhas.get(ator, set())
        for prompt in lista:
            dado = json.loads(prompt)
            presentes = assinaturas(dado.get("sua_cabeca", {}))
            for vazada in presentes & so_do_outro:
                achados.append((ator, vazada))
    return achados
