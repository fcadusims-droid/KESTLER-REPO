---
section: "01 · Game Design"
description: "Loop, point of view, Intelligence Ledger, difficulty, modes."
order: 2
---

# Core Gameplay

An arcade flight-combat game in the Ace Combat tradition: readable dogfights, large set pieces, a story told over the radio. Its distinguishing system is an enemy that fights the operator rather than the aircraft, and an intelligence layer that turns the in-world dossier into the player's progression.

Related: [Project Overview](PROJECT_OVERVIEW.md) · [Flight and Combat](FLIGHT_AND_COMBAT.md) · [Squadron and Wingmen](SQUADRON_AND_WINGMEN.md) · [MINOZIS Encounter Design](MINOZIS_ENCOUNTER_DESIGN.md) · [Campaign Structure](CAMPAIGN_STRUCTURE.md)

---

## 1. Design Pillars in Play

| Pillar | Mechanical expression |
|---|---|
| **Hesitation is worth protecting** | The Verify input; the prologue's override; restraint choices with real consequences (M05); the loop window in the finale |
| **The enemy fights the operator** | Operator Pressure and Load; ghost transmissions as gameplay events; HUD integrity attacks |
| **Physics is the only thing it cannot redefine** | Fuel rung state, power budget, discharge windows, altitude and thermal vulnerabilities |
| **Know it before you fight it** | The Intelligence Ledger: evidence collected in missions raises confidence grades and unlocks tools |
| **The last human aces** | Four distinct pilots with distinct signature mechanics; the circle between missions |

## 2. Core Loop

```text
Briefing (dossier pages, Ledger) 
   → Training (simulator drill scene, when scheduled)
      → Hangar (aircraft, loadout, parts, doctrine modules, optional drill, inspection)
         → Sortie (objectives, enemy, evidence collection)
            → Debrief (results, Ledger updates)
               → Circle (squadron scene, cohesion)
                  → next Briefing
```

The sortie is the center. The Ledger and the circle are the two outer rings: one makes the player smarter about the enemy, the other makes the squadron stronger under pressure. Every beat of the loop, cutscenes included, can change how the squadron and the enemy fly afterward (see [Adaptive Progression](ADAPTIVE_PROGRESSION.md)).

## 3. Sortie Structure

Each sortie is built from these elements:

| Element | Purpose |
|---|---|
| Objectives | Primary, secondary and hidden (see each mission document) |
| Evidence | Signatures, recordings and observations that feed the Ledger |
| Pressure events | Moments when the enemy targets a pilot's Load |
| Restraint points | Moments where the doctrinally correct action is not to fire, not to pursue, or not to break formation |
| Set pieces | One per mission, built around a single memorable image |

## 4. Point of View

The player flies as different existing characters across the campaign (see [Campaign Structure](CAMPAIGN_STRUCTURE.md#2-point-of-view)). Each POV changes three things:

| Changes | Example |
|---|---|
| Aircraft and handling | Thorne's F-35C versus Marsh's F/A-18E |
| Signature mechanic | Command Picture, Edge, Read, Empathy display |
| What the enemy presses on | Thorne's orders, Marsh's helplessness, Asano's isolation, Eirhei's requests |

The non-POV squadron members always fly as AI wingmen with their own signature behaviors.

## 5. The Intelligence Ledger

The Ledger is the in-world Strategic Intelligence Dossier presented as the game's codex and progression layer. It opens in [M04](M04_EYES_ONLY.md).

### Entries

Each entry is a claim about the enemy or the world, carrying a confidence grade: Confirmed, High, Medium, Low, Speculative, or Unknown. Entries are written in the cell's voice.

### Raising grades

Evidence from missions raises grades. Examples:

| Entry | Evidence needed | Grade change |
|---|---|---|
| EMP discharge window | Attack successfully inside a discharge window | High → Confirmed |
| RCS hotspot map | Hold aspect for 60 s of signature collection | New → High; Confirmed with thermal data |
| Port panel line failure point | Katya's analysis (story) plus thermal signature | New → Medium → High |
| Morgenstern illumination | Fire on the aircraft while illuminated | New → Confirmed |

### What grades unlock

When an entry reaches High or Confirmed, it unlocks a matching **doctrine module** in the hangar or an interface aid in the cockpit:

| Entry at High/Confirmed | Unlock |
|---|---|
| EMP discharge window | Discharge-window timer on the HUD |
| RCS hotspot map | Passive-radar aspect overlay |
| Scream bearing | Audio direction cue for the scream |
| Port panel line | The faint marking used in M09 Phase 3 |
| Pursuit is reconnaissance | Pursuit warning when closing on the aircraft outside doctrine |

Unlocks never make a scripted outcome possible or impossible. They make the player's job clearer.

### Permanent unknowns

Some entries can never be raised: subjective awareness; the meaning of *let me go*; the pistol. They remain Unknown at the end of the game. The Ledger states this plainly.

## 6. Difficulty

| Setting | Changes |
|---|---|
| Story | Wider discharge windows; slower Load gain; Verify assists |
| Normal | Baseline |
| Hard | Narrower windows; faster Load gain; enemy uses its two discharges more aggressively; enemy carries more counter-adaptations between missions |
| Ace | Hard, plus no HUD integrity warnings: the player must notice instrument lies unaided; enemy adapts after a single use |

Learning rates by difficulty are listed in [Adaptive Progression](ADAPTIVE_PROGRESSION.md#9-difficulty).

The finale's Phase 3 window recurs on failure at every difficulty.

## 7. Modes

| Mode | Contents |
|---|---|
| Campaign | Prologue through epilogue |
| Free Mission | Replay squadron missions (M01–M08) with any unlocked aircraft, using the squadron and enemy state recorded at that point in the campaign (or the Final Record after completion); interludes and the finale replay with their fixed aircraft |
| Ledger Archive | The full dossier, every entry at its achieved grade, all recovered logs and recordings |

The MNZ-41 is never available outside the prologue.

## 8. What the Player Never Does

- Fly MINOZIS after the prologue.
- Kill a named character.
- Choose whether the aircraft is destroyed.
- Learn whether Anton is inside it.
