"""Regras de nível impostas na construção, atributos, referências e métricas."""

import unittest

from apoio import canon_de, docs, fato
from nlean.diagnostics import Diagnostico, DiagnosticoInvalido, Evidencia
from nlean.metrics import pontuar_golden, wilson
from nlean.segment import Unidade, classificar, segmentar
from nlean.verifiers import attributes, references


def diag(**kw):
    base = dict(prefixo="X", nivel="WARNING", verificador="v", camada="formal", metodo="m",
                titulo="t", regra="r", evidencias=[], conflito="c", acao="RELATORIO")
    base.update(kw)
    return Diagnostico(**base)


class RegrasDeNivel(unittest.TestCase):
    def test_semantico_nunca_emite_error(self):
        with self.assertRaises(DiagnosticoInvalido):
            diag(nivel="ERROR", camada="semantica")

    def test_metodo_proprio_limitado_a_suggestion(self):
        with self.assertRaises(DiagnosticoInvalido):
            diag(nivel="WARNING", camada="semantica", metodo="proprio")
        diag(nivel="SUGGESTION", camada="semantica", metodo="proprio")

    def test_confianca_nunca_passa_a_da_extracao(self):
        ev = Evidencia(arquivo="a.md", linha_inicio=1, linha_fim=1, citacao="x", confianca="baixa")
        self.assertEqual(diag(confianca="alta", evidencias=[ev]).confianca, "baixa")


class Atributos(unittest.TestCase):
    def test_canon_contra_obra(self):
        canon = canon_de({"rigidez_padrao": "STRICT",
                          "personagens": [{"nome": "Heitor", "atributos": {"olhos": "verdes"}}]})
        f = fato("Heitor", "tem_atributo", "azuis", qualificadores={"atributo": "olhos"})
        d = attributes.verificar(docs(f), canon)
        self.assertEqual(len(d), 1)
        self.assertEqual(d[0].nivel, "ERROR")

    def test_obra_contra_obra_com_maioria(self):
        fs = [fato("Heitor", "tem_atributo", "verdes", qualificadores={"atributo": "olhos"}) for _ in range(4)]
        fs.append(fato("Heitor", "tem_atributo", "azuis", qualificadores={"atributo": "olhos"}))
        d = attributes.verificar(docs(*fs), canon_de())
        self.assertEqual(len(d), 1)
        self.assertEqual(d[0].nivel, "WARNING")
        self.assertIn("Há maioria clara", d[0].conflito)


BIBLIA = """# O Mundo

## I. Site Anvil

O **Conselho Rubro** governa a partir de Site Anvil, e a Ordem de Vidro obedece.

## II. O Conselho Rubro

Sete cadeiras. A NASA nunca soube.
"""


class Referencias(unittest.TestCase):
    def _unidades(self):
        return {"b.md": segmentar("b.md", BIBLIA, "biblia")}

    def test_termo_citado_e_nunca_definido(self):
        termos = {d.chave["termo"] for d in references.verificar(self._unidades(), canon_de())}
        self.assertIn("ordem de vidro", termos)

    def test_termo_definido_em_titulo(self):
        termos = {d.chave["termo"] for d in references.verificar(self._unidades(), canon_de())}
        self.assertNotIn("conselho rubro", termos)
        self.assertNotIn("site anvil", termos)

    def test_termo_declarado_em_termos_conhecidos(self):
        c = canon_de(entidades={"termos_conhecidos": ["NASA"]})
        termos = {d.chave["termo"] for d in references.verificar(self._unidades(), c)}
        self.assertNotIn("nasa", termos)

    def test_biblia_que_usa_termo_do_mundo_real_sem_verbete(self):
        # Violação intencional que funciona: o detector acusa (SUGGESTION), e o
        # remédio é declarar o termo, não "corrigir" a obra.
        d = [x for x in references.verificar(self._unidades(), canon_de()) if x.chave["termo"] == "nasa"]
        self.assertEqual(d[0].nivel, "SUGGESTION")


class Segmentacao(unittest.TestCase):
    def test_id_da_unidade_nao_muda_quando_se_insere_secao_antes(self):
        a = {u.id for u in segmentar("b.md", BIBLIA, "biblia")}
        b = {u.id for u in segmentar("b.md", BIBLIA.replace("## I.", "## 0. Novo\n\ntexto\n\n## I."), "biblia")}
        self.assertTrue(a <= b)

    def test_front_matter_nao_vira_unidade_e_linhas_batem(self):
        texto = "---\ntitle: X\n---\n\n# Título\n\ncorpo\n"
        u = segmentar("x.md", texto, "prosa")
        self.assertEqual(u[0].linha_inicio, 5)
        self.assertEqual(u[0].linhas[0], "# Título")

    def test_classificacao_incerta_e_baixa(self):
        texto = "# Algo\n\n" + "\n\n".join(["Uma frase expositiva longa sobre o mundo " * 8] * 5)
        self.assertEqual(classificar(texto)["confianca"], "baixa")


class Wilson(unittest.TestCase):
    """Os números do próprio documento (seção 11), fixados como teste."""

    def test_59_de_60_da_limite_inferior_de_90(self):
        self.assertGreaterEqual(wilson(59, 60)[0], 0.90)
        self.assertLess(wilson(58, 60)[0], 0.90)

    def test_55_de_60_da_limite_inferior_de_80(self):
        self.assertGreaterEqual(wilson(55, 60)[0], 0.80)
        self.assertLess(wilson(54, 60)[0], 0.80)

    def test_18_de_20_vai_de_70_a_97(self):
        lo, hi = wilson(18, 20)
        self.assertAlmostEqual(lo, 0.70, delta=0.01)
        self.assertAlmostEqual(hi, 0.97, delta=0.01)

    def test_9_de_10_vai_de_60_a_98(self):
        lo, hi = wilson(9, 10)
        self.assertAlmostEqual(lo, 0.60, delta=0.01)
        self.assertAlmostEqual(hi, 0.98, delta=0.01)


class Golden(unittest.TestCase):
    def test_mentira_registrada_como_fato_e_erro_grave(self):
        item = {"id": "G-1", "dificuldade": "mentira", "origem": "autor",
                "fatos_esperados": [{"sujeito": "Ana", "predicado": "tem_idade", "objeto": 30,
                                     "modo": "fala"}]}
        extraido = fato("Ana", "tem_idade", 30, modo="narrador")
        r = pontuar_golden({"G-1": [extraido]}, [item])
        self.assertEqual(r["recall"]["k"], 1)
        self.assertEqual(r["modo"]["k"], 0)
        self.assertEqual(len(r["erros_graves"]), 1)

    def test_sujeito_por_sobrenome_casa(self):
        item = {"id": "G-2", "fatos_esperados": [{"sujeito": "Anselm Reiter", "predicado": "tem_idade",
                                                  "objeto": 29}]}
        r = pontuar_golden({"G-2": [fato("Reiter", "tem_idade", 29)]}, [item])
        self.assertEqual(r["recall"]["valor"], 1.0)


class UnidadeHash(unittest.TestCase):
    def test_tipo_entra_no_hash(self):
        a = Unidade("x#a", "x.md", "a", 1, 1, ["texto"], "prosa")
        b = Unidade("x#a", "x.md", "a", 1, 1, ["texto"], "biblia")
        self.assertNotEqual(a.hash, b.hash)


if __name__ == "__main__":
    unittest.main()
