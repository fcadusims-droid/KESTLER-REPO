-- KESTLERIUM — schema da Fase 1 (L0: mundo físico, sem drama, sem LLM)
--
-- Nada aqui sabe o que é crença, objetivo ou pressão. Fase 1 responde uma
-- pergunta só: as pessoas se movem por um mundo real e se encontram com
-- variedade? Se os encontros forem sempre entre os mesmos pares, o drama das
-- fases seguintes vira ruído.

CREATE TABLE IF NOT EXISTS agent (
    id                TEXT PRIMARY KEY,
    name              TEXT NOT NULL,
    origin            TEXT NOT NULL,   -- obra de origem, ou 'nativo'
    kind              TEXT NOT NULL,   -- 'encarnado' | 'entidade'
    arrival_tick      INTEGER NOT NULL,-- chegada contínua: antes disso não existe
    home_location_id  TEXT,            -- NULL para entidades
    constitution_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS location (
    id        TEXT PRIMARY KEY,
    name      TEXT NOT NULL,
    kind      TEXT NOT NULL,   -- residencia | trabalho | social | servico | transito
    capacity  INTEGER NOT NULL,
    connected INTEGER NOT NULL, -- 1 = tem rede; canal de encontro das entidades
    shared    INTEGER NOT NULL  -- 1 = espaço comum; 0 = moradia (unidades privadas)
);

-- Grafo de deslocamento. Gravado nas duas direções na carga.
CREATE TABLE IF NOT EXISTS location_edge (
    from_id      TEXT NOT NULL,
    to_id        TEXT NOT NULL,
    travel_ticks INTEGER NOT NULL,
    PRIMARY KEY (from_id, to_id)
);

-- Rotina por faixa horária do dia (ticks 0..47). Não é obrigação: necessidade
-- crítica e desvio aleatório sobrescrevem.
CREATE TABLE IF NOT EXISTS routine (
    agent_id    TEXT NOT NULL,
    start_tod   INTEGER NOT NULL,
    end_tod     INTEGER NOT NULL,
    location_id TEXT NOT NULL,
    activity    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS agent_state (
    agent_id    TEXT NOT NULL,
    tick        INTEGER NOT NULL,
    location_id TEXT,              -- NULL = em trânsito
    activity    TEXT NOT NULL,
    needs_json  TEXT NOT NULL,
    PRIMARY KEY (agent_id, tick)
);

-- Um encontro é a TRANSIÇÃO para co-presença, não cada tick junto. Sem isso a
-- tabela vira contagem de tempo compartilhado e a métrica de variedade mente.
CREATE TABLE IF NOT EXISTS encounter (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    tick        INTEGER NOT NULL,
    location_id TEXT,
    channel     TEXT NOT NULL,   -- 'presencial' | 'rede'
    agent_a     TEXT NOT NULL,   -- sempre o menor id do par, para o par ser canônico
    agent_b     TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_encounter_tick ON encounter(tick);
CREATE INDEX IF NOT EXISTS idx_encounter_pair ON encounter(agent_a, agent_b);
CREATE INDEX IF NOT EXISTS idx_state_tick     ON agent_state(tick);

-- Relógio do mundo. Linha única. `last_tick` é até onde o mundo já foi
-- simulado; no modo real, a execução seguinte compara com o tick de agora e
-- recupera o atraso. Isso mantém o Kestlerium colado no horário de Brasília
-- mesmo quando o agendador atrasa ou falha.
CREATE TABLE IF NOT EXISTS world_clock (
    id        INTEGER PRIMARY KEY CHECK (id = 1),
    epoch_iso TEXT NOT NULL,
    last_tick INTEGER NOT NULL,
    mode      TEXT NOT NULL   -- 'real' | 'rapido'
);

-- Registro de execução: toda rodada fica gravada com seed e parâmetros, para
-- que um resultado ruim possa ser reproduzido e explicado depois.
CREATE TABLE IF NOT EXISTS run (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at    TEXT NOT NULL,
    mode          TEXT NOT NULL,
    seed          INTEGER NOT NULL,
    from_tick     INTEGER NOT NULL,
    to_tick       INTEGER NOT NULL,
    ticks_per_day INTEGER NOT NULL,
    params_json   TEXT NOT NULL,
    wall_seconds  REAL
);

-- ===========================================================================
-- FASE 2 — verdade vs. crença
-- ===========================================================================

-- A VERDADE. Append-only: um fato nunca é atualizado nem apagado. O que muda
-- é quem acredita nele e com que fidelidade.
CREATE TABLE IF NOT EXISTS fact (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    tick          INTEGER NOT NULL,
    subject       TEXT NOT NULL,
    predicate     TEXT NOT NULL,
    object        TEXT,
    visibility    TEXT NOT NULL,   -- publico | privado | oculto
    witnesses_json TEXT NOT NULL
);

-- A CRENÇA. Ponteiro para o fato, nunca cópia.
--
-- REGRA INVIOLÁVEL: nenhum agente lê `fact`. Toda leitura passa por aqui.
-- Quebrar isso uma vez destrói a capacidade de representar segredo.
--
-- distortion 0 = fiel. > 0 = o agente acredita em `distorted_object`, não no
-- objeto real. Um nativo que testemunha uma anomalia racionaliza por padrão:
-- ele não passa a crer "é um vampiro", ele crê "foi truque". Testemunho
-- repetido corrói a racionalização — é assim que a exposição acontece.
CREATE TABLE IF NOT EXISTS belief (
    agent_id        TEXT NOT NULL,
    fact_id         INTEGER NOT NULL,
    confidence      REAL NOT NULL,   -- 0..1
    distortion      INTEGER NOT NULL,
    distorted_object TEXT,
    source_agent_id TEXT,            -- NULL = testemunhou em primeira mão
    salience        REAL NOT NULL,   -- decai com o tempo, sobe ao ser reativada
    acquired_tick   INTEGER NOT NULL,
    PRIMARY KEY (agent_id, fact_id)
);

CREATE TABLE IF NOT EXISTS goal (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id  TEXT NOT NULL,
    type      TEXT NOT NULL,
    target_id TEXT,
    priority  REAL NOT NULL,
    status    TEXT NOT NULL,   -- ativo | bloqueado | satisfeito | abandonado
    depends_on_facts_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS relation (
    agent_a           TEXT NOT NULL,
    agent_b           TEXT NOT NULL,
    affect            REAL NOT NULL,   -- -1..1
    trust             REAL NOT NULL,   -- 0..1
    tension           REAL NOT NULL,   -- 0..1
    last_contact_tick INTEGER,
    PRIMARY KEY (agent_a, agent_b)
);

CREATE INDEX IF NOT EXISTS idx_belief_fact  ON belief(fact_id);
CREATE INDEX IF NOT EXISTS idx_belief_agent ON belief(agent_id);
CREATE INDEX IF NOT EXISTS idx_fact_subject ON fact(subject);

-- ===========================================================================
-- FASE 3 — pressão
-- ===========================================================================
CREATE TABLE IF NOT EXISTS pressure_event (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    tick        INTEGER NOT NULL,
    day         INTEGER NOT NULL,
    agent_a     TEXT NOT NULL,
    agent_b     TEXT NOT NULL,
    location_id TEXT,
    channel     TEXT NOT NULL,
    value       REAL NOT NULL,
    de REAL, co REAL, cr REAL, re REAL, ta REAL,  -- componentes, para diagnóstico
    participants_json TEXT                        -- quem estava na cena
);
CREATE INDEX IF NOT EXISTS idx_pressure_day ON pressure_event(day);
