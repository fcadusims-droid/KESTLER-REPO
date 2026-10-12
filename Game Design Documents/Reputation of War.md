---
title: "Reputation of War"
description: "Technical game design document for a Roblox strategy game where the player is a commander who keeps a squad of individually-named soldiers alive through logistics — and whose choices about how that power is used turn each soldier, and the commander, into a hero or a villain."
genre: "Squad Tactics / Logistics / Reputation"
category: "Game Design Document"
---

# Reputation of War — Technical Game Design Document

**Version:** 2.0 (Feature-Complete Technical Draft)
**Document type:** Technical GDD — systems, mechanics, and architecture only
**Platform target:** Roblox (Luau, server-authoritative)
**Status:** Pre-production / Vertical Slice definition

> **Note on scope.** This document is intentionally *technical*. Lore, worldbuilding, faction names, character names, and narrative fiction are deliberately omitted and will be authored separately. Where a name is needed for an example (e.g. "Arthur"), treat it as a placeholder. The working title *Reputation of War* is itself a placeholder — the reputation/morality system (§9) is why the title is no longer *Heroes' Logistics*: the player does not only make heroes.

---

## 1. Design Pillars

These pillars are the constitution of the project. Any feature that does not serve at least one of them is a candidate for cutting. When two features conflict, the lower-numbered pillar wins.

1. **Human scale over aggregate statistics.** The player manages *individuals* (Arthur, Carlos, Rodolfo), never anonymous clones. Every system must surface the individual, not the crowd. A squad of ten is ten faces, not one health bar.

2. **Logistics is power; what you do with power is who you are.** The player's fantasy is *keeping favored soldiers alive and effective through logistics* — supply, equip, reinforce, rescue. But logistics buys reach, and reach forces choices: spare or execute, protect or plunder, hold the line or break it. The core verbs are never raw "attack." They are the logistical verbs plus the *moral* verbs those logistics make possible. Keeping a squad alive is the price of admission to the decisions that define a reputation.

3. **Coordinated squads, not ten soloists.** A squad of soldiers behaves as a *unit* — it moves together, flanks together, covers its own — while each member remains an individual with a name, a history, and a role. The tension between "the squad as a body" and "the soldier as a person" is the heart of the tactical layer.

4. **Emergent stories, authored drama.** The simulation generates events; the presentation layer (alerts, dynamic camera, notable panel, reputation beats) curates them into a narrative the player can follow and care about.

5. **Attachment through investment.** Players bond with what they spend effort on. Every emotional peak — a rescue, a betrayal, a soldier's fall — must be preceded by a costly player decision.

### 1.1 The North-Star Success Metric

The prototype is a success if, after 30 minutes of play, the player **knows the name of their best soldier**, **feels the stakes when that soldier enters the Agony state** on the battlefield, and **can articulate one moral choice they made** ("I executed the surrendering squad to protect my flank, and I'd do it again" / "I lost Arthur because I refused to sacrifice the prisoners"). The first two clauses test attachment; the third tests that the reputation layer produced a decision the player owns. Everything below is in service of producing those moments.

---

## 2. What the Prototype Must Actually Validate

The concept carries three hypotheses, and the Vertical Slice is designed so each is tested by a specific, minimal mechanic rather than assumed.

| Hypothesis | The claim | The minimal mechanic that tests it |
|---|---|---|
| **H1 — Attachment** | Players bond with individually-named, persistent soldiers. | Named roster + persistence + Follow camera (§8). |
| **H2 — Logistics as love** | *Doing* logistics under pressure — not just watching — is what creates attachment. | The Rescue: one costly logistical decision on the field (§7). |
| **H3 — Reputation as identity** | Players will make, own, and remember a moral choice their power enabled. | One binding moral decision per session (§9.4), with a visible reputation consequence. |

The risk to guard against: shipping a Vertical Slice that validates only H1 (an auto-battler where you get attached to NPCs) and *assumes* H2 and H3. The slice below keeps its minimalism but forces **one rescue** and **one moral decision** into every session, because those are the smallest atoms of the two hypotheses that are actually the game. A slice without them tests a third of the thesis.

---

## 3. Core Loop

### 3.1 Macro Loop (Session-to-Session, Persistent)

```
   ┌────────────────────────────────────────────────────────────┐
   │                                                              │
   ▼                                                              │
[Barracks] → [Compose Squad] → [Deploy] → [Battle] → [Moral      │
   │              │                           │        Junctions] │
   │              │                           │           │       │
   │              │                           ▼           ▼       │
   │              │                   [Logistical     [Reputation │
   │              │                    Decisions:      shifts]    │
   │              │                    supply,           │        │
   │              │                    rescue,           │        │
   │              │                    reinforce]        │        │
   │              │                                      │        │
   └── [Persist stats + reputation, retire/recruit, manage slots] ┘
```

### 3.2 Micro Loop (In-Battle, Moment-to-Moment)

```
Read the battlefield (multiple routes, front lines, squad positions)
        │
        ▼
Issue a high-level order (advance / flank right / hold / fall back)
        │
        ▼
Squad AI executes; individuals fill their roles within it
        │
        ├──► A soldier falls into Agony  ──► Decide: rescue? (spend Supply)
        │
        └──► A Moral Junction fires       ──► Decide: the binding choice (§9.4)
        │
        ▼
Watch it resolve → feel relief, grief, guilt, or pride → loop
```

The micro loop now has **two** kinds of intervention, not one: the *logistical* (rescue) and the *moral* (junction). Both must be fast — from "I see the situation" to "I can act on it" in **under 5 seconds** — or the drama dissipates. The order-issuing layer sits above both and runs continuously.

---

## 4. Vertical Slice (MVP) Definition

### 4.1 Scope Table

| Keep in MVP | Cut from MVP (Post-MVP) | Add vs. a naive auto-battler |
|---|---|---|
| One squad of named soldiers vs. AI opponent | Manual crafting & full economy (§16) | Multi-route battlefield (§6) |
| Range/cooldown combat with squad coordination | Multiple eras — one era only (§17) | High-level order system (§6.4) |
| Notable Soldiers panel + dynamic camera | Full PvP networking (§14) | Logistical Airdrop Rescue (§7) |
| Commander avatar (presence, non-combatant) | Procedural maps (§18) | One binding Moral Junction per session (§9.4) |
| Cinematic global alerts | Fog of war (§19) | Persistence of soldier identity, stats & reputation |
| Supply meter (§7.7) | Deep reputation tree (§9.7) | Squad-level Agony + Fallen/Fell-From Wall (§9.6) |

### 4.2 MVP Map

- Two bases: Blue (player) vs. Red (AI opponent).
- **Three parallel routes** connecting the bases — a central road and two flanking paths — joined at **two junction nodes** where a unit can cross between adjacent routes (§6.1). This is the minimum topology that makes "flank" a real verb while keeping every path a cheap spline to follow.
- The MVP map is **hand-authored, fixed, and full-information** — one known layout, no fog. Procedural maps (§18) and fog of war (§19) are Post-MVP: the North-Star (§1.1) is validated against *one* controlled, fully-visible map so attachment and moral weight — not novelty or scouting — are what is being measured. Treat the MVP map as the degenerate, minimal case of the procedural ruleset (§18.4).

### 4.3 MVP Win/Loss — Multi-Route Tug-of-War

Each route `r` has its own front-line scalar `L_r` (`0` = Blue base, `RouteLength_r` = Red base). Each moves toward whichever side has local superiority *on that route*:

```
dL_r/dt = k × (BlueEffectiveNearFront_r − RedEffectiveNearFront_r)
```

`EffectiveNearFront` is not a raw head-count — it is the **flanking-adjusted** strength defined in §6.5, so a squad that pincers a route from two sides pushes harder than its numbers alone. Overall victory is decided by an aggregate: a side wins when it pushes the *weighted* front position past the enemy base threshold, where the central route is weighted highest (it is the shortest path to the base). The exact aggregation weights are `[PLACEHOLDER — tune in M2]`; the design intent is that winning the center matters most but a decisive double-flank on both wings can also break the enemy.

- `k` is tuned so a typical round lasts **≈6–9 minutes** — long enough for a soldier to gain competence, become notable, get into danger, trigger a rescue, and reach at least one Moral Junction.
- Front-line positions are recomputed by `MatchService` at 1 Hz (§13.3) — cheap and legible on the radar.

**Field composition.** The player fields one squad of up to **10 units**, but the barracks holds a small number of **named, persistent slots** (§12.2). The difference is filled by **generic line troops**: unnamed, non-persistent soldiers auto-supplied by the base (§12.3). The named roster is the emotional core; the generics are the crowd from which new names — and the troops whose behavior feeds reputation — emerge.

### 4.3.1 The Opponent (MVP AI Director)

- Red units run the **same squad AI** (§6) — no special enemy code path.
- A minimal **Director script** replaces the enemy player: it maintains Red's field, issues simple orders (push the weakest route, flank when it has numbers), and may include 1–2 fixed mid-tier soldiers so the player faces visible skill contrast.
- The Director has **no rescue system and no Agony** for its units in the MVP, and does not participate in Moral Junctions — Red units simply die, and Red is never offered a moral choice. Asymmetry is acceptable: the prototype tests the *player's* attachment and the *player's* reputation, not enemy parity.
- Difficulty has exactly three knobs: respawn delay, count of mid-tier units, and flank-aggression of the Director. No adaptive difficulty in the MVP.

### 4.4 MVP Validation Plan & Telemetry

**Attachment proxies (H1/H2)**
- Did the player click "Follow" on any soldier?
- Did the player attempt at least one rescue?
- Post-session unprompted recall: "What was your best soldier's name?"

**Reputation proxies (H3)**
- Did the player reach and resolve the session's Moral Junction (§9.4)?
- Post-session unprompted recall: "Tell me about a choice you made." — the true H3 win condition is that the answer is specific and owned, not "I don't remember."

**Telemetry hooks**

| Event | Fires when |
|---|---|
| `Telemetry_Order_Issued` | Player issues any high-level order; records order type |
| `Telemetry_Flank_Resolved` | A flanking bonus (§6.5) is applied in combat |
| `Telemetry_Rescue_Attempted` / `_Succeeded` | Airdrop launched / soldier returns to base |
| `Telemetry_Rescue_Failed_Reason` | `TIMER_EXPIRED`, `BARRICADE_DESTROYED`, or `CART_INTERCEPTED` |
| `Telemetry_Junction_Reached` | A Moral Junction is presented to the player |
| `Telemetry_Junction_Choice` | Records which branch the player took, and time-to-decide |
| `Telemetry_Reputation_Delta` | Any reputation change, with source (junction vs. emergent §9.3) |

**Tuning targets.** Rescue success rate for first-session players: `[PLACEHOLDER — tune toward a band where attachment peaks; provisionally 65–75%, but the true band is an M3 finding, not a decision]`. Any value that produces mass abandonment after a lost soldier triggers rebalancing. Junction reach-rate should be **100%** — if a player finishes a session without hitting the junction, the pacing (§9.4) is broken, not the player.

> **A note the old document lacked.** The success band above is written as a *hypothesis to locate*, not a decision already made. M3 (§15) measures where attachment peaks, and — critically — also measures **post-loss churn**, because "did the player quit after a soldier died?" is a different question from "did the rescue succeed?", and it is the one the frustration risk (§14.3) actually turns on.

---

## 5. Combat Resolution ("Fake" Combat by Range & Cooldown)

Combat is **resolved by range and cooldown timers**, RPG-style, not by physics or hit detection. This is a deliberate performance and readability choice: it keeps server cost low and makes outcomes legible to the commanding player. The squad-coordination layer (§6) sits *on top* of this resolution — it decides *where* soldiers go and *who* they focus, but individual attacks still resolve through the cheap timer model below.

### 5.1 Attack Resolution

- Each soldier holds a **target lock**: it engages the highest-priority enemy (see §5.3, as modified by squad focus §6.6) within its vision radius and commits until one dies or the target leaves range.
- Attacks fire on a cooldown via the two-phase protocol in §5.2.

| Unit tier | Attack interval | Design intent |
|---|---|---|
| Recruit | 1.8 s | Baseline; feels deliberate, slightly clumsy |
| Higher tiers | down to 1.0 s (ladder in §5.5) | *Looks* more skilled without inflating raw damage — speed reads as competence |

> **Design principle:** Veterans should feel better through *cadence and behavior*, not bigger numbers. A faster, smarter soldier reads as a hero; one that just hits harder reads as a stat block.

### 5.2 Two-Phase Damage Validation (no phantom hits)

To eliminate phantom damage from animation/telegraph latency, the server delegates only the *visual* execution to the client and keeps factual truth behind two temporal checks:

- **T₀ (attack start):** Server confirms the target is alive and in range, then fires the `Telegraph` event so the client plays the (heavy) attack animation.
- **T_damage (attack resolution):** After the animation duration elapses, the server **re-validates** the target before applying HP reduction. If the target has entered Agony, died, or retreated beyond `maxRange + latencyMargin`, the damage is **discarded**.

The telegraph is purely cosmetic; truth is decided at resolution. `latencyMargin` exists so a target legitimately retreating at the edge of range is not punished by network jitter.

### 5.3 Target Acquisition — Aggro-Weighted Effective Distance

The AI does not attack what is *geographically* nearest; it attacks what is mathematically most *valuable*, balancing threat against proximity. To avoid native square roots in the hot loop, the comparison uses squared distance divided by a **linear** threat weight:

```
EffectiveDistanceSquared = RealDistanceSquared / ThreatWeight
```

**Threat weights (placeholder tuning):** Airdrop Barricade = 100, Medical Cart = 50, Soldier = 10. Lowest `EffectiveDistanceSquared` wins the lock. Because the divisor is linear, proximity still dominates point-blank while threat steers medium/long-range choices — a barricade (§7.2) pulls the horde without breaking close combat. **Squad focus (§6.6) can override this** by broadcasting a shared priority target, which is applied as a large temporary `ThreatWeight` multiplier on that one enemy for the squad's members only.

### 5.4 Damage Model

- Flat damage per hit, modified by equipment, Competence tier (§11.6), and **flanking bonus (§6.5)**.
- No armor/resistance layers in the MVP — they obscure the "is my soldier winning?" read the player needs from the camera. The one positional modifier that *does* exist is the flank bonus, because it is the mechanical payoff of the whole squad-coordination pillar and must be legible.

### 5.5 Baseline Numbers (MVP placeholders, internally consistent)

All values are tuning placeholders **designed to close as a system** — the rescue math (§7) and flank math (§6.5) must keep balancing whenever any one changes.

| Parameter | Value | Note |
|---|---|---|
| Route length (each) | 400 studs | Bases at 0 and 400; midpoint 200 |
| Junction node positions | ~130 & ~270 studs | Where crossing between routes is possible (§6.1) |
| Soldier walk speed | 12 studs/s | ≈33 s base → midpoint |
| Melee engage range | 5 studs | `maxRange` in §5.2 |
| Vision radius | 40 studs | Target acquisition scan (§5.3) |
| Recruit HP / damage | 100 HP / 12 per hit | ≈6.7 DPS; recruit-vs-recruit TTK ≈16 s (long enough to watch and react) |
| Flank damage bonus | +35% | Applied to attacks on an enemy engaged from a non-frontal angle (§6.5) |
| Tier attack interval | 1.8 / 1.6 / 1.2 / 1.0 s | Recruit / Seasoned / Veteran / Elite |
| Tier precision modifier | +5% / +15% / +25% | Seasoned / Veteran / Elite (§11.6) |
| Medical Cart speed | 16 studs/s | Base → midpoint ≈12.5 s |
| Barricade HP | 400 | See rescue math (§7.8) |
| Agony duration | 60 s | §7.1 |
| Loading channel | 4.5 s | §7.4 |
| Generic respawn delay | 8 s | §4.3 |

> **On these numbers.** They are a *starting point for tuning*, not a derivation of correct values. The old document presented a chain of estimates (reaction time + travel + channel) as "why these numbers are what they are"; that chain is a reasonable first guess, but real reaction time under a chaotic multi-route battle is an empirical question M3 answers, not a spreadsheet. Barricade HP and cart speed are the primary success-rate dials (§7.8); everything else is held fixed so rebalancing stays diagnosable.

---

## 6. Squad Coordination & the Multi-Route Battlefield

This is the largest structural change from a single-soldier auto-battler, and it is Pillar 3 made mechanical. A squad is not ten soldiers who happen to be near each other — it is a coordinated body with a shared objective, shared focus, and a formation, while every member stays an individual (Pillar 1). The player commands it through **high-level orders**; the squad AI resolves the details.

### 6.1 The Battlefield Topology: Routes and Junctions

The battlefield is **not** an open 2D arena and **not** a single 1D corridor. It is a small graph of **parallel routes joined at junction nodes** — the minimum structure that makes flanking a real spatial verb without the cost of free 2D pathfinding.

- **Routes** are splines (like the single road of a corridor design). The MVP has **three**: `Left`, `Center`, `Right`. Units follow their current route's spline — cheap waypoint following, no A*.
- **Junction nodes** are fixed points where a unit may **cross to an adjacent route** (`Left↔Center`, `Center↔Right`). Crossing is the *only* lateral movement; between junctions a unit is committed to its route. This is what keeps navigation to "which spline am I on + how far along," a two-number state per unit.
- **Flanking** is therefore a concrete decision: send part of the squad to cross a junction and hit an enemy front from the side or rear on the adjacent route. It is not free traversal of terrain; it is graph movement with a real time cost (crossing takes seconds, during which the flankers are off the front line and exposed).

```
Blue base                                             Red base
   │                                                      │
 L ●───────────────◐ J1 ───────────────◐ J2 ─────────────● L
   │                │                   │                 │
 C ●───────────────◐ J1 ───────────────◐ J2 ─────────────● C
   │                │                   │                 │
 R ●───────────────◐ J1 ───────────────◐ J2 ─────────────● R
                    ▲                   ▲
              junction node       junction node
            (cross L↔C, C↔R)    (cross L↔C, C↔R)
```

**Why this and not open 2D.** Open 2D requires per-unit pathfinding recomputed as the battlefield changes — the exact scaling risk this architecture exists to avoid on Roblox. The route-graph gives genuine spatial coordination (splitting, flanking, converging) while every unit's navigation stays a spline-follow. The honest trade-off: this is "attack from 2–4 fixed angles," not "surround from any direction." That is the correct fidelity for a prototype, and the topology can be widened Post-MVP (§18) if playtests demand it.

### 6.2 The Squad as an Entity

A squad is a first-class object in the `EntityStore` (§13.5), separate from its members:

```lua
Squad = {
  id          = string,
  team        = "BLUE" | "RED",
  memberIds   = { string, ... },   -- soldier IDs; membership can change (deaths, reinforcement)
  order       = SquadOrder,        -- current high-level order, §6.4
  formation   = "LINE" | "COLUMN" | "WEDGE" | "SCATTER",  -- §6.3
  anchorRoute = "LEFT" | "CENTER" | "RIGHT",  -- the route the squad's mass holds
  focusTarget = string?,           -- shared priority target, §6.6; nil = individual targeting
  cohesion    = number,            -- 0..1, how tightly members hold formation, §6.7
}
```

Soldiers keep their own entity record (§12.5); the squad only holds *references by ID* and the collective intent. A soldier can be **detached** from its squad (e.g. sent to flank) and rejoin — detachment is how a flank is executed without a second squad object.

### 6.3 Formations

A formation is a **relative offset pattern** applied along and across the current route. It is not physics; each member is assigned a target slot (an offset from the squad's front position on its route) and walks to it via the same spline-follow used for everything else.

| Formation | Shape | Use |
|---|---|---|
| **LINE** | Members spread laterally across the route width | Default; maximizes soldiers in contact, holds a front |
| **COLUMN** | Members stacked along the route | Fast travel / crossing a junction; weak in contact |
| **WEDGE** | A point soldier forward, others trailing back | Punches into a line; the point takes the hits (put a Bastion there, §11.7) |
| **SCATTER** | Loose spacing | Reduces losses to area threats; weak cohesion bonus (§6.7) |

Formation is chosen automatically by the squad AI based on the order (a `FLANK` order forces `COLUMN` during the crossing, then `LINE` on arrival), but the player can override it. Slot assignment respects roles: the tankiest members (Bastions, §11.7) are assigned front slots, damage-dealers (Reapers) the flanks of the formation where they can exploit flank bonuses.

### 6.4 High-Level Orders (the player's tactical verbs)

The player never micromanages individual soldiers. The player issues **orders to the squad**, and the squad AI executes. This is the "commander, not puppeteer" model and it is what keeps Pillar 1 intact even in a tactical game — you command people, you do not pilot them.

| Order | What the player specifies | What the squad AI resolves |
|---|---|---|
| **ADVANCE** | Which route to push | Formation, pace, when to engage, target selection |
| **HOLD** | Where to dig in | Which cover points to occupy, retreat thresholds |
| **FLANK** | Which route to cross to, at which junction | Who detaches, the crossing path, timing, rejoin |
| **FALL BACK** | (none — just the order) | Orderly retreat along the route, rear-guard assignment |
| **FOCUS** | An enemy target (tap it) | Broadcasts shared priority (§6.6); individuals re-target |

Orders are issued via the radar/tactical view (§13.3) or the follow camera. Each is **one interaction** — tap a route, tap a junction, tap an enemy. The 5-second responsiveness rule (§3.2) applies: an order must visibly begin executing within a second of issuing it, or the commander fantasy breaks.

### 6.5 Flanking — the Mechanical Payoff

Flanking is the reason the multi-route topology exists. It resolves as a **damage bonus and a front-line pressure multiplier**, both driven by *engagement angle*, which the route graph makes cheap to compute.

An enemy is **flanked** when it is engaged by squad members from **two different routes at the same junction-adjacent segment**, or from **front and rear on the same route**. Because position is "(route, distance-along)", the angle test is a comparison of two integers and a sign, not a 2D dot product:

```lua
-- Returns true if `attacker` hits `target` from a flanking angle.
-- Positions are (routeId, s) where s is distance along the route spline.
local function isFlanking(attacker, target, engagers)
    -- Case A: attacker is on a different route than the target's "facing" route,
    -- and both are within a shared junction band.
    if attacker.routeId ~= target.routeId
       and inSameJunctionBand(attacker.s, target.s) then
        return true
    end
    -- Case B: same route, but another friendly engages from the opposite side,
    -- so `target` is caught between two engagers (front and rear).
    for _, other in ipairs(engagers) do
        if other.id ~= attacker.id
           and other.routeId == target.routeId
           and sign(other.s - target.s) ~= sign(attacker.s - target.s) then
            return true  -- pincered
        end
    end
    return false
end
```

- A flanking hit deals `+35%` damage (§5.5) and the flanked enemy's contribution to *its* side's `EffectiveNearFront` (§4.3) is halved while flanked — so a successful pincer both kills faster and pushes the front. This is why `dL_r/dt` uses `EffectiveNearFront`, not a raw head-count: coordination beats numbers, which is the whole point of Pillar 3.
- **Legibility (Pillar 4).** A flanked enemy shows a clear visual (a red arc, a "Flanked!" floating tag) and the flank contributes a P2 alert (§8.4) when it's a roster soldier landing the pincer — the player must *see* that their maneuver worked, or the tactical layer is invisible math.

### 6.6 Shared Focus (squad-level target priority)

By default each soldier targets by §5.3 individually — good for a brawl, bad for concentrating fire. A **FOCUS** order (§6.4) sets `Squad.focusTarget`. While set:

- Every squad member applies a large temporary `ThreatWeight` multiplier to that one enemy in its §5.3 computation, so the squad collapses fire onto it without abandoning self-preservation (a soldier at melee range still handles the point-blank threat first — the multiplier steers, it doesn't override survival).
- This is how you kill an enemy Champion (§11.4) or an enemy Bastion before it anchors: focus, then flank.
- Focus decays after the target dies or leaves vision; the squad returns to individual targeting.

### 6.7 Cohesion (the glue, and the failure mode)

Cohesion is a `0..1` squad stat that models how well the squad is holding together. It is the mechanical expression of "a squad is more than its members."

- **Full cohesion** grants a small squad-wide bonus: `−10%` damage taken while in formation, faster order execution. A tight squad is a tougher squad.
- Cohesion **drops** when members die, when the squad is split too long (a flank that never rejoins), when the leader (§6.8) falls, or under `SCATTER`. It **regenerates** slowly while the squad is intact and in formation.
- At **low cohesion the squad degrades toward ten soloists** — members revert to individual targeting and self-preservation, orders execute sluggishly. This is a *legible failure state*, not a hidden penalty: a broken squad visibly falls apart, teaching the player that keeping the squad whole (and its members alive — Pillar 2) is itself a tactical resource.

Cohesion is the tactical mirror of the emotional thesis: **the reward for keeping your people alive and together is that they fight as one; the cost of losing them is that the survivors fight alone.**

### 6.8 The Squad Leader (emergent, not assigned)

One member of a squad is its **leader** — and, consistent with §11.7, the player never assigns this; it emerges. The leader is the squad's highest-Competence living member (ties broken by Notable score, §8.2). The leader:

- Is the **anchor point** for formation offsets (the squad forms up around them).
- Grants a **cohesion regen bonus** while alive.
- Makes a leader's fall a genuine tactical blow, not just an emotional one: when the leader enters Agony, cohesion drops sharply and a new leader must emerge, so the *rescue* of a leader (§7) is now both an act of love **and** a tactical necessity. This deliberately couples the two pillars — the person you're most attached to is also the one the squad most needs, so the stakes stack.

### 6.9 Squad AI — Tick Architecture

The squad layer adds **one** scheduler above the existing per-unit ones. It is cheap because it runs per *squad* (a handful), not per *unit*.

```
SERVER
 ├─ NavigationScheduler   → 0.2s: advances each unit along its route spline; handles junction crossings
 ├─ CombatScheduler       → event-driven per-unit cooldowns (unchanged from single-soldier model)
 ├─ BehaviorScheduler     → 0.5s: per-unit Layer-3 survival behavior (cover, retreat)
 ├─ SquadScheduler        → 0.5s: per-SQUAD — reads the order, assigns formation slots,
 │                          evaluates flank opportunities, sets focus, updates cohesion
 └─ ScoringScheduler      → 1.0s: Notable score + post-battle accumulators (spec §11.7, reputation §9.3)
```

A worked sketch of the squad tick — this is the non-obvious part, so it's shown in real Luau rather than described:

```lua
-- Runs every 0.5s per squad. Assumes EntityStore access by ID (§13.5), no retained refs.
function SquadScheduler.tick(squadId)
    local squad = EntityStore.getSquad(squadId)
    if not squad then return end  -- squad wiped; MatchService will GC it

    local members = {}
    for _, id in ipairs(squad.memberIds) do
        local s = EntityStore.getUnit(id)
        if s and s.status == "ACTIVE" then members[#members+1] = s end
    end

    -- 1. Leadership: highest competence living member (§6.8)
    local leader = nil
    for _, s in ipairs(members) do
        if not leader or s.competence > leader.competence then leader = s end
    end
    squad.leaderId = leader and leader.id or nil

    -- 2. Cohesion update (§6.7). Three inputs, matching the text: how many members
    --    survive, how many hold formation, and whether a leader is alive (§6.8).
    local intact     = #members / math.max(1, #squad.memberIds)
    local inForm     = countInFormation(members, squad) / math.max(1, #members)
    local hasLeader  = squad.leaderId and 1 or 0   -- leaderless squads decay sharply (§6.8)
    local target     = 0.4 * intact + 0.4 * inForm + 0.2 * hasLeader
    squad.cohesion   = squad.cohesion + (target - squad.cohesion) * 0.25  -- smooth toward target

    -- 3. Execute the current order (§6.4) — assigns each member a slot/route/target intent
    OrderExecutors[squad.order.kind](squad, members, leader)

    -- 4. Flank opportunity scan (cheap: routes are integers, §6.5)
    for _, s in ipairs(members) do
        local tgt = s.targetId and EntityStore.getUnit(s.targetId)
        if tgt then
            s.isFlanking = isFlanking(s, tgt, members)  -- cached for CombatResolver
        end
    end
end
```

The point of the code above is not the exact arithmetic — those constants are placeholders. It is the **shape**: the squad layer is O(squads × members), reads everything by ID with no retained references (§13.5), and produces cached flags (`isFlanking`, formation slots, focus) that the cheaper per-unit schedulers consume without recomputing. This is what keeps coordinated squads inside the anti-lag budget (§13.4).

---

## 7. The Rescue System — Logistical Airdrop

The mechanical heart of the "logistics as love" half of Pillar 2, **mandatory in the MVP** (§2). It routes all tension through **threat manipulation (aggro)** rather than sacrificing friendly units, and it works on the multi-route battlefield with one addition: the rescue is now spatially harder, because a soldier can fall on a flanking route deep in contested ground.

### 7.1 Agony State

- When a tracked soldier reaches 0 HP, instead of dying it enters **Agony** for 60 s (tunable).
- During Agony the soldier is downed, vulnerable, and stranded at wherever it fell — which route, and how far along, now matters (a soldier downed mid-flank on the far route is a much harder rescue than one downed on the center front).
- A visible countdown and a global alert (P0, §8.4) fire.

### 7.2 Logistical Airdrop

Rather than sending recruits to die as bait — which would cannibalize the thesis, since recruits are also named individuals — the player spends Supply to **airdrop a destructible barricade** onto the downed soldier's location.

- The barricade has its own HP and a high threat weight (§5.3, weight = 100), pulling the enemy horde's aggro at medium/long range, drawing fire off the rescue and clumping the enemy.
- The barricade is the shield; no friendly soldier is spent as bait. The rescue stays a *pure logistics* act.

### 7.3 Absolute Risk — no safety nets

Once committed:
- If the barricade falls early, the **Medical Cart becomes the highest-value target** the horde turns on.
- If the cart is intercepted, the player loses **both** the Supply **and** the veteran, instantly.

The gamble is what produces attachment.

### 7.4 The Vulnerability Window (dramatic climax)

The rescue completes only when the Medical Cart holds a **static 4.5-second loading channel** beside the downed soldier. The tension is **two bars racing**: barricade HP melting vs. load timer advancing. The player watches, able only to have supplied well or poorly.

- The cart rides route splines (§6.1) — including **crossing junctions** to reach a soldier on another route, which is what makes far-route rescues take longer and cost more of the Agony clock. It never uses free physics or `TweenService`.

### 7.5 The Rescue and the Squad

A rescue now has a squad dimension. While a soldier is in Agony:
- Nearby squad members can be ordered to **HOLD around the barricade** (§6.4) — the Anchor role (§11.7) does this automatically. This is not sacrifice-as-bait; it is protecting the operation, and it earns `RescueAssist` credit (§8.2).
- Pulling members back to protect a rescue **weakens the front line** they leave — the rescue's real cost is not only Supply, it's the tactical pressure you divert. This is the tactical layer and the emotional layer fused: saving the person you love costs you ground.

### 7.6 MVP Simplification

One resource type fuels it; one button launches airdrop + cart. Multiple cart types and upgrades are deferred (§16).

### 7.7 The Supply Meter (the MVP's single resource)

- A single meter, **0–100 Supply**, regenerating at **2 Supply/s**, full at match start.
- **One rescue costs 80 Supply.** Nothing else consumes Supply in the MVP — generics respawn free (§4.3) — so the meter exists to price the one costly logistical decision.
- After a rescue (20 left), the player needs **30 s of regen** to afford another. With Agony at 60 s and a cart needing ~17 s (longer across a junction), two roster soldiers falling close together forces a genuine triage: *which one, and does the second even have time?*
- Server-authoritative (`EconomyService`, §13). Post-MVP, Supply becomes the bridge into the full economy (§16).

### 7.8 The Rescue Math Chain (why these numbers — with the honest caveat)

A typical center-route rescue: player reaction + cart travel (~12.5 s center, more across a junction) + loading channel (4.5 s) ≈ 25–35 s of the 60 s window. The barricade at 400 HP under ~4 attacking recruits (~27 DPS) holds ~15 s — slightly less than the cart's exposure, which is the two-bars-racing tension.

> This chain is a **design target, not a derivation**. It assumes a reaction time, a clean route, and a fixed number of attackers the barricade pulls — all of which the live multi-route battle will violate. It is written to give tuning a starting point and to keep the numbers *internally consistent*, so that changing barricade HP or cart speed moves success rate predictably. Where it lands is an M3 measurement (§4.4).

---

## 8. Presence, Direction & Visualization

The player is neither passive spectator nor faceless camera. The interface is engineered to make the player **pick favorites** and **own choices**.

### 8.1 Commander Avatar

- A physical character the player controls in the barracks and at the front. Presence without combat: it cannot fight; its verbs are logistical and moral (inspect, dispatch, supply, and — at Moral Junctions — decide).

### 8.2 Notable Soldiers Panel

Real-time top-3 most-distinguished soldiers, scored so a defensive tank or a support hero can rise, not only a killer:

```
Score = (Kills × 10)
      + (RescueAssists × 8)      ← support/tank heroes emerge
      + (FrontlineTime × 0.5)    ← rewards holding the line
      + (FlankKills × 6)         ← rewards executing the coordination layer (§6.5)
      + CompetenceTier
      + (TimeAlive × 0.2)
```

- `RescueAssists` = fighting within a fixed radius of an active rescue (§7.5). Constants are placeholders; intent is **archetype diversity**, not one optimal build.
- Recomputed by `ScoringScheduler` at 1 Hz over living units only.

### 8.3 Dynamic Camera ("Follow" button)

- Tapping a soldier snaps the camera to an over-the-shoulder view behind that NPC. One click, instant. Primary attachment interaction.
- A focused unit is promoted to the 20 Hz replication tier (§13.3) for smooth movement/HP.

### 8.4 Cinematic Global Alerts

The game *actively* surfaces drama via a priority-queued, cooldown-gated alert system. A constantly-firing alert trains the player to ignore it, which kills the North-Star moment.

| Priority | Events | Queue behavior |
|---|---|---|
| **P0** | Roster soldier enters Agony; rescue resolved; **Moral Junction reached (§9.4)**; reputation tier change | Always immediate; preempts the queue |
| **P1** | Crystallization ("became a Bastion"); promotion to Veteran/Elite; leader fell (§6.8) | Shown next; never dropped |
| **P2** | Champion equipped; enemy Champion sighted; **flank landed by a roster soldier (§6.5)**; near-miss feedback (§7) | Shown if no P0/P1 pending |
| **P3** | Minor color (first kill, first cover use, first flank) | Shown only when the queue is idle |

- **Cooldown:** ~8 s between non-P0 alerts. P0 ignores the cooldown — a roster soldier's life, and a moral choice, are never delayed.

### 8.5 Post-Match Battle Report

- **Per roster soldier:** stats (kills, damage taken, frontline time, rescue assists, flank kills), competence gained, a **tendency hint** foreshadowing crystallization (§11.7), and any **reputation contribution** the soldier's conduct made this match (§9.3).
- **Rescue recap:** outcome of any rescue, including near-miss % (§7).
- **Moral recap:** the session's Junction (§9.4), the choice made, and the reputation delta — the choice is *re-told*, so the player leaves the match having narrated their own decision.
- **Recruit Candidates:** generics who earned a name (§12.3), for sign-or-dismiss.

### 8.6 HUD Layout (MVP)

| Region | Element |
|---|---|
| Bottom-right | Tactical radar (§13.3) — tap unit to Follow; tap route/junction to order; tap downed icon to rescue |
| Right edge | Notable Soldiers panel (§8.2) |
| Top-left | Supply meter (§7.7) + reputation meter (§9.5) |
| Top-center | Alert toasts (§8.4), one at a time |
| Contextual | **Rescue button** (roster soldier in Agony); **Order palette** (when a squad is selected); **Junction dialog** (full-screen, when a Moral Junction fires — §9.4) |

Design rule: keep the **center clean** — the soldiers are the show; the interface is the stage lighting. The one exception is the Moral Junction, which *takes* the center deliberately (§9.4), because a moral choice should stop the show.

---

## 9. Reputation & Morality

This is the system that renames the game. The player is not building heroes by default — they are building a *reputation*, and reputation can bend either way. A commander who keeps a squad alive is not automatically good; keeping them alive is what earns the *reach* to make the choices that reveal who the commander is. This section defines how those choices are surfaced, weighted, and made permanent.

### 9.1 The Two Axes of Reputation

Reputation is not a single good–evil slider — a slider invites min-maxing and flattens the fiction. It is **two independent axes**, each `−100..+100`, tracked per universe (§14):

| Axis | −100 pole | +100 pole | Driven by |
|---|---|---|---|
| **Mercy ↔ Ruthlessness** | Ruthless (executes, sacrifices, no quarter) | Merciful (spares, protects, accepts cost to save life) | Junction choices about *lives* (§9.4) + emergent conduct (§9.3) |
| **Honor ↔ Cunning** | Cunning (deceives, ambushes, breaks terms) | Honorable (fights fair, keeps terms, open force) | Junction choices about *methods* + how the player wins fights (flanks/ambushes lean Cunning) |

A commander is a **point in this 2D space**, and the four quadrants read as recognizable archetypes (placeholder names — final naming in the narrative doc):

- Merciful + Honorable → the **Paladin** (the classic hero)
- Merciful + Cunning → the **Trickster-Protector** (saves lives by any means)
- Ruthless + Honorable → the **Iron General** (brutal but fair, no deceit)
- Ruthless + Cunning → the **Warlord** (the classic villain)

This is better than a single axis because it lets the player be a *specific* kind of hero or villain, and because the two axes can conflict inside one choice (sparing an enemy is Merciful but, if you'd promised your squad blood, may cost you honor with them). Conflict is where the interesting decisions live.

> **Why two axes and not more, or a full tree.** More axes dilute legibility (Pillar 4) — the player must be able to say "I'm becoming a Warlord" as clearly as they say a soldier's name (the North-Star, §1.1). The Post-MVP reputation tree (§9.7) adds depth *within* these two axes; it does not add new axes. Two is the most the player can hold in their head while also tracking a squad of individuals.

### 9.2 What Reputation Changes (mechanics, not just flavor)

Reputation must *do* something or it is decoration. Each pole unlocks and locks real mechanics — and crucially, **the axes gate each other's toys**, so no single build is strictly best:

| Reputation lean | Unlocks | Locks / costs |
|---|---|---|
| **Ruthless** | Can execute prisoners for a Supply refund (§9.4); generics respawn faster (fear drives them); higher base damage (soldiers fight harder for a feared commander) | Merciful-only rescues (see below) unavailable; some Recruit Candidates refuse to sign |
| **Merciful** | Spared enemies can become **defectors** — recruitable Candidates (§12.3); a once-per-match **free** rescue (allies rally to a beloved commander); wounded recover faster | No execution refund; slightly slower generic respawn |
| **Honorable** | Enemy honorable commanders offer **truces** (a tactical breather); Champion equipment more effective (a fair fighter's weapon) | Cannot ambush from fog (Post-MVP §19); no deceptive orders |
| **Cunning** | **Ambush** orders (Post-MVP): units in fog deal bonus first-strike damage; can feign retreat to bait | Enemies distrust truces; higher risk of desertion at low cohesion |

The design rule: **every reputation identity is viable, none is optimal.** A Warlord wins through fear and ambush; a Paladin wins through loyalty and fair strength. If telemetry (§4.4) shows one quadrant dominating win rate, the asymmetry is mis-tuned, not the player being smart.

### 9.3 Emergent Reputation (the squad's conduct)

Half of reputation comes from what the player's soldiers *do* in combat, read the same way specialization is (§11.7) — the player does not choose it, the simulation reads it. This is the "day-to-day in combat also weighs" half of the answer.

After each battle, the `ScoringScheduler` reads conduct signals already tracked and nudges the axes by a **small** amount (emergent conduct is a slow drift; junctions §9.4 are the fast, decisive moves):

```
Ruthlessness += w1 × (killsOnFleeingEnemies + killsOnDownedEnemies)
Mercy        += w2 × (enemiesLeftAliveWhenAbleToKill)   -- e.g. broke off a rout
Cunning      += w3 × (flankKills + ambushKills)          -- winning by angle, not force
Honor        += w4 × (frontalKills + heldGroundWithoutFlanking)
```

- Weights `w1..w4` are **deliberately small** so a player cannot grind their way across the map — reputation drifts from *how you habitually fight*, but it *turns* on the junctions.
- This closes a consistency loop: the same coordination system that produces flank kills (§6.5) also, quietly, pushes you toward Cunning. Winning by pincer *is* a cunning way to fight, and the game notices. A player who always fights frontally drifts Honorable without ever being asked. Identity emerges from habit, then junctions force it to crystallize — exactly the philosophy already governing soldier roles.

### 9.4 Moral Junctions (the decisive choices)

A **Moral Junction** is an authored decision point that fires from an emergent battlefield state. It is the fast, heavy input to reputation — one junction moves the axes far more than a whole match of emergent drift (§9.3). **The MVP guarantees at least one per session** (§2, H3).

A junction is triggered by a *condition*, so it feels earned rather than scripted:

| Trigger condition | The junction | The choice (and its axis pressure) |
|---|---|---|
| Enemy squad routed and surrendering | **The Surrender** | Spare (Mercy+, Honor+) / Execute for Supply refund (Ruthless+, and if you'd have won anyway, Honor−) |
| A roster soldier in Agony *and* a push that could win the round *now* | **The Sacrifice** | Divert to rescue (Mercy+, but lose the push) / Push and abandon them (Ruthless+, Honor− if the soldier was loyal) |
| Enemy civilians/supply depot in a route you could take | **The Plunder** | Protect it (Mercy+, Honor+, no reward) / Seize it for Supply (Ruthless+, Cunning+) |
| Chance to strike an enemy commander from fog (Post-MVP §19) | **The Ambush** | Announce and fight fair (Honor+) / Strike from hiding (Cunning+, big tactical edge) |

Mechanically a junction:
1. Fires a **P0 alert** (§8.4) and **pauses the tactical pressure locally** — not a full game pause (the rest of the battle continues), but the junction's actors freeze so the choice has weight without being punished by the clock. `[PLACEHOLDER — decide whether the whole match soft-pauses or only the local actors; M3 playtest question]`.
2. Presents a **full-screen dialog** (§8.6) — the one time the HUD is allowed to take the center — showing the choice, the axis consequences (shown honestly; the player sees "this will push you Ruthless"), and who is affected (named soldiers if relevant).
3. Applies the reputation delta, any mechanical reward (Supply refund, a defector), and fires a follow-up beat in the Battle Report (§8.5).

The junction is **binding** — no undo. Ownership of the choice (H3) requires that it cost something and cannot be taken back.

### 9.5 The Reputation Meter (HUD)

- A compact 2D indicator (top-left, §8.6): a dot in the Mercy↔Ruthless / Honor↔Cunning plane, with the current quadrant archetype named beneath it.
- It **animates on change** — a junction visibly shoves the dot toward a corner, and crossing a tier boundary (§9.6) fires a P0 alert. The player must *see* their identity move.

### 9.6 Making Reputation Permanent — Tiers & the Two Walls

Reputation, like everything in this game, is made to *stick* through authored beats.

- **Reputation tiers.** Each axis has named tiers at thresholds (e.g. Mercy at +40 = "Protector", +80 = "Saint"; Ruthlessness at −80 = "Butcher"). Crossing a tier is a **crystallization beat** (§11.7's philosophy applied to the commander): a cinematic alert, *"You are becoming a Warlord."* Identity is celebrated, not silently accumulated.
- **The Fallen Heroes Wall** honors roster soldiers lost permanently — in Post-MVP PvP, and in the MVP through a Moral Junction that cost them their life (§14.2): a memorial granting small **non-inflationary** logistical bonuses. Loss is honored without inflating power.
- **The Wall of the Fallen-Upon** (new, the villain's mirror) records those the commander *chose* to let die or executed — the prisoners you shot, the loyal soldier you abandoned to win. It grants **Ruthless-aligned** bonuses (faster respawn, the execution refund improving). A Warlord builds power from a body count; a Paladin builds it from sacrifice. The two walls are the same mechanic — permanent memory that pays out — pointed at opposite moralities, so *both* playstyles have a growing monument to what they've done.

### 9.7 Post-MVP: The Reputation Tree

Gated behind M3 (§15). Within the two axes (§9.1), a tree of unlocks deepens each identity: a Warlord branch (terror tactics, forced conscription of defeated enemies), a Paladin branch (rally auras, enemy defection on sight of your banner), etc. The tree adds *depth within* an identity; it never adds a third axis and never lets a player buy their way into a reputation they didn't earn through choices (§9.4) and conduct (§9.3). `[PLACEHOLDER — the tree's contents are Post-MVP and should be designed only after M3 confirms the two-axis model reads clearly.]`

### 9.8 Known Tension (watch in playtest)

Reputation-locked mechanics (§9.2) plus PvP permadeath (§14) mean a committed Warlord and a committed Paladin play measurably differently — which is the goal, but it is also a balancing knife-edge and a potential new-player trap (a player who drifts into a reputation by accident may feel locked out of tools they wanted). Telemetry (§4.4) must watch quadrant win-rate spread and whether players *feel* their reputation was chosen or imposed. If "imposed," the emergent drift (§9.3) is weighted too high relative to junctions (§9.4).

---

## 10. The Four-Layer Soldier AI

Each soldier runs a four-layer AI, server-authoritative, staggered across schedulers (§6.9) so no layer runs every frame for every unit. The squad layer (§6) sits above these and feeds them intent (formation slot, focus target, flank flag); the four layers below are what an individual does *within* that intent.

### 10.1 Layer 1 — Navigation
- Movement along the current route spline toward its formation slot or the enemy base. Junction crossings (§6.1) are handled here as a spline-to-spline handoff at the node — no A*, no `PathfindingService` in the hot path.

### 10.2 Layer 2 — Target Acquisition & Combat
- Acquire highest-priority enemy by §5.3 (as modified by squad focus §6.6) → target lock → engage until death or out-of-range → drive the two-phase attack loop (§5.2).
- Aggro updates are **dirty-flagged**, not recomputed every frame (§10.5).

### 10.3 Layer 3 — Survival & Behavior
Behavior diverges by tier — where individuality emerges:

| Behavior | Recruit | Elite |
|---|---|---|
| Retreat threshold | Retreats at 20% HP | Fights to 5% HP |
| Targeting | Highest-priority by §5.3 | Also hunts dangerous enemy units (Champions) |
| Cover | Never uses cover | Uses cover; may emit an aura buffing nearby recruits |
| Squad discipline | Breaks formation easily under fire (low personal cohesion contribution) | Holds slot, stabilizes cohesion (§6.7) |

### 10.4 Layer 4 — Equipment
- Before marching, each soldier checks the arsenal. The one who equips the single **legendary weapon** becomes the **Champion**: larger scale, glowing nameplate, significant stat bonus. Scarcity forces a logistics decision — *who deserves it* — and the Champion is a natural FOCUS target (§6.6) for the enemy, so equipping it also paints a target. (There is exactly **one** legendary in the MVP; a Post-MVP tech-tree unlock can add a second slot, §11.9 — but even then legendaries stay scarce and are never craftable, §16.3.)

### 10.5 Tick Architecture & CPU-Spike Mitigation
- **Never run all layers every frame for every unit.** Stagger on independent intervals (§6.9); combat is event-driven off cooldowns.
- **Dirty-flag aggro (generalized).** Aggro-changing events (airdrop landing, Champion entering, cart appearing, a FOCUS order) set `RequiresTargetUpdate = true` on units in radius; the `CombatScheduler` reads and clears these **spread across ticks** (time-slicing), diluting CPU load. Standard mechanism for *all* aggro changes.
- **Time-slicing:** split the unit list across N frames; only `units/N` processed per frame.

---

## 11. Veterancy, Specialization & Progression

The governing rule: **power emerges from survival; the player authors identity, logistics, and morality, never a soldier's raw combat power.** A soldier is loved for who he *became*, not who the player *built*.

### 11.1 Competence Progression (Veterancy)

Delivers "*this soldier survived 40 battles and you can see he's smarter than a recruit*" without machine learning. The system does not simulate learning; it **stages its result** — the player cannot distinguish "learned to take cover" from "unlocked cover at Tier 3," but the staged version is cheap, deterministic, and tunable.

### 11.2 The Core Driver — Survival
Competence accrues from **battles survived**. Because soldiers gain competence by staying alive, and the player's job is to keep them alive, **progression and the core fantasy are the same act.** Every rescue (§7) protects accumulated competence.

### 11.3 The Curve — Logarithmic, ~40 battles to Elite

```
Competence = floor( K × ln(1 + BattlesSurvived) )
```

Fast visible early gains hook the player; a long plateau makes Elite rare and precious. `K` and thresholds tuned so Elite costs ~40 battles, not 10. Survival is the only input.

### 11.4 Tier Table — Unlocked Behaviors

| Tier | Battles (approx.) | Unlocked behavior |
|---|---|---|
| **Recruit** | 0–5 | Marches straight; strikes nearest mass; no cover; retreats at 20%; breaks formation easily |
| **Seasoned** | ~6–15 | Uses cover; smarter retreat; slight precision modifier; holds formation better |
| **Veteran** | ~16–35 | Precise strikes (damage/precision multiplier); prioritizes dangerous enemies; can lead a squad (§6.8) |
| **Elite** | ~36+ | Aura buffing recruits; fights to 5%; reads aggro/barricade state; strong formation anchor |

### 11.5 Visible Behavior vs. Invisible Stat
The "where to strike" fantasy is two layers read as one skill: **visible behaviors** (cover, prioritization, fighting to 5%) the player watches, and an **invisible precision modifier** surfaced only through authored narration ("Precise strike!"). Pairing the hidden modifier with visible behavior makes higher numbers read as *competence*, not inflation.

### 11.6 Emergent Specialization (roles are revealed, not chosen)

A soldier's role **emerges from how he survived**, read from stats the simulation already tracks. Three lifetime accumulators update post-battle:

```
B += 0.6 × DamageTakenNorm  + 0.4 × FrontlineTimeNorm    (Bastion / tank)
R += 0.7 × KillsNorm        + 0.3 × FlankKillsNorm        (Reaper / DPS)
A += 0.6 × RescueAssistNorm + 0.4 × AllyProximityNorm     (Anchor / support)
```

- Computed once post-battle by `ScoringScheduler` — zero hot-loop cost. (Note the Reaper now weights **flank kills**, coupling specialization to the coordination layer §6.5.)
- At crystallization, `role = argmax(B, R, A)`; ties resolve toward the tendency whose single best battle contributed most.

### 11.7 Crystallization & Role Kits

Specialization stays fluid at Recruit/Seasoned, then **crystallizes permanently at Veteran** — the game reads the dominant lifetime tendency and fires a cinematic beat (*"Arthur has become a Bastion"*). The North-Star needs the player to name a soldier's role with the certainty of his name; a blurred identity weakens the read. Anti-manipulation: the read uses the entire history, so a player can't force a role in the last two battles.

Each role unlocks a small, legible kit — **sidegrades around one power budget**, not power jumps:

| Role | Behavior unlocks | Modifier | Squad interaction |
|---|---|---|---|
| **Bastion** | Anchors cover near allies; shields downed allies | +20% max HP; raised ThreatWeight (draws fire) | Assigned front/point formation slots (§6.3); stabilizes cohesion |
| **Reaper** | Re-targets fast after a kill; hunts Champions & low-HP; **seeks flank angles** (§6.5) | Attack interval floor 1.0 s | Assigned formation flanks; the squad's designated flanker on a FLANK order |
| **Anchor** | Escorts active Medical Cart; gravitates to clustered allies | Aura: −10% damage taken within 15 studs | Boosts cohesion regen; the natural rescue-protector (§7.5) |

Each role's kit now *plugs into the squad layer*, not just individual combat — a Reaper is who you send to flank, a Bastion is your formation point, an Anchor holds your rescues. Specialization and coordination reinforce each other.

### 11.8 Customization — cosmetic only, scaling with tier
Purely cosmetic/identity; never functional. Rename + basic color from Recruit (naming is the first act of attachment, available early so the 30-min North-Star lands). More options unlock with tier, so a heavily-customized soldier is by definition a long-survivor — a visible badge of veterancy. Crystallized role fits the cosmetic line (heavier armor for a Bastion). The player dresses the soldier as the role he *became*, never choosing the role through the wardrobe.

### 11.9 Army Tech Tree (logistics, not individuals — Post-MVP)
Commander progression unlocks army/logistics upgrades (faster carts, higher-HP barricades, reduced dispatch time, a second legendary slot), **never** per-soldier stat choices. Individual power comes only from emergent Competence and specialization. This is also where reputation-gated logistics live (§9.2). `[PLACEHOLDER — full tree Post-MVP.]`

### 11.10 Cover Points (route furniture)
Discrete defensive positions along route edges (~every 40 studs, alternating sides, capacity 1). A soldier in cover takes −30% damage from attackers beyond ~10 studs and lowers his own ThreatWeight. Point-blank ignores cover — it helps you *hold*, not hide. Seasoned+ soldiers move to cover when their target is out of range or HP < 50%. One extra Layer-3 branch, no pathfinding (cover nodes sit on route splines). Stepping into cover is a *visible* veterancy behavior — the player reads experience at a glance.

---

## 12. Persistent Progression & the Barracks Limit

### 12.1 Unique Identity
Every generated soldier gets a random name and unique visual traits (scars, faces). Per-soldier stats persist between sessions in a per-universe table (§14).

### 12.2 The Rule of Few
The barracks has a **hard slot limit (5 initial)**. Scarcity is the point: few slots force the player to remember each face and make hard discard decisions when a prodigy appears (§12.3). Surface a soldier's stats at the moment of discard so the cost is felt.

### 12.3 Line Troops, Earning a Name & Defectors
- **Generic line troops** fill the field beyond the named roster — unnamed, simplified, non-persistent, free-respawning (§4.3). No Agony; they simply die. Their *conduct* still feeds emergent reputation (§9.3) — how your anonymous troops fight is part of your reputation even before they have names.
- **Earning a name:** a generic who finishes a match alive with notable performance (placeholder: ≥3 kills *or* ≥60 s frontline *or* a flank kill) becomes a **Recruit Candidate** in the Battle Report. Only then is a name/face generated. The player may **sign** them (forcing a discard if full) or dismiss.
- **Defectors (reputation-gated).** A Merciful commander (§9.2) can turn *spared* enemies into Recruit Candidates — mercy literally grows your roster. A Ruthless commander cannot, but gets other tools (§9.2). Where your next hero comes from depends on who you are.
- **Pillar reconciliation.** Identity is **earned, not issued**: the crowd exists so individuals can emerge from it. The moment a generic earns a name — or a spared enemy defects — is an authored beat (Pillar 4).

### 12.4 The Wounded State
A soldier returns **Wounded** after a successful rescue or any PvE fall. MVP rule: unavailable for the **next 1 match**, then auto-returns to Active. Wounded soldiers stay **visible in the barracks** (bandaged) — recovery is shown, because seeing Arthur bandaged after the rescue you pulled off is a free attachment beat. With 5 slots and a soldier out, the player feels the cost of every close call.

### 12.5 Persisted Soldier Record (schema)

```lua
SoldierRecord = {
  id = string,                -- stable unique ID
  name = string,
  visualSeed = number,        -- deterministic face/scars
  battlesSurvived = number,
  competence = number,        -- cache; derived from battlesSurvived (§11.3)
  tier = string,              -- RECRUIT | SEASONED | VETERAN | ELITE
  spec = { B = n, R = n, A = n },   -- tendency accumulators (§11.6)
  role = string?,             -- nil until crystallization (§11.7)
  stats = { kills, flankKills, rescueAssists, frontlineTime, timeAlive },
  conduct = { fleeingKills, downedKills, sparedEnemies },  -- feeds emergent reputation (§9.3)
  cosmetics = { ... },
  status = string,            -- ACTIVE | WOUNDED | FALLEN
  woundedMatchesRemaining = number?,
  fallen = { cause, date, finalScore, wall }?  -- wall = "HEROES" | "FALLEN_UPON" (§9.6)
}
```

- `competence` is derivable from `battlesSurvived` (cache only); the source of truth is the battle count, so tuning `K` re-grades everyone consistently.
- `conduct` is new — it is what §9.3 reads to drift the reputation axes.

---

## 13. Technical Architecture (Roblox / Luau)

### 13.1 Authority Model
- **Server-authoritative for everything that matters:** AI, combat, squad coordination, economy, reputation, persistence, rescue outcomes, Moral Junction resolution.
- Client handles only **presentation**: camera, UI, alerts, VFX, radar, the junction dialog. Never trusted with state — a client must never be able to report "I chose Spare" and have the server believe the reputation delta without re-deriving it.
- Communication via `RemoteEvent`/`RemoteFunction` with server-side validation on every action.

### 13.2 Suggested Module Layout

```
ServerScriptService/
 ├─ MatchService        (multi-route tug-of-war §4.3; SOLE owner of EntityStore §13.5)
 ├─ AIController        (orchestrates the schedulers §6.9)
 ├─ SquadService        (squad objects, orders, formations, flank & cohesion §6)
 ├─ CombatResolver      (two-phase range+cooldown damage, flank bonus §5.2/§5.4)
 ├─ ScoringService      (Notable §8.2; specialization §11.6; emergent reputation §9.3)
 ├─ RescueService       (Agony FSM, airdrop + cart §7 / §21.2)
 ├─ CommsService         (comms graph, hierarchy tiers, messengers — Post-MVP §20)
 ├─ MoralityService     (junction triggers, choice resolution, reputation axes §9)
 ├─ EconomyService      (server-authoritative Supply §7.7)
 ├─ ReplicationService  (two-rate pipeline §13.3)
 ├─ TelemetryService    (§4.4 hooks)
 └─ PersistenceService  (per-universe profiles, session-locked §14 / §12.5)

ReplicatedStorage/
 ├─ SharedData          (schemas, read-only to client)
 └─ Remotes             (validated RemoteEvents/Functions)

StarterPlayerScripts/
 ├─ CameraController    (Follow / dynamic camera §8.3)
 ├─ AlertController     (curated alerts, priority queue §8.4)
 ├─ RadarController     (tactical radar + order issuing §13.3 / §6.4)
 ├─ OrderController     (order palette, junction dialog §6.4 / §9.4)
 ├─ ReportController    (post-match report §8.5)
 └─ HUDController       (Notable panel, Supply + reputation meters §8.6)
```

### 13.3 Two-Rate Replication / Interest Management

| Data type | Frequency | Scope | Client use |
|---|---|---|---|
| **Tactical matrix** (ID, Team, ClassID, RouteID, S-position) | 1 Hz | Per player; own units always, enemy units per revealed vision (Post-MVP §19) | Radar icons; order targeting |
| **Focused entities / active operations** | 20 Hz | Clients with a locked camera, an active rescue, or an open Moral Junction | Smooth load bars, HP, cart, junction actors |

- **Active rescues and active Moral Junctions are always 20 Hz** regardless of camera, so the climax and the choice never stutter.
- Payload is a flat numeric array (`[ID, Team, ClassID, RouteID, S, ...]`), not a keyed table. Positions quantized to 0.1 stud. Note the position is now `(RouteID, S)` — two numbers — not a full 2D `(X,Z)`; the route-graph topology (§6.1) is what keeps replication this cheap even with spatial coordination.
- **Radar projection.** Each route maps to a lane on the mini-map; `S` maps to position along the lane; junctions are drawn as rungs. World→UI is a fixed transform per route, a constant in the MVP, generator-emitted Post-MVP (§18).

#### 13.3.1 Tier-Transition Smoothing (anti-"bungee")
A naive 1 Hz → 20 Hz promotion rubber-bands. Mitigation: **client-side interpolation, never extrapolation** — the radar icon lerps between the two most recent received positions over the 1 s window, lagging one cycle but never overshooting. An `IsHighFrequency` flag on each cached entry excludes promoted units from the 1 Hz loop and the cleanup sweep, so a focused unit missing from the global matrix isn't deleted. Written on promotion, cleared on demotion, never implicit.

#### 13.3.2 Focus/Rescue High-Frequency Channel
Focus (Follow) or rescue promotes a unit/region to 20 Hz via a **dedicated channel directed only at the operating player — it does NOT move `Player.ReplicationFocus`.** `ReplicationFocus` controls 3D instance streaming around the avatar; repointing it to a distant rescue could stream out the ground under the commander. Two separate truths: where the player *is* (streaming, anchored to avatar) vs. what the player is *watching* (the 20 Hz data channel).

### 13.4 Performance Budget (anti-lag)
- Combat is event-driven off cooldowns, never per-frame.
- Schedulers staggered on independent intervals (§6.9); aggro uses dirty-flag + time-slice.
- The squad layer is per-squad (a handful), not per-unit — coordination adds O(squads) cost, not O(units²).
- Object-pool soldiers, cart, VFX, alert UI. Cart moves as a spline vector, not physics.

### 13.5 `EntityStore` — Ownership & Memory Lifecycle
All live entities (units **and squads**) live in a **pure Luau dictionary**, read by ID. `CollectionService`/`Attributes` banned from the hot loop (GC pressure). Rules:
- **Single owner.** `MatchService` is the only module permitted to write or delete keys (units and squads alike).
- **Access by ID, no long-term retention.** Schedulers and services read by ID every operation; a local ref is allowed only within one tick, never across ticks.
- **Death cleanup.** On death, `MatchService` removes the key; next cycle, other schedulers read `nil`, clear their target/search state, release to GC. When a squad's `memberIds` all die, `MatchService` GCs the squad object too.

### 13.6 Scalability Path
The MVP runs ~20 units + 2 squads trivially. Scaling to larger battles later needs only tuning scheduler intervals and time-slice widths — not a rewrite. Server-authority, dirty-flag aggro, per-squad coordination, and `EntityStore` discipline are decided *now* precisely so scale is a tuning exercise.

---

## 14. Data Architecture: PvE vs. PvP Separation

Total data separation between two universes eliminates illegitimate farming (alt-accounts feeding a main).

| System | Offline (PvE / Campaign) | Online (PvP Competitive) |
|---|---|---|
| Economy & Items | Saved in PvE inventory | Generated from scratch each match |
| Competence & Progression | PvE-only | PvP-only |
| **Reputation (§9)** | **Earned and saved in PvE** | **Earned from scratch in PvP** |
| Era Progression (§17) | PvE-only | From scratch in PvP profile |
| Soldier Death | **Temporary** — wounded, return | **Rescue or Permadeath** |

### 14.1 Implementation Notes
- Two independent persistent profiles per player (`profile_pve`, `profile_pvp`), never cross-reading. `DataStoreService` with **session-locking** (ProfileService pattern) prevents dupes and write races. All economy and reputation mutations server-authoritative. Because PvP resources regenerate each match, there's no persistent PvP currency to farm — structural anti-cheat, not a patch.

### 14.2 Soldier Death by Universe
- **PvE:** temporary by default; a low-stakes place to *form* attachment and *discover* your reputation lean.
- **PvP:** Agony → rescue-or-permadeath. Where attachment and reputation are *tested*. The two Walls (§9.6) make loss permanent and visible.

> **MVP reconciliation (important — the universe separation and the North-Star must not contradict).** The MVP ships in the **PvE universe** (PvP networking is Post-MVP), but the North-Star (§1.1) and hypothesis H3 (§2) require a *permanent* loss for the moral weight to be real — a soldier you merely "abandon" who then walks back from the barracks next match teaches the player their choice was free. So the MVP applies a **narrow permadeath rule inside PvE**: a roster soldier lost through a **Moral Junction** (§9.4) — abandoned in *The Sacrifice*, or a consequence of an execution/plunder choice — dies permanently and goes to a Wall (§9.6). All *other* PvE deaths (a soldier who simply reaches Agony and isn't rescued in an ordinary fight) stay temporary → Wounded (§12.4). The line is: **the simulation forgives you; your choices do not.** This keeps the low-stakes attachment-forming space intact while giving the moral layer teeth, and it does not weaken the universe separation, whose real job is anti-farming data isolation (§14.1), not the death rule. Post-MVP PvP then makes *all* loss permanent, raising the stakes uniformly. `[PLACEHOLDER — confirm in M3 that junction-permadeath lands as "earned" rather than "unfair"; if players read it as a gotcha, the junction dialog (§9.4) must telegraph the permanence more loudly before the choice is locked.]`


### 14.3 Balancing the Punishment (Design Risk — and how M3 actually measures it)

The hard 5-slot roster + PvP permadeath + absolute-risk rescue (§7.3) + reputation lock-in (§9.2) is a **real frustration and lock-out risk**: losing veterans and resources in one failed rescue, or feeling trapped in a reputation, can drive players out rather than deepen investment.

The old document listed mitigations that were mostly restatements of the risk (e.g. "keep the success rate in band" — but the success rate is the same variable causing the risk). The honest position:

- **The mitigations are hypotheses, and M3 tests them directly.** M3's exit criterion (§15) explicitly measures **post-loss churn** — the fraction of players who quit within N minutes of losing a roster soldier — as a first-class metric alongside rescue success rate. "Did the rescue succeed?" and "did the player keep playing after it failed?" are different questions; the frustration risk turns on the second, so the second is what's measured.
- **Fast recruiting reduces ruin-to-turnover** — but note the tension it creates with Pillar 1 (a too-easily-replaced hero was never a hero). M3 watches whether fast replacement *dilutes* attachment (measured by whether players still name-recall after a loss-and-replace cycle). If it does, replacement speed is wrong.
- **Reputation lock-out** is softened by making mercy and ruthlessness *both* rewarding (§9.2), so no reputation feels like a dead end — but §9.8 flags this as a knife-edge to watch.

This is the section the old document was weakest on, so it is deliberately the most explicit here: the risks are named, the mitigations are labeled as unproven, and the exit criteria are written to measure the actual failure mode, not a proxy for it.

---

## 15. Open Questions & Roadmap

### 15.1 Open Questions
To be answered *within* prototyping, not guessed now.

1. **Route count & junction placement:** Are three routes and two junctions the right amount of flanking opportunity for a 6–9 min round, or does it slow the push below target? (§4.2, §6.1)
2. **Flank bonus magnitude:** Does +35% (§5.5) make flanking feel decisive without making frontal fighting pointless?
3. **Junction pacing:** Does one guaranteed Moral Junction per session (§9.4) land at the right moment, or does it fire too early/late to feel earned?
4. **Emergent vs. chosen reputation weight:** Do the §9.3 drift weights make players feel their reputation was *chosen* (via junctions) rather than *imposed* (via drift)? (§9.8)
5. **Reputation viability spread:** Do all four quadrants (§9.1) reach comparable win rates, or does one dominate?
6. **Cohesion failure legibility:** When a squad breaks (§6.7), does the player *read* it as "my squad fell apart" or just feel vaguely weaker?
7. **Success-band & post-loss churn:** Where does attachment peak, and where is the churn cliff after a lost soldier? (§4.4, §14.3)
8. **Specialization distribution:** Do the §11.6 weights produce rough thirds, or does one role dominate?

### 15.2 Roadmap — Milestones with Exit Criteria
Hard exit criteria; do not advance without meeting them.

| Milestone | Build | Exit criterion |
|---|---|---|
| **M0 — Foundation** | `EntityStore` (units + squads), schedulers (§6.9), range/cooldown combat (§5), multi-route tug-of-war (§4.3), generics + Director (§4.3.1) | A full round runs 8 min within frame budget, no leaks under unit/squad churn (§13.5 verified) |
| **M1 — Squad & Command** | Squad objects, formations, high-level orders, flanking, cohesion (§6) | Player can flank and win a route *because* of the flank; flank bonus visibly resolves; squad break is legible |
| **M2 — Identity** | Names/visual seeds, persistence (§12.5), Notable panel (§8.2), Follow camera (§8.3), Battle Report (§8.5) | Playtesters recall a soldier's name unprompted after one session |
| **M3 — Rescue, Morality & Validation** | Agony, Supply (§7.7), airdrop+cart FSM (§21.2), Moral Junctions (§9.4), reputation axes + meter (§9.1/§9.5), telemetry (§4.4) | **The North-Star (§1.1):** 30-min sessions; players name their best soldier, feel the Agony stakes, **and articulate one moral choice they own**. Rescue success in band. **Post-loss churn below threshold** (§14.3) |
| **M4 — Veterancy & Roles** | Competence tiers (§11.4), cover (§11.10), crystallization + kits (§11.7), earning a name / defectors (§12.3), cosmetics (§11.8), the two Walls (§9.6) | Two distinct archetypes appear in the Notable panel; players describe a soldier *by role* and describe *themselves* by reputation quadrant, unprompted |
| **Post-MVP** | PvP + permadeath (§14), full economy (§16), tech tree (§11.9), reputation tree (§9.7), era system (§17), procedural maps (§18), fog of war & recon (§19), **command hierarchy, comms devices & messengers (§20)** | Gated on M3's emotional + moral validation; within Post-MVP, eras gate on the economy, cross-era PvP on same-era PvP, procedural maps + fog on the North-Star validating against the fixed full-information MVP map, **and the comms hierarchy (§20) gates on the era system since devices are era-specific unlocks** |

The ordering is deliberate and each phase tests one hypothesis: **squad tactics work (M1) before identity (M2), identity before the emotional + moral core (M3), and the core before any expansion.** M3 is the gate the whole project lives or dies on.

> **On writing the Post-MVP sections now.** §16–19 specify systems that don't ship until after M3 validates. They are written now for one reason: **to prove the core systems don't foreclose them** — that the squad/route/reputation architecture can *grow* into an economy, eras, and fog without a rewrite. They are design *insurance*, not a commitment to build. If M3 invalidates a core assumption, these sections change with it; nothing here should be read as a decision that survives a failed North-Star test.

---

## 16. Economy Systems (Post-MVP): Gathering, Rarity & Crafting

> **Scope gate.** Post-MVP, gated on M3. Until then, the Supply meter (§7.7) is the entire economy. Designed under the same constitution: **the economy serves keeping soldiers alive and fueling the choices that define you (§9), never power accumulation for its own sake.**

### 16.1 The Three Resources
Deliberately few; each maps to a verb of care:

| Resource | Source | Feeds | Verb |
|---|---|---|---|
| **Provisions** | Depot/farm nodes | Supply meter (regen + cap) | *Sustain* — rescues, reinforcement |
| **Timber** | Forest nodes | Crafting, repair, barricade upgrades | *Build* — the shield between them and death |
| **Iron** | Mine nodes | Weapons and armor (§16.4) | *Arm* — capability without buying raw stats |

### 16.2 Resource Nodes on the Route Graph
Nodes sit on **flank routes**, accessible only while that route's front is pushed past them — so gathering *is* a spatial gamble, tied to the coordination layer (§6). A rich node on the far route means committing a flank to hold it, which weakens your center. **The Plunder Junction (§9.4)** lives here: seizing an enemy depot is a Ruthless economic shortcut. Economy and morality intersect at the node.

### 16.3 Crafting — Deterministic, Tech-Gated
Deterministic recipes (no gacha), quality gated by the tech tree (§11.9). Highest craftable tier = **Masterwork**; **Legendary is never craftable** (preserving Champion scarcity, §10.4).

### 16.4 Equipment States & Repair
Equipment degrades to **Damaged** after its bearer falls, reduced effect until repaired with Timber. Repair is a logistics verb, not a shop transaction.

---

## 17. The Era System (Post-MVP)

> **Scope gate.** Post-MVP; gates on the economy. One era only in the MVP.

The army advances through historical technology stages (medieval → gunpowder → industrial → modern), each a **parameter and roster swap on the same rules**, never a new ruleset. Eras change *what* fills the routes (§6.1), not *how* routes work.

### 17.1 Combined Arms Inside the Route Graph
- **Mounts (early eras):** a speed/charge parameter on the soldier entity — fast route travel, first-strike charge negated by cover/barricades. No new entity type. Excellent flankers (§6.5) because they cross junctions fast.
- **Vehicles (industrial+):** standard `EntityStore` entities on route splines with vehicle-class ThreatWeight; crush barricades via a contact check the `NavigationScheduler` already approximates.
- **Aircraft (modern):** *temporary* entities on a second authored spline (the air spline) — spawned, one pass, despawned by `MatchService`. No flight physics. A recon sortie reveals a stretch (feeds fog, §19); a strike sortie hits a route segment; a fighter negates enemy air. Capped at 1–2 to keep the sky *eventful*, not noisy.

### 17.2 The Counter Story (history as balance)

| Threat | Countered by | The history it tells |
|---|---|---|
| Cavalry charge | Cover, barricades, formed infantry | Open shock vs. prepared positions |
| Trenches + MG | Armor | Why cavalry died and tanks were born |
| Armor | Cannon, strike aircraft, combined cost | No single answer — combined arms |
| Strike aircraft | Fighters | Air superiority as enabling condition |

Each era's signature threat is answered by the next era's signature unlock.

### 17.3 Cross-Era PvP — The Legacy Handicap
Cross-era matches apply an automatic numeric handicap (stats + closing speed + logistics terms scaling with era gap), so a medieval army isn't hopeless against an industrial one. The mechanical counterplay (§17.2) already exists in the roster, which is why the handicap can stay numeric.

### 17.4 Scope Discipline
Combined arms ships *inside* the era ladder and inherits every gate above it. If scope must be cut, cut from the sky down: fighters, then strikes, then armor — mounts are nearly free (a parameter set) and survive any cut.

---

## 18. Procedural Maps as Real-Time Strategy (Post-MVP)

> **Scope gate.** Post-MVP, after the North-Star validates on the fixed map (§4.2). Variety is introduced only once attachment and morality are proven on one known battlefield.

The map is a **constraint the player reads and answers in real time**: the terrain (route shapes, junction placement, node distance, chokepoints) poses a question; the player's logistics and orders (where to commit, which route to push, when to flank) are the answer.

### 18.1 Two Layers: Fixed Terrain vs. Player Placement
The generator owns route shapes, junction positions, node/base locations (the *question*, immutable for the match). The player owns barricade airdrops, which cover to garrison, how far to push a route, when to flank (the *answer*, where skill lives). Because terrain is fixed and only *commitment* is free, every generated map poses a genuinely different tactical question — and when Arthur dies on a route you over-committed, the fault is yours. Fault is attachment.

### 18.2 Generation: Rule-Governed, Not Random
The generator is a **constraint satisfier**: it varies terrain within **hard invariants** that guarantee every map is a legible, winnable multi-route tug-of-war. Candidates violating any invariant are rejected and re-rolled.

### 18.3 Hard Invariants (never violated)
1. **Topology is always a route graph** — 2–4 parallel routes joined by 1–3 junction bands, each route a well-defined spline with a scalar front (§4.3). No open 2D arenas — the AI, replication, and tug-of-war assume the graph.
2. **Every route connects base to base**; branches rejoin the graph; no dead ends.
3. **Symmetry of opportunity** — terrain balanced between halves; PvP requires mirrored/rotationally-symmetric layouts.
4. **Route length in range** (e.g. 350–550 studs) for the 6–9 min target.
5. **Junctions reachable and meaningful** — placed so flanking is a real option on every map, never trivially safe or suicidally exposed.
6. **Cover density in the §11.10 band.**
7. **Reachability** — every cover point, node, junction, and rescue position sits on or adjacent to a route spline (no pathfinding islands).

### 18.4 The MVP Map as the Degenerate Case
The fixed MVP map (§4.2) is exactly this ruleset at its minimum: three straight routes, two junctions, default cover spacing, full vision. Downstream systems cannot tell a generated map from the hand-authored one — which is the point: the generator ships without touching the combat, squad, or reputation code.

### 18.5 Technical: Deterministic, Seed-Based
The generator runs once on the server at match start, producing a compact **map descriptor** (route splines, junction/node/base positions, bounds). Seed-based determinism: a pure function of seed + parameters, stored in match state, shipped as a descriptor (not streamed geometry), subject to fog filtering (§19). Both players share one seed. No runtime cost — all placement at start-up; the hot loop never sees the generator. Reproducible from seed alone for debugging and fairness review.

### 18.6 Authoring Still Matters
Designers author the rules, invariants, parameter ranges, and fallback templates, and curate **seed pools** — vetted seeds — for ranked PvP and key campaign beats. The generator provides breadth; human curation guards the peaks.

---

## 19. Fog of War & Reconnaissance (Post-MVP)

> **Scope gate.** Ships with procedural maps (§18). The MVP is full-information. Fog is what makes routes, junctions, and flanking *matter strategically* — without it a flank is visible and counterable; with it, the far route is an unanswered question until someone looks.

### 19.1 The Golden Rule (anti-cheat)
**The server never sends a client what that player should not see.** Vision is computed server-side per player; replication (§13.3) transmits only entities within the revealed area. A client that strips its own rendering still receives nothing it hasn't earned. This makes the tactical matrix **per-player and vision-filtered**, the one structural change fog imposes.

### 19.2 Transparency of Your Own; Darkness of Theirs
- **Your own units are always fully visible to you** — position, HP, Agony, everything. When Arthur falls into Agony you *always* know instantly (the P0 alert, §8.4, still fires) — the emotional core is untouched.
- **Fog hides the enemy and unexplored terrain only.** You earn knowledge of their army and the far ground by looking.

### 19.3 Dynamic Darkness
Three states per route segment: **Unexplored** (nothing known), **Active vision** (full real-time view — a unit of yours is there), **Remembered** (terrain shape known, but live enemy movement hidden once you leave). Leaving drops a segment from Active to Remembered — reconnaissance is a *continuous investment*, not a checklist. The classic dread of a route you cleared and can no longer see.

### 19.4 Reconnaissance as a Tactical Resource
Vision is spent, not free. Every unit has a vision radius revealing fog as it advances; scout-leaning units (mounts §17.1, recon sorties) see farther. The recon-vs-commit tension: units sent ahead to *see* are exposed and off the front. Scouting costs pressure; blindness costs ambushes — and **ambush is a Cunning-reputation tool (§9.2)**, so fog is also where the Honor↔Cunning axis becomes tactical: a Cunning commander thrives in fog, an Honorable one gives it up by choice.

### 19.5 Fog and the Radar
The radar shows **your units always**, **terrain as Remembered-or-better**, **enemy units only in Active vision**. Enemy icons wink out as they slip into fog — itself information. A recon sortie temporarily promotes a stretch to Active at 20 Hz, then decays to Remembered.

### 19.6 Technical (server-side vision)
Vision runs in a low-frequency pass (~4–5 Hz): for each player, union the vision radii of their living units along each route into revealed intervals. The route topology (§6.1) makes this cheap — vision is intervals on splines, not 2D field-of-view. `ReplicationService` intersects each entity's `(route, S)` against the requesting player's revealed intervals before including it. Per-player vision-filtered replication costs more than one global matrix — the accepted server cost of honest fog, kept tractable by the interval model and the unit cap.

---

## 20. Command Hierarchy, Communications & Messengers (Post-MVP)

> **Scope gate.** Post-MVP, gated on M3 (§15) and layered onto the economy (§16) and era system (§17). The MVP is one squad of ≤10 with perfect, free coordination (§6) — the simplification that this section explains and eventually replaces at scale. Nothing here changes M3.

### 20.1 The Problem This Solves

The Squad model in §6 treats coordination as instantaneous and free: every member of a 10-unit squad executes an order the same tick, regardless of distance. That is a deliberate MVP simplification — at ≤10 units clustered on 2–3 routes, it is close enough to true (soldiers in shouting distance of each other) that modeling anything more would add cost for no readable benefit.

It stops being true once the player commands more people than can hear a shout. **This section answers two things at once:** how coordination scales from 1 to a hard cap of **100 NPCs**, and why upgrading a communication device is a real mechanical unlock rather than a stat multiplier.

### 20.2 The Hard Cap: 100, and Why

100 is not an arbitrary round number — it is chosen from two directions that meet in the middle.

**From the military-realism direction.** Real infantry command scales in fixed tiers, and those tiers map directly onto why coordination *needs* communication technology at all:

| Tier | Real size | What holds it together in reality |
|---|---|---|
| **Fireteam** | ~4 | Voice and line of sight. No equipment needed. |
| **Squad** | ~9–10 (2 fireteams + a leader) | Still voice/sight range on a real battlefield; a squad leader can see and shout to both fireteams. |
| **Platoon** | ~30–40 (3–4 squads + HQ element) | **Exceeds shouting range.** Historically this is exactly the size where formal signaling (whistles, flags, runners) becomes necessary, and where radio changed warfare most. |

A player commanding up to **~2–3 platoons** (≈100) is commanding at the edge of what one human battlefield voice could ever coordinate without equipment — which is the entire point: **the cap is the same number where reality itself required communication technology.** Above it, you're modeling company/battalion-level logistics, which is a different game.

**From the Roblox performance direction.** The existing architecture already scales per-unit cost cheaply: combat is event-driven off cooldowns (§5.2), navigation is spline-follow with no pathfinding (§6.1), aggro is dirty-flagged and time-sliced (§10.5). What does *not* automatically scale is coordination logic if it were naively computed per-pair of units (`O(n²)`). The hierarchy below is what keeps it cheap:

```
Cost at 100 units, hierarchical:
  Fireteams:  ~25  (4 each)
  Squads:     ~10  (2-3 fireteams each)
  Platoons:    ~3  (3-4 squads each)
  ───────────────────────────────────
  Coordination nodes to tick: ~38, not 100² = 10,000
```

The `SquadScheduler` (§6.9) already runs per-squad, not per-unit — this section just adds two more cheap tiers above it (fireteam-internal is folded into existing per-unit behavior; platoon is one more scheduler tier). **1 to 100 is a real, continuous range** — a 1-NPC "squad" is a valid edge case (a lone-wolf hero mission), and everything in between just has fewer active tiers. A 7-unit force never instantiates a platoon tier at all; the hierarchy only grows the levels it needs.

### 20.3 The Comms Graph (not radio physics)

The system does **not** simulate real signal propagation — that would be expensive and, worse, unreadable (a player can't see radio waves). Instead it's a graph, recomputed at low frequency exactly like fog-of-war vision (§19.6):

- Every hierarchy node (fireteam, squad, platoon HQ) has a **connectivity range** — how far it can coordinate *without* a device, based on the tier (fireteams: short, voice-range; squads: a bit more, a leader relaying; platoons: effectively zero without equipment — this is the whole point of §20.2's tier table).
- A **communication device**, once researched (§16 tech tree) and issued to a specific named NPC (the "operator" or "signaler" for that node), **multiplies that node's effective connectivity range** by an era-appropriate factor (§20.5) — not a flat "+50%," but enough to bridge the specific gap the tier table identifies (voice → whistle/flag closes fireteam-to-squad gaps; runner/telephone/radio closes squad-to-platoon and platoon-to-commander gaps).
- Recomputed at ~1 Hz by `CommsService`, producing a simple boolean per node-pair: `inCommsRange`. Cheap, because it's the same interval-on-a-route-graph trick as vision (§19.6) — not 2D field checks, not signal simulation.

```lua
-- Runs ~1 Hz. Determines whether two hierarchy nodes can coordinate this tick.
function CommsService.canCoordinate(nodeA, nodeB)
    local dist = routeDistance(nodeA.position, nodeB.position)  -- reuses §6.1's (route, S) math
    local rangeA = nodeA.baseRange * (nodeA.device and nodeA.device.rangeMultiplier or 1)
    local rangeB = nodeB.baseRange * (nodeB.device and nodeB.device.rangeMultiplier or 1)
    -- Coordination requires EITHER node to reach the other; a squad leader's whistle
    -- doesn't need the platoon HQ to also have one for the squad to hear the order.
    return dist <= math.max(rangeA, rangeB)
end
```

### 20.4 What Losing Comms Actually Means (the line you asked me to protect)

This is the rule that keeps the feature from ever feeling punishing in the wrong way: **losing communication degrades orchestration, never survival.** A node that drops out of `inCommsRange`:

- **Keeps executing its last received order** (§6.4) indefinitely — it does not freeze, does not panic, does not go idle.
- **Keeps full Layer 3 survival behavior** (§10.3: retreat thresholds, cover use) — completely independent of comms, always.
- **Loses only:** new orders from above it in the hierarchy, and the ability to synchronize with sibling nodes (e.g. two squads timing a pincer together, §6.5).

Mechanically, a comms-cut node's squad AI (§6) simply keeps running on stale intent — which is a genuine, legible battlefield event ("your 3rd platoon is fighting its own war now, cut off"), not a bug state. This is deliberately the same design move as squad cohesion breaking (§6.7): losing coordination degrades *toward* competent independence, never toward brokenness.

### 20.5 Devices by Era (verisimilitude without tedium)

Each device does one clear thing: closes a specific gap in the tier table (§20.2), and creates one specific, ownable risk. This table is the *whole* spec — no hidden sub-mechanics per device, so it stays fast to learn:

| Era | Device | Closes the gap | The real risk it creates |
|---|---|---|---|
| Medieval | Flag / drum signaler | Fireteam ↔ Squad, within sightline only | Must stay visible to be useful — the signaler can't take cover and still work |
| Medieval | **Mounted messenger** | Squad ↔ Platoon ↔ Commander, no sightline needed | Travels alone across the map; can be **killed** (order never arrives) or **intercepted** (§20.6) |
| Industrial | Field telephone | Any two *fixed* points already wired | Only connects positions you pre-wired — moving past the wire's end drops you off the net |
| Modern | Radio | Squad ↔ Platoon ↔ Commander, long range, no sightline or wiring needed | The **operator is a marked target** (§20.7) — enemy can hunt him specifically to cut a whole squad's coordination in one kill |
| Futuristic | Mesh network | Near-total connectivity, self-healing if one node is lost | **Hackable** — an enemy with the right tech can eavesdrop or feed false orders (a hook for a later "electronic warfare" verb, not built now) |

This is where the era system's promise (§17: "a parameter and roster swap on the same rules") pays off for comms too — nothing above needs a new subsystem per era, only new values plugged into §20.3's `rangeMultiplier` and a device-specific risk hook.

### 20.6 The Messenger — a Named NPC Carrying a Payload

For eras without instant long-range comms, a **Messenger** is how a squad/platoon reaches the commander (or vice versa) across a gap the tier table says voice can't cross. It is not a UI abstraction — it is a real `EntityStore` entity, on the route graph, that can be killed, delayed, or captured, exactly like a soldier.

```lua
Messenger = {
  id = string,
  routeId = string, s = number,       -- same (route, S) position as any unit (§6.1)
  payload = {
    kind = "ORDER" | "INTEL",
    -- ORDER: a squad-order to deliver (§6.4)
    -- INTEL: what the sender currently knows (enemy positions in their vision, a planned flank, etc.)
    data = table,
  },
  originNodeId = string, destinationNodeId = string,
  status = "EN_ROUTE" | "DELIVERED" | "KILLED" | "CAPTURED",
}
```

- **Killed:** the payload is simply lost. If it was an `ORDER`, the destination node keeps executing its last known order (§20.4) — the commander's new plan never arrives, which is a real tactical cost, not a soft failure.
- **Captured (§20.7):** the payload doesn't vanish, it **changes hands** — this is the mechanic you specifically asked for, and it's more interesting than death because the enemy now *knows something they shouldn't*.

### 20.7 Interception & Stolen Intel

An enemy unit within melee range of a Messenger with no friendly escort nearby may **capture** it instead of killing it (an AI/opponent choice, weighted by the Director's aggression knob, §4.3.1, or a player choice in PvP). On capture:

- The payload's `data` becomes readable by the capturing side. An `ORDER` payload reveals **your next move** — the enemy Director gets a temporary bonus to react correctly to it (e.g. reinforcing the exact route you were about to push). An `INTEL` payload reveals **what you had seen** — effectively a one-time fog-of-war leak (§19) of whatever the sender's vision held at send time.
- **A captured Messenger is a prisoner, not a corpse** — which deliberately opens a **Moral Junction** (§9.4): *"The Interrogation."* The side holding the prisoner chooses to extract more (interrogate for further intel — Ruthless+) or release/exchange them (Merciful+, and a captured-then-returned messenger can become a grateful Recruit Candidate, §12.3, mirroring the defector mechanic). Symmetrically, if it's *your* messenger captured, a short window opens where **you can attempt a rescue** — reusing the Rescue System's tension (§7) with a twist: the clock here isn't Agony, it's how long before the enemy finishes extracting what they know.
- **Radio-era operators (§20.5) are marked**, so capture there is rarer than in low-tech eras (a radio operator is usually protected precisely because losing him is understood to be costly) — but killing him still instantly and completely cuts that node's long-range comms, which is arguably the sharper tactical prize.

### 20.8 Why This Doesn't Contradict the MVP

Everything above is additive scaffolding on systems that already exist: the hierarchy reuses `SquadScheduler` (§6.9), the comms graph reuses the interval-on-a-route trick from fog vision (§19.6), the Messenger reuses `EntityStore` unit patterns (§13.5) and the Rescue FSM's tension model (§21.2), and the Interrogation reuses the Moral Junction machinery (§9.4) wholesale. Nothing here required inventing a new architectural primitive — which is exactly the test §15.2 said the Post-MVP sections had to pass.

---

## 21. State Machines (Reference)

### 21.1 Soldier Lifecycle
```
[Barracks] → [Marching] → [In Formation] → [Engaged] → [Retreating] → [Marching]
                               │                │
                               │                ▼
                               │             [Agony] ── rescued ──────────► [Wounded/Barracks]
                               │                │
                               │                └─ not rescued ─┬─ (ordinary fall) ──► [Wounded/Barracks]
                               │                                ├─ (lost via Moral Junction, §14.2) ──► [Dead] → [Wall]
                               │                                └─ (Post-MVP PvP) ──► [Dead] → [Wall]
                               ▼
                          [Detached (flanking)] ── rejoins ──► [In Formation]
```
Note the two new states versus a single-soldier model: **In Formation** (the squad-coordinated default) and **Detached** (executing a flank, §6.5). A detached soldier that dies before rejoining hurts cohesion harder (§6.7). Permanent death has two sources: any loss in Post-MVP PvP, and — in the MVP — a soldier lost as the *consequence of a Moral Junction* (§14.2); ordinary unrescued falls stay temporary.

### 21.2 Rescue Sub-Machine (Medical Cart)
```
[Agony start, 60s timer]
        │
   player launches Airdrop + Cart? ──no──► TIMER_EXPIRED
        │ yes
        ▼
   [EN_ROUTE (cart rides route splines, may cross junctions)]
        │ ── cart intercepted? ──yes──► TOTAL_LOSS (CART_INTERCEPTED; no load %)
        │ cart reaches soldier
        ▼
   [LOADING (4.5s channel)]
        │ ── barricade destroyed mid-channel? ──yes──► TOTAL_LOSS (BARRICADE_DESTROYED; show "% achieved")
        │ channel completes
        ▼
   [RETURNING] ──► [Rescued] ──► soldier persists, returns Wounded
```
`PARTIAL_FAILURE` (the "% achieved" case) is reachable *only* from `LOADING` — a failure `EN_ROUTE` has no load %, avoiding an "85% of 0%" bug. The 60 s timer runs through the whole operation; expiring `EN_ROUTE` resolves as `TIMER_EXPIRED`, expiring during `LOADING` uses the % feedback. Crossing a junction lengthens `EN_ROUTE`, so a far-route rescue genuinely races the clock harder.

### 21.3 Moral Junction Sub-Machine
```
[Trigger condition met (§9.4)]
        │
        ▼
   [PRESENTED] ── P0 alert, local actors freeze, full-screen dialog
        │
   player chooses? ──timeout?──► [DEFAULT branch] (the "no choice is a choice" — usually the passive/merciful default)
        │ choice made
        ▼
   [RESOLVING] ── apply reputation delta, mechanical reward, update Walls
        │
        ▼
   [RESOLVED] ── follow-up beat queued for Battle Report (§8.5); actors resume
```
The **timeout → default branch** matters: refusing to decide is itself a decision the game records, so a player can't dodge reputation by ignoring junctions. `[PLACEHOLDER — the default branch per junction and the timeout length are M3 tuning questions.]`

### 21.4 The "Near-Miss" Feedback
If the cart is destroyed *during* the loading channel, the client shows the percentage reached ("Arthur was 85% to being saved"). Legible failure teaches; opaque failure frustrates — the player learns the rescue *was* possible and is motivated to try again.

---

## 22. Glossary

| Term | Meaning |
|---|---|
| **Agony** | 60 s downed state of a roster soldier at 0 HP; the rescue window (§7.1) |
| **Airdrop Barricade** | Destructible, high-threat supply drop that pulls horde aggro during a rescue (§7.2) |
| **Anchor / Bastion / Reaper** | The three emergent specializations: support / tank / damage (§11.7) |
| **Champion** | The soldier holding the single legendary weapon (§10.4). "MVP" is reserved for Minimum Viable Product |
| **Cohesion** | 0–1 squad stat: how tightly a squad holds together; grants bonuses, degrades to soloists when broken (§6.7) |
| **Comms Graph** | The low-frequency, per-node-pair connectivity check that determines whether hierarchy nodes can coordinate (§20.3) |
| **Competence** | The veterancy stat derived from battles survived (§11.1) |
| **Crystallization** | The moment a soldier's role (§11.7) or the commander's reputation tier (§9.6) becomes permanent, celebrated by a beat |
| **Defector** | A spared enemy who becomes a recruitable Candidate — a Merciful-reputation tool (§12.3) |
| **Detached** | A soldier temporarily split from its squad to flank; rejoins after (§21.1) |
| **Director** | The minimal script controlling the Red side in the MVP (§4.3.1) |
| **EntityStore** | The pure Luau dictionary holding all live entities *and squads*; single-owner, no retained references (§13.5) |
| **Fallen Heroes Wall / Wall of the Fallen-Upon** | The two memorials: heroes lost (§9.6) vs. those the commander chose to let die/execute; each pays out for its morality |
| **Flanking** | Engaging an enemy from a non-frontal angle via the route graph; +35% damage and front-line pressure (§6.5) |
| **Focus** | A squad order broadcasting a shared priority target so the squad collapses fire (§6.6) |
| **Fog of War** | Per-player server-side vision; own units always visible, enemy/terrain only when revealed (§19) |
| **Formation** | A relative offset pattern (LINE/COLUMN/WEDGE/SCATTER) a squad holds along/across its route (§6.3) |
| **Generic / Line Troop** | Unnamed, non-persistent filler soldier; may earn a name (§12.3); conduct still feeds reputation |
| **Junction / Junction Band** | A fixed node where a unit may cross between adjacent routes; the only lateral movement (§6.1) |
| **Legacy Handicap** | Automatic cross-era PvP compensation scaling with era gap (§17.3) |
| **Leader** | A squad's highest-Competence living member; the formation anchor and cohesion bonus (§6.8) |
| **Loading channel** | The 4.5 s static vulnerability window of the Medical Cart (§7.4) |
| **Messenger** | A named `EntityStore` NPC carrying an Order or Intel payload between hierarchy nodes; can be killed or captured (§20.6) |
| **Map Descriptor** | Compact server-generated map definition (route splines, junctions, nodes, bounds) shipped to clients (§18.5) |
| **Map Invariant** | A hard rule every generated map must satisfy or be rejected (§18.3) |
| **Mercy ↔ Ruthlessness / Honor ↔ Cunning** | The two reputation axes; a commander is a point in their 2D plane (§9.1) |
| **Moral Junction** | An authored, condition-triggered, binding decision that moves reputation decisively (§9.4) |
| **North-Star** | The success metric: name recall + the Agony-stakes moment + an owned moral choice (§1.1) |
| **Platoon / Squad / Fireteam** | The three command-hierarchy tiers (≈4 / ≈10 / ≈30–40 NPCs) that scale coordination from 1 to 100 units (§20.2) |
| **Quadrant Archetype** | Paladin / Trickster-Protector / Iron General / Warlord — the four reputation identities (§9.1) |
| **Recon** | Vision gained by advancing units / scout sorties; a continuous investment under fog (§19.4) |
| **Reputation Tier** | A named threshold on a reputation axis; crossing it is a crystallization beat (§9.6) |
| **Rescue Assist** | Fighting within a radius of an active rescue; feeds the Notable score and Anchor spec (§8.2) |
| **Roster** | The player's few named, persistent barracks slots (§12.2) |
| **Route** | One of the parallel battlefield splines (Left/Center/Right in the MVP); units follow it, no A* (§6.1) |
| **Squad** | A first-class entity coordinating up to 10 soldiers with a shared order, formation, and focus (§6.2) |
| **Supply** | The MVP's single resource; prices the rescue (§7.7) |
| **Two-rate replication** | 1 Hz tactical matrix + 20 Hz focus/rescue/junction channel (§13.3) |
| **Wounded** | Post-rescue / PvE-fall status; unavailable one match (§12.4) |

---

## Apêndice A — Guia Para Iniciantes: Colocando o MVP de Pé no Roblox Studio

> Esta seção é escrita em português e em tom de tutorial, separada do corpo técnico do documento. Ela não define design novo — ela traduz o MVP (§4) num caminho prático para quem nunca fez um jogo no Roblox. Se algo aqui divergir do corpo do documento, o corpo do documento vence; este guia é a rampa de acesso, não a fonte da verdade.

### A.0 Antes de começar: a mentalidade certa

Você **não** vai construir o jogo inteiro deste documento. Ninguém constrói. Você vai construir o **M0** primeiro (§15.2) — uma única batalha que roda sem travar — e só depois subir um degrau de cada vez. Cada milestone (M0 → M1 → M2 → M3) é uma coisa que funciona por si só. A regra de ouro: **se não roda, não avança.** É melhor ter um M0 feio que funciona do que um M3 lindo que existe só na sua cabeça.

Uma segunda coisa, e talvez a mais importante para não se frustrar: **o Roblox é servidor-autoritativo** (§13.1). Isso significa que existem duas "mentes" rodando seu jogo ao mesmo tempo — o **Servidor** (a verdade oficial) e o **Cliente** (o que cada jogador vê na tela). Quase todo bug de iniciante no Roblox vem de confundir os dois. Neste jogo, a regra é simples e você vai repetir ela como um mantra: **o Servidor decide tudo que importa** (quem bate em quem, quem morre, quanto de Supply você tem). **O Cliente só mostra e pede.** O Cliente nunca decide nada.

### A.1 Instalando e conhecendo o Studio

1. Baixe o **Roblox Studio** em `create.roblox.com` (é grátis). Instale e faça login com sua conta Roblox.
2. Ao abrir, escolha o template **"Baseplate"** — uma plataforma cinza vazia. É tudo que precisamos; nosso mapa vai ser construído por cima dela.
3. Três painéis que você vai usar o tempo todo:
   - **Explorer** (Explorador): a árvore de tudo que existe no jogo. Se não estiver visível, ative em `View → Explorer`.
   - **Properties** (Propriedades): os atributos do que você selecionou no Explorer. `View → Properties`.
   - **Output** (Saída): onde aparecem os erros e as mensagens do seu código. `View → Output`. **Deixe sempre aberto** — é onde você vai descobrir o que deu errado.

### A.2 Entendendo os "lugares" onde o código mora

No Explorer, alguns contêineres têm significado especial. Você não precisa decorar todos, só estes quatro para o MVP (eles espelham exatamente o §13.2 do documento):

| Contêiner no Explorer | O que roda aqui | O que você vai colocar aqui |
|---|---|---|
| `ServerScriptService` | Código **só do servidor** (a verdade oficial) | Toda a lógica: combate, IA, resgate, Supply, reputação |
| `ReplicatedStorage` | Coisas **compartilhadas** entre servidor e cliente | Os `RemoteEvents` (a "ponte" entre os dois) e dados só-leitura |
| `StarterPlayer → StarterPlayerScripts` | Código **do cliente** (o que cada jogador roda na própria máquina) | Câmera, HUD, radar, botões |
| `Workspace` | O mundo 3D em si | As bases, as rotas, os modelos dos soldados |

**Por que essa separação importa aqui:** se você colocar a lógica de dano em `StarterPlayerScripts`, cada jogador poderia mentir sobre o próprio dano — é assim que trapaça acontece. Colocar em `ServerScriptService` significa que **só o servidor** calcula o dano, e ninguém consegue forjar. Isso não é burocracia, é a fundação anti-trapaça do §13.1 na prática.

### A.3 A linguagem: Luau em 5 minutos

O Roblox usa **Luau** (uma versão do Lua). Você não precisa dominar programação para começar; precisa reconhecer estes padrões:

```lua
-- Isto é um comentário. O jogo ignora.

local vida = 100          -- 'local' cria uma variável. Aqui, vida = 100.

local soldado = {         -- Isto é uma "table" — o coração do Luau.
    nome = "Arthur",      -- É como uma ficha com vários campos.
    vida = 100,
    rota = "CENTER",
}

print(soldado.nome)       -- Mostra "Arthur" no Output. 'print' é seu melhor amigo para debugar.

local function bater(alvo, dano)   -- Uma função: um bloco de ação reutilizável.
    alvo.vida = alvo.vida - dano   -- Tira 'dano' da vida do 'alvo'.
    if alvo.vida <= 0 then         -- 'if' testa uma condição.
        print(alvo.nome .. " caiu!")  -- '..' junta textos.
    end
end

bater(soldado, 30)        -- Chama a função. Agora soldado.vida = 70.
```

Se você entendeu que uma **table** é uma ficha com campos e que uma **função** é uma ação que você chama, você já consegue ler 80% do código deste documento. O `SoldierRecord` (§12.5) e o `Squad` (§6.2) são só tables grandes.

### A.4 Passo a passo do M0 — a primeira batalha que roda

O objetivo do M0 (§15.2) é: **uma batalha de esquadrão contra esquadrão que roda ~8 minutos sem travar e sem vazar memória.** Sem resgate, sem reputação, sem nomes ainda. Só soldados andando numa rota, se batendo, e uma frente de batalha que se move. Vamos por partes.

#### Passo 1 — Construa o mapa mínimo (sem código)

1. No `Workspace`, crie duas `Part` grandes e coloridas — uma **azul** em `x = 0` e uma **vermelha** em `x = 400` (use o painel Properties para setar `Position` e `Color`). Essas são as bases (§4.2). Renomeie-as `BlueBase` e `RedBase`.
2. Crie três `Part` longas e finas ligando as bases, lado a lado — essas representam visualmente as três rotas `Left`, `Center`, `Right` (§6.1). Por enquanto são só decoração; a lógica de rota vai viver no código como números, não nessas peças.
3. Ancore tudo: selecione as peças e marque `Anchored = true` em Properties, senão elas caem pela gravidade.

> **Dica:** No MVP, a posição de um soldado é `(rota, distância)` — dois números — não uma coordenada 3D livre (§13.3). Essas peças no Workspace são só para você *ver* onde as coisas estão. A verdade é `soldado.rota = "CENTER"` e `soldado.s = 150`. Guardar isso na cabeça desde o começo evita muita confusão.

#### Passo 2 — O EntityStore (a memória viva da batalha)

Em `ServerScriptService`, crie um `ModuleScript` (clique com o botão direito → `Insert Object → ModuleScript`), renomeie para `EntityStore`. Este é o §13.5 do documento na sua forma mais simples: uma table que guarda todos os soldados vivos, acessados por ID.

```lua
-- ModuleScript: ServerScriptService/EntityStore
local EntityStore = {}

local units = {}   -- a table onde todos os soldados vivos moram, indexados por ID

function EntityStore.add(unit)
    units[unit.id] = unit
end

function EntityStore.getUnit(id)
    return units[id]
end

function EntityStore.remove(id)
    units[id] = nil   -- tirar do table libera a memória (§13.5)
end

function EntityStore.all()
    return units
end

return EntityStore
```

**A regra crítica do §13.5, em português simples:** só *um* script (o `MatchService`, que faremos a seguir) tem permissão de **adicionar ou remover** soldados deste store. Todos os outros só *leem* por ID. Se você seguir essa disciplina desde o M0, nunca vai ter aquele bug horrível de "soldado fantasma" que continua atacando depois de morto.

#### Passo 3 — Spawnar soldados e fazê-los andar

Crie um `Script` (não ModuleScript — um `Script` roda sozinho) em `ServerScriptService`, chamado `MatchService`. Ele cria os soldados e move eles pela rota:

```lua
-- Script: ServerScriptService/MatchService
local EntityStore = require(script.Parent.EntityStore)

local nextId = 0
local function makeSoldier(team, route)
    nextId = nextId + 1
    local soldier = {
        id = "S" .. nextId,
        team = team,          -- "BLUE" ou "RED"
        route = route,        -- "LEFT" | "CENTER" | "RIGHT"
        s = (team == "BLUE") and 0 or 400,  -- azul começa em 0, vermelho em 400
        hp = 100,
        walkSpeed = 12,       -- studs por segundo (§5.5)
        status = "ACTIVE",
    }
    EntityStore.add(soldier)
    return soldier
end

-- Cria 3 soldados de cada lado, um por rota (o MVP mira ~10, comece pequeno)
for _, route in ipairs({"LEFT", "CENTER", "RIGHT"}) do
    makeSoldier("BLUE", route)
    makeSoldier("RED", route)
end

-- O loop de navegação (§10.1): move cada soldado pela sua rota, a cada 0.2s (§6.9)
task.spawn(function()
    while true do
        task.wait(0.2)
        for id, u in pairs(EntityStore.all()) do
            if u.status == "ACTIVE" then
                local dir = (u.team == "BLUE") and 1 or -1  -- azul avança +, vermelho -
                u.s = math.clamp(u.s + dir * u.walkSpeed * 0.2, 0, 400)
            end
        end
    end
end)

print("MatchService rodando: soldados criados e andando.")
```

Aperte **Play** (o botão ▶). No Output você verá "MatchService rodando". Os soldados existem e andam — mas ainda são invisíveis (só existem como dados). Isso é **correto e esperado**: a verdade existe no servidor antes de qualquer visual. Ver isso funcionar no Output é seu primeiro marco real.

> **Por que `task.wait(0.2)` e não rodar todo frame?** Porque rodar tudo todo frame é exatamente o erro de performance que o §13.4 alerta. Mover soldados 5 vezes por segundo é suave o suficiente e custa uma fração do processamento. Este é o primeiro lugar onde a arquitetura do documento vira código real na sua mão.

#### Passo 4 — Combate por alcance e cooldown

Agora os soldados precisam se bater quando ficam perto. Isto é o §5 (combate "falso" por alcance e temporizador). Adicione ao `MatchService`, dentro de um novo loop:

```lua
-- Combate (§5.1): cada soldado procura o inimigo mais próximo na MESMA rota e bate no cooldown
task.spawn(function()
    while true do
        task.wait(0.5)
        local now = os.clock()
        for id, u in pairs(EntityStore.all()) do
            if u.status == "ACTIVE" then
                u.lastAttack = u.lastAttack or 0
                -- acha o inimigo mais próximo na mesma rota, dentro do alcance de visão (40 studs, §5.5)
                local target, bestDist
                for oid, other in pairs(EntityStore.all()) do
                    if other.team ~= u.team and other.status == "ACTIVE"
                       and other.route == u.route then
                        local d = math.abs(other.s - u.s)
                        if d <= 40 and (not bestDist or d < bestDist) then
                            target, bestDist = other, d
                        end
                    end
                end
                -- se tem alvo no alcance de corpo-a-corpo (5 studs) e o cooldown passou, bate
                if target and bestDist <= 5 and (now - u.lastAttack) >= 1.8 then
                    target.hp = target.hp - 12   -- dano de recruta (§5.5)
                    u.lastAttack = now
                    if target.hp <= 0 then
                        target.status = "DEAD"
                        EntityStore.remove(target.id)   -- só o MatchService remove (§13.5)
                        print(u.id .. " matou " .. target.id)
                    end
                end
            end
        end
    end
end)
```

Aperte Play de novo. Agora, quando soldados azuis e vermelhos se encontram no meio da rota, eles se batem, e o Output vai cuspir "S1 matou S4" etc. **Você tem uma batalha.** Ela é invisível e brutalmente simples, mas cada linha aqui é um sistema do documento na sua forma-semente: alcance de visão, corpo-a-corpo, cooldown de ataque, e a regra sagrada de que só o `MatchService` remove do store.

#### Passo 5 — A frente de batalha (o tug-of-war)

Falta o §4.3: a posição da frente `L` que se move conforme quem tem mais gente viva perto dela. Por enquanto, o mais simples possível, uma rota só para provar o conceito:

```lua
-- Frente de batalha do Center (§4.3), recalculada a 1 Hz
local frontCenter = 200   -- começa no meio
task.spawn(function()
    while true do
        task.wait(1.0)
        local blue, red = 0, 0
        for id, u in pairs(EntityStore.all()) do
            if u.route == "CENTER" and u.status == "ACTIVE"
               and math.abs(u.s - frontCenter) <= 60 then   -- "perto da frente" = ±60 studs
                if u.team == "BLUE" then blue = blue + 1 else red = red + 1 end
            end
        end
        frontCenter = math.clamp(frontCenter + 2 * (blue - red), 0, 400)  -- k=2 (§4.3)
        print("Frente Center em: " .. math.floor(frontCenter))
        if frontCenter <= 0 then print("VERMELHO venceu o Center!") end
        if frontCenter >= 400 then print("AZUL venceu o Center!") end
    end
end)
```

Pronto: **este é o M0.** Soldados nascem, andam, lutam, morrem, e uma frente de batalha se move conforme quem domina. Roda num loop, não trava, e você pode assistir tudo pelo Output. Feio? Muito. Mas é uma fundação **correta** — cada peça está no lugar certo da arquitetura, e nada aqui precisa ser jogado fora quando você subir para o M1.

### A.5 O que vem depois (a ordem que não te deixa afogar)

Siga o roadmap (§15.2) na ordem, e resista à tentação de pular. Aqui está o que cada próximo degrau adiciona, em termos do que você já construiu:

1. **Dar corpo visível aos soldados (fim do M0):** crie um modelo simples (um `Part` ou um `R15` dummy) por soldado e, num `Script` do cliente, mova o modelo para acompanhar o `(rota, s)` que o servidor manda. Aqui você encosta pela primeira vez na ponte servidor↔cliente — use um `RemoteEvent` em `ReplicatedStorage` (§A.6).
2. **M1 — Esquadrão e comando (§6):** transforme sua lista solta de soldados num objeto `Squad`, adicione o `SquadScheduler`, e implemente **uma** ordem (`ADVANCE`) e o **flanqueamento** (§6.5). O critério de saída é conseguir vencer uma rota *por causa* de um flanco.
3. **M2 — Identidade (§8, §12):** dê nomes e caras aos soldados, salve os stats entre sessões com `DataStoreService`, e faça o botão **Follow** (§8.3). Critério: um amigo joga e depois lembra o nome de um soldado.
4. **M3 — Resgate + Moralidade (§7, §9):** o coração emocional. Estado de Agony, medidor de Supply, o carrinho de resgate, e **uma** Junção Moral por sessão. Este é o milestone que decide se o jogo funciona (§1.1).

Cada um desses é semanas de trabalho para um iniciante, e tudo bem. O documento inteiro (§16 em diante) só existe *depois* que o M3 provar que a ideia central gruda.

### A.6 A ponte servidor↔cliente (o conceito que mais confunde iniciantes)

Você vai precisar disto assim que quiser mostrar qualquer coisa na tela. Um `RemoteEvent` é um "telefone" entre servidor e cliente. Crie um em `ReplicatedStorage`, chamado por exemplo `SoldierUpdate`.

**O servidor avisa o cliente** (ex: "o soldado S1 está em `s=150`"):
```lua
-- No servidor (dentro do MatchService)
local remote = game.ReplicatedStorage.SoldierUpdate
remote:FireAllClients(soldier.id, soldier.route, soldier.s, soldier.hp)
```

**O cliente escuta e atualiza a tela:**
```lua
-- Script em StarterPlayerScripts
local remote = game.ReplicatedStorage.SoldierUpdate
remote.OnClientEvent:Connect(function(id, route, s, hp)
    -- aqui você move o modelo 3D e atualiza a barra de vida na tela
end)
```

**A regra de ouro (§13.1), de novo, porque é a que mais salva iniciantes:** o **cliente nunca manda o servidor "eu tomei 30 de dano"**. É sempre o contrário — o servidor calcula e *avisa* o cliente. Se você inverter isso, criou uma brecha de trapaça. Quando o cliente precisa *pedir* algo (ex: "quero resgatar o Arthur"), ele pede via `RemoteEvent`, e o **servidor decide** se pode (tem Supply? o soldado está em Agony?). O cliente pede; o servidor manda. Sempre.

Para o resgate (§7), o medidor de Supply mora no servidor (§7.7): o cliente só desenha a barrinha e envia "quero resgatar"; o servidor confere os 80 de Supply, e só ele mesmo mexe no número. Isso é o §13.1 inteiro num parágrafo.

### A.7 Erros de iniciante que vão te economizar horas

- **"Meu script não faz nada."** Confira se é um `Script` (roda sozinho) e não um `ModuleScript` (só roda quando outro script o chama com `require`). E confira se está no contêiner certo (§A.2).
- **"Attempt to index nil."** Você tentou ler um campo de algo que não existe — quase sempre um soldado que já foi removido do EntityStore. É por isso que o §13.5 manda **ler por ID toda vez** e nunca guardar a referência do soldado: se ele morreu, você lê `nil` e trata isso, em vez de segurar um fantasma.
- **O jogo trava/engasga com muitos soldados.** Você provavelmente está rodando lógica pesada todo frame. Volte para os `task.wait()` (§A.4) — combate e IA são escalonados em intervalos (§6.9), nunca todo frame (§13.4).
- **Mudanças no cliente não afetam o jogo dos outros.** Correto e esperado — o cliente é local. Se algo precisa ser real para todos, tem que acontecer no servidor.
- **Perdi meus dados salvos ao testar.** `DataStoreService` não funciona em jogos não publicados por padrão e tem limites de frequência. Publique o jogo (mesmo que privado) e ative `Studio Access to API Services` nas configurações do jogo antes de testar persistência (M2).

### A.8 Onde aprender o resto

- **Documentação oficial:** `create.roblox.com/docs` — a referência de tudo (em inglês, mas com exemplos claros).
- **Assunto por assunto, na ordem que você vai precisar:** primeiro *Scripts e ModuleScripts*, depois *RemoteEvents*, depois *DataStoreService* (para o M2), depois *ProfileService* (uma biblioteca da comunidade que resolve o "session-locking" do §14.1 para você — não reinvente isso).
- **Regra de estudo:** aprenda a coisa *no momento em que o milestone pede*, não antes. Você não precisa saber `DataStoreService` para fazer o M0. Aprender tudo de uma vez é como decorar o dicionário antes de escrever uma frase — cansa e não gruda.

Comece pelo Passo 1 do §A.4. Faça o M0 rodar no Output antes de qualquer outra coisa. O resto do documento estará esperando quando você chegar lá.

---

*End of technical draft v2.0. Lore, worldbuilding, faction and character names, and narrative fiction to be authored in a separate document.*
