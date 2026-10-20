# Adaptive Progression

In *Ace Combat MINOZIS*, the story is the progression system. Whatever happens in a cutscene, a briefing, the circle or a sortie changes how the characters fly afterward: the player, the AI wingmen and the enemy. A pilot who trains in a scene flies differently in the next mission. A pilot who is hurt flies more carefully. An enemy that is beaten one way does not fall for it twice.

Related: [Progression and Hangar](PROGRESSION_AND_HANGAR.md) · [Squadron and Wingmen](SQUADRON_AND_WINGMEN.md) · [MINOZIS Encounter Design](MINOZIS_ENCOUNTER_DESIGN.md) · [Core Gameplay](CORE_GAMEPLAY.md) · [Campaign Structure](../NARRATIVE/CAMPAIGN_STRUCTURE.md)

---

## 1. The Contract

Four rules govern the whole system.

1. **What the story shows, the game does.** If a scene shows a character learning, deciding or breaking, that character's in-mission behavior changes from that point on. No scene is decoration.
2. **What the game does, the story names.** Every behavior change has a source the player can point to: a scene, a mission event or a drill. The [Squadron Record](#7-the-squadron-record) lists each one, and the radio calls back to it the first time it is used.
3. **Learning is authored, not emergent.** Each change is a designed *lesson* with a fixed trigger, a fixed behavior and a quality tier. The system feels organic because the triggers come from the player's own play and the story's own events. It is never trained live, so it never produces behavior nobody tested.
4. **Learning never changes who lives, who dies or how the story ends.** Lessons make windows easier to use, Load easier to carry and calls arrive sooner. Every mission can be completed with every lesson at its lowest tier. This keeps the campaign's fixed outcomes intact (see [Campaign Structure](../NARRATIVE/CAMPAIGN_STRUCTURE.md#6-narrative-choices)).

## 2. Three Sources of Learning

| Source | What triggers it | Example |
|---|---|---|
| **Story** | A scene the player watches or plays: a cutscene, a briefing, the circle | After M01, Thorne admits his error in front of the unit. From M02 onward, AI Thorne acts on a wingman's break call without waiting to confirm it on his own display. |
| **Experience** | Something that happened to the pilot in a sortie | If Marsh is caught by an emitter discharge in M06 because nobody ordered Disperse, he scatters early from M07 on, on his own, at the cost of a slower re-attack. |
| **Training** | A simulator drill between missions, built from evidence the squadron collected | Before M07, Marsh replays the M06 discharges alone in the simulator. In M07 he fires inside the window without being ordered. |

### Quality tiers

Story lessons are binary: the scene happened, so the lesson exists. Experience and Training lessons have a tier.

| Tier | Meaning | Typical effect size |
|---|---|---|
| **Rough** | Learned from incomplete evidence | Small: the behavior appears late or inconsistently |
| **Sound** | Learned from good evidence | Standard |
| **Sharp** | Learned from complete evidence and reinforced in play | Strong: earlier, more reliable, with a radio call that helps the player |

Training quality is set by the [Intelligence Ledger](CORE_GAMEPLAY.md#5-the-intelligence-ledger). The simulator can only be as accurate as the dossier: a drill built on a Medium entry produces a Rough lesson, High produces Sound, Confirmed produces Sharp. When the player collects evidence on secondary objectives, the gain is felt twice: once in the player's own cockpit aids and once in how well the squadron trains.

## 3. Training Scenes

The simulator bay aboard ISN *Albatross* is where the Task Force turns evidence into practice. Its threat model is built from the Ledger, so it improves as the dossier does.

Each drill is a short scene in the between-missions sequence, placed after the briefing and before the hangar. It shows one pilot rehearsing a specific problem. That pilot flies as an AI wingman in the next mission and uses what the scene showed.

| Drill | When | Pilot | What the scene shows | Built from (Ledger) | In the next mission | Also applies |
|---|---|---|---|---|---|---|
| **T1 Cross-check** | After M04 | Eirhei | Replays the M04 intrusion logs: false fuel readings, a ghost wingman 300 m off, and calls each lie aloud | "Assume observation began before contact"; Honeypot effectiveness | **M05:** AI Eirhei calls false launch warnings and drifted tracks on the radio ("Your warning's false, Over. Eyes say no launch.") before the player's HUD flags them. Each correct call lowers the target pilot's Load. | M06–M09 |
| **T2 Escort geometry** | After M05 | Thorne | Flies the M05 radar signature against a slow transport, again and again, until he finds the geometry that denies a cannon pass | RCS hotspot map; Pursuit is reconnaissance | **M06:** AI Thorne takes the cover slot on the transport without being ordered, sits on the aircraft's preferred approach aspect and calls heading corrections when the transport's instruments drift. | M08 (protecting Althéa) |
| **T3 The window** | After M06 | Marsh | Night, alone, no jokes. Replays the two M06 discharges and fires into the window until his timing holds | EMP discharge window; Two-discharge behavior | **M07:** AI Marsh fires inside the discharge window on his own and calls "Window" the moment it opens. | M08, M09 |
| **T4 The budget** | After M07 | Asano | Studies the M07 loop recording to read the power budget's tells. Marsh sits in the next seat and says nothing | Radiation-induced confusion; Substrate-cooling margin | **M08:** AI Asano calls power-budget shifts one to two seconds earlier ("Glow's up, no cyber. It's committing."), giving the player time to Disperse or turn in. | M09 |
| **T5 Four seconds** | After M08 | Vance | Rehearses a gun pass down the port panel line inside a window under four seconds. She misses it in the simulator many times before she makes it once | Port panel line as structural failure point; RCS hotspot map | **M09 Phase 3:** Vance is the player's POV. Her gun cone settles faster on the panel line, in proportion to the tier. The loop window still recurs on failure at every tier. | — |

### What T5 is for

Vance is the one pilot whose drill the player then flies personally. The scene sets up her last line in M09, "This time I know." She knows because the player watched her learn it.

### Drills and patterns

The Ledger has said since M04 not to show the aircraft a pattern. A drill *is* a pattern, and this tension is deliberate (see [Section 5](#5-enemy-learning-minozis)). A Sharp lesson that is used the same way twice in one encounter is read and countered. The player keeps drills useful by varying orders: alternating flank, timing and which wingman leads.

### Optional drills

From M04 onward, the player can assign one optional drill per between-missions sequence to any squadron pilot who is not the next POV. It costs **Readiness** (see [Progression and Hangar](PROGRESSION_AND_HANGAR.md#1-readiness)), and the drill appears as a brief scene. The list is built from Ledger entries at High or above:

| Optional drill | Requires (High or Confirmed) | Effect |
|---|---|---|
| Honeypot discipline | Honeypot effectiveness | The wingman holds EMCON longer and loses fewer HUD aids to intrusion |
| Scream bearing | Scream bearing | The wingman calls the scream's bearing on first detection |
| Altitude denial | Radiation-induced confusion | The wingman keeps an altitude slot without orders during altitude-denial phases |
| Illumination coordination | Morgenstern illumination defeats plasma stealth | The wingman fires during the first second of illumination instead of waiting for a lock tone |

An optional drill starts at one tier lower than a story drill built from the same entry.

## 4. Squadron Lessons

These are the lessons that come from the story and from experience, by pilot. The baseline behaviors in [Squadron and Wingmen](SQUADRON_AND_WINGMEN.md#2-wingman-personalities) describe each pilot at the start of the campaign. This table describes how they change.

### Thorne (Over)

| Lesson | Source | Effect when AI-controlled | Effect when POV |
|---|---|---|---|
| **Trust call** | Story, M01 (admits the error; the bar scene) | Responds immediately to a wingman's break call | Wingman break calls appear on the Command Picture as priority marks |
| **Cleared** | Story, M02 (authorizes Double or Nothing) | Will join a Double or Nothing that someone else calls | Double or Nothing becomes available to the leader |
| **Track, don't chase** | Story, M05 (if the player held restraint) | Never pursues outside doctrine; shadows and collects signature | Pursuit Warning is quieter, because he no longer needs it |
| **Ordered alone** | Experience, M05 (if the player pursued) | Hesitates half a second longer before risky orders; Load starts higher in M06 | — |

### Marsh (Six)

| Lesson | Source | Effect when AI-controlled | Effect when POV |
|---|---|---|---|
| **Double or Nothing** | Story, M02 | Calls it himself when three or more separable targets line up | Available as a command |
| **No jokes** | Story, M06 (the loadmaster's call; his jokes stop) | Radio calls become short and purely informational. His joke-based Load relief for Asano ends; the private channel now relieves through his presence instead | Edge holds steadier under Load |
| **Scatter early** | Experience, M06 (if he was hit by a discharge) | Disperses ahead of discharges on his own; re-attacks slower | — |
| **The window** | Training T3 | See T3 | — |

### Asano (Nine)

| Lesson | Source | Effect when AI-controlled | Effect when POV |
|---|---|---|---|
| **Fifth handshake** | Story, M03 (if she marked it; her line in the circle) | From M04 on, calls cyber intrusion on the datalink before HUD integrity alerts | Read highlights the MINOZIS handshake class in a distinct color |
| **Doesn't have to be funny** | Story, M07 (Marsh's line) | Her Load relief no longer depends on jokes; the private channel relieves her even in silence | Read dims more slowly under Load |
| **The budget** | Training T4 | See T4 | — |

### Eirhei (AME)

| Lesson | Source | Effect when AI-controlled | Effect when POV |
|---|---|---|---|
| **Cross-check** | Training T1 | See T1 | — |
| **Stranger's Translate** | Story, M08 (talks Althéa through it) | Can Translate non-squadron pilots in M09 (Vance, Task Force assets) | Translate works on any friendly voice on the channel |
| **Asked** | Story, any circle (if someone asks how she is) | Starts the next mission with lower Load | Same |

### Vance (Wraith)

| Lesson | Source | Effect |
|---|---|---|
| **Held weapons** | Story, I01 | In M04–M08 briefings, her pilot-level warnings include her own first-hand account of the aircraft's stalking behavior |
| **Four seconds** | Training T5 | See T5 |

### Scars

Experience lessons are not always improvements. A pilot who has been hurt learns caution, and caution costs time. "Ordered alone" and "Scatter early" are scars. Neither is a punishment: each makes that pilot safer and slower, and the circle can soften it. High cohesion with the right partner (Thorne with Eirhei, Marsh with Asano) lowers a scar's cost by one tier.

## 5. Enemy Learning: MINOZIS

The dossier's instruction is: "Do not show it a pattern and expect the pattern to go unread" (see [MINOZIS Intelligence](../WORLD_AND_LORE/TECHNOLOGY/MINOZIS_INTELLIGENCE.md)). The game holds the enemy to that. MINOZIS keeps an **operator model** of everyone it meets, and it carries that model from one encounter to the next. It has no simulator. It trains on the squadron.

### What it learns, and what it never can

| It learns (instrumental domain) | It never learns (semantic domain and physics) |
|---|---|
| Which approach aspect a pilot uses in the discharge window | How to avoid the discharge window itself |
| Which pilot's Load spikes fastest, and on what stimulus | Why a voice affects a person |
| A drilled maneuver repeated identically | How to escape illumination once it is held |
| Whether the flight pursues or tracks | How to cool its substrate faster than physics allows |
| Which honeypot profiles are decoys | What *let me go* means |

Counter-adaptations change geometry, timing and target selection. They never close a window, extend its own endurance or remove a vulnerability the story established. This keeps [Windows, not health bars](MINOZIS_ENCOUNTER_DESIGN.md#1-design-principles) true.

### How it learns

| Scale | Rule |
|---|---|
| **Within an encounter** | If the flight uses the same tactic twice (same aspect, same timing, same wingman leading), the aircraft adapts before the third use. On Ace difficulty it adapts after the first. |
| **Between encounters** | It carries its operator model forward. The first counter-adaptation in each mission is aimed at whatever beat it hardest in the previous one. |
| **Seeding** | Its model of each pilot starts the first time it observes them, not the first time they fight it. |

### When it first saw them

| Observation | Source | What it carries forward |
|---|---|---|
| **Belyaev** | P00, the whole flight | The player's own choices as Belyaev (holding Verify, complying, saying "Leave it") enter the cockpit audio library. Borrowed-voice events drawn from the cockpit recording, such as M09's, select among scripted variants built from what the player actually did. |
| **The squadron** | M03, through the hijacked swarm | Whatever the flight relied on against the swarm. If Asano marked the fifth handshake, M04's network probing targets her datalink first. |
| **Vance** | I01 | Whether she attempted a lock. Its question to her ("Did you know") is the same either way, but its stalking distance in later missions differs. |
| **The carrier** | M04, forty minutes of probing | Which honeypots it identified; later probing skips them unless the player varies the profile. |

### Its learned procedures across the campaign

The encounter configurations in [MINOZIS Encounter Design](MINOZIS_ENCOUNTER_DESIGN.md#6-encounter-configurations) are the record of what it learned from failure:

| After | What hurt it | Procedure it learns | Seen in |
|---|---|---|---|
| M05 | Being tracked rather than chased gave away its signature | Moves faster through radar coverage; spends less time where it can be recorded | M06 approach out of the sun |
| M06 | Both discharge windows were used against it | Spends its emitter more sparingly, holding the second discharge in reserve | M07: one discharge |
| M07 | Altitude denial pushed it into radiation | Avoids high zoom escapes; holds low and middle altitudes | M08: no zoom; fights close |
| M08 | Illumination exposed it, and Eirhei talked Althéa through its attack | Stops spending effort on hiding from a light it cannot escape. Spends it on the operator who holds the others together | M09 Phase 2: the search turns on Eirhei |

The residue does not learn. It only grows louder and more fragmented. Ghost Interference keeps degrading on its own schedule while the core gets better at using it. This split, a machine that learns and a man who only fades, is the enemy's arc in play.

## 6. Other Enemies

Enemies in Act I learn only within a mission. Each has one counter-adaptation, telegraphed on enemy radio so the player hears it happen.

| Mission | Enemy | Adaptation | Telegraph |
|---|---|---|---|
| M01 | Neo-Belkan cells | Mobile SAMs relocate after their first launch | Ground chatter: "They have us. Move." |
| M02 | Mercenary escort | After the first Edge gun pass, closes spacing around the lead vehicles | Escort lead orders "Tighten up" |
| M03 | Hijacked swarm | After two clusters are destroyed by the same formation, splits into smaller groups | No telegraph; Asano's Read shows the split before it happens |

General Resource's recovery teams do not fight, but they learn too. In M09 they are already waiting outside the exclusion zone because they have been shadowing the Task Force's operations all campaign (see [General Resource](../WORLD_AND_LORE/FACTIONS/GENERAL_RESOURCE.md#4-gr-in-play)).

## 7. The Squadron Record

A hangar screen, opened from M01, presents each pilot's lessons in the cell's dossier style:

| Field | Content |
|---|---|
| Lesson | Name and one-line effect |
| Source | The scene, mission or drill, with a replay link to the scene |
| Tier | Rough, Sound or Sharp, with what would raise it |
| Exposure | For drilled lessons: how many times MINOZIS has seen it used |

A matching page, **Operator Model (assessed)**, opens at M04. It is the Task Force's estimate of what the aircraft has learned about each pilot, graded like any other Ledger entry. The Task Force can be wrong about it.

### Radio callbacks

The first time a lesson changes behavior in a mission, the pilot says so in a line that names the source:

| Lesson | Callback |
|---|---|
| Trust call | THORNE: "Breaking. Your call, Six." |
| Cross-check | EIRHEI: "Like the logs, Over. That warning's lying." |
| The window | MARSH: "Window." (Nothing else.) |
| The budget | ASANO: "Glow's up, no cyber. Same as the tape." |
| Four seconds | VANCE: (silence, then the gun) |

## 8. Persistence and Modes

| Mode | State used |
|---|---|
| Campaign | Lessons accumulate from the moment they are earned and never reset |
| Free Mission | Each mission replays with the squadron and enemy state recorded at that point in the player's campaign. After the campaign, a **Final Record** option replays M01–M08 with every lesson the squadron ended with |
| New Game | Clears all lessons |

## 9. Difficulty

| Setting | Squadron lessons | Enemy learning |
|---|---|---|
| Story | One tier higher (capped at Sharp) | Adapts after the third use |
| Normal | As earned | Adapts after the second use |
| Hard | As earned | Adapts after the second use; carries two counter-adaptations between missions |
| Ace | As earned; no callbacks | Adapts after the first use |
