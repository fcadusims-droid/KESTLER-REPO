"""Regras do mundo, hierarquia é_um, exceções e regra × regra (seção 5).

O cenário é o do próprio documento: "toda magia exige âncora, exceto as bênçãos
de sacerdotes"; "cura é_um magia"; "sacerdotes curam sem objetos".
"""

import unittest

from apoio import canon_de, docs, fato
from nlean.canon import hash_formal
from nlean.verifiers import rules

ENT = {"e_um": {"cura": ["usa_poder"], "sacerdote": ["clerigo"], "clerigo": ["pessoa"],
                "mago": ["pessoa"]},
       "instancias": {"Lira": ["mago"], "Frei Tomas": ["sacerdote"]}}

MAGIA = {"id": "R-MAGIA-03", "descricao": "toda magia exige âncora",
         "aplica_a": {"predicado": "usa_poder"}, "exige": {"ancora": True}}


def regras(*lista, rigidez="STRICT"):
    return {"rigidez_padrao": rigidez, "regras": list(lista)}


class RegrasDoMundo(unittest.TestCase):
    def test_heranca_e_um_aplica_a_regra(self):
        canon = canon_de(regras=regras(MAGIA), entidades=ENT)
        f = fato("Lira", "cura", qualificadores={"ancora": False})
        diags, _ = rules.verificar_regras(docs(f), canon)
        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].nivel, "ERROR")

    def test_excecao_tira_o_caso_do_escopo(self):
        r = {**MAGIA, "excecoes": [{"sujeito_e_um": "sacerdote"}]}
        canon = canon_de(regras=regras(r), entidades=ENT)
        f = fato("Frei Tomas", "cura", qualificadores={"ancora": False})
        self.assertEqual(rules.verificar_regras(docs(f), canon)[0], [])

    def test_qualificador_ausente_e_lacuna_nao_violacao(self):
        canon = canon_de(regras=regras(MAGIA), entidades=ENT)
        diags, lacunas = rules.verificar_regras(docs(fato("Lira", "cura")), canon)
        self.assertEqual(diags, [])
        self.assertEqual(len(lacunas), 1)

    def test_formalizacao_nao_aprovada_vira_warning(self):
        r = {**MAGIA, "formalizacao": {"proposta_por": "claude"}}
        canon = canon_de(regras=regras(r), entidades=ENT)
        diags, _ = rules.verificar_regras(docs(fato("Lira", "cura", qualificadores={"ancora": "não"})), canon)
        self.assertEqual(diags[0].nivel, "WARNING")

    def test_aprovacao_cai_quando_a_forma_muda(self):
        r = rules.aprovar({**MAGIA, "formalizacao": {"proposta_por": "claude"}})
        canon = canon_de(regras=regras(r), entidades=ENT)
        self.assertTrue(canon.autoridade_regra(r)["autoritativo"])
        mudada = {**r, "exige": {"ancora": False}}
        self.assertFalse(canon.autoridade_regra(mudada)["autoritativo"])
        self.assertNotEqual(hash_formal(r), hash_formal(mudada))

    def test_regra_derivada_flexible_nunca_e_error(self):
        canon = canon_de(regras=regras(MAGIA, rigidez="FLEXIBLE"), entidades=ENT)
        diags, _ = rules.verificar_regras(docs(fato("Lira", "cura", qualificadores={"ancora": False})), canon)
        self.assertEqual(diags[0].nivel, "WARNING")


class RegraXRegra(unittest.TestCase):
    CURA = {"id": "R-CURA-01", "descricao": "sacerdotes curam sem objetos",
            "aplica_a": {"predicado": "cura", "sujeito_e_um": "sacerdote"}, "exige": {"ancora": False}}

    def test_conflito_do_documento_e_detectado(self):
        canon = canon_de(regras=regras(MAGIA, self.CURA), entidades=ENT)
        diags, _ = rules.regra_x_regra(canon)
        self.assertEqual(len(diags), 1)
        self.assertIn("cura", diags[0].conflito)
        self.assertIn("sacerdote", diags[0].conflito)

    def test_excecao_resolve_o_conflito(self):
        r = {**MAGIA, "excecoes": [{"sujeito_e_um": "sacerdote"}]}
        canon = canon_de(regras=regras(r, self.CURA), entidades=ENT)
        self.assertEqual(rules.regra_x_regra(canon)[0], [])

    def test_regra_nao_aprovada_fica_fora_do_solver(self):
        cura = {**self.CURA, "formalizacao": {"proposta_por": "claude"}}
        canon = canon_de(regras=regras(MAGIA, cura), entidades=ENT)
        diags, ignoradas = rules.regra_x_regra(canon)
        self.assertEqual(diags, [])
        self.assertEqual(len(ignoradas), 1)

    def test_escopos_sem_intersecao_nao_conflitam(self):
        voo = {"id": "R-VOO", "aplica_a": {"predicado": "viaja_para"}, "exige": {"ancora": False}}
        canon = canon_de(regras=regras(MAGIA, voo), entidades=ENT)
        self.assertEqual(rules.regra_x_regra(canon)[0], [])


class Bateria(unittest.TestCase):
    def test_casos_gerados_mecanicamente_dos_dois_lados_da_excecao(self):
        r = {**MAGIA, "excecoes": [{"sujeito_e_um": "sacerdote"}]}
        canon = canon_de(regras=regras(r), entidades=ENT)
        textos = [c["texto"] for c in rules.bateria(canon, r)]
        self.assertIn("sacerdote realizando cura com ancora = False: permitido", textos)
        self.assertTrue(any(t.startswith("qualquer um realizando cura com ancora = False: violação")
                            for t in textos))
        # O outro lado da fronteira: um irmão de sacerdote na hierarquia.
        self.assertTrue(any("mago" in t or "clerigo" in t for t in textos))


if __name__ == "__main__":
    unittest.main()
