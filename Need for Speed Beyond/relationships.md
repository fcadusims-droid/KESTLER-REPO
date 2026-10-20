# Relationships: Standing and Personality

Every named racer carries two independent values:

- **Standing** — how they feel about the protagonist. It changes.
- **Personality** — who they are regardless of him. It never changes.

Standing is willingness; Personality is capability. Standing never overrides Personality.

## Standing

A per-NPC value on a seven-point scale, from **Hostile (−3)** through **Neutral (0)** to **Loyal (+3)**. Every named racer, crew leader, shop owner and recurring NPC carries their own Standing.

### Inputs

This table is the single source for every Standing change in the game.

| Source | Effect |
|---|---|
| Dialogue choices | The primary driver. Every conversation with a named NPC moves Standing by ±1 or holds it ([Jake's voice](#jakes-voice)). |
| Contact during races | Ramming a specific racer lowers their Standing by 1 per event — including in a roaming challenge, whatever the result. |
| Racing clean against them | Winning without contact raises Standing by 1 — **twice per NPC, and then no more**. |
| Beating them repeatedly | Three consecutive wins against the same racer lower Standing by 1. Humiliation costs. |
| Losing to them | No effect. Losing does not damage relationships. |
| Taking their car in a pink slip | −2 ([Wagers](street-events.md#wager-events)). |
| Winning an Invitational against them | −2 ([Invitationals](street-events.md#invitationals)). |
| Declining their Invitational the first time | +1, once per racer. |
| Being busted in a car they lent | −1 ([Borrowing a car](police.md#borrowing-a-car)). |
| A family member's Standing changing | See [Family ties](#family-ties). |
| Neglect | See [Decay](#decay). |

**Resolving multiple inputs.** Inputs apply in the order they occur and accumulate; the two-win ceiling applies before anything else.

- Three consecutive clean wins against the same racer: +2 from clean racing (the third earns nothing) and −1 from repeated defeat = **net +1**.
- Three consecutive wins *with contact*: −3 from contact and −1 from repeated defeat = **net −4**.

Beating someone fairly builds respect slowly; beating them badly destroys it fast.

### The ceiling on racing

**Racing alone cannot take anyone past Friendly.** Clean wins move an NPC from Neutral to +2 and stop. The last point — the one that separates a competent colleague from someone who will bury their own result for you — comes the first time only from things that are not repeatable:

| Source of the final point | Availability |
|---|---|
| Their crew's storyline, completed ([Crew storylines](../story/crew-storylines.md)) | Once per NPC |
| A dialogue thread across multiple encounters, answered consistently | Once per NPC |
| Helping them with something that costs the protagonist money or a car | Once per NPC |
| Declining their Invitational | Once per racer |

**Reaching Loyal the first time is finite by construction.** No grind produces it, and no NPC can be farmed into it.

**Once reached, Loyal can be regained.** An NPC who has been Loyal once has had their once-per-NPC source spent. If their Standing later falls — through decay, a pink slip, an Invitational — ordinary dialogue can bring them all the way back to Loyal, one conversation at a time. What was earned is never lost for good; what it costs to restore is time spent going back.

### Decay

**Standing decays through neglect.** An NPC the protagonist has not raced, spoken to or done business with drifts one point toward Neutral every fourteen in-game days. Decay stops at Neutral from either side: abandoning someone makes them indifferent, not hostile. NPCs in the district where Jake lives do not decay — he already sees them ([Property](property.md#rent-ownership-and-location)).

Decay applies to shop owners exactly as to racers, so credit terms erode when the player stops using a shop.

**This is the consequence the game is about.** A player cannot keep every relationship in the city, because keeping one means going back, and time spent going back is time not spent elsewhere ([Time](time.md)). By Act 5 the roster is not a list of everyone the player was nice to. It is a list of who they kept.

### Family ties

Crew leaders and their district's mechanic are family ([Families](../story/cast.md#families)), and what Jake does to one reaches the other:

- **A pink slip or an Invitational win** against one family member (−2) moves the other **one point down**.
- **Completing a family's crew storyline** moves the related family member **one point up**.
- **A family tie never takes anyone to Loyal.** Upward spill stops at Friendly; the last point still has to be earned with that person directly, the first time.
- **Nothing else spills.** An ordinary conversation, a clean win, contact or a decay step stays between Jake and that one person.

### Outputs

| Standing | On track | Off track |
|---|---|---|
| **Hostile (−3)** | Actively blocks, brake-checks, forces contact; will crash themselves to stop the player | Insults, refuses information, and calls in the player's location: pursuits in that NPC's home district start one heat level higher while Standing stays Hostile ([Heat](police.md#heat)) |
| **Unfriendly (−2 to −1)** | Defends aggressively, closes doors, no quarter | Curt; withholds event invitations |
| **Neutral (0)** | Races to win, clean by default | Transactional |
| **Friendly (+1 to +2)** | Races hard but clean, gives room in ambiguous situations | Shares event locations, warns of police patrols |
| **Loyal (+3)** | Will work *for* the player in team events, as far as their Personality allows | Lends a car when Jake's is impounded ([Borrowing a car](police.md#borrowing-a-car)); sells parts at cost |

**Friendly and Loyal NPCs are the only people who can be recruited onto a festival team** ([Team](../festival/team.md#recruitment)). Every relationship built in the city is a potential seat on that roster.

## Jake's voice

**Jake starts quiet.** He was never much of a talker, he arrived in Nitroit having told no one anything true about himself, and his early dialogue shows it: short answers, deflections, silences the other person has to fill.

**He opens up as he gets to know people.** The range of what the player can have him say grows with the number of people Jake is close to:

| People at Friendly or better | What his dialogue options become |
|---|---|
| **0–2** | Short and guarded. He answers questions and asks almost none. |
| **3–5** | He asks back, jokes, admits small things — about cars, about the city. |
| **6–9** | He talks about himself: where he has been, what he likes, what he will not do. |
| **10 or more** | He says what he thinks, unprompted, and argues when he disagrees. |

The player always chooses among responses written in Jake's voice. Every option is something Jake would say; none is cruel for its own sake, and none breaks the two things he never says in Nitroit:

- **His surname.** Nobody in Nitroit learns that he is John Spaid's son ([The name](../story/campaign.md#the-name)).
- **What the account is.** He mentions the inherited money twice in the whole game, both times without saying what it is or how much ([The money](../story/backstory.md#the-money)).

The growth is one-way. A relationship lost later does not shut him back up; it only means fewer people to talk to.

## Shops and credit

Each independent shop carries its own Standing, built by using that shop for real work. It sets credit terms:

| Shop Standing | Credit terms |
|---|---|
| Hostile / Unfriendly | Cash only. No credit under any circumstance. |
| Neutral | Credit at high interest. |
| Friendly | Credit at low interest. |
| Loyal | Credit at zero interest, repayable at the player's discretion. |

Credit applies to parts, repairs, labour, bail and impound fees alike. Outstanding debt accrues interest per in-game week and is deducted automatically from race winnings until cleared.

A player deep in debt to a high-interest shop is functionally forced to keep racing — thematically exact and mechanically real.

Shop Standing also decides which mechanics will join a festival team ([Mechanics](../festival/mechanics.md)).

## Personality

Every named **racer** carries one of six personalities. It never changes, cannot be influenced, and is not a stat the player can improve. It decides how that racer drives when the result is in doubt — in the city and, far more consequentially, in the festival.

Mechanics and shop owners are outside this system. They have personalities, but those live in dialogue and touch no number ([Mechanics](../festival/mechanics.md#mechanic-personality)).

| Personality | On track |
|---|---|
| **Competitor** | Cannot stand losing to anybody, including people on his own side. Races teammates exactly as hard as rivals, never yields a position, never lifts. |
| **Wingman** | Reads the race as a position to hold rather than a place to gain. Exceptional at defending, mediocre at attacking; will sit on a rival's nose for an entire event to keep them behind. |
| **Metronome** | Does the same lap every lap. Rarely brilliant, effectively never wrong. Does not crash, make contact or take risks. |
| **Spike** | Enormous variance. Capable of beating anyone on his day, and of putting it in the wall at the first corner. |
| **Technician** | Fastest alone, against a clock, with time to build into it. Strong in timed formats, uncomfortable wheel to wheel, loses positions under close pressure. |
| **Brawler** | Fast and physical. Leans on people, uses contact as a tool, gains places nobody else could — and collects penalties doing it. |

**The two axes do not substitute for each other:**

- A **Loyal Competitor** would do anything for the protagonist except lose to him.
- A **Friendly Wingman** will defend his position for a whole race to keep a rival off the protagonist — not out of affection, but because that is what he does.
- A **Loyal Brawler** wrecking a rival for the protagonist's benefit still incurs the conduct penalty, and the team still pays for it ([Scoring](../festival/rank-and-championship.md#scoring)).
- A **Hostile Metronome** is harmless. He will not touch the protagonist; he will simply be in front of him.

**Personality is visible in the city before it matters.** Racing someone on the street shows who defends, who lifts, who leans, who is quick alone and soft in traffic. Recruitment is therefore an informed decision, and a player who never raced anyone outside their own district is choosing a roster blind. How each personality behaves in each festival discipline is in [Disciplines](../festival/disciplines.md#running-order).
