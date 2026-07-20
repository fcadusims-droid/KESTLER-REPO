---
title: "Generational"
description: "Game design document for a generational roguelite where the player does not steer a hero but tends a bloodline and its legacy across centuries of human history, from the Stone Age to the stars."
genre: "Roguelite / Life-Sim"
category: "Game Design Document"
---

# GENERATIONAL
### Game Design Document

> *"A life ends. A lineage continues. The universe never forgets."*

---

## 1. Overview

**Generational** is a single-player generational roguelite built on interactive text and unfolding events. The player does not control a hero. The player tends a bloodline — and, more importantly, a legacy — as it travels across centuries of human history, from the first fires of the Stone Age toward the threshold of the future.

The whole experience is a self-contained campaign: a grounded, historical simulation of one human lineage climbing through the real arc of civilization, from the Stone Age to the dawn of a space-faring age. There is no multiplayer, no online layer, and no science fiction within the game itself — only the intimate, human story of a family across deep time, told entirely through text and choice. The design carries one distant, deliberately out-of-scope ambition for a possible future expansion — a multiverse layer called Project Chronos — but it is named only as a long-horizon vision and forms no part of the product this document describes. As designed here, *Generational* is complete and satisfying on its own, and asks nothing of the player beyond their own lineage's story.

Every run is a single human life, told through choices, encounters, and the slow accumulation of consequence. When that life ends, the game does not. What the character built, learned, and left behind passes forward — sometimes through a child of their blood, sometimes through a stranger whose life they touched so deeply that the stranger carried their name into the future. The death of one person is the birth of the next chapter, and the chain of chapters is the game.

Where most games measure progress in levels and loot, Generational measures it in inheritance. A bloodline grows stronger not because the player grinds, but because each life leaves something behind for the next to stand upon: sharper instincts in the blood, deeper knowledge in the mind, wealth in the coffers, and a name in the mouths of others. Over dozens or hundreds of lives, a humble hunter's descendants might raise the first walls of a city, forge the first empire, or look up one night and decide to reach for the stars.

**Genre:** Generational roguelite / narrative life-simulation
**Platform:** PC (Windows, macOS, Linux), with strong portability to mobile
**Modes:** Single-player only (a future multiverse expansion, Project Chronos, is out of scope for this product)
**Perspective:** Intimate, character-level interactive text — each life lived up close, the lineage shaped across many
**Session shape:** Variable — a life may last minutes or hours, paced by the player
**Target audience:** Players who love *BitLife*, *Reigns*, *Crusader Kings*, *Cultist Simulator*, and the "one more turn" pull of *Civilization*; readers who want history to feel personal; people who find more drama in a family tree than in a boss fight.

**What sets it apart:** Generational treats *legacy* — not survival, not victory — as the core resource. It is the rare life-sim where dying without an heir is the true failure, and where an heir need not share your blood. A soldier who fell heroically in a forgotten war can live on through the son of the friend he saved, raised on stories of a man he never met. The game asks a quieter, stranger question than most: not *did you win*, but *did you matter to anyone enough to be remembered*.

---

## 2. The Core Loop

Generational turns on a single, unbroken cycle. The player is always somewhere on this wheel, and the wheel never stops turning until a lineage dies out entirely.

A new character is **born**, carrying inherited blood and a set of traits uniquely their own. The player guides them as they **live** — growing from child to elder, making choices at every turning point, forming bonds, taking up a craft or a cause, facing the dangers and temptations of their era. Throughout that life, the character has the chance to **leave a mark**: by raising a child, or by shaping another person so profoundly that the bond itself becomes inheritable. Eventually the character **dies**, and the game tallies what their life meant. From the marks they left, an **heir** steps forward, and the player chooses who continues the story. Then the wheel turns again, and a new life begins atop everything the last one built.

There is one hard rule woven through this loop, and it gives every life its quiet tension: **a lineage that leaves no one behind ends.** If a character dies having neither raised a child nor truly touched another soul — and no collateral kin of the extended family survives to carry the name — there is no one to continue the story. The bloodline is extinguished, the accumulated inheritance is lost, and the player must begin again from far less. Extinction is the game's only real failure state, and the extended family is the net that keeps it rare rather than constant: a single character's failure is survivable, but a whole family's is not. Because of this, every relationship a character forms is, in some sense, a bet against oblivion.

The diagram below shows the full loop. The inner wheel is a single life. Surrounding it are the two things that make Generational more than a string of lives: the **persistent lineage ledger** that every life writes into and the next inherits, and the **two era clocks** that tick in the background, the world's on its own and the lineage's only when the player carries it across a threshold.

```
        TWO ERA CLOCKS (always ticking in the background)
        ┌────────────────────────────────────────────────┐
        │  WORLD ERA  ▸ advances on its own                │
        │  LINEAGE ERA ▸ advances only when YOU cross it   │
        │  → the GAP between them drives pressure & chance  │
        └────────────────────────────────────────────────┘
                              ║ (frames every life)
                              ▼
        ┌───────────────────────── ONE LIFE ─────────────────────────┐
        │                                                             │
        │   BIRTH ──▶ LIVE ──▶ LEAVE A MARK ──▶ DEATH ──▶ CHOOSE HEIR │
        │   inherited   choices,   a child  —or—   life      blood    │
        │   self +      bonds,     a legacy      weighed      or      │
        │   ledger      craft, war  (kin/mark)              legacy    │
        │                                                      │      │
        └──────────────────────────────────────────────────────┼─────┘
                              ▲                                  │
                              │                                  ▼
        ┌─────────────────────┴──────────────┐     ┌────────────────────────┐
        │   PERSISTENT LINEAGE LEDGER         │     │  HEIR TYPE decides what │
        │   (carries across every life)       │◀────│  the next life inherits │
        │                                     │     ├────────────────────────┤
        │   • Possibility space  (permanent)  │     │ BLOOD ▸ directed genome │
        │   • Bearing            (permanent)  │     │   you AIM; full control │
        │   • Genome             (blood only) │     │ LEGACY ▸ Bearing seats  │
        │   • Reputation/Wealth  (fade)       │     │   a strong but GENERIC  │
        │                                     │     │   heir; possibility     │
        │   updated at each death ────────────┼────▶│   space carries on      │
        └─────────────────────────────────────┘     └────────────────────────┘

        ✕  No child, no mark, AND no collateral kin  →  LINEAGE EXTINCT  →  begin anew, diminished
```


---

## 3. Beginnings: The Founding Blood

Before the first life, there is no character to play. There is only potential. The player shapes the **founding blood** — the genetic seed from which an entire lineage will grow.

In these earliest moments, humanity is unrefined and the options are deliberately few. The player distributes a small pool of essence across the foundations of a person: their physical resilience, their quickness of mind, their creative spark, their capacity to adapt to hardship, and the first faint coloring of temperament. A founder who is strong but slow will sire a different history than one who is frail but brilliant. These early choices are not powerful in themselves — a Stone Age body can only do so much — but they bias everything that follows, the way the shape of a riverbed decides where a river will run a thousand years downstream.

The narrowness of the beginning is intentional, and it is a promise. Humanity earns its possibilities. Traits that cannot be chosen at the dawn of the lineage become available only after generations of lived experience unlock them: the disciplined focus of a people who have known war, the silver tongue of a line of traders, the inherited curiosity of a family that has always asked *why*. The founding blood is not where the player builds their ideal character. It is where they plant the first seed and accept that they will not live to see the tree.

---

## 4. Life: Living a Single Generation

Each life is experienced as a stream of unfolding text — moments, decisions, and reactions presented to the player as the character moves from cradle to grave. The rhythm is closer to a novel that bends to the reader than to a simulation watched from above. Some passages are quiet and pass in a sentence; others stop the world and demand a choice that will echo for generations.

A life is divided loosely into the seasons of a human existence. In **childhood**, the character's inherited traits settle and the first formative experiences begin to bend their personality — a cruel winter, a kind teacher, a sibling's death. In **youth**, the world opens: the character chooses or stumbles into a path, takes up a craft or a calling, and begins forming the bonds that will define them. In **adulthood**, the stakes are highest — this is when most marks are made, when children are born, when reputations are won and lost, when a life either reaches outward into the world or folds quietly inward. In **old age**, the character reaps what they sowed, and the player begins to feel the approach of the inheritance to come.

Because lives vary so wildly in length and consequence, the player sets the pace — but the pacing system is built so that speed never becomes a trap. A life that grips the player can be **lived slowly**, every fork explored, every relationship tended. An ordinary life can instead be **let run**, the character living on a light hand while the game advances time and resolves minor events on its own.

The accelerated mode is not an autopilot that can blunder a lineage into extinction, and it does not rely on a vague sense of "danger." It runs on **explicit pacing rules** governed by a single question the simulation can always answer precisely: *has this character secured continuity yet?* A character who has at least one living child, or one bond that has crossed the mark threshold, is **grounded** — their lineage is safe to continue no matter what happens next. A character who has neither is **ungrounded**, and the entire weight of the pacing system bears only on them.

When a character is **grounded**, let-run flows freely and fast. It skims through the quiet years *and* through the ordinary dramas of adulthood — the friendships, the rivalries, the marriages, the births — stopping only for things the player has asked to be stopped for (a configurable filter: major life events, pivotal opportunities, deaths) and for the era-threshold moments described below. Crucially, the mere *possibility* that a passing acquaintance might deepen into a mark does not halt acceleration, because continuity is already secured; these moments resolve on a light hand and are reported in the life-summary, not surfaced one by one. This is what keeps let-run fluid rather than stopping every few years to flag bonds that do not actually threaten the lineage. Most lives, most of the time, are grounded early — and so most acceleration is genuinely smooth.

When a character is **ungrounded**, and only then, let-run becomes careful. It still advances time smoothly through stretches where no continuity-bearing choice is reachable, but it stops at the specific forks whose outcome could *open or foreclose the character's only paths to an heir* — the courtship that could become a marriage, the apprentice who could become a mark, the dangerous venture that could kill a still-childless character. It does not stop at every social encounter; it stops at the ones the event system flags as able to create or destroy a continuity path for a character who has none. The effect is intuitive: the game pays close attention precisely while a life hangs by a thread, and relaxes the moment the thread is secured. A character cannot sleepwalk past their fertile, sociable years and leave the player stranded at forty-five, because while they remained ungrounded the system was already surfacing exactly the choices that could have prevented it.

The same pacing system governs the rhythm of a long playthrough at the largest scale. Lives the engine flags as pivotal — poised to cross an era threshold, to found something, to secure or lose the lineage's future — always interrupt acceleration regardless of grounding, because these are the moments the whole game exists to make the player feel. A journey that may span hundreds of generations never becomes a chore, and the lives that count are never reduced to a line of summary text. The intimacy is protected precisely where intimacy matters.

Every choice a character makes feeds two ledgers at once. One is the immediate story — what happens next, who lives, who is wronged, who is loved. The other is the inheritance — what this life will be worth when it ends. A player who only chases the moment may find their character beloved and their lineage poor; a player who only optimizes inheritance may build a dynasty of cold, hollow people. The game never tells the player which ledger to favor. That tension is the heart of playing well.

---

## 5. Inheritance: The Heart of the Game

When a character dies, Generational asks the question the entire design exists to pose: **who continues?** The answer is never automatic, and the two paths it offers are genuinely different ways to play.

### Blood

The most familiar path is the one written in blood. If the character has raised children, those children are heirs. A child of the body inherits the **strongest genetic legacy** — the physical gifts and predispositions accumulated across the whole bloodline, refined or coarsened by the parent's own life — along with a share of material wealth and the family's standing. Choosing blood is choosing to *deepen* a lineage: to compound genetic advantages generation after generation, to build a family that is, in its very flesh, the product of everything that came before.

But blood is fragile. Children die young in harsh eras. A character may never have any. And a bloodline that pursues only its own perfection can grow narrow, inbred, and brittle — strong in body, perhaps, but unloved and unremembered by the wider world.

### Legacy

The second path is the one the player will remember. A character who never had children — or who had them and lost them — is not necessarily the end of anything. Throughout a life, the character forms bonds, and the deepest of these are tracked as **marks**: people whose lives were genuinely altered by the character. The apprentice taught a trade. The orphan taken in. The soldier whose life was saved on a battlefield. When such a bond runs deep enough, it becomes **inheritable** — and when the character dies, that person, or even *their* descendant, may step forward to carry the story on.

The mark cannot be bought or rushed. It is earned only through choices that cost the character something real and that change the other person's life in a lasting way. A coin tossed to a beggar means nothing. Years spent raising another man's son as your own means everything.

A legacy heir is profoundly different from a blood heir, but — and this is the design's central balancing act — they are never a reset. They bring their **own** genome, their own body, rather than the lineage's optimized one; the lineage can spend Bearing to make that single heir broadly strong (the per-heir rules are detailed later in this section), but it cannot hand them the *specific*, sculpted genome that only direct descent preserves. What they do *not* lose is everything the lineage has permanently earned. The unlocked possibility space of the bloodline — every trait the family has ever unlocked, every discovery, every path opened across all of history — belongs to the *lineage*, not to any one body, and it carries forward intact through a legacy heir exactly as it would through a child. The future descendants of a legacy heir can still be born with *Restless Mind* or *Iron Constitution*, because the family long ago earned the right for those traits to exist in its blood; the legacy heir simply re-seeds that earned potential into a new genome rather than inheriting a single optimized one.

Beyond the possibility space, a legacy heir inherits the character's **knowledge, culture, reputation, and the memory of who they were** — the soldier who fell at the wall living on not in the boy's blood but in everything the boy was taught about him. And critically, legacy carries its own *compounding* resource, so that choosing it advances the lineage rather than merely preserving it. Where blood compounds the **genome**, legacy compounds **Bearing** — the lineage's accumulated renown and tradition, a parallel axis of long-term power explained in full below. Choosing legacy is choosing to *spread* a lineage rather than deepen it: trading the slow perfection of the body for reach, resilience against extinction, and a different, equally permanent kind of strength.

### What Passes, What Fades, What Transforms

Inheritance is not a single growing pile. Different things obey different laws, and understanding them is the strategic spine of the game.

Some things are **permanent**. Genetic gains, once won, belong to the bloodline and only ever change through breeding and lived experience — they cannot be stolen or lost, only redirected. The unlocked *possibility space* of the lineage — the traits, paths, and discoveries the family has earned access to — likewise never disappears.

Some things **fade**. Reputation is loud at a death and quiet a generation later; a great name unspoken will dim until it means nothing. Wealth can be squandered, stolen, taxed away, or lost to a foolish heir. Material inheritance is always at risk in the gap between one life and the next, and a lineage that lives only on its hoard will eventually find the hoard gone.

Some things **transform**. Knowledge passed to a legacy heir becomes *teaching* — slightly lossy, filtered through one mind into another, sometimes distorted, occasionally improved. Reputation, if actively kept alive by descendants who tell the story, can transform from mere memory into living **tradition** — a permanent cultural fixture of the lineage that no longer needs a single person to sustain it. The greatest legacies are the ones that complete this transformation: a deed becomes a story, a story becomes a tradition, and a tradition becomes simply *who this family is*.

### Two Axes of Power: The Mathematics of Blood and Legacy

The relationship between blood and legacy is the spine of the whole game's balance, and it rests on a single principle: **they are two different axes of permanent progression, not a strong path and a weak one.** The difference between a balanced dual-path system and a punishing one lives entirely in the numbers, so the rules that follow are stated concretely. The specific values are the implementation's chosen constants; what is fixed by the design is the set of *relationships* between them.

**Attributes and trait expression.** Every character has five base attributes — Resilience, Acuity, Creativity, Adaptability, and Temperament — each on a 0–100 scale. Traits are not free-floating bonuses; each trait has an **expression requirement** tied to an attribute, and a trait only delivers its full effect when its attribute clears a threshold. *Restless Mind* keys off Acuity; below roughly 40 Acuity it manifests only as a mild restlessness (a small flavor effect and a minor penalty to contentment), and above it the inventive bonus scales with the attribute. This requirement creates a specific failure mode that the system must guard against — an heir who has a trait unlocked but lacks the attribute to power it, a prodigy in name with a body that cannot deliver — and the Bearing rules below exist precisely to ensure that choosing legacy never *forces* that outcome.

**Blood: compounding the genome — with control.** A blood heir is generated from a blend of both parents' attributes, each child attribute drawn near the parental average with a small variance (roughly ±8) and a rare chance of a larger mutation in either direction. Careful breeding — choosing partners who are themselves strong or who carry complementary traits — lets a bloodline raise its average attributes a few points per generation, slowly concentrating excellence into the body. This is deep and powerful, and deliberately fragile: a single early death, a sterile generation, or an unlucky draw can stall or reverse the climb, and a line that breeds only for one attribute grows narrow and brittle.

The decisive thing blood offers — the thing the legacy axis can never replicate — is **control**. Because a blood heir descends directly from the character the player just lived, the player chooses the partner, sees the parents' traits, and knows exactly which strengths are being concentrated. Blood lets the player *aim*: to build a specific genome, to chase a particular trait synergy, to sculpt a line of scholars or warriors or diplomats toward an intended shape across generations. It is slow and risky, but it is *directed*. This is what keeps blood essential no matter how much Bearing a lineage accumulates, and it is the reason the two axes stay in balance rather than one swallowing the other.

**Legacy: compounding Bearing.** Bearing is a permanent, lineage-level resource — the accumulated cultural weight of every mark made, tradition founded, and deed remembered. It is earned in concrete amounts: a mark contributes Bearing scaled by its depth; founding a tradition banks a large fixed sum permanently; a remembered life adds a smaller amount at death proportional to its renown. Bearing does two things, and together they ensure the generation that follows a legacy choice begins strong rather than at rock bottom, while still never letting legacy eclipse blood.

The first, **Bearing seats a strong legacy heir — but a generic one.** A legacy heir does not arrive with a genome drawn from the general population. When the player chooses legacy, the lineage spends accumulated Bearing to raise *that single heir's* starting attributes, at a defined exchange rate (a meaningful slice of Bearing buys each point added across the heir's attributes). This is the crucial design boundary: **the Bearing boost is per-heir, not a permanent lineage modifier.** It elevates the one person being seated; it does not raise the bloodline's underlying genome, and it does not persist into that heir's own children, who are born from the heir's actual genome like anyone else. A player therefore cannot farm Bearing across many generations to inflate a permanent genetic ceiling — each legacy seating pays only for the heir in front of them, and the underlying line is exactly as strong as its real breeding made it.

The boost also, deliberately, **buys raw strength without control.** It raises attributes broadly toward a respectable level, but the player does not direct *how* — they cannot concentrate the points into one attribute, cannot hand-pick which traits the heir carries, and cannot reproduce a specific genome they had been building. A legacy heir seated on great Bearing is reliably *good*; they are never the precisely *sculpted* champion that directed blood-breeding produces. This is the deliberate division of the two axes: blood is the only path to a *targeted* genome, while Bearing is the only path to *guaranteed, risk-free* competence. A player who leans entirely on Bearing will field a long line of solid, interchangeable heirs and never the exceptional, synergistic specialist that only patient breeding creates — and the late game's hardest challenges are built to demand exactly that specialist. Neither axis dominates because they do not offer the same thing.

A lineage of great Bearing can thus always seat a capable legacy heir; a lineage of little Bearing seats a weak one, exactly as a family of no standing would. The cost of choosing legacy with no Bearing banked is a genuinely poor heir — the correct price of never having made marks.

The second, **Bearing pays out as immediate, felt power every generation.** It is not an abstract score the player accumulates toward some distant payoff. Inherited traditions grant permanent passive bonuses that apply from the heir's birth; high Bearing opens starting positions, mentors, and opportunities unavailable to the obscure; a renowned lineage's heir begins life already known, with doors open that a genetically superior but nameless character must spend a whole life prying at. The generation immediately after a legacy choice is therefore not a "fund-the-future" trough — it begins with concrete advantages in hand. The player feels powerful *in a different currency*, not powerless while saving up.

**Why weaving between them is the deep game.** Because the two axes sell different things — blood sells *control*, Bearing sells *risk-free competence* — the strongest dynasties alternate deliberately. A bloodline that has spent generations sculpting a specialized genome but now stands at the brink of extinction can spend its accumulated Bearing to seat a capable legacy heir and survive the gap, accepting that this one heir will be broadly strong rather than the precise specialist the line had been building — then resume directed breeding from that heir's children to rebuild the targeted genome over a few generations. Conversely, a lineage rich in Bearing but never carefully bred uses its open doors and inherited traditions to arrange the marriages that finally let it *aim* its genome for the first time. Choosing a legacy heir never erases the lineage's permanent progress — the possibility space and banked Bearing endure — but it does cost the player the *specific* genome they had concentrated, which only blood preserves. The strategic question is never "do I have to give up everything?" It is "can I afford to trade my sculpted line for a safe, generic one this generation, and rebuild the edge later?"

The resulting balance has a clear intended shape across a full multi-era playthrough: weaving the two axes outperforms committing to either; directed blood-breeding reaches sculpted specialists that the legacy axis cannot match; and a player who leans entirely on Bearing fields reliably competent but interchangeable heirs that hit a generic ceiling well below what blood achieves. The constants that produce this shape are a 0–100 attribute scale, a trait-expression threshold near 40, a generic Bearing ceiling around 60 against which directed breeding can push individual attributes far higher, and the collateral-heir rescue rate described in Section 7.2.

---

## 6. Progression: The March of Eras

A lineage does not merely survive across time — it climbs through it. Generational's long arc carries a family from the Stone Age through the Bronze and Iron Ages, into antiquity, the medieval world, the age of gunpowder and sail, the industrial revolution, the information age, and finally toward a speculative future of genetic mastery and the stars. This is the game's grandest form of progression, and it is the player's true measure of how far a lineage has come.

Progression runs on **two clocks**, and the relationship between them is one of the game's defining mechanics. The first clock is the **World Era** — the technological and social level of the wider world the lineage lives in. The second is the **Lineage Era** — the level the player's own family has actually attained and adopted. These two clocks are distinct, they advance by different rules, and the *gap* between them is one of the game's richest sources of drama.

**The World Era advances on its own momentum — unevenly.** The world does not wait for the player, and crucially it does not advance at a smooth, predictable rate. Most of the time it inches forward through the slow activity of neighboring peoples; but every so often it *lurches*, when a neighbor's golden age, a conquering empire, or a discovery spreading along trade routes vaults the wider world forward by a sudden leap. This unevenness is deliberate and load-bearing: a world that crept forward at a perfectly steady pace would let a lineage track it almost exactly and the gap between the clocks would never grow large enough to matter. It is the *bursts* — the times the world suddenly outruns the family — that create the dangerous, dramatic gaps the whole two-clock system exists to produce. A family can fall behind its world, and this is a real and visible state: a lineage of stone-tool hunters can find itself living at the frontier of a world that has already reached bronze, facing neighbors with better weapons, denser cities, and organized power. Falling behind is not a soft abstraction — it is a concrete disadvantage the lineage must survive or close.

**The Lineage Era advances only when the family adopts an advance for itself.** Knowing that bronze exists in the world is not the same as *working* bronze. For the lineage's own era to rise, someone in the bloodline must actually make or learn the leap — through the pivotal lives described below. The world's clock turns on its own; the family's clock turns only when the player earns it.

**The gap between the clocks drives the game.** A lineage *ahead* of its World Era is a pioneer — the first to plant seeds, the first to work iron, enjoying the enormous advantages of a discovery its neighbors lack, and able to spread or hoard it. A lineage *level* with its World Era lives in comfortable step with its time. A lineage *behind* its World Era is in danger, but not doomed: it can close the gap far faster than a pioneer ever could, because the advance already exists in the world and can be learned, traded for, married into, captured, or stolen rather than invented from nothing. This asymmetry is deliberate and merciful — pioneering is slow and precious; catching up is hard but achievable — and it is what keeps a stumbling lineage from ever being permanently locked out of history.

These three states are not a class the player chooses but a **posture they drift into**, emerging entirely from how they spend their lives. The intended shape is this: a family that consistently pushes invention leads the world only intermittently — pioneering is high-effort and the lead slips without constant work — while a family that neglects advancement spends a real share of its history behind, pressured but never permanently trapped. Most generations, for most players, are spent roughly level with the world; the pioneer's lead and the laggard's deficit are the dramatic exceptions that posture makes more or less common. "Falling behind is dangerous but never a dead end" is therefore a firm promise of the design, not a hope — which is precisely what frees the player to take the risks that make the gap dramatic in the first place.

This is why certain lives matter more than others. Most generations consolidate; they live within the world as it is. But every so often, the conditions align — either because the lineage stands at the true frontier of a new discovery, or because it finally has the chance to adopt something the wider world already holds — and a single life stands at a threshold. These are the lives the game urges the player to live slowly. The hunter who first plants a seed. The smith who first works iron. The exile who returns from a richer city having learned to read. To play one of these lives well is to advance the Lineage Era — and the player feels the weight of it, because everything afterward is built on what this one person does now.

A threshold is never staked on a single fragile life. Once the conditions for an advance exist — whether through the lineage's own accumulated knowledge or through contact with a more advanced world — the *opportunity* persists rather than vanishing with one death. If a character poised to cross a threshold dies young of plague, the opening is not lost forever; it resurfaces in a later life, perhaps delayed, perhaps less ideally placed, but never permanently foreclosed. What a premature death costs is time and advantage — and, dangerously, it may let the World Era pull further ahead in the meantime — but never the future itself.

As eras advance, the lineage's **possibility space** expands permanently. New genetic traits become available to the founding pool of future heirs. New crafts, professions, and social roles open. New kinds of choices — political, scientific, philosophical — appear that simply could not exist in an earlier age. The narrow handful of options offered at the dawn of the bloodline blossoms, across the full span of a long playthrough, into a sprawling tree of human possibility that the player has personally cultivated, generation by generation.

---

## 7. Systems

### 7.1 Genetics and Traits

Every character is the meeting point of two forces: the **bloodline genome** — the slowly evolving genetic legacy of the whole lineage — and their **own expression**, the particular way that legacy surfaces in one person, shaped by the randomness of birth and bent further by the life they live.

The genome is built from a set of underlying attributes — physical resilience, mental acuity, creativity, adaptability, and the seeds of temperament — each held as a heritable value with a small range of natural variation from parent to child. A blood heir inherits a blend of their parents' genomes, nudged by mutation and by lived experience — the only path by which the player can *aim* the genome toward a chosen shape. A legacy heir does not inherit that optimized genome; they bring their own, which the lineage can raise to a respectable level for that one heir by spending Bearing (a per-heir boost, not a permanent change to the bloodline, detailed in Section 5). What a legacy heir always inherits, regardless of that boost, is the lineage's **possibility space** — the full set of traits the family has ever unlocked — so that their own children can still be born expressing every trait the bloodline has earned. The body is a new draw; the *range of what that body can become* never resets.

Traits sit atop attributes as concrete, named expressions: *Iron Constitution*, *Quick Study*, *Silver Tongue*, *Restless Mind*. Early in a lineage's history, only the most primal traits can appear. As eras advance and the lineage accumulates the right experiences, new traits unlock into the pool from which heirs are born — the genetic vocabulary of the family growing richer the longer it endures. Some traits are gifts; some are burdens; many are both, depending on the life and the era. A *Restless Mind* is a curse for a peasant and a blessing for an inventor.

### 7.2 Relationships and the Mark System

Relationships are the most important system in Generational, because they are the only thing standing between a lineage and extinction. Every meaningful person in a character's life is tracked as a bond with a measurable depth and a particular nature — kin, friend, rival, lover, mentor, student, enemy.

Most bonds are ordinary and pass with the character's death. But a bond can deepen, through repeated, costly, life-altering interaction, into a **mark** — a relationship so significant that it becomes part of the other person's identity. The system continuously evaluates bonds against a threshold that asks, in effect: *has this character permanently changed this person's life?* Saving a life crosses it. Raising a child not your own crosses it. A single act of kindness does not. When a bond becomes a mark, that person — and potentially their own descendants — enters the pool of possible **legacy heirs**, ensuring the story can continue even if blood fails.

This system is what gives every social choice weight. The player is never merely deciding whether to help a stranger; they are deciding whether to plant a seed of their own immortality in someone else's life.

**Collateral heirs: the safety net that makes the lineage survivable.** A lineage is not a single fragile thread running through one person at a time — it is an extended family. When a character dies having secured neither a child nor a mark, the line does not automatically end: the extended family is checked for a collateral heir, a sibling's child, a cousin, a niece or nephew, or an adopted kin raised within the family. Only when no collateral heir exists either does the lineage truly go extinct. This generalizes the founding image of the design — the war-friend's son who carries a dead soldier's name forward — into the structural backbone of survival, and that backbone is essential: without a collateral net, the compounding per-generation risk of a single life failing would drive nearly every lineage to extinction within a handful of generations, long before it could climb through history. With the collateral rescue rate set so that lineages survive a full multi-era arc roughly two times in three, extinction remains a genuine threat the player can suffer but never an arbitrary wipe. A collateral heir continues the bloodline without the directed control of a chosen child, making them a survival mechanism rather than an optimization one: they keep the family alive, but the player who wants a *sculpted* line must still actively secure their own heirs.

### 7.3 Skills, Knowledge, and Craft

Over a life, a character accumulates **knowledge** — practical skills, accumulated wisdom, and learned techniques appropriate to their era. A flint-knapper's mastery, a scribe's literacy, an engineer's calculations. Knowledge is held separately from genetics, because it travels differently: blood heirs receive a strong, direct transmission of what their parents knew, while legacy heirs receive a *taught* version — filtered, slightly lossy, occasionally embellished or corrupted in the passing.

Knowledge is also the raw material of Lineage Era progression. The thresholds that let a family adopt or invent an advance are, mechanically, accumulations of knowledge crossing critical levels across multiple generations. A single brilliant life rarely carries the Lineage Era forward alone; it contributes to a rising tide that a later life finally rides over the threshold. When the family instead closes a gap to a more advanced World Era, that same knowledge accumulates faster, because it can be learned from the outside rather than invented from nothing.

### 7.4 Wealth and Material Inheritance

Wealth in Generational is deliberately precarious. A character accumulates material resources appropriate to their era — herds, land, coin, holdings, eventually corporations and beyond — and passes a portion to their heir. But the gap between lives is dangerous: wealth can be taxed, stolen, divided among rivals, squandered by a weak heir, or lost to the upheavals of a changing world. A lineage that defines itself by its hoard is always one bad generation from ruin. Wealth is a tool and an accelerant, never a foundation. The foundations are blood, knowledge, and name.

### 7.5 Reputation and Tradition

Reputation is the world's memory of the lineage, and it behaves like an echo: loud at first, fading with time unless something sustains it. A character builds reputation through deeds witnessed and remembered, and passes it to their heir as a starting standing in the world. Left untended, it decays — a great name three generations unspoken is just a name.

But reputation actively maintained can **crystallize into tradition.** When descendants keep a story alive — retelling a heroic death, honoring an ancestor's craft, upholding a founder's code — that reputation can transform into a permanent cultural fixture of the lineage, no longer dependent on any single person to carry it. Tradition is the most durable thing a lineage can own, more permanent than wealth and more resilient than reputation, because it has become part of the family's very identity. Renown and traditions together accumulate into the lineage's **Bearing** — the permanent cultural-progression axis described in Section 5 — which is what makes the legacy path a true engine of long-term growth rather than a mere safety net. Every tradition founded is Bearing banked forever.

### 7.6 World Events and the Era Engine

Around the intimate story of one life churns the wider world: harvests and famines, wars and plagues, the rise and fall of powers the lineage may never directly touch. The world generates its own pressures and opportunities, and these flow into the lives the player lives as events — the conscription that pulls a son into a war, the trade route that makes a family rich, the plague that tests a bloodline's resilience.

The era engine governs both clocks described in Section 6. It runs the **World Era** on its own autonomous schedule — a mix of slow steady progress and occasional sudden bursts, when a neighboring power's golden age or a spreading discovery vaults the wider world forward regardless of the lineage's fortunes. This unevenness is what makes the gap between the clocks meaningful: a world advancing at a perfectly smooth rate would keep the lineage tracking it too closely for the gap to generate drama, whereas an uneven world produces the divergences that define a family's story. Separately, the engine tracks the lineage's own accumulated knowledge, stability, and circumstances, and opens **Lineage Era** thresholds — the chances for the family itself to adopt or invent an advance — by surfacing pivotal opportunities in living characters' paths, with thresholds deliberately cheaper to cross when the family is behind a more advanced world (adopting existing technology) and slower when pioneering (inventing from nothing). The world turns on its own; the lineage rises only when the player carries it across each threshold. The engine's most important job is managing the gap between the two clocks, since a lineage that falls far behind its world faces escalating pressure, while a lineage that pulls ahead enjoys the spoils of a pioneer.

### 7.7 The Content Engine: Defeating Combinatorial Explosion

The single greatest production risk in a game of this scope is not technical but editorial. A naive design would demand a unique hand-written event for every intersection of era, profession, trait, and circumstance — a matrix that multiplies into the tens of thousands of cells and guarantees a stalled project. Generational's content architecture is built specifically to make that matrix unnecessary, so that a small team can produce a world that feels vast without authoring every combination by hand.

The core technique is **layered events with era-banded text, not raw slot-filling in the middle of prose.** This distinction is everything, and it is where naive parameterization fails. The brittle approach — stitching `[rival_name]` and `[challenge_method]` into a single fixed sentence — does break the literary illusion, because the human brain detects the seams within a few readings. Generational avoids this by parameterizing at the level of *structure and outcome*, while authoring the actual prose as complete, hand-written variants bound to each era band. A single logical event — "a rival challenges your standing" — is one node in the design, but its surface text is not one sentence with holes punched in it; it is a small set of fully written passages, one per era band it can occur in, each authored as natural prose for that world. The duel in the Iron Age and the smear campaign in the information age are *different written texts* sharing one underlying mechanical skeleton, not one text with the weapon swapped. The engine selects the right variant and weaves in only the lightest dynamic elements — a name, a relationship word — at natural grammatical seams where substitution is invisible, the same way a novel uses a character's name without anyone noticing the "slot."

This approach has strong precedent. Text-driven simulation games such as *Caves of Qud*, *Dwarf Fortress*, and *Wildermyth* generate enormous narrative variety from systemic content and are nonetheless celebrated for the texture and surprise of their stories. The lesson from all of them is consistent: procedural narrative reads well when the *prose* is human-written and only the *combination* is systemic, and reads badly when the prose itself is assembled from fragments at runtime. Generational commits firmly to the former.

The honest cost of this is acknowledged plainly: it trades the combinatorial *event-count* explosion for a real **writing-craft burden**. Authoring a universal beat that lands with equal weight across radically different eras is genuinely hard, and the project's single largest content investment is therefore not engineering but *writing* — a dedicated, ongoing authorial effort to produce era-band variants that each feel native to their time. The architecture makes the scope *finite and additive* rather than multiplicative, but it does not make it free. This is the correct place for an indie team to spend its scarcest resource, because the writing *is* the game.

This is reinforced by **separation of the universal from the flavor.** Most human events are universal — ambition, betrayal, love, loss, rivalry, mentorship, grief — and these recur across all of history as the same emotional beats. The mechanical skeleton of each is authored once; the era bands then supply fully written prose realizations. Adding a new era means writing a new band of prose for the existing beats, not inventing the human drama from scratch — finite, parallelizable authorial work rather than an open-ended matrix.

**Writing the gap between the clocks.** The two-clock progression model raises a specific authoring problem the standard era-band approach cannot answer on its own: what prose does the engine show when the lineage's era and the world's era diverge — a Stone Age family bargaining with an Iron Age city, or scavenging a tool centuries beyond anything they could make? An ordinary event banded to a single era fails here, because no single era describes the scene; the character's mind, vocabulary, and assumptions belong to their *own* low era, while the artifacts, dangers, and opportunities belong to the *world's* higher one. Pulling the low band renders the advanced world invisible; pulling the high band puts modern thoughts in a primitive head. Both are wrong.

The solution is to treat era-gap situations as their **own dedicated category of event, indexed by the *pair* of clocks rather than by one era.** These "contact events" are written from a fixed, deliberate point of view: always the perspective and voice of the *lineage's* era — the lower mind encountering the higher world — because that perspective is exactly where the drama lives. The Stone Age scavenger does not narrate a "rifle"; they narrate a fire-stick that kills with a thunderclap, a thing of the gods, terrifying and coveted and not understood. The prose renders the advanced artifact *through primitive eyes*, which is not a writing failure but the entire emotional point of falling behind: wonder, fear, and the vertiginous sense of a world that has outrun you. This is authored content, not runtime assembly, and it is bounded — contact events are written not for every possible pairing but in **bands of gap-magnitude** (a small gap, a moderate gap, a chasm), each capturing the felt experience of being that far behind regardless of the exact eras involved.

The scope of this content is deliberately small, because extreme era gaps are **real but rare**. Large divergences — a gap of three or more eras — arise in only a minority of playthroughs: uncommon in careful play, and reaching perhaps a fifth of runs when a player falls badly behind or takes large risks. Contact events are therefore designed as **tail content**, not a marquee system: genuinely worth authoring, because a meaningful minority of playthroughs will reach them and because they are among the most memorable moments the game can produce, but deserving only a small slice of the overall writing budget — a handful of gap-magnitude bands rather than a sprawling library. Treated this way, the era-gap mechanic is a finite, high-impact garnish: rarely seen, never forgotten, and cheap to support.

Two further mechanisms keep the world feeling fresh without proportional authoring cost. A **weighting and recency system** prevents repetition by suppressing recently seen events and favoring those that engage the current character's distinctive traits and relationships, so a *Restless Mind* and an *Iron Constitution* genuinely encounter different lives from the same library; this also stretches the perceived size of the content far beyond its raw count. And because events are **data, not code**, the library is endlessly and safely extensible — by the team during development, and through expansion packs after launch. The goal is a world whose apparent depth scales well beyond the raw content authored: a finite, human-written corpus producing a combinatorial wealth of lived, specific moments.

---

## 8. Worldbuilding

### 8.1 The World of the Lineage (Single-Player)

The world the lineage inhabits is grounded, historical, and human, and for the entire single-player campaign it is the *only* world there is. It begins in the deep past of a recognizable Earth-like world — small bands surviving against weather and want — and moves through the genuine arc of human civilization: the first settlements, the first cities, the first empires, the long medieval middle, the violent acceleration of industry, the dizzying compression of the information age, and onward toward the threshold of a space-faring future. The geography, the cultures, the conflicts, and the discoveries are drawn from the real shape of human history, reorganized into a world the player's own choices help author. Cultures rise around the lineage; some the family helps build, some it merely survives.

Crucially, there is no time travel, no science fiction, and no hidden cosmic frame anywhere in this campaign. The single-player game is a pure historical simulation of one family's passage through deep time, and it never asks the player to believe in anything stranger than ambition, scarcity, love, and consequence. Every element of this world earns its place through cause and effect. Settlements appear where rivers and resources make sense. Conflicts arise from real pressures — hunger, ambition, faith, fear. Technologies emerge in plausible sequence, each resting on what came before. The world is coherent not because it follows a script, but because it follows consequence, and the player, across a long enough lineage, becomes one of its causes. A player can begin and finish Generational here, carrying a lineage from a Stone Age campfire to the launch of its world's first true spacecraft, and experience a complete game without ever encountering what comes next.

### 8.2 The Summit: The End of the Journey

The single-player campaign culminates as a lineage reaches the summit of its world's technology — genetic self-mastery, artificial minds, and the first true ventures beyond the home world. This summit is the campaign's natural and complete endgame, the payoff for everything the player has built across the long climb from a Stone Age campfire. To carry a single thread of people across all of human history and watch them, at the last, reach for the stars is the full and finished arc of the game. There is no twist waiting beyond it and nothing the player must do afterward; reaching the summit is winning, in the only sense a game about continuation can have a victory.

At the very peak of that climb, a lineage may begin the most ambitious research its world has ever attempted — the first experimental work into the nature of time itself. Within the scope of this game, that research is the lineage's final, crowning achievement: the furthest a family can climb, the capstone of the possibility space, the last great mark a dynasty can make. It is presented as an ending, not as a doorway the player is expected to walk through.

### 8.3 Future Vision (Out of Scope)

The fiction deliberately leaves one thread loose at the summit, as a seed for the future rather than a promise of this product. The time research a lineage completes at its peak hints — only hints — that a single timeline may not be all there is, and that one day, timelines that each spent millennia believing themselves alone might touch. This is the long-horizon vision for the *Generational* universe: a possible future expansion or sequel, **Project Chronos**, in which matured lineages from many players' single-player histories meet across the fracture between worlds.

It is named here only to record the design's ultimate ambition and to ensure the single-player fiction plants its seed honestly. It is explicitly **not part of this game's scope.** No multiplayer infrastructure, netcode, server persistence, or cross-timeline systems are designed, budgeted, or promised for the product this document describes. *Generational* is, in full, a complete single-player historical roguelite that begins at a Stone Age fire and ends at the summit of a world reaching for space. The multiverse is a story for another day, and the game stands whole without it.

---

## 9. Narrative

**Premise.** You are not a person. You are a thread of people, pulled taut across the centuries — each life a single knot, each death a passing of the thread into another hand. You begin as raw genetic potential and rise, if you endure, from a Stone Age campfire to the day your lineage reaches for the stars. In between is everything: birth, work, love, war, grief, and the long, patient labor of building something that will outlast every one of the people who built it. To carry one family across all of human history, and to see them at the last touch the edge of their world's future, is the whole of the journey.

**Central conflict.** The deepest conflict in Generational is not against an enemy. It is against forgetting. Every life is a small struggle to matter enough to continue — to leave behind a child, a student, a saved life, a story worth retelling. The world is indifferent and time is corrosive; reputations fade, wealth scatters, bloodlines fail. To play is to push, life after life, against the entropy that erases ordinary people from history. Victory is not conquest. Victory is continuation.

**Character.** There is no single protagonist, and that absence is the point. The recurring character of Generational is the *lineage* itself — its accumulating traits, its hardening traditions, its name growing heavy with history. Individual characters are vivid and mortal, loved and lost in the span of a session. But the player's true relationship is with the thread that runs through all of them: the slowly emerging personality of a family that the player has shaped, knot by knot, across a thousand years.

---

## 10. Art Direction

Generational is a text-forward experience, and its visual identity should serve the written word rather than compete with it. The aim is the quiet authority of an illuminated chronicle — a sense that the player is reading a family's true history, written down and preserved across the ages.

The interface should feel like a living document: clean, literary typography that carries the bulk of the experience, framed by restrained ornamentation that *shifts with the era*. The same lineage's chronicle should look subtly different in the Stone Age than in the industrial age than in the far future — the marginalia, the textures, the typographic flourishes evolving as the family climbs through time, so that the look of the page itself becomes a record of how far the lineage has come.

Color should be muted and parchment-warm in the early eras, gradually cooling and sharpening toward the clinical precision of the future. Imagery, where it appears, should be evocative rather than literal — a sigil, a silhouette, a family tree rendered as a growing organic form — privileging mood and memory over spectacle. The single most important visual artifact is the **family tree** itself: an evolving, explorable record of every life lived, every mark left, every branch that flourished or failed. It should be beautiful enough that players want to return to it simply to remember.

**References in spirit:** the typographic restraint of *Reigns* and *Cultist Simulator*; the warmth of an old family bible's records page; the austere data-beauty of a well-kept genealogical chart.

---

## 11. Audio

Audio in Generational works almost entirely beneath conscious notice, because the player's attention belongs to the words. The score should be ambient and era-aware — sparse percussion and bone flutes in the deep past, swelling toward orchestral and then electronic textures as the lineage climbs through history. Music should mark the *eras* more than the moments, so that crossing into a new age is something the player hears as well as reads.

Ambient soundscapes ground each era's setting without demanding focus: wind and fire and distant animals in the earliest ages, the murmur of a city, the clamor of industry, the hum of machines. The most important audio is **feedback for meaning** — restrained, deliberate sounds that mark the moments the game wants the player to feel. The soft finality of a death. The warm resonance of a mark being made. The quiet, weighty tone of an era threshold crossed. These cues should be rare enough to stay powerful, so that the sound of a legacy being secured never loses its weight.

---

## 12. Technology

### 12.1 Recommended Engine

Generational is a text-and-data game, not a graphics-driven one, and its engine choice should follow from that. The dominant cost is not rendering but **systems, content, and persistence**: a large body of authored events, a simulation of heredity and relationships, and a save system robust enough to hold the full history of a lineage.

**Godot 4** (with C#) is the strongest fit. It is lightweight, free of licensing friction for an indie, has excellent UI and rich-text tooling for a text-forward game, exports cleanly to desktop and mobile, and its node-and-scene model maps well to a UI-heavy application. **Unity** (with C#) is a fully viable alternative if the team's expertise leans that way, with a more mature asset ecosystem at the cost of more overhead than this game needs. A pure-code stack (a custom engine over a framework like a web or .NET UI layer) is also defensible given how little real-time rendering the game requires — but a game engine pays for itself in tooling, input handling, and cross-platform export.

The recommendation is **Godot 4 with C#**, with the explicit understanding that the engine is the least important technical decision in the project. The architecture below is engine-agnostic by design.

### 12.2 Architecture

The cleanest way to structure Generational is to separate it firmly into three layers that know as little about each other as possible: a **simulation core** that holds all the game's truth, a **content layer** of authored events and data that feeds the core, and a **presentation layer** that renders the core's state as readable text and turns the player's taps back into commands. This separation is what keeps a content-heavy game maintainable as the event count grows into the thousands.

**The simulation core** is pure logic with no knowledge of how it will be displayed. It owns the model of a character, the bloodline genome and possibility space, the relationship and mark graph, the knowledge and reputation ledgers, the wealth state, the lineage's Bearing, and the era engine. It exposes a clean interface: feed it a choice, and it advances the world and returns what changed. Keeping this layer free of any UI or engine dependency makes it independently testable — which matters enormously for a game whose fun lives in the balance of its numbers.

**The content layer** holds the game's vast body of authored material as *data, not code*. Events, their conditions, their choices, and their consequences should live in an external, human-editable format (such as structured data files) loaded at runtime, so that writers and designers can pour in content — and balance it — without touching the simulation. A small scripting or expression system lets event conditions and outcomes reference the simulation state ("requires era ≥ Bronze; requires trait Restless Mind; on choose, +knowledge metallurgy, -wealth").

**The presentation layer** subscribes to the simulation and renders it. It holds no game truth of its own. This strict one-way flow — state lives in the core, the view only reflects it — is what makes the same game trivially portable from desktop to mobile, since only this layer changes.

A lightweight **event bus** connects the layers: the simulation emits events ("a mark was made," "an era threshold crossed," "a character died"), and the presentation and audio layers listen and react. This keeps the satisfying feedback moments decoupled from the logic that triggers them.

### 12.3 Core Data Model

At the center sits the **Character**: a current age and life-stage, an own-expression of attributes, a set of expressed traits, and references into the lineage's shared ledgers. Around it:

The **Bloodline** holds the lineage-level state that persists across all generations: the heritable genome, the permanent and ever-growing possibility space of unlocked traits, paths, and discoveries, and the accumulated **Bearing** — the cultural-progression resource spent to seat strong legacy heirs and earned through marks and traditions. These are the things that can never be lost.

The **Relationship Graph** records every meaningful bond as a typed, weighted edge, with the subset that have crossed the mark threshold flagged as inheritable. This graph is the source of truth for who may continue the lineage.

The **Ledgers** track the fading and transforming inheritances — knowledge, reputation, wealth — each with its own rules for decay, transmission, and crystallization into permanence (knowledge into teaching, reputation into tradition).

The **Era State** holds both clocks of progression — the autonomous World Era and the lineage's own Lineage Era — along with the accumulated conditions that drive each, and decides when Lineage Era thresholds open and how wide the gap between the two has grown.

The **Chronicle** is the complete, append-only record of every life ever lived in this lineage — the data behind the family tree, and the emotional payload of a long playthrough. It is written to, never overwritten, so that the full history is always recoverable and explorable.

### 12.4 The Generation Cycle in Code

The loop, expressed as the simulation's main rhythm, is straightforward. The core constructs a new character from the chosen heir. For a blood heir, it draws a genome blended from the parents (the player-directed path) and applies the lineage's possibility space; for a legacy heir, it attaches a fresh genome whose attributes are raised generically for that one heir by spending the lineage's Bearing — a per-heir boost that never alters the underlying bloodline — and carries forward the same possibility space along with the inherited ledgers, so that neither path discards the family's permanent progression, only shifts which axis it advances. It then drives that character through their life-stages, at each step selecting eligible events from the content layer (filtered by both era clocks, traits, relationships, and history), presenting them, and applying the chosen consequences back into the simulation state. Throughout, it continuously re-evaluates relationships against the mark threshold. When the player has enabled let-run, the pacing system applies the grounded/ungrounded rules — flowing freely once continuity is secured, and stopping only at continuity-bearing forks while the character remains ungrounded. On death, it weighs the life, writes the completed record into the Chronicle, and assembles the pool of eligible heirs — blood and legacy alike — for the player to choose from. If that pool is empty, the lineage is declared extinct.

Mechanically, the pivotal lives discussed earlier are produced here: when the Era State's accumulated conditions place a living character at a Lineage Era threshold, the engine injects a high-weight opportunity event into that character's stream and emits a signal on the event bus, which the presentation layer uses to invite the player to slow down and live the moment deliberately.

### 12.5 Persistence and Scalability

The save system is unusually important here, because a Generational save is not a snapshot — it is a *history*. The Chronicle grows without bound across a long playthrough, so it must be stored efficiently: completed lives can be compressed into compact summary records once they are no longer the active generation, preserving the family tree and the inheritance math while discarding the moment-to-moment detail no longer needed. The active generation is held in full fidelity; the past is held in summary. This keeps even a thousand-generation save small and fast to load.

Because the simulation core is deterministic given its state and a seeded random source, saves can be compact (state plus seed) and the game's balance can be tested by replaying histories — a significant advantage for a small team tuning a deeply systemic game.

### 12.6 Scalability of Content

The content strategy itself — era-banded authored prose over a shared mechanical skeleton — is described in Section 7.7. What matters technically is that the architecture supports it cleanly: because every event, condition, trait, and era lives in external data rather than code, the content library can grow without recompilation, writers can author and balance in parallel with engineering, and a tagging-and-condition system routes each piece automatically to the lives where it belongs. The same property makes the game expandable after launch — new eras, cultures, and event packs are content drops, not code releases — and keeps the simulation core stable no matter how large the library becomes.

---

## 13. Roadmap

**Minimum Viable Product.** The MVP exists to prove the core loop is fun in the smallest possible form: a single early era (the Stone Age through the dawn of agriculture), the full birth-live-die-inherit cycle, both inheritance paths (blood and legacy with the mark system), basic genetics and a handful of traits, the extinction failure state, and a working family-tree chronicle. If a player will happily play "just one more life" in this slice, the game works. Everything else is expansion.

**Vertical Slice.** A polished, representative wedge of the full experience: two fully realized eras with a genuine threshold crossing between them, a deeper trait and relationship system, the reputation-into-tradition mechanic, era-aware presentation and audio, and enough authored events that no two lives feel identical. This is the build that demonstrates the *feel* of climbing through history.

**Alpha.** All core systems implemented end to end across a meaningful span of eras (roughly Stone Age through a medieval or early-modern ceiling), the full inheritance and decay rules, the era engine driving pivotal lives, and a large enough event library to support long playthroughs. Feature-complete for the historical arc; rough in balance and polish.

**Beta.** Content-complete across the full historical span, balanced through iterative tuning against the project's two systems-balance models — one for the Blood/Bearing two-axis economy and extinction safety net, one for the two-clock era model and gap dynamics — which run hundreds of lineages headlessly and serve as a regression bench so that adding content never silently breaks the balance. The two-axis progression (genome and Bearing, including the genetic-floor and trait-expression math) is tuned so that blood and legacy are genuinely co-equal strategies, and the era engine is tuned so that the world-vs-lineage gap is a real but recoverable source of drama. Full UI and audio polish, save robustness proven across very long lineages, and platform parity for desktop and mobile.

**Release.** A complete, deeply replayable single-player generational roguelite carrying a lineage from the Stone Age to the summit of a world reaching for space. The game is whole and finished at this scope; it requires no online component. Post-launch, the data-driven content architecture supports ongoing single-player growth: new eras, new cultures, and new event packs that deepen the historical experience. The multiverse vision — Project Chronos — remains a possible future sequel or major expansion, to be scoped as its own project if and when the single-player game has earned it. It is deliberately excluded from this game's plan so that the project remains buildable, finishable, and excellent at the thing it actually is.

---

*A life ends. A lineage continues. The universe never forgets.*
