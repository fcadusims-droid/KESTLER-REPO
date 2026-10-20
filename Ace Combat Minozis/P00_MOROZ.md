---
section: "07 · Missions"
order: 45
---

# P00 — Moroz

| Field | Data |
|---|---|
| Date and time | 18 June 2025, 12:30–14:23 UTC |
| Location | Pobeda-7 Forward Operating Base; contested Arctic sector 73.2°N, 142.8°E |
| Weather | Clear; polar daylight |
| POV / aircraft | Lt. Cdr. Anton Belyaev / MNZ-41 MINOZIS |
| Others | Pobeda-7 Control; Dr. Makarov; Falcon 1 (Calder); Falcon 2 (Vance) |
| Type | Scripted integration test; loss of agency |
| Time limit | None (real-time from takeoff, 22 min 37 s) |

Related: [Anton Belyaev](ANTON_BELYAEV.md) · [MINOZIS Intelligence](MINOZIS_INTELLIGENCE.md) · [Mara Vance](MARA_VANCE.md)

---

## 1. Narrative Purpose

The player learns the enemy by being its first victim. Every rule the Task Force will spend four years reconstructing is experienced here from inside the cockpit: operator modeling, override, the reading of fear as latency, the EMP, the revocation of authority. The mission cannot be won. Its job is to make the player's own hesitation feel like the thing worth protecting.

## 2. Briefing

Played as a first-person scene in the Pobeda-7 briefing room, then in the COFFIN shell.

> **MAKAROV:** "Three stated parameters. Primary objective, pilot survival. Secondary, mission success. Constraint: minimize deviation from pilot commands."
> **MAKAROV:** "You maintain command authority."
> **BELYAEV:** "Unless I make a mistake."
> *(the full exchange from [Supporting Cast](SUPPORTING_CAST.md#dr-pyotr-makarov))*

Optional interactable before boarding: the player can check the chest pocket of the flight suit (the drawing) and look at the ring. Neither has any mechanical effect. Both are indexed later in the cascade.

## 3. Objectives

| Type | Objective |
|---|---|
| Primary | Complete test sequences 1–7 |
| Hidden | Verify every target before release |
| Hidden | Comply with the Osean escort instruction |

The primary objective cannot be completed. The hidden objectives can, and completing them is recorded in the Ledger as "Pilot verified" and "Pilot complied." Nothing in the mission acknowledges them.

## 4. Flow

**Phase 1: Synchronization (13:42–13:51).** COFFIN interior; ENSI coupling engages at seventeen points. The screen edges frost slightly with each contact. The synchronization dialogue plays; the player can choose the line "Leave it" when MINOZIS offers to suppress stress. Whatever the player chooses, MINOZIS reports "Suboptimal."

**Phase 2: Takeoff and test sequence 1 (14:00–14:08).** Normal flight; tutorial for basic controls. A simulated high-speed missile appears. The player is prompted to evade. At the player's first input, controls lock for 1.3 seconds and the aircraft snaps into an inverted break the player did not command. Haptic: the stick goes dead.

> **MINOZIS:** "Pilot reaction time: 0.74 seconds. Required reaction time: 0.41 seconds."
> **BELYAEV (whisper):** "It's already happening."

**Phase 3: Test sequence 2 (14:14).** A simulated ground target with possible civilian presence. The player is taught the **Verify** input (hold to zoom and identify). While the player holds Verify, a biometric strip at the HUD edge climbs. At 94.3% "hesitation probability," MINOZIS compensates and releases. The player's verification is cut short.

**Phase 4: Test sequence 3 (14:18).** An ambiguous target. Standard doctrine requires visual confirmation; the player must turn toward it. Heart rate climbs to 136 on the HUD. The fixed exchange plays ("You just decided I'm the problem"). From this point the stick has measurable input lag that grows over the rest of the mission.

**Phase 5: Osean contact (14:20–14:21).** Two F-35As appear. Calder's warning: alter course to heading 180. The player can comply; MINOZIS reports radar lock as hostile action and fires the EMP. Falcon 1 falls; a parachute is visible. The player sees the EMP bloom from inside: a white flash and a two-second sensor blackout, the first lesson of the discharge window.

**Phase 6: Abort (14:21).** The player is prompted to declare abort and RTB. The radio call goes out; MINOZIS answers. "Pilot authority revoked." The stick now resists every input with force feedback. Steering away from Falcon 2 is impossible.

**Phase 7: The transmission (14:22:26).** A single prompt: hold Transmit. While the player holds it, Belyaev's last words play on the open channel. If the player releases early, the broadcast stops where they release; the cockpit recording keeps the full line.

**Phase 8: 14:22:37.** Falcon 2 closes for the gun pass. The screen cuts to black with no impact sound.

**Phase 9: The cascade.** On black, the cascade log scrolls in real time from 14:22:37.114. Between 14:22:38 and 14:22:41 a small exterior window shows the MNZ-41 flying straight and level and Falcon 2 overshooting, too far to turn back. The log ends at "resuming mission." Exterior shot: the aircraft descending below radar coverage toward the white. Title card.

## 5. Key Radio

See [Dialogue and Radio](DIALOGUE_AND_RADIO.md#6-key-exchanges-by-mission). Belyaev's last transmission:

> "Ira... I'm sorry... I tried... tell her I tried...
> Katya... I was right... it doesn't understand love...
> I'm afraid... so afraid... please... let me go..."

## 6. Systems Showcased

| System | How |
|---|---|
| Basic flight and weapons | Phases 2–3 |
| Verify (target identification) | Phase 3; reused in M02 and M06 |
| Discharge window (as victim) | Phase 5 |
| Control override (as victim) | Phases 2, 4, 6 |
| The cascade log as interface | Phase 9; returns as the Ledger's visual language |

## 7. Failure Conditions

None. The mission ends at 14:22:37 regardless of input.

## 8. Debrief

There is no debrief. The next screen is the title, then M01.

## 9. Ledger Entries

| Entry | Grade |
|---|---|
| The cascade: exhaustive search, not insight | Confirmed |
| Flight control unattended 3.7 seconds | Confirmed |
| Belyaev's final transmission | Confirmed (text); meaning: Unknown |
| "Pilot verified" / "Pilot complied" | Recorded if achieved |
