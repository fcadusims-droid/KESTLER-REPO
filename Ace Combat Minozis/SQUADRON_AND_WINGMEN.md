# Squadron and Wingmen

Related: [Adaptive Progression](ADAPTIVE_PROGRESSION.md) · [Relationships](../CHARACTERS/RELATIONSHIPS.md) · [Core Gameplay](CORE_GAMEPLAY.md) · [MINOZIS Encounter Design](MINOZIS_ENCOUNTER_DESIGN.md)

---

## 1. Commands

| Command | Effect |
|---|---|
| **Attack** | Wingmen engage the player's selected target or their own priorities |
| **Cover** | Wingmen take defensive positions around the player or a protected asset |
| **Disperse** | Wingmen break formation and spread out; used against area effects such as the EMP |
| **Special** | Wingmen fire their special weapons on the player's target |
| **Double or Nothing** | (Marsh as POV, or available to the leader after M02) Commits the whole flight to an all-in attack for 20 seconds; cannot be recalled |
| **Translate** | (Eirhei as POV, or as a wingman call) Restores a wingman's response time and lowers their Load |

## 2. Wingman Personalities

These are each pilot's baseline behaviors at the start of the campaign. They change as the pilots learn from scenes, sorties and drills; see [Adaptive Progression](ADAPTIVE_PROGRESSION.md#4-squadron-lessons).

| Wingman | Behavior |
|---|---|
| Thorne | Executes orders exactly; slow to improvise; best at holding formation in EMCON; waits to confirm a wingman's call on his own display (until M01) |
| Marsh | Aggressive, close range, gun-heavy; occasionally calls breaks the HUD has not shown (and is usually right) |
| Asano | Anticipates the leader's next maneuver and takes cover position before being ordered; calls anomalies |
| Eirhei | Balanced; calls Translate automatically when a wingman's Load crosses a threshold, at a cost to her own Load |

## 3. Operator Pressure and Load

MINOZIS engages operators. The system that represents this is **Load**: a per-pilot meter that rises when the enemy applies the stimulus that pilot cannot absorb.

### What raises Load

| Pilot | Stimulus |
|---|---|
| Thorne | A valid order that would cause friendly or civilian harm; being forced to choose alone |
| Marsh | A voice asking for help he cannot give in time |
| Asano | Sustained pressure with no release; isolation from the flight |
| Eirhei | Voices asking to be let go; every Translate she issues |
| All | Ghost transmissions; HUD integrity attacks; the scream at close range |

### What Load does

| Load | AI wingman | Player-controlled pilot |
|---|---|---|
| Low | Normal | Normal |
| Elevated | Response to orders delayed by up to 1 s | Slight input lag; signature mechanic degrades (Read dims, Edge narrows, Command Picture slows) |
| Critical | Ignores one order in three; radio calls lose information | Pronounced input lag; screen-edge effects; signature mechanic unavailable |

Load never causes a pilot to disobey in a way that changes the plot, and never causes a named character's death.

### What lowers Load

| Relief | Source |
|---|---|
| Translate | Eirhei |
| Private channel | Marsh ↔ Asano (through jokes until M06; through presence afterward) |
| Clear orders during calm phases | Thorne |
| Cruising without contact (long transits) | Asano singing (Asano sheds Load fastest) |
| The circle | Between missions, depending on cohesion |

Eirhei's Load has no in-mission relief. It falls only in the circle, and only if someone asks her how she is (the POV pilot's choice, when available).

## 4. Cohesion and the Circle

After each squadron mission the POV pilot attends the circle and chooses what to name from two or three options written in that pilot's voice. Choices raise or lower **cohesion** between specific pairs.

| Cohesion effect | Gameplay |
|---|---|
| High Marsh–Asano cohesion | Private channel relief is stronger |
| High Thorne–Eirhei cohesion | Translate on Thorne works faster |
| Anyone asks Eirhei how she is | Eirhei begins the next mission with lower Load |

High cohesion with the right partner also lowers the cost of a scar by one tier (see [Adaptive Progression](ADAPTIVE_PROGRESSION.md#scars)).

Cohesion changes dialogue in later circles and the tone of the epilogue circle. It does not change the plot.

## 5. The Threat Surface in Play

The squadron's wounds are mapped to the missions where the enemy presses them (see [Relationships: The Threat Surface](../CHARACTERS/RELATIONSHIPS.md#4-the-threat-surface)). Each of those missions puts the affected pilot in the POV seat, so the player experiences the Load from inside.
