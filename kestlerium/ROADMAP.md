# Kestlerium — o que falta

Estado: Fases 1-8 aprovadas na bancada (5 e 6 como infraestrutura), camada de
conhecimento funcionando, a vila publicando sozinha a cada 30 minutos. O motor
gera estrutura narrativa, decide o que contar e escreve os fios em Markdown —
sem LLM nenhum. Falta a prosa, que é a única coisa para a qual um modelo é
realmente necessário.

---

## A pergunta que reorganiza tudo: como um terrário fica ligado sem servidor

Um terrário está sempre ligado. Se cada visitante precisa iniciá-lo, deixa de
ser terrário e vira demonstração.

**A contradição se dissolve com uma distinção:** o mundo não precisa estar
*computando* o tempo todo — precisa estar *correto* quando alguém olha.

Três propriedades já construídas tornam isso possível:

1. **O relógio é o de Brasília**, não um contador interno.
2. **O avanço é por tempo decorrido**, não por "uma execução = um tick".
3. **A simulação é determinística**: o estado é função do tick e da seed.

Portanto o mundo não *acontece* enquanto alguém assiste. Ele já aconteceu, e
publicar é só registrar. Um agendador avança e publica a cada 30 minutos — que
é exatamente a duração de um tick, então **o snapshot publicado é sempre o tick
corrente.** O visitante abre a página e vê o agora. Não inicia nada, não espera
nada, e o mundo continua depois que ele fecha a aba.

Custo: zero servidor, zero hospedagem nova. O mesmo GitHub Actions que já
publica o arquivo passa a avançar o mundo.

---

## Como se olha para dentro

Não é um jogo. É um terrário, e o que prende não é o gráfico: é ver que Clara
acredita numa versão errada do que viu, que Oswine está perdido há três
semanas, que uma fofoca chegou torta no fim da rua.

- **3D:** custa assets, engine e desempenho, e não mostra nada que os dados
  tenham. Descartado.
- **2D com arte:** ainda é mais do que o necessário.
- **Planta baixa em SVG + painéis de estado:** locais como formas, pessoas como
  pontos, e ao lado o que não se vê olhando — crenças, conhecimento, tensão.
  São ~15 pontos numa tela. Roda em celular, sem assets, sem engine.

A visualização deve mostrar **o invisível**, porque o visível é trivial.

---

## Etapas

### A. A vila — só NPCs, sem os personagens do autor  ✅

Primeiro o mundo funcionando sozinho. Sem deslocado, sem anomalia, sem segredo
sobrenatural: um lugar pequeno com gente comum, rotinas, dívidas, promessas e
fofoca.

Isto também é um teste honesto: **o mundo gera drama sem os personagens
especiais?** Se não gerar, o problema é o mundo — e colocar Severin nele só
esconderia isso.

- ~8 locais, escala de vila
- ~10 NPCs com função declarada (quem trabalha onde, quem sabe o quê)
- fatos plantados: dívida, promessa, mentira — nada de anomalia
- os portões das Fases 1-3 revalidados nesta configuração

### B. Publicação contínua  ✅

- agendador avança o mundo e publica a cada 30 min
- estado persistido entre execuções (o banco precisa sobreviver ao runner)
- snapshot em JSON, pequeno, versionado

### C. Visualização  ✅

- planta baixa da vila em SVG, gerada do snapshot
- painéis: quem está onde, quem sabe o quê, quem acredita em quê
- página estática servida pelo mesmo site do arquivo

### D. Fase 4 — Governador de ritmo  ✅

Orçamento de cenas por semana, tempo de descanso por personagem para impedir
protagonista acidental, fila com bônus de espera. Sem isto, a narração das
fases seguintes gasta sem critério.

### E. Fase 5 — Beats narrados (o primeiro LLM)  ◐ infra pronta, modelo pendente

**Restrição fixada: nada pago.** Só modelo aberto ou camada gratuita. Isso não é
detalhe de custo — muda a arquitetura, e é melhor decidir agora do que descobrir
na hora.

Consequências concretas:

- **A narração não pode rodar no agendador.** O runner do GitHub Actions não tem
  GPU e tem teto de tempo; modelo local de 7B em CPU não fecha uma janela de 30
  minutos com folga. Então o laço se divide: **o mundo avança na nuvem** (é
  barato, é só aritmética), **a narração roda em outro lugar** — máquina local
  com Ollama/llama.cpp, ou camada gratuita de API — e o texto volta como commit.
- **O contrato JSON estrito fica mais importante, não menos.** Modelo pequeno
  erra formato com mais frequência que modelo grande. A validação de delta
  contra limites, a rejeição com uma re-tentativa e o delta neutro no fracasso
  deixam de ser precaução e viram caminho normal.
- **O cache indexado por hash vira obrigatório desde o primeiro dia.** Com
  geração cara em tempo (minutos por beat em CPU), reprocessar é inviável — e
  sem cache o replay determinístico morre junto.
- **Beats primeiro, cenas muito depois.** Um beat é uma chamada curta com saída
  estruturada, que é justamente o que modelo pequeno faz melhor. Diálogo
  encenado com vários turnos é o caso mais caro e mais frágil; só depois que os
  beats estiverem estáveis.

Candidatos a avaliar quando chegar a hora, sem compromisso: modelos abertos na
faixa 7-14B rodando local, e camadas gratuitas de inferência. A escolha deve ser
feita medindo **taxa de saída válida no contrato**, não qualidade de prosa — se
o JSON não fecha, a prosa não importa.

**Construído e validado (`engine/narrate.py`), sem modelo nenhum:** contrato
JSON estrito, limites por tipo de delta, re-tentativa única, delta neutro no
fracasso com o motivo registrado, cache indexado por hash e adaptador para
qualquer endpoint compatível com OpenAI — Ollama, llama.cpp, vLLM ou camada
gratuita, sem mudar uma linha. Um stub determinístico que imita o *contrato*
(não a prosa) exercita todos esses caminhos, e é contra ele que o portão roda.

**Falta só escolher e ligar o modelo.** O que o portão já mede: saída válida
aceita, malformada recuperada por uma re-tentativa, duas falhas viram delta
neutro, delta fora do limite recusado sem aparar, delta sobre quem não estava
presente recusado, campo inventado recusado, cache que evita a segunda chamada
e devolve exatamente o mesmo, e o pacote que não vaza verdade.

### F. Fase 6 — Cenas encenadas  ◐ infra pronta, modelo pendente

Vários atores em turnos, limite duro de turnos, **cada ator recebe só o pacote
de crenças dele** — e um teste explícito de vazamento, que é o bug mais provável
desta fase.

Construído em `engine/staging.py`. A defesa é estrutural, não uma checagem no
fim: um turno = um ator = o pacote dele, e o prompt de cada turno é montado do
zero com uma cabeça só. O que os outros disseram em voz alta atravessa; o que os
outros pensam, nunca. O portão inspeciona os prompts enviados — não só as
respostas — e é verificado nos dois sentidos.

### G. Fase 7 — Deriva de identidade  ✅

Constituição imutável, trajetória mutável, e toda mudança citando o `fact_id`
que a causou.

Feito sem LLM: a trajetória é reconstruída de `acquired_tick` e `learned_tick`,
que são históricos e imutáveis, então ela não pode divergir do que aconteceu. A
previsão falsificável da fase se confirmou — deslocado aprende mais que nativo,
18,5 conceitos contra 12,0.

### H. Fase 8 — Chronicler  ✅

Fios como objetos de primeira classe. Gera o texto legível — o único artefato
que um humano de fato consome — em Markdown, publicado pelo mesmo deploy.

Feito sem LLM nenhum, e essa foi a ordem certa: o modelo escreve melhor, mas
não sabe o que é uma história continuada. Quando a Fase 5 trouxer um modelo
aberto, ele substitui a camada de frase e encontra os fios já prontos.

O fio é tabela, não consulta: `agent_state` e `pressure_event` são podados a
cada publicação para o banco caber no repositório, e o que o mundo já contou
não pode depender de dados que serão apagados amanhã.

### I. Depois  ◐ chegada validada, desligada de propósito

Entrada dos personagens do autor, um por vez, via front matter na própria obra.
Entidades (Suomynona, The Continuity), que precisam de desenho próprio porque
não chegam: se manifestam. Escala.

**A versão estável do Kestlerium é a vila com NPCs e mais nada.** O mecanismo de
chegada está construído (`engine/arrival.py`) e validado (`run.py chegada`), mas
nenhum personagem foi colocado no mundo publicado, e nenhuma obra ganhou bloco
`kestlerium` no front matter. Isso é decisão, não pendência: primeiro o lugar
funciona sozinho.

Três regras já viraram código, e não comentário:

- **Só o front matter é lido; o corpo da obra, nunca.** Um personagem sabe
  apenas o que viveu dentro da história dele. Se o motor lesse o texto para
  enriquecê-lo, ele saberia o próprio final — e a fronteira que sustenta o
  projeto viraria conveniência. O autor declara o que o personagem sabe.
- **O arquivo da obra nunca é alterado.** Este módulo só lê.
- **Entidades são recusadas com explicação**, em vez de virarem moradores com
  pernas.

Quando o autor decidir mandar o primeiro, basta um bloco na obra:

    kestlerium:
      - id: severin
        nome: "Severin Sângelună"
        constituicao: "Nascido duas vezes. Não pergunta o que é permitido."
        casa: pensao
        trabalho: bar
        traz: [sangue, noite, juramento]

---

## Ordem e risco

A → B → C deu o terrário **vivo e observável** sem gastar um centavo de LLM.
Era o marco que valia perseguir primeiro: se o mundo não fosse interessante de
observar sem narração, nenhuma narração o salvaria.

De D a I saiu mais barato do que o previsto aqui. A previsão era que "D em
diante é onde o custo começa"; na prática o governador de ritmo, a deriva de
identidade, o cronista e a chegada saíram **inteiros sem modelo nenhum**, e das
Fases 5 e 6 só falta plugar o modelo — o contrato, o cache, os limites de delta
e os testes de vazamento já estão de pé e validados contra um stub
determinístico.

**O custo real só começa agora**, e num ponto só: escolher um modelo aberto e
medir a taxa de saída válida no contrato. Nenhuma outra peça depende disso.
