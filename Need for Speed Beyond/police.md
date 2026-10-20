---
section: "03 · Systems"
description: "Heat and starting heat, fines, impound, auctions, borrowing a car, and the police List."
order: 18
---

# Police

Police exist only in Nitroit. Revada has none ([Revada](revada.md#not-an-open-world)).

## Heat

Heat is a five-level pursuit-intensity value. It rises during a pursuit and decays when the player is out of police contact.

| Heat | Response |
|---|---|
| **1** | Single patrol unit. Basic pursuit. |
| **2** | Multiple patrol units. Coordinated blocking. |
| **3** | Undercover units, spike strips, radio coordination. |
| **4** | Highway interceptors, roadblocks, helicopter spotting. |
| **5** | Citywide alert, heavy interceptors, rolling roadblocks, sustained air support. |

### Starting heat

Every pursuit starts at Heat 1 plus these modifiers, which add together:

| Modifier | Effect | How it goes away |
|---|---|---|
| **Recent pursuits in this district** | +1 for each pursuit in the same district in the last seven in-game days, to a maximum of +2 | Drops by 1 for every three in-game days without a pursuit in that district |
| **Marked title** | +1, everywhere ([Titles](reputation.md#titles)) | Never — it is permanent |
| **A Hostile NPC from this district** | +1 in that district, however many Hostile NPCs live there ([Outputs](relationships.md#outputs)) | When no NPC from the district is Hostile any more |

**Starting heat is capped at 4.** Heat 5 is only ever reached during a pursuit. The List decides what the units are driving, not where heat starts ([The List](#the-list)).

## Being busted

**The player is never permanently arrested.** There is no game-over state, no jail sequence, and no lost save progress. When busted:

1. A failure screen is shown.
2. REP is lost ([REP changes](reputation.md#rep-changes)).
3. **The state issues a fine**, and Jake pays it himself. The fine has two parts, shown separately:
   - **Bail**, scaling with heat level at the moment of capture — modest at Heat 1, severe at Heat 5.
   - **The impound fee**, scaling with the car's total value: base market value plus the cumulative value of every installed performance and visual part. A heavily built flagship costs dramatically more than a stock entry-level chassis.
4. **If Jake can pay on the spot**, in cash or on shop credit ([Shops and credit](relationships.md#shops-and-credit)), he pays and keeps the car.
5. **If he cannot**, the car is taken to the impound lot.

## Impound

An impounded car stays in the impound lot until its fine is paid. It is not damaged, does not expire, and accrues nothing while it waits.

The player may hold several cars in impound at once and reclaim them in any order, provided there is space for them ([Property](property.md#capacity-is-a-hard-cap)). A reclaimed car is collected by driving to the lot in another vehicle and driving the reclaimed one out.

**This is where the system has teeth.** The punishment for reckless driving with police present is economic and escalating, and scales with how much the player has invested in the car they were caught in. Driving the best car in the garage during high heat is the highest-risk decision available in the city.

### When Jake has nothing else to drive

If Jake's car is impounded and he has no other car he can drive — every other car he owns is impounded too, or he owns no other — he has one way out before the state acts:

- **Borrow a car from a Loyal friend** ([Borrowing a car](#borrowing-a-car)).

If no friend is Loyal, **the state auctions the impounded car at once** to settle the fine. The proceeds pay the fine, and whatever is left over is Jake's. The state never leaves him with less than the price of the cheapest car on the Halvorsen Motors lot; any part of the fine beyond that is written off. The screen transitions to the lot, where he buys something simpler and starts again.

**An auctioned car is gone for good.** It is the only way in the game to lose a car permanently, and it only happens to a player who is out of money, out of credit, out of cars and out of friends at the same moment.

### Borrowing a car

A Loyal racer can lend Jake a car while one of his is impounded. The option is a phone call, made from the car's menu.

- The loan is **that friend's own street car**, as they built it.
- It stays with Jake **until one of his impounded cars is released**, then goes back to its owner.
- **It is not his.** It cannot be modified beyond tuning values, staked in a wager or Invitational, sold, or entered in the festival. It takes no garage space.
- **If Jake is busted in it**, the car goes straight back to its owner, the fine is added to what he already owes the state, and that friend's Standing drops by 1 ([Inputs](relationships.md#inputs)).

A borrowed car is not a gift; the game still never gives Jake a car ([What the purchase establishes](campaign.md#what-the-purchase-establishes)).

## The List

**The police keep their own ranking, and it does not care what the scene thinks.**

Running from the police accumulates a **bounty** — a score, not a sum of money. Once the protagonist reaches **Marked**, the department adds him to an internal list of the twenty street racers it most wants off the road, ordered by bounty, not ability.

### What raises the bounty

| Action | Bounty |
|---|---|
| Disabling or wrecking a police vehicle | The largest single source in the game |
| Escaping a pursuit | Scales with the heat level at the moment of escape |
| Sustaining a pursuit past a duration threshold | Moderate, per threshold crossed |
| Causing civilian collisions during a pursuit | Moderate |
| Being busted | Raises it. Being caught is evidence, not absolution. |

**Bounty never decreases.** There is no cooling off, no lying low, no paying it down. The List is the one number in the game that only goes up.

### What position does

Every position gained upgrades the fleet the department sends.

| Position | What they send |
|---|---|
| **#20 – #17** | Standard patrol sedans. Slow, numerous, easy to lose. |
| **#16 – #13** | Uprated patrol cars and the first unmarked units. |
| **#12 – #9** | Pursuit-tuned sedans, coordinated boxing, spike strips as standard. |
| **#8 – #5** | High-performance interceptors, faster than anything in the player's garage below S class. |
| **#4 – #2** | A dedicated pursuit unit in cars built for nothing else, driven by people who do nothing else. Helicopter on station rather than called. |
| **#1** | All of the above, deployed from the first heat level, in every district, permanently. |

The List runs on top of Heat rather than replacing it. **Heat decides how many units come and how hard they try. The List decides what they are driving.**

**The escalation is permanent.** A player who spends Act 2 wrecking police cars for the bounty spends Acts 3, 4 and 5 being chased by the fleet Act 2 bought them.

### Why players climb it anyway

Bounty is not money. Nobody pays it to Jake and he never pays it: it is a score the department keeps on him. The money in police encounters only ever flows one way — from Jake to the state, as fines.

What a pursuit gives back is REP: escaping pays more the higher the heat ([REP changes](reputation.md#rep-changes)), and escaping is one of the few ways to earn REP without winning a race.

**So the List is a bargain the player strikes without ever being asked.** Every pursuit turned into a demolition derby buys reputation tonight and a harder city forever. Nobody warns them. Most players first notice on the night the car that has been catching them all game is no longer the fastest thing in the mirror.

### What it never does

Reaching **#1** unlocks nothing: no reward, no acknowledgement in dialogue, no congratulating NPC, no scene. It is not a goal, and the game never presents it as one.

**The scene's ranking and the police ranking disagree on purpose.** A player who races constantly and rarely runs can reach King of the Streets while sitting at #18, in a city that still sends sedans. A player who spends half their nights at Heat 5 can be #1 at Contender, hunted by interceptors, having won nothing.

The scene's title is what he built. The List is what it cost.
