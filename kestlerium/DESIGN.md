# KESTLERIUM — Documento de Design

Documento de Fase 0. Fixa o que não pode mudar sem refazer schema.
Vive fora da raiz: subpasta = privado por padrão, nunca publicado no arquivo.

**Kestlerium** é o mundo: o substrato contemporâneo onde os personagens de todas
as obras chegam deslocados e passam a coexistir sob uma única lógica de
realidade.

## 1. Domínio e escala

Um distrito de uma cidade contemporânea. **A lógica da realidade é a do mundo
real** — dinheiro, aluguel, documentos, transporte, polícia, câmeras, telefones,
hospitais. Personagens das obras chegam deslocados e precisam viver dentro dessa
lógica.

As capacidades de origem continuam funcionando. O mundo é que não tem
vocabulário para elas. Essa assimetria é o motor.

- **12 locais**, grafo com tempo de deslocamento (a pé / transporte).
- **16 personagens**: 12 deslocados + **4 nativos**.
- Os nativos não são cenário. São a linha de base de normalidade contra a qual a
  anomalia é medida. Sem eles, ocultar não tem custo e o drama colapsa.

## 2. Ontologia de objetivos (10 tipos)

Cada tipo tem condição de satisfação verificável em código.

| Tipo | Satisfeito quando |
|---|---|
| `estabelecer_identidade` | existe fato `(a, possui_documento, tipo)` com `visibility=publico` |
| `adquirir_recurso` | `agent.resources >= alvo` |
| `ocultar_anomalia` | **ativo enquanto** nenhum nativo tem crença fiel em `(a, usou_anomalia, *)` com `confidence > 0.6` |
| `compreender_mundo` | contagem de regras-do-mundo aprendidas `>= limiar` (decai a pressão do deslocamento) |
| `retornar_origem` | existe fato `(a, retornou, origem)` — quase nunca satisfazível: fonte permanente de tensão |
| `obter_informação` | `belief(a, fact_id).confidence > 0.8` |
| `formar_vínculo` | `relation(a,b).affect > 0.6` **e** `trust > 0.6`, mútuo |
| `proteger_pessoa` | violado se alvo é subject de `matou` ou `feriu` |
| `remover_obstáculo` | alvo perde posição / deixa o local |
| `expor_verdade` | fato transiciona `oculto → publico` |

`compreender_mundo` e `retornar_origem` só existem por causa da premissa de
deslocamento. São elas que impedem isso de virar "um sim de cidade moderna".

## 3. Ontologia de predicados (15)

```
matou · feriu · salvou · roubou_de · deve_a · prometeu_a
ama · teme · mentiu_sobre · testemunhou · trabalha_para · é_parente_de
usou_anomalia · é_de_origem · reconheceu_origem_de
```

Os três últimos são a camada de anomalia:

- **`usou_anomalia`** — gera fato com testemunhas. Nativo que testemunha forma
  crença **distorcida** por padrão (racionalização), não fiel. A versão fiel e a
  racionalizada competem pela mesma aresta com confianças diferentes.
- **`é_de_origem`** — de qual obra o personagem veio. `oculto` por padrão.
- **`reconheceu_origem_de`** — um deslocado identifica outro. É o único evento de
  crossover que não é arbitrário: nasce de mecânica, não de conveniência.

## 4. Horizonte temporal

1 tick = **30 min** · 48 ticks/dia.

**O tempo do Kestlerium é o tempo real do Brasil** (`America/Sao_Paulo`). Se
aqui são 21h de uma terça, lá são 21h da mesma terça e está de noite. A época é
a meia-noite local do dia em que o mundo nasceu, o que faz `tick % 48` casar com
a hora de Brasília sem conversão nenhuma — e fica gravada em `world_clock`, não
no código: recalculá-la deslocaria o histórico inteiro a cada execução.

Isso obriga dois relógios sobre o mesmo motor:

| Modo | Uso | Relógio |
|---|---|---|
| **real** | O mundo de verdade | Brasília, 1 tick = 30 min reais |
| **rápido** | Só validação das Fases 1-3 | 90 dias em segundos, banco separado |

O modo rápido não é atalho — é a bancada de teste. Esperar 90 dias reais para
descobrir que a ontologia de objetivos está errada não é uma opção.

O modo real avança por **tempo decorrido desde a última execução**, não por
"uma execução = um tick". Agendador atrasa; assim o mundo alcança o relógio em
vez de ficar para trás.

## 5. Adições ao plano original (decididas aqui, não na Fase 8)

1. **Ralo de tensão em L0.** O critério da Fase 3 exige tensão oscilando, mas
   nada reduz tensão antes do LLM. Resolução simbólica: tensão acima do limiar +
   par co-localizado → evento de confronto mecânico com deltas limitados.
2. **`leverage` sobre relações** = fatos cujo subject e object são as duas pontas
   da aresta. Derivado, sem tabela nova.
3. **Cache de LLM desde o primeiro dia da Fase 5**, indexado por
   `hash(prompt + contexto)`, ou o replay determinístico morre.
4. **Saída do Chronicler é Markdown** commitado no repositório. O deploy estático
   que já existe publica sozinho. Sem backend, sem hospedagem nova.

## 6. Critério de saída da Fase 0

Três fatos e três objetivos que cobrem o drama pretendido — atravessando obras
diferentes, para provar que a premissa de crossover gera estrutura.

**Fatos**

1. `(severin, usou_anomalia, fechou_ferida_com_sangue)` — `oculto`, testemunha: `clara` (nativa)
2. `(lacrimel, é_de_origem, aspectros)` — `oculto`, testemunha: `lotus`
3. `(suomynona, reconheceu_origem_de, severin)` — `oculto`, sem testemunha

**Objetivos**

1. `severin: ocultar_anomalia` — bloqueado se Clara consolidar a crença fiel
2. `clara: obter_informação` sobre o fato 1 — ela viu o impossível; a crença
   distorcida disputa com a fiel dentro da cabeça dela
3. `suomynona: expor_verdade` sobre o fato 2 — compulsão de publicar identidade

Os três se travam mutuamente e envolvem três obras distintas mais uma nativa.
Se este trio não produz drama na simulação, a ontologia está errada — não os pesos.

---

# ADENDO — Verossimilhança e a configuração de produção

Decidido depois da Fase 2, a ser implementado **após o portão da Fase 3**.

## 7. O personagem não conhece a própria obra

Um personagem sabe **apenas o que viveu dentro da história dele**. Não conhece o
enredo da obra, o que aconteceu fora da vista dele, o que outros esconderam, nem
a estrutura narrativa. Isso é conhecimento do autor, não da criatura.

Isto não exige mecanismo novo: é a separação `fact` / `belief` da Fase 2. O
conhecimento de origem de um personagem é um **conjunto de crenças**, limitado ao
que ele testemunhou — nunca a tabela de verdade do mundo dele.

## 8. Conhecimento como segunda rede

A fofoca move *fatos sobre pessoas*. O ensino move *conceitos sobre o mundo*.
Mesma maquinaria de distorção, redes distintas.

- **Conhecimento de origem** — o que o universo dele ensinou. Severin sabe
  linhagem, juramento, corte, sangue. Não sabe carro, telefone, cartão, triagem
  de hospital.
- **Conhecimento do Kestlerium** — começa em quase zero e cresce por convívio.
- **Troca nos dois sentidos.** O deslocado aprende o que é um ônibus; o local
  ouve falar de juramento de sangue e racionaliza como história de doido — a
  mesma regra que já faz Clara ver o impossível e concluir "truque de luz".

Um deslocado sem conhecimento suficiente **não consegue executar rotina**: não
sabe pegar o transporte, não entende a moeda, não sabe o que é um turno de
trabalho. `compreender_mundo` deixa de ser objetivo decorativo e passa a ser
pré-requisito de sobrevivência.

## 9. NPCs

Habitantes que não são obra do autor. Existem para que o deslocado tenha com
quem aprender o básico, e para serem a régua de normalidade (o papel que os
"nativos" já cumprem, agora explícito). Não têm arco próprio: têm função,
rotina e conhecimento local.

## 10. Configuração de produção: a vila

O Kestlerium de verdade **não começa como um distrito urbano de 16 pessoas.**

- Uma **vila**, tempo moderno, com o básico: casas, NPCs, posto de saúde,
  mercearia, ponto de ônibus.
- Começa com **um personagem deslocado**, que chega sem entender nada.
- Cresce por chegada contínua: cada obra nova manda alguém.

O distrito de 16 personagens continua existindo como **bancada de teste**. Ele é
necessário: os portões das Fases 1-3 medem distribuições, e uma vila com um
morador seria legitimamente quieta demais para distinguir detector quebrado de
mundo calmo. Bancada e produção são dois arquivos de dados, não dois motores.
