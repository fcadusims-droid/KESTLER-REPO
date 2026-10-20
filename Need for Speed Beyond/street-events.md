---
section: "03 · Systems"
description: "Street event types, wagers, roaming racers and Invitationals."
order: 19
---

# Street Events

REP for every event outcome is listed in [REP changes](reputation.md#rep-changes); Standing effects in [Standing inputs](relationships.md#inputs). Events take as long as they take to drive ([Time](time.md#the-clock)).

## Event types

| Type | Format |
|---|---|
| **Sprint** | Point to point through live city traffic. |
| **Circuit** | Multi-lap loop through public streets, held open by spotters. Unsanctioned. |
| **Drag** | Straight line, manual shifting, launch control, live traffic. |
| **Drift** | Scored run on a designated section: angle, speed, line, duration. |
| **Speed Run** | Highest average speed across a long high-speed route. |
| **Crew Event** | Team format. Aggregate crew position decides the outcome. |
| **Rival Challenge** | One-on-one against a named racer. |
| **Night Meet** | Non-competitive gathering. The player drives in, parks among the others and stays in the car; dialogue, build display, event invitations and spontaneous challenges all happen through the window. [Presentation](cars-and-building.md#presentation) drives NPC reaction. |
| **Wager Event** | Cash or pink slip. See [Wager events](#wager-events). |
| **Roaming challenge** | An impromptu race against a crew member met on the road. See [Roaming racers](#roaming-racers). |
| **Invitational** | An unsolicited one-on-one challenge from one of the city's nine best drivers. See [Invitationals](#invitationals). |

All street events run with live civilian traffic and active police presence unless the controlling crew has arranged otherwise. Which events run in a district, and on what terms, is set by the crew that controls it ([Territorial rule](street-scene.md#territorial-rule)).

## Wager events

Cash wagers unlock at Runner and pink slips at Contender ([Titles](reputation.md#titles)). Player-initiated and optional.

- **Cash wagers.** Both parties stake an agreed sum. The loser pays. No further consequence.
- **Pink slips.** Both parties stake a car. The loser's car transfers to the winner's garage.

**A car lost in a pink slip is never permanently gone.** The NPC who won it drives it, and the protagonist may challenge them to a rematch for it at any time. Winning the rematch returns the car with all installed parts intact.

Taking a car from an NPC costs Standing, which makes pink slips both the fastest way to acquire a rare chassis and the fastest way to drive an NPC toward Hostile. The damage can be rebuilt through dialogue and clean racing like any other, but it is the largest one-shot penalty in the Standing system.

A player with no garage space must choose, before accepting, which car they would give up ([Property](property.md#capacity-is-a-hard-cap)).

## Roaming racers

**Crew members drive around the city.** They are not confined to their home district, not event markers, and not waiting for the player. They commute, cruise, run errands and show off, in their crew's build language, on their own routes, at their own hours. A Meridian member in a Zonda can be idling at a light near the Docks; an Old Guard driver can be caught on the Expressway Ring at 4 a.m. Where a racer is has nothing to do with where their crew rules.

**Challenging.** Pull alongside and flash the headlights. They accept or refuse, and the refusal is not arbitrary:

| Condition | Response |
|---|---|
| Player is below the Plate title ([Titles](reputation.md#titles)) | Refuses — they do not race nobodies |
| Player's car is within one class of theirs | Accepts |
| Player's car is two or more classes below | Refuses, dismissively |
| Player's car is two or more classes above | Refuses, uninterested |
| Standing is Hostile | Always accepts, regardless of class |
| Standing is Loyal | Often refuses, in good humour |
| Recently raced this NPC | Refuses until a cooldown elapses |
| Police pursuit active | Refuses and leaves |

**Format.** A destination is marked somewhere in the city. There is no course, no checkpoints and no route: both cars leave from where they stand and the first to reach the marker wins. Each driver picks their own line through live traffic, so the two cars often do not see each other again until the finish.

**Stakes.** A cash wager, set automatically by the lower of the two cars' classes. Winner takes it. No pink slips and no negotiation — these are impulsive races between strangers at a red light.

| Outcome | Effect |
|---|---|
| Win | Cash wager and REP; Standing unchanged |
| Win with no contact | Cash wager and REP; Standing +1, subject to the two-win ceiling |
| Lose | Wager forfeited |
| Ram the opponent during the race | Standing −1, regardless of result |
| Busted mid-race | Wager forfeited, plus standard [bust consequences](police.md#being-busted) |

Roaming challenges are fast money, not free money: the clock keeps running while the player hunts for one ([Time](time.md)). Police do not schedule these races and do not know they are happening, but they run through live traffic at speed, and a patrol that sees one joins in. A roaming challenge that starts as easy money can end in impound.

**Why they exist.** Roaming racers are the city's fastest source of money and cheapest source of REP. They can be challenged from the first minute of Act 1, but refuse anyone below Plate, so the first 800 REP has to be earned in district events; from then on they are open to the player anywhere in the city. They also teach the class system without a tutorial: a player in a C-class tuner spends Act 1 being refused by cars they cannot yet touch, watches hypercars move through traffic they have no way to challenge, and understands exactly what The Heights is long before they are allowed near it.

## Invitationals

Unlocked at **Name**, with the final two racers appearing at **Headliner** ([Titles](reputation.md#titles)). The player does not find these; they arrive. Once the protagonist is somebody, the city's best drivers contact him directly with an unsolicited one-on-one challenge — the highest-stakes content in the city.

**The roster is finite.** Nine racers issue Invitationals: the seven named crew leaders the game begins with, regardless of who leads their crew later ([Who leads a crew](street-scene.md#who-leads-a-crew)), plus the two unaffiliated drivers, who belong to nobody and are the two hardest opponents in the illegal scene ([Cast](cast.md)). Each can be raced once per act. They are not procedurally generated and do not respawn.

**The terms are fixed and non-negotiable:**

- **Both cars are staked.** The winner takes the loser's car with every installed part.
- **A cash purse on top**, larger than anything else the city pays.
- **The rival's car is disclosed in advance.** The player knows exactly what they are racing and what they would win before accepting.
- **The player nominates their own stake** from their garage, within the class the invitation specifies. A hypercar cannot be entered against a B-class rival to farm cars.

**Declining** is permitted and free the first time, and raises that racer's Standing once. A second refusal from the same racer withdraws the invitation for the rest of the act and costs REP — publicly refusing a challenge twice is a statement, and the city reads it as one.

**Losing** transfers the staked car to the rival. It is recoverable under the pink-slip rule: the rival drives it, and the protagonist can challenge them for it again. But the rematch is another Invitational, on the same terms, against a driver who has just beaten him.

### Formats

Invitationals are **endurance events**: long, unbroken, and covering ground no other event uses.

**Cross-City Sprint.** Point to point, corner to corner of the map, fifteen to twenty-five minutes. The route crosses every district and finishes in the mountains above Ridgeline: dock roads, city grid, expressway, residential boulevards, then a climb that does not stop until the finish. No checkpoints beyond the destination; each driver chooses their own way.

**Ring Circuit.** Three laps of a loop around the entire city, using the Expressway Ring on one side and surface streets on the other. Twenty to twenty-five minutes. The expressway sections are flat-out and the surface sections traffic-choked, demanding opposite setups from the same car.

**Ridgeline Duel.** The mountain roads above the city, on the steepest sustained gradients in the game, in two phases:

1. *The rival leads and the protagonist chases.* Points accumulate the closer he stays without contact; contact scores nothing. Overtaking and holding the lead for ten seconds ends the phase immediately in his favour.
2. *The positions reverse.* The protagonist leads and bleeds points while the rival sits on his bumper. The same ten-second rule applies against him.

Nitrous is disabled for the whole duel. There are no barriers; leaving the road means a long recovery and time the player will not get back. The car will look worse for it, not drive worse ([Damage in the city](driving-and-damage.md#damage-in-the-city)).

### Why they are endurance races

The city is arcade: there is no tyre wear, no brake fade and no performance loss from damage. What makes an Invitational hard is that **nothing resets inside it**.

- **No restarts.** The event runs from green to finish in one piece; quitting forfeits the staked car.
- **Concentration over distance.** Every other city event lasts two to four minutes. An Invitational lasts up to twenty-five, through live traffic, with a car worth more than the player's remaining money on the line. The failure mode is not a bad corner; it is the eleventh minute.
- **Police are live throughout.** A pursuit does not pause the race, heat escalates normally, and the rival does not wait. Being busted forfeits the event and the staked car — the worst single outcome in the city.
- **The route changes character several times.** One setup cannot suit all of it; the player picks which section to be fast in.
- **The opponents are the city's best.** They do not crack under pressure the way crew members do, do not take bad lines, and know the routes.

This is the closest the city gets to what the festival demands: sustained precision over distance with a real consequence for one error. The festival adds wear, temperature, live damage and a rulebook on top — but the habit of holding a race together for twenty-five minutes is learned here, from criminals, in the dark, with the player's own car on the line.

### Outcomes

| Outcome | Effect |
|---|---|
| Win | Rival's car with all parts, cash purse, REP, Standing −2 with that racer |
| Lose | Staked car forfeited, REP loss |
| Busted mid-event | Staked car forfeited, event lost, standard [bust consequences](police.md#being-busted) |
| Decline (first time) | Standing +1 with that racer, once |
| Decline (second time) | Invitation withdrawn for the act, REP loss |

Eight of the nine are people the player could otherwise recruit to a festival team. The consequences are set out in [The Invitational problem](team.md#the-invitational-problem).
