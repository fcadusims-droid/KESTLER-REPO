# Relatório NarrativeLean — v1

Gerado em 2026-09-28T20:32:15Z.

## 1. Classificação dos documentos (confira primeiro)

| Documento | Tipo | Fonte | Confiança | Unidades | Não extraídas | Fatos |
|---|---|---|---|---|---|---|
| narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md | biblia | declarado | alta | 23 | 0 | 48 |

## 2. Qualidade da extração

### narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md
- Fatos por modo: {'narrador': 44, 'documento_interno': 2, 'pensamento': 1, 'fala': 1}
- Citações rejeitadas (não encontradas no texto ou inválidas): 0
- Divergências entre extração aberta e dirigida: 0
- Reextração da amostra (concordância com o cache):
  - obra-plantada#iv-the-synthetic-threshold: jaccard 1.0 (2 de 2)
  - obra-plantada#vii-the-bloom: jaccard 1.0 (2 de 2)
  - obra-plantada#ix-the-modeling-engine: jaccard 1.0 (1 de 1)
  - obra-plantada#xi-the-man-they-buried: jaccard 1.0 (4 de 4)
  - obra-plantada#xiii-the-compromise-he-could-not-make: jaccard 1.0 (1 de 1)
  - obra-plantada#xv-the-instruction: jaccard 1.0 (0 de 0)
  - obra-plantada#xvii-the-disclosure: jaccard 1.0 (5 de 5)

## 3. Diagnósticos

ERROR: 0 · WARNING: 5 · SUGGESTION: 1

Não existe meta de zerar esta lista (seção 8). Um diagnóstico é um indício para o autor avaliar, não uma ordem de correção.

```text
WARNING TL-001  —  Idade de Anselm Reiter incompatível com o nascimento
Verificador: timeline (formal)
Regra: Anselm Reiter.nascimento = 1948
Evidência:
  canon/characters.yaml — Anselm Reiter.nascimento = 1948
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.115 — "Anvil recruited him in 1977, at thirty-nine"
Conflito:
  nascimento em 1948 → em 1977 a idade seria 28 ou 29; o texto diz 39.
  Para ter 39 anos em 1977, o nascimento seria em 1937 ou 1938 (não em 1948).
Confiança da extração: alta
Ação: REVISAO após pergunta ao autor: mudar a idade (39 → 28 ou 29) ou o ano (1977 → 1987–1988)?
Nota: a regra do canon não tem autoridade plena (ver motivo no canon)
Nota: regra FLEXIBLE ou derivada: vira WARNING
Nota: Anselm Reiter.nascimento = 1948: proposto pelo Claude, aguardando aprovação do autor
Verifique: a citação sustenta o fato extraído?
Impressão: 23d1a8d45c254805
```

```text
WARNING TL-002  —  Idade de Anselm Reiter incompatível com o nascimento
Verificador: timeline (formal)
Regra: Anselm Reiter.nascimento = 1948
Evidência:
  canon/characters.yaml — Anselm Reiter.nascimento = 1948
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.147 — "The first viable clone line was completed in 2009. Reiter was seventy-one."
Conflito:
  nascimento em 1948 → em 2009 a idade seria 60 ou 61; o texto diz 71.
  Para ter 71 anos em 2009, o nascimento seria em 1937 ou 1938 (não em 1948).
Confiança da extração: alta
Ação: REVISAO após pergunta ao autor: mudar a idade (71 → 60 ou 61) ou o ano (2009 → 2019–2020)?
Nota: a regra do canon não tem autoridade plena (ver motivo no canon)
Nota: regra FLEXIBLE ou derivada: vira WARNING
Nota: Anselm Reiter.nascimento = 1948: proposto pelo Claude, aguardando aprovação do autor
Verifique: a citação sustenta o fato extraído?
Impressão: d46e1fafebe7facf
```

```text
WARNING TL-003  —  Idade de Anselm Reiter incompatível com o nascimento
Verificador: timeline (formal)
Regra: Anselm Reiter.nascimento = 1948
Evidência:
  canon/characters.yaml — Anselm Reiter.nascimento = 1948
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.215 — "He died in the spring of 2029, ninety-one years old"
Conflito:
  nascimento em 1948 → em 2029 a idade seria 80 ou 81; o texto diz 91.
  Para ter 91 anos em 2029, o nascimento seria em 1937 ou 1938 (não em 1948).
Confiança da extração: alta
Ação: REVISAO após pergunta ao autor: mudar a idade (91 → 80 ou 81) ou o ano (2029 → 2039–2040)?
Nota: a regra do canon não tem autoridade plena (ver motivo no canon)
Nota: regra FLEXIBLE ou derivada: vira WARNING
Nota: Anselm Reiter.nascimento = 1948: proposto pelo Claude, aguardando aprovação do autor
Verifique: a citação sustenta o fato extraído?
Impressão: e7f4fee4e2d360bb
```

```text
WARNING TL-004  —  Restrições de tempo em conflito
Verificador: timeline (formal)
Regra: consistência interna (rede de tempo)
Evidência:
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.251 — "When he finally came up, in 2037, he came up as him"
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.241 — "In 2031 the organism went in first."
Conflito:
  Estas restrições não podem valer ao mesmo tempo:
  - o sucessor viaja_para superfície em 2037
  - o organismo entra primeiro no sucessor ocorre em 2031
  - o sucessor viaja_para superfície: 3–3 anos depois de o organismo entra primeiro no sucessor ocorre
  Juntas, elas exigem um intervalo impossível (faltam 730 dia(s)).
Confiança da extração: alta
Ação: REVISAO após pergunta ao autor: qual dos trechos está certo?
Nota: contradição interna da obra, sem canon envolvido
Verifique: a citação sustenta o fato extraído?
Impressão: e4bca8703d21341e
```

```text
WARNING TL-005  —  Restrições de tempo em conflito
Verificador: timeline (formal)
Regra: consistência interna (rede de tempo)
Evidência:
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.281 — "He came out of the ground in 2037 carrying two hundred and eleven doses of Lattice Zero"
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.241 — "In 2031 the organism went in first."
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.245 — "twelve years old in every way that experience counts"
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.303 — "in the hands of a twelve-year-old man wearing a dead scientist's face"
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.301 — "Seventy-four doses have been placed in four years."
Conflito:
  Estas restrições não podem valer ao mesmo tempo:
  - o sucessor viaja_para superfície em 2037
  - o organismo entra primeiro no sucessor ocorre em 2031
  - o sucessor tem_idade 12: 0–0 dias depois de o organismo entra primeiro no sucessor ocorre
  - o sucessor tem 12 anos em: o sucessor tem_idade 12
  - o sucessor tem_idade 12: 0–0 dias depois de setenta e quatro doses aplicadas ocorre
  - setenta e quatro doses aplicadas ocorre: 4–4 anos depois de o sucessor viaja_para superfície
  Juntas, elas exigem um intervalo impossível (faltam 2911 dia(s)).
Confiança da extração: media
Ação: REVISAO após pergunta ao autor: qual dos trechos está certo?
Nota: contradição interna da obra, sem canon envolvido
Verifique: a citação sustenta o fato extraído?
Impressão: 2121e84a630b96b2
```

```text
SUGGESTION REF-001  —  'United States' é citado e nunca definido
Verificador: referencia_sem_definicao (semantica)
Método: proprio
Regra: lente: informação não estabelecida, adaptada a bíblia (método próprio, seção 6.4)
Evidência:
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.13 — "four hundred Americans, none of whom worked, on paper, for the United States."
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.251 — "is the largest problem he has, because Anselm Reiter is a man the United States government is certain it killed in 2016, in an operation still"
  narrativelean/tests/seeded_errors/lattice-zero/obra_plantada.md, l.257 — "On the ninth of March, 2036, the President of the United States told the world that we are not alone, that we have not been alone"
Conflito:
  'United States' aparece 4 vez(es) e não há verbete, título, termo em negrito, primeira coluna de tabela ou item do canon que o defina.
Confiança da extração: alta
Ação: NOVO_CONTEUDO após pergunta ao autor: definir o termo num verbete, ou declará-lo em canon/entidades.yaml → termos_conhecidos?
Nota: método próprio (sem fonte publicada): limitado a SUGGESTION
Verifique: a citação sustenta o fato extraído?
Impressão: 3cab58c359a17f0e
```
