---
section: "07 · Feasibility"
description: "Costs, revenue, cases, break-even, population, verdict"
order: 34
---

# The Business Case

*This document is the business case for the Service documents: what Resident Evil Online costs to build and run, what it earns, and what happens if it earns less. Every figure carries a label: **[P]** Public Data, **[E]** Industry Estimate, **[A]** Model Assumption. Dollars are US dollars, converted at ¥150 to the dollar [A].*

## The Answer

**Only as a bet on a hit.** As the Service documents now describe it, with the whole of Raccoon City rebuilt for the launch, Resident Evil Online costs about $205M before launch. At that cost it does not pay for itself in the Base case: it ends about $110M short. It pays for itself if the First Run sells about 12 million copies, and it makes about $105M if it becomes a hit. The model still holds together, and three things still make it hold:

- **The price pays for the game.** A US$29.99 First Run brings in most of the money.
- **Cosmetics pay for the service.** The Wardrobe, Patron, and early access keep the online game running after the Opening.
- **The rules cap the loss.** Promise 14 and `offline-and-ownership.md` keep a failure from becoming a slow drain.

A free-to-play launch with the same player-friendly rules would not work: at $8 a year per player it would need about 9 million monthly players just to run at full size, and about 18 million to also repay its cost within five years [A].

## Anchors

| Fact | Figure | Label |
|---|---|---|
| Capcom net sales, FY ended March 2026 | ¥195.3 billion (≈ $1.30 billion) | P |
| Capcom Digital Contents operating margin, same year | 48.9% | P |
| Capcom development investment, same year / plan for FY ending March 2027 | ¥54.8 billion (≈ $365M) / ¥62.9 billion (≈ $419M) | P |
| Capcom average annual salary | ¥9.18 million (≈ $61,000) | P |
| Loaded cost per Capcom developer, salary plus overhead | ≈ $100,000 a year | E |
| *Resident Evil Requiem*, first fiscal year | 6.91 million units | P |
| *Helldivers 2*, a US$40 online game | 20 million copies, more than $700M gross | E |
| *Fall Guys*, after going free in June 2022 | 50 million players within two weeks | P |
| Peak Steam players of Capcom's online spin-offs | *Resistance* 4,181 · *Re:Verse* 2,080 · *Exoprimal* 4,522 | P |
| Platform fees | Steam 30% / 25% above $10M / 20% above $50M; consoles about 30% | P (Steam) · E (consoles) |
| Server cost, 100-player battle royale on AWS GameLift, 100,000 peak players | $165,000 a month on demand, $105,000 optimized | P |
| Proximity voice middleware (4Players ODIN), price per peak concurrent user a month | €0.29, falling to €0.19 above 80,000 | P |
| Capcom's RE Engine department / REX | About 200 engineers, 160 on the engine; REX, detailed October 2026, evolves the RE Engine step by step | P |
| *Resident Evil 2* (2019), people involved | More than 800, Capcom's figure during development | P |
| *Resident Evil Requiem*, in-house staff | About 150 to 200, by its director, plus R&D and technical art | P |
| A newly greenlit AAA game, development alone | About $200M or more, against $50–150M five years earlier | E (CMA, 2023) |
| *ARC Raiders*, a US$40 extraction game (Embark) | About $75M including marketing, about 70 people, three years; more than 16 million copies in about six and a half months | E (cost) · P (sales) |
| *Concord* (Sony), a live-service shooter shut down two weeks after launch | Reported at about $400M | E |

## 1 · Building It

The launch is still smaller than the whole design (`seasons-and-new-content.md`): Survivor on one world, the Raccoon City of 1998. But that one world is now the whole city, rebuilt as a new remake, with what the remakes of *Resident Evil 2* and *3* made reused wherever the city holds it (`presentation-and-technology.md`, Raccoon City, Rebuilt Whole). It is lit for every hour and every weather, and Survivor carries more systems than before: safe rooms, stashes, vehicles, worn inventory, proximity voice carried by the city's acoustics, and Hardening, whose every stage is captured in motion (`survivors.md`). The world is also a story night (`story-nights.md`), costed as its own line.

| Component | Low | Realistic | High |
|---|---|---|---|
| Core team (average headcount × years × $100k) | 160 × 3.5 = $56M | 200 × 4 = $80M | 250 × 4.5 = $112.5M |
| The city: outsourced environment art for every district no remake built, and the rework of every reused one for scale, hours, and weather | $22M | $32M | $48M |
| Technology, backend, networking: a 100-survivor server running the dead and the director | $15M | $20M | $28M |
| Motion capture and animation: Hardening's two bodies, vehicles, the dead | $4M | $6M | $9M |
| Voice and acoustics: proximity voice through the city's sound, and reading a whisper from a shout | $3M | $5M | $8M |
| The Echo system (`presentation-and-technology.md`) | $4M | $6M | $10M |
| The story night: live scenes and their branches, Moments, ΜΝΗΜΗ's voices, and the as-recorded bodies (`story-nights.md` and `presentation-and-technology.md`) | $6M | $10M | $16M |
| QA, load tests, betas | $6M | $10M | $14M |
| **Build cost** | **$116M** | **$169M** | **$245.5M** |
| Launch marketing | $20M | $30M | $40M |
| Launch preparation | $4M | $6M | $8M |
| **Total before launch** | **$140M** | **$205M** | **$293.5M** |

All [A], with the head cost from Capcom's own pay [E]. The Realistic core team sits at *Requiem*'s in-house size [P], held for four years, with the city's art outsourced as Capcom outsourced much of *Resident Evil 2*'s 800 [P]. The Realistic build is about $42M a year over four years, about 10% of Capcom's planned yearly development investment [E]; the total before launch is about half of one year's [E]. It is in line with what a newly greenlit AAA game costs [E], nearly three times what *ARC Raiders* is reported to have cost [E], and half of what *Concord* is reported to have lost [E].

**What changed since the earlier estimate.** The earlier launch, $131M Realistic, was Survivor built on the pieces of Raccoon City the remakes already held, with four Outbreak scenarios and Mercenaries beside it. Those modes are gone from the launch (`future-development.md`), which saves about $20M [A]. Rebuilding the whole city, lighting it for every hour and weather, and adding the new systems cost about $95M more [A]. The city is the difference.

**How long.** About four years from the first gate's funding to launch in the Realistic case: three and a half if the city's reuse goes further than planned, four and a half if it does not [A]. A project begun in 2027 launches about 2031, on the RE Engine as REX changes it underneath (`presentation-and-technology.md`, Engine and Platforms).

## 2 · Running It

Promise 14 makes the operating budget a set of tiers, not a fixed cost. Each year the service runs at the highest tier its earnings can pay for.

| Tier | Live team | Content | Backend | Support | Moderation | Anti-cheat | QA | Marketing | Localization | **Total, before servers** |
|---|---|---|---|---|---|---|---|---|---|---|
| **Full** | 80 heads, $8.0M | $14M | $3M | $2.5M | $1.5M | $2M | $2.5M | $6M | $1M | **$40.5M** |
| **Standard** | 50 heads, $5.0M | $6M | $2.5M | $1.8M | $1.0M | $1.5M | $1.5M | $3M | $0.7M | **$23.0M** |
| **Lean** | 25 heads, $2.5M | $2.5M | $2M | $1.2M | $0.7M | $1.0M | $0.8M | $1M | $0.3M | **$12.0M** |
| **Keep-alive** | 15 heads, $1.5M | $0.5M | $1.5M | $0.8M | $0.5M | $0.8M | $0.4M | none | $0.2M | **$6.2M** |

All [A]. The Full tier's content budget pays for the second year's arrivals: the Ruins, made from the rebuilt 1998 city and what *Requiem* made of it, at about $12M, and the anomaly library, its limits, and its testing at about $6M, spread over the First Run's two years with the seasons (`seasons-and-new-content.md`, The Order of Arrival).

Servers are added on top at **$2.00 per peak concurrent player per month** [A], and proximity voice at **$0.25** [P, from ODIN's volume prices]. Servers sit above the AWS battle-royale example because each Survivor server also runs the dead and the director, but below a full-size city, because the worlds are built to the scale of the records (`worlds.md`). With peak players at 4% of monthly players [A], servers and voice cost **about $1.08 per monthly player per year**.

**The Valley is not in any tier.** Rebuilt from the remake of *Resident Evil 4*, with its own story night, it costs about $30–45M [A], more than any tier's content budget. It is built only if the First Run sells more than 6 million copies in its first year, on course for the Hit case, and is paid for from that year's earnings. In the Base case it is not built.

Below Keep-alive, the online service ends and the game goes offline under `offline-and-ownership.md`.

## 3 · What It Earns

- **The First Run:** about **$20 net per copy**, blending $29.99 and the $49.99 Founder's Edition after regional prices, discounts, and platform fees [A].
- **The Wardrobe, Patron, and early access**, gross per monthly player per year [A]:

| | First Run, owners | After the Opening, free |
|---|---|---|
| Conservative | $8 | $5 |
| Base | $12 | $8 |
| Hit | $15 | $10 |

Owners spend more than free players because they already chose to pay. The figures stay modest because every look can be earned, nothing leaves, and nothing creates urgency: those rules cost revenue, and the model counts that cost.

## 4 · Three Cases

| | Conservative | Base | Hit |
|---|---|---|---|
| Copies sold in the First Run | 2.5M | 7M | 14M |
| Monthly players in the first free year | 1.5M | 3.5M | 7M |
| Decline of free players each year | 20% | 20% | 20% |
| Years the online service runs | 2 | 7 | 10 or more |
| **Result over the whole online life, after building it** | **−$217M** | **−$110M** | **+$105M** |
| Year the project has repaid itself | never | never, about $110M short | year 2 |

All [A]. The copy assumptions are anchored to *Requiem*'s first year at full price [P], *Helldivers 2* at $40 [E], and *ARC Raiders* at $40 [P], and the Base case is lower than all three. The Conservative loss is the loss of a project that launches; one stopped at the second gate loses about $120M (Capcom's Decision, below).

The Base case, year by year:

| Year | Copies | Monthly players | Net revenue | Tier | Result | Running total |
|---|---|---|---|---|---|---|
| 1 | 4.2M | 1.3M | $95M | Full | +$53M | −$152M |
| 2 | 2.8M | 2.2M | $75M | Full | +$32M | −$120M |
| 3 (Opening) | free | 3.5M | $20M | Lean | +$4M | −$116M |
| 4 | free | 2.8M | $16M | Lean | +$1M | −$116M |
| 5 | free | 2.2M | $12M | Keep-alive | +$4M | −$112M |
| 6 | free | 1.8M | $10M | Keep-alive | +$2M | −$110M |
| 7 | free | 1.4M | $8M | Keep-alive | about $0 | −$110M |
| 8 | | | | Offline | | |

All [A]. The First Run carries the project, and after the Opening the service pays for itself at a smaller size, but never earns back the build. In the Conservative case the free game cannot pay even for Keep-alive, so the Opening and the move offline come together (`offline-and-ownership.md`).

## 5 · Break-Even

| First Run copies | Result over the online life, Realistic costs |
|---|---|
| 7M | −$110M |
| 9M | −$64M |
| 11M | −$18M |
| 12M | about break-even |
| 14M, the Hit case | +$105M |

**The project breaks even at about 12 million First Run copies** [A]: more than *Requiem* sold in its first year at full price [P], and fewer than *ARC Raiders* sold at $40 in half a year [P].

After the Opening, each tier needs this many monthly players at the Base case's $8 a year [A]:

| Tier | Monthly players needed |
|---|---|
| Keep-alive | 1.4M |
| Lean | 2.7M |
| Standard | 5.1M |
| Full | 9.0M |

The free game sustains a modest service, not a large one. New places after the Opening arrive only as fast as those tiers allow.

## 6 · Population

Survivor matches in two kinds of night, Solo and Squad, and three regions: six queues at launch (`presentation-and-technology.md`). When the Ruins arrive, each sleeper's choice between the classic rotation and the Ruins doubles that to twelve. A queue fills a 64-survivor night in 90 seconds if about 1,900 players are in it at once, assuming each spends about 45 minutes in a night before queuing again [A]. Echoes filling up to a quarter of a night lower that to about 1,450 [A].

| | Peak players needed | Monthly players |
|---|---|---|
| Six queues, players only | ≈ 28,500 | ≈ 0.7M |
| Six queues, with Echoes filling up to a quarter | ≈ 21,750 | ≈ 0.54M |
| Twelve queues, players only | ≈ 57,000 | ≈ 1.4M |
| Twelve queues, with Echoes filling up to a quarter | ≈ 43,500 | ≈ 1.1M |

All [A], with off-peak taken as 40% of peak, peak players at 4% of monthly players, and all play in Survivor. The Base case clears the six-queue threshold from the first year, with about 50,000 peak players, and the twelve-queue threshold once the Ruins arrive, with about 88,000 in the second year and about 140,000 after the Opening. The Conservative case does not: about 18,000 in the first year, across all platforms. Capcom's online spin-offs peaked at 2,000 to 4,500 on Steam alone [P]. These are the figures for a hard split. The lobby's choice is softer than that (`presentation-and-technology.md`, Matchmaking): a player can tick both maps, and one who waits four minutes is offered the other, so the twelve queues behave like fewer when the population is thin. When Echo fill is not enough, queues merge regions and nights start at forty.

## 7 · Capcom's Decision

- **Fit:** $205M is more than Capcom has put into any online spin-off, and about what it puts into a mainline game [A]. It is built on a city it already owns half of and sold the way Capcom sells what works: a paid game with free updates and cosmetics, like *Street Fighter 6* and *Monster Hunter* [P].
- **Gates:** two gates cap the Conservative loss before it is spent. The first is a playable slice of Survivor, tested with outside players at about $25M spent: one district of the rebuilt city at two hours and two weathers, with proximity voice reading whispers from shouts, and Hardening's first and last stages. The second is a closed beta of the whole city, at about $120M spent, judged on whether players come back and on peak concurrency. A project that fails the second gate stops there.
- **Fallback:** if the first gate shows the story night costs more than its line, the launch can ship Late Nights in its place (`story-nights.md`), at roughly half that line's cost [A].
- **The city is the lever.** Every district the remakes already built that can be reused instead of rebuilt lowers the largest new line. If the first gate shows that reuse goes as far as the Low case, the project costs about $140M and breaks even near 9 million copies [A].
- **Franchise:** most of the units Capcom sells each year are catalog titles, not new releases [P], and Resident Evil is the largest part of that catalog. A free Resident Evil game set in the places of *Resident Evil 2*, *3*, *4*, and *Requiem* sends players to those games. The model does not count that value. It is a reason to fund the project, not a reason it pays.

## 8 · Verdict

**ONLY AS A BET ON A HIT.** The Base case loses about $110M. The project is worth funding only if Capcom believes the First Run can sell about 12 million copies, or the first gate brings the city's cost down toward the Low case.

**The five numbers that matter**

1. **$205M** realistic cost before launch, about 10% of Capcom's yearly development investment for four years [A].
2. **12 million** First Run copies to break even over the online life [A].
3. **$20** net per First Run copy, against **$8** a year per free player after the Opening [A].
4. **2.7 million** monthly free players to keep a Lean service running after the Opening, 1.4 million for Keep-alive [A].
5. **21,750** peak players for healthy Survivor queues with Echo fill at launch, and **43,500** once the Ruins arrive [A].

**The three biggest financial risks**

1. **A First Run that sells like a good Resident Evil, not like a hit.** Below about 12 million copies, the project does not recover its cost; at 7 million it loses about $110M. Everything rests on Survivor being good enough to sell like *ARC Raiders* did.
2. **The free phase earns little per player.** Earnable looks, no urgency, and no currency for sale keep revenue per free player low. The free game must stay large to run more than a small service.
3. **The city.** A whole city rebuilt at the series' fidelity is the largest and least certain line, and the one most likely to grow. Adding the Ruins, the Valley and its story night, or any future mode before launch on top of it pushes the cost past the roughly $290M of the High case [A].

**The three conditions for sustainability**

1. **Launch on one world:** Survivor in the Raccoon City of 1998, rebuilt whole, reusing every piece the remakes made, for no more than about $205M, and less if the first gate allows.
2. **Sell the First Run, and keep the Opening date:** about 12 million copies in two years, and no later Opening.
3. **Let earnings set the service:** the tiers of Promise 14, the gates before launch, and Echo fill in the queues. When the game earns less, it shrinks. It never turns to what the Promises forbid.

## Sources

- Capcom IR: consolidated results and results presentation for the year ended March 2026; Integrated Report 2025.
- Capcom Open Conference RE:2026 (REX), as reported by Digital Citizen; MP1st (REX, 2023).
- TweakTown and PlayStation LifeStyle (*Resident Evil 2*, 800 people); Twisted Voxel (*Requiem* staff).
- GamingBolt, on the UK CMA's figures for AAA costs; Insider Gaming and 80.lv (*ARC Raiders* cost); Digital Citizen (*ARC Raiders* sales); KitGuru (*Concord*).
- 4Players, ODIN pricing.
- Nikkei, Capcom average salary.
- Gematsu (*Street Fighter 6*).
- Steamcharts (*Resistance*); Insider Gaming (*Re:Verse*); Game World Observer and KitGuru (*Exoprimal*).
- Shacknews (*Fall Guys*); Alinea Analytics (*Helldivers 2*).
- Amazon GameLift Servers pricing; Steam revenue-share tiers.
