# Kreator
## The Operating System for Human Creativity

> *Human Creativity. AI Operations.*

---

**Autor:** Johnny Kestler (pseudônimo) — João Vitor Perazzolo
**Data de criação:** 27 de junho de 2026
**Versão:** 2.0
**Documento:** Produto — Visão e Arquitetura de Alto Nível
**Documento complementar:** Kreator Runtime (especificação de arquitetura interna)

---

## Sumário

1. [Visão Geral](#1-visão-geral)
2. [O Problema](#2-o-problema)
3. [A Solução](#3-a-solução)
4. [Filosofia Central](#4-filosofia-central)
5. [Os Quatro Pilares](#5-os-quatro-pilares)
6. [Os K Agents](#6-os-k-agents)
7. [Arquitetura do Sistema](#7-arquitetura-do-sistema)
8. [K Protocol — Coordenação, Permissões e Determinismo](#8-k-protocol--coordenação-permissões-e-determinismo)
9. [Trust Layers e Immutable Core](#9-trust-layers-e-immutable-core)
10. [Edições, Hospedagem e a Kreator Network](#10-edições-hospedagem-e-a-kreator-network)
11. [Fluxo Completo de Produção](#11-fluxo-completo-de-produção)
12. [K Intelligence — Inteligência de Mercado](#12-k-intelligence--inteligência-de-mercado)
13. [Editing Profile](#13-editing-profile)
14. [K Memory — Sistema de Memória e Aprendizado](#14-k-memory--sistema-de-memória-e-aprendizado)
15. [O Problema do Cold Start](#15-o-problema-do-cold-start)
16. [Responsible Learning](#16-responsible-learning)
17. [K Store — Marketplace](#17-k-store--marketplace)
18. [MVP — Produto Inicial](#18-mvp--produto-inicial)
19. [Economia Unitária — Custo por Vídeo](#19-economia-unitária--custo-por-vídeo)
20. [Riscos de Plataforma e Dependências de API](#20-riscos-de-plataforma-e-dependências-de-api)
21. [Análise Competitiva e Cunha de Diferenciação](#21-análise-competitiva-e-cunha-de-diferenciação)
22. [Creator Success Program](#22-creator-success-program)
23. [Roadmap](#23-roadmap)
24. [Evolução para Modelos Próprios](#24-evolução-para-modelos-próprios)
25. [Visão de Longo Prazo](#25-visão-de-longo-prazo)
26. [Diferenciação Competitiva](#26-diferenciação-competitiva)
27. [Premissas Críticas e Plano de Validação](#27-premissas-críticas-e-plano-de-validação)
28. [Identidade da Marca](#28-identidade-da-marca)

**Apêndice A** — [Stack Técnica e Infraestrutura](#apêndice-a--stack-técnica-e-infraestrutura)

---

## 1. Visão Geral

O **Kreator** não é um gerador de conteúdo.

É um **sistema operacional para produção de conteúdo digital**.

Seu objetivo é automatizar todo o trabalho operacional de criação de vídeos sem substituir a criatividade humana. O conteúdo sempre nasce de um criador real. A inteligência artificial observa, organiza, edita, otimiza, publica, analisa e aprende.

Enquanto outras plataformas usam IA para substituir pessoas, o Kreator usa IA para **escalar pessoas**.

A criatividade continua sendo humana.
O estilo continua sendo humano.
As decisões artísticas continuam sendo humanas.
A inteligência artificial assume apenas aquilo que computadores fazem melhor: tarefas repetitivas, organização, execução, análise de dados e otimização contínua.

> *O Kreator não cria criadores. O Kreator potencializa criadores.*

---

## 2. O Problema

### O problema dos criadores

Nos últimos anos, a IA generativa tornou trivial produzir milhares de vídeos artificiais. Esse fenômeno criou um volume enorme de conteúdo sintético — frequentemente chamado de *AI slop* —, reduzindo a qualidade média do conteúdo online e gerando desconfiança entre criadores, plataformas e público.

Ao mesmo tempo, criadores humanos autênticos enfrentam a realidade oposta: quanto mais crescem, mais demanda operacional acumulam. Edição, thumbnails, SEO, agendamento, análise de métricas, resposta a comentários — tudo isso consome o tempo que deveria ser dedicado à criação.

### O problema dos editores

Editores de vídeo profissionais têm sua capacidade limitada pelo tempo disponível. Quanto mais clientes têm, mais difícil fica manter qualidade e velocidade. Hoje existem apenas duas saídas:

- Contratar mais pessoas
- Trabalhar mais horas

Nenhuma das duas escala de forma eficiente.

### A lacuna do mercado

Existe uma distinção fundamental que nenhuma solução atual endereça de forma completa:

| IA Generativa | Kreator |
|---|---|
| A IA cria o conteúdo | O humano cria o conteúdo |
| Vídeos sintéticos | Vídeos reais |
| Gameplay falso | Gameplay gravado pelo criador |
| Voz sintética como protagonista | Voz sintética como ferramenta opcional |
| Canal feito por IA | Canal **operado** por IA |

Essa última linha resume a tese:

> **AI-generated content ≠ AI-operated content**

É importante delimitar a fronteira do mercado. Já existem ferramentas que executam *parte* deste trabalho a partir de footage real — corte automático de Shorts, reframe e legendas. Isso, hoje, é commodity. A lacuna que o Kreator ataca é outra: operar o **canal inteiro como um estúdio**, com memória, estratégia, publicação e um marketplace de processos editoriais. O posicionamento detalhado frente às soluções existentes está na [Seção 21](#21-análise-competitiva-e-cunha-de-diferenciação).

---

## 3. A Solução

O Kreator propõe uma terceira alternativa ao dilema de criadores e editores.

Em vez de substituir o criador ou o editor, o sistema **amplia sua capacidade**.

Funciona como uma equipe digital composta por **K Agents** especializados, que executam tarefas repetitivas enquanto preservam integralmente a identidade criativa do profissional.

O objetivo nunca é criar conteúdo do zero. O objetivo é **potencializar conteúdo real**.

Uma analogia útil é a de uma produtora de cinema: ela tem diretor, editor, colorista, operador de áudio, social media, analista e gerente. Nenhum desses profissionais cria o ator ou a cena — todos trabalham em cima do material filmado. O Kreator é exatamente isso: **uma produtora digital**.

### Conteúdo suportado

Embora o foco inicial seja YouTube (gameplay e Shorts), o Kreator foi projetado para trabalhar com qualquer mídia original fornecida pelo criador:

- gameplays e transmissões gravadas
- vídeos de câmera e vlogs
- podcasts e entrevistas em vídeo
- aulas e conteúdo educativo
- vídeos institucionais e corporativos
- cobertura de eventos e esportes

O sistema não exige formato específico — apenas que o conteúdo seja de autoria do criador ou devidamente licenciado por ele.

### O criador decide o nível de automação

**Exemplo 1 — automação técnica:** o criador envia uma gameplay sem narração e pede edição dinâmica, cortes inteligentes, zooms, legendas, efeitos sonoros da biblioteca pessoal e exportação em Shorts. Nada é inventado — os agentes apenas transformam o material enviado.

**Exemplo 2 — produção em escala:** o criador envia 2 horas de vídeo e pede que os agentes identifiquem os melhores momentos, produzam cinco Shorts, criem um vídeo de highlights e organizem os arquivos finais. Todo o processo usa exclusivamente o conteúdo enviado.

**Exemplo 3 — refinamento mínimo:** o criador envia um vlog bruto e pede apenas remoção de pausas, correção de áudio, legendas, thumbnail a partir de um frame real e preparo para publicação. O conteúdo permanece integralmente autêntico.

### Modos de interação

**Modo Guiado** — o criador escolhe as opções na interface: tipo de output, intensidade de edição, estilo de legendas, formato, duração máxima, workflow a usar, biblioteca de ativos e destino de publicação.

**Modo Conversacional** — à medida que os agentes evoluem, o Kreator interpreta instruções em linguagem natural:

> *"Transforme esta gameplay de GTA V em um Short de ~30 segundos. Escolha o momento mais engraçado, use o K Workflow do Editor X, adicione legendas animadas, memes da minha biblioteca, efeitos sonoros discretos e exporte em vertical para YouTube Shorts."*

Selecionar *o* melhor momento de um vídeo é o pedido mais difícil de todo o sistema — um julgamento editorial subjetivo. Por isso o Kreator não tenta acertar sozinho de primeira: ele entrega um *ranking* de candidatos, cada um com a justificativa de por que foi escolhido, e mantém o criador no controle da decisão até que a memória do canal aprenda o gosto dele. O funcionamento desse processo está detalhado no [K Clipper](#k-clipper).

### Todo resultado permanece baseado no material enviado

Independente do nível de automação, existe uma regra que nunca muda. Os K Agents apenas: analisam, organizam, selecionam, editam, sincronizam, refinam, otimizam e exportam.

Nenhum agente substitui, fabrica ou inventa conteúdo. Todo vídeo produzido mantém como base exclusiva o material originalmente fornecido pelo criador.

> *O Kreator não cria conteúdo para seus usuários. Ele potencializa o conteúdo que eles já criaram — eliminando as tarefas operacionais repetitivas e preservando autenticidade, autoria e identidade criativa.*

---

## 4. Filosofia Central

### Human Creativity. AI Operations.

Este é o princípio fundamental do projeto. Não é um slogan de marketing — é uma **restrição arquitetural** que orienta todas as decisões do sistema.

### Reality First Principle

Todo K Agent deve obedecer ao seguinte princípio:

> *Always preserve the authenticity of the original content. Never fabricate events, gameplay, conversations or situations that did not occur.*

Na prática:

- O K Voice não pode afirmar que houve uma vitória se o jogador perdeu
- O K Editor não pode criar uma explosão que nunca existiu no vídeo
- O K Clipper não pode inventar um highlight
- O K Thumbnail nunca sintetiza pixels que não existiam no vídeo original — nem para "melhorar" a imagem

O sistema **nunca inventa acontecimentos**, nunca cria histórias falsas, nunca fabrica gameplay e nunca altera o significado dos acontecimentos.

### Zero Generated Images

Este princípio é um dos diferenciais mais estratégicos do projeto, e por isso precisa ser tratado com total coerência.

**A regra inviolável:** o Kreator nunca usa IA generativa para *fabricar conteúdo visual que não existia* — nenhum agente pede a um modelo de difusão que "gere" uma cena, um cenário, uma expressão, um personagem, uma arma ou uma explosão que não estavam no vídeo.

Em vez disso, os agentes de imagem operam como um **editor de Photoshop experiente**: pegam frames reais, recortam, ajustam cor, aplicam contraste, detectam o rosto do criador, removem ou desfocam o fundo, compõem dois frames reais e adicionam texto, bordas e efeitos programáticos. Tudo a partir de pixels que já existiam.

A fronteira correta não está entre "usar ou não usar redes neurais", e sim entre **dois tipos de operação sobre pixels**:

| Permitido (transforma pixels reais) | Proibido (fabrica pixels novos) |
|---|---|
| Recorte, reenquadramento, composição de frames reais | Geração text-to-image de cenas inexistentes |
| Ajuste de cor, contraste, nitidez (Pillow/OpenCV) | "Imaginar" uma expressão facial que não houve |
| Remoção/desfoque de fundo via segmentação (rembg) | Inserir objetos, armas, cenários inventados |
| Upscaling / denoise de um frame real (super-resolução) | Criar um plano de fundo sintético |

Upscaling e denoise são aceitáveis porque **não inventam conteúdo** — apenas aumentam a fidelidade de pixels que já existiam. Geração text-to-image, não.

Na prática, o pipeline de thumbnail é 100% programático desde o primeiro dia: seleção de frame real + Pillow + OpenCV + rembg + MediaPipe. Quando há necessidade de ganho de qualidade visual, usa-se exclusivamente super-resolução sobre o frame real — nunca geração de cena.

A consequência dessa escolha é assumida com clareza: uma thumbnail composta de frames reais pode parecer ligeiramente menos "chamativa" que uma criada por um gerador. Em troca, o Kreator ganha **integridade de marca**, conformidade nativa com o YouTube e a garantia de que cada miniatura representa fielmente o que o vídeo contém.

Isso importa por três razões:

**Autenticidade com o público.** A thumbnail mostra o que o vídeo realmente contém — reduzindo abandono precoce e melhorando os sinais de satisfação que o YouTube usa para distribuição orgânica.

**Conformidade com políticas.** O YouTube exige que thumbnails representem fielmente o conteúdo. Uma thumbnail gerada por IA com algo que nunca apareceu no vídeo pode resultar em penalização ou desmonetização. Thumbnails compostas de frames reais são intrinsecamente conformes.

**Identidade visual genuína.** Editores profissionais não geram thumbnails do zero — eles escolhem o melhor frame, trabalham a imagem e adicionam texto e estilo do canal. O Kreator faz exatamente isso, de forma automática.

> *Agentes de imagem = editores de Photoshop. Não geradores de imagem.*

---

## 5. Os Quatro Pilares

### Pilar 1 — Human Content
Todo vídeo parte de material criado por um ser humano real. O criador é a fonte. A IA é a equipe de produção.

### Pilar 2 — AI Operations
Uma equipe de K Agents especializados assume todo o trabalho operacional após a gravação: compreensão, edição, publicação, análise e otimização contínua.

### Pilar 3 — Community Learning
O sistema evolui junto com sua comunidade. Criadores e editores que desejarem podem contribuir voluntariamente para aprimorar os agentes, com consentimento explícito, transparente e revogável.

### Pilar 4 — Modular Intelligence
A inteligência não pertence aos modelos. Ela pertence ao sistema. Se amanhã surgir um modelo open source melhor, basta substituir um componente. A inovação não está em possuir o melhor LLM — está em possuir a melhor arquitetura para coordenar dezenas de modelos diferentes. Essa modularidade se estende à própria distribuição da plataforma: o usuário instala apenas os pacotes de que precisa, no modelo de **K Packages** descrito na [Seção 10](#10-edições-hospedagem-e-a-kreator-network).

---

## 6. Os K Agents

Cada **K Agent** tem uma responsabilidade única e trabalha de forma coordenada com os demais — formando uma equipe digital especializada. O usuário não interage com uma única IA; ele trabalha com uma equipe completa de especialistas, segundo o princípio:

> **One Agent. One Responsibility.**

A inteligência do sistema emerge da colaboração entre todos eles.

### K Orchestrator
**Papel:** orquestrador / gerente do estúdio digital.

Recebe o material após o upload e distribui tarefas para todos os demais agentes. Nunca edita vídeos. Nunca escreve roteiros. Sua única função é **coordenar** — garantindo que cada agente receba a informação certa, no momento certo, na sequência correta.

**Ferramentas:** LangGraph (MIT) como motor de orquestração. Implementado como grafo de estados finitos onde cada nó é uma etapa de processamento. O checkpointing nativo garante que, em caso de falha, o pipeline retome do último ponto estável sem reprocessar o vídeo bruto. O estado global do projeto transita em um objeto unificado entre os nós. Para protótipos, CrewAI oferece curva de aprendizado menor e pode ser portado para LangGraph depois.

### K Analyst
**Papel:** compreensão completa do vídeo.

Não processa o vídeo inteiro de uma vez — nenhum modelo faz isso com confiança. Opera como sistema distribuído:

```
Vídeo
  ↓ Segmentação automática em cenas de 20–60s
  ↓ VLM analisa cada segmento individualmente
  ↓ K Memory salva cada análise
  ↓ LLM conecta os segmentos em narrativa coerente
  ↓ Mapa temporal completo do vídeo
```

Quem entende a história inteira não é um único modelo — é a **cadeia de contextos** preservada pela K Memory e conectada pelo LLM.

Produto final — mapa temporal detalhado:

```
00:02:31  Encontrou um tanque        Importância: média
00:07:15  Explosão inesperada        Importância: alta
00:15:41  Momento muito engraçado    Importância: muito alta
```

**Ferramentas:** Qwen2.5-VL 7B (Apache-2.0) como VLM; PySceneDetect (BSD-3) para segmentação; YOLO v8 para detecção de objetos/eventos do jogo (HUDs, ícones de kill, barras de vida); WhisperX para transcrição com timestamps por palavra. Para vídeos de 2–3h, opera em janelas de 20–30 min com sobreposição. O LLM local (Qwen3 ou Llama 3 via Ollama) gera o mapa semântico final em JSON.

### K Clipper
**Papel:** avaliar e ranquear o destino de cada momento (Short / vídeo longo / descarte) e montar os recortes preliminares.

Decidir o que "merece virar Short" é um julgamento editorial subjetivo, e o Kreator trata isso com humildade de design. Em vez de impor uma escolha única, o K Clipper:

1. **Ranqueia, não decide** — entrega os top-N candidatos com pontuação e justificativa por sinal (gancho, pico emocional, conflito, revelação, frase citável, energia visual).
2. **Mantém o humano no loop** nos primeiros vídeos: o criador aprova ou reprova candidatos, e cada decisão alimenta a K Memory.
3. **Calibra por canal** ao longo do tempo, até que o ranking convirja com o gosto do criador.

**Ferramentas:** AI-Youtube-Shorts-Generator (MIT) como base de ranqueamento por transcrição; Crispy para detecção visual de eventos em FPS/MOBA (kill feed, explosões, telas de fim de jogo); picos de amplitude de áudio como gatilho adicional. Offsets configuráveis capturam ~7s antes e ~3s após cada evento. Clipes sobrepostos são deduplicados.

### K Classifier
**Papel:** categorizar cada corte (Épico, Engraçado, Assustador, Bug, Fail, Highlight, Tutorial, Surpresa, Tenso, Competitivo).

**Ferramentas:** LLM local (Qwen3 via Ollama) recebe o trecho de transcrição + metadados visuais e classifica em JSON; KeyBERT (MIT) extrai termos dominantes. A saída é persistida com o `segment_id` para consulta futura pelo K Publisher e pelo K Strategy.

### K Editor
**Papel:** edição propriamente dita.

Executa decisões de edição com ferramentas reais:

```
Mapa temporal + Transcrição
  ↓ LLM → entender contexto e intenção
  ↓ VLM → confirmar eventos visuais
  ↓ FFmpeg → cortes
  ↓ K Library → selecionar meme/asset
  ↓ FFmpeg → incorporar e exportar
```

Ações: zoom, cortes, transições, efeitos, memes, músicas, legendas, enquadramento vertical. Todos os elementos vêm da **K Library** — nunca de geradores.

**Ferramentas:** auto-editor (domínio público) para o primeiro corte (remoção de silêncios); FFmpeg para todas as operações determinísticas (cortes, zoom, transições, 9:16, composição); MoviePy como API Python de alto nível. Normalização de áudio via auto-editor (`--edit audio:threshold=0.04`).

### K Subtitle
**Papel:** gerar e sincronizar legendas automaticamente.

**Ferramentas:** WhisperX (faster-whisper + wav2vec2, BSD-2) com timestamps por palavra, permitindo legendas animadas palavra-a-palavra. Estilo (fonte, cor, animação, posição) definido pelo Editing Profile do canal.

### K Voice
**Papel:** locução (quando aplicável). Quatro modos: (1) sem narração, (2) narração via IA genérica, (3) voz clonada do criador com autorização explícita, (4) somente legendas.

**Ferramentas:** Fish Speech (Apache-2.0) para canais monetizados; XTTS v2 (CPML) para máxima qualidade de clonagem (a partir de 6s de referência, recomendado 15s; 17 idiomas com transferência cross-lingual); Kokoro-82M (Apache-2.0) para operação em CPU no MVP. No Modo 3, usa gravação de referência como condicionamento — sem treinamento adicional.

### K Motion
**Papel:** efeitos visuais e animações.

**Ferramentas:** FFmpeg com `-filter_complex` para composição de camadas, overlays animados, shake, zoom cinético e transições; MoviePy como abstração. Todos os assets vêm da K Library — o agente não gera efeitos do zero, ele seleciona, parametriza e aplica recursos existentes conforme o Editing Profile.

### K Thumbnail
**Papel:** editor programático de miniaturas — **edita** imagens, não as gera.

```
Frame real selecionado
  ↓ Detecção facial (MediaPipe)
  ↓ Recorte inteligente (composição ideal)
  ↓ Remoção/desfoque de fundo (rembg / U2Net)
  ↓ Ajuste de cor, contraste, saturação (Pillow)
  ↓ Sharpening seletivo (OpenCV)
  ↓ Composição com segundo frame real (opcional)
  ↓ Template do canal (Editing Profile)
  ↓ Texto (Pillow + fontes da K Library)
  ↓ Bordas, glow, sombra (programáticos)
  ↓ Exportação em múltiplas versões
```

**O que nunca faz:** criar cenários, expressões, personagens, armas ou itens que não apareceram no vídeo. O detalhamento do princípio está na [Filosofia Central](#4-filosofia-central).

**Ferramentas:** VLM (Qwen2.5-VL) + CLIP (MIT) para seleção de frame; MediaPipe FaceMesh (Apache-2.0) para detecção facial; rembg (MIT) para segmentação; Pillow/PIL (MIT) e OpenCV (Apache-2.0) para edição programática; super-resolução opcional sobre o frame real (sem fabricação de cena).

### K SEO
**Papel:** otimização para descoberta — título, descrição, hashtags e palavras-chave alinhados ao estilo do canal e aos padrões de desempenho da K Memory.

**Ferramentas:** LLM local (Qwen3-14B ou Llama 3 via Ollama/vLLM) com saída JSON; DSPy (MIT, Stanford) para otimização programática de prompts contra o histórico do canal; KeyBERT para palavras-chave; yt-dlp (Unlicense) para metadados de concorrentes como referência.

### K Publisher
**Papel:** publicação e gestão do canal — agendar/publicar, responder comentários simples, atualizar playlists, organizar a estrutura.

**Ferramentas:** YouTube Data API v3 (Apache-2.0) via `google-api-python-client`; agendamento via `status.publishAt`; upload em chunks com retry e backoff exponencial.

A publicação automatizada depende das cotas e dos termos da YouTube API, o que torna a arquitetura de autenticação um ponto sensível. O Kreator adota **OAuth por criador** — cada criador autoriza com a própria conta, de modo que a cota é individual e escala naturalmente com a base. As implicações completas dessa dependência estão tratadas nos [Riscos de Plataforma](#20-riscos-de-plataforma-e-dependências-de-api).

### K Validator
**Papel:** verificação automática de autenticidade antes da publicação.

Checa: existem assets não registrados? Existe imagem gerada artificialmente? Existe frame sintético? Existe áudio sintético sem autorização explícita? **Se qualquer verificação falhar, o vídeo não é publicado.**

### K Security
**Papel:** integridade do sistema — não toca em vídeos.

Verifica assinaturas digitais, hashes, permissões, isolamento de sandbox e controle de acesso. Confirma que cada Workflow, modelo ou biblioteca utilizado é exatamente o componente original, íntegro e não modificado. Enquanto o K Validator garante a autenticidade do *conteúdo*, o K Security garante a integridade da *plataforma*. O detalhamento está na [Seção 9](#9-trust-layers-e-immutable-core).

### K Analytics
**Papel:** monitorar o desempenho real dos vídeos e acompanhar a evolução do canal.

**Ferramentas:** YouTube Analytics API + Grafana (ou Metabase / Superset). Alimenta a K Memory com CTR, retenção, comentários, compartilhamentos e horários.

### K Memory
**Papel:** nunca produz — apenas lembra. O agente mais silencioso e um dos mais importantes.

Registra tudo: CTR por vídeo, retenção média, comentários e sentimento, compartilhamentos, horários, tipo/duração/tema, humor/música/thumbnail, títulos e descrições. Com o tempo descobre padrões invisíveis à análise manual:

> Perseguição + menos de 28s + música acelerada + explosão antes dos 5s → **3× mais visualizações**

Ninguém programa esse padrão — a K Memory o descobre.

**Ferramentas (3 camadas):**
- **Memória de agente:** Mem0 (Apache-2.0) para personalização e recuperação semântica; Letta (Apache-2.0) para sessões longas.
- **Banco vetorial:** pgvector no PostgreSQL para volumes iniciais; migração para Qdrant (Apache-2.0, Rust) ao escalar.
- **Grafo de conhecimento:** Microsoft GraphRAG (MIT) + Neo4j Community (GPLv3), exposto como microsserviço MCP. Permite perguntas como *"quais thumbnails usaram tons frios em vídeos de GTA V com CTR acima de 8%?"* sem alucinações.

### K Scientist
**Papel:** experimentação sistemática (testes A/B autônomos).

> "Thumbnails com fundo vermelho aumentam o CTR?" → cria duas versões → publica ambas → espera dados → compara → registra a conclusão.

**Ferramentas:** Arize Phoenix (MIT) para observabilidade (traces OpenTelemetry); statsmodels + scipy.stats (BSD-3) para testes de hipótese; PyMC (Apache-2.0) para inferência bayesiana com poucos vídeos por coorte. Cada conclusão é registrada no grafo com metadados de confiança: `(duração<25s) -[CORRELACIONA_COM]→ (retenção: +12%, n=8, confiança: baixa)`. Conclusões com n baixo são tratadas como hipóteses a re-testar — não como verdades.

### K Strategy
**Papel:** direção estratégica do canal. Após meses de operação, conhece o canal melhor que qualquer consultor externo:

- "Não grave mais missões. Grave perseguições."
- "Pare de postar às 10h. Seu público responde melhor às 19h."
- "Esse formato de missão longa perdeu força — migre para cortes mais curtos."

**Ferramentas:** Prophet (MIT, Meta) para séries temporais e sazonalidade; AutoGluon (Apache-2.0, AWS) como AutoML tabular para prever desempenho antes da gravação; LightFM (Apache-2.0) modelando "o que produzir a seguir" como sistema de recomendação; LangGraph para sintetizar números em recomendações em linguagem natural.

---

## 7. Arquitetura do Sistema

### Visão geral

```
Kreator
├── Modelos Base (Open Source)
│   ├── LLM (Llama, Qwen)
│   ├── VLM — Visão
│   ├── Whisper — Transcrição
│   ├── TTS — Síntese de Voz
│   └── OCR — Leitura de Texto
├── Ferramentas
│   ├── FFmpeg — Processamento de Vídeo
│   └── Vector DB — Memória Semântica
├── K Library — Coleção de Mídias Autorizadas
├── K Registry — Índice de Workflows, Modelos e Ativos
├── K Validator — Verificação de Autenticidade de Conteúdo
├── K Security — Integridade do Sistema (hashes, assinaturas)
├── Channel Profile — Perfil do Canal
├── K Memory — Histórico Persistente
└── K Agents
    ├── K Orchestrator (coordenador central)
    ├── K Analyst   ├── K Clipper    ├── K Classifier
    ├── K Editor    ├── K Subtitle   ├── K Voice
    ├── K Motion    ├── K Thumbnail  ├── K SEO
    ├── K Publisher ├── K Validator  ├── K Security
    ├── K Analytics ├── K Memory     ├── K Scientist
    └── K Strategy
```

### Níveis de inteligência

**Nível 1 — Conhecimento geral (pré-treinado).** Os modelos open source já dominam linguagem, visão e áudio. Vem "de fábrica".

**Nível 2 — Configuração do criador.** O usuário responde poucas perguntas que definem o perfil do canal. Isso gera um arquivo de configuração — não um modelo treinado.

```yaml
channel:
  niche: gta
  humor: high
  subtitles: energetic
  clip_length: 25
  narration: false
```

**Nível 3 — Memória persistente.** O aprendizado acontece por registro de fatos, não por fine-tuning. Após centenas de vídeos, acumula padrões reais de desempenho.

**Nível 4 — Ajuste por feedback.** O usuário avalia resultados (gostei / não gostei / muito longo). O sistema registra preferências e as aplica — sem GPUs, sem treinamento.

### K Library

Toda mídia usada pelos agentes precisa estar registrada previamente e é indexada pelo Asset Registry (parte do [K Registry](#9-trust-layers-e-immutable-core)). Nenhum agente tem acesso a modelos de geração de imagem.

```
✓ Frames capturados do vídeo original
✓ Vídeo e áudio enviados pelo criador
✓ Memes da biblioteca pessoal
✓ Músicas autorizadas
✓ Overlays, templates, fontes, efeitos sonoros, stingers
```

### Stack e infraestrutura

Todas as ferramentas usadas pelos agentes são open source — a stack tecnológica completa e os requisitos de hardware estão consolidados no [Apêndice A](#apêndice-a--stack-técnica-e-infraestrutura). A camada de thumbnail, em particular, é 100% programática, sem nenhum modelo de geração de imagem.

### Comunicação Inter-Agentes

Os agentes não trocam arquivos de vídeo — apenas referências (payloads JSON leves apontando para o MinIO):

```json
{
  "task_id": "clip_001",
  "video_path": "/shared-scratch/raw-vods/session_01.mp4",
  "segment_start": "00:07:10",
  "segment_end": "00:07:22",
  "importance": "high",
  "category": "explosion"
}
```

Para chamadas entre serviços, o sistema usa **MCP (Model Context Protocol)** — protocolo aberto que permite a um agente chamar ferramentas de outro de forma padronizada. A K Memory, por exemplo, expõe consultas ao Neo4j como microsserviços MCP.

### Execução incremental

O Kreator não reprocessa o vídeo inteiro a cada ajuste. Quando o criador muda uma legenda, troca uma música ou corta dois segundos, o sistema identifica exatamente quais etapas dependem daquela mudança e reexecuta **somente o necessário**, reaproveitando do cache tudo o que permaneceu igual. É o que separa uma edição que custa centavos e segundos de uma que custa minutos e dólares de GPU — e é uma vantagem difícil de copiar. O funcionamento desse motor (grafo de dependências, política de cache e invalidação) está especificado no documento **Kreator Runtime**.

### Estratégia de Deploy

**Estágio 1 — Docker Compose (single-node):** todos os serviços em uma máquina. Ideal para desenvolvimento e primeiros criadores.

**Estágio 2 — Multi-node distribuído:** workers GPU (VLM, TTS) em máquinas dedicadas; comunicação via Redis Streams; renderização FFmpeg escala horizontalmente.

**Estágio 3 — Kubernetes (multi-canal):** workers sem GPU escalam via HPA; bancos como StatefulSets; NVIDIA device plugin para alocação de GPU por pod; MinIO distribuído.

---

## 8. K Protocol — Coordenação, Permissões e Determinismo

Dezenas de K Agents podem participar de um mesmo projeto, mas nenhum tem autoridade para alterar livremente o trabalho de outro. A coordenação é centralizada no **K Orchestrator**, que distribui tarefas, controla permissões pelo princípio do menor privilégio, resolve dependências e valida cada entrada e saída. Cada agente tem uma única responsabilidade e nunca se comunica diretamente com outro: toda troca passa pelo orquestrador, o que elimina decisões concorrentes e mantém o comportamento do sistema previsível.

Essa coordenação obedece a um princípio único, o **K Protocol**:

> Nenhum agente altera diretamente o trabalho de outro. Cada agente produz um artefato estruturado — análise, timeline, metadados, recomendação ou validação — verificado pelo K Orchestrator antes de ser consumido pelo próximo.

Na prática, isso aproxima o Kreator de uma arquitetura de microsserviços, e não de um amontoado de prompts encadeados — é o que permite à automação escalar sem virar caos.

O Kreator também busca **reprodutibilidade auditável**: dois projetos executados com o mesmo material, a mesma configuração e a mesma versão dos componentes produzem resultados equivalentes. Com modelos rodando em GPU, identidade bit-a-bit é inviável, mas seeds fixos, temperatura zero onde aplicável e registro completo de versões garantem auditoria, depuração e evolução controlada.

> O mecanismo interno — contratos de execução entre módulos, motor de execução incremental, isolamento por sandbox e o escalonador de recursos — está especificado no documento complementar **Kreator Runtime**.

---

## 9. Trust Layers e Immutable Core

A integridade do Kreator se apoia em uma separação rígida entre o que é descartável e o que é permanente. Cada projeto roda em um **Sandbox** isolado, que pode ser destruído ao fim sem afetar nada; já o núcleo da plataforma — modelos, Workflows, bibliotecas e ativos — nunca é alterado em produção. Componentes não são editados: são **substituídos por novas versões**.

> **Everything is Replaceable. Nothing is Mutable.**
> *Tudo pode ser substituído. Nada deve ser alterado diretamente.*

Esse princípio entrega três garantias de produto. **Versionamento e auditoria:** nada é sobrescrito — cada atualização cria uma versão nova e a anterior continua existindo, então qualquer projeto pode ser reproduzido ou auditado no futuro. **Rollback instantâneo:** se algo dá errado, o sistema apenas reaponta para a versão anterior, sem reconstruir nada — o mesmo modelo de imutabilidade que sustenta Git, NixOS e Docker. **Integridade verificável:** cada componente é identificado pelo hash do próprio conteúdo e assinado digitalmente, e o agente **K Security** confirma, antes de cada uso, que o que está rodando é exatamente o componente original e íntegro.

A distinção de papéis é clara: o **K Validator** cuida da autenticidade do *conteúdo* (Reality First, zero imagens geradas, apenas assets registrados), enquanto o **K Security** cuida da integridade do *sistema*. Uma consequência direta: se um atacante comprometer um agente, o máximo que alcança é um Sandbox — o núcleo permanece intacto, porque é somente leitura.

> O detalhamento de mecanismo — armazenamento endereçado por conteúdo, K Registry, banco versionado (MVCC) e isolamento entre processos — está no documento **Kreator Runtime**.

---

## 10. Edições, Hospedagem e a Kreator Network

O Kreator é distribuído como um sistema operacional, não como um aplicativo monolítico. A mesma arquitetura de agentes roda em diferentes ambientes; o que muda é a origem dos recursos e o local de execução.

### Edições: Cloud e Local

**Kreator Cloud** é a experiência completa do ecossistema: K Agents continuamente atualizados, K Marketplace, Workflows publicados pela comunidade, bibliotecas compartilhadas, inteligência de mercado em tempo real, sincronização entre dispositivos e processamento distribuído. É indicada para quem quer aproveitar todo o potencial colaborativo da plataforma.

**Kreator Local** executa tudo na máquina do usuário — agentes, bibliotecas, Workflows próprios, modelos open source compatíveis, banco de dados e memória local. Nenhum conteúdo precisa sair do equipamento. É indicada para quem prioriza privacidade, controle e personalização, incluindo a possibilidade de especializar agentes com os próprios dados (vídeos antigos, projetos, presets) inteiramente offline. Em contrapartida, recursos que dependem de licenciamento comunitário — Workflows comerciais, bibliotecas licenciadas, inteligência colaborativa — podem não estar disponíveis nessa edição.

As duas edições compartilham a mesma arquitetura, o que permite migrar projetos entre ambientes sem reconstrução.

### K Packages

A instalação é modular, como em uma distribuição Linux. Em vez de instalar "o Kreator" inteiro, o usuário instala apenas o que precisa:

```
Kreator Core
├── K Orchestrator
├── K Memory
├── K Security
└── K Workflow Engine

+ K Video Pack
+ K Audio Pack
+ K Subtitle Pack
+ K SEO Pack
+ K Analytics Pack
+ K Market Intelligence Pack
```

Quem só edita gameplays offline instala apenas os módulos necessários; quem quer o ambiente completo instala tudo. A modularidade reduz consumo de disco e memória, permite atualizar ou substituir um pacote sem reinstalar a plataforma e incentiva a comunidade a desenvolver extensões compatíveis. É a materialização concreta do Pilar 4 — Modular Intelligence.

### Modelos de hospedagem

Os agentes personalizados pertencem exclusivamente aos seus criadores; a plataforma não os armazena nem assume sua propriedade. Cada criador decide onde hospedar sua infraestrutura.

**Self-hosted** — o criador executa seus K Agents em sua própria infraestrutura (computador pessoal, workstation, servidor doméstico, NAS, VPS ou nuvem própria), mantendo controle absoluto sobre modelos, bibliotecas, Workflows e disponibilidade.

**Kreator Cloud Hosting** — para quem não deseja administrar infraestrutura, a plataforma fornece servidores, escalabilidade, monitoramento, backups e disponibilidade global. Mesmo hospedados na nuvem oficial, os agentes continuam pertencendo ao criador; a plataforma atua apenas como provedora de infraestrutura.

O criador pode migrar seus agentes entre ambientes a qualquer momento, sem alterar a identidade dos agentes nem os serviços já contratados pelos usuários.

### A Kreator Network

O marketplace não distribui agentes — distribui **acesso** a eles. Quando um usuário contrata um Workflow ou um conjunto de agentes, ele não recebe uma cópia do sistema; o Kreator estabelece uma conexão segura com a infraestrutura definida pelo criador, e toda a execução permanece sob controle do proprietário. O usuário recebe apenas o resultado do processamento autorizado.

```
                 Kreator Network
                    Marketplace
                         │
        ──────────────────────────────────
        │               │                │
     Creator A       Creator B       Creator C
     (Self-Host)     (Cloud)          (NAS)
        │               │                │
     K Agents        K Agents        K Agents
```

Essa federação protege naturalmente a propriedade intelectual: modelos, parâmetros e bibliotecas nunca deixam a infraestrutura do criador, e não há necessidade de distribuir modelos proprietários para milhares de dispositivos.

### Duas camadas de marketplace

A federação convive com o marketplace de Workflows descrito na [Seção 17](#17-k-store--marketplace) em uma hierarquia de duas camadas:

- **Camada base — K Workflows.** Metodologias leves (parâmetros, regras, bibliotecas licenciadas) executadas pelos agentes-padrão do Kreator. É o caminho mais simples para o editor monetizar seu estilo, sem hospedar nada.
- **Camada avançada — Custom Agents federados.** O editor hospeda seus próprios agentes, com modelos e lógica proprietários, e a Kreator Network federa o acesso a eles. É o caminho para quem desenvolveu inteligência própria e quer mantê-la sob seu controle.

### Marketplace verificável

Combinando a federação com a imutabilidade descrita na [Seção 9](#9-trust-layers-e-immutable-core), o comprador verifica a assinatura digital e o checksum de um Workflow **antes** de executá-lo — mesmo quando ele roda no nó do próprio criador. A confiança não depende de inspecionar o conteúdo, e sim da verificação criptográfica de que o componente é íntegro e autêntico.

### O que permanece centralizado

A maior parte do sistema é descentralizada. O Kreator centraliza apenas os serviços que precisam de uma fonte única de verdade: autenticação de usuários, pagamentos, licenciamento, descoberta de agentes (registry), reputação e avaliações, logs de uso autorizados e faturamento. Mesmo que um serviço central fique indisponível, os agentes continuam pertencendo aos criadores e podem ser migrados entre infraestruturas. Isso torna o Kreator menos uma plataforma de IA e mais uma rede de agentes criativos, na qual o marketplace funciona como intermediário confiável entre quem oferece e quem utiliza os serviços.

### Implicação de custo

O modelo de hospedagem desloca a conta de compute. Na edição Cloud, o custo de processamento é da plataforma e entra no modelo de [Economia Unitária](#19-economia-unitária--custo-por-vídeo). No self-hosted, esse custo passa para o criador, que em troca ganha controle total e margem sobre o próprio hardware — um trade-off que cada perfil resolve de forma diferente.

### Filosofia

O Kreator parte do princípio de que criadores devem ser proprietários da inteligência que desenvolvem. A plataforma não centraliza esse conhecimento: fornece a infraestrutura para conectar criadores, agentes e usuários de forma segura, escalável e transparente. O valor do ecossistema não está em possuir os agentes, e sim em permitir que cada criador monetize sua própria infraestrutura mantendo o controle sobre seu trabalho.

---

## 11. Fluxo Completo de Produção

```
Criador grava o vídeo
        ↓ Upload automático
   K Orchestrator recebe o material
        ↓ K Analyst mapeia o vídeo
        ↓ K Clipper seleciona/ranqueia cortes
        ↓ K Classifier categoriza
        ↓ K Editor produz versões
        ↓ K Subtitle gera legendas
        ↓ K Voice gera locução (opcional)
        ↓ K Motion adiciona efeitos
        ↓ K Thumbnail gera miniaturas
        ↓ K SEO cria título e descrição
        ↓ K Validator verifica autenticidade
        ↓ K Publisher agenda e publica
            ↓ YouTube
        ↓ K Analytics coleta métricas
        ↓ K Memory registra tudo
        ↓ K Scientist experimenta
        ↓ K Strategy aprende
   Todo o sistema melhora
```

---

## 12. K Intelligence — Inteligência de Mercado

### Antes da criação

A maioria das ferramentas só ajuda *depois* que o vídeo foi produzido. O Kreator acompanha o criador desde a ideia, com um sistema de inteligência de mercado atualizado continuamente.

### Market Intelligence Dashboard

Monitora informações públicas de YouTube, Instagram, TikTok, Reddit, X, notícias e tendências de pesquisa, e apresenta uma visão consolidada: nichos em crescimento, temas em alta, formatos com melhor desempenho, duração média competitiva, frequência de publicação, tipos de thumbnail, padrões de título, categorias em crescimento e oportunidades pouco exploradas.

Responde perguntas de alto valor:

- Quais nichos crescem mais rápido nesta semana?
- Quais formatos estão saturados?
- Quais oportunidades têm pouca concorrência?
- Que tipo de vídeo combina melhor com o histórico do meu canal?
- Se eu gravar este vídeo hoje, qual o potencial estimado?

Gerado continuamente pelo K Strategy com browser-use e Crawl4AI, que varrem fontes públicas de forma assíncrona.

A coleta de tendências respeita os limites legais e técnicos das plataformas. O Kreator prioriza **APIs oficiais** sempre que existem (YouTube Data API, dados públicos de tendências) e trata scraping como complemento de baixa frequência, respeitando robots.txt e termos de uso. Trata-se de uma fonte que exige manutenção contínua, e não de um componente que se configura uma vez e se esquece.

### Regional Intelligence System

Toda a inteligência pode ser regionalizada (país específico, mercado global ou múltiplos simultâneos). As recomendações refletem a realidade do mercado-alvo do criador — não médias globais irrelevantes.

**Exemplo:** vídeos longos sobre programação podem crescer no Brasil e cair nos EUA ao mesmo tempo. As recomendações ao criador brasileiro refletem o Brasil.

### Market Simulator

Antes de gravar, o criador testa a viabilidade de uma ideia:

> *"Quero gravar 2h aprendendo Python para o público brasileiro."*

```
Potencial de demanda:       Alto
Nível de concorrência:      Médio
Crescimento do nicho (30d): +18%
Formato mais competitivo:   Vídeos longos (90–180 min)
Horário recomendado:        19h–21h (Brasília)
Oportunidade estimada:      Alta
```

Não garante sucesso — transforma a decisão em escolha baseada em dados, não só intuição. A decisão final sempre pertence ao criador.

### O ciclo completo

```
K Intelligence → Criação Humana → Operação pelos K Agents
   → Publicação → Aprendizado Contínuo → K Intelligence (atualizada)
```

---

## 13. Editing Profile

### O problema do estilo

Dizer "meu estilo é cinematográfico" não ensina nada a um sistema. O desafio é transformar **arte em dados mensuráveis**.

### Como o perfil é extraído

O sistema **não infere intenção artística** — isso seria inviável. Ele apenas **mede** o trabalho real de um editor e extrai parâmetros objetivos a partir de vídeos editados, projetos originais e arquivos de timeline (Premiere, DaVinci, Final Cut). É estatística, não mágica:

```
zoom_intensity:      0.35
cut_average_time:    2.8s
caption_style:       centralizada, animada
shake_level:         baixo
humor_density:       alto
sound_fx_frequency:  1 a cada 18s
meme_frequency:      1 a cada 50s
music_volume:        0.18
```

### O perfil como ativo

Esse conjunto de parâmetros vira o **Editing Profile** — a identidade criativa digital do editor, expressa como dados mensuráveis. Se um criador quer vídeos "no estilo do Editor João", o sistema carrega o Editing Profile daquele editor e executa a edição seguindo exatamente aquela configuração.

---

## 14. K Memory — Sistema de Memória e Aprendizado

### Channel Profile

Toda a inteligência sobre um canal é centralizada em um arquivo persistente — `channel_profile.json`. Todos os agentes o consultam antes de decidir.

```json
{
  "preferred_short_length": 24,
  "best_upload_time": "19:00",
  "thumbnail_style": "high contrast",
  "favorite_intro": "explosion",
  "zoom_intensity": 0.35,
  "caption_style": "animated",
  "music_volume": 0.18,
  "peak_retention_topics": ["perseguição", "explosão", "humor"],
  "low_performance_topics": ["missões longas", "tutoriais"],
  "best_ctr_thumbnail": "rosto + texto + fundo vermelho"
}
```

Esse arquivo é portátil. Trocou de computador? Basta copiá-lo — e o canal "volta a lembrar" de tudo.

### Arquitetura de cada agente

```
Modelo Base (open source) + Prompt + Ferramentas
  + Memória persistente + Channel Profile + Feedback acumulado
  = Agente especializado
```

Não existe fine-tuning individual. O que evolui é o **conhecimento sobre o canal** — não os modelos.

### Separação entre conhecimento e comportamento

O K Voice não precisa aprender português — ele já sabe. Precisa aprender velocidade, emoção, pausas e tom. O K Editor não precisa aprender a cortar vídeos — precisa descobrir quanto zoom usar, quanto dura um meme, quando colocar efeitos. Isso torna o sistema leve e eficiente.

---

## 15. O Problema do Cold Start

O diferencial de longo prazo do Kreator é o aprendizado acumulado por canal. Esse mesmo diferencial, porém, cria uma fragilidade no início que o projeto reconhece abertamente:

- Um canal novo tem **poucos vídeos** → pouca significância estatística (como ilustra o exemplo do K Scientist, com `n=8` e confiança baixa).
- O aprendizado **cruzado** entre canais precisa de **escala** → que precisa de produto funcionando → que precisa do loop de aprendizado. O ciclo se realimenta.

**Conclusão estratégica:** o aprendizado por canal **compõe com o tempo** e não pode ser a fonte de valor no dia 1. O valor inicial precisa vir de outro lugar. A estratégia tem quatro alavancas:

**1. Priors por nicho (bootstrap).** Em vez de começar "do zero", cada canal novo recebe defaults derivados de heurísticas públicas e benchmarks agregados do nicho (duração competitiva típica, horários comuns, padrões de thumbnail). Não é treinar em conteúdo de terceiros — é começar com um chute informado em vez de uma página em branco.

**2. Editing Profile do marketplace.** Um criador novo pode licenciar o **Editing Profile** de um editor experiente e obter "bons defaults" instantâneos, sem nenhum histórico próprio. Isso entrega valor imediato e desacopla o produto do aprendizado lento.

**3. Inferência bayesiana (PyMC).** Começa com o prior do nicho e atualiza por canal a cada novo vídeo. Com poucos dados, o sistema é honesto sobre a incerteza em vez de fingir certeza.

**4. Padrões federados com consentimento.** Conforme a base cresce (modestamente), padrões agregados entre canais do mesmo nicho — com consentimento explícito — aceleram a calibração de canais novos.

Nos primeiros meses, portanto, a proposta de valor do Kreator é concreta e imediata: **economia de tempo, bons defaults e workflows do marketplace** — e não "uma IA que já conhece seu canal". O conhecimento profundo por canal é uma recompensa que chega depois, e é justamente o que torna o produto difícil de abandonar no longo prazo.

---

## 16. Responsible Learning

### Princípio Fundamental

> **Consentimento antes de aprendizado. Colaboração antes de coleta.**

Nenhum conteúdo de terceiros é usado para treinar agentes sem autorização explícita. O sistema não depende de datasets obtidos por scraping indiscriminado.

Comportamento padrão:

> Todo conteúdo pertence ao criador e será usado exclusivamente para executar o serviço solicitado.

### Community Training Program

Contribuição totalmente opcional, sempre:

- **Explícita** — o criador decide conscientemente
- **Revogável** — pode ser retirada a qualquer momento
- **Transparente** — o uso dos dados é claramente descrito
- **Granular** — o criador escolhe exatamente o que compartilha (vídeos públicos, vídeos para pesquisa, apenas metadados, apenas timelines, apenas estatísticas, apenas projetos, ou nada)

### Especialistas como professores

Criadores experientes podem atuar como professores: um editor profissional disponibiliza projetos de edição; os agentes aprendem padrões a partir de exemplos fornecidos voluntariamente por especialistas reais.

### Programa de Contribuidores

Quem compartilha dados pode receber: acesso antecipado a novos agentes, descontos, remuneração proporcional e reconhecimento. O crescimento da inteligência acontece por **colaboração voluntária**, não por extração.

---

## 17. K Store — Marketplace

### Editing Profile como produto

Cada editor tem um estilo próprio. Hoje esse conhecimento existe só na cabeça do editor e é vendido como horas de trabalho. No Kreator, vira um ativo digital reutilizável e escalável: um único editor pode atender centenas de criadores. Em vez de vender horas, **o editor vende seu conhecimento**.

### Estratégia de lançamento por fases

O marketplace **não existe no lançamento**. É consequência do sucesso do produto — não o produto inicial.

- **Fase 1 — Ferramenta pessoal:** provar que o sistema funciona para um único criador.
- **Fase 2 — Editores parceiros:** convite a 10–15 editores conhecidos para criar os primeiros Editing Profiles.
- **Fase 3 — K Store fechada:** por convite, criadores selecionados testam os primeiros estilos.
- **Fase 4 — K Store pública:** aberta para qualquer editor cadastrar e qualquer criador escolher.

### Filosofia — Processos, não Pessoas

O marketplace não comercializa pessoas, identidades ou modelos treinados para imitá-las. Comercializa **K Workflows** — metodologias de produção e processos editoriais de profissionais reais.

**O que é um K Workflow:** regras de edição, lógica de seleção de cenas, ritmo de cortes, posicionamento de legendas, transições, intensidade de zoom, organização de timeline, critérios para memes, regras de efeitos sonoros, composição de thumbnails, estratégias de SEO e bibliotecas de ativos licenciados.

**O que NUNCA é comercializado:** voz sintetizada de criadores, rostos ou avatares sintéticos, vídeos gerados para imitar alguém, personalidades artificiais — qualquer recurso cujo objetivo seja reproduzir a identidade de um indivíduo.

> *O Kreator acredita que a identidade de um criador não deve se tornar um produto.*

### Modelos de remuneração

| Modelo | Descrição |
|---|---|
| Por vídeo processado | Remuneração a cada uso do K Workflow |
| Por hora de material | Baseado na duração do conteúdo editado |
| Assinatura mensal | Acesso ilimitado ao K Workflow por período |
| Licenciamento corporativo | Para equipes e empresas de volume alto |
| Participação no processamento | Percentual sobre o valor gerado |

> *O Kreator não licencia pessoas. Licencia processos criativos. A criatividade continua pertencendo aos seus autores.*

### Duas camadas: Workflow e Custom Agent

O K Store opera em duas camadas complementares. Na **camada base**, o que se licencia é o K Workflow — parâmetros e regras leves, executados pelos agentes-padrão do Kreator, sem que o editor precise hospedar nada. Na **camada avançada**, editores que desenvolveram inteligência própria podem disponibilizar **Custom Agents** hospedados em sua própria infraestrutura, federados pela Kreator Network. Em ambos os casos o conhecimento permanece com o autor; muda apenas o nível de sofisticação e de controle. Essa hierarquia, junto ao modelo de federação e à verificação criptográfica de cada item, está detalhada na [Seção 10](#10-edições-hospedagem-e-a-kreator-network).

---

## 18. MVP — Produto Inicial

O MVP é **intencionalmente pequeno**. O objetivo é provar o conceito central — não construir o sistema completo antes de validar o valor.

### Escopo do MVP

```
Gameplay gravado pelo criador
  ↓ Upload do vídeo
  ↓ K Clipper ranqueia os melhores momentos (humano aprova)
  ↓ K Editor edita com assets do usuário
  ↓ K Subtitle adiciona legendas
  ↓ K Thumbnail gera miniatura a partir de frames reais
  ↓ Upload para o YouTube
```

### O que o MVP exclui (lista explícita de "não agora")

- K Store / marketplace de editores
- K Scientist (testes A/B)
- K Strategy
- Clonagem de voz (K Voice modo 3)
- Narração automática
- Respostas automáticas a comentários
- Inteligência multirregional
- Grafo de conhecimento (Neo4j/GraphRAG)
- Qualquer IA generativa de imagem

Tudo isso pertence às Fases 2 e 3. No MVP, seriam distração.

### Critério de sucesso do MVP

> Se um criador grava um vídeo, faz upload e recebe um Short **que ele realmente postaria** — com no máximo uma aprovação de candidatos e zero edição manual — o MVP foi um sucesso.

O teste decisivo não é "o sistema rodou". É "**o output passa no critério editorial do criador?**".

Todo o valor do MVP está na **orquestração** — não nos modelos individualmente. A stack específica do MVP está no [Apêndice A](#apêndice-a--stack-técnica-e-infraestrutura).

---

## 19. Economia Unitária — Custo por Vídeo

A pergunta que precede qualquer estratégia de preço: **é possível processar um vídeo por menos do que será cobrado por ele?** Nenhum modelo de cobrança faz sentido sem essa resposta, e por isso a economia unitária é tratada como parte central do projeto.

### Modelo de custo (drivers principais)

O custo por vídeo é dominado por **GPU-tempo**. Os drivers, em ordem de peso:

1. **VLM (K Analyst)** — o mais caro; escala com a duração do vídeo.
2. **ASR (WhisperX)** — moderado; escala com a duração do áudio.
3. **Renderização (FFmpeg)** — CPU/GPU; escala com nº de outputs e efeitos.
4. **TTS (K Voice)** — opcional; só quando há narração.
5. **LLM de SEO/classificação** — barato; texto curto.
6. **Armazenamento + egress** — pequeno por vídeo, relevante em escala.

### Estimativa de referência

As estimativas a seguir constituem um modelo de referência, a ser substituído por medições reais durante o desenvolvimento. Servem para orientar a decisão de preço, não como números definitivos.

Cenário: **2h de gameplay → 5 Shorts + 1 highlight**, em GPU alugada na comunidade (RTX 4090 / L4 ≈ US$ 0,40–0,80/h).

| Etapa | GPU-tempo estimado | Custo estimado |
|---|---|---|
| K Analyst (VLM, amostragem de frames, janelas com overlap) | ~0,4–0,8 h | US$ 0,20–0,60 |
| K Subtitle (WhisperX large-v2) | ~0,1–0,2 h | US$ 0,05–0,15 |
| K Editor + K Motion (FFmpeg, render de 6 outputs) | ~0,2–0,5 h | US$ 0,10–0,40 |
| K Thumbnail (programático, leve) | ~0,02 h | < US$ 0,02 |
| K SEO / K Classifier (LLM texto) | ~0,02 h | < US$ 0,02 |
| Armazenamento + egress (por vídeo) | — | US$ 0,05–0,20 |
| **Total (sem narração)** | **~0,7–1,5 h GPU** | **≈ US$ 0,50–1,50** |

Com retries, overhead de orquestração e margem de segurança, um teto inicial prudente é **US$ 2–4 por vídeo de 2h** em infraestrutura alugada. Em hardware próprio (RTX 4090 amortizado + energia), o custo marginal cai, mas entra o custo fixo de capital e ociosidade.

### A regra de decisão

> **Custo por vídeo deve ficar confortavelmente abaixo do preço cobrado, com margem para suportar o "primeiro vídeo grátis".**

Se o primeiro vídeo é gratuito (ver [Seção 22](#22-creator-success-program)), cada criador novo custa ~US$ 0,50–4,00 de aquisição em compute. Isso é sustentável **se** a taxa de conversão para pagante for razoável. Exemplo de sanity check:

- Custo do vídeo grátis: ~US$ 2
- Conversão para pagante: 20%
- Custo de aquisição efetivo por pagante: ~US$ 10 em compute
- Preço por vídeo pago precisa cobrir isso + margem + custo do próprio processamento.

### Alavancas de redução de custo

- **Amostragem inteligente de frames** no VLM (não processar todos os frames) — maior alavanca isolada.
- **Quantização** (modelos 4-bit/8-bit) para caber em GPU menor.
- **Batching** de tarefas na fila (Redis) para maximizar ocupação da GPU.
- **CPU para o que dá** (Kokoro TTS, Pillow/OpenCV, bancos).
- **Cache** de análise por segmento (reuso entre Shorts do mesmo vídeo).

A medição real do custo de ponta a ponta de um lote de vídeos é uma das primeiras prioridades de engenharia, e seus resultados substituem as estimativas desta seção por números efetivos.

---

## 20. Riscos de Plataforma e Dependências de API

O Kreator opera sobre plataformas de terceiros, e parte significativa de sua operação depende delas. Mapear essas dependências e suas mitigações é essencial para a robustez do projeto.

### Risco 1 — Cota da YouTube Data API

A YouTube Data API v3 tem cota padrão (na ordem de ~10.000 unidades/dia por projeto) e **upload custa caro em unidades** — o que limita drasticamente uploads automatizados por projeto.

**O que NÃO fazer:** rotacionar API keys de um mesmo projeto para furar cota. Isso viola os termos e pode resultar em **suspensão do projeto** — um risco existencial que o Kreator evita por princípio de arquitetura.

**Arquitetura correta:**
- **OAuth por criador:** cada criador autoriza com a própria conta Google. A cota passa a ser **por criador**, não compartilhada — escala naturalmente com a base.
- **Solicitar aumento de cota** via processo oficial de auditoria/compliance do Google (leva semanas, exige revisão; planejar com antecedência).
- **Publicação semi-assistida** como fallback: o sistema prepara tudo (vídeo, thumbnail, metadados, agendamento) e o criador confirma o upload — reduz consumo de cota crítica e mantém o humano no controle.
- **Agendamento via `status.publishAt`**, sem automação de browser.

### Risco 2 — Outras plataformas

- **Instagram:** publicação automatizada exige Graph API com conta Business/Creator e tem limites próprios.
- **TikTok:** Content Posting API exige aprovação e tem restrições de uso.
- **Implicação:** o multi-plataforma do K Publisher é faseado — começa só com YouTube, adiciona outras conforme aprovação de API.

### Risco 3 — Concorrência nativa das plataformas

YouTube, TikTok e Instagram já oferecem (ou estão construindo) ferramentas nativas de geração de Shorts, legendas e edição. Isso pressiona a camada de "clipping". **Mitigação:** o Kreator não compete na feature isolada — compete na **camada de operação de canal** (memória, estratégia, marketplace, publicação multi-canal), que as plataformas não têm incentivo para construir.

### Risco 4 — Scraping para K Intelligence

Mudanças de layout, rate limits e ToS tornam scraping frágil. **Mitigação:** priorizar APIs oficiais, tratar scraping como complemento de baixa frequência e orçar manutenção contínua.

---

## 21. Análise Competitiva e Cunha de Diferenciação

### Os concorrentes reais já existem

Ferramentas como **Opus Clip, Vizard, Submagic, Klap e Descript** já fazem, hoje, a partir de footage real: detecção de momentos, corte em Shorts, reframe automático, legendas animadas e até thumbnails. "Cortar vídeo real automaticamente" **não é mais diferencial** — é commodity, e o Opus Clip em particular faz isso muito bem.

| Dimensão | Opus Clip / Vizard / Klap | Submagic | Descript | **Kreator** |
|---|---|---|---|---|
| Clipping de footage real | ✅ Forte | Parcial | ✅ | ✅ |
| Legendas animadas | ✅ | ✅ Forte | ✅ | ✅ |
| Memória por canal | ❌ | ❌ | ❌ | ✅ (acumulativa) |
| Estratégia de canal | ❌ | ❌ | ❌ | ✅ (K Strategy) |
| Publicação + gestão de canal | Parcial | ❌ | ❌ | ✅ (K Publisher) |
| Marketplace de processos editoriais | ❌ | ❌ | ❌ | ✅ (K Store) |
| Self-host / controle de dados | ❌ (SaaS fechado) | ❌ | ❌ | ✅ (stack open source) |
| Zero imagens geradas (compliance) | Varia | — | — | ✅ (princípio) |

### A cunha específica ("por que não o Opus Clip?")

A diferenciação **não pode** ser "não geramos imagem" sozinha — é fina demais, porque o Opus também corta vídeo real. A cunha real é a soma de quatro coisas que nenhum concorrente entrega junto:

1. **Sistema operacional, não ferramenta.** Opus Clip entrega clipes. O Kreator opera o canal: compreensão → edição → publicação → análise → estratégia → memória. É a diferença entre um app e um estúdio.

2. **Aprendizado acumulado por canal (moat temporal).** Cada vídeo torna o próximo melhor *para aquele canal específico*. Concorrentes SaaS tratam todo cliente igual. (Ver [Seção 15](#15-o-problema-do-cold-start) sobre por que isso compõe com o tempo.)

3. **K Store — marketplace de Editing Profile.** Um modelo de negócio que transforma o conhecimento de editores em ativo licenciável. Nenhum dos concorrentes tem isso — e é o que cria um ecossistema de dois lados (criadores + editores).

4. **Controle de dados e custo via stack open source / self-host.** Para criadores e estúdios que não querem entregar footage a um SaaS fechado, e para o próprio Kreator controlar custo unitário.

A qualidade do clipping é pré-requisito de entrada no mercado. O Kreator precisa primeiro *empatar* com os melhores cortadores automáticos em qualidade de corte, e então *vencer* na camada de sistema operacional — memória, estratégia, marketplace e operação de canal. Um corte inferior comprometeria todo o resto da proposta; por isso a paridade na qualidade do recorte é uma meta inegociável da primeira fase.

---

## 22. Creator Success Program

### Modelo baseado em desempenho

Criadores iniciantes não deveriam assumir risco financeiro antes de saber se o conteúdo tem potencial. Por isso:

> **O primeiro vídeo processado pelo Kreator é sempre gratuito.**

Funciona como demonstração e permite avaliar resultados sem compromisso. O custo desse primeiro vídeo é uma decisão consciente de aquisição de cliente, dimensionada no modelo de [Economia Unitária](#19-economia-unitária--custo-por-vídeo).

### Benchmark Inteligente

Sucesso não é um número fixo de views. Cada nicho tem métricas próprias. Antes da publicação, os agentes constroem um modelo de referência para aquele tipo de conteúdo (nicho, duração, formato, plataforma, tendências, comportamento do público, desempenho de conteúdos semelhantes recentes). Cada vídeo é comparado só com conteúdos genuinamente semelhantes.

### Creator Success Score

Antes da publicação, gera um relatório com alcance esperado, faixa provável de views, potencial de engajamento, retenção estimada e competitividade no nicho. Depois, compara o desempenho real com o benchmark. O **Creator Success Score** é uma métrica proprietária de desempenho *relativo ao mercado do nicho* — não absoluto.

### Modelo de cobrança

O primeiro vídeo é grátis. Se o Score indicar que atingiu/superou o esperado para o nicho, o criador contrata os serviços para os próximos vídeos.

> *O Kreator demonstra seu valor antes de cobrar por ele. Cresce apenas quando seus criadores também crescem.*

---

## 23. Roadmap

### Fase 1 — Integrate, don't train
**Objetivo:** validar a orquestração de modelos existentes.
- MVP com gameplay e Shorts
- Pipeline de análise e edição básica
- Channel Profile inicial
- Publicação no YouTube (OAuth por criador)
- **Medição de custo unitário real**

Nenhum treinamento. Apenas integração.

### Fase 2 — Specialize, don't replace
**Objetivo:** aprofundar a especialização por canal.
- K Memory completo
- K Scientist com testes A/B
- Extração automática de Editing Profile
- K Store fechada com editores parceiros
- Outros nichos (vlog, educação, podcast)

### Fase 3 — Train only where it creates unique value
**Objetivo:** modelos próprios apenas onde há vantagem competitiva clara.
- K Strategy com histórico profundo
- K Store pública
- Community Research Program ativo
- Modelos especializados por nicho

A stack recomendada para cada fase está no [Apêndice A](#apêndice-a--stack-técnica-e-infraestrutura).

---

## 24. Evolução para Modelos Próprios

### Filosofia de três fases

> **Não treine o que já existe. Especialize o que já funciona. Desenvolva do zero apenas onde nenhuma alternativa serve.**

Evita o erro mais comum em startups de IA: gastar recursos escassos treinando modelos antes de validar o produto. Um modelo multimodal do zero pode custar dezenas de milhões e exigir equipe de pesquisa dedicada. Integrar modelos open source maduros e concentrar a inovação na orquestração é realizável com uma equipe pequena.

### Fase 1 — Integrate (presente)
O Kreator usa exclusivamente modelos open source. O valor não está nos modelos — está na arquitetura que os coordena, na memória que aprende e no Channel Profile que preserva a identidade do criador. Se surgir um VLM 3× melhor, troca-se um componente sem reescrever o pipeline. É Modular Intelligence na prática.

### Fase 2 — Specialize (médio prazo)
A especialização acontece por configuração e memória — não por treinamento. O `channel_profile.json` codifica preferências de centenas de vídeos; o feedback ajusta parâmetros; o K Scientist identifica combinações vencedoras; a extração de Editing Profile transforma histórico de edições em parâmetros mensuráveis. Nenhuma GPU de treinamento. O sistema aprende pelo uso.

### Fase 3 — Train (longo prazo)
Após anos em escala, o Kreator terá algo que nenhum laboratório externo replica: **dados reais de produção autorizados pela comunidade**. Com isso, é possível treinar modelos de domínio específico:

- **Classificador de viralidade por nicho**
- **Preditor de CTR de thumbnail** (sobre impressões/cliques reais)
- **Detector de highlights por título** (clips anotados pelos próprios criadores)
- **Ranqueador de viralidade calibrado por canal**

### O que nunca será desenvolvido internamente
LLMs de propósito geral, VLMs genéricos ou TTS de propósito geral. Essas categorias têm alternativas open source excelentes e financiadas por bilhões. O foco do desenvolvimento próprio é **modelos de domínio específico** que os genéricos não resolvem bem.

### Critério de decisão
> Um modelo customizado só faz sentido quando a plataforma tem dados suficientes para treiná-lo com qualidade superior à alternativa open source, e quando essa superioridade gera vantagem competitiva mensurável. Antes disso, integrar é sempre a escolha certa.

---

## 25. Visão de Longo Prazo

O objetivo do Kreator não é criar vídeos automaticamente. É criar a **infraestrutura** que permite que milhões de criadores produzam conteúdo autêntico com a eficiência de um grande estúdio, sem perder sua identidade.

O ativo principal deixa de ser apenas os vídeos publicados. Passa a ser o **conhecimento acumulado pelo sistema**: memória persistente sobre público, estilo, formatos que funcionam, horários ideais, padrões de retenção e estratégias de crescimento. Esse conhecimento torna cada novo vídeo potencialmente melhor que o anterior.

### Três perfis de usuários

- **Criadores** — produzem conteúdo e usam os K Agents para automatizar a operação do canal.
- **Editores** — transformam seu estilo em K Workflows reutilizáveis, gerando receita recorrente via K Store.
- **Desenvolvedores** — criam novos agentes, integrações e plugins via **K SDK**, expandindo a plataforma.

### A escala do futuro

Imagine a plataforma daqui a cinco anos: 50 mil criadores ativos, 8 milhões de vídeos processados, 5 mil editores na K Store, 500 milhões de edições. Com essa base, torna-se possível desenvolver modelos especializados com uma vantagem única: todos os dados cedidos voluntariamente por uma comunidade que acredita no projeto.

---

## 26. Diferenciação Competitiva

### O que o Kreator não é
- Não é um gerador de vídeos com IA
- Não é um canal "faceless"
- Não é um substituto para criadores humanos
- Não é só mais uma ferramenta de edição automática
- Não usa IA generativa para criar imagens, thumbnails ou elementos visuais

### Limitações assumidas

O Kreator é honesto sobre o que a automação não faz. A IA que sustenta os K Agents é **probabilística**: ela erra, classifica com incerteza e não compreende intenção artística. Por isso o sistema é deliberadamente **assistivo, não autônomo** — o criador aprova candidatos, ajusta perfis e mantém a palavra final, sobretudo nas decisões editoriais subjetivas como a escolha do melhor momento. Os parâmetros de um Editing Profile são estatísticas mensuráveis, não a "alma" de um editor; e prompts ou metodologias não são, isoladamente, segredos protegíveis — o valor defensável está na execução, na memória acumulada e na infraestrutura, não em um texto de prompt. Assumir esses limites explicitamente é o que torna as promessas do restante do documento críveis.

### O que o Kreator é
Um sistema operacional para a economia criativa, onde a IA funciona como equipe especializada a serviço de criadores e editores reais, preservando a autoria humana e transformando conhecimento criativo em ativo escalável.

### Posicionamento

| Dimensão | IA generativa | Automações de canal | Kreator |
|---|---|---|---|
| Quem cria o conteúdo | A IA | A IA | O humano |
| Origem das imagens | Difusão | Geradas ou scraped | Frames reais |
| Thumbnail | IA do zero | IA cria/reutiliza | Edição programática de frames reais |
| Autenticidade | Sintética | Parcial | 100% autêntica |
| Conformidade YouTube | Risco | Risco | Nativa |
| Identidade do criador | Ausente | Fraca | Preservada |
| Aprendizado por canal | Não | Genérico | Específico e acumulativo |
| Modelo de negócio do editor | Substituído | Ignorado | Escalado e remunerado |

### Por que é difícil de copiar
Um concorrente pode usar os mesmos modelos open source. O que **não se copia facilmente**:
- Uma arquitetura de agentes bem projetada
- Memória persistente calibrada por canal
- Editing Profiles extraídos de centenas de projetos reais
- Um ecossistema onde criadores e editores colaboram com consentimento
- Meses ou anos de aprendizado acumulado sobre um canal
- A decisão filosófica de não usar IA generativa para imagens — e o trust que isso constrói

> *Agentes de imagem = editores de Photoshop. Não geradores de imagem.*

---

## 27. Premissas Críticas e Plano de Validação

O Kreator se apoia em um conjunto de premissas que precisam ser comprovadas empiricamente antes de qualquer investimento em escala. Esta seção lista essas premissas e os experimentos que as validam, em ordem de prioridade. O objetivo da fase inicial é provar que o loop central de produção funciona ponta a ponta — da gravação ao Short publicável.

### E1 — Qualidade da curadoria de momentos
**Premissa:** o K Clipper escolhe momentos que um criador realmente publicaria.
**Método:** processar 10 gameplays reais, gerar o ranking de candidatos e comparar com as escolhas de um editor humano sobre o mesmo material, medindo a taxa de concordância.
**Critério de sucesso:** concordância majoritária entre o ranking do sistema e o editor humano. Esta é a premissa de maior impacto do produto e a primeira a ser validada.

### E2 — Custo unitário real
**Premissa:** é possível processar um vídeo por menos do que será cobrado por ele.
**Método:** medir o custo de ponta a ponta de um lote de vídeos e preencher o modelo de [Economia Unitária](#19-economia-unitária--custo-por-vídeo) com números reais.
**Critério de sucesso:** custo por vídeo confortavelmente abaixo do preço, com folga para suportar o primeiro vídeo gratuito.

### E3 — Coerência do "Zero Generated Images"
**Premissa:** o pipeline programático de thumbnail entrega qualidade suficiente sem nenhuma IA generativa.
**Método:** gerar thumbnails programáticas para 20 vídeos e comparar CTR e qualidade percebida com thumbnails feitas manualmente.
**Critério de sucesso:** qualidade aceitável que sustente o princípio na prática.

### E4 — Realidade das cotas de API
**Premissa:** é possível publicar automaticamente dentro dos termos do YouTube.
**Método:** validar o fluxo OAuth por criador e medir o consumo de cota por upload real.
**Critério de sucesso:** cota suficiente para a operação prevista; caso contrário, adoção do modelo de publicação semi-assistida.

### E5 — Cunha contra concorrentes diretos
**Premissa:** existe uma razão clara para um criador escolher o Kreator em vez de um cortador automático já estabelecido.
**Método:** articular e validar com criadores reais a proposta de diferenciação descrita na [Análise Competitiva](#21-análise-competitiva-e-cunha-de-diferenciação).
**Critério de sucesso:** criadores reconhecem e valorizam a camada de plataforma como motivo de escolha.

As três premissas de maior peso para o futuro do projeto são a qualidade da curadoria (E1), o custo unitário (E2) e a cunha competitiva (E5). São essas que concentram a prioridade de validação na primeira fase.

---

## 28. Identidade da Marca

A nomenclatura segue um padrão consistente:

| Conceito | Nome |
|---|---|
| Plataforma | **Kreator** |
| Agentes | **K Agents** |
| Marketplace | **K Store** (ou K Marketplace) |
| Memória | **K Memory** |
| Inteligência de Mercado | **K Intelligence** |
| Análises | **K Analytics** |
| Fluxos / Metodologias | **K Workflows** |
| Bibliotecas de ativos | **K Library** |
| Desenvolvimento | **K SDK** |

### A ideia de identidade (estilo GPTs)

Assim como a OpenAI fez com os GPTs, os agentes são tratados como **membros de uma equipe**, não funcionalidades de software. As pessoas não dizem "abra o editor" — elas dizem:

> *"Chame o K Editor."*
> *"Peça ao K Analyst para analisar esse vídeo."*
> *"O K Strategy recomendou que eu grave um vídeo sobre programação."*

### Slogan e filosofia

- **Filosofia:** *Human Creativity. AI Operations.*
- **Slogan da marca:** *Kreator — The Operating System for Human Creativity.*
- **Variante (ênfase em operação):** *Kreator — The Operating System for Content Creators.*

No fim, o Kreator não é apenas um editor nem apenas uma plataforma de IA. É a infraestrutura operacional que conecta criadores humanos a uma equipe de **K Agents**, cada um especializado em uma etapa do processo criativo — uma identidade de marca coesa, escalável e fácil de expandir conforme novos agentes e funcionalidades surgirem.

## Apêndice A — Stack Técnica e Infraestrutura

Referência técnica consolidada. Não é necessária para entender a proposta de produto — serve a quem vai implementar ou avaliar a arquitetura. A especificação interna do runtime (Signal Layer, Planner, execução incremental, contratos) está no documento complementar **Kreator Runtime**.

### Stack Tecnológico Recomendado (2026)

| Camada | Ferramenta Principal | Alternativa | Licença |
|---|---|---|---|
| Orquestração de agentes | **LangGraph** | CrewAI (protótipos) | MIT |
| Compreensão de vídeo (VLM) | **Qwen2.5-VL / Qwen3-VL 7B** | InternVL3 | Apache-2.0 |
| Detecção de cenas | **PySceneDetect + YOLO v8** | OpenCV puro | BSD-3 / AGPL |
| Detecção de highlights | **AI-Youtube-Shorts-Generator** | Crispy (FPS/MOBA) | MIT |
| Motor de corte | **auto-editor + FFmpeg** | MoviePy | Unlicense / LGPL |
| Narração / TTS | **Fish Speech** / **XTTS v2** | Kokoro-82M (CPU) | Apache-2.0 / CPML |
| Legendas / ASR | **WhisperX** | faster-whisper puro | BSD-2 |
| Thumbnail — seleção de frame | **VLM + CLIP** | PySceneDetect | Apache-2.0 / MIT |
| Thumbnail — detecção facial | **MediaPipe FaceMesh** | OpenCV Haar Cascade | Apache-2.0 |
| Thumbnail — edição programática | **Pillow + OpenCV + rembg** | ImageMagick (Wand) | MIT / Apache-2.0 |
| SEO / metadados | **LLM local (Qwen3 / Llama 3) + DSPy** | Prompt direto via Ollama | MIT |
| Publicação | **YouTube Data API v3 + youtool** | google-api-python-client | Apache-2.0 |
| Analytics | **YouTube Analytics API + Grafana** | Metabase / Superset | AGPL |
| Memória de agente | **Mem0 + Letta** | Zep / Graphiti | Apache-2.0 |
| Banco vetorial | **pgvector → Qdrant** | Milvus | PostgreSQL / Apache-2.0 |
| Grafo de conhecimento | **Neo4j Community + GraphRAG** | pgvector puro | GPLv3 / MIT |
| Observabilidade e experimentos | **Arize Phoenix + statsmodels** | MLflow | MIT / BSD-3 |
| Pesquisa de tendências | **browser-use + Crawl4AI** | Scrapy + Playwright | MIT / Apache-2.0 |
| Análise de comentários | **BERTopic + HF Sentiment** | KeyBERT | MIT |
| Fila de mensagens | **Redis Streams** | RabbitMQ / Kafka | BSD-3 |
| Armazenamento de objetos | **MinIO** (S3-compatível) | NFS local | AGPL |
| Banco relacional | **PostgreSQL** | — | PostgreSQL License |
| Inferência LLM local | **vLLM ou Ollama** | TGI | Apache-2.0 |
| Conteinerização | **Docker + Docker Compose** | Kubernetes (fase escalável) | Apache-2.0 |

### Requisitos de Hardware (single-node)

| Componente | Mínimo | Recomendado |
|---|---|---|
| GPU principal | 1× RTX 4090 (24 GB) | 1× RTX 4090 (VLM + LLM) |
| GPU secundária | — | 1× RTX 4080 16 GB (TTS em paralelo) |
| RAM | 32 GB DDR5 | 64 GB DDR5 |
| CPU | i7-14700K 12 cores | Ryzen 9 7950X 16 cores |
| Armazenamento | 1 TB NVMe (3.500 MB/s) | 4 TB NVMe Gen4 (7.000 MB/s) |

### Stack do MVP

| Componente | Ferramenta | Licença |
|---|---|---|
| Orquestração | LangGraph | MIT |
| Compreensão de vídeo | Qwen2.5-VL-7B via vLLM | Apache-2.0 |
| Detecção de highlights | AI-Youtube-Shorts-Generator | MIT |
| Corte e edição | auto-editor + FFmpeg | Unlicense / LGPL |
| Legendas | WhisperX | BSD-2 |
| Narração (opcional) | Kokoro-82M via CPU | Apache-2.0 |
| Thumbnail | Pillow + OpenCV + rembg + MediaPipe (frames reais, **zero IA generativa**) | MIT / Apache-2.0 |
| SEO | Qwen3-14B via Ollama + JSON | Apache-2.0 |
| Publicação | YouTube Data API v3 | Apache-2.0 |
| Armazenamento | MinIO (S3) | AGPL |
| Banco de dados | PostgreSQL + pgvector | PostgreSQL License |
| Fila | Redis Streams | BSD-3 |
| Deploy | Docker Compose (single-node) | Apache-2.0 |

### Stack por fase do roadmap

- **Fase 1 — Integrate:** LangGraph (checkpointing via PostgreSQL); Qwen2.5-VL-7B via vLLM; PySceneDetect; auto-editor + FFmpeg; WhisperX; Pillow + OpenCV + rembg + MediaPipe (thumbnails 100% programáticas); Qwen3 via Ollama; pgvector; Docker Compose; Redis Streams.
- **Fase 2 — Specialize:** Mem0 + Letta; migração pgvector → Qdrant; Neo4j + GraphRAG; Arize Phoenix + statsmodels/scipy; Prophet + AutoGluon; Fish Speech / XTTS v2; multi-node com workers GPU dedicados; Grafana + Prometheus.
- **Fase 3 — Train:** Kubernetes; Kafka; pipelines de anotação; MLflow; CUDA para fine-tuning; dados anotados com consentimento explícito.

---

*Kreator — Human Creativity. AI Operations.*

*Documento criado por Johnny Kestler (João Vitor Perazzolo) em 27 de junho de 2026.*
