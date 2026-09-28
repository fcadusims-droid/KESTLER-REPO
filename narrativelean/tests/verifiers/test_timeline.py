"""Timeline e idades (seção 6.1), incluindo o exemplo TL-003 do documento."""

import unittest

from apoio import canon_de, docs, fato
from nlean.verifiers import timeline

ANA = {"rigidez_padrao": "STRICT", "personagens": [{"nome": "Ana", "nascimento": 1987}]}


def rodar(canon, *fatos):
    return timeline.verificar(docs(*fatos), canon)


class Idade(unittest.TestCase):
    def test_tl003_do_documento_e_error(self):
        # "Ana, com seus vinte anos, entrou na academia em 2001." canon: 1987.
        diags, _ = rodar(canon_de(ANA), fato("Ana", "tem_idade", 20, ano=2001))
        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].nivel, "ERROR")
        self.assertIn("1980 ou 1981", diags[0].conflito)

    def test_janela_do_aniversario_nao_acusa(self):
        # Nascida em 1987, 20 anos em 2008: possível se o aniversário não passou.
        # A conta do documento (1987 + 20 = 2007 ≠ 2008) acusaria ERROR falso.
        for ano in (2007, 2008):
            diags, _ = rodar(canon_de(ANA), fato("Ana", "tem_idade", 20, ano=ano))
            self.assertEqual(diags, [], ano)

    def test_data_completa_e_exata(self):
        canon = canon_de({"rigidez_padrao": "STRICT",
                          "personagens": [{"nome": "Ana", "nascimento": "1987-05-10"}]})
        t = {"ano": 2008, "mes": 1, "dia": 1, "relativo_a": None, "flashback": False, "calendario": None}
        self.assertEqual(rodar(canon, fato("Ana", "tem_idade", 20, tempo=t))[0], [])
        self.assertEqual(len(rodar(canon, fato("Ana", "tem_idade", 21, tempo=t))[0]), 1)

    def test_fala_de_personagem_vira_warning(self):
        diags, _ = rodar(canon_de(ANA), fato("Ana", "tem_idade", 20, ano=2001, modo="fala"))
        self.assertEqual(diags[0].nivel, "WARNING")
        self.assertTrue(any("modo fala" in n for n in diags[0].notas))

    def test_canon_proposto_pelo_claude_nao_da_error(self):
        canon = canon_de({"rigidez_padrao": "STRICT", "personagens": [
            {"nome": "Ana", "nascimento": 1987, "proposto_por": "claude"}]})
        diags, _ = rodar(canon, fato("Ana", "tem_idade", 20, ano=2001))
        self.assertEqual(diags[0].nivel, "WARNING")

    def test_confianca_baixa_vira_warning_e_limita_o_diagnostico(self):
        diags, _ = rodar(canon_de(ANA), fato("Ana", "tem_idade", 20, ano=2001, confianca="baixa"))
        self.assertEqual(diags[0].nivel, "WARNING")
        self.assertEqual(diags[0].confianca, "baixa")

    def test_idades_que_nao_fecham_entre_si_sem_canon(self):
        diags, _ = rodar(canon_de(), fato("Bia", "tem_idade", 20, ano=2001),
                         fato("Bia", "tem_idade", 29, ano=2005))
        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].nivel, "WARNING")
        self.assertIn("não se cruzam", diags[0].conflito)

    def test_idades_coerentes_entre_si(self):
        diags, _ = rodar(canon_de(), fato("Bia", "tem_idade", 29, ano=1977),
                         fato("Bia", "tem_idade", 48, ano=1996),
                         fato("Bia", "tem_idade", 81, ano=2029))
        self.assertEqual(diags, [])


class Vida(unittest.TestCase):
    def test_age_antes_de_nascer(self):
        diags, _ = rodar(canon_de(ANA), fato("Ana", "viaja_para", "Berlim", ano=1980))
        self.assertEqual(len(diags), 1)
        self.assertIn("antes de nascer", diags[0].titulo)

    def test_morte_que_e_so_crenca_nao_conta(self):
        # "o governo tem certeza de que o matou em 2016" é pensamento, não fato.
        diags, _ = rodar(canon_de(),
                         fato("Reiter", "morre_em", ano=2016, modo="pensamento"),
                         fato("Reiter", "viaja_para", "superfície", ano=2037))
        self.assertEqual(diags, [])

    def test_age_depois_de_morrer_como_fato_narrador(self):
        diags, _ = rodar(canon_de(),
                         fato("Reiter", "morre_em", ano=2016),
                         fato("Reiter", "viaja_para", "superfície", ano=2037))
        self.assertEqual(len(diags), 1)
        self.assertIn("depois de morrer", diags[0].titulo)


class Rede(unittest.TestCase):
    def _rel(self, ref, n, unidade="dias", sentido="depois"):
        return {"ano": None, "mes": None, "dia": None, "flashback": False, "calendario": None,
                "relativo_a": {"ref": ref, "fato": None, "resolvido": True,
                               "desvio": {"min": n, "max": n, "unidade": unidade, "sentido": sentido}}}

    def test_tempo_relativo_contradiz_data_absoluta(self):
        a = fato("cerco", "ocorre", ano=2001, ref="cerco")
        t = self._rel("cerco", 3)
        b = fato("rendição", "ocorre", tempo=t)
        b["tempo"]["ano"] = 1999          # "três dias depois do cerco", mas em 1999
        b["tempo"]["relativo_a"]["fato"] = a["id"]
        diags, _ = rodar(canon_de(), a, b)
        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].titulo, "Restrições de tempo em conflito")
        self.assertEqual(len([e for e in diags[0].evidencias if e.fonte == "obra"]), 2)

    def test_cadeia_relativa_consistente(self):
        a = fato("cerco", "ocorre", ano=2001, ref="cerco")
        b = fato("rendição", "ocorre", tempo=self._rel("cerco", 3))
        b["tempo"]["relativo_a"]["fato"] = a["id"]
        self.assertEqual(rodar(canon_de(), a, b)[0], [])

    def test_ancora_nao_resolvida_e_indeterminada_nunca_erro(self):
        t = self._rel("algo que não existe", 3)
        t["relativo_a"]["resolvido"] = False
        diags, indet = rodar(canon_de(), fato("x", "ocorre", tempo=t))
        self.assertEqual(diags, [])
        self.assertEqual(len(indet), 1)

    def test_canon_que_contradiz_a_si_mesmo(self):
        tl = {"rigidez_padrao": "STRICT", "eventos": [
            {"id": "EV-A", "data": 2000},
            {"id": "EV-B", "data": 1990, "depois_de": {"evento": "EV-A",
                                                        "desvio": {"valor": 5, "unidade": "anos"}}}]}
        diags, _ = rodar(canon_de(timeline=tl))
        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].nivel, "WARNING")
        self.assertTrue(any("canon se contradiz" in n for n in diags[0].notas))

    def test_calendario_nao_padrao_fica_indeterminado(self):
        t = {"ano": 340, "mes": None, "dia": None, "relativo_a": None, "flashback": False,
             "calendario": "breakout"}
        diags, indet = rodar(canon_de(ANA), fato("Ana", "tem_idade", 5, tempo=t))
        self.assertEqual(diags, [])
        self.assertEqual(len(indet), 1)


class Dias(unittest.TestCase):
    def test_contagem_de_dias(self):
        self.assertEqual(timeline.dias(1970, 1, 1), 0)
        self.assertEqual(timeline.dias(2000, 3, 1), 11017)
        self.assertEqual(timeline.dias(-1, 12, 31) + 1, timeline.dias(0, 1, 1))


if __name__ == "__main__":
    unittest.main()


class IdadeRelativa(unittest.TestCase):
    def test_idade_relativa_contra_idade_absoluta_sem_nascimento(self):
        a = fato("Sucessor", "tem_idade", 12, ano=2034)
        saida = fato("Sucessor", "viaja_para", "superficie", ano=2037, ref="saida")
        t = {"ano": None, "mes": None, "dia": None, "flashback": False, "calendario": None,
             "relativo_a": {"ref": "saida", "fato": saida["id"], "resolvido": True,
                            "desvio": {"min": 4, "max": 4, "unidade": "anos", "sentido": "depois"}}}
        b = fato("Sucessor", "tem_idade", 12, tempo=t)
        diags, _ = timeline.verificar(docs(a, saida, b), canon_de())
        self.assertEqual(len(diags), 1, [d.conflito for d in diags])
        self.assertEqual(diags[0].nivel, "WARNING")

    def test_idade_relativa_coerente(self):
        a = fato("Sucessor", "tem_idade", 12, ano=2034)
        saida = fato("Sucessor", "viaja_para", "superficie", ano=2037, ref="saida")
        t = {"ano": None, "mes": None, "dia": None, "flashback": False, "calendario": None,
             "relativo_a": {"ref": "saida", "fato": saida["id"], "resolvido": True,
                            "desvio": {"min": 4, "max": 4, "unidade": "anos", "sentido": "depois"}}}
        b = fato("Sucessor", "tem_idade", 19, tempo=t)
        self.assertEqual(timeline.verificar(docs(a, saida, b), canon_de())[0], [])
