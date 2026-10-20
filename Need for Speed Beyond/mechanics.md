# Mechanics

The mechanic is the most important non-driving relationship in the game, and in the festival he is worth more than the teammate.

**A driver can only be as good as the car allows. In the city, the player decides what the car is. In the festival, the mechanic does** — because the mechanic knows where the rulebook has room in it.

A team registers five mechanics, one assigned to each discipline, recruited from shops through shop Standing ([Recruitment](team.md#recruitment)). The named mechanics are listed in [Cast](../story/cast.md#shops-and-mechanics).

## Expertise

Every mechanic has an **Expertise rating from 1 to 5**, inherited from their shop and raised by the player's Standing with them. Expertise sets the baseline: how good the car is before the player touches anything.

| Function | Effect |
|---|---|
| **Baseline setup** | The car's starting tune for that track. A 1-Expertise mechanic hands over something generic; a 5 hands over something already close to optimal. |
| **Scrutineering** | Catches regulation breaches before registration. A weak mechanic misses things and the car is rejected at the gate; a strong one flags the problem and proposes the fix ([Regulations](regulations.md)). |
| **Repair between rounds** | Faster and cheaper repair of damage carried out of an event. At Expertise 5, repairs are free. |
| **Tyre strategy** | Chooses compound, pressure and starting temperature for the conditions — a festival-only concern, since the city does not simulate wear ([Simulation layer](../systems/driving-and-damage.md#the-simulation-layer)). |

**What a mechanic's level means for a season:**

| Expertise | A season with him |
|---|---|
| **1** | Generic setups, missed breaches, expensive repairs, no Insights. The car is legal and nothing more. |
| **3** | Competent baseline, catches most breaches, some Insights at Friendly. Competitive, never advantaged. |
| **5** | Near-optimal baseline, never fails scrutineering, free repairs, full Insight access at Loyal. The car is better than its specification suggests. |

A player with a weak drift mechanic shows up with a car that is legal, prepared, and half a second off — every round, all season.

## Specialisation

**Every mechanic can work on any car, in any discipline.** Each is also a **specialist in one discipline**, and that is where their work goes past competent.

| Assigned to… | Effect |
|---|---|
| **Their specialist discipline** | Expertise counts one level higher (to a maximum of 5), and their Insights apply. |
| **Any other discipline** | Base Expertise, and no Insights. The car is prepared, legal and repaired, and nothing more. |

A mechanic's specialist discipline comes from the shop and the culture they work in, and does not change. A drag specialist can make a drag car better than anyone else on the team can — which matters when the Drag ladder has a hard rival — but that knowledge does nothing for a Sprint car. To get the same edge in Sprint, the team needs a Sprint specialist.

**Assignment is a real decision.** Six shops can supply a mechanic, two of them Sprint specialists, and a team needs five. A player missing the specialist for one discipline can still register by putting another mechanic there, at base Expertise and without Insights — a legal season, half a second off in that discipline.

Each mechanic also has a **craft**: the area their Insights tend to come from — engine, aero, chassis, rubber, or the rulebook itself. Craft shapes what the mechanic talks about in the build dialogue and touches no number.

## Insights

**This is what separates a good mechanic from a great one.**

Every mechanic holds a personal set of **Insights**: specific, legal, non-obvious optimisations they know and most of the paddock does not. An Insight is never a cheat and never a grey area; it is a place where the regulations permit something the field has not thought to do. Examples of the form:

- Minimum ride height is measured at the front axle only, so rake is free.
- The permitted treaded tyre has a compound that comes up to temperature a full lap earlier than the one everybody runs — worth more over three laps than anything else on the car.
- A splitter cut to the inner edge of the dimensional limit rather than the outer loses almost no downforce and sheds real drag.
- Minimum weight is a total, not a distribution, so where the remaining mass sits is entirely the team's business.
- The Drift rulebook caps camber but says nothing about the steering arm, so the angle available is not the angle most people run.

None would embarrass anyone if the scrutineer read it aloud. They are places where a short rulebook is silent and most of the field assumed it was not.

**How Insights become available.** They are not bought and not unlocked by progression. They open as Standing with that mechanic rises: a Neutral mechanic prepares the car, a Friendly one starts thinking out loud, a Loyal one tells the player everything he knows. Expertise is what he can do; Insights are what he will share. Insights only ever apply to the mechanic's specialist discipline.

## The build dialogue

Insights are delivered as **dialogue in the build screen**, while the player works on the car.

The mechanic is present. He watches what the player installs and comments — unprompted, in character, about the part currently selected. The player can act on it or ignore it. The register is a working mechanic talking to someone he is building a car with:

> *"They measure ride height at the front axle. Only the front axle. Lift the back two millimetres and you've got rake for free, and it's legal, and I've never seen anyone in this class do it."*

> *"Don't. That kit's four millimetres over on the splitter. It'll pass a glance and fail the gauge, and they check the gauge."*

> *"You're on the hard compound because everyone's on the hard compound. On this surface the soft goes off two laps early and gains you half a second for eight. Your call."*

**Nothing in the build dialogue is mandatory, and nothing is a quest marker.** The mechanic has no objectives, does not track whether the player listened, and does not repeat himself. He says his piece once per part and goes back to work.

A player who ignores their mechanic can still win the festival — in a car that is legal, prepared, and slower than it needed to be, against teams whose mechanics were listened to.

## Mechanic personality

**Mechanics do not use the racer Personality system** ([Personality](../systems/relationships.md#personality)). They never take a start, so there is no on-track behaviour for a personality to govern.

They have personalities anyway, expressed entirely in dialogue: the one who explains everything twice, the one who says four words a session, the one who is openly contemptuous of the festival and does the work perfectly regardless, the one who will not stop talking about a car he built in 2009, the one who used to race. None of it touches a number; all of it is why the player remembers which one they took.

A Loyal mechanic at Expertise 5 is the most constant presence in the Epilogue — there for every build, every registration, every repair and every radio call, including the last one ([The Circuit Final](rank-and-championship.md#the-circuit-final)).
