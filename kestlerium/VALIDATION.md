# Registro de validação

Cada problema encontrado, o que ele revelou e o que foi mudado por causa dele.
Existe para que um resultado ruim no futuro possa ser explicado em vez de
adivinhado — e para não repetir uma correção que já foi tentada.

Princípio: quando um portão reprova, **conserta-se o modelo de mundo, não o
número do portão.** Afrouxar o critério até passar produz um mundo que passa no
teste e não gera drama.

---

## Fase 1 — L0: corpos, mapa, rotinas, encontros

Portão: 90 dias em < 10s, ninguém isolado, saturação diária < 20%, nenhum par
dominante (< 12%), cobertura de pares > 50%.

### P1 — Saturação diária de 46,7% (alvo < 20%)

**Sintoma.** Quase metade dos pares possíveis se encontrava todo dia.
`apartamentos` sozinho respondia por 5415 dos 10572 encontros.

**Causa.** Nove personagens moram no Edifício Aurora, e o modelo tratava o
prédio como uma sala única. Os 36 pares de moradores ficavam em co-presença
contínua sempre que estavam em casa.

**Diagnóstico.** Morar no mesmo prédio não é estar na mesma sala. O modelo
confundia endereço com convivência.

**Correção.** Campo `shared` no local. Moradias (`shared = 0`) deixam de gerar
co-presença automática; vizinhos se cruzam em área comum, ocasionalmente.

**Resultado.** 46,7% → 27,8%. `apartamentos` caiu de 5415 para 902 encontros e
`cafe` assumiu a liderança — o que é o esperado para um distrito.

### P2 — Suomynona dominando os encontros

**Sintoma.** Ainda 27,8% de saturação. Os pares mais frequentes eram quase
todos com Suomynona; 1401 dos 4237 encontros vinham do canal de rede.

**Causa.** `NETWORK_USE_P = 0.06` por tick significava que a entidade
"encontrava" alguém toda vez que a pessoa usava um dispositivo — ou seja, quase
todo o elenco, todo dia.

**Diagnóstico.** Erro conceitual, não de calibragem. Encontro com Suomynona
deve significar *resolveu uma identidade*, não *alguém abriu o telefone*. Se a
detecção fosse frequente, a compulsão dela terminaria o trabalho na primeira
semana: elenco inteiro exposto, tensão central resolvida, nenhum drama
restante. **A raridade da detecção é o que dá tempo ao segredo existir.**

**Correção.** `NETWORK_USE_P` = 0.012, com a semântica documentada no código.

**Resultado.** 27,8% → 23,2%. Rede caiu de 1401 para 289 encontros.

### P3 — Saturação residual de 23,2%

**Sintoma.** Perto do alvo, mas ainda reprovado. `cafe` com 870 encontros e
capacidade 10; várias rotinas sociais empilhadas na mesma faixa horária.

**Causa.** A coluna `capacity` existia no schema desde o início e **nunca era
usada**. Todo local, de qualquer tamanho, gerava co-presença total.

**Diagnóstico.** O mesmo erro de P1, um nível acima. Oito pessoas num café não
formam 28 conversas simultâneas, e dois ocupantes de um parque de 25 lugares
podem nunca se ver.

**Correção.** Probabilidade de contato entre um par específico =
`CONTACT_K / capacidade`, com persistência (uma vez em contato, o par continua
até se desfazer, para o encontro não piscar e inflar a contagem). Isso
generaliza a regra de moradia de P1 em vez de manter dois casos especiais.

**Resultado.** 23,2% → **11,1%. Fase 1 aprovada**, todos os cinco portões.

### P4 — Teste de determinismo mal construído (erro meu, não do motor)

**Sintoma.** Duas execuções com a mesma seed produziam hashes diferentes.

**Causa.** Eu comparava o hash do **texto do relatório**, que inclui o tempo de
execução — naturalmente variável. O mundo era idêntico; a medição é que estava
errada. Um `--seed 999` aparentemente vazio era só o `argparse` rejeitando a
flag depois do subcomando, porque ela só existia no parser pai.

**Correção.** Determinismo passou a ser medido sobre a sequência de encontros
lida do banco. `--seed` registrada em cada subcomando.

**Resultado.** Mesma seed → mundo idêntico. Seed diferente → mundo diferente.

### P5 — Época no futuro travava o modo real

**Sintoma.** `avancar` respondia "nada a avançar" com o mundo parado no tick 0.

**Causa.** `EPOCH` era constante de código, fixada em 29/07 00:00 — mas em
Brasília ainda era 28/07 21:54. A época estava adiante do presente, o tick
atual saía negativo, e o mundo se recusava a andar.

**Diagnóstico.** O erro não é a data errada: é a época ser constante de código.
Recalculá-la a cada execução também seria errado — a numeração dos ticks
mudaria de um dia para o outro e o histórico inteiro se deslocaria, inclusive
as datas de chegada dos personagens.

**Correção.** A época é decidida quando o mundo nasce e gravada em
`world_clock.epoch_iso`. Execuções seguintes leem de lá.

**Resultado.** Mundo nasce à meia-noite local, recupera as horas até o presente
e para. Rodar de novo não duplica nada.

---

## Fase 2 — verdade vs. crença

Portão: o segredo plantado escapa do círculo original, chega a 15-70% do elenco
em 60 dias, degrada ao circular, e o sujeito nunca vaza o próprio segredo.

### P6 — Difusão de 88% do elenco (alvo 15-70%)

**Sintoma.** O segredo de Severin chegou a 14 de 16 personagens em 60 dias.
O comportamento qualitativo estava certo — a verdade só na cabeça dele, Clara
com a racionalização dela, e uma terceira versão circulando que ninguém
testemunhou — mas o alcance saturava.

**Causa.** Suomynona era o maior vetor de fofoca do distrito. Recebeu de Clara e
distribuiu para quatro pessoas diretamente.

**Diagnóstico.** Erro conceitual. Uma entidade de rede não comenta com a vizinha
o que descobriu — ela acumula e publica. Deixá-la repassar boato casual a
transformava no oposto do que ela é.

**Correção.** Entidades não transmitem por fofoca. Recebem (detectam) e retêm.

**Resultado.** 88% → 56% em 60 dias. **Fase 2 aprovada.** Uma única correção de
modelo; nenhum parâmetro de propagação foi tocado.

### P7 — Portão medindo a coisa errada (erro meu, de novo)

**Sintoma.** Com 60 dias o portão passava; com 90 dias reprovava por 75%.

**Causa.** O critério do plano é temporal — "difusão parcial e distorcida em
~30-60 dias" — mas eu media o estado no fim da execução, qualquer que fosse a
duração. Uma run mais longa reprovava só por ter continuado a rodar.

**Diagnóstico.** Mesmo erro de P4: o instrumento medindo outra coisa que não o
critério. Vale registrar que dois dos sete problemas desta fase foram medição
ruim, não mundo ruim — é a categoria de erro mais fácil de confundir com
fracasso de design, e a mais cara se levar a "consertar" um mundo que estava
certo.

**Correção.** O alcance passou a ser avaliado numa janela fixa de 60 dias, via
`belief.acquired_tick`. A curva completa entrou no relatório.

**Resultado.** Portão independente da duração da execução.

---

## Fase 3 — o portão de verdade

Portão: cauda pesada, 2-8% dos dias com pico, >60% do elenco em algum pico,
picos correlacionados mas sem cascata, tensão sem saturar.

Nove problemas. Três eram bugs meus, quatro eram modelo, dois eram o plano
precisando de correção. Nenhum foi resolvido afrouxando um portão.

### P8 — Detector medindo potencial estático (61% dos dias com pico)

`goal_conflict` perguntava "estes dois têm objetivos incompatíveis?". Severin
quer ocultar, Suomynona quer expor — logo todo encontro entre eles pontuava
alto, no dia 1 e no dia 90, tenha acontecido algo ou não. **Conflito que nunca
muda não é drama, é constante de fundo.** O plano escreve `CO = objetivos
bloqueados/avançados`: verbos de mudança. Passou a medir variação de progresso.
61% → 20%.

### P9 — Plantio antecipado matou a Fase 2 (regressão minha)

Para instanciar objetivos eu plantei todos os fatos antes do laço. Com os 18
existindo no tick 0, as saliências decaíam juntas e a fofoca morria por volta
do dia 40: o segredo travou em 2 crentes. Além de quebrar a Fase 2, estava
conceitualmente errado — **ninguém tem o objetivo de ocultar antes de existir
algo a ocultar.** Objetivos passaram a ser reconstruídos quando fatos novos
entram no mundo.

### P10 — Soma de componentes gera pressão sem evento

O plano soma os cinco termos. Dois deles existem mesmo quando nada aconteceu:
todo primeiro encontro de um par tem `RE = 1.0`, e a maioria dos primeiros
encontros é banal. Substância (crença e objetivo que de fato mudaram) passou a
multiplicar, não somar com, os amplificadores (raridade, carga, tensão).
Pressão média 0.28 → 0.029, curtose +3.6 → +28.

**Desvio consciente do plano**, marcado no código.

### P11 — Toda descoberta valendo o mesmo

Doze pessoas descobrindo o mesmo segredo produziam doze picos iguais. Mas **o
valor dramático de uma informação é inverso a quantos já a possuem**: o
primeiro a saber muda o mundo, o décimo confirma o que a rua comenta. A
alavancagem passou a ser dividida pelo número de portadores.

### P12 — Elenco parasita (38% em algum pico)

Só quatro personagens tinham segredo plantado; os outros doze não tinham nada
em jogo e nunca entravam num pico. Ontologia rala, não peso baixo. Sete fatos
viraram dezoito, distribuídos por quinze sujeitos.

### P13 — Canal errado no detector (bug)

Todo evento chegava ao detector marcado como `"presencial"`, inclusive as
detecções de rede. O detector tratava varredura de dados como conversa no café.

### P14 — Objetivos lendo a verdade em vez da crença (violação de arquitetura)

`instantiate()` construía objetivos a partir de `facts`. Suomynona ganhava
`expor_verdade` sobre quinze segredos, incluindo os que nunca detectou. Isso
viola a regra central do projeto: **um agente não pode ter objetivo sobre um
fato que ele não conhece.** Objetivos passaram a se apoiar em `belief`.

### P15 — O mundo não gerava fatos próprios

Os picos paravam no dia 21 e os 69 dias seguintes eram mortos. O Kestlerium só
distribuía os fatos plantados; quando terminavam de circular, não havia mais
nada a dizer. Confronto (quando a tensão descarrega) e vínculo (quando afeto e
confiança se firmam) passaram a gerar fatos, com testemunhas.

### P16 — Seis dos dez objetivos eram inertes

`progress()` devolvia 0.0 para `adquirir_recurso`, `elevar_status`,
`proteger_pessoa`, `estabelecer_identidade`, `compreender_mundo` e
`remover_obstaculo`. A ontologia rodava a 30% da capacidade, e por isso a
pressão era um penhasco: `W_conflito` 0.5 dava 3 picos, 0.45 dava zero. Quatro
ganharam mecanismo (recursos, reputação, dano ao protegido, burocracia do
cartório). `compreender_mundo` continua inerte até a fase de verossimilhança.

### P17 — Escalas incomparáveis fingindo de pesos

Medido: `dE ∈ [0, 0.18]`, `CO ∈ [0, 1.76]`. Somados com peso 1, CO dominava
sempre e varrer os pesos apenas trocava qual componente mandava — quatro dos
cinco não alteravam o resultado. **Calibragem não conserta unidade errada.**
Cada componente passou por `x/(x+k)`, com k derivado do p99 medido de cada um.
Só depois disso os pesos passaram a significar importância relativa.

### P18 — Carga relacional sempre zero (dois bugs em cima do outro)

O componente era p50 = p95 = p99 = max = 0. Primeiro: τ = 180 dias, sugerido
pelo plano, apaga o termo num mundo onde as pessoas se cruzam a cada dois dias
(1−exp(−2/180) ≈ 0.01). Corrigido para 21 dias. Segundo, e pior: o detector lia
`last_contact_tick` **depois** de `on_encounter` já tê-lo atualizado — o
intervalo era zero por ordem de chamada.

### P19 — O evento era o par, não a cena

Restava uma fronteira: menos picos custava sempre menos cobertura de elenco, e
nenhuma combinação de pesos satisfazia os dois critérios. **Um momento
dramático não acontece entre duas pessoas isoladas — acontece numa sala.** O
evento passou a creditar todos os presentes, e a plateia virou amplificador
(um segredo revelado diante de cinco pesa mais que diante de uma).

Isso separou os dois botões que estavam grudados: **substância controla quantos
picos, plateia controla quem participa.** Com eles independentes, o portão
abriu.

---

## Verossimilhança — conhecimento, ensino e a regra do autor

Não é uma fase do plano original: nasceu do pedido de que o Kestlerium fosse
verossímil — Severin não pode chegar e ir trabalhar no bar, porque ele não sabe
o que é um bar, nem um turno, nem dinheiro.

### A regra que organiza tudo

**Um personagem conhece apenas o que viveu dentro da história dele, nunca a
obra.** Severin sabe o que é linhagem e juramento porque atravessou os dois;
não sabe o enredo de *One Blood*, não sabe o que aconteceu longe da vista dele,
não sabe que é personagem de coisa alguma. Essa fronteira é do autor.

Isso não exigiu mecanismo novo — é a separação `fact`/`belief` da Fase 2
aplicada a conceitos. Conhecimento de origem é um conjunto limitado, não a
tabela de verdade do mundo de origem.

### A consequência que dá verdade ao mundo

Sem o conceito, a atividade não acontece. Quem não sabe o que é emprego não vai
trabalhar; quem não sabe o que é transporte fica preso onde chegou. Medido ao
fim de 90 dias:

```
Severin Sângelună   chegou d0    sabe  7/10   perdido  683 ticks
Alex                chegou d0    sabe  9/10   perdido 1567 ticks
Lácrimel            chegou d12   sabe  7/10   perdido 1113 ticks
Oswine              chegou d34   sabe  5/10   perdido  933 ticks
O Escriba           chegou d51   sabe  4/10   perdido  257 ticks
Sphaira             chegou d68   sabe  3/10   perdido  208 ticks
```

`perdido` são os ticks em que o personagem não soube o que fazer e ficou por
perto observando. `compreender_mundo` deixou de ser rótulo inerte e virou
pré-requisito de sobrevivência.

A troca é nos dois sentidos e a de volta é distorcida — Severin ensinou
`juramento` a Clara, que o arquiva como curiosidade, não como ferramenta.

### P20 — A camada de conhecimento desestabilizou o portão da Fase 3

**Sintoma.** Antes dela, 4 de 5 seeds passavam em todos os portões. Depois,
1 ou 2 — e a varredura de pesos encontrava um penhasco: `ep=0.56` dava 3% dos
dias com pico, `ep=0.70` dava 22%, sem meio-termo.

**Causa.** `compreender_mundo` entrava no cálculo de conflito de objetivo.
Como todos os deslocados aprendem ao mesmo tempo e depois saturam, o mundo
alternava entre "todos aprendendo" (pressão em todo lugar) e "todos já sabem"
(pressão nenhuma).

**Diagnóstico.** **Aprender o que é um ônibus não é um evento dramático.** O
plano escreve `CO = objetivos bloqueados/avançados`, e a palavra que importa é
*bloqueado*: pressão vem de objetivo que alguém pode atrapalhar. Ninguém se
opõe a Severin descobrir o que é dinheiro.

**Correção.** Só tipos que aparecem em `CONFLICTING` geram pressão de conflito.
Os demais continuam reais e continuam governando comportamento — apenas não são
drama.

**Resultado.** 1/5 → 4/5 seeds, e os valores entre seeds deixaram de ser
bimodais.

### P21 — Sem NPC, o aprendizado fica ao acaso

Com o ensino dependendo só de encontro fortuito, um deslocado que não cruzasse
com um morador cedo travava, e o mundo esfriava junto. Moradores locais passaram
a ensinar ativamente — é esse o papel deles diante de alguém que acabou de
chegar sem entender nada.

---

## Estado atual — três fases + verossimilhança

```
FASE 1 APROVADA     FASE 2 APROVADA          FASE 3 APROVADA
                                             curtose         +7.2
                                             dias com pico    6.7%  (2-8%)
                                             elenco em pico    73%  (>60%)
```

Pesos: `ep 0.62 · co 0.50 · cr 1.25 · re 0.82 · ta 0.40 · plateia 2.30`
**Robustez: 4 de 5 seeds passam em todos os portões.**

---

## Decisões de escopo e pendências

**Entidades adiadas.** Suomynona e The Continuity não são personagens do mesmo
jeito que Severin ou James Revex: não têm corpo, não dormem, não podem ser
presas, e não *chegam* — se manifestam onde há substrato. A introdução delas
merece desenho próprio, não um remendo no elenco de pessoas. `NETWORK_USE_P` e
o ramo de rede em `_detect_encounters` são código dormente por decisão, não por
esquecimento.

**A vila não existe ainda.** A configuração de produção — poucos locais, NPCs
com função declarada e **um** personagem chegando sem entender nada — é o passo
seguinte. O distrito de 15 fica como bancada, porque os portões medem
distribuições e uma vila com um morador seria quieta demais para distinguir
detector quebrado de mundo calmo.

**Outras, menores:**

- `out/` está fora do versionamento. Quando o Kestlerium for para produção via
  agendador, o banco do mundo real precisará persistir entre execuções — ou
  commitado, ou em cache do runner.
- Ninguém se encontra em trânsito. O metrô é o nó central do grafo e deveria ser
  onde estranhos se cruzam, mas quem viaja fica sem lugar.
- `remover_obstaculo` e `reconheceu_origem_de` estão na ontologia e ainda sem
  mecanismo. Declarados para não serem reinventados com outro nome depois.

---

## A vila — a base do mundo

Primeira configuração de produção: dez moradores, onze lugares, nenhum
personagem de obra. O objetivo é ver o mundo funcionar sozinho antes de povoar.

### P22 — A ordem de uma lista decidia os portões

**Sintoma.** Ao mover os locais para pastas por mundo, `FOOD_LOCATIONS` deixou
de ser a tupla `("mercado", "cafe")` cravada no motor e passou a vir dos dados,
ordenada. As Fases 2 e 3 do distrito reprovaram na hora.

**Causa.** `min()` desempata pela ordem de iteração, e vários locais ficam à
mesma distância. Trocar `("mercado","cafe")` por `("cafe","mercado")` mudava
metade dos destinos de "comer" — e o mundo inteiro andava junto. Medido: a
primeira ordem passa nas duas fases, a segunda reprova nas duas.

**Diagnóstico.** Resultado que depende de ordenação alfabética é acidente de
implementação, não propriedade do mundo. E revela margem estreita nos portões.

**Correção.** Entre os igualmente perto, sorteia. Além de remover o artefato, é
mais verdadeiro: ninguém almoça no mesmo lugar sempre.

### P23 — O portão da Fase 2 com nome de personagem cravado

`collect_phase2` procurava literalmente por `severin` + `usou_anomalia`. Na
vila não existe Severin, então o portão respondia "sem segredo plantado" e
passava em branco sem medir nada. Cada mundo passou a **declarar** nos dados
qual fato é o seu teste.

Terceira vez que um instrumento meu media a coisa errada. É a categoria de erro
que mais me custou neste projeto.

### P24 — Fofoca sem lealdade: a vila sabia de tudo

**Sintoma.** O segredo plantado chegava a 100% dos moradores em 60 dias, contra
56% no distrito.

**Causa.** A decisão de fofocar olhava só a confiança entre quem fala e quem
ouve. O **sujeito do fato não tinha peso nenhum** — a testemunha espalhava o
segredo de um amigo de trinta anos como se fosse notícia de jornal.

**Correção.** Afeto pelo sujeito segura a língua. Vila não sustenta segredo
porque as pessoas se cruzam — sustenta porque elas se protegem.

**Resultado.** Vila 100% → 70%; distrito manteve os portões.

### P25 — Lealdade sem piso travava o mundo

Com lealdade proporcional a qualquer afeto positivo, uma vila onde todos
convivem há décadas parava de fofocar inteiramente: zero picos, zero elenco
envolvido. Só amizade de verdade cala a boca; conhecido casual fala. Lealdade
ganhou piso.

### P26 — Dez moradores não são amostra

Varrendo a densidade da vila, o resultado **não é monotônico**: fator 1.4 dá 20%
de difusão, 1.5 dá 90%. Com dez pessoas e 45 pares possíveis, qualquer ajuste
pequeno joga a estatística para qualquer lado.

Os portões medem distribuições. A vila é pequena demais para eles serem
estáveis — e isso é propriedade da escala, não defeito do motor.

### P27 — Eu estava validando a coisa errada

**O achado que resolveu o impasse.** Eu vinha tentando fazer a vila passar nas
Fases 2 e 3, ajustando densidade e lealdade sem conseguir fechar as duas ao
mesmo tempo.

O erro era anterior: **eu tinha dado memória fake aos NPCs.** Biografias densas,
dívidas ocultas, mentiras, um roubo na oficina. Drama que não é deles.

Os moradores da base **sabem que estão no Kestlerium e que o Kestlerium é um
mundo digital.** Não escondem nada porque não têm o que esconder. Estão ali para
sustentar o lugar e ensinar quem chegar. As Fases 2 e 3 medem drama — difusão de
segredo e pressão narrativa — e a vila da base não tem drama **por projeto**.

Medir drama nela era reprovar um mundo por fazer exatamente o que devia.

**Correção.** Constituições curtas e funcionais; fatos plantados reduzidos ao
operacional (quem trabalha onde); e cada mundo declara quais portões se aplicam
a ele. A vila valida a Fase 1 — o lugar funciona — e espera os personagens para
o resto.

---

## Estado atual

```
DISTRITO (bancada)              VILA (produção, base)
Fase 1  APROVADA                Fase 1  APROVADA
Fase 2  APROVADA                Fases 2-3: não se aplicam
Fase 3  APROVADA                          (sem drama por projeto)
```

A vila roda no horário de Brasília. Às 9h de uma quarta: Ruth na mercearia,
Aurélio e Zé Bruno na oficina, Neide no posto, Djalma no ponto, três em trânsito.
