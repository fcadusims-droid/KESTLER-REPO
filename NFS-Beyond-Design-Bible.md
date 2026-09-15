# NEED FOR SPEED: BEYOND
## Design Bible — v2.3

---

## 1. Premise

**Need for Speed: Beyond** is an open-world racing game built around two halves of the same car culture: the illegal street scene of a single large city, and a months-long sanctioned racing festival held on closed circuits outside it.

The city is the core experience and occupies Acts 1 through 5. The festival is the epilogue — unlocked only after the main story concludes — and functions as a second, parallel career.

Both halves run on a single simcade driving model. The game does not switch physics when the player crosses from street to circuit.

**Beyond is a single-player game.** There is no competitive multiplayer, no lobbies, no racing against other players in real time. Its online component is entirely asynchronous: players never meet, and they contribute to each other's games by leaving behind the one thing this game is actually about — cars they built. See Section 17.

The title refers to the protagonist's arc: he conquers everything inside the world he built for himself, and then has to go past it.

---

## 2. Thematic Core

### 2.1 The Father

The protagonist's father was a professional GT3 driver.

GT3 is a category of competition car — race machinery built to a regulation, rear-wheel drive, equalised against rival makes by Balance of Performance, and campaigned by customer teams across national and international championships. His father spent his career in that world: contracts, sponsor liveries, endurance grids, a job rather than a fantasy.

**GT3 exists nowhere inside the playable world.** Not in the city, not in the festival. It is the tier above both — the level the protagonist's father worked at, the level the ending sends him to, and a level the player never drives at during the game. It appears in this document only in the father's history and in the final scene.

In his last season he reached the only stage GT3 offers that carries a world title: the GT3 class of the world endurance championship. He led the championship into the final round, and he led the final race.

**He died on the final lap of that race, holding first place, with the title already won on the road.**

He never took the flag. The championship was never awarded to him.

### 2.2 The Inversion

This is the load-bearing fact of the entire game, and it is deliberately ironic: the only death in this fiction happened in the *sanctioned, regulated, scrutineered, marshalled* environment — the one the protagonist's own reasoning tells him is the safer of the two.

The protagonist knows this intellectually. Emotionally he inverts it. After the funeral he never returns to a closed circuit. He goes to the streets instead, because on the street he believes he controls the variables: he knows the roads, he knows the racers, he knows when the police run patrols and when they don't. Control is the lie he tells himself; familiarity is what he actually has.

**What the avoidance actually covers.** Not laps, not corners, not racing in circles — the city has lap-based street events and he runs them without difficulty. What he avoids is the *apparatus*: a permanent circuit, grandstands, an organising body, scrutineering, official timing, marshal posts, a classification sheet with his name on it. His father died inside that apparatus, and it is the apparatus he will not walk into. This distinction is precise and load-bearing: a scene in which he races a multi-lap loop through The Heights at 3 a.m. is not a scene about his trauma, and a scene in which he stands outside a festival gate is.

The game never argues that street racing is morally lesser than sanctioned racing, or the reverse. It argues that the protagonist chose one over the other for a reason that has nothing to do with racing.

**The central transformation is not that he stops being a street racer. It is that he stops racing out of fear.**

### 2.3 The Shape of the Ending

For most of the game the protagonist cannot choose. One of the two doors is closed, and he is the one holding it shut.

The festival is him opening it. The championship is him walking through. What he does on the other side — a professional career, the exact path his father was on — is the first decision in his adult life that fear did not make for him.

The point is not that the circuit was the right answer and the street was the wrong one. The point is that a choice made out of terror was never a choice at all.

---

## 3. Structure

| Act | Title | Content |
|-----|-------|---------|
| **1** | The Unknown | Entry into the street scene. First district. Reputation from zero. |
| **2** | Ascent | Multiple districts contested. Crews, rivalries, police attention escalates. |
| **3** | King of the Streets | Final districts taken. The protagonist becomes the name the city uses for street racing. |
| **4** | The Hollow | Everything is won and nothing is resolved. Wealth, cars, respect, unchanged guilt. |
| **5** | The Choice | The festival — present in the world since Act 2 as advertising, television, conversation — stops being background and becomes a decision. |
| **Epilogue** | Beyond | The festival map unlocks. Second career begins at zero Rank. Ends with the championship and a professional contract. |

The city does not close at any point. After the epilogue unlocks, the player moves freely between city and festival for the remainder of the game.

---

## 4. Driving Model

A single simcade physics model governs every event type in both halves of the game.

**What is simulated with weight:**

- Mass distribution and its effect on rotation
- Weight transfer under braking, acceleration and lateral load
- Drivetrain layout (FWD / RWD / AWD) as a genuine behavioural difference
- Tyre grip as a function of compound, surface and load
- Aerodynamic downforce and drag, scaling with the square of velocity and becoming handling-relevant above roughly 140 km/h
- Power delivery curves, including turbo lag and supercharger linearity

**What is abstracted everywhere:**

- Fuel is not modelled anywhere in the game
- Mechanical failure from abuse never occurs mid-event
- Recovery from a spin is more forgiving than a simulator would allow

**What does not change between city and festival:** nothing in the physics model itself. A car that oversteers on a wet industrial road oversteers on a wet circuit. The player's accumulated driving skill transfers to the festival completely.

### 4.1 The Simulation Layer

**The handling model is identical in both halves. The simulation layer on top of it is not.**

The city is arcade. The festival is simulated. This is not a physics change — it is a change in how much of the car's condition the game tracks while the player is driving it.

| | City | Festival |
|---|---|---|
| **Handling model** | Identical | Identical |
| **Tyre wear** | Not simulated | Simulated. Compound and driving style determine how long grip lasts. |
| **Tyre temperature** | Not simulated | Simulated. Cold tyres are slower; overheated tyres lose grip. |
| **Brake fade** | Not simulated | Simulated over long events |
| **Damage during an event** | Visual only. No performance effect. | Aerodynamic, mechanical and alignment damage degrade the car in real time. |
| **Damage after an event** | Persists. Costs money to repair. | Persists. Repaired by the discipline's mechanic (Section 12.4.5). |
| **Restarts** | Freely available | Not available inside a session |
| **Setup depth** | Simplified presets plus manual tuning | Full setup: dampers, ride height, camber, toe, gearing, differential, brake bias, pressures |
| **Regulation** | None (Section 5.4) | Scrutineered before and after (Section 13.2) |

**Why it is split this way.** The city is where the protagonist is comfortable, and the game lets the player be comfortable there. Street racing in *Beyond* is immediate: get in, drive, win, leave. Nothing is being measured except whether you were first.

The festival measures everything. It measures tyre temperature, it measures contact, it measures whether the car was legal, and it measures it in public. **The step up in simulation is the same step up the protagonist is taking**, and the player feels it in the controller the first time they put a lap in on cold tyres and wonder why the car will not turn.

Neither layer is the "real" one. The city is not a tutorial for the festival and the festival is not the game's true form. They are two different relationships with the same car.

---

## 5. The City

### 5.1 Districts and Crews

The city is divided into **seven districts**. Each is controlled by a crew, and each crew is a complete competitive identity: its own discipline, its own machinery, its own entry rules, and its own reason for existing.

A district is not a region of the map with races in it. It is a filter. What the player is allowed to bring into a district determines what they have to build to win there, and no two districts ask for the same car.

---

**DOCKLINE — The Docks**
*Container yards, half-mile straights, poor lighting, standing water.*

- **Discipline:** Drag, and nothing else.
- **Events:** Quarter-mile, half-mile, roll racing from 100 km/h, standing-start launch challenges.
- **Entry rules:** Rear-wheel drive only. No aero of any kind. Classes B through S.
- **Philosophy:** Power and launch. Nothing in a Dockline build is there to help it turn. They regard cornering as an admission that you did not build enough engine.

---

**THE OLD GUARD — Old Quarter**
*Narrow street grid, tight corners, heavy civilian traffic, stone kerbs.*

- **Discipline:** Grip. Multi-lap circuit racing on public streets.
- **Events:** Multi-lap street circuits, timed single laps, sector runs.
- **Entry rules:** Classes C and B only, capped. Naturally aspirated engines only. No nitrous.
- **Philosophy:** The oldest crew in the city and the most conservative. They believe forced induction and nitrous are ways of buying what a driver should earn. Their restrictions exist to strip everything out of the equation except the driver, and their events are the hardest in the city to win on raw speed.

---

**RIDGE UNION — Ridgeline**
*Mountain road, sustained elevation change, blind crests, no barriers.*

- **Discipline:** Drift, downhill and uphill.
- **Events:** Solo scored runs, tandem battles, downhill time runs, uphill sprints.
- **Entry rules:** Rear-wheel drive only — front and all-wheel drive are refused at the gate. Classes B and A. Aero permitted but unfashionable.
- **Philosophy:** Style is the score. A Ridge Union run that is fast but flat scores below a slower run held at angle. They are the only crew in the city that judges rather than times.

---

**RINGRUNNERS — Expressway Ring**
*Elevated multi-lane loop encircling the city. Continuous, no exits, no stopping.*

- **Discipline:** Top speed.
- **Events:** Speed traps, sustained average-speed runs, full-loop time attacks, rolling standoffs at licence-losing velocity.
- **Entry rules:** Classes A and S. Minimum top-speed threshold verified before entry — slow cars are simply not eligible. Aero mandatory above a defined power figure.
- **Philosophy:** Nerve over craft. Ringrunner events run at velocities where a lane change is a commitment and a truck in the wrong lane ends the run outright. They attract the most police attention in the city and do not care.

---

**THE YARD — Industrial Flats**
*Warehouse district, open lots, abandoned infrastructure, endless usable space.*

- **Discipline:** All of them.
- **Events:** Everything the other six crews run, plus the largest night meets in the city.
- **Entry rules:** None. Any class, any drivetrain, any build, any car.
- **Philosophy:** The Yard is the city's common ground and the only district where the other six crews mix. It is where a player finds out which discipline they are actually good at, and where every rivalry in the city eventually gets settled in front of an audience.

---

**RIVERSIDE — Riverside**
*Residential, mid-speed, unpredictable civilian traffic, well-lit boulevards.*

- **Discipline:** Build quality, expressed through racing.
- **Events:** Cruise runs judged on presentation, short sprints where entry is conditional on the car passing judgement, coordinated multi-car runs.
- **Entry rules:** No class restriction whatsoever. Instead, the car must pass a **build coherence check** — the game reads the car's Presentation rating (Section 10.4) alongside whether the visual and performance work read as one intentional car rather than an accumulation of parts. A fast car assembled at random is refused; a modest car built with a clear idea is welcomed.
- **Philosophy:** Riverside is the only crew that does not care how fast the car is. It is also the only crew that will refuse the player's best car outright, which is exactly why it exists: it forces a player who has been optimising numbers to make something on purpose.

---

**MERIDIAN — The Heights**
*Millionaires' district. Gated streets, private estate roads, hillside switchbacks, underground garages beneath luxury towers.*

- **Discipline:** Street racing, on the most expensive machinery in the city.
- **Events:** Night runs on estate roads, hill sprints through the gated streets, tunnel and garage circuits under the towers, head-to-head challenges for sums nobody else in the city can cover.
- **Entry rules:** **Classes S and X only.** Road-going supercars and hypercars. The entrant must own the car — no borrowed entries, no detuned cars, no exceptions. Ownership is verified before the gate opens.
- **Philosophy:** Meridian is a private club inside a rich neighbourhood, and its members are wealthy people who race because they can. Membership is the car. There is no application, no reputation requirement beyond being let in, and no way to buy your way past the class rule except by owning a supercar.

**Meridian is illegal like everything else in the city.** Nothing about it is sanctioned. There are no marshals, no scrutineers, no timing officials and no rulebook — only a gate, a class restriction, and enough private money that the police in The Heights are slower to arrive and less interested when they do. It is the least *policed* district in the city, and the one with the most expensive consequences for being caught.

It is also the last district in the campaign, and the hardest wall in the city: the only way in is to own a hypercar, and hypercars are the most expensive thing the game sells. Taking The Heights is the point where street winnings stop being spending money and become capital.

Meridian's machinery is road machinery — Bugatti, Koenigsegg, Pagani and their peers. Hypercars built for the street and sold to people who can afford them (Section 10.1).

**Meridian supplies no drivers and no mechanics to a festival team.** Its members have no discipline in the festival's sense and no interest in working for anybody. What a Loyal Meridian contact offers instead is money: they will sponsor the protagonist's team and cover its salaries for a season (Section 12.4.4). It is the only district whose relationships convert into funding rather than personnel, and it is exactly what a district full of rich people would be worth.

### 5.2 Territorial Rule

**In the city, the crew that controls a district sets the rules inside it.**

This is not decoration. It has concrete consequences:

- The controlling crew decides which event types run in that district
- The controlling crew sets the buy-in and payout for events there
- The controlling crew decides whether outsiders may enter at all
- The controlling crew sets the entry rules — class ceilings and floors, drivetrain requirements, aspiration limits, aero and nitrous rules (Section 10.1)

**Entry rules are checked at the gate, not enforced technically.** No one inspects the car. The crew looks at it, reads its class and its build, and either waves it through or does not. A player who wants into a restricted event brings a car that fits, or detunes one that does.

To take a district, the protagonist must defeat each ranked member of the controlling crew in sequence, then defeat the crew leader. Crew members can be challenged in any order; the leader only becomes available once all members have been beaten.

Taking a district transfers rule-setting authority to the protagonist. He can then set the district's rules himself — an authority the game deliberately does *not* grant him in the festival.

### 5.3 The Festival in the City

From Act 2 onward, the festival is visible in the city world: billboards, magazine racks, radio spots, television in shop interiors, NPC conversation. It is never hidden and never mysterious.

The protagonist's response, consistently, is disinterest. He changes the subject. He looks away. NPCs who bring it up get short answers.

This is the only place in the game where the protagonist's avoidance is dramatised without the player being told it is avoidance.

### 5.4 Street Culture

The city runs on **underground car culture**: unsanctioned, self-organised, and answerable to nobody but the people inside it.

**Who is in it.** Amateurs, self-taught drivers, mechanics, shop owners, people who build cars in home garages and residential driveways. Nobody in the city races for a living. They race because the scene is the only place their car means anything.

**What a car is for.** Identity first, performance second — and the two are not separated. A car that is fast but anonymous earns nothing at a night meet. The scene reads a build the way it reads a person: stance, wheel fitment, paint, exhaust note, engine swap choice, whether the work was done properly or bodged.

**What the rules are.** Whatever the crew that controls the district says they are (Section 5.2). Rules are verbal, local, inconsistent between districts, and enforced socially — by refusal of entry, by reputation damage, by being run off the road.

**What legitimacy looks like.** Recognition. There is no certificate, no licence, no ranking body. A racer is what other racers say he is.

**What is technically permitted.** Everything a car can physically be made to do. Engine swaps across manufacturers, nitrous, illegal-height suspension, straight-piped exhausts, removed catalytic converters, unhomologated aero, non-road-legal tyres. No scrutineering exists because no organising body exists, and no build is ever rejected on grounds of legality.

The only restrictions in the city are **entry conditions set by a controlling crew for its own events** (Section 5.2) — a power cap here, a no-nitrous rule there. These are house rules, not regulations: they apply to one crew's events in one district, they change when the district changes hands, and nobody inspects the car. A racer who ignores them is not disqualified; he is simply not let in.

**What the risk is.** Police, other racers, and money. Nothing else.

---

## 6. Reputation

The city runs **two independent reputation systems**. They are separate variables with separate inputs and separate outputs, and neither overrides the other.

### 6.1 REP — General Reputation

A single numeric score representing the protagonist's standing in the city's street scene as a whole.

**Gains:**

| Action | REP |
|---|---|
| Win a street event | +100 to +400 by event tier |
| Win a roaming challenge | +75 |
| Magazine feature | +100 to +600 by brief match and composition |
| Win an Invitational | +2,500 |
| Win against a racer ranked above the player in a crew hierarchy | +50 bonus |
| Complete a police pursuit without being busted | +25 to +200 by heat level |
| Defeat a district's crew leader | +1,000 |
| Attend a night meet with a newly completed build | +50, once per build |

**Losses:**

| Action | REP |
|---|---|
| Busted by police | −150 |
| Lose to an unranked racer, or to a crew member the player has already beaten | −100 |
| Lose a roaming challenge | No REP change — these are informal and the city does not keep score |
| Withdraw from an event after accepting | −75 |
| Lose an Invitational | −300 |
| Decline the same Invitational twice | −200 |

**Tiers:**

| Tier | Threshold | Unlocks |
|---|---|---|
| Nobody | 0 | Low-stakes district events only |
| Known | 2,500 | Crew challenges, night meets |
| Contender | 8,000 | Wager events, cross-district events |
| Name | 20,000 | Invitational events, high-tier crew leaders |
| King | 45,000 | Citywide events, Act 3 conclusion |

REP determines **access and recognition**. At high REP, NPCs across the city acknowledge the protagonist by name, defer to him in conversation, and refer to him as the city's street king.

**REP never decreases below the threshold of a tier already earned.** Progression is not lost, only slowed.

### 6.2 Standing — Individual Relationship

A separate per-NPC value on a seven-point scale, from **Hostile (−3)** through **Neutral (0)** to **Loyal (+3)**.

Every named racer, crew leader, shop owner and recurring NPC in the city carries their own Standing value.

**Inputs:**

| Source | Effect |
|---|---|
| Dialogue choices | Primary driver. Every conversation with a named NPC moves Standing by ±1 or holds it. |
| Contact during races | Repeatedly ramming a specific racer lowers their Standing by 1 per event. |
| Racing clean against them | Winning without contact raises Standing by 1. |
| Roaming challenges | Same rules as any race: clean win +1, contact −1 (Section 11.1). |
| Beating them repeatedly | Three consecutive wins against the same racer lowers Standing by 1 — humiliation costs. |
| Losing to them | No effect. Losing does not damage relationships. |
| Wager outcomes | Taking a car from an NPC in a pink-slip event lowers Standing by 2. |

**Outputs:**

| Standing | On-Track Behaviour | Out-of-Race Behaviour |
|---|---|---|
| Hostile (−3) | Actively blocks, brake-checks, forces contact, will crash themselves to stop the player | Insults, refuses information, will tip off police |
| Unfriendly (−2 to −1) | Defends aggressively, closes doors, no quarter | Curt, withholds event invitations |
| Neutral (0) | Races to win, clean by default | Transactional |
| Friendly (+1 to +2) | Races hard but clean, gives room in ambiguous situations | Shares event locations, warns of police patrols |
| Loyal (+3) | Will block *for* the player in team events | Offers cars and sells parts at cost |

Friendly and Loyal NPCs are the only people the protagonist can recruit onto a festival team (Section 12.4). Every relationship built in the city is a potential seat on that roster.

**Standing is willingness, not capability.** How an NPC actually drives when it matters is governed by their personality (Section 6.4), which Standing never overrides. A Loyal racer who cannot stand losing will still not let the protagonist past.

**Resolving multiple inputs.** Inputs are applied in the order they occur and accumulate. Three consecutive clean wins against the same racer produce +3 from clean racing and −1 from repeated defeat, for a net +2: beating someone fairly builds respect faster than it builds resentment. Three consecutive wins *with contact* produce −3 and −1, for a net −4.

### 6.3 How the Two Interact

**They do not override each other. They operate on separate channels.**

REP governs what NPCs *say about* the protagonist and what he can *access*. Standing governs what individual NPCs *do to* him.

A racer at Hostile Standing, in a city where the protagonist has reached King tier, will openly acknowledge him as the king of the streets — and then spend the entire race trying to put him into a wall. Recognition is not affection. Status buys access, not goodwill.

There is no REP value high enough to make a Hostile NPC race cleanly, and no Standing value high enough to grant access to an event the player's REP tier has not unlocked.

### 6.4 Personality

Standing is how an NPC feels about the protagonist. **Personality is who they are regardless of him.**

Every named **racer** in the game carries one of six personalities. It never changes, it cannot be influenced, and it is not a stat the player can improve. It determines how that racer drives when the result is in doubt — in the city and, far more consequentially, in the festival.

Mechanics and shop owners are outside this system entirely; they have personalities, but those live in dialogue and touch no number (Section 12.4.5).

| Personality | On track |
|---|---|
| **Competitor** | Cannot stand losing to anybody, including people on his own side. Races teammates exactly as hard as rivals, never yields a position, never lifts. |
| **Wingman** | Reads the race as a position to be held rather than a place to be gained. Exceptional at defending, mediocre at attacking, will sit on a rival's nose for an entire event to keep them behind. |
| **Metronome** | Does the same lap every lap. Rarely brilliant, effectively never wrong. Does not crash, does not make contact, does not take risks. |
| **Spike** | Enormous variance. Capable of beating anyone in the field on his day and capable of putting it in the wall on the first corner. |
| **Technician** | Fastest alone, against a clock, with time to build into it. Strong in timed formats, uncomfortable wheel to wheel, loses positions under close pressure. |
| **Brawler** | Fast and physical. Leans on people, uses contact as a tool, gains places nobody else could — and collects penalties doing it. |

**The two axes do not substitute for each other.**

- A **Loyal Competitor** would do anything for the protagonist except lose to him.
- A **Friendly Wingman** will defend his position for an entire race to keep a rival off him, not out of affection, but because that is what he does.
- A **Loyal Brawler** wrecking a rival for the protagonist's benefit still incurs the conduct penalty, and the team still pays for it (Section 14.1).
- A **Hostile Metronome** is harmless. He will not touch the protagonist. He will simply be in front of him.

**Personality is visible in the city before it matters.** A player who races someone in the streets learns who they are by watching them drive: who defends, who lifts, who leans, who is quick alone and soft in traffic. Recruitment is therefore an informed decision, and a player who never raced anyone outside their own district is choosing a roster blind.

---

## 7. Police

### 7.1 Heat

Heat is a five-level pursuit-intensity value that rises during a pursuit and decays when the player is out of police contact.

| Heat | Response |
|---|---|
| **1** | Single patrol unit. Basic pursuit. |
| **2** | Multiple patrol units. Coordinated blocking. |
| **3** | Undercover units, spike strips, radio coordination. |
| **4** | Highway interceptors, roadblocks, helicopter spotting. |
| **5** | Citywide alert, heavy interceptors, rolling roadblocks, sustained air support. |

Heat carries a persistent component: repeated pursuits raise the *starting* heat level for future pursuits within the same district, decaying over several in-game days.

### 7.2 Being Busted

**The player is never permanently arrested.** There is no game-over state, no jail sequence, no removed save progress.

When busted:

1. Failure screen.
2. **Bail** is deducted automatically, scaling with heat level at the moment of capture (Heat 1: modest; Heat 5: severe).
3. **REP −150.**
4. **The car is impounded.** It is not destroyed. It is not lost.

### 7.3 Impound

An impounded car remains in the impound lot until the player pays its release fee.

**The release fee scales with the car's total value** — its base market value plus the cumulative value of every installed performance and visual part. A heavily built flagship car costs dramatically more to reclaim than a stock entry-level chassis.

The player may hold multiple cars in impound simultaneously and reclaim them in any order. Nothing in impound expires or is sold off.

This is the system's actual teeth: the punishment for reckless driving with police present is **economic and escalating**, and it scales precisely with how much the player has invested in the car they were caught in. Driving the best car in the garage during high heat is the highest-risk decision available in the city.

### 7.4 Credit and Shop Relationships

The player does not always have to pay cash.

Each of the city's independent shops carries its own **Standing** value (Section 6.2). Shop Standing determines credit terms:

| Shop Standing | Credit Terms |
|---|---|
| Hostile / Unfriendly | Cash only. No credit under any circumstance. |
| Neutral | Credit available at high interest. |
| Friendly | Credit available at low interest. |
| Loyal | Credit available at zero interest, repayable at the player's discretion. |

Credit applies to parts, repairs, bail and impound release alike. Outstanding debt accrues interest per in-game week and is deducted automatically from race winnings until cleared.

A player deep in debt to a high-interest shop is functionally forced to keep racing — which is thematically exact, and mechanically real.

---

## 8. Damage and Repair

Damage is persistent and visible everywhere in the game, and never destructive. A car cannot be written off, totalled, or removed from the garage by impact. At worst it becomes badly beaten and expensive to restore.

**What damage does depends on where the player is** (Section 4.1).

### 8.1 In the City

Damage is **visual only during an event**. Panels deform, paint scars, glass cracks, bumpers hang off — and the car drives exactly as it did before the contact. A street race is not going to be decided by a dented wing.

Damage still persists **after** the event, and it still costs money. It shows on the car in the world, at night meets, in magazine shoots, and in every NPC reaction to the build. A player who races dirty drives a visibly wrecked car around a city that judges cars.

| Damage | City effect |
|---|---|
| Cosmetic | Visible. Reduces Presentation (Section 10.4). |
| Aerodynamic | Visible. Reduces Presentation. No performance effect. |
| Mechanical | Visible under the hood. Reduces Presentation. No performance effect. |
| Alignment | Visible in stance. Reduces Presentation. No performance effect. |

### 8.2 In the Festival

Damage is **live**. Aerodynamic damage costs downforce and adds drag, a frontal impact reduces power delivery and cooling, and a heavy lateral hit introduces steering pull and uneven grip — all of it immediately, for the rest of the session, with no restart available.

This is the single largest mechanical difference between the two halves, and it is what makes the festival's conduct multiplier (Section 14.1) bite twice: contact costs points *and* costs lap time.

### 8.3 Repair

In the city, repair is performed at any shop and costs money, scaling by damage severity and by the value of the parts affected. Shop Standing applies to repair pricing and credit exactly as it does to parts (Section 7.4).

In the festival, repair between rounds is handled by that discipline's mechanic, at a cost and speed determined by their skill (Section 12.4.5).

**This is the mechanical consequence of Hostile Standing.** A racer who rams the protagonist for an entire event produces a repair bill in the city and a lost result in the festival. Relationships have a running cost, and it is paid in different currency on each side of the map.

---

## 9. Wager Events

Unlocked at Contender tier.

**Cash wagers:** both parties stake an agreed sum. Loser pays. No further consequence.

**Pink slips:** both parties stake a car. The loser's car transfers to the winner's garage.

A car lost in a pink-slip event is **never permanently gone**. The NPC who won it will drive it, and the protagonist may challenge them to a rematch for it at any time. Winning the rematch returns the car with all its installed parts intact.

Taking a car from an NPC costs 2 Standing with that NPC. Pink-slip events are therefore the fastest way to acquire a rare chassis and the fastest way to drive an NPC to Hostile. The damage is not permanent — Standing can be rebuilt through dialogue and clean racing like any other — but it is the single largest one-shot penalty in the system.

**Wager events are player-initiated and optional. Invitationals (Section 11.3) are the inverse**: the rival initiates, the stake is compulsory on both sides, and the opponent is one of the nine best drivers in the city.

---

## 10. Cars and Building

### 10.1 Vehicle Classes

Every car in the game carries a **class**, assigned automatically from a computed performance index. The index is derived from power-to-weight ratio, drivetrain layout, aerodynamic load, tyre specification and braking capability — not from purchase price.

| Class | Name | Typical Machinery |
|---|---|---|
| **D** | Street | Stock economy cars, base compacts, unmodified daily drivers |
| **C** | Tuner | Hot hatches, entry-level sport compacts, lightly built coupés |
| **B** | Sport | Sports coupés, muscle cars, seriously built compacts |
| **A** | Performance | High-end sports cars, heavily built B-class machinery |
| **S** | Supercar | Road-going supercars |
| **X** | Hypercar | Road-going hypercars and the most extreme builds in the game |

**Every car in the game is a road car.** No competition machinery exists anywhere in *Beyond* — no GT cars, no prototypes, no single-seaters, no purpose-built race chassis. The city sells road cars and the festival is contested in road cars that have been built for competition. Class X is the ceiling, and its ceiling is a hypercar with a number plate.

**Class is earned, not bought.** Installing parts raises the index, and when the index passes a class ceiling the car moves up a class. A fully built C-class tuner becomes a B-class car and races B-class fields; it does not become an unbeatable C-class car.

This single index governs every restriction in the game. Crews use it to gate district events (Section 5.2), the festival uses it to assign competition classes (Section 13.2), and both read the same number.

**A car can be detuned.** Parts can be removed or swapped down to bring a car back under a class ceiling. This is a legitimate strategy — a B-class car at the very top of its class beats an A-class car at the bottom of its own — and it is how a player enters a restricted event with a chassis they have already over-built.

### 10.2 Performance

Tunable systems: engine internals, forced induction (turbo and supercharger, with distinct delivery characteristics), suspension geometry and damping, brakes, tyre compound, transmission and individual gear ratios, differential, aerodynamics, exhaust, weight reduction, nitrous.

Every performance change has a corresponding behavioural change in the physics model. There is no purely numerical upgrade.

### 10.3 Customisation

Customisation in **Beyond** is deliberately total. The reference point is *Underground 2*: a car is not a stat block with a paint option, it is an object the player assembles from the engine bay to the boot, and most of what they install is visible.

**Exterior — body**
Front and rear bumpers, hoods, side skirts, fenders, wide-body kits, spoilers and wings, roof scoops, mirrors, door handles, splitters, diffusers, exhaust tips, roof racks, hood pins, window tint.

**Exterior — finish**
Paint in gloss, matte, satin, metallic, pearl, candy, chrome and raw. Two-tone and multi-panel schemes. Vinyl and decal editor with layering, scaling, rotation, mirroring and per-layer colour. Livery import from a player's own saved designs.

**Exterior — lighting**
Headlight and taillight units, bulb colour and temperature, fog lamps, light bars, underglow neon, wheel-well neon, interior neon.

**Wheels and stance**
Wheel design, diameter, width, offset, tyre profile, brake caliper colour, ride height, camber, toe, track width. Stance is visible and physically real — the same setting that produces the look changes how the car behaves.

**Interior**
Seats, harnesses, roll cage, steering wheel, shift knob, pedals, gauge cluster, dashboard trim, door cards, upholstery material and colour, headliner, floor mats, interior lighting.

**Engine bay**
Visible engine dress-up: intake piping, filters, valve covers, strut braces, radiator and intercooler hardware, wiring routing, painted and polished components. An engine swap is visible when the hood opens — the bay shows what is actually installed.

**Audio and boot**
Full boot build-outs, in the *Underground 2* idiom: subwoofers, mid-range speakers, amplifiers, LCD screens, displayed nitrous bottles, wiring and trim panels, boot neon. Multiple boot layouts per car, each with a different slot arrangement, including a custom layout that exposes the largest display slots.

### 10.4 Presentation

Every build carries a **Presentation** rating from 1 to 6, computed from the visual and interior work installed on it: bodywork, finish, wheels and stance, interior, engine bay and boot all contribute.

Presentation is not cosmetic bookkeeping. It is an input to three separate systems:

- **Riverside entry** (Section 5.1) — the build coherence check reads Presentation alongside build consistency
- **Magazine features** (Section 11.2) — magazines only approach cars above a Presentation threshold
- **Night meet dialogue** — NPC reactions to the car scale with it

**Audio and interior parts have a cost, and it is weight.** A full boot build with subwoofers, amplifiers and screens adds real mass, carried high and behind the rear axle — the worst place in the car for it. The physics model simulates this: a heavily built audio system shifts the balance rearward, slows direction changes, and makes the car lazier on turn-in.

A player can therefore build a 6-Presentation show car that is measurably slower than the same chassis stripped, and the game never resolves that tension for them. Riverside and the magazines want one thing. The Old Guard's stopwatch wants the other. Most players end up keeping two Blueprints for the same car.

**Presentation does nothing in the festival.** It is not scored, not read, not referenced, and most of what produces it is prohibited there outright (Section 13.2). The rating exists entirely inside the city, which is the only place that cares what a car looks like.

### 10.5 Cultural Fit

Each district's culture has a recognised build language. A car built in a district's idiom is recognised by that district's NPCs — appearing at a Ridgeline meet in a coherent drift build produces different dialogue than appearing in an untouched showroom car.

This does not gate content. It is the game's way of letting the player's build speak in conversation without the player having to say anything.

### 10.6 Blueprints

A **Blueprint** is a complete saved specification of a car: every installed performance part, every tuning value, every visual modification, paint, vinyl layout, wheel choice, ride height and alignment setting.

Each car in the garage holds multiple Blueprints, and the player switches between them freely without re-purchasing anything they already own. A single chassis can hold a street setup, a wet-weather setup and a class-legal circuit setup simultaneously.

Blueprints are the unit of the game's online system (Section 17).

---

## 11. Street Event Types

| Type | Format |
|---|---|
| **Sprint** | Point to point through live city traffic. |
| **Circuit** | Multi-lap loop through public streets, held open by spotters. Unsanctioned. |
| **Drag** | Straight-line, manual shifting, launch control, live traffic. |
| **Drift** | Scored run on a designated section — angle, speed, line, duration. |
| **Speed Run** | Highest average speed across a long high-speed route. |
| **Crew Event** | Team format. Aggregate crew position determines outcome. |
| **Rival Challenge** | One-on-one against a named racer. |
| **Night Meet** | Non-competitive gathering. Build display, dialogue, event invitations, spontaneous challenges. Presentation drives NPC reaction. |
| **Wager Event** | Cash or pink slip. See Section 9. |

All street events run with live civilian traffic and active police presence unless the controlling crew has arranged otherwise.

### 11.1 Roaming Racers

**Crew members drive around the city.** They are not confined to their home district, they are not event markers, and they are not waiting for the player. They commute, cruise, run errands and show off, in their own crew's build language, on their own routes, at their own hours.

A Meridian member in a Zonda can be found idling at a light near the Docks. An Old Guard driver in a naturally aspirated coupé can be caught on the Expressway Ring at 4 a.m. Where a racer is has nothing to do with where their crew rules.

**Challenging.** Pull alongside, flash the headlights. They accept or they refuse, and the refusal is not arbitrary:

| Condition | Response |
|---|---|
| Player's car is within one class of theirs | Accepts |
| Player's car is two or more classes below | Refuses, dismissively |
| Player's car is two or more classes above | Refuses, uninterested |
| Standing is Hostile | Always accepts, regardless of class |
| Standing is Loyal | Often refuses, in good humour |
| Recently raced this NPC | Refuses until a cooldown elapses |
| Police pursuit active | Refuses and leaves |

**Format.** A destination is marked somewhere across the city. There is no course, no checkpoints and no route — both cars leave from where they are standing and the first to reach the marker wins. The player picks their own line through live traffic, and so does the opponent, which means the two cars frequently do not see each other again until the finish.

**Stakes.** A cash wager, set automatically by the lower of the two cars' classes. Winner takes it. No pink slips and no negotiation — these are impulsive races between strangers at a red light, not arranged events.

**Rewards and consequences.**

| Outcome | Effect |
|---|---|
| Win | Cash wager, REP +75, Standing with that NPC ±0 |
| Win with no contact | Cash wager, REP +75, Standing +1 |
| Lose | Wager forfeited, no REP change |
| Ram the opponent during the race | Standing −1, regardless of result |
| Busted by police mid-race | Wager forfeited, standard bust consequences (Section 7.2) |

Police do not schedule these races and do not know they are happening — but the race runs through live traffic at speed, and a patrol that sees it joins in. A roaming challenge that starts as easy money can end in impound.

**Why this exists.** Roaming racers are the city's fastest source of money and its cheapest source of REP, available from the first minute of Act 1 with no unlock requirement. They are also how the class system is taught without a tutorial: a player in a C-class tuner will spend Act 1 being refused by cars they cannot yet touch, will watch hypercars move through traffic they have no way to challenge, and will understand exactly what The Heights is long before they are allowed near it.

### 11.2 Magazine Features

The city's underground car magazines approach the protagonist once he is worth putting on a cover.

**Trigger.** An offer arrives when two conditions are met simultaneously: the player has reached a REP tier the magazine cares about, and owns a car above a **Presentation** threshold (Section 10.4). Offers scale — early magazines want a 2-Presentation build, the last ones will not photograph anything under 5.

**The magazines.** Each is tied to a crew culture, publishes accordingly, and wants a specific kind of car:

| Magazine | Culture | Wants |
|---|---|---|
| **Torque & Tenths** | Old Guard | Naturally aspirated, low class, immaculate, no flash |
| **Sideways** | Ridge Union | Rear-wheel drive, angle kit visible, mountain backdrop |
| **Quarter** | Dockline | Drag builds, wheelie bars, cages, engine bay open |
| **Boulevard** | Riverside | Stance, finish, interior, boot — presentation above all |
| **Redline** | Ringrunners | Aero, long gearing, speed machinery, expressway backdrop |
| **Private Plate** | Meridian | Class S and X only. Hypercars, nothing else. |

**The shoot.** The player controls the photograph:

- **Car.** Any owned car that meets the magazine's brief and threshold.
- **Location.** Any district. The backdrop is the district's real geography.
- **Time of day and weather.** Set freely.
- **Panels.** Doors, hood and boot open or closed, independently.
- **Camera.** Position, height, angle, focal length, depth of field.

**Scoring.** The magazine issues a brief, and the shot is graded against it rather than against taste. *Quarter* asked for the engine bay — a beautiful photograph with the hood closed scores badly. *Private Plate* asked for a hypercar — a perfectly composed shot of a built Civic is rejected outright. *Boulevard* asked for the boot build; the boot had better be open.

| Result | REP |
|---|---|
| Brief met, strong composition | +600 |
| Brief met, weak composition | +300 |
| Brief partially met | +100 |
| Brief ignored | Offer withdrawn, no REP, magazine will not approach again for that tier |

**Afterwards, the cover exists in the world.** It appears on newsstands, in shop interiors, and in the garages of NPCs. Crew members reference it in dialogue. A player who photographed a Dockline drag car for *Quarter* will hear about it from Dockline; so will Riverside, who will have opinions.

**Why this exists.** Magazine features are the only REP source in the game that does not involve winning a race. They are how a player who builds obsessively converts that work into standing, and they are the mechanism that makes the entire customisation system — interior, engine bay, boot audio, none of which makes a car faster — matter to progression instead of sitting beside it.

---

### 11.3 Invitationals

Unlocked at **Name** tier. The player does not find these — they arrive.

Once the protagonist is somebody, the city's best drivers start contacting him directly. An Invitational is an unsolicited one-on-one challenge from a named elite racer, and it is the highest-stakes content in the city.

**The roster is finite.** Nine racers issue Invitationals: the highest-ranked driver from each of the seven crews, plus two unaffiliated drivers who belong to nobody and are the two hardest opponents in the illegal scene. Each can be raced once per act. They are not procedurally generated and they do not respawn.

**The terms are fixed and non-negotiable.**

- **Both cars are staked.** Winner takes the loser's car, with every installed part.
- **A cash purse on top**, larger than anything else the city pays.
- **The rival's car is disclosed in advance.** The player knows exactly what they are racing and exactly what they would win before accepting.
- **The player nominates their own stake** from their garage, within the class the invitation specifies. A player cannot enter a hypercar against a B-class rival to farm cars.

**Declining.** Permitted, and free the first time. A second refusal from the same racer withdraws the invitation for the remainder of the act and costs REP −200 — publicly refusing a challenge twice is a statement about the protagonist, and the city reads it as one.

**Losing.** The staked car transfers to the rival, and REP −300. The car is recoverable under the standard rule (Section 9): the rival drives it, and the protagonist can challenge them for it again. Nothing is permanently gone. But the rematch is another Invitational, on the same terms, against a driver who has just beaten him.

---

#### Formats

Invitationals are **endurance events**. They are long, they are unbroken, and they cover ground no other event in the game uses.

**CROSS-CITY SPRINT**
Point to point, corner to corner of the map, fifteen to twenty-five minutes. The route crosses every district in the city and finishes in the mountains above Ridgeline — dock roads to city grid to expressway to residential boulevards to a climb that does not stop until the finish. No checkpoints beyond the destination; the player chooses their own way through and so does the rival.

**RING CIRCUIT**
Three laps of a loop that encircles the entire city, using the Expressway Ring on one side and surface streets on the other. Roughly thirty minutes. The expressway sections are flat-out and the surface sections are traffic-choked, and the two demand opposite setups from the same car.

**RIDGELINE DUEL**
The mountain roads above the city, on the steepest sustained gradients in the game. Two phases.

*Phase one:* the rival leads and the protagonist chases. Points accumulate the closer he stays without making contact — contact scores nothing. Overtaking and holding the lead for ten seconds ends the phase immediately in his favour.

*Phase two:* the positions reverse. The protagonist leads and bleeds points while the rival sits on his bumper. The same ten-second rule applies against him.

Nitrous is disabled for the entire duel. There are no barriers — Ridgeline never had any — and leaving the road means a long recovery back to it and time the player will not get back. The car will look worse for it; it will not drive worse (Section 8.1).

---

#### Why These Are Endurance Races

The distance is not the point, and neither is simulation. The city is arcade (Section 4.1) — there is no tyre wear here, no brake fade, and no performance loss from damage. What makes an Invitational hard is that **nothing resets inside it**.

- **No restarts.** The event runs from green to finish in one piece. There is no retry from a checkpoint, and quitting forfeits the staked car.
- **Concentration over distance.** Every other event in the city is two to four minutes long. An Invitational is twenty-five, through live traffic, at speed, with a car worth more than the player's remaining money riding on it. The failure mode is not a bad corner — it is the eleventh minute.
- **Police are live throughout.** A pursuit does not pause the race. Heat escalates normally, the rival does not wait, and being busted forfeits the event and the staked car in one stroke — the worst single outcome available in the city.
- **The route changes character several times.** A cross-city sprint runs dock straights, then a traffic-choked grid, then an expressway, then a mountain climb. One setup cannot be right for all four, and the player picks which section to be fast in.
- **The opponents are the city's best.** These drivers do not make mistakes under pressure the way crew members do, they do not take bad lines, and they know the routes.

**This is the closest the city gets to what the festival will demand — sustained precision over distance, with a real consequence for a single error.** It is not the same thing. The festival will add wear, temperature, live damage and a rulebook on top of everything above. But the habit of holding a race together for twenty-five minutes is learned here, from criminals, in the dark, with the player's own car on the line.

---

#### Rewards

| Outcome | Effect |
|---|---|
| Win | Rival's car with all parts, cash purse, REP +2,500, Standing −2 with that racer |
| Lose | Staked car forfeited, REP −300 |
| Busted mid-event | Staked car forfeited, event lost, standard bust consequences (Section 7.2) |
| Decline (first time) | Nothing |
| Decline (second time) | Invitation withdrawn for the act, REP −200 |

Winning an Invitational takes a car from a driver who did not want to lose it, which costs 2 Standing exactly as a pink slip does (Section 6.2). **The nine best drivers in the city are therefore the nine easiest people to turn Hostile**, and a player who wins every Invitational in the game arrives at the festival having alienated the only city racers good enough to have followed him there.

## 12. The Festival

### 12.1 What It Is

A large sanctioned motorsport festival held on a dedicated closed-circuit complex outside the city. Grandstands, paddocks, scrutineering, official timing, sponsor presence, a rulebook.

It is **not** Formula 1, GT3, or any factory-backed professional series. There are no works teams, no manufacturer programmes, no driver contracts, no homologated race cars built for a rulebook from the ground up.

It is the tier directly below that: **the sanctioned tuner scene** — the *ProStreet* model. Built cars, not race cars. Private entrants, small independent teams, and sponsored tuning shops. Closed tracks, scheduled race days, technical scrutineering, official timing, and a championship at the top.

It **runs for several months**, not a single weekend, with events held on scheduled official dates.

### 12.1.1 Sanctioned Culture

**Who is in it.** Semi-professionals and professionals: drivers who race for a living or close to it. Shop-sponsored entrants, funded privateers, team-run cars with dedicated crews, engineers, data, and telemetry. No manufacturer money and no works programmes — the support is commercial and local, not industrial. Some of these drivers have never raced on a public road in their lives.

**What a car is for.** Winning within a rulebook. Visual identity still exists — liveries, sponsor decals, team presentation — but it is subordinate to legality and effectiveness. An illegal car is not a bold statement here. It is a car that does not start.

**What the rules are.** Fixed, written, published in advance, identical for everyone, and enforced by scrutineers who inspect cars before and after events. No crew and no amount of winning changes them (Section 12.2).

**What legitimacy looks like.** Ranking. Timing sheets, standings boards, championship points. The scene does not care who you are; it cares what the clock and the classification say.

**What is technically permitted.** Only what each discipline's regulations allow (Section 13). Everything else is rejected at scrutineering.

**What the risk is.** Disqualification, penalties, suspension, and failing to qualify.

### 12.1.2 Why the Festival Is Hard

The festival is the hardest content in the game, and it is hard for six compounding reasons — none of them arbitrary difficulty inflation.

**1. The field is better than the city's field.** Street racers in the city are amateurs driving cars they built themselves. Festival competitors are professionals and semi-professionals with team support, engineering data, and track-specific setups. Festival AI runs tighter lines, brakes later and more consistently, defends without error, and does not make the unforced mistakes that city AI makes under pressure. A build that dominates a district will finish mid-pack in its first festival event.

**2. The festival gives the player nothing.** No cars are awarded, loaned, or provided for any event, including championship rounds. Every car the player enters must be a car they acquired in the city and built themselves. The festival is a competition the protagonist enters using the product of the life he spent avoiding it.

**3. Every event is regulated.** Cars that are quick on the street are frequently illegal on the circuit. The player cannot simply bring their fastest car; they must bring a car that is *legal for that discipline and class* and then make it as good as the regulations permit.

**4. Breadth is mandatory.** Qualification requires top-four standing in all five disciplines (Section 14.2). A single exceptional car cannot carry the player. Five compliant, purpose-built cars are the minimum entry requirement to the championship.

**5. He cannot enter alone.** Registration is by team, not by driver — five drivers, five mechanics, all of them named people recruited in the city (Section 12.4). The single hardest entry requirement in the game is not a car or a lap time. It is having ten people willing to put their season in the hands of a street racer.

**6. The car is being simulated now.** Tyres wear and change temperature, brakes fade, and damage degrades the car live with no restart available (Section 4.1). None of this existed in the city. A player arriving from five acts of arcade street racing will lose their first festival event to a set of cold tyres and not understand why.

### 12.1.3 The Shift in Mindset

The festival does not just ask the player to drive better. It asks them to think about the car differently, and the game is explicit that this is the hard part.

**In the city, the car is an expression.** The player builds what they want, how they want it, and the only question ever asked is whether it is theirs. Nothing is prohibited. Nothing is inspected. A subwoofer in the boot, a wide-body kit that fits nothing, neon under the sills, an engine from a different manufacturer — all of it is legal because legality is not a concept the street scene has.

**In the festival, the car is a submission.** It is a document handed to an authority that will check it, line by line, against a rulebook it did not write for the player's benefit. The question is no longer what the player wants the car to be. It is what the car is allowed to be, and then how far the player can push it *inside* that.

This is the single largest adjustment in the game, and it lands in three places at once:

| | City mindset | Festival mindset |
|---|---|---|
| **Goal of a build** | Make it mine | Make it legal, then make it optimal |
| **Constraint** | Money | Regulation, then money |
| **What "better" means** | Faster, or more me | Faster inside a fixed box |
| **Who decides** | The player | The rulebook, read by the mechanic |
| **What gets removed** | Nothing | Most of what the player installed in the city |

**The first festival registration is where the player feels this.** They will bring their favourite car — the one they built over five acts, photographed for a magazine, and drove to the top of the city — and the registration screen will reject it for four separate regulation breaches. The boot build is illegal ballast. The body kit is outside the dimensional limits. The tyres are not a permitted compound. The nitrous cannot be there at all.

The car is not bad. The car is not *for this*.

**And the skill the festival actually rewards is the one the city never asked for: working inside somebody else's constraints and finding room in them.** That is the protagonist's father's job description. It is also, not coincidentally, the thing he has spent the entire game refusing to do — and the mechanic is the person who teaches it to him.

### 12.2 Regulation

**In the festival, nobody the player can beat sets the rules.**

This is the structural inversion of the city. In the city, taking a district transfers rule-setting authority to the protagonist. In the festival, the rules come from an organising body that does not race and cannot be challenged. Class regulations, technical scrutineering, conduct penalties and event scheduling are fixed and external.

The protagonist can win everything in the festival and never gain authority over it. That is the point.

### 12.3 What Carries Over and What Does Not

| Carries over | Does not carry over |
|---|---|
| Every car in the garage | City REP |
| All money and outstanding debt | Any district authority |
| All installed parts and Blueprints | Any rule-setting privilege |
| Shop relationships and credit terms | Access unlocked by city tier |
| Individual NPC Standing — and the roster it makes possible | The ability to compete alone |
| Driving skill, entirely | — |

The protagonist arrives with everything he built and none of what he became. He is a stranger with a garage and ten people who agreed to come.

### 12.4 The Team

**A driver cannot register for the festival. Only a team can.**

The protagonist does not enter the festival by paying an entry fee and showing up with a car. He enters by submitting a full team registration to the organising body: a named roster, a declared car list, and a signed entry for every discipline he intends to contest. An incomplete roster is rejected. There is no solo entry, no guest entry, and no exception for a driver who won everything in the city.

This is the wall the protagonist hits the moment he decides to go. He has spent five acts being the best driver in a scene that required nothing of him but driving, and the festival's first question is who else is coming.

---

#### 12.4.1 Roster Requirements

A legal team registration requires **ten named people plus the protagonist**:

| Role | Count | Function |
|---|---|---|
| **Driver** | 5 — one per discipline | Races alongside the protagonist in every event of that discipline. Both cars score. |
| **Mechanic** | 5 — one per discipline | Prepares, tunes, scrutineers and repairs the cars for that discipline. |

The protagonist is the team's second entry in all five disciplines. He races everything. The teammate races it with him.

**All ten of these seats must be filled by named NPCs the player recruited in the city.** The festival does not supply staff, the game does not generate filler personnel, and money cannot buy a roster. A player who reaches the end of Act 5 with no relationships has nothing to register and cannot enter.

---

#### 12.4.2 Recruitment

Recruitment happens in the city, during the campaign, through Standing (Section 6.2).

| Standing | Response to an invitation |
|---|---|
| Hostile / Unfriendly | Refuses. Will not discuss it. |
| Neutral | Refuses. Has no reason to care. |
| Friendly (+1 to +2) | Considers it. Accepts if the discipline matches their culture and the salary is met. |
| Loyal (+3) | Accepts immediately, regardless of salary. |

**Drivers come from crews. Mechanics come from shops.** A mechanic's Standing is built the way any shop relationship is built — by using that shop, over time, for real work (Section 7.4). A driver's Standing is built by racing them, talking to them, and not wrecking them.

**Specialisation is cultural and it is binding.** Every recruitable NPC has one discipline, inherited from where they come from:

| Discipline | Recruit from |
|---|---|
| **Drag** | Dockline |
| **Grip** | The Old Guard |
| **Drift** | Ridge Union |
| **Speed** | Ringrunners |
| **Sprint** | Riverside and The Yard |

A Ridge Union driver cannot be registered for Drag. A Dockline mechanic cannot prepare a Grip car. There is no cross-training and no substitution.

**Standing decides who will come. Personality decides what they are worth once they do** (Section 6.4) — for drivers. For mechanics, Standing decides who will come and **Expertise, specialisation and Insights** decide what they are worth (Section 12.4.5). A player choosing between two Friendly drift drivers is choosing between two temperaments; a player choosing between two drift mechanics is choosing between two bodies of knowledge.

**The consequence is unavoidable: the player must build relationships across the entire city.** A player who spent the campaign inside one district, however dominant, cannot field a legal roster. The five disciplines map onto five crew cultures, and the festival requires all five.

---

#### 12.4.3 The Invitational Problem

The nine best drivers in the city are the nine best drivers the player could put on the roster. They are also the nine hardest people to keep Friendly, because the only way to face them is an Invitational, and winning one takes their car and costs 2 Standing (Section 11.3).

A player who wins every Invitational in the game arrives at registration with an elite garage and a roster of nobodies. A player who declines them keeps the relationships and enters the festival slower than they could have been.

**The game never resolves this.** It is the sharpest expression of the protagonist's whole problem: he is extremely good at taking things from people, and the one thing he needs cannot be taken.

---

#### 12.4.4 Salaries

Every registered team member draws a salary for the season, paid from the player's money, deducted per scheduled race date.

| Factor | Effect on salary |
|---|---|
| NPC's standing in their own crew | Higher-ranked racers cost more |
| Standing at Loyal | Waived entirely — they are not doing it for money |
| Discipline scarcity | A driver for a discipline the player has few contacts in commands more |

A roster of Friendly professionals is expensive enough to compete with the five-car budget (Section 13.3), and the player will be back in the city earning between race dates to cover both. A roster of Loyal friends costs nothing and is the single largest economic advantage available in the game.

**Sponsorship.** A Meridian contact at Loyal Standing will underwrite the team's salaries for a full season (Section 5.1). This is the only way to field a roster of paid professionals without funding it out of street winnings, and it is the one thing The Heights is good for beyond hypercars.

**Relationships are the game's real currency, and this is where it is spent.**

---

#### 12.4.5 Mechanics

The mechanic is the most important non-driving relationship in the game, and in the festival he is worth more than the teammate.

**A driver can only be as good as the car allows. In the city, the player decides what the car is. In the festival, the mechanic does** — because the mechanic is the one who knows where the rulebook has room in it.

---

##### Expertise

Every mechanic carries an **Expertise rating from 1 to 5**, inherited from their shop and raised by the player's Standing with them. Expertise governs the baseline: how good the car is before the player touches anything.

| Function | Effect |
|---|---|
| **Baseline setup** | The car's starting tune for that track. A 1-Expertise mechanic hands over something generic; a 5 hands over something already close to optimal. |
| **Scrutineering** | Catches regulation breaches before registration (Section 13.2). A weak mechanic misses things and the car is rejected at the gate; a strong one flags the problem and proposes the fix. |
| **Repair between rounds** | Faster and cheaper repair of damage carried out of an event. At Expertise 5, repairs are free. |
| **Tyre strategy** | Chooses compound, pressure and starting temperature against the conditions — a festival-only concern, since the city does not simulate wear (Section 4.1). |

---

##### Specialisation

Beyond Expertise, every mechanic has one **technical specialisation**. It is where their knowledge is deep rather than broad.

| Specialisation | What they are unusually good at |
|---|---|
| **Engine** | Extracting power inside restrictor and aspiration limits |
| **Aero** | Finding downforce inside the dimensional limits, and cutting drag nobody noticed |
| **Chassis** | Geometry, weight distribution, damper and spring work |
| **Rubber** | Compound selection, pressure, temperature windows, wear management |
| **Rulebook** | Knows the regulations better than the scrutineers do, and where they are silent |

A team with five mechanics has five specialisations, and the player chooses which disciplines get which. A Rulebook mechanic on Grip and an Engine mechanic on Drag is a different season than the reverse.

---

##### Insights

**This is what actually separates a good mechanic from a great one.**

Every mechanic holds a personal set of **Insights** — specific, legal, non-obvious optimisations that they know and most of the paddock does not. An Insight is never a cheat and never a grey area. It is a place where the regulation permits something the field has not thought to do.

Examples of the form:

- A shorter intake runner recovers most of what a class restrictor takes away, and the restrictor rule says nothing about runner length
- Running the minimum permitted ride height at the front and two millimetres above it at the rear passes the ride-height check and produces measurable rake
- The permitted treaded competition tyre has a compound that comes in a full lap earlier than the one everybody runs
- A splitter cut to the inner edge of the dimensional limit rather than the outer edge loses almost no downforce and sheds real drag
- The minimum weight is verified post-event, not pre-event, which means where the ballast sits is entirely the team's business

**How Insights are acquired.** They are not bought and not unlocked by progression. Each mechanic's Insights become available as Standing with that mechanic rises — a Neutral mechanic prepares the car, a Friendly one starts thinking out loud, a Loyal one tells the player everything he knows. Expertise is what he can do; Insights are what he will share.

---

##### The Build Dialogue

Insights are delivered as **dialogue in the build screen**, while the player is working on the car.

The mechanic is present. He watches what the player installs, and he comments — unprompted, in character, and specifically about the part currently selected. The player can act on it or ignore it.

The register is a working mechanic talking to somebody he is building a car with:

> *"That restrictor's going to strangle you. But the rule's on the restrictor, not the plenum — put the short runners on and you'll get most of it back. Nobody in this class does it. I don't know why."*

> *"Don't. That kit's four millimetres over on the splitter. It'll pass a glance and fail the gauge, and they check the gauge."*

> *"You're on the hard compound because everyone's on the hard compound. On this surface the soft goes off two laps early and gains you half a second for eight. Your call."*

**Nothing in the build dialogue is mandatory and nothing is a quest marker.** The mechanic does not have objectives, does not track whether the player listened, and does not repeat himself. He says his piece once per part and goes back to work.

A player who ignores their mechanic can still win the festival. They will be doing it in a car that is legal, prepared, and slower than it needed to be, against teams whose mechanics were listened to.

---

##### Mechanic Personality

**Mechanics do not use the racer personality system** (Section 6.4). They are not drivers, they never take a start, and there is no on-track behaviour for a personality to govern.

They have personalities anyway, and they come through entirely in dialogue: the one who explains everything twice, the one who says four words a session, the one who is openly contemptuous of the festival and does the work perfectly regardless, the one who will not shut up about a car he built in 2009. None of it touches a number. All of it is why the player remembers which one they took.

A player with a Loyal mechanic at Expertise 5 has, functionally, a second protagonist — the only character in the festival who is there for every build, every registration, every repair, and every radio call.

---

##### What a Weak Mechanic Costs

| Expertise | Season with him |
|---|---|
| **1** | Generic setups, missed breaches, expensive repairs, no Insights. The car is legal and nothing more. |
| **3** | Competent baseline, catches most breaches, some Insights at Friendly. Competitive, never advantaged. |
| **5** | Near-optimal baseline, never fails scrutineering, free repairs, full Insight access at Loyal. The car is better than its specification suggests. |

A player with a weak drift mechanic will show up with a car that is legal, prepared, and half a second off — every single round, all season.

---

#### 12.4.6 Team Standings

Every festival event scores twice: once for the individual Driver Rank (Section 14), and once for the **team**.

Team points from a single event are the sum of both team entries' points — the protagonist's and his teammate's — after each has had its own conduct multiplier applied (Section 14.1). A teammate who finishes fourth cleanly contributes more than one who finishes second by punting someone off.

Team points accumulate across all five disciplines into a single Team Standings table, and that table is public, updated after every race date, and displayed at the festival complex.

**Team Standings are a qualification requirement.** To reach the championship the protagonist must satisfy both conditions (Section 14.2):

1. Top four in all five disciplines individually, and
2. His team inside the top eight of the Team Standings.

A player can therefore drive flawlessly all season and still fail to qualify, because the five people he recruited were the five people who would have him.

---

#### 12.4.7 During the Championship

Championship rounds are contested by teams, not individuals. The protagonist and his discipline teammate both enter each round, and both results count toward the team's championship total — but the individual championship, and the Circuit Final that decides it, is his alone (Section 15).

Teammates race their own race. **Standing decides whether they are willing to help the protagonist; personality decides whether helping is something they are capable of** (Section 6.4). A Loyal Wingman will bury his own result to protect the protagonist's. A Loyal Competitor will do everything for him except finish behind him.

Neither is a bug and neither is disloyalty. The player chose both of them.

### 12.5 Standing During a Season

Standing is **frozen for the duration of a festival season**. Festival dialogue does not modify it, contact in a festival event does not modify it, and a teammate cannot be recruited, replaced or lost mid-season. The roster the protagonist registers is the roster he races with until the season ends.

Standing continues to move normally in the city between scheduled race dates and between seasons. A player who fails to qualify and re-registers (Section 14.2) does so with a fresh roster drawn from whatever Standing values the city has produced in the meantime — which is the second chance the system offers: a failed season is time to go back and build the relationships that were missing.

### 12.6 Calendar and Time

The festival calendar consists of scheduled official race dates across its multi-month run.

Time in the city does not advance on a fixed clock. It advances when the player **elects to advance to the next scheduled festival date** from the festival registration menu. Between two scheduled dates, the player has unlimited time in the city to earn money, build cars, contest street events and pursue city content.

**No festival event can be missed.** The next scheduled date does not arrive until the player chooses to attend it. The months-long duration is fiction the world reflects — seasonal lighting changes, NPC dialogue referencing the festival's progress, updated standings boards — without imposing a real-time failure condition on the player.

---

## 13. Festival Disciplines

Five disciplines, each with its own ladder and its own points table.

**GRIP** — Multi-lap circuit racing. Contains four sub-formats:
- *Open Grip* — full field, mixed specification
- *Class Grip* — restricted to a single performance class
- *Sector Shootout* — the track is divided into sectors; points awarded per fastest sector
- *Time Attack* — single fastest lap, no wheel-to-wheel running

**DRAG** — Straight-line over a fixed distance. Manual staging, launch, shift precision. Build specialisation is near-total; a drag car is useless elsewhere.

**DRIFT** — Scored runs judged on angle, speed, line and commitment. Two solo runs and a team tandem; see Section 13.1.

**SPEED** — Long, fast, narrow point-to-point routes where top speed and stability at the limit matter more than cornering.

**SPRINT** — Point-to-point circuit racing on the festival complex's connected road courses. Wheel-to-wheel, no laps, no second chance at a corner.

### 13.1 Running Order

**Every festival event is entered by two cars from the same team** — the protagonist and his discipline teammate (Section 12.4). How those two cars run is not the same in any two disciplines.

Some disciplines put them on track together. Some run them one at a time. One scores them as a single unit and cannot be won by a driver alone. The running order is fixed per discipline and is part of what each discipline is.

---

#### SPRINT — Both cars, together, from the same grid

Full grid, both team entries released at once. Eight cars, four teams, two apiece.

There is no phase structure and no solo running. It is a point-to-point race from a standing start, and the teammate is simply another car in it — one who happens to be wearing the same colours.

**Team relationship: positional, and it is where the Wingman earns his keep.** Sprint has no phase structure and no cooperation mechanic, but it does have a rival directly behind the protagonist, and a teammate is a car that can be between them.

| Personality | Behaviour toward the protagonist's race |
|---|---|
| **Wingman** | Actively defends. Will drop back to cover the protagonist, hold a faster rival for the whole distance, and finish lower than he could have to do it. |
| **Metronome** | Neutral. Races his own race cleanly and is a rolling obstacle to whoever is behind him. |
| **Technician** | Vulnerable. Fast in clean air, gives up positions the moment someone sits on his bumper. |
| **Competitor** | Races the protagonist as hard as anyone else. If he is quicker, he passes him. |
| **Brawler** | Will physically block, and will earn the conduct multiplier to prove it. |
| **Spike** | Either leads the race or is not in it. |

Both entries score their own classified position and the two are summed. Sprint is the baseline the other four are variations on.

---

#### GRIP — Split by sub-format

Grip runs four sub-formats and the running order changes between them.

| Sub-format | Running order |
|---|---|
| **Open Grip** | Both cars on the grid, full field, simultaneous |
| **Class Grip** | Both cars on the grid, restricted to one performance class |
| **Time Attack** | Sequential. Teammate runs alone, then the protagonist runs alone. No wheel-to-wheel contact is possible. |
| **Sector Shootout** | Sequential. Each car runs the full lap alone; sectors are timed independently. |

**Team relationship: additive, never cooperative.** In the timed sub-formats the two drivers never share a track, so there is no slipstream, no blocking, no interference and no way to help — the team score is the plain sum of two solo performances.

This makes Time Attack and Sector Shootout the purest read of a teammate's actual quality in the entire festival. Nothing the protagonist does can flatter or drag down the number. A weak Grip teammate is visible on the timing sheet, alone, in public, every round.

---

#### DRAG — Sequential qualifying, then a bracket that can pair them against each other

Two phases.

*Phase one — qualifying.* Each car runs the strip alone against the clock. Teammate first, protagonist second. Elapsed times set the bracket seeding.

*Phase two — elimination.* Head-to-head, two lanes, single elimination. Seeding places the two team entries on opposite sides of the bracket, so they cannot meet before the final.

**If both reach the final, they run against each other.** This is the only event in the festival where the protagonist races his own teammate with something on the line, and the game does not soften it:

- The team scores first and second regardless of the outcome — the maximum available.
- The individual Driver Rank does not. One of them wins the round and one does not.
- **Whether the teammate lifts is a matter of personality, not Standing.** A Wingman or a Metronome at Loyal will hand it over. A **Competitor will not, at any Standing** — he came to win, and the game does not treat that as betrayal.

---

#### DRIFT — Three phases, ending as a pair

The most structured event in the festival, and the only one where the two team entries are scored as a single unit.

*Phase one — teammate solo.* He runs the course alone, judged on angle, speed, line and commitment. The protagonist watches from the wall. He cannot intervene, cannot advise once the run starts, and his own performance has not begun.

*Phase two — protagonist solo.* Same course, same judges, same criteria, run alone.

*Phase three — team tandem.* The two of them run the course together as a pair, lead and chase, against another team's pair. This phase is scored on **synchronisation**: proximity held through the corners, matched angle, matched transition timing, and the chase car mirroring the lead car's line without contact.

**Team relationship: the deepest in the game, and it is gated by both axes.**

Standing decides whether the teammate is trying to synchronise. Personality decides whether he can.

| | Friendly | Loyal |
|---|---|---|
| **Metronome / Wingman** | Predictable, holds a usable line | Best tandem scores in the game — identical lines, matched transitions |
| **Technician** | Precise alone, hesitant in proximity | Synchronises, but only after a run or two to settle |
| **Competitor** | Runs his own line, will not follow | Tries to lead every phase; the pair scores well but never cleanly |
| **Brawler** | Close, aggressive, contact risk | Very close, very committed, occasional contact that costs both of them |
| **Spike** | Unusable — either perfect or in the wall | Same, with more commitment |

Two drivers who trust each other and are temperamentally able to work together score dramatically higher than two drivers who are merely both fast. **Drift is the one discipline in the festival that a player cannot win on driving alone**, and it is deliberately placed in a game about a man who spent five acts insisting he did not need anyone.

---

#### SPEED — Released together, and the slipstream is real

Both cars released as a pair over a long, fast point-to-point route. Trap speeds and elapsed time are recorded individually.

**Team relationship: mechanically cooperative, and personality decides who benefits.** At the velocities Speed runs at, the slipstream is worth real time, and the car in front is giving it away. A tow is a genuine sacrifice — the lead car takes the full aerodynamic load so the following car does not.

| Personality | Behaviour at Friendly | Behaviour at Loyal |
|---|---|---|
| **Wingman** | Leads by instinct, gives the tow | Leads the whole run, gives the tow |
| **Metronome** | Holds station wherever he starts | Leads and gives the tow |
| **Technician** | Uses the tow himself | Alternates, trading the lead |
| **Competitor** | Takes the tow and keeps it | Takes the tow and keeps it — he will not give up trap speed for anyone |
| **Brawler** | Sits far too close | Sits far too close, and the contact risk at that speed is real |
| **Spike** | Unpredictable | Unpredictable |

The team total is the sum of both cars, so a teammate sacrificing his own trap speed to lift the protagonist's is not always the optimal team play — and the ones who do it anyway are doing it because of who they are, not because it is correct.

---

#### Summary

| Discipline | Running order | What the teammate can be |
|---|---|---|
| **Sprint** | Simultaneous, full grid | A shield, an obstacle, or a rival |
| **Grip — Open / Class** | Simultaneous, full grid | A shield, an obstacle, or a rival |
| **Grip — Time Attack / Sector** | Sequential solo | A number on the sheet, nothing more |
| **Drag** | Solo qualifying, then head-to-head bracket | A potential opponent in the final |
| **Drift** | Teammate solo, protagonist solo, then tandem pair | A partner, and the score depends on it |
| **Speed** | Released as a pair | A tow, or someone using yours |

### 13.2 Technical Regulations

Every festival event has an entry specification. A car that does not meet it cannot be registered, and the player is told exactly which regulation it fails at the registration screen — never mid-event.

**Universal regulations (all disciplines):**

- Full roll cage, fixed racing seat, harness, external kill switch, fire suppression
- Working lights, functional windscreen, no exposed sharp bodywork
- Minimum weight by class, verified post-event
- Nitrous is prohibited in every discipline except Drag

**Visual and interior regulations.** The rulebook governs how the car is built, not only how it performs, and this is where a city build is most often rejected:

| Item | Ruling |
|---|---|
| **Boot audio** — subwoofers, amplifiers, screens, display panels | **Prohibited outright.** Classified as unsecured ballast. The boot must be empty or contain only permitted equipment. |
| **Neon** — underglow, wheel-well, interior | Prohibited. No exterior lighting beyond the homologated units. |
| **Body kits** | Permitted only within the dimensional limits for that discipline. A wide-body kit legal in Sprint is illegal in Grip. Overhang, splitter projection and wing dimensions are measured. |
| **Interior trim** | Non-structural trim, upholstery and dashboard dressing must be removed. Only the cage, seat, harness, wheel, pedals and instrumentation remain. |
| **Glass and tint** | Tint above a defined limit is prohibited. Side glass may be replaced with permitted lightweight panels. |
| **Ride height and camber** | Minimum ride height enforced per discipline. Camber is capped. |
| **Livery** | Unrestricted, and the only part of the car's visual identity the festival does not touch. Paint, vinyls, decals and sponsor branding are entirely the team's. |

**A car cannot be part-legal.** Every item is checked, and one breach rejects the whole entry.

**This is not the game punishing customisation.** It is the game drawing a line the protagonist has never had to acknowledge: the thing he made to be looked at and the thing he brings to be measured are not the same object. Most players will end up keeping two Blueprints of the same car (Section 10.6) — the one they built, and the one the rulebook allows.

**Per-discipline regulations:**

| Discipline | Drivetrain | Aspiration | Aero | Tyres | Additional |
|---|---|---|---|---|---|
| **Grip** | Any | Any | Wing and splitter within dimensional limits | Treaded competition tyre, no slicks | Fuel restrictor by class; ride height minimum |
| **Drag** | Any | Any, nitrous permitted | Wheelie bar permitted; front aero unrestricted | Drag radial or slick permitted | Parachute required above a defined trap speed; no traction-limiting electronics |
| **Drift** | **Rear-wheel drive only** — front and all-wheel drive are barred outright | Any | No limits | Any | Angle kit permitted; ABS must be disabled |
| **Speed** | Any | Any | Stability aero mandatory above class power threshold | Speed-rated tyre mandatory | Minimum brake specification enforced |
| **Sprint** | Any | Any | Same dimensional limits as Grip | Treaded competition tyre | Same restrictor rules as Grip |

**Performance classes.** Each discipline runs three competition classes, drawn from the same performance index that governs the city (Section 10.1): a lower class covering C and B, a middle class covering A, and a top class covering S and X. Upgrading a car past a class ceiling moves it up rather than making it dominant in the class below, and detuning to re-enter a lower class is legal here exactly as it is in the city. The player cannot buy their way out of a competitive field.

### 13.3 The Five-Car Requirement

Because regulations are discipline-specific and mutually exclusive, no single car can legally contest all five disciplines.

A drift car is rear-wheel drive with disabled ABS and a steering angle kit — it carries no mandatory stability aero, cannot meet the Speed brake specification, and is unusable at Speed velocities. A drag car runs slicks, nitrous and a wheelie bar, all three of which are prohibited in Grip. A Speed car runs long gearing and heavy stability aero that make it hopeless over a Sprint's corner sequence.

**The player therefore maintains a minimum of five separate cars**, each acquired in the city, each built and tuned specifically for one discipline's rulebook, each legal.

**Teammates bring their own cars.** A recruited driver arrives with the car they raced in the city, and it is their responsibility and their property — the player does not fund it. It must still pass scrutineering for the discipline, which is what the discipline's mechanic is for, and its quality is whatever that NPC's quality is. A Loyal Meridian driver brings a hypercar. A Friendly Dockline driver brings whatever is in his garage.

The player may lend a car from their own garage to a teammate instead, and often should for a discipline where their contact is weak. That car is then unavailable to the player for the whole race date.

This is the festival's real cost. Money earned in the city is not a score — it is the budget for five compliant race cars and ten salaries, and the player will go back to the streets to earn it.

---

## 14. Festival Rank

The festival's progression variable is **Rank**, and it measures driving, not status.

Rank is accumulated separately in each of the five disciplines. **Through the regular season there is no combined Driver Rank** — a driver is ranked five times, once per discipline, and never once overall. The only aggregate figure in the regular season is the Team Standings table (Section 12.4.6), which is a team figure, not a driver figure.

A combined individual table exists only in the championship itself (Section 14.4).

### 14.1 Scoring

Points per event are calculated in two stages:

Every festival event, regardless of format, resolves into a classification of eight. Grip and Sprint classify by finishing order; Speed by trap time; Time Attack and Sector Shootout by lap time; Drag by elimination bracket, where the winner classifies first, the losing finalist second, the losing semi-finalists third and fourth, and so on.

**Drift is scored differently, because of its running order (Section 13.1).** A drift entry's classified position is built from three scores: the driver's own solo run, and the team tandem score, which is awarded identically to both team entries. A protagonist who qualifies brilliantly alone and runs a ragged tandem with a teammate he barely knows classifies below a driver who did both adequately.

**Stage 1 — Base points by classified position:**

| Position | Base Points |
|---|---|
| 1st | 100 |
| 2nd | 80 |
| 3rd | 65 |
| 4th | 50 |
| 5th | 40 |
| 6th | 30 |
| 7th | 20 |
| 8th | 10 |

**Stage 2 — Conduct multiplier:**

| Conduct | Multiplier |
|---|---|
| No contact, no track limits violations | ×1.5 |
| Minor contact or one track limits violation | ×1.2 |
| Repeated contact or repeated track limits violations | ×1.0 |
| Cause a collision that eliminates another competitor | ×0.5 |
| Deliberate ramming, judged by race control | Disqualification, zero points, one-event suspension |

**Result:** finishing position determines how much the player earns; driving conduct determines how much of it they keep.

A clean second place (80 × 1.5 = 120) outscores a dirty first place (100 × 1.0 = 100). The festival rewards the racer who wins without needing to touch anybody — and it makes street habits expensive without ever telling the player to stop being a street racer.

This is also the festival's answer to a Hostile NPC problem the city never solves: in the city, a hostile racer can ram the protagonist at no cost. In the festival, race control is watching, and contact is scored.

### 14.2 Qualification for the Championship

The championship has two entry conditions, identical for every team in the festival:

1. **The driver** must finish the regular season ranked in the top four of all five disciplines.
2. **The team** must finish the regular season inside the top eight of the Team Standings (Section 12.4.6).

This is what makes the championship field small. Most competitors are specialists — a drag driver may top his own ladder and place thirtieth in drift — and a specialist never qualifies no matter how dominant he is in his own discipline. Most teams, likewise, are built around one or two strong disciplines and collapse across the other three.

Failing either condition ends the season. The festival closes without the protagonist, a failure screen is shown, and the player returns to the city.

**The two conditions fail for different reasons, and the game does not conflate them.** Missing the driver condition means he was not good enough. Missing the team condition means the people he brought were not, which is a different sentence and a harder one: it is the game telling him that who he spent five acts becoming friendly with is now a result on a board.

**The player may then re-register for the next festival season.** The city remains fully available: money can be earned, cars built, weak disciplines addressed with purpose-built machines. Re-registration resets festival Rank to zero in all disciplines and begins a new regular season.

The requirement is deliberately total. The city rewards specialisation — a player can dominate the street scene on Ridgeline drift builds alone. The festival refuses that. It demands a driver who is competitive in a grip car, a drag car, a drift car, a speed car and a sprint car, and it is the only place in the game that does.

The protagonist's father was that kind of driver. The festival asks whether the son is.

### 14.3 Two Classifications

The festival keeps two entirely separate tables, and they measure different things.

| | Driver Rank | Team Standings |
|---|---|---|
| **Who it ranks** | Individual drivers | Teams |
| **Structure** | Five separate tables, one per discipline (Section 14) | One combined table across all five disciplines (Section 12.4.6) |
| **What feeds it** | That driver's own classified position and conduct multiplier | Both team entries' points, summed |
| **What it decides in the regular season** | Whether the protagonist meets condition 1 of qualification | Whether his team meets condition 2 |
| **What it decides in the championship** | Who the protagonist faces at the end (Section 15) | Which team wins the festival |

**The two can disagree sharply, and a teammate is where they disagree hardest.**

A **Competitor** teammate maximises his own Driver Rank at the cost of the team — he will not hold a position for anybody, will not give a tow in Speed, and will not sink his own result into a tandem score. A **Wingman** does the reverse: his own table looks unremarkable all season while the team's table quietly climbs, because every rival he sat in front of is a rival who scored less.

Neither is wrong. They are different players to have, and the player chooses which one they need by choosing who to recruit (Section 12.4.2).

### 14.4 The Individual Championship

During the regular season there is no combined Driver Rank — five tables, no overall (Section 14).

**The championship is where an individual overall exists.** Across the five championship rounds (Section 15.1), every qualified driver accumulates championship points into one table. That table is the festival's answer to the question of who the best driver here actually is, and it is the table the game's ending is decided on.

**The protagonist's final opponent is whoever is second in it going into the Circuit Final.**

That is determined by the season the player actually had. It can be a rival from any team. **It can also be his own teammate** — and if that teammate is a Competitor who has been maximising his own result all season while the protagonist did the same, it frequently is.

**This changes nothing about the story.** The narrative requirement is that the team reaches the championship and that the protagonist wins the Circuit Final. Who is in his mirrors on the last lap is not a branch, not an alternate ending, and not a different scene. The dialogue, the staging, the silence on the final lap and the outcome are identical.

What changes is who it is.

A player who recruited a Loyal Wingman spends the final lap with a stranger behind them and a friend somewhere back in fourth. A player who recruited a Loyal Competitor spends it with the one person in the festival who came here because of them, driving flat out to take it away — which is not betrayal, and the game never frames it as betrayal. It is a man who does not lose to people, doing the thing he was always going to do, in the car the protagonist helped him get there in.

**The game does not resolve which of those is the better ending.** It is the last thing the player built, and it arrived without them choosing it.

---

## 15. The Championship

### 15.1 Structure

The championship is a fixed, scripted sequence of five events — one per discipline — contested only by qualified teams.

Each round is entered by two cars per team: the protagonist and his discipline teammate. Both results feed the team championship. Only the protagonist's results feed the individual championship, which is the one the story is about.

The order is fixed and does not vary between playthroughs:

1. **Drag**
2. **Speed**
3. **Drift**
4. **Sprint**
5. **Grip — Circuit Final**

Championship points accumulate across all five. The Circuit Final carries double points, which makes it mathematically decisive regardless of what came before: no accumulated lead is large enough to win the championship without the Circuit Final going the protagonist's way.

The order exists for one reason. **The championship must end on a closed circuit, on a multi-lap race, because that is the kind of race that killed his father.**

### 15.2 The Circuit Final

The Circuit Final is structured to reproduce the specific conditions of the father's death — not the outcome, the conditions.

- **Multi-lap closed circuit**, grandstands full, official timing, marshal posts, race control on the radio.
- The race is designed so that the protagonist arrives at the **final lap in the lead, under pressure, with a car close enough behind to matter.** Field pacing ensures this: a runaway is not permitted to occur, and a large deficit is not permitted to become unrecoverable before the last lap.
- **The car behind is whoever finished second in the individual championship going into this round** (Section 14.4) — a rival from another team, or the protagonist's own teammate. The staging does not change either way.
- The final lap runs with **no commentary, no music, and reduced crowd audio.** Engine, tyres, and the car behind.

The protagonist is in the same position his father was in, in the same kind of race, at the same point in it.

**With one difference, and it is on the radio.** His Grip teammate is on track and his Grip mechanic is on the channel. Neither can win the race for him and the game does not let them. What they do is make it impossible for him to pretend he arrived alone — which is the only thing about this race that is not a repetition of his father's.

His father died in a crewed, team-entered car, surrounded by people. The protagonist spent five acts believing the lesson was to need nobody.

### 15.3 Losing the Final

**The Circuit Final can be lost, and losing it is a designed part of the experience.**

If the player loses the Circuit Final, the failure screen appears. The player returns to the paddock. The race can be re-entered immediately — the championship is not reset, the festival season is not reset, and no progress is lost.

This is intentional and it is the one place where the game's retry loop carries meaning. Every other failure in the game costs something outside the protagonist — money, a car, a season, a place on a board. This one does not. The player fails at the exact thing the protagonist has spent the entire game avoiding, and then does it again.

The game does not comment on this. No dialogue acknowledges the retries. The protagonist simply lines up again.

### 15.4 Winning

He wins on the final lap of a circuit race, from the lead.

His father did not finish that lap. He does.

There is no speech and no montage. The win is the statement.

### 15.5 The Invitation

In the paddock afterwards, the protagonist is approached by a professional GT3 team.

The offer is a real one and it is specific: a seat, a contract, a season, in GT3 — the category his father drove. Purpose-built race cars, works and customer teams, endurance grids, the ladder that ends at a world title.

It is the first time in the protagonist's life that he is offered a car he did not build and does not own, and the first car he will ever drive that was never a road car.

It is not a reward for winning the festival. It is a consequence of it: a driver who placed top four in five disciplines and then won a championship against the people who did the same is exactly the profile a professional team recruits from. The festival is where that recruitment happens, and always was — which is why the professionals in it are there.

**He accepts.**

### 15.6 The Ending

The final sequence is the protagonist arriving at a professional circuit as a contracted driver. Team transporter, garage, crew, race suit, a car he did not build and does not own.

Everything he spent the game surrounded by is gone. No city, no crew, no district, no reputation, no one who knows him. He is at the start of exactly the career his father had, at exactly the level his father started at, with the same thing at the end of it.

The game ends there. It does not show him winning anything. It does not show him in a world championship. It does not promise that it goes well.

**What the ending explicitly does not do:**

- It does not present the streets as a mistake or a phase. Nothing in the final sequence disowns them.
- It does not have him announce that he has healed, moved on, or made peace.
- It does not give him his father's title, or any title.
- It does not close the city. The player returns to a fully open game (Section 16).

The father died with a world championship won on the road and never awarded. The son signs a contract for the first season of a career that might get him to the same place. The game does not say whether it will.

It says that he is going, and that fear is no longer the reason for anything he does.

---

## 16. Post-Championship

After the Circuit Final is won, both halves of the game remain permanently open.

- The city keeps all seven districts, all street events, all police pursuit content, all wager events, and all crew content.
- The festival can be re-entered for new seasons; Rank and Team Standings reset per season, cars and money do not.
- Every NPC the player built a relationship with remains available in both locations, and rosters can be rebuilt season to season.
- No content is locked out by completion.

The player who wants to go back to running from police at Heat 5 in the Docks at three in the morning can do exactly that, forever. Nothing in the game's structure, dialogue or scoring treats that as regression.

The ending sends the protagonist to a professional career. The game does not follow him there, and it does not take the city away from the player to make the point. Both facts are load-bearing: the story is finished, and the world he built is still his.

That is the thesis stated mechanically. The streets were never the wrong answer. The reason he was in them was.

---

## 17. The Blueprint Network — Asynchronous Online

### 17.1 Principle

**Beyond has no competitive multiplayer.** No lobbies, no matchmaking, no real-time races against other players, no ghosts of other players on track, no shared world instances.

Its online layer is asynchronous and cooperative in the *Death Stranding* sense: players are never present in each other's games, but the work they do persists and can be inherited by strangers. Player A builds a car. Player B, playing alone weeks later, downloads that build and races it. They never meet, never speak, and never compete.

The reason this fits **Beyond** specifically: the game is about a solitary protagonist who is good at exactly one thing, building cars, and who spends the entire story unable to ask anyone for help with the thing that is actually wrong with him. The online system does the inverse — it lets players help each other with the only thing that can be handed over.

### 17.2 What Is Shared

Only Blueprints (Section 10.6). Nothing else is transmitted: no save data, no money, no progress, no cars.

A downloaded Blueprint is a **specification, not a car**. It tells the receiving player's game what this build is. It does not grant the chassis and it does not grant the parts.

### 17.3 Applying a Downloaded Blueprint

To apply a Blueprint, the receiving player must:

1. **Own the same chassis.** Blueprints are chassis-locked. A Blueprint for one car cannot be applied to another.
2. **Own or purchase every part it specifies.** The game presents a full parts manifest with a total cost and a single purchase action. Parts already owned are not charged again.
3. **Have the parts unlocked.** Parts gated behind city progression cannot be acquired early by downloading a Blueprint that uses them.

Once applied, the build is fully editable. A downloaded Blueprint is a starting point, not a locked configuration.

**This is the system's central constraint: Blueprints transfer knowledge, never progress.** A new player can download the best drift setup in the game and still has to go and earn the car and the parts. Nothing is skipped. What is skipped is the trial and error of finding out which damper setting works.

### 17.4 Attribution and Lineage

Every Blueprint permanently carries the name of the player who authored it.

When a player sets a personal best, wins a festival event, or takes a district using a downloaded Blueprint, the author's name is displayed alongside the result. If that player then modifies the build and re-uploads it, the new Blueprint credits both: the original author and the editor.

Builds therefore accumulate **lineage** — a visible chain of everyone who touched a setup before it reached the current player. A well-developed drift Blueprint five revisions deep carries five names.

### 17.5 Endorsements

Downloaded Blueprints can be **endorsed** — the game's single unit of player-to-player feedback. There is no rating scale, no downvote, no comments. A player endorses a build or does not.

Endorsements have three effects:

- The author's **Builder Rank** increases.
- The Blueprint appears more frequently in other players' garage feeds.
- The Blueprint is preserved longer in circulation. Builds nobody uses fall out of the feed over time; builds that keep getting used persist indefinitely.

Builder Rank has no effect on the single-player game. It does not grant money, parts, cars, REP or Festival Rank. It is a reputation that exists entirely outside the protagonist's world and entirely between players.

### 17.6 Where Blueprints Appear

Blueprints surface in three places, always optional and never intrusive:

- **Garage feed.** When the player owns a chassis, community Blueprints for it become browsable, filterable by discipline, class legality and endorsement count.
- **Shop terminals.** Independent shops display community builds that use parts they stock.
- **Festival registration.** When the player registers for a discipline, the game offers community Blueprints that are *legal for that specific class and regulation set* — the most practically useful surfacing point in the game, and the one most likely to rescue a player stuck outside the top four in a discipline they are weak at.

### 17.7 Offline

The entire game is playable offline with no feature loss. Blueprints authored offline are queued and uploaded on next connection. No content, event, car, part or ending is gated behind the online layer.

---

## 18. Identity Statement

**Need for Speed: Beyond** is a single-player street racing game with a sanctioned-racing epilogue, not a hybrid of two genres.

It is built on **two car cultures that share a physics model and share nothing else:**

| | City — Underground | Festival — Sanctioned |
|---|---|---|
| **Who races** | Amateurs, self-taught, home-built cars | Professionals and semi-professionals, team support |
| **What a car is for** | Identity, expressed through performance | Winning inside a rulebook |
| **Who writes the rules** | Whoever controls the district | An organising body that does not race |
| **How rules are enforced** | Socially — exclusion, reputation, contact | Scrutineering, timing, penalties, disqualification |
| **What counts as legitimacy** | Recognition by other racers | Position on a classification sheet |
| **Technical limits** | None enforced; crews set house rules for their own events | Per-discipline regulations, per-class indices, scrutineered |
| **Failure costs** | Bail, impound, repair, lost wagers | Penalties, suspension, failing to qualify |
| **Authority available to the player** | Total — districts can be taken and ruled | None — the festival cannot be owned |
| **Entry** | Alone. One driver, one car | By team. Five drivers, five mechanics, all recruited in the city |
| **Simulation** | Arcade. No wear, no fade, damage is visual | Simulated. Wear, temperature, fade, live damage |

- The city is the game. The festival completes it.
- One physics model spans both, so that skill transfers and status does not.
- The street half rewards specialisation, territory and relationships. The sanctioned half rewards breadth, compliance and clean driving.
- The festival supplies nothing. Every car in it was earned on the street, and every person on the team was met there.
- A driver can own the city alone. Nobody enters the festival alone — registration is by team, and the roster is built out of relationships, not money.
- The online layer is asynchronous and cooperative: players hand each other builds, never races.
- Nothing in the game is permanently lost: not cars, not money, not progress, not relationships past repair.

It does not compete with simulation racing. It does not abandon street racing to become *ProStreet*. It takes the street culture that defines the series, and gives the protagonist one place he cannot enter by being the best street racer alive — and then makes him enter it anyway.

**The street is where he found out who he was. The circuit is where he stopped being afraid of it. The contract at the end is the first thing he ever chose without fear choosing it for him.**
