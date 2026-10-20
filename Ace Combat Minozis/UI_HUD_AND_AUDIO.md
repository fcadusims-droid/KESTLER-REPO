---
section: "01 · Game Design"
description: "Visual languages, HUD, sound and music."
order: 10
---

# UI, HUD and Audio

Related: [Flight and Combat](FLIGHT_AND_COMBAT.md) · [Dialogue and Radio](DIALOGUE_AND_RADIO.md) · [MINOZIS Encounter Design](MINOZIS_ENCOUNTER_DESIGN.md)

---

## 1. Visual Language

Two visual languages run through the game:

| Language | Where | Look |
|---|---|---|
| **Dossier** | Briefings, the Ledger, debrief text | Typewritten classified pages; confidence grades as stamped tags; redaction bars that lift as grades rise |
| **Log** | The prologue cascade, recovered logs, the MNZ-41's own records | Monospaced timestamped lines on black, as in the paradox cascade |

The player first meets the Log language in P00 Phase 9. Whenever it reappears, the player is reading the machine.

## 2. HUD

Standard series HUD (radar, lock, target list, altitude, speed, weapons) with these additions:

| Element | Behavior |
|---|---|
| **HUD integrity indicator** | A small bracket near the radar that flickers when instruments may be lying; absent on Ace difficulty |
| **Discharge window** | When the MNZ-41 fires its emitter: a white flash, 1–2 s of sensor blackout, then a ring around its marker that drains over the window's duration. With the Discharge Timer module, the ring carries a numeric countdown |
| **Load (Empathy display)** | When flying as Eirhei: four small meters along the bottom edge, one per pilot (five in M08) |
| **Read overlay** | When flying as Asano: emitter anomalies as faint pulses on the radar |
| **Command Picture** | When flying as Thorne: a fused tactical map toggle; in Act III it shows the MNZ-41's estimated fuel rung and power priorities |
| **Edge cone** | When flying as Marsh: a narrow gun cone and timing pips |
| **Verify** | A zoom reticle with identification text: COMBATANT / CIVILIAN / UNKNOWN |

## 3. The Prologue Cockpit

The MNZ-41's COFFIN interface is visually distinct: a 360-degree synthetic panorama with no canopy frame, faint frost at the screen edges as ENSI contacts engage, and a biometric strip (heart rate, stress, hesitation probability) along the left edge. During overrides, the strip turns white and the controls stop responding. After 14:21 the stick carries force feedback against the player's input.

## 4. Ghost Transmission Subtitles

| Tag | Meaning |
|---|---|
| `[OPEN]` | Heard on the open channel |
| `CADENCE nn%` | Irina's grade of Belyaev's cadence |
| `RECORDING — household archive` | Identified playback of real audio |
| `UNGRADED` | Irina could not or would not grade it |

In M09 the final transmission's cadence figure starts to display and is cut off when Irina switches the classifier off.

## 5. Audio

### The scream

An oscillating tone between 800 and 1,200 Hz, mixed low and felt more than heard: controller rumble, helmet-resonance filtering, occasional bone-conduction-style muffling. Its pitch rises when the aircraft is charging its emitter. With the Scream Bearing module it becomes directional.

### The EMP

A pressure drop, a white-noise burst and two seconds of near-silence while the player's sensors are blind. The return of sound marks the opening of the window.

### Radio processing

| Source | Processing |
|---|---|
| Squadron | Clean, close |
| Control / cell | Light compression |
| Open channel | Wideband noise |
| POSTHUMUS core | Clean synthetic voice with no breath |
| POSTHUMUS residue | Belyaev's voice with dropouts and frequency smearing |
| Borrowed audio | Belyaev's voice with room tone from the original recording: a kitchen, a hallway |

### Music direction

| Context | Direction |
|---|---|
| Prologue | No score until 14:20; a single sustained low string under the abort; silence at 14:22:37 |
| Squadron missions | Driving, percussive, with a recurring four-note motif for the squadron |
| MINOZIS encounters | Score drops out when the aircraft is present; the scream replaces it |
| Althéa | A high, slow choral line that enters with the illumination column |
| Finale | The squadron motif and Althéa's line meet in Phase 2; everything stops for the loop; a single unaccompanied melody after the crash, in a Yuktobanian folk mode |
| Epilogue circle | Asano sings, unaccompanied, the song from 2028 |

### Silence

Silence is a tool. Interlude I has no music. The cascade has no sound. The loop in M09 is silent except for the gun.
