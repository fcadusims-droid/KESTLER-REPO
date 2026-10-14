---
section: "07 · Feasibility"
description: "Costs, revenue, cases, break-even, sensitivity, population, verdict"
order: 37
---

# The Business Case

*This document is the business case for the Service documents: what Resident Evil Online costs to build and run, what it earns, and what happens if it earns less. Every figure carries a label: **[P]** Public Data, **[E]** Industry Estimate, **[A]** Model Assumption. Dollars are US dollars, converted at ¥150 to the dollar [A]. The games it is measured against, and the context each succeeded or failed in, are in `market-precedents.md`.*

## The Answer

**Only as a bet on a large hit.** As the documents describe it, with the whole of Raccoon City rebuilt for the launch and every system they define, Resident Evil Online costs about $246M before launch. At that cost it does not pay for itself in any case the model runs. In the Base case, 7 million First Run copies, it ends about $190M short. It pays for itself at about 17 million copies, the size of ARC Raiders' first eight months (`market-precedents.md`), and more than twice what *Resident Evil Requiem* sold in its first four.

The model still holds together, and three things still make it hold:

- **The price pays for the game.** A US$29.99 First Run brings in most of the money a copy will ever bring.
- **Cosmetics pay for the service.** The Wardrobe, Patron, and early access keep the online game running after the Opening.
- **The rules cap the loss.** Promise 14 and `offline-and-ownership.md` keep a failure from becoming a slow drain: in the cases that miss, the game goes offline at the Opening instead of losing money every year after it.

What is wrong is the cost. The precedents are plain about it: the one game in this genre that sold this many copies cost a third as much, and the games that cost this much are on the failure side (`market-precedents.md`, What the Successes Share). Two levers, both already in the documents or a decision away, bring the break-even down to about 11 million copies (Break-Even, below). Resident Evil's fans do not change the answer: they make the cases short of a hit less likely and make a hit pay, and in the Base case they are worth about $60M once Capcom's catalog is counted, not $190M (What the Fans Are Worth, below).

A free-to-play launch with the same player-friendly rules would not work: at $8 a year per player it would need about 10 million monthly players just to run at full size, and about 23 million to also repay its cost within five years [A].

## Anchors

| Fact | Figure | Label |
|---|---|---|
| Capcom net sales and operating income, FY ended March 2026 | ¥195.3 billion (≈ $1.30 billion) and ¥75.3 billion (≈ $502M); profit at a record for the ninth year running | P |
| Capcom forecast, FY ending March 2027 | ¥210.0 billion net sales | P |
| Capcom units sold, FY ended March 2026 | 59.07 million, 93% digital, 54.5% on PC | P |
| Capcom development investment, FY ended March 2026 / plan for FY ending March 2027 | ¥54.8 billion (≈ $365M) / ¥62.9 billion (≈ $419M) | P |
| Capcom average annual salary | ¥9.18 million (≈ $61,000) | P |
| Loaded cost per Capcom developer, salary plus overhead | ≈ $100,000 a year | E |
| *Resident Evil Requiem* | 5 million in its first week, 6.91 million by March 2026, over 8 million by June 2026; the series at 213 million | P |
| *ARC Raiders*, a US$40 PvPvE extraction game (Embark) | 14 million copies in two months, 16.3 million by June 2026, more than $550M in revenue; about $75M to make with marketing, about 70 people | P (sales) · E (cost) |
| *Helldivers 2*, a US$40 online game | 12 million copies in twelve weeks, 20 million by January 2026, more than $700M gross from copies | P · E |
| *Marathon* (Bungie), a US$40 extraction game | About 1.2 million copies and $55M in its first weeks; 71% of its Steam players gone a month later; budget reported above $250M | E |
| *Concord* (Sony), a live-service shooter shut down two weeks after launch | Budget estimates from about $100M to about $400M | E |
| Peak Steam players of Capcom's online spin-offs | *Resistance* 4,181 · *Re:Verse* 2,080 · *Exoprimal* 4,522 | P |
| Monthly players against copies | *ARC Raiders*: about 10 million monthly players three months in, on about 15 million copies. *Helldivers 2*: about 3.6 million on 20 million, two years in | E |
| Peak concurrency against monthly players | *ARC Raiders*: 700,000 concurrent in its second week; *Marathon*: about 125,000 at launch on 2.2 million players that month | E |
| Platform fees | Steam 30% / 25% above $10M / 20% above $50M; consoles about 30% | P (Steam) · E (consoles) |
| Server cost, 100-player battle royale on AWS GameLift, 100,000 peak players | $165,000 a month on demand, $105,000 optimized | P |
| Proximity voice middleware (4Players ODIN), price per peak concurrent user a month | €0.29, falling to €0.19 above 80,000 | P |
| Age assurance, price per check | About $0.10 for facial age estimation to $1.50 or more for document checks | E |
| Cloud speech-to-text, price per minute | $0.016, falling to $0.004 at volume | E |
| Capcom's RE Engine department / REX | About 200 engineers, 160 on the engine; REX, detailed in 2026, evolves the RE Engine step by step | P |
| *Resident Evil 2* (2019), people involved | More than 800, Capcom's figure during development | P |
| *Resident Evil Requiem*, in-house staff | About 150 to 200, by its director, plus R&D and technical art | P |
| A newly greenlit AAA game, development alone | About $200M or more, against $50–150M five years earlier | E (CMA, 2023) |
| Share of Steam revenue from free-to-play games, 2025 | About 22% | E |

**What the precedents set.** Four assumptions below come from them, not from judgment alone [A]:

- **Sales come early.** ARC Raiders sold 86% of its first eight months in its first two, and Helldivers 2 sold 60% of its first two years in its first twelve weeks. The model sells 75% of the First Run's copies in its first year.
- **Monthly players fall from the first month.** The model holds monthly players, on average, at 35% of the copies sold in the first year, and 22% of all copies in the second: between ARC Raiders early and Helldivers 2 late.
- **Peak concurrency is 5% of monthly players while the game is sold, and 4% after the Opening.** Both precedents ran higher at launch; mature games run lower.
- **Most players are on PC.** The model takes Capcom's own share, 55% of copies on Steam.

## 1 · Building It

The launch is smaller than the whole design (`seasons-and-new-content.md`, `launch-scope.md`): Survivor on one world, the Raccoon City of 1998. But that one world is the whole city, rebuilt as a new remake, with what the remakes of *Resident Evil 2* and *3* made reused wherever the city holds it (`presentation-and-technology.md`, Raccoon City, Rebuilt Whole). It is lit for every hour and every weather, and it carries every system the launch holds: safe rooms and their Wardens, stashes, vehicles, worn inventory, hunger and thirst, Self-Examination and the tending of wounds, destruction, proximity voice carried by the city's acoustics, Hardening, the story night, the director, the Echoes, and the protections `legal-feasibility.md` requires.

| Component | Low | Realistic | High |
|---|---|---|---|
| Core team (average headcount × years × $100k) | 160 × 3.5 = $56M | 200 × 4 = $80M | 250 × 4.5 = $112.5M |
| The city: outsourced environment art for every district no remake built, and the rework of every reused one for scale, hours, and weather | $22M | $32M | $48M |
| Server and backend: a 100-survivor server running the dead at scale, deciding what each player may see, and holding every night's state (`presentation-and-technology.md`, Servers) | $12M | $16M | $22M |
| The director: the Pulse, the planner, the Law validator, the announcer and its truth tests, the audit log, telemetry, deterministic replay, the director console (`director-architecture.md`) | $6M | $8M | $12M |
| Motion capture and animation: Hardening's two bodies, Self-Examination and the tending of every wound, the Wardens and their punishments, the weight of the Heavy, vehicles, the dead | $6M | $9M | $14M |
| Voice and accessibility: proximity voice through the city's sound, reading a whisper from a shout, typed speech and captions (`legal-feasibility.md`, Accessible Communication) | $4M | $6M | $9M |
| The Echo system (`director-architecture.md`, The Echoes) | $4M | $6M | $10M |
| The story night: live scenes and their branches, Moments, the as-recorded bodies, the Last Scenes (`story-nights.md`) | $6M | $10M | $16M |
| ΜΝΗΜΗ's voices: two performers in every voiced language recording pools for a thousand nights per file, every changing value recorded as its own piece, and every line tested; nothing synthesized (`project-overview.md`, Performed by People) | $5M | $9M | $14M |
| Destruction: breach points, collapse sites, and traps of the city across every district (`destruction.md`) | $3M | $5M | $8M |
| Localization at launch: text in every launch language, and ΜΝΗΜΗ, the live scenes, the Stranded, and the companions voiced in the largest | $5M | $8M | $12M |
| Compliance and privacy: age assurance, parental tools, impact assessments, notice-and-action, ratings, counsel in five markets (`legal-feasibility.md`) | $2M | $3M | $5M |
| The launch Wardrobe: the First File, the Dossier and Portrait, the first sets, diorama pieces, kits, and models (`cosmetics-and-dossier.md`) | $4M | $6M | $9M |
| QA, load tests, betas | $8M | $12M | $16M |
| **Build cost** | **$143M** | **$210M** | **$307.5M** |
| Launch marketing | $20M | $30M | $40M |
| Launch preparation | $4M | $6M | $8M |
| **Total before launch** | **$167M** | **$246M** | **$355.5M** |

All [A], with the head cost from Capcom's own pay [E]. The core team pays for the design, the code, and the people; every other line is spending beyond it, most of it outsourced. The Realistic core team sits at *Requiem*'s in-house size [P], held for four years, with the city's art outsourced as Capcom outsourced much of *Resident Evil 2*'s 800 [P]. The Realistic build is about $53M a year over four years, about 13% of Capcom's planned yearly development investment [E]; the total before launch is a little more than half of one year's [E]. Every performance in it is recorded from a person, which costs more than the synthetic voices other studios use and is the project's rule (`project-overview.md`, Performed by People). It is in line with what a newly greenlit AAA game costs [E]. It is also about what *Marathon* is reported to have cost, and more than three times what *ARC Raiders* is reported to have cost [E].

**How long.** About four years from the first gate's funding to launch in the Realistic case: three and a half if the city's reuse goes further than planned, four and a half if it does not [A]. A project begun in 2027 launches about 2031, on the RE Engine as REX changes it underneath (`presentation-and-technology.md`, Engine and Platforms).

## 2 · Running It

Promise 14 makes the operating budget a set of tiers, not a fixed cost. While the First Run lasts, the service runs at Full. After the Opening, each year it runs at the highest tier its earnings can pay for, and below Keep-alive the online service ends and the game goes offline under `offline-and-ownership.md`.

| Tier | Live team | Content | Backend | Support | Moderation | Anti-cheat | QA | Marketing | Localization | Compliance | ΜΝΗΜΗ's new lines | **Total, before players** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Full** | 80 heads, $8.0M | $10M | $3.0M | $2.5M | $3.0M | $2.0M | $2.5M | $6M | $1.5M | $1.0M | $1.5M | **$41.0M** |
| **Standard** | 50 heads, $5.0M | $5M | $2.5M | $1.8M | $2.0M | $1.5M | $1.5M | $3M | $1.0M | $0.8M | $0.8M | **$24.9M** |
| **Lean** | 25 heads, $2.5M | $2M | $2.0M | $1.2M | $1.2M | $1.0M | $0.8M | $1M | $0.4M | $0.6M | $0.3M | **$13.0M** |
| **Keep-alive** | 15 heads, $1.5M | $0.3M | $1.5M | $0.8M | $0.8M | $0.8M | $0.4M | none | $0.2M | $0.5M | none | **$6.8M** |

All [A]. Content pays for the seasons, a release every two weeks with its headline set, the events, and the Casefiles (`seasons-and-new-content.md`). Moderation pays for a person to review every report, voice and diorama alike, and for a statement of reasons with every sanction (`the-service-and-promises.md`, Conduct). ΜΝΗΜΗ's new lines are recorded by her performers in sessions each season. Compliance keeps the impact assessments, the risk assessments the UK and Brazil require, a legal representative in Brazil, and ratings for every update current (`legal-feasibility.md`).

**The second year's arrivals.** On top of Full, the First Run pays for what opens in its second year: the Ruins, made from the rebuilt 1998 city and what *Requiem* made of it, at about $12M, and the anomaly library, its limits, and its testing at about $6M, spread over the First Run's two years at $9M a year [A] (`seasons-and-new-content.md`, The Order of Arrival).

**What each player costs.** Added on top of the tier, year by year [A]:

| Cost | Rate | Why |
|---|---|---|
| Servers | $2.50 per peak concurrent player per month | About one and a half times the AWS battle-royale example on demand, because each Survivor server also runs the dead, the director's planner, up to a quarter of its survivors as Echoes, and a separate view for every player |
| Proximity voice | $0.25 per peak concurrent player per month | ODIN's volume price [P] |
| Captions and typed speech | $0.20 per monthly player per year | Cloud speech-to-text at volume prices, for the share of players who turn captions on [E] |
| Age assurance | $0.50 per new account | Between facial estimation and document checks; Brazil does not accept a player's own word [E] |

With peak players at 5% of monthly players while the First Run lasts, and 4% after the Opening, servers and voice cost about $1.65 per monthly player per year in the First Run and about $1.32 after it.

**The Valley is not in any tier.** Rebuilt from the remake of *Resident Evil 4*, with its own story night, it costs about $30–45M [A], more than any tier's content budget. It is built only if the First Run sells more than 6 million copies in its first year, on course for the Hit case, and is paid for from the second year's earnings. In the Base case it is not built. In the Hit case it is, and it is the difference between profit and loss: the Hit case ends about $17M short with the Valley and about $20M ahead without it, because the Valley is paid for in the year the First Run's sales are falling, and the model counts its cost and none of what it might earn after the Opening [A]. That is the rule as it stands; `market-precedents.md` (Open Questions) asks whether it should follow what the project has earned back instead.

## 3 · What It Earns

**The First Run: about $18.70 net per copy** [A]:

| Step | Per copy |
|---|---|
| List price, with 15% of buyers taking the US$49.99 Founder's Edition | $32.99 |
| After regional prices and discounts, at 82% | $27.05 |
| After sales taxes included in shown prices, 7% blended | $25.16 |
| After platform fees: 55% of copies on Steam at about 22% effective, 45% on consoles at 30% | **$18.72** |

**The Wardrobe, Patron, and early access**, gross per monthly player per year [A]. The same taxes and fees take about 31% of it, so the net is about 69% of the figure shown.

| | First Run, owners | After the Opening, free |
|---|---|---|
| Miss | $6 | $4 |
| Conservative | $8 | $5 |
| Base | $12 | $8 |
| Hit | $15 | $10 |

Owners spend more than free players because they already chose to pay. The figures stay modest because every look can be earned, nothing leaves, and nothing creates urgency: those rules cost revenue, and the model counts that cost.

## 4 · Four Cases

| | Miss | Conservative | Base | Hit |
|---|---|---|---|---|
| Copies sold in the First Run | 1.5M | 3M | 7M | 15M |
| Its precedent | *Marathon*'s first weeks | A well-received niche game | Fewer than *Requiem* sold in its first four months | *ARC Raiders*' first eight months |
| Monthly players, first year / second year | 0.39M / 0.33M | 0.79M / 0.66M | 1.84M / 1.54M | 3.94M / 3.30M |
| Monthly players in the first free year, against the last paid year | 1.2 × | 1.5 × | 2 × | 2.5 × |
| Decline of free players each year | 25% | 25% | 25% | 25% |
| Years the online service runs | 2 | 2 | 4 | 9 |
| **Result over the whole online life, after building it** | **−$317M** | **−$286M** | **−$190M** | **−$17M** |
| Year the project has repaid itself | never | never | never | never |

All [A]. The free-player multipliers are anchored to PUBG and Fall Guys, whose players rose sharply when they went free [P], held lower than either because Resident Evil Online goes free on a planned date, not to rescue a falling game. In the Miss and Conservative cases the free game cannot pay even for Keep-alive, so the Opening and the move offline come together (`offline-and-ownership.md`). A project stopped at the second gate loses about $120M (Capcom's Decision, below): every case short of a hit loses more by launching than by stopping there.

The Base case, year by year:

| Year | Copies | Monthly players | Peak players | Net revenue | Tier | Result | Running total |
|---|---|---|---|---|---|---|---|
| 1 | 5.25M | 1.84M | 92,000 | $114M | Full, and the second year's arrivals | +$58M | −$189M |
| 2 | 1.75M | 1.54M | 77,000 | $46M | Full, and the second year's arrivals | −$8M | −$197M |
| 3 (Opening) | free | 3.08M | 123,000 | $17M | Keep-alive | +$5M | −$192M |
| 4 | free | 2.31M | 92,000 | $13M | Keep-alive | +$2M | −$190M |
| 5 | | | | | Offline | | |

All [A], rounded. The First Run carries the project. The second year already loses money: its copies fall to a quarter of the first's, and it still pays for Full and for the Ruins. After the Opening the free game pays only for Keep-alive, and in the fifth year not even that. It is not the population that ends the service: a peak of 69,000 would still fill every queue (Population, below). It is that 1.7 million free players do not pay for the smallest service the game can run.

## 5 · Break-Even

| First Run copies | Result over the online life, Realistic costs |
|---|---|
| 7M, the Base case | −$190M |
| 10M | −$157M |
| 12M | −$111M |
| 14M | −$65M |
| 16M | −$24M |
| 17M | about break-even |
| 20M | +$66M |

All [A], with the Base case's spending and free players. Above 8 million copies the first year passes 6 million, and the Valley is built.

**The project breaks even at about 17 million First Run copies** [A]: about what *ARC Raiders* sold in eight months at $40 [P], and more than twice what *Requiem* sold in its first four at full price [P]. Without the Valley's rule it would break even at about 15.5 million.

**The two levers.**

| | Realistic costs, US$29.99 | Low costs, US$29.99 | Realistic costs, US$39.99 | Low costs, US$39.99 |
|---|---|---|---|---|
| Break-even | about 17M copies | about 13.5M | about 13.5M | about 11M |
| Base case result | −$190M | −$111M | −$150M | −$71M |

- **The Low case** is what the city's reuse decides, and the first gate measures it (Capcom's Decision, below). It is the lever already in the documents.
- **A US$39.99 First Run** would raise the net per copy to about $24.40. It is not a lever this document can pull: Promise 6 fixes the price at US$29.99 (`the-service-and-promises.md`). The successes in this genre sold at $40, and so did *Marathon*; the price alone did not decide any of them (`market-precedents.md`). Whether to change Promise 6 is a decision for the design, and these are its numbers.

**What else moves the Base case,** each against the Base case's −$190M [A]:

| Assumption | Range tested | Effect |
|---|---|---|
| Build cost | The Low / the High case | +$79M / −$110M |
| Wardrobe spending | A third lower / higher | −$16M / +$11M |
| Server cost | $1.75 / $3.50 per peak player a month | +$4M / −$5M |
| Players after the Opening | 1.5 × / 2.5 × the last paid year | −$5M / +$1M |
| Share of copies on PC | 40% / 70% | −$3M / +$3M |
| Share of copies in the first year | 60% / 85% | −$2M / +$2M |

Nothing but copies and cost moves the result by more than a few million. The model is a bet on how many people buy the First Run, and on how much it cost to make.

**After the Opening**, each tier needs this many monthly players at the Base case's $8 a year, after taxes, fees, and what each player costs [A]:

| Tier | Monthly players needed |
|---|---|
| Keep-alive | 1.7M |
| Lean | 3.3M |
| Standard | 6.4M |
| Full | 10.5M |

The free game sustains a small service, not a large one. New places after the Opening arrive only as fast as those tiers allow.

## 6 · What the Fans Are Worth

Resident Evil has a fanbase thirty years deep. The question is whether it makes this game earn more than the cases above already assume. It can, in three ways, and by less than the size of the franchise suggests.

**What the record shows.**

| Evidence | Figure | What it shows | Label |
|---|---|---|---|
| The franchise | 213 million units. *Requiem*, the fastest seller in the series, sold 5 million in its first week, 6.9 million by March 2026, and over 8 million by June 2026 | Fans buy a new Resident Evil at once, and in numbers | P |
| The best seller, over time | *Resident Evil 2* (2019) reached 18.3 million after seven years; no Resident Evil game has sold 17 million in two | The break-even asks for more than any Resident Evil has ever sold in a First Run's time | P |
| Resident Evil online | *Outbreak* sold 1.45 million (2003). *Operation Raccoon City* sold 2.8 million (2012), when *Resident Evil 5* and *6* each sold over 10 million. *Umbrella Corps* (2016) never reached Capcom's million-seller list and was rated 36 to 38 on Metacritic. *Resistance* and *Re:Verse* were given away with mainline games | The fans have never followed Resident Evil online in numbers. The best result was about a quarter of a mainline game | P |
| Capcom's own online franchise | *Monster Hunter Wilds* sold 10 million in its first month and 11.4 million by March 2026; *Monster Hunter: World* reached 22.1 million | A fanbase fills the launch. What a game does with it decides the tail | P |
| The catalog | About 85% of the units Capcom sold in the year to March 2026 were catalog titles; five catalog Resident Evil games sold over a million each in the three months to June 2026 | The fans' lasting value is in the games they already own | P |

**What the fans can add, against the Base case's −$190M** [A]:

| Effect | Assumption | Base case |
|---|---|---|
| A larger launch | The Base case already sells, over two years, nearly what *Requiem* sold in four months, and two and a half times the best online Resident Evil. A larger First Run is the Hit case, not a fan effect | — |
| Spending on the records | A third more spent in the Wardrobe by owners and free players, on what only Resident Evil can sell: the models of its people and creatures, the uniforms of S.T.A.R.S., the R.P.D., and the U.B.C.S., the backdrops of its places | +$11M, to −$179M |
| The catalog | A free Resident Evil game in the places of four of its games sends players to them (Capcom's Decision, below): 5% more of an estimated 16 million catalog Resident Evil units a year, at about $10 net each, about $8M a year while the game is online. It is Capcom's revenue, not the project's | +$32M, to −$158M |
| Both | | +$59M, to −$131M |

**The Fan case.** If the fans carry the First Run to 11 million copies, between the Base case and the Hit, and spend a third more, the project ends about $58M short with the catalog counted, and about $21M ahead at the Low case's cost. With the fans' spending and the catalog counted, the break-even falls from about 17 million copies to about 13 million at Realistic costs, and about 10 million at Low ones.

**What it means.** The fans make the Miss and Conservative cases less likely, and make the Hit case pay: with their spending and the catalog it ends about $109M ahead instead of $17M short. They do not make the Base case pay, because the Base case already counts on them. Two cautions follow from the record:

- **The fans come for Resident Evil, not for an online game.** *Umbrella Corps* was judged a generic shooter with a Resident Evil skin, and its players treated it as one. What this game offers the fans is in the story night, the people of the records, their looks as recorded, and ΜΝΗΜΗ's world (`story-nights.md`, `market-precedents.md`). Those are costed lines, and cutting them to reach the Low case cuts what the fans pay for.
- **The fans arrive in the first month.** *Monster Hunter Wilds* sold about 90% of its first year's copies in its first month. A launch the fans leave is not saved by the fans.

## 7 · Population

Survivor matches in two kinds of night, Solo and Squad, and three regions: six queues at launch (`presentation-and-technology.md`, Matchmaking). When the Ruins arrive, each player's choice between the classic rotation and the Ruins doubles that to twelve. A queue fills a 64-survivor night in 90 seconds if about 1,900 players are in it at once, assuming each spends about 45 minutes in a night before queuing again [A]. Echoes filling up to a quarter of a night lower that to about 1,425 [A].

| | Peak players needed | Monthly players, while sold | Monthly players, after the Opening |
|---|---|---|---|
| Six queues, players only | 28,500 | 0.57M | 0.71M |
| Six queues, with Echoes filling up to a quarter | 21,375 | 0.43M | 0.53M |
| Twelve queues, players only | 57,000 | 1.14M | 1.43M |
| Twelve queues, with Echoes filling up to a quarter | 42,750 | 0.86M | 1.07M |

All [A], with off-peak taken as 40% of peak and all play in Survivor. No players in China are counted: selling there needs a state licence and its own rules for minors (`legal-feasibility.md`, Markets Considered). The Base case clears the six-queue threshold from the first year, with about 92,000 peak players, and the twelve-queue threshold once the Ruins arrive, with about 77,000 in the second year and about 123,000 after the Opening. The Conservative case clears six queues with Echo fill, with about 39,000. The Miss case does not: about 20,000 at launch, falling, which is how *Marathon*'s and *Splitgate 2*'s queues emptied (`market-precedents.md`). Capcom's online spin-offs peaked at 2,000 to 4,500 on Steam alone [P]. These are the figures for a hard split. The lobby's choice is softer than that (`presentation-and-technology.md`, Matchmaking): a player can tick both maps, and one who waits four minutes is offered the other, so the twelve queues behave like fewer when the population is thin. When Echo fill is not enough, queues merge regions and nights start at forty: two merged queues need only about 7,000 peak players.

## 8 · Capcom's Decision

- **Fit:** $246M is more than Capcom has put into any online spin-off, about what it puts into a mainline game, and about what *Marathon* is reported to have cost [E]. It is built on a city Capcom already owns half of, and sold the way Capcom sells what works: a paid game with free updates and cosmetics, like *Street Fighter 6* and *Monster Hunter* [P].
- **Gates:** two gates cap the loss before it is spent.
  - **The first gate** is a playable slice of Survivor, tested with outside players at about $25M spent: one district of the rebuilt city at two hours and two weathers, with proximity voice reading whispers from shouts, and Hardening's first and last stages. It also measures how far the city's reuse goes, which decides whether the project is on the Low case's path. A slice that shows the Realistic cost or worse, with no fallback taken, should not go on as designed.
  - **The second gate** is a closed beta of the whole city, at about $120M spent, judged on whether players come back and on peak concurrency. Its test is the one every failure in `market-precedents.md` failed: a beta that keeps fewer than half of its first week's players four weeks later [A], or whose players would put the launch below the six-queue population with Echo fill, stops there.
- **Fallback:** if the first gate shows the story night costs more than its line, the launch can ship Late Wakings in its place (`story-nights.md`), at roughly half that line's cost [A].
- **The city is the lever.** Every district the remakes already built that can be reused instead of rebuilt lowers the largest new line. The city is also built once for every mode: a future mode plays on bounds of it and pays for its seals, not for a map (`worlds.md`, One World, Every Mode). At the Low case's cost the project breaks even near 13.5 million copies [A].
- **Franchise:** most of the units Capcom sells each year are catalog titles, not new releases [P], and Resident Evil is the largest part of that catalog. A free Resident Evil game set in the places of *Resident Evil 2*, *3*, *4*, and *Requiem* sends players to those games. The model counts that value only in What the Fans Are Worth, as about $8M a year while the game is online [A]. It is a reason to fund the project, not a reason it pays.

## 9 · Verdict

**ONLY AS A BET ON A LARGE HIT.** The Base case loses about $190M. The project is worth funding only if Capcom believes the First Run can sell about 17 million copies, or the first gate brings the cost toward the Low case and the break-even toward 13.5 million. Resident Evil's fans make a hit likelier and more profitable; they do not turn the Base case into a profit. It is cheaper to stop at the second gate than to launch anything short of a hit.

**The five numbers that matter**

1. **$246M** realistic cost before launch, about 13% of Capcom's yearly development investment for four years [A].
2. **17 million** First Run copies to break even over the online life; 13.5 million at the Low case's cost; about 13 million with the fans' spending and Capcom's catalog counted [A].
3. **$18.70** net per First Run copy, against **$5.50** a year per free player after the Opening [A].
4. **1.7 million** monthly free players to keep the service at Keep-alive after the Opening, 3.3 million for Lean [A].
5. **21,375** peak players for healthy Survivor queues with Echo fill at launch, and **42,750** once the Ruins arrive [A].

**The three biggest financial risks**

1. **The cost.** A whole city rebuilt at the series' fidelity, with every system the documents define, costs what the genre's failures cost. The city is the largest and least certain line, and the one most likely to grow. Adding the Ruins, the Valley and its story night, or any future mode before launch on top of it pushes the cost past the roughly $355M of the High case [A].
2. **The first month.** Every failure in `market-precedents.md` lost most of its players in thirty days, and the First Run earns 75% of its copies in its first year. A slow start is not recovered by the Opening.
3. **The free phase earns little per player.** Earnable looks, no urgency, and no currency for sale keep revenue per free player low. After the Opening the game revives its population and shrinks its service; it does not repay its build.

**The three conditions for sustainability**

1. **Launch on one world, at the Low case's cost:** Survivor in the Raccoon City of 1998, rebuilt whole, reusing every piece the remakes made, for about $167M, with Late Wakings ready if the story night runs over, and without cutting what the fans come for (What the Fans Are Worth).
2. **Win the first month, then sell the First Run:** a launch the second gate has shown players return to, and about 13.5 million copies in two years at that cost, with the Opening on its date.
3. **Let earnings set the service:** the tiers of Promise 14, the gates before launch, and Echo fill in the queues. When the game earns less, it shrinks. It never turns to what the Promises forbid.

## Sources

- Capcom IR: consolidated results for the year ended March 2026 and for the first quarter of the year ending March 2027; Integrated Report 2025. WN Hub, *Record profit for the ninth consecutive year*, May 2026; Nasdaq/RTT, *Capcom Q1 net profit rises*, July 2026.
- Game Developer, *Resident Evil Requiem has sold over 8M units*, July 2026.
- Capcom Open Conference RE:2026 (REX), as reported by Digital Citizen; MP1st (REX, 2023).
- TweakTown and PlayStation LifeStyle (*Resident Evil 2*, 800 people); Twisted Voxel (*Requiem* staff).
- GamingBolt, on the UK CMA's figures for AAA costs; Insider Gaming and 80.lv (*ARC Raiders* cost); GamesBeat, on Nexon's results (*ARC Raiders* sales); Notebookcheck, on Alinea Analytics (*ARC Raiders*, *Marathon*); tbreak, on Forbes (*Marathon* budget); KitGuru and TechRadar (*Concord*).
- FRVR, on Alinea Analytics (*Helldivers 2*); TechSpot (*PUBG*); Shacknews (*Fall Guys*).
- WN Hub, *Alinea Analytics: free-to-play did not take over the PC gaming market*, 2026.
- 4Players, ODIN pricing; Amazon GameLift Servers pricing; Steam revenue-share tiers.
- Didit, *Top age verification software*, 2026 (vendor comparison, used for the price range only); CostBench, *Google Cloud Speech-to-Text pricing*, 2026.
- Nikkei, Capcom average salary.
- Gematsu (*Street Fighter 6*).
- Steamcharts (*Resistance*); Insider Gaming (*Re:Verse*); Game World Observer and KitGuru (*Exoprimal*).
- Gematsu, *Capcom Platinum Titles sales update, as of March 31, 2026*; Automaton, *Capcom expects next year's profits to be carried by past releases*, 2026; Wikipedia, *Umbrella Corps*; Push Square, *Monster Hunter Wilds sells 11 million in just under a year*, 2026.
- Every game in `market-precedents.md`, with its own sources there.
