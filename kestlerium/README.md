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
python3 run.py agora       # quem está onde, agora
```

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
schema.sql      as tabelas
data/           locais e elenco (é aqui que se mexe no conteúdo)
engine/
  clock.py      relógio de Brasília, épocas, os dois modos
  world.py      carga do mundo, grafo de deslocamento
  sim.py        laço de tempo, necessidades, encontros
  report.py     os portões de validação de cada fase
```

Conteúdo vive em `data/*.json`. Mexer no elenco ou no mapa não exige tocar em
código.

## Fases

- [x] **Fase 1** — corpos, mapa, rotinas, encontros. Sem drama, sem LLM.
- [x] **Fase 2** — verdade vs. crença, grafo social, fofoca distorcida
- [x] **Fase 3** — detector de pressão. **Portão de verdade: aprovado.**
- [x] **Verossimilhança** — conhecimento de origem, ensino, rotina bloqueada por ignorância
- [ ] **A vila** — configuração de produção: 1 personagem, NPCs, 8 locais
- [ ] **Fase 4** — governador de ritmo
- [ ] **Fase 5+** — narração, cenas, deriva de identidade, crônica

A Fase 3 é o portão de verdade: ela responde se o modelo de mundo gera
estrutura narrativa sozinho. Tudo depois disso é execução.
