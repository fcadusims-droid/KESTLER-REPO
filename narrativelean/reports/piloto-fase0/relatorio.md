# Relatório NarrativeLean — v1

Gerado em 2026-09-28T20:32:15Z.

## 1. Classificação dos documentos (confira primeiro)

| Documento | Tipo | Fonte | Confiança | Unidades | Não extraídas | Fatos |
|---|---|---|---|---|---|---|
| lattice_zero.md | biblia | declarado | alta | 23 | 0 | 48 |

## 2. Qualidade da extração

### lattice_zero.md
- Fatos por modo: {'narrador': 44, 'documento_interno': 2, 'pensamento': 1, 'fala': 1}
- Citações rejeitadas (não encontradas no texto ou inválidas): 0
- Divergências entre extração aberta e dirigida: 0
- Reextração da amostra (concordância com o cache):
  - lattice-zero#iv-the-synthetic-threshold: jaccard 1.0 (2 de 2)
  - lattice-zero#vii-the-bloom: jaccard 1.0 (2 de 2)
  - lattice-zero#ix-the-modeling-engine: jaccard 1.0 (1 de 1)
  - lattice-zero#xi-the-man-they-buried: jaccard 1.0 (4 de 4)
  - lattice-zero#xiii-the-compromise-he-could-not-make: jaccard 1.0 (1 de 1)
  - lattice-zero#xv-the-instruction: jaccard 1.0 (0 de 0)
  - lattice-zero#xvii-the-disclosure: jaccard 1.0 (5 de 5)

## 3. Diagnósticos

ERROR: 0 · WARNING: 1 · SUGGESTION: 1

Não existe meta de zerar esta lista (seção 8). Um diagnóstico é um indício para o autor avaliar, não uma ordem de correção.

```text
WARNING TL-001  —  Restrições de tempo em conflito
Verificador: timeline (formal)
Regra: consistência interna (rede de tempo)
Evidência:
  lattice_zero.md, l.281 — "He came out of the ground in 2037 carrying two hundred and eleven doses of Lattice Zero"
  lattice_zero.md, l.241 — "In 2034 the organism went in first."
  lattice_zero.md, l.245 — "twelve years old in every way that experience counts"
  lattice_zero.md, l.303 — "in the hands of a twelve-year-old man wearing a dead scientist's face"
  lattice_zero.md, l.301 — "Seventy-four doses have been placed in four years."
Conflito:
  Estas restrições não podem valer ao mesmo tempo:
  - o sucessor viaja_para superfície em 2037
  - o organismo entra primeiro no sucessor ocorre em 2034
  - o sucessor tem_idade 12: 0–0 dias depois de o organismo entra primeiro no sucessor ocorre
  - o sucessor tem 12 anos em: o sucessor tem_idade 12
  - o sucessor tem_idade 12: 0–0 dias depois de setenta e quatro doses aplicadas ocorre
  - setenta e quatro doses aplicadas ocorre: 4–4 anos depois de o sucessor viaja_para superfície
  Juntas, elas exigem um intervalo impossível (faltam 1815 dia(s)).
Confiança da extração: media
Ação: REVISAO após pergunta ao autor: qual dos trechos está certo?
Nota: contradição interna da obra, sem canon envolvido
Verifique: a citação sustenta o fato extraído?
Impressão: bfddcb57a354ce40
```

```text
SUGGESTION REF-001  —  'United States' é citado e nunca definido
Verificador: referencia_sem_definicao (semantica)
Método: proprio
Regra: lente: informação não estabelecida, adaptada a bíblia (método próprio, seção 6.4)
Evidência:
  lattice_zero.md, l.13 — "four hundred Americans, none of whom worked, on paper, for the United States."
  lattice_zero.md, l.251 — "is the largest problem he has, because Anselm Reiter is a man the United States government is certain it killed in 2016, in an operation still"
  lattice_zero.md, l.257 — "On the ninth of March, 2036, the President of the United States told the world that we are not alone, that we have not been alone"
Conflito:
  'United States' aparece 4 vez(es) e não há verbete, título, termo em negrito, primeira coluna de tabela ou item do canon que o defina.
Confiança da extração: alta
Ação: NOVO_CONTEUDO após pergunta ao autor: definir o termo num verbete, ou declará-lo em canon/entidades.yaml → termos_conhecidos?
Nota: método próprio (sem fonte publicada): limitado a SUGGESTION
Verifique: a citação sustenta o fato extraído?
Impressão: 3cab58c359a17f0e
```
