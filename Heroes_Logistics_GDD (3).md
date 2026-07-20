---
title: "Heroes' Logistics"
description: "Technical game design document for a Roblox strategy game where the power fantasy is keeping favored soldiers alive through supply, reinforcement and rescue — logistics as an act of love, never combat."
genre: "Management / Logistics"
category: "Game Design Document"
---

# Heroes' Logistics — Technical Game Design Document

**Version:** 1.5 (Feature-Complete Technical Draft)
**Document type:** Technical GDD — systems, mechanics, and architecture only
**Platform target:** Roblox (Luau, server-authoritative)
**Status:** Pre-production / Vertical Slice definition

> **Note on scope.** This document is intentionally *technical*. Lore, worldbuilding, faction names, character names, and narrative fiction are deliberately omitted and will be authored separately. Where a name is needed for an example (e.g. "Arthur"), treat it as a placeholder.

---

## 1. Design Pillars

These pillars are the constitution of the project. Any feature that does not serve at least one of them is a candidate for cutting.

1. **Human scale over aggregate statistics.** The player manages *individuals* (Arthur, Carlos, Rodolfo), never anonymous clones. Every system must surface the individual, not the crowd.
2. **Logistics is the act of love.** The player's power fantasy is *keeping favored soldiers alive through industrial efficiency*, not fighting. The core verbs are supply, equip, reinforce, and rescue — never "attack."
3. **Emergent stories, authored drama.** The simulation generates events; the presentation layer (alerts, dynamic camera, notable panel) curates them into a narrative the player can follow and care about.
4. **Attachment through investment.** Players bond with what they spend effort on. Every emotional peak must be preceded by a costly player decision.

### 1.1 The North-Star Success Metric

The prototype is a success if, after 30 minutes of play, the player **knows the name of their best soldier** and **feels a knot in their chest when that soldier enters the Agony state** on the road. Everything below is in service of producing that single moment.

---

## 2. Critical Design Resolution: What the Prototype Must Actually Validate

The original concept carried a hidden risk: the title is *Heroes' Logistics*, but the first proposed Vertical Slice removed all logistics (no crafting, no economy, no automation), leaving an auto-battler spectator. That would validate "players get attached to NPCs" — but **not** "the act of doing logistics is what creates the attachment." Those are two different hypotheses, and only the second is the actual game.

**Resolution.** The Vertical Slice keeps its minimalism but must contain **one costly logistical decision**: the Rescue. This is the smallest possible atom of the power fantasy — the player spends resources and risks the operation to keep one individual alive. Without it, the prototype tests half the thesis. See Section 4 (Vertical Slice) and Section 8 (Rescue System).

---

## 3. Core Loop

### 3.1 Macro Loop (Session-to-Session, Persistent)

```
   ┌─────────────────────────────────────────────────────┐
   │                                                       │
   ▼                                                       │
[Barracks]  →  [Deploy Roster]  →  [Battle / Spectate]  → [Resolve]
   │                                      │                  │
   │                                      ▼                  │
   │                              [Logistical              │
   │                               Decisions:               │
   │                               supply, rescue,          │
   │                               reinforce]               │
   │                                                         │
   └──── [Persist stats, retire/recruit, manage 5 slots] ◄──┘
```

### 3.2 Micro Loop (In-Battle, Moment-to-Moment)

```
Observe front line  →  Identify a soldier in danger / excelling
        │                          │
        ▼                          ▼
Decide: intervene?         Follow with camera (emotional investment)
        │
        ▼
Spend resource (airdrop barricade + medical cart)
        │
        ▼
Watch the two bars race (barricade HP vs. 4.5s load timer)
        │
        ▼
feel relief OR grief  →  loop
```

The micro loop is the engine that produces the North-Star moment. It must be tight: from "I notice Arthur is in trouble" to "I can do something about it" should be **under 5 seconds** of player action, or the drama dissipates.

---

## 4. Vertical Slice (MVP) Definition

### 4.1 Scope Table

| Keep in MVP | Cut from MVP | Add to MVP (vs. original draft) |
|---|---|---|
| 10v10 tug-of-war on a single central road | Manual crafting (§14, Post-MVP) | Logistical Airdrop Rescue (§8) |
| Target-lock combat with attack cadence | Heavy automation | Persistence of soldier identity + stats between sessions |
| Notable Soldiers panel + dynamic camera | Full PvP networking | Agony state + Fallen Heroes Wall |
| Commander avatar (presence, non-combatant) | Multiple eras — medieval only (§15, Post-MVP) | Two-rate replication + tactical radar |
| Cinematic global alerts | Complex economy (§14, Post-MVP) | The Supply meter to fuel the airdrop/cart (§8.7) |

### 4.2 MVP Map

- Two bases: Blue (player) vs. Red (AI opponent).
- One direct central road connecting them.
- A contested midpoint where the tug-of-war is decided.
- **The MVP map is hand-authored, fixed, and full-information** — a single known layout with no fog. Procedural maps (§16) and fog of war (§17) are Post-MVP: the North-Star (§1.1) is validated against *one* controlled, fully-visible map so attachment, not novelty or scouting, is what is being measured. Treat the MVP map as the degenerate case of the procedural ruleset (one straight road, default cover spacing, full vision).

### 4.3 MVP Win/Loss — Tug-of-War Mechanics

The contested **front line** is a scalar position `L` on the road (`0` = Blue base, `RoadLength` = Red base). It moves toward whichever side currently has local superiority:

```
dL/dt = k × (BlueAliveNearFront − RedAliveNearFront)
```

- "Near front" = units within a fixed window (e.g. ±60 studs) of `L`. Units retreating or in Agony do not count.
- `k` is the push-rate constant, tuned so a typical round lasts **≈5–8 minutes** — long enough for a soldier to gain competence, become notable, get into danger, and trigger a rescue decision.
- Pushing `L` into the enemy base wins the round. The MVP does **not** need a full campaign; it needs one repeatable round.
- The front-line position is recomputed by `MatchService` at 1 Hz (same cadence as the tactical matrix, §11.3) — it is cheap and visually legible on the radar.

**Field composition (roster vs. fielded).** Each side fields up to **10 units**, but the player's barracks holds only **5 named slots** (§10.2). The difference is filled by **generic line troops**: unnamed, non-persistent soldiers auto-supplied by the base (§10.3). The named roster is the emotional core; the generics are the crowd from which new names can emerge. When a generic dies, a replacement spawns at base after a fixed delay (e.g. 8 s) at no resource cost in the MVP — Supply (§8.7) is reserved exclusively for rescues, keeping the one costly decision clean.

### 4.3.1 The Opponent (MVP AI Director)

The Red side requires no symmetric "enemy commander" simulation in the MVP:

- Red units run the **same four-layer AI** (§6) — no special enemy code path.
- A minimal **Director script** replaces the enemy player: it maintains Red's 10-unit field with the same respawn delay and may include 1–2 fixed mid-tier units (Seasoned-equivalent stats) so the player faces visible skill contrast.
- The Director has **no rescue system and no Agony** for its units in the MVP — Red units simply die. Asymmetry is acceptable: the prototype tests the *player's* attachment, not enemy parity.
- Difficulty is tuned with exactly two knobs: respawn delay and the count of mid-tier units. No adaptive difficulty in the MVP.

### 4.4 MVP Validation Plan & Telemetry

Instrument the prototype to capture both attachment formation and the frustration threshold.

**Attachment proxies**
- Did the player click "Follow" on any soldier? (attachment forming)
- Did the player attempt at least one rescue? (logistics-as-love working)
- Post-session unprompted recall: "What was your best soldier's name?" — the true win condition.

**Rescue telemetry hooks**

| Event | Fires when |
|---|---|
| `Telemetry_Rescue_Attempted` | Airdrop is launched |
| `Telemetry_Rescue_Succeeded` | Soldier returns to base |
| `Telemetry_Rescue_Failed_Reason` | Records cause: `TIMER_EXPIRED` (60s), `BARRICADE_DESTROYED`, or `CART_INTERCEPTED` |

**Tuning target.** Initial balance (barricade HP and cart speed) should aim for a **65–75% rescue success rate** for first-session players. Any value **below 50%** triggers immediate rebalancing of the numeric attributes. Capturing the *reason* for failure is what makes the rebalance diagnosable rather than guesswork.

---

## 5. Combat System ("Fake" Combat by Range & Cooldown)

Combat is **resolved by range and cooldown timers**, RPG-style, not by physics or hit detection. This is a deliberate performance and readability choice: it keeps server cost low and makes outcomes legible to the spectating player.

### 5.1 Attack Resolution

- Each soldier holds a **target lock**: it acquires the highest-priority enemy (see §5.3) within its vision radius and commits to that target until one of them dies or the target leaves range.
- Attacks fire on a cooldown via the two-phase protocol in §5.2.

| Unit tier | Attack interval | Design intent |
|---|---|---|
| Recruit | 1.8 s | Baseline; feels deliberate, slightly clumsy |
| Higher tiers | down to 1.0 s (full ladder in §5.5; Reaper floor in §6.7.7) | *Looks* more skilled without inflating raw damage — speed reads as competence |

> **Design principle:** Veterans should feel better through *cadence and behavior*, not bigger numbers. A faster, smarter soldier reads as a hero; one that just hits harder reads as a stat block.

### 5.2 Two-Phase Damage Validation (no phantom hits)

To eliminate phantom damage caused by animation/telegraph latency, the server delegates only the *visual* execution to the client and keeps factual truth behind two temporal checks:

- **T₀ (attack start):** Server confirms the target is alive and in range. If so, it fires the `Telegraph` network event so the client plays the (heavy) attack animation.
- **T_damage (attack resolution):** After the animation duration elapses, the server **re-validates** the target before applying HP reduction. If the target has entered Agony, died, or retreated beyond `maxRange + latencyMargin`, the damage is **discarded** and the pending attack is cleared from memory.

The telegraph is purely cosmetic; truth is decided at resolution. `latencyMargin` exists so a target legitimately retreating at the edge of range is not punished by network jitter.

### 5.3 Target Acquisition — Aggro-Weighted Effective Distance

The AI does not attack what is *geographically* nearest; it attacks what is mathematically most *valuable* to attack, balancing threat weight against proximity. To avoid the cost of native square roots in the hot loop, the comparison uses squared real distance divided by a **linear** threat weight:

```
EffectiveDistanceSquared = RealDistanceSquared / ThreatWeight
```

**Threat weights (placeholder tuning):** Airdrop Barricade = 100, Medical Cart = 50, Soldier = 10. Lowest `EffectiveDistanceSquared` wins the lock.

The threat weight divides **linearly**, not squared, so proximity still dominates close combat while threat steers medium- and long-range choices:

- Enemy **3 studs** from a recruit (`ThreatWeight = 10`): `3² / 10 = 0.9`
- Enemy **50 studs** from a barricade (`ThreatWeight = 100`): `50² / 100 = 25`

Since `0.9 < 25`, the NPC eliminates the point-blank threat first. The barricade pulls aggro at **medium and long range**, naturally clumping the horde and opening tactical gaps without breaking close combat.

> **Tuning note.** The barricade's effective "lure radius" relative to a soldier scales as `√(ThreatWeight_barricade / ThreatWeight_soldier)` ≈ 3.16×. To make the barricade more or less magnetic, change only the weights; keep the divisor linear.

### 5.4 Damage Model

- Keep it simple and transparent for the prototype: flat damage per hit, modified by equipment and Competence tier (§6.6).
- Avoid armor/resistance layers in the MVP — they obscure the "is my soldier winning?" read the player needs from the camera.

### 5.5 Baseline Numbers (MVP placeholders, internally consistent)

All values are tuning placeholders, but they are **designed to close as a system** — the rescue math below must keep balancing whenever any one of them changes.

| Parameter | Value | Note |
|---|---|---|
| Road length | 400 studs | Bases at 0 and 400; midpoint 200 |
| Soldier walk speed | 12 studs/s | ≈33 s base → midpoint |
| Melee engage range | 5 studs | `maxRange` in §5.2 |
| Vision radius | 40 studs | Target acquisition scan (§5.3) |
| Recruit HP / damage | 100 HP / 12 per hit | At 1.8 s interval → ≈6.7 DPS; recruit-vs-recruit TTK ≈ 16 s (long enough to watch and react) |
| Tier precision modifier | +5% / +15% / +25% | Seasoned / Veteran / Elite (the invisible modifier, §6.6.4) |
| Tier attack interval | 1.8 / 1.6 / 1.2 / 1.0 s | Recruit / Seasoned / Veteran / Elite |
| Medical Cart speed | 16 studs/s | Base → midpoint ≈ 12.5 s |
| Barricade HP | 400 | See rescue math below |
| Agony duration | 60 s | §8.1 |
| Loading channel | 4.5 s | §8.4 |
| Generic respawn delay | 8 s | §4.3 |

**The rescue math chain (why these numbers).** A typical mid-road rescue: player reaction (~10 s) + cart travel (~12.5 s) + loading channel (4.5 s) ≈ **27 s of the 60 s Agony window** — succeeding with margin, but collapsing if the player hesitates or the front line is pushed back (cart travels farther). The barricade at 400 HP under ~4 attacking recruits (≈27 DPS combined) holds ≈ **15 s** — slightly less than the cart's full exposure, which is exactly the two-bars-racing tension of §8.4. The first-session success rate target of 65–75% (§4.4) is tuned primarily through **barricade HP and cart speed**; everything else stays fixed so rebalancing remains diagnosable.

---

## 6. The Four-Layer Soldier AI

The AI is split into four logical layers running **server-authoritative** for security and consistency. The layering keeps each layer cheap and independently tunable.

### 6.1 Layer 1 — Navigation

- Direct movement along the road toward the enemy base.
- **Avoid heavy pathfinding.** Use waypoint following / a precomputed road spline. Full `PathfindingService` recomputation per unit per frame is the primary scaling risk and is forbidden in the hot path. The Medical Cart rides this same spline (§8.4).

### 6.2 Layer 2 — Target Acquisition & Combat

- Acquire highest-priority enemy by §5.3 → set target lock → engage until death or out-of-range.
- Drives the two-phase attack loop from §5.2.
- **Aggro updates are dirty-flagged, not recomputed every frame** (§6.5).

### 6.3 Layer 3 — Survival & Behavior

Behavior diverges by tier — this is where individuality emerges. The two columns below show the extremes; the full tier ladder is §6.6.3:

| Behavior | Recruit (lowest tier) | Elite (highest tier) |
|---|---|---|
| Retreat threshold | Retreats to base at 20% HP | Fights until 5% HP |
| Targeting priority | Highest-priority by §5.3 | Also hunts dangerous enemy units (enemy Champions) |
| Passive effect | None | May emit an aura that buffs nearby allied recruits |

### 6.4 Layer 4 — Equipment

- Before marching, each soldier checks the arsenal.
- The soldier that equips the single available **legendary weapon** becomes the **Champion**: larger physical scale, glowing nameplate, and a significant stat bonus. *(Named "Champion" deliberately — "MVP" is reserved in this document for Minimum Viable Product.)*
- Equipment is a scarcity mechanic — there is normally *one* legendary, forcing the player to decide *who* deserves it (a logistics decision; supports Pillar 2).

### 6.5 AI Tick Architecture & CPU-Spike Mitigation (anti-lag)

```
SERVER
 ├─ NavigationScheduler   → updates every 0.2s (low frequency, batched); owns cart spline movement
 ├─ CombatScheduler       → each unit fires on its own cooldown timer (event-driven, not per-frame)
 ├─ BehaviorScheduler     → re-evaluates Layer 3 every 0.5s OR on HP-threshold events
 └─ ScoringScheduler      → recomputes Notable score every 1.0s, only for living units
```

- **Never run all four layers every frame for every unit.** Stagger them on independent intervals; combat is event-driven off cooldowns.
- **Dirty-flag aggro pattern (generalized).** Aggro-changing events — an Airdrop landing, an enemy Champion entering the field, a Medical Cart appearing — do **not** force every nearby AI to recompute targets in the same frame. The event sets `RequiresTargetUpdate = true` on enemies within its radius; the `CombatScheduler` then reads and clears these flags **spread across subsequent ticks** (time-slicing), diluting the CPU load. This is the standard mechanism for *all* aggro changes, not a special case for the Airdrop.
- **Time-slicing:** split the unit list across N frames so only `units/N` are processed per frame.

### 6.6 Competence Progression (Veterancy)

This system delivers the fantasy "*this soldier survived 40 battles, and you can see he's smarter than a recruit*" without real machine learning. The system does not simulate learning; it **stages its result**. The player cannot distinguish "the soldier learned to take cover" from "the soldier unlocked the cover behavior at Tier 3" — what they observe is identical, but the staged version is cheap, deterministic, server-authoritative, and fully tunable.

> **Naming.** Called **Competence / Veterancy** in code and docs, not "RL" or "learning." Real reinforcement learning would place neural-net inference inside the hot loop, which is incompatible with the range-and-cooldown, table-based, anti-lag architecture (§5, §6, §11) and with the deterministic security model (§11.1). Veterancy achieves the *felt* outcome at scheduler cost.

#### 6.6.1 The Core Driver — Survival

Competence accrues from **battles survived**, which is the design intent (survival = skill) *and* ties progression directly to the game's thesis: because soldiers gain competence by staying alive, and the player's job is to keep them alive via logistics, **progression and the core fantasy become the same act.** Every successful rescue (§8) does not just save a soldier — it protects his accumulated competence.

#### 6.6.2 The Curve — Logarithmic, ~40 battles to Elite

The player's explicit requirement is realism: no legends in 10 battles. A **logarithmic** curve delivers this — fast, visible early gains (a recruit improves quickly, hooking the player) followed by a long plateau (becoming Elite is expensive, so an Elite is rare and precious, reinforcing the 5-slot scarcity and the Fallen Heroes Wall).

```
Competence = floor( K * ln(1 + BattlesSurvived) )
```

`K` and the tier thresholds are tuned so Elite costs ~40 battles, not 10. Survival is the only input; the curve is the only pacing control.

#### 6.6.3 Tier Table — Unlocked Behaviors

Each tier unlocks branches in the **existing Layer 3 AI** (§6.3) and modifiers in §5 — it does not add a new system, it grows the state machine already specified.

| Tier | Battles survived (approx.) | Unlocked behavior |
|---|---|---|
| **Recruit** | 0–5 | Marches straight; strikes the nearest body mass; never uses cover; retreats at 20% HP (§6.3) |
| **Seasoned** | ~6–15 | Begins using cover points along the road; smarter retreat timing; slight precision/damage modifier |
| **Veteran** | ~16–35 | Aims strikes at high-damage points (the "where to strike" fantasy → a damage/precision multiplier); prioritizes dangerous enemy units (enemy Champions, §6.3) |
| **Elite** | ~36+ | Passive aura buffing nearby recruits; fights to 5% HP; reads aggro/barricade state; largest precision modifier |

#### 6.6.4 Visible Behavior vs. Invisible Stat — a deliberate split

The "where to strike for more damage" fantasy is implemented as **two layers the player reads as one skill**:

- **Visible behaviors** (cover use, target prioritization, fighting to 5%) — the player can *watch* the veteran do these. These carry the perception of skill and must be legible on camera (§7.3). Pillar 3.
- **Invisible modifier** (the "precise strike" damage/accuracy multiplier scaling with tier) — a hidden stat, surfaced only through *authored narration*, e.g. an alert or floating "Precise strike!" so the player attributes it to learned skill, not a dice roll.

The split matters: if "where to strike" were purely an invisible multiplier, the veteran would feel like a bigger stat block (the exact failure §5.1 warns against). Pairing the hidden modifier with visible behavior is what makes higher numbers read as *competence* rather than *inflation*.

### 6.7 Emergent Specialization, Customization & Army Progression

This section defines how soldiers become *roles* (tank/DPS/support), how the player customizes them, and how the army as a whole upgrades. The governing rule across all three: **power emerges from survival; the player authors only identity and logistics, never a soldier's combat power.** This keeps the human-scale pillar intact — a soldier is loved for who he *became*, not who the player *built*.

#### 6.7.1 Emergent Specialization (roles are revealed, not chosen)

The player never selects "make this one a tank." A soldier's role **emerges from how he survived**, read from stats the simulation already tracks. The `BehaviorScheduler` (§6.5) accumulates a survival-style tendency across the soldier's **entire history**, not just recent battles.

| Survival style (signal) | Emergent specialization |
|---|---|
| Survived absorbing damage and holding the line (high damage taken + high FrontlineTime, still alive) | **Bastion** (tank) |
| Survived by eliminating threats fast (high kills, short engagements) | **Reaper** (DPS) |
| Survived near rescues and allies (high RescueAssists, aura/support proximity) | **Anchor** (support) |

(Role names are placeholders; final naming belongs to the separate narrative document.) Because each role is the mathematical consequence of a survival style, specialization never contradicts Competence (§6.6) — it is the same survival, read from another angle.

**Tendency accumulation (the math).** After each battle the soldier survives, three lifetime accumulators are updated from that battle's normalized stats (each metric scaled 0–1 against the battle's own maximum):

```
B += 0.6 × DamageTakenNorm + 0.4 × FrontlineTimeNorm     (Bastion)
R += 0.7 × KillsNorm        + 0.3 × FinishingBlowsNorm    (Reaper)
A += 0.6 × RescueAssistNorm + 0.4 × AllyProximityNorm     (Anchor)
```

- Computed **once, post-battle** by the `ScoringScheduler` — zero hot-loop cost.
- All metrics are already tracked for the Notable score (§7.2) or trivially derived; the specialization system adds no new instrumentation.
- At crystallization (§6.7.2), `role = argmax(B, R, A)`. Ties resolve toward the tendency whose **single best battle contributed most** — the soldier's most dramatic moment decides who he is, which is the thematically correct tiebreaker.

#### 6.7.2 Crystallization at Veteran (the dramatic beat)

Specialization stays **fluid while the soldier is Recruit/Seasoned** — tendencies accumulate without commitment, and the game may hint at the lean ("Arthur has been holding the line"). On reaching **Veteran** (§6.6.3), the game reads the dominant lifetime tendency and the soldier **crystallizes** into that role permanently, unlocking that role's behaviors and cosmetic line.

- **Why crystallize (not stay fluid):** the North-Star (§1.1) needs the player to say "Arthur is a Bastion" with the same certainty as his name. A blurred 70/30 identity weakens the emotional read; this game optimizes for legibility over simulation fidelity.
- **The beat:** crystallization fires a cinematic alert (§7.4), e.g. *"Arthur has become a Bastion."* This turns a stat change into an authored narrative moment the game actively celebrates.
- **Anti-manipulation:** the read uses the soldier's **entire survival history**, so a player cannot "correct" a near-Reaper into a Bastion by forcing tanking in the last two battles — the prior battles outweigh recent ones. Combined with the ~16-battle Veteran threshold, deliberately steering a role is too expensive to be worth min-maxing.

#### 6.7.3 Customization — cosmetic only, scaling with tier

Customization is **purely cosmetic / identity-level** and never functional. It deepens attachment to a soldier who already earned it; it never fabricates power.

- **From Recruit (minimal):** the player can **rename** the soldier and apply a basic color. Naming is the first act of attachment and must be available early, so the 30-minute North-Star has time to land.
- **Scaling with tier:** more cosmetic options (marks, armor detail, insignia) unlock as the soldier climbs tiers. A heavily customized soldier is therefore, by definition, a long-survivor — customization becomes a **visible badge of veterancy** that reinforces field legibility (§7.3) rather than cluttering it.
- **Celebrating the role:** once crystallized (§6.7.2), the unlocked cosmetic line *fits the emergent role* — heavier armor visuals for a Bastion, etc. The player dresses the soldier as the role he *became*, never choosing the role through the wardrobe.

#### 6.7.4 Army Tech Tree (logistics, not individuals)

Player/commander progression unlocks a tech tree that upgrades the **army and its logistics**, never an individual soldier's stats. This is the systemic power axis, and it is pure Pillar 2.

- Examples: faster Medical Carts, higher-HP barricades, reduced rescue dispatch time, a second legendary-weapon slot, recruits that start at the Seasoned tier.
- **Hard rule:** the tech tree must never grant per-soldier stat choices. Individual power comes only from emergent Competence (§6.6) and emergent specialization (§6.7.1). Mixing army upgrades with individual stat-shopping would reintroduce min-maxing and erode Pillar 1.

#### 6.7.5 The Three Axes (summary)

| Axis | What it changes | Driver | Pillar |
|---|---|---|---|
| **Competence & specialization** | Soldier's power and role | Survival (automatic, emergent) | Pillar 1 |
| **Cosmetic customization** | Soldier's appearance / identity | Soldier's tier (player authors look, not power) | Pillar 4 |
| **Army tech tree** | Army-wide logistics | Commander progression | Pillar 2 |

The army begins fully generic. Every soldier starts as an un-customized Recruit and must earn both power and the right to be personalized by surviving.

#### 6.7.6 Known Tension (watch in playtest)

Crystallized role + heavy cosmetic investment makes PvP permadeath (§9.2) sting harder — losing a customized Veteran Bastion is a large loss. This is intended drama but a sharp edge; telemetry (§4.4) must watch whether it deepens attachment or drives players out, alongside the existing 5-slot/permadeath risk (§9.3).

#### 6.7.7 Role Kits — what crystallization unlocks

Each role unlocks a small, legible kit of behaviors and modifiers. Kits are **sidegrades around the same power budget**, not power jumps — the power comes from Competence (§6.6); the kit only shapes *how* it expresses.

| Role | Behavior unlocks | Modifier |
|---|---|---|
| **Bastion** | Anchors at cover points (§6.8) near allies; stands over allied soldiers in Agony, shielding them | +20% max HP; raised own ThreatWeight (≈15) so he *draws* fire — tanking is visible |
| **Reaper** | Re-targets twice as fast after a kill; prioritizes the enemy Champion and low-HP targets (the finisher) | Attack interval floor 1.0 s |
| **Anchor** | Moves to **escort an active Medical Cart** when within vision; gravitates toward clustered allies | Aura: −10% damage taken for allies within 15 studs |

- The Anchor's cart-escort behavior creates emergent rescue drama (a support hero racing to defend the cart) **without** violating §8.2's no-bait rule — escorting is protection, not sacrifice, and the Anchor fights normally.
- The Bastion's raised ThreatWeight plugs directly into the existing aggro formula (§5.3) — no new targeting code, just a weight.

### 6.8 Cover Points (road furniture)

Referenced by the Seasoned+ tiers (§6.6.3) and the Bastion kit (§6.7.7); specified here.

- **What they are:** discrete defensive positions along the road edges (overturned carts, rock piles, stakes), roughly every **40 studs**, alternating sides. Capacity: **1 soldier each**. Placement is fixed in the MVP and produced by the generator's rules Post-MVP (§16.3) — the 40-stud spacing is a generation invariant, not a hand-tuned constant per map.
- **Mechanical effect:** a soldier occupying a cover point takes **−30% damage** from attackers farther than ~10 studs and slightly lowers his own ThreatWeight (he is "dug in"). Point-blank melee ignores cover — cover helps you *hold*, not hide.
- **Behavioral rule:** Seasoned+ soldiers move to a free cover point when their target is beyond engage range or when HP < 50%; they leave cover to engage when an enemy enters melee range. Implemented as one extra branch in Layer 3 (§6.3) evaluated by the `BehaviorScheduler` — no pathfinding cost (cover nodes sit on the road spline).
- **Legibility:** stepping into cover is a *visible* veterancy behavior (§6.6.4) — a recruit stands in the open and a Seasoned soldier visibly takes position. The player reads experience at a glance.

---

## 7. Presence, Direction & Visualization

The player is neither a passive spectator nor a faceless floating camera. The interface is engineered to make the player **pick favorites**.

### 7.1 Commander Avatar

- A physical character the player controls in the barracks and at the front.
- Gives a sense of presence without involving the player in combat. The avatar cannot fight — its verbs are logistical (inspect, dispatch, supply).

### 7.2 Notable Soldiers Panel

- A side panel showing, in real time, the top 3 most-distinguished soldiers.
- **Scoring formula** (weighted so a defensive tank can become a favorite, not only a high-kill soldier):

```
Score = (Kills × 10)
      + (RescueAssists × 8)         ← lets support/tank heroes emerge
      + (FrontlineTime × 0.5)        ← rewards holding the line, not just killing
      + CompetenceTier
      + (TimeAlive × 0.2)
```

- **`RescueAssists`** = participation in an active rescue: fighting within a fixed radius of the barricade/cart while the operation runs (§8). Soldiers do not perform rescues — the cart does (§8.4); soldiers *assist* by protecting the operation. One increment per operation survived.

- Constants are placeholders; the design intent is **archetype diversity among emergent heroes**, not a single optimal build.
- The `CompetenceTier` term (§6.6) naturally weights a long-surviving veteran toward the panel, coupling visibility to veterancy.
- Recomputed by `ScoringScheduler` at 1 Hz over living units only (§6.5).

### 7.3 Dynamic Camera ("Follow" button)

- Clicking a soldier (in the panel or on the radar/map) instantly snaps the camera to an RTS-style over-the-shoulder view behind that NPC.
- This is the primary attachment-forming interaction. One click, instant.
- A focused unit is promoted to the **20 Hz replication tier** (§11.3) so its movement and HP read smoothly.

### 7.4 Cinematic Global Alerts

- The game *actively* surfaces dramatic moments via pop-ups, e.g. "Arthur has become a Bastion!", "Arthur is now a Veteran!", or "Your veteran Rodolfo has entered Agony!"
- Each alert offers a one-click jump to that event's camera.
- **Curation rule:** alerts are the game's narrator. A constantly-firing alert trains the player to ignore it — which kills the North-Star moment. The queue enforces priorities and a cooldown:

| Priority | Events | Queue behavior |
|---|---|---|
| **P0** | Roster soldier enters Agony; rescue resolved (saved / lost) | Always shown immediately; preempts the queue |
| **P1** | Crystallization ("became a Bastion"); promotion to Veteran/Elite | Shown next; never dropped |
| **P2** | Champion equipped; enemy Champion sighted; near-miss feedback (§12.3) | Shown if no P0/P1 pending |
| **P3** | Minor color (first kill, first cover use) | Shown only when the queue is idle |

- **Cooldown:** minimum ~8 s between non-P0 alerts. P0 ignores the cooldown — drama about a roster soldier's life is never delayed.

### 7.5 Post-Match Battle Report

A dedicated post-match screen — cheap to build, disproportionately valuable for attachment (Pillar 4):

- **Per roster soldier:** battle stats (kills, damage taken, frontline time, rescue assists), competence gained, and a one-line **tendency hint** generated from the specialization accumulators (§6.7.1), e.g. *"Arthur held the line again."* The hint foreshadows crystallization, building anticipation across sessions.
- **Rescue recap:** outcome of any rescue attempted, including the near-miss percentage (§12.3) — the failure is re-told, not buried.
- **Recruit Candidates:** generics who earned a name this match (§10.3) are presented here, with their revealed name and battle stats, for the player's sign-or-dismiss decision.
- The report is assembled from data the `ScoringScheduler` already holds at match end; no extra in-match cost.

### 7.6 HUD Layout (MVP)

| Screen region | Element |
|---|---|
| Bottom-right | Tactical radar (§11.3) — tap a unit to Follow; tap a downed roster icon to open the rescue action |
| Right edge | Notable Soldiers panel (§7.2) |
| Top-left | Supply meter (§8.7) |
| Top-center | Alert toasts (§7.4), one at a time |
| Contextual | **Rescue button** — appears only while a roster soldier is in Agony; one click launches airdrop + cart (§8.6) |

Design rule: the HUD must keep the **center of the screen clean** — the soldiers are the show; the interface is the stage lighting.

---

## 8. The Rescue System — Logistical Airdrop (Logistics Under Pressure)

This is the mechanical heart of the emotional thesis and is **mandatory in the MVP** (§2). It is designed to work on the 1D tug-of-war road without breaking the AI, by routing all tension through **threat manipulation (aggro)** rather than friendly-unit sacrifice.

### 8.1 Agony State

- When a tracked soldier reaches 0 HP, instead of dying it enters **Agony** for 60 seconds (tunable).
- During Agony the soldier is downed, vulnerable, and stranded on the road.
- A visible countdown and a global alert fire.

### 8.2 Logistical Airdrop

Rather than sending recruits to die as bait — which would cannibalize the thesis, since recruits are also named individuals — the player spends resources to **airdrop a destructible supply barricade** onto the downed soldier's location.

- The barricade has its own HP and a high threat weight (§5.3, weight = 100), so it **pulls the enemy horde's aggro** at medium/long range, drawing fire away from the rescue operation and clumping the enemy.
- The barricade is the shield; no friendly soldier is spent as bait. This keeps the rescue a *pure logistics* act (Pillar 2).

### 8.3 Absolute Risk — no safety nets

There are no automatic retreats and no fallback. Once committed:

- If the barricade falls early, the **Medical Cart becomes the highest-value target** the horde turns on.
- If the cart is intercepted, the player loses **both** the logistical resource **and** the veteran, instantly.

This stakes the decision honestly: committing to a rescue is a real gamble, and the gamble is what produces attachment.

### 8.4 The Vulnerability Window (dramatic climax)

The rescue is **not** completed by touch/collision. The Medical Cart must hold a **static 4.5-second loading channel** beside the downed soldier. The core tension becomes **two bars racing**: the barricade's HP melting versus the load timer advancing. The player watches, helpless to fight, able only to have supplied well or poorly.

- The cart rides the navigation spline (§6.1) as a smooth vector — it does **not** use free physics or `TweenService` (network/collision cost).

### 8.5 Non-Inflationary Legacy

- Veterans killed in PvP **do not drop weapons** — dropping the legendary would shatter the scarcity that makes §6.4 meaningful.
- Instead, the Fallen Heroes Wall grants small **non-monetary logistical** bonuses (e.g. a slight global reduction in rescue dispatch time). Loss is honored without inflating power. (See §9.2.)

### 8.6 MVP Simplification

For the prototype the rescue is reduced to its atom: **one** resource type fuels it, **one** button launches the airdrop + cart. Multiple cart types and upgrades are deferred.

### 8.7 The Supply Meter (the MVP's single resource)

The resource that fuels the rescue without requiring an economy:

- A single meter, **0–100 Supply**, regenerating passively at **2 Supply/s** while the match runs. Starts the match full.
- **One rescue (airdrop + cart) costs 80 Supply.** Nothing else consumes Supply in the MVP — generics respawn free (§4.3), so the meter exists exclusively to price the one costly decision (§2).
- The numbers produce the intended pressure: after a rescue (100 − 80 = 20 left), the player needs **30 s of regen** to afford another. With Agony lasting 60 s and the cart needing ~17 s to operate (§5.5), two roster soldiers falling close together forces a genuine choice — *which one do I save first, and does the second even have time?* That choice is the thesis (§1.1) compressed into one meter.
- Server-authoritative (`EconomyService`, §9.1): the client renders the meter; only the server mutates it.
- Post-MVP, Supply becomes the bridge into the full logistics economy (production, upgrades via the tech tree §6.7.4) — the meter is the seed, not a throwaway.

---

## 9. Data Architecture: PvE vs. PvP Separation

To eliminate illegitimate farming (alt-accounts across multiple machines feeding a main account), the game enforces **total data separation** between two universes.

| System | Offline Universe (PvE / Campaign) | Online Universe (PvP Competitive) |
|---|---|---|
| Economy & Items | Resources/weapons saved only in the PvE inventory | Resources/weapons collected and generated from scratch each match |
| Competence & Progression | Player and NPC progress restricted to PvE | Player and NPC progress restricted to PvP |
| Era Progression (§15.2) | Era advancement earned and saved in PvE only | Era advancement earned from scratch in the PvP profile |
| Soldier Death | **Temporary** — NPCs are wounded and return to the menu | **Airdrop rescue or Permadeath** |

### 9.1 Implementation Notes

- Maintain two independent persistent profiles per player keyed by universe (`profile_pve`, `profile_pvp`). They never read or write across the boundary.
- Use `DataStoreService` with **session-locking** (ProfileService pattern) to prevent duplication exploits and write races.
- All economy mutations are **server-authoritative**. The client never reports resource counts; it requests actions and the server validates.
- Because PvP resources are generated from scratch each match, there is no persistent PvP currency to farm — this is the structural anti-cheat, not a patch.

### 9.2 Soldier Death by Universe

- **PvE:** death is temporary; wounded soldiers recover. A low-stakes place to *form* attachment.
- **PvP:** Agony → airdrop-rescue-or-permadeath. Where attachment is *tested*. The Fallen Heroes Wall makes loss permanent and visible, granting only non-inflationary logistical bonuses (§8.5).

### 9.3 Balancing the Punishment (Design Risk)

The hard 5-slot roster plus PvP permadeath plus the "absolute risk" rescue (§8.3) is a real frustration risk: losing veterans *and* resources in one failed rescue can drive players out rather than deepen attachment. Mitigations, validated by telemetry (§4.4):

- Keep the rescue success rate inside the target band (§4.4); rebalance if it drops below the floor.
- Make recruiting a replacement fast, with its own emergent-hero potential, so loss feels like *turnover*, not *ruin*.
- Grief-to-pride conversion: the Fallen Heroes Wall mourns *and* honors loss (§8.5).

---

## 10. Persistent Progression & The Barracks Limit

### 10.1 Unique Identity

- Every generated soldier receives a random name and unique visual traits (scars, faces).
- Per-soldier stats (kills, rescue assists, time alive) persist between sessions in a per-universe table.

### 10.2 The Rule of Few

- The barracks has a **hard limit of slots (5 initial)**.
- Scarcity is the point: few slots force the player to remember each face and create hard discard decisions when a prodigy recruit appears (§10.3).
- Surface a soldier's stats at the moment of discard so the cost is felt.

### 10.3 Line Troops & Earning a Name

This resolves the composition gap (5 roster slots vs. 10 fielded, §4.3) and defines where new recruits come from.

- **Generic line troops** fill the field beyond the deployed roster. They are unnamed, visually simplified, non-persistent, and respawn freely (§4.3). They have no Agony state — they simply die.
- **Earning a name:** a generic who **finishes a match alive** with notable performance (placeholder threshold: ≥3 kills *or* ≥60 s of frontline time) becomes a **Recruit Candidate** in the Battle Report (§7.5). Only then is a name and face generated and revealed. The player may **sign** them into a barracks slot (forcing a discard if full — the §10.2 hard decision) or dismiss them.
- **Pillar reconciliation.** Pillar 1 says the player manages individuals, never anonymous clones — and the generics do not contradict this; they *enable* it. Identity in this game is **earned, not issued**: the crowd exists precisely so that individuals can emerge from it. The moment a generic earns a name is itself an authored beat (Pillar 3) — the game introduces you to someone who fought their way into existence.
- Signing decisions feed the attachment loop: the player chooses *who gets to exist*, which is investment (Pillar 4) before the soldier's first roster battle.

### 10.4 The Wounded State

Referenced throughout (§9.2, §12.1); defined here.

- A soldier returns **Wounded** after a successful rescue, or after any fall in PvE.
- **MVP rule:** a Wounded soldier is **unavailable for the next 1 match**, then returns to Active automatically. Flat and simple; severity scaling is deferred.
- Wounded soldiers remain **visible in the barracks** (bandaged) — recovery is shown, not hidden, because seeing Arthur bandaged after the rescue you pulled off is a free attachment beat.
- Roster pressure is intentional: with 5 slots and a soldier out for a match, the player feels the cost of every close call, not only of deaths.

### 10.5 Persisted Soldier Record (schema)

The per-soldier record stored by `PersistenceService` (§9.1), one table per universe:

```lua
SoldierRecord = {
  id = string,                -- stable unique ID
  name = string,
  visualSeed = number,        -- deterministic face/scars generation
  battlesSurvived = number,
  competence = number,        -- derived: floor(K * ln(1 + battlesSurvived)), §6.6.2
  tier = string,              -- RECRUIT | SEASONED | VETERAN | ELITE
  spec = { B = n, R = n, A = n },  -- tendency accumulators, §6.7.1
  role = string?,             -- nil until crystallization, §6.7.2
  stats = { kills, rescueAssists, frontlineTime, timeAlive },
  cosmetics = { ... },        -- unlocked/applied cosmetic IDs, §6.7.3
  status = string,            -- ACTIVE | WOUNDED | FALLEN
  woundedMatchesRemaining = number?,   -- §10.4
  fallen = { cause, date, finalScore }?  -- populated only on FALLEN (PvP), feeds the Wall
}
```

- `competence` is **derivable** from `battlesSurvived` and is stored only as a cache — the source of truth is the battle count, so a tuning change to `K` retroactively re-grades all soldiers consistently.
- The Fallen Heroes Wall (§8.5) reads only `fallen` records; it never needs live data.

---

## 11. Technical Architecture (Roblox / Luau)

### 11.1 Authority Model

- **Server-authoritative for everything that matters:** AI, combat resolution, economy, persistence, rescue outcomes.
- Client handles only **presentation**: camera, UI panels, alerts, VFX, radar. Never trusted with state.
- Communication via `RemoteEvent`/`RemoteFunction` with server-side validation on every action.

### 11.2 Suggested Module Layout

```
ServerScriptService/
 ├─ MatchService        (tug-of-war state §4.3, win/loss; SOLE owner of the EntityStore — §11.5)
 ├─ AIController        (orchestrates the four schedulers from §6.5)
 ├─ CombatResolver      (two-phase range + cooldown damage — §5.2)
 ├─ ScoringService      (Notable score §7.2; post-battle specialization accumulators §6.7.1)
 ├─ RescueService       (Agony state machine, airdrop + cart — §8 / §12.2)
 ├─ EconomyService      (server-authoritative Supply — §8.7 / §9.1)
 ├─ ReplicationService  (two-rate pipeline: 1 Hz matrix + 20 Hz focus channel — §11.3)
 ├─ TelemetryService    (rescue/attachment analytics hooks — §4.4)
 └─ PersistenceService  (per-universe profiles, session-locked — §9.1 / §10.5)

ReplicatedStorage/
 ├─ SoldierData         (shared schema, read-only to client)
 └─ Remotes             (validated RemoteEvents/Functions)

StarterPlayerScripts/
 ├─ CameraController    (Follow button, dynamic camera — §7.3)
 ├─ AlertController     (curated cinematic alerts, priority queue — §7.4)
 ├─ RadarController     (tactical radar from the global matrix — §11.3)
 ├─ ReportController    (post-match Battle Report — §7.5)
 └─ HUDController        (Notable panel, Supply meter, rescue button — §7.2/§7.6/§8)
```

### 11.3 Two-Rate Replication / Interest Management

To keep the network budget lean and still deliver the North-Star drama, the server segments the replication pipeline:

| Data type | Frequency | Transmission scope | Client use |
|---|---|---|---|
| **Tactical matrix** (ID, Team, ClassID, X/Z) | 1 Hz | Per player; own units always, enemy units only within revealed vision (§17.1) | Icons on the mini-map / radar |
| **Focused entities / active operations** | 20 Hz | Only clients with the camera locked on a unit **or** an active rescue on screen | Smooth rendering of load bars, HP, and cart movement |

> Note: with fog of war (§17), the tactical matrix is **per-player and vision-filtered**, not global — the server omits enemy entities the player has not revealed. In the MVP (no fog) it is effectively global.

- Roblox `StreamingEnabled` hides heavy 3D models in distant areas; the radar lets the player make global logistical decisions without rendering the whole army.
- **Active rescues are always high-priority replication** regardless of camera, so the 4.5s climax never stutters.
- **Payload format.** The 1 Hz matrix is serialized as a flat numeric array (`[ID, Team, ClassID, X, Z, ...]`), not a verbose keyed Luau table, to keep bandwidth low. `ClassID` reuses the entity's `ThreatWeight` (soldier/cart/barricade are already distinguished by it), avoiding an extra field. Positions are quantized to 0.1 stud. *(Known minor risk: at very low unit speeds, quantization can repeat a coordinate across two ticks, briefly freezing a radar icon; negligible at mini-map scale, flagged for awareness only.)*
- **Radar projection.** World→UI mapping is a fixed orthographic transform against the match's map bounds: `uiX = (worldX − minX) / (maxX − minX)`, `uiY = (worldZ − minZ) / (maxZ − minZ)`, applied as `UDim2` scale. Bounds are part of the match's map data — a constant in the MVP, emitted by the generator Post-MVP (§16.4); the transform itself is unchanged either way.

#### 11.3.1 Tier-Transition Smoothing (anti-"bungee")

A naive 1 Hz → 20 Hz promotion causes visible **rubber-banding**: a client holding a unit's last 1 Hz position (up to ~1 s stale) snaps the camera there, then the 20 Hz feed delivers the true position several studs away, teleporting the model on screen — exactly when the player focuses, breaking Pillar 3.

- **Mitigation: client-side interpolation (not extrapolation).** The radar icon is always drawn by lerping between the **two most recent received positions** (`Lerp(LastPosition, TargetPosition, alpha)` over the 1 s window), never by projecting forward from a velocity vector. Interpolation lags by one cycle but never overshoots; for a 2D mini-map icon, ~1 s of lag is imperceptible and smoothness matters more than temporal precision. *(Deliberately chosen over extrapolation, which overshoots and self-corrects on turns/stops, re-creating a micro-bungee.)*
- **`IsHighFrequency` handshake.** Each cached radar entry carries an `IsHighFrequency` flag. When the server promotes a unit to the 20 Hz tier, the client sets this flag on that entry; while set, the entry is **excluded** from both the 1 Hz interpolation loop and the radar-cleanup sweep (so a focused unit absent from the global matrix is not deleted). This flag is the explicit contract linking the radar (§11.3) to the focus/rescue pipeline (§11.3.2). It must be written on promotion and cleared on demotion — never left implicit.

#### 11.3.2 Focus/Rescue High-Frequency Channel

When the player triggers a focus (Follow) or a rescue, that unit/region is promoted to 20 Hz. **The promotion uses a dedicated high-frequency `RemoteEvent` channel directed only at the operating player — it does NOT move `Player.ReplicationFocus`.**

- **Rationale (Pillar 1 / §7.1).** `Player.ReplicationFocus` controls *3D instance streaming* around the player. Repointing it to a distant rescue site risks streaming-out the area around the commander avatar — the player could watch the ground vanish beneath their own avatar while spectating a far rescue. We keep `ReplicationFocus` anchored to the avatar (stable physical presence) and open a parallel data channel that feeds only the rescue camera/UI.
- **Two separate truths:** where the player *is* (instance streaming, anchored to avatar) vs. what the player is *watching* (the 20 Hz data channel). They never share an authority.

### 11.4 Performance Budget (anti-lag)

- Combat is event-driven off per-unit cooldowns, never per-frame.
- AI layers are staggered on independent intervals (§6.5); aggro changes use the dirty-flag + time-slice pattern.
- Object-pool soldiers, the cart, VFX, and alert UI to avoid instantiation spikes.
- The cart moves as a spline vector, not physics or `TweenService` (§8.4).

### 11.5 `EntityStore` — Ownership & Memory Lifecycle

All active units/entities live in a **pure Luau dictionary** (`EntityStore`), read directly from memory. `CollectionService` and `Attributes` are **banned from the hot loop** to avoid GC pressure. Strict ownership rules prevent leaks from retained references:

- **Single owner.** `MatchService` is the only server module permitted to **write or delete** keys in the global entity dictionary.
- **Access by ID, no long-term retention.** `CombatScheduler`, `NavigationScheduler`, and `RescueService` must **not** store entity-object references in long-lived locals. Every operation reads the table by `ID` (string).
  - *Single-tick exception:* a local reference is allowed **within the scope of one tick** (re-reading the dictionary by ID multiple times per frame for the same entity is wasteful); it must never persist into the next tick.
- **Death cleanup.** When a unit dies, `MatchService` removes the key. On the next cycle, the other schedulers read `nil`, automatically clear their search/target state, and release the instance to the Garbage Collector.

### 11.6 Scalability Path

The MVP runs ~20 units trivially. The architecture is designed so scaling to larger battles later requires only tuning scheduler intervals and widening time-slicing — not a rewrite. This is why server-authority, dirty-flag aggro, and the `EntityStore` discipline are decided *now*.

---

## 12. State Machines (Reference)

### 12.1 Soldier Lifecycle

```
[Idle/Barracks] → [Marching] → [Engaged] → [Retreating] → [Marching]
                                    │
                                    ▼
                                 [Agony] ──► rescued ──────────► [Wounded/Barracks]
                                    │
                                    └─ not rescued ─┬─ (PvE) ──► [Wounded/Barracks]
                                                    └─ (PvP) ──► [Dead] → [Fallen Heroes Wall]
```

### 12.2 Rescue Sub-Machine (Medical Cart)

```
[Agony start, 60s timer]
        │
   player launches Airdrop + Cart? ──no──► TIMER_EXPIRED ──► resolve by universe
        │ yes
        ▼
   ┌─────────────┐
   │  EN_ROUTE   │ ── cart intercepted? ──yes──► TOTAL_LOSS (reason: CART_INTERCEPTED)
   │ (cart rides │                               (no load %, so NO partial-failure feedback)
   │  spline)    │
   └─────┬───────┘
         │ cart reaches soldier
         ▼
   ┌─────────────┐
   │   LOADING   │ ── barricade destroyed mid-channel? ──yes──► PARTIAL_FAILURE
   │  (4.5s      │                                              → TOTAL_LOSS (reason: BARRICADE_DESTROYED)
   │  channel)   │                                              → client shows "% achieved"
   └─────┬───────┘
         │ channel completes
         ▼
   ┌─────────────┐
   │  RETURNING  │ ──► [Rescued] ──► soldier persists, returns wounded
   └─────────────┘
```

**`PARTIAL_FAILURE` is a sub-case of `TOTAL_LOSS` reachable *only* from `LOADING`.** A failure during `EN_ROUTE` has no loading percentage, so it resolves as a plain interception. This prevents an "85% of 0%" bug; the player-facing feedback is described in §12.3.

**The 60 s Agony timer keeps running through the entire operation.** If it expires while the cart is still `EN_ROUTE` (dispatched too late, or the route stretched by a pushed-back front line), the operation resolves as `TOTAL_LOSS (reason: TIMER_EXPIRED)` — the same reason code as never launching (§4.4). If it expires during `LOADING`, the `PARTIAL_FAILURE` percentage feedback applies. Launching is not a guarantee; it is a bet against the clock.

### 12.3 The "Near-Miss" Feedback (`PARTIAL_FAILURE`)

If the cart is destroyed *during* the 4.5s loading channel, the client displays the percentage reached (e.g. "Arthur was 85% to being saved"). This converts a dry mechanical failure into a legible tactical narrative — the player learns the rescue *was* possible and is motivated to try again. Legible failure teaches; opaque failure frustrates.

---

## 13. Open Questions & Roadmap

### 13.1 Open Questions

Deliberately unresolved; to be answered within prototyping.

1. **Notable formula constants:** Tune §7.2 so at least two distinct archetypes appear in the top 3 across test sessions.
2. **Success-band confirmation:** Validate that the 65–75% rescue success band (§4.4) is where attachment peaks; locate the true frustration cliff (§9.3).
3. **Cover density:** Is one cover point per 40 studs (§6.8) the right rhythm for a 400-stud road, or does it slow the tug-of-war below the 5–8 min round target?
4. **Earning-a-name thresholds:** Are ≥3 kills / ≥60 s frontline (§10.3) generous enough to produce ~1 candidate per match without flooding the report?
5. **Wounded duration:** Does the flat 1-match cooldown (§10.4) create interesting roster pressure, or should severity scale with how the soldier fell?
6. **Specialization weights:** Do the §6.7.1 accumulator weights produce a believable role distribution (~rough thirds), or does one role dominate?

### 13.2 Roadmap — Milestones with Exit Criteria

Each milestone has a hard exit criterion; do not advance without meeting it.

| Milestone | Build | Exit criterion |
|---|---|---|
| **M0 — Foundation** | `EntityStore`, four schedulers (§6.5), range/cooldown combat (§5), tug-of-war loop (§4.3), generics + Director (§4.3.1) | A 10v10 round runs 8 min within frame budget, no leaks (§11.5 verified under unit churn) |
| **M1 — Identity** | Names/visual seeds, persistence (§10.5), Notable panel (§7.2), Follow camera (§7.3), Battle Report (§7.5) | Playtesters recall a soldier's name unprompted after one session |
| **M2 — Replication** | Tactical radar, two-rate pipeline, anti-bungee, focus channel (§11.3) | Follow and radar are smooth at budget; no visible rubber-banding on promotion |
| **M3 — Rescue** | Agony, Supply meter (§8.7), airdrop + cart FSM (§12.2), telemetry (§4.4) | **The North-Star test (§1.1):** 30-min sessions; players know their best soldier's name and report the knot-in-chest moment; rescue success rate inside the band |
| **M4 — Veterancy & Roles** | Competence tiers (§6.6), cover (§6.8), crystallization + kits (§6.7), earning a name (§10.3), cosmetics (§6.7.3) | Two distinct archetypes appear in the Notable panel; players describe a soldier *by role* unprompted |
| **Post-MVP** | PvP universe + permadeath (§9), full economy: gathering, rarity & crafting (§14), tech tree (§6.7.4), era system (§15), procedural maps as RTS (§16), fog of war & recon (§17), Fallen Heroes Wall bonuses (§8.5) | Gated on M3's emotional validation; within Post-MVP, eras gate on the economy, cross-era PvP gates on same-era PvP (§15.6), and procedural maps + fog gate on the North-Star validating against the fixed full-information MVP map (§16/§17) |

The ordering is deliberate: **attachment is validated before logistics (M1 before M3), and logistics before any expansion (M3 before Post-MVP).** Each phase tests one hypothesis.

---

## 14. Economy Systems (Post-MVP): Resource Gathering, Rarity & Crafting

> **Scope gate.** Everything in this section is **Post-MVP** and gated on M3's North-Star validation (§13.2). Until then, the Supply meter (§8.7) is the game's entire economy. This section exists now so the economy is *designed before it is needed* — and designed under the same constitution: **the economy serves keeping soldiers alive, never power accumulation for its own sake** (Pillar 2).

### 14.1 The Three Resources

Deliberately few — each resource maps to one verb of care:

| Resource | Source | Feeds | The verb |
|---|---|---|---|
| **Provisions** | Farms/depot nodes | The Supply meter (§8.7): raises regen rate and cap | *Sustain* — rescues and reinforcement |
| **Timber** | Forest nodes | Crafting and repair (§14.4–14.5); barricade upgrades | *Build* — the shield between them and death |
| **Iron** | Mine nodes | Crafting and repair; weapon/armor quality | *Arm* — the edge they carry |

- Provisions plugging into the Supply meter is the structural link: the MVP's single resource becomes the consumption end of the full economy, exactly as §8.7 anticipated ("the meter is the seed").
- No fourth resource without a new *verb of care* to justify it. Resource-type creep is scope creep.

### 14.2 Resource Gathering — Territorial & Automated

The commander does not click on trees. Gathering is **logistics**, played at the level of routes, territory, and protection:

- **Resource nodes** sit along the road's flanks (forests, mines, farm depots), placed by the same rules that position cover (§6.8, §16.3). A node is **accessible only while the front line (§4.3) is pushed beyond it** — territory *is* the harvest.
- **Supply Carts** (a sibling of the Medical Cart) automatically shuttle between the base and accessible nodes along the navigation spline (§6.1). The player sets **priorities** (which resource to favor), not waypoints — decisions, not micromanagement.
- **Carts are interceptable.** A Supply Cart has HP and a mid ThreatWeight (≈30, below the Medical Cart's 50 — saving a life outranks saving cargo, by design). An enemy push past the front line raids your supply route. Protecting logistics *is* the game.
- **The central tension this creates:** pushing the line deeper unlocks richer nodes but stretches your soldiers thinner and your cart routes longer — *greed measured in risk to the people you love*. Holding back is safe and poor. This single trade-off is the strategic layer of the tug-of-war.
- **Per-universe behavior (§9):** in PvE, stockpiles persist between sessions. In PvP, nodes are harvested **from scratch each match** — consistent with the structural anti-farm rule (§9.1). No persistent PvP wealth exists to bot.
- **Technical reuse:** Supply Carts ride the same spline system, live in the same `EntityStore` (§11.5), and use the same aggro formula (§5.3). No new movement or targeting code — only a new `ThreatWeight` and a route schedule owned by the `NavigationScheduler`.

### 14.3 Rarity — Scarcity Without RNG

Four quality tiers, with hard anti-inflation rules:

| Tier | How it exists | Power budget | Reads as |
|---|---|---|---|
| **Common** | Default production | Baseline | Issued kit |
| **Sturdy** | Standard Forge output (§14.4) | +5% | Reliable steel |
| **Masterwork** | High-tier Forge, unlocked deep in the tech tree (§6.7.4); expensive in Iron | +12–15% | A named smith's pride |
| **Legendary** | **Never craftable.** Found/awarded in rare authored events only; normally **one** exists (§6.4) | Champion bonus | Myth |

**Hard rules:**

1. **No random drops.** Enemies drop nothing; chests roll nothing. Rarity is the output of *deterministic production quality* — better forge, better steel. A logistics game earns its items through industry, not slot machines.
2. **Legendary stays out of the crafting loop.** The Champion's weapon (§6.4) is meaningful because it is singular; a craftable legendary would dissolve §8.5's entire non-inflation stance.
3. **Equipment power is capped low (≤~15%)** while Competence (§6.6) ranges far wider. A Masterwork sword on a Recruit loses to an Elite with a Common one. *The soul outranks the steel* — this is the rule that protects Pillar 1 from the entire economy.

### 14.4 Crafting — The Forge

- **Deterministic recipes.** The player selects a recipe (e.g. *Sturdy Sword: 4 Iron, 2 Timber*); the output is exactly what the recipe says. Quality is gated by **Forge upgrades on the army tech tree** (§6.7.4) — never by roll.
- **Production queue, between matches (PvE).** The Forge lives in the barracks; orders queue and complete between battles. Crafting is preparation — the quiet act of care before the storm — not a mid-combat distraction.
- **PvP field version:** a stripped-down field forge with per-match recipes built from per-match resources, consistent with the from-scratch PvP economy (§9.1).
- **No crafting UI in combat.** During a battle, the only economic verb is spending Supply on rescues. The battle's focus budget is reserved for the soldiers.

### 14.5 Allocation & Maintenance — Equipment as a Logistics Decision

- **Equipping is choosing who deserves what** — the same decision the legendary already forces (§6.4), now extended army-wide. Layer 4 of the AI (§6.4) already handles arsenal checks; rarity adds depth without new behavior code.
- **Wear on fall:** when a soldier falls into Agony or returns Wounded (§10.4), his equipment becomes **Damaged** — functional at reduced effect until repaired (a fraction of the craft cost in Timber/Iron). Every close call thus has a *material* cost as well as an emotional one, keeping the economy circulating without grind: maintenance is generated by drama, not by timers.
- **Loss on death (PvP):** a soldier who dies permanently takes his equipment with him — recorded on his Fallen Heroes Wall entry (§8.5). The gear is part of the memorial, not salvage. This extends the no-weapon-drop rule to its honest conclusion: you do not loot the dead you loved.

### 14.6 Anti-Inflation Guardrails (summary)

| Rule | Protects |
|---|---|
| No random drops; production is deterministic | The game's identity (logistics, not looter) |
| Legendary never craftable | Champion scarcity (§6.4), §8.5 |
| Equipment ≤ ~15% power; Competence dominates | Pillar 1 — the soldier matters more than the item |
| No player-to-player trading (either universe) | §9.1's structural anti-farm; prevents RMT economies |
| Dead soldiers' gear is memorialized, never recovered | Non-inflationary legacy (§8.5); the weight of loss |
| PvP resources from scratch every match | §9.1 |

### 14.7 Telemetry Additions

When this layer ships, extend §4.4 with: `Telemetry_Node_ControlTime` (per node), `Telemetry_Cart_Intercepted` (gathering loss events), and `Telemetry_Forge_QueueDepth` — the first two tune the territorial risk/reward curve; the third detects whether crafting reads as care or as chore.

---

## 15. The Era System (Post-MVP): Army Evolution Across History

> **Scope gate.** Eras ship after the full economy (§14) and after **same-era PvP is validated**. Cross-era PvP (§15.5) ships last of all, behind its own validation gate (§15.6). The MVP remains medieval-only (§4.1).

The army evolves through historical eras — Medieval, Gunpowder, the Great War (WWI), the World War (WWII) — each unlocking new equipment, logistics vehicles, battlefield furniture, and tech-tree branches. The era is the *context*; the soldiers are the *constant* (§15.3).

### 15.1 The Era Ladder

| Era | Combat character | Unlocks (examples) | Logistics expression |
|---|---|---|---|
| **I — Medieval** | Melee + short-range archery; engage range ~5–25 studs | Baseline kit; **war mounts** (§15.8.1) | Medical Cart, palisade barricade |
| **II — Gunpowder** | Line volleys; engage range ~40 studs | Muskets, sabers, light cannon; **saber cavalry** (§15.8.1) | Horse-drawn wagon, earthwork barricade |
| **III — Great War** | Sustained ranged; engage range ~60 studs | Rifles, machine-gun nests (static, high ThreatWeight); **first armor & recon aircraft** (§15.8.2–15.8.3) | Motor truck, **trenches** (evolved cover, §15.4), sandbag barricade |
| **IV — World War** | Ranged + suppression; engage range ~70 studs | Semi-auto rifles; **tanks, strike aircraft & fighters** (§15.8.2–15.8.3) | **Ambulance** (faster Medical Cart), fortified barricade |

- Each era adds **one new battlefield concept**, not ten — eras are paced like tiers, not expansions. The table is extensible (future eras append without redesign).
- Era-specific Forge recipes (§14.4) and tech-tree branches (§6.7.4) open on advancement; earlier-era recipes remain available (a WWII army can still build cheap palisades).

### 15.2 Era Advancement

- Advancing is the **capstone of the army tech tree** (§6.7.4): a high-cost research unlock paid in all three resources (§14.1) — the most expensive logistics decision in the game.
- **Per-universe (§9):** PvE era progress and PvP era progress are fully separate, consistent with total data separation. A player's PvP era is whatever their PvP profile has earned from scratch.
- Advancement is **permanent** — research is never lost — and **additive**: the player may deploy as any unlocked era (loadout choice pre-match). Owning WWII does not delete the medieval army; it adds an option. This matters for cross-era matchmaking (§15.7) and for players who simply love their knights.

### 15.3 Souls Persist Across Eras

The roster (§10.2) **transcends the era.** When the army advances, Arthur does not get deleted and replaced — the same soldier, with the same name, scars, Competence (§6.6), and crystallized role (§6.7.2), now carries a rifle instead of a sword. The continuity of the *people* through changing technology is the emotional spine of long-term play, and the deepest expression of Pillar 1.

Roles **re-express** per era — same soul, new tools:

| Role | Medieval expression | Great War / World War expression |
|---|---|---|
| **Bastion** | Tower shield, anchors at palisades | Holds the machine-gun nest / fortified trench position |
| **Reaper** | Duelist, hunts the enemy Champion | Marksman priority targeting; finisher fire |
| **Anchor** | Escorts the Medical Cart on foot | Rides escort with the Ambulance; aura as squad cohesion |

- Mechanically this is **zero new behavior code**: the role kits (§6.7.7) are parameter sets, and eras re-skin the parameters (which cover node type the Bastion anchors at, which vehicle the Anchor escorts).
- The Fallen Heroes Wall (§8.5) records the **era of death** — "fallen in the Great War" — giving the memorial historical depth for free.

### 15.4 Technical: Eras Are Data, Not Code

The architecture absorbs eras without structural change — this is why the early decisions were made the way they were:

- **The "fake" combat system (§5) is era-agnostic by construction.** Ranged combat is the same range-and-cooldown resolution with a larger `maxRange`. No projectile physics, no hitscan — a rifle is a 60-stud sword with a different telegraph animation (§5.2). Server cost is identical across eras.
- **Trenches are cover points (§6.8) with era parameters:** higher damage reduction (−50%), multi-soldier capacity, positioned along the road by the cover-placement rules (§16.3) with an era-dependent type. The cover *behavior* is unchanged; only the node data differs.
- **Logistics vehicles are the same spline entities** (§6.1, §14.2) with era speeds: cart → wagon → truck → ambulance. The Ambulance is simply a Medical Cart with higher speed — which directly tightens the rescue math chain (§5.5) and is therefore a *real* logistical upgrade, not a skin.
- **Per-era tuning lives in data tables** (engage ranges, intervals, ThreatWeights, vehicle speeds) keyed by era ID. The four schedulers (§6.5), the `EntityStore` (§11.5), and the replication pipeline (§11.3) are untouched.

### 15.5 Cross-Era PvP — The Legacy Handicap

Cross-era matches (e.g. Player A's medieval army vs. Player B's WWII army) are permitted, leveled by an automatic compensation system applied to the **older** army. The handicap scales with the **era gap** `g` (number of eras between the two armies):

```
HP        × (1 + 0.35 × g)
Damage    × (1 + 0.25 × g)
DamageTaken × (1 − 0.15 × g)   -- the defense term: incoming damage reduced
MoveSpeed × (1 + 0.10 × g)     -- closing speed: the anti-kiting term
SupplyCosts × (1 − 0.15 × g)   -- rescues/reinforcement cheaper
GenericRespawn × (1 − 0.20 × g) -- the old army replenishes faster
```

*(All constants are placeholders; the tuning target is a 45–55% cross-era win rate band, measured by telemetry.)*

**Why the handicap is not stats alone.** Pure stat inflation (HP/damage/defense only) produces a degenerate pendulum (§15.6). Two additional terms stabilize it:

- **Closing speed** attacks the real asymmetry — range — directly: knights who *arrive* are knights who fight.
- **Logistical compensation** (cheaper Supply, faster replenishment) is the thematically correct term for *this* game and the historically honest one: low-tech forces have always compensated with numbers, cost, and a light logistics tail, while modern armies drag a heavy one. In a game about logistics, the old army's advantage *is* logistics.

The result reads as a fantasy both players accept: the medieval army is a **relentless, cheap, fast-replenishing tide**; the modern army is **fewer, deadlier, more expensive soldiers** holding ground with firepower. Asymmetric identities, not a stat mirror.

### 15.6 The Range Problem (known risk #1 of this entire section)

Stats compensate numbers; they do not compensate **mechanics**. The modern army shoots first across 60+ studs; the medieval army must *travel* to fight. The balance between "the tide reaches melee and crushes" and "the tide dies walking" is **unstable** — small tuning shifts swing it violently, and both failure modes feel terrible (the modern player: "my rifles don't kill swordsmen?!"; the medieval player: "I never even arrive").

Mitigations, in order of leverage:

1. **Closing speed + respawn terms** (§15.5) keep pressure continuous instead of all-or-nothing.
2. **Cover/trench density** (§6.8, §15.4) gives the advancing army survivable geometry — tuning cover spacing is tuning the matchup.
3. **The barricade economy:** a Post-MVP Supply action lets the player airdrop **standalone barricades** (extending §8.2 beyond rescues) — older eras' cheaper Supply (§15.5) makes mobile cover their signature tactic for crossing open ground.
4. **Validation gate:** cross-era PvP ships only after same-era PvP holds the 45–55% band for *every adjacent-era pair* (gap 1) before any gap-2+ match is enabled. Gap is widened one step at a time, each step re-validated.

If the band cannot be held for some pairing, that pairing is **restricted in matchmaking** rather than shipped broken — an honest limitation beats a degenerate matchup.

### 15.7 Matchmaking Rules

- **Ranked: same-era only.** Competitive integrity is not negotiable; the handicap is a leveling tool, not a ranked-fairness proof.
- **Casual: cross-era allowed**, handicap applied automatically and **disclosed in the lobby** (both players see the multipliers — hidden handicaps breed conspiracy theories).
- Since players may deploy any *unlocked* era (§15.2), a veteran player can deliberately field their beloved medieval roster against modern opponents — the handicap makes nostalgia viable, which protects long-term attachment to old soldiers.

### 15.8 Mounts, Vehicles & Aircraft — The Combined-Arms Layer

> **Governing principle: vehicles are equipment; crews are souls.** The emotional unit of this game is always the soldier (Pillar 1). A horse is a mount the soldier rides; a tank is armor the soldier crews; an aircraft is a machine the soldier flies. Machines are crafted, repaired, and lost as *matériel* (§14); the people inside them live, fall into Agony, and are rescued as *people* (§8). No machine ever has a name, a tier, or a place on the Wall — its crew does.

#### 15.8.1 Mounts (Eras I–II)

- A mount is **equipment** (§14.4-craftable, rarity up to Masterwork) assigned to a soldier — the unit on the field is still that soldier, now faster.
- **Mechanics:** high move speed; a **Charge** bonus (first strike on engaging while at speed deals bonus damage and briefly staggers the target's attack cooldown). After the charge, the rider fights as normal cavalry melee.
- **Counters:** soldiers in cover (§6.8) and behind barricades negate the Charge bonus entirely — the charge needs open road.
- **The mount can die under its rider:** mount HP is tracked separately; when it falls, the soldier dismounts (briefly staggered) and continues **on foot**. Legible drama at zero extra systems — the player watches Arthur's horse fall and Arthur stand back up.
- **Historical obsolescence as mechanics:** in Era III+, trench density (§15.4) and machine-gun nests make Charge unusable along most of the road. Cavalry is not nerfed by patch notes — it is *aged out by the battlefield itself*, exactly as in 1914–1918. The game teaches the history mechanically.

#### 15.8.2 Ground Vehicles (Eras III–IV)

- **Light armor (Era III) → tank (Era IV):** a slow, high-HP, high-ThreatWeight entity on the same road spline. Crewed by **1–2 soldiers** (roster or generic) assigned pre-match in the Layer-4 arsenal step (§6.4).
- **What armor is for:** the tank **ignores cover damage-reduction** of enemies it engages, **crushes barricades and trench segments** on contact (slowly), and shrugs small-arms fire. It is the trench-breaker — the mechanical answer to the era that killed cavalry. Its counters: cannon (Era II+ recipe kept relevant), strike aircraft (§15.8.3), and cost.
- **Cost is the balance:** vehicles consume significant Supply to field, take Damaged state aggressively (§14.5), and repair in Iron. A tank is a *logistical commitment*, not a default.
- **Crew and destruction:** when the vehicle is destroyed, surviving crew **bail out into Agony beside the wreck** — the standard rescue system (§8) takes over seamlessly. The wreck itself persists briefly as road furniture (improvised cover, §6.8) before despawning: even destruction feeds the cover game.
- **Roster crews amplify attachment:** putting Arthur in the tank makes the tank precious *because Arthur is inside* — the machine borrows its meaning from its crew, never the reverse.

#### 15.8.3 Aircraft (Eras III–IV): Sorties, Not Units

Aircraft never live on the road and never join the tug-of-war. They exist as **sorties**: temporary entities that enter on a parallel **air spline** above the road, perform one pass, and exit. This preserves the 1D battlefield that every system depends on, and it is the historically honest model of tactical air support.

| Sortie type | Era | Effect |
|---|---|---|
| **Recon** | III+ | One pass; reveals detailed enemy data on the radar (positions at 20 Hz fidelity for ~20 s — a temporary, server-granted exception to the 1 Hz global tier, §11.3) |
| **Strike** | IV | One pass; damage along a short road segment — barricades and armor take full damage, infantry in trenches take reduced |
| **Fighter** | IV | Launches *reactively* to intercept an enemy sortie; brief air-to-air resolution on the air spline (same range-and-cooldown math, §5) |

- **The pilot is a soldier** (roster or generic). A sortie is launched from the base, costs substantial Supply, and has a long cooldown — air power is rare punctuation, not a spam loop. **Max 1–2 sorties simultaneously** per match (hard cap; performance and readability).
- **Being shot down is the game's most dramatic rescue.** A downed pilot enters Agony **wherever he fell along the road — possibly deep behind the enemy line.** A behind-the-lines pilot rescue (long cart route, hostile territory, the full §8 apparatus stretched to its limit) is the apex expression of the North-Star: maximum distance, maximum cost, maximum love.
- **Fighters answer strikes:** if the opponent fields air power, your fighter cover negates it — a clean counter pair. No anti-air ground grind in scope; the counter is symmetrical and legible.

#### 15.8.4 The Counter Story (history as balance)

| Threat | Countered by | The history it tells |
|---|---|---|
| Cavalry charge (I–II) | Cover, barricades, formed infantry | Open-field shock vs. prepared positions |
| Trenches + MG nests (III) | **Armor** (15.8.2) | Why cavalry died and tanks were born |
| Armor (III–IV) | Cannon, strike aircraft, cost | Combined arms — no single answer |
| Strike aircraft (IV) | Fighters | Air superiority as enabling condition |

Each era's signature threat is answered by the next era's signature unlock. Cross-era PvP (§15.5) inherits these counters, which is part of why the Legacy Handicap can stay numeric — the *mechanical* counterplay already exists in the unit roster.

#### 15.8.5 Technical Notes (full reuse)

- Mounts: a speed/charge parameter set on the existing soldier entity. No new entity type.
- Vehicles: standard `EntityStore` entities (§11.5) on the existing road spline with vehicle-class `ThreatWeight`; crushing barricades is a contact check the `NavigationScheduler` already approximates for the cart.
- Aircraft: **temporary** `EntityStore` entities on a second authored spline (the air spline); spawned, run one pass under the `NavigationScheduler`, despawned by `MatchService` (single-owner rule intact). No flight physics, no 3D pathing — a sortie is a moving point with a schedule.
- Replication: sorties and active vehicles are **always 20 Hz tier** (§11.3) — they are rare, dramatic, and few by the hard cap, so the budget holds.
- The sortie cap (1–2) is not only performance: it keeps the sky *eventful*. A plane that appears twice a match is drama; constant air traffic is noise (§7.4's curation logic, applied to the battlefield itself).

#### 15.8.6 Scope Discipline

Combined arms ships **inside the era ladder** — mounts with Era I–II, armor and air with Era III–IV (§15.1) — and inherits every gate above it (§13.2, §15.6). Nothing in this subsection exists in the MVP. If scope must be cut, cut from the sky downward: fighters first, then strikes, then armor — mounts are nearly free (a parameter set) and survive any cut.

---

## 16. Procedural Maps as Real-Time Strategy (Post-MVP)

> **Scope gate.** The MVP map is hand-authored and fixed (§4.2). Everything here ships **Post-MVP**, after the North-Star (§1.1) is validated on the controlled map — variety and terrain strategy are introduced only once attachment is proven on one known map.

The battle map is not a backdrop the player acts *upon* — it is a **constraint the player must read and answer in real time.** Each match generates one shared, procedural battlefield from rules; the terrain *asks a question* (where are the chokepoints, how far is the wealth, where can cavalry charge) and the player's logistics *are the answer* (where to commit barricades, which cover to garrison, how far to gamble a push). This turns logistics from "execute rescues" into "read terrain and commit resources in space" — the deepest expression of Pillar 2. Combined with fog of war (§17), the map becomes the central strategic layer: a real-time RTS of supply, scouting, and positioning, fought by soldiers the player loves.

### 16.1 The Two Layers: Fixed Terrain vs. Player Placement

The critical split. If the player could move *everything*, every map would collapse to one optimal solution and the terrain would become decorative. So the map has two layers:

| Layer | Who decides | Examples | Role |
|---|---|---|---|
| **Fixed terrain** | The generator (immutable for the match) | Road shape, chokepoints, flank width, **resource node locations**, base positions | The *question* — the constraint the player cannot change |
| **Player placement** | The player, live, during combat | Where to airdrop barricades (§8.2), which cover points to garrison and with whom, how far to push to capture a node, where to site a trench/MG nest (Era III+) | The *answer* — where skill lives |

Because terrain is fixed and only *resource commitment* is free, **every generated map poses a genuinely different tactical question.** A chokepoint near your base demands defense; rich nodes placed far demand an aggressive gamble. The player reads, then responds — and because the placement is *theirs*, when Arthur dies on a barricade the player sited badly, the fault is the player's. Fault is attachment: the terrain is the stage, the player's placement is the script, the soldiers are the actors.

### 16.2 Real-Time, No Prep Phase

There is **no pre-battle planning screen.** The match begins and the player discovers the map *as units advance into it* (§17, fog of war). All placement decisions are made live, under pressure, as the front line moves and the unknown resolves — true to the "logistics commander under fire" fantasy. The tension is reading a battlefield you cannot fully see while committing resources you cannot fully afford.

### 16.3 Generation: Rule-Governed, Not Random

"Procedural" means *rule-governed assembly*, not chance. The generator is a **constraint satisfier**: it varies the fixed-terrain layer within hard invariants that guarantee every map is a legible, winnable 1D tug-of-war. A candidate violating any invariant (§16.4) is rejected and re-rolled, never shipped — a purely random map could produce an unreadable or unfair battlefield, the opposite of the legibility every system depends on (Pillar 3).

### 16.4 Hard Invariants (never violated)

1. **Topology is always a 1D corridor.** A single contestable axis from Blue to Red base; it may bend or pinch, but the front line (§4.3) must stay a well-defined scalar position along a primary spine. No open 2D arenas — the AI, replication, and tug-of-war stack assume the corridor.
2. **A single primary road spline** connects the bases end-to-end (navigation backbone, §6.1). Branches rejoin the spine; no dead ends.
3. **Symmetry of opportunity.** Terrain is balanced between halves so neither base starts advantaged. PvP requires mirrored or rotationally-symmetric layouts; PvE may relax this for designed difficulty.
4. **Road length within range** (e.g. 350–550 studs) so rounds stay in the 5–8 min target (§4.3).
5. **Cover density within the §6.8 band** (≈1 per 40 studs ± tolerance) — enough to enable veterancy behaviors, not so much that the push stalls.
6. **Reachability.** Every cover point, node, and rescue position sits on or adjacent to the road spline (no pathfinding islands — §6.1 forbids heavy pathing).

### 16.5 Generation Parameters (the rules that vary)

| Parameter | Range / options | Strategic question it poses |
|---|---|---|
| Road shape | Straight, bent, S-curve, pinch | Sightlines and how the front flows (interacts with fog, §17) |
| Cover rhythm | Even / clustered / sparse (within §16.4 #5) | Clustered favors Bastions; sparse favors mobility |
| Node placement | Distance of richest nodes from center | How far to gamble a push (greed-vs-risk, §14.2) |
| Chokepoints | 0–2 narrow segments | Where pushes stall and rescues turn desperate |
| Flank width | Narrow ↔ wide shoulders | Room for cavalry charge (§15.8.1) and cart routing |
| Era dressing | Per-era furniture types (§15.4) | Cosmetic + parameter swap, not a new ruleset |

- **Era is an input, not a separate generator.** One ruleset produces a medieval lane or a WWII front; only furniture *type* and engage-range context change.
- PvE biome tags (e.g. "mountain pass" → more chokepoints) bias parameters without touching invariants.

### 16.6 Technical: Deterministic, Server-Authoritative, Seed-Based

- **The generator runs once on the server at match start**, producing a compact **map descriptor**: spline control points, fixed node/cover/base positions and types, and map bounds.
- **Seed-based determinism.** Generation is a pure function of a seed plus parameters. The server stores the seed in match state and ships the *descriptor* (not streamed geometry) to clients, **subject to fog-of-war filtering (§17)** — clients receive terrain as they discover it, not all at once. Both players share one seed, guaranteeing the same battlefield.
- The descriptor feeds the radar projection (§11.3) and `MatchService`. Generated cover/nodes register into the `EntityStore` (§11.5) exactly as fixed ones would — downstream systems cannot tell a generated map from a hand-authored one.
- **No runtime generation cost.** All placement happens at start-up before units spawn; the hot loop (§6.5) never sees the generator. Rejected candidates re-roll in the same step, bounded by a max-attempts cap that falls back to a known-good template.
- **Reproducibility.** A map is fully defined by its seed — problematic layouts reproduce from the seed alone for debugging and fairness review.

### 16.7 Authoring Still Matters

Designers author the **rules, invariants, parameter ranges, and fallback templates**, and curate **seed pools** — vetted seeds known to produce excellent maps — for ranked PvP and key campaign beats, where a great fixed layout beats a random good one. The generator provides breadth; human curation guards the peaks.

### 16.8 Telemetry Additions

Extend §4.4 with `Telemetry_Map_Seed` (per match, for reproducibility), `Telemetry_Map_RerollCount` (invariant-failure rate — a spike means the rules are too tight), and per-seed aggregates of round length and win-side bias (detects layouts quietly favoring one base, feeding back into §16.4 #3).

---

## 17. Fog of War & Reconnaissance (Post-MVP)

> **Scope gate.** Ships with procedural maps (§16), Post-MVP. The MVP is full-information on its fixed map. Fog of war is what makes terrain (§16) and scouting *matter* — without it, a generated map is decoration; with it, every meter of road is an unanswered question until someone goes to look.

The shared battlefield (§16) is covered in fog. Each player sees only what their own units currently reveal. The terrain, enemy positions, enemy barricades, and contested nodes beyond your sight are **unknown** — discovered in real time by pushing units forward, AoE/StarCraft-style, inside a 1D corridor. This is the system that elevates the map from backdrop to the game's strategic core.

### 17.1 The Golden Rule (anti-cheat, §9.1)

**The server never sends a client what that player should not see.** Fog is not a client-side visual mask over full data — that is trivially hacked. Vision is computed **server-side per player**, and the replication pipeline (§11.3) transmits only entities within that player's revealed area. A client that strips its own rendering still receives nothing it has not earned. This makes §11.3's "global tactical matrix" **per-player and vision-filtered**, not global — the one structural change fog imposes, and a necessary cost of honest fog.

### 17.2 Transparency of Your Own; Darkness of Theirs

The division that protects the North-Star (§1.1):

- **Your own units are always fully visible to you** — position, HP, Agony state, everything. Fog never hides your soldiers from you. When Arthur falls into Agony you *always* know instantly (the alert, §7.4, still fires), so the emotional core is untouched.
- **Fog hides the enemy and unexplored terrain only.** You earn knowledge of *their* army and the *far* ground by looking.

This asymmetry is the rule: total clarity about the people you love; earned darkness about everything else.

### 17.3 Dynamic Darkness (explored ≠ permanently visible)

Three states per region of the corridor:

| State | What you see |
|---|---|
| **Unexplored** | Nothing — terrain shape and contents unknown |
| **Active vision** | Full real-time view: terrain + live enemy unit positions (a unit of yours is currently there) |
| **Remembered** | Terrain you have seen stays known (its shape, node locations), **but live enemy movement there is hidden again** once you leave |

Leaving an area drops it from Active to Remembered: you recall the ground but lose the live picture. This makes reconnaissance a **continuous investment**, not a one-time checklist — to know what the enemy is doing *now*, you must keep eyes there. It rewards maintaining scouts and creates the classic dread of a position you cleared an hour ago and can no longer see.

### 17.4 Reconnaissance as a Tactical Resource

Vision becomes something you spend units to obtain:

- Every unit has a **vision radius** (the §5.5 value, ~40 studs) that reveals fog around it as it advances.
- **Scout-leaning units see farther.** Vision radius is a unit property, so mounts (§15.8.1, fast wide-scouting) and the **Recon aircraft sortie** (§15.8.3, a sweeping pass that reveals a long stretch for ~20 s) are the dedicated recon tools — already specified, now given purpose.
- **Emergent scouts.** Because vision is a property and survival shapes specialization (§6.7.1), a soldier who survives by ranging ahead can lean toward a scouting identity. Recon is not a separate system; it is a role the battlefield reveals — consistent with §6.7's whole philosophy.
- **The recon-vs-commit tension:** units sent ahead to *see* are exposed and away from the front line's push (§4.3). Scouting costs pressure; blindness costs ambushes. That trade is the real-time strategy.

### 17.5 Fog and the Radar (§7.2 / §11.3)

- The tactical radar shows **your units always**, **terrain as Remembered-or-better**, and **enemy units only where you have Active vision.** Enemy icons wink out as they slip into fog — itself a piece of information ("they were heading there 5 seconds ago").
- A Recon sortie (§15.8.3) temporarily promotes a stretch to Active vision at 20 Hz fidelity (the §11.3 exception already noted), then it decays back to Remembered.

### 17.6 Technical Notes (server-side vision)

- **Vision computation** runs in a dedicated low-frequency pass (e.g. 4–5 Hz, between the §6.5 schedulers' cadence): for each player, union the vision radii of their living units along the 1D corridor into a set of revealed intervals. The corridor topology (§16.4 #1) makes this cheap — vision is intervals on a line, not 2D field-of-view.
- **Replication filtering:** `ReplicationService` (§11.2) intersects each entity's position against the requesting player's revealed intervals before including it in that player's 1 Hz/20 Hz payload (§11.3). Remembered terrain is sent once on first reveal; live enemy entities are sent only while inside Active intervals.
- **Cost honesty:** per-player vision-filtered replication is more expensive than one global matrix — this is the server cost of dynamic darkness, accepted deliberately (§17.3). The interval-based model keeps it tractable; the unit cap per match bounds it.
- All vision is server-authoritative; the client renders fog from the filtered data it legitimately receives and nothing more (§17.1).

### 17.7 Telemetry Additions

Extend §4.4 with `Telemetry_Recon_UnitTimeAhead` (scout exposure), `Telemetry_Ambush_Events` (kills made on units with no prior Active vision of the attacker — the cost of blindness), and `Telemetry_Map_RevealedFraction` at match end (how much of the map a player ever saw — tunes whether fog is too thick or too thin).

---

## 18. Glossary

| Term | Meaning |
|---|---|
| **Agony** | 60 s downed state of a roster soldier at 0 HP; the rescue window (§8.1) |
| **Airdrop Barricade** | Destructible, high-threat supply drop that pulls horde aggro during a rescue (§8.2) |
| **Anchor / Bastion / Reaper** | The three emergent specializations: support / tank / damage (§6.7.1) |
| **Champion** | The soldier holding the single legendary weapon (§6.4). Never called "MVP" — that term is reserved for Minimum Viable Product |
| **Charge** | Mounted first-strike bonus; negated by cover and barricades (§15.8.1) |
| **Competence** | The veterancy stat derived from battles survived (§6.6) |
| **Crew** | Soldiers assigned to a vehicle; they bail into Agony when it is destroyed (§15.8.2) |
| **Crystallization** | The moment at Veteran tier when a soldier's role becomes permanent (§6.7.2) |
| **Damaged** | Equipment state after its bearer falls; reduced effect until repaired (§14.5) |
| **Director** | The minimal script controlling the Red side in the MVP (§4.3.1) |
| **EntityStore** | The pure Luau dictionary holding all live entities; single-owner, no retained references (§11.5) |
| **Era / Era Gap** | A historical technology stage of the army (§15.1); the gap is the era distance between two PvP opponents (§15.5) |
| **Fallen Heroes Wall** | Permanent memorial of PvP-dead soldiers; grants non-inflationary bonuses (§8.5) |
| **Fog of War** | Per-player server-side vision; you see your own units always, enemy/terrain only when revealed (§17) |
| **Forge** | The barracks crafting facility; deterministic recipes, quality gated by tech tree (§14.4) |
| **Generic / Line Troop** | Unnamed, non-persistent filler soldier; may earn a name (§10.3) |
| **Legacy Handicap** | Automatic cross-era PvP compensation: stats + closing speed + logistics terms scaling with era gap (§15.5) |
| **Loading channel** | The 4.5 s static vulnerability window of the Medical Cart (§8.4) |
| **Map Descriptor** | Compact server-generated map definition (spline, cover/nodes, bounds) shipped to clients (§16.4) |
| **Map Invariant** | A hard rule every generated map must satisfy or be rejected (§16.2) |
| **Masterwork** | Highest craftable rarity tier; Legendary is never craftable (§14.3) |
| **Mount** | Rideable equipment (Eras I–II); can die under its rider, who fights on (§15.8.1) |
| **North-Star** | The single success metric: name recall + the knot-in-chest moment (§1.1) |
| **Provisions / Timber / Iron** | The three Post-MVP resources: sustain / build / arm (§14.1) |
| **Recon** | Vision gained by advancing units / scout sorties; a continuous investment under dynamic darkness (§17.3–17.4) |
| **Resource Node** | Flank-side gathering point, accessible only while the front line is pushed beyond it (§14.2) |
| **Remembered / Active vision** | Fog states: terrain you recall vs. ground you currently see live enemy movement in (§17.3) |
| **Roster** | The player's 5 named, persistent barracks slots (§10.2) |
| **Seed** | The integer that deterministically defines a generated map; stored in match state (§16.4) |
| **Sortie** | A temporary aircraft pass on the air spline: recon, strike, or fighter (§15.8.3) |
| **Supply** | The MVP's single resource; prices the rescue (§8.7) |
| **Supply Cart** | Automated gathering cart; interceptable, lower ThreatWeight than the Medical Cart (§14.2) |
| **Trench** | Era-III+ evolution of cover points: higher reduction, multi-soldier capacity (§15.4) |
| **Two-rate replication** | 1 Hz global matrix + 20 Hz focus channel (§11.3) |
| **Wounded** | Post-rescue/PvE-fall status; unavailable one match (§10.4) |

---

*End of technical draft v1.5. Lore, worldbuilding, and narrative to be authored in a separate document.*
