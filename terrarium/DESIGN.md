# DESIGN — O Terrário

Documento de Fase 0. Fixa o que não pode mudar sem refazer schema.
Vive fora da raiz: subpasta = privado por padrão, nunca publicado no arquivo.

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

1 tick = **30 min** · 48 ticks/dia · **90 dias** = 4320 ticks no v0.

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
