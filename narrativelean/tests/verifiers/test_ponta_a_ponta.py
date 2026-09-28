"""O fluxo inteiro, pela CLI, numa cópia temporária do projeto.

preparar → operador (um processo por pacote) → ingerir → verificar

O operador aqui é um script falso e determinístico, mas o caminho é o mesmo que
`claude -p` ou um modelo local percorrem. Nada nos arquivos reais do projeto é
tocado.
"""

import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

OBRA = """# Ana

## I. A academia

Ana, com seus vinte anos, entrou na academia em 2001. O inverno daquele ano foi longo.

## II. A viagem

Carlos atravessou a fronteira sem olhar para trás, e ninguém o seguiu.
"""

OPERADOR = r'''
import re, sys
pacote = sys.stdin.read()
texto = pacote.split("<<<TEXTO", 1)[1].split("TEXTO>>>", 1)[0]
dirigida = "## Perguntas" in pacote
fatos = []
if "vinte anos" in texto:
    fatos.append("""  - tipo: atributo
    sujeito: Ana
    predicado: tem_idade
    objeto: 20
    tempo: { ano: 2001 }
    modo: narrador
    citacao: "Ana, com seus vinte anos, entrou na academia em 2001"
    confianca_extracao: alta""")
if "fronteira" in texto:
    # Citação inventada: não existe no texto. Tem de ser rejeitada.
    fatos.append("""  - tipo: evento
    sujeito: Carlos
    predicado: viaja_para
    objeto: Portugal
    modo: narrador
    citacao: "Carlos cruzou a fronteira de Portugal em 1990"
    confianca_extracao: alta""")
if dirigida:
    ids = re.findall(r"^### (Q-[\w-]+)", pacote, re.M)
    print("```yaml")
    print("checklist:")
    for i in ids:
        print(f"  {i}: {'sim' if fatos else 'nao'}")
    print("instancias:")
    print("\n".join(fatos) if fatos else "  []")
    print("```")
else:
    print("```yaml")
    print("fatos:")
    print("\n".join(fatos) if fatos else "  []")
    print("```")
'''


class PontaAPonta(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        destino = self.tmp / "narrativelean"
        shutil.copytree(RAIZ, destino, ignore=shutil.ignore_patterns(
            "cache", "facts", "reports", "work", "reviews", "__pycache__", "tests"))
        (self.tmp / "obra.md").write_text(OBRA, encoding="utf-8")
        (destino / "doctypes.yaml").write_text("documentos:\n  - arquivo: obra.md\n    tipo: prosa\n")
        canon = destino / "canon"
        (canon / "characters.yaml").write_text(textwrap.dedent("""
            rigidez_padrao: STRICT
            personagens:
              - nome: Ana
                nascimento: 1987
        """))
        (canon / "timeline.yaml").write_text("rigidez_padrao: STRICT\neventos: []\n")
        (canon / "world_rules.yaml").write_text("rigidez_padrao: STRICT\nregras: []\n")
        (self.tmp / "operador.py").write_text(OPERADOR, encoding="utf-8")
        self.script = destino / "nl.py"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def nl(self, *args) -> str:
        r = subprocess.run([sys.executable, str(self.script), *args], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r.stdout

    def pendentes(self) -> list:
        return sorted((self.tmp / "narrativelean" / "work" / "pendentes").glob("*.md"))

    def test_fluxo_completo(self):
        self.nl("validar")
        self.nl("extrair", "preparar")
        self.assertTrue(self.pendentes())

        saida = self.nl("extrair", "rodar", "--comando", f"{sys.executable} {self.tmp / 'operador.py'}")
        self.assertEqual(json.loads(saida)["restantes"], 0)

        ingestao = json.loads(self.nl("extrair", "ingerir", "--operador", "teste"))
        self.assertGreaterEqual(ingestao["rejeitados"], 1, "citação inventada precisa ser rejeitada")
        self.assertEqual(self.pendentes(), [])

        self.nl("verificar")
        rel = json.loads((self.tmp / "narrativelean" / "reports" / "v1" / "relatorio.json").read_text())
        erros = [d for d in rel["diagnosticos"] if d["nivel"] == "ERROR"]
        self.assertEqual(len(erros), 1, rel["diagnosticos"])
        self.assertEqual(erros[0]["verificador"], "timeline")
        ev = [e for e in erros[0]["evidencias"] if e["fonte"] == "obra"][0]
        self.assertEqual(ev["linha_inicio"], 5, "a linha vem do código, não do extrator")
        doc = rel["documentos"]["obra.md"]
        self.assertGreaterEqual(doc["rejeitados"], 1)
        self.assertEqual(doc["nao_extraidas"], [])

        # Cache: sem mudança no texto, nada a extrair de novo.
        self.nl("extrair", "preparar")
        self.assertEqual(self.pendentes(), [])

        # Muda só a seção II: só ela (e a vizinha) voltam para o operador.
        obra = self.tmp / "obra.md"
        obra.write_text(OBRA.replace("ninguém o seguiu", "ninguém o seguiu naquela noite"))
        self.nl("extrair", "preparar", "--sem-vizinhas")
        metas = [json.loads(p.read_text()) for p in
                 (self.tmp / "narrativelean" / "work" / "pendentes").glob("*.json")]
        self.assertTrue(metas)
        self.assertTrue(all(m["unidade"].endswith("ii-a-viagem") for m in metas), metas)

        # Resposta obsoleta: o texto muda de novo depois do pacote gerado.
        self.nl("extrair", "rodar", "--comando", f"{sys.executable} {self.tmp / 'operador.py'}")
        obra.write_text(OBRA.replace("ninguém o seguiu", "ninguém jamais o seguiu"))
        ingestao = json.loads(self.nl("extrair", "ingerir"))
        self.assertGreaterEqual(ingestao["obsoletos"], 1)

        # E a unidade que ficou sem extração aparece como NÃO verificada.
        self.nl("verificar")
        rel = json.loads((self.tmp / "narrativelean" / "reports" / "v1" / "relatorio.json").read_text())
        self.assertTrue(rel["documentos"]["obra.md"]["nao_extraidas"])


if __name__ == "__main__":
    unittest.main()
