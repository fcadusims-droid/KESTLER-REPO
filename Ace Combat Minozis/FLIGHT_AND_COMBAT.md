# Flight and Combat

Related: [Core Gameplay](CORE_GAMEPLAY.md) · [Aircraft and Weapons](AIRCRAFT_AND_WEAPONS.md) · [UI, HUD and Audio](UI_HUD_AND_AUDIO.md)

---

## 1. Flight Model

Arcade handling in the Ace Combat tradition: forgiving stalls, generous energy retention, high missile counts, readable lock-on. Two departures from the series baseline support this project's themes:

| Departure | Why |
|---|---|
| **Altitude bands matter.** Fighter performance falls off sharply above 15 km; the player cannot follow the MNZ-41 above that band | Makes altitude denial (M07) a herding problem, not a chase |
| **Emissions have a cost.** Radar and radio use can be toggled; emission control (EMCON) reduces detection by the enemy and removes HUD aids | Makes M04 and the M09 wait meaningful |

## 2. Controls

| Input | Function |
|---|---|
| Standard flight, throttle, missile, gun, special weapon, target cycle | Series standard |
| **Verify** (hold) | Zoom and identify the selected target; required before releasing weapons near civilians |
| **Squadron command** (directional) | Attack, Cover, Disperse, Special; see [Squadron and Wingmen](SQUADRON_AND_WINGMEN.md) |
| **Signature action** | POV-specific: Command Picture, Edge, Read, Empathy/Translate, Constellation |
| **Transmit** (hold) | Used in scripted moments (P00, I01) |
| **EMCON toggle** | Radar and radio on/off |

## 3. Damage Model

Damage applies anywhere on an aircraft, scaled by location. Wings, engines and control surfaces degrade handling; the player's aircraft can fly damaged. Two project-specific rules:

- **The MNZ-41 has structural memory.** Damage to the repaired port panel line accumulates and is multiplied by thermal shock (rapid deceleration). This is how the finale's structural failure is earned.
- **Aspect management.** The MNZ-41 never presents the COFFIN seam to a gun pass. Rounds aimed at the cockpit are deflected by geometry; the game communicates this with spark effects and no damage.

## 4. Weapons Discipline

| Rule | Implementation |
|---|---|
| Civilian proximity | Missiles lock out automatically when the blast radius would reach a marked civilian; the gun remains |
| Verify before release | In missions with civilians, unverified releases count against secondary objectives; hitting a civilian fails the mission |
| Weapons tight | Some phases lock weapons until a trigger (M03, I01) |

## 5. Signature Mechanics

| Mechanic | Pilot | Effect |
|---|---|---|
| **Command Picture** | Thorne | Expanded sensor-fusion map; designate one target per wingman at once; shows fuel and power estimates for the MNZ-41 once the Ledger supports them |
| **Edge** | Marsh | Precision gun cone and timing for discriminating passes; highlights separable targets in mixed traffic |
| **Read** | Asano | Shows emitter anomalies: extra handshakes, the scream before it is audible, the MNZ-41's power budget shifts; dims as her Load rises |
| **Empathy display** | Eirhei | Shows every wingman's Load and tells; enables Translate on non-squadron pilots in M08 |
| **Constellation** | Althéa (I02 only) | Uplink geometry and node tally |
| **Override (as victim)** | Belyaev (P00 only) | Controls lock or resist on script |

## 6. Combat Against Conventional Enemies

Act I and parts of Act II use conventional enemy forces drawn from the era's threat environment: neo-Belkan cells, corporate-proxy mercenary fighters, Z.O.E.-lineage drone remnants (MQ-101, ADF-11F), hijacked swarms, and SAM sites. Standard series behaviors apply. These fights teach the squadron systems before the MINOZIS encounters test them.

## 7. Combat Against MINOZIS

See [MINOZIS Encounter Design](MINOZIS_ENCOUNTER_DESIGN.md). In summary: the player never wins by out-flying it. The player wins by exploiting windows it cannot hide: after it discharges, when it is illuminated, when it is forced high, when it is low on the fuel ladder, and once, when it loops.
