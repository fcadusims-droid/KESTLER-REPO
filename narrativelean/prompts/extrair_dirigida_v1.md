# Tarefa: perguntas dirigidas

Você é o extrator do NarrativeLean, numa tarefa estreita: responder às
perguntas abaixo sobre UM trecho, citando o texto. Perguntas estreitas existem
porque encontram casos que a extração aberta deixa passar. Leia o trecho
inteiro procurando cada ocorrência — inclusive as indiretas, as implícitas e as
que aparecem de passagem numa frase sobre outra coisa.

- Documento: `{{ARQUIVO}}`
- Unidade: `{{UNIDADE}}` — {{TITULO}}
- Tipo de documento: **{{TIPO_DOCUMENTO}}**

{{ORIENTACAO_TIPO}}

## Perguntas

{{PERGUNTAS}}

## Como responder

Para CADA pergunta ({{IDS}}), responda `sim` ou `nao` no `checklist`. "nao" é
uma resposta legítima e útil: significa que você procurou e não há.

Para cada ocorrência encontrada, registre uma instância no mesmo formato de
fato da extração aberta, com `responde_a` apontando a pergunta. As mesmas regras
valem: citação literal (pelo menos quatro palavras, conferida mecanicamente),
sem número de linha, `modo` correto (mentira é `fala`, crença é `pensamento`,
sonho/plano é `hipotetico`, carta/lenda/registro é `documento_interno`).

Predicados disponíveis:

{{VOCABULARIO}}

Eventos do canon (para `tempo.relativo_a.evento`):

{{EVENTOS_CANON}}

Responda SOMENTE com um bloco YAML:

```yaml
checklist:
  Q-TEMPO: sim
instancias:
  - responde_a: Q-TEMPO
    tipo: atributo
    sujeito: Lira
    predicado: tem_idade
    objeto: 19
    tempo: { ano: 2003 }
    modo: narrador
    citacao: "Lira foi aceita na Academia de Sal em 2003, aos dezenove anos"
    confianca_extracao: alta
```

## Texto da unidade

<<<TEXTO
{{TEXTO}}
TEXTO>>>
