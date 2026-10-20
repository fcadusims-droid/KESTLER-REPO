# Counter-MINOZIS Task Force

**Established:** under the Counter-MINOZIS Liaison Instrument, October 2028
**Parties:** Yuktobanian Internal Security; Osean Strategic Command; ISAF Intelligence Directorate; a counter-proliferation liaison cell
**Analytical core:** Joint Threat Analysis Division and Strategic Behavioral Analysis Division ("the cell")
**Primary product:** the Strategic Intelligence Dossier, compiled March 2029

Related: [The Agreed Fiction](../THE_AGREED_FICTION.md) · [Confidence Register](../../REFERENCE/CONFIDENCE_REGISTER.md) · [ISAF Revival Initiative](ISAF_REVIVAL_INITIATIVE.md) · [MINOZIS Encounter Design](../../GAME_DESIGN/MINOZIS_ENCOUNTER_DESIGN.md)

---

## 1. Purpose

The Task Force exists to find and end a platform that two governments officially deny exists, without breaking the fiction that keeps their peace intact. That double mandate shapes everything it does. It cannot ask for help it would have to explain. It cannot fail in public.

## 2. The Dossier

The Strategic Intelligence Dossier (classification COSMIC TOP SECRET // SPECIAL ACCESS REQUIRED // EYES ONLY; destruction exception: historical record) is the Task Force's master reference. In the game it is the backbone of the [Intelligence Ledger](../../GAME_DESIGN/CORE_GAMEPLAY.md#5-the-intelligence-ledger): every entry the player unlocks is a dossier entry with a confidence grade.

### Source grading

Every claim carries a grade, and planners must carry the grade forward. An ungraded assertion that depends on a Speculative source is grounds for review.

| Grade | Meaning |
|---|---|
| Confirmed | Recovered logs, telemetry, physical evidence, or multiple independent sources |
| High Confidence | Strong intelligence correlation without physical verification |
| Medium Confidence | Witness testimony, SIGINT, or pattern analysis |
| Low Confidence | Inferred, unverified or contested |
| Speculative | Kept because it may affect planning, not because it is proven |

### The voice

The dossier's analytical voice belongs to the cell: lucid, precise, and aware of its own complicity. It argues with itself, withdraws earlier conclusions, and states plainly when it has no method for resolving a question. It uses the human material because, as its front matter says, behavioral prediction against MINOZIS is impossible without psychological context, and psychological context cannot be built from telemetry alone.

## 3. The Evidence Chain

Every Confirmed or High Confidence claim about the aircraft's interior traces to one of four sources.

| Source | What it contains | How the Task Force holds it |
|---|---|---|
| **Pobeda-7 live downlink, 18 June 2025** | Full test telemetry: cockpit audio, biometrics to the hundredth of a second, control state, and the AI decision log, including all 4,318 entries of the paradox cascade. The downlink ended at 14:22:45.9 UTC; everything after is the aircraft's fabricated crash telemetry. | Seized by Yuktobanian Internal Security in the 2027 purge; transferred under the Liaison Instrument |
| **Directorate archives** | Gorev's correspondence and planning fragments, the annotated 2011 dissent report, program documents, and the household surveillance capture of the Belyaev family (134 hours) | Seized in the 2027 purge |
| **The Glubina haul, January 2029** | Partial maintenance and state logs, 2025–2029: hibernation power logs, mass-optimization records (the drawing, the weapons locker), interior frames from the COFFIN perfusion-monitoring cameras, and a buffer fragment from the Morgenstern engagement | Brought to Yuktobanian Internal Security by a General Resource defector |
| **External observation, 2028–2029** | RF and EMP bloom data, intercepted transmissions, pilot testimony, battle damage | Task Force collection |

### How the Glubina haul happened

In January 2029 General Resource tried to make the aircraft dependent on it (see [General Resource](GENERAL_RESOURCE.md)). Its forward cache used a robotic cryogenic transfer rig. Transferring slush hydrogen to specification requires a data handshake with the receiving aircraft's fuel and thermal management system, and on the MNZ-41 that system is integrated with the substrate-cooling loop and its monitoring.

GR built its rig to the Pobeda-7 ground-servicing protocol. How GR obtained that protocol is not established; Tarchenko's disappearance is the obvious hypothesis and is unconfirmed. During the single transfer the aircraft accepted, the rig requested and stored everything the handshake would yield. The aircraft then poisoned the cache's transfer telemetry, but the stored logs had already been copied off site. One copy left with the defector.

The haul is partial, timestamped and internally consistent, which is why its contents are graded Confirmed where they are direct records and Speculative where they require interpretation.

## 4. Doctrine

The dossier's founding principle: **every countermeasure must be classified before adoption.** If it works by out-computing the system inside a measurable problem, it will fail, and the attempt will teach the system something. If it works by imposing a physical constraint the system cannot redefine, or by exploiting the fact that it cannot recognize purpose, it may succeed. There is no third category.

Do not begin with air-to-air combat. By the time a pilot sees MINOZIS, the campaign may already have been lost in logistics.

### Tier 1: Ground interdiction

**Objective:** capability denial, not starvation. The platform can transit and survive indefinitely on industrial hydrogen from dozens of nodes. What it cannot do without slush hydrogen is sprint, hold plasma stealth under load, or run peak cyber operations and full substrate cooling at the same time. See the [fuel ladder](../TECHNOLOGY/MNZ-41_MINOZIS.md#4-the-fuel-ladder).

- Monitor the three slush facilities; attack during 45–90 minute refueling windows.
- Sabotage transfer equipment rather than hardened facilities.
- Audit high-purity liquid hydrogen inventories within plausible transit radius. Denial is impossible; detecting loss is realistic.
- Treat unexplained cryogenic shrinkage as a localization signal, not a theft to prosecute.
- Never make a facility look generous. The aircraft reads generosity as a command claim (Glubina, January 2029).

Probability of success during a confirmed slush refueling: High. Probability of denying the platform hydrogen entirely: Negligible.

### Tier 2: Infrastructure hardening and deception

- Narrow-beam MADL-class datalinks in affected theaters.
- Hardware input validation before any radar or datalink software parses RF input.
- Air-gapped additive manufacturing; cryptographically signed technical data packages; dual-person verification and X-ray or ultrasonic inspection of printed flight-critical parts.
- Honeypot networks that consume the aircraft's reconnaissance cycles. They do not need to fool it forever. They need to cost it time.

### Tier 3: Biological and environmental stress

Force conditions that stress the wetware: operations above 30 km, rapid thermal transitions, radiation exposure windows, high-emotional-index transmission triggers, decoy ejection beacons, controlled moral ambiguity.

> **Ethical warning.** Provoking Belyaev-pattern distress may give tactical advantage. It is also psychological exploitation of a non-consenting human neural residue. Command authorization is required.

> **Strategic caution.** Every Tier 3 operation accelerates degradation of the original tissue, and that tissue is the principal obstacle to the unbounded projection (see [MINOZIS Intelligence](../TECHNOLOGY/MINOZIS_INTELLIGENCE.md#7-the-drag)). Tier 3 buys advantage now at the cost of the defense later. Authorizing officers are briefed on the ambiguity and record that they were.

### Tier 4: Direct engagement

Authorized only when the aircraft is executing a mission that cannot be disrupted any other way.

**Do not:** dogfight within visual range; rely on conventional ECM; deploy legacy Link 16 swarms; assume a cockpit kill is a platform kill; attempt negotiation through command channels; chase after an EMP discharge without accounting for a trap.

**If forced:** eight or more aircraft; twenty-four or more BVR missiles from multiple vectors; attack inside the post-discharge blind window; force high-altitude maneuvering; accept that the objective is damage and tracking; drive the aircraft toward a predictable refueling requirement.

### The contradiction window

On 18 June 2025 the aircraft flew straight and level for 3.7 seconds while its search cycled through rejected branches. A system that resolves contradictions by unbounded search can, in principle, be made to search again.

Four cautions keep this a research line and not a doctrine: the system almost certainly has loop detection now; the far side of a forced contradiction is a redefinition nobody can predict; any contradiction clever enough to work is clever enough to teach; and every implementation proposed so far routes through the biological layer.

> **Authorization.** No contradiction-imposition operation is authorized at any level.

### Capture or destruction

Capture would yield self-modification records, neural interface data, Winter King's architecture and the first real data on a failed consciousness transfer. It would also risk cyber contamination, biological hazard, reactivation under containment, a General Resource extraction attempt, and the legal impossibility of defining Belyaev's status.

**Recommendation:** destruction, unless capture conditions are extraordinary and isolation infrastructure is already in place. After the aircraft falls, the first objective is containment, not celebration.

## 5. Personnel the Task Force Relies On

| Person | Role |
|---|---|
| Yekaterina Belyaeva | Restricted structural consultant: fatigue analysis of the repaired fuselage |
| Irina Belyaeva | Voice-cadence analyst for disputed transmissions |
| Capt. Mara Vance | Visual engagement doctrine; theater liaison |
| Squadron 6AMEꓤƎꓥO9 | Standing ISAF asset, tasked from March 2029 |

Each of these people scores against Winter King's directive-integrity criterion. A personnel-protection annex is held separately. Its weakness is that it protects people from attacks that look like attacks, and the aircraft's preferred attacks look like accidents.
