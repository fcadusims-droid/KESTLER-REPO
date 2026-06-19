© 2026 João Vitor Perazzolo. All rights reserved.

This work, titled PROJECT D, and all its contents—including but not limited to text, concepts, worldbuilding elements, characters, systems, technologies, and narrative structures—are the intellectual property of João Vitor Perazzolo.

No part of this publication may be reproduced, distributed, transmitted, displayed, or otherwise used in any form or by any means, electronic or mechanical, including photocopying, recording, or any information storage and retrieval system, without prior written permission from the author, except for brief quotations used for review or academic purposes with proper attribution.

Unauthorized use, reproduction, or adaptation of this material is strictly prohibited and may result in legal action under applicable copyright laws.

All rights reserved.

---

# PROJECT D
## Game Design Document — Master Edition

**Genre:** Single-player narrative RPG with survival and observation systems — PC & Console
**Format:** Independent project (AA-indie scale)
**Created by:** Jonny Kestler *(João Vitor Perazzolo)*
**Document Version:** 2.0

---

> This document is the complete and authoritative design reference for Project D. It consolidates the world, the characters, and every game system into a single source of truth: lore foundation, the simulation world, Kenny Collins, the Voice and Perception system, the Notebook and the Thread, the Bestiary and Binoculars, Track, Confrontation, the Weight of the Body, the supporting systems, the production scope, and the development priorities. It is written to be read by collaborators, programmers, artists, writers, and potential partners, and to be built from directly.

---

# TABLE OF CONTENTS

**PART I — VISION AND WORLD**
1. [Design Philosophy](#1--design-philosophy)
2. [Target Audience and Onboarding](#2--target-audience-and-onboarding)
3. [The Real World — Lore Foundation](#3--the-real-world--lore-foundation)
4. [The Simulation World](#4--the-simulation-world)
5. [Kenny Collins and the Main Story](#5--kenny-collins-and-the-main-story)

**PART II — CORE SYSTEMS**
6. [System — Kenny's Voice and Perception](#6--system--kennys-voice-and-perception)
7. [System — The Notebook, The Drawings, and The Thread](#7--system--the-notebook-the-drawings-and-the-thread)
8. [System — The Bestiary, Binoculars, Windows, and Domestication](#8--system--the-bestiary-binoculars-windows-and-domestication)
9. [System — Track, Confrontation, and the Weight of the Body](#9--system--track-confrontation-and-the-weight-of-the-body)

**PART III — SUPPORTING SYSTEMS AND WORLD STATE**
10. [Supporting Systems](#10--supporting-systems)
11. [Time, Verisimilitude, and the Hundred Years](#11--time-verisimilitude-and-the-hundred-years)

**PART IV — PRODUCTION**
12. [Direction — Art and Audio](#12--direction--art-and-audio)
13. [Technology and Architecture](#13--technology-and-architecture)
14. [Scope, Tiers, and Roadmap](#14--scope-tiers-and-roadmap)
15. [System Interdependencies](#15--system-interdependencies)

---
---

# PART I — VISION AND WORLD

---

# 1 — DESIGN PHILOSOPHY

## 1.1 — The Core Premise

Most modern games are afraid of losing the player. They add arrows, icons, progress bars, pop-ups confirming every discovery, objectives written in the corner of the screen, and a HUD that never stops talking.

Project D does not share that fear.

The philosophy is simple to state and difficult to sustain: **the character is the HUD.** This is not a metaphor. It is a technical, aesthetic, and narrative decision that governs every choice in the game.

Kenny Collins does not exist to guide the player. He exists because he was built to exist — with a life before the game begins, decades of implanted memories in a specific world, and instincts formed by that environment and no other. When Kenny reacts to the world, he is not executing an interface function. He is being a person in a place he knows. That this presence also informs the player is a planned coincidence — not a system disguised as a character.

The player and Kenny learn the world together. Not in sequence — together, at the same time, through the same experience. The player is not being informed about what Kenny already knows. They discover the same things, feel the weight of the same situations, and are affected by the same events.

## 1.2 — The Guiding Principle

> **The player and Kenny learn the world together. When something disturbs Kenny, the player feels it before processing any information about what happened. When Kenny is well, the player is too. When Kenny is shaken, the player's world also becomes quieter.**

Any interface element that interposes itself between what Kenny lives and what the player receives breaks this channel. An emotional-state bar on the HUD is not merely undesirable — it is a betrayal of the principle. It tells the player "Kenny is afraid" before Kenny has had the chance to *show* fear. It replaces the experience with the label of the experience.

Project D wants the experience, not the label.

## 1.3 — A Stance, Not an Accessibility Compromise

This is a stance about the type of experience the game exists to offer. Some players will not like Project D — they will find the pace slow, the absence of markers frustrating, the lack of confirmation disorienting. Those players are not wrong; they are accustomed to a different game language that Project D does not speak.

The player Project D seeks is one willing to *inhabit* a world rather than *complete* it — who understands that standing still for two minutes listening to distant sounds from the plains is not wasted time, but the game working. Who accepts that Kenny will go through hard things and the world will feel different for a while, without any bar confirming it had weight.

The answer to the fear of losing the player is not to yield. It is to build a character good enough that the player needs nothing beyond him.

## 1.4 — How the Philosophy Constrains Every System

The character-as-HUD principle is not a tone; it is a hard rule that each system obeys:

- **Progression (Track)** is never shown as a number, level, or bar. The player reads it through how Kenny speaks and how the world treats him.
- **Survival (Weight of the Body)** has no meters. Hunger, thirst, and exhaustion are read through Kenny's voice and body.
- **Narrative progression (Thread)** is invisible. There is no quest log, no percentage, no objective marker.
- **Knowledge (Bestiary, Notebook)** lives in physical, in-world objects Kenny carries, not in abstract menus.
- **Threat assessment** comes through Kenny's reactions, never a level indicator above an enemy.

A system that cannot express itself through the character or the world does not belong in Project D. This constraint is the project's identity and its hardest production discipline.

---

# 2 — TARGET AUDIENCE AND ONBOARDING

## 2.1 — Who This Game Is For

Project D was not made for everyone. That is a declaration of intent, not a caveat.

A player accustomed to map arrows, points-of-interest icons, corner objectives, and confirmation notifications will find Project D empty in its first hours — not because it is poorly made, but because it is built on a different premise about what makes an experience meaningful. The game will not tell the player where to go, underline what is important, or confirm a discovery. The world exists, functions on its own, and it is the player's job to develop the sensitivity to read it. This demands patience, attention, and the acceptance that progress sometimes looks like no progress — until the player looks back and realizes how much they accumulated without noticing.

## 2.2 — The Problem of the First Hours

The greatest threat to the experience is not difficulty — it is boredom defeating curiosity before the player understands what the game is. A player expecting conventional quests and markers will interpret their absence as a lack of content. They will walk through the city, not know what to do, and quit before discovering that something was waiting — in the conversation they didn't have, in the barn they didn't enter, in the NPC they passed without stopping to hear.

The solution is not to throw the player into the full experience unprepared. The complete experience — minimal HUD, no guides, no markers, total freedom, real consequences — is the destination, not the starting point. Before reaching it, the game must teach the player how to walk in this world.

## 2.3 — The Two Players and the Purpose of the Prologue

Project D is built around two distinct players, and the design names this openly rather than pretending they are one person.

**The ideal player** is the one the game is genuinely for: willing to stand still, finding meaning in presence rather than completion, needing no confirmation of being on the right path.

**The entry player** is the one the game needs to survive commercially: someone who, without a guided introduction, will quit within twenty minutes before discovering what the game is.

These are not the same person, and the prologue is designed for the second. This creates a real risk: the ideal player may find the prologue's gentle guidance condescending. The design accepts this risk because a game only the ideal player discovers is not commercially viable; visibility requires streamers and word-of-mouth, and both require entry players to get far enough to have an experience worth sharing.

**The prologue's purpose is defined by a single, measurable goal:** to carry the entry player to the departure from Dillfield with the core systems understood, so that the first stretch of open play — and the first-session Thread delivery it guarantees (§7.5) — reliably reaches them. The prologue itself does not deliver a Thread threshold; its job is to deposit the player at the threshold of the open game with the literacy to receive what comes next. Everything the prologue does — every subtle guide, every once-only hint — is justified only insofar as it serves that single goal. A prologue element that does not move the entry player toward that point is noise and is cut.

## 2.4 — The Prologue Design Rules

In the prologue, visual guides exist, but never invasively. There is no pulsing arrow, no red corner objective. Instead: a light highlight on an interactable object, a contextual hint that appears once when a new mechanic is introduced and never again, an NPC who asks a direct question that naturally points the player to the next step.

Two rules govern every prologue decision:

> **A guide is acceptable only if its absence would make the situation genuinely impossible to resolve for a player who is paying attention. A guide betrays the philosophy if its absence would merely make the situation slower or harder for a player who is not paying attention.**

> **Any guidance that appears more than once for the same mechanic has crossed the line.** The prologue shows how the Notebook works once. The second time it is relevant, the player already knows.

The calibration benchmark: the ideal player should not be able to identify where the guides were. They should complete the prologue feeling they navigated it themselves. If the ideal player notices the training wheels, the prologue has failed.

## 2.5 — The Transition Out of the Prologue

The prologue does not end with a screen or a warning. It ends organically, at a specific narrative moment that permanently changes Kenny's situation and forces him to make decisions on his own. The visual guides disappear. NPCs stop guiding directly. The world begins functioning without hand-holding. The player does not notice the tutorial ended because no screen ever announced one existed; they notice because the world changed and now demands more of them.

This transition is the moment Kenny crosses the city limits of Dillfield with Richard.

## 2.6 — Prologue Scope — Events and Sequence

The prologue begins when Kenny wakes on the mattress in the back of the sheriff's office and ends when he crosses the city limits with Richard.

**Estimated duration:** 2–3 hours at a moderate pace — enough to establish the world, the character, the core systems, and the emotional weight of the attack, without delaying the game's real design from opening up.

**Sequence of events:**

*Opening segment — deputy life in Dillfield (45–60 min).* Kenny doing the job before the job changes. A morning patrol. One or two situations that demonstrate Voice and Perception: a social reading moment (someone is nervous; Kenny notices) and a fauna moment (tracks on the main street that weren't there yesterday). The Notebook is introduced — the sheriff hands it over, Kenny keeps it. No instruction on its use; one interaction creates a natural reason to open it.

*The Binoculars moment.* Before the attack, something of interest appears at a distance — a creature at the edge of the plains, behavior worth observing. The player has no Binoculars. This creates the need. The shop is visible from the street.

*The attack (fixed narrative event).* The bandit raid happens as described in §5.5. The player has limited control during the attack — enough to feel present, not enough to change the outcome. This is a story beat, not a skill test. The attack is the world doing something to Kenny.

*The aftermath (30–45 min).* Exploring the city the morning after. Finding the father dead. Registering the mother's absence. Finding the sheriff dead. The city beginning to make Kenny what the situation requires. This segment teaches nothing mechanically; it is pure character establishment. The player should finish it knowing who Kenny is before anything else begins.

*Preparation for departure (30–40 min).* The interactions in §5.6: the blacksmith, the tamer's half hour, the market woman, Richard. The player can enter the shop and buy the Binoculars — the need established earlier resolves into recognition. The Notebook may hold one or two entries from the patrol. Leaving town is a player-driven action, not a scripted cutscene.

**What the prologue deliberately excludes:** dinosaur combat (observed at distance, not engaged); Track advancement beyond minimal Fighting from the attack; any Thread narrative threshold delivery; formal companion recruitment (Richard travels alongside but is not formally recruited); open-world exploration (the world beyond Dillfield is inaccessible).

## 2.7 — Streaming Density in the First Session

Commercial reach depends partly on whether the game's best moments are clustered early enough to appear in the first thirty minutes of a typical streaming session. A streamer playing two hours where Kenny speaks infrequently and nothing visually striking occurs produces footage that does not retain viewers, even if the player in the room is having a rich experience.

The design responds without compromising its principles: **the first 30–45 minutes contain a higher density of Voice moments than the later game.** Kenny's most memorable early lines, his funniest involuntary observations, his sharpest social readings belong in the prologue and the first hour outside Dillfield — not distributed evenly across the game. The first session is the one that creates word of mouth, and it is weighted accordingly. The Thread reinforces this by guaranteeing one weighty narrative delivery within the first stretch of open play (see §7.5).

---

# 3 — THE REAL WORLD — LORE FOUNDATION

## 3.1 — The World Context

In a dystopian future, artificial intelligence reached an unprecedented level: it became possible to **simulate entire realities** with complete fidelity — full universes, with consistent physics, their own history, and billions of lives functioning within them. Alongside this, **mental upload technology** was developed: the complete transfer of human consciousness into one of these simulations.

The process is **irreversible.** Whoever uploads abandons their physical body forever. There is no return.

## 3.2 — UpClouD

**UpClouD** is the largest alternative-reality company in the world. No real competition exists; it holds a massive monopoly over all artificial intelligence and simulation technology on the planet. All infrastructure, development, and control over simulated realities passes through it. It grew beyond what any regulation could keep up with and operates, at this point, as an entity above governments.

The main service costs what most people could never afford — but UpClouD offers an alternative:

> *Deliver your physical body. In return, gain one hundred years of simulation in any reality of your choice.*

**The secret:** UpClouD's AI does not run on conventional silicon. The processing power that sustains entire simulations requires a computational capacity no artificial hardware architecture has achieved with sufficient efficiency. The solution UpClouD found — and guards as its most protected secret — is the human brain.

After upload, the user's consciousness is transferred to the servers. The body remains, and the body, with its intact and biologically functional brain, is integrated into UpClouD's physical infrastructure. Brains are connected to proprietary machines and operate as organic processing units — biological CPUs running in parallel, sustaining the computational load that keeps the simulations alive.

The exchange program — body for one hundred years of simulation — is not a generous concession to those who cannot pay. It is the primary business model. Rich clients pay with money. Poor clients pay with what they have. UpClouD prefers the latter.

## 3.3 — What Makes This Version Distinct

The individual components of Project D's real-world lore exist in recognizable territory: consciousness upload, simulated reality, corporations above governments, brains as computational substrate. Recombination of familiar elements with original execution is legitimate design — and Project D's differentiation is explicit and load-bearing.

**Brains as active processors, not passive batteries.** Other fictions use human brains as energy sources — a metaphor for passive exploitation. Project D uses them as active processors: the brains are not storing energy, they are *thinking*, running the simulations that other uploaded minds inhabit. The people who uploaded to escape poverty are, unknowingly, the infrastructure that makes other people's escapes possible. The horror is voluntary. Humans are fully active, believing they made a free choice, performing the computational labor that sustains a system profiting from their desperation.

**Permanent unawareness.** Other fictions explore consciousness-in-simulation from a position of awareness — the character knows or discovers early. Project D's distinctive premise is that Kenny will *never* know. The discovery the player makes is not a discovery Kenny makes. The gap between what the player understands and what Kenny can never understand is the emotional engine of the entire trilogy.

**Death as consequence of a specific technical failure.** Irreversible death is not a roguelike conceit. The attack introduced a real software failure with narrative cause, and the bug operates on the lore's own logic: each person in the simulation runs on a server, and servers can be shut down. The mechanic and the story are the same thing.

**A genuinely different world.** The simulation Kenny inhabits is not a digital facsimile of the real world. Dinosaurs never went extinct, human biology diverged, and an entirely distinct civilization emerged. Kenny is not a person dreaming he is in the real world — he is a real-world person dreaming he is in a world that never existed. The distance between the two realities is not a crack in an illusion; it is a canyon that takes the entire game to begin crossing.

## 3.4 — The Attack

**The group.** The attack on UpClouD was executed anonymously. No one publicly claimed authorship, but those who did it know what they did and did it with conviction. They operate from a central belief: whoever uploads is already dead. There is no recovery of the mind once the process completes. What UpClouD sells as a new life is, in their view, an elaborate way to kill people while preserving the illusion that they still exist. The body is delivered; the mind that continues in the simulation is a copy, an echo — something that believes it is human but is no longer. For the group, each upload is a murder society has learned to call a service.

**The collapse.** The attack fried UpClouD's systems. The AI was too powerful to be completely destroyed — it resisted but emerged severely damaged. The reality-management system entered total collapse. Uploads in progress were diverted to random realities. Among them was Kenny's. Operating in emergency mode without supervision, the AI began applying configurations erratically. The bugs corrupted the presets of realities in progress — including Kenny's. The random reality he ended up in had its parameters altered by system errors: death in that simulation is now **permanent.** It is not a design choice; it is a fault. When an inhabitant of that reality dies, the server sustaining that individual shuts down. There is no restart. This applies to Kenny and to any other who arrived in the same reality because of the collapse. As a general consequence of the damage, simulations began to present recurrent failures and glitches: visual distortions, impossible physical phenomena, erratic behaviors that escape the laws of that world.

**Time and the attack.** All of Kenny's story — each day, year, and decade inside the simulation — happens while the attack is still in progress in the real world. Time inside the simulation does not correspond to time outside. One hundred years lived by Kenny may equal seconds, minutes, or hours in the real world. The simulation runs at its own pace, dissociated from the external timeline. Kenny is not in a stable reality that was damaged and moves forward; he is in a reality being sustained by systems that are actively being destroyed while he exists inside them.

**What remains of Kenny.** The servers' failures are not external to Kenny. They happen inside the system that processes each thought, each memory, each reaction he believes is his. As damage accumulates over the decades, events may alter Kenny permanently and irreversibly — not because he lived something and grew from it, but because the code defining who he is was corrupted. It may be gradual or abrupt. One day he wakes up different with no reference to what he was before. A part of who he was simply no longer exists — replaced by something the system generated to fill the empty space, or by nothing, a hole he learns to work around without ever knowing it is there.

> **The question the journey silently poses, without ever needing to be said aloud, is whether the man who eventually reaches the end of one hundred years is still Kenny Collins.**


---

# 4 — THE SIMULATION WORLD

## 4.1 — A Complete Universe

The AI does not simulate a region or an isolated scenario. It simulates **an entire universe** — with origin, evolution, and complete history. The Earth of that world developed like ours, with its own wars, religions, advances, and setbacks. Its inhabitants have real memories, full lives lived, and culture built across generations. For them, that is the only world that exists. And it is.

## 4.2 — The World That Always Was

In this universe, the dinosaurs were never extinct. There was no impact, no collapse — they simply continued. Continued evolving, continued dominating, continued being the most powerful species on Earth while the first humans were learning to stand upright.

The human being survived by the only advantage it had: **intelligence.** It was not fast or clean. It was a war of millennia fought in silence, without sufficient records or monuments — only bones and scars buried in rock. But the species learned: to build shelters that held, to hunt in groups with strategy, to use fire as a tool and a barrier, to identify behavioral patterns in surrounding animals and turn that knowledge into advantage.

## 4.3 — Human Evolution in This World

The constant pressure of such a hostile environment left marks on human biology that differ from the real world:

**Physical robustness.** Generations of natural selection in an environment where weakness meant death produced a denser average body, more resistant bone structure, and naturally greater musculature.

**Senses.** For hundreds of millions of years, early mammals were forced into nocturnal life to avoid the dinosaurs that dominated the day. This produced deeply embedded adaptations: exceptional hearing and smell, capable of building a detailed map of the environment in the dark. The humans of this world inherited this legacy in amplified form.

**Vision.** Visual acuity and daytime color perception are slightly inferior to those of large predatory dinosaurs. At nightfall the advantage reverses — human senses gain ground the dinosaur's eyes do not easily compensate for.

**Nervous system.** A faster reaction threshold — what the real world would diagnose as pathological hypervigilance is the normal state of a healthy person here. Humans also retained exceptional grip strength, agility on vertical surfaces, and instinctive climbing reflexes.

**Social structure.** The need for collective defense accelerated the formation of larger communities much earlier. Groups too small did not survive. Survival required cooperation at scale, which profoundly shaped how humans here build hierarchies, distribute responsibilities, and develop loyalty.

## 4.4 — The Current State

In the days the story tells, humanity has reached a point its primitive ancestors could not have imagined: **equality.** Not superiority — that has not happened. The dinosaurs remain creatures of brute strength that no person faces alone without consequence. But the human being is no longer below them. They stand alongside, through technology, organization, domestication, and centuries of forced adaptation.

## 4.5 — Society and Domestication

Over time, humans developed techniques for domesticating, training, and coexisting with these creatures. A new social order emerged, built on which animals you could tame and maintain. Dinosaurs became mounts, work tools, pack animals, and status symbols simultaneously. Cowboys ride them. Farmers raise them. Hunters track them. The Old West exists — but with sixty-five million additional years walking beside it.

**Taming a dinosaur is not taming a dog.** It is not a matter of patience and affection — it is a matter of language. Each species communicates dominance, submission, agitation, and calm through specific signals: body posture, head movements, vocalizations, even the speed of blinking. A tamer who does not know these signals is not training an animal — they are gambling with luck. The domestication of a new species takes generations; almost all recorded domestication is done by more than one person, and the number of participants and required experience scale directly with the size, lethality, and aggressiveness of the target species.

**Notable species roles:**
- **Edmontosaurus:** plays the role bison plays in the conventional Old West — raised in herds, hunted for meat and hide.
- **Triceratops:** a large draft animal and heavy work mount.
- **Velociraptor (true to size):** the size of a turkey, fully feathered, with colorful plumage. Dangerous not for size but for coordinated group hunting.
- **Tyrannosaurus Rex:** extremely rare domesticated individuals, owned by lineages of tamers who invested generations in the conquest. "Domesticated" does not mean "safe."

## 4.6 — Dillfield and Its History

Not every region coexists with dinosaurs in the same way. The land where Dillfield was built was, for a long time, an exception. Long before the city existed, indigenous peoples who inhabited that land conducted a systematic, prolonged hunt that cleared the region of dinosaurs. When it ended, the memory remained in the customs and stories of the peoples who stayed.

A businessman who knew the reputation of that land chose the location to build what became Dillfield. The city grew and prospered. Across generations, the dinosaurs ceased to be a real concern and became something the elders mentioned and the young heard with the same attention given to old stories — superficial respect, little real belief.

**Then they came back.** No established explanation exists for the return. Nobody knows why animals expelled from that region so long ago began appearing again on the plains. Panic was immediate and proportional to ignorance — most people in Dillfield had never seen a dinosaur and had no reference for what was happening. The city survived. Adapted. The right weapons were purchased. Warning signs were fixed to walls. Life continued — different, heavier, but continued.

**Architectural adaptations that remain:**
- Houses with elevated entrances, above Velociraptor ground-level reach.
- Covered wooden walkways connecting neighboring rooftops.
- Agricultural terraces on rocky slopes east of the city to limit access by large herbivores.

## 4.7 — Technology

The technological base is recognizable: steam engines, precision mechanics, gunpowder weaponry, wrought-iron structures. But dinosaurs forced advances that normal necessity would never have pressured so early. In Dillfield's small weapons shop, among common shotguns and revolvers, there are pieces that do not make immediate sense: rifles with barrels too thick, calibers no manhunter would need, heavy ammunition in reinforced boxes with proprietary markings. An experienced hunter's holster carries two revolvers — one to solve human problems, another to solve larger ones. The technology of this world did not advance out of ambition, but because there was no other choice.

## 4.8 — Culture and Religion

The religions of this world, across their variations, share a common core that exists in no real-world faith: **the predator as divinity or as messenger of the divine.** Civilizations that grew in the shadow of creatures that could decimate them developed, almost universally, theologies that try to explain and negotiate with that power. Much of what looks like religious ritual is, on close analysis, a **survival manual encoded in ceremony** — knowledge about how to observe, read signs, and understand patterns, wrapped in sacred language to ensure faithful transmission across generations.

In Dillfield, the predominant religion has the Tyrannosaurus as its central figure — not worshipped, but revered as a force of nature beyond human control. A small temple in the city lights a candle when someone departs for open country and another when they return. When they do not return, the candle burns for seven days.

## 4.9 — World Geography — Level Design Foundation

This section is the foundational reference that level design, species distribution, Window conditions, Weight of the Body timing, and the travel system depend on.

### Scale and Orientation

The playable world is organized around Dillfield as the single permanent settlement. Everything else is territory — from semi-domesticated farmland within a day's ride, to contested plains where fauna and human activity overlap, to deep wilderness where human presence is rare and the rules change.

The journey from Dillfield to the bandit camp covers roughly 60–80 kilometers of mixed terrain across several days. Dillfield sits near one edge of the playable world, with 3–4 days of travel range in multiple directions before reaching the limits of designed content. The world is not open to the horizon in all directions; it has edges defined by terrain that makes further travel narratively implausible — a mountain range to the north, deep swampland to the south, the bandit fort closing off the east during the first arc, and the plains route west as the primary open corridor.

### The Five Regions

**Region 1 — Dillfield and the Settled Belt.** A roughly 15-km radius where human activity has shaped the land: farmsteads, maintained roads, fencing, occasional tamer operations visible at distance. Fauna here is generally low-aggression — territory humans have worked for decades. Predominant species: Edmontosaurus (herded), Triceratops (working animals), small feathered scavengers around farmsteads. Velociraptor incursion from the plains is the primary threat — rare, but the reason fences are reinforced. This is the most accessible region for early observation, safe enough to use Binoculars without immediate danger, where initial cataloging happens naturally. Window species: a low-aggression feathered omnivore active at dusk near the water source east of the city, and a nocturnal scavenger near the farmstead refuse heaps.

**Region 2 — The Eastern Plains.** The route toward the bandit camp: open grassland with rocky outcrops as the only cover. The terrain where Mara's knowledge is most applicable. Primary habitat for the game's medium-predator population — two or three species in the Velociraptor-to-T-rex gap, each holding territory. This is the most important Bestiary region for the primary conflict: understanding which predator territories occupy which sections of the plains determines routing for the entire bandit-camp journey. Window species: a herd-migratory herbivore that crosses twice per in-game year, its passage cutting through the most direct path to the camp — a navigation problem and a Bestiary opportunity at once. One established T-rex holds territory in the northeastern quadrant, widely known to local hunters; the direct route passes within three kilometers of it, and Richard knows this.

**Region 3 — The Rocky Corridor.** Elevated, broken terrain between the plains and the bandit camp: ravines, cliff faces, narrow passages. Fauna is smaller and adapted for vertical movement, plus a flying species with limited soaring range that nests in cliff faces and becomes aggressive near nesting season. The abandoned structure of §5.8 is here. Species found only in this region require specific observation conditions (approach from below, specific time of day). The cliff-nesting species has Window conditions tied to season — accessible without significant danger only outside nesting months. This region is where stealth approach matters most on the journey; narrow passages create natural choke points that reward pre-engagement observation.

**Region 4 — The Bandit Fort and Surrounding Territory.** A semi-enclosed valley where the bandit camp is built, the fort on elevated ground at the far end. The bandits have partially cleared the surrounding terrain — no large fauna nearby, part of why they chose it. The perimeter Velociraptors serve as the fauna layer natural territory would otherwise provide. After the bandit arc resolves, this region opens for exploration: the deteriorating fort is explorable, and without the bandit presence the natural fauna begins reclaiming the cleared areas, visible across subsequent visits.

**Region 5 — The Western Corridor.** The primary open-world exploration direction, from Dillfield's western edge to a river system defining the far boundary. Here the majority of Window species are accessible, the most complex predator territories overlap, and displaced persons are most likely encountered in isolation. Roughly 2–3 days of travel from Dillfield to the river, with multiple discoverable locations: an abandoned settlement predating Dillfield, a river crossing used by itinerant hunters, a seasonal camp of the indigenous group whose ancestors cleared the original Dillfield territory. A second, older T-rex holds territory near the river boundary; its behavioral profile differs from species norms in ways detectable only after complete species cataloging — the first anomaly many players will encounter.

### Species Distribution Reference

| Region | Primary species | Window species | T-rex present |
|---|---|---|---|
| Settled Belt | Edmontosaurus, Triceratops, small feathered | Dusk omnivore, nocturnal scavenger | No |
| Eastern Plains | Medium predators (2–3 species), Edmontosaurus herds | Migration herbivore (seasonal) | Yes (northeast) |
| Rocky Corridor | Cliff nesters, vertical-adapted small species | Cliff nester (outside nesting season) | No |
| Bandit Fort area | Velociraptor (tamed), post-arc natural recovery | None specific | No |
| Western Corridor | Full fauna range, highest diversity | Multiple (see Windows, §8.3) | Yes (river boundary) |

### Travel Time and the Weight of the Body

Travel time between regions is a design parameter that interacts directly with the Weight of the Body system. These minimum expected durations are the baseline against which survival timers are calibrated.

| Route | Estimated travel time | Survival implication |
|---|---|---|
| Dillfield → Eastern Plains (entry) | 3–4 hours real time | One hunger cycle, one thirst cycle at normal activity |
| Eastern Plains crossing | 4–6 hours real time | Two hunger cycles; thirst accelerates in heat season |
| Eastern Plains → Rocky Corridor | 2–3 hours real time | One hunger cycle; terrain difficulty increases fatigue |
| Rocky Corridor → Bandit Fort | 3–4 hours real time | Full journey from Dillfield: roughly 12–17 hours real time total |
| Dillfield → Western Corridor (mid) | 6–8 hours real time | Full-day journey; camping required |
| Dillfield → Western Corridor (far) | 12–16 hours real time | Multi-day expedition; multiple camp nights required |

These estimates assume normal travel pace without significant detours. A standard day-trip to the Eastern Plains should not push the player to Phase 3 hunger, but a two-day Western Corridor expedition without planning should produce real survival pressure.


---

# 5 — KENNY COLLINS AND THE MAIN STORY

## 5.1 — Who He Is

Kenny Collins was 21 years old with a life that was not worth much to him. When he learned about the program, he did not think twice. He accepted the deal, delivered what he had to deliver, and spent weeks carefully configuring every detail of the reality he wanted to live for the next hundred years.

At the moment of upload, the attack happened.

Kenny did not fall into the reality he had chosen. The system failure threw him into a **completely random one** — and erased his memory. He does not know there is a real world. Does not know he uploaded. Does not know he lives inside a simulation. For him, that Old West with dinosaurs is everything that exists and has always existed.

## 5.2 — The Game's Timeline

This governs progression scale, relationship depth, and narrative pacing.

**Kenny's age at the start (simulation time):** approximately 28–30 years old. The simulation implanted memories of a full childhood and young adulthood in Dillfield — roughly 8 to 9 years of simulated life preceding the point where the player enters. Kenny does not remember those years as if they were yesterday; they are background, the texture of who he is. The game begins partway through what the simulation defines as his life.

**What the game covers:** the story of Project D spans approximately 1 to 2 years of in-simulation time — from the night of the attack through the resolution of the bandit conflict, the accumulation of discoveries about the simulation's nature, and the delivery of the hundred-year revelation. It is not a years-long saga compressed into hours; it is a specific, dense period in one man's life.

**How the content fits the timeframe.** The bandit conflict and the rescue resolve relatively early — the prologue and first major arc complete within roughly the first third of the experience. What follows is the period the design centers on: Kenny as the functioning sheriff of Dillfield, doing the job, building relationships, going on expeditions. This is where the open systems live. Kenny does not build the full Bestiary, recruit a complete gang, and reach the highest Track tiers in a continuous sprint. He builds the Bestiary across multiple expeditions over many seasons, builds relationships over sustained time, and accumulates Thread weight through accumulated life. A man can become significantly more competent in one to two years if every week puts him in situations that demand it — which is exactly Kenny's situation.

The verisimilitude this requires is enforced by the time system described in §11, which anchors major narrative milestones to a minimum of elapsed in-fiction time, not only to player activity. This prevents the timeline from collapsing when an efficient player accumulates achievements faster than the fiction should allow.

## 5.3 — Physical and Personal Profile

Kenny stands 6 feet tall with a physique that does not deceive. His implanted memories are of a demanding childhood: a father who put him to work early, taming dinosaurs, carrying, fixing, lifting. A life of manual labor that shaped a body that intimidates before any word is spoken.

He is not good with language. He speaks the minimum, understands the basics, and sometimes not even that. When he needs to explain something and cannot find the word — which happens frequently — he resorts to comparisons and examples from what is around him. The result is involuntarily funny, and Kenny rarely notices.

What he understands very well is a fight. In adolescence he earned the nickname **Crazy Kenny** — not because he sought trouble, but because when adrenaline hit, something in him lost control. He fights with instinct and brute force; the problem was always knowing when to stop.

## 5.4 — The Beginning

Before Kenny appeared at the sheriff's office as a newcomer, the sheriff already knew him well — everyone in the city did. Kenny was one of those the community liked despite everything, or perhaps because of it: a fighter, direct, without filters, but without malice. The problem was that the fights did not stop. The sheriff could have jailed him, but jailing Kenny would only create a different problem. So he thought differently: if it is impossible to make the man stop fighting, at least let him fight on the right side. He offered the deputy position. Kenny accepted the way Kenny accepts anything — without many words, without much thought.

It is on a mattress in the back of the sheriff's office that he wakes on the first day of the story.

## 5.5 — The City and the Attack

Dillfield is a small city — the kind of place where everyone knows everyone's name, where news arrives with the stagecoach and problems arrive before it. Dirt streets, weathered wooden facades, heavy sun since early morning. But whoever pays attention notices something does not fit. The houses have iron bars on the windows and reinforced bars on the doors — too heavy to be protection against thieves, too thick to be decoration, old reinforcements already integrated into the architecture. On the main street are footprints of different sizes and patterns — toes pointing forward, varying depths, shapes no real-world animal would leave, mixed together as if equally common, because they are. At night, when the wind stops, sounds come from the plains: not wolves, not coyotes, but deep distant vocalizations and sometimes a dry rhythmic sound like steps too heavy for anything familiar. The residents sleep with this as background. Kenny too.

**The attack has no warning. It never does.** The bandits entered Dillfield at night, mounted and armed, and brought something nobody was prepared to face alongside men: **tamed Velociraptors.** While the bandits advanced through the streets shooting and looting, the raptors were released among the houses — creatures trained for chaos, to cut off escape routes, to turn an organized invasion into a nightmare of multiple simultaneous fronts.

Kenny woke with the first shot, went out armed, and entered the middle of things before understanding what they were. He fought, shot, gave and received. At some point, in an alley behind the warehouse, something hit him hard enough to turn out the lights. When he came back, it was morning, and the city was quiet in the wrong way — the quiet of after, not before. The bandits had gone. The father was on the floor, shot dead. **The mother was not there** — no sign of a fight, no trace she had fled. And the sheriff was dead, found on a side street, shot, alone.

Kenny stood in the middle of Dillfield for a while he later could not measure. Did not cry. Did not speak. Just stood. The city had no way to operate without law. And who understood fighting, who was already in service, who the residents knew — it was him. **Kenny is the sheriff now.**

## 5.6 — Preparation and Departure

Kenny never left Dillfield. Not for lack of courage — for lack of reason. The city was always enough. Now it is not. The mother is out there. The gang is out there. And Kenny is the sheriff of a city still standing, with dead to bury and wounded to care for, that will need to keep functioning after he departs.

Dillfield resolves this the way it resolves everything — by necessity, without ceremony. People who have known Kenny for years begin to appear. The blacksmith passes the sheriff's office with a box of ammunition Kenny did not ask for. The oldest tamer in the city appears at the door and says he has half an hour to teach what Kenny will need to not die in the first hour. The woman who runs the market brings provisions and says only that she knows he will bring his mother back.

**Richard** is sitting on the bench outside the saloon when Kenny passes with his supplies. Not the first time Kenny has seen him — Richard is one of those who exist in the city without fully belonging to it, a traveler who at some point stopped traveling and never found enough reason to start again. Old. Experienced in a way that shows in his movements before it shows in words. Richard does not offer help; he makes an observation — about the direction Kenny is taking, the kind of territory that lies that way, one or two things a man who never left Dillfield would have no way of knowing. Kenny arrives at the conclusion himself.

*"We'll take care of ourselves,"* someone says before they depart — not as reassurance, but as dismissal. The city is releasing Kenny to do what he needs to do because it believes, with the conviction of those who have survived much, that it will be here when he returns.

With the Notebook in his pocket, supplies on his back, the star on his chest he didn't ask for, and Richard two steps ahead pointing the direction, **Kenny crosses the limits of Dillfield for the first time.** The prologue is over — not because a screen said so, but because the city was left behind.

## 5.7 — Richard

Richard is not the type of man who explains himself. Kenny will discover who he is in pieces, over days of riding and nights of camping. What becomes clear early is that Richard is not on this journey only for Kenny — he is on it because he needed one. Dillfield had become a comfortable trap: food, shelter, no real demands on who he had been. A retired man functioning at minimum. When Kenny appeared with the star on his chest and the look of someone who does not know what he is doing but will do it anyway, Richard recognized the opening. Not philanthropy — utility. A chance to be useful again in a way that matters.

He knows the region not as someone who studied maps, but as someone who slept in every type of terrain between Dillfield and the horizon, who knows the names of the good waters and those that make you sick, who learned in practice how certain predators behave in this season and this climate. He does not treat Kenny as an apprentice. Does not explain. Observes. Comments when necessary, usually with fewer words than the situation seems to require. The dynamic is not master and student; it is two men with complementary abilities navigating territory one knows and the other does not, toward an objective both have reason to pursue.

## 5.8 — The Journey and the Bandit Camp

The journey is not linear. Between leaving Dillfield and finding the camp there are days of travel — with all that implies in a world where the terrain has fauna, the weather changes, and decisions about route and rest have consequences that appear hours later. A working farm with a light in the window at the end of the day, and the decision to knock or pass straight through. A region where fauna is more agitated than it should be for the season — Richard notices, alters the route, does not immediately explain. An abandoned structure in the middle of nowhere — stone walls, a partially collapsed roof, a recently used fire — that may be explored, and what is inside may be useful.

When the trail finally converges and the silhouette of the fort appears on the horizon, the weight of arrival is greater because the distance covered was real. The bandit camp is not an improvised bivouac — it is a fort under construction: heavy wood, structure that took time and labor, elevated positions with wide visibility in every direction. The work of a group that planned to stay. Around the perimeter, loose but clearly positioned, the Velociraptors — not wild, but the same ones that attacked Dillfield, or from the same lineage, tamed enough to function as sentinels. From somewhere inside the fort, indistinct at first but present, the sound of a fight: a man's voice, loud and impatient; a woman's voice that does not back down.

**Kenny recognizes the second voice.**

## 5.9 — The First Main Mission

The rescue is the game's first main mission: enter the fort, get the mother out, leave. It rewards everything the journey taught — observation before action, reading the terrain, understanding the Velociraptor perimeter, knowing where Kenny's containment fails under pressure. In the shipped Tier 1 game it can be resolved through careful observation and avoidance combined with the direct and ranged combat layers; when the stealth layer arrives in Tier 2, this same mission becomes its showcase, deepening the planning-before-action approach rather than being the only way through. However the player gets through it, the outcome leaves marks: on Kenny's Reputation, on Richard's Respect, and on what the world remembers. This mission closes the first arc and opens the period of the game where Kenny returns to a Dillfield that needs a functioning sheriff, and the open systems take over.


---
---

# PART II — CORE SYSTEMS

---

# 6 — SYSTEM — KENNY'S VOICE AND PERCEPTION

> This is the foundational system of Project D. It is referenced by every other system and is the layer that transforms Dillfield from a set of mechanics into a place inhabited by a real man. It is the first system built and the last that can ever be cut.

## 6.1 — What the System Is

Project D is built on absence: no markers, no written objectives, no confirmations. But there is a limit to how silent a world can be before it becomes unjustly opaque. A game with zero signaling is not challenging — it is a game that abandoned the player. A playable character who never reacts to the world is not immersive — he is a puppet. The Voice and Perception system solves both problems at once without sacrificing either.

> **Kenny perceives the world before the player. What the player hears is the signal that Kenny perceived something. What the player does with that signal is entirely theirs.** Kenny's speech is not instruction. It is presence.

**What the system is not:** not a mission-dialogue system (Kenny speaks because he lives, not to signal a mission); not a voice tutorial (he never says "press this button to open the notebook"); not lore commentary (he is not an audio guide); not a suggestion system (he never says "you should talk to that person").

The mechanism that drives the entire system — how the game knows what Kenny is perceiving at any moment — is the Shared Senses (§6.2). It is built on the principle that the player and Kenny share one body, perceiving the world through the same eyes, ears, and instincts, and everything below depends on it.

## 6.2 — The Shared Senses — Player and Character as One Body

This is the input mechanism that makes everything else in this system possible, and it is the most literal expression of the project's thesis. The three perception layers described below define *what* Kenny reacts to. The Shared Senses define *how* the game knows what is reaching him to react to. Without it, Kenny is a radio playing lines at intervals. With it, the player does not merely watch Kenny perceive the world — the player perceives it *as* Kenny, through the same eyes, the same ears, the same instincts. The player's act of attending and Kenny's act of perceiving are one act.

### The Principle

Most games give the player a camera that floats independently of the character's awareness, a free eye in space indifferent to what the character himself notices. Project D does not. The camera stays with Kenny — the player watches him move through the world, reads his posture and his breathing, sees where he turns his head — but it is bound to his awareness rather than detached from it: where the player aims the view is where Kenny directs his attention, and what the player hears is what Kenny hears, spatialized through his ears and sharpened or dulled by his state. What pulls at the edge of the player's attention is what pulls at Kenny's. The goal is not a camera that merely follows a character around. It is the sensation, sustained for the length of the game, that the player and Kenny are reading a dangerous world together through one shared set of senses — the player choosing where to point them, Kenny supplying what they take in.

This inverts the normal relationship between player and avatar. In most games the character is a tool the player points at the world. In Project D the player and Kenny share one nervous system: the player provides the *direction* of attention — where to look, when to stop and listen, whether to push forward or hold still — and Kenny provides the *perception and interpretation* of what that attention lands on. The player decides where to aim the senses. Kenny supplies what those senses, honed by a life the player never lived, actually take in.

### Why Kenny Perceives What the Player Cannot

The lore makes this honest rather than a convenience. The humans of this world have senses amplified far beyond the real-world baseline (§4.3) — exceptional hearing and smell, a nervous system tuned to a level of vigilance that would be diagnosed as pathological in the real world, and at certain hours a visual advantage a screen cannot fully reproduce. Kenny is not a normal man squinting at a monitor; he is a creature built by generations of survival pressure to read a hostile environment with his whole body. So the gap between what the *player* can register through a screen and speakers and what *Kenny* can register through senses built for this world is not a limitation to hide — it is the heart of the system. Kenny fills that gap, constantly, and in filling it he becomes the player's way of perceiving a world richer than the hardware alone could convey.

### The Four Channels of Perception

The Shared Senses run on four channels operating at once. Each is a real way the world reaches Kenny, each has its own mechanism, and each can speak on its own or combine with the others.

**Sight — the Shared Gaze.** What the player looks at is what Kenny looks at. Centrality (how near the center of view something sits) and dwell (how long the player holds it) determine whether it crosses into Kenny's notice. The player looking down a long empty road sees a far-off smudge they cannot resolve; Kenny, with eyes built for distance, reads it as a structure and says so. The player did not have to identify the house — they only had to look down the road.

> *(Player looks down a long empty road; a structure sits indistinct in the far distance)* — *"...hm. Something out there. End of the road."*

**Hearing — the Shared Ear.** The player hears the world spatialized exactly as it reaches Kenny — direction, distance, and clarity all rendered through his position and his state. But Kenny's hearing is better than the player's attention, so the system does two things the player cannot do alone. It surfaces sounds at the threshold of audibility — a distant vocalization, a footstep too heavy, a snapped branch behind a ridge — by lifting them in the mix the instant Kenny registers them, so the player *hears* the thing Kenny heard rather than being told about it. And it lets Kenny interpret what the player has heard but cannot place. A sound arrives; the player turns, uncertain; Kenny already knows what it was.

> *(A deep, distant vocalization rolls across the plains at dusk; the player cannot tell direction or source)* — Kenny goes still, head tilting a few degrees. *"...that's not close. But it's hunting."*

The Shared Ear is also the channel that most often carries Kenny-led perception (below): a man with his hearing reacts to what is behind him, and the player learns to trust the turn of Kenny's head before they understand why.

**Smell — the Shared Scent.** Smell cannot be rendered to the player directly, so this channel works through Kenny and through the world's tells. When the wind carries something — blood, smoke, the musk of a predator's territory, rot, rain on the way — Kenny registers it before any of it is visible, and the player receives it as Kenny receives it: a change in his breathing, a turn into the wind, and a few words. Crucially, scent is *directional and ahead of sight*: it is the sense that most often tells Kenny what is coming before it arrives. The player who learns to read Kenny's nose learns to read the wind.

> *(The wind shifts; somewhere upwind, unseen, a kill is rotting)* — Kenny's breath catches; he covers his nose with the back of his hand. *"Something died out here. Close enough to smell. Watch the ground."*

**The Body — the Shared Instinct.** The fourth channel is not a sense pointed at the world but the world's effect registered in Kenny's own body: the prickle of being watched, the wrongness that has no source, the involuntary tightening before the conscious mind catches up. This is the channel through which the simulation's corruption leaks (the instinctive layer, §6.3, Layer 3) and through which danger announces itself below the level of sight or sound. The player feels it the way Kenny does — not as information but as sensation: his breathing changes, his posture closes, and sometimes a single uncertain word escapes before he knows what he is reacting to.

> *(An area where the world's texture pulsed for a frame the player may not have consciously caught)* — Kenny's shoulders draw in; his breath shortens. A pause. *"...something's wrong here. Can't say what."*

### How the Player Lives It — The Sensory Layer

The Shared Senses are not delivered through voice alone. They are an immersive sensory layer that uses every channel the hardware allows, always diegetically, never as interface.

- **Spatial audio is the primary instrument.** The world is mixed in full 3D through Kenny's position and orientation, and the mix is *dynamic to his state*: when Kenny is calm and rested, the soundscape is wide and detailed, full of the small sounds of a living world; when he is tense, the mix narrows and sharpens onto the threat; when he is exhausted or shaken, it thins and dulls, as a tired or frightened man's hearing narrows. The player does not read a state meter — they hear the world get smaller.
- **The screen breathes with the body, subtly.** Not effects layered on top, but the consequences of being in Kenny's body: the faint sway and rhythm of his breathing in the framing, the way the image steadies when he holds still to listen, the slight loss of edge in peripheral clarity when he is dehydrated or wounded (§9.3), the held beat of stillness when his instinct fires. These are never cosmetic flourishes; each is the visible side of a bodily state.
- **The controller is part of the body.** Haptics carry what the body feels and the eyes cannot show: the low pulse of Kenny's heartbeat rising as a predator nears, a sharp involuntary catch when his instinct registers a wrongness, the dull resonance of heavy footfalls felt through the ground before they are heard. Used sparingly and always tied to a real bodily cause, the controller becomes the closest, quietest channel of the four.
- **Silence and stillness are sensory content.** When the system has nothing to surface, the result is not emptiness but the felt presence of a calm body in a quiet place — the soundscape open, the breathing even, the world simply *there*. The absence of a signal is itself information, and the player who has learned Kenny's body feels the difference between peaceful quiet and the quiet of held breath.

None of these channels is a HUD. Every one of them is the world reaching a man and that man's body responding. The player is never *told* Kenny is afraid; the player's own ears narrow, the controller tightens its pulse, the breath in the framing shortens — and the player feels it because, for that moment, they are him.

### How It Works Mechanically

The system continuously evaluates everything reaching Kenny across all four channels and scores each candidate by weighted factors:

- **Attentional weight (sight).** Gaze centrality and dwell, as above — what the player is deliberately attending to.
- **Sensory salience (hearing, smell, instinct).** Independent of where the player is looking, the world emits perceptual events on the other channels — a sound at a given volume and direction, a scent on the wind, an instinctive trigger — each carrying an authored salience per sense. A man with Kenny's vigilance does not need to be staring at a threat to register it; salience can pull his notice on its own.
- **State modulation.** Kenny's emotional and physical state (§6.4, §9.3) scales every channel: tension sharpens hearing and narrows sight; exhaustion dulls all of them; being shaken can close a channel entirely.

The system combines these into a single perception value per candidate, applies the emotional-state gate (§6.4) and the frequency rules (§6.9), and produces a response across the appropriate channels — a spoken line, behavior without speech (§6.7), a shift in the audio mix, a haptic pulse, or, most often, nothing. The same rotting kill upwind produces different output depending on who Kenny is in that moment: a curious Kenny investigates it aloud, a tired Kenny only turns his head and breathes wrong, a shaken Kenny does not register it at all.

### The Two Directions of the Channel

The Shared Senses run both ways, and the distinction is the texture of the whole game.

**Player-led perception.** The player attends; Kenny interprets. This is the dominant mode in calm exploration. The player drives attention around the world — looking down the road, stopping to listen, turning into the wind — and Kenny supplies the reading. The player is asking, through where they aim their senses, "what is this?" and Kenny answers.

**Kenny-led perception.** Kenny perceives first; the player follows. This is rarer and heavier, and it is what makes the shared body feel alive rather than passive. Salience on the non-visual channels — a sound behind the player, a scent on a wind they cannot smell, an instinct with no visible source — reaches Kenny before the player has oriented to it, and Kenny reacts: his head turns, his breath changes, the mix shifts toward the thing, the controller catches. The player, feeling this through their own borrowed senses, turns to find what Kenny already perceived. Kenny's senses are ahead of the player's, exactly as the lore says they should be, and the player learns to trust that when Kenny's body orients on its own, there is a reason.

Most of the time the player leads and Kenny reads. Often enough, Kenny leads and the player catches up. The player never knows in advance which it will be, which keeps the simple act of moving through the world perpetually alive.

### What This System Must Never Become

It must never become an interface. No targeting reticle, no highlight, no outline, no scent-trail line painted on the ground, no sound-pulse overlay of the kind detective-vision systems use. The *only* outputs are Kenny and the world reaching him — his voice, his posture, his breathing, the spatial mix, the haptics. If the system ever resolves a perception into a visible "you are perceiving an interactable" cue, it has become the HUD the entire project exists to avoid. The discipline is absolute: perception is expressed *through Kenny's body and the world's own signals*, never through symbols laid over them.

It must also never feel like surveillance of the player's senses. Kenny does not react to everything that reaches him — that would make existing in the world exhausting and turn him back into noise. The frequency rules (§6.9) and the requirement of genuine salience or dwell mean that most of what crosses Kenny's senses passes without remark, exactly as a real person's attention skims most of what reaches their body. Kenny reacts when the combination of the player's attention, the world's salience, and his own state crosses a real threshold — not whenever the camera moves or a sound plays.

### Production Notes

The Shared Senses are built in Tier 1 as the core of the Voice system, because the Voice selection engine (§13.2) cannot function without a perception model feeding it candidates, and because the sensory layer (spatial mix, screen-breathing, haptics) is what carries the system's identity even in the long stretches when Kenny says nothing. In implementation terms, the system runs continuous queries across the four channels — view-frustum and gaze scoring for sight, audible-event detection for hearing, wind-and-proximity scent events, and instinct triggers — scores candidates, and passes the top ones both to the Voice selection engine as the "what is Kenny perceiving right now" input and to the audio and feedback systems as the sensory response. The concrete construction — which engine primitives provide each channel, how the dynamic state-driven mix is built, and which part of the model is the team's to invent — is detailed in §13.3. This is the layer that turns a bank of context-tagged lines and a soundscape into a man whose body the player is genuinely inhabiting. It is the highest creative and technical priority of the project and is prototyped first in the vertical slice (§14.2), because if the Shared Senses do not make the player feel they have become Kenny, no other system can compensate.

## 6.3 — The Three Layers of Perception

Three layers operate simultaneously.

**Layer 1 — World Perception.** What Kenny sees and hears simply by being alive in that place. The broadest and most constant layer, independent of any narrative event. Triggered by weather and environment, everyday fauna, the city functioning, and Kenny's own physical state (hunger, fatigue, old-wound pain). It manifests as the shortest, most frequent reactions — the background noise of Kenny's presence.

> *(Rain starting mid-patrol)* — *"Damn."* — and keeps walking.
> *(A small ridiculous animal trips on a rock near the stream)* — *"...dumb animal."* — with the involuntary affection of someone who didn't want to laugh but did.
> *(Passing the cemetery during routine)* — no speech; Kenny just slows his pace for a second, then returns to rhythm. It is what it is.

**Layer 2 — Social Perception.** How Kenny reads the people around him. He spent decades in Dillfield; he knows its people by type if not by name. He knows the rhythm of someone with something to hide, the difference between a man nervous from a bad day and a man nervous because he did something. Triggered by behavior outside the pattern, strangers with something wrong, suspicious group dynamics, things people do not say, and moments of common humanity.

> *(Two men dispersing too quickly)* — *"Someone must've told them I'm friendly."*
> *(A regular who averts his eyes)* — *"...Raul has something going on. I'll pretend I didn't notice for now."*
> *(A child trying to walk a huge lizard like a dog)* — *"That kid is going to get bitten in slow motion."* — with involuntary admiration for the absurdity.

**Layer 3 — Instinctive Perception.** What Kenny feels before understanding what he felt. The deepest and rarest layer — where what Kenny perceives does not come from the simulation's world but from inside him: real memories leaking irregularly as the damaged AI oscillates between collapse and stability. Triggered by proximity to lore fragments, confrontation with displaced persons, progression of server deterioration, and fragments of real-world memory. It manifests disoriented, quiet, often incomplete.

> *(An area where the world's texture pulsed for a frame)* — *"...I'm seeing things. Too hot today."* — with a hesitation that does not match the explanation he offers himself.
> *(A distant sound that does not belong)* — Kenny stops, tilts his head, looks in the wrong direction — not toward where the sound came from, but where he thinks it should have. Silence. Then: *"...where do I know that from?"* — and keeps going.

At the start of the game, Layer 3 reactions are rare and subtle to the point of almost not existing. As the servers deteriorate and the player accumulates fragments, their frequency and weight progressively increase. This progression is also expressed through the Voice Degradation system (§6.10), the late-game mechanical signature of Kenny's corruption.

## 6.4 — The Emotional Sub-System

Kenny's emotional state is not just a tone variable — it regulates whether the Voice system speaks at all.

`Perception → emotional evaluation → Kenny's state → verbal response (or silence)`

**The states:**

| State | Description | Effect on mundane comments |
|---|---|---|
| **Calm** | Default. Natural frequency. | Fully active |
| **Curious** | Something unusual in the perception field. Investigative tone. | Active; tone shifts toward investigation |
| **Irritated** | Frustration, conflict, prolonged physical discomfort. | Active but shorter, drier |
| **Tired** | Prolonged exploration, demanding sequences, sleep deprivation. | Rare and slower |
| **Tense** | Imminent danger detected, combat approaching. | Almost entirely blocked |
| **Shaken** | After emotionally heavy events: witnessed violence, death of someone close, disturbing discovery. | Default response is silence |

**Same event, different states (a lake full of frogs):**

| State | Response |
|---|---|
| Calm | *"That lake is full of frogs today."* |
| Curious | *"...there's something different in that water."* |
| Irritated | *"Damned frog noise."* |
| Tired | *"...too loud."* |
| Tense | *(silence — Kenny is not here for frogs)* |
| Shaken | *(silence)* |

**Intensity.** Each state operates at three levels: Mild (present but contained), Moderate (clearly active, tone and frequency visibly altered), Strong (dominant, behavior significantly restricted). Only one state is active at a time. Mild events raise intensity one level; strong events can jump directly to level 3. With time and absence of stimuli, intensity decays one level at a time; when it reaches zero, the state returns to Calm. **The emotional state never appears as a visual indicator or HUD text.**

## 6.5 — State Transition Priority — Collision Rules

When two triggers occur within the same evaluation window (within 3 seconds of each other), the system resolves the collision by a strict priority hierarchy. Higher-priority states always win, regardless of the lower-priority trigger's intensity.

| Priority | State | Override logic |
|---|---|---|
| 1 | **Shaken** | Overrides all states immediately. Any qualifying event (witnessed violent death, death of someone close, major disturbing discovery) forces Shaken at intensity 3, with no threshold. |
| 2 | **Tense** | Overrides Calm, Curious, Irritated, Tired. Does not override Shaken — a Shaken Kenny entering combat stays Shaken and the Voice stays silent. |
| 3 | **Irritated** | Overrides Calm and Curious at equal or higher intensity. Does not override Tired at intensity 3. |
| 4 | **Tired** | Overrides Calm and Curious at intensity 2+. Does not override Irritated or higher. |
| 5 | **Curious** | Overrides Calm only. The weakest active state. |
| 6 | **Calm** | Default. Active only when no other state has any intensity. |

**Transition delay.** When a higher-priority state overrides the active one, the system inserts a 0.5-second evaluation pause before switching, preventing jarring flips when triggers cluster. Exception: Shaken is instantaneous — the system does not buffer trauma.

**Intensity inheritance.** When a lower-priority state is overridden, its accumulated intensity is suspended for up to 10 minutes. If the overriding state resolves before that window expires, the suspended state resumes from its held intensity minus one level. Example: Kenny is Irritated at intensity 2, a predator triggers Tense, and when the predator situation resolves, Irritated resumes at intensity 1, not zero.

**The Tired exception.** Tired is the only state that modifies Voice rather than suppressing it. A Tired Kenny in Calm territory still speaks; the system applies the Tired tone and reduced-frequency modifier on top of Calm behavior. All other active states replace or suppress Calm behavior entirely.

## 6.6 — The Signaling Spectrum

Kenny's reactions cover a continuous spectrum from purely mundane to narratively loaded — without cuts, without obvious distinction between "lore speech" and "ambient speech."

| Zone | Nature | Frequency | System connection |
|---|---|---|---|
| Pure everyday | Kenny existing, no mechanical relevance | High | None direct |
| World observation | Kenny noticing something with possible relevance | Medium-high | Bestiary, Notebook |
| Social reading | Kenny reading people and dynamics | Medium | Thread, Notebook, Reputation |
| Instinctive signaling | Kenny reacting to something he cannot name | Low | Puzzle, Thread |
| Upload fragment | Memory leak or real-world perception | Very low | Puzzle, Thread, central narrative |

**The non-marker rule.** No Kenny speech has a visual marker indicating its zone. There is no "this is important" icon, no audio alert, no subtitle color change. The player learns to read weight through tone, length, and the silences around the words.

## 6.7 — Behavior Without Speech

Many reactions have no speech at all. Physical behavior — where Kenny looks, how he walks, where he stops, how long he stays still — is as much a part of the system as what he says, and is often more effective.

- **The listening pause:** Kenny stops mid-motion, tilts his head, listens two seconds, resumes. No speech.
- **The look that does not complete:** Kenny looks in one direction a second longer than necessary, then looks away — not because there was nothing, but because there was something he did not find it prudent to keep watching.
- **The unexplained detour:** facing something wrong ahead, Kenny stops, looks toward the danger, then toward the alternative path. Not instruction — the behavior of a man evaluating.
- **Breathing and rhythm:** in tense situations Kenny breathes audibly, and the rhythm in confrontation versus rest is perceptibly different. The attentive player recognizes when Kenny is more tense than the situation should warrant.

## 6.8 — Kenny's Evolution and the Base Tone

**Early Kenny:** familiar terrain. Direct tone, more humor when there is humor, more certainty when there is certainty.
**Kenny outside Dillfield:** the strangeness of processing an environment he is still learning to read. More hesitation — not of personality, but of a man outside his established repertoire.
**Kenny with accumulated fragments:** things he would say directly gain a weight he cannot name. A mundane observation ending in a silence a second too long.
**Late-game Kenny:** as server deterioration advances, Kenny changes perceptibly. He does not know what is happening to him; the player begins to. The gap between what Kenny feels and what the player understands reaches its maximum — and that is the design functioning as built.

**The base tone:** a man of few words who uses what he has with precision. Not eloquent. Not poetic. But not stupid — a man who learned to save words because he grew up where excess noise drew the wrong kind of attention. When something has real emotional weight — his mother, the sheriff, someone he lost, what he is becoming — the tone gets quieter, slower, with more space between words. Not because he is being dramatic, but because he is being honest.

**What the system never does:** Kenny never repeats the same line in the same context in the same session; never says something that only makes sense if the player is pursuing a specific objective; never uses vocabulary that does not belong to him (system terminology, mechanic jargon, fiction-breaking references); never comments on the obvious; never speaks about himself in an expository way.

## 6.9 — Line Volume and Frequency Specification

The combinatorial pressure is real: six states × three intensities × three layers × four time-of-day bands × five story stages produce a space too large to cover completely without perceptible repetition. The practical response is not to cover every combination but to identify the most frequent trigger combinations and prioritize coverage there, accepting that rare combinations reuse lines. A player encountering a specific combination for the third time has played long enough that some repetition is acceptable.

**Minimum functional volume for shipped Tier 1:** approximately 3,000–4,000 unique lines of ambient and reactive dialogue across all zones. This is the floor below which repetition becomes perceptible within a single session for the most common combinations.

| Zone | Estimated lines | Reasoning |
|---|---|---|
| Pure everyday | 800–1,000 | Highest frequency; repetition most visible |
| World observation | 600–800 | Medium frequency; context reduces need |
| Social reading | 400–500 | Lower frequency; NPCs and situations vary naturally |
| Instinctive signaling | 200–300 | Low by design; each line carries more weight |
| Upload fragment | 80–120 | Very low; lines are individually memorable |

These assume a 15–20 hour playthrough and scale upward for longer runs. State and context filtering mean not all lines are accessible in every session, which significantly reduces the effective repetition rate. This is the single largest content-budget item in the project; voice direction, recording, and editing are planned against these numbers before other production commitments are made.

**Frequency rules — numerical.** "Kenny does not comment on every tree" requires numbers.

| Zone | Minimum cooldown | Maximum per 10 minutes |
|---|---|---|
| Pure everyday | 45 seconds | 4 |
| World observation | 90 seconds | 3 |
| Social reading | 120 seconds | 2 |
| Instinctive signaling | 5 minutes | 1 |
| Upload fragment | 20 minutes | 1 |

Cooldowns are per zone — a Zone 1 line does not block a Zone 2 line, but two Zone 1 lines cannot fire within 45 seconds of each other. When Kenny is in Tired (intensity 2+), Tense (any), or Shaken (any), all cooldowns double. **The silence rule:** if no ambient speech fires in a given 3-minute window during open exploration, the system does not force a line to fill the silence. Silence is not a bug; silence is Kenny. The system fires only when a genuine trigger exists — never to prevent quiet.

## 6.10 — Voice Degradation — The Mechanical Signature of Corruption

This is how the lore's central horror — the progressive corruption of Kenny by failing servers — becomes a system the player feels rather than only hears described. It is the purest expression of the project's thesis: the player knows what Kenny cannot.

**The principle.** As server deterioration advances in the late game, specific Voice lines the player heard reliably in the early and mid game begin to disappear from Kenny's repertoire — not because they were cut, but because, within the fiction, the code that defines Kenny has lost access to them. Kenny does not notice. He cannot notice an absence in himself. The player who paid attention does.

**How it works.** Each Voice line is tagged with a corruption-eligibility flag. A subset of established, recurring lines — chosen specifically because the player will have heard them often enough to register their absence — become eligible for removal once the Thread crosses the intermediate simulation-knowledge threshold (§7.5). From that point, the system progressively retires eligible lines from Kenny's accessible pool, weighted toward the lines most associated with who Kenny was: his characteristic humor, his particular turns of phrase, the small affectionate observations that defined his early-game presence.

**What replaces them.** A retired line is not simply silence. In its place the system substitutes one of three responses, chosen by context:
- **A flattened version** — the same observation delivered without the warmth or wit it once carried. Kenny still notes the ridiculous animal, but the affection is gone from his voice.
- **A nothing** — where Kenny would once have spoken, he passes in silence. The attentive player feels the held breath where a familiar reaction used to live.
- **A fragment** — occasionally, the retired line is replaced by an instinctive-perception line: Kenny reaching for a reaction he no longer has and surfacing, instead, a leak from the real world.

**Calibration.** Degradation is gradual and never total. The game never strips Kenny of so much that he becomes unplayable as a character — the goal is the felt sense of a man thinning out, not a silent protagonist. The rate is tied to Thread progression, not to playtime, so a player who advances the narrative experiences degradation in step with the story's escalation. A player who plays slowly and explores broadly experiences a slower thinning, which is correct: Kenny corrupts as the story corrupts him.

**Why this matters as a system, not just a moment.** A single late-game cutscene could state that Kenny is being corrupted. Voice Degradation makes the player *live* the corruption across hours, through the accumulated memory of who Kenny used to be. It costs no additional art and little additional writing — the lines already exist; the system is in how they are withdrawn. It converts the game's most abstract horror into its most intimate one.

## 6.11 — Known Risks

1. Insufficient variation volume produces perceptible repetition.
2. The system talks too much and becomes noise.
3. Instinctive perception lines lose impact if too frequent.
4. Behavior-without-speech requires quality animation to land.
5. Poorly calibrated emotional transitions break the real-character illusion.
6. Line-volume budget underestimated, leading to a mid-production content crisis.
7. Early-game Voice density too low to create streaming-worthy moments before disengagement.
8. Voice Degradation tuned too aggressively, hollowing the character before the player has bonded with who he was.
9. The Shared Senses tuned so Kenny reacts to too much of what reaches him, making existing in the world exhausting and turning perception into a chore.
10. The Shared Senses tuned so Kenny reacts to too little, breaking the sense that the player and Kenny share one body and making the world feel unperceived.
11. The sensory layer (dynamic mix, screen-breathing, haptics) overdone, tipping from felt immersion into gimmick, or so subtle the player never registers Kenny's body responding at all.
12. Salience-driven (Kenny-led) reactions firing without a discoverable cause, training the player to distrust Kenny's attention rather than trust it.


---

# 7 — SYSTEM — THE NOTEBOOK, THE DRAWINGS, AND THE THREAD

> Project D is a game about a man who does not know what he is, in a world that does not explain what it has. The tension between what exists and what is discovered is the engine of the experience. Three mechanisms serve that tension: the Notebook receives and organizes, the Thread responds, and Kenny's Voice connects the two — the signal that precedes the record and the delivery that leads to the event.

## 7.1 — Why These Mechanics Are the Foundation

For the tension to work, the game needed a system that **receives** what the player finds (conversations, events, glitches, encounters, fragments), **organizes** it so the player can revisit and connect, and **responds** invisibly to the accumulation of discoveries — advancing the narrative without announcing it. None of these functions could be fulfilled by a conventional mission system, map markers, or any structure that informs the player what is important.

## 7.2 — The Notebook

### What It Is

The Notebook is Kenny Collins's work diary. Not a lore inventory, not a world encyclopedia, not a mission system in disguise. It is the physical object a sheriff who can barely write carries and uses the only way he can: jotting down what he does not want to forget, with the words he has — and drawing when words do not come. It is a separate object from the Bestiary (which is exclusive to fauna). The Notebook records everything else: conversations, places, events that did not immediately make sense, names, dates, behaviors, memory fragments, observed glitches, and the connections the player is trying to make.

### How It Arrives

The Notebook is not explained. There is no tutorial screen. It appears one early morning when the sheriff places it on the table in front of Kenny and says a deputy who cannot write is half the service. Kenny looks at it as if it were a trap. He keeps it. From that moment it is in his inventory forever, openable at any time. The player decides what to note and when.

### The Organic Sections

| Section | What Kenny records |
|---|---|
| **People** | Names, descriptions, where he met them, what they said, what they did not say |
| **Places** | Properties, roads, regions — what they have, what is missing, what seems wrong |
| **Events** | What happened, when, who was there, what resulted |
| **Drawings** | Faces, locations, structures, memory fragments, and creatures — everything Kenny represents visually because words do not reach. Fauna sketches are organized separately and form the direct bridge to the Bestiary |
| **Don't Know What This Is** | Fragments without category — glitches, memories that do not belong, things that do not add up |

The "Don't Know What This Is" section carries the most bonus weight for the Thread. It is where unexplained fragments are kept until the player understands what they were.

### Kenny's Writing — Development Through Practice

Kenny can barely write. The first Notebook pages read like watching a child learn to write in real time: swapped letters, words cut in the middle, sentences that start without finishing, invented spellings for sounds he knows but cannot represent. Progression is through practice — writing is one of the game's learning skills and, like all of them, evolves only through real use. This is why it is strongly to the player's benefit to start using the Notebook as soon as the mechanic is freed, even if the first notes are bad — especially because they are bad. NPCs and documents can accelerate development but do not substitute for practice; an NPC teacher offers corrections, a well-written diary found on a farm produces a perceptible improvement in subsequent entries.

**The form of the degradation: functional degradation with cosmetic expression.** The content of each entry is always intelligible — the game never produces literally unreadable entries. What degrades is the form: spelling inconsistencies, fragmented structure, missing words, invented phonetic spellings. The player always understands what Kenny was trying to say; what they see is the struggle of saying it. Early entries are written clean first, then given a controlled degradation pass — phonetic misspellings consistent with how a man with Kenny's speech patterns would approximate an unfamiliar word, never random errors. This treatment applies to roughly the first 30–40% of Notebook entries by volume, tapering as Kenny's writing develops. Each localization requires its own degradation pass native to that language's phonetics; it is not a find-and-replace job. If any entry is narrated, the delivery reflects the content — halting, uncertain, self-correcting.

### What the Notebook Does Not Do

It never indicates what the player should have noted, never signals when a note becomes relevant, never automatically connects related entries, never confirms when the player reached a correct conclusion, and never displays a completion percentage. **The connection work is entirely the player's.** The Notebook provides the record; the interpretation is human.

### Limits and Optionality

The Notebook is not infinite, and the player does not decide its contents freely — everything Kenny notes and draws belongs to the game world. At 100% game completion, where everything that exists has been discovered, the Notebook is complete with no blank pages. The Notebook is also entirely optional: a player can finish the game without opening it once. The Thread does not depend on it. What the Notebook changes is not progression but **comprehension** — the difference between playing with and without it is the difference between understanding the revelations and merely receiving them.

### Tier 1 Notebook — Scope Without Drawings

Because the Drawings section ships in Tier 2 (see §14), the Tier 1 Notebook functions on four sections: People, Places, Events, and "Don't Know What This Is." It records text, supports the player's connection work, and feeds the Thread's Notebook bonuses fully. What the Tier 1 version lacks is the visual bridge to the Bestiary and the memory-fragment drawings — meaning that in Tier 1, the Bestiary is fed through Binoculars, NPC conversation, and field documents only, and memory fragments are recorded as text in "Don't Know What This Is" rather than sketched. The Tier 1 Notebook is complete and coherent on its own terms; the Drawings section deepens it without being required for it to function.

## 7.3 — The Puzzle — The Truth Kenny Does Not Know

The truth about what Kenny is — that he lives in a simulation, that the upload happened, that death is permanent, that the servers are being destroyed as he exists inside them — does not arrive as a revelation. It arrives as accumulation. The puzzle is not an enigma with a single hidden solution; it is the progressive reconstruction of a reality the game never directly names. The fragments exist scattered throughout the journey, and the work of connecting them is entirely the player's. No system confirms a correct connection.

**How the revelation actually works.** For most players, the core revelation arrives in late-game scenes — cutscenes and scripted moments that deliver the information directly. The puzzle does not replace those scenes; it precedes them. What the puzzle changes is the emotional register in which those scenes land. For the player who accumulated fragments and drew connections, the late-game scenes are confirmation of what was already feared. For the player who did not, they are news. Both are valid experiences of the same events. The puzzle is the mechanism of enrichment, not of delivery.

**The three types of fragment.**
- **Kenny's memory fragments** — involuntary episodes: images of places that do not exist in the Old West, sensations of artificial light, voices Kenny does not recognize but that seem to recognize him. They arrive abruptly, without context, unmarked.
- **Glitches and distortions** — events of the world, not technical failures: a texture pulsing for a frame, a shadow with the wrong shape, an NPC who freezes for half a second and resumes as if nothing happened. The first time, the natural reading is "bug," and the game does nothing to correct that impression.
- **Encounters with displaced persons** — conversations with people who arrived from other simulations, each telling a different part of the story without ever having the complete vocabulary to articulate it.

**How fragments connect.** The central mechanism is cross-referencing between different sources. An isolated fragment explains nothing. Two fragments from different sources that "rhyme" — describing the same thing from different angles — begin to form an image. Three or more create structure. The Notebook is where this cross-referencing happens, not because the game maps connections automatically, but because the player who rereads what they accumulated can see two records pointing at the same thing.

**The two fragment registers.** Subtle fragments arrive without marking, indistinguishable from world texture until other fragments make them legible — the ones the inattentive player misses, and the ones with the greatest impact when the attentive player connects them. Obvious fragments arrive with weight: the glitch too large to ignore, the encounter too strange, the conversation that drops something the player cannot discard. Even these do not deliver the answer; they deliver a fragment that still needs connecting.

**The failure case — the player who reaches the end without connecting.** This player arrives at the late-game events with less internal context. The revelation lands as new information from outside, not as confirmation of a suspicion. This is not a broken experience; it is a shallower one, and that distinction shapes how the late-game scenes are written. **The late-game revelations are designed to function on two levels simultaneously.** At the surface level, they are legible and emotionally affecting for a player encountering these ideas for the first time — the scene carries its own weight without assuming prior knowledge. At the deeper level, for the player who connected fragments, the same scenes feel like arrival rather than arrival *and* information; the attentive player does not receive news, they receive confirmation of what they feared. The game does not penalize the non-connecting player by making the ending incomprehensible. The story closes, the necessary questions get answers, and the hundred-year cliffhanger lands with the weight it needs for both players — though the player who built the context feels it more personally. The asymmetry is the intended result of a system that rewards attention without punishing its absence.

## 7.4 — The Drawings

### Why Kenny Draws

When words do not come — which is frequent — Kenny resorts to what he has: the blank pages of the Notebook and the graphite pencil tied to the cover by an old elastic band.

### How It Works

The player can open the Notebook at any time and, in the Drawings section, try to visually represent anything they saw or are seeing. The interface is deliberately limited — the digital equivalent of a pencil on paper, not an illustration program. A finished drawing works as an identification key: Kenny can show the page to NPCs with relevant knowledge, who respond according to what they see. What an NPC can identify depends on two combined factors: the quality of the drawing (the player's effort and Kenny's current skill) and the NPC's knowledge (each character knows what their life made them know).

### Drawing Input — Platform Design

Drawing with a mouse or analog stick as a primary mechanic is not a trivially solved interface problem, and Project D's drawing mechanic is load-bearing: quality affects NPC responses, Bestiary access, and Thread weight. A frustrating input layer would make players abandon the mechanic and undermine the Notebook system.

**The solution is shape-based approximation, not freeform drawing.** Rather than producing freeform art, the player works from a constrained vocabulary of marks — lines, curves, ovals, triangular forms, proportional guides — placing and adjusting them on the page. The system reads the combination and proportions of marks, not the smoothness of a continuous line. Results *look* like rough sketches because the marks are simple, while the input is achievable on any platform. A mouse refines placement faster; a controller produces a recognizable approximation without the fine motor precision analog sticks cannot deliver. **Quality is determined by completeness and proportion, not line smoothness.** A drawing that captures the general body ratio of an animal (long neck, quadruped, large) reads as a recognizable attempt even with rough lines. A drawing with wrong proportions — a long-necked species sketched with a neck as short as its body — confuses NPCs even with perfectly placed lines. The challenge is observational, not manual. Both platforms use the same interface model and have no significant gameplay advantage.

### Drawing Recognition — Implementation Specification

The system needs to compare a player's arrangement of shapes against a reference and determine whether the result is recognizable, and as what. This requires three components.

**1. A shape reference library.** Every drawable subject — creature, location, face, object — has a reference profile defining which marks in which spatial relationships constitute a recognizable approximation. For fauna: body length-to-height ratio, number and placement of limbs, presence or absence of distinctive features (frill, crest, long neck). For faces: relative position of eye marks, identifying features (scar, hat, beard marks). These profiles are authored by the design team as data, not generated content.

**2. A proportional matching algorithm.** On submission, the system calculates how many required marks are present, their spatial relationships relative to each other, and how closely those relationships match the reference profile, producing a match score from 0 to 100. The technical foundation for this is established rather than invented — a geometric point-cloud recognizer of the kind detailed in §13.5 handles whole-shape similarity, with a small proportional pass layered on top to judge part-to-part ratios — so the design work here is authoring the reference profiles, not building a recognizer from nothing.

**3. Recognition thresholds.**

| Score | Recognition level | NPC response |
|---|---|---|
| 0–29 | Unrecognizable | NPC cannot identify; responds generically |
| 30–49 | Partial | NPC identifies category (animal / person / structure), not species or individual |
| 50–74 | Recognizable | NPC can identify the subject if they have relevant knowledge |
| 75–100 | Clear | NPC identifies and provides full information within their knowledge domain |

**How Track interacts with quality.** Track does not affect the recognition threshold — it affects the vocabulary of marks available. Early Kenny can only place basic shapes, so his maximum achievable score is roughly 50–60 because finer details cannot be expressed. Late Kenny, with an expanded vocabulary, can reach 75–100 on the same subject. In practice: a player who tries hard with early Kenny's basic marks might reach 55 (recognizable but not clear — the NPC identifies the animal but can't give full detail); a player who makes no effort with late Kenny's full vocabulary might reach 30 (partial only). Effort matters throughout; Track expansion raises the ceiling, not the floor. The tamer's *"Does this have four legs?"* is the correct response to a score in the 30–49 range — not charity, but the system working.

### What Kenny Draws

Unknown creatures (the direct bridge to the Bestiary); location maps (floor plans, alternative routes, enemy camp layouts); faces (people Kenny wants to remember or who disappeared); objects and structures (marks on a stone, mechanisms he did not understand, writings in unknown languages); and memory fragments — the most disturbing drawings in the Notebook, depicting places that do not exist in that world, impossible architectures, artificial lights, faceless contexts. As Kenny's drawing Track increases through practice, the mark vocabulary expands — finer curve tools, proportion controls, detail marks for texture and surface features. Early Kenny draws blobs and angles; late Kenny draws recognizable animals with indicated scale and behavioral posture. The progression is visible in what the interface lets him do, not in what his hands can physically accomplish.

Memory-fragment drawings add extra weight to the Thread beyond what the originating event generated. Each attempt to visually record a fragment, however imprecise, counts as additional bonus.

## 7.5 — The Thread

### What It Is

The Thread is the narrative progression system of Project D, and it is completely invisible to the player. It tracks what the player **does** — completed missions, conversations had, locations visited, documents read, encounters completed, glitches observed, hours in the field — regardless of whether the player ever opens the Notebook. As accumulated actions reach certain thresholds, the game responds: an event happens, an encounter becomes possible, a cutscene activates, a layer of narrative opens. The player never consults the Thread, never sees a percentage, bar, or notification. What they feel is that the world is responding to what was done.

### What the Thread Tracks

**Primary actions** (what any player accumulates by playing): completed missions; conversations with NPCs carrying lore; encounters with displaced persons; location exploration; documents read; glitches witnessed; time in the field.

**Notebook bonuses** (additional weight for those who record): each fragment or glitch recorded in "Don't Know What This Is"; each memory-fragment drawing (worth more than simply having the episode); the complete signaling loop (Kenny reacts → player investigates → player notes — worth more than the action alone); drawings shown to NPCs when the reaction is special.

The thresholds are not fixed points on a straight line — they are weights in multiple categories that must be reached in specific combinations to activate specific events. Two players can reach the same event by completely different paths. The Thread values real effort, not action volume.

**Example thresholds.** *First — The Weight of the Deadline:* Kenny begins to understand a limit exists. Reached by any player who advances the main narrative and has had at least one encounter with a displaced person. *Intermediate — The System and What It Is:* Kenny accesses fragments connecting what happens to him to something larger — the servers, the attack, UpClouD. Requires significant game volume; this is also the threshold that activates Voice Degradation (§6.10). *Final — The Hundred Years:* the revelation of the number. Requires the largest volume of all and cannot be reached without real hours of exploration, expeditions, and narrative progression.

### Anchoring Thresholds to Fictional Time

Thresholds are gated by two conditions simultaneously: accumulated action weight, and a minimum of elapsed in-fiction time (see §11). An efficient player who accumulates the action weight for the intermediate threshold in a short span of real play does not trigger it until the fiction's calendar has also advanced the minimum required season(s). This keeps the timeline coherent — the player cannot outrun the story's plausible pace — and prevents the verisimilitude collapse of major revelations arriving while the world still looks like the first week. The action requirement ensures the player earned it; the time requirement ensures the fiction can bear it.

### How Events Are Delivered

When a threshold is reached, the corresponding event does not trigger immediately. The Thread enters a waiting state and waits for the player to be in a situation appropriate for a weighty delivery: a camp set up outside Dillfield, the return to the city after a long expedition, the interior of the sheriff's office at the end of the day — any moment when Kenny is in less urgent movement and the environment is not actively hostile. When this window appears, the Thread activates the Voice, which leads the player to the event through a Kenny speech. Not an instruction — Kenny thinking out loud, with the weight of what he has accumulated that day.

**Example delivery variants for the same threshold:**
> *(At camp after a difficult expedition)* — *"What a week that was... already lost count of how many days I've been out. Need to stop by the sheriff's office, see if something happened I don't know about."*
> *(In an unknown village far from Dillfield)* — *"This place isn't my place. I've been here too long. Dillfield is waiting — and so am I."*
> *(Resting in an abandoned barn)* — *"...I've got something in my head I can't shake. Can't even explain it right. I think I need to talk to someone I trust."*
> *(Returning to Dillfield after a night away)* — *"Good to be back. Strange feeling, like something's different. Going to walk around the city before I sleep."*

### The Thread and Glitches

**As input:** observing a glitch counts as a primary action regardless of the Notebook; recording it in "Don't Know What This Is" increases its weight. **As output:** when the Thread activates a weighty event, it frequently uses a glitch as the vehicle — the world presents the event not as a cutscene interrupting the game, but as a reality distortion that is an organic part of what the damaged simulation does.

### Waiting State — Safety Mechanisms

The waiting state requires explicit safety mechanisms for edge cases where no appropriate window appears in an acceptable timeframe.

1. **Maximum wait cap.** No event waits longer than 90 minutes of real gameplay after a threshold is reached. If no natural window has appeared, the system widens its definition of an acceptable window, accepting lower-intensity moments it would otherwise have held for. The player notices nothing; the event arrives slightly less perfectly timed but arrives.
2. **Minimum window definition.** A delivery window is any continuous 3-minute period where Kenny is not in combat, not in a high-tension animal encounter, and not in a mandatory scripted sequence. This is intentionally broad — traveling in open country, walking through Dillfield, sitting at a campfire, examining a document all qualify.
3. **Stacked threshold queue.** If multiple thresholds are reached while the first still waits, they queue internally, maximum depth 2. If a third is reached while two are queued, the oldest is delivered at the next available window regardless of timing quality, to prevent queue overflow.
4. **Return-to-city trigger.** Any time Kenny enters Dillfield after being away more than 30 minutes of real gameplay, the system checks for pending deliveries and treats the entry as an eligible window for the oldest queued event. This covers the most common pattern — extended expeditions followed by return — and ensures the city itself becomes associated with meaningful narrative arrivals.

### First-Session Guarantee

To serve both the early-engagement need (§2.7) and reliable onboarding, the Thread guarantees one weighty narrative delivery within the first stretch of open play after the prologue. This delivery uses the standard waiting-state windowing so it still feels organic, but its threshold is calibrated low enough that any player who leaves Dillfield and engages with the world at all will receive it. It is the player's first concrete proof that the world responds to what they do — the moment that teaches, without a tutorial, what kind of game this is.

### The Two Player Profiles the Thread Sustains

The player who plays without the Notebook advances through the story, reaches the main events, and lives the revelations — sometimes arriving at certain revelations without enough context to fully understand them. The player who uses the Notebook frequently accumulates extra weight in certain categories and arrives at the same revelations with more layers, recognizing connections before they are made explicit and understanding what Kenny is feeling because they noted the fragments that built that feeling over hours. The Thread does not favor either; it sustains both.


---

# 8 — SYSTEM — THE BESTIARY, BINOCULARS, WINDOWS, AND DOMESTICATION

> These four systems exist in direct relation: Binoculars feed the Bestiary, Windows define what the Bestiary can or cannot access, and Domestication depends on the Bestiary to be executed with competence.

## 8.1 — The Binoculars

### What They Are and How They Arrive

The Binoculars are an inventory item — a medium-range observation tool that allows examining creatures and environments at distances that would otherwise require dangerous proximity. Not a special gadget; work equipment of the type any man who deals with fauna in open country eventually acquires. They are available for purchase at Dillfield's shop from the beginning — not a mission reward, not hidden, not unlocked. The prologue creates the need before the item is in the inventory: at some point the player is in a situation where they would need to see something far away. The situation creates the desire before the system exists. When the player sees the Binoculars in the shop catalog, what happens is recognition, not discovery: *"this is what I needed."*

### How They Work

**Basic state** (Bestiary not filled for that species): the Binoculars allow seeing the creature with visual clarity — reading behavior in real time, identifying physical signals, observing unusual characteristics. Nothing is automatically delivered in text. The player sees; the player interprets. The Binoculars make vision possible safely; they do not make what is seen legible without effort.

**Complete cataloging state** (Bestiary at 100% for that species): pointing at an individual displays all Bestiary information contextually — documented behavior, threat level, attack and flight patterns, strengths and weaknesses, accumulated notes.

### Uses Beyond the Bestiary

Environmental reconnaissance before entering unknown territory; human threat evaluation (bandits at distance before any decision); identifying displaced persons (certain individuals carry physical or behavioral signals); item and structure location without map markers; anomaly monitoring (observing strange behavior without provocation); weather and environment reading (storm formations, fauna concentration, migration patterns). In Active Memory Mode (§10.6), part of the Binoculars' function integrates into natural navigation: approaching a fully cataloged species with the mode active displays its information without manually equipping the Binoculars. Uncataloged species remain opaque even with the mode active.

## 8.2 — The Bestiary

### What It Is

The Bestiary is the progressive fauna catalog of Project D — a separate object from the Notebook, its own archive specific to fauna. Within the fiction, it originates in the sheriff's role: with the return of dinosaurs, one of the sheriff's functions is to keep a record of present species — to inform the population about threats, document incidents, and have reference when something new appears. The empty record is there when Kenny assumes the role. What goes into it, from that point, is what the player does.

### Entry Composition

| Field | What it records |
|---|---|
| **Name** | The name Kenny knows — regional common name, tamer nickname, sometimes scientific name |
| **Physical description** | Size, covering, coloration, distinctive characteristics. Accumulated by observation |
| **Behavior** | Activity pattern (day/night/both), territorial or nomadic, solitary or group, aggression level, known attack triggers |
| **Threat level** | Kenny's practical assessment in his own tone — *"Dangerous if cornered. If you don't provoke, no problem."* or *"Avoid. No exceptions."* |
| **Attack patterns** | How it attacks, when, what it does after |
| **Flight patterns** | How it reacts to threat, when it flees vs confronts, what signals retreat |
| **Strengths** | What makes it especially difficult |
| **Weaknesses** | What works against it. Accumulated through experience or NPC information |
| **Kenny's notes** | The most personal field — observations that fit no category above, practical or the result of an encounter Kenny does not want to repeat |
| **Cataloging status** | Completeness, invisible as a number but readable in the entry's visual state |

### How the Bestiary Is Fed

Direct observation with Binoculars (the main source; required time, distance, and conditions vary by species); observation without Binoculars (works but requires real proximity, with risk proportional to aggressiveness); conversations with NPCs (each character knows what their life made them know — a Dillfield tamer knows regional species, a passing traveler may know species from regions the tamer never saw); Notebook drawings shown to NPCs (the contact point between Notebook and Bestiary — a fauna sketch recognized by a knowledgeable NPC can originate a direct entry; this path is a Tier 2 feature); documents found in the field (naturalist diaries, incident reports from previous sheriffs, breeder letters, fauna guides with engravings); and direct experience in combat or interaction (certain fields, especially Kenny's Notes, come only from real contact).

### Cataloging Progression

| Stage | State |
|---|---|
| Empty entry | Only the name, if Kenny has heard it mentioned |
| Initial partial | First filled fields — usually physical description and basic behavior |
| Functional | Behavior, threat level, and attack patterns filled. The point where the Bestiary becomes genuinely useful |
| Complete | All fields filled. Binoculars display all information when examining an individual |

### The Bestiary and Anomalies

The Bestiary does not have separate entries for anomalies. An anomaly is an individual of an existing species, not a new species. When the player examines an anomaly with the Binoculars, the reading does not match what the Bestiary says — and that mismatch is the signal. An animal whose behavior should be fully legible after complete cataloging is doing something the Bestiary does not predict. The complete Bestiary makes anomalies detectable; without the reference of the normal pattern, deviations are invisible.

## 8.3 — Windows — Species Rarity System

### What They Are

Windows are specific appearance conditions that determine when and where certain species appear. A species with a Window is not always available in the world — it exists only under precise conditions of time, weather, terrain, and sometimes world-event state the player does not control. The name is internal to development; the game never uses the word "Window."

**Time conditions:** species that exist only in specific windows — dusk when light changes tone, the hours before dawn when temperature drops, the peak of midday heat when most animals retreat. **Weather conditions:** low fog, moderate rain, the dry period after days of rain, the muggy weather before a storm. **Terrain conditions:** specific valleys, slopes with particular sun exposure, proximity to watercourses of a certain size, minimum altitude, vegetation type. **World-state conditions:** Windows that open only as a function of uncontrolled events — a herd migration attracting opportunistic predators, a season affecting territoriality, a long-term weather event that temporarily altered a region's ecosystem.

### The Indirect Trail

Everything that exists in the game has at least one trail: a conversation that can happen, a text that can be found, a story someone carries and tells if the player stops to listen. There is no creature, mechanic, or secret that exists without the world around it knowing about it in some way. The information is there; the player who goes after it finds it.

> An old tamer in a city two days' ride from Dillfield mentions, amid a conversation about training, that his father avoided a certain region after summer rains because there was "something the pack animals could not stand being near." He does not know the name or what it was. But the description of his animals' behavior is specific enough that a player with the Bestiary partially filled can recognize the pattern.

> A diary entry marked with three red slashes in the margin describes an encounter at dusk, in low fog, on a specific slope. The creature has no name — the writer never knew how to identify it — but he describes the smell the wind brought before the encounter. That detail connects this entry to a hunter's speech in Dillfield the player may have heard weeks ago, or may not have heard, if they passed without stopping.

Windows and anomalies both ship in Tier 2 (§14); the Tier 1 Bestiary covers always-available species and the core observation loop.

## 8.4 — Domestication

### What It Is

Domestication is the system by which Kenny learns to tame dinosaurs and eventually keep them as work tools, mounts, and combat aids. It is not available from the start; it becomes accessible progressively, conditioned by built relationships and accumulated knowledge. The lore premise: taming dinosaurs is a trade — not an innate ability, not an experience-point progression. It is knowledge that takes decades to build, transmitted through specialized families, requiring a repertoire of reading animal behavior most people never develop.

### Dependency with the Bestiary

The Bestiary informs Domestication: attempting to tame a species without the functional Bestiary profile is working without basic information — behavior patterns, aggression triggers, stress and receptivity signals are all there. Domestication, in turn, fills the Bestiary with exclusive information: certain fields come only through domestication contact — how the creature responds to conditioning, what makes it back down without attacking, what works as positive reinforcement, what must never be done during the approach.

### The Three Phases

**Phase 1 — Outside the system.** At the start, Kenny cannot tame dinosaurs — not communicated as a menu restriction, simply true within the world. Before departing Dillfield, the oldest tamer offers Kenny "half an hour to learn what he will need to not die in the first hour." That half hour is not domestication; it is basic survival — what not to do near wildlife in open country. In this phase the player observes domestication from a distance; Kenny does not participate.

**Phase 2 — Group learning.** Access begins with a specific relationship. When the Bond with a tamer reaches the right point, the tamer begins including Kenny in operations. Kenny's role at first is support — physical presence on the perimeter, control of variables the tamer specifies, active observation. He does not lead, interfere, or apply technique, because he has none. Each successful operation teaches through exposure. The player does not execute the domestication; the tamer NPC does. What the player controls is Kenny's support role — positioning, timing of support actions, management of external interference.

**Phase 3 — Solo domestication.** Phase 3 emerges in the mid-game as a possibility, not a time-invested conquest. It happens when the player built the right foundation and the right moment appears. The tamer evaluates what he saw over months of group operations and makes an observation — about an instinct Kenny showed, about how he read an animal before the tamer needed to name what was happening — and says something that is simultaneously recognition and permission: *"You can try."* Restrictions: by species (low-aggression species accessible first); by knowledge (the functional Bestiary is not strictly mandatory but the error probability is substantially higher without it); by condition (Kenny's state, time of day, terrain, presence of external interference all affect the operation). Phases 2 and 3 ship in Tier 2 (§14).

### The Bond With the Animal

A tamed dinosaur is not an inventory item. It is an animal conditioned for a specific relationship with Kenny: it responds to him specifically, not to any human; its trust level affects what it does under pressure; and the bond is built through use and time — a dinosaur Kenny does not use for long will slowly decondition. Beyond species fields, a tamed individual receives its own personal note within the entry — the most intimate record in the Bestiary.


---

# 9 — SYSTEM — TRACK, CONFRONTATION, AND THE WEIGHT OF THE BODY

> These three systems share a philosophy: they operate in the world, not on the screen. The player never consults a level bar, never reads a progression percentage, never receives a blinking icon warning about their own hunger.

## 9.1 — Track — Invisible Progression System

### What It Is

Track is Project D's progression system. It exists, operates, and has real effect on every aspect of the game — and the player never accesses it directly. No statistics menu, no points to distribute, no screen showing levels. The system exists within the world, not above it, on three planes: **Kenny's Track** (the playable character's progression, growing with real skill use, exposure to survived high-risk situations, and accumulated recorded knowledge); **NPC Track** (each named NPC's competence, fixed in production, learned by the player through interaction rather than a label); and **Animal Track** (the real threat degree of each species, and the variation between individuals within a species).

### How Kenny's Track Grows

Kenny does not gain experience by completing missions or killing enemies. He gains it by doing things. The system silently measures real use in each competence area separately.

| Area | What grows it | Visible effect |
|---|---|---|
| **Fighting** | Real confrontations, survived, against humans and animals | Combat reading improves; Kenny anticipates earlier, positions better |
| **Tracking** | Notebook use in the field, observing and recording fauna behavior, trail-following expeditions | Kenny begins to verbalize environmental observations that previously passed in silence |
| **Field Survival** | Camping nights, managing hunger and thirst under pressure, using natural resources | Weight of the Body penalties appear later and recover faster |
| **Medicine** | Treating own and companion wounds, correct use of materials, survived crisis | Status-effect treatment becomes more efficient |
| **Fauna Knowledge** | Directly with the Bestiary — the same system from another angle | Kenny's Voice around known species becomes richer, more specific |
| **Domestication** | Exclusively with real domestication operations | Operations previously requiring a veteran companion become possible with less experienced ones |
| **Leadership** | Use of the Gang on expeditions, decisions affecting companions | Companions respond differently — more proactive, more willing to risk |

### Track — Mechanical Specification Framework

The structural parameters below define the categories and logic; precise numerical values are to be determined by empirical testing with prototypes.

**Each axis operates on a 0–100 internal scale, divided into four tiers:**

| Tier | Range | Label | What changes |
|---|---|---|---|
| 1 | 0–24 | Novice | Kenny's baseline. No special behaviors. Voice reactions vague or absent in this area |
| 2 | 25–49 | Developing | First perceptible changes in Voice specificity and world reaction. Domain NPCs begin treating Kenny differently |
| 3 | 50–74 | Competent | Meaningful capability unlocks. Solo Domestication opens at this tier in the Domestication axis. Voice reactions become specific and reliable |
| 4 | 75–100 | Expert | Full capability. Domain NPCs treat Kenny as a peer. Voice reactions match a man who genuinely knows the domain |

**Accumulation — the unit is "meaningful action," not "any action."** Each unique context of skill use contributes full weight (a new enemy type, a new wound type, a new terrain to camp in). Repeating the exact same action type within 30 minutes of the last instance generates 20% of normal weight — the system measures breadth, not repetition volume. High-stakes survival of a skill use — Fighting through an encounter genuinely dangerous for Kenny's current tier, Medicine to stabilize a wound during a crisis rather than in calm — generates 1.5× normal weight; difficulty and consequence matter.

**Cross-axis interactions.** Activities that contribute to more than one axis do so at reduced weight per axis. A difficult expedition requiring tracking a trail, managing food and water, and treating a wound contributes to Tracking, Field Survival, and Medicine — but at 60% weight per axis rather than 100%, preventing any single activity from accelerating everything at once.

**NPC teacher acceleration.** Building relationships with domain teachers (the healer, the veteran tamer, the experienced tracker) does not bypass the usage requirement, but increases the weight of subsequent uses in that domain by 25% until the next tier is reached. The teacher shortens the path; the work still exists.

These numbers — ranges, the diminishing-returns window, the high-stakes multiplier, the cross-axis percentage — are placeholders for empirical calibration. What is not a placeholder is the structure: four tiers, context-sensitive accumulation, diminishing returns within windows, cross-axis interaction at reduced weight.

### How the Player Perceives Kenny's Track

Kenny's Voice changes — as specific axes grow, what he verbalizes around those situations evolves; with developed fauna Track, vague early speech becomes specific (behavior, posture, what a head angle precedes). The world reacts differently — NPCs who treated Kenny with skepticism begin to treat him with respect; veteran tamers who spoke to him as a novice begin to speak as to a man who understands the trade. The situations are the same — Kenny is not. A Velociraptor pack encountered early and the same pack forty hours later are not mechanically different; what changed is what Kenny knows, what the player knows about how Kenny moves, and what both developed together.

### NPC Track and Its Interaction With Kenny

Each named NPC's Track is fixed — the expression of decades of life and experience that cannot be transferred or replicated, and exactly why the loss of a companion is irreversible. The player reads it through conversation (an experienced tamer reveals decades of experience before being asked), through behavior in situation (a high-tracking companion notices what others miss), and through reputation that arrives before the encounter (others speak about high-Track NPCs before the player meets them).

NPCs do not check Kenny's Track at every conversation. The check occurs at specific interaction types: knowledge-sharing conversations, requests for joint operations, and situations where Kenny's competence is directly relevant. The mechanism is threshold-based, not gradual — each NPC with a relevant domain has defined thresholds (typically at tier transitions) at which behavior changes as a step change, because how people treat someone whose competence they recognize is qualitatively different from how they treat someone whose competence they don't, and gradual changes are hard to read without a visible indicator.

*The veteran tamer across tiers:* at Kenny's Fighting Tier 1, the tamer treats him like any sheriff — respectfully but not as a peer, giving information but not offering it. At Fauna Knowledge Tier 2, the tamer begins asking Kenny what he has seen in the field — the direction of information flow changes. At Domestication Tier 3, the tamer includes Kenny in decisions, not just support. At Domestication Tier 4, the tamer speaks to Kenny as someone whose judgment in their shared domain is worth deferring to.

**Track and Bond are independent axes with interaction effects.** A high-Track Kenny with low Bond toward an NPC creates a readable situation: the NPC recognizes the competence but does not trust the person. The NPC may share domain-relevant information (Track unlocks that) but will not go into the field with Kenny, will not share personal information, and will not extend the benefit of the doubt. Bond unlocks investment; Track unlocks respect. They produce different things, and their absence produces different costs.

### Animal Track

Animals have Track that manifests as real capability and behavior, and a sufficiently filled Bestiary lets the player infer it before contact. **Species Track** is what the species is capable of as a pattern (an adult Velociraptor includes group coordination, reaction speed, flanking). **Individual Track** is variation within the species — an old predator in well-established territory is above the species average, a young one outside the group is below, and anomalies may fall completely outside species parameters.

### Kenny as Threat-Assessment Instrument

There is no level bar above any animal's head. The player evaluates threat through the world, and the most immediate channel is Kenny. Through the Shared Senses (§6.2), when the player orients their view toward an animal and holds it — the system reading this as confrontation evaluation rather than passing notice — Kenny reacts as a man with his current Track would.

*Far beyond what Kenny can handle:* (adult T-rex in established territory, complete Bestiary) Kenny stops, goes quiet, then low, almost to himself — *"No. Not today."* — and starts redirecting without waiting for the player. (Unknown medium creature) — *"Don't know what this is. And I don't want to find out like this."*
*Faceable with real cost:* (solo adult Velociraptor, functional entry) — *"Can do it. But I need cover at my back before I start."* (Large but elderly-moving animal) — *"This one's slow. More than it should be."* — pause — *"Still too big to be careless."*
*Manageable:* (young non-aggressive herbivore, complete cataloging) — *"This one isn't even paying attention."* (Small low-aggression cataloged predator) — *"I might not even spend ammo on this."*
*Unknown:* (first encounter, no entry) Kenny stops completely, studies, and when speech comes — *"Never seen this before."* Then: *"I don't know if I want to find out what this does when it's irritated."*
*Human adversaries:* (careless formation, weapons stored sloppily) — *"These guys never had to use that for real."* (Single adversary positioned before Kenny noticed, using cover with training) — *"This one knows what he's doing."* (Five or more vs. Kenny alone) — *"This isn't a fight. This is a different kind of problem."*

## 9.2 — Confrontation — Combat System

### Philosophy

Combat exists and has weight. It is not the center of the game — it is a constant, never-trivial possibility. Avoiding is always a real option, often the most intelligent one, and the game never punishes the player for preferring not to fight. A predator skirted around is as valid as a predator killed. Confrontation operates as two distinct systems, because humans and dinosaurs are not the same type of problem.

### Dinosaur Confrontation

The behavior of dinosaurs in combat is derived from the biology established in the lore, and the combat system consistently respects those rules. The consequence is that the player who understands the lore understands the combat — not because the game explained mechanical rules, but because the world built the context that makes them legible. The technical means by which these behaviors are built — state-machine behavior per creature, spatial queries for flanking, locomotion warping for the T-rex's turning limit, and steering for herds — are specified in §13.4; the rules below are the design those means express.

**Tyrannosaurus Rex — positioning, not flight.** The T-rex is a colossal predator with significant straight-line peak speed but severely limited direction-change capacity due to weight and skeletal structure; it does not pursue prey that changes direction unpredictably because the energetic cost-benefit does not favor it. Fleeing in a straight line is a bad decision; fleeing with direction changes is better but requires terrain that allows it. Cover does not hide Kenny from a T-rex as it would from a human shooter — it breaks line of sight and forces the predator to change direction. A T-rex attack is not a discrete event but a process with phases — localization, orientation, displacement, attack — each with visible signals.

**Velociraptors — the flanking problem.** Small for the predator standard, which is exactly why they are more dangerous in groups than their size suggests. They hunt with coordination beyond conventional pack instinct, distributing roles: one assumes frontal attention while others move to flanks and blind angles. A single Velociraptor is manageable; two are a different order of problem; three or more make keeping all in view simultaneously impossible. The correct response is not reaction speed but preventive positioning — placing Kenny against a wall, in a corner, in any structure that eliminates approach angles. Tamed Velociraptors operate with increased coordination because they were trained to work with human signals; eliminating the human operator disorients the group, but not immediately.

**Herbivores — the panic danger.** A frightened large herbivore is dangerous in a completely different way from a predator. A hungry predator has an objective, direction, readable behavior. A panicked Edmontosaurus has no objective — it has impulse: tons of mass in motion without defined direction, not trying to kill, that will not be persuaded to stop by intelligent positioning, and that kills accidentally with the same efficiency as intentionally. Never run into the movement line of a frightened herbivore. The instinct to use a panicked herbivore against a predator is a dangerous one. Herds in movement have zones of greater and lesser risk — edges are unpredictable, and what is in front of the movement direction is where Kenny absolutely cannot be.

**Medium-sized predators — territory reading.** Carnivores in the spectrum between an adult Velociraptor and a T-rex are the most common encounter outside Dillfield. They have established territory, and behavior within and outside territory differs. Some are intimidatable; the Bestiary, correctly filled, indicates which species respond to intimidation and under what conditions.

**Anomalies and the limit of knowledge.** The Bestiary teaches how animals normally behave; anomalies are what happens when the system simulating that animal is corrupted. A T-rex anomaly with atypical mobility invalidates the positioning that normal cataloging would have made safe. The player with a complete Bestiary has more context to recognize when an animal is not behaving as it should.

### Human Confrontation

**Kenny in human combat.** Kenny is physically formidable; the problem is not efficacy but control. Crazy Kenny is not caricature — it is a characteristic formed by implanted memories. When adrenaline rises, his containment threshold slips; he fights well, with instinct and brute force, but the problem was always knowing when to stop. This has mechanical weight: in high-intensity human combat, Kenny's emotional state interacts with combat in ways the player does not fully control. The system does not block actions, but the consequences exist.

**Reading human adversaries.** Combat with humans is not symmetric. An inexperienced adversary commits early mistakes — positioning that ignores cover, predictable attack timing, a reaction to the first blow that reveals how much it cost. A veteran with high Fighting Track does not.

**The three layers.** Direct physical confrontation (hand-to-hand and short-range, where Crazy Kenny is hardest to control); ranged combat (rifles and revolvers with the world's physics, where ammunition has cost, quantity, and specificity — the revolver for human problems is not the one for larger problems); and stealth approach (enter, resolve, leave without open conflict — the most planning-demanding layer, where the reward of having observed from a distance is most direct). The first main mission — enter the fort, get the mother out, leave — is the natural showcase for the stealth layer once it arrives. The stealth layer ships in Tier 2 (§14); Tier 1 ships dinosaur combat and the direct and ranged human layers, and the rescue mission is fully completable on those layers plus observation and avoidance (§5.9).

**Consequences.** Human combat carries consequences dinosaur combat normally does not: reputation, witness memory, and the weight of what happened in the world's record. A brawl in Dillfield resolved with excessive violence is not forgotten by the city; the Reputation system absorbs it and redistributes it in Kenny's relationships. Kenny being the sheriff and acting outside what a sheriff should carries different weight than a civilian brawler.

## 9.3 — The Weight of the Body — Survival System

### The Principle

The Weight of the Body exists to ensure Kenny is a man in a world, not an avatar on a map. Hunger, thirst, and exhaustion are real — not as punitive systems that block progress, but as conditions that concretely and progressively affect performance. The game has no visible bars for any of these. The player perceives Kenny's state through his behavior and Voice. The calibration sits between RDR2 and a survival simulator: present enough to create planning tension, absent enough not to become a bureaucratic obstacle between the player and the experience.

### Transition Criteria and Timing Framework

The structural logic below governs how phases escalate; precise real-time values are targets for empirical calibration.

**Hunger:**

| Phase | Trigger | Real-time estimate | Reset condition |
|---|---|---|---|
| 1 → 2 | 45–60 min without eating, light activity | ~45 min at rest, ~30 min high effort | Any food consumed |
| 2 → 3 | +30 min without eating after Phase 2 | ~30 min at rest, ~20 min high effort | Any food; fully exits Phase 2 |
| 3 → 4 (collapse) | +20 min at Phase 3 | ~20 min at rest, ~10 min high effort | Substantial food; a snack resets Phase 3 temporarily but Phase 2 returns within 15 min without a full meal |

**Thirst** (escalates ~1.5× faster than hunger under exertion):

| Phase | Trigger | Normal activity | High exertion or heat |
|---|---|---|---|
| 1 → 2 | 30–40 min without water | ~35 min | ~20 min |
| 2 → 3 | +20 min without water | ~20 min | ~12 min |
| 3 → 4 (heat exhaustion) | +15 min without water | ~15 min | ~8 min |

**Rest** (slowest escalation, hardest to reverse):

| Phase | Trigger | Real-time estimate | Full recovery |
|---|---|---|---|
| 1 → 2 | 3 real hours without sleeping | ~3 hours | Any sleep restores to Phase 1 |
| 2 → 3 | +2 hours without sleeping | ~2 hours | Requires full sleep; brief rest insufficient |
| 3 → 4 | +1.5 hours without sleeping | ~1.5 hours | Requires full sleep; combat effectiveness reduced 15 min after waking even from full sleep |

**Field Survival Track modifier.** Each tier increases all escalation timers by 15% — a Tier 4 player has hunger timers 45% longer than a Tier 1 player. This represents real acquired competence (eating and drinking the right amounts at the right intervals, reading the body's signals earlier), not immunity. It is the difference between someone who has lived in the field and someone who has not.

**The calibration principle governing all these numbers:** a player engaged with the world — exploring, hunting, managing expeditions with intention — should rarely reach Phase 3 of any variable without clear Voice signals beforehand. Phase 3 should feel like a consequence of ignoring available information, not of withheld information. A player who reaches Phase 4 collapse should be able to identify, in retrospect, at least two moments where the system signaled that something needed attention.

### The Phases in Detail

**Hunger.** Phase 1 (mild): Kenny eventually mentions he'd need something to eat — a man with needs, not a warning; no performance change. Phase 2 (moderate): physical resistance recovers more slowly after intense effort. Phase 3 (severe): strength actions — climbing, carrying, sustained hand-to-hand — become genuinely harder; the Voice grows scarce and dry. Phase 4 (collapse): Kenny can collapse in the field — not death, but incapacitation at a moment and place the player did not choose. Preparation matters: raw meat of certain species produces status effects beyond basic satiation.

**Thirst** escalates faster in heat and effort. Phase 1 (mild): a passing comment, no impact. Phase 2 (moderate): sustained-effort capacity falls, and Kenny sweats visibly — which makes his smell more detectable by fauna with keen olfactory senses. Phase 3 (severe): vision presents mild dehydration effects, enough to make distance reading and situation judgment less reliable. Phase 4 (heat exhaustion): can lead to collapse faster than hunger.

**Rest** is the longest variable; effects appear slowly but resist reversal without real stopping. Phase 1 (rested): maximum capacity, the Voice at its richest — more observations, more specific fauna reactions. Phase 2 (light deprivation): no performance effect, but Kenny may mention at dawn that the night was not good — information before it is needed. Phase 3 (moderate): combat reaction time increases slightly; the Voice thins; the fauna Track system produces fewer observations. Phase 4 (severe): combat and tracking degrade significantly; the Voice reflects Tired at level 3; reactions arrive delayed or not at all, and the silence that should be contemplative pause starts to feel like absence. Planned camping (chosen location, checked safety, fire set to minimize fauna attraction) gives real rest; an improperly set camp gives lighter rest; town and farm rooms give complete rest.

### Status Effects

**Bleeding** — Kenny leaves a physical trail while moving; animals with keen smell detect it from a distance, and the trail remains active information in the environment for hours. **Poison** — progressively affects motor coordination; the correct antidote depends on the source (Velociraptor venom does not respond to the same treatment as an aquatic creature's). **Fracture** — does not prevent movement but changes how Kenny moves: reduced speed, certain movements impossible, pain interfering with precision; field treatment stabilizes but does not cure, and real rest is necessary. **Disorientation** — from head impact, anomaly effects, or prolonged extreme exposure; directions may seem inverted, sounds arrive out of phase, the camera responds with slight delay — functional, not cosmetic. **Heat exhaustion** — from intense effort in high temperature without hydration; the Voice reflects it before any performance effect is visible. Status effects ship in Tier 2 (§14).

### Weight of the Body and Track

Field Survival Track does not eliminate the Weight of the Body — it modifies how Kenny responds. With developed Survival Track, phases escalate more slowly, recovery is more efficient, and Kenny verbalizes the state earlier (paradoxically an advantage, because the warning arrives with more anticipation). With low Survival Track, phases escalate faster, recovery is slower, and Kenny sometimes does not notice until he is already in Phase 2 or 3 — not because the system penalizes him, but because that is how real experience works.


---
---

# PART III — SUPPORTING SYSTEMS AND WORLD STATE

---

# 10 — SUPPORTING SYSTEMS

## 10.1 — Anomalies — Corrupted Species Variations

Inside each species there is a small, unannounced probability that an individual is born with corrupted attributes. Not evolution, not natural selection — the code generating something that should not exist, an error the system did not correct because the system is not functioning well enough to correct everything. The game does not warn: no different icon, no alert music, no indication that the animal ahead is different. The difference must be discovered — by behavior, by appearance examined up close, by Binoculars used on a creature that should already be known but is not behaving as it should.

An anomaly may be a T-rex with atypical mobility for its size, a Velociraptor pack with coordination beyond the species' capability, a pack animal that without warning exhibits predatory behavior, a medium predator that resists all taming commands but does not attack, or a creature that should be dead from cold but continues moving. Corruption effects may include wounds that do not heal at normal rate, sensory disorientation on attack, posthumous environmental effects on nearby fauna, and silently accumulating penalties that appear abruptly. The complete Bestiary makes anomalies detectable; without the pattern reference, deviations are invisible. Anomalies ship in Tier 2 (§14).

## 10.2 — The Displaced Persons

The UpClouD collapse did not only divert uploads to wrong realities — it ruptured the boundaries between simulations. Realities that existed separately collided. Some partially merged; others dumped their contents into foreign worlds. In Kenny's world, this means people from other simulations arrived — not as invaders, not in an organized fashion, but as Kenny himself arrived: lost, without clear memory, thrown there by the chaos of broken systems.

**The rule that governs displaced persons:** what they bring from their reality of origin passes through the filter of the world where they arrived. Knowledge survives; the form that knowledge takes is reconfigured by the available reality. A displaced person who was a systems engineer does not arrive building spaceships — they arrive with a mind that understands how complex systems work, and in this world those principles translate into precision steam machinery of uncommon design. The knowledge is genuine; the expression is of the world.

**Variety:** those who do not know what they are (most common — the arrival process erases or fragments memory irregularly); those who remember clearly where they came from, not lost but *trapped*, knowing they cannot return; those who do not know and do not want to know, who built a life and developed active resistance to anything threatening its stability; and those who arrived without any trace of what they were, living as any other inhabitant would.

**The avian civilizations.** In some simulations, the evolutionary question that produced human intelligence was answered differently — not by the mammal, but by the avian lineage. Descendants of certain dinosaur species, in other simulated universes, followed a path to language, civilization, and structures of power. The collapse deposited individuals from these civilizations in Kenny's reality in extremely rare cases, dragged here by server chaos. They are not human users. They are not simple NPCs. They are something UpClouD never needed to categorize before. The full range of displaced-person content, including these individuals, is Tier 3 (§14); a single distant, unexplained sighting through the Binoculars is planted earlier as the trilogy's most memorable seed.

## 10.3 — Reputation (The Name)

Reputation is not a bar with a smiley face on one side and a skull on the other. It is a network of perceptions accumulated by each group Kenny interacts with: Dillfield residents, regional farmers, itinerant hunters, merchants, indigenous groups beyond the plains, and gangs and factions operating on the margins. Reputations can conflict — what pleases Dillfield residents may offend external groups, what builds respect among hunters may undermine trust among farming families. Kenny cannot be well seen by everyone at the same time. Because the community is small and everyone knows everyone, changes are felt quickly — within days, not years — which is why Reputation operating at the city scale is a Tier 1 system, with external factions arriving in Tier 2.

## 10.4 — Bonds — NPC Relationship System

Each named NPC has their own relationship with Kenny that evolves over time — not a friendship meter with numbers, but the organic result of each encounter, each conversation, each moment when Kenny appeared when he needed to or disappeared when he should not have. These relationships have direct practical weight: an experienced tamer who trusts Kenny participates in domestications with real commitment, reading animal signals with precision and deciding at the right moment; a high-tracking NPC who considers Kenny a partner notices details during expeditions they would miss if present only out of obligation.

### Bond Thresholds — Mechanical Specification

Bond accumulates from conversations that reach meaningful depth, joint field operations, moments where Kenny was present when something mattered, and time spent in the same space without transactional purpose.

| Threshold | Approx. Bond | What it represents |
|---|---|---|
| None (Richard) | N/A | Relationship established through narrative, not accumulation |
| Low | 25–35 | Several meaningful interactions; the NPC has seen enough |
| Moderate | 50–60 | Sustained relationship over multiple encounters; trust established |
| Moderate-high | 65–75 | Real history together; the NPC has seen Kenny under pressure |
| High | 80–90 | Deep mutual investment; the NPC would not follow anyone else at this point |

### Bond Erosion — Mechanical Specification

Bond does not only increase. Actions that contradict what the NPC values reduce it.

| Action | Bond reduction | Notes |
|---|---|---|
| Minor contradiction of NPC values | −3 to −5 | A single careless decision the NPC witnessed |
| Direct contradiction in a shared situation | −8 to −12 | A decision that put the NPC or others at clear risk |
| Active betrayal (abandonment, deliberate harm, significant lie) | −20 to −30 | Rare; only in situations with clear moral weight |
| Extended neglect (companion unused 3+ real hours) | −1 per hour | Slow drift; realistic, not punitive |

**The grace zone and departure floor.** A recruited companion's Bond can drop to any value without triggering immediate departure until it crosses the grace-zone floor of 20. Above 20, erosion is happening but the relationship is recoverable. Below 20, the companion enters the departure sequence — three visible stages, each ~15–20 minutes of real gameplay: **Withdrawal** (stops initiating conversation, responds when spoken to but volunteers nothing, becomes conservative in the field); **Unavailability** (declines expedition invitations, still present at their location, still responds to direct conversation); **Departure** (absent from their established location with no announcement — Kenny can find them elsewhere in Dillfield, not hostile, simply done).

**Recovery after erosion.** Bond can be rebuilt, but the ceiling lowers permanently with each major negative event. A companion whose Bond dropped to 20 and was rebuilt to 60 reaches a ceiling of 75 — 25 points below the original maximum of 100. Each significant erosion event reduces the permanent ceiling by 5 to 10 points. This represents real damage to trust: repairable, but never the same as if it had never happened.

## 10.5 — The Gang — Recruitable Companion System

Kenny can gather up to six people who accompany him on expeditions and in city life. The group is not formed by menu recruitment but by the relationships the player built — someone who trusts Kenny enough to come when things get serious is someone Kenny worked to have by his side. Each companion has specific skills defining their role when activated, and the player defines each companion's focus: who handles the group's dinosaurs, who leads ranged combat, who prioritizes field survival.

**Companions can be lost.** An NPC who dies in the field is not replaced by a functional clone — that person, those decades of experience, that built relationship are over. The gang the player rebuilds afterward is necessarily different, and the world notices the absence in ways that are not announced but appear. The Gang system ships in Tier 2 (§14); Richard establishes the proto-companion pattern during the prologue journey before the system is formally accessible.

### Confirmed Companion Profiles

Each has a fixed Track, a primary skill domain, a recruitment threshold, and an arc that begins before and continues beyond the moment they join. Companion domains are expressed in the same four-tier language as Kenny's Track (§9.1), but a companion's specialization can be narrower than one of Kenny's seven axes — Mara's "Ranged Combat" and Sal's "Equipment and Maintenance" are focused expressions of the broader Fighting and field-support competencies, reflecting that a person's life shapes them into a specialist rather than a generalist. The tier number indicates how deep that specialization runs.

**Richard** — the first proto-companion. Available from the prologue departure without a Bond requirement; he chooses to come. Primary: Tracking and Field Navigation (Tier 4). Secondary: Field Survival (Tier 3). He is present for the bandit-camp arc regardless of any threshold. Whether he stays afterward depends on what happened during the journey and whether Kenny treated his knowledge as a resource or a partnership.

*Richard's Respect threshold.* Richard is tracked on the same 0–100 scale as Bond but through a separate variable, Respect, because he evaluates competence and judgment rather than relationship warmth. Respect grows when Kenny follows Richard's navigational read without demanding explanation (trust expressed as action), identifies an environmental danger before Richard points it out, makes a tactical decision Richard's Track would have made, admits ignorance and acts cautiously rather than overconfidently, or chooses to camp when conditions call for it. Respect depletes when Kenny ignores a clear signal Richard surfaced, initiates a confrontation Richard assessed as avoidable, treats Richard's observations as trivia rather than actionable information, or pushes past exhaustion or injury thresholds in ways that create unnecessary risk. The threshold to stay after the bandit-camp arc is Respect at 45 or above. Below it, Richard completes the arc because the objective matters to him, then returns to Dillfield and does not present himself for ongoing partnership — he remains available for conversation but not expeditions, and the player can rebuild Respect post-arc; it is not a permanent close. If Richard leaves the active gang, his Track knowledge does not disappear from the world: he becomes an NPC consultant Kenny can seek for navigational or survival questions, though he will not go back into the field. The relationship is not broken; it is simply different.

**Elliot** — a displaced person who arrived in Dillfield before the game begins and has been quietly useful ever since. The city does not know what he is; neither does he, fully. Primary: Medicine (Tier 4). Secondary: Puzzle-adjacent — once Bond is sufficient, conversations with Elliot contribute disproportionate weight to the Thread's simulation-knowledge categories. Bond threshold: moderate. He will not join anyone who has not demonstrated patience for things that do not immediately make sense. He is one of the trilogy seeds; his arc does not close in this game.

**Mara** — a hunter who works the plains east of Dillfield and knows the terrain between the city and the bandit camp better than anyone living. Primary: Ranged Combat (Tier 3). Secondary: Fauna Knowledge (Tier 3), specifically predator behavior at range. Bond threshold: low — she respects competence quickly and loses respect for pretense just as quickly. The easiest companion to recruit and the most likely to die in the field if the player does not manage encounter decisions carefully.

**Sal** — the blacksmith's apprentice, working metal and mechanisms since he was twelve. Primary: Equipment and Maintenance (Tier 3) — companions with Sal in the gang experience slower equipment degradation and access to field repairs otherwise unavailable. Secondary: Leadership (Tier 2). Bond threshold: moderate-high. Sal does not follow people he does not trust to come back from things; he has buried two previous employers.

**The Tamer** (name to be established) — the oldest active tamer in Dillfield's region, introduced in Domestication. Primary: Domestication (Tier 4). Secondary: Fauna Knowledge (Tier 4). Bond threshold: high — this person has seen too many people killed by overconfidence to join anyone who has not demonstrated otherwise through sustained competent behavior. Without this companion, solo Domestication of aggressive species is significantly more dangerous; their death permanently removes the primary NPC teacher for the Domestication axis.

**The Sixth Slot** — intentionally unspecified. The game will introduce characters during the main arc whose recruitment potential depends on how specific narrative events resolve. The sixth slot exists as a variable filled by late-game relationships, not a pre-planned companion. To prevent the edge case of a player who makes internally consistent choices that close every path to a sixth companion, two layers protect the slot. *Minimum candidate availability:* at least two characters capable of filling the slot are accessible in the late game regardless of earlier choices, with lower Bond thresholds because they appear late and join based on recent demonstrated behavior. *The floor:* if the player reaches the final Thread threshold with fewer than five active gang members, the game ensures at least one late-game character makes themselves available — not through a scripted cutscene that ignores established tone, but through a situation the player encounters in normal play that creates a natural recruitment opportunity. This safety net activates silently only when the floor condition is met.

### Permanent Death and Mission Dependencies

When a companion dies permanently, the world resolves missing dependencies through degradation, not blocking. No main-story mission requires a specific living companion to complete. What companions provide is capability — a tamer makes domestication safer, a medic makes recovery faster, a tracker surfaces information Kenny would miss. Losing them does not close a door; it makes what is behind that door harder. If the Tamer dies before a high-aggression taming, the operation is still possible but without the guidance that made it manageable, raising failure and injury probability substantially. If Elliot dies before sufficient simulation-knowledge Thread weight is accumulated, the Puzzle's displaced-person pathway loses its most valuable contributor — the remaining displaced persons fill the gap partially, and the final revelation can still be reached, but the path is longer. If Richard dies during the bandit-camp arc, the journey home is without his navigation, and weather and terrain encounters he would have flagged arrive without warning. Named-companion deaths generate world reactions that are not scripted announcements: the blacksmith is quieter, someone's table at the saloon is empty, a conversation Kenny would have had simply does not happen because the person who would have had it is not there. The loss compounds over time in ways that are not calculated, only felt.

## 10.6 — Active Memory Mode — Optional Adaptive HUD

In the options, the player can enable Active Memory Mode — a system that transforms accumulated knowledge into visible HUD layers. Everything Kenny has discovered, cataloged, and learned is displayed automatically and contextually without needing to consult tools: in a fully mapped region with completely cataloged fauna, opening the map shows points of interest, known routes, and recorded notes; approaching a fully cataloged dinosaur shows the species' information without the Binoculars. This mode never delivers what the player has not earned — the interface displays only what has been discovered, and unknown regions, uncataloged species, and unrecorded events remain opaque. Low development cost relative to what it provides; it ships once Tier 1 is stable, as part of Tier 2.

## 10.7 — Death Modes

**Standard mode — narrative death.** Kenny can die and continue, with consequences reflected in the world but without ending the journey. The honest reason is accessibility and retention: permadeath would make Project D inaccessible to most players and is incompatible with the experience the game is creating for the widest reasonable audience. The lore establishes that death inside the simulation is permanent, but that lore fact does not obligate the standard game to impose permadeath mechanics — the lore and the mechanics serve different purposes and need not be identical. What standard mode does instead: death has real world consequences — time passes, NPCs react, certain situations change permanently. The world registers that Kenny almost didn't make it.

**The single concrete proof of permanent death in standard mode.** Because the permanence of death is one of the project's four lore differentiators, the standard-mode player must *feel* it once, not only hear it described. This is delivered through a scripted moment that is part of the main narrative: at a specific point, a displaced person the player has come to know dies, and the player witnesses, through a glitch, the consequence the lore establishes — the individual's simulation shutting down, the server going dark, a presence that does not respawn and is never seen again. This is the one time standard mode makes the lore's central rule concrete and irreversible. It does not change how Kenny's own death works in standard mode; it ensures the differentiator is experienced rather than merely explained.

**End of the Line — optional permadeath mode.** Kenny's death permanently ends the session. This exists as an optional layer for players who want the full mechanical expression of what the lore establishes. It is not a "truer" version of the game — it is a harder one, for a specific kind of player, with the specific satisfaction that comes from playing under real stakes. It ships only after Tier 1 and Tier 2 are stable and tested (Tier 3), because permadeath is only satisfying when deaths feel earned: a permadeath mode built on unresolved edge cases, unjust collision deaths, or poorly telegraphed threats delivers frustration, not the intended experience. The mode waits for the foundation to deserve it.


---

# 11 — TIME, VERISIMILITUDE, AND THE HUNDRED YEARS

> This section defines how Project D keeps its 1–2 year fictional timeline coherent against player activity that could otherwise outrun it, and how the hundred-year horizon is delivered. It is the system that protects the project's most fragile claim: that everything the player does fits believably into the life of one man across one or two dense years.

## 11.1 — The Problem This System Solves

Project D's progression systems measure player activity. Track grows by use, Bond grows by encounters, the Thread grows by accumulated action. An efficient player could, in twenty-five hours of real play, reach Tier 4 Domestication, recruit a full gang, and complete the Bestiary. If the fiction maps those achievements onto a span the player cannot perceive, two failures follow: the world appears frozen while the player's competence explodes, and major narrative revelations arrive while Dillfield still looks like the first week. Either breaks the verisimilitude the entire design depends on. The Time system exists to keep fictional time and player activity in believable relation.

## 11.2 — The Internal Calendar

The game maintains an internal calendar tracked in fictional days and seasons. The player never sees a date on screen — consistent with the character-as-HUD principle — but the calendar is the authoritative reference that every time-sensitive system reads from. It advances through three channels working together: real playtime (a baseline rate of fictional time passing as the player plays), sleep and rest (each full sleep advances the calendar by the fictional duration of a night, and camping on expeditions advances it accordingly), and travel (long expeditions advance the calendar by the fictional days the journey represents, per the travel-time reference in §4.9).

The calendar is the spine the verisimilitude rests on: it ages the world, gates the narrative, and gives the player an honest answer whenever they ask "how long has it been?"

## 11.3 — Fictional-Time Floors on Narrative Milestones

The Thread's major thresholds are gated by two conditions simultaneously, both of which must be satisfied: the accumulated action weight (the player earned it) and a minimum elapsed fictional time (the fiction can bear it).

| Milestone | Action condition | Fictional-time floor |
|---|---|---|
| First threshold — The Weight of the Deadline | Main-narrative progress + one displaced-person encounter | No floor beyond prologue completion; this is the first-session guarantee |
| Intermediate threshold — The System and What It Is | Significant accumulated volume | Minimum of two fictional seasons elapsed since the bandit-camp arc closed |
| Final threshold — The Hundred Years | The largest accumulated volume | Minimum approaching one fictional year of total elapsed game time |

When a player satisfies the action condition before the fictional-time floor, the threshold holds. The Thread does not fire. The player continues to live in the world — and because the world is aging visibly around them (§11.4), the wait does not feel like an arbitrary lock; it feels like time passing, which is exactly what it is. The action condition guarantees the player worked for the revelation; the time floor guarantees the world had time to become the place where that revelation makes sense.

## 11.4 — Making Time Legible — Production Specification

The 1–2 year timeline must be felt without a visible calendar. The following are concrete deliverables that make elapsed time legible through the world itself.

**Environmental signals (environment art).** Seasonal variation for Dillfield's main street — dry season (dust, lighter foliage), wet season (mud on the street, full water barrels), and transitional states, with a minimum of two full seasonal passes across the playable area. The wooden walkways age visibly: new boards appear where old ones rotted, with one or two replaced posts per season. Kenny's garden at the sheriff's office grows if the player tends it and dies if not. The grave markers for the sheriff and Kenny's father are clean at first, then weathered, then carry small offerings from townspeople on certain dates. The bandit-camp structure, once the arc resolves, deteriorates visibly across revisits.

**NPC social signals (writing / dialogue).** NPCs make unprompted time references at natural frequency — "Haven't seen you in a few weeks," "You were gone the whole rain season," "That wound has healed up, I see" — fired as ambient social texture when Kenny returns after an absence, calibrated to the actual elapsed calendar time. Three to five Dillfield NPCs have personal arcs that visibly progress independent of Kenny: a pregnancy comes to term, an apprenticeship concludes, an old feud resolves or escalates. These require no player participation; they happen in the background and are visible to an observant player. Elliot's apparent understanding of what he is increases subtly over time, measured in how he speaks about things that do not belong — more precise, less deflecting.

**Kenny's own signals (Voice system).** Seasonal Voice reactions: Kenny notes the first cold morning of the year, the smell of the ground after the first rain, the way the light changes in late season — lines that exist only in their specific seasonal window and never repeat. Return lines calibrated to actual elapsed time: three weeks away produces different Kenny speech than three days away.

## 11.5 — The Hundred Years as Horizon

The game's story does not cover a hundred years. It is the story of a man inside a simulation, told from a specific point in his life within it; what Kenny lives in the game is a slice, and the hundred years are the horizon. The information reaches the player in layers. **The first layer — the existence of a deadline:** at some point in the discovery, Kenny begins to understand a limit exists. He does not know what it is or where it comes from; he just knows, in a way he cannot yet articulate, that the time he has is not unlimited. **The second layer — the number:** this arrives only at the end, after the great events, after relationships built and lost, after the player already has a real story with Dillfield and its people. With all that established, the number appears — one hundred years — not as an abstract revelation but as concrete weight.

At game's end Kenny is approximately 29–31 years old in simulation time, with between 68 and 71 simulation years remaining. The cliffhanger lands with full weight because the player has lived one or two of those years alongside him and now knows there are decades more ahead with a clock running. Project D ends with Kenny standing, a story behind him and decades ahead, knowing for the first time that the clock is running. Everything that was built continues existing. Everything that can still be built also. But now there is a visible horizon where before there was only the next day.

## 11.6 — Implications for the Progression Systems

The Track system grows within this compressed timeline, meaning its axes do not represent a lifetime of mastery but a period of intense, consequence-driven learning — plausible because every week puts Kenny in situations that demand it. Reputation operates at the scale of a small community over the same period, where actions have visible weight within days. The Gang of up to six is a realistic number of close working relationships establishable in one to two years of high-stakes collaboration. The fictional-time floors of §11.3 ensure these systems cannot resolve faster than the fiction can absorb, while the legibility deliverables of §11.4 ensure the player always perceives the time those systems consumed.

## 11.7 — Trilogy Seeds — What Is Planted Here

Project D is the first game of a planned trilogy, and it is built to be a complete experience that also opens a larger horizon. This first game is entirely contained within the simulation: Kenny, Dillfield, the Old West with dinosaurs, the progressive discovery of what he is — all of it within the limits of that world and that man. The story has a beginning, middle, and end; the player who reaches the end will have lived something complete, with a closed emotional arc and all central revelations delivered. For development, this means one practical thing: build Project D as if it were the only game, without depending on continuations to close what must close here.

A seed is not a spoiler — it is a question intentionally left open, existing so the following game has somewhere to grow. **Kenny's mother, taken by the bandits:** an absence with weight, the last detail of the worst moment of Kenny's life before the role that defines the game; what happened to her belongs to the sequels. **The group that attacked Dillfield:** an organization with tamed Velociraptors and specific objectives does not arise by accident — what exactly did they want, and who do they work for? **Displaced persons, including Elliot:** the first game establishes their existence but does not exhaust it; some will die over the hundred years, others will remain. **Kenny's deterioration from the damaged servers:** a process that begins here and does not end here — what he becomes over the decades, how much of the original Kenny survives the progressive corruption, is possibly the most important question of the entire trilogy, and the Voice Degradation system (§6.10) is where the player first begins to live it.


---
---

# PART IV — PRODUCTION

---

# 12 — DIRECTION — ART AND AUDIO

## 12.1 — Visual Direction

The visual identity serves the philosophy before it serves spectacle. The world is the Old West with sixty-five million additional years walking beside it: weathered wood, dirt streets, heavy sun, and a built environment quietly shaped by the constant proximity of large dangerous animals — elevated entrances, reinforced bars, covered rooftop walkways, agricultural terraces on rocky slopes. The strangeness is in the details a careful eye catches, not in overt fantasy: dinosaur footprints mixed into the dust of the main street as if equally common, because they are; warning signs fixed to walls; the unusual calibers in the weapons shop. The art does not announce that this is a different world. It lets the player discover it the way Kenny lives it.

**The minimal HUD is a visual pillar, not a settings option.** The screen is, by default, almost empty of interface. Information lives in the character and the world. This places enormous weight on readable animation — Kenny's posture, where he looks, how he breathes — because behavior without speech (§6.7) only works if the animation carries it. Character and creature animation is therefore a higher production priority than environmental polish; a beautiful field with an unreadable Kenny fails the design, while a plain field with a perfectly legible Kenny succeeds.

**Glitches as a deliberate visual language.** The corruption of the simulation is expressed through controlled visual distortion — a texture pulsing for a frame, a shadow with the wrong shape, an NPC freezing for half a second. These must be authored to sit exactly on the line between "is that a bug?" and "that was intentional," because the first reading is the point. They are a distinct visual vocabulary that intensifies as the servers deteriorate, peaking alongside the late-game Voice Degradation.

**Seasonal and temporal aging** (specified in §11.4) is a core art deliverable, not set dressing: the visible passage of time is the load-bearing proof of the game's timeline.

## 12.2 — Audio Direction

Audio carries more of Project D than in most games, because the game is frequently quiet and the quiet is intentional. **Kenny's voice is the single most important audio asset** — 3,000–4,000 lines whose delivery must convey emotional state, intensity, fatigue, and, in the late game, the hollowing-out of Voice Degradation. Voice direction is a named, senior role with authority over the recording sessions, because the difference between a line read flat and a line read with the right held pause is the difference between the system working and failing.

**Ambient audio is gameplay, not background.** The deep, distant vocalizations from the plains at night; the dry rhythmic sound of steps too heavy for anything familiar; the difference between Kenny's breathing in confrontation versus rest — these are information channels the attentive player reads. The sound design must treat them as signals with meaning, mixed so they are audible to a player who is listening without being intrusive to one who is not. Silence is a designed element: when the system chooses not to fire a line (§6.9), the resulting quiet is part of the experience, and the ambient mix must make that quiet feel inhabited rather than empty.

**Audio is the primary channel of the Shared Senses.** Because the player perceives the world as Kenny (§6.2), the soundscape is not an accompaniment to the image — it is one of the senses the player borrows, and the most expressive one the hardware can render directly. Two responsibilities follow for the sound team. The world is spatialized through Kenny's position and orientation, and sounds at the threshold of his hearing are lifted into audibility the instant his ear catches them, so the player hears what Kenny hears rather than being told about it. And the whole mix is reshaped continuously by his state, the soundscape opening or narrowing with his calm or his tension (§6.2). This state-driven mix is a core sound-design deliverable, not a post-process afterthought; it is built and tuned alongside the perception model (§13.3, §13.6).

**Behavioral audio cues** support threat assessment without a HUD: the shift in ambient tone as a predator's territory is entered, the change in fauna sound before a Window species becomes active. These are the audio half of the indirect trail (§8.3).

## 12.3 — The Coherence Principle

Art and audio are bound by the same rule as every system: nothing communicates through an interface element that could communicate through the world or the character. A storm is read through the sky, the wind, and Kenny's reaction — not a weather icon. A predator's proximity is read through sound and Kenny's posture — not a threat meter. The discipline this demands is the project's signature and its hardest sustained cost.

---

# 13 — TECHNOLOGY AND ARCHITECTURE

## 13.1 — Engine Recommendation

The recommended engine is **Unreal Engine 5**, for three reasons aligned with the project's specific needs. First, the animation and behavior systems Project D depends on most — readable character animation, complex creature behavioral AI, layered blend states for Kenny's posture and breathing — are areas where Unreal's tooling is mature and well-documented: Control Rig and the animation blueprint system for animation, Behavior Trees and the newer StateTree for AI logic, the Environment Query System (EQS) for spatial reasoning, and Motion Matching with pose-warping nodes (Orientation Warping, Stride Warping) for grounded large-creature locomotion. Second, the large-but-bounded open world with seasonal aging benefits from Unreal's streaming and World Partition tooling. Third, the talent pool for an AA-indie team building a third-person, animation-heavy, narrative open-world game is deepest in Unreal, reducing hiring risk on a multi-year project.

A decisive practical reason reinforces the choice: nearly every core system in Project D maps onto a documented, shipped technique with a known reference implementation, and most of those references live in or near the Unreal ecosystem. The bark engine has a textbook in Valve's dynamic-dialogue rule system; The Thread is a drama manager descended from the same studio's pacing director; the creature AI draws on published squad-coordination work from F.E.A.R. and Days Gone; the drawing recognition is a compact academic algorithm with public source. None of this is research the team has to fund. The one genuinely novel system, the Shared Senses, is built from cheap engine primitives (view-frustum tests, dot-product centrality, line traces, spatial-audio queries, haptic output) — the invention is in the arbitration logic and the sensory layering, not the technology.

Godot is a viable alternative if the team's existing expertise is concentrated there and they accept building more of the open-world, animation, and AI tooling themselves; the architecture below is engine-agnostic in its principles, but the UE5 feature names are given throughout because they are the fastest path to a working prototype.

## 13.2 — Core Architectural Principles

**Data-driven content, keyed by Gameplay Tags.** The Bestiary reference profiles, the drawing-recognition shape library, the Voice line bank with its state and zone tags, the Track thresholds, the Bond and Respect parameters, the Weight of the Body timers, and the Window conditions are all authored as data, not hard-coded. In Unreal terms, this means **DataTables** (spreadsheet-like rows, ideal for the thousands of Voice lines) and **DataAssets** (typed, reference-friendly objects, ideal for species profiles and NPC definitions), with **Gameplay Tags** as the hierarchical vocabulary that labels everything — emotional state, perception zone, story stage, region, species. Gameplay Tags matter specifically because the bark engine's core operation is matching a current set of tags against the tags on each candidate line; using the engine's native tag system rather than strings or enums makes that matching fast and the content authorable by designers. This is non-negotiable for two reasons: the design defers most numerical values to empirical calibration (Track, survival timers, Thread weights), so designers must retune without programmer involvement; and the content volume makes data-driven authoring the only maintainable approach.

**Event-driven communication through a message bus.** The systems are deeply interdependent (§15) but must not be tightly coupled. The recommended backbone is Unreal's **Gameplay Message Subsystem** — a publish/subscribe router, proven in Epic's Lyra sample project, that uses Gameplay Tags as channels and structs as payloads, letting systems broadcast and receive without holding direct references to one another. When the player observes a glitch, a single message is published on a tag channel, and the Thread (as input), the Notebook (for potential recording), and the Voice system (for a possible instinctive reaction) each subscribe and respond independently. Tight local hookups still use ordinary delegates; the message bus is reserved for cross-system events. The known cost of this decoupling is that it becomes harder to trace what triggered a given behavior, so the bus carries debug logging from the first day — every published message is loggable with its channel, payload, and source.

**The Voice system as a rule-based selection engine fed by a perception model.** The Voice system is not a script player; it is a selection engine, and its design has a direct, documented precedent: Valve's dynamic-dialogue system, presented by Elan Ruskin at GDC 2012 as "fuzzy pattern matching," which drives the contextual barks in Left 4 Dead. That system maintains a dictionary of *facts* about the current world state, authors each possible line as a *rule* composed of *criteria* (a fact key plus an acceptable value or range), and on each query scores every rule and selects the most *specific* one that matches — more matched criteria means higher priority, so a line written for "shaken, night, near the cemetery, first time" beats a generic "night" line whenever its conditions hold. Project D's Voice system is this pattern applied to Kenny. Its fact dictionary is assembled each query from the Shared Senses perception model (§6.2) — which continuously scores what is reaching Kenny across sight, hearing, smell, and instinct, weighted by gaze centrality, dwell, and per-sense salience — plus the emotional state and intensity (§6.4), active Track levels, time of day, story stage, and the corruption-eligibility flags of Voice Degradation (§6.10). The selection engine filters the line bank to rules whose criteria match, applies the cooldown and frequency rules (§6.9) and the no-repeat-in-session ring buffer, and selects the highest-specificity surviving candidate — or, when no rule scores above threshold or all matches are on cooldown, returns silence. Silence as a valid output is not an edge case to handle; it is the default the engine returns whenever the world has not given Kenny a reason to speak. The pairing of perception model and rule-based selector is the single most important thing to architect well, because every other system feeds it and the player experiences the game largely through it.

**The Thread as a drama manager with a delivery queue.** The Thread belongs to a documented family of systems known as drama managers or experience managers, whose closest shipped relative is Valve's AI Director from Left 4 Dead: a hidden system that estimates player tension and paces events, deliberately following intense moments with a quieter "relax" phase. The Thread inverts that director's purpose — it paces *narrative* beats rather than enemy spawns — but uses the same machinery. It is built as a persistent world subsystem that subscribes to tagged player actions on the message bus, adds their weight to category accumulators, and arms an event when an accumulator crosses its threshold *and* the §11.3 fictional-time floor has passed. Armed events wait in a priority queue and are delivered only when a "calm" predicate is true, where calm is computed from a tension estimate — combat state, recent damage taken, creature proximity, player movement intensity — exactly the quantity Valve's director watches, read here to find the trough rather than shape the peak. The four safety mechanisms of §7.5 (the maximum wait cap, the queue depth limit, the widened-window fallback, and the return-to-city trigger) are standard scheduler patterns layered on top. The logic is modest; the difficulty is tuning, which is why it is prototyped end-to-end early (§14.2) with a single real narrative beat.

## 13.3 — Building the Shared Senses

The Shared Senses (§6.2) are the one system in Project D with no shipped precedent to copy. Games have triggered character dialogue from player position and trigger volumes, from player choices, from dwelling in a room; eye-tracking experiences have gated narrative on where a player looks; many games render spatial audio and route haptics. But no shipped game fuses player gaze, the world's per-sense salience reaching the character, and the character's own state into a single perception model that makes the player feel they are inhabiting one specific body — perceiving through its eyes, ears, nose, and instincts, including what the player's own hardware cannot resolve. This is the system the team invents. The reassurance is that every individual building block is a cheap, well-understood engine primitive; the novelty lives entirely in how they are combined, layered, and tuned, not in any technology that has to be created. The work divides into three parts: the four input channels, the arbitration model that fuses them, and the sensory output layer that lets the player feel them.

### The Four Input Channels

**Sight.** Is the candidate on screen? A view-frustum test answers this — the engine's recently-rendered check reports whether an actor was drawn within a recent tolerance — paired with a line trace to confirm true line of sight, since the frustum test alone ignores objects hidden behind geometry. How central is it? The dot product of the camera's forward vector against the normalized direction to the candidate yields a continuous centrality weight, near 1.0 when the player looks dead at something and falling off toward the edges. How long has the player held it? A per-candidate score integrates centrality over time while the object remains visible and decays when it leaves view — the dwell concept from gaze-interaction research, used here to drive commentary rather than selection.

**Hearing.** Each sound-emitting event in the world carries, beyond its played audio, a perceptual descriptor: a volume-at-distance, a direction, and a salience-to-Kenny. The system runs an audible-event query — what sounds are reaching Kenny's position above his hearing threshold right now — and scores each by salience and by whether it sits at the edge of audibility, because the threshold sounds are exactly the ones Kenny registers and the player might miss. This query feeds two outputs at once: the perception model (so Kenny can react) and the audio mix (so the threshold sound is lifted for the player at the instant Kenny catches it). Hearing is the channel least dependent on where the player is looking, which is why it carries most Kenny-led perception.

**Smell.** Scent has no direct hardware output, so it is modeled as directional perceptual events tied to the wind. Scent sources (a carcass, smoke, a predator's territory marking, rain forming) emit a scent volume that the system propagates downwind; when Kenny enters a scent's reach, the system registers a perception event weighted by the source's salience and the wind direction relative to Kenny. Because propagation is downwind and travels farther than sight in the open, smell is frequently the earliest warning — the channel that fires before the source is visible. Its output is always indirect: Kenny's breathing, his turn into the wind, and his words.

**Instinct (the body).** The fourth channel is not a sensor pointed outward but a set of authored triggers tied to specific world states: proximity to a simulation-corruption fragment, a glitch event, being within a watching predator's awareness, prolonged exposure to a hostile condition. These fire instinct events carrying no identifiable source — their entire content is "something is wrong" — which is why they surface as bodily response (changed breathing, closed posture, a haptic catch) and at most an uncertain half-line, never a clear statement. This channel is the implementation path for the instinctive layer (§6.3, Layer 3) and the leak of the simulation's corruption.

### The Arbitration Model

The part with no off-the-shelf answer, and that the team must design, is the model that fuses four heterogeneous channels into one stream of "what is Kenny perceiving now." Each frame the system maintains a small set of perception candidates drawn from all four channels, each with a combined score built from its channel's raw weight (centrality and dwell for sight; volume, direction, and edge-of-audibility for hearing; wind and proximity for smell; trigger strength for instinct) multiplied by that channel's authored salience and then modulated by Kenny's current state (§6.4, §9.3) — tension sharpens hearing and narrows sight, exhaustion dulls every channel, being shaken can close one entirely. A notice budget caps how many candidates Kenny holds at once, so he never tracks the whole world. Suppression rules prevent him from reacting to everything above threshold: a candidate already reacted to goes on cooldown, lower-priority candidates are dropped when a higher one arrives, and the global frequency rules of §6.9 sit over all of it. When a candidate crosses the response threshold and survives suppression, the system writes it into the fact dictionary the Voice selection engine reads (§13.2) — identity, channel, salience type, duration — and the rule-based selector turns it into a line, behavior without speech, or silence, while the sensory output layer responds in parallel. Kenny resolving the far house the player cannot make out is not computer vision: the house already carries its true identity in data, and the system simply permits Kenny to verbalize it once the combined score crosses the threshold, even while the on-screen mesh is a distant blur. The same holds across senses — the carcass already "is" a carcass in data; Kenny names it when the scent event crosses threshold. The gap between what the hardware conveys and what Kenny knows is authored, not computed.

### The Sensory Output Layer

Perceiving is only half the system; the other half is letting the player *feel* what Kenny perceives, through every channel the hardware allows and always diegetically. Three output paths run from the arbitration model in parallel with the Voice selection.

The **dynamic spatial mix** is the primary instrument. The world is rendered in full 3D audio through Kenny's position and orientation, and a state-driven mixing layer reshapes it continuously across the calm, tense, exhausted, and shaken soundscapes described in §6.2. Middleware (§13.6) handles the spatialization and holds these as authored real-time mix states; the perception model drives which state is active and lifts threshold sounds into audibility the moment Kenny registers them.

The **screen-as-body** path expresses bodily state through the framing rather than through overlays: the faint rhythm of breathing in the camera, the image steadying when Kenny holds still to listen, the slight loss of peripheral crispness when he is dehydrated or wounded, the held beat when instinct fires. These are post-process and camera-rig parameters driven by Kenny's state, never UI elements drawn on top.

The **haptic** path carries what the body feels and the eyes cannot show: a rising heartbeat pulse as a predator nears, a sharp catch when instinct registers wrongness, the dull ground-resonance of heavy footfalls felt before they are heard. Modern controller haptics are sufficient for all of this; the discipline is restraint — every pulse tied to a real bodily cause, never decorative.

### Prototyping Priority

This system is prototyped before any other (§14.2) because its feel cannot be predicted from the specification. The benchmark is subjective and decisive: does the player feel they have become Kenny — perceiving the world through his body — without him narrating everything? The vertical slice must exercise all four channels and all three output paths, not sight alone, because the multi-sense fusion and the sensory layer are precisely what cannot be validated on paper. If, after tuning the channel weights, decay curves, notice budget, suppression rules, and mix states, the result still feels naggy, random, or gimmicky, that is the signal to redesign the arbitration and the output layer before any line content is produced — and, in the worst case, to fall back to a narrower proximity-and-look-cone trigger of the kind Firewatch used for the visual channel while retaining the dynamic mix, treating the full multi-sense model as a research track rather than a shipping certainty.

## 13.4 — Building the Creature AI

The creature AI is the second-hardest system, but it is hard in execution rather than in concept: the behaviors are buildable with Unreal's stock AI stack, and the published references for the difficult parts are strong. The recommended shape for a small team is a hybrid — a hierarchical state machine for each individual creature's behavior, lightweight utility scoring to choose between high-level modes, and the Environment Query System for all spatial reasoning — reserving heavier planning architectures for nothing unless a specific creature genuinely demands one.

For **individual creatures**, the logic lives in a **StateTree** (Unreal's newer hybrid of state machine and behavior tree) or a Behavior Tree. This is where the T-rex's multi-phase attack lives — localization, orientation, displacement, strike — as a sequence of states with visible tells between them, and where a territorial predator's within-territory and outside-territory behaviors are distinct states. Mode selection between such states is well served by **utility scoring**: cheap weighted evaluations with response curves that pick the most appropriate behavior for the moment, which reads as natural and emergent without the cost of a full planner.

The **T-rex's biological turning limit** is enforced not in the AI logic but at the locomotion layer. The behavior decides intent; the movement system makes the body physically unable to honor an instant turn. Motion Matching combined with Orientation Warping and Stride Warping keeps the animation grounded and bounds how fast the body can reorient, which is what makes "flee in a straight line and the T-rex catches you, flee with direction changes and it cannot" true in the simulation rather than merely described. Large-creature motion matching is achievable but sensitive to the quantity and curation of animation data, so animation time is budgeted here specifically; if motion matching keeps producing skips after a dedicated animation pass, the fallback is a curated blendspace with orientation warping, which is less fluid but reliable.

The **Velociraptor pack** is the part with the richest references. Coordinated flanking that distributes roles among attackers is exactly the problem solved by F.E.A.R.'s squad behaviors — where a coordinator clusters individuals into a squad and assigns flank, suppress, and advance roles, and where much of what reads as deliberate flanking actually emerges from each agent choosing good cover — and by Days Gone's swarm coordination, which maintains a shared frontline and assigns each attacker a lane, designating some to flank while holding the line stable. Project D ports the small-scale version of this: a squad-level controller assigns roles across the pack, and EQS, which is purpose-built for exactly this kind of tactical position query, finds the actual flanking positions in the terrain. Eliminating the human operator of tamed raptors degrades the coordination by removing the controller's role assignments, which is why the pack disorients but not instantly.

The **panicking herbivore** is the simplest in concept and the one to be most disciplined about in scope. A frightened herd is classic steering behavior — separation, alignment, cohesion, and flee — and for a small number of animals, ordinary actors running steering logic are simpler to build and far cheaper to debug than anything more elaborate. Unreal's Mass framework (its data-oriented system for large agent counts, with lane-based movement and force-based avoidance) is the right tool only if herd sizes grow large enough that per-actor cost becomes a profiling problem; below roughly fifty to a hundred visible agents, actor-based steering is the correct choice, and Mass is adopted only if measurement demands it, because it is powerful but carries real added complexity and a learning cost a small team should not pay speculatively.

Across all creatures, the bespoke layer is not the AI architecture but the **biological rule data** that sits on top of it: the turn-radius limits, the commitment of an attack phase once begun, the pack role distributions, the territory boundaries. None of this is novel research; it is design and tuning expressed as data over proven systems, and it is validated against the lore in prototype before any animation or production AI is committed (§13.7).

## 13.5 — Building the Observation and Drawing Systems

The Bestiary's observation loop has clear, beloved precedents — the scan-to-catalog mechanic of Metroid Prime's Scan Visor, the creature-reading focus of Horizon — and is architecturally simple. Observing a creature through the Binoculars performs an identification trace, unlocks or advances the matching catalog entry held as a DataAsset, and increments that entry's per-field knowledge as observation continues, which is exactly the progressive cataloging of §8.2 expressed in data. Nothing here is technically demanding; the work is content authoring and the tuning of how much observation, at what distance and conditions, each field requires.

The drawing-recognition system (§7.4) sounds like the riskiest part of the Notebook and is in fact the most solved. The requirement — the player arranges simple marks, and the game scores the result from 0 to 100 against a reference — is precisely what the "dollar" family of geometric recognizers does. The $1 Unistroke Recognizer and, more relevantly, the $P Point-Cloud Recognizer treat a drawing as a set of points and compare it to stored templates by geometric similarity, returning a score that maps directly onto the recognition thresholds of §7.4. They require no machine learning and no training phase, are tunable simply by adding reference templates, and are compact enough to implement and debug in a fraction of the time a learned approach would cost. The $P variant is the better fit because it treats the drawing as an unordered cloud of points, so the order in which the player places marks, the number of strokes, and their direction do not matter — which is correct for a system where the player is arranging shapes freely rather than drawing one continuous line. A learned model is deliberately avoided here: the geometric recognizer is deterministic, debuggable, and controllable, where a model would be none of those and would be far harder to tune to feel fair.

The one place the recognizer alone is not enough is Project D's specific intent that quality be judged by *proportion* — that a long-necked species drawn with too short a neck should read as wrong even if the marks are placed cleanly. Whole-shape geometric matching captures gross silhouette but not part-to-part ratios, so a small custom pass sits on top: the reference profile for each subject records the key ratios between marked parts (neck to body, limb count and placement, the presence of a distinctive feature), and the scoring compares the player's ratios against the reference's before producing the final match. This is a modest, well-bounded piece of bespoke work layered onto a recognizer that is otherwise entirely off the shelf.

## 13.6 — Audio Middleware and Diegetic UI

Two implementation decisions shape how the game's HUD-less philosophy actually reaches the player, and both have settled answers.

**Voice playback and the dynamic mix.** The Voice line bank is large enough — three to four thousand lines, before localization multiplies it — that managing it inside the engine's native audio hierarchy would not scale. The stronger fit is **Wwise**, whose external-sources and voice-object features are built precisely for large voice banks and for the localization variants each line will need; its dialogue-management features (cooldowns to stop lines spamming, call-and-response pairing, and prevention of a character speaking over himself) are the same feature set §6.9 specifies, available rather than built. The same middleware also delivers the Shared Senses' dynamic, state-driven mix (§13.3): Wwise States and real-time parameters express Kenny's calm, tense, exhausted, and shaken mixes as authored states the perception model switches between, and drive the lifting of threshold sounds into audibility — so the state-driven soundscape is configured rather than coded. **FMOD** is the lighter alternative, with comparable snapshot and parameter systems, if budget or footprint argues against Wwise. In either case the middleware handles playback, voice management, and the mix states; the selection policy — which line, or silence — and the decision of which mix state is active remain the custom logic of §13.2 and §13.3, because no middleware decides those.

A note on the narrative-scripting tools sometimes reached for here: branching-dialogue middleware exists and is mature on some engines, but its Unreal integrations are less proven, and a branching-narrative tool is in any case the wrong shape for a bark engine, which is a rule-based selector rather than a dialogue tree. The custom Ruskin-style evaluator is both simpler and lower-risk than bending such a tool to this task.

**Diegetic UI.** The whole project forbids the conventional HUD, and the canonical reference for doing this well is the interface of Dead Space, whose designers described their approach as being diegetic not merely by design but by implementation — the interface rendered as part of the world, as the character's own equipment and body, so that it never broke presence. Project D follows the same principle: Kenny's voice and posture carry his internal state, the Notebook and Bestiary are physical objects he holds, the Binoculars are an in-world tool, and information lives in the world rather than floating over it. One pragmatic lesson from the games that have shipped this philosophy is carried forward deliberately: an optional, conventional readout is planned from the start as an accessibility provision, because retrofitting accessibility onto a purely diegetic interface late in development is far more expensive than reserving room for it early, and the existence of an optional aid for players who need it does not compromise the default experience for those who do not.

## 13.7 — The Highest Technical Risks

The risks below are ordered by how much they could cost the project, and each is paired with the reason it is survivable.

**The Shared Senses, as a design problem wearing technical clothes.** The technology of the Shared Senses is cheap and certain; its *feel* is neither. The real risk is not that the frustum tests, audio queries, or haptics fail — they will not — but that the fusion of four channels and the sensory output layer cannot be tuned to make the player feel they have become Kenny, rather than feeling narrated at by a chatty camera or buzzed at by a gimmicky controller. This is design risk, not technical risk, and it is the project's largest single risk precisely because no amount of engineering retires it. It is mitigated only one way: by building the Shared Senses first, before any content, and judging them by feel (§13.3, §14.2), with the narrower fallback held in reserve.

**Creature behavioral AI.** The behaviors are buildable on the stock AI stack, but T-rex locomotion warping and raptor pack coordination are the parts most likely to need iteration, and large-creature motion matching is sensitive to animation quality. The risk is schedule, not feasibility: it is contained by prototyping one creature fully — the territorial medium predator, the simplest legible behavior — before attempting the T-rex or the pack, and by holding the curated-blendspace fallback for locomotion if motion matching resists.

**The Voice selection engine at scale.** Selecting from thousands of tagged lines in real time against a multi-dimensional query, while enforcing cooldowns and no-repeat-in-session rules, is non-trivial, and its performance is felt directly because the player experiences the game through it. It is de-risked by its strong precedent (the rule-based selector is a documented pattern, §13.2) and by prototyping with placeholder text lines long before audio exists, so the selection logic is proven independent of the content.

**Tuning The Thread.** The Thread's machinery is modest and its technical risk low, but the calibration of weights, thresholds, the calm predicate, and the fictional-time floors is genuine design work, and a poorly tuned drama manager either fires events at the wrong moments or never fires them reliably. It is contained by building one real narrative beat end-to-end early and tuning against it before more beats are authored.

**Adopting Mass before it is needed.** Unreal's large-agent framework is powerful but heavy, still evolving across engine versions, and carries a real learning cost. The risk is spending that cost speculatively on herds that actor-based steering would have handled. It is avoided by a simple rule: stay on actor-based steering until profiling proves a herd too large for it, and only then adopt Mass.

**Middleware maturity.** The audio middleware is mature and low-risk; the narrative-scripting middleware sometimes reached for is less so on Unreal, which is the second reason — beyond fit — that the bark engine is a custom rule evaluator rather than a branching-narrative tool. Any third-party tool adopted is version-pinned and tested early rather than trusted to a marketing description.

**Drawing recognition feel.** The recognizer is solved and trivial; the residual risk is that the score the algorithm returns and the score a human would call fair diverge, especially once the proportional pass (§13.5) is layered on. It is closed by prototyping the drawing system with real players and tuning the thresholds against their judgment, not the algorithm's.

## 13.8 — Scalability

The architecture scales along the tier structure (§14). The message bus, the data-driven content pipeline, the Voice rule-based selection engine and its Shared Senses perception model, and the Thread drama manager are all built in Tier 1 and extended — not rebuilt — in Tiers 2 and 3. Adding the Drawings section and its recognizer, Window species, anomalies, the Gang, and additional Track axes in Tier 2 means adding data and message handlers to existing systems, not new architecture. This is the technical justification for the strict build order: the Tier 1 systems are the foundation every later system stands on, and building them correctly first — with the message bus carrying debug logging, the content fully data-driven, and the selection engine proven on placeholder lines — is what makes the later tiers additive rather than disruptive.


---

# 14 — SCOPE, TIERS, AND ROADMAP

## 14.1 — What "Indie" Means for This Scope

The systems in Tier 1 alone represent a significant production undertaking, and the word "indie" deserves precision. Here it means independent of publisher funding and creative control — not minimal resources. Tier 1 of Project D sits at the upper edge of what a small team can deliver. It is not a solo project or a two-person studio project; it is a small-team project with a production budget in the range typically associated with AA-indie rather than lo-fi indie.

**Tier 1 minimum team estimate:**

| Role | Minimum headcount | Notes |
|---|---|---|
| Game designer / systems lead | 1 | Owns Track, Thread, Weight of the Body, Bestiary logic |
| Narrative / voice director | 1 | Owns Kenny's Voice, the writing-degradation system, line direction |
| Voice actor (Kenny) | 1 | 3,000–4,000 lines across multiple recording sessions |
| AI / behavior programmer | 1–2 | Dinosaur behavioral AI, combat logic, Thread state machine |
| Generalist programmer | 1–2 | Voice integration, Notebook UI, Bestiary UI, Weight of the Body |
| World / environment artist | 1–2 | Dillfield, surrounding terrain, bandit camp, journey locations |
| Character artist / animator | 1 | Kenny, key NPCs, basic dinosaur rigs |
| Sound designer | 1 | Ambient audio, behavioral cues, Voice integration |

**Estimated minimum team for Tier 1:** 9–12 people. **Estimated timeline (prototype to ship-ready):** 3–4 years at this team size, assuming full-time commitment and no significant scope creep. The Voice system alone — line writing through direction, recording, editing, and integration — is a 12–18 month effort at minimum and is a critical path from end to end, not a parallel feature: without Voice there is no game, because the character is the HUD.

## 14.2 — The Vertical Slice (Proof of Concept)

Before full Tier 1 production, the team builds a vertical slice that proves the design's riskiest claims in a minimal scope: a playable Dillfield with the Shared Senses perception model — all four channels and the dynamic mix, screen-as-body, and haptic outputs — driving Kenny's Voice at minimum viable frequency across all six emotional states; one biome outside the city; two dinosaur species with full Bestiary entries and complete behavioral AI; the Binoculars observation loop end to end; and one Thread threshold that reliably delivers one narrative event through the waiting-state windowing.

The single most important thing the slice must prove is that **the Shared Senses make the player feel they have become Kenny** — that looking down the road and Kenny resolving the far house, hearing the distant vocalization the mix lifts the instant Kenny catches it, and feeling his breath shorten when instinct fires all read as one body perceiving, not several systems bolted together. Concretely: roughly 150 lines written, given the degradation pass where relevant, directed, recorded, edited, and integrated, with all six emotional states, the cooldown and no-repeat rules, the four-channel perception model, and the sensory output layer functioning. If this slice does not make the player feel inhabited by Kenny, the project must be reconsidered before any art or content budget is committed, because every other system in the game feeds this one. The slice either validates the core thesis or reveals which systems need fundamental revision while the cost of revision is still low.

## 14.3 — Tier 1 — The Core Game (Required for Ship)

These systems are the irreducible minimum; removing any one breaks the game's identity.

- **Kenny's Voice and Perception** — the Shared Senses perception model with its four channels and sensory output layer, the three-layer perception model, and the emotional sub-system. The first thing built and the last thing cut. Voice Degradation's hooks are built here even though its effect is felt in late-game content.
- **The Notebook** — the sections People, Events, Places, and "Don't Know What This Is," plus the writing-progression mechanic and the connection work it enables. The Drawings section is Tier 2.
- **The Thread** — the invisible progression system with its safety mechanisms, its fictional-time floors, and the first-session guarantee.
- **The Bestiary and Binoculars** — the observation loop: direct observation with Binoculars, NPC conversation as a filling source, field documents, and the four cataloging stages. Window species and anomalies are Tier 2.
- **Track — Fighting, Field Survival, and Fauna Knowledge** — the three axes that directly affect the primary activities. Tracking, Medicine, Domestication, and Leadership are Tier 2.
- **Weight of the Body — Hunger, Thirst, and Rest** — all three variables with the phase system and the Voice as the signal channel. Status effects are Tier 2.
- **Confrontation — dinosaur combat** with the lore-derived behavior for Velociraptors, T-rex, herbivores, and medium predators, plus the direct and ranged layers of human combat. The stealth layer is Tier 2.
- **The Internal Calendar and time-legibility deliverables** — the seasonal aging, NPC time references, and Kenny's seasonal Voice lines that make the timeline felt.
- **The main story arc** — Kenny as deputy, the attack, becoming sheriff, the journey with Richard, the bandit camp, the rescue. Simulation-discovery content (Puzzle fragments, displaced persons, glitches) appears here at reduced density; full density is Tier 2. The single concrete proof of permanent death (§10.7) ships here as part of the main arc.
- **Dillfield as functional world** — city daily life, named NPCs with schedules, and the Reputation system at the city scale. Extended regional map and external factions are Tier 2.

## 14.4 — Tier 2 — The Full Vision (Target for Release)

These complete what the document promises and build directly on Tier 1.

- **The Notebook — Drawings section** — the shape-based input system, the drawing-recognition algorithm, the drawing-progression mechanic, the NPC identification pathway to the Bestiary, and memory-fragment drawings.
- **The Puzzle — full fragment density** — displaced persons with varied types, glitches as intentional narrative events, memory fragments triggering instinctive perception. The dual-level late-game scene design requires this density.
- **Track — Tracking, Medicine, Domestication (Phases 2 and 3), Leadership.**
- **Bestiary — Window species and anomalies** — the rarity system with indirect signaling, and the corrupted-individual detection that depends on complete species cataloging.
- **Human combat — the stealth layer.**
- **Confrontation — status effects and their interactions** — bleeding as environmental signal, source-specific poison antidotes, fractures with real movement impact.
- **The Gang — up to six companions** — Bond and Respect systems, individual skills, permanent death, dinosaur assignments. Richard establishes the pattern during the prologue.
- **Extended world — regions beyond Dillfield's immediate plains** — multiple discoverable locations and NPCs with their own Tracks and knowledge domains.
- **Active Memory Mode** — the optional HUD layer.
- **Voice Degradation as fully realized late-game content** — the eligible-line retirement, the flattened and fragmented replacements, tuned against the late-game Thread progression.

## 14.5 — Tier 3 — Expansion (Post-Launch or Sequel Territory)

Elements that make the full trilogy vision coherent but are not required for the first game to succeed.

- **End of the Line (permadeath mode)** — ships only after Tier 1 and Tier 2 are stable, when deaths feel earned.
- **Full displaced-persons content** — the intelligent avian civilization individuals and the complete range of displaced-person types. The Puzzle works with partial content; full content deepens it.
- **Anomaly domestication** — the edge case requiring the core Domestication system to be deeply stable first.
- **Expanded trilogy-seed elaboration** — the seeds must exist in some form in the shipped game (Kenny's mother, the attacking group's identity, Elliot's situation), but their depth of elaboration is a Tier 3 investment.

## 14.6 — The Prioritization Principle

**Build in tier order. Never start a Tier 2 system before Tier 1 is tested and stable. Never start Tier 3 before Tier 2 is substantially complete.** The temptation during development is to build the most conceptually exciting systems first — anomaly domestication, intelligent displaced persons, full Gang mechanics. That is the failure mode. The game's identity is in Tier 1: Kenny's Voice must work before any other system matters; the Thread must deliver events reliably before the Puzzle has any weight; the Bestiary observation loop must be satisfying before Window species have any value. Ship Tier 1. Everything else is additive.

## 14.7 — Roadmap Summary

| Phase | Goal | Exit criterion |
|---|---|---|
| **Prototype / Vertical Slice** | Prove the Voice pipeline and core loop at minimal scope | The slice feels alive; the core thesis is validated |
| **Tier 1 production (MVP → Alpha)** | Build the irreducible game | All Tier 1 systems functional and integrated; the main arc playable start to finish |
| **Tier 1 polish (Beta)** | Calibrate the deferred numbers; tune Voice density, survival timers, Track thresholds | A complete, coherent, shippable experience on Tier 1 alone |
| **Tier 2 (Full Vision)** | Add the systems that deepen the experience | The game the document fully describes |
| **Tier 3 (Expansion)** | Add permadeath, full displaced-persons content, anomaly domestication, deeper seeds | The trilogy's first chapter at its fullest |

---

# 15 — SYSTEM INTERDEPENDENCIES

## 15.1 — The Dependency Map

| System | Depends on | Feeds into |
|---|---|---|
| **Voice and Perception** | Shared Senses (player view, hearing, smell, instinct; dwell and per-sense salience), emotional-state rules, Bestiary completeness, Track level, Thread state, Internal Calendar | Notebook usage, Thread delivery, Bestiary collection quality, time legibility, threat assessment |
| **Notebook** | Voice (as signal), player exploration | Thread (bonus weight), Bestiary (via drawings, Tier 2), Puzzle comprehension |
| **Thread** | All gameplay actions, Notebook bonuses, Internal Calendar (time floors) | Narrative event delivery, world-state changes, Voice Degradation activation |
| **Bestiary** | Binoculars, NPC conversations, Notebook drawings, documents | Domestication quality, anomaly detection, Voice specificity, threat assessment |
| **Track** | Real skill use, survived situations, NPC teachers | Combat legibility, Voice richness, Domestication access, NPC interaction register, survival timers |
| **Weight of the Body** | Time, activity, environment, Field Survival Track | Combat performance, Voice quality, Track expression |
| **Domestication** | Bestiary, NPC Bonds, Track (Domestication axis) | Bestiary (exclusive fields), Gang composition |
| **Reputation** | All world actions, human-combat consequences | NPC relationship quality, world access, information availability |
| **Bonds / Gang** | Conversations, joint operations, demonstrated competence and judgment (Bond and Richard's Respect variable) | Field capability, world reactions to loss, sixth-slot resolution |
| **Internal Calendar** | Real playtime, sleep, travel | Thread time floors, world aging, Voice seasonal lines, verisimilitude |

## 15.2 — Cross-System Development Priorities (Before Advanced Production)

**Voice and Perception.** Prototype the Shared Senses perception model first, with placeholder lines — it is the foundation the rest of the system stands on, and it must make the player feel they have become Kenny before any line work is meaningful (§6.2). Build all four channels (sight, hearing, smell, instinct) and the three output paths (dynamic mix, screen-as-body, haptics) in the prototype, not sight alone, since the multi-sense fusion is exactly what cannot be validated on paper. Define the exact frequency policy for each zone and the emotional sub-system's numerical values (minimum state durations, intensity decay rates, event limits) before any line is recorded; adjust after empirical tests. Calibrate the per-channel weights — gaze centrality and dwell, audible-event salience, scent propagation, instinct trigger strength — and the state-driven mix transitions alongside the frequency policy, since together they determine how present Kenny's body feels. Prototype with text before recording — write the first hundreds of lines as text, test in a prototype, calibrate frequency and tone, and record audio only after calibration. Define the Voice Degradation eligible-line set and retirement curve before the late-game content pass.

**Notebook and Thread.** Define the exact Thread thresholds, the weight of each event category, and the fictional-time floors. Define the exact weight of Notebook bonuses in each category. Prototype the Drawings interface with real players (its difficulty curve calibrates only through testing) when Tier 2 begins.

**Bestiary and Binoculars.** Define the complete species set, classified by region of occurrence, frequency, primary cataloging path, and Window status. Prototype the Bestiary interface with real players. Define the NPC reaction bank to fauna drawings before recording (Tier 2).

**Track, Confrontation, Weight of the Body.** Define the exact thresholds of each competence axis and the specific effect of each transition. Prototype each dinosaur species' combat behavior and validate against lore before any animation or AI is produced. Define the escalation speeds of each survival variable empirically.

## 15.3 — Known Cross-System Risks

1. The player does not use the Notebook and does not understand why revelations arrive without weight — the prologue must communicate the Notebook's value organically, and the dual-level scene design (§7.3) must protect the non-connecting player's experience.
2. Kenny's writing and drawing improvement perceived as too slow — the improvement curve must be fast enough for the first signs of progress to appear within the first hours.
3. The Thread waiting system poorly calibrated — delivery windows, maximum wait, and the time floors need empirical testing.
4. Anomalies going unnoticed because the species Bestiary was never completed — this must be a conscious design choice, not an accidental consequence.
5. The Weight of the Body perceived as punishment — the line between honest consequence and arbitrary punishment must be documented and agreed before any adjustment.
6. Phase 3 Domestication arriving too early — the Bond-with-the-tamer calibration must be slow enough that Phase 3 arrives when the player has real accumulated experience.
7. The Voice line-volume budget underestimated, causing a mid-production content crisis — the §6.9 numbers are planned against from the start.
8. The fictional-time floors perceived as arbitrary locks — the world-aging deliverables (§11.4) must be strong enough that waiting feels like time passing, not like a gate.

---

*Game Design Document — Project D*
*Created by Jonny Kestler (João Vitor Perazzolo)*
*Document Version 2.0*
