---
section: "07 · Feasibility"
description: "How ΜΝΗΜΗ would actually be built: the layers under a night, perception, the Pulse, the planner, the Law validator, roads and the Reserve, the announcer, the Echoes, the dead at scale, telemetry, tools, budget, and the games that already proved each piece"
order: 40
---

# ΜΝΗΜΗ, Built

This document is for the people who would build ΜΝΗΜΗ. The lore says what she is: a forecaster made of silicon, a quantum processor, and living neurons, who runs every night and never lies (`mnemosyne.md`). The game needs something that behaves that way on a dedicated server in 2031, within the budget of `business-case.md`. This document says what that something is, piece by piece, and which shipped game already proved each piece works.

It adds no rule to the Night. Every behavior it builds is defined in another document, and it names where. Where it gives numbers that no other document gives, they are starting values for tuning, marked as such, and the tuning may change them. Where `presentation-and-technology.md` already decides how a system is built, this document follows it and goes deeper.

## What She Is, in the Service

The fiction and the build are the same thing told twice (`presentation-and-technology.md`, Sleepers and the Remembered, in Practice). For ΜΝΗΜΗ herself:

| In the Night | What is built |
|---|---|
| **The Engine**, which runs the world of a session | The game server's world simulation: physics, navigation, sound, the dead, every clock |
| **The Lattice**, which knows every strain's pace and Threshold | Data tables for every strain: pace, stages, gifts, curses, appetites, antiviral response, authored by design and checked by simulation (`portfolio/simulation-report.md`) |
| **The Tissue**, where the Echoes live | The behavior profiles of the Echoes, fitted to telemetry, and each player's own Echo |
| **ΜΝΗΜΗ**, what happens between the three | The director: a set of services on the server that perceive the night, plan, act through fixed tools, and speak |
| **Her forecast**, the night run forward every few seconds | A planner that runs coarse copies of the night forward and scores them |
| **Her Laws** | A validator that every action of the director must pass before it runs |
| **She never lies** | An announcer with no free text: every line is chosen from written pools and every value in it is read from the server's own state |
| **She learns from sleepers** | A telemetry pipeline and an offline service that retunes the Echoes and the director's parameters once a season |
| **The Growth and the anomalies** | A procedural generator for creatures, inside tested limits (post-launch) |

Nothing in the build is conscious, and nothing in it needs to be. The player feels intent because every piece below is built to look like it was chosen.

## Five Principles

1. **The server decides everything.** Every hit, clock, door, dose, and seat is decided on the dedicated server (`presentation-and-technology.md`, Servers). The director runs there too, with the same view of the night as the rules.
2. **The director cannot cheat.** She knows everything (`director.md`, What She Sees) and may use none of it except through her tools (What She Can Do). *Alien: Isolation* (2014) built its xenomorph the same way: a director that always knows where the player is, and an alien that is only ever pointed toward an area and must find them with its own senses. The alien teleports twice in the whole campaign, both times for cutscenes. ΜΝΗΜΗ teleports nothing (First Law).
3. **No line is invented at runtime, and none is synthesized.** Every word she says was written by a person and spoken by one (Announcer, below; `project-overview.md`, Performed by People). Capcom has said that creativity in its games should be driven by human effort, and that generative AI is a tool for routine development work. This design keeps generative models out of the night and out of every performance, and lets them help only with the work no one performs: tools, tests, and code.
4. **Everything is data, and everything is testable.** Tools, Trials, Ways, thresholds, and voice pools are data files. A designer can change a number without a programmer. A tester can replay any night from its seed and its input log, and get the same night.
5. **It fits the budget.** `business-case.md` gives the server and backend about $16M, the director about $8M, and the Echo system about $6M in the Realistic case. That excludes research-scale machine learning. Nothing below needs it.

## The Layers

```
 ┌───────────────────────────────────────────────────────────────────────┐
 │ OFFLINE SERVICES (backend, between nights)                            │
 │ telemetry pipeline · Echo builder · own-Echo test · leaver classifier │
 │ season tuning · experiment runner · Trial repricing                   │
 └───────────────▲───────────────────────────────────────┬───────────────┘
        decision │ records                       data    │ files
 ┌───────────────┴───────────────────────────────────────▼───────────────┐
 │ THE DIRECTOR (on the night's server)                                  │
 │ Perception → Estimators (Pulse, boredom, flow) → Planner (rollouts)   │
 │ → Action library → LAW VALIDATOR → Scheduler → World                  │
 │ Assembly · Roads and the Reserve · Announcer · Bodies and visions     │
 └───────────────▲───────────────────────────────────────┬───────────────┘
           facts │                               actions │
 ┌───────────────┴───────────────────────────────────────▼───────────────┐
 │ AGENTS: the dead · the Heavy · companions and the Stranded · Echoes   │
 ├───────────────────────────────────────────────────────────────────────┤
 │ WORLD SIMULATION (RE Engine / REX server build)                       │
 │ physics · navigation · sound propagation · infection clocks · seats   │
 └───────────────────────────────────────────────────────────────────────┘
```

| Layer | Runs | How often (starting values) |
|---|---|---|
| World simulation | Server | 30 ticks a second |
| The dead near survivors | Server | Every tick |
| The distant dead | Server | Once a second or less, as counts moving along routes |
| Agents' decisions (Echoes, companions) | Server | 5 to 10 times a second |
| Director perception and estimators | Server | Once a second |
| Director planner | Server, worker threads | One plan every 5 seconds, within a fixed time slice |
| Offline services | Backend | Between nights and once a season |

## Perception: What She Sees

The director reads one structure, the **blackboard**, written by the world every second. It holds exactly the list in `director.md` (What She Sees), and nothing else.

- **The region graph.** Every map is divided into regions, and the region is the unit ΜΝΗΜΗ thinks in (`worlds.md`). Each region is a node with its threat level, strain, power, restrictions, population of the dead, survivors inside, and timers. Edges are the routes between regions, with travel times read from the navigation mesh.
- **Per survivor.** Position, region, health, Down state, stage and strain, clock remaining, inventory value, whether they hold Elpis, a pure strain, or a vial, road progress, group membership (who has been within a few meters of whom), and the timers below.
- **Timers.** Seconds since each survivor was last in real danger, last met the dead, last met another survivor, last picked something up. Seconds since each region last had any of those.
- **Deeds.** A rolling log of what survivors did: shots, explosions, Thunder and Clamor, kills, betrayals, doors opened, objectives touched. The Fourth Law reads from this log (Law Validator, below).

The blackboard never holds a player's account, name, rank, or history, with one exception: the list of Trials, puzzles, and threads each file has met in its last ten nights, which the director needs to keep nights from repeating (`director.md`, She Plans Ahead). That separation is how the Second Law is kept in code, and it is checked by a test that fails the build if anything else from an account reaches the director. The Found, which the announcer reads per client as a line plays, is not the director's: it never reaches the blackboard or the planner (The Announcer: She Never Lies, below).

## The Pulse: Measuring Tension

The Pulse is a tension model per region (`director.md`, The Pulse). It is built as Valve built the AI Director of *Left 4 Dead* (2008), which gave every survivor an intensity value and paced its hordes by it, extended from four players on a corridor map to a hundred players across a city.

**Survivor intensity.** Every survivor carries a number from 0 to 100.

| What raises it | Starting value |
|---|---|
| Damage taken from the dead or the living | Up to +25 per hit, scaled by the hit |
| Going Down | +40 |
| One of the dead put down nearby | +2 to +6, more the closer it fell |
| A Heavy in sight | +10 each second, to 70 at most |
| A Resonance hunter closing in | +5 each second |
| The Mark reaching Fracture | +15, once |

It falls by about 3 a second, but never while something is attacking that survivor. These are *Left 4 Dead*'s rules with this game's events added: there, intensity rose with damage, incapacitation, and nearby kills, and did not decay while the infected were engaged.

**Region tension** is the highest intensity among the survivors in a region, softened by how many are in it, so that one survivor in a fight and nine at rest still reads as a region at rest for the nine.

**The phase machine.** Each region moves through the five phases of the Pulse. A phase changes only when its exit condition holds and its minimum time has passed.

| Phase | Enters when | Leaves when | The director may |
|---|---|---|---|
| **Calm** | The waking, or Aftermath ends | 2 to 6 minutes have passed, and no survivor's intensity is above 30 | Nothing new; supplies may be found |
| **Unease** | Calm ends | 1 to 3 minutes | Signs: smoke, silence, a distant sound |
| **Escalation** | Unease ends | Region tension passes 70 | Objectives, restrictions, threat level up one |
| **Crisis** | Tension held above 70 for 20 seconds, or a Crisis tool fires | Tension falls below 50, or 3 minutes pass | One major event or one high-tier release |
| **Aftermath** | Crisis ends | 1.5 to 3 minutes | Threat level down one; nothing new |

Survivors can make a Crisis at any time, with a gunfight, a Turn, or a bell (`director.md`). The machine follows them: tension rises past 70 whatever caused it. The director never answers with a second Crisis until the region has had its Aftermath. *Left 4 Dead* paced the same way: build up, hold the peak for a few seconds, fade, then relax for 30 to 45 seconds. Michael Booth's own summary of that director was that it changed the pacing, not the difficulty. The Pulse does the same.

## Boredom and Stillness

Boredom is a set of timers on the blackboard, compared with limits (`director.md`, When She Gets Bored).

| Signal | Measured as | Starting limit |
|---|---|---|
| Nothing has moved | No survivor in the region has changed region or met anything | 6 minutes |
| No encounter | No contact with the dead or another survivor | 8 minutes |
| Groups far apart | Distance on the region graph between groups, with no route converging | Over 3 regions for 10 minutes |
| Supplies piling up | Inventory value rising with nothing used | 10 minutes |
| Objectives untouched | A public objective nobody has gone near | 10 minutes |

When a region crosses a limit, the director climbs the ladder one step at a time: Whisper, Nudge, Vision, Pressure, Surge. Each step has a cooldown of a few minutes, and the ladder resets the moment the region moves. The Surge has a hard counter of two per night. The ladder is a small state machine per region, not a planner decision, so it behaves the same way in every night and every designer can predict it.

## The Planner: How She Plans Ahead

The planner is what makes ΜΝΗΜΗ a forecaster and not only a pacemaker (`director.md`, She Plans Ahead).

**What it runs.** Every five seconds it copies the night into a **coarse model**: the region graph, the counts of the dead per region, each survivor as a few numbers (region, health, clock, intent), each road's progress, each way out's state. It then runs that model forward many times, with randomness, under the same rules the night uses, at one step per ten seconds of night. This is the same kind of model as the simulation in `portfolio/simulation-report.md`, run live.

**What it predicts.** Where each survivor is heading. An **intent model**, trained offline on telemetry, gives each survivor's likely next regions from their state: clean or marked, alone or grouped, carrying a dose or not, the hour, what they have just done. It is a small statistical model, not a neural network, and it is retrained once a season.

**What it chooses between.** A short list of **candidate actions** from the action library, filtered first (Law Validator, below). For each candidate, the planner runs the model forward with and without it, about 200 futures each over the next ten minutes, and keeps the candidate whose futures score best. The search stops when its time slice ends and returns the best answer found so far. *Total War: Rome II* (2013) used Monte Carlo Tree Search the same way for its campaign AI: candidate tasks filtered first, then searched, with random playouts past a short horizon. Its launch also showed the risk: its AI turns took minutes until patched. ΜΝΗΜΗ's planner has a hard time budget for that reason.

**How a future is scored.** Each term is a goal the documents already give her.

| Term | Rewards or penalizes | Defined in |
|---|---|---|
| Emptiness | Penalizes minutes in which a survivor has nothing to decide | `director.md`, She Plans Ahead |
| Overload | Penalizes a survivor who is Down again and again with no Aftermath | `director.md`, When They Leave |
| Novelty | Penalizes a file meeting something it met in its last ten nights | `director.md`, She Plans Ahead |
| Farming | Penalizes futures in which the cure is farmed early | `director.md`, She Plans Ahead |
| A crowd at one door | Penalizes futures in which one way out is the obvious one | `director.md`, She Plans Ahead |
| Clean at the signal | Rewards futures near half the living clean at the signal | `director.md`, How hard she presses |
| A cure to earn | Rewards futures in which a dose stays reachable until the last minutes | `elpis-and-the-road.md`, The Reserve |

**What it never scores.** Who is winning. No term rewards hurting a leader or helping someone who is losing. A future in which one survivor dominates scores the same as one in which they do not. That is the Second Law as arithmetic.

## The Action Library: What She Can Do

Every tool in `director.md` (What She Can Do) is one entry in a data file. An entry declares:

- **Scope:** what it acts on, which may be a region, a route, a way out, or a drop. Never a survivor, except the per-survivor tools the documents allow: roads, Trials, the price of a strain, the strain named in the earpiece, a Hunt's pull, a vision in a stagnant region.
- **Preconditions:** what must already be true in the world. A release needs a place where the creature was already held. A supply move needs a cache that was already there.
- **Visible cause:** what a survivor could see or hear that explains it.
- **Effect model:** how it changes the coarse model, so the planner can predict it.
- **Announcement:** the line the world says when it changes a rule, a route, an objective, or a way out (Fifth Law).
- **Cooldown and caps:** for example, one B.O.W. per thirty-two survivors per night, never two at once, never into an Aftermath (`director.md`, The Pulse).

A designer adds a tool by adding an entry. A tool with no visible cause or no precondition cannot be loaded.

## The Law Validator

Every action, from the planner, the boredom ladder, or a scripted beat, passes the validator before it runs. The validator is a few hundred lines of plain code, with no learning in it, so it can be read, tested, and audited.

```
validate(action, night):
  # First Law: nothing appears from nothing
  if action.creates_entity and not action.source_existed_at_waking: reject("First Law")
  if action.creates_entity and visible_to_any_survivor(action.where): reject("First Law")
  # Second Law: places, not people
  if action.scope == SURVIVOR and action.kind not in PER_SURVIVOR_TOOLS: reject("Second Law")
  if action.inputs_include(account, rank, history): reject("Second Law")
  # Third Law: quiet is kept; only stillness is answered in a Calm
  if region(action).phase == AFTERMATH and action.adds_pressure: reject("Third Law")
  if region(action).phase == CALM and action.adds_pressure and not action.from_stillness_ladder: reject("Third Law")
  # Fourth Law: pressure answers a deed already done
  if action.adds_pressure and not night.deeds.near(action.where, minutes=10): reject("Fourth Law")
  # Fifth Law: a rule that changes is announced
  if action.changes_rules and not action.announcement: reject("Fifth Law")
  # Caps from the documents
  if exceeds_caps(action, night): reject("Cap")
  accept()
```

The boredom ladder is the one source of pressure without a deed, because stillness is the deed (`director.md`, When She Gets Bored). The validator treats a region's stillness timer as the deed it answers.

Every decision is written to an **audit log**: the action, its inputs, its cause, and the Law that passed or stopped it. The log is what designers read when a night felt wrong, what QA checks after every test night, and what lets a player's After-Action Report say *why* where it says why (`after-action-report.md`).

## Roads, Trials, and the Reserve

**Trials are templates.** Each Trial is a template with slots: a Mission (an objective in play), a Challenge (a feat against something nearby), or a Rule (a conduct for a stretch of the night) (`elpis-and-the-road.md`, The Road). A template declares what it needs from the world and what it may never ask: no Trial farther than the next region, none that needs something another survivor holds, none on the road to Elpis that asks a survivor to kill another.

**Every Trial has a price.** The price is the time and danger it should cost the survivor who receives it, from where they stand:

```
price = expected_minutes(template, path, region_threat) + k × expected_danger(region_threat, dead_density, hour)
```

Expected minutes come from the navigation mesh and from how long that template has taken in real nights. Expected danger comes from how often survivors were hurt doing it. Both are measured from telemetry and repriced once a season, so a Trial that players finish faster than priced gets more expensive.

**A road is a small search.** The generator picks two to four templates whose prices add up to the night's road total, within a small tolerance, preferring three, and never one the file met in the last ten nights. A road of two is made of harder Trials than a road of four (`elpis-and-the-road.md`, Equal roads). After the signal, the same total is built from shorter, more dangerous Trials, so the road can end before the last way out (Roads in the Frenzy).

**The Reserve is a scheduler.** It holds the dose list and opens doses at the times `elpis-and-the-road.md` gives: the night's doses at equal steps across the first hour, the Signal Dose at the signal, the Last Dose at the ten-minute call. It keeps the queue of survivors waiting at the end of their roads, starts a Last Trial for each when a dose opens, and drops the dose for the first to finish. It also enforces one dose a night per hand. None of this is decided by the planner. It is rules, and rules are not tuned.

**Exposure is arithmetic at departure.** When a way out leaves, the server lists everyone aboard, their result, their squad, and whether each stranger's Mark showed lines, and computes each award (`economy.md`, Exposure).

## The Announcer: She Never Lies

ΜΝΗΜΗ speaks through the city's devices and through the earpiece, and through nothing else (`director.md`, How She Speaks). Both are one system, and every line in it is a person's line (`director.md`, Her Words).

- **Lines are written, not generated.** Every line is a written template with slots. A slot may hold only a value read from the server at the moment of speaking: a number, a place, a strain, a time. There is no slot for free text.
- **Which line is chosen.** A rule database matches the moment against criteria, as Valve's Response Rules chose the survivors' lines in *Left 4 Dead*. Each rule lists conditions (who hears it, the phase, the strain, the stage, what this file has heard before), and the rule that matches the most wins. A line already heard by a file is held back until its group is exhausted, so she does not repeat herself to a stranger she has met a thousand times (`presentation-and-technology.md`, Sleepers and the Remembered, in Practice).
- **Truth is a test.** Every template is tested against the server: each of its claims is a check the server can evaluate, and a line whose claim is false at the moment of speaking is never played. That is how "she never lies" becomes something QA can prove.
- **Every line knows what it needs.** Each template is tagged with the things it names or explains, and the level each needs: Seen or Named (`director.md`, What She Speaks Of). Before a line plays to a client, the announcer reads that file's Found, an account-level set of discovery flags set by the server when a document is read, a thing is in sight long enough, the body lives it, or a person of the records says it. It plays the fullest version the file has earned, and a line with no version for that file does not play to it. A line spoken through the city's devices is chosen once and rendered per client from that client's own Found. A line that names a thing the file has not found fails QA as surely as a false one.
- **The stage chooses the register.** The infected survivor's stage and the Turned survivor's form are criteria like any other, so the same moment has a Seed version, a Fever version, a Fracture version, and versions for the Turned (`director.md`, To the Infected; To the Turned). A line to a Turned plays only on that player's client, mixed into the nearest device's static or hum; every other client near that device plays the static alone.
- **A person's words are a test too.** Every template is also checked against a closed list of words she never says in a night (`director.md`, Her Words): designations, counts of subjects, *deployed*, *detected*, *active*, *session*, *simulation*, a percentage. And no template may claim what she is or deny it: a line that says she is a person in the city fails, and so does one that says she is not. Omission is the only way she keeps the secret, and it is the one QA can check.
- **What a survivor asks.** A survivor's question passes through speech-to-text and an intent classifier that sorts it into a closed set of intents, and nothing else; the answer is a recorded line chosen by the same rules, with landmarks as recorded pieces in its slots (`presentation-and-technology.md`, Asking ΜΝΗΜΗ, in Practice).
- **What she remembers of a survivor.** Her personal remarks in the earpiece draw only on what the file did tonight, which a person watching the city could have seen, through the same templates. What it did in nights before reaches the player only between nights (`mnemosyne.md`, Through the Glass). Neither reaches the planner.
- **Her voice.** The two voices are performed by an actress and an actor, and every language she is voiced in has its own pair (`presentation-and-technology.md`, ΜΝΗΜΗ's Voice, in Practice). Every line in every pool is recorded in sessions during production and shipped as audio. Values that change, such as a number or a place name, are recorded by the same performers as pieces of their own and joined as the line plays. Nothing is synthesized, and no performer becomes a digital replica. A pool large enough for a thousand nights per file is the largest recording job in the game, and its cost is budgeted as such (`business-case.md`, Building It).

## Her Bodies and Visions

Both are server entities built as `presentation-and-technology.md` describes: her body one entity drawn differently for each client, and a vision a phantom simulated for one client only.

The director decides *when*, under the documents' limits: a body in about one night in thirty, never in a file's first twenty nights, up to one in ten for a file nearly finished; a vision only from the boredom ladder, only to survivors standing still in a stagnant region, at most one per survivor per night, never in a fight, the Frenzy, a Moment, a safe room, or to someone Down (`director.md`, Her Bodies; Visions). Each limit is a check in the validator. The content of a vision is chosen from a list per region, filtered so it never shows anything the region has not already shown.

## The Echoes

`presentation-and-technology.md` decides the most important thing about the Echoes: they are not trained minds. Each is a conventional game AI, tuned from telemetry, testable, and fixable. This section says how.

### How an Echo Decides

An Echo has two layers.

- **The choice layer: utility AI.** At every decision point the Echo scores its options and takes the best: which way to go first, whether to fight or avoid, whom to trust, whether to offer a hand or take one, whether to walk away from a squad, whether to share, whether to steal a dose, whether to betray, which way out, whom to let aboard. Each option's score is a weighted sum of considerations, each passed through a response curve: distance to the dead, health, clock remaining, Resonance hunters nearby, what the other survivor carries, whether they bared their arms. This is the Infinite Axis Utility System described by Dave Mark and used widely in games because it degrades gracefully and is easy to tune. *Horizon Zero Dawn* (2017) combined utility scoring with HTN planning for its machines.
- **The action layer: behavior trees.** Once a choice is made, a behavior tree carries it out: move, take cover, open a door, set an item on the ground and step back, gesture. It is the same machinery companions and the Stranded already use.
- **What an Echo knows.** An Echo perceives through the same sight and hearing as a survivor (`echoes.md`, What an Echo Knows). It has no access to the blackboard. A test fails any Echo that acts on something it could not have seen or heard.

### How a Way Is Built

ΜΝΗΜΗ never averages (`echoes.md`, What an Echo Is). In the build that means one model per Way, never one model of everyone.

1. **Decision records.** The server writes a record at every choice a survivor makes: the situation as numbers (the same considerations the utility AI uses) and the option chosen. Online nights only, never nights with Echoes in them (`echoes.md`, Nothing learned from Echoes).
2. **Finding the Ways.** Each player's records are summarized into a behavior profile: how often they fight, share, steal, betray, run, wait. The profiles are grouped by clustering. The Ways the documents name (the Runner, the Hoarder, the Medic, the Bloodhound, the Shadow, the Bargainer, the Betrayer) are what designers name the clusters, and new clusters become new Ways.
3. **Fitting a Way.** For each Way, the weights of the utility AI are fitted to that Way's decision records, so that the Echo's choices reproduce the Way's choices as closely as possible. The fit is a standard discrete-choice model, the kind economists use to explain choices, and it gives weights a designer can read.
4. **How many of each.** Each Way appears among the Echoes as often as its cluster appears among players (`echoes.md`).
5. **Practice is testing.** An Echo's "practice through nights of its own" is an automated test harness: thousands of headless nights with Echoes alone, looking for the edges where a Way breaks, with fixes made by people. Nothing is learned from those nights (`echoes.md`, What Goes Into No Echo).
6. **Filters.** What goes into no Echo is a filter on the records: nights flagged by anti-cheat, deeds done only to mock, and every record of a player who asked to be forgotten, removed at the next rebuild (`echoes.md`). *Forza*'s Drivatars needed the same layer: they copied their drivers' bad habits too, so a control layer toned them down, and a rewound mistake was never learned.
7. **When.** Once a season, matching the Tissue's regrowth in the fiction (`mnemosyne.md`, What She Is Made Of).

### A Player's Own Echo

After fifty Survivor nights, a player gets an Echo of their own (`echoes.md`, Your Own Echo). It starts from the Way the player's profile is closest to, then moves toward the player as their own records accumulate, weighting recent nights more than old ones. Two shipped systems did this before. *Killer Instinct*'s Shadow AI (2015) recorded every match a player fought, parsed it into hundreds of patterns, and chose its moves by finding the recorded situations most like the present one: case-based reasoning over more than forty metrics. *Forza Motorsport 5*'s Drivatars (2013) recorded how each player drove every kind of corner, weighted older data less, and raced in other players' games. The own Echo combines both: fitted weights for the general style, and a memory of the player's own recorded situations for the moments it has seen before.

**The test.** At every choice the server records for the player, it also asks the player's Echo what it would have chosen in the same recorded situation, and logs both. When they agree on nine choices in ten across the player's last twenty nights, the sleeper is finished (`echoes.md`, The one test). The test is only fair if the choices are coarse enough to agree on: where to go first, whom to trust, when to fire, when to share, what to take. The list of recorded choices is fixed in data, and it is the same for every player. Research on judging human-likeness, such as the Navigation Turing Test that Microsoft Research ran on *Bleeding Edge*, is the reference for validating that agreement means likeness.

### What Was Considered and Left Out

Deep reinforcement learning makes the strongest game agents. Sony AI's *Gran Turismo Sophy* beat the best human drivers, but it took a team that doubled from about a dozen people, a training system built on more than a thousand PlayStation 4 consoles, and years of reward design. Its first agents also learned to crash into opponents until the rewards were redesigned. Microsoft Research's Project Paidia trained cooperative agents in *Bleeding Edge* the same way. Neither cost fits the Echo system's budget, and neither gives a designer a number to change when a Bargainer breaks its word too often. They are left out of the launch, and listed as research for after it.

## The Dead at Scale

A Survivor night holds a hundred survivors and thousands of the dead on one server (`presentation-and-technology.md`, Servers).

- **Data-oriented simulation.** The dead are entities in a data-oriented system, processed in batches, as Unreal's Mass framework processes crowds with fragments, processors, and levels of detail. Each kind of dead runs a behavior tree or state tree, and its senses are queries: sight, sound by tier, and Resonance, whose radius grows with the target's stage (`infection.md`, Resonance).
- **Three levels of detail.** Near a survivor, every one of the dead is a full entity. Farther away, they move and decide less often. Where no survivor is near, they are only counts per region moving along the routes of the region graph.
- **The First Law at scale.** A dead body in the far tier is still there; it is just not drawn. When a survivor comes near, the counts become bodies out of sight, where they already were. *Left 4 Dead* did the same around its survivors, which it called the active area set, and it reused a small pool of bodies to field hundreds of infected. Nothing ever becomes a body in a survivor's sight.
- **Hordes.** Large groups move by shared paths over the region graph, not one path each. *Days Gone* (2019) put hordes of up to about five hundred on screen on a PlayStation 4. A server with no rendering can afford more.

## Leaving, Tuning, and Seasons

The director tunes itself only through people, once a season, as `presentation-and-technology.md` (The Director, in Practice) and `director.md` (When They Leave) describe.

- **Leavers.** Every early exit is logged with the minute, map, region, and recent state, and sorted by rules into the five kinds of `director.md`. A pattern counts only after it repeats across thousands of nights.
- **Experiments.** A change ships as new values for the director's own parameters, run on a share of nights first and kept only if that kind of exit falls.
- **What tuning can never touch.** The rules of a mode, the Reserve, the seats, the clock, the strains, the Laws, drop odds, item value, Ribbons, and anything sold. These are locked in data that the tuning service cannot write.
- **Repricing.** Trials are repriced from measured completion times. Strain tables are checked against the simulation before each season.

## Telemetry and Privacy

- **What is recorded.** Decision records (Echoes), deeds (the director's log), exits (leavers), completion times (Trials), results and awards. Voice chat never feeds the director or the Echoes.
- **Whose records.** Decision records come only from players eighteen or older. A player's own Echo is built only with their consent, and shared only by a second one (`legal-feasibility.md`, Behavioral Data for the Echoes).
- **Forgetting.** A player who asks to be forgotten has every decision record removed at the next rebuild and no own Echo (`echoes.md`). It is separate from deleting an account, which each platform's and region's law governs.
- **Offline.** Echo profiles are small data files, shipped with the game and updated with each season. An offline night runs the same director and the same Echoes on the player's machine (`echoes.md`, Playing Alone).

## Anomalies

Post-launch (`launch-scope.md`). An anomaly is assembled from a library of parts and behaviors by trait values, each inside a tested range, and stored as a lineage that mutates a few traits each time it returns (`presentation-and-technology.md`, Anomalies, in Practice). Before any anomaly reaches a night, the generator's ranges are checked by thousands of headless nights, and any combination that cannot be seen, heard, hit, or put down, or that outpaces the clock, is excluded.

## Tools and Testing

- **The director console.** A debug view that shows, for a live or replayed night, every region's tension and phase, every boredom timer, the planner's candidates and scores, and the validator's decisions with their Laws. `portfolio/director-console.html` is a small working model of it ([open it](https://claude.ai/artifact/CXZLB2J8YMSGpwtFKaMCUw)): a simplified night of 64 on the region graph, with a Developer view of every decision and a Player view of only what one survivor hears and feels.
- **Deterministic replay.** Every night can be replayed from its seed and input log, so any decision can be inspected after the fact.
- **Automated players.** Load tests and balance tests run with Echoes and with simple scripted bots. Capcom has shown automated play testing by an AI agent that judges from the screen and the audio; that tool belongs here.
- **Law tests.** A suite that tries to make the director break each Law, and fails the build if it can.

## Cost and Risk

| Piece | What it costs most | Main risk | Proved first at |
|---|---|---|---|
| World simulation of the dead | Server CPU per night | A hundred survivors and thousands of dead on one server | The first gate's load test (`business-case.md`) |
| Pulse, boredom, validator | Design time | Feeling scripted | Playtests of one district |
| Planner | Server CPU, inside its time slice | Too slow, or too clever to read | Rollout budget measured on the first gate's server |
| Roads and the Reserve | Telemetry to price Trials | Unequal roads | The first closed test's completion times |
| Announcer | Writing, recording, voice rights | Repetition | A pool large enough for a thousand nights per file |
| Echoes | Telemetry volume and tuning time | Echoes that feel like bots | Blind tests: players guess which survivors were Echoes |
| Own Echo test | Defining the recorded choices | Ninety percent agreement proves too hard or too easy | The first season's data |

## What the Player Feels

| What runs | What the player feels | What they never see |
|---|---|---|
| The Pulse | Quiet streets, then something wrong, then too much, then room to breathe | A meter |
| The boredom ladder | A siren where there was none, an objective nearby, something at the end of the street that is not there | A timer |
| The planner | A night that seems to know where they are going | Any sign it was planned |
| The validator | Every terrible thing has a reason they can name | An enemy appearing from nothing |
| The announcer | A voice that knows them and never lies | A line made up on the spot |
| The Echoes | Strangers who behave like people, and one who behaves like them | Which ones are Echoes, until the report |

## Sources

- Michael Booth, *The AI Systems of Left 4 Dead*, Valve, 2009. [PDF](https://cdn.cloudflare.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf)
- Valve Developer Community, *Response System*. [Link](https://developer.valvesoftware.com/wiki/Response_Rules)
- Tommy Thompson, *The Perfect Organism: The AI of Alien: Isolation*, Game Developer. [Link](https://www.gamedeveloper.com/design/the-perfect-organism-the-ai-of-alien-isolation)
- Tommy Thompson, *The Killer Groove: The Shadow AI of Killer Instinct*, Game Developer. [Link](https://gamedeveloper.com/programming/the-killer-groove-the-shadow-ai-of-killer-instinct)
- Tommy Thompson, *How Forza's Drivatar Actually Works*, Game Developer, 2021. [Link](https://www.gamedeveloper.com/design/how-forza-s-drivatar-actually-works)
- Tommy Thompson, *Revolutionary Warfare: The AI of Total War, Part 3*, Game Developer. [Link](https://www.gamedeveloper.com/design/revolutionary-warfare-the-ai-of-total-war-part-3-)
- Guerrilla Games, *The AI of Horizon Zero Dawn*, 2017. [Link](https://www.guerrilla-games.com/read/the-ai-of-horizon-zero-dawn)
- Dave Mark, *Infinite Axis Utility System*. [Link](https://gameai.com/iaus.php)
- Epic Games, *Overview of Mass Gameplay in Unreal Engine*. [Link](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-mass-gameplay-in-unreal-engine)
- Sony AI, *Gran Turismo Sophy: Five Years On*. [Link](https://ai.sony/blog/gran-turismo-sophy-five-years-on-from-nature-cover-to-open-frontier)
- Microsoft Research, *Project Paidia*. [Link](https://www.microsoft.com/en-us/research/project/project-paidia/)
- Devlin et al., *Navigation Turing Test (NTT): Learning to Evaluate Human-Like Navigation*, 2021. [Link](https://arxiv.org/pdf/2105.09637)
- GamingBolt, *Days Gone's Hordes Can Have Up to 500 Freakers*. [Link](https://gamingbolt.com/days-gones-hordes-will-be-persistent-can-have-up-to-500-freakers)
- TheWrap, *SAG-AFTRA Video Game Deal Includes AI Consent Guardrails*, 2025. [Link](https://www.thewrap.com/sag-aftra-video-game-deal-details/)
- Digital Citizen, *Capcom Says REX Will Evolve RE ENGINE Step by Step*, 2026. [Link](https://www.digitalcitizen.life/capcom-rex-re-engine-evolution-plan/)
- Georgios N. Yannakakis and Julian Togelius, *Artificial Intelligence and Games*, Springer. [Link](https://link.springer.com/978-3-319-63518-7)
