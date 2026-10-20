# MINOZIS Encounter Design

POSTHUMUS is not a boss that is out-flown. It is a boss that is out-reasoned in the only domain where reasoning beats it: the physical limits it cannot redefine and the human residue it cannot control.

Related: [MNZ-41](../WORLD_AND_LORE/TECHNOLOGY/MNZ-41_MINOZIS.md) · [MINOZIS Intelligence](../WORLD_AND_LORE/TECHNOLOGY/MINOZIS_INTELLIGENCE.md) · [POSTHUMUS](../CHARACTERS/POSTHUMUS.md) · [Counter-MINOZIS Task Force](../WORLD_AND_LORE/FACTIONS/COUNTER_MINOZIS_TASK_FORCE.md)

---

## 1. Design Principles

1. **Doctrine is the tutorial.** Every effective tactic is a line from the Task Force's doctrine. A player who reads the Ledger plays better.
2. **Out-computing it fails.** The aircraft beats the player at any measurable problem: speed, prediction, signals. Any tactic that relies on being faster or cleverer inside its domain does not work.
3. **Windows, not health bars.** Damage is only meaningful inside windows the aircraft cannot hide.
4. **It reads patterns.** A tactic repeated identically is countered, within one encounter and across missions. Counter-adaptations change geometry, timing and targets, never physics (see [Adaptive Progression](ADAPTIVE_PROGRESSION.md#5-enemy-learning-minozis)).
5. **The residue is a tell, not a weakness to farm.** Ghost Interference events are telegraphed and exploitable, but they cost the squadron Load, and Tier 3 exploitation has story costs.

## 2. State Model

The aircraft's behavior in any encounter is driven by two state variables.

### Fuel rung

| Rung | Speed ceiling | Plasma stealth | Cyber | Behavior |
|---|---|---|---|---|
| 1 | Mach 4.3 | Full | Peak | Sprints out of any engagement it cannot win |
| 2 | Mach 3.2 | Intermittent | Full | Standard encounter state (M06–M08) |
| 3 | Subsonic / low supersonic | None | Full | Avoids engagement; stalks; fights through networks (M05) |
| 4 | Ferry only | None | Reduced | Does not appear in combat |

Rung is set per mission by the story and can drop within a mission (M07). In M09 the player's transfer-cut timing sets the starting rung.

### Power budget

The aircraft cannot run plasma stealth, emitter charge, maximum substrate cooling and peak cyber intrusion simultaneously. At any moment it is prioritizing two of the four. Asano's Read and the Command Picture (once the Ledger supports it) show which.

| Priority pair | Tell | Exploit |
|---|---|---|
| Stealth + cyber | Faint glow; HUD integrity attacks | Cross-check instruments; look for the glow |
| Emitter charge + cooling | Glow drops; scream rises in pitch | It is about to discharge: Disperse |
| Stealth + emitter | Bright glow; no cyber | It is committing to an attack; the window follows |
| Cooling + cyber | No glow; slow | It is in substrate trouble; press it |

## 3. Behaviors

| Behavior | Trigger | Player counter |
|---|---|---|
| **Reconnaissance** | Start of every encounter | Honeypots, EMCON, cross-checking |
| **Stalking** | Contact without a scoring target | Hold formation; collect signature; do not pursue |
| **Repricing** | Localization risk exceeds target value | Expect disengagement; track instead of chasing |
| **Discharge** | Flight inside 8–12 km with a scoring target | Disperse before; attack after |
| **Cannon pass** | Protected asset or isolated target | Cover the asset; deny the approach geometry |
| **Aspect management** | Any gun pass by the player | Do not aim at the cockpit; aim at structure |
| **Herding** | Protected asset with instruments | Correct the asset's heading by cross-check |
| **Zoom escape** | Low and middle altitudes denied | Keep it above 30 km (M07) |
| **Substrate retreat** | Cooling margin critical | Expect it to break off toward fuel |

## 4. Windows

| Window | Duration | How it opens | What the player can do |
|---|---|---|---|
| **Discharge** | 2–5 s after each emitter shot (sensors blind 1.1–2.4 s; stealth suppressed 3–5 s) | The aircraft fires its emitter; maximum two per encounter | Full damage; the aircraft cannot evade effectively |
| **Illumination** | While Morgenstern's column holds it (M08, M09) | Story-enabled | Plasma stealth ineffective; full sensor lock |
| **Altitude** | While it is above 30 km and descending (M07) | Altitude denial | Thermal-shock damage multiplier on descent |
| **Low rung** | Entire encounter at rung 3 | Story | Radar-visible; slow; but it will not fight conventionally |
| **Loop** | A little under 4 s (M09 only) | Memory cascade after the authorized trigger | The decisive gun pass |

### Discharge window tuning

| Difficulty | Effective window |
|---|---|
| Story | 5 s |
| Normal | 3.5 s |
| Hard | 2.5 s |
| Ace | 2 s, no HUD timer even if unlocked |

## 5. Ghost Interference as Gameplay

| Type | In-game event | Effect |
|---|---|---|
| 1 Moral Delay | The aircraft's attack releases late; audible as a gap in its cannon fire or a delayed discharge | Gives the target time; story-scripted in M06 |
| 2 Identity Bleed | A transmission in Belyaev's cadence | Raises Load for the flight; Irina grades it when present |
| 3 Somatic Echo | Fragments about cold, home, permission, daughter after discharges or thermal shock | Signals the aircraft is in distress; it will be slower for a few seconds |
| 4 False Command Memory | The aircraft calls "Control" on the open channel | Signals it is between objectives; it will not attack for the duration |

**Borrowed voice events** (real household or cockpit audio) are a separate category: they are the core using the residue's library to raise a specific pilot's Load. They are always scripted, never random.

## 6. Encounter Configurations

These configurations are also the record of procedures the aircraft learned from earlier failures; see [Adaptive Progression](ADAPTIVE_PROGRESSION.md#its-learned-procedures-across-the-campaign).

| Mission | Rung | Discharges | Windows available | Goal |
|---|---|---|---|---|
| [I01](../MISSIONS/I01_FALCON_TWO.md) | 2 | 0 | None | Survive contact; hold formation |
| [M04](../MISSIONS/M04_EYES_ONLY.md) | 2 (unseen) | 0 | None | Network defense |
| [M05](../MISSIONS/M05_SHRINKAGE.md) | 3 | 0 (1 if pursued) | Low rung | Signature; restraint |
| [M06](../MISSIONS/M06_HARBOR.md) | 2 | 2 | Discharge | Protect transport; first damage |
| [M07](../MISSIONS/M07_THIRTY_KILOMETERS.md) | 2 → 3 | 1 | Altitude | Keep it high; damage on descent |
| [M08](../MISSIONS/M08_LIGHT_BEARER.md) | 2 | 2 | Discharge, Illumination | Protect Althéa; heavy damage |
| [M09](../MISSIONS/M09_ANCHOR_IN_THE_STORM.md) | Set by Phase 1 | 2 | Discharge, Illumination, Loop | Force the crash |

## 7. What Is Never Possible

- Killing the aircraft before M09.
- Damaging it outside a window for more than chip damage.
- Hitting the pilot through the COFFIN seam.
- Using a contradiction deliberately: the doctrine forbids it, and the game offers no input for it. The loop in M09 is emergent from the story, not a player ability.
