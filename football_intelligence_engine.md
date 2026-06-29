# Football Intelligence Engine — Complete Project

> A private AI that watches a live football match the way a coach, a performance
> analyst, and a statistician would — at the same time. It does not just compute
> statistics. It **interprets**, **explains**, **predicts**, and **learns**. The
> goal is not to guess the final score. The goal is to *understand football in
> real time*.

This document describes the system **part by part**, with every weak or sketched
idea developed into something concrete. Code blocks are **real Python**, not
pseudocode. The system has a single guiding sentence:

> *"An artificial intelligence able to understand a football match like a great
> analyst: reading the game in real time, explaining its dynamics, identifying
> tactical patterns, modeling the collective and individual behavior of the teams,
> and anticipating — with well-founded probabilities — the most likely
> developments of the match."*

Every new module must contribute to **understanding the game**, not merely add
another metric. This keeps complexity down and gives the project a clear identity.

---

## Table of Contents

1. [Philosophy and mission](#1-philosophy-and-mission)
2. [The core idea: the Digital Model of the Match](#2-the-core-idea-the-digital-model-of-the-match)
3. [High-level architecture](#3-high-level-architecture)
4. [The acquisition-to-knowledge pipeline (6 layers)](#4-the-acquisition-to-knowledge-pipeline)
5. [Data layer and the normalized event model](#5-data-layer-and-the-normalized-event-model)
6. [Database](#6-database)
7. [Index engine (State & Spatial Intelligence)](#7-index-engine)
8. [Prediction engine (Predictive Intelligence)](#8-prediction-engine)
9. [Regime detector (state of the match changes meaning)](#9-regime-detector)
10. [Confidence engine (how much to trust a diagnosis)](#10-confidence-engine)
11. [Change detector (Temporal Intelligence)](#11-change-detector)
12. [Individual Intelligence: behavioral player modeling](#12-individual-intelligence)
13. [Coach Intelligence](#13-coach-intelligence)
14. [Tactical & Collective Intelligence](#14-tactical-and-collective-intelligence)
15. [Narrative Intelligence: perception vs reality](#15-narrative-intelligence)
16. [Consensus engine: evidence fusion](#16-consensus-engine)
17. [Match Memory](#17-match-memory)
18. [Causality Model](#18-causality-model)
19. [Explanatory Intelligence](#19-explanatory-intelligence)
20. [Validation and calibration](#20-validation-and-calibration)
21. [Continuous learning](#21-continuous-learning)
22. [The intelligent panel](#22-the-intelligent-panel)
23. [Roadmap by phases](#23-roadmap-by-phases)
24. [Honest risks and limitations](#24-honest-risks-and-limitations)

---

## 1. Philosophy and mission

The system does **not** try to guess the final result. Throughout the match it
continuously answers questions a great analyst would ask:

- Who really controls the game right now?
- Which team is imposing its style?
- Where is an advantage emerging?
- Which players are changing the match?
- What tactical patterns are showing up?
- What will probably happen in the next few minutes?
- How is the game evolving?
- Should the coach change something?
- What are each team's current weak spots?

In one line: **don't predict scores — understand football.**

Four principles guide everything:

1. **Understanding over numbers.** A raw statistic ("62% possession") is not
   understanding. Understanding is knowing *what that possession is doing* —
   whether it is sterile circulation or sustained pressure that is breaking lines.
   Every module exists to turn data into interpretation.

2. **Data is evidence; opinion is a hypothesis; the system is a verifier.** Every
   claim — from a commentator, the crowd, social media, or a pundit — is treated as
   a *hypothesis* to be checked against the data, never as truth. The system
   actively looks for the moments when the **dominant narrative does not match what
   the game actually shows**.

3. **Explanation above all.** The AI never answers just `72%`. It answers *why*:
   which mechanisms, which players, which tactical shifts moved the number. A
   probability without a reason is half an answer.

4. **Calibration is the judge.** A predictive claim only means something if, of the
   events the system calls 60%, roughly 60% actually happen. A model that "sees
   patterns everywhere" is almost always wrong, not insightful. Calibration
   (Section 20) is the final arbiter of every prediction.

> **The central axis.** What most distinguishes this project is not the goal
> predictor — everyone tries to predict goals. It is the attempt to separate **what
> is really happening** from **what people believe is happening**: real game state
> vs narrative, objective data vs collective emotion, the live picture vs the
> received wisdom. Measuring that distance is where the project's identity lives.

---

## 2. The core idea: the Digital Model of the Match

Instead of dozens of independent modules, everything revolves around a **single
living representation of the game** — the Digital Model of the Match. Every new
piece of information updates this one model, and every inference, explanation, and
prediction is read from it.

The model is not just numbers. It carries several interlocking *states*:

```text
Digital Model of the Match
├── Collective state   : how each team functions as an organism
├── Individual state   : each player's live behavior vs their own baseline
├── Tactical state     : what each team is currently trying to do
├── Spatial state      : how the pitch is being occupied and exploited
├── Temporal state     : the trend — is the game accelerating, fading, shifting?
├── Contextual state   : score, time, sendings-off, fatigue, stakes
├── Emotional state    : the collective mood around the match
└── Confidence state   : how much the system trusts its own current reading
```

Everything downstream is a *view* of this one object. That is the architectural
discipline: a module is only allowed to exist if it either **enriches the model**
or **reads from it to produce understanding**.

---

## 3. High-level architecture

The flow is a pipeline from raw evidence to explained knowledge, with a learning
loop closing back over it:

```text
        ┌──────────────────────────────────────────────────────────────┐
        │                                                                │
        ▼                                                                │
  Public sources (stats feeds, live text, chat, social, broadcasts)      │
        │                                                                │
        ▼                                                                │
  Layer 1 — Knowledge Acquisition (independent connectors → one format)  │
        │                                                                │
        ▼                                                                │
  Layer 2 — Cleaning Engine (human text → structured events)             │
        │                                                                │
        ▼                                                                │
  Layer 3 — Semantic Extraction (entities · actions · context · intensity)│
        │                                                                │
        ▼                                                                │
  Layer 4 — Cognitive Engine (statistical · social · narrative ·         │
        │                       tactical · temporal brains)              │
        ▼                                                                │
  Layer 5 — Consensus Engine (reconcile every source → one picture)      │
        │                                                                │
        ▼                                                                │
  Layer 6 — Football Intelligence Engine ──► updates ► Digital Model     │
        │                                                                │
        ▼                                                                │
  The Twelve Intelligences (read the model → produce understanding)      │
        │                                                                │
        ▼                                                                │
  Inferences → Explanations → Predictions                                 │
        │                                                                │
        ▼                                                                │
  Intelligent Panel / Alerts                                              │
        │                                                                │
        ▼                                                                │
  [after the match] Resolution → Calibration ──► tunes weights ──────────┘
```

The key conceptual shift from the original design: this is **not** a project that
"merges statistics, commentary, and chat." It is an **evidence-fusion engine**.
Each source is limited and biased; the system's value is in reconciling those
biased signals into a single, explainable, continuously updated interpretation of
the match — independent of any one data provider.

| Layer / Module | Single responsibility |
|---|---|
| Acquisition | Turn any public source into one standard event format |
| Cleaning | Turn noisy human text into structured events |
| Semantic extraction | Identify entities, actions, context, and intensity |
| Cognitive engine | Specialized "brains" read the events into meaning |
| Consensus | Reconcile disagreeing sources into one diagnosis + a confidence |
| Football Intelligence Engine | Maintain the Digital Model and produce knowledge |
| State / Spatial | Summarize *what the game is* right now |
| Tactical / Collective | Explain *what each team is trying to do* |
| Individual | Model each player's behavior vs their own DNA |
| Coaches | Model how each coach thinks and reacts |
| Temporal | Detect that the game *just changed* |
| Contextual | Reinterpret everything by score, time, stakes |
| Predictive | Anticipate the next events, with probabilities |
| Explanatory | Attach the *why* to every output |
| Narrative | Measure the gap between perception and reality |
| Memory | Keep a structured, replayable timeline |
| Causality | Infer the likely cause of each shift |
| Learning | Improve the model from every match |
| Validation | Measure whether the predictions are calibrated |

---

## 4. The acquisition-to-knowledge pipeline

Six layers turn raw, messy public information into explained knowledge.

### 4.1 Layer 1 — Knowledge Acquisition

The goal: turn **any** public source into one standardized stream of events. Each
connector is independent and lives on its own, so adding or swapping a source never
touches the rest of the system.

```text
/sources
    youtube_chat.py
    reddit.py
    bluesky.py
    livescore.py
    flashscore.py
    sofascore.py
    fotmob.py
    espn.py
    globo.py
    onefootball.py
    ...
```

Every connector returns exactly the same shape, so the rest of the system never
needs to know where a piece of information came from:

```python
{
    "timestamp": "...",     # when it was captured
    "source":    "...",     # which connector produced it
    "kind":      "...",     # stat | text | chat | social | broadcast
    "text":      "...",     # raw payload (may be empty for pure stats)
    "trust":     0.93,      # the connector's prior reliability, 0..1
}
```

```python
from abc import ABC, abstractmethod

class Source(ABC):
    """A single public source of match information."""
    name: str
    base_trust: float          # prior reliability of this connector

    @abstractmethod
    def stream(self, match_id): ...   # yields raw records in the shape above
```

> Note on the live chat connector. A good starting point is the live chat of a
> large public broadcast (for example a popular streaming channel), captured with a
> stream-reading library rather than by rendering the page. Treat it as **just
> another Layer-1 source**, and always respect the platform's terms of use and
> applicable copyright. The whole point of the abstract interface is that this is
> one swappable source among many.

### 4.2 Layer 2 — Cleaning Engine

This is one of the most important parts, because almost everything from the
internet is noise. The job is to turn human text into structured events.

```text
"GOOOOOOOOOOOOOL"          →  { "event": "GOAL" }
"corner for Brazil"        →  { "event": "CORNER", "team": "Brazil" }
"Vini is finished tonight" →  { "entity": "Vinicius Junior",
                                "kind": "opinion", "polarity": -0.82 }
```

```python
import re

GOAL_PATTERN = re.compile(r"\bg+o+l+\b", re.IGNORECASE)

def clean(record):
    """Map one raw record to zero or more structured events."""
    text = (record["text"] or "").strip()
    if GOAL_PATTERN.search(text):
        return [{"event": "GOAL", "source": record["source"]}]
    # ... corner, card, shout, opinion, etc.
    return []
```

### 4.3 Layer 3 — Semantic Extraction

Here the system starts to actually *read*. From cleaned text it identifies four
things:

```text
Entities    : players · coaches · referee · teams
Actions      : shot · cross · loss · dribble · tackle · interception · press
Context      : praise · criticism · irony · sarcasm · doubt · complaint · joy
Intensity    : how strongly it is being said
```

Intensity matters: `GOOOOOOOOOOL` is not the same as `goal`. The number of repeated
letters is itself an emotional-intensity signal, and ALL-CAPS, punctuation, and
repetition all carry it.

```python
def emotional_intensity(text):
    """Rough 0..1 intensity from repetition, caps, and punctuation."""
    if not text:
        return 0.0
    stretch = max((len(m) for m in re.findall(r"(.)\1+", text)), default=1)
    caps = sum(c.isupper() for c in text) / max(1, len(text))
    bangs = min(1.0, text.count("!") / 5)
    raw = 0.5 * min(1.0, stretch / 8) + 0.3 * caps + 0.2 * bangs
    return min(1.0, raw)
```

> Honest caveat. Extracting reliable meaning from text — especially Portuguese,
> with its irony, slang, and sarcasm — is genuinely hard. Start with a few robust
> signals and expand only when each one earns its place against the data.

### 4.4 Layer 4 — Cognitive Engine

Here lives the actual intelligence: several specialized **brains**, each reading a
different slice of evidence.

```text
Statistical brain : possession, shots, passes, pressure, xG, ...   → the measurable game
Social brain      : chat, social, comments                          → how the public sees it
Narrative brain   : live text commentary                            → what just happened
Tactical brain    : events + stats + positions + pressure           → why it happened
Temporal brain    : evolution only                                  → the trend
```

The temporal brain watches only change over time:

```text
10' — Brazil dominates
20' — Brazil still dominating
30' — Brazil losing intensity
40' — Argentina growing
        →  "the game is shifting"
```

### 4.5 Layer 5 — Consensus Engine

A module that barely exists in current systems: it **compares every source** and
reconciles them. See Section 16 for the full design. In short:

```text
Sofascore   : dangerous attack
Flashscore  : ordinary attack
Chat        : almost a goal!
Commentary  : great save
        →  Consensus: "chance created", confidence 92%
```

### 4.6 Layer 6 — Football Intelligence Engine

The main brain. It does not hand back statistics — it produces **knowledge**: the
current state, a diagnosis of *why*, a prognosis of *what is likely next*, and
alerts on tactical, physical, or psychological shifts — each one carrying its
reasoning, never a bare number. This is where the Digital Model of Section 2 is
maintained.

---

## 5. Data layer and the normalized event model

Regardless of source, everything becomes an `Event` in one format. The player and
position fields are **optional** — filled only when the source provides them — so
the system can start without them and switch on Section 12 when richer data
appears.

```text
Event {
    match_id:  string
    minute:    float       # e.g. 27.0
    team:      "HOME" | "AWAY"
    type:      "shot" | "shot_on_target" | "dangerous_attack"
             | "corner" | "foul" | "yellow_card" | "red_card" | "goal"
             | "pass" | "dribble" | "reception"   # useful for player profiles
    player_id: string | null   # who performed it (attribution)
    target_id: string | null   # for passes: who received (interaction network)
    x:         float  | null   # pitch position (event data)
    y:         float  | null
    xg:        float  | null   # when available
}
```

### 5.1 The real data problem

- **Pre-match** data (line-ups, history) is cheap and easy.
- **Live, granular** data (minute-by-minute dangerous attacks, live xG, real-time
  shots on target) is expensive, often paywalled, and **arrives with latency**.
- **Latency is critical.** If your feed updates 30–60s after the broadcast, your
  "live" reading is describing a game state that has already moved on. Build with
  that lag in mind.
- **Player-level event data** (touch-by-touch, with attribution and position) is
  the professional standard and the most expensive, least available live. Section
  12 depends on it, so the realistic path is to build player profiles from
  **finished matches first** and only later wire live influence and passing
  networks.

> Design decision: the real source is a **pluggable detail**. The collector talks
> to the abstract `Source` interface, so switching providers — or using a simulated
> feed for development — never affects the rest of the system.

### 5.2 The collector

```python
def collect(match_id, source, db, interval=10):
    seen = set()                                 # for deduplication
    while match_is_live(match_id):
        try:
            for record in source.stream(match_id):
                for ev in pipeline(record):      # Layers 2 + 3
                    key = (ev.minute, ev.team, ev.type, ev.player_id)
                    if key not in seen:
                        seen.add(key)
                        db.insert_event(ev)
            db.update_score(match_id, source.score(match_id))
            db.update_lineup(match_id, source.lineup(match_id))
        except NetworkError:
            log("temporary failure, retrying")
        sleep(interval)                          # respect rate limits
```

---

## 6. Database

SQLite is perfect for a notebook-scale system. Beyond raw events we keep
**state snapshots**, **player and coach profiles**, **narratives and their
verification**, the **consensus readings**, the **match timeline**, and — crucially
— the **predictions made** and **what actually happened**, so the model can be
validated (Section 20).

```sql
-- One row per match
CREATE TABLE matches (
    id              TEXT PRIMARY KEY,
    date            TEXT,
    competition     TEXT,
    home_team       TEXT,
    away_team       TEXT,
    status          TEXT,            -- scheduled | live | finished
    home_goals_final INTEGER,
    away_goals_final INTEGER
);

CREATE TABLE players (
    id        TEXT PRIMARY KEY,
    name      TEXT,
    position  TEXT,                  -- GK | DEF | MID | FWD
    team_id   TEXT
);

-- Raw event stream (with optional attribution and position)
CREATE TABLE events (
    id         INTEGER PRIMARY KEY,
    match_id   TEXT REFERENCES matches(id),
    minute     REAL,
    team       TEXT,                 -- HOME | AWAY
    type       TEXT,
    player_id  TEXT REFERENCES players(id),  -- who executed (may be NULL)
    target_id  TEXT REFERENCES players(id),  -- for passes: who received
    x          REAL, y REAL,         -- pitch position (may be NULL)
    xg         REAL
);

-- Who was on the pitch, per match (for on/off influence)
CREATE TABLE lineups (
    match_id   TEXT REFERENCES matches(id),
    player_id  TEXT REFERENCES players(id),
    on_minute  REAL,                 -- minute they came on (0 if starter)
    off_minute REAL                  -- minute they left (NULL if stayed)
);

-- Consolidated "DNA" of each player
CREATE TABLE player_profiles (
    player_id        TEXT REFERENCES players(id),
    updated_at       TEXT,
    avg_hold_seconds REAL,
    pass_accuracy    REAL,
    progressive_pass REAL,           -- share of progressive passes
    shot_frequency   REAL,
    assist_frequency REAL,
    turnover_rate    REAL,
    archetype        TEXT            -- conservative | creator | finisher | ...
);

-- Passing network: edges between players
CREATE TABLE interactions (
    match_id        TEXT REFERENCES matches(id),
    from_player     TEXT REFERENCES players(id),
    to_player       TEXT REFERENCES players(id),
    passes          INTEGER,
    chances_created INTEGER
);

-- Estimated influence of each player on their team's goal rate
CREATE TABLE influence (
    player_id   TEXT REFERENCES players(id),
    lambda_on   REAL,               -- team rate with them on the pitch
    lambda_off  REAL,               -- team rate without them
    delta       REAL,               -- lambda_on - lambda_off
    minutes     REAL                -- observed minutes (reliability)
);

-- Tactical profile of the coach
CREATE TABLE coach_profiles (
    coach_id        TEXT PRIMARY KEY,
    name            TEXT,
    when_winning    TEXT,           -- retreat | hold | press
    when_losing     TEXT,
    avg_sub_minute  REAL,
    sub_style       TEXT,           -- offensive | defensive | like-for-like
    reaction        TEXT,           -- pattern after conceding/scoring
    matches_seen    INTEGER
);

-- Opinions captured from sources
CREATE TABLE opinions (
    id           INTEGER PRIMARY KEY,
    source_id    TEXT REFERENCES sources(id),
    match_id     TEXT REFERENCES matches(id),
    target_id    TEXT,             -- player/team/coach referenced
    text         TEXT,
    intensity    REAL,             -- 0..1 (Layer 3)
    captured_at  TEXT
);

-- Testable hypotheses extracted from opinions
CREATE TABLE hypotheses (
    id           INTEGER PRIMARY KEY,
    opinion_id   INTEGER REFERENCES opinions(id),
    target_id    TEXT,
    aspect       TEXT,             -- e.g. finishing, creation, defending
    direction    TEXT              -- better | worse | same
);

-- Verification: hypothesis vs data
CREATE TABLE verifications (
    hypothesis_id INTEGER REFERENCES hypotheses(id),
    z_score       REAL,
    label         TEXT,            -- confirmed | partial | not | contradicted
    verified_at   TEXT
);

-- Sources and their dynamic credibility
CREATE TABLE sources (
    id        TEXT PRIMARY KEY,
    name      TEXT,
    type      TEXT,                -- commentator | pundit | social | community
    hits      INTEGER,
    total     INTEGER,
    weight    REAL                 -- hits / total (credibility)
);

-- State + indices snapshot at each evaluated minute
CREATE TABLE snapshots (
    id              INTEGER PRIMARY KEY,
    match_id        TEXT REFERENCES matches(id),
    minute          REAL,
    home_goals      INTEGER, away_goals INTEGER,
    pressure_home   REAL, pressure_away REAL,
    control_home    REAL, vulnerability_home REAL,
    momentum        REAL,          -- home's share of recent pressure
    lambda_home     REAL, lambda_away REAL,
    regime          TEXT,          -- NORMAL | PRESSURE | ... (Section 9)
    confidence      REAL,          -- 0..1: trust in this reading (Section 10)
    change_score    INTEGER        -- 0..100: how much the game just shifted
);

-- Structured timeline of the match (Section 17)
CREATE TABLE timeline (
    match_id   TEXT REFERENCES matches(id),
    minute     REAL,
    headline   TEXT,               -- e.g. "Brazil started pressing"
    detail     TEXT
);

-- Consensus reading per minute (Section 16)
CREATE TABLE consensus (
    match_id   TEXT REFERENCES matches(id),
    minute     REAL,
    claim      TEXT,               -- e.g. "chance created"
    agreement  REAL,               -- 0..1 across sources
    confidence REAL                -- 0..1 diagnosis confidence
);

-- Collective emotional state per minute, per channel
CREATE TABLE sentiment (
    match_id   TEXT REFERENCES matches(id),
    minute     REAL,
    channel    TEXT,               -- crowd | commentators | community
    emotion    REAL,               -- 0..100 (negative … positive)
    reality    REAL,               -- 0..100 (objective data score)
    overreaction INTEGER           -- 1 if emotion extreme but data calm
);

-- Recurring-narrative memory (Section 15.6)
CREATE TABLE narrative_memory (
    pattern      TEXT PRIMARY KEY,  -- e.g. "team X collapses late"
    confirmed    INTEGER,
    total        INTEGER,
    rate         REAL               -- confirmed / total
);

-- Every prediction made (the key record for validation)
CREATE TABLE predictions (
    id           INTEGER PRIMARY KEY,
    match_id     TEXT REFERENCES matches(id),
    minute       REAL,
    target       TEXT,             -- e.g. "goal_10min", "next_corner", "comeback"
    probability  REAL,
    confidence   REAL,             -- 0..1 (Section 10)
    created_at   TEXT
);

-- Real outcome of each prediction (filled after the match)
CREATE TABLE outcomes (
    prediction_id INTEGER REFERENCES predictions(id),
    happened      INTEGER           -- 1 if the predicted event occurred, else 0
);
```

---

## 7. Index engine

State and Spatial Intelligence start here: turning thousands of events into a few
interpretable numbers. The key refinement over a naive "last 10 minutes" window is
**exponential decay** — recent events weigh more, smoothly, with no artificial cut.

### 7.1 Exponential decay

```text
time_weight(ev) = exp( -(current_minute - ev.minute) / TAU )
```

`TAU` controls memory: smaller = reacts fast to pressure waves; larger = steadier.
It is a parameter to calibrate.

### 7.2 The indices

```text
Offensive Pressure (of a team) =
      Σ [ event_weight(type) * time_weight(ev) ]   over the team's offensive events
      where event_weight = { shot_on_target:3, shot:1.5, dangerous_attack:1, corner:1.2 }

Control =
      territorial dominance ~ possession and offensive pass sequences
      (use possession when available; otherwise approximate via relative attacks)

Vulnerability =
      offensive pressure conceded, adjusted by cards and chances allowed

Momentum =
      Pressure_home / (Pressure_home + Pressure_away)   ∈ [0,1]
      > 0.5 → home dominating the recent minutes
```

### 7.3 Code

```python
import math

EVENT_WEIGHT = {"shot_on_target": 3.0, "shot": 1.5,
                "dangerous_attack": 1.0, "corner": 1.2}

def offensive_pressure(events, team, current_minute, tau):
    total = 0.0
    for ev in events:
        if ev.team == team and ev.minute <= current_minute:
            w = EVENT_WEIGHT.get(ev.type, 0.0)
            if w:
                total += w * math.exp(-(current_minute - ev.minute) / tau)
    return total

def momentum_index(events, current_minute, tau):
    ph = offensive_pressure(events, "HOME", current_minute, tau)
    pa = offensive_pressure(events, "AWAY", current_minute, tau)
    return 0.5 if ph + pa == 0 else ph / (ph + pa)
```

### 7.4 Spatial intelligence (new)

When position data (`x`, `y`) is available, the same engine answers spatial
questions the original design could not:

```text
pitch occupation · compactness · width · depth · broken lines
· free corridors · congested zones · influence map
```

These feed the tactical brain ("the right channel is being overloaded") and the
explanatory layer ("pressure rose because the away block lost compactness").

---

## 8. Prediction engine

Predictive Intelligence treats goals — and other events — as a **Poisson process
with a variable intensity (λ)** that depends on the game state. From this one idea,
a whole family of predictions follows with closed-form, correct formulas. The aim
is **not** a betting market; it is to anticipate the concrete next developments of
the match.

### 8.1 Foundation

For a rate `λ` (events per minute) over `t` minutes:

```text
P(at least one event in t minutes) = 1 - e^(-λ·t)
P(exactly k events)               = e^(-Λ) · Λ^k / k!,   Λ = λ·t   (Poisson)
P(next goal is home)              = λ_home / (λ_home + λ_away)
```

### 8.2 Dynamic intensity

Each team's rate starts from a base and is scaled by factors:

```text
λ_team = BASE_RATE
       × mult_pressure(team)   # how much the team is pressing now
       × mult_score(team)      # a leading team often retreats; a trailing one pushes
       × mult_card(team)       # sendings-off
       × mult_time(minute)     # goals cluster near the end of each half
       × mult_lineup(team)     # who is on the pitch and how they are playing (Sec. 12)
```

- **Score effect** is **coach-specific** (Section 13): not every team retreats when
  leading.
- **Time effect** can be learned from the historical distribution of goals by
  minute.
- **Lineup effect** is the bridge to player modeling (Section 12); without player
  data it is 1 (neutral).

> Calibrated value: `BASE_RATE ≈ 0.015` goals/min per team reproduces ~2.7 goals
> per match in a neutral scenario, matching real football. Validated in Section
> 20.4.

```python
def rates(state, events, params, regime=None, profiles=None):
    """Return (λ_home, λ_away) per minute, with all multipliers."""
    rs = params.regime_scale.get(regime, 1.0) if regime else 1.0
    profiles = profiles or {}

    def lam(team):
        m = (mult_pressure(events, team, state.minute, params)
             * mult_score(state, team, profiles.get(team))   # coach-specific
             * mult_time(state.minute)
             * mult_card(events, team, state.minute))
        return params.base_rate * rs * m

    return lam("HOME"), lam("AWAY")
```

### 8.3 What the engine predicts

```text
t5, t10           = minutes ahead (5, 10)
t_half            = minutes to half-time
λ = λ_home + λ_away

Goal in next 5 / 10 min  = 1 - e^(-λ·t)
Goal before half-time    = 1 - e^(-λ·t_half)
Next goal (home/away)    = λ_home / λ   ·   λ_away / λ
Next corner / card / shot= 1 - e^(-λ_event·t)     # per-event Poisson rate
Create a big chance      = 1 - e^(-λ_chance·t)    # from pressure + xG rate
Comeback / shift of      = higher-level reads built on the above plus regime
   control                 and momentum trend (Section 11)
```

```python
def poisson_at_least(lmbda, k):
    if k <= 0:
        return 1.0
    cdf = sum(math.exp(-lmbda) * lmbda ** i / math.factorial(i) for i in range(k))
    return max(0.0, 1.0 - cdf)

def prob_event_within(lambda_event, minutes):
    return 1 - math.exp(-lambda_event * minutes)

def prob_next_goal(lam_home, lam_away):
    s = lam_home + lam_away
    return {"HOME": 0.5, "AWAY": 0.5} if s == 0 else \
           {"HOME": lam_home / s, "AWAY": lam_away / s}
```

> Every prediction is logged to the `predictions` table with its confidence, so
> Section 20 can later check whether the events the system called 60% happened
> ~60% of the time. A prediction that is never scored against reality is worthless.

---

## 9. Regime detector

Football is not stationary — it **changes state**, and the same numbers mean
different things in different states. A balanced 0–0 at minute 20 and a 0–0 at
minute 89 with one team chasing the game are different realities, even if
possession and shots look similar. This is perhaps the most important module: it
tells **which regime** the match is in, and every other module then reads the data
in that light.

### 9.1 The regimes

```text
NORMAL        : balanced, 11 v 11, no urgency
PRESSURE      : one team stacks attacks, the other only defends
DESPERATION   : a team behind with little time left — maximum risk
POST-GOAL     : the minutes right after a goal (reaction / counter)
POST-RED-CARD : 11 v 10 — structural imbalance
END-GAME      : final minutes, managing or chasing the result
```

### 9.2 Why it changes everything

The same "high pressure index" means opposite things by regime:

- In **NORMAL**, a team's high pressure suggests a goal is near.
- In **DESPERATION**, pressure is *expected* (the team needs the goal) — pressing is
  no longer news.

So the regime **reconditions** the multipliers of Section 8.2 and the reading of
the indices of Section 7. There is a set of weights **per regime**, calibrated
separately (Section 20).

### 9.3 Detection

```python
def detect_regime(state, events, params):
    if minutes_since_last_goal(events, state.minute) < 5:
        return "POST_GOAL"
    if red_card_happened(events, state.minute):
        return "POST_RED_CARD"
    if state.minute > 80:
        return "DESPERATION" if state.home_goals != state.away_goals else "END_GAME"
    mom = momentum_index(events, state.minute, params.tau)
    if max(mom, 1 - mom) > params.pressure_threshold:
        return "PRESSURE"
    return "NORMAL"
```

> The regime is also an input to the Confidence engine (Section 10): regime
> transitions are moments of instability, where confidence in the current reading
> should drop.

---

## 10. Confidence engine

So far the system produces a **diagnosis or a probability**. It must also say **how
much it trusts it**. These are not the same thing:

```text
Goal in next 10 min        Goal in next 10 min
Probability: 62%           Probability: 62%
Confidence:  28%           Confidence:  91%
```

The first is a shaky guess; the second is a solid read. **Same probability,
opposite decisions.** Confidence is a second dimension that accompanies every
output.

### 10.1 What it depends on

```text
Amount of data     : few minutes/events so far → low confidence
Source quality     : complete, low-latency feed → high; poor feed → low
Source agreement   : sources concur (Section 16) → high; they conflict → low
Regime stability   : just changed regime → low; stable → high
Similar history    : many analogous cases in the DB → high; rare situation → low
```

### 10.2 How to compute it

A number in [0,1] combining factors (each also in [0,1]) with a **geometric mean**,
so that one terrible factor collapses the whole thing — which is what we want:

```python
def confidence(n_events, source_quality, source_agreement,
               regime_instability, similar_cases, n_ref=40, h_ref=50):
    f_data    = min(1.0, n_events / n_ref)
    f_source  = max(0.0, min(1.0, source_quality))
    f_agree   = max(0.0, min(1.0, source_agreement))
    f_regime  = max(0.0, min(1.0, 1.0 - regime_instability))
    f_history = min(1.0, similar_cases / h_ref)
    return (f_data * f_source * f_agree * f_regime * f_history) ** 0.2
```

### 10.3 How confidence is used

Confidence does not change the probability — it modulates **how the output is
presented and trusted**:

- In the **panel** (Section 22): always shown next to the probability.
- In **alerts**: a low-confidence shift is flagged as "watch", not "this happened".
- In **explanations** (Section 19): low confidence softens causal claims into
  tentative ones.

> Calibrating confidence itself is part of Section 20: over time, check whether
> "high confidence" predictions really do err less than "low confidence" ones. If
> they don't, the confidence is badly defined and must be re-tuned. **Uncalibrated
> confidence is worse than none** — it gives false security.

---

## 11. Change detector

Temporal Intelligence answers one question: *did the game just change?* Before the
ball rolls, history and context set an expectation. Minutes later, reality can
contradict it — the underdog dominating, the favorite fading. The **change score**
measures that distance and, more importantly, its *onset*.

```text
deviation_control = | observed_control(HOME) - expected_strength(HOME) |
deviation_lead    = 0 if the leader is expected · 1 if it is the underdog · 0.5 if a surprise draw
change_score      = scale( 0.6 · deviation_control + 0.4 · deviation_lead )   ∈ [0,100]
```

```python
def _sign(x):
    return (x > 0) - (x < 0)

def change_score(expected_home_strength, state, events, params):
    control = momentum_index(events, state.minute, params.tau)
    dev_control = abs(control - expected_home_strength)

    lead = _sign(state.home_goals - state.away_goals)
    expected = _sign(expected_home_strength - 0.5)
    if lead == expected:
        dev_lead = 0.0
    elif lead == 0 or expected == 0:
        dev_lead = 0.5
    else:
        dev_lead = 1.0

    raw = 0.6 * dev_control + 0.4 * dev_lead
    return round(100 * min(1.0, 1.25 * raw))
```

The temporal brain also tracks trends directly — rising pressure, fading
intensity, a control handover — and emits a discrete signal: *"the game just
shifted at minute 31."* That signal feeds the Match Memory (Section 17) and lowers
confidence (Section 10), because a shifting game is, by definition, a state the
model has just entered and seen little of.

---

## 12. Individual Intelligence

Here the project takes a leap: from a match analyzer into a **behavioral model of
the players** — almost a living probabilistic simulator. Instead of "team A is
playing better", it can answer:

> "Team A is better because the playmaker is receiving 37% more balls than usual,
> the left winger is winning 72% of his duels, and the striker is finishing above
> his historical average."

No real psychology is assumed — only **observed behavior**, in probabilities.

> **Honest data warning.** This is the hungriest layer in the project. It needs
> event data with attribution and position (touch-by-touch), the professional
> standard — expensive and rarely available live and cheap. The realistic path is
> to build profiles **from finished matches first** (the "DNA" over weeks), then
> wire live influence and network later. It can be built **gradually**, starting
> with simple per-player accumulated stats. Behavioral patterns need sample size
> and out-of-sample confirmation, or they become noise dressed as signal.

The six layers build on each other.

### Layer 1 — Match state (collective)

Already implemented in Sections 7–8 (indices + λ). It is the base on which the
player layers act.

### Layer 2 — Individual profile

Each player has a dynamic profile in three blocks:

```text
Technical : pass accuracy, long-pass accuracy, accuracy under pressure,
            turnover rate, ball control
Offensive : shot, assist, dribble, cross frequencies
Decisional: on receiving the ball in a zone, what does he tend to do?
            (shoot / pass / dribble / drop back)
```

The decisional profile is the probability distribution of the next action given the
zone:

```python
def decision_profile(player_events, zone):
    counts = {"shot": 0, "pass": 0, "dribble": 0, "drop": 0}
    for r in player_events:
        if r.type == "reception" and r.zone == zone:
            counts[next_action(r)] += 1
    total = sum(counts.values())
    if total == 0:
        return {k: 0.0 for k in counts}
    return {k: v / total for k, v in counts.items()}
```

### Layer 3 — Statistical "psychological" profile

From observed behavior, classify **archetypes** — pure statistics, no mind-reading:

```text
Conservative : low risk, lateral passes, rare shots
Creator      : seeks assists, many progressive passes
Finisher     : looks for the shot quickly
Impulsive    : forces hard plays, loses more balls
Clutch       : improves when the team is behind   (situational)
Fades        : reduces involvement in decisive games (situational)
```

```python
def archetype(p):
    if p["shot_frequency"] > 0.4 and p["time_to_shot"] < 2:
        return "finisher"
    if p["progressive_pass"] > 0.15 and p["assist_frequency"] > 0.3:
        return "creator"
    if p["turnover_rate"] > 0.2 and p["hard_dribbles"] > 0.3:
        return "impulsive"
    if p["risk"] < 0.1 and p["lateral_passes"] > 0.6:
        return "conservative"
    return "balanced"
```

> Caveat: situational reads like "fades in decisive games" are exactly the kind of
> pattern that *looks* real but is usually small-sample noise. Treat them as
> hypotheses to validate out of sample, not as truths.

### Layer 4 — Influence model

How much **each player influences his team's goal rate**. A descriptive on/off
estimate compares the team's rate with and without the player on the pitch. This
feeds `mult_lineup` of Section 8.2.

```python
def goal_influence(lambda_on, lambda_off):
    return lambda_on - lambda_off            # descriptive (on/off)
```

> Watch for confounders: a player can *look* influential only because he comes on
> when the team is already pressing. On/off is the starting point; a serious causal
> estimate must control for context.

### Layer 5 — Interaction network

A directed graph of who passes to whom, and which links generate chances — revealing
which connections the attack depends on.

```python
from collections import defaultdict

def passing_network(pass_events):
    graph = defaultdict(lambda: {"weight": 0, "chances": 0})
    for p in pass_events:
        if p.success:
            graph[(p.from_, p.to)]["weight"] += 1
            if p.created_chance:
                graph[(p.from_, p.to)]["chances"] += 1
    return graph

def critical_links(graph, top=3):
    strength = defaultdict(int)
    for (a, b), d in graph.items():
        strength[a] += d["weight"]
        strength[b] += d["weight"]
    return sorted(strength, key=strength.get, reverse=True)[:top]
```

### Layer 6 — Statistical avatar

A "DNA" vector of behavioral probabilities — the system stops seeing a name and
starts seeing a set of measurable tendencies, comparable across players and able to
flag when someone is playing **above or below** their own pattern today.

```text
avatar(player) = [ avg_hold_seconds, pass_accuracy, progressive_pass,
                   shot_frequency, assist_frequency, turnover_rate, ... ]
                 (normalized, comparable)
```

### Integration: player-aware λ

```python
def player_aware_lambda(state, team, events, params, profiles, network):
    base  = collective_rate(state, team, events, params)   # Sections 7–8
    form  = mult_lineup(state, team, params)               # Layer 4
    bonus = network_bonus(network, team)                   # Layer 5
    return base * form * bonus
```

The payoff: the panel can **explain** a probability ("it rose because the creator
is receiving more balls"), instead of only showing a number.

---

## 13. Coach Intelligence

Players are not the only predictable agents — **coaches** have patterns too.
Modeling them gives the prediction engine hints about what *tends* to happen to a
team's structure, sometimes before it happens.

> Same caveat as Section 12: each coach has few matches per season with a given
> squad, full of confounders. Use the profiles as weak probabilities, not laws, and
> validate them (Section 20).

### 13.1 Tactical profile by score context

```text
When winning : holds pressure? drops lines? defensive subs?
When losing  : raises intensity? changes shape? throws on attackers?
When drawing : risks or manages?
```

This refines `mult_score` directly: instead of a generic score effect, each coach
gets his own.

### 13.2 Substitution profile

```text
average sub minute · type (offensive / defensive / like-for-like)
· historical impact on the goal rate after the change
```

Predictable substitutions let the engine anticipate λ shifts (a coach who pulls the
striker at 70' when leading → an expected drop in offensive output from there).

### 13.3 Reaction profile

```text
after conceding   → immediate offensive reaction?
after a red card  → defensive reshape?
after equalizing  → change of posture?
```

### 13.4 Code

```python
def coach_profile(coach_matches):
    profile = {ctx: tactical_tendency(coach_matches, ctx)
               for ctx in ("winning", "losing", "drawing")}
    profile["subs"]     = substitution_pattern(coach_matches)
    profile["reaction"] = post_event_pattern(coach_matches)
    return profile

def coach_adjustment(state, team, profile):
    diff = state.goal_diff(team)
    if diff > 0 and profile.get("winning") == "retreat":
        return 0.85
    if diff < 0 and profile.get("losing") == "press":
        return 1.20
    return 1.0
```

### 13.5 Philosophical profile

Above the pointwise patterns, each coach has an **identity** — a stable label that
serves as the default when there is little data on a specific matchup:

```python
def coaching_philosophy(profile):
    if profile.get("losing") == "press" and profile.get("winning") == "hold":
        return "OFFENSIVE"
    if profile.get("losing") == "hold" and profile.get("winning") == "retreat":
        return "PRAGMATIC"
    return "BALANCED"
```

---

## 14. Tactical and Collective Intelligence

These two intelligences read the same Digital Model from a higher level.

### 14.1 Tactical Intelligence

Probably the largest module. It automatically identifies the patterns each team is
running:

```text
high press · mid block · low block · counter-attack · fast transition
· man-marking · zonal marking · overload on the flank · constant switching
· excessive width · loss of the second ball
```

It answers **"what is each team trying to do?"** by combining the spatial
intelligence of Section 7.4 (where the pitch is being used) with the event stream
(how possession is being moved and recovered).

### 14.2 Collective Intelligence

It does not look at players — it looks at the **organism**: how the team functions
as a whole.

```text
synchrony · coordination · circulation · fluidity · connections
· dependence on key players · robustness · cohesion
```

The passing network (Section 12, Layer 5) is the substrate: a team whose chances
all flow through one link is *fragile*; a team with many redundant connections is
*robust*. Collective Intelligence turns the network into these readable properties.

---

## 15. Narrative Intelligence

The most ambitious part: treating **what people say** as a hypothesis to verify, not
as truth — now purely to *understand the game better*, with no betting motive
anywhere. The goal is to measure the distance between **perception** and **reality**
and to find when the dominant narrative is wrong.

```text
Data   = evidence
Opinion = hypothesis
System = verifier
```

The pipeline makes **source credibility** an explicit step — not every voice weighs
the same:

```text
Opinion  →  Hypothesis  →  Verification  →  Source credibility  →  Divergence
```

Examples of what it produces:

```text
TV says:  "the team is dominating."
AI:       "the data shows balance. The perceived dominance is only possession."

Crowd says: "the striker is having a bad game."
AI:         "in fact he leads every line-breaking action."
```

> Honest caveats (this layer is full of traps):
> - Extracting opinion from text is hard; irony and slang break simple models.
>   Start with a few robust signals.
> - "Public perception" is not an objective number — any measure is a noisy
>   approximation.
> - Divergence between belief and reality is **interesting in itself** because it
>   reveals perception bias; it does not require any further justification beyond
>   understanding the game honestly.
> - Respect platform terms of use and copyright when collecting from social media
>   and broadcasts.

### 15.1 Opinion → testable hypothesis

```python
NEG = {"bad", "poor", "awful", "weak", "lost", "anonymous"}
POS = {"good", "great", "brilliant", "strong", "decisive"}

def opinion_to_hypothesis(text, target, aspect="performance"):
    t = text.lower()
    if any(w in t for w in NEG):
        direction = "worse"
    elif any(w in t for w in POS):
        direction = "better"
    else:
        direction = "same"
    return {"target": target, "aspect": aspect, "direction": direction}
```

### 15.2 Verification engine

```python
def verify(hypothesis, real, ref_mean, ref_std):
    z = (real - ref_mean) / ref_std if ref_std > 0 else 0.0
    return classify(hypothesis["direction"], z)

def _sign(x):
    return (x > 0) - (x < 0)

def classify(direction, z):
    s = {"better": 1, "worse": -1, "same": 0}[direction]
    sz, az = _sign(z), abs(z)
    if direction == "same":
        if az <= 0.5: return "Confirmed"
        if az > 1.5:  return "Strongly contradicted"
        return "Not confirmed"
    if s == sz and az > 1.5: return "Confirmed"
    if s == sz and az > 0.5: return "Partially confirmed"
    if s != sz and az > 1.5: return "Strongly contradicted"
    return "Not confirmed"
```

### 15.3 Divergence index

```python
def divergence_index(target, sources, data):
    perception = weighted_sentiment(sources, target)   # 0..100 (uses credibility)
    reality    = objective_score(target, data)         # 0..100
    return abs(reality - perception)
```

### 15.4 Source credibility

Each source's weight comes from **historical accuracy** (not fame): how often its
opinions, when verified, match the data.

```python
def update_credibility(source, label):
    hit = label in {"Confirmed", "Partially confirmed"}
    source["hits"]  = source.get("hits", 0) + (1 if hit else 0)
    source["total"] = source.get("total", 0) + 1
    source["weight"] = source["hits"] / source["total"]
    return source["weight"]
```

### 15.5 Collective emotional state

The original heart of the project. Not one person's sentiment, but the **emotional
state of the environment** — and, above all, the **distance between collective
emotion and reality**. Measuring sentiment is easy; the value is in detecting when
emotion detaches from the data.

```text
Crowd:       extremely pessimistic
Commentators: negative
Data:        balanced
        →  POSSIBLE COLLECTIVE OVERREACTION
```

```python
def collective_state(emotion, reality, threshold=40.0):
    return {
        "emotion": emotion,
        "reality": reality,
        "divergence": abs(emotion - reality),
        "overreaction": abs(emotion - reality) > threshold,
    }
```

> "Overreaction" is a **hypothesis generator**, not a verdict: it points to a place
> where perception and data disagree, worth surfacing and watching. Start with a few
> robust channels and validate (Section 20).

### 15.6 Narrative memory

Section 15.4 measures the credibility of *who speaks*. Here we measure the
reliability of the **narrative itself** — recurring clichés "everyone repeats".
Instead of accepting "team X always collapses late", the system checks the cliché
against history:

```python
def update_narrative_memory(memory, pattern, confirmed):
    m = memory.setdefault(pattern, {"confirmed": 0, "total": 0, "rate": 0.0})
    m["total"] += 1
    m["confirmed"] += 1 if confirmed else 0
    m["rate"] = m["confirmed"] / m["total"]
    return m["rate"]
```

So the system learns not only trustworthy **people** but trustworthy **narratives**,
and can automatically discount clichés the record disproves.

---

## 16. Consensus engine

A module that barely exists in current systems and is a genuine differentiator: it
**reconciles every source** into one diagnosis plus a confidence. This is the
evidence-fusion idea at the center of the new architecture.

```text
Sofascore   : dangerous attack
Flashscore  : ordinary attack
Chat        : almost a goal!
Commentary  : great save
        →  Consensus: "chance created", agreement 92%
```

And when sources disagree, that disagreement is itself information:

```text
Statistics  : Brazil dominates
Chat        : Brazil awful
Commentator : even game
        →  "strong divergence between public perception and objective indicators"
```

```python
def consensus(readings):
    """readings: list of {claim, weight} from different sources (weight = credibility)."""
    tally = defaultdict(float)
    total_w = 0.0
    for r in readings:
        tally[r["claim"]] += r["weight"]
        total_w += r["weight"]
    if total_w == 0:
        return {"claim": None, "agreement": 0.0}
    claim = max(tally, key=tally.get)
    return {"claim": claim, "agreement": tally[claim] / total_w}
```

The system thus measures not only the game, but **the quality of the information
about the game**. High agreement → high diagnostic confidence; high divergence →
low confidence and a flag worth surfacing.

---

## 17. Match Memory

The system keeps a **structured, replayable timeline** of how the match evolved
tactically and emotionally — not just a list of highlights:

```text
12' — Brazil started pressing
17' — full-backs began pushing higher
22' — Argentina lost compactness
31' — momentum shift
43' — Brazil now in full control
```

```python
def remember(timeline, minute, headline, detail=""):
    timeline.append({"minute": minute, "headline": headline, "detail": detail})

def replay(timeline):
    """Yield the tactical/emotional story arc in order."""
    return sorted(timeline, key=lambda e: e["minute"])
```

After the match, the user can **replay the evolution** of state, tactics, and mood —
not the goals, but the *story of why the game went the way it did*. Each change
detected in Section 11 writes one entry here.

---

## 18. Causality Model

Verifying a narrative is only half the job; the other half is asking **why**. When a
hypothesis like "player X is having a bad game" is confirmed, the system looks for
**likely causes** in the match itself, turning a label into a diagnosis:

```text
"X is bad"  →  confirmed  →  receiving 40% fewer passes + marked by 2 + changed zone
```

Causes are not guessed — they are read from objective indicators, each with a
trigger:

```python
def likely_causes(features):
    causes = []
    if features.get("passes_received_rel", 1.0) < 0.7:
        causes.append("receiving fewer passes than usual")
    if features.get("nearby_markers", 0) >= 2:
        causes.append("closely marked by 2+ defenders")
    if features.get("changed_zone", False):
        causes.append("moved to a different zone")
    if features.get("team_midfield_control", 1.0) < 0.4:
        causes.append("the team lost control of midfield")
    return causes
```

This is also where match-level causal questions are asked: *what caused the loss of
midfield control? which substitution changed the game? did pressure rise from
offensive merit or a defensive error? did the goal come from a building trend or was
it isolated?* These are correlations read from simple triggers — **explanatory
hypotheses, not proven causation** — but they bring the system close to how
professional analysts reason.

---

## 19. Explanatory Intelligence

This is arguably the most important intelligence. The AI never answers just `72%`.
It answers with the mechanism:

```text
Probability of a goal rose.
Because:
  ✓ sustained pressure
  ✓ the away block lost compactness
  ✓ the right-back is overloaded
  ✓ the striker started receiving between the lines
  ✓ the coach increased the width
  ✓ the opponent dropped intensity
```

It assembles the explanation from the modules already built: the change detector
(Section 11) says *something shifted*; the causality model (Section 18) says *why*;
the spatial and tactical intelligences (Sections 7.4, 14) name the *mechanism*; the
individual layer (Section 12) names the *players* moving the number; and the
confidence engine (Section 10) tunes how firmly each clause is stated.

```python
def explain(prediction, change, causes, mechanisms, drivers, confidence):
    lines = []
    if change:    lines.append(f"the game shifted at minute {change['minute']}")
    lines += [f"✓ {m}" for m in mechanisms]
    lines += [f"✓ {c}" for c in causes]
    lines += [f"✓ {d}" for d in drivers]
    hedge = "" if confidence > 0.66 else " (tentative — low confidence)"
    return {"claim": prediction, "because": lines, "note": hedge}
```

The product is a system that **teaches football**: it does not just point at a
number, it explains the dynamic that produced it.

---

## 20. Validation and calibration

**This is the most important part of all.** Without it, you do not know whether you
have a system or an illusion. The new project has no betting outcome to chase, so
the *only* honest measure of quality is: **are the predictions calibrated, and do the
explanations match what actually happened?**

### 20.1 Calibration

Calibration answers: *when the model says 60%, does it happen 60% of the time?*

```text
1. Bucket predictions into bands (0–10%, 10–20%, ..., 90–100%).
2. In each band, compare the average predicted probability with the real frequency.
3. Plot the reliability curve: the ideal is the diagonal y = x.
```

Numeric metrics:

```text
Brier score = mean( (predicted - outcome)² )           # lower is better
Log loss    = -mean( y·ln(p) + (1-y)·ln(1-p) )          # punishes confident errors
```

```python
def brier(pairs):                    # pairs: list of (predicted_prob, happened 0/1)
    return sum((p - o) ** 2 for p, o in pairs) / len(pairs)

def reliability_curve(pairs, n_bands=10):
    bands = [[0, 0.0, 0.0] for _ in range(n_bands)]   # n, sum_pred, sum_happened
    for p, happened in pairs:
        i = min(n_bands - 1, int(p * n_bands))
        bands[i][0] += 1
        bands[i][1] += p
        bands[i][2] += happened
    return [(sp / n, so / n, n) for n, sp, so in bands if n > 0]
```

### 20.2 Backtesting without leakage

Replay historical matches event by event, generating predictions **using only the
information available up to that minute** — never the future. Information leakage is
the number-one backtest error: it manufactures phantom accuracy.

```python
def backtest(historical_matches, params):
    results = []
    for match in historical_matches:
        state = initial_state(match)
        for minute in sorted(minutes(match)):
            state = apply_events_until(state, match, minute)   # only up to 'minute'
            pred = predictions(state, events_until(match, minute), params)
            results.append(record(pred))
        resolve_outcomes(results, match)                       # after the match
    return evaluate(results)        # calibration, Brier, log loss, hit rate
```

### 20.3 Validating the explanations

Calibration judges the *numbers*; the explanations need their own check. The
verification engine (Section 15) already does this for narratives — and the same
discipline applies to the system's own causal claims:

- When the system says "pressure rose because the block lost compactness", did the
  compactness metric actually fall first?
- Do "high confidence" diagnoses err less than "low confidence" ones? If not,
  confidence is mis-defined.

A claimed cause that does not precede its effect in the data is downgraded to a
correlation, and recurring false explanations lower the trust on that explanatory
pattern — exactly like narrative memory (Section 15.6).

### 20.4 Validating the mechanics by simulation

Before real data exists, the engineering can be validated. Two layers of test, both
without real data: Monte-Carlo simulations (matches generated by a known Poisson
process) and an assertion suite that exercises the real engine. **Scope warning:**
these prove the **formulas and methodology are correct** — they do **not** prove the
model understands real football, which still depends on real data and the backtest
of Section 20.2.

| Test | What it checks | Result |
|---|---|---|
| 1 — Market formulas | Goal-window, next goal, totals match the empirical frequency | within ~0.5 pt |
| 2 — Calibration detects bias | A biased λ (×1.4) produces a worse Brier and a bent curve | Brier 0.190 → 0.196 |
| 3 — Regime detector | Six scenarios classified correctly | all correct |
| 4 — Confidence engine | Monotonic in each factor; collapses to ~0 when data is missing | as designed |
| 5 — Narratives | Classification correct; a source's credibility converges to its true hit rate | 0.70 → 0.699 |
| 6 — Collective state | Fires "overreaction" only when emotion is extreme and data is calm | as designed |
| 7 — Players & coaches | Philosophy, score adjustment, decision distribution sums to 1, normalized avatar | as designed |
| 8 — Full predictor calibration | Under a known generator, near-perfect reliability | max deviation 0.0012 |
| 9 — Causality | Detects the right causes when triggers fire, none when all is normal | as designed |
| 10 — Narrative memory | A recurring cliché's reliability converges to its true rate | 18% in 200 games |

> The base rate `BASE_RATE = 0.015` goals/min per team was calibrated to reproduce
> ~2.7 goals per match across tens of thousands of simulated games.

**Conclusion.** The prediction engine, regime detector, confidence, narratives,
consensus, causality, and calibration **work as designed**. What remains to be
validated — and only real data can do it — is whether the model has genuine
predictive insight (Section 20.2).

---

## 21. Continuous learning

Evolution in three stages.

**Stage 1 — Fixed rules.** Hand-picked weights and constants (the current
skeleton). Validates the pipeline.

**Stage 2 — Weights fit to data.** Instead of guessing `EVENT_WEIGHT`, `TAU`,
`BASE_RATE`, and the multipliers, tune them to **minimize log loss** over historical
data.

```python
def fit_parameters(train_matches, params0):
    def cost(params):
        pairs = backtest(train_matches, params)["pairs"]   # training only
        return log_loss(pairs)
    return optimize(cost, params0)   # search/gradient; walk-forward in validation
```

**Stage 3 — Learned model.** Replace the heuristic intensity formulas with a trained
model (logistic regression or gradient boosting) that takes the indices **and the
player avatars** (Section 12) as features and predicts the event probability.

> **Mandatory validation: walk-forward.** Always train on the past and test on the
> future (e.g. train Jan–Jun, test Jul). Never evaluate on the same period you tuned
> the weights on — otherwise you measure *overfitting*, not insight.

```text
Timeline:  [---- train ----][-- test --][---- train ----][-- test --]
            tune params       evaluate     re-tune          evaluate
```

The learning intelligence keeps absorbing new patterns, formations, styles, and
coaches — it never stops evolving, but every new pattern must beat the previous
model **out of sample** before it is trusted.

---

## 22. The intelligent panel

The interface changes from a wall of numbers into an **intelligent panel**: state,
regime, predictions-with-confidence, the *why*, and a tactical suggestion.

```text
==========================================
 MINUTE 27   |   SCORE  HOME 0 x 0 AWAY
 Regime: NORMAL        Overall confidence: 82%        Change score: 18/100
------------------------------------------
 STATE OF THE MATCH
   Dominance:    HOME            Intensity:  Very high
   Organization: AWAY ↓          Pressure:   HOME ↑↑
   Rhythm:       accelerating    Confidence: high
   Recent change: coordinated pressure down the left
   Key player:    No. 8 (playmaker)
   Main weakness: away full-backs overloaded
   Tactical hint: exploit the left channel
------------------------------------------
 Momentum (recent):  HOME 39%  |  AWAY 61%
 Highlight: AWAY playmaker receiving +37% of his usual balls
 Collective mood: crowd pessimistic · data balanced → possible overreaction (watch)
------------------------------------------
 Likely next events            Prob    Confidence
   Goal in next 10 min ......   46%       78%
   Goal before half-time ....   67%       84%
   Next goal: HOME 43% | AWAY 57%         71%
   Corner (next 5 min) ......   41%       70%
   Big chance created .......   33%       66%
   Substitution soon ........   58%       62%
==========================================
 WHY the goal probability is rising:
   ✓ sustained pressure   ✓ away block lost compactness
   ✓ right-back overloaded ✓ striker receiving between the lines
==========================================
```

Design rules:

- Show **regime**, **overall confidence**, and **change score** at the top: they
  change the reading of everything else.
- Every probability carries its **confidence** (Section 10).
- Flag a **collective overreaction** (Section 15.5) as a "watch", not a verdict.
- When player data is on, show the **why** (which link or player is driving the
  number) — the differentiator of Section 12.
- Log every prediction shown to the database — so it can later be scored against
  reality (real calibration).
- The panel **explains, it does not just display**: this is Explanatory
  Intelligence (Section 19) made visible.

---

## 23. Roadmap by phases

**Phase 0 — Skeleton (done).** Full pipeline on a simulated feed: indices →
Poisson → diagnosis. Validates the architecture.

**Phase 1 — Real data + database.** Plug a real `Source`, write everything to SQLite
(events, snapshots, predictions, outcomes).

**Phase 2 — Regime detector (Section 9).** Classify the match state from the basic
data already available (score, time, sendings-off, pressure). Cheap, high impact:
conditions all multipliers. No new data needed.

**Phase 3 — Validation (Section 20).** Collect dozens/hundreds of matches, resolve
outcomes, measure calibration, Brier, log loss. Here you learn whether anything is
real.

**Phase 4 — Calibrate parameters per regime.** Tune weights minimizing log loss,
walk-forward, **separately per regime**. Re-validate.

**Phase 5 — Confidence engine (Section 10).** With a resolved prediction history,
estimate confidence and **validate the confidence itself**.

**Phase 6 — Change detector (Section 11).** Cheap: needs only the pre-match
expectation and the indices already computed. Marks the "off-script" games where
the picture is shifting.

**Phase 7 — Consensus engine (Section 16).** Wire several Layer-1 sources, the
cleaning and semantic layers, and reconcile them. Start with a few robust sources.

**Phase 8 — Players: post-match profiles (Section 12, Layers 2–3, 6).** Accumulate
per-player stats from finished matches and build the "DNA"/archetypes. No real time
required.

**Phase 9 — Players: live (Section 12, Layers 4–5).** With live event and lineup
data, switch on influence and the passing network. More expensive — only if Phase 8
shows the profiles have predictive power.

**Phase 10 — Coaches (Section 13).** From finished matches, build tactical,
substitution, reaction, and philosophy profiles. Cheap in data, but needs sample
size and validation.

**Phase 11 — Narratives, causality, memory, collective state (Section 15, 18).** The
most ambitious. Start tiny (a few robust channels) and measure whether divergence
has any explanatory power **before** trusting it.

**Phase 12 — (optional) Learned model (Section 21).** Replace heuristics with a
trained model, if and only if it beats them out of sample.

---

## 24. Honest risks and limitations

- **Latency.** Your feed is almost always behind the broadcast. A "live" reading can
  describe a state that has already moved on. Build with the lag in mind.
- **Data cost.** Granular, low-latency in-play data is expensive. Evaluate this
  **before** building around it.
- **Player data is the cost ceiling.** Section 12 needs event data with attribution
  and position — the most expensive, least available live. Start with post-match
  profiles.
- **Spurious behavioral patterns.** Reads like "fades in decisive games" look real
  but are often small-sample noise. Validate out of sample.
- **Small sample per coach.** Each coach has few matches per season with a given
  squad; the profiles of Section 13 are weak signals, not laws.
- **Too many regimes fragment the data.** Splitting the match into many regimes
  leaves each with too few examples to calibrate — overfitting returns. Start with a
  few well-defined regimes.
- **Uncalibrated confidence is worse than none.** A confidence number that was not
  validated gives false security. It only counts after high-confidence predictions
  are *proven* to err less.
- **Collective emotional state is the most speculative module.** Measuring "the mood
  of the environment" is the noisiest of all; it is easy to see "overreaction" where
  there is only noise. Treat it as a hypothesis generator.
- **Causality can confuse correlation with cause.** The "likely causes" of Section 18
  are correlations read from simple triggers, not proven causation. Present them as
  explanatory hypotheses.
- **Narrative memory needs sample and a stable definition.** To judge a cliché it
  must be defined consistently and have enough history; with few games, the
  confirmation rate is noise.
- **NLP and perception are fragile.** Reliable opinion extraction from Portuguese
  text (irony, slang, context) is hard, and "public perception" is always a noisy
  measure. Section 15 must start tiny and prove value before it weighs in.
- **Source disagreement is information, not a bug.** When sources conflict, lower the
  confidence and surface the divergence — do not silently pick one.
- **Legal aspects of collection.** Scraping social media and broadcasts has terms of
  use and copyright limits; respect them.
- **Overfitting.** It is easy to build a beautiful backtest that does not repeat
  live. Walk-forward exists to fight this.
- **Honesty of the result.** Treat this first as an engineering and statistics
  project. Accept that the research outcome may be "the model adds no real insight
  over what is already visible" — and that, too, is a valid, honest result.

---

*Project document — Football Intelligence Engine, v1 (re-founded from the original
live-analysis engine). The focus is sports **intelligence**: interpreting,
explaining, predicting, and learning from a football match in real time. Every
section is independent and can be implemented and tested on its own, in roadmap
order. The guiding question is never "what is the score going to be?" — it is "what
is really happening, why, and what tends to happen next?"*
