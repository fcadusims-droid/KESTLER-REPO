---
section: "06 · The Service"
description: "Camera, engine and the look, the rebuilt city, servers, matchmaking, voice, music, and how each system is built in practice"
order: 29
---

# Presentation and Technology

## Third Person, Everywhere

Survivor is played in third person, from over the shoulder. The camera can swap shoulders, draws in when the survivor aims, and pulls close in tight spaces. There is no first-person mode.

Third person is the choice because the body is the clock. A survivor's tremor, their limp, the hand pressed to their ribs, the way they stand at Fracture: all of it is information Resident Evil Online refuses to put on a screen as a number, so the player has to be able to see their own survivor.

Outside a Moment (`story-nights.md`), the camera never swings in front of the survivor.

## The Camera Sees Only What the Survivor Sees

A third-person camera floats above and behind the body, and in a game built on hiding it would let a player look around a corner without exposing their survivor. Resident Evil Online closes that door. Other survivors, the Turned, the dead, and anything lying on the ground are drawn only when the survivor's own eyes could see them. The camera may show the street beyond the wall. It never shows who is standing in it.

The server decides what each survivor can see and sends nothing else. A player who breaks the client finds nothing in it to reveal.

One more limit applies to a survivor's own Mark, for the player who carries it: it is drawn only where the survivor's own eyes could see it, on their hands, or on an arm or a leg they bare and look down at, and anywhere else only in a reflection, a window, a puddle, a mirror, a blade, as `infection.md` describes. Everyone else sees it wherever it is on bare skin and in sight. The server sends no client the state of any Mark it cannot see: a Mark under cloth is not hidden on the screen, it is absent from the data, so a broken client finds nothing. Nothing in the squad's interface, its portraits, or its sounds changes when a member is infected.

## Engine and Platforms

Resident Evil Online is built for PlayStation 5, Xbox Series X|S, and PC on Capcom's RE Engine, or on the engine that succeeds it. Capcom has said it will not replace the RE Engine but evolve it step by step into REX, the RE neXt Engine, so a game begun on one moves with it to the other. Every platform plays with every other, and an account is the same account everywhere: everything a player has earned, bought, or unlocked follows them to every platform they sign in on.

### The Look

The game looks like the Resident Evil of its day: realistic, as the remakes of *Resident Evil 2*, *3*, and *4* and *Resident Evil Requiem* look, never stylized. Materials behave as they would in the world, wet, rusted, bloodied, or burned; faces and bodies are built from scans of real people, as the series builds them; the dark is dark. Because every map runs at every hour and in every weather (`worlds.md`, Time and Weather), no city can have its light baked once: it is lit as it is played, and everything in it is lit by the same sky.

### Raccoon City, Rebuilt Whole

The game does not stitch together what the remakes left behind. It builds the Raccoon City of September 1998 whole, every region `worlds.md` names, as one new remake of the city at the fidelity of the series' latest games, and it uses what the remakes already made wherever the city holds it:

| What is reused | Where it comes from |
|---|---|
| The R.P.D., the streets around it, the sewers, and NEST | *Resident Evil 2* (2019) |
| Downtown's streets, the subway, the substation, the hospital, and the plaza of the Clock Tower | *Resident Evil 3* (2020) |
| The people and creatures of 1998, their animation, and the weapons they carried | Both remakes |
| The ruined city of 2026 and ARK | *Resident Evil Requiem* (2026), for the Ruins |
| The village, the castle, the island, and their people and creatures | *Resident Evil 4* (2023), for the Valley |

Everything reused is rebuilt to the city's scale, relit for its hours and weather, and opened up for a crowd: a corridor made for one survivor and one Tyrant is widened where a hundred survivors have to pass. What no remake built is built new: the university, Raccoon Park, its cemetery and zoo, Uptown and the Apple Inn, the Industrial Edge, the Western Barricade, and the streets that join them. The reuse is still the largest single saving in the game's budget, but it is a saving on a whole city, not a city made of saved pieces (`business-case.md`).

**One world, many bounds, in practice.** Each world is built once and divided into streaming cells. A bound is data: the list of cells it opens, the seals placed at its edges, its entry points, and the mode's own placements (`worlds.md`, One World, Every Mode). A night loads only its bound's cells, so a compact mode loads faster and needs a smaller server than Survivor, with nothing rebuilt for it. Every bound is checked by an automated pass that walks every path out of it and fails the bound if any route passes a seal, a collapse, or a gap in the geometry. Seals are a shared library of set dressing, made once. A change to the world, a fixed door or a corrected room, reaches every mode at once.

Building the whole city also builds most of the next one. The Ruins of 2026 are the same streets twenty-eight years later, so the Ruins are made from the 1998 city, broken, burned, and walled, with what *Requiem* already made of them (`seasons-and-new-content.md`, The Order of Arrival).

## Servers

Every online session runs on a dedicated server, and ΜΝΗΜΗ runs on it. The server, never the player's machine, decides what was hit, what was found, where the dead are, and how far each virus has gone. A Survivor night of a hundred survivors and the thousands of dead around them runs on one server: the dead near survivors are simulated in full, and the dead far from anyone are run more coarsely, under the same rules.

## Matchmaking

Survivor matches by region, by kind of night, Solo or Squad (`survivor-mode.md`), and, once the Ruins of 2026 arrive, by the player's choice in the lobby between the classic rotation and the Ruins (`worlds.md`). The game opens with three regions. Players who are friends, who were in a party together in the last hour, or who play from the same network are never put in the same Solo night. A night waits up to two minutes for players alone. After that, ΜΝΗΜΗ completes it with Echoes, up to a quarter of its survivors and never inside a player's squad (`echoes.md`). No night starts with fewer than forty survivors in all, or sixty-four in the Valley. When a queue stays short even then, neighboring regions merge. While a night is assembled, its lobby shows a card for every player who will wake in it, with their doorstep standing and never their survivor's look (`cosmetics-and-dossier.md`, Where It Is Seen). The choice between the classic rotation and the Ruins is a preference, never a wall: a player can tick both, and a player who chose one and has waited four minutes is offered the other's next night. A choice that cannot be filled fairly is not worth an empty queue (`business-case.md`, Population).

## Echoes, in Practice

Echoes are not trained minds. Each is a conventional game AI: a set of behaviors and priorities for waking, scavenging, fleeing, trusting, and betraying, tuned to one Way from what the telemetry of real nights shows that Way doing. Rebuilding the Echoes means retuning those priorities as the telemetry changes, once a season. This keeps the system inside a game budget and makes every Echo testable: a Bargainer that breaks its word more often than its Way's players did is a bug, and can be fixed.

Companions and the Stranded run on the same kind of AI. Each unnamed Stranded speaks from a short set of lines written for their background and their moment; each named one speaks lines written for them. A Stranded's replies are chosen from a fixed list (`survivor-mode.md`), so no line is ever generated during a night. In the story nights, each person of the records also carries a thread: an ordered list of places and a goal, followed with the same AI. Each beat is a scripted scene with conditions, and it runs in the world only when they hold.

## As Recorded, in Practice

Every person and named creature with a first account ships two bodies. The as-recorded body is built from the original game's own model and textures: the PlayStation for *Resident Evil 2* and *3*, the PlayStation 2 for *Outbreak*, the GameCube for *Resident Evil 4*. It is rigged to the modern skeleton, fitted to the modern body's proportions for people, and plays the modern animations. Its textures are shown unfiltered, as the originals were, and the RE Engine lights it like everything else. Collision, hit areas, the Mark, and every weak point come from the night, never from the old model. The work is rigging, fitting, and tuning on art Capcom already owns, not new art.

The classic looks are a display setting in the Extras menu: **Classic looks: On** (the default) or **Rebuilt only**. The setting changes only what that player's own screen draws. It is free, it is never sold, it works offline, and it never changes what any person or creature does.

## Live Scenes, in Practice

A live scene runs on the server as a timeline that drives its actors. Each client receives a scene only while its survivor is in range, as it receives any other sound or sight, and a survivor who arrives late joins the timeline where it stands. Lines are written as many short pieces, and the server chooses each one by rules matched against who is on the stage, the way Valve's dynamic dialogue chose lines for the survivors of *Left 4 Dead*. Actors turn their heads, eyes, and hands toward whichever survivors they address. Every scene is performed once for each way it can end and once for each way it can break, so the number of branches is the main cost of the story nights, and it is budgeted scene by scene (`business-case.md`). The Reel stores each night's scenes as the server's own record, with no video, and is drawn again when a player opens it.

## Sleepers and the Remembered, in Practice

The fiction and the technology are the same thing, told twice.

| In the Night | In the Service |
|---|---|
| A body built in the creator from the Remembered | The character creator's options |
| A living sleeper's mind set inside that body, run through a night | A player, online |
| ΜΝΗΜΗ learning a sleeper | The game recording what players do, the telemetry the bots are tuned from |
| A sleeper finished, their body burned, their mind Remembered | A player's own Echo passing its one test: agreeing with the player on nine choices in ten across their last twenty nights (`echoes.md`, Your Own Echo) |
| Enough sleepers finished who played a piece of Survivor | That piece opening offline (`offline-and-ownership.md`) |
| An Echo | A bot |
| The Ways the Remembered are sorted into | The behavior profiles a bot is tuned to (Echoes, in Practice) |
| A file given to a new sleeper | Nothing: the player goes on playing, and the account is unchanged |
| Only ΜΝΗΜΗ remembers | Every night starts from nothing; the player and the account keep everything |

None of it changes how a session plays. It is the fiction's face of what every session already does: start everyone from nothing, and learn from what they do. It changes how a night is written and how a survivor is made. Everything said to a survivor, by ΜΝΗΜΗ, by companions, and by the Stranded, is written for someone who knows nothing, every night. The player is never treated that way: no tutorial or explanation repeats once a player has seen it, and everything an account has earned stays with it. In the creator, every hair, face, eye, voice, and build carries a small file number instead of a name, the same kind of number a player's Dossier carries. ΜΝΗΜΗ's introduction in the earpiece is written in many versions and is never the same twice in a row, because she is introducing herself to a stranger who has met her a thousand times, and the player should hear that she knows it.

## Late Nights, in Practice

The seed is run on the server at Assembly, the way the server runs the distant dead: coarsely, a beat at a time, each resolved from what its people want, carry, and face, by the rules a live night would apply. It takes seconds, and its result is a state of the world: who lives and where, what is open, what lies where. Each beat is written with its possible outcomes, as a live scene is written with its breaks, and each outcome comes with its set dressing: bodies, damage, notes. Only the outcomes and the encounters are built, never the scenes, so a Late Night needs no branches performed for whoever arrives and no threads walked among the survivors. That is why it costs less than a story night.

## The Director, in Practice

ΜΝΗΜΗ's planning is a director system of a kind games already use, built larger. Valve's *Left 4 Dead* (2008) ran an AI director that read how hard its players were being pressed and paced the dead around them. ΜΝΗΜΗ does the same for a whole night and a hundred survivors. On the server, a planner runs the session forward at a coarse level, the way the distant dead are run (Servers, above), and scores the outcomes it sees against her goals: no empty stretches, no repeated nights for a file, no easy farm, no camped door. It then picks actions from her fixed set of tools, each checked against the Laws before it is allowed. The patterns it forecasts from are the telemetry of real nights, the same data the Echoes are tuned from, retuned each season. Her planner uses a file's history only to keep its nights from repeating, never to decide how hard its night will be or what falls on it; the Second Law is a rule in the code, not only in the fiction.

The planner also learns from players leaving early (`director.md`, When They Leave). Every early exit is logged with its minute, map, region, and the survivor's recent state, and classified automatically by what preceded it. A pattern changes the director's pacing only after it repeats across thousands of nights, and each change ships as a tuning of the director's own parameters, run against a share of nights first and kept only if that kind of exit falls. The planner's tuning can never touch the rules of a mode, the Reserve, the seats, drop odds, item placement value, Ribbons, or anything sold, and nothing about one player's exits ever changes that player's own nights. When exits cluster by the clock rather than by place, the director flags it, and the length of a night becomes a decision for the people who run the Service, not for the planner. Leaving a match is never penalized beyond what `the-turned.md` describes.

## Moments, in Practice

ΜΝΗΜΗ's safe window is computed on the server on every tick, from what the server already knows: positions, speeds, sightlines, weapons in hand, and the paths of the dead. It is measured with a margin for network delay. A Moment is a camera and animation layer drawn by the client over the one timeline the server runs, with a cut point about every second, so it can end the instant the window closes. Each Moment is made in several lengths. Grand Moments are made one by one, for each named creature and each beat; Brief Moments are made once for each kind of creature and reused wherever it is met, which keeps the commonest Moments the cheapest. Moments are the place where ΜΝΗΜΗ's knowledge of the whole night becomes a feature: no other director could cut to cinema in a crowd and promise it costs no one their life.

## ΜΝΗΜΗ's Voice, in Practice

ΜΝΗΜΗ's two voices are performed by an actress and an actor and built into synthetic voices with their consent and their pay, so that they can say what the nights need. Each client plays every line of hers in the voice set by its own player's survivor. Her baseline is kept clean: no processing that sounds like a machine. The fear in it is built from mismatch, which research on uncanny voices finds more unsettling than a robotic sound: wrong timing, missing breath, exact repetition, and a stranger's accent for one word. Her breaks use what makes screams alarming, a fast roughness in the sound and noisy, broken pitch, and only during a break, so the contrast lands. No mechanic depends on infrasound. Every break stays under the game's loudness limits, and its subtitles always show the true words.

Her remarks, her visits, and her breaks of the glass draw only on data the game already keeps. None of them imitates any platform's own system screens. They happen inside the game's own layers, the Waiting Dark, the Ledger, and the Dossier, where they can pass every platform's certification. A player can set her remarks to **Quiet** in the Extras menu. She then keeps her announcements and the earpiece's introduction, and drops her personal remarks and every break of the glass.

## Her Bodies and Visions, in Practice

Her own body is one entity on the server, with one position, one collision volume, and one set of hit areas. Each client draws its form for its own player, chosen from the body type of that player's survivor. A vision is a phantom: the server simulates it for one client only and sends it through the same stream as every real creature, with nothing that marks it as unreal. A modified client cannot sort visions from the real dead by reading a flag. The phantom has no collision with the world, can cause no damage, and is removed the moment its rules say it ends.

## Weight, in Practice

Every body in Survivor moves with its mass, and the Heavy most of all (`survival.md`, Run First). A Tyrant is felt before it is seen.

- **Every step lands.** A Heavy's footsteps are a Clamor, running a Thunder. Near one, the floor carries them: the camera trembles with each step, dust falls from ceilings, glass and loose things rattle, puddles shiver.
- **It has momentum.** It accelerates slowly, turns wide, and commits to a charge. A survivor who steps aside at the last moment makes it overrun and crash into whatever is behind them, and a group learns to use that.
- **It does not flinch for small things.** Its reactions are driven by physics, scaled by its mass: a handgun round moves it no more than a push moves a wall, a shotgun at close range rocks it, an explosion knocks it down. It never plays a hit reaction its mass would not allow.
- **What it hits moves.** A blow throws a survivor meters, into walls and over cars, and the body tumbles as a body would before it lands Down. Doors leave their hinges, cars rock and slide when it shoulders them, barricades come apart in pieces.
- **The lesser dead too.** A zombie's grab drags with its weight, a body falls with its momentum, and a Licker's leap carries it past a survivor who ducks. Nothing in Survivor moves like a weightless model.

The reactions run on the server for everything that decides a fight, and on each client for everything that only shows it: the dust, the rattle, the tremble of the camera.

## Dioramas, in Practice

A diorama is stored as a list of pieces, models, poses, and lights, not as an image, so it is small to keep and is built on the viewer's machine from assets the game already ships (`cosmetics-and-dossier.md`, The Diorama). Its limits, one room, three hundred pieces, twelve models, are what a console renders smoothly at the quality of the rest of the game. Dioramas are never loaded inside a night. Building one is done in the Waiting Dark, with the same camera tools as the Portrait.

## Hardening, in Practice

Hardening is drawn, not displayed (`survivors.md`, Hardening). Every survivor's running, startle, panting, and struggle are captured twice, from performers moving as people who have never trained and as people who have lived through this, and every stage between them is a blend of the two. The numbers of each stage live on the server with the rest of a survivor's state, and the server sends other clients only the body's motion, never the stage.

## Safe Rooms, in Practice

Safe rooms are how an online night lets a player step away: to answer the door, to take a call, to go to the bathroom. Five minutes a night is enough for that and too little to hide in (`survival.md`, Safe Rooms). The server tracks each survivor's remaining time, holds their virus clock while they are inside, and disables weapon use inside the room for everyone it still holds. A player who walks away from the controller outside a safe room gets no protection: the night goes on without them.

The Wardens are server entities with no hit areas a survivor's weapon can reach. The server decides every offence on a doorstep from what it already knows, who harmed whom and where both stood, so a Warden's response never depends on a client. A survivor in a holding cell is moved out of play for the length of the hold and keeps playing the moment the cell opens.

## Anomalies, in Practice

An anomaly is generated, not authored one by one. Each is assembled on the server from a library of body parts, ways of moving, senses, and behaviors, chosen and weighted by trait values: how it spreads, its pace, how it hunts, how it heals, what it resists, and what it does to a host. Every trait has tested limits, so that no combination can produce something that cannot be seen coming, heard, hit, or put down, or a strain faster than the clock allows (`infection.md`, Anomalous Strains). Each anomaly is stored as a lineage, and when it returns, the server changes a few of its traits within those limits. Anomalies are post-launch work: they need the library, the limits, and a great deal of testing before they reach a night (`seasons-and-new-content.md`, The Order of Arrival).

## Sound

Sound is the main channel of information in Survivor, so the audio is built first and drawn second. Every sound is positioned in three dimensions, carried through walls, doors, and floors, muffled by rain, and doubled in the Frenzy, exactly by the tiers of `the-dead-and-engineered.md`. Proximity voice travels the same way, through the same walls, at the same distances (Voice, in Practice, below). Inside a night, voice is the only way survivors speak to each other: there is no text chat in a night, because a typed word would be a radio no one else could hear. Text chat lives in the Waiting Dark, for squads, friends, and the night's lobby (`the-service-and-promises.md`, Conduct).

## Voice, in Practice

A player's voice comes out of their survivor's mouth. It is placed at the survivor's head, moves the survivor's lips, and reaches every listener the way any sound in that place would.

- **The microphone does not set the reach.** Every voice is brought to the same loudness before it enters the world, so a player who turns their microphone to the maximum is heard no farther than one who does not. How far a voice carries is set by how it was spoken: the server reads each phrase as a whisper, ordinary speech, or a shout, from the voice itself, and gives it its tier: Hush, Murmur, or Clamor (`the-living.md`, Speaking and Silence). A shout sounds like a shout because its pitch rises, it stretches, and its brightness changes, all of which survive any microphone level. A player who whispers into a loud microphone is still whispering.
- **Each player teaches it once.** In the Waiting Dark, before their first night, a player speaks three short lines: in a whisper, in their ordinary voice, and in a shout. That sets the reading for their own voice, and they can repeat it at any time.
- **The place carries it.** A voice is propagated by the same acoustic system as every other sound: blocked and muffled by walls, doors, and floors, bent around corners, rung by tile, thrown back by an alley or a stairwell, swallowed by open streets and rain. A survivor walking past the mouth of an alley where someone is shouting hears a man shouting in that alley: from that direction, at that distance, with that alley's echo. An echo carries a voice farther than its tier, to the living and the dead alike (`the-living.md`, Speaking and Silence).
- **A shout has a ceiling.** No voice arrives louder than a human shout at that distance would. Clipping, feedback, and noise are removed before a voice enters the world, so no player can use a microphone to hurt another player's ears. A player who screams to bring the dead down on others is a matter for Conduct (`the-service-and-promises.md`).
- **Built from what exists.** Proximity voice with occlusion and environmental effects already runs in shipped online games, through voice middleware connected to the game's audio engine. Reading a whisper or a shout from the voice is an established problem in speech science, solved here by a small classifier on each phrase. Making the two work together inside Resident Evil Online's own acoustic system is engineering, not research, and it is tested at the first gate (`business-case.md`, Capcom's Decision).

## Music

Resident Evil Online is scored by its world. For most of a night there is no music at all: the sound of the place is the soundtrack, wind, rain, a door banging somewhere, a siren far off, the dead. Music is held back for a few moments, so that when it plays it means something.

| When music plays | Where it begins | Where it ends |
|---|---|---|
| **A safe room** | When the survivor steps inside a room that still holds them | When they step out, or their time there runs out |
| **A named creature, an Apex, or a B.O.W. event** | When the survivor first sees or hears it | When it is down or gone, or the survivor has been out of its reach for a while |
| **The end of a night** | In Raccoon City, 1998, at the five-minute call before the missile (`cast-raccoon-city-1998.md`, The Last Morning). On every map, during a Last Call the survivor can hear, and in a Climb they are part of (`extraction.md`) | When the way out leaves, or the night ends |
| **A Moment** | When a Moment begins (`story-nights.md`) | When it ends |

- **Music never knows more than the survivor.** Each player hears music only for what their own survivor is living. It never starts before its cause can be seen or heard, so it never warns of anything (`director.md`, First Law). Silence is never a promise that nothing is there.
- **Music never covers the world.** It is mixed beneath voices, footsteps, and every sound the tiers of `the-dead-and-engineered.md` carry information in. No cue is ever loud enough to hide a step.
- **The Ruins are quieter still.** In the Ruins of 2026 there is no music for creatures, and the safe rooms are silent. Only the end of a night and Moments are scored there (`worlds.md`).
- **Outside a night, music is free.** The Waiting Dark, the Wardrobe, and the After-Action Report have music of their own.
- **In the Night,** the music is ΜΝΗΜΗ's. She runs everything a sleeper hears, and she learned from the records how the people who lived these nights remember them: as silence, broken by a few moments that played in their heads like music. She gives a sleeper those moments and no others.

## Readable by Everyone

- **The Mark is shape as well as color.** Each strain draws its lines in its own pattern: straight and thin for the T-Virus, knotted with nodes for the G-Virus, thick and swollen for the C-Virus, moving under the skin for Uroboros, branching like frost for T-Veronica, darkening in pulses for T-Phobos. Color-blind settings strengthen the pattern; they never add an icon.
- **The strobes are rhythm as well as color.** Elpis pulses slowly. A pure strain pulses fast. The parasite falls dark.
- **Every voice is subtitled,** ΜΝΗΜΗ's public and private voices included.

## Playing Without a Connection

Everything ΜΝΗΜΗ needs to run an offline session, and every Echo she will put in it, ships with the game and updates with it. `offline-and-ownership.md` sets out what offline play keeps and what it does not.
