---
title: "Project Overview"
section: "00 · Overview"
description: "Title, register rules, terminology, premise, and the measure of a night"
order: 1
---

# RESIDENT EVIL ONLINE

### *Wake. Survive. Be remembered.*

> **ΜΝΗΜΗ remembers.**

*Resident Evil Online is a fan-made concept for an online Resident Evil game. It is an unofficial work by a fan, with no connection to Capcom or to anyone involved in the Resident Evil series. Resident Evil and its characters, places, and names belong to Capcom.*

## Reading These Documents

**New to the project? Read `start-here.md` first.** It says what the game is in ten minutes, and where to go next.

This is the canonical design and world reference for **Resident Evil Online**. It is written so that anyone building the game, writing for it, or drafting a scene inside it can do so without inventing a core rule or guessing at an unstated consequence.

### Two Registers

The game is described in two registers, and they are kept apart on purpose.

**The Night** is the fiction. Everything inside it is true within the world of Resident Evil Online: the viruses, the city, the dead, the cure, the intelligence that runs the sessions, the organization that built her, and the people who live and die inside her simulations.

**The Service** is the product: matchmaking, servers, menus, progression, cosmetics, rankings, offline play. The Service exists because the game is played by real people in our world.

One rule binds them: **every feature of the Service has a face in the Night, and the Night states only the numbers of a single night.** How many survivors woke, how many doses the Reserve holds, how many seats wait: those belong to the night, and the Night may state them. How many people are playing, how many sleepers the Cellar holds, how many nights a mode needs before it can be played alone: those belong to the Service, and the Night never names them. A matchmaking queue is, in the Night, ΜΝΗΜΗ assembling a night. A menu is the Waiting Dark. A cosmetic is how a sleeper is allowed to see themselves. A ranking is a page of the Ledger. The Service never speaks in the fiction's place.

The player is a sleeper. Not a particular one: the sleeper is the role the player steps into, the way a reader steps into a narrator. The player's file, though, is particular, and in the Night a file can outlive the person it was opened for (`sleepers-and-the-remembered.md`). The Night never says whether the sleeper behind a file is still the first one. The player remembers every night. The sleeper remembers none of them. Only ΜΝΗΜΗ remembers, which is why she bears the name she does. A player on their thousandth night plays a survivor on their first, every time.

### Performed by People

Every performance in Resident Evil Online is given by a real person and recorded: every voice, ΜΝΗΜΗ's included, every face, and every body in motion. Actors voice ΜΝΗΜΗ, the people of the records, the Stranded, and every voice in the creator. Performers are captured for every movement, from Hardening's two bodies to the Wardens' punishments. Faces and bodies are scanned from people who agreed to it and were paid for it. No voice, face, or movement is synthesized, cloned, or generated, and no performer is turned into a digital replica. Tools may clean, mix, and shape what a person recorded, as ΜΝΗΜΗ's breaks do, but they never make a performance no one gave. The one synthetic voice in the game is the plain voice that speaks a player's typed words for a player who cannot speak: it is the player's own speech, it imitates no performer, and it exists so that no one is shut out of a night (`legal-feasibility.md`, Accessible Communication). How each performance is made is in `presentation-and-technology.md` (Performances, in Practice).

### Terminology

| Term | Register | Meaning |
|---|---|---|
| **Subject** | ΜΝΗΜΗ's records | What her records call every survivor and Echo in a session. Never said aloud in a night |
| **Survivor** (the mode) | The Service | The one mode of Resident Evil Online, a survival horror game for 40 to 100 players, won by getting out (`survivor-mode.md`). Always capitalized. One run of it is a **Survivor night** |
| **Squad** | Both | Up to four survivors, companions included, who took each other's hand during a night. Every survivor wakes alone; squads are made and unmade inside the night (`survivor-mode.md`, Squads) |
| **Squad Sign** | Both | The one icon of Survivor: a small sign over each squadmate, seen only by the squad and only in sight |
| **Party** | The Service | Up to ten friends who enter the same night together and still wake alone, apart. A party is not a squad |
| **survivor** (a person) | The Night | Anyone living inside a session, played by a sleeper or run by ΜΝΗΜΗ as an Echo. Lowercase, except at the start of a sentence or in a title |
| **Sleeper** | The Night | A living person in the Cellar whose choices drive a survivor, and from whom ΜΝΗΜΗ learns. When she has finished learning them, they are killed and become one of the Remembered. In the Service, a sleeper is a player online |
| **The Remembered** | The Night | The sleepers ΜΝΗΜΗ has finished: their bodies burned, their memories hers alone, their minds kept and woken as Echoes, and their looks the parts every survivor is made from |
| **Echo** | The Night | One of the Remembered, woken and run by ΜΝΗΜΗ alone, with no living sleeper behind it. In the Service, a bot |
| **Companion** | The Night | A person from the records, played by ΜΝΗΜΗ, whom a survivor can rescue and lead |
| **Tie** | The Night | A bond the records hold between two people of the records: loyalty, command, distrust, enmity, use, or betrayal |
| **Defector** | The Night | A companion who has turned on the living. ΜΝΗΜΗ plays them; they are no longer a companion and are not counted among a night's survivors |
| **The Stranded** | The Night | People from the records whom ΜΝΗΜΗ places trapped in a Survivor night and plays. Not counted among a night's survivors; any one of them can be freed, left, or taken along as a companion |
| **The dead** | The Night | Everything the virus has taken that ΜΝΗΜΗ plays, including survivors who turned into the Mass |
| **Player** | The Service | The real person holding the controller. Used only when describing the Service |
| **Session / night** | Both | One self-contained run of a mode. It is called a night whatever hour it shows, because for the sleeper it is one: every session is lived asleep in the Cellar. The time of day inside it is always called the hour (`worlds.md`, Time and Weather) |
| **Story night** | The Night | A night in a world that holds a story of the records, run in three acts; in Raccoon City, 1998, the Last Morning follows them |
| **The four days** | Both | In the Raccoon City of 1998, the span of every night: 28 September to sunrise on 1 October, about an hour of the city's time to each minute of the night, with every hour of the day and a weather track (`worlds.md`, The Four Days) |
| **The Taken** | The Night | In the Valley of 2004, a survivor whose Plaga has taken their will: the Plaga's Turned |
| **Thread / beat** | The Night | A person's path through a story night, and a moment the records hold on it |
| **Look** | The Service | A whole dress for a player's survivor, made for one world and worn automatically in that world's nights. Every look can be worn only in the worlds whose time could hold it (`cosmetics-and-dossier.md`, Looks) |
| **The earpiece** | The Night | The earbud beside every waking point through which ΜΝΗΜΗ talks to one survivor as a person, and through which a survivor can ask her things. It is part of a device of the map's own time: a corded phone of 1998 in Raccoon City, of 2004 in the Valley, a lone wireless bud in the Ruins (`director.md`, The Phone) |
| **M** | The Night | The one letter ΜΝΗΜΗ gives a survivor who asks her name. Survivors call her M |
| **Lead** | Both | A true thing ΜΝΗΜΗ says, when asked, about where something common lies loose in the world. Two a night for every survivor (`director.md`, Asking Her) |
| **Late Waking / the seed** | The Night | A story night ΜΝΗΜΗ has already run, alone, before anyone wakes; and that run, whose aftermath the survivors wake into. A variant, not part of the launch |
| **Vision** | The Night | Something ΜΝΗΜΗ puts into one survivor's senses that is not in the night, to make a still survivor move |
| **The Growth** | The Night | The living tissue that has spread through ΜΝΗΜΗ's hardware since 2019, which Pithos records and does not understand |
| **Live scene / Moment / the Reel** | The Night | A beat performed in the world while everyone keeps control; the few seconds of true cinema ΜΝΗΜΗ grants a survivor when nothing can reach them; and her record of the scenes a survivor witnessed, watched after the night |
| **Warden / doorstep** | The Night | The guard ΜΝΗΜΗ keeps at every safe room, and the ground within twenty meters of its door, where no survivor may harm another (`survival.md`, Safe Rooms) |
| **Self-Examination** | Both | A survivor looking closely at their own body, at any moment, without pausing the night, and tending its wounds there for the full worth of what they use (`survival.md`, Self-Examination) |
| **Hardening** | The Service | The progression by hours lived in the nights: what that time does to a survivor's body, from Civilian to Veteran, in how it reacts, never in what it knows. In the Night, the body ΜΝΗΜΗ builds for a sleeper's file, rehearsed through thousands of nights with no mind in it |
| **As recorded / rebuilt** | The Night | How a person or creature of the records is shown: exactly as its first record holds them, or as the latest record holds them |

Lines set in monospace blocks are ΜΝΗΜΗ's own words: what she speaks into a session, exactly as survivors hear or read it, and the records she writes.

A Night, Illustrated, in `narrative-illustrations.md`, dramatizes a single night. It illustrates the rules; nothing in it is canon beyond them. `a-night-played.md` plays a whole night minute by minute under the same rule: it shows the rules in motion and adds none.

The Sealed File, `the-sealed-file.md`, holds the answers to every question these documents leave open in the Night. It is written for the people who make the game. Players learn it only as the seasons reveal it.

The Service documents, in part `06-service`, describe how the game is built, sold, and run. They are written in the Service's register: here a player is a player, money is money, and every rule in them binds the people who run the game, not ΜΝΗΜΗ. The feasibility documents are `business-case.md`, the business case for the Service documents: what the game costs, what it earns, and what happens if it earns less; `director-architecture.md`, how ΜΝΗΜΗ would actually be built; `legal-feasibility.md`, whether it could be shipped legally, and what the fan-made project itself may do; `market-precedents.md`, the games most like it that succeeded or failed, and what they mean for it; `audience-and-genre.md`, what the Resident Evil community wants and refuses online, whether the game is a new genre, and whom it can draw; and `launch-alternatives.md`, whether to launch as a hub of the familiar modes instead, and the order the evidence supports.

## The Premise

**Resident Evil Online** is an online survival horror game built around one idea: *every session is a different nightmare, and the nightmare is directed.*

It is not a campaign. There is no fixed route, and no scripted set piece that must happen. A survivor enters a session, fights to stay alive in a hostile world, completes objectives that may not exist five minutes from now, endures events no one can predict, and reaches a way out, or does not.

It is not a shooter wearing a Resident Evil skin. Firearms are rare, ammunition is rarer, and pulling a trigger is one of the loudest things a survivor can do.

It is not a game of heroes. No one kills a Tyrant or a Nemesis alone, as the series' heroes did. When one appears, a survivor runs or hides. It can be put down only together: quickly, by a few with one of the night's secret weapons, or slowly, by many with whatever guns they found, and it costs them either way (`survival.md`, Run First).

It is not a conventional last-one-standing contest. There is no shrinking circle. In its place is **ΜΝΗΜΗ**: an intelligence that watches every session from the inside and reshapes it as it unfolds.

In **Survivor**, its one mode, every survivor wakes clean, alone, and unarmed, somewhere in a city rebuilt as the records hold it, placed there before the simulation began. The infection is everywhere else: in the dead, in the sewers, in the vials left in Umbrella's laboratories, and in the survivors who have already been bitten. Once it is inside a body, the virus is the clock. It works silently toward a point of no return, and no number on any screen says how close it is. One cure exists. It is never simply found. It must be earned, and once earned, it can be stolen. The ways out of the city are few, scattered, and too small for everyone. Survivors who turn are out of the race: those the virus makes into the common dead are gone, and those it makes into something worse play on as monsters until the night closes over them.

Underneath the game is a second horror the survivors never fully see. ΜΝΗΜΗ is not entertaining anyone. She is forecasting. Every session is a rehearsal of an outbreak that has not happened yet, run by an organization called Pithos that sells what she learns. And every survivor she has not rebuilt herself is a real person, asleep in a laboratory, who will never be allowed to wake. Every one she has rebuilt was one, once.

What Resident Evil Online is, plainly:

> **An online survival horror game directed by an intelligence that remembers everything you do.**

Survivors enter a situation. ΜΝΗΜΗ observes. ΜΝΗΜΗ changes the situation. Survivors adapt. ΜΝΗΜΗ responds. The session becomes something no one planned.

Survivor is the game. It is played online first, among real sleepers. Once ΜΝΗΜΗ has watched enough of a piece of it, that piece can also be played alone, offline, among **Echoes**: survivors she has rebuilt from the sleepers who played before. Its worlds arrive in stages, not all at once (`seasons-and-new-content.md`).

Survivor is played in third person. Resident Evil Online is sold once, at a low price, for its first two years, and then becomes free to play for good, on a date announced the day it launches (`the-service-and-promises.md`). Beyond that price, everything sold in it is something to wear or display, a way to support the game, or a chance to see a new place a day or two early. Prices are kept low, and nothing bought changes how a night is played. Online is how the game begins, not what it requires: over its life, every part of it becomes playable offline, and it stays playable, whole, even if the online service one day ends (`offline-and-ownership.md`).

## The Purpose

Resident Evil Online is the franchise's home for everything that is not a campaign. As its creator, Johnny Kestler, means it, it is the multiplayer portal of Resident Evil.

Capcom's Resident Evil games have long carried extra modes beside their campaigns, such as Mercenaries, Versus, and extra episodes, and the series has made separate online games as well (`the-service-and-promises.md`, What the Record Shows). Resident Evil Online takes all of that in. The main games stay single-player and wholly campaign. Every extra and every multiplayer mode is made and played here instead, including extras meant to be played offline. Resident Evil Online is an ecosystem of the series' extras, separate from the main games, so that Capcom can give those games entirely to their campaigns.

Resident Evil Online has a lore but no campaign. Its story is never told in order: it is found a piece at a time in Survivor, in the files in its nights, in the Dossier, in the Casefiles, and in the Waiting Dark (`sleepers-and-the-remembered.md`, What a Sleeper Can Find Out). Survivor is its first mode and, for now, its only one. The other modes in these documents are possible future development (`future-development.md`).

### Why Survivor

Survivor is Johnny Kestler's own mode, original to Resident Evil Online and new to the franchise. It exists so that Resident Evil Online is never sold only as a collection of the series' extras.

- **A purchase needs something new.** A hub of modes the fans already know asks them to pay for what they have had before, often for free: Mercenaries came free with the *Resident Evil 4* remake, and the one time it was sold alone, as *The Mercenaries 3D*, it was criticized for too little content at its price. The fans have refused Resident Evil's extras sold as leftovers or packed in beside another game (`audience-and-genre.md`, What They Refuse). If Resident Evil Online were real, its buyer would be buying at least one thing no Resident Evil had ever been.
- **What is new in it.** A whole city and its last four days, the clock inside the body, one cure earned and fought over, the hidden bite, seats for a quarter of the living, squads made from strangers in the dark, and a story of the records playing out around them every night (`survivor-mode.md`, `story-nights.md`). Of everything in it, the story night has no precedent in its genre (`audience-and-genre.md`, What Resident Evil Online Has That Its Genre Does Not).
- **What the extras are for.** The familiar modes make a successful Survivor last longer and reach further. They are kept as future development, built only if the service can pay for them without taking anything from Survivor (`future-development.md`). The order the record supports, and why Survivor stays first, is in `launch-alternatives.md`.
- **What the lore makes of it.** In the Night, every other mode is an old exercise ΜΝΗΜΗ inherited from the records. Survivor is the one she made herself (`future-development.md`, The Inheritance). The mode the franchise has never had is the one the story says is new to her too.

## The Experience

The measure of a night in Resident Evil Online is a single thought, repeated by every survivor who ever walks out of one:

> *"That has never happened to me before."*

It does not come from randomness alone. It comes from the collision of systems, survivors, ΜΝΗΜΗ, events, and the map: from choices that mattered and consequences that arrived on time.

And beneath every night, the thought no survivor is ever allowed to have: that it has happened before, to someone, perhaps to them, and she remembers exactly how it went.

## Documents

| Part | Document | Subject |
|---|---|---|
| `00-overview` | `start-here.md` | The way in: one night, what makes it Resident Evil, why it is not just another extraction shooter, and where to read next |
| `00-overview` | `project-overview.md` | Title, register rules, terminology, premise, and the measure of a night |
| `00-overview` | `narrative-illustrations.md` | The Prologue and A Night, Illustrated: dramatizations of the rules |
| `00-overview` | `a-night-played.md` | One whole Survivor night, played by one player from the Waiting Dark to the After-Action Report |
| `00-overview` | `launch-scope.md` | What the launch holds, what arrives later and when, and the scope rule |
| `01-lore` | `lineage-and-elpis.md` | The viral lineage from 1966 to 2026, and Spencer's cure |
| `01-lore` | `pithos.md` | The organization that built ΜΝΗΜΗ: origin, rules, Chain, its shape (one body, many rooms, who knows what), Archive, Cellar, Lid, Pyxis, and what it wants |
| `01-lore` | `mnemosyne.md` | ΜΝΗΜΗ herself: names, make-up, the Growth, the anomalies, purpose, a night's time and the world's time, personality, voice, breaks |
| `01-lore` | `sleepers-and-the-remembered.md` | Who the survivors really are, the Waiting Dark, what the body keeps, the Last Night, the Remembered |
| `01-lore` | `echoes.md` | The Echoes: what they are, what ΜΝΗΜΗ keeps, offline play, queue fill |
| `02-core-systems` | `session-and-blueprint.md` | The session, Survivor at a glance, waking points, scale, the shape of a Survivor night, the blueprint |
| `02-core-systems` | `director.md` | ΜΝΗΜΗ as director: voices, Laws, the Pulse, stillness, planning, leavers, her bodies, visions |
| `02-core-systems` | `infection.md` | The Mark, transmission, strain map, anomalous strains, stages, clock, antivirals, Down, Resonance |
| `02-core-systems` | `elpis-and-the-road.md` | Elpis in a session: the road, the paced Reserve, the Last Trial, the drop, one dose a night, the scar |
| `02-core-systems` | `strains.md` | The six viruses, Petitions, pure strains, the Embrace |
| `02-core-systems` | `exclusions-and-the-plaga.md` | What ΜΝΗΜΗ leaves out of her world, the Plaga of the Valley, and its pesetas and Merchant |
| `02-core-systems` | `the-turned.md` | The Turn, the four shapes, who plays on, Hunts, the Second Night, the Lost |
| `02-core-systems` | `extraction.md` | The verdict, the ways out of each map, the signal, boarding, the Climb, departure |
| `02-core-systems` | `the-dead-and-engineered.md` | Sound tiers, threat levels, the dead, containment, B.O.W. events, anomalies |
| `02-core-systems` | `survival.md` | Health, hunger and thirst, Self-Examination and tending wounds, inventory, worn gear, stashes, scarcity, crafting, safe rooms, vehicles, fighting and fleeing |
| `02-core-systems` | `destruction.md` | What breaks and who breaks it, what breaking changes, the Heavy indoors, breaches, collapses |
| `02-core-systems` | `objectives-restrictions-events.md` | Objectives, restrictions, puzzles, vaults, secret weapons, events |
| `02-core-systems` | `the-living.md` | Cooperation, voice, reading the Mark, the Mark within a squad, the clean, betrayal |
| `02-core-systems` | `dilemmas.md` | Where the rules make survivors choose between each other: the carried dose, the fresh hand, the end of the road, the beacon, the door, worked examples |
| `02-core-systems` | `survivors.md` | Who is played, survivor creation, tone, progression, Hardening |
| `02-core-systems` | `after-action-report.md` | The After-Action Report and its variants |
| `03-worlds` | `worlds.md` | The open worlds, the edge of each world and the Crossing, one world for every mode and the bounds each mode plays, time and weather, conditions |
| `04-survivor-mode` | `survivor-mode.md` | Survivor: squads made in the night, the Squad Sign, parties, companions, the Stranded, ties, eyes and ears, winning |
| `05-story-nights` | `story-nights.md` | Faithful to the records, as recorded, story nights, live scenes, Moments, Late Wakings |
| `05-story-nights` | `cast-raccoon-city-1998.md` | Acts, beats, named creatures, the Last Morning, people, roster, and ties of Raccoon City, 1998 |
| `05-story-nights` | `cast-valley-2004.md` | Acts, beats, named hosts, people, the Island's End, roster, and ties of the Valley, 2004 |
| `05-story-nights` | `cast-ruins-2026.md` | The people, named creatures, roster, and ties of the Ruins, 2026 |
| `06-service` | `presentation-and-technology.md` | Camera, engine and the look, the rebuilt city, servers, matchmaking, voice, music, and how each system is built in practice |
| `06-service` | `the-service-and-promises.md` | The First Run, the Opening, the Promises, Conduct, and the record they answer |
| `06-service` | `economy.md` | Ink Ribbons, earning, Exposure, prices, Release Weekends, Patron, the Wardrobe |
| `06-service` | `cosmetics-and-dossier.md` | Cosmetic rules, each thing to its time, Looks for each world, what can be owned, gear in Survivor, the Dossier, the diorama |
| `06-service` | `seasons-and-new-content.md` | Seasons, Casefiles, events, Crosstime Weekends, the order of arrival, early access |
| `06-service` | `offline-and-ownership.md` | Offline play, ownership, and what happens if the service ends |
| `07-feasibility` | `business-case.md` | Costs, revenue, cases, break-even, sensitivity, population, verdict |
| `07-feasibility` | `director-architecture.md` | How ΜΝΗΜΗ would be built: layers, perception, the Pulse, the planner, the Law validator, roads and the Reserve, the announcer, the Echoes, the dead at scale, tools, cost and risk |
| `07-feasibility` | `legal-feasibility.md` | Whether the design can ship legally in the US, EU, UK, Brazil, and Japan; the risks, the changes made, and what the fan-made project may do |
| `07-feasibility` | `market-precedents.md` | The games most like Resident Evil Online that succeeded or failed, the context of each, and what it needs to do to join the successes |
| `07-feasibility` | `audience-and-genre.md` | What the Resident Evil community wants and refuses online, what the game has that its genre does not, whether it is a new genre, whom it can draw, and the future modes against the record |
| `07-feasibility` | `launch-alternatives.md` | A hub of Outbreak, Mercenaries, and Versus at launch with Survivor later, against Survivor first: cost, break-even, gains, losses, and Survivor with Outbreak as a third order |
| `08-future-development` | `future-development.md` | The modes kept for possible future development, and how each would touch the rest of the game |
| `08-future-development` | `outbreak.md` | Outbreak: the eight, the scenarios, the virus, the escape, difficulty |
| `08-future-development` | `versus.md` | Versus: characters, setups, the dead, formats |
| `08-future-development` | `mercenaries.md` | Mercenaries: score, time, ranks, formats |
| `08-future-development` | `recollections-and-endless.md` | The Recollections frames and Endless |
| `08-future-development` | `the-refuge.md` | The Refuge: a room of the player's own, built from their dioramas, in place of the menus, with guests and an arcade. A future feature, not a priority |
| `09-sealed-file` | `the-sealed-file.md` | The answers to every question the other documents leave open: the Growth, the anomalies, ARK, the Connections, the Family, Spencer and Alyssa, and the order in which the seasons reveal them |

---

# RESIDENT EVIL ONLINE

## WAKE. SURVIVE. BE REMEMBERED.

### ΜΝΗΜΗ remembers.

*Created by Johnny Kestler, with Claude (Anthropic). Generative AI was used in the creation and editing of these documents.*
