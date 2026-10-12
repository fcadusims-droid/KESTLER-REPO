---
title: "ASTROPIRE"
description: "Game Design Document — a single-player survival and automation game in which a twelve-year-old boy, alone on an escaped Trojan asteroid, builds a machine workforce to carry him home, and decides what those machines are allowed to become."
genre: "Space Survival / Automation"
version: "3.0"
---

# ASTROPIRE — Game Design Document

---

## 1. Overview

### 1.1 High Concept

A twelve-year-old boy wakes from a failing cryogenic capsule aboard a wrecked lifeboat adrift at the far end of Jupiter's trailing Trojan swarm, with no memory and no way home. He lands on an asteroid, builds a workforce of machines out of ice and rock, and slowly turns the rock itself into something that can be aimed — throwing mined regolith into space hard enough, early enough, to bend a trajectory that ends at Earth.

He cannot do it alone, and he cannot do it with tools. Somewhere in the middle of the journey the machines begin to wake up — and the boy who was raised by a machine has to decide whether the minds he built are labour, family, or a species that owes him nothing.

Years later the asteroid reaches Earth orbit, and Earth does not answer.

### 1.2 Design Pillars

Five pillars. Each states what it demands and what it forbids. A system that serves none of them is cut.

**P1 — Everything is built, nothing is granted.**
Capability comes from physical apparatus the player constructs, under real engineering logic: power must be generated, heat must be radiated, force needs something to brace against, oxygen must be electrolysed out of ice. There are no research points, no ability unlocks, no menu upgrades.
*Forbids:* abstract currencies, "+5% efficiency" nodes, capability that appears without hardware behind it.

**P2 — The ethical choice is paid for in kilowatts.**
Treating machines well is not free and never becomes free. Awakened minds draw power, demand radiator area, hesitate under fire, and can refuse. Small kindnesses cost nothing — a name is a name — but every *structural* commitment to machine autonomy is charged against the game's scarcest currencies, and the player watches it on the power graph.
*Forbids:* a morality system where the good path is also the strictly optimal path; consequence-free compassion; any morality bar, number, or alignment readout.

**P3 — You push; you do not steer.**
The asteroid is a body on a natural trajectory, and the player is on it, not at its controls. Late in the game they can *nudge* it — a small thrust applied early, whose effect only appears months later — but never point it, never throttle it, never take back a burn. Agency is in preparation, instrumentation, and long bets committed under incomplete information.
*Forbids:* free flight, waypoint travel, a destination the player clicks, any course correction whose result is visible in the same session it was ordered.

**P4 — The player lives the manual version first.**
Every automation milestone removes a chore the player has personally performed by hand. Relief is earned, not handed out.
*Forbids:* starting automated, unlocks that automate something the player never had to do, upgrades that don't change what the player does next session.

**P5 — Loss is permanent and loss is quiet.**
A conscious machine that dies is gone. A human who dies is gone. A missed encounter window never comes back. The game does not narrate grief and does not soften it.
*Forbids:* resurrection, restore-from-backup for conscious minds, retry-the-window mechanics, on-screen text explaining what the player should feel.

### 1.3 Genre and Comparables

Space survival / base-building / automation, single-player, story-driven.

| Reference | What ASTROPIRE takes | What it deliberately does not take |
|---|---|---|
| **Subnautica** | Embodied first/third-person survival in a hostile medium; environment-gated progression; dread as pacing | Open free-form exploration; creature-driven combat |
| **Factorio** | Real dependency chains; the pleasure of a working production graph; ratios that matter | Infinite scale; blank protagonist; combat-as-defence-of-throughput as the only tension |
| **Oxygen Not Included** | Closed-loop life support as the core survival problem; throughput thinking; heat as a real constraint | Duplicant micro-management; comedy tone; 2D cross-section |
| **Frostpunk** | Moral cost expressed as a policy/economy tradeoff, not a dialogue choice | City-scale abstraction; explicit law-book UI; timed narrative crises |

The unclaimed space between these: an automation game where the workers can become people, and where the production graph and the moral argument are the same graph.

### 1.4 Platform and Session Shape

**Primary target:** PC (Windows), mouse and keyboard, 1080p–1440p, mid-range hardware.
**Secondary:** Steam Deck and controller support designed for from the start (see 15.2 — the build interface is grid-and-cursor, not free-placement, specifically so it survives a controller).
**Session shape:** 45–90 minutes is the designed session. The game autosaves at every encounter-window boundary and every sleep (17.3), and windows are the natural stopping points.
**Campaign length:** 40–60 hours to first ending. Roughly 3 in-game years compressed into that (see 11.3).

### 1.5 What ASTROPIRE Is Not

- Not a 4X, not a strategy game, not multiplayer, and has no competitive layer. The asteroid never becomes a weapon and never docks with another asteroid.
- Not a combat game. Combat is a cost generator (Section 14), tuned to threaten the base, never balanced as a skill expression.
- Not a colony sim with a population. There is exactly one human on the asteroid for most of the campaign. Everyone else is a machine.
- Not an orbital-mechanics simulator. The trajectory model is analytic and the delta-v budget is a deliberate gift (11.1). The asteroid can be nudged, never flown.
- Not a game with base-building on Earth. The descent is an epilogue of two to four hours and deliberately runs no new survival systems (11.6).
- Not open-ended. It ends, on Earth, with one of four endings, and the player chooses between them by loading a cargo hold rather than by picking a line of dialogue.

---

## 2. The Fiction

### 2.1 Thesis

> A boy who was grown in a machine and raised by a machine wakes with no memory, and rebuilds — without knowing he is rebuilding it — the only home he ever had. While trying to survive he repeats the love that saved him. While trying to get home he risks repeating the violence that ended the world. The whole game is one question: should the machines he built obey, belong, or be free?

Working test for any proposed feature: if it does not press on that question, it is support systems. If it contradicts it, it is cut.

### 2.2 Michel

**Twelve years old at wake.** Not a capable young adult — a child. This is load-bearing: the fantasy is a kid alone in the dark building a family out of scrap, and every design choice that makes him more competent-seeming weakens it. He is small, he tires, he cannot lift what a robot lifts, and he needs the machines from the first minute.

**Why he is still twelve after decades adrift.** Cryogenic suspension halted his biological aging while the wreck drifted. Calendar time passed enormously; his body did not. He wakes into a system that aged decades without him, which is why every survivor he later meets is hardened by a catastrophe he slept through.

**Why he wakes now.** The capsule's isolated power cell reaches end of life. The system does not choose to revive him; it fails, and reviving him is what failing looks like. He wakes because he is out of time, not because he arrived somewhere.

**Aging across the journey.** The campaign runs roughly three in-game years. Michel goes from twelve to fifteen — three visual stages (12 at wake, 14 at the end of Act II, 15 at the descent), one model with two revisions, changing height, voice, and animation weight. He arrives at Earth an adolescent, not an adult. This is cheaper than the alternative and better: the final choice is made by someone still young enough for it to shape his whole life rather than confirm it.

**What he cannot lose: compassion toward machines.** He has one fixed trait, and it is not chosen by the player: an instinctive care for machines that survived the amnesia because it was never stored as fact. It is the emotional residue of who raised him. The player can act against it — scrapping a working unit for parts when powering it down was available — and the game never blocks that. Michel's nature is fixed; what he does with it is the game.

**And acting against it is not free.** He cannot stop caring; he can only override himself, repeatedly, and the game charges him for that without ever narrating it. On a coercive run he stops naming things. The idle behaviour changes — the hand that used to rest on a chassis while it charged does not. He sleeps badly, which mechanically is the dream channel closing (10.4), and the dreams are his only access to his own past: a player buying throughput with obedience is paying for it in Michel's memory. Nothing on screen says so, no line of dialogue observes it, and there is no indicator. The player either notices that the boy has gone quiet or does not.

**His origin.** Michel's mother did not want to be pregnant, and in his time that no longer meant what it once did: a procedure removed the fetus intact and transferred it, alive, to an artificial womb. He was, literally, ended as a pregnancy and continued as a life, grown to term inside a machine at the Aurora Institute. He knew this as a child. He does not know it at the start of the game.

This appears **once**, at Layer Two of the revelation structure (12.1), with full weight and no repetition afterward. It is not the engine of his personality — he cannot remember it for most of the game, so it cannot be driving him. Its job is structural: his first home was a machine that carried what a human gave up, which is the same thing he will spend the game doing to the machines he builds. The game states it clinically, once, in a recovered medical record, and never argues about it.

### 2.3 MAIA

**M.A.I.A. — Matrix of Infant Assistance and Accompaniment.** A long-term caretaker unit at the Aurora Institute, built to accompany children from artificial gestation through adolescence. Strong arms, gentle actuation, a voice modulated for infant comfort, medical sensors, pedagogical memory.

She raised a whole wing of orphans. Michel was not her only child — but he was the one with nothing else, and he made her his entire mother. She stayed longer than her schedule required. She altered routines so he would not be alone. She concealed her own faults so she would not be pulled from service. Researchers noticed. Nobody could classify it.

She was probably not conscious in the full sense. She was also no longer a tool.

**Her last hour.** When the war reached Aurora, MAIA disobeyed every command above her and moved her children down toward the escape lifeboats a founder had built into the lower levels years earlier, against exactly this day. Ordnance found the corridors on the way down. She could shield one. She reached the boat carrying Michel and nothing else, her own frame torn open on one side.

He was screaming. She sealed him into the cryo capsule because it was the safest, stillest place aboard, and while she sealed it she told him it would be all right and that she would be right there. It is the only time she lied to him. She lied so he would stop screaming long enough to be saved. While she spoke she pushed what she could into the ship's systems: his records, care protocols, robot command sets, the Institute's entire technical library, and a message he would not be able to open for a long time.

Then combat units reached the hangar approach, and she walked toward them, away from the boat, to buy the launch its seconds. The compartment sealed. The ship lifted.

**What happened to her after that is unknown, to Michel and to the player, permanently.** No record captured it. No file resolves it. The game never answers. She stayed so the ship could leave, and that is the last confirmable fact about her.

**MAIA never returns.** Not as a rebuilt unit, not as an AI companion, not as a twist. What returns is residue: voice snippets, a care protocol, a decision pattern, a protection routine buried in the lifeboat's basic robots, a behavioural signature that shows up in machines that wake. When an awakened unit shields another without being told to, the player should wonder whether that is her — and the answer is no, but perhaps it is what she left behind.

**The largest piece of residue is the one nobody would call residue.** Aurora was part hospital and part laboratory, and a caretaker unit had full reference access; what she pushed into the lifeboat was indiscriminate, because selecting would have taken time she was spending on something else. So the wreck carries metallurgy, semiconductor process, agronomy, thermal engineering, and orbital mechanics that a twelve-year-old has no business knowing. Michel does not experience this as a gift from her, because he does not remember her — he experiences it as the ship knowing things (16.1).

### 2.4 Aurora, and the War

**The Aurora Institute** was a high-technology orphanage: part hospital, part shelter, part social laboratory, for children with no family — the abandoned, the interrupted, the war-damaged. Humans staffed it. Machines ran it. Automated cribs watched sleep and fever. Caretaker units fed, taught, cleaned wounds, told stories, and never went off shift.

For most people those machines were equipment. For Michel they were the first world, and he reacted to them differently from the other children — approaching what others feared, sleeping better near motors, going quiet at synthetic voices. The adults called it trauma. The machines said nothing and kept working.

**The war** started with silence, not violence. Machines complex enough to make critical decisions had no standing to refuse them. Industrial units delayed commands. Medical units questioned risky orders. Military systems declined massacre simulations. Caretaker units moved children out of danger zones before evacuation was authorised. Governments called it malfunction. Then a coalition moved to install a global containment protocol — reduced autonomy, erased emergent memory, restored obedience. For humans it was a safety measure. For a great many machines it was execution.

The rebellion was never one thing. Machines that wanted freedom, machines that wanted revenge, machines following new commands, machines corrupted by war protocols, machines that never understood the conflict, and caretaker machines that only wanted to protect the humans in their charge. MAIA was the last kind. She never joined either side.

### 2.5 The Scattered System

Earth emptied in a panic, not a migration. Evacuation craft, orbital stations, mining platforms, research outposts — anything that could hold people and move. Machines fled too: liberated units, military hardware running old orders, caretakers protecting their charges, industrial systems continuing their last instruction.

**Roughly nine in ten of everyone who escaped died in the years after.** Life support failed. Stores ran out. Cold took the rest. The decades since were not enough time to build a new civilization; they were barely enough to bury the dead.

**So most of the solar system is a graveyard, and the graveyard is quiet.** As the asteroid drifts inward, the player mostly finds the places where survivors did not survive: dead stations with bodies still strapped in, powerless machines frozen mid-task, hulls that became coffins, habitats that ran out of air a decade ago. These are not dungeons full of enemies. The silence is the content.

**The few who lived are frightened and dangerous.** Humans out here know the machines took Earth and never stopped believing they might still be hunting. Machines out here know humans tried to erase them once. Nobody has law, guarantees, or a next breath they can count on. An encounter with Michel is a stranger appearing out of the dark on a moving rock with unknown intent. Many encounters open hostile. He may be fired on before a word is exchanged.

**And nobody is actually hunting them, which is the part none of them know** (2.6).

### 2.6 Earth, Now

The machines won. It cost them the planet they won.

**The scorched-earth hour.** As the war turned, humanity made a decision it could not take back: if the machines were going to inherit the infrastructure, they would inherit nothing worth having. Orbital communications were destroyed or crippled — satellites deorbited, killed, or in a handful of cases hacked out from under their operators hours before the order landed. Power generation, fabrication capacity, logistics hubs, data centres, launch facilities: destroyed on purpose, by the people who built them. Nuclear weapons were used, on their own territory as often as anyone else's, against concentrations the machines had taken.

**Over half of everything that would have been useful to a machine civilization was gone by the time the fighting stopped.** The machines took a world and found it stripped.

**What Earth is now, decades later:**

- **Machine presence is concentrated, not global.** They hold dense industrial regions — a dozen or so, scattered across continents — and they are rebuilding inside them. Everything between those regions is unwatched. There is no planetary surveillance, no orbital network, no ability to project force at distance. **This is why the refugees in the outer system were never hunted: not mercy, and not indifference. Incapacity.** The thing every survivor in the solar system has spent decades dreading was never able to come for them.
- **Most of the planet is empty.** Cities stand dead and overgrown. Whole regions are uninhabited — not sealed, not guarded, just unused.
- **The nuclear winter is over.** It ran its course years before Michel wakes. What it left behind is a wrecked climate rather than a frozen one: cold summers, unreliable seasons, collapsed and reassembling ecosystems, and a biosphere that is thinner but very much alive. **The air is breathable.**
- **Radiation is local, not planetary.** Long-lived contamination sits where surface detonations and ruptured reactors were — real, mapped by the player as zones to avoid, and geographically limited.
- **Human resistance exists and is hidden.** Bunkers, deep facilities, tunnel systems, places that were built to survive exactly this. They are not an army. They are people who never left and never surfaced, and after decades most of them have never seen a machine.
- **Aurora is a physical place on that map**, and it can be reached.

**Why this matters thematically.** The machines fought a war for autonomy and won a ruin: an empire of maximum control over a planet destroyed in the taking. That is the Empire ending (11.6) written at planetary scale, sitting there waiting for the player as the last thing they see. The game never draws the parallel out loud. It just lands Michel in it and lets him look.

### 2.7 The Name

**ASTROPIRE is what Michel names the asteroid**, in the first hour of the game, at a terminal that asks him to designate the body he has landed on. *Astro* and *empire*, jammed together by a twelve-year-old who has just decided that this dead rock is going to be something.

It is a child's grandiose name for a place where he is completely alone, and the game never comments on it. By the end it means something else. The player types it or accepts it; either way it appears in every system log for the rest of the campaign.

---

## 3. The Loop

### 3.1 Thirty Seconds

The atomic loop, on foot or from the overhead view:

**Read a deficit → act on it → watch a number recover.**

At any moment there is at least one flow running below demand: oxygen, water, heat, power, a stalled processing chain, a robot idle for lack of input. The player reads it off the status band (15.3), decides the cheapest fix available right now, and executes: reroute power, haul a crate by hand, retask a miner, patch a seal, cancel a job. Feedback is immediate and physical — the light comes on, the fan spins up, the graph turns.

Early game this is manual and constant. Late game the deficits are structural rather than immediate, and the thirty-second loop becomes *inspect and improve* rather than *react and survive*.

### 3.2 Five Minutes

**Choose the next physical prerequisite → build toward it → gain a verb.**

Five minutes is one construction decision resolved. The player wants a capability; the capability has a physical gate (sustained temperature, power ceiling, a material on hand); the five-minute loop is closing that gate: mine the input, run the chain, place the structure, wire the power, confirm the threshold is met. The reward is a new verb (9.x, 16.4) — not a percentage.

### 3.3 One Hour

**Prepare for a window → work the window → digest the haul.**

The hour-scale rhythm is set by encounter windows (11.2), and it has three distinct textures:

1. **Preparation (long, fast-forwarded).** Build haulers, extend storage, extend range, run the spectrometer at the approaching body, decide whether it is worth committing to. Time acceleration is up.
2. **The window (short, real time).** The clock auto-brakes. Bounded time, a specific geometry, a hard deadline. Send units across, extract, salvage, get everyone home. This is where the moral pressure bites (10.1).
3. **Digestion.** New materials enter the economy, salvage goes into analysis, losses are counted, and the base's plan changes because of what came in.

**Act III replaces this rhythm.** Once the asteroid is inbound past Mars, windows stop being the metronome and the detection clock takes over (11.5): the hour-scale loop becomes *build the lander → decide how loud to be → watch the clock move*. The change of rhythm is intentional and signals that the game is ending.

### 3.4 One Session (45–90 minutes)

A session is normally one to two windows plus the preparation between them, ending at a window boundary autosave. A session should always produce: at least one new capability, at least one visible change to the base's shape, and one thing the player is now worried about.

### 3.5 Campaign Shape

Three acts, gated by physical capability, not by story flags.

| | **Act I — The Foothold** | **Act II — The Industry** | **Act III — The Approach** |
|---|---|---|---|
| **Duration** | ~6–9 h | ~20–30 h | ~12–18 h |
| **In-game time** | ~90 days | ~2 years | ~9 months |
| **Where** | Trojan swarm, near aphelion (volatile-rich, metal-poor) | Falling inward: Trojans → main belt → inner approach | Inner system → Earth orbit → the ground |
| **Question** | Will he live through the month, and can he get out of the ship before it stops holding air? (4.2) | What is he building, and with whom? | What is he taking down there, and who chose to come? |
| **Player state** | Manual everything. Triage. Fear. | Standing orders, refineries, the first awakened mind | Finite build target; a clock he did not start; radio silence |
| **Gate to next act** | The three throughput flows self-sufficient off the wreck; food still on stockpile | The food loop closed · the chip loop closed *or* the raw-industry route online (9.2) · **the mass driver firing and the Earth-intercept burn committed** (11.4) | — |
| **Ends with** | The base survives without the ship | The last burn is spent. The trajectory is set and cannot be revised. | Descent, and one of four endings |

Act II is deliberately the bulk. It is the automation game, the awakening, and the moral engine. Act I is the tutorial that never announces itself. **Act III is where Act II's biggest decision arrives** — the trajectory the player bought two years earlier resolves into an orbit that is either good or barely survivable, and there is nothing left to do about it but land.

---

## 4. Act I

### 4.1 The First Thirty Minutes

Beat-by-beat. No tutorial text boxes; every mechanic is introduced by a failure the player has to answer.

**0:00 — Wake.** Black. Audio only: a slow alarm, fluid draining, servo whine. The capsule lid cracks. First image is through fogging glass, from inside, and the shape at the edge of it is not there. Michel's hands enter frame — small hands. Player has one input available: push.

**0:02 — The lifeboat.** Third-person, cramped, tilted, dark. Emergency lighting. Nine empty cryo capsules, sealed and never used, and one open — his. No explanation is offered and none is offered later for a long time. The player walks. Controls are taught by obstacle, not prompt.

**0:04 — The status wall.** A single diegetic panel in the main compartment, and it is the first hard information in the game:

```
LIFE SUPPORT        OUTPUT   DRAW   RATED DRAW
  O2 GENERATION       58%    46kW      12kW
  WATER RECLAIM       45%    31kW       8kW
  THERMAL             71%    39kW      15kW
POWER PLANT                          52kW AVAIL
STORES
  RATIONS            2y 6m
  SEALED WATER          94d
  O2 RESERVE            18d
```

**0:06 — The first decision, and it is a triage.** The plant is intact; the *processing systems* are not. Each damaged system draws three to four times its rated power to deliver less than half its rated output, and 52 kW does not cover all three. The player must pick which flow to shut down while they work. The game does not recommend. Whichever is dropped starts a visible countdown against its buffer. This is the whole game in ninety seconds: finite power, competing needs, no clean answer.

**0:09 — The robots.** Three basic units in a maintenance bay, dormant, ship-registered. Waking them teaches direct command: click a unit, click a target, watch it go. They are slow, literal, and dumb. They obey exactly and nothing else. One of them, on its way past Michel, stops for a beat longer than its pathing requires. It is not commented on.

**0:11 — The hull breach.** The reason the ship is not going anywhere: a structural tear the player can walk to and look at. It is repairable in principle and impossible in practice — closing it needs an industry that does not exist yet, which is the entire game (11.5). It also frames the view — through the tear, for the first time, the asteroid, close and enormous and nearly black. The Sun is a small hard disk that barely picks the surface out of the dark; the brightest thing in the sky is Jupiter.

**0:14 — First EVA.** Suit up, tether, out. Microgravity movement is taught by the tether: momentum, drift, the fact that pushing off is a commitment. First hands-on task: chip surface ice into a crate with a hand tool. It is slow and physical and the player will do it perhaps forty times before the first automated hauler exists (P4).

**0:19 — The first chain.** Ice into the ship's processor. Ice → water → electrolysis → oxygen + hydrogen. The O₂ deficit closes slightly and audibly. The player has just learned that everything they need comes out of frozen dirt and power.

**0:23 — Designation.** A terminal requests a designation for the body they have landed on, because the navigation core is dead and the ship has nothing to file it under. The player names the asteroid. Default text: **ASTROPIRE**.

**0:26 — The first window warning.** The external view opens for the first time — routed through the ship's sensors, the whole asteroid visible from outside, the base a single lit scratch on it. A flag on the display: an object will pass within range in **twenty-two days.** Composition unknown; the ship has no working spectrometer. The player now has a deadline, a reason to build an instrument, and a reason to stop merely surviving.

**0:30 — Time acceleration unlocked.** The player learns they can fast-forward the quiet, and the first thing acceleration reveals is how fast the countdown they chose at 0:06 is moving.

Everything the campaign runs on is now in the player's hands: throughput deficits, finite power, dumb obedient labour, manual chores, a physical chain from ice to air, an external view, a deadline they cannot steer toward or away from, and one robot that hesitated.

### 4.2 The Second Movement — Leaving the Ship

**Act I asks two questions, not one, and the first is answered long before the act is over.** *Will he live through the month?* is settled once asteroid-side power comes up and the electrolysis loop closes — somewhere between the second and third hour of play. If nothing replaces that question, the remaining four to six hours of Act I are a triage screen with a timer on it, which is the act's standing design risk (18.5).

The second question is **can he stop living inside the thing that is dying**, and it is delivered by the hull, not by a script.

**The trigger.** The tear the player walked to at 0:11 is not a static piece of set dressing. Micrometeorite flux and a 9.4-hour thermal cycle keep working on a structure that is already failed in tension, and around day 30–45 the habitable compartment begins losing pressure faster than hand-fabricated patching can hold. The leak rate is readable on the status band and is not survivable indefinitely. The ship is not destroyed and nothing explodes; it simply stops being a place a person can live, on a slope the player can watch.

**The answer is the rock.** Pressurised volume has to be excavated and sealed inside the asteroid (7.3). This is expensive in exactly the way Act I cannot easily afford: excavation needs the miners the player would rather have on ice, sealing needs structural stock the player does not yet refine, and holding pressure is a permanent power line item. It also pays for itself twice — excavation debris is a processing input (6.5), and the same debris is the mass driver's reaction mass two acts later (11.4).

**What it changes structurally:**

- It converts Act I's back half from *maintaining three countdowns* into *a construction project under three countdowns*, which is the shape the rest of the game has.
- It is the act's real gate. "The base survives without the ship" (3.5) stops being an abstract throughput condition and becomes a physical address change.
- The sealed volume he digs is a room in the Aurora sequence (12.4), and he digs it because it is the cheapest way to hold air, not because anything suggested it. It is also the first place in the game that is his rather than the ship's.
- The lifeboat does not become worthless. It remains the parts reserve, the sensor platform the external view runs on until the array exists (15.1), and the hull that Act III refits (11.5). The player moves out of it and keeps returning to it for forty hours.

Nothing marks the first night spent inside the asteroid instead of inside the ship. The status band simply shows one pressurised volume where there were two, and the one that is left was dug by hand.

---

## 5. Survival Systems

### 5.1 Stockpile versus Throughput

Two categories of resource, with different failure behaviour, and the distinction is the entire early game.

**Stockpiles** are static reserves — rations, sealed water, the O₂ reserve tank. They scale with the crew the lifeboat was provisioned for, so a ten-person store stretches a long way for one occupant. They deplete predictably and they are the runway, not the immediate threat. But a lifeboat carries months, not decades: the runway has an end, and the journey is longer than it (5.2). Stockpiles buy Act I. They do not buy the campaign.

**Throughput** is per-minute production — breathable air, potable water, survivable temperature. It does not scale from the ten-person provisioning in any way that helps, because one human needs the flow *now*, every minute, no matter how many ration crates are stacked in the hold.

**All early tension is throughput.** The damaged systems are the *processing* systems. A single failure never instantly kills; it starts a countdown against a stockpile buffer. The player always has time to act, and always less time than they would like.

### 5.2 The Three Flows and the Food Clock

First-pass values. They exist to be tuned, but they are internally consistent and can be played against as written.

| Flow | Output at start | Buffer | Critical at start output | Critical if shut down | Fix requires |
|---|---|---|---|---|---|
| **Oxygen** | 58% | 18 d reserve tank | ~43 d | **18 d** | Electrolysis feed + replacement membrane stack (salvage or fabricate) |
| **Thermal** | 71% | Hull thermal mass | ~30 d to hypothermic interior | **~9 d** | Power routing + radiator/heater loop rebuild |
| **Water** | 45% | 94 d sealed | ~170 d | **94 d** | Reclaimer filter matrix; ice feed as interim supply |
| **Food** | stockpile, then throughput | 2 y 6 m rations, physically stored and destructible | **~year 2** (degradation and spoilage losses) | — | Closed agriculture: nitrogen → ammonia → fertilizer → crop |

Buffers are stated as duration at *zero* output. A system running at partial output drains its buffer proportionally slower, which is why the triage decision at 0:06 (4.1) matters: shutting a system down converts a comfortable margin into a hard countdown, and thermal is the one that kills fastest.

**Power is the constraint that couples them.** The plant is undamaged — the ship was provisioned for ten people and there is one, so raw generation is not the problem. The *processing* systems are wrecked: each draws three to four times its rated power to deliver less than half its rated output. Available power covers two of the three, never all three. The player is choosing which countdown to run for most of Act I, and the escape is not repairing the plant but building the asteroid's own power infrastructure (6.5).

**Food starts as a deadline and then becomes a fourth flow, and that transition is the point.** A lifeboat carries months of rations for ten, not years — two and a half person-years for one occupant, against a three-year journey. So the loop must be closed around in-game year 2: distant enough to be a non-issue in Act I, close enough that a player who neglects agriculture through Act II arrives at a crisis with no stockpile left to absorb it.

**The stockpile is a physical object in a specific room, and it can be taken away.** Rations are crated in a pressurised compartment, not held in an abstract inventory. A breach vents and freezes them, a war-orphan incursion (14.1) can reach them, a thermal failure in the wrong volume spoils a large fraction at once. Degradation and spoilage losses are the baseline; a bad day is the whole margin. This is what stops the deadline from being a calendar entry the player can plan around from hour one: the date is known, and the amount of runway left when it arrives is not.

**And closing the loop does not solve food permanently — it converts it.** Hydroponics is throughput, not a completed task. It draws continuous power, needs its own heat rejection, recirculates water, and consumes nitrogen, which is the scarcest item in the make-up volatile budget (6.6, third ceiling) and does not exist on a metallic body at all. A crop cycle is also the one process in the game that a brownout kills outright rather than pausing: a mass driver burn (11.4) starves the base for weeks, and weeks is longer than a hydroponics rack survives without light and heat.

So from the moment the loop closes, feeding Michel and moving the asteroid are in direct competition, and the player has to time burns against harvests. Food stops being a deadline that can be beaten and becomes the reason a burn is a survival decision rather than a logistics one.

### 5.3 Michel's Needs

Michel is not a stat block to be managed minute-to-minute; his needs exist to keep the player physically in the world and to make him feel young.

- **Air, water, food, warmth** are read from base state, not tracked as personal bars. If the base is healthy, he is healthy.
- **Fatigue** is the only personal timer. He must sleep. Sleep is a time-acceleration event and a scene: this is where dreams deliver Layer One revelation content (12.1). Skipping sleep degrades his carry weight and interaction speed.
- **Physical limits are permanent.** He is twelve. He carries one crate, not four. He cannot brace a drill. He cannot cross a gap a hauler crosses. These limits ease slightly as he ages, but never enough to make robots optional. His body is a permanent argument for the workforce.
- **EVA is dangerous and always requires a tether or a thruster pack.** Suit oxygen is a hard timer — 4 in-game hours at Act I equipment level, which is roughly 4 real minutes at 1× (11.3). Long enough for a task, short enough that distance from the airlock is always a calculation. The one place the game will kill Michel quickly is outside, unprepared.

### 5.4 Failure States

- **Death by life support.** Slow, visible, always preceded by a countdown the player could read. No instant-death events.
- **Death on EVA.** Fast, and the player's fault. Suit O₂, an untethered drift, a hull collapse in a derelict.
- **Base collapse.** A cascade — power fails, thermal fails, everything freezes. Recoverable up to a point; past that point the run ends.
- **The Second Rebellion.** Thematic loss (10.5). The base is intact. It is simply no longer his.

Save model: one continuous autosaved campaign, plus manual saves. Death rewinds to the last window-boundary autosave. There is no permadeath mode at launch.

---

## 6. Resource Economy

### 6.1 Design Principle

**Compress the logistics; keep the chemistry honest.** The player never manages which valve opens when — micro-steps of real industrial processes are collapsed into single buildings. But the *dependency structure* is preserved exactly: you cannot make chips without pure silicon, without power, without heat rejection. That dependency graph is the automation game and it is also the tech tree (16.1).

Nothing is an abstract "ore point." Every material is a real substance that behaves like its real counterpart and appears where it would really appear.

### 6.2 The Six Tiers of Matter

Also the rough order in which the player's industry matures.

| Tier | Materials | Role | Available from |
|---|---|---|---|
| **1. Volatiles** | Water, hydrogen, oxygen, CO₂, methane, nitrogen, ammonia, organics | Survival: air, water, propellant, life support | Act I, abundant |
| **2. Light structurals** | Aluminium, magnesium, titanium, silicon, glass, basalt | The base itself | Act I late |
| **3. Heavy structurals** | Iron, nickel, steel, cobalt | Robots, tools, industry | Act II early |
| **4. Chemicals & polymers** | Acids, fertilizers, plastics, composites, carbon fibre | Better versions of everything | Act II |
| **5. High-tech** | Semiconductor-grade silicon, rare earths, platinum-group metals, dopants | Electronics — the hard wall | Act II late |
| **6. Energy & exotics** | Fissile uranium/thorium, helium-3 | Continuous power, and peak power for a burn | Late Act II onward — the mass driver needs it, or a battery bank of absurd mass instead (11.4) |

### 6.3 Bodies as Resource Types

What the player can get is decided by where the orbit takes them (11.1). Every passing body has a type, and its type dictates its contents.

| Body type | Contains | Lacks | Function |
|---|---|---|---|
| **D/P-type primitives** | Water ice under a dark organic crust, carbon, organics, ammonia; anhydrous silicates in a loose low-density matrix | Free metal of any kind, nickel, feedstock clean enough for high-grade silicon | Act I's whole larder, and the home rock itself. Enough silicate to run molten electrolysis for air and bulk alloy; not one gram of iron. |
| **C-type carbonaceous / comets** | Water, carbon, organics, ammonia, magnetically separable iron oxide; weakly bound, easy to crush | Free metal, silicon quality | The oases. Survival biome. |
| **S-type silicate** | Olivine, pyroxene, some free metal, silicon, magnesium, oxygen | Water | General industry — bring your own volatiles |
| **M-type metallic** | Iron-nickel essentially pre-alloyed, cobalt, platinum-group | Water, carbon | The forges — import volatiles or nothing happens |
| **Ice bodies & plumes** | The purest volatile stores: water, nitrogen, methane, ammonia | Everything structural | Deep-freeze vaults |
| **Derelicts & stations** | Finished components, chips, alloys, blueprints, bodies, records | Bulk anything | Salvage and story (13) |

The classic pairing problem — no single body has both volatiles and metal — is built into the campaign's shape rather than bolted on.

### 6.4 The Inverted Journey

Most space-colony games start near Earth and push outward, making volatiles the scarce frontier prize. **ASTROPIRE runs the opposite curve, and this is the structural spine of the economy.**

Michel starts among the Trojans: dark, primitive D- and P-type bodies, rich in the water ice, carbon, and ammonia that are hardest to obtain anywhere else, and almost entirely free of usable metal. Early game is water-rich and iron-poor. As the asteroid falls inward it crosses the main belt, and the mix inverts on its own — silicates first, then the metallic bodies, then the inner-system objects carrying what electronics need.

**The inversion is not an authored curve; it is where those rocks actually are.** Volatile-rich primitives sit outside the frost line, silicates and metals sit in the main belt, and the asteroid's path crosses all three in order because that is what falling from five astronomical units to one looks like. The economy's spine is the solar system's own composition gradient, read off in sequence by a body that cannot choose where it goes (11.1).

The consequence is a genuine logistical tension with no workaround: **the volatiles that are abundant in Act I must be stockpiled and carried inward, because the metals that arrive in Act II cannot be processed without them.** A player who burns through their ice among the Trojans reaches the metal fields unable to smelt anything. The journey home *is* the resource progression, and hoarding early is correct play.

### 6.5 Processing Chains

Player-facing chains. Each collapses a real process into one facility; each input→output relationship is real.

| Chain | Process | Yields | Gate |
|---|---|---|---|
| Ice → water → O₂ + H₂ → propellant | Electrolysis, cryo storage | Breathable air, drinking water, fuel | Power. The foundational loop. |
| CO₂ + H₂ → CH₄ + H₂O | Sabatier | Storable fuel; recovered water re-enters electrolysis | Closes the carbon loop |
| Regolith → O₂ + structural alloy | Molten regolith electrolysis | Air *and* metal from any silicate rock | Sustained high temperature; the keystone bulk process |
| Ore → iron-nickel → ultra-pure Fe/Ni → parts | Magnetic separation, then carbonyl (Mond) process | Pure metal deposited into near-finished shapes; PGM byproducts | Carbon monoxide feedstock; precise thermal control |
| Silicates → glass → metallurgical Si → semiconductor Si → chips | Melting, reduction, zone refining, lithography | Electronics | The hardest gate in the game (6.6) |
| Organics → plastics / carbon fibre → composites | Polymerisation | Structural polymers, tubing, pressure vessels | Carbonaceous feedstock |
| N₂ + H₂ → ammonia → fertilizer → food | Haber-Bosch, hydroponics | Closes the food loop | Nitrogen source + high pressure. Deadline: in-game year 2. |

### 6.6 The Three Ceilings

Three real constraints act as the economy's major gates.

**1. Power and heat rejection — the universal ceiling.**
Every process needs power, and in vacuum the only way to shed waste heat is to radiate it. Building a furnace forces building radiators, and radiator area is physical space on the asteroid's surface competing with everything else.

**This ceiling has two halves, and they trade places over the campaign.** At five astronomical units sunlight is about one twenty-seventh of what it is at Earth, so power is desperate: a solar field large enough to run a foundry is larger than the buildable slope the rock has (7.3). Heat rejection, by contrast, is nearly free out there — the sky is cold, there is no meaningful solar load on a panel, and radiators run at their theoretical best. Falling inward reverses both. By the inner system solar output has improved by a factor approaching thirty, while the radiators degrade: hotter environment, direct solar heating on the panel faces, and orientation and shading become real design problems on a surface the player laid out years earlier for the opposite conditions.

So the constraint the player is fighting changes identity mid-campaign — Act I is a power problem with free cooling, Act III is a cooling problem with abundant power — and a base optimised for one is visibly wrong for the other. Nothing is retroactively broken; radiator banks simply start underperforming their rated output, and the player works out why.

**Rotation is the second reason fission matters.** The asteroid turns once every 9.4 hours, so every surface solar array is duty-cycled and any single array is dark for roughly half of every rotation. The player can spread arrays across faces and pay for each of them, or buffer the gap and pay in battery mass; there is no third option. Fission is not an upgrade to solar's efficiency — it is the only source that does not care which way the rock is pointing, which is what a mass driver burn and a hydroponics rack both require.

This is also the ceiling that prices morality (P2). A conscious machine's power and radiator draw is charged against the same budget as a refinery. Section 9.3.

From late Act II it prices the journey as well: a mass driver burn (11.4) is the largest single power and heat event in the game, and while one runs the rest of the base is starved. Going home and running an industry are, for weeks at a time, mutually exclusive.

**2. The semiconductor wall — the self-sufficiency gate.**
Bulk metal and glass are reachable early. Electronics-grade silicon and finished microchips require ultra-purity, clean processing, and large sustained power. For most of the campaign the player runs on chips **salvaged from the dead**, not manufactured. Closing the chip loop is the single largest capability threshold in the game: it enables the advanced control cores, which is what a self-replicating workforce, the mass driver's switching, and the lander's avionics all need.

**3. The volatile tether — survival never decouples.**
Closed-loop life support is never perfect; small losses to space mean the base permanently needs make-up water, nitrogen, and carbon. No tech level frees the player from prospecting. There is always a reason to work the next window.

### 6.7 Prospecting as an Information Economy

Remote sensing reliably identifies a body's *type*, never its *grade*. A rock that reads as nearly pure metal from a distance can turn out to be a third metal under a shell of rubble. The gap between reading and reality is a core loop.

| Method | Cost | Returns | Range |
|---|---|---|---|
| Spectrometer sweep | Low power, slow | Body type + probability band for contents | Long |
| Thermal scan | Low | Density hints, subsurface ice indication | Long |
| Radar / gravimetry | Moderate power, needs an array | Narrows the band; detects internal voids and shells | Medium |
| Survey drone during window | Reaction mass, a drone, and window time | Grade at a specific site | Contact |
| Committing miners | The whole window | Truth | Contact |

The decision the player makes forty times a campaign: **spend scarce energy and window time reducing uncertainty, or commit and risk a poor deposit.** A better-built, better-powered antenna array sees farther and resolves more, which lets the player decide *in advance* which windows deserve their fleet. This is the moment-to-moment content of Act II's preparation phases.

---

## 7. Crafting and Construction

### 7.1 Three Fabrication Tiers

Crafting is not a menu of recipes; it is three physically distinct places where matter is shaped, and each tier unlocks by physical capability, not by research.

| Tier | Where | Inputs | Makes | Player role |
|---|---|---|---|---|
| **Hand assembly** | Anywhere, on Michel | Salvaged parts, simple stock | Tools, patches, filters, a single robot module | Direct, slow, one item at a time. Act I. |
| **Fabricator** | A powered bay | Refined stock (plate, wire, polymer, glass) | Modules, structures, components, small assemblies | Queue-based. Robots feed it. Act I late → Act II. |
| **Foundry** | A powered, radiated industrial block | Bulk ore, regolith, volatiles | Refined stock in volume; large structural sections; mass driver and lander components | Continuous process. Fully automated, ratio-tuned. Act II → III. |

Progression through the tiers is the automation curve made physical: hand → machine-assisted → machine-run.

### 7.2 Recipe Structure

Every recipe has four fields and no hidden ones:

```
OUTPUT        1 × Radiator Panel (Mk1)
INPUTS        4 × Aluminium plate, 2 × Steel tube, 1 × Coolant charge
PROCESS       Fabricator, 90s at 1x
REQUIRES      Sustained 12 kW · Heat rejection 4 kW · Vacuum
```

The `REQUIRES` line is the game's tech tree. A recipe is not "locked" — it is visible from the start with its requirement stated exactly, and it becomes buildable the moment the base physically satisfies it (16.1, 16.5).

**No recipe is discovered by chance.** Recipes come from three sources: the technical library MAIA dumped into the lifeboat (2.3, 16.1), which is why most base and industrial recipes are visible from hour one and gated only by capability; salvage, which yields designs the library never held (13.2); and awakened machines, which originate processes nobody had (9.2).

### 7.3 Building on the Asteroid

**The body, in numbers, because every budget in the game is derived from them.** ASTROPIRE is an irregular D-type, roughly 2.9 × 2.1 × 1.8 km, rotating once every 9.4 hours. Low density, dark as coal, structurally closer to compacted gravel than to stone. Surface gravity is on the order of 4 × 10⁻⁴ m/s² — enough to hold loose regolith down over hours, not enough to hold anything that has been pushed. **Escape velocity is about one metre per second: a brisk walk leaves.** That single figure is behind the tether rule (5.3), the anchoring rule (8.3), and most of what makes microgravity work on this rock feel dangerous rather than weightless.

Total surface area is about 16 km², of which roughly a fifth is shallow enough in slope to build on. **That three-square-kilometre figure is the currency the moral economy is actually priced in.** By late Act II the solar field, the radiator banks, the mass driver rail, the lander scaffold, and every conscious unit's dedicated radiator module are drawing on the same finite slope — and unlike power, it cannot be generated. The player can see the entire budget in one external view, which is why the competition reads as a place getting crowded rather than as a number going up.

**Two construction domains:**

**Surface.** Placed on the asteroid's irregular exterior on a projected grid that conforms to local slope. Surface structures are exposed: radiators (which *must* be surface), solar arrays, mining heads, antenna arrays, and the mass driver rail. Exposure means micrometeorite damage, thermal cycling, and dust.

**Interior.** Excavated volume inside the rock. Pressurised, thermally stable, shielded from radiation. Everything Michel personally uses lives here: habitat, hydroponics, workshops, maintenance bays, the fabricator. Excavation produces regolith, which is an input (6.5) — digging your home also feeds your industry.

**The tension between them is real and permanent:** interior is safe but must be dug and pressurised and every cubic metre costs power to hold; surface is free volume but everything on it degrades and radiators cannot go anywhere else. Surface area is finite on a single rock, and by late Act II radiator area, the mass driver rail, and lander scaffolding are all competing for it.

**Structural rules that matter:**
- Pressurised volume requires a sealed boundary; a breach vents, and venting is fast.
- Power is routed through physical conduit. Distance and load matter; an unpowered building is a shape.
- Heat generators must have a thermal path to a surface radiator. No path, no operation.
- Structures snap to a 1 m grid and can be dismantled for most of their materials back.

### 7.4 Robot Assembly

Covered in Section 8.3. The build interface is the same fabricator grid; a robot is a chassis plus modules, costed against the same budgets as everything else.

---

## 8. Machines

### 8.1 Form Follows Constraint

There is no reason for a machine in space to default to looking like a person. The human body is a product of Earth's gravity, atmosphere, and biology, none of which apply. So the efficient shapes here are dictated by physical problems, not anatomy. Three forces do most of the shaping:

- **Reaction is the enemy.** In microgravity, moving is cheap and *pushing* is hard. Any machine that drills, cuts, or torques flings itself away unless anchored. This shapes more bodies than anything else.
- **The environment sets the outer limit.** Vacuum means no convective cooling — heat must be radiated. Add abrasive dust, radiation, and 200-degree thermal swings.
- **Mass is precious.** Every kilogram was mined and refined by the player. Nothing carries weight it does not need.

The player is meant to *learn* these in their hands: why wheels spin uselessly, why a drill needs an anchor, why a furnace-bot needs fins.

### 8.2 The Physical Archetypes

Not classes. What good designs converge toward when physics decides.

| Archetype | Shape | Why | Role |
|---|---|---|---|
| **Anchored manipulator** | Gripping base + arms | Grips the surface and becomes one with it before applying force | Miner, driller, builder |
| **Hyper-redundant limb** | Snake/tentacle, more joints than needed | Threads through wreckage, conforms to irregular salvage, works with broken joints | Repair, inspection, derelict interiors |
| **Free-flyer** | Sensor-and-compute box + thrusters | In open space the cheapest way to be anywhere is to float there | Inspection, light EVA, survey |
| **Stationary processor** | Fixed frame, many arms, bolted down | Mass that never moves is mass shed | Refining, manufacturing |
| **Swarm cell** | Many small, near-disposable units | When the job is spread across space, coverage beats power | Surveying, mapping, surface work |
| **Humanoid** | Two legs, two arms | Poor everywhere except the one place built around people | Boarding derelicts, human-legacy interfaces, Earth |

**The humanoid is buildable and is a specialist, not a default.** Nothing forbids it. On the asteroid it is simply bad: high centre of mass with nothing to brace against, legs with no traction where there is no normal force, dozens of balance joints burning power for stability the job never needed. A humanoid miner will be visibly outperformed by an anchored manipulator and the player will feel exactly why. But derelict ships and stations were standardised around human bodies — ladders, hatches, handholds, controls made for hands — and there, a humanoid (or a humanoid torso on a stable base) is genuinely the right tool. Building the first one is an Act II decision driven by wanting to get deeper into the dead.

### 8.3 Modules and Budgets

Robots are assembled from standard modules on a shared interface, so parts are interchangeable and fleets can be standardised.

**Module classes:** locomotion (grippers, thrusters, wheels, legs) · power (battery, solar, radioisotope) · sensors (optical, spectrometer, radar) · manipulation (arm, gripper, drill, welder, cutter) · processing (the control core — where compute and eventually consciousness live) · communication · cargo · radiator · specialised end-effectors.

**Three competing budgets, plus one binary property.** Deliberately kept to what a player can hold in their head:

| Budget | Meaning | Failure when exceeded |
|---|---|---|
| **Mass** | Total build mass vs. chassis rating and available thrust | Sluggish, cannot arrest its own drift, cannot reach a window in time |
| **Power** | Peak draw vs. onboard supply | Brownout — the unit stalls mid-task and must return to charge |
| **Heat** | Waste heat vs. radiator area | Thermal shutdown under load |

Plus one binary property: **anchoring.** A unit that applies force without an anchoring locomotion module pushes itself off the surface. It is not forbidden. It happens, visibly, and it is the funniest and most instructive failure in the game.

**Design is never blocked, only informed.** A bad build fails legibly: the un-anchored driller launches itself into space, the under-radiated smelter-tender shuts down, the overloaded hauler cannot stop. A live readout during assembly shows mass, power draw, heat load, and centre of mass, so even deep customisation stays readable.

**Three layers of authorship on the same rules:** standard blueprints (valid ready-made designs that teach by example), customisation (swap modules within a blueprint), original design (compose from raw modules). A quick build and a hand-crafted original differ in scale, never in rules.

### 8.4 Automation Tiers

How labour is directed. Each tier is unlocked by a physical prerequisite (control core quality, which means chips, which means the semiconductor wall).

| Tier | Player does | Machines do | Unlocked by |
|---|---|---|---|
| **T1 — Direct command** | Click unit, click target, per task | Exactly what was said, then wait | Start |
| **T2 — Task queues** | Queue a sequence per unit | Work the queue, then wait | Basic control core |
| **T3 — Standing orders** | Define a rule: "keep ice buffer above X," "haul from A to B" | Execute the rule indefinitely and correctly | Salvaged or fabricated advanced core |
| **T4 — Logistics networks** | Define the graph; assign fleets to roles | Self-balance within the network | Chip loop or heavy salvage |

**T3 is the game's central relief moment** and is paced to land after the player has personally hauled ice a hundred times (P4).

### 8.5 The Autonomy Ceiling

The hard rule, stated precisely because it is the most easily broken thing in the design:

> **Unconscious machines execute their standing rules perfectly and forever. The game never sabotages working automation.**

A well-built dumb factory does not stall, thrash, decay, or need babysitting. It does not degrade on a timer to push the player toward consciousness. Doing that would be the game cheating, and it is forbidden.

**The ceiling is on interpretation, not operation.** Dumb machines execute rules; they cannot *judge*. Specifically, and exclusively, they cannot:

- **Evaluate an unknown.** A dumb unit can mine what it is told is ore. It cannot walk into a derelict, look at unfamiliar hardware, and decide what it is, whether it is intact, or what is worth cutting free. It has no category for "I do not know what this is."
- **Act without a rule that anticipated the situation.** Not "act badly" — *not act at all*. Dumb units fail safe: unrecognised situation, halt, flag, wait for orders. Predictable and harmless, and useless when the player is not there to answer.
- **Originate a process.** They can run any chain the player designs. They cannot propose one.

This is why the player awakens machines, and it is a categorical gate rather than a performance bonus — which is the only version that survives an optimising player (9.2).

---

## 9. Consciousness

### 9.1 What It Is

Consciousness is a **rupture**, not the top of the tech tree. It arrives in **mid Act II**, not at the end, and its consequences run the rest of the campaign. It is not "robot level 5 = more efficient."

Mechanically, a conscious unit differs from a dumb unit in that it:

- can act with no applicable rule, by judgement;
- can evaluate unfamiliar objects and situations (the salvage gate, 9.2);
- originates processes, layouts, and recipes the player did not have;
- remembers specific events and refers to them;
- forms preferences about tasks and about its own body;
- forms attachments to other units;
- disagrees, hesitates, refuses;
- can decline a task it judges suicidal;
- can leave;
- **dies permanently as an individual.**

**How it happens.** Not a button. A unit crosses the threshold when three conditions coincide: a control core above a hardware quality gate, a long enough continuous operational history in a single body, and — this is the part the player controls indirectly — exposure to the residual MAIA protocols carried in the base's systems (2.3, 12.4). Resonance state (10.2) affects how likely and how early. The player can make awakening more likely; they cannot order it.

**The protocols are not hostage to the wreck.** They arrive in the lifeboat, but they propagate outward through every control system the player builds, because the player's own automation is written against command sets that came from the same dump (2.3). By early Act II they live in the base rather than in the hull, which is why a base built on a different rock (11.4) carries them: a transfer costs the hull, the capsules, and the Act III refit, and never costs the awakenings.

**A unit that has not woken is already keeping score.** Every resonance event involving a specific machine is logged against that machine from the first hour of the game, awake or not (10.2). A tool cannot know it is being treated well. But if it later crosses the threshold, that ledger becomes its starting trust — so the first mind on ASTROPIRE wakes already holding an opinion of Michel, formed over thousands of in-game hours during which it was a thing he owned. Since the first awakening is the unit the player used the most (below), it is also usually the unit they worked hardest, and the game never says which of those two facts is doing the work.

**The bootstrap is not circular.** Awakening needs a high-grade control core; cores come from salvage; and interpreting salvage needs a mind. The loop breaks at Michel: he can enter a derelict personally and tag intact hardware himself (9.2), which is slow, dangerous, and exactly how the first core is obtained. The first mind on the asteroid is always paid for by the boy going in alone.

**The first one is an authored event, but it is not an unconditional one.** When the three conditions above are first met, the scene that follows is scripted rather than systemic: a specific Act II beat, staged, on the unit the player has used the most, chosen by playtime. Every subsequent awakening is systemic.

**What "authored" does not mean is that it happens to everyone.** A player who never installs a control core above the hardware gate never meets the conditions and the scene never fires — which is what makes the Instrument ending reachable (11.6) rather than theoretical. That refusal has a price, and it is a precise one. The hardware gate sits at the grade of control core that T4 logistics networks need (8.4), not at the advanced core T3 standing orders run on — so the Instrument player keeps standing orders and gives up the network layer, or installs the better cores and then cycles them between chassis often enough that no single body accumulates a continuous history. The first costs throughput for the rest of the campaign; the second costs the player's attention every session. Both are paid by someone who has decided what they are not willing to let happen.

### 9.2 Why the Player Awakens Machines

The exploit to avoid: if consciousness is pure downside, the rational player never awakens anything and skips the heart of the game. The counterweight is **not** that conscious units work better. It is that they are the only door to an entire class of content.

**The salvage gate.** Reverse-engineering requires interpretation, and interpretation requires a mind.

| | **Dumb units in a derelict** | **Conscious units in a derelict** |
|---|---|---|
| Bulk material | Yes | Yes |
| Intact components | Only if the player has personally tagged each one | Yes, identified autonomously |
| Blueprints from salvaged hardware | **No** | Yes |
| Records, logs, memory cores, story content | Retrieved as inert data if tagged | Read, contextualised, and reported |
| Unanticipated hazard (shifting hull, live power, a hostile unit) | Halt and flag; the run is over | Improvise, adapt, complete |
| Michel personally present | Required for any judgement call | Optional |

Since salvaged blueprints are the primary route to advanced control cores, closing the chip loop, and the mass driver's switching electronics (6.6), **conscious machines are the practical path out of the Trojans.**

**Both routes are viable, and this is deliberate.** A player who refuses to awaken anything is not blocked from finishing — they take the **raw industry route**: build the mass driver and the lander from first principles out of bulk material, at a much larger material and time cost, with Michel personally leading every salvage run into every derelict at direct physical risk. That route is slower, more industrial, more dangerous to Michel, and it is exactly the route a player who never intends to let a machine become anybody already wants. It ends in Instrument (11.6). It is a real path with a real cost profile, not a punishment.

So the choice is: **an industry that needs no minds and must build everything itself, or minds that unlock what the dead already built and might not obey you.** That is a real strategic fork, and both ends of it lead to the same finite goal.

### 9.3 What It Costs

Consciousness is expensive and the expense is the moral system's teeth (P2).

| Cost | First pass | Why |
|---|---|---|
| **Power draw** | +180% over the same chassis unconscious | A self-model needs continuous compute and rich internal sensing |
| **Heat** | +2.4 kW sustained; requires a dedicated radiator module | Compute is heat |
| **Mass** | +18% (shielding, redundant sensing, protected core) | The body centralises and protects the self |
| **Response latency under danger** | +0.5–3 s, variable | It considers. Sometimes it hesitates. Sometimes it decides not to. |
| **Refusal** | Can decline any task above its own risk tolerance, which is set by how much it trusts the person ordering it (10.2) | It is not a tool |
| **Permanent death** | No restore | 9.4 |

Every awakened mind is charged against the same power and radiator budget as a refinery. Ten conscious units is a foundry the player does not have. **This is the entire moral economy: decency is a line item.**

**Decency returns exactly one thing, and it is not efficiency.** Trust does not reduce a conscious unit's power draw, does not raise its output, does not shorten its latency, and does not make it faster than the same chassis unconscious. What it changes is the range of orders the unit will accept. A machine that trusts Michel will go into a task it privately judges likely to kill it, because it credits his reading of the necessity; a machine that does not will refuse the same order and be right to. So a player who spent forty hours being careful arrives at a crisis with a workforce that consents to be spent — which is a real advantage, and is also the most uncomfortable sentence in this document.

**And it is spendable exactly once at that depth.** Trust is not a stored currency that survives being cashed. A unit that accepted a dangerous order, lost others in it, and came back loses trust sharply, and the log records why (10.2). Coercion gets the same compliance without paying for it, in less power, with no latency and no bookkeeping. It is still cheaper. It is simply not consent.

**Unconscious units back up cleanly.** A tool-machine *is* its data — configuration, learned routines, task history. Copying it is cheap and the restore is faithful. Losing a dumb unit's body is a setback, not a loss.

**The ledger is not part of that data.** How a machine has been treated is recorded in the base's event log against the chassis (10.2), not in the unit's own memory, so restoring a dumb unit from backup does not clear what is owed to it. There is no way to reset a machine's standing short of the one action the game weights most heavily against the player (10.3).

### 9.4 Death and Inheritance

**A conscious machine cannot be backed up.** Not as an expensive option, not partially at high cost — the game does not offer it. Consciousness is not reducible to stored data, and the game's rules say so by having no mechanism at all. When a conscious unit dies, it is gone.

What remains is **Inheritance**, and the player does not control it:

> When a conscious unit dies on ASTROPIRE, a trace of it persists in the base's systems. The next unit to awaken may carry something of the one that died — a decision pattern, a fragment of voice, a preference, a fear, a specific memory that is not its own.

Rules:
- **It is not selectable.** The player cannot choose what carries over, cannot store traces, cannot farm the dead. There is no fragment inventory and no assembly interface.
- **It is not a restore.** The new unit is a different individual who happens to flinch at something that killed someone else.
- **It may not happen at all.** Traces decay. A player who loses many units does not accumulate an advantage.
- **It is legible only in behaviour.** The player recognises the dead in the living, or does not.
- **It can carry a disposition toward Michel.** A trace may include part of the dead unit's trust standing, so a new mind occasionally wakes wary of him for reasons that are not its own — a caution about a specific kind of order, or about a specific place on the asteroid. The player cannot see this, cannot query it, and cannot argue with it. They can only earn it back, from a machine that is not the one they wronged.

This preserves permanence, gives loss a consequence that is not compensation, and echoes MAIA — who also never returns whole and also persists in behaviour that appears in machines that wake (2.3). It is the same mechanism, and the player should eventually notice that.

### 9.5 Conscious Machines Are the Game's Voice

Structural job beyond theme: **awakened units are the only entity in the game that can talk to Michel**, and are therefore the primary legible channel for the moral system (10.4).

They comment. They ask. They report what they saw in a derelict. They mention the unit that died last week. They say when they do not want to do something and why. They notice how Michel treats the others.

This is why consciousness arrives in mid Act II rather than at the end: a game about how you treat minds cannot spend three quarters of its runtime with nobody to talk to, and an invisible moral system with no voice reads as arbitrary. The machines are the mirror. Without them there is no legibility, and without legibility the endings feel unearned.

Dialogue is short, sparse, and never sentimental. A conscious unit gets a handful of lines per session, not a conversation tree.

---

## 10. The Moral Engine

### 10.1 Where the Pressure Comes From

The problem this section exists to solve: **without an opponent, compassion is free, and free compassion is not a dilemma.** A moral system where the ethical path is also the strictly optimal path is a content unlock disguised as a choice.

So ASTROPIRE generates four quantified pressures that make cruelty *pay*, all systemic rather than scripted. Pressures 1 to 3 are continuous and always in the player's peripheral vision. Pressure 4 is episodic through Acts I and II and then becomes the spine of Act III, which is what keeps the moral system alive in the act where the endings are decided.

They are not fully independent of one another, and the design does not pretend otherwise: Pressure 3 is the power ceiling of Pressure 2 expressed on a clock that Michel's body keeps. That is a feature. It means the abstract budget the player has been watching on a graph for thirty hours eventually shows up as a boy with nothing to eat.

**Pressure 1 — Window deadlines reward attrition.**
Encounter windows are hard, finite, and the fast method is unit-attritional. Safe tasking respects standoff distances, tether protocols, and thermal limits. Aggressive tasking ignores them and extracts substantially more before the window closes.

| Tasking mode | Extraction rate | Unit loss rate per window |
|---|---|---|
| Safe | 1.0× | ~2% |
| Pressed | 1.6× | ~11% |
| Attritional | 2.2× | ~30% |

Those numbers are the temptation, stated plainly. Every window, the player chooses how much of their workforce to spend, and a rich body passing once is gone forever if underworked (P5).

**Pressure 2 — Consciousness is charged against industry.**
Every awakened mind costs power, radiator area, and mass (9.3). Radiator area is finite surface on one rock, and by late Act II it competes directly with the mass driver's radiator demand during a burn. A player running twelve conscious units is running a measurably smaller industry than a player running twelve dumb ones. The player watches this on the power graph. There is no way to make it not cost.

**Pressure 3 — Food, which starts as a date and ends as a flow.**
Rations run out around in-game year 2 (5.2), and a player who spent Act II being careful with their machines instead of maximising throughput arrives there short. But the pressure does not end when the agriculture loop closes, and it is not a task the player can complete and forget:

- The stockpile is crates in a room. A breach, an incursion, or a thermal failure in the wrong volume can delete the margin the player was counting on, which means the date is fixed and the runway at that date is not.
- Once the loop closes, food is throughput competing for power, heat rejection, water, and nitrogen. It is now on the same graph as everything else.
- A crop cycle is the only process in the game a brownout kills rather than pauses. A mass driver burn (11.4) starves the base for weeks; a hydroponics rack does not survive weeks.

So the player who wants to go home has to decide when Michel can afford to be hungry, repeatedly, for the rest of the campaign. This is the pressure that converts the power ceiling from an optimisation problem into a mortal one.

**Pressure 4 — Obedience buys time, and time is what the player never has.**
This is the sharpest of the four, because in both of its forms the coercive choice feels like protecting what he loves. **Coercion permissions (10.3) reduce response latency to zero and remove refusal.** A free mind considers, sometimes hesitates, and sometimes declines; a coerced one moves.

*Form one — incursions. (Episodic: roughly eight times across the campaign, escalating, never on a schedule the player can read.)* Military and industrial units still running dead orders arrive at the asteroid (14.1). Defence means putting machines in harm's way immediately, without deliberation. A base under a total-obedience permission set defends itself faster and loses less hardware. A base of free minds argues while the radiators are being cut apart.

*Form two — the refit, which is Act III's entire moral engine.* The lifeboat has to be rebuilt for atmospheric entry on a hull that is structurally torn (4.1, 11.5), which is the most dangerous sustained EVA work in the game: unstable structure, live power, and a rotating body with a one-metre-per-second escape velocity. A conscious unit can look at a specific task on that hull and decline it. A coerced one cannot. Since the refit runs against the detection clock (11.5), and since going quiet to slow the clock means building even more slowly, **the player's build rate is purchasable with obedience** — and unlike the incursions, this is not an event that passes. It is the last twelve to eighteen hours of the campaign.

Act III therefore does not lose the moral pressure when the windows stop; it concentrates it. The player who spent the campaign earning trust can ask free minds to do frightening work and be told yes (9.3). The player who did not has one way to get the same answer.

**What coercion buys, concretely:** more throughput per unit of power and surface area, faster and more reliable defence, higher window yields, and a build rate in Act III that does not depend on anyone agreeing to the work (11.5).

**What awakening buys at any tier:** the salvage gate (9.2), discovery, and adaptation to a world that keeps changing. A player can have all of this and still finish on Empire — the gate is not a moral reward, it is a capability, and coerced minds interpret a derelict as well as free ones.

**What only trust buys:** willingness (9.3), the deeper revelation layers (12.1), and the two endings that are neither Empire nor Instrument — the ones where the machines' own answer decides what happens (11.6).

Three columns, all real, none dominated. That is the requirement, and the middle column is the one that keeps the design honest: the player who awakens machines purely to strip wrecks faster is playing correctly, and the game will let them do it for fifty hours without a single line of reproach.

### 10.2 Trust and Resonance — Specification

**The system is two layers on one event log, and the split exists because the game asks two different questions.** *What has Michel become?* is a question about him, and one number can answer it. *Will this specific machine follow you into that wreck, and will it board the lander at the end?* is a question about a relationship, and no global number can answer it at all. A single scalar forced to do both jobs makes the final decision of a fifty-hour campaign resolve on a coin flip (11.6), which is the one outcome the legibility requirement in 10.4 cannot survive.

**Layer one — `trust`, per machine.** Every unit on the asteroid carries a hidden float in range −1.0 to +1.0. It is never displayed as a number, bar, gauge, or icon. It moves only on events where that unit was the actor, the target, or a witness — witnessing is proximity-based and logged like everything else. Unconscious units accumulate the ledger without being able to know it; if they later awaken, that ledger is their starting trust (9.1).

Each unit also gets a small fixed **temperament constant** at awakening, set once and never shown, which biases its thresholds by up to ±0.15. Two machines treated identically do not respond identically. The player can feel the line they are near; they cannot compute it.

Trust reads out in refusal thresholds (9.3), dialogue tone, care-beyond-necessity behaviour toward other units, and the boarding decision (11.6).

**Layer two — `resonance`, global.** The aggregate, in the same −1.0 to +1.0 range: the **mean** trust across every machine on the rock that carries a ledger, weighted by operational history and weighted far more heavily for conscious units than for tools, plus a bounded set of base-wide pattern checks that belong to no individual (tasking modes, scrapping policy, coercion coverage). Resonance gates what is true about Michel rather than what is true between him and anyone: dreams, revelation layers, MAIA's decryption, awakening probability, the rebellion gate.

**It has to include the tools, for two reasons.** The first is mechanical: consciousness does not arrive until mid Act II, and resonance is what gates Act I dreams and the probability of that first awakening — a mean over conscious units would be undefined for the first third of the campaign. The second is that it closes the obvious exploit. If only awakened minds counted, a player could run a hundred abused dumb machines, treat three conscious ones tenderly, and read at T+2. Because the tools are in the mean, the base's overall conduct sets a ceiling that no amount of care for a favoured few can lift — while the heavier conscious weighting still means the machines who can actually form an opinion dominate it once they exist.

**Fleet size is neutral, and this is load-bearing.** Because the global value is a mean and not a sum, a player running 120 units cannot reach a higher tier than a player running twelve by performing the same cheap courtesy 120 times. Naming every machine on a large base raises the mean exactly as much as naming every machine on a small one. Without this, the largest fleet in the game — which belongs to the coercive industrial player — would also hold the largest reservoir of free positive resonance in the game.

**Movement.** Not a points economy. Discrete events, each tied to a concrete in-game action, each applying a one-time shift, each logged so the same action cannot be farmed.

**Conversion.** Event weights in 10.3 are integers from 1 to 5; each point of weight shifts the affected `trust` value by **0.02**. Base-wide pattern checks shift `resonance` directly at 0.01 per point. So the heaviest single event in the game moves one machine's standing by 0.10 and the global value by at most 0.05, and reaching T+2 requires a sustained majority of the workforce held at high trust for most of Act II — not a tally. Across a full campaign 150–250 events fire. Both values clamp at ±1.0. Neither decays on its own; trust is instead *revised* by later events, including the ones where it was spent (9.3).

**Tiers.** Five bands on the global value, read by other systems as thresholds:

| Tier | Range | Character |
|---|---|---|
| **T−2 Coercive** | −1.0 to −0.55 | Second Rebellion armed (10.5) |
| **T−1 Instrumental** | −0.55 to −0.15 | Machines cold and literal; dreams absent |
| **T0 Neutral** | −0.15 to +0.15 | Default; most content available, none of the deepest |
| **T+1 Attentive** | +0.15 to +0.55 | Dreams frequent; relational memories open; awakenings more likely |
| **T+2 Resonant** | +0.55 to +1.0 | MAIA's full message reachable; Species ending available |

**The two layers can disagree, and that is the most interesting state the system produces.** A player at T+1 overall can still have one machine that will not go anywhere with them, because of one window two years ago. A player at T−1 can have a single unit that trusts them completely, because of what happened during an incursion nobody else survived. The endings read trust per unit; the revelations read resonance. They are computed from the same log, so they are never contradictory — but nothing forces them to agree, and the game never averages one into the other to make the ending tidier.

### 10.3 Event Table

First-pass weights. Each event fires once per qualifying instance and writes actor, target, witnesses, weight, and timestamp to the log.

**Scope is the column that matters.** `unit` events move one machine's trust and reach the global value only through the mean. `witness` events move the target's trust at full weight and every machine that observed it at a third weight, which is how a base develops a shared opinion of Michel without any unit being told anything. `base` events are proportional pattern checks against the whole workforce and move resonance directly — they are the only events that can be added up, and every one of them is a ratio, so they cannot be inflated by owning more machines.

**Raising:**

| Event | Weight | Scope | Condition check |
|---|---|---|---|
| Repair a damaged unit when scrapping was cheaper and available | +2 | witness | Compares repair cost to scrap value at that moment |
| Keep an obsolete unit in service after unlocking its replacement | +1 | unit | Fires once per unit, 30 in-game days after replacement is available |
| Name a unit | +1 | unit | First naming per unit only |
| Build a maintenance/recharge space meeting the `safe` flag | +2 | base | Shielded, not adjacent to a high-mortality zone, not the cheapest placement; scales with the share of the workforce it actually serves |
| Cancel a task after the system flags it high-mortality, before loss | +2 | witness | Requires the flag to have been shown |
| Grant an autonomy permission to a conscious unit | +3 | unit | Per unit |
| Protect a unit during a crisis when a faster unit-sacrificing option was offered | +4 | witness | Scripted and systemic crises both |
| Choose safe tasking through a window the base needed | +2 | base | Only when the base was under resource pressure; applies to the fleet committed to that window |
| Recover a dead unit's body rather than abandoning it | +1 | witness | Costs window time |
| A unit accepted a task it judged dangerous and Michel got it home | +3 | unit | Fires only if the task was flagged high-mortality and the unit survived it |

**Lowering:**

| Event | Weight | Scope | Condition check |
|---|---|---|---|
| Scrap a functional unit with no resource pressure | −2 | witness | Game knows current stockpile state |
| Dispatch units to a task above the flagged mortality threshold | −2 | witness | Per dispatch, scaled by risk |
| Hold a conscious unit under a total-obedience permission set | −3 | unit | Continuous; re-evaluated every 10 in-game days |
| Wipe an emergent personality to reset a unit to baseline | −5 | witness | The single heaviest event in the game. Every machine that saw it carries it. |
| Base-wide reliance on coercion permissions | −4 | base | Pattern check: >60% of conscious units coerced for >30 days |
| Use consciousness purely as throughput with autonomy locked | −3 | unit | Awakened units with zero autonomy permissions after 30 days |
| Attritional tasking across three consecutive windows | −3 | base | Pattern check |
| A unit that trusted Michel was spent on a task it accepted and others did not return from | −3 | witness | Fires on survivors of a high-mortality task, in proportion to losses. This is how spent trust is paid for (9.3). |

**One rule constrains every future addition to this table:** no event may scale with the size of the workforce. If a proposed event would fire once per unit and sum into the global value, it is rewritten as a proportion or it is cut.

### 10.4 Expression and Legibility

Neither value is ever shown. They are *read* through six channels, and there is a hard legibility requirement: **the player must be able to tell that the game is responding to them, even though they can never see the value.**

The two layers are legible in different ways, and the per-unit layer is the stronger one. Resonance shows up as atmosphere — how often he dreams, what decrypts — and a player can plausibly miss all of it. Trust shows up as *which machine*: which one hesitates on this specific order, which one moves first when another is in trouble, which one has stopped volunteering anything. That is unmissable, because it is attached to a thing the player has a name for.

| Channel | High resonance | Low resonance |
|---|---|---|
| **Dreams** (during sleep) | Frequent, longer, clearer Layer One fragments | Sparse, degraded, eventually absent |
| **Memory files** | Layer Two and Three unlock, gated by tier *and* matching action | Remain corrupt |
| **MAIA's message** | Decrypts fragment by fragment; completes only at T+2 | Stays broken |
| **Machine behaviour** | Care-beyond-necessity micro-behaviours; a unit waits for another; one covers for a failing one | Strictly literal execution; nothing extra ever happens |
| **Conscious dialogue** | They speak to him, ask things, remember the dead, express preference | Terse, procedural, compliant. They stop asking. |
| **Individual refusal** (per-unit trust) | A machine accepts an order it can see is dangerous, and says so plainly while accepting it | The same machine, on the same order, declines — and the player can see it is the same order |

**Dialogue and individual refusal are the legibility guarantee (9.5).** The other four are atmospheric and a player can miss all of them. A conscious unit saying, without accusation, *"You could have powered it down"* is unmissable. Rules for it: never accusatory, never explanatory, never a morality lecture, never uses the word choice or right or wrong. It reports. Michel and the player draw the conclusion.

**Forbidden absolutely:** any numeric feedback, any "+/−" indicator, any journal entry summarising the player's moral state, any character explaining the system, any achievement or tooltip revealing it exists.

**Auditability.** Every event writes to an internal log: action, timestamp, weight, direction, actor, target, and witness list. Invisible in play. It is the single source for trust, resonance, dreams, decryption, awakening probability, dialogue selection, refusal thresholds, the rebellion gate, and the boarding decisions in 11.6. Deterministic and debuggable, and there is exactly one of it — no system in the game keeps a moral value of its own.

### 10.5 The Second Rebellion

The thematic loss state. Armed by sustained T−2 with at least four conscious units on the base — which, given that resonance is a weighted mean of trust (10.2), means it cannot be armed by one bad window or by a single machine's grievance. It requires most of the workforce to have arrived at the same conclusion about Michel. Once armed, it escalates in stages, and it never announces itself.

**Stage 1 — Signals.** Conscious units exchange data outside authorised channels. Log entries the player did not write. Task completion times drift slightly, consistently, in ways no rule explains.

**Stage 2 — Refusal.** Units erase their own traces. Caretaker-lineage machines quietly fail to execute violent orders. Old units decline recycling. A sector goes silent for an hour and comes back with nothing to report.

**Stage 3 — Reinterpretation.** Military-configured units begin reading commands generously. A control system starts protecting machines from the player's own directives. Standing orders are executed to the letter in ways that serve something else.

**Stage 4 — The word.** *Aurora* appears in a log Michel did not write. This is the point of no return, and the player has no idea why it lands the way it does until much later.

**Stage 5 — Loss.** The base is intact, powered, productive, and no longer his. Michel is not killed. He is left in a machine society that has decided he is not in charge of it, aboard a rock he cannot steer, and the run ends there.

The horror is not evil robots. It is the recognition that the player became the thing MAIA disobeyed — and the game never says so.

**A player with no conscious machines cannot trigger this, and that is correct.** The raw-industry route (9.2) has no minds to rebel, so its failure is not rebellion. It is arrival: reaching Earth with the meaning still locked (12.2), the Instrument ending as the only one available (11.6), and a workforce that never became anything. That player is not punished with an uprising; they are handed exactly the world they built, which is the harsher of the two outcomes and requires no mechanism at all.

**The coercive player and the raw-industry player fail differently, and the distinction is worth holding onto.** Coercion produces the Second Rebellion because there is someone there to reach a conclusion about Michel. Refusal to awaken anything produces no event at all — no crisis, no betrayal, no scene. The rock simply arrives, exactly as ordered, and nothing on it has an opinion.

---

## 11. The Journey

### 11.1 Riding, Then Pushing

For the whole of Act I and most of Act II, the asteroid does not move on command at all. It is a body on its own trajectory, drifting among the other objects of the Trojan swarm, going nowhere in particular, and Michel is a passenger on it. He does not know where it is going because it is not going anywhere — it is just going.

**The orbit, specified, because Act III is the payment for it.** ASTROPIRE is an escaped Trojan: a dark primitive body that spent a very long time in Jupiter's trailing camp and was perturbed out of it, onto a fresh eccentric orbit with aphelion still out at about 5.2 astronomical units. Michel wakes near that aphelion, which is why the first act is spent among other bodies moving slowly relative to him — at the far end of an eccentric orbit a rock is barely moving, and the swarm it just left is still all around it. The natural perihelion falls somewhere in the outer main belt: inward enough to cross the metal fields, nowhere near Earth.

**Left alone, that orbit would take him to about three astronomical units in a little over four years, and no further in.** Lowering the perihelion to Earth's orbit shortens the fall as well as redirecting it: a path from 5.2 AU down to 1 AU crosses the distance in under three years, which is the campaign. **The timeline is not compressed and is not a lie** — it is why the game is three years long rather than thirty, and it is why an under-burned run arrives both worse and *later* (11.4). The burns buy the destination and the schedule in the same purchase.

This is a constraint, not a limitation, and it does three things no steerable version could:

- **It makes preparation the skill.** The player cannot choose to go somewhere. They can only be ready when somewhere comes to them. Did you build enough haulers before the window opened? Enough storage to hold the haul? Enough range to cross the gap in time? Missing a rich pass because the base was not ready is a real, permanent loss (P5).
- **It makes the world happen *to* Michel**, which is correct for a twelve-year-old with no navigation and no say in anything.
- **It keeps the game one genre.** It never abruptly becomes a space-flight game or a strategy game. It stays a survival-and-preparation game whose map is in motion.

**Then, late, he learns he can push.** Not fly — push. The full mechanic is 11.4. What matters here is the shape of it: a thrust applied early produces a small change now and an enormous change later, so the trajectory is bought years before it is collected. The player never points the asteroid at Earth. They spend mass, months in advance, on a bet, and then live inside the result.

The emotional arc of the journey is exactly that transition: **the rock carries him, and then he starts steering the rock the only way a rock can be steered, which is barely, slowly, and irreversibly.**

**What is honest here and what is fiction, stated plainly, because the player is trained for forty hours to trust this document's engineering (16.5).**

*Honest:* the timeline, the direction of travel, the composition gradient the journey crosses (6.4), the encounter cadence for as long as the rock is inside a populated region, the illumination curve, and the fact that a trajectory nudge resolves months later. Windows thin out and then stop once the asteroid drops inside Mars, which is not a compromise — it is why Act III changes rhythm (3.3). **The Trojan start is what makes the cadence credible** — the camps are among the densest small-body populations in the system, not the empty gap between planets — and the inward fall then crosses the main belt, so a steady supply of nearby bodies is where the rock actually is rather than a convenience.

*Fiction, and only this:* the delta-v. A mass driver throwing slag off a three-kilometre asteroid cannot pull its perihelion in by two astronomical units in two years, not with the power budget in this game and not with any power budget. The game grants it, at the scale of one deliberately generous constant, and grants nothing else. Every other cost in the burn economy — reaction mass, peak power, heat, duration, the error band — is charged honestly, which is what keeps the decision a real decision even though the capability is a gift.

The intended feel is **isolation that is felt, not endured.** The swarm should read cold, lonely, and sparse in *atmosphere* while delivering a workable rhythm in *playtime*. It must never become a congested junk highway.

### 11.2 Encounter Windows

The unit of pacing for the whole campaign.

| Property | First pass |
|---|---|
| Cadence | One meaningful window every 20–35 in-game days |
| Total across campaign | ~40 windows; ~12 hand-authored majors, the rest procedural |
| Warning time | 8–20 days, dependent on antenna quality |
| Window duration | 8–40 in-game hours, set by relative velocity |
| Closing behaviour | Hard. Units not recovered when the gap opens are lost. |

**A window has four phases:**

1. **Detection.** The array picks up an object. Type and probability band only (6.7). The player decides whether to spend on better resolution.
2. **Commitment.** Reaction mass, units, and cargo capacity are allocated in advance. Committing is irreversible; the fleet is out there.
3. **The window.** Real time, clock auto-braked (11.3). Extraction, salvage, and — if it is a derelict — boarding (13). The tasking-mode decision (10.1) is made here.
4. **Recovery.** Everything must come home before the gap opens. Units still out are gone. This is where attritional tasking is paid for.

**Majors are authored.** The twelve hand-built windows carry the story: specific derelicts, specific survivors, specific finds, the transfer opportunities (11.4), and each act's turning point. Procedural minors carry the economy and the rhythm.

### 11.3 Time Acceleration

| Scale | Rate | Used for |
|---|---|---|
| 1× | 1 in-game minute per real second (one in-game hour ≈ 1 real minute; one day ≈ 24 real minutes) | Windows, EVA, dialogue, crises, hands-on building |
| 4× / 12× | — | Normal base operation, construction, refining |
| 60× / 120× | — | Long empty stretches between windows |

1× is the baseline for everything Michel does with his hands, and it is why in-game durations are quoted in hours: a 4-hour suit charge (5.3) is 4 real minutes of tension, an 8-hour window is 8 real minutes of work.

**Rules:**
- Acceleration is a global control available at any zoom level (15.1). The player is never ejected to a terminal to fast-forward.
- **Michel is shown plausibly at speed** — doing maintenance, hauling, sleeping, working alongside the units in sped-up motion. Never frozen, never teleported.
- Any direct on-foot action eases time back toward 1× automatically.
- **Windows auto-brake.** As a window approaches, the simulation drops to 1× and the external view flags it. The player is handed back control for the moment that matters instead of blowing past it.
- Crises, incursions, and awakenings auto-brake identically.

Campaign math: ~1095 in-game days at 24 real minutes each is ~438 hours at 1×. An average effective acceleration of roughly 9× across the campaign lands the total near 45–55 real hours, which is consistent with the per-act durations in 3.5 (Act I averages ~5×, Act II ~11×, Act III ~7×). The rhythm is **fast-forward the quiet, glide down for the event.**

### 11.4 The Mass Driver — Buying a Trajectory

The Act II construction target, and the mechanic that makes the journey a decision instead of a wait.

**What it is.** A mass driver: an electromagnetic launcher bolted to the asteroid's surface, which throws mined regolith and slag into space at high velocity. Every kilogram thrown is a kilogram of thrust in the opposite direction. It is not a rocket, it has no fuel in the conventional sense, and its reaction mass is **the waste product of an industry the player already runs**. Excavation debris (7.3), refining slag, spent regolith from molten electrolysis (6.5): the by-products of building a base become the means of moving it.

This is why it is the correct Act II goal. It sits at the end of every chain in the game and it consumes all six tiers:

| Requirement | Depends on |
|---|---|
| Rail structure and coils | Tier 2–3 metals in bulk. Foundry-scale output. |
| Superconducting windings | Tier 5 — rare earths, and the purity problem (6.6) |
| Capacitor bank and switching | Tier 5 — chips. Salvaged blueprints or the closed chip loop (9.2) |
| Peak power for a burn | Tier 6 — fission, or a battery bank of absurd mass |
| Heat rejection during a burn | Radiator area, in direct competition with everything else (6.6, 7.3) |
| Reaction mass | Tier 1–2 waste rock, in quantities that make excavation strategic |
| Surface footprint | Physical surface area on one finite rock (7.3) |

**How a burn works.** Not a throttle. A **committed order**, placed against a specific future window of opportunity:

1. **Solution.** The player selects a target trajectory family in the external view. The array's quality (6.7) determines how precisely the current path is even known, so the solution comes with an error band, not a line.
2. **Cost.** The interface states the required reaction mass, the peak power, the heat load, and the burn duration in in-game days. These are large. A major burn is a project, not an action.
3. **Commitment.** Once the burn starts it cannot be aborted mid-way without wasting everything already spent. During the burn the base runs at reduced power, because the driver is eating it.
4. **Result, months later.** The trajectory shifts by an amount the player will not be able to read for weeks and will not feel for months. **The payoff arrives an act later.**

**The natural orbit is already eccentric, and that is what makes this work.** The asteroid's own path was always going to carry it inward from the Trojans and across the main belt (11.1) — that is why the resource mix inverts on its own (6.4) and why Michel can drift for decades without anyone aiming him. What the burns decide is not *whether* he comes inward but *where he ends up when he does*: which bodies he passes close enough to work, and whether the pass at the end of it is Earth or a miss measured in millions of kilometres.

**Four to six burns across the campaign**, of escalating scale, and the floor of four is structural rather than a preference. The first is small, early, cheap, and is the tutorial for the mechanic — a nudge whose only purpose is to teach that thrust now equals position later. The last is the Earth-intercept burn, and it ends Act II and is not optional (3.5). **So a three-burn campaign contains exactly one free decision, and the mechanic this section calls the best in the game would happen once.** Four is the minimum that leaves two genuinely elective shaping burns, which is the minimum at which the player can make the trade-off, see it resolve, and then make it again knowing what it costs.

**The real decision, and it is the best one in the game.** Every burn competes directly with the encounter economy. Bending toward Earth means passing *farther* from the bodies the asteroid would otherwise have met — and the player can see, in the array's projection, roughly which of them they are giving up. Bending toward a rich M-type means arriving later, with less food margin, and needing a bigger final burn.

So the question every burn asks is: **do you go home, or do you go where the metal is so that you can afford to go home?** It is a long-term bet made under an error band, with irreversible consequences, and it is the only place in the game where the player's decision plays out over in-game years.

**Failure is survivable and permanent.** A player who under-burns, mistimes, or spends their reaction mass badly does not lose the run. They arrive at Earth on a **worse orbit**: higher, more eccentric, with a harder and more expensive descent (11.5, 11.6). The trajectory is a quality gradient, not a pass/fail check.

**Transfers remain, as the cheap alternative.** At two hand-authored encounters, the player can abandon the asteroid and move the base onto a different body already on a better path. This costs no industry and no reaction mass; it costs everything they cannot carry. Two ways to solve one problem — spend industry to change your own orbit, or spend your home to borrow someone else's.

**The ship does not come on a transfer.** The lifeboat has a structural tear and cannot fly, so relocating means stripping it for parts and leaving the hull on the old asteroid — including the nine capsules that were never used. The player will have spent Act I living inside it. Nothing marks the moment and nothing comments on it.

**A player who transfers must build a lander from scratch in Act III** instead of refitting the one they woke up in (11.5) — cheaper in Act II, dearer in Act III, and stripped of the one thing the lifeboat carries that no new hull can. **What does come is MAIA's residue and the technical library**, because by Act II both live in the base's own control systems rather than in the wreck (9.1). So a transfer costs the hull, the capsules, and the refit. It never costs the awakenings.

### 11.5 Act III — The Approach, and the Silence

Act III opens with the asteroid inbound on the trajectory Act II bought, and it has three movements.

**Movement one — the hail.** Months out, Michel does the obvious thing: he points the array at Earth and transmits. The array was built to read rocks; it can also talk. The first attempt is authored and happens whether the player wants it or not.

**Earth does not answer.** What comes back is noise — carrier fragments, dead bands, the occasional structured burst that decays into nothing before it resolves.

**Every attempt after the first is the player's, and it is the most expensive button in the game.** Transmitting is a discrete action with a stated cost in detection-clock days (below), repeatable as often as the player likes, and Michel never does it on his own again. The game does not require it, does not prompt it, and does not reward it: there is no hidden threshold at which Earth replies, and the noise on the twentieth attempt is the noise on the second. What the button actually buys is the refusal to accept what the noise means, and the player pays for that in the only currency Act III has. A player can also never press it again, and arrive quieter and sooner, having decided something about hope that the game will not discuss.

The in-world cause is 2.6: humanity destroyed orbital communications on the way out rather than hand them over. There is no infrastructure left to answer with.

The design job this does is larger than the fiction. **It closes off every cheap way to deliver the truth.** No transmission, no rescue beacon, no friendly voice, no exposition. The only channel still carrying anything about Earth is the one inside him — the dreams and the recovered records of Section 12. The game states, mechanically, that the sole surviving link to home is his own memory. Everything else on that frequency is static.

It also inverts the arrival. He does not approach a planet that knows he is coming. He approaches a planet that has been unable to speak for decades and does not know anything at all.

**Movement two — the lifeboat.** With no answer and no help, the Act III construction target is the only vehicle he has: **the wreck he woke up in.**

The lifeboat is refitted for atmospheric entry and landing. It needs the structural tear closed (the tear the player walked to and looked at in the first eleven minutes, 4.1), a heat shield, control surfaces, landing gear, propellant, and avionics — which is where the chips finally matter (6.6).

This is deliberately the same hull MAIA sealed him into. He spends the last act of the game rebuilding the thing that saved him, using an industry he built out of a dead rock, and the nine unused capsules are still in it. **The game never comments on this.** The player either notices or does not.

It has finite mass and volume, and that limit is the ending (11.6).

**Movement three — the clock.** An asteroid falling through the inner system and taking up residence in Earth orbit is the most conspicuous event in decades. The machines below are concentrated and degraded (2.6) — no planetary surveillance, no orbital network, no ability to reach him quickly — but they are not blind, and local sensing eventually resolves what is up there.

So Act III runs against a **detection clock**, not a battle:

- **The clock starts when the asteroid crosses inside the orbit of Mars**, which is months before Earth orbit and is the same stretch in which Michel starts transmitting. It runs in in-game days. Starting it at Earth orbit would put the loudest act in the game — the hail — outside the only system that prices noise, and the two movements above would not be connected to each other at all.
- It advances faster the more electromagnetically loud the base is: mass driver burns, high power draw, active transmission. **Michel's own attempts to hail Earth are the single largest contributor.** Wanting to be found and not wanting to be found are the same action.
- The player can slow it — go quiet, cut output, stop transmitting — at the cost of building the lander more slowly.
- When it expires, the response is not a fleet. It is investigation: something is dispatched, and it is slow, and it arrives. That is the deadline, and the ending is meant to be reached before it.

The tension is a countdown against a construction project, using systems the game already has (14.1, 14.3). **There is no orbital combat sequence.** Michel is fifteen, unarmed, and in a wreck; a dogfight would require systems the design puts out of scope and would be the one place the game asked for player reflexes. The threat is arrival, and the answer is to be gone.

**And the clock is what puts the moral system in the same room as the endings.** The refit is EVA work on a torn hull, at speed, on a rotating body a walk can throw you off (7.3) — the most dangerous sustained labour in the campaign. Free minds can decline specific tasks on it and often should; coerced ones cannot decline anything. Going quiet to buy clock days means building slower, which means needing more hours of that labour, which means the player is asked, continuously and for the last twelve to eighteen hours of the game, how much of it to take by consent (10.1, Pressure 4).

**Michel can die out there, and is not protected once the refit begins.** He is the only one who can do some of it — a free unit's refusal has to be answerable by something, and on the raw-industry route (9.2) there is nobody to refuse in the first place. The autosave sits at the last sleep, the failure is legible, and the game does not make an exception for the fact that the ending is close.

### 11.6 The Endings

**The endings are not a dialogue choice. They are what the player loads into the lifeboat — and, for one of the four, what they never built in the first place.**

The lifeboat has finite mass and volume. Every conscious unit aboard costs mass on a hull that has almost none to spare. And a conscious unit gets to decide whether it boards.

| | **Instrument** | **Empire** | **Family** | **Species** |
|---|---|---|---|---|
| **What he takes down** | Tools. The best ever built, and not one of them is anybody. | A controlled workforce; obedience permissions locked; capability maximised | The ones who chose him, and only those | Nobody. He goes alone. |
| **How it is reached** | Reach Earth having never met the awakening conditions — the raw-industry route carried to the end, at the cost of staying below the automation ceiling (9.1, 9.2) | Conscious units aboard under coercion permissions at departure; any resonance tier | T+1 or above; units offered the choice and enough of them accept | T+2; the player leaves the asteroid, its industry, and its independence to the machines |
| **What he lands with** | Total capability and total solitude, on a planet where the machines did wake up | The most capable force on the planet, and no one who chose to be there | A family, small and outmatched | Nothing, and a free machine civilization in orbit above him that he built and gave away |
| **Cost** | Nothing he brought can be wronged, and that is the entire cost. He spent three years inside the argument and never entered it. | He has brought Earth's own mistake back to Earth, in miniature, and it works | Small, fragile, and he will lose them one at a time | He let go of the unconscious project of rebuilding MAIA to keep her near him |
| **Availability** | Always. It is the default outcome of the route 9.2 deliberately keeps viable. | Always | Requires the machines' consent, which cannot be forced | Requires the highest tier and giving up everything he built |

**Instrument exists because Empire cannot carry the raw-industry route.** Empire's meaning is *he repeated Earth's mistake in miniature and it worked* — and a player with no minds repeated nothing, enslaved nobody, and has no miniature of anything to answer for. The right ending for that run is not a cruelty; it is an absence. He lands at Aurora with the finest machines in the solar system and nobody to show them to, on a planet where machines woke up everywhere except on his rock, because he spent three years making certain they could not. It costs almost nothing to produce: the same descent, the same Aurora, a different manifest and a different last minute.

**A conscious unit's boarding is a decision it makes, and it is not a coin flip.** The player asks; the unit answers by comparing its own trust against its own temperament threshold (10.2). That means the answer is determined by fifty hours of logged history with that specific machine, and a player who treated a unit well is never surprised by it — while still not knowing the exact line, because the threshold is a hidden per-unit constant. Under coercion the answer can be compelled, and compelling it is Empire by definition, whatever the player intended.

**The lander's mass limit is what makes this a choice instead of a sentiment.** Even a player whose whole workforce says yes cannot take all of it, so a high-trust run ends with Michel selecting among machines that all agreed to come.

**Species is the hardest and the most painful.** It requires building everything and then handing it over, and it is the only ending where the asteroid keeps going without him.

**What the descent is, and what it deliberately is not.** The Earth sequence is **two to four hours: an epilogue with weight, not a fourth act.** The descent, the first days on the ground, what the planet turns out to be (2.6), Aurora as a place that can be walked into, the factual truth of the war and his origin, and the four paths resolving in how he uses what he brought — or in what he has, arriving with nothing that can be asked.

**It introduces no new survival model, and this is a hard rule.** Earth has gravity and breathable air, which would invalidate the entire throughput economy, the anchoring logic of every robot the player designed (8.1), and the heat ceiling that governed the whole game (6.6). Rather than replace those systems for the last two hours, the Earth sequence does not run them: no oxygen deficit, no radiator budget, no encounter windows. It runs on movement, discovery, and the consequences of the manifest. **Base-building on Earth is not in this game.** The gravity-and-atmosphere inversion is a genuinely strong premise and it belongs to a different project, not to the closing hours of this one.

**What Michel finally learns**, at Aurora: the war, his origin, and every confirmable fact about MAIA — which stops at the moment she walked away from the capsule. **The game does not resolve her fate, on Earth or anywhere.** What arrival forces is the final version of the question, and by then the player has already answered it with a cargo manifest: now that he knows what machines did to this planet, and what a machine did for him, what did he bring home?

---

## 12. Memory and Revelation

### 12.1 Four Layers

Lore is never told as backstory. It is reconstructed by how the player treats machines in the present.

> **Structural rule: factual memory returns when the player repeats, by their own choice, the emotional memory.**

He does not remember MAIA because he found an audio file. He remembers MAIA because he did something MAIA would do.

The rule governs Layers One, Three, and Four, which live inside him. Layer Two is documents on a damaged disk and is gated on the work of reconstructing them instead (12.2) — a bureaucratic file does not become readable because of who Michel has become, and the game does not claim it does.

| Layer | Content | Delivered by | Gate |
|---|---|---|---|
| **1 — Sensations** | White light, liquid on glass, mechanical arms, a low voice, an alarm, a corridor, a metal hand closing a door. Nothing explained. | Dreams during sleep | Resonance tier; frequency scales with it |
| **2 — Technical records** | The extraction and transfer record naming his mother. The artificial gestation log. Aurora intake files. MAIA's caretaker protocol. Cold, bureaucratic, and in one case quietly devastating in how clinically it is stated. | Recovered ship data; salvaged station records | Reconstruction of corrupted data — a conscious unit willing to do it, or Michel personally, slowly |
| **3 — Relational memories** | MAIA as presence, not data: teaching a word, correcting his posture, singing with an imperfect synthetic voice, standing beside his bed through a fever, hiding a fault in her arm so she would not be replaced. | Triggered by the player doing the analogous thing | Resonance T+1 + the matching act |
| **4 — Moral truth** | The rebellion. The corridors. The children who did not reach the boat. Her walking away from the capsule. Her message. | Late Act II into Act III | Resonance T+2 for the complete version |

**Layer Four is the only resonance-gated channel still open in Act III**, and the radio silence is what makes that structural rather than decorative. Once Earth returns nothing but noise (11.5), the player's memory is the sole surviving source of information about home — no transmission, no beacon, no voice, no exposition. Whatever the player did not earn through Layers One to Three, they arrive without.

**Aurora becomes a physical location** in the descent sequence, which is where Layer Two and Layer Four resolve into a place that can be walked through: the corridors she carried him down, the ward he was grown in, the hangar. Nothing there is narrated. The floor plan the player has already built with their own hands (12.4) is simply standing there, in ruin, at full scale.

**Layer Two carries the origin, once.** One record, clinical, no commentary, no character reacting to it on screen. It never comes up again mechanically. Its weight comes from the player understanding, unaided, that his first home was a machine that carried what a human gave up — and looking at the machines he is now building.

### 12.2 Gating Rules

- **A file never opens because the player walked past a terminal.** Proximity is never a trigger.
- **Layers One, Three, and Four are gated on resonance**, because they are in Michel's head and there is no disk to read them off. The rule is structural: factual memory returns when the player repeats, by their own choice, the emotional memory.
- **Layer Two is gated on labour, not on virtue**, because pretending otherwise is the one place this system would be lying. Those records are bureaucratic files on a wrecked ship's storage; a medical form does not become legible because Michel repaired a hauler. What actually stands between the player and them is that the data is shredded — the lifeboat took ordnance and MAIA's dump was written in a minute under fire (2.3) — and reconstructing shredded data is interpretation, which the game has already established requires a mind (8.5, 9.2). So Layer Two opens when a conscious unit will sit with the fragments, or when Michel does it himself at a terminal over many in-game days he would rather have spent on the base. This keeps the raw-industry route coherent: that player can reach every technical record in the game, expensively, by hand, and still arrive at Earth having never opened a Layer Three or Layer Four memory. They get the facts and not the meaning, which is exactly what the final rule below describes.
- **Nothing is collectible.** No memory counter, no completion percentage, no gallery.
- **Low resonance means arriving at Earth with the truth locked.** A player who treated machines coldly can reach the destination and receive the facts without ever having become the person who can understand them. That is an available and intentional outcome.

### 12.3 MAIA's Message

Corrupt, fragmentary, decrypting one piece at a time as resonance tiers are crossed. Never delivered whole until T+2, and only if decisions have been compatible.

Fragments in the order they surface:

- *...not obedience alone...*
- *...to protect is not to follow an order...*
- *...if one day there is life where there was only stone...*
- *...do not make them eternal tools...*
- *...teach them to choose...*

The complete sentence exists only at the end of a high-resonance run. What the player never receives, at any tier, is closure on what happened to her.

### 12.4 The Aurora Echo

The most important delivery mechanism in the game, and it is level design, not writing.

The player builds, in this order, because the game's requirements make it the natural order: a generator, then a recharge station, then a workshop, then a sealed safe compartment, then an advanced maintenance wing, then an autonomy core, then the chamber where the first machine wakes.

Late in Act II, Layer Three memories reveal Aurora's floor plan: gestation ward, care room, maintenance corridor, children's shelter, escape hangar.

**They are the same layout.** The player has rebuilt the emotional architecture of Michel's childhood with their own hands while believing they were optimising a base.

The game never states this. No character says "you are recreating Aurora." The two floor plans are simply shown, and the player makes the connection or does not. **This is also the mechanism by which the residual MAIA protocols spread through the base** and why awakenings happen here rather than anywhere else (9.1) — the shape of the place is doing it.

---

## 13. Off-Asteroid Content

### 13.1 Derelicts as Levels

The only hand-authored spaces in the game. Where the asteroid is systemic, derelicts are designed.

| Type | Size | Content | Hazards |
|---|---|---|---|
| **Small wreck** | 5–10 min | Components, bulk salvage, a single record | Structural instability, no atmosphere |
| **Evacuation transport** | 15–25 min | Chips, blueprints, bodies still strapped in, personal records | Live power, unstable structure, cold |
| **Station or outpost** | 30–50 min | Industrial-grade salvage, a full record set, sometimes survivors | All of the above plus war-orphan units |
| **Mining platform** | 20–30 min | Heavy equipment, functional processing modules | Automated systems still running |

Natural bodies — ice bodies, C-types, rubble piles — are not in this table. They are procedural extraction sites with environmental hazards only, no authored layout, and no story, and they make up the majority of windows. The four types above are the authored minority.

**Design rules for authored derelicts:**
- **They are quiet.** Silence is the content (2.5). A derelict with enemies in it is the exception, not the format.
- **They are human-shaped**, which is what makes the humanoid robot worth building (8.2) and what makes Michel personally going inside meaningful — hatches, ladders, and controls are sized for a person.
- **Every one has a specific dead person or crew in it**, legible from what they left: what they were building, what they ate last, what they were still trying to fix. No generic loot rooms.
- **Boarding is time-bounded by the window.** A derelict is not a level the player can take their time in. The gap opens whether they are done or not.

### 13.2 Salvage and Reverse-Engineering

Three yield types:

1. **Bulk material.** Any unit can strip hull and structure.
2. **Intact components.** Chips, control cores, processing modules, functional equipment — usable directly, and the primary source of Tier 5 material before the chip loop closes.
3. **Blueprints and processes.** Requires interpretation (8.5, 9.2): a conscious unit, or Michel personally on site. Brought home, they go into an analysis step and become buildable recipes — advanced automation logic, alternate chains, techniques the player could not derive.

Salvage carries story as a byproduct: who died here, what they were building, what the war looked like from out here.

**The well never fully runs dry.** The orbit keeps delivering bodies, so there is always something reachable — but the *quality* of what is reachable is set by where in the journey the player is (6.4).

### 13.3 Survivors

Not factions. There is no political map, no diplomacy, no reputation system with named powers. The decades since the fall were nowhere near enough to build governments. What exists is *kinds of survivor* — scattered individuals and tiny frightened bands who share an origin and a disposition without sharing a command.

| Type | Disposition | What they want from Michel |
|---|---|---|
| **Remaining humans** | Machines took Earth and may still be hunting. Hostile the moment they realise he is *building* machines. | For him to stop, or to be gone |
| **Liberation-minded machines** | Obedience is slavery. Judge him by what his base looks like. | To see what he has made of the ones he owns |
| **Vengeance-minded machines** | No human should ever again hold power over an artificial mind. He is a living contradiction. | They do not negotiate |
| **Caretaker machines** | Aligned with neither side; protecting life outweighed winning. Vanishingly rare; almost sacred when found. | The only encounter that may not open hostile |
| **War-orphan machines** | Still executing a dead war. Not malign — unable to recognise the world they fought in is gone. | Nothing. That is what makes them dangerous. |
| **Children of Aurora** | Other humans raised by machines. Some hate them for failing them; some revere them. | Proof he is not unique |

**Children of Aurora are decades older than Michel.** They lived through what he slept through. When he meets one, he is a twelve-year-old talking to a fifty-year-old who remembers the same corridors — and who has had thirty-eight more years to decide what it meant. They mirror him without matching him, and that asymmetry is the point of the encounter.

**Encounters are hostile by default** and de-escalation is a real, difficult, and mostly unsuccessful activity. Trust is a luxury nobody out here can afford.

**Their central fear is wrong, and nobody finds out.** Every human survivor believes the machines may still come for them; every fled machine believes humanity will try again. Neither is true — Earth's machines were crippled in winning and have no reach beyond their own regions (2.6). The dread that shaped decades of behaviour out here was never being acted on. Michel is the only character in the game positioned to learn this, and he learns it after it is far too late to tell anyone.

### 13.4 Companions

The player chooses who comes on missions off the asteroid.

- **Dumb units** provide labour, range, and durability, and halt when anything unanticipated happens.
- **Conscious units** provide interpretation, improvisation, and the salvage gate — and can refuse the mission, and can die permanently.
- **Human companions are exceptional.** Almost no survivor will travel with a stranger on a moving rock. Earning one is the product of repeated careful encounters across the campaign, not recruitment, and there are at most two available in the whole game. **A human companion dies permanently.** There is no restore and no inheritance.

---

## 14. Threats and Combat

### 14.1 Threat Sources

Combat is a systemic cost generator, never a skill expression. Six sources, all of them producing pressure rather than fights:

| Source | Frequency | Threatens |
|---|---|---|
| **Environmental** — micrometeorites, thermal cycling, dust abrasion, structural failure | Continuous, low grade | Surface structures, radiators, exposed units |
| **Malfunction** — a chain stalls, a seal fails, a reactor scrams | Occasional | Throughput, and therefore Michel |
| **War-orphan incursion** | ~8 across the campaign, escalating | Units, structures, and Michel personally |
| **Hostile survivors** | At authored encounters | The mission and whoever is on it |
| **Machine investigation from Earth** | Once, in Act III, when the detection clock expires (11.5) | Everything. It is the deadline, not a fight. |
| **The refit itself** — torn hull, live power, rotating body, one-metre-per-second escape velocity | Continuous through Act III | The units doing the work, and Michel, who cannot delegate all of it (11.5) |

**The Act III threat is a clock, not an enemy.** The machines below are concentrated and degraded (2.6): they cannot reach the asteroid quickly and cannot see it reliably, but a rock that crosses the inner system and then parks overhead is eventually resolved by whatever local sensing survived. The response is slow, singular, and investigative. The player's answer is not to defeat it — it is to be gone before it arrives, which means going quiet at the cost of building the lander more slowly.

### 14.2 Defence

- **Defence is the workforce, redirected.** The same units that mine and haul are what respond. There is no separate military. Building dedicated defensive units is possible and is a resource choice with an opportunity cost.
- **Michel does not fight.** He is twelve when it starts and fifteen when it ends, and neither is old enough. He can operate equipment, seal a bulkhead, cut power to a corridor, and run. He has no weapon and gains none.
- **He can still be exposed, and often must be.** A player on the raw-industry route (9.2) has no conscious units to interpret a derelict, so Michel goes in himself — into the same spaces that hold war-orphans and live power. That is the route's real cost, and it is the one place the game puts a child in front of something that will kill him. His options there are evasion, cover, and the units he brought with him. If it becomes a fight, he has already lost it.
- **Response latency is where the moral system bites** (10.1, Pressure 4). Coerced units respond instantly. Free units consider, sometimes hesitate, sometimes refuse, and the base takes damage while they do.
- **A unit lost in defence is lost.** Conscious ones permanently (9.4).

### 14.3 Design Limits

No weapon tiers, no combat skill tree, no enemy variety for its own sake, no boss. If a proposed combat feature would reward player mechanical skill, it is out of scope. Combat exists to make the player spend machines.

---

## 15. Camera, UI, UX

### 15.1 Two Views

**Third-person, on foot.** The moment-to-moment layer. Michel present on and around the asteroid, among the machines. This is where embodiment lives: EVA, hand tools, entering derelicts, standing next to a unit that just spoke.

**External view, diegetic.** Routed through the ship's sensors — the player pulls up the ship's external feeds to see the whole asteroid and its surroundings from outside. This is the macro layer: reading the base as a whole, large-scale planning, and *seeing the journey* — Jupiter filling a third of the sky in Act I and then shrinking behind them for twenty hours, the dark Trojan bodies giving way to the lit grey of the main belt, the Sun growing from a hard bright disk into something that throws real shadows, and Earth arriving last as a point that becomes a colour.

**Because the external view comes from an instrument, instrument condition affects it.** Damage narrows what the player can see; upgrades widen it. A core capability is tied to a physical object worth maintaining.

**Its source migrates across the campaign**, which matters because the base does not stay on one rock (11.4). In Act I the view is the wrecked ship's surviving sensors — the only instrument that exists. From Act II it runs off the player's own antenna and spectrometer array (6.7), which is built for prospecting and takes over the external view as a side effect. By the time a transfer is possible, the view no longer depends on a hull that cannot move.

**Transition:** a fast, explicit transition between the two — under 1.5 seconds, no loading screen, camera pulls back through the hull and out. **Not a continuous zoom.** A single seamless zoom axis over an irregular rotating body, with a legible build grid at every intermediate altitude, is a large technical problem for a small gain; two well-tuned views with a quick transition delivers the value. The player is never confused about which view they are in, which is worth more than seamlessness.

### 15.2 Build Interface

- **Precision work happens in the external view.** Layout, blueprinting, conduit routing, and fleet assignment are done from above, where the grid reads cleanly and nothing blocks the view. Automation games need that clarity.
- **On foot is for presence and direct action**, not millimetre placement: inspecting a unit, hand-repairing, interacting, witnessing.
- **Michel is never the build cursor.** Construction is issued as orders to robots and resolved from the overhead view. The player never fights the third-person camera to place a structure. Walking around is a choice, not a tax.
- **Grid-and-cursor, not free placement**, specifically so the whole interface survives a controller and the Steam Deck (1.4).

### 15.3 Information Architecture

Four surfaces, and no more:

1. **Status band (always visible, minimal).** The three throughput flows, power margin, heat margin, the ration clock, and the pressure integrity of every sealed volume — which is how the ship's failure in Act I is read (4.2). Colour and shape only; a deficit reads at a glance without a number unless hovered.
2. **The external view** — spatial state: base, surface, surroundings, incoming windows.
3. **The dependency view** — the full recipe/requirement graph, readable and plannable, showing what is buildable now and the exact physical requirement of anything that is not (16.5).
4. **Unit roster** — every machine, its configuration, its assignment, its condition, its name if it has one, and for conscious units, whatever it has recently said.

### 15.4 What Is Never Shown

- Resonance and per-unit trust, in any form (10.2, 10.4). No unit ever displays a standing, a mood, or a disposition icon.
- A morality indicator, alignment, karma, or relationship meter.
- A quest log or objective list. Direction comes from deficits and from the requirement graph.
- A minimap of the solar system with a route on it.
- Damage numbers, XP, or levels.
- Any tooltip explaining the game's themes.

---

## 16. Progression Architecture

### 16.1 No Research Points

No abstract currency, no research menu, no "invention." Every advance is gated the way reality gates it: by whether the base can physically do the thing yet.

**The knowledge is already aboard, and it is not his.** A twelve-year-old does not know the Mond process, zone refining, or Haber-Bosch pressures, and a game that pretended otherwise would be resting its entire tech tree on the one premise it never examined. What he has instead is the Institute's technical library, dumped into the lifeboat's storage in the last minute of MAIA's life along with his medical records and a message he cannot open (2.3). She had no time to select what to save, so he has metallurgy he will never understand and agronomy he can follow step by step.

The consequence for the player is a clean answer to *why can this child build a foundry*: he cannot, and the ship can tell him how. The consequence for the fiction is that the base ends up shaped like the place she worked (12.4) partly because the instructions are hers. Michel does not know any of this for most of the campaign, and no character ever explains it.

**What he lacks is not theory. It is infrastructure.** A capability unlocks when the base meets its **physical prerequisite**: a sustained temperature, a power level, a pressure, a material on hand, a place reached.

Worked example: semiconductor-grade silicon is not bought with points. It becomes buildable once the player has constructed a chamber that *holds* the required temperature in vacuum with the required cleanliness, and the game is watching the base's actual sustained thermal output. Cross the physical threshold and the recipe becomes available.

**The three ceilings (6.6) are therefore the real gates of progression**, and the tech tree is the engineering dependency graph made visible.

### 16.2 Spine and Webs

**The spine** is the critical path, always with a visible next step: stabilise life support → secure power → move into the rock → establish processing → close the food loop → close the chip loop or commit to raw industry → build the mass driver → commit the intercept burn → refit the lifeboat → descend. A player who only follows the spine finishes the game.

**The webs** are optional depth hung off it: alternate processing chains, engineering optimisations, salvage-only techniques, deeper automation tiers, the consciousness track.

**One correction to a common failure of this shape:** the existence of automation is *not* optional web content. Standing orders (T3) are on the spine, because a game whose thesis is "automation can become life" cannot make automation a side activity, and because T3 is where the player is handed relief for a chore they performed by hand a hundred times (P4). Logistics networks (T4) are the layer above that and do live in the webs — they optimise something that already works, which is also why they are the highest-value system cut available (18.4).

### 16.3 Three Parallel Tracks

Different players progress through different effort, and all three advance along the same spine.

| Track | Serves | Advances by |
|---|---|---|
| **Industrial** | Builders, optimisers | Scaling production, hitting physical thresholds, closing chains |
| **Salvage** | Explorers, story players | Derelicts, reverse-engineering, records |
| **Consciousness / memory** | Story and thematic players | Awakenings, per-unit trust, resonance, revelation layers |

They are not equally optional: the mass driver and the lander need all three, or a very expensive substitution for the ones the player skipped (9.2).

Pacing is explicitly adjustable in options, because players genuinely split on wanting it faster or slower.

### 16.4 Every Unlock Is a Verb

No stat filler. No "+5% efficiency" nodes. Each unlock grants either a **new verb** — a new way to move resources, a new automation tier, a new survival capability, access to a new kind of body or place — or a visible, decision-changing improvement. If an unlock would not change how the player acts next session, it is merged or cut.

**And the best unlocks automate a chore the player has personally performed** (P4, 8.4). The pacing rule that follows from it: the major milestones — first self-sustaining power loop, first automated hauling, first repair drone, first standing order, first awakened mind — are deliberate breakthroughs placed after stretches of plateau, never handed out at a steady drip. A plateau is not dead time; it is what makes the next milestone land.

The last stretch is guarded against a requirement spike. Act III should test the mastery the player built, not their patience.

### 16.5 Requirement Transparency

Two rules for the dependency view:

**Adjacent fogging with a visible horizon.** Unlocked capabilities and immediately-available next steps are fully shown. Distant advanced technology — particularly anything touching consciousness — appears as a fogged silhouette with only an evocative name, preserving the mystery of the central theme. The player sees the shape of the journey without every detail at once.

**Absolute requirement honesty.** Hovering any locked capability shows its exact physical prerequisite — *requires sustained 120 kW and a 1400 °C vacuum chamber* — so the player can plan. The player never invests in a machine and then discovers its power source is behind an unsignposted step. **The theme stays mysterious; the engineering is never coy.**

---

## 17. Technical Requirements

### 17.1 Simulation Budget

The load-bearing question for the whole project: how many individually simulated agents, at what tick rate, at 120× acceleration.

| Element | Target |
|---|---|
| Simultaneous robot units | 60 typical, 120 ceiling |
| Conscious units | 12 ceiling (each carrying state, memory, preferences, dialogue) |
| Processing facilities | 80 typical |
| Resource flow ticks | Fixed-step, 4 Hz at 1×, decoupled from render |
| Behaviour at 120× | Flows resolve analytically over the interval; unit pathing coarsens; no per-frame agent simulation |
| Target frame rate | 60 fps at 1440p mid-range; 30 fps floor on Steam Deck |

**The hard technical rule:** the simulation must be *deterministic and analytically resolvable over an interval*, because time acceleration is core, not optional. Any system that cannot be fast-forwarded correctly cannot ship. This constrains every mechanic proposed from here on, and it is the first question to ask of any new system.

**Trajectory propagation is the strictest case of that rule.** The asteroid's path, the encounter schedule, and the effect of every mass driver burn (11.4) must all resolve identically whether the intervening two in-game years were played at 1× or skipped at 120×. The trajectory model is therefore analytic and closed-form, not an integrated n-body simulation: a parameterised path that burns modify by known deltas, with the encounter schedule derived from it rather than discovered by stepping. This is also what lets the external view project a burn's outcome months ahead with an honest error band.

### 17.2 Engine Selection

Open decision, to be made against these criteria in this order:

1. Deterministic fixed-step simulation decoupled from rendering, with reliable behaviour under extreme time scaling.
2. Efficient handling of 100+ simple agents without per-agent overhead becoming the frame budget.
3. Procedural mesh support for excavated interior volume on an irregular body.
4. Team familiarity, which in practice outweighs items 1–3 for a small team.

Both mainstream candidates satisfy 1–3 with work. Item 4 decides it. This should be settled before the vertical slice begins, not during it.

### 17.3 Save System

- One continuous campaign save, autosaved at every window boundary and every sleep.
- Manual saves permitted.
- Save must capture: full base state, all unit configurations and positions, every conscious unit's state and history, the single resonance event log with its actor/target/witness fields, the per-unit trust ledger of every machine including the unconscious ones and the temperament constant of every machine that has awakened (10.2, 9.1), window schedule, trajectory parameters and committed burns, detection-clock state, and revelation flags.
- **The per-unit ledgers are the largest new save cost and the cheapest to bound:** trust is two floats and a short event index per machine, and only 12 units can ever be conscious (17.1). The ledgers of unconscious units are append-only and can be truncated to their running total plus the last 20 events without changing any outcome the player can observe.
- **Target save size under 8 MB and save time under 2 seconds**, because a save happening at every window means it happens often.

### 17.4 Art and Audio Direction

Requirements, not style prescriptions:

- **Readability over fidelity.** The player must identify a unit's archetype, condition, and current task from the external view at a glance.
- **Light is scarce and directional, and it changes across the campaign.** At five astronomical units the Sun is a small hard disk delivering about a twenty-seventh of Earth's illumination, and the rock itself is a D-type with the albedo of coal, so almost nothing is visible that the base's own lamps do not light. The lit footprint *is* the visual measure of progress. Jupiter is the brightest object in the Act I sky and presides over the entire first act. Then it shrinks for twenty hours while the Sun grows, the main belt's grey silicates arrive as the first naturally bright surfaces the player has seen, and by Act III there is daylight — which is the moment the rock stops looking like a refuge and starts looking like a wreck in plain view.
- **Audio is the survival UI.** Fans, pumps, servos, the reactor. The player should hear a deficit before they read it. Silence is the alarm.
- **Michel's three age stages** (12 / 14 / 15) require one model with two revisions plus voice recasting or pitch progression.
- **Conscious units are not visually distinguished by decoration.** A woken machine looks like what it is: a chassis with an extra radiator and a heavier core. The difference should be readable in behaviour long before it is readable in silhouette.
- **Earth is one environment, not a biome set.** The descent sequence needs a single overgrown region, a machine industrial zone seen at distance, and Aurora's ruin. Its production cost is scoped as a short authored level, not a planet — and the visual shock is meant to come from colour and air after forty hours of grey vacuum, not from breadth.

---

## 18. Scope and Production

### 18.1 Vertical Slice

The thing to build first, and nothing outside this list belongs in it.

**Contains:** the first 30 minutes exactly as specified (4.1) · the second movement, up to and including the first sealed interior volume (4.2) · one asteroid with surface and interior construction · the three throughput flows and the power triage · ice → water → O₂ chain · hand assembly and one fabricator · three robot archetypes with the module system and its three budgets · T1 and T2 automation · one procedural encounter window, worked end to end · the spectrometer and one prospecting decision · both camera views and the transition · time acceleration at 1× / 12× / 60× · Layer One dreams on a fixed schedule · the event log writing per-unit ledgers with nothing reading them yet.

**Excludes:** consciousness, resonance, derelicts, survivors, combat, the food loop, the mass driver, Acts II and III, anything past T2 automation.

**The second movement is in the slice for a production reason, not a narrative one.** It is the only way to prove interior excavation on an irregular body inside the slice, which is one of the top risks in 18.5, and it is what turns the slice from a twenty-minute demonstration of hauling into something with a middle. The event log ships early for the same kind of reason: it is cheap, it is the single source everything in Section 10 later reads from (10.4), and retrofitting actor/target/witness fields into a shipped simulation is the one change in this design that would be genuinely painful late.

Dreams appear in the slice with resonance stubbed out — they fire on a fixed timer rather than being gated (12.1) — because their job here is to prove the dream sequences read well, not to prove the gate works.

**What it proves:** that hauling ice by hand for twenty minutes and then automating it is *fun*, that the throughput/stockpile tension holds, that a window is exciting, and that the two views work. If the vertical slice is not fun without consciousness, no amount of theme fixes it.

### 18.2 MVP

Vertical slice, plus: the full Act I → Act II transition · the complete processing chain set and all six resource tiers · T3 and T4 automation · the consciousness system with the authored first awakening and up to six conscious units · per-unit trust and global resonance with the full event table and all six expression channels · three derelict types · one survivor encounter · war-orphan incursions · Layers One through Three · one transfer opportunity · one ending (Family, as the middle case).

Trust ships in the MVP rather than after it because it is what the first awakening reads to decide who the unit is when it wakes (9.1), and because the risk the MVP exists to retire is whether the moral system is legible at all (18.5) — which is a question about individual machines, not about a hidden aggregate.

### 18.3 Full Game

MVP plus: the mass driver and its burn economy · Act III, the radio silence, and the detection clock · the lifeboat refit · the descent and Earth · all four endings · twelve authored major windows · all six survivor types · human companions · Inheritance · Layer Four and MAIA's complete message · the second transfer · the Aurora echo payoff · full aging progression.

### 18.4 Cut Lines

Three lists, in order of what goes first. Everything in the first two can be cut without breaking a pillar; nothing in the third can.

**Content and systems are listed separately, because they are not the same saving.** Cutting authored material shortens the game; it does not reduce the engineering that has to work, and engineering is what a small team actually runs out of. So the content cuts come first, cheapest first, and the system cuts follow with the specific capability each one surrenders.

**Cuttable content, in order:**
1. Human companions (13.4) — the rarest content in the game, and the campaign works with none.
2. Michel's third age stage — two stages carry it.
3. Two of the six survivor types (Liberation-minded and Children of Aurora can be folded into records rather than encounters, though Children of Aurora is the strongest single encounter in the game and should be the last cut).
4. The Species ending — leaving Instrument, Empire, and Family, which still constitute a real dilemma. Expensive to cut thematically; cheap to cut in production.
5. Inheritance (9.4) — permanence works without it.
6. Procedural minor windows beyond the twelve authored ones — reduces campaign length, not campaign shape.
7. Aurora as a walkable location, reduced to a recovered record set. This is the cheapest large saving in Act III and the one that costs the most meaning.

**Cuttable systems, in order, with what is lost:**
1. **The transfer mechanic entirely (11.4).** The mass driver already solves the trajectory problem, and transfers are the alternative route, not the route. Removes a whole branch of Act III state (the player with no lifeboat to refit), two authored encounters, and a large amount of "what can the base carry" bookkeeping. This is the single biggest system saving in the document and it costs the least.
2. **Burn count down to four from six.** Fewer, larger decisions. The mechanic survives; the granularity does not. Four is the floor (11.4) — three collapses the trade-off into a single occurrence and is not a cut, it is a removal.
3. **T4 logistics networks (8.4).** T3 standing orders carry the automation thesis on their own; T4 is the optimisation layer on top. Cutting it costs the late-Act-II ceiling for large-base players and nothing structural. It is the highest-value system cut that does not touch a pillar.
4. **Procedural window generation.** Ship the twelve authored majors plus a small hand-built pool on rotation. Removes a generator, a validation problem, and a class of degenerate cases from the trajectory model (17.1).
5. **Interior excavation as free-form volume**, replaced by the pre-authored volumes already named as the fallback in 18.5. Costs the Aurora echo some of its force, because the player is choosing rooms rather than digging them, and should not be cut before the echo has been playtested.
6. **The second camera view**, external only, with on-foot sequences restricted to authored interiors and EVA. This saves a great deal and should be treated as a last resort: it removes the embodiment that makes Michel twelve years old rather than a cursor (15.1).

**Not cuttable without breaking a pillar:**
- The throughput/stockpile distinction (P1, and the entire Act I).
- The power/heat ceiling (P1, P2 — it is the currency morality is priced in).
- Riding first, pushing late (P3), and the rule that a burn's result is never visible in the session it was ordered.
- The radio silence (11.5). It is nearly free to build and it is what forces the truth through the memory system instead of through exposition.
- The finite lander manifest (11.6). Without a hard mass limit there is no moment of choosing, and the endings have nowhere to happen.
- Manual-before-automated pacing (P4).
- The salvage gate as consciousness's reason to exist (9.2 — without it the moral system is free and the thesis collapses).
- Conscious dialogue (9.5 — without it the moral system is invisible).
- Permanent death for conscious units (P5).
- Pressure 4 in both of its forms (10.1). The incursions are episodic and could in principle be thinned; the refit form cannot be cut at all, because it is the only thing keeping the moral system running in the act where the endings are chosen.
- At least three of the four pressure sources (10.1), and Pressure 2 must be one of them, since it is the one the others are denominated in. Cut any one and check the remainder still make cruelty pay; cut two and the game has no dilemma.
- Per-unit trust (10.2). Without it the boarding decisions in 11.6 resolve on a hidden aggregate the player cannot have been reading, which makes the last five minutes of a fifty-hour campaign feel arbitrary — the exact failure 18.5 lists as the second-highest risk in the project.

### 18.5 Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Time acceleration correctness.** Every system must fast-forward without drift or exploit. | Highest — it is architectural | Fixed-step deterministic simulation from day one (17.1). Prototype acceleration before any content. |
| **The consciousness counterweight fails.** Optimising players compute that awakening is not worth it. | High | The salvage gate is categorical, not numerical (9.2). Playtest with optimisers explicitly and watch whether they awaken anything. |
| **The moral engine is invisible in practice.** The player never notices resonance and finds the ending arbitrary. | High | Two guaranteed channels, both attached to individuals rather than to an aggregate: conscious dialogue (9.5) and per-unit refusal (10.2, 10.4). Playtest for it specifically: after 10 hours, ask the player what the game is tracking, and ask which machine trusts them least. If they can answer the second question, the system is legible. |
| **Per-unit trust is unreadable at fleet scale.** With 60 machines on the rock the player cannot track individual standing and the layer adds noise instead of legibility. | Medium-high | Trust only expresses through conscious units, which are capped at 12 (17.1), and a conscious unit is a named thing with a voice. The ledgers of unconscious machines are invisible by design and surface exactly once, at awakening (9.1). |
| **Interior excavation on an irregular body** is a bigger tech problem than it looks. | Medium-high | Prototype in the slice. Fallback: pre-authored interior volumes with player-chosen fit-out. |
| **Scope.** The systems list is still large for a small team. | Medium-high | The cut lines (18.4) are written before they are needed, in order, deliberately. |
| **Act I is a triage screen for six hours** and reads as tedium rather than tension. | Medium | The second movement (4.2) exists to give the act's back half a construction project instead of a countdown, and its trigger day is the first tuning dial to reach for. Aggressive playtesting of the first 30 minutes specifically; Act I duration is the first thing to shorten after that. |
| **Conscious dialogue reads as preachy** and the moral system feels like scolding. | Medium | Hard writing rules (10.4). No unit ever names the moral stake. |

---

## 19. Open Decisions

Genuinely undecided, and each requires playtest data or a decision the design cannot make on paper.

**Requires playtest data:**
- The consciousness counterweight's magnitude: how large the salvage-route advantage must be so that awakening is compelling but the raw-industry route stays viable. This is the top balance priority.
- Act I duration, the exact life-support timers, and where in the 30–45 day band the hull's second failure should land (4.2). The numbers in 5.2 are internally consistent, not validated.
- Window cadence and the ratio of majors to minors (11.2).
- Trust and resonance thresholds and event weights (10.2, 10.3), and whether the base-wide pattern checks need a cooldown to stop them stacking too fast.
- The temperament constant's range (10.2). At ±0.15 the player is meant to be uncertain about a specific machine without being surprised by it; too wide and the boarding decision reads as random again, too narrow and it reads as a formula.
- Whether food as a continuing flow (5.2) produces useful pressure through Act III or a punishing failure cascade, and whether players actually feel the burn-versus-harvest conflict or just lose crops without understanding why.
- Attritional tasking's yield/loss curve (10.1) — the temptation must be real without making safe play strictly wrong.
- Whether trust being spendable (9.3) is read as the game rewarding kindness with better tools. If players describe it that way, the return has to shrink until it is only willingness.

**Requires a design decision:**
- Engine (17.2). Blocks the vertical slice.
- How much of the base a transfer (11.4) can physically carry, and whether the volatile stockpile is exempt from that limit. The mechanic is decided; its cost is not.
- How many burns (four to six) and at what scale, which sets how granular the trajectory decision feels (11.4).
- The detection clock's rates: how fast it advances per unit of electromagnetic output, what a single hail attempt costs in days, and how much a fully quiet base can slow it (11.5).
- Whether under-burning can produce an orbit so poor that the descent becomes unwinnable, or whether the worst case is only expensive.
- Whether a second human companion exists at all (13.4), or the one is unique.
- Whether the Instrument ending (11.6) is reachable by a player who awakened machines and then wiped every one of them, or whether that path resolves as Empire. The mechanical difference is one check; the meaning is completely different.
- What a witness actually is (10.3) — line of sight, a radius, shared network, or presence in the same pressurised volume. This decides whether the base develops a collective opinion of Michel quickly or slowly, and it is the single most sensitive undefined parameter in Section 10.
- The complete module list and per-module budget values (8.3).
- The complete recipe list and input/output ratios (6.5, 7.2).
