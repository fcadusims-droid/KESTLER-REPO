# Kreator Runtime
## Especificação de Arquitetura Interna

> *Documento técnico interno. Não destinado a clientes ou material de marketing.*

---

**Autor:** Johnny Kestler (pseudônimo) — João Vitor Perazzolo
**Data de criação:** 27 de junho de 2026
**Versão:** 1.0
**Documento:** Arquitetura Interna / Runtime (RFC)
**Documento complementar:** Kreator — Produto (visão, K Agents, K Store, roadmap)

---

## Sumário

1. [Propósito e Princípios](#1-propósito-e-princípios)
2. [Visão de Camadas](#2-visão-de-camadas)
3. [Signal Layer](#3-signal-layer)
4. [Evidence Layer](#4-evidence-layer)
5. [Planner — Decisão Determinística](#5-planner--decisão-determinística)
6. [Execution Contracts](#6-execution-contracts)
7. [Execução Incremental](#7-execução-incremental)
8. [Scheduler e Resource Budget](#8-scheduler-e-resource-budget)
9. [Versionamento e Provenance](#9-versionamento-e-provenance)
10. [Marketplace Runtime](#10-marketplace-runtime)
11. [Mapeamento K Agents → Módulos](#11-mapeamento-k-agents--módulos)
12. [Escopo do Runtime no MVP](#12-escopo-do-runtime-no-mvp)
13. [Trabalho Futuro](#13-trabalho-futuro)
14. [Plano de Validação Técnica](#14-plano-de-validação-técnica)

---

## 1. Propósito e Princípios

Este documento especifica o **runtime** do Kreator — a camada que coordena, executa e versiona o trabalho dos módulos de processamento de mídia. O documento de Produto descreve *o que* o usuário obtém; este descreve *como* o sistema entrega isso.

A tese de engenharia é direta: **modelos são commodity; infraestrutura não.** O valor durável do Kreator não está em possuir o melhor modelo de visão ou de linguagem — esses serão superados em meses — e sim em uma arquitetura que trata modelos como componentes intercambiáveis e entrega custo menor, velocidade maior e estabilidade. Quando um modelo melhor surge, troca-se o componente sem reescrever o pipeline.

Quatro princípios governam todas as decisões deste runtime:

1. **A IA classifica; o Planner decide.** Modelos fornecem propriedades probabilísticas (rótulos, scores, transcrições). Nenhum modelo decide o que entra no vídeo final. A decisão é de um Planner determinístico, que recebe evidências e aplica regras explícitas.
2. **Tudo é contrato.** Cada módulo recebe um contrato de entrada e produz um contrato de saída, com versão e dependências declaradas. Não há efeitos colaterais ocultos.
3. **Reexecutar só o que mudou.** O render completo a cada edição é o comportamento que o Kreator se recusa a ter. O runtime é incremental por construção.
4. **Nada é sobrescrito.** Toda alteração cria uma nova revisão. O histórico é imutável e auditável.

A régua para qualquer adição a este runtime: ela reduz o custo de execução, reduz a complexidade do sistema, melhora a experiência do usuário ou aumenta a confiabilidade do núcleo? Se a resposta for "não" para todas, a mudança não entra.

---

## 2. Visão de Camadas

O processamento de um vídeo flui por camadas com responsabilidades estritas. Sinais determinísticos nascem primeiro; a inferência probabilística entra depois, sempre sobre sinais já extraídos; a decisão vem por último.

```
Vídeo / Áudio bruto
        │
        ▼
   Signal Layer        sinais determinísticos (VAD, OCR, cenas, fluxo óptico, DSP)
        │
        ▼
   Evidence Layer      evidências estruturadas (sinais + classificações dos modelos)
        │
        ▼
     Planner           decide o plano de execução a partir das evidências
        │
        ▼
    Scheduler          ordena o trabalho por benefício/custo, respeitando recursos
        │
        ▼
 Execution Runtime     executa módulos sob contrato, com cache incremental
        │
        ▼
  Cache + Provenance   materializa, versiona e registra cada artefato
        │
        ▼
      Render           projeta o resultado final (lazy)
```

A inversão central em relação ao padrão comum do mercado é deliberada. Em vez de `Vídeo → LLM → Resposta`, o Kreator faz `Vídeo → Signal Layer → Evidências → IA classifica → Planner decide`. Isso é mais barato (a maior parte do trabalho é determinística e roda em CPU), mais estável (a inferência opera sobre features normalizadas) e mais auditável.

---

## 3. Signal Layer

A Signal Layer é a fundação determinística de todo o sistema. Toda inferência posterior nasce daqui, e nada nela depende de modelos probabilísticos: os mesmos bits de entrada produzem sempre os mesmos sinais.

Componentes principais:

- **VAD (Voice Activity Detection)** — segmenta fala e silêncio; base para cortes por silêncio e para acionar transcrição apenas onde há voz.
- **Scene Detection** — detecta cortes de cena e transições por diferença de quadro (PySceneDetect).
- **OCR** — extrai texto presente em tela (HUDs, placares, legendas embutidas).
- **Optical Flow** — mede intensidade e direção de movimento; identifica picos de ação.
- **Histogramas e DSP** — distribuição de cor/luminância por quadro e análise de amplitude/energia do áudio; detectam mudanças bruscas, picos sonoros e variações visuais.

A saída da Signal Layer é um conjunto de séries temporais alinhadas ao timecode do vídeo. Como é determinística e barata, ela é calculada uma vez e fortemente cacheada — toda etapa subsequente a consome em vez de reprocessar o vídeo.

---

## 4. Evidence Layer

A Evidence Layer transforma sinais brutos em **evidências estruturadas** que o Planner consegue consumir. É a fronteira onde a inferência probabilística entra — mas de forma contida.

O fluxo de uma evidência:

1. A Signal Layer entrega features determinísticas (ex.: pico de fluxo óptico em `00:07:15`, pico de amplitude de áudio no mesmo instante).
2. Os modelos (VLM, ASR, classificadores) recebem **apenas o trecho relevante** apontado pelos sinais — não o vídeo inteiro — e produzem rótulos com score de confiança (ex.: `evento=explosão, conf=0.82`).
3. Sinal + classificação são reconciliados em uma evidência única, normalizada e versionada:

```
Evidence {
  t_start: 00:07:10
  t_end:   00:07:22
  signals: { optical_flow_peak: 0.91, audio_peak: 0.88 }
  labels:  { event: "explosion", conf: 0.82, source: "qwen2.5-vl@<hash>" }
  evidence_id: <hash>
}
```

A normalização é o que isola o sistema do não determinismo dos modelos: scores contínuos são reduzidos a faixas estáveis (*buckets*) e mudanças pequenas não derrubam a decisão (*histerese*). Assim, uma variação irrelevante na confiança de um modelo entre duas execuções não muda o plano — o que mantém o comportamento previsível mesmo com inferência probabilística por baixo.

---

## 5. Planner — Decisão Determinística

O Planner é onde as decisões acontecem, e nenhuma delas é tomada por um modelo. Ele recebe o conjunto de evidências e produz um **plano de execução**: a lista ordenada de etapas, com seus módulos, dependências e parâmetros.

A separação é estrita:

- **A IA fornece propriedades.** "Este trecho tem 0,82 de confiança de ser uma explosão." "Esta fala é citável." "Este frame tem um rosto centralizado."
- **O Planner decide.** "Promover este trecho a candidato de Short." "Aplicar o template de thumbnail X." "Cortar aqui."

As regras do Planner são explícitas e versionadas — não um prompt. Dado o mesmo conjunto de evidências e a mesma versão de regras, o plano é idêntico. Isso torna o comportamento testável: pode-se alimentar o Planner com evidências fixas e verificar exatamente qual plano sai.

Decisões editoriais subjetivas (a escolha do "melhor momento") não são resolvidas como verdade única: o Planner produz um **ranking** de candidatos com justificativa por sinal, e o humano permanece no loop até que a memória do canal calibre o critério. (A racional de produto está em *Kreator — Produto*, na seção do K Clipper.)

---

## 6. Execution Contracts

Todo módulo do runtime opera sob um **contrato**. O contrato é o que substitui o encadeamento de prompts por uma rede de serviços verificável.

Um contrato declara:

```
Contract {
  input:        referências de entrada (por hash)
  output:       tipo e esquema do artefato produzido
  version:      versão do módulo + versão das regras/parâmetros
  dependencies: contratos dos quais este depende
  invariants:   condições que a saída deve satisfazer
}
```

Propriedades que os contratos garantem:

- **Determinismo de fronteira.** Um módulo não lê estado oculto nem escreve fora de seu artefato declarado.
- **Composição segura.** O orquestrador (K Orchestrator, no vocabulário de produto) valida que a saída de um módulo satisfaz o contrato de entrada do próximo antes de encadeá-los.
- **Testabilidade.** Cada módulo pode ser testado isoladamente contra seu contrato, sem subir o pipeline inteiro.

Os contratos são a base da execução incremental: como input, versão e dependências são explícitos, o runtime sabe exatamente quando um resultado anterior continua válido.

---

## 7. Execução Incremental

Esta é a peça que mais diferencia o Kreator, e a mais difícil de copiar. O padrão da indústria é `editar → renderizar tudo`. O Kreator faz `editar → identificar dependências → reexecutar somente o necessário`.

### Grafo de dependências

Cada artefato é um nó; cada contrato declara de quais nós depende. O resultado é um DAG (grafo acíclico dirigido) que descreve toda a produção de um vídeo. Quando algo muda, o runtime percorre o grafo a partir do ponto de mudança e marca como inválidos apenas os nós alcançáveis a jusante.

### Cache: hit, miss, materialização

A chave de cache de um artefato é derivada de `hash(input) + version + params`. Na hora de executar uma etapa:

- **Cache hit** — existe um artefato com a mesma chave: reutiliza, custo zero.
- **Cache miss** — a chave não existe: executa o módulo e materializa o novo artefato.

Como a chave inclui a versão do módulo e dos parâmetros, atualizar um modelo invalida automaticamente apenas o que dependia dele.

### Invalidação

Mudou a legenda? Só os nós de legenda e render a jusante invalidam; a análise de vídeo, a transcrição e a thumbnail permanecem válidas e vêm do cache. Trocou o modelo de transcrição? Invalida transcrição e tudo que dela depende, mas preserva os sinais determinísticos da Signal Layer.

### Por que isso importa

O efeito prático é econômico e perceptível: reprocessar um ajuste custa **segundos e centavos** em vez de minutos e dólares de GPU. É o mesmo argumento que qualquer pessoa entende — *o runtime existe para que o vídeo inteiro não seja reprocessado a cada edição* — e é a vantagem competitiva mais defensável do projeto.

---

## 8. Scheduler e Resource Budget

O Scheduler ordena o trabalho. Ele **não tenta ser inteligente artisticamente** — essa inteligência vive nos módulos. Ele apenas agenda execução respeitando recursos e prioridade.

A prioridade segue uma razão simples:

```
prioridade = benefício esperado / custo estimado
```

O benefício é **operacional**, não artístico. Exemplos:

- O usuário abriu a timeline e a thumbnail está visível → prioridade máxima para materializar a thumbnail.
- SEO foi solicitado → executar WhisperX primeiro, depois o resumo, depois o título (ordem de dependência).

O Resource Budget garante que o agendamento respeite os limites físicos da máquina: fila de tarefas, CPU, GPU, RAM e VRAM. Tarefas pesadas de GPU (VLM, TTS) são serializadas ou agrupadas (*batching*) para maximizar ocupação; tarefas de CPU (DSP, Pillow/OpenCV, bancos) rodam em paralelo. No MVP, isso é um escalonador de fila com prioridade e limites de recurso — não um planejador universal.

---

## 9. Versionamento e Provenance

Nada no runtime é sobrescrito. Toda alteração cria uma nova revisão, e cada artefato carrega sua proveniência completa.

### Provenance Database

Cada inferência e cada artefato registram:

```
Provenance {
  artifact_id: <hash do conteúdo>
  model:       nome + versão do modelo
  params:      parâmetros e seed
  contract:    versão do contrato
  inputs:      hashes das entradas
  evidence:    evidências que sustentaram a decisão
  timestamp
}
```

Isso garante **auditabilidade total**: para qualquer frame, legenda ou corte do resultado final, é possível responder "qual modelo, qual versão, quais parâmetros e quais evidências produziram isto?".

### Versionamento por conteúdo

O identificador de cada componente é o **hash do seu próprio conteúdo**. Um único mecanismo resolve, de uma vez, versionamento, deduplicação, verificação de integridade e rollback: se o conteúdo muda, o id muda; se dois artefatos têm o mesmo hash, são o mesmo artefato. Referências são sempre por id e checksum — nunca por nome.

No MVP, o versionamento é uma tabela append-only em PostgreSQL (revisões nunca sobrescritas). A forma completa de MVCC e de armazenamento endereçado por conteúdo em larga escala é tratada em [Trabalho Futuro](#13-trabalho-futuro).

---

## 10. Marketplace Runtime

O marketplace distribui **componentes executáveis** — não prompts, não texto copiável. Um item do marketplace (um Editing Profile ou um módulo) é empacotado, versionado e **assinado digitalmente**.

No momento da contratação:

1. O comprador recebe o componente por id de conteúdo.
2. O runtime verifica assinatura e checksum **antes** de executar — mesmo quando o componente roda na infraestrutura do próprio criador (modelo federado descrito em *Kreator — Produto*, seção Edições/Network).
3. A confiança não depende de inspecionar o conteúdo, e sim da verificação criptográfica de que o componente é íntegro e autêntico.

A consequência de design: como o que se vende é um componente compilado e assinado, e não um prompt, o ativo é mais difícil de copiar e mais fácil de licenciar e revogar.

---

## 11. Mapeamento K Agents → Módulos

No produto, o usuário conversa com uma **equipe de K Agents**. No runtime, cada agente é um **módulo determinístico sob contrato**. A dualidade é intencional e segue o mesmo padrão de qualquer plataforma madura: internamente, componentes; externamente, experiências.

| Produto (experiência) | Runtime (módulo) |
|---|---|
| K Analyst | Signal + Evidence Modules |
| K Clipper | Candidate Ranking Module |
| K Classifier | Semantic Classification Module |
| K Editor | Timeline/Edit Module |
| K Subtitle | Subtitle Module |
| K Voice | TTS Module |
| K Motion | Motion/FX Module |
| K Thumbnail | Thumbnail Composition Module |
| K SEO | Metadata Module |
| K Publisher | Publish Module |
| K Validator | Content Authenticity Module |
| K Security | Integrity/Signature Module |
| K Orchestrator | Scheduler + Contract Validator |

Nenhum módulo tem autonomia: todos recebem contratos e produzem contratos. A "personalidade" de equipe existe na camada de produto para tornar o sistema legível e memorável; por baixo, o comportamento é determinístico e testável.

---

## 12. Escopo do Runtime no MVP

O runtime do MVP é deliberadamente mínimo. O objetivo é provar o núcleo — pipeline de sinais, decisão pelo Planner e execução incremental — sobre poucos módulos.

Entra no MVP:

- Signal Layer (VAD, scene detection, DSP; OCR e optical flow conforme o nicho).
- Evidence Layer com normalização básica (buckets + histerese).
- Planner determinístico com regras explícitas e ranking de candidatos.
- Execution Contracts entre os módulos do pipeline de Shorts.
- Execução incremental com cache por `hash(input)+version+params` e invalidação por grafo.
- Scheduler de fila com prioridade e limites de recurso.
- Provenance append-only em PostgreSQL.

Não entra no MVP (ver seção seguinte): MVCC completo, CAS sofisticado, IPC de alta performance, Projection Engine complexo, Time Chunk Architecture e qualquer runtime de inferência generalista.

---

## 13. Trabalho Futuro

Os itens abaixo são arquiteturalmente legítimos, porém pertencem a fases de escala — não ao MVP. Adicioná-los cedo seria o mesmo overengineering que o projeto evita. Cada um só entra quando houver volume real que o justifique.

- **MVCC completo** sobre a timeline (hoje, append-only simples já basta).
- **Content-Addressable Storage sofisticado** com chunking e deduplicação em nível de bloco (hoje, hash por artefato basta).
- **IPC de alta performance** (memória compartilhada, Apache Arrow/Plasma) para troca de tensores entre módulos sem serialização.
- **Projection Engine** com separação formal entre *projection metadata* e *projection pixels* e materialização lazy avançada.
- **Time Chunk Architecture** — divisão do vídeo por blocos estruturais (não por frame nem por silêncio) para granularidade fina de invalidação.
- **Scheduler com orçamento preditivo de VRAM** e deadlines por tarefa.
- **Execução distribuída multi-node** como padrão (hoje, single-node com Docker Compose).

A régua de admissão continua a mesma: reduz custo, reduz complexidade, melhora a experiência ou aumenta a confiabilidade do núcleo? Sem isso, fica fora.

---

## 14. Plano de Validação Técnica

As premissas técnicas do runtime são validadas por experimentos próprios, complementares aos experimentos de produto:

- **E1 — Recall da Signal Layer.** Os sinais determinísticos capturam os eventos relevantes (a Evidence Layer recebe candidatos suficientes)?
- **E2 — Eficiência do cache.** Qual a taxa de cache hit em ciclos típicos de edição?
- **E3 — Latência incremental.** Quanto tempo custa um ajuste pequeno (legenda, música) versus um render completo?
- **E4 — Qualidade do Planner.** Dado um conjunto de evidências, o plano produzido coincide com a decisão de um editor humano?
- **E5 — Custo por minuto.** Qual o custo de GPU/CPU por minuto de footage processado, ponta a ponta?
- **E6 — Tempo de recompilação.** Após trocar um modelo, quanto do pipeline precisa ser reexecutado?
- **E7 — Estabilidade.** A normalização (buckets + histerese) mantém o plano estável entre execuções com a mesma entrada?

Os experimentos de maior peso são E2 (eficiência do cache) e E3 (latência incremental), porque sustentam diretamente a tese de custo e velocidade que diferencia o Kreator. O custo por minuto (E5) conecta este documento à seção de Economia Unitária do documento de Produto.

---

*Kreator Runtime — documento de arquitetura interna. Complementa o documento de Produto, que permanece a referência de visão, identidade e modelo de negócio.*
