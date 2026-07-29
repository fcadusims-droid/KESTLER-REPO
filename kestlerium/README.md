# Kestlerium

Um mundo contemporâneo onde os personagens das obras do arquivo chegam
deslocados e passam a viver sob a lógica da realidade daqui — enquanto as
capacidades que trouxeram de casa continuam funcionando.

O tempo do Kestlerium é o tempo real do Brasil. Se aqui são 21h de uma terça,
lá são 21h da mesma terça e está de noite.

## Rodar

Sem dependências. Só Python 3.11+ e a biblioteca padrão.

```bash
python3 run.py validar     # 90 dias em segundos, banco descartável
python3 run.py avancar     # leva o mundo até o instante atual de Brasília
python3 run.py publicar    # avança e escreve a janela do terrário
python3 run.py agora       # quem está onde, agora
python3 run.py cronica     # escreve os fios de história em Markdown
python3 run.py chegada     # prova que um personagem funcionaria (não mexe no mundo)
```

Todos aceitam `--mundo`: `vila` é a produção, `distrito` é a bancada de teste.
O padrão é `distrito`, então o mundo publicado só é tocado com `--mundo vila`.

## Os dois modos

| Modo | Para quê | De onde vem o tempo |
|---|---|---|
| **real** | O Kestlerium de verdade | Horário de Brasília, 1 tick = 30 min reais |
| **rápido** | Só validação | Intervalo fixo, 90 dias em segundos, banco separado |

O modo rápido não é atalho: é a bancada de teste. Esperar 90 dias reais para
descobrir que a ontologia está errada não é uma opção. Ele queima os erros de
design antes do mundo começar a viver.

O modo real calcula **quantos ticks se passaram desde a última execução** em vez
de assumir que rodou na hora certa. Agendador atrasa; com recuperação por tempo
decorrido o mundo alcança o relógio em vez de ficar para trás.

## Onde as coisas estão

```
DESIGN.md       decisões travantes — o que não muda sem refazer schema
VALIDATION.md   tudo que deu errado, por quê, e o que foi mudado
ROADMAP.md      o que já está de pé e o que falta
schema.sql      as tabelas
data/           locais e elenco (é aqui que se mexe no conteúdo)
engine/
  clock.py      relógio de Brasília, épocas, os dois modos
  world.py      carga do mundo, grafo de deslocamento
  sim.py        laço de tempo, necessidades, encontros
  ledger.py     fatos, crenças, fofoca, relações
  knowing.py    conhecimento sobre o mundo, e o ensino dele
  goals.py      objetivos e a tabela de conflito
  pressure.py   o detector: o que poderia ser contado
  pacing.py     o governador: o que será contado, e o que espera
  chronicle.py  os fios de história, em Markdown
  identity.py   constituição imutável, trajetória com causa citada
  narrate.py    contrato, cache e adaptador de modelo (sem modelo ainda)
  staging.py    cenas turno a turno, um pacote por ator
  arrival.py    a obra vira gente — construído, e desligado de propósito
  viewer.py     a janela: planta baixa em SVG e painéis
  report.py     os portões de validação de cada fase
```

Conteúdo vive em `data/*.json`. Mexer no elenco ou no mapa não exige tocar em
código.

## Fases

- [x] **Fase 1** — corpos, mapa, rotinas, encontros. Sem drama, sem LLM.
- [x] **Fase 2** — verdade vs. crença, grafo social, fofoca distorcida
- [x] **Fase 3** — detector de pressão. **Portão de verdade: aprovado.**
- [x] **Verossimilhança** — conhecimento de origem, ensino, rotina bloqueada por ignorância
- [x] **A vila** — base do mundo: 10 moradores, 11 locais, sem personagens ainda
- [x] **Fase 4** — governador de ritmo: orçamento, descanso, fila com espera
- [x] **Fase 5** — contrato, cache e adaptador. *Falta plugar o modelo.*
- [x] **Fase 6** — cenas turno a turno, um pacote por ator. *Idem.*
- [x] **Fase 7** — deriva de identidade: constituição fixa, trajetória com causa
- [x] **Fase 8** — o cronista: fios de história em Markdown
- [x] **Chegada** — validada em banco descartável, **fora do mundo publicado**

A Fase 3 é o portão de verdade: ela responde se o modelo de mundo gera estrutura
narrativa sozinho. Tudo depois disso é execução — e saiu inteiro sem LLM nenhum.

**Nada aqui chama modelo pago.** As Fases 5 e 6 falam com qualquer endpoint
compatível com OpenAI (Ollama, llama.cpp, vLLM, camada gratuita) e são validadas
contra um stub determinístico que imita o *contrato*, não a prosa.

A versão estável do Kestlerium é **a vila com NPCs e mais nada**. O mecanismo de
chegada existe e está provado, mas nenhum personagem do autor foi colocado no
mundo publicado, e nenhuma obra ganhou bloco `kestlerium` no front matter. Isso é
decisão, não pendência.
