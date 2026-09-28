"""Contratos das lentes semânticas e tensões entre elas (seções 6.4 e 6.5).

Cada lente tem um contrato em `verifiers/semantic/contracts/<id>.yaml`, e as
três regras da seção 6.4 são checadas aqui, não confiadas à boa vontade:

1. O verificador não afirma mais do que o método: nenhuma lente emite ERROR.
2. Sem fonte publicada (`metodo: proprio`), no máximo SUGGESTION.
3. Uma lente só passa a `estado: implementado` com testes que disparam E testes
   que não disparam — incluindo obras que violam o método de propósito e
   funcionam.

`lens_conflicts.yaml` não é escrito à mão: é gerado dos campos `tensao_com`
dos contratos, para que a lista de tensões que o advogado do diabo usa nunca
divirja do que os contratos dizem.
"""

from __future__ import annotations

from .io import RAIZ, carregar_yaml, salvar_yaml

PASTA = RAIZ / "verifiers" / "semantic" / "contracts"
CAMPOS = ("verificador", "metodo", "fonte", "o_que_o_metodo_afirma", "o_que_o_metodo_nao_afirma",
          "operacionalizacao", "nivel_maximo", "acao", "criticas_conhecidas", "lente_padrao",
          "estado", "testes")


def carregar() -> dict[str, dict]:
    return {p.stem: (carregar_yaml(p, {}) or {}) for p in sorted(PASTA.glob("*.yaml"))}


def validar(contratos: dict[str, dict] | None = None) -> list[str]:
    contratos = contratos if contratos is not None else carregar()
    problemas = []
    for nome, c in contratos.items():
        for campo in CAMPOS:
            if campo not in c:
                problemas.append(f"contrato {nome}: falta `{campo}`")
        if c.get("nivel_maximo") not in ("WARNING", "SUGGESTION"):
            problemas.append(f"contrato {nome}: nivel_maximo precisa ser WARNING ou SUGGESTION "
                             f"(nenhuma lente emite ERROR)")
        if str(c.get("metodo", "")).strip().casefold() == "proprio" and c.get("nivel_maximo") != "SUGGESTION":
            problemas.append(f"contrato {nome}: método próprio fica limitado a SUGGESTION")
        if c.get("acao") not in ("revisao", "novo_conteudo", "relatorio"):
            problemas.append(f"contrato {nome}: acao inválida: {c.get('acao')}")
        if c.get("estado") == "implementado":
            t = c.get("testes") or {}
            if not t.get("dispara") or not t.get("nao_dispara"):
                problemas.append(f"contrato {nome}: implementado sem testes que disparam e que não disparam")
            if not t.get("violacao_intencional"):
                problemas.append(f"contrato {nome}: faltam testes com obra que viola o método de "
                                 f"propósito e funciona")
        for tensao in c.get("tensao_com") or []:
            alvo = str(tensao.get("com", ""))
            if alvo.startswith("lente:") and alvo.split(":", 1)[1] not in contratos:
                problemas.append(f"contrato {nome}: tensão com lente inexistente {alvo}")
    return problemas


def gerar_conflitos(contratos: dict[str, dict] | None = None) -> dict:
    contratos = contratos if contratos is not None else carregar()
    pares = []
    for nome, c in contratos.items():
        for tensao in c.get("tensao_com") or []:
            pares.append({"lente": nome, "com": tensao.get("com"), "motivo": tensao.get("motivo")})
    dados = {
        "_gerado": "NÃO EDITE: gerado de verifiers/semantic/contracts/*.yaml (campo tensao_com) "
                   "por `nl.py contratos`. Edite os contratos.",
        "tensoes": pares,
    }
    salvar_yaml(RAIZ / "lens_conflicts.yaml", dados)
    return dados
