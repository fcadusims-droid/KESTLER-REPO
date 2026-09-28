# NarrativeLean

Verificadores para documentos narrativos: timeline e idades, regras do mundo,
atributos, regra × regra, referências sem definição. Implementação do
documento de design *NarrativeLean v3*, com as correções descritas em
[O que mudou em relação ao v3](#o-que-mudou-em-relação-ao-v3).

**Pasta privada.** Nada aqui é publicado: o site só constrói os `.md` da raiz
do repositório (`srcExclude` em `.vitepress/config.mts` exclui toda subpasta).
Nenhum arquivo fora desta pasta menciona o sistema. As obras não são copiadas
nem movidas; o sistema lê os `.md` da raiz onde eles já estão.

**Sem API paga.** O código não chama modelo nenhum. Quem lê linguagem é um
*operador* externo: `claude -p` (Claude Code no plano do autor), um modelo
aberto local (`ollama run ...`), ou um Claude Code interativo seguindo o
[CLAUDE.md](CLAUDE.md). Todo o resto é Python determinístico.

---

## Instalação

Python 3.11+ e PyYAML.

```bash
pip install -r narrativelean/requirements.txt
python narrativelean/nl.py validar          # confere configuração, canon, contratos
python -m unittest discover -s narrativelean/tests/verifiers   # 57 testes
```

Todos os comandos rodam da raiz do repositório.

## Como funciona, em uma tela

```
obra.md ──segmentar──▶ unidades ──preparar──▶ work/pendentes/*.md
                                                   │  um processo por pacote
                                                   ▼  (claude -p | ollama | manual)
                                             work/respostas/*
                                                   │
                        ingerir: a citação existe mesmo no texto?  ──não──▶ rejeitado (contado)
                                                   │ sim; linhas calculadas pelo código
                                                   ▼
                                  cache/ ──▶ facts/v1/*.yaml ──verificar──▶ reports/v1/relatorio.md
                                                                   ▲
                                          canon/*.yaml (só o que o autor aprovou vale como autoridade)
```

- **Unidade**: seção (título `#`…`###`), cena (`***`, `---`) ou cena de roteiro
  (`INT.`/`EXT.`), conforme o tipo do documento.
- **Fato**: `sujeito · predicado · objeto`, com `tempo`, `modo` e uma
  `citacao` literal. O vocabulário de predicados é fechado
  (`schema/predicados.yaml`); o que não cabe vira `predicado_livre`, que o
  relatório lista para o autor decidir.
- **Modo**: `narrador`, `fala`, `pensamento`, `documento_interno`, `sonho`,
  `hipotetico`. Só `narrador` restringe o mundo; o resto é o que alguém diz,
  pensa ou escreveu. ("O governo tem certeza de que o matou em 2016" não é uma
  morte em 2016.)
- **Níveis**: `ERROR` só quando a autoridade é canon aprovado e STRICT, toda a
  evidência é do narrador e nenhuma extração tem confiança baixa. Contradição
  interna vira `WARNING` com pergunta ao autor. Lentes semânticas nunca dão
  ERROR; método próprio (sem fonte publicada) no máximo `SUGGESTION`.

## Uso do dia a dia

```bash
# 1. Declarar o documento (opt-in: só o que está em doctypes.yaml é verificado)
python narrativelean/nl.py classificar --todos       # palpite; confiança baixa = declare à mão

# 2. Extrair
python narrativelean/nl.py extrair preparar           # só unidades novas ou mudadas (+ vizinhas)
python narrativelean/nl.py extrair rodar --comando "claude -p"
python narrativelean/nl.py extrair ingerir
python narrativelean/nl.py extrair status

# 3. Verificar
python narrativelean/nl.py verificar                  # reports/v1/relatorio.md e .json

# 4. Tratar o relatório
python narrativelean/nl.py suprimir TL-001 --motivo "o epíteto 'doze anos' é intencional"
python narrativelean/nl.py advogado preparar          # segunda leitura, contrária, dos diagnósticos
python narrativelean/nl.py extrair rodar --fila advogado --comando "claude -p"
python narrativelean/nl.py advogado ingerir
```

### O operador

`extrair rodar` entrega cada pacote, pela entrada padrão, a um processo novo,
numa pasta temporária vazia (fora do repositório: o operador só sabe o que
está no pacote). A saída inteira vira a resposta. Se o comando tiver
`{arquivo}`, o caminho do pacote vai no lugar.

| Operador | Comando |
|---|---|
| Claude Code, não interativo | `--comando "claude -p"` |
| Modelo aberto, local | `--comando "ollama run qwen2.5:14b"` |
| llama.cpp | `--comando "llama-cli -m modelo.gguf -f {arquivo}"` |
| Manual | abrir `work/pendentes/X.md`, responder em `work/respostas/X.yaml` |

Opções: `--limite N` (só N pacotes), `--tempo 900` (segundos por pacote),
`--fila principal|golden|advogado|baseline|retrotraducao`.

Com `claude -p`, vale desligar as ferramentas do extrator se a sua versão
aceitar (confira `claude --help`): ele só precisa ler o pacote.

### O cache

A chave de uma extração é o hash do texto da unidade + versão do schema +
hash do texto do prompt. Mudou o prompt, tudo volta para o operador; mudou uma
unidade, só ela e as vizinhas voltam. Um predicado novo no vocabulário **não**
invalida o cache: gera um pacote complementar só com o predicado novo. Fatos
guardam a posição relativa à unidade e são relocalizados quando linhas acima
mudam.

## Canon e autoridade

`canon/characters.yaml`, `timeline.yaml`, `world_rules.yaml`,
`entidades.yaml` (hierarquia é_um, instâncias, `termos_conhecidos`),
`locations.yaml`, `intencoes.yaml` (escolhas deliberadas que não são defeito).

Cada arquivo declara `rigidez_padrao: STRICT | FLEXIBLE`; o sistema nunca
adivinha. Um item com `proposto_por: claude` **não é autoridade**: vale como
FLEXIBLE até o autor aprovar. Regras cuja forma (`aplica_a`, `exige`,
`proibido`, `excecoes`) foi traduzida pelo Claude levam
`formalizacao: {proposta_por: claude}` e só valem depois que o autor confere
as consequências:

```bash
python narrativelean/nl.py regras bateria R-MAGIA-03    # casos gerados: quem a regra pega e quem ela solta
python narrativelean/nl.py regras retrotraduzir preparar  # outro operador lê SÓ a forma e diz o que ela significa
python narrativelean/nl.py regras aprovar R-MAGIA-03    # SÓ O AUTOR roda isto
python narrativelean/nl.py canon aprovar characters "Anselm Reiter"   # SÓ O AUTOR roda isto
```

A aprovação guarda o hash da forma. Mudou a forma, a aprovação cai.

O canon que está aqui hoje (Anselm Reiter e quatro eventos de *Lattice Zero*)
foi **proposto pelo Claude** para o piloto e não está aprovado. É por isso que
os diagnósticos contra ele saem como WARNING e não ERROR.

---

## Validação real (Fase 1)

O sistema está pronto para ser medido. Medir exige material que só o autor
pode produzir: se o Claude planta os erros e escreve o gabarito, o recall sai
otimista, porque ele planta o tipo de erro que ele mesmo detecta.
`plantar status` e `golden pontuar` separam as notas por origem.

Critérios de parada, definidos **antes** (em `project.yaml`), sempre contra o
**limite inferior** do IC 95% de Wilson, nunca contra o valor observado:

| Medida | Mínimo (LI) | Na prática, com 60 erros |
|---|---|---|
| Recall em erros plantados | 0,80 | achar ≥ 55 de 60 |
| Recall de extração (golden) | 0,80 | |
| Precisão de extração (golden) | 0,80 | |
| Erros plantados | ≥ 60, com ≥ 30% difíceis | |

### Passo a passo

**1. Tipos dos documentos.** Rode `classificar --todos`, confira e declare em
`doctypes.yaml` as obras que entram. O piloto (`lattice_zero.md`) está como
`biblia` por leitura do Claude; confirme ou troque.

**2. Canon.** Revise `canon/characters.yaml` e `canon/timeline.yaml`. O que
estiver certo: `canon aprovar`. Acrescente personagens, datas e regras que
você considera fixos. Sem canon aprovado, o sistema só acha contradições
internas (WARNING).

**3. Golden set de extração (~30 itens).** Um item por arquivo em
`tests/golden_extraction/`, no formato de `_modelo.yaml`: um trecho curto, os
fatos que um bom extrator tiraria dele e os que ele não pode tirar (a fala
mentirosa registrada como fato do mundo). Pelo menos 30% difíceis: tempo
relativo, informação distante, implícita, herança de classe, modo ambíguo.

```bash
python narrativelean/nl.py golden preparar
python narrativelean/nl.py extrair rodar --fila golden --comando "claude -p"
python narrativelean/nl.py golden pontuar
```

Mede o prompt de produção, não um prompt de teste. Se o recall não passa, o
problema é a extração, e nenhum verificador compensa: pare e ajuste o prompt
(novo arquivo `prompts/extrair_aberta_v2.md` e troca em `project.yaml`).

**4. Erros plantados (≥ 60).** Em `tests/seeded_errors/<nome>/plantio.yaml`
(veja `lattice-zero/plantio.yaml`): cada erro troca um trecho `localizar`
(único no original) por `substituir`, com `categoria`, `dificuldade` e
`origem: autor`.

```bash
python narrativelean/nl.py plantar status <nome>     # conta, cota de difíceis, origem
python narrativelean/nl.py plantar aplicar <nome>    # gera obra_plantada.md + gabarito
# declare a cópia em doctypes.yaml com experimento: true
python narrativelean/nl.py extrair preparar narrativelean/tests/seeded_errors/<nome>/obra_plantada.md
python narrativelean/nl.py extrair rodar --comando "claude -p"
python narrativelean/nl.py extrair ingerir
python narrativelean/nl.py verificar --documentos narrativelean/tests/seeded_errors/<nome>/obra_plantada.md
python narrativelean/nl.py plantar pontuar <nome>
```

A cópia fica sempre dentro desta pasta; nunca na raiz, onde o site a
publicaria.

**5. Gabarito por pooling** (recall numa obra real, sem erros plantados). Veja
`tests/gabarito/README.md`: amostra lida à mão + pipeline + baseline, o autor
rotula os candidatos, `gabarito pontuar` compara as três fontes.

**6. Baseline.** Um modelo lendo a obra inteira de uma vez, com o mesmo
operador (`baseline preparar|ingerir`). Se ele acha o mesmo que o pipeline, o
pipeline não se paga.

**7. Decisão.** Tudo passou: próxima fase (as lentes semânticas, na ordem de
`lenses.yaml`). Algo deu `PARE`: o relatório diz qual medida, e o conserto vem
antes de qualquer coisa nova.

---

## O que está implementado

| Parte | Estado |
|---|---|
| Segmentação por tipo, classificador conservador, `doctypes.yaml` | pronto |
| Pacotes, operador (um processo por pacote), ingestão | pronto |
| Ancoragem mecânica da citação; linhas calculadas pelo código | pronto |
| Extração aberta + dirigida (Q-TEMPO + uma pergunta por regra STRICT), divergências | pronto |
| Cache por unidade, pacotes complementares, relocalização, vizinhas, estabilidade | pronto |
| Timeline e idades: janela do aniversário, antes de nascer / depois de morrer | pronto |
| Rede temporal (tempo relativo, ciclos negativos, conjunto mínimo em conflito) | pronto |
| Regras: hierarquia é_um, exceções, qualificador ausente = lacuna | pronto |
| Regra × regra, bateria de consequências, retrotradução | pronto |
| Atributos funcionais contraditórios | pronto |
| Referência sem definição (bíblias, método próprio → SUGGESTION) | pronto |
| Relatório (formato da seção 7), supressões que expiram quando o trecho muda | pronto |
| Advogado do diabo (roteamento determinístico, não apaga, não sobe nível) | pronto |
| Contratos das 13 lentes, validador, `lens_conflicts.yaml` gerado | pronto |
| Golden set, erros plantados, pooling, baseline, Wilson, critérios de parada | pronto |

### Adiado de propósito

O próprio v3 congela o desenvolvimento até a Fase 1 passar (seção 11). Ficou
fora, esperando a medição:

- **Lentes semânticas em execução** (voz, arco, setup/payoff, ritmo…): só os
  contratos existem. Cada uma entra depois, uma de cada vez, com teste de
  violação intencional (o validador de contratos exige).
- **Perfis derivados e leave-one-out**, checagem de não-criação, **laço de
  edição** em branches, fluxo de conteúdo novo (briefings/direções).
- **Geografia**, conhecimento de personagem, regressão de canon, verificação
  por estado para `ramificado`, cruzamento bíblia-promovida × prosa.

---

## O que mudou em relação ao v3

Problemas encontrados no documento de design e o que foi feito:

1. **A citação nunca era conferida.** O v3 pede "verifique: a citação
   sustenta o fato?", mas não checa se ela existe. Modelo inventa citação e
   número de linha com a mesma fluência com que acerta. → Ancoragem mecânica
   antes de tudo (`grounding.py`); citação não achada = fato rejeitado e
   contado; a linha vem do código.
2. **A conta de idade ignora o aniversário.** `nascimento + idade = ano` dá
   ERROR falso para quem nasceu em 1987 e tem 20 anos em 2008. → Janela
   `{ano − idade − 1, ano − idade}`; exata só com datas completas.
3. **O cache se contradiz.** A chave incluía a versão do vocabulário, e o
   texto dizia que um predicado novo não força re-extração total. → A chave
   não leva o vocabulário; cada entrada registra os predicados cobertos e
   predicado novo gera pacote complementar. O hash do *texto* do prompt entra
   na chave (editar o prompt sem trocar a versão não passa despercebido).
4. **"Sessões separadas" não tinha como ser garantido.** → Um processo por
   pacote, numa pasta vazia fora do repositório.
5. **Seeded errors e golden set feitos por quem é medido.** → Harness com
   `origem` em cada item, notas separadas por origem, e `plantar status`
   recusando declarar pronto sem erros do autor.
6. **Rigidez padrão não definida.** → `rigidez_padrao` obrigatório em cada
   arquivo de canon; o validador acusa se faltar.
7. **Canon escrito pelo Claude virava autoridade.** → `proposto_por: claude`
   e `formalizacao` com hash de aprovação; nada disso gera ERROR até o autor
   aprovar. Vale para todos os verificadores formais, não só regras.
8. **Propriedades exigidas por regras não tinham lugar no fato.** (`exige:
   {ancora: true}`) → Campo `qualificadores`; qualificador ausente vira
   *lacuna* (o texto não diz), não violação.
9. **Âncoras relativas entre unidades são impossíveis para um operador
   isolado.** → Relativo só a algo da mesma unidade ou a evento do canon; o
   resto fica *indeterminado* e é listado, nunca vira ERROR.
10. **Classificação com confiança média é o pior caso** (erra com cara de
    certa). → Classificador conservador: alta só com evidência declarada e
    margem; baixa = o autor declara, e o documento não roda até isso.
11. **Supressão sem hash do trecho nunca expira.** → A supressão guarda o
    hash do trecho e cai quando ele muda.
12. **Unidade sem extração parecia "sem problemas".** → O relatório lista
    unidades não extraídas como NÃO verificadas.
13. **Só fatos do narrador restringem o mundo.** Fala, pensamento e documento
    interno aparecem como evidência, nunca como restrição.
14. **Os números de IC do v3 batem com Wilson** (59/60 → LI ≥ 0,90; 55/60 → LI
    ≥ 0,80). Viraram testes.
15. **O corpus é, na maioria, bíblia**, não prosa. → Referência sem definição
    (a lente mais útil para bíblia) veio antes das lentes de prosa;
    negrito conta como definição (calibrado no piloto: 5 de 7 falsos
    positivos eram termos em negrito).

## Piloto de fumaça (Fase 0)

Feito pelo Claude, com o Claude como operador, na mesma sessão. Serve para
provar que o caminho funciona de ponta a ponta. **Não mede nada**: aberta e
dirigida tiveram o mesmo leitor, e os erros foram plantados por quem detecta.

Os relatórios ficaram em `reports/piloto-fase0/`. O cache e os fatos do piloto
**não** foram versionados de propósito: a chave do cache seria a mesma, e a
primeira rodada real reaproveitaria as extrações do teste de fumaça em vez de
chamar o operador de verdade. A primeira rodada real extrai tudo do zero.

- `lattice_zero.md`: 23 unidades, 46 pacotes, 48 fatos, 0 citações
  rejeitadas. Modos: 44 narrador, 2 documento interno, 1 pensamento, 1 fala.
  As duas "mortes" de Reiter em 2016 (notícia e crença do governo)
  corretamente **não** contaram como morte.
- Relatório (`reports/piloto-fase0/relatorio.md`): 1 WARNING — o sucessor tem "doze
  anos" em 2034 e ainda "doze anos" quatro anos depois de 2037; pode ser
  epíteto intencional, e é por isso que é pergunta, não erro. 1 SUGGESTION —
  "United States" nunca definido (nome real: cabe em `termos_conhecidos`).
- Uma possível inconsistência que o sistema **não** pega: "There are
  seventy-four carriers" (l. 349) depois de quatro portadores mortos
  (l. 323). Pode ser contagem histórica; de todo modo, contagens não são
  verificadas. (A conta das doses fecha: 211 = 74 + 9 + 6 + 14 + 108.)
- Erros plantados (6, `origem: claude`): 4 achados (IC 95% 0,30–0,90 →
  `PARE`, como deveria com n = 6). Perdidos: geração ligada ao Bloom
  (a extração não fez a ligação — teto da extração) e um erro implícito.
  Só as unidades mudadas e as vizinhas voltaram para o operador.

## Mapa da pasta

```
nl.py                  CLI
nlean/                 código (io, schema, segment, grounding, canon, extraction,
                       operator, diagnostics, report, metrics, advocate,
                       contracts, validate, verifiers/)
project.yaml           configuração, prompts em uso, critérios de parada
doctypes.yaml          quais documentos entram e com que tipo
lenses.yaml            lentes por tipo de documento (tabela da seção 4.3)
lens_conflicts.yaml    tensões entre lentes (gerado pelos contratos)
suppressions.yaml      diagnósticos suprimidos, com motivo
schema/                formato do fato, vocabulário, perguntas-base
canon/                 o que é verdade no mundo (e quem aprovou)
prompts/               prompts versionados
verifiers/semantic/contracts/   contratos das lentes semânticas
cache/, facts/         extrações (criadas na primeira rodada; versione: são caras de refazer)
reports/               relatórios (piloto-fase0/ = teste de fumaça)
tests/verifiers/       testes unitários e ponta a ponta
tests/golden_extraction/, tests/seeded_errors/, tests/gabarito/   material da Fase 1
work/                  pacotes e respostas em trânsito (fora do git)
```
