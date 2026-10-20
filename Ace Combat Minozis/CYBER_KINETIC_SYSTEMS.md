# Cyber-Kinetic Systems

The aircraft fights the airbase before it fights the aircraft. These systems put that fight into the player's hands without turning the game into a hacking minigame.

Related: [Cyber-Kinetic Warfare (lore)](../WORLD_AND_LORE/TECHNOLOGY/CYBER_KINETIC_WARFARE.md) · [MINOZIS Encounter Design](MINOZIS_ENCOUNTER_DESIGN.md) · [Progression and Hangar](PROGRESSION_AND_HANGAR.md)

---

## 1. Principle

The player never "hacks back." The player defends by refusing to trust any single source: cross-checking instruments, using narrow links, inspecting parts and feeding the enemy decoys. This mirrors the doctrine: out-computing the system fails; denying it a pattern works.

## 2. HUD Integrity

During cyber-active encounters the aircraft can make the player's own instruments lie.

| Lie | Example |
|---|---|
| Position drift | A wingman's datalink position 300 m from where he visibly is |
| Phantom warning | A missile-launch warning with no launch |
| Fuel disagreement | Fuel state inconsistent with time aloft |
| Track injection | A contact on radar that does not exist |
| Heading drift (protected assets) | A transport's reported heading diverging from its actual heading |

### Cross-check

When the HUD integrity indicator flickers (Normal difficulty and below), the player can cross-check:

- **Visual:** look at the thing in question (wingman, transport, missile trail).
- **MADL:** compare against the narrow-beam datalink, which the aircraft cannot spoof.
- **Wingman call:** ask a wingman to confirm (Asano is most reliable).

Accepting a lie has consequences: wasted countermeasures, a wingman out of position, a transport herded toward an ambush. Repeatedly accepting lies in M04 compromises *Albatross*'s real network and fails the mission.

On Ace difficulty, the integrity indicator is disabled; the player must notice lies unaided.

## 3. Datalinks

| Link | Property |
|---|---|
| Legacy Link 16-derived | Full data; vulnerable to injection |
| MADL-class narrow beam | Limited data; cannot be spoofed; requires line of sight between flight members |

Switching to MADL removes some HUD aids (shared targeting at range) in exchange for trustworthiness. In EMCON (M09 Phase 1), MADL is the only link.

## 4. Honeypots

In M04 and M09, Task Force decoy networks run alongside real ones. The player flies emission profiles that make the decoys credible. A well-flown profile means the aircraft spends its reconnaissance cycles on the decoy, which reduces HUD integrity attacks later in the mission.

## 5. Compromised Parts

Case Delta showed the aircraft can poison manufacturing files so that printed parts fail under load. In the hangar, parts printed aboard *Albatross* carry a small risk of compromise from Act II onward.

| Hangar choice | Effect |
|---|---|
| Inspect (X-ray / ultrasonic) | Costs Readiness; eliminates the risk |
| Fly uninspected | Free; a compromised part fails at a random moment under high G (one per mission at most) |
| Signed technical data packages (Ledger unlock) | Reduces risk for all printed parts |

A failed part never causes mission failure on its own. It forces an emergency (lost control surface, degraded gear on landing) that the player must handle.

## 6. Network Probing as Mission Pressure

When the aircraft is probing a network (M04, M09 Phase 1), the mission UI shows a probing indicator on the protected network. It increases the frequency of HUD integrity events and reduces the effectiveness of non-MADL sensors. It is countered by flying the honeypot profile well and maintaining EMCON.
