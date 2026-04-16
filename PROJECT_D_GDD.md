© 2026 João Vitor Perazzolo. All rights reserved.

This work, titled PROJECT D, and all its contents—including but not limited to text, concepts, worldbuilding elements, characters, systems, technologies, and narrative structures—are the intellectual property of João Vitor Perazzolo.

No part of this publication may be reproduced, distributed, transmitted, displayed, or otherwise used in any form or by any means, electronic or mechanical, including photocopying, recording, or any information storage and retrieval system, without prior written permission from the author, except for brief quotations used for review or academic purposes with proper attribution.

Unauthorized use, reproduction, or adaptation of this material is strictly prohibited and may result in legal action under applicable copyright laws.

All rights reserved.

# PROJECT D
## Game Design Document — Master Edition

**Genre:** Singleplayer RPG — PC & Console  
**Format:** Indie Project  
**Created by:** Jonny Kestler *(João Vitor Perazzolo)*  
**Document Version:** 1.0 — Internal Use

---

> This document consolidates the full design documentation for Project D — lore, world-building, characters, and all game systems — into a single reference. It combines the Master Overview, the GDD for Kenny's Voice and Perception, the GDD for the Notebook and the Thread, the GDD for the Bestiary and Binoculars, and the GDD for Track, Confrontation, and the Weight of the Body.

---

# TABLE OF CONTENTS

1. [Design Philosophy](#1-design-philosophy)
2. [Target Audience](#2-target-audience)
3. [The Real World — Lore Foundation](#3-the-real-world--lore-foundation)
4. [The Simulation World](#4-the-simulation-world)
5. [Kenny Collins](#5-kenny-collins)
6. [SYSTEM — Kenny's Voice and Perception](#6-system--kennys-voice-and-perception)
7. [SYSTEM — The Notebook and The Thread](#7-system--the-notebook-and-the-thread)
8. [SYSTEM — The Bestiary and Binoculars](#8-system--the-bestiary-and-binoculars)
9. [SYSTEM — Track, Confrontation, and the Weight of the Body](#9-system--track-confrontation-and-the-weight-of-the-body)
10. [Additional Systems Overview](#10-additional-systems-overview)
11. [Scope — Project D as First of Three](#11-scope--project-d-as-first-of-three)
12. [Development Notes — Cross-System Priorities](#12-development-notes--cross-system-priorities)

**New in v1.2:**
- §3.4 — What Makes This Version Distinct (lore differentiation)
- §5.1a — The Game's Timeline (Kenny's age, game scope, progression implications)
- §7.2 Writing Progression — Functional vs Cosmetic (production clarification)
- §7.3 The Failure Case (puzzle design for non-connecting players)
- §7.4 Drawing Input — Platform Design (PC/Console input solution)
- §7.5 Thread Waiting State — Safety Mechanisms (delivery edge case handling)
- §9.1 Track — Mechanical Specification Framework (tier structure, accumulation logic)
- §9.3 Weight of the Body — Transition Criteria and Timing Framework (phase timers)
- §11.1 Minimum Viable Product and Feature Prioritization (Tier 1/2/3 build order)

---

# 1. DESIGN PHILOSOPHY

## 1.1 — The Core Premise

Most modern games are afraid of losing the player. So they add arrows. Icons. Progress bars. Pop-ups confirming every discovery. Objectives written in the corner of the screen. A HUD that never stops talking.

Project D does not share that fear.

The philosophy behind Project D is simple to state and difficult to sustain during development: **the character is the HUD**. Not a metaphor. A technical, aesthetic, and narrative decision that governs every design choice in this game.

Kenny Collins does not exist to guide the player. He exists because he was built to exist — with a life before the game begins, with decades of implanted memories in a specific world, with instincts formed by that environment and no other. When Kenny reacts to the world around him, he is not executing an interface function. He is being a person in a place he knows. The coincidence that this presence also informs the player is exactly that — a planned coincidence, not a system disguised as a character.

**The player and Kenny learn the world together.** Not in sequence — together, at the same time, through the same experience. The player is not being informed about what Kenny already knows. Kenny and the player are discovering the same things, feeling the weight of the same situations, being affected by the same events.

## 1.2 — The Guiding Principle

> **The player and Kenny learn the world together. When something disturbs Kenny, the player feels it before processing any information about what happened. When Kenny is well, the player is too. When Kenny is shaken, the player's world also becomes quieter.**

Any interface element that interposes itself between what Kenny lives and what the player receives breaks this channel. An emotional state bar on the HUD is not just aesthetically undesirable — it is a betrayal of the principle. It tells the player "Kenny is afraid" before Kenny has had the chance to *show* that he is afraid. It replaces the experience with the label of the experience.

Project D wants the experience. Not the label.

## 1.3 — This Is Not an Accessibility Stance

This is a stance about the type of experience this game exists to offer.

There are players who will not like Project D. Who will find the pace slow, the absence of markers frustrating, the lack of confirmations disorienting. Those players are not wrong — they are accustomed to a different game language. Project D simply does not speak it.

The player Project D seeks is one willing to *inhabit* a world rather than *complete* it. Who understands that standing still for two minutes listening to distant sounds from the plains is not wasted time — it is the game working. Who accepts that Kenny will go through hard things and that the world will feel different for a while, without any bar on screen confirming that it had weight.

**The answer to the fear of losing the player is not to yield. It is to build a character good enough that the player needs nothing beyond him.**

---

# 2. TARGET AUDIENCE

## 2.1 — Who This Game Is For

Project D was not made for everyone. That is not a caveat — it is a declaration of intent.

If you are accustomed to games that put arrows on the map, icons over every point of interest, objectives written in the corner of the screen and notifications confirming you are on the right path, Project D will feel empty in the first hours. Not because it is poorly made — because it was built differently, with a different premise about what makes an experience meaningful.

The game will not tell you where to go. Will not underline what is important. Will not confirm when you have discovered something. The world exists, functions on its own, and it is up to the player to develop the sensitivity to read it. This demands patience. Attention. Accepting that progress sometimes looks like not making progress — until you look back and realize how much you accumulated without noticing.

## 2.2 — The Problem of the First Hours

The greatest threat to the Project D experience is not difficulty — it is boredom defeating curiosity before the player understands what the game is.

A player who opens the game expecting the conventional structure of quests and markers will interpret their absence as a lack of content. They will walk through the city, will not know what to do, and will close before discovering something was waiting — in the conversation they didn't have, in the barn they didn't enter, in the NPC they passed without stopping to hear.

The solution is not to throw the player immediately into the complete Project D experience without any preparation. The complete experience — minimal HUD, no guides, no markers, total freedom and real consequences — is the destination, not the starting point. Before getting there, the game needs to teach the player how to walk in this world.

## 2.3 — The Prologue: Guided Introduction

The first hours of Project D have a more guided structure, deliberately different from what the game becomes afterward. It is not a separate tutorial, not a menu screen with difficulty options — it is the world itself presenting its rules through concrete situations, with enough guidance for the player to understand what is happening before being left on their own.

In this phase, visual guides exist. Not in an invasive way — there is no pulsing arrow on screen nor a red objective in the corner — but there are subtle indications pointing to what deserves attention: a light highlight on an object that can be interacted with, a contextual hint that appears once when a new mechanic is introduced for the first time and never again, an NPC who asks a direct question that naturally guides the player to where to go next.

**The criterion that governs each prologue decision:**

> *A guide is acceptable if its absence would make the situation genuinely impossible to resolve for a player who is paying attention. A guide betrays the philosophy if its absence would only make the situation slower or harder for a player who is not paying attention.*

A second rule: any guidance that appears more than once for the same mechanic has crossed the line. The prologue can show how the notebook works once. The second time the notebook is relevant, the player already knows.

## 2.4 — The Transition

The end of the prologue is not marked by a screen or a warning. It happens organically — a specific narrative moment where the more guided structure dissolves and total freedom opens up. The visual guides disappear. NPCs stop guiding directly. The world starts functioning on its own, without hand-holding.

This moment coincides with a significant narrative event — something that permanently changes Kenny's situation and requires him to make decisions on his own. The player does not notice that the tutorial ended because no screen announced there was a tutorial. They notice because the world changed and now demands more of them.

---

# 3. THE REAL WORLD — LORE FOUNDATION

## 3.1 — The World Context

In a dystopian future, artificial intelligence reached an unprecedented level: it became possible to **simulate entire realities** with complete fidelity — full universes, with consistent physics, their own history, and billions of lives functioning within them. Alongside this, **mental upload technology** was developed: the complete transfer of human consciousness into one of these simulations.

The process is **irreversible**. Whoever uploads abandons their physical body forever. There is no return.

## 3.2 — UpClouD

**UpClouD** is the largest alternative reality company in the world. No real competition exists — UpClouD holds a massive monopoly over all artificial intelligence and simulation technology on the planet. All infrastructure, all development, all control over simulated realities passes through it. It is a corporation that grew beyond what any regulation could keep up with, and by this point operates practically as an entity above governments.

The main service costs what most people could never afford — but UpClouD offers an alternative:

> *Deliver your physical body. In return, gain one hundred years of simulation in any reality of your choice.*

**The secret:** UpClouD's AI does not operate on conventional silicon. The processing power that sustains entire simulations requires a computational capacity that no artificial hardware architecture has achieved with sufficient efficiency. The solution UpClouD found — and keeps as its most protected secret — is the human brain.

After upload, the user's consciousness is transferred to the servers. The body remains. And the body, with its intact and biologically functional brain, is integrated into UpClouD's physical infrastructure. Brains are connected to proprietary machines and begin to operate as organic processing units — biological CPUs running in parallel, sustaining the computational load that keeps the simulations alive.

The exchange program — body for one hundred years of simulation — is not a generous concession to those who cannot pay. It is the primary business model. Rich clients pay with money. Poor clients pay with what they have. UpClouD prefers the latter.

## 3.3 — What Makes This Version Distinct

The individual components of Project D's real-world lore exist in recognizable territory: consciousness upload (Upload, Black Mirror), simulated reality (The Matrix), corporations above governments (Neuromancer, Cyberpunk), brains as computational substrate (The Matrix again). Recombination of familiar elements with original execution is legitimate design — but for a project that will be presented to collaborators, publishers, or players, the question of differentiation deserves an explicit answer rather than an implicit one.

**What Project D does that its references do not:**

The Matrix uses human brains as batteries — a metaphor for passive exploitation. Project D uses them as active processors: the brains are not storing energy, they are *thinking*, running the simulations that other uploaded minds inhabit. The people who chose to upload to escape poverty are, unknowingly, the infrastructure that makes other people's escapes possible. The exploit is not that humans are asleep while machines drain them — it is that humans are fully active, believing they made a free choice, doing the computational labor that sustains a system that profits from their desperation. The horror is voluntary.

Upload and Black Mirror explore what consciousness in simulation means for identity and relationship — usually from a position of awareness. The character knows they are uploaded or discovers it early. Project D's distinctive premise is the *permanent unawareness*: Kenny will never know. The discovery the player makes is not a discovery Kenny makes. The gap between what the player understands and what Kenny can never understand is the emotional engine of the entire trilogy.

The irreversible-death mechanic is not a roguelike conceit. It exists because the attack introduced a bug — a real software failure with narrative cause — and the bug operates on the lore's own logic: each person in the simulation runs on a server, and servers can be shut down. Death is permanent not as game design philosophy but as consequence of a specific technical failure in a specific moment of the fiction's history. The mechanic and the story are the same thing.

Finally: the simulation Kenny inhabits is not a digital facsimile of the real world. It is a genuinely different world — dinosaurs never went extinct, human biology diverged, an entirely distinct civilization emerged. Kenny is not a person dreaming they are in the real world. He is a real-world person dreaming they are in a world that never existed. The distance between the two realities is not a crack in an illusion — it is a canyon that takes the entire game to begin crossing.

## 3.4 — The Attack

### The Group

The attack on UpClouD was executed anonymously. No one publicly claimed authorship — but those who did it know what they did, and did it with conviction.

The group operates from a central belief: whoever uploads is already dead. There is no recovery of the mind once the process is completed. What UpClouD sells as a new life is, in their view, just an elaborate way to kill people while preserving the illusion that they still exist. The body is delivered. The mind that continues in the simulation is not the same one that entered — it is a copy, an echo, something that believes it is human but is no longer. For the group, each upload performed is a murder that society has learned to call a service.

### The Collapse

The attack fried UpClouD's systems. The AI was too powerful to be completely destroyed — it **resisted, but emerged severely damaged**. The reality management system entered total collapse. Uploads that were in progress were diverted to completely random realities.

Among these uploads was Kenny's.

Without human supervision and operating in emergency mode, the AI began applying configurations erratically. The bugs generated by the attack corrupted the presets of the realities in progress — including the one Kenny had configured. The random reality he ended up in had its parameters altered by system errors: death in that simulation is **permanent**. It is not a design choice. It is a fault.

When an inhabitant of that reality dies, the server sustaining that individual's simulation shuts down. There is no restart, no continuity. This applies to Kenny — and to any other who arrived in the same reality because of the collapse.

As a general consequence of the damage, simulations began to present **failures and glitches** recurrently: visual distortions, impossible physical phenomena, erratic behaviors that escape the laws of that world.

### Time and the Attack

All of Kenny's story — each day, each year, each decade he lives inside the simulation — happens while the attack is still in progress in the real world. The time inside the simulation does not correspond to the time outside. One hundred years lived by Kenny may equal seconds, minutes, or hours in the real world. The simulation runs at its own pace, completely dissociated from the external timeline.

This means Kenny is not in a stable reality that was damaged and moves forward. He is in a reality being sustained by systems **that are actively being destroyed while he exists inside them**.

### What Remains of Kenny

The servers' failures are not external to Kenny. They happen inside the system that sustains him, that processes each thought, each memory, each reaction he believes is his. As damage accumulates over the decades, events may occur that alter Kenny permanently and irreversibly — not because he lived something and grew from it, but because the code that defines who he is was corrupted.

It may be gradual. It may be abrupt. One day he wakes up different and has no reference to what he was before to notice. A part of who he was simply no longer exists — replaced by something the system generated to fill the empty space, or by nothing, a hole he learns to work around without ever knowing it is there.

**The question the journey silently poses, without ever needing to be said aloud, is whether the man who eventually reaches the end of one hundred years is still Kenny Collins.**

---

# 4. THE SIMULATION WORLD

## 4.1 — A Complete Universe

The AI does not simulate a region or an isolated scenario. It simulates **an entire universe** — with origin, evolution, complete history. The Earth of that world developed like ours, with its own wars, religions, advances and setbacks. The inhabitants have real memories, full lives lived, culture built across generations.

For them, that is the only world that exists. And it is.

## 4.2 — The World That Always Was

In this universe, the dinosaurs were never extinct. There was no impact, no collapse — they simply continued. Continued evolving, continued dominating, continued being the most powerful species on Earth while the first humans were learning to stand upright.

The human being survived by the only advantage it had: **intelligence**.

It was not fast. It was not clean. It was a war of millennia fought in silence, without sufficient records, without monuments — only bones and scars buried in layers of rock. But the species learned. Learned to build shelters that held, to hunt in groups with strategy, to use fire as a tool and as a barrier, to identify behavioral patterns in surrounding animals and transform that knowledge into advantage.

## 4.3 — Human Evolution in This World

The constant pressure of such a hostile environment left marks on human biology itself that differ from what happened in the real world:

**Physical robustness:** generations of natural selection in an environment where physical weakness meant death produced a denser average body, with more resistant bone structure and naturally more developed musculature.

**Senses:** for hundreds of millions of years, early mammals were forced into nocturnal life to avoid the dinosaurs that dominated the day. This produced deeply embedded adaptations: exceptional hearing and smell, capable of building a detailed map of the environment in the dark. The humans of this world inherited this legacy in amplified form.

**Vision:** visual acuity and daytime color perception are slightly inferior to those of large predatory dinosaurs. At nightfall, the advantage reverses — human senses gain ground that the dinosaur's eyes do not easily compensate for.

**Nervous system:** a faster reaction threshold — what in the real world would be diagnosed as pathological hypervigilance is simply the normal state of a healthy person here. Humans also retained exceptional grip strength, agility on vertical surfaces, and instinctive climbing reflexes.

**Social structure:** the need for collective defense accelerated and consolidated the formation of larger communities much earlier. Groups that were too small simply did not survive. Survival required cooperation at scale, and this profoundly shaped how humans in this world build hierarchies, distribute responsibilities, and develop loyalty.

## 4.4 — The Current State

In the days the story tells, humanity has reached a point their primitive ancestors could not have imagined as possible: **equality**.

Not superiority — that has not happened yet. The dinosaurs continue to be creatures of brute strength that no person faces alone without consequences. But the human being is no longer below them. They stand alongside — through force of technology, organization, domestication, and centuries of forced adaptation.

## 4.5 — Society and Domestication

With time, humans developed techniques for domesticating, training, and coexisting with these creatures. A new social order emerged — built on which animals you could tame and maintain. Dinosaurs became mounts, work tools, pack animals, and status symbols simultaneously. Cowboys ride them. Farmers raise them. Hunters track them. The Old West exists — but with sixty-five million additional years walking beside it.

**Taming a dinosaur is not taming a dog.** It is not a matter of patience and affection — it is a matter of language. Each species communicates dominance, submission, agitation, and calm through specific signals: body posture, head movements, vocalizations, even the speed of blinking. A tamer who does not know these signals is not training an animal — they are gambling with luck.

The domestication process of a new species takes generations. Almost all recorded domestication is done by more than one person. The number of participants and required experience scale directly with the size, lethality, and natural aggressiveness of the target species.

**Notable species roles:**
- Edmontosaurus: plays the role bison plays in the conventional Old West — raised in herds, hunted for meat and hide
- Triceratops: functions as a large draft animal and heavy work mount
- Velociraptors (real): the size of a turkey, fully feathered, with colorful plumage. Dangerous not for size — for coordinated group hunting
- Tyrannosaurus Rex: extremely rare domesticated individuals. Owned by lineages of tamers who invested generations in the conquest. "Domesticated" does not mean "safe"

## 4.6 — Dillfield and Its History

Not every region of the world coexists with dinosaurs in the same way. The area where Dillfield was built was, for a long time, an exception.

Long before the city existed, indigenous peoples who inhabited that land conducted a systematic and prolonged hunt that cleared the region of dinosaurs. When it ended, the memory remained in the customs and stories of the peoples who stayed.

A businessman who knew the reputation of that land chose the location to build what would become Dillfield. The city grew. Prospered. Then, across generations, the dinosaurs ceased to be a real concern and became something the elders mentioned sometimes and the young heard with the same attention given to old stories — with superficial respect and little real belief.

**Then they came back.**

No established explanation exists for the return. Nobody knows for certain why animals that had been expelled from that region so long ago began appearing again on the plains around the city. Panic was immediate and proportional to ignorance — most people in Dillfield had never seen a dinosaur in their lives and had no reference for what was happening.

The city survived. Adapted. The right weapons were purchased. Warning signs were fixed to walls. Life continued — different, heavier, but continued.

**Architectural adaptations that remain:**
- Houses with elevated entrances (above Velociraptor ground-level reach)
- Covered wooden walkways connecting neighboring rooftops
- Agricultural terraces on rocky slopes east of the city to limit access by large herbivores

## 4.7 — Technology

The technological base of this world is recognizable — steam engines, precision mechanics, gunpowder weaponry, wrought iron structures. But dinosaurs forced advances that normal necessity would never have pressured so early or so quickly.

In the small weapons shop in Dillfield, among common shotguns and revolvers, there are pieces that do not make immediate sense. Rifles with barrels too thick, calibers no manhunter would need, heavy ammunition kept in reinforced boxes with proprietary markings. An experienced hunter's holster carries two types of revolver — one to solve human problems, another to solve larger ones.

**The technology of this world did not advance out of ambition, but because there was no other choice.**

## 4.8 — Culture and Religion

Religions of this world, in their variations, share a common core that exists in no faith of the real world: **the predator as divinity or as messenger of the divine.**

Civilizations that grew in the shadow of creatures that could decimate them developed, almost universally, theologies that try to explain and negotiate with that power.

Much of what seems like religious ritual in this world is, when closely analyzed, a **survival manual encoded in ceremony** — knowledge about how to observe, read signs, understand patterns wrapped in sacred language to ensure faithful transmission across generations.

In Dillfield, the predominant religion has the Tyrannosaurus as its central figure — not worshiped, but revered as a force of nature that exists beyond human control. There is a small temple in the city where a candle is lit when someone departs for open country and another when they return. When they do not return, the candle burns for seven days.

---

# 5. KENNY COLLINS

## 5.1 — Who He Is

Kenny Collins was 21 years old with a life that was not worth much to him. When he learned about the program, he did not think twice. He accepted the deal, delivered what he had to deliver, and spent weeks carefully configuring every detail of the reality he wanted to live for the next one hundred years.

At the moment of upload, the attack happened.

Kenny did not fall into the reality he had chosen. The system failure threw him into a **completely random one** — and beyond that, erased his memory. He does not know there is a real world. Does not know he did an upload. Does not know he lives inside a simulation. For him, that Old West with dinosaurs is everything that exists and has always existed.

## 5.1a — The Game's Timeline

This is a design-critical clarification that governs progression scale, relationship depth, and narrative pacing.

**Kenny's age at the start of the game (simulation time):** approximately 28–30 years old. The simulation implanted memories of a full childhood and young adulthood in Dillfield — roughly 8 to 9 years of simulated life preceded the point where the player enters. Kenny does not remember those years as if they were yesterday; they are background, the texture of who he is, the way anyone carries their past. The game begins partway through what the simulation defines as his life.

**What the game covers:** the story of Project D spans approximately 1 to 2 years of in-simulation time — from the night of the attack through the resolution of the bandit conflict, the accumulation of discoveries about the simulation's nature, and the delivery of the hundred-year revelation. It is not a years-long saga compressed into hours. It is a specific period, dense with consequence, in one man's life.

**The hundred years as horizon:** at game's end, Kenny is approximately 29–31 years old in simulation time. He has between 68 and 71 simulation years remaining. The cliffhanger lands with full weight because the player has lived one or two of those years alongside him — and now knows there are decades more ahead, with a clock running.

**Implications for the progression systems:** The Track system grows within a compressed timeline — 1 to 2 years of active experience. This means Track axes do not represent a lifetime of mastery but a period of intense, consequence-driven learning. A man can become significantly more competent in one year if every week puts him in situations that demand it. The Reputation system operates at the scale of a small community over that same period — changes are felt quickly because everyone knows everyone and the community is small enough that actions have visible weight within days, not years. The Gang — up to six companions — is a realistic number of close working relationships that can be meaningfully established in one to two years of high-stakes collaboration.

## 5.2 — Physical and Personal Profile

Kenny stands 6 feet tall with a physique that does not deceive. The memories he carries — implanted by the simulation — are of a demanding childhood: his father putting him to work early, taming dinosaurs, carrying, fixing, lifting. A life of manual labor that shaped a body that intimidates before any word is spoken.

He is not good with language. Speaks the minimum, understands the basics and sometimes not even that. When he needs to explain something and cannot find the right word — which happens frequently — he resorts to comparisons and examples from what is around him to make the person understand somehow. The result is involuntarily funny, and Kenny rarely notices.

What he understands very well, however, is a fight. In adolescence he earned the nickname **Crazy Kenny** — not because he sought trouble, but because when the adrenaline hit, something in him lost control. He fights well, with instinct and brute force, but the problem was always knowing when to stop.

## 5.3 — The Beginning

Before Kenny appeared at the sheriff's office as a newcomer, the sheriff already knew him well — everyone in the city did. Kenny was one of those the community liked despite everything, or perhaps because of everything. A fighter, direct, without filters, but without malice. The problem was that the fights did not stop.

The sheriff could have imprisoned him. But imprisoning Kenny would not solve anything — it would just create a different problem. So he thought differently: if it is impossible to make the man stop fighting, at least let him fight on the right side. He called Kenny and made the proposal. Deputy sheriff. Kenny accepted the way Kenny accepts anything — without many words, without much thought.

**It is on a mattress in the back of the sheriff's office that he wakes up on the first day of the story.**

## 5.4 — The City of Dillfield

Dillfield is a small city. The kind of place where everyone knows everyone's name, where news arrives with the stagecoach and problems arrive before that. Dirt streets, weathered wooden facades, heavy sun since early morning — a setting any person would recognize as the Old West.

But whoever pays attention notices something does not quite fit.

The houses have iron bars on the windows and reinforced bars on the doors — too heavy to be protection against thieves, too thick to be decoration. They are old reinforcements, already integrated into the architecture as if they had always been part of the design. On the ground of the main street there are footprints of different sizes and patterns — toes pointing forward, varying depths, shapes no real-world animal would leave. Mixed among each other as if equally common — because they are.

At night, when the wind stops, sounds can be heard from the plains around the city. Not wolves. Not coyotes. Deep and distant vocalizations, sometimes a dry rhythmic sound like steps too heavy for anything familiar. The residents sleep with this as background. Kenny too.

## 5.5 — The Attack

**What happens next has no warning. It never does.**

The group of bandits entered Dillfield at night, mounted, armed — and brought something nobody in the city was prepared to face alongside men: **tamed Velociraptors**. While the bandits advanced through the streets shooting and looting, the raptors were released among the houses — creatures trained for chaos, to cut off escape routes, to transform an organized invasion into a nightmare of multiple fronts simultaneously.

Kenny woke up with the first shot. Went out armed and entered the middle of things before completely understanding what things were. He fought. Shot. Gave and received. At some point, in an alley behind the warehouse, something hit him hard enough to turn out the lights.

When he came back, it was morning. The city was quiet in the wrong way — the quiet of after, not before. The bandits had gone. The father was on the floor, shot dead. **The mother was not there** — and there was no sign of a fight in the room, no trace that she had fled.

And the sheriff was dead — found on a side street, shot, alone.

Kenny stood in the middle of Dillfield for a while he later could not measure. Did not cry. Did not speak. Just stood.

The city had no way to operate without law. And who understood fighting, who was already in service, who the residents knew — it was him. **Kenny is the sheriff now.**

## 5.6 — The Preparation and Departure

Kenny never left Dillfield. Not because of lack of courage — lack of reason. The city was always enough.

Now it is not.

The mother is out there. The gang of bandits is out there. And Kenny is the sheriff of a city that is still standing, with dead to bury and wounded to care for, and that will need to continue functioning after he departs.

Dillfield resolves this the way Dillfield resolves everything — by necessity and without ceremony. People who have known Kenny for years begin to appear. The blacksmith passes by the sheriff's office with a box of ammunition Kenny did not ask for. The oldest tamer of the city appears at the door and says he has half an hour to learn what he will need to know to not die in the first hour. The woman who runs the market appears with provisions and says only that she knows he will bring his mother back.

**Richard** is sitting on the bench outside the saloon when Kenny passes with his supplies. Not the first time Kenny has seen the man — Richard is one of those who exist in the city without fully belonging to it, a traveler who at some point stopped traveling and never found enough reason to start again. Old. Experienced in a way that shows in his movements before it shows in words.

Richard does not offer help. He makes an observation — about the direction Kenny is taking, about the kind of territory that lies that way, about one or two things a man who never left Dillfield would have no way of knowing.

Kenny arrives at the conclusion himself.

*"We'll take care of ourselves,"* someone in the city says before they depart. Not as reassurance. As dismissal. The city is releasing Kenny to do what he needs to do because it believes, with the conviction of those who have survived many things already, that it will be here when he returns.

It is at this moment — with the notebook in his pocket, the supplies on his back, the star on his chest he didn't ask for, and Richard two steps ahead pointing the direction — that **Kenny crosses the limits of Dillfield for the first time.**

**The prologue is over. Not because a screen said so. Because the city was left behind.**

## 5.7 — Richard

Richard is not the type of man who explains himself. Kenny will discover who he is in pieces, over days of riding and nights of camping.

What becomes clear early is that Richard is not on this journey only for Kenny. He is on it because **he needed one**. Dillfield had become a comfortable trap — food, shelter, no real demands on who he had been. A retired man functioning at minimum. When Kenny appeared with the star on his chest and the look of someone who does not know what he is doing but will do it anyway, Richard recognized the opening. Not philanthropy. Utility. A chance to be useful again in a way that matters.

He knows the region — not as someone who studied maps, but as someone who slept in every type of terrain between Dillfield and the horizon, who knows the names of the good waters and those that make you sick, who learned in practice how certain predators behave in this season in this type of climate.

He does not treat Kenny as an apprentice. Does not explain. Observes. Comments when necessary, frequently with fewer words than the situation seems to require. The dynamic between them is not of master and student. It is of two men with complementary abilities navigating territory one knows and the other does not, with an objective both have reason to pursue.

## 5.8 — The Journey and the Bandit Camp

The journey is not linear. Between leaving Dillfield and finding the bandit camp there are days of travel — with all that implies in a world where the terrain has fauna, where the weather changes, where decisions about route and rest have consequences that appear hours later.

**A working farm with a light in the window at the end of the day.** The decision to knock or pass straight through.

**A region where fauna is more agitated than it should be** for that time of year — Richard notices, alters the route, does not immediately explain.

**An abandoned structure in the middle of nowhere** — stone walls, partially collapsed roof, a fire recently used. May be explored. What is inside may be useful.

When the trail finally converges in a clear direction and the silhouette of the fort begins to appear on the horizon, the weight of arrival is greater because the distance covered was real.

**The bandit camp** is not an improvised bivouac — it is a fort under construction. Heavy wood, structure that took time and labor to erect, elevated positions with wide visibility in all directions. The work of a group that planned to stay.

And around the perimeter, loose but clearly positioned, the Velociraptors. Not wild — the same ones that attacked Dillfield, or from the same lineage. Tamed enough to function as sentinels, trained for the type of work they did in the city.

From somewhere inside the fort — indistinct at first, but present — the sound of a fight. A man's voice, loud and impatient. A woman's voice that does not back down.

**Kenny recognizes the second voice.**

---

# 6. SYSTEM — KENNY'S VOICE AND PERCEPTION

> *This system is referenced in all other GDDs of Project D. Its design crosses the entire game and is the layer that transforms the world of Dillfield from a set of systems into a place inhabited by a real man.*

## 6.1 — What the System Is

### The Problem It Solves

Project D is built on absence: no markers, no written objectives, no confirmations. The player navigates a world that does not bend for them — and needs to develop the sensitivity to read it on their own.

But there is a limit to how silent a world can be before becoming unjustly opaque. A game that offers zero signaling is not a challenging game — it is a game that abandoned the player. And a playable character who never reacts to the world around them is not an immersive character — they are a puppet.

The Voice and Perception system of Kenny solves both problems simultaneously, without sacrificing either.

### The Central Principle

> **Kenny perceives the world before the player. What the player hears is the signal that Kenny perceived something. What the player does with that signal is entirely theirs.**

This principle governs every design decision of this system. Kenny's speech is not instruction. It is **presence**.

### What the System Is Not

- Not a mission dialogue system. Kenny does not speak when there is a mission to signal. He speaks because he lives.
- Not a voice tutorial system. Kenny will not say "remember that you can open the notebook by pressing such a button."
- Not a lore commentary system. Kenny is not an audio guide.
- Not a suggestion system. Kenny will not say "you should talk to that person."

## 6.2 — The Three Types of Perception

The perception system is divided into three layers operating simultaneously.

### Layer 1 — World Perception
*What Kenny sees and hears simply by being alive in that place*

This is the broadest and most constant layer. It exists independent of any narrative event or game progression. It is Kenny being an inhabitant of the world.

**What activates it:** weather and environment, fauna of daily life, the city functioning, moments without narrative importance, Kenny's own physical state (hunger, fatigue, old wound pain).

**How it manifests:** the shortest and most frequent reactions of the system. The background noise of Kenny's presence.

**Examples:**
> *(Rain starting mid-patrol)* — *"Damn."* — and keeps walking.

> *(Seeing a small, clearly ridiculous animal trip on a rock near the stream)* — *"...dumb animal."* — said with the involuntary affection of someone who did not want to laugh but did.

> *(Extreme heat at midday)* — *"A hundred degrees in the shade. Should've stayed in bed."*

> *(Passing the city cemetery during routine)* — No speech. Kenny just slows his pace for a second and then returns to normal rhythm. Nothing to say. It is what it is.

**The Frequency Rule:** Reactions cannot be constant. Kenny does not comment on every tree, every stone, every cloud. The correct frequency is that of a real person: they notice things, react to what stands out from the pattern, and pass in silence through the majority.

---

### Layer 2 — Social Perception
*How Kenny reads the people around him*

Kenny spent decades in Dillfield. He knows the people of Dillfield — not necessarily by name, but by type. Knows the rhythm of someone who has something to hide. Knows the difference between a man who is nervous because he had a bad day and a man who is nervous because he did something.

**What activates it:** behavior outside the pattern from familiar NPCs, strangers with something wrong, suspicious group dynamics, things people do not say, moments of common humanity.

**Examples of professional skepticism:**
> *(Two men dispersing too quickly)* — *"Someone must've told them I'm friendly."*

> *(Regular NPC who averts eyes when Kenny passes)* — *"...Raul has something going on. I'll pretend I didn't notice for now."*

**Examples of common humanity:**
> *(A couple fighting in the middle of the street)* — Kenny slows involuntarily, evaluates for a second if it is something to intervene in, and keeps going when it is clear it is just noise.

> *(A child with a huge lizard in his lap, trying to walk it like a dog)* — *"That kid is going to get bitten in slow motion."* — said with involuntary admiration for the absurdity.

---

### Layer 3 — Instinctive Perception
*What Kenny feels before understanding what he felt*

This is the deepest and rarest layer. It is where what Kenny perceives does not come from the simulation's real world — it comes from inside him. Real memories leaking irregularly as the damaged AI oscillates between states of collapse and stability.

**What activates it:** proximity to simulation lore fragments, confrontation with displaced persons, progression of server deterioration, fragments of real-world memory.

**How it manifests:** disoriented, quiet, frequently incomplete. Kenny does not know what he is feeling. What comes out is the edge of something he cannot hold whole.

**Examples:**
> *(Passing through an area where the world's texture pulsed for a frame)* — *"...I'm seeing things. Too hot today."* — but with a hesitation that does not match the explanation he offers himself.

> *(Hearing a distant sound that does not belong)* — Kenny stops. Tilts his head slightly. Looks in the wrong direction — not toward where the sound came from, but where he thinks it should have come from. Silence. Then: *"...where do I know that from?"* — and keeps going.

**The Progression of This Layer:** In the beginning of the game, these reactions are rare and subtle to the point of almost not existing. As the servers deteriorate and the player accumulates fragments, the frequency and weight of these reactions progressively increases.

## 6.3 — The Variation System

### The Problem of Repetition

A character reaction system that repeats the same lines shatters the illusion at brutal speed. The solution is not simply having a large bank of lines for each situation. The real solution is making **what Kenny says depend on who Kenny is at that specific moment** — not just the event that triggered the speech.

### Variables That Define the Speech

Each reaction of Kenny is the product of multiple simultaneous variables:

1. **The type of event** — what Kenny is perceiving
2. **Kenny's emotional state** — where he is emotionally (see Section 6.4)
3. **History with that stimulus** — first time vs. tenth time
4. **Time of day and weather** — affect tone regardless of emotional state
5. **Story progress** — certain lines only exist after certain events

## 6.4 — The Emotional Sub-System

Kenny's emotional state is not just a tone variable — it is the layer that regulates whether the Voice and Perception system speaks or stays silent.

**System flow:**
```
Perception → Emotional evaluation → Kenny's state → Verbal response (or silence)
```

#### The Emotional States

| State | Description | Effect on Mundane Comments |
|---|---|---|
| **Calm** | Default state. Natural frequency. | Fully active |
| **Curious** | Something unusual in perception field. Investigative tone. | Fully active, tone shifts toward investigation |
| **Irritated** | Frustration, conflict, prolonged physical discomfort. | Active but shorter, drier |
| **Tired** | Prolonged exploration, demanding sequences, sleep deprivation. | Rare and slower |
| **Tense** | Imminent danger detected, combat approaching. | Almost entirely blocked |
| **Shaken** | After emotionally heavy events: witnessed violence, death of someone close, disturbing discovery. | Default response is silence |

#### Same Event, Different States

| State | Event: lake with frogs | Response |
|---|---|---|
| **Calm** | Natural observation | *"That lake is full of frogs today."* |
| **Curious** | Already active from another stimulus | *"...there's something different in that water."* |
| **Irritated** | Noise as irritation | *"Damned frog noise."* |
| **Tired** | Minimum reaction | *"...too loud."* |
| **Tense** | Frogs ignored | *(silence — Kenny is not here for frogs)* |
| **Shaken** | Stimulus does not penetrate | *(silence)* |

#### Emotional Intensity Scale

Each state operates in three intensity levels:

| Level | Description |
|---|---|
| **1 — Mild** | State present but contained. Behavior lightly affected. |
| **2 — Moderate** | State clearly active. Tone and frequency of speech visibly altered. |
| **3 — Strong** | Dominant state. Behavior significantly restricted or altered. |

**Rules:**
- Only one emotional state is active at a time
- Mild events increase intensity one level at a time
- Strong events can elevate intensity directly to level 3
- With time and absence of stimuli, intensity decreases one level at a time
- When intensity of a state reaches zero, the state returns to Calm
- The emotional state **never appears as a visual indicator or HUD text**

## 6.5 — The Signaling Scale

Kenny's reactions cover a spectrum from purely mundane to narratively loaded. This spectrum must be **continuous** — without cuts, without obvious distinction between "lore speech" and "ambient speech."

| Zone | Nature | Frequency | System Connection |
|---|---|---|---|
| **Pure everyday** | Kenny existing, no mechanical relevance | High | None direct |
| **World observation** | Kenny noticing something with possible relevance | Medium-High | May connect to Bestiary, Notebook |
| **Social reading** | Kenny reading people, behaviors, dynamics | Medium | May connect to Thread, Notebook, Reputation |
| **Instinctive signaling** | Kenny reacting to something he cannot name | Low | Connects to Puzzle, Thread |
| **Upload fragment** | Memory leak or real-world perception | Very low | Connects to Puzzle, Thread, central narrative progression |

**The Non-Marker Rule:** No Kenny speech has a visual marker indicating its spectrum zone. The "this is important" icon does not exist. The audio alert sound does not exist. The subtitle color change does not exist.

## 6.6 — Behavior Without Speech

Many of Kenny's reactions have no speech. Physical behavior — where he looks, how he walks, where he stops, how long he stays still before continuing — is part of the system as much as what he says. In many cases, it is more effective.

**Examples:**

- **The listening pause:** Kenny stops in motion, tilts his head slightly to the side, listens for two seconds, resumes. No speech.

- **The look that does not complete:** Kenny looks in one direction for a second longer than necessary and then looks away and continues. Not because there was nothing — because there was something Kenny did not find it prudent to observe for longer.

- **The unexplained detour:** In a situation where the path ahead has something wrong, Kenny can emit a signal without speech: stop for a second, look toward the danger, then look toward the alternative path. Not instruction. The behavior of someone evaluating.

- **Breathing and rhythm:** in combat or a tense situation, Kenny breathes audibly. The rhythm of Kenny's breathing in confrontation versus rest is perceptibly different — and the player who paid attention will recognize when Kenny is more tense than the situation should require.

## 6.7 — Kenny's Evolution Throughout the Game

**Early Kenny:** Familiar terrain. Reactions have a more direct tone. More humor when there is humor. More certainty when there is certainty.

**Kenny Outside Dillfield:** The strangeness of someone processing an environment they are still learning to read. More hesitation — not of personality, but of someone outside their established repertoire.

**Kenny with Accumulated Fragments:** Things he would say directly gain a weight Kenny cannot name. A mundane observation that ends with a silence a second too long.

**Late-Game Kenny:** As server deterioration advances, Kenny changes perceptibly. He does not know what is happening to him. The player begins to know. The gap between what Kenny feels and what the player understands reaches its maximum point — and that is the design functioning as it was built to function.

## 6.8 — Production Rules

**What the system never does:**
- Kenny never repeats the same line in the same context in the same session
- Kenny never says something that only makes sense if the player is pursuing a specific objective
- Kenny never uses vocabulary that does not belong to him — game system terminology, mechanic jargon, references that break the fiction
- Kenny never comments on the obvious
- Kenny never speaks about himself in an expository way

**The base tone:** Kenny Collins is a man of few words who uses what he has with precision. Not eloquent. Not poetic. But not stupid — a man who learned to save words because he grew up in an environment where excess noise attracted the wrong kind of attention.

When something has real emotional weight — when it is about his mother, about the sheriff, about someone he lost, about what he is becoming — the tone changes. Gets quieter. Slower. Less speech, more space between words. Not because Kenny is being dramatic — because he is being honest.

**Known Risks:**
1. Insufficient variation volume produces perceptible repetition
2. The system talks too much and becomes noise
3. Instinctive perception lines lose impact if too frequent
4. Behavior-without-speech requires quality animation to work
5. Poorly calibrated emotional state transitions break the real-character illusion

---

# 7. SYSTEM — THE NOTEBOOK AND THE THREAD

## 7.1 — Why These Mechanics Are the Foundation

Project D is a game about a man who does not know what he is, in a world that does not explain what it has. The tension between what exists and what is discovered is the engine of the entire experience.

For this tension to work, the game needed a system that:

1. **Receives** what the player finds in the world — conversations, events, glitches, encounters, fragments
2. **Organizes** this content so the player can revisit and connect
3. **Responds** invisibly to the accumulation of discoveries, advancing the narrative without announcing it is doing so

Neither of these three functions could be fulfilled by a conventional mission system, map markers, or any structure that would inform the player what is important.

**The Notebook receives, organizes, and communicates. The Thread responds. The Voice of Kenny — a separate system — is what connects the two: the signal that precedes the record and the delivery that leads to the event.**

## 7.2 — THE NOTEBOOK

### What It Is

The Notebook is Kenny Collins's work diary. Not a lore inventory, not a world encyclopedia, not a mission system in disguise. It is the physical object that a sheriff who can barely write carries and uses the only way he can: jotting down what he does not want to forget, with the words he has — and drawing when words do not come.

**The Notebook is separate from the Bestiary**, which is exclusive to fauna. The Notebook records everything else: relevant conversations, visited places, events that did not immediately make sense, names, dates, people's behaviors, Kenny's memory fragments, observed glitches, connections the player is trying to make — and the drawings Kenny makes when vocabulary fails.

### How It Arrives to the Player

The Notebook is not explained. There is no tutorial screen announcing its existence.

It appears one early morning in the first days of the game: the sheriff places the object on the table in front of Kenny and says a deputy sheriff who cannot write is half the service. Kenny looks at the notebook as if it were a trap. He keeps it.

The Notebook is in Kenny's inventory forever from that moment. It can be opened at any time. The player decides what to note and when.

### The Organic Sections

| Section | What Kenny records there |
|---|---|
| **People** | Names, descriptions, where he met them, what they said, what they did not say |
| **Places** | Properties, roads, regions — what they have, what is missing, what seems wrong |
| **Events** | What happened, when, who was there, what resulted |
| **Drawings** | Faces, locations, structures, memory fragments, and creatures — everything Kenny represents visually because words do not reach. Fauna sketches within this section have separate organization from other drawings, being the direct bridge to the Bestiary |
| **Don't Know What This Is** | Fragments without category — glitches, memories that do not belong, things that do not add up |

**The "Don't Know What This Is" section carries the most bonus weight for the Thread.** It is where unexplained fragments are kept until the player understands what they were.

### Kenny's Writing: Development Through Practice

Kenny can barely write. Not a metaphor and not an exaggeration — it is the real starting point of the mechanic.

The result, in the first Notebook pages, is what one would expect: **it is like watching a child learning to write in real time.** Swapped letters, words cut in the middle, sentences that start without finishing, invented spellings for sounds he knows but does not know how to represent.

**Progression is through practice.** The only real way for Kenny to improve his writing is to write. Writing is one of the skills of the game's learning system — and like all others, it only evolves through real use.

This is why **it is strongly advisable for the player to start using the Notebook as soon as the mechanic is freed**, even if the first notes are bad. Especially because they are bad.

NPCs and documents scattered throughout the world can accelerate development but do not substitute for practice. An NPC teacher may offer punctual corrections. A well-written diary found on an abandoned farm may produce a perceptible improvement in subsequent entries.

### Writing Progression — Functional vs Cosmetic: A Production Clarification

This question must be answered explicitly before any Notebook content goes into production, because the answer has direct consequences for localization, voice, and writing workload.

**The answer is: functional degradation with cosmetic expression.**

The *content* of each Notebook entry is always intelligible to the player — the game does not produce entries that are literally unreadable. What degrades is the *form*: spelling inconsistencies, fragmented sentence structure, missing words, invented phonetic spellings. The player can always understand what Kenny was trying to say. What they see is the struggle of saying it.

This means:

**Writing workload:** Each early-game entry requires a second pass by a writer to introduce controlled degradation — phonetic misspellings consistent with how a man with Kenny's vocal patterns would approximate a word he's never written, not random errors. This is skilled specialized work. Estimated scope: every Notebook entry produced for the first third of the game requires this treatment, tapering as Kenny's writing develops. Budget the writing pass for approximately the first 30–40% of total Notebook entries by volume.

**Localization:** Degraded writing does not translate directly. A Portuguese speaker's phonetic approximations are not the same as an English speaker's, and neither is the same as a French speaker's. Each localization requires its own pass to produce degradation authentic to that language's phonetics. This is not a find-and-replace job. It requires a localization writer who understands the system's intention and can reproduce the effect natively.

**Voice and narration:** If any Notebook content is narrated, the degraded early entries cannot simply be read by the voice actor in clean speech. The delivery must reflect the content — halting, uncertain, self-correcting. This is a direction note that must be carried into the recording session.

**The production sequence:** write clean entries first, establish what Kenny is saying clearly, then apply the degradation pass on top. Never write degraded-first — it produces uncontrolled errors that are hard to manage consistently.

### What the Notebook Does Not Do

- Never indicates what the player should have noted
- Never signals when a note becomes relevant
- Never automatically connects related entries
- Never confirms when the player reached a correct conclusion
- Never displays completion percentage of any section

**The connection work is entirely the player's.** The Notebook provides the record. The interpretation is human.

### The Notebook Has a Limit — And the Player Does Not Control It

The Notebook is not infinite and the player does not decide what goes in it.

Everything Kenny notes and draws in the Notebook belongs to the game world — conversations he had, places he visited, creatures he saw, glitches he witnessed, faces of people he met, memory fragments he cannot explain. The player does not have the possibility of writing or drawing anything freely.

At the limit — the 100% of the game, where everything that exists in the world has already been discovered — the Notebook will be complete. No blank pages will remain.

### The Notebook Is Optional

The Notebook is not required to advance in the story. A player can go through the entire game without opening the Notebook once, do missions, explore the world, talk to people, and the story will advance. The Thread does not depend on the Notebook to function.

What the Notebook does is make this progression clearer, faster, and richer for those who use it. The difference between playing with and without the Notebook is not of progression — it is of **comprehension**.

## 7.3 — THE PUZZLE — The Truth Kenny Does Not Know

### What the Puzzle Is

The truth about what Kenny is — that he lives in a simulation, that the upload happened, that death in that world is permanent, that the servers are being destroyed as he exists inside them — does not arrive as a revelation. It arrives as accumulation.

The puzzle of Project D is not an enigma with a single hidden solution. It is the progressive reconstruction of a reality that the game itself never directly names. The fragments exist in the world, scattered throughout the entire journey. The work of connecting them is entirely the player's. No system confirms when a connection has been made correctly. No screen says "you found a clue." **The revelation happens in the head of the person playing — or does not happen, if the fragments were not accumulated.**

### The Three Types of Fragment

**Kenny's Memory Fragments** — involuntary episodes. Images of places that do not exist in the Old West. Sensations of artificial light. Voices Kenny does not recognize but that seem to recognize him. They arrive abruptly, without context. The game does not underline them as important.

**Glitches and Distortions** — events of the world, not technical failures. A texture that pulses for a frame before returning to normal. A shadow with the wrong shape. An NPC who freezes for half a second and resumes the conversation as if nothing happened. The first time the player sees any of these, the most natural reading is that it is a bug — and the game does nothing to correct that impression.

**Encounters with Displaced Persons** — conversations with people who arrived from other simulations. Each displaced person tells a different part of the story, without ever having the complete vocabulary to articulate it.

### How Fragments Connect

The central mechanism of the puzzle is **cross-referencing between different sources.** An isolated fragment from any of the three sources explains nothing on its own. Two fragments from different sources that "rhyme" — describing the same thing from different angles — begin to form an image. Three or more create structure.

The Notebook is where this cross-referencing happens — not because the game automatically maps connections, but because the player who rereads what they accumulated can see, on a People page and a "Don't Know What This Is" page, two records pointing at the same thing.

### The Two Fragment Registers

**Subtle fragments** — arrive without marking, without explicit narrative weight, indistinguishable from world texture until other fragments make them legible. The ones the inattentive player will miss. Also the ones that, when the attentive player connects them, have the greatest impact.

**Obvious fragments** — arrive with weight. The glitch is too large to ignore. The encounter is too strange. The conversation drops something the player cannot discard. These moments are intentional — the clues in plain sight — but even they do not deliver the answer. They deliver a fragment that still needs to be connected to others.

### The Failure Case — The Player Who Reaches the End Without Connecting

This is the design question the puzzle system must explicitly answer, not leave implicit.

The player who completes the game without connecting the fragments will arrive at the late-game narrative events — the scenes where what Kenny is begins to be articulated through cutscene and contextual revelation — with less internal context than the player who accumulated and connected everything. The revelation will land as new information delivered from outside, not as a confirmation of what was already suspected.

This is not a broken experience. It is a shallower one — and that distinction matters for how the late-game scenes are written.

**The late-game revelations must be designed to function on two levels simultaneously:**

At the surface level, they must be legible and emotionally affecting for a player encountering these ideas for the first time. The scene cannot assume prior knowledge. It must carry its own weight — the information it delivers, the stakes it establishes, the emotional consequence it produces — without requiring that the player has spent hours preparing for it.

At the deeper level, for the player who accumulated fragments and made connections, those same scenes must feel like arrival rather than arrival *and* information. The emotional register is different. The attentive player does not receive news — they receive confirmation of what they feared was true.

**What the game does not do is penalize the non-connecting player by making the ending incomprehensible.** The story closes. The questions that need answers get answers. The cliffhanger of the hundred years lands with the weight it needs to land with for both players — though the player who built the context will feel the weight differently, more personally, more specifically.

The asymmetry between these two experiences is not a failure of design. It is the intended result of a system that rewards attention without punishing its absence. Both players finish Project D. They finish it with different amounts of what they were given the opportunity to understand.

## 7.4 — THE DRAWINGS

### Why Kenny Draws

When words do not come — which happens frequently — he resorts to what he has: blank pages of the Notebook and the graphite pencil attached to the cover by an old elastic band.

### How It Works

The player can open the Notebook at any time and in the Drawings section, try to visually represent anything they saw or are seeing. The interface is simple and deliberately limited — not an illustration program. It is the digital equivalent of a pencil on paper.

**The drawing works as an identification key:** after making a drawing, Kenny can show the page to NPCs with relevant knowledge. The NPC examines the paper and responds according to what they see.

What the NPC can identify depends on two combined factors:
1. **The quality of the drawing** — determined by the player's effort and Kenny's current skill level
2. **The NPC's knowledge** — each character knows what their life made them know

### Drawing Input — Platform Design

This is a design problem with a history of failure and a solution that must be decided before the drawing mechanic can enter production. The game targets PC and Console. Drawing with a mouse or a controller analog stick as a primary mechanic is not a trivially solved interface problem — it has been attempted in games and reliably produced player friction when the quality of the output directly determined gameplay outcomes.

Project D's drawing mechanic is load-bearing: drawing quality affects NPC responses, Bestiary access, and Thread weight. This means the input layer cannot be frustrating or players will abandon the mechanic, which undermines the entire Notebook system.

**The proposed solution: shape-based approximation, not freeform drawing.**

Rather than asking the player to produce freeform art with an analog stick, the drawing interface works from a constrained vocabulary of shapes and marks that Kenny can place and adjust on the page. The player chooses from a set of marks — lines, curves, ovals, triangular forms, proportional guides — and positions them to approximate what they saw. The system reads the combination and proportions of marks placed, not the smoothness of a continuous line.

This approach produces results that *look* like rough sketches — because the marks are simple and imprecise — while making the input achievable on any platform. A player with a mouse can refine placement more quickly, but a player with a controller can produce a recognizable approximation without fine motor precision that analog sticks cannot deliver.

**Quality in this system is determined by completeness and proportion, not by line smoothness:**

A drawing that correctly captures the general body ratio of an animal (long neck, quadruped, large) reads as a recognizable attempt even if the lines are rough. A drawing that gets the proportions wrong — a Brachiosaurus sketched with the neck as short as its body — will confuse NPCs even if the lines are perfectly placed. The challenge is observational, not manual. This is the challenge that belongs in Project D.

**Progression:** As Kenny's Track in drawing increases through practice, the available mark vocabulary expands — more precise curve tools, finer proportion controls, the ability to add detail marks for texture and surface features. Early Kenny draws blobs and angles. Late Kenny draws recognizable animals with indicated scale and behavioral posture. The progression is visible in what the interface lets him do, not in what his hands can physically accomplish.

**PC and Console parity:** Both platforms use the same interface model. Mouse users have smoother placement. Controller users navigate a cursor over the page with the analog stick and place marks with buttons. Neither platform has a significant gameplay advantage — the observation challenge is the same on both.

### Kenny's Drawings: Development Through Practice

The starting point of Kenny's drawings is even worse than the writing. He has never drawn in his life. **It is like watching a child learning to draw in real time** — with all the honesty and all the failure that implies.

NPCs react to what they see, not to a statistic. In the first attempts:

> *The tamer picks up the notebook, turns it sideways, frowns. "Does this have four legs?" — "I think so." — "Good. Reduces the options."*

> *The hunter looks for a long time. "I don't know what you saw, but this here I've never seen anywhere."*

**What Kenny draws:**
- Unknown creatures (for later identification — these are the direct bridge to the Bestiary)
- Location maps — floor plans of properties, alternative routes, enemy camp layouts
- Faces — portraits of people Kenny wants to remember or who disappeared
- Objects and structures — marks engraved on a stone, mechanisms he did not understand, writings in unknown languages
- Memory fragments — when Kenny has an episode of real-world memory leaking, these drawings are the most disturbing in the notebook: places that do not exist in that world, impossible architectures, artificial lights, faceless contexts

**Drawings and the Thread:** Memory fragment drawings add extra weight to the Thread beyond what the event already generated by occurring. Each attempt to visually record a fragment, regardless of how imprecise, counts as additional bonus.

## 7.5 — THE THREAD

### What It Is

The Thread is the narrative progression system of Project D. **It is completely invisible to the player.**

The Thread tracks what the player **does** in the game — not what they note. Completed missions, conversations had, visited locations, read documents, completed encounters, observed glitches, hours of field exploration: everything feeds the system regardless of whether the player has opened the Notebook even once.

As the accumulation of actions reaches certain thresholds, the game responds: an event happens, an encounter becomes possible, a cutscene is activated, a layer of the narrative opens.

**The player never consults the Thread.** Never sees a percentage, a bar, a notification. What they feel is that the world is responding to what was done.

### What the Thread Tracks

**Primary actions — what any player accumulates just by playing:**

| Category | Examples of tracked events |
|---|---|
| Completed missions | Any main or secondary mission concluded |
| Conversations with NPCs | Complete conversations with characters carrying lore information |
| Encounters with displaced persons | Any interaction with characters displaced from other simulations |
| Location exploration | Visited properties, traversed regions, entered abandoned structures |
| Read documents | Letters, diaries, notes found in the field |
| Witnessed glitches | Visual distortions the player was present to see |
| Time in the field | Hours of gameplay outside Dillfield |

**Notebook bonuses — additional weight for those who record:**

| Category | How the Notebook amplifies |
|---|---|
| Notes in "Don't Know What This Is" | Each fragment or glitch record adds extra weight to that event |
| Memory fragment drawings | Attempts to record the real world are worth more than simply having the episode |
| Complete signaling loop | Kenny reacts → player investigates → player notes: this complete cycle has greater weight than the action alone |
| Drawings shown to NPCs | When the NPC's reaction is special, the encounter is recorded with additional weight |

### The Thresholds and What They Open

The Thread has multiple thresholds. They are not fixed points on a straight line — they are weights in multiple categories that need to be reached in specific combinations to activate specific events.

Two players can arrive at the same event by completely different paths. The Thread values real effort, not action volume.

**Example thresholds:**

*First threshold — The Weight of the Deadline:* Kenny begins to understand that a limit exists. Reached by any player who advances in the main narrative and has had at least one encounter with a displaced person.

*Intermediate threshold — The System and What It Is:* Kenny begins to have access to fragments that allow the player to connect what happens to him to something larger — the servers, the attack, UpClouD. Requires significant game volume.

*Final threshold — The Hundred Years:* The revelation of the number. Requires the largest game volume of all — cannot be reached without real hours of exploration, expeditions, and narrative progression.

### How Events Are Delivered

When the player reaches a Thread threshold, the corresponding narrative event **does not trigger immediately.** The Thread enters a waiting state — and waits.

It waits for the player to be in a situation the game considers appropriate for a weighty narrative delivery: a camp set up outside Dillfield, the return to the city after a long expedition, the interior of the sheriff's office at the end of the day, any moment when Kenny is in less urgent movement and the surrounding environment is not actively hostile.

When this window appears, the Thread activates the Voice — which leads the player to where the event will happen through a Kenny speech.

**Not an instruction. Kenny thinking out loud, with the weight of what he has accumulated that day.**

#### Example Delivery Variants for the Same Threshold

**Kenny at camp after a difficult expedition:**
> *"What a week that was... already lost count of how many days I've been out. Need to stop by the sheriff's office, see if something happened I don't know about."*

**Kenny in an unknown village far from Dillfield:**
> *"This place isn't my place. I've been here too long. Dillfield is waiting — and so am I."*

**Kenny resting in an abandoned barn:**
> *"...I've got something in my head I can't shake. Can't even explain it right. I think I need to talk to someone I trust."*

**Kenny returning to Dillfield after a night away:**
> *"Good to be back. Strange feeling, like something's different. Going to walk around the city before I sleep."*

The last speech delivers the event with the most immediacy — Kenny is already arriving in the city and the "walk around the city" is the natural path to the event trigger.

### The Thread and Glitches

**As input:** Observing a glitch already counts for the Thread as a primary action — this happens regardless of the Notebook. If the player also opens the Notebook and records the glitch in "Don't Know What This Is," the weight of that event in the Thread is greater.

**As output:** When the Thread activates a weighty narrative event, it frequently uses a glitch as the vehicle. The world presents the event not as a cutscene interrupting the game, but as a reality distortion that is an organic part of what the damaged simulation does.

### Thread Waiting State — Safety Mechanisms

The Thread enters a waiting state after a threshold is reached and holds the delivery until an appropriate situational window appears. This is the correct behavior. But the system requires explicit safety mechanisms for edge cases where that window does not appear within an acceptable timeframe.

**Safety mechanism 1 — Maximum wait cap:** No Thread event waits longer than 90 minutes of real gameplay time after a threshold is reached. If a delivery window has not appeared naturally within that time, the system widens its definition of an acceptable window — accepting lower-intensity moments it would otherwise have held for. The player notices nothing. The event arrives slightly less perfectly timed than ideal, but arrives.

**Safety mechanism 2 — Minimum window definition:** A delivery window is defined as any continuous 3-minute period where Kenny is not in combat, is not in a high-tension animal encounter, and is not in a mandatory scripted sequence. This definition is intentionally broad — it includes traveling in open country, walking through Dillfield, sitting at a campfire, examining a document. A player who never reaches this definition is a player in constant active combat for 90 minutes, which is incompatible with Project D's design at a level that indicates a different problem.

**Safety mechanism 3 — Stacked threshold queue:** If multiple thresholds are reached while the first is still waiting for delivery, they queue internally. Maximum queue depth is 2. If a third threshold is reached while two are queued, the oldest queued event is delivered at the next available window regardless of timing quality, to prevent queue overflow blocking the most recent and narratively relevant event from reaching the player.

**Safety mechanism 4 — Return-to-city trigger:** Any time Kenny enters Dillfield city limits after being away for more than 30 minutes of real gameplay, the system checks for pending Thread deliveries and considers the entry as an eligible window for the oldest queued event. This covers the most common player pattern — extended expeditions followed by return — and ensures that the city itself becomes associated with meaningful narrative moments arriving.

### The Two Player Profiles the Thread Sustains

**The player who plays without the Notebook** will advance in the story. Will arrive at the main events, will live the revelations, will have a complete Project D experience. What may happen is arriving at certain revelations without enough context to fully understand them.

**The player who uses the Notebook frequently** will accumulate extra weight in certain categories and will arrive at the same revelations with more layers. Will recognize connections before they are made explicit. Will understand what Kenny is feeling because they noted the fragments that built that feeling over hours.

**The Thread does not favor either one. It sustains both.**

---

# 8. SYSTEM — THE BESTIARY AND BINOCULARS

> *This section also covers the Windows system (species rarity) and the Domestication system. The four exist in direct relation: Binoculars feed the Bestiary, Windows define what the Bestiary can or cannot access, and Domestication depends on the Bestiary to be executed with competence.*

## 8.1 — THE BINOCULARS

### What They Are

The Binoculars are an inventory item — a medium-range observation tool that allows examining creatures and environments at distances that without them would require real and dangerous proximity.

Not a special gadget. Work equipment of the type that any man who deals with fauna in open country eventually acquires.

### How They Arrive to the Player

The Binoculars are available for purchase at Dillfield's shop from the beginning of the game. Not a mission reward, not hidden, not needing to be unlocked.

**The prologue creates the need before the item is in the inventory.** At some point in the first hours, the player is in a situation where they would need to see better something that is far away. The situation creates the desire before the system exists. When the player arrives at the shop and sees the Binoculars in the catalog, what happens is recognition, not discovery: *"this is what I needed."*

### How They Work

**Basic state** (without Bestiary filled for that species): the Binoculars allow seeing the creature with visual clarity. This means reading behavior in real time, identifying physical signals, observing unusual physical characteristics.

Nothing is automatically delivered in text. **The player sees. The player interprets.** What the Binoculars do is make vision possible safely — not make what is seen legible without effort.

**Complete cataloging state** (Bestiary at 100% for that species): when pointing at an individual of the cataloged species, all Bestiary information is displayed contextually: documented behavior, threat level, attack and flight patterns, strengths and weaknesses, notes accumulated throughout the journey.

### Uses Beyond the Bestiary

- **Environmental reconnaissance** before entering unknown territory
- **Human threat evaluation** — bandits at distance before any decision
- **Identifying displaced persons** — certain individuals carry physical or behavioral signals distinguishing them
- **Item location** — structures without map markers may be read from outside
- **Anomaly monitoring** — an animal behaving strangely can be observed without provocation
- **Weather and environment reading** — storm formations, fauna concentration, migration patterns

### Binoculars and Active Memory Mode

In Active Memory Mode (optional HUD system), part of the Binoculars' function is integrated into natural navigation. Upon approaching a fully cataloged species with the mode active, Bestiary information appears without needing to manually equip the Binoculars. Species not cataloged remain opaque even with the mode active.

## 8.2 — THE BESTIARY

### What It Is

The Bestiary is the progressive fauna catalog of Project D. It is a **separate object from the Notebook** — not a section of Kenny's notes. It is its own archive, specific to fauna.

Within the fiction, the Bestiary has its origin in the sheriff's role. One of the sheriff of Dillfield's functions, with the return of dinosaurs to the region, is to keep a record of present species — to inform the population about threats, to document incidents, to have reference when something new appears.

The empty record is there when Kenny assumes the role. **What goes into it, from that point on, is what the player does.**

### Bestiary Entry Composition

Each species entry is composed of:

| Field | What it records |
|---|---|
| **Name** | The name Kenny knows — regional common name, tamer nickname, sometimes scientific name |
| **Physical description** | Size, covering (feathers, scales, mixed), standard coloration, distinctive characteristics. Accumulated by visual observation |
| **Behavior** | Activity pattern (day/night/both), territorial or nomadic, solitary or group, general aggression level, known attack triggers |
| **Threat level** | Kenny's practical assessment — not a numerical score, a note in his tone. *"Dangerous if cornered. If you don't provoke, no problem."* or *"Avoid. No exceptions."* |
| **Attack patterns** | How the creature attacks, when it attacks, what it does after |
| **Flight patterns** | How it reacts to threat, when it flees vs confronts, what signals retreat |
| **Strengths** | What makes that creature especially difficult |
| **Weaknesses** | What works against it. Accumulated through experience or NPC information |
| **Kenny's notes** | The most personal field — observations that do not fit the categories above. May be practical or the result of a specific encounter Kenny does not want to repeat |
| **Cataloging status** | Percentage of completeness. Invisible to the player as number — but the partial vs complete state is readable in the entry's visual |

### How the Bestiary Is Fed

**Direct observation with Binoculars:** The main filling source. The amount of time required, at what distance, in what conditions — varies by species.

**Observation without Binoculars:** Works, but requires real proximity. Risk increases proportionally with the species' aggressiveness.

**Conversations with NPCs:** Tamers, hunters, naturalists, experienced travelers. Each character knows what their life made them know. A Dillfield tamer knows regional species. A passing traveler may know species from other regions that the tamer never saw.

**Notebook Drawings shown to NPCs:** The contact point between the Notebook and the Bestiary. A fauna sketch in the Drawings section, shown to NPCs with fauna knowledge, can originate a direct Bestiary entry if the NPC recognizes what they see.

**Documents found in the field:** Naturalist diaries, incident reports from previous sheriffs, letters between breeders, fauna guides with engravings found on abandoned farms.

**Direct experience in combat or interaction:** Certain Bestiary fields only come from real contact. The Kenny's Notes field frequently receives the most specific and useful entries after encounters that demanded attention — and sometimes after encounters that almost were the last.

### The Cataloging Progression

| Stage | State |
|---|---|
| **Empty entry** | Only the name, if Kenny has heard someone mention it |
| **Initial partial entry** | First filled fields — usually physical description and basic behavior |
| **Functional entry** | Behavior, threat level, and attack patterns filled. Point where the Bestiary becomes genuinely useful |
| **Complete entry** | All fields filled. Binoculars display all information when examining an individual of the species |

### The Bestiary and Anomalies

The Bestiary does not have separate entries for anomalies. An anomaly is an individual of an existing species, not a new species.

When the player examines an anomaly with the Binoculars, the reading does not match what the Bestiary says. **That is the signal.** An animal whose behavior, after complete cataloging of the species, should be fully legible — but is doing something the Bestiary does not predict.

**The complete Bestiary makes anomalies detectable.** Without the reference of normal pattern, deviations from pattern are invisible.

## 8.3 — WINDOWS — Species Rarity System

### What They Are

Windows are specific appearance conditions that determine when and where certain species appear. A species with a Window is not always available in the world — it exists in precise conditions of time of day, weather, terrain type, and sometimes world-event state the player does not control.

**The name is internal to development. The game never uses the word "Window."**

### Types of Window Conditions

**Time conditions:** Certain species only exist in specific time windows — at dusk when light changes tone, in the hours before dawn when temperature drops, at the peak of midday heat when most other animals retreat.

**Weather conditions:** Low fog, moderate rain, the dry period after days of rain, the muggy weather before a storm — certain species become active or visible in conditions that others avoid.

**Terrain conditions:** Specific valleys, slopes with particular sun exposure, proximity to watercourses of a certain size, minimum altitude, vegetation type.

**World state conditions:** Some Windows only open as a function of uncontrolled events: the passage of a herd migration attracting opportunistic predators, a season affecting the territoriality of certain species, a long-term weather event that temporarily altered a region's ecosystem.

### The Indirect Trail — NPCs and Documents as the Only Signaling

Everything that exists in the game, without exception, has at least one trail: a conversation that can happen, a text that can be found, a story someone carries and tells if the player stops to listen. **There is no creature, mechanic, or secret that exists without the world around it knowing about it in some way.** The information is there. The player who goes after it finds it.

**Example of indirect signaling:**

> An old tamer in a city two days' ride from Dillfield mentions, in the middle of a conversation about training techniques, that his father avoided a certain region after summer rains because there was "something the pack animals could not stand being near." He does not know the name. Does not know what it was. But the description of his animals' behavior is specific enough that a player with the Bestiary partially filled can recognize the pattern.

> A diary with an entry marked with three red slashes in the margin. The text describes an encounter at dusk, with low fog, on a specific slope. The creature described has no name in the diary — the man who wrote it never knew how to identify it. But he describes the smell the wind brought before the encounter. That smell detail is what connects this entry to a hunter's speech in Dillfield that the player may have heard weeks ago of game — or may not have heard, if they passed without stopping.

## 8.4 — DOMESTICATION

### What It Is

Domestication is the system by which Kenny learns to domesticate dinosaurs — and eventually have them as work tools, mounts, and combat aids. It is not a system that exists from the beginning of the game. It is one that becomes accessible to the player progressively, conditioned by built relationships and accumulated knowledge.

**The lore premise:** domesticating dinosaurs is a trade. Not an innate ability, not an experience-point progression. It is the type of knowledge that takes decades to build, transmitted from generation to generation in specialized families, and requires a specific repertoire of reading animal behavior that most people never develop.

### The Dependency with the Bestiary

**The Bestiary informs Domestication.** Trying to tame a species without having the functional Bestiary profile is working without basic information. The behavior patterns, aggression triggers, stress and receptivity signals — all of this is in the Bestiary.

**Domestication fills the Bestiary with exclusive information.** Certain fields of a species entry only come through domestication contact: how the creature responds to conditioning, what makes it back down without attacking, what works as positive reinforcement, what should under no circumstances be done during the approach.

### The Three Domestication Phases

#### Phase 1 — Outside the System

At the beginning of the game, Kenny cannot tame dinosaurs. Not communicated as a menu restriction. It is simply true within the world.

Before departing Dillfield for the first time, the oldest tamer in the city appears and offers Kenny "half an hour to learn what he will need to know to not die in the first hour." What happens in that half hour is not domestication — it is basic survival: what not to do near wildlife in open country.

In this phase, the player observes domestication from a distance. Kenny does not participate.

#### Phase 2 — Group Learning

Domestication access begins with a specific relationship.

When the Bond with a tamer reaches the right point, the tamer begins including Kenny in operations. **Kenny's role at the beginning is support** — physical presence on the perimeter, control of variables the tamer specifies, active observation. He does not lead. Does not interfere. Does not apply technique because he has no technique. Each successful operation teaches through exposure.

**What the player controls in this phase:** The player does not execute the domestication. The tamer NPC executes. What the player controls is Kenny's support role — positioning, timing of support actions, management of external interference.

#### Phase 3 — Solo Domestication

Phase 3 emerges in the mid-game as a possibility — not a time-invested conquest. It is what happens when the player built the right foundation and the right moment appears.

The tamer evaluates what he saw in months of group operations and makes an observation — about an instinct Kenny demonstrated in a specific situation, about the way he read an animal before the tamer needed to name what was happening — and says something that is simultaneously recognition and permission: *"You can try."*

**Phase 3 restrictions:**
- **By species:** low-aggressiveness species are accessible first
- **By knowledge:** the functional Bestiary for the species is not exactly mandatory — but the probability of error is substantially greater without it
- **By condition:** Kenny's state, time of day, terrain, presence or absence of external interference — all affect the operation

### The Bond with the Animal

A tamed dinosaur is not an inventory item. It is an animal conditioned for a specific relationship with Kenny — and this conditioning has characteristics that depend on how it was made.

**What the Bond with the animal means:**
- The animal responds to Kenny specifically — not any human, not any sheriff
- Trust level affects what the animal does in pressure situations
- The Bond is built through use and time. A dinosaur Kenny does not use for a long time will slowly decondition

**Bestiary notes for tamed individuals:** beyond species fields, a tamed specific animal receives its own note within the entry — not a separate entry, but a personal observation of Kenny about that individual. The Kenny's Notes field, here, is the most intimate record in the Bestiary.

---

# 9. SYSTEM — TRACK, CONFRONTATION, AND THE WEIGHT OF THE BODY

> *The three systems in this section share a philosophy: they operate in the world, not on the screen. The player never consults a level bar, never reads a progression percentage, never receives a blinking icon warning about their own hunger.*

## 9.1 — TRACK — Invisible Progression System

### What It Is

Track is the internal name of Project D's progression system. It exists, operates, and has real effect on every aspect of the game. **The player never accesses it directly** — no statistics menu, no points to distribute, no screen showing Kenny's current level or any NPC's or animal's level.

The system exists **within the world**, not above it.

### The Three Planes of Track

**Kenny's Track** — the playable character's progression. Grows with real skill use, with exposure to high-risk survived situations, with accumulated and recorded knowledge.

**NPC Track** — the competence level of each named NPC in the game. Static in the sense that the NPC exists with the Track they have — but dynamic in that the player learns what that Track means through interaction, not a label.

**Animal Track** — the real threat degree of each species, and within each species, the variation between individuals.

### How Kenny's Track Grows

Kenny does not gain experience by completing missions or killing enemies. **He gains by doing things.**

The system silently measures real use in each competence area separately.

**The Independent Competence Areas:**

| Area | What grows it | Visible effect |
|---|---|---|
| **Fighting** | Real confrontations, survived, against humans and animals | Quality of combat reading improves. Kenny anticipates earlier, positions better |
| **Tracking** | Use of Notebook in the field, observing and recording fauna behavior, expeditions requiring following trails | Kenny begins to verbalize environmental observations that previously passed in silence |
| **Field Survival** | Camping nights, managing hunger and thirst under pressure, using natural resources | Weight of the Body penalties appear later and recover faster |
| **Medicine** | Treating own and companion wounds, correct use of healing materials in field, survived crisis situations | Status effect treatment becomes more efficient |
| **Fauna Knowledge** | Directly with the Bestiary — same system seen from another angle | Kenny's Voice around known species becomes richer, more specific |
| **Domestication** | Exclusively with real domestication operations | Operations previously requiring a veteran companion become possible with less experienced companions |
| **Leadership** | Use of the Gang on expeditions, decisions affecting companions | Companions begin to respond differently — more proactive, more willing to risk |

### Track — Mechanical Specification Framework

The following defines the structural parameters of the Track system. Precise numerical values are to be determined by empirical testing with game prototypes — these are the categories and logic, not the final numbers.

**Each Track axis operates on a 0–100 internal scale, divided into four tiers:**

| Tier | Range | Design label | What changes |
|---|---|---|---|
| **1** | 0–24 | Novice | Kenny's baseline. No special behaviors unlocked. Voice reactions in this area are vague or absent. |
| **2** | 25–49 | Developing | First perceptible changes in Voice specificity and world reaction. NPCs in this domain begin to treat Kenny differently. |
| **3** | 50–74 | Competent | Meaningful capability unlocks. Solo options open in Domestication at this tier. Voice reactions become specific and reliable. |
| **4** | 75–100 | Expert | Full capability expression. NPCs in the domain treat Kenny as a peer. Voice reactions match the richness of a man who genuinely knows this domain. |

**How points accumulate — the unit is "meaningful action", not "any action":**

Not every instance of using a skill contributes equally. The system uses a diminishing returns model within short time windows to prevent grinding. Specifically:

- Each unique context of skill use contributes full weight. Fighting a new type of enemy, treating a new type of wound, camping in a new terrain type — these are unique contexts and generate full points.
- Repeating the exact same action type within 30 minutes of the last instance generates 20% of normal weight. The system is measuring experience breadth, not repetition volume.
- High-stakes survival of a skill use — using Fighting to survive an encounter that was genuinely dangerous given Kenny's current Tier, using Medicine to stabilize a wound during a crisis rather than in calm conditions — generates 1.5× normal weight. Difficulty and consequence matter.

**Cross-axis interactions:**

Certain activities contribute to more than one axis simultaneously, but at reduced weight per axis. A difficult expedition that requires tracking a trail, managing food and water, and treating a wound along the way contributes to Tracking, Field Survival, and Medicine — but at 60% weight per axis rather than 100%, to prevent any single activity from accelerating everything simultaneously.

**NPC teacher acceleration:**

Finding and building relationships with NPC teachers in each domain (the healer, the veteran tamer, the experienced tracker) does not bypass the usage requirement — but it increases the weight of subsequent uses in that domain by 25% until the next tier is reached. The teacher shortens the path; the work still exists.

**These numbers — the ranges, the diminishing returns window, the high-stakes multiplier, the cross-axis percentage — are all placeholders for empirical calibration.** What is not a placeholder is the structure: four tiers, context-sensitive accumulation, diminishing returns within windows, cross-axis interaction at reduced weight.

### How the Player Perceives Kenny's Track

**Kenny's Voice changes.** As specific Track axes grow, what Kenny verbalizes around those situations evolves. In the early hours, approaching unknown fauna in open country, he might say nothing — or say something vague. With developed fauna Track, the speeches become specific: behavior, posture, what that head angle normally precedes.

**The world reacts differently.** NPCs who previously treated Kenny with skepticism begin to treat him with respect. Veteran tamers who in the beginning of the game spoke with Kenny the way they would speak with any novice begin to speak as they would with a man who understands the trade.

**The situations are the same — Kenny is not.** A Velociraptor pack encountered at the beginning of the game and the same pack encountered forty hours later are not mechanically different. What changed is what Kenny knows about Velociraptors, what the player knows about how Kenny moves, and what both developed together during that time.

### NPC Track

Each named NPC has their own Track, defined in production and invisible to the player. This Track determines what the NPC is capable of in each competence area — and the player learns this Track through interaction, not a label over their head.

**For all NPCs** — both those the player encounters in the world and those recruited to the Gang — the Track is fixed. It is the expression of decades of life and experience that person has: it cannot be transferred, cannot be replicated, and is exactly why the loss of a companion is irreversible.

**How the player reads an NPC's Track:**
- **Conversation** — an experienced tamer speaks about animals in a way that reveals decades of experience before the player asks any information about them
- **Behavior in situation** — a companion with high tracking Track notices things others pass without seeing
- **Reputation that arrives before the encounter** — NPCs with high Track usually have history in the world — other characters speak about them before the player meets them

### Animal Track

Animals have Track that manifests as real capability and real behavior. The Bestiary, filled with sufficient information, allows the player to start inferring this before direct contact.

**Track operates in two planes:**

**Species Track** — what that species is capable of, as a pattern. A Velociraptor adult has species Track that includes group coordination, reaction speed, and flanking capability.

**Individual Track** — variation within the species. An old predator in well-established territory has individual Track above the species average. A young one outside the group has individual Track below. Anomalies may have individual Track completely outside species parameters.

### Kenny as Threat Assessment Instrument

There is no level bar above any animal's head. The player evaluates threat through the world. And the most immediate channel of the world is Kenny.

When the system detects that the player is orienting the camera or approaching an animal with intent it reads as confrontation evaluation, Kenny reacts the way a man with the Track he has at that moment would react.

**The assessment scale in practice:**

**Animal far beyond what Kenny can handle:**
> *(Adult T-rex in established territory, complete Bestiary for species)* — Kenny stops. Goes quiet for a second. Then, low, almost to himself: *"No. Not today."* — and starts redirecting without waiting for the player to decide.

> *(Unknown creature, medium size)* — *"Don't know what this is. And I don't want to find out like this."*

**Animal that can be faced with real cost:**
> *(Solo adult Velociraptor, functional Bestiary entry)* — *"Can do it. But I need cover at my back before I start."*

> *(Large but elderly-moving animal)* — *"This one's slow. More than it should be."* — pause — *"Still too big to be careless."*

**Manageable animal:**
> *(Young herbivore, non-aggressive, complete cataloging)* — *"This one isn't even paying attention."*

> *(Small, low-aggressiveness cataloged predator)* — *"I might not even spend ammo on this."*

**Unknown animal:**
> *(First time Kenny encounters species without any Bestiary entry)* — Kenny stops completely. Studies. When speech comes: *"Never seen this before."* Then: *"I don't know if I want to find out what this does when it's irritated."*

**The same logic for human adversaries:**
> *(Group of bandits observed from distance — careless formation, weapons stored in ways revealing inexperience)* — *"These guys never had to use that for real."*

> *(Single adversary who positioned before Kenny noticed, uses cover in ways revealing training)* — *"This one knows what he's doing."*

> *(Clear numerical disadvantage — five or more vs. Kenny alone)* — *"This isn't a fight. This is a different kind of problem."*

## 9.2 — CONFRONTATION — Combat System

### The Philosophy of Combat in Project D

Combat exists and has weight. It is not the center of the game — it is a constant and never trivial possibility.

**Avoiding is always a real option**, often the most intelligent one, and the game never punishes the player for preferring not to fight. A predator skirted around is as valid as a predator killed.

### Two Separate Systems

Confrontation operates as two distinct systems. **Combat with humans and combat with dinosaurs do not share the same logic** because they should not: humans and dinosaurs are not the same type of problem.

---

### Dinosaur Confrontation

#### The Lore as Design

The behavior of dinosaurs in combat in Project D is not derived from gameplay convenience. It is derived from the biology established in the lore — and this biology has rules that the combat system consistently respects.

**Consequence:** the player who understands the lore understands the combat. Not because the game explained the mechanical rules — because the world built the context that makes them legible.

#### Tyrannosaurus Rex — Positioning, Not Flight

The T-rex is not a race.

In Project D's lore, the T-rex is a predator of colossal size with significant straight-line peak speed, but with severely limited direction-change capacity due to weight and skeletal structure. It does not pursue prey that changes direction unpredictably because the energetic cost-benefit does not favor prolonged pursuit.

**Combat implications:**
- Fleeing in a straight line from an adult T-rex is a bad decision. Fleeing with direction changes is better — but requires terrain that allows it
- Cover does not serve to hide from a T-rex as it does from a human shooter. It serves to break the line of sight and force the predator to change direction
- A T-rex attack is not a discrete event — it is a process with phases: localization, orientation, displacement, attack. Each phase has visible signals

#### Velociraptors — The Flanking Problem

Velociraptors are small for the predator standard. That characteristic is why they are more dangerous in groups than anything proportional to their size would suggest.

Velociraptors hunt with coordination that goes beyond conventional pack instinct. They are not just animals that attack at the same time — they are predators that distribute roles: one individual assumes frontal attention while others move to flanks and blind angles.

**Combat implications:**
- A single Velociraptor is a manageable problem. Two are a problem of a different order. Three or more create a situation where keeping all in view simultaneously is impossible
- The correct response is not reaction speed. It is preventive positioning: placing Kenny against a wall, in a corner, in any structure that eliminates approach angles
- Tamed Velociraptors operate with increased coordination beyond natural instinct, because they were trained to work with human signals. Eliminating the human operator disorients the group — but not immediately

#### Herbivores — The Panic Danger

Frightened large herbivores are dangerous in a way completely different from any predator.

The distinction is essential: a hungry predator has an objective, has direction, has behavior that can be read and anticipated. A panicked Edmontosaurus has no objective — it has impulse. It is tons of mass in motion without defined direction, not trying to kill, that will not be persuaded to stop by intelligent positioning, and kills accidentally with the same efficiency as intentionally.

**Combat implications:**
- Never run into the movement line of a frightened herbivore
- The instinct to use a panicked herbivore against a predator is a dangerous instinct
- Herds in movement have zones of greater and lesser risk. Edges are more unpredictable. What is in front of the movement direction is where Kenny absolutely cannot be

#### Medium-Sized Predators — Territory Reading

Medium-sized predators — carnivores in the spectrum between an adult Velociraptor and a T-rex — are the most common encounter outside Dillfield.

These predators have established territory. Behavior **within** territory and **outside** territory is different. Some medium-sized predators are intimidatable. The Bestiary, correctly filled, indicates which species respond to intimidation and under what conditions.

#### Anomalies and the Limit of Knowledge

The Bestiary teaches Kenny how animals normally behave. Anomalies are what happens when the system that simulates that animal is corrupted.

A T-rex anomaly with atypical mobility invalidates the positioning that the normal species cataloging would have made safe. The player with a complete Bestiary has more context to recognize when an animal is not behaving as it should.

---

### Human Confrontation

#### Kenny in Human Combat

Kenny is physically formidable. But the problem is not efficacy — it is control.

**Crazy Kenny from the nickname is not caricature.** It is a characteristic formed by implanted memories. When adrenaline rises, something in the containment threshold slips. He fights well, with instinct and brute force, but the problem was always knowing when to stop. This has mechanical weight: in high-intensity human combat, Kenny's emotional state interacts with combat in ways the player does not fully control. The system does not block actions — but the consequences exist.

#### Reading Human Adversaries

Combat with humans in Project D is not symmetric. An inexperienced adversary commits mistakes that appear early: positioning that does not use cover, predictable attack timing, reaction to the first blow that reveals how much it cost. A combat veteran — someone with high fighting Track — does not commit these mistakes.

#### The Three Layers of Human Combat

**Direct physical confrontation** — hand-to-hand fighting and short-range weapons. Where Crazy Kenny is hardest to control.

**Ranged combat** — rifles and revolvers with the world's physics. Ammunition has cost, quantity, specificity. The revolver a Dillfield man uses to solve human problems is not the same as the one used to solve larger problems.

**Stealth approach** — enter, resolve, and leave without the open conflict happening. The most planning-demanding layer and where the reward of having observed from a distance before acting is most direct. The first main mission of the game — enter the fort, get the mother out, leave — exists as an introduction to this layer.

#### Consequences of Human Combat

Combat with humans has consequences that combat with dinosaurs normally does not: **reputation, witness memory, and the weight of what happened in the world's record.**

A brawl in Dillfield resolved with excessive violence is not forgotten by the city. The Reputation system absorbs what happened and redistributes it in Kenny's relationships. Kenny being the sheriff and having acted outside what a sheriff should do carries different weight than being a civilian brawler.

## 9.3 — THE WEIGHT OF THE BODY — Survival System

### The Principle

The Weight of the Body exists to ensure that Kenny is a man in a world, not an avatar in a map.

Hunger, thirst, and exhaustion are real. Not as punitive systems that block progress — as conditions that concretely and progressively affect performance. **The game has no visible bars for any of these metrics.** The player perceives Kenny's state through Kenny's behavior and Voice.

The calibration is between RDR2 2018 and a survival simulator: present enough to create planning tension, absent enough not to become a bureaucratic obstacle between the player and the experience.

### Weight of the Body — Transition Criteria and Timing Framework

The following defines the structural logic governing how phases escalate, how long they take, and what triggers transitions. Precise real-time values are targets for empirical calibration, not final specs.

**Hunger — phase transition logic:**

| Phase | Trigger | Real-time estimate | Transition reset condition |
|---|---|---|---|
| 1 → 2 | 45–60 min without eating, light activity | ~45 min at rest, ~30 min during high effort | Any food item consumed |
| 2 → 3 | Additional 30 min without eating after Phase 2 entry | ~30 min at rest, ~20 min during high effort | Any food item consumed; fully exits Phase 2 |
| 3 → 4 (collapse) | Additional 20 min at Phase 3 | ~20 min at rest, ~10 min during high effort | Requires substantial food — snack resets Phase 3 temporarily but Phase 2 again within 15 min without full meal |

**Thirst — phase transition logic (escalates ~1.5× faster than hunger under exertion):**

| Phase | Trigger | Real-time estimate under normal activity | Under high exertion or heat |
|---|---|---|---|
| 1 → 2 | 30–40 min without water | ~35 min | ~20 min |
| 2 → 3 | Additional 20 min without water | ~20 min | ~12 min |
| 3 → 4 (heat exhaustion) | Additional 15 min without water | ~15 min | ~8 min |

**Rest — phase transition logic (slowest escalation, hardest to reverse):**

| Phase | Trigger | Real-time estimate | Full recovery condition |
|---|---|---|---|
| 1 → 2 | 3 real hours of gameplay without sleeping | ~3 hours | Any sleep restores to Phase 1 |
| 2 → 3 | Additional 2 hours without sleeping | ~2 hours | Requires full sleep (camp or room); brief rest insufficient |
| 3 → 4 | Additional 1.5 hours without sleeping | ~1.5 hours | Requires full sleep; combat effectiveness reduced for 15 min after waking even from full sleep |

**Field Survival Track interaction — phase modifier:**

Each tier of Field Survival Track increases all escalation timers by 15%. A player at Tier 4 (Expert) has hunger timers 45% longer than a Tier 1 player. This represents real acquired competence — eating and drinking in the right amounts, at the right intervals, reading the body's signals earlier. It is not immunity. It is the difference between someone who has lived in the field and someone who has not.

**The calibration principle that governs all these numbers:** a player who is engaged with the game's world — exploring, hunting, managing expeditions with intention — should rarely reach Phase 3 of any variable without having received clear Voice signals beforehand. Phase 3 should feel like a consequence of ignoring information that was available, not of information that was withheld. A player who reaches Phase 4 collapse should be able to identify, in retrospect, at least two moments where the system signaled that something needed attention.

### Hunger

**Phase 1 — Mild hunger:** Kenny eventually mentions he would need something to eat. Not a system warning — just a man with needs. Performance has not yet changed.

**Phase 2 — Moderate hunger:** Physical resistance begins to recover more slowly after intense effort.

**Phase 3 — Severe hunger:** Physical performance degrades concretely. Strength actions — climbing, carrying, sustained hand-to-hand combat — become genuinely harder. The Voice grows scarce and dry.

**Phase 4 — Collapse:** Kenny can collapse in the field if severe hunger is ignored long enough. Not death — incapacitation at a moment and place the player did not choose.

**What Kenny eats:** Any meat from hunting prepared at camp, provisions bought or found, food offered by NPCs on farms along expeditions. Preparation matters — raw meat of certain species produces status effects beyond basic satiation.

### Thirst

Thirst escalates faster than hunger in conditions of heat and effort.

**Phase 1 — Mild thirst:** Kenny mentions it in passing — a comment about needing water, delivered with the same casual tone as Phase 1 hunger. No performance impact yet.

**Phase 2 — Moderate thirst:** Sustained effort capacity begins to fall. Kenny sweats visibly — **which has a consequence beyond discomfort: sweat makes Kenny's smell more detectable by fauna with keen olfactory senses.**

**Phase 3 — Severe thirst:** Vision begins to present mild dehydration effects — not incapacitating, but enough to make reading distance and situation judgment less reliable.

**Phase 4 — Heat exhaustion:** Can lead to collapse faster than hunger because phases escalate more quickly with physical activity and temperature.

### Rest

Rest is the longest variable — sleep deprivation effects do not appear quickly, but when they appear, they are difficult to reverse without real stopping.

**Phase 1 — Rested:** Maximum cognitive and physical capacity. Kenny's Voice is at its richest — more observations, more specific fauna reactions, more speeches that reveal what he is perceiving. Behavior without speech communicates presence and attention.

**Phase 2 — Light deprivation:** No performance effect yet. Kenny may mention, in the context of a camp or at dawn, that the night was not good. The player who hears this has the information before needing it.

**Phase 3 — Moderate deprivation:** Combat reaction time increases slightly. The Voice begins to thin — fewer speeches, shorter. The fauna Track system begins to produce fewer observations.

**Phase 4 — Severe deprivation:** Combat and tracking performance degrade significantly. The Voice reflects "Tired" state at level 3. Reactions to events Kenny would normally notice arrive delayed or do not arrive. **The silence between speeches that should be contemplative pause starts to feel like absence.**

**How to rest:** Planned camping — chosen location, checked safety, fire set up to minimize fauna attraction risk. An improperly set camp offers lighter rest. Town and farm rooms offer complete rest.

### Status Effects

**Bleeding** — Kenny leaves a physical trail on the ground while moving. Animals with keen smell detect the scent from a distance. The bleeding trail that already exists on the ground does not disappear immediately — it is active information in the environment for hours.

**Poison** — progressively affects Kenny's motor coordination. The correct antidote depends on the source: Velociraptor venom does not respond to the same treatment as an aquatic creature's venom.

**Fracture** — does not prevent movement, but changes how Kenny moves. Reduced speed, certain movements impossible, pain interfering with precision action concentration. Field treatment stabilizes but does not fully cure: real rest is necessary.

**Disorientation** — caused by head impact, certain anomaly effects, or prolonged exposure to extreme conditions. The environment around Kenny becomes unstable in ways that directly affect player control: directions may seem inverted for moments, sounds arrive out of phase, the camera responds with slight delay. **Not cosmetic — functional.**

**Heat exhaustion** — result of intense effort in high temperature without sufficient hydration. The Voice reflects this in a way the player feels before seeing any performance effect.

### The Weight of the Body and Track

Kenny's Field Survival Track does not eliminate the Weight of the Body. It modifies how Kenny responds to it.

With developed Survival Track: phases escalate more slowly, recovery is more efficient, and Kenny verbalizes the state earlier — which paradoxically is an advantage, because the warning arrives with more anticipation.

With low Survival Track: phases escalate faster, recovery is slower, and Kenny sometimes does not notice what is happening until he is already in Phase 2 or 3. Not because the system penalizes him — because that is how real experience works.

---

# 10. ADDITIONAL SYSTEMS OVERVIEW

> The Thread, the Bestiary, and Windows are fully documented in Sections 7.5, 8.2, and 8.3 respectively. The systems below are those not covered in dedicated sections elsewhere in this document.

## 10.1 — Anomalies — Corrupted Species Variations

Inside each species in the game there is a small, unannounced probability that an individual is born with corrupted attributes. Not evolution. Not natural selection. **It is the code generating something that should not exist** — an error the system did not correct because the system is not functioning well enough to correct everything.

The game does not warn. There is no different icon, no alert music, no indication that the animal ahead is different from others of the same species. The difference needs to be discovered — by behavior, by appearance examined up close, by binoculars used on a creature that should already be known but is not behaving as it should.

**What an anomaly can be:**
- A T-rex with atypical mobility for its size
- A Velociraptor pack with coordination above what the species is capable of
- A pack animal that without warning exhibits predatory behavior
- A medium predator that resists all taming commands but does not attack
- A creature that should be dead from cold but continues moving

**Corruption effects** may include: wounds that do not heal at normal rate, sensory disorientation upon attack, posthumous environmental effects affecting nearby fauna, silently accumulating penalties that appear abruptly.

**The complete Bestiary makes anomalies detectable.** Without the pattern reference, deviations from pattern are invisible.

## 10.2 — The Displaced Persons

The UpClouD collapse did not only divert uploads to wrong realities. The boundaries between different simulations were ruptured. Realities that existed separately collided with each other. Some partially merged. Others dumped their contents into foreign worlds.

In Kenny's world, this means **people from other simulations arrived.** Not as invaders, not in an organized fashion — they arrived as he himself arrived: lost, without clear memory of what happened, thrown there by the chaos of broken systems.

**The Rule That Governs Displaced Persons:** What they bring from their reality of origin passes through the filter of the world where they arrived. Knowledge survives. The form that knowledge takes is reconfigured by available reality.

A displaced person who in their original simulation was a systems engineer does not arrive in Kenny's world building spaceships. They arrive with a mind that understands principles of how complex systems work — and in this world, these principles translate into precision steam machinery of uncommon design. **The knowledge is genuine. The expression is of the world.**

**Variety of displaced persons:**
- Those who do not know what they are (most common — the arrival process erases or fragments memory irregularly)
- Those who remember clearly where they came from — not lost but **trapped**, knowing they cannot return
- Those who do not know and do not want to know — who built a life and developed active resistance to anything that threatens its stability
- Those who arrived without any trace of what they were — living in Kenny's world as any other inhabitant would

**In some simulations, the evolutionary question that produced human intelligence was answered differently** — not by the mammal, but by the avian lineage. Descendants of certain dinosaur species, in other simulated universes, followed a path that led them to build language, civilization, structures of power. The collapse deposited individuals from these civilizations in Kenny's reality in extremely rare cases — dragged here by the server chaos. They are not human users. They are not simple NPCs. **They are something UpClouD never needed to categorize before.**

## 10.3 — The Reputation (The Name)

The Reputation system is not a bar with a smiley face on one side and a skull on the other. It is **a network of perceptions accumulated by each group with whom Kenny interacts:** Dillfield residents, regional farmers, itinerant hunters, merchants, indigenous groups beyond the plains, gangs and factions operating on the margins.

Reputations can conflict. What pleases Dillfield residents may offend external groups. What builds respect among hunters may undermine trust among farming families. Kenny cannot be well seen by everyone at the same time.

## 10.4 — Bonds — NPC Relationship System

Each named NPC in the game has their own relationship with Kenny that evolves over time. Not a friendship meter with numbers — it is the organic result of each encounter, each conversation, each moment when Kenny appeared when he needed to appear or disappeared when he should not have.

**These relationships have direct practical weight.** An experienced tamer who trusts Kenny participates in domestications with real commitment — reads animal signals with precision, makes decisions at the right moment. A NPC with tracking skill who considers Kenny a partner will notice details during expeditions that they would not notice if there just out of obligation.

## 10.5 — The Gang — Recruitable and Customizable Companion System

Kenny can gather around him a group of up to six people — companions who accompany him on expeditions and in city daily life. This group is not formed by menu recruitment. It is formed by **the relationships the player built.** Someone who trusts Kenny enough to go along when things get serious is someone Kenny worked to have by his side.

Each companion has a set of specific skills that define the role they occupy in the group when activated. The player defines the focus of each companion in the gang: who is responsible for the group's dinosaurs, who leads ranged combat, who prioritizes field survival.

**Companions can be lost.** An NPC who dies in the field is not replaced by a functional clone of the same abilities. That person, those decades of experience, that built relationship — it is over. The gang the player reconstructs afterward is different, necessarily. And the world notices the absence in ways that are not announced but appear.

## 10.6 — Active Memory Mode — Optional Adaptive HUD

In the game's options, the player can enable **Active Memory Mode** — a system that transforms accumulated knowledge throughout the journey into visible HUD layers.

Everything Kenny has already discovered, cataloged, and learned is automatically and contextually displayed, without needing to consult tools. In a fully mapped region with completely cataloged fauna, opening the map already shows points of interest, known routes, and recorded notes. When approaching a fully cataloged dinosaur, the species' information appears without needing the binoculars.

**This mode does not deliver what the player has not earned.** The interface only displays what has already been discovered — and unknown regions, uncatalogized species, and not-yet-recorded events remain opaque.

## 10.7 — End of the Line — Optional Permadeath Mode

In standard mode, Kenny's death is narrative — he can die and continue, with consequences that are reflected in the world but without ending the journey. This is consistent with the fiction: permanent death within the simulation is a fact of the universe that Kenny discovers throughout the story, not a system imposed on the player from the start.

**The End of the Line mode** — where Kenny's death permanently ends the session, in alignment with the simulation's rules — is on the development horizon as an optional layer for those who want the full experience of what the lore establishes.

**This mode only exists healthily after the base game is in sufficient stability** so that unjust deaths are a real exception, not a constant risk.

---

# 11. SCOPE — PROJECT D AS FIRST OF THREE

## 11.1 — Minimum Viable Product and Feature Prioritization

This section addresses a structural gap in the document: a complete inventory of systems with no stated build order, no feature tiers, and no explicit definition of what constitutes a shippable game versus what constitutes the full vision. For an indie project, this omission is not a philosophical stance — it is a production risk.

The following divides Project D's systems into three tiers. **Tier 1 is the game.** Tier 2 is what makes it significantly richer. Tier 3 is what makes it everything the document describes. A team should be capable of shipping Tier 1 alone and having delivered a complete, coherent experience. Tiers 2 and 3 are earned through successful development of what came before.

---

### Tier 1 — The Core Game (Required for Ship)

These systems are the irreducible minimum. Removing any one of them breaks the game's identity.

**Kenny's Voice and Perception** — the character-as-HUD principle collapses without this. The three-layer perception model (World, Social, Instinctive) and the emotional sub-system must function before any other system is meaningful. This is the first thing built and the last thing cut.

**The Notebook** — specifically: the sections People, Events, Places, and "Don't Know What This Is." The writing progression mechanic (controlled degradation) and the connection work it enables. The Drawings section is Tier 2.

**The Thread** — the invisible progression system with its safety mechanisms. Without this, narrative events are either scripted in a fixed sequence (which contradicts the game's philosophy) or never reliably triggered (which breaks the game).

**The Bestiary and Binoculars** — the observation loop. At minimum: direct observation with Binoculars, NPC conversation as filling source, and the four cataloging stages. Window species are Tier 2. Anomalies are Tier 2.

**Track — Fighting, Field Survival, and Fauna Knowledge** — the three axes that directly affect the experience of the game's primary activities. Tracking, Medicine, Domestication, and Leadership are Tier 2.

**Weight of the Body — Hunger, Thirst, and Rest** — all three variables with the phase system and the Voice as the signal channel. Status effects are Tier 2.

**Confrontation — Dinosaur combat** — with the lore-derived behavior for Velociraptors, T-rex, herbivores, and medium predators. Human combat (stealth layer) is Tier 2.

**The main story arc** — Kenny as deputy, the attack, becoming sheriff, the journey with Richard, the bandit camp, the rescue. The simulation discovery content (Puzzle fragments, displaced persons, glitches) begins appearing in this arc but at reduced density. Full puzzle density is Tier 2.

**Dillfield as functional world** — city daily life, the NPCs with names and schedules, the Reputation system operating at the city scale. Extended regional map and external factions are Tier 2.

---

### Tier 2 — The Full Vision (Target for Release)

These systems complete what the document promises. They build directly on Tier 1 and cannot exist without it.

**The Notebook — Drawings section** — including the shape-based input system, the drawing progression mechanic, the NPC identification pathway to the Bestiary, and the memory fragment drawings.

**The Puzzle — Full fragment density** — displaced persons with varied types, glitches as intentional narrative events, memory fragments triggering instinctive perception reactions in Kenny. The failure case design (dual-level late-game scenes) requires this density to function.

**Track — Tracking, Medicine, Domestication (Phase 2 and Phase 3), Leadership** — the deeper skill axes that reward extended engagement with specific parts of the world.

**Bestiary — Window species and Anomalies** — the rarity system with indirect signaling through NPCs and documents, and the corrupted-individual detection system that depends on complete species cataloging.

**Human combat stealth layer** — the planning-before-action layer that rewards Binocular observation and pre-engagement analysis.

**Confrontation — Status effects and their interactions** — bleeding as environmental signal, poison with source-specific antidotes, fractures with real movement impact.

**The Gang — up to 6 companions** — Bond system, individual skills, permanent death, dinosaur assignments. Richard as the first proto-companion during the prologue journey establishes the pattern before the Gang system is formally accessible.

**Extended world — regions beyond Dillfield's immediate plains** — multiple discoverable locations, NPCs encountered during expeditions with their own Tracks and knowledge domains.

**Active Memory Mode** — the optional HUD layer. Low development cost relative to what it provides; goes in when Tier 1 is stable.

---

### Tier 3 — Expansion (Post-Launch or Sequel Territory)

These are the elements that make the full trilogy vision coherent but are not required for the first game to succeed.

**End of the Line (Permadeath mode)** — requires Tier 1 and Tier 2 stability before it is safe to ship. The risk of unjust deaths making a permadeath run feel unfair is real; this mode only exists when the base game has been tuned to a level where deaths feel earned.

**Full displaced persons content** — the intelligent avian civilization individuals, the complete range of displaced person types (aware, resistant, unaware, blank-slate). The Puzzle works with partial content; full content deepens it.

**Anomaly domestication** — the edge case that requires the core domestication system to be deeply stable first.

**Trilogy seed content** — the narrative material that plants questions for games two and three. These seeds must exist in some form in the shipped game (Kenny's mother, the attacking group's identity, Elliot's situation) but their depth of elaboration is a Tier 3 investment.

---

### The Prioritization Principle

**Build in tier order. Never start a Tier 2 system before Tier 1 is tested and stable. Never start Tier 3 before Tier 2 is substantially complete.**

The temptation during development will be to build the most interesting systems first — anomaly domestication, intelligent displaced persons, full Gang mechanics — because they are the most conceptually exciting. This is the failure mode. The game's identity is in Tier 1. Kenny's Voice must work before any other system matters. The Thread must deliver events reliably before the Puzzle has any weight. The Bestiary observation loop must be satisfying before Window species have any value.

Ship Tier 1. Everything else is additive.

## 11.2 — Project D as the First Game

Project D is the first game of a planned trilogy. Understanding this is important to calibrate what this game intends to be: not an opening without conclusion, but a complete experience in itself that also opens a larger horizon.

**This first game is entirely contained within the simulation.** Kenny, Dillfield, the Old West with dinosaurs, the progressive discovery of the truth about what he is — everything happens within the limits of that world and that man. The story has beginning, middle, and end. The player who reaches the end will have lived something complete, with a closed emotional arc and all central revelations delivered.

**For current development, this means one practical thing: build Project D as if it were the only existing game, without depending on continuations to close what needs to be closed here.**

## 11.3 — How the Hundred Years Reaches the Player

The game's story does not cover a hundred years. It is the story of a man inside a simulation, told from a specific point in his life within it. What Kenny lives in the game is a slice. The hundred years are the horizon.

**This information arrives to the player in layers:**

**The first layer — the existence of a deadline.** At some point in the discovery about the simulation, Kenny begins to understand that a limit exists. Does not know what it is. Does not know where it comes from. Just knows, in a way he cannot yet completely articulate, that the time he has is not unlimited.

**The second layer — the number.** This only arrives at the end of the game — after the great events, after relationships built and lost, after the player already has a real story with Dillfield and the people who inhabit that world. It is at this moment, with all this established, that the number appears: **one hundred years.** Not as an abstract revelation — as concrete weight.

This moment is a cliffhanger. Project D ends with Kenny standing, with a story behind him and decades ahead, knowing for the first time that the clock is running. Everything that was built continues existing. Everything that can still be built also. **But now there is a visible horizon where before there was only the next day.**

## 11.4 — Seeds — What Needs to Be Planted Here

A seed is not a spoiler of what comes next. It is a question intentionally left open — a character, a situation, a world detail that this game introduces but does not completely resolve, and that exists here precisely so the following game has somewhere to grow.

**Narrative seeds identified:**

**Kenny's mother taken by the bandits** — an absence with weight. Not mentioned in passing — it was the last detail of the worst moment of Kenny's life before assuming the role that defines the entire game. The question of what happened to her belongs to the sequels.

**The group that attacked Dillfield** — an organization with tamed Velociraptors and specific objectives in an Old West with dinosaurs does not arise by accident. What exactly did they want? Who do they work for?

**Displaced persons, including Elliot** — the first game establishes their existence but does not exhaust it. What happens to them over the hundred years? Some will die. Others will remain.

**Kenny's deterioration caused by damaged servers** — a process that begins here and does not end here. What he becomes over the decades, how much of the original Kenny survives the progressive corruption — this is possibly the most important question of the entire trilogy.

---

# 12. DEVELOPMENT NOTES — CROSS-SYSTEM PRIORITIES

## 12.1 — High Priority (Before Advanced Production)

**Voice and Perception:**
- Define the exact frequency policy for each zone of the spectrum. Must be documented and agreed upon before any line is recorded
- The emotional sub-system's numerical values (minimum state duration times, intensity decay rates, event limits) need to be defined before any lines are recorded, and adjusted after empirical tests
- Prototype with text before recording: write the first hundreds of lines as text, test in game prototype, calibrate frequency and tone. Record audio after this calibration

**Notebook and Thread:**
- Define the exact Thread thresholds and the weight of each event category
- Prototype the Drawings section interface with real players. Quality of drawing as mechanic depends on a difficulty curve that only empirical tests will correctly calibrate
- Define the exact weight of Notebook bonuses in each Thread category

**Bestiary and Binoculars:**
- Define the complete set of game species and classify them by: region of occurrence, frequency, primary cataloging path, and whether they are Window species
- Prototype Bestiary interface with real players
- Define the NPC reactions bank to fauna drawings before any line is recorded

**Track, Confrontation, Weight of the Body:**
- Define the exact thresholds of each competence axis and specific effects of each transition
- Prototype each dinosaur species' combat behavior and validate against lore before any animation or AI is produced
- Define the escalation speeds of each survival variable empirically

## 12.2 — Known Risks (Cross-System)

1. **The player does not use the Notebook and does not understand why revelations arrive without weight** — the prologue must communicate the Notebook's value organically
2. **Kenny's writing and drawing improvement perceived as too slow** — the improvement curve needs to be fast enough for the first signs of progress to appear within the first hours
3. **The Thread waiting system poorly calibrated** — delivery windows and maximum wait time need empirical testing
4. **Anomalies going unnoticed because the species Bestiary was never completed** — this needs to be a conscious design choice, not an accidental consequence
5. **The Weight of the Body becoming perceived punishment** — the line defining where it is honest consequence vs arbitrary punishment must be documented and agreed upon before any adjustment
6. **Phase 3 Domestication arriving too early** — the Bond with the tamer NPC calibration must be slow enough for Phase 3 to arrive when the player has real accumulated experience

## 12.3 — System Interdependencies

| System | Depends on | Feeds into |
|---|---|---|
| **Voice and Perception** | Emotional state rules, Bestiary completeness, Track level | Notebook usage, Thread delivery, Bestiary collection quality |
| **Notebook** | Voice (as signal), player exploration | Thread (bonus weight), Bestiary (via drawings), Puzzle comprehension |
| **Thread** | All gameplay actions, Notebook bonuses | Narrative event delivery, world state changes |
| **Bestiary** | Binoculars, NPC conversations, Notebook drawings, documents | Domestication quality, Anomaly detection, Voice specificity |
| **Track** | Real skill use, survived situations | Combat legibility, Voice richness, Domestication access |
| **Weight of the Body** | Time, activity, environment | Combat performance, Voice quality, Track expression |
| **Domestication** | Bestiary, NPC Bonds, Track (Domestication axis) | Bestiary (exclusive fields), Gang composition |
| **Reputation** | All world actions | NPC relationship quality, world access, information availability |

---

*Game Design Document — Project D*   
*Created by Jonny Kestler (João Vitor Perazzolo)*
