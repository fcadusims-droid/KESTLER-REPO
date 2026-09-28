"""A citação existe no texto? Linhas calculadas pelo código, nunca pelo extrator."""

import unittest

import apoio  # noqa: F401
from nlean.grounding import ancorar

TEXTO = """Ana tocou o ombro de Carlos.
Os dois sumiram, reaparecendo em “Berlim” — sem aviso.

Ele disse: **nunca mais**
volto àquela cidade."""


class Ancoragem(unittest.TestCase):
    def test_citacao_literal_e_linhas(self):
        r = ancorar("Os dois sumiram, reaparecendo em", TEXTO, linha_base=10)
        self.assertTrue(r["ok"])
        self.assertEqual((r["linha_inicio"], r["linha_fim"]), (11, 11))

    def test_aspas_travessao_e_espacos_normalizados(self):
        r = ancorar('reaparecendo em "Berlim" - sem   aviso', TEXTO)
        self.assertTrue(r["ok"], r)

    def test_citacao_atravessa_linhas_e_ignora_markdown(self):
        r = ancorar("Ele disse: nunca mais volto àquela cidade", TEXTO)
        self.assertTrue(r["ok"], r)
        self.assertEqual((r["linha_inicio"], r["linha_fim"]), (4, 5))

    def test_reticencias_em_ordem(self):
        self.assertTrue(ancorar("Ana tocou o ombro ... reaparecendo em Berlim", TEXTO)["ok"])
        self.assertFalse(ancorar("reaparecendo em Berlim ... Ana tocou o ombro", TEXTO)["ok"])

    def test_citacao_inventada_e_rejeitada(self):
        r = ancorar("Ana teletransportou Carlos para Berlim", TEXTO)
        self.assertFalse(r["ok"])
        self.assertIn("não encontrada", r["motivo"])

    def test_citacao_curta_demais_nao_prova_nada(self):
        self.assertFalse(ancorar("Berlim", TEXTO)["ok"])

    def test_parafrase_nao_passa(self):
        self.assertFalse(ancorar("Ana encostou no ombro de Carlos", TEXTO)["ok"])


if __name__ == "__main__":
    unittest.main()
