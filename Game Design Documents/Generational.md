---
title: "Generational"
description: "Game design document for a generational roguelite where the player does not steer a hero but tends a bloodline and its legacy across centuries of human history, from the Stone Age to the stars."
genre: "Roguelite / Life-Sim"
category: "Game Design Document"
status: "Design draft — balance constants marked [TUNING TARGET] pending model validation"
---

# GENERATIONAL
### Game Design Document

> *"A life ends. A lineage continues. The universe never forgets."*

---

## 1. Overview

**Generational** is a single-player generational roguelite built on interactive text and unfolding events. The player does not control a hero. The player tends a bloodline — and, more importantly, a legacy — as it travels across centuries of human history, from the first fires of the Stone Age toward the threshold of the future.

The whole experience is a self-contained campaign: a grounded, historical simulation of one human lineage climbing through the real arc of civilization, from the Stone Age to the dawn of a space-faring age. There is no multiplayer, no online layer, and no science fiction within the game itself — only the intimate, human story of a family across deep time, told entirely through text and choice. The design carries one distant, deliberately out-of-scope ambition for a possible future expansion — a multiverse layer called Project Chronos — but it is named only as a long-horizon vision and forms no part of the product this document describes. As designed here, *Generational* is complete and satisfying on its own.

Every run is a single human life, told through choices, encounters, and the slow accumulation of consequence. When that life ends, the game does not. What the character built, learned, and left behind passes forward — sometimes through a child of their blood, sometimes through a stranger whose life they touched so deeply that the stranger carried their name into the future. The death of one person is the birth of the next chapter, and the chain of chapters is the game.

Where most games measure progress in levels and loot, Generational measures it in inheritance. A bloodline grows stronger not because the player grinds, but because each life leaves something behind for the next to stand upon: sharper instincts in the blood, deeper knowledge in the mind, wealth in the coffers, and a name in the mouths of others.

**Genre:** Generational roguelite / narrative life-simulation
**Platform:** PC (Windows, macOS, Linux), with strong portability to mobile
**Modes:** Single-player only (a future multiverse expansion, Project Chronos, is out of scope)
**Perspective:** Intimate, character-level interactive text — each life lived up close, the lineage shaped across many
**Session shape:** Variable — a life may last minutes or hours, paced by the player
**Target audience:** Players who love *BitLife*, *Reigns*, *Crusader Kings*, *Cultist Simulator*, and the "one more turn" pull of *Civilization*; readers who want history to feel personal; people who find more drama in a family tree than in a boss fight.

**What sets it apart:** Generational treats *legacy* — not survival, not victory — as the core resource. It is the rare life-sim where dying without an heir is the true failure, and where an heir need not share your blood. The game asks a quieter question than most: not *did you win*, but *did you matter to anyone enough to be remembered*.

---

## 2. Design Pillars

Everything in this document serves four pillars. When two mechanics conflict, the pillar hierarchy decides which one yields — later, the cut-line section (Section 16) uses these same pillars to decide what dies first under schedule pressure. This list is the spine; the rest is elaboration.

**P1 — Legacy is the resource, not survival.** The core loop optimizes for *continuation and remembrance*, not for keeping one character alive. Any system that makes the player play to protect a single life rather than to invest in what outlasts it is fighting the pillar. This is why extinction, not death, is the failure state, and why a bloodline can pass through a stranger.

**P2 — Two co-equal axes of permanent power.** Blood (a *sculpted, directed* genome) and Bearing (*guaranteed, risk-free* competence and reach) are different kinds of strength, never a strong path and a weak one. The design's central balancing job is to keep them non-substitutable: blood is the only route to a targeted specialist, Bearing the only route to safe generic strength. If either can be farmed to replace the other, the pillar is broken.

**P3 — The gap between world and lineage is the drama.** Progression runs on two clocks — the world's and the family's — and the *distance* between them, not either clock alone, generates pressure and opportunity. Falling behind must always be dangerous but recoverable; pioneering must always be precious but slippery.

**P4 — Human-written prose, systemic combination.** The game reads like a chronicle because every passage is authored by a human, and feels vast because the *combinations* are systemic. The moment prose is assembled from fragments at runtime, the illusion dies. This pillar is also the project's largest cost, and the design is honest that it trades an event-count problem for a writing-craft problem rather than eliminating it (Section 8.7).

---

## 3. The Core Loop

Generational turns on a single, unbroken cycle. The player is always somewhere on this wheel, and it never stops turning until a lineage dies out entirely.

A new character is **born**, carrying inherited blood and a set of traits uniquely their own. The player guides them as they **live** — growing from child to elder, making choices at every turning point, forming bonds, taking up a craft or a cause. Throughout that life, the character has the chance to **leave a mark**: by raising a child, or by shaping another person so profoundly that the bond itself becomes inheritable. Eventually the character **dies**, and the game tallies what their life meant. From what they leave behind, an **heir** steps forward, and the player chooses who continues the story. Then the wheel turns again, atop everything the last life built.

One hard rule gives every life its quiet tension: **a lineage that leaves no one behind ends.** If a character dies having neither raised a child nor truly touched another soul — and no collateral kin of the extended family survives to carry the name — the story cannot continue. The bloodline is extinguished and the player begins again from far less. Extinction is the sole exception to the permanence described in Section 7.3: with no lineage left to hold them, even the possibility space and banked Bearing end with the family — which is exactly what makes extinction the game's one true failure state rather than a setback. The extended family is the net that keeps it rare rather than constant.

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
        │   BIRTH ──▶ LIVE ──▶ LEAVE A MARK ──▶ DEATH ──▶ CHOOSE HEIR │
        │   inherited   choices,   a child  —or—   life      blood    │
        │   self +      bonds,     a legacy      weighed      or      │
        │   ledger      craft, war  (kin/mark)              legacy    │
        └──────────────────────────────────────────────────────┼─────┘
                              ▲                                  │
                              │                                  ▼
        ┌─────────────────────┴──────────────┐     ┌────────────────────────┐
        │   PERSISTENT LINEAGE LEDGER         │     │  HEIR TYPE decides what │
        │   • Possibility space  (permanent)  │◀────│  the next life inherits │
        │   • Bearing            (permanent)  │     │ BLOOD ▸ directed genome │
        │   • Genome             (blood only) │     │   you AIM; full control │
        │   • Reputation/Wealth  (fade)       │     │ LEGACY ▸ Bearing seats  │
        │   updated at each death ────────────┼────▶│   a strong GENERIC heir │
        └─────────────────────────────────────┘     └────────────────────────┘

        ✕  No child, no mark, AND no surviving collateral kin
           →  LINEAGE EXTINCT  →  begin anew, diminished
```

---

## 4. Beginnings: The Founding Blood

Before the first life, there is no character to play. There is only potential. The player shapes the **founding blood** — the genetic seed from which an entire lineage will grow.

In these earliest moments, humanity is unrefined and the options are deliberately few. The player distributes a small pool of essence across the foundations of a person: physical resilience, quickness of mind, creative spark, capacity to adapt, and the first faint coloring of temperament. A founder who is strong but slow will sire a different history than one who is frail but brilliant. These choices are not powerful in themselves — a Stone Age body can only do so much — but they bias everything downstream, the way the shape of a riverbed decides where a river runs a thousand years later.

The narrowness is intentional, and it is a promise. Humanity earns its possibilities. Traits that cannot be chosen at the dawn of the lineage become available only after generations of lived experience unlock them. The founding blood is not where the player builds their ideal character. It is where they plant the first seed and accept that they will not live to see the tree.

---

## 5. Life: Living a Single Generation

Each life is experienced as a stream of unfolding text — moments, decisions, and reactions presented as the character moves from cradle to grave. The rhythm is closer to a novel that bends to the reader than to a simulation watched from above. Some passages pass in a sentence; others stop the world and demand a choice that echoes for generations.

A life divides loosely into seasons. In **childhood**, inherited traits settle and the first formative experiences bend the personality. In **youth**, the world opens: a craft or a calling, the first defining bonds. In **adulthood**, the stakes peak — most marks are made here, children born, reputations won and lost. In **old age**, the character reaps what they sowed, and the player begins to feel the approach of inheritance.

### 5.1 The Pacing System: Two Orthogonal Concerns

Because lives vary wildly in length and consequence, the player sets the pace. A gripping life can be **lived slowly**, every fork explored. An ordinary life can be **let run**, advancing time and resolving minor events on a light hand. The accelerated mode is not an autopilot that can blunder a lineage into extinction, and — critically — it also never quietly robs the player of the one thing that makes the blood axis meaningful: *directed breeding*.

This is the resolution of a real tension. Two different player intents both live in the flow of a life, and a naive pacing system conflates them:

- **Continuity** — avoiding extinction. Governed by whether the character has *secured an heir at all*.
- **Sculpting** — pursuing a *specific* genome. Governed by whether the player is actively trying to concentrate a trait or attribute.

The pacing system tracks these as two independent states, and let-run consults both.

**Continuity state — grounded vs. ungrounded.** A character with at least one living child, or one bond past the mark threshold, is **grounded**: their lineage has a secured path forward for as long as that child lives or that mark endures. (Grounding is evaluated on current state — if the only child dies, the character becomes ungrounded again, and the pacing system resumes its careful attention.) A character with neither is **ungrounded**, and the extinction-avoidance weight of the pacing system bears only on them. While ungrounded, let-run stops at exactly the forks the event system flags as able to *open or foreclose the character's only paths to an heir* — the courtship that could become a marriage, the apprentice who could become a mark, the dangerous venture that could kill a still-childless character. It does not stop at every social encounter. The moment continuity is secured, these stops cease entirely.

**Sculpting state — breeding intent.** Separately and optionally, the player may set a **breeding intent**: a target attribute or trait the lineage is currently trying to concentrate (e.g. "raise Acuity," "chase *Silver Tongue*"). While a breeding intent is active, let-run **always stops at partner-selection and reproduction forks, regardless of grounding.** This is the fix for the old contradiction: being grounded relaxes *survival* pressure, but it must never suppress the *optimization* decisions that are the entire point of the blood axis (P2). A player sculpting a line keeps full agency over every mating choice even when the character is safe from extinction ten times over. A player who has no breeding goal set leaves the intent empty, and let-run flows through partner choices on a light hand like any other minor event.

**The combined rule, stated once:**

| Fork type | Let-run stops when… |
|---|---|
| Pivotal / era-threshold life | **Always** (Section 6 — the whole game exists for these) |
| Continuity fork (open/foreclose the only path to an heir) | Character is **ungrounded** |
| Partner / reproduction fork | A **breeding intent is active** (any grounding) |
| Player-configured filter (major events, deaths, opportunities) | Player has enabled that category |
| Everything else (ordinary friendships, rivalries, minor bonds) | **Never** — resolved on a light hand, reported in the life-summary |

The effect is intuitive. The game pays close attention precisely while a life hangs by a thread *or* while the player is actively building something specific, and relaxes everywhere else. Most lives are grounded early and carry no breeding intent, so most acceleration is genuinely smooth — but the player who wants a sculpted dynasty is never sped past the choices that build it.

### 5.2 Two Ledgers, Every Choice

Every choice feeds two ledgers at once. One is the immediate story — who lives, who is wronged, who is loved. The other is the inheritance — what this life will be worth when it ends. A player who only chases the moment may find their character beloved and their lineage poor; a player who only optimizes inheritance may build a dynasty of cold, hollow people. The game never says which ledger to favor. That tension is the heart of playing well.

---

## 6. Progression: The March of Eras

A lineage does not merely survive across time — it climbs through it, from the Stone Age through Bronze and Iron, antiquity, the medieval world, gunpowder and sail, industry, the information age, and toward a speculative future of genetic mastery and the stars.

Progression runs on **two clocks** (P3), and the relationship between them is a defining mechanic.

**The World Era advances on its own momentum — unevenly.** The world does not wait for the player, and it does not advance smoothly. Most of the time it inches forward; but every so often it *lurches*, when a neighbor's golden age, a conquering empire, or a discovery spreading along trade routes vaults it forward. This unevenness is load-bearing: a world creeping at a steady pace would let a lineage track it almost exactly, and the gap would never grow large enough to matter. It is the *bursts* that create the dangerous, dramatic gaps. Falling behind is a concrete, visible state — a lineage of stone-tool hunters at the frontier of a bronze-working world faces neighbors with better weapons, denser cities, and organized power.

**The Lineage Era advances only when the family adopts an advance for itself.** Knowing that bronze exists is not the same as *working* it. For the family's clock to rise, someone in the bloodline must make or learn the leap, through the pivotal lives below. The world's clock turns on its own; the family's turns only when the player earns it.

**The gap drives the game.** A lineage *ahead* of its World Era is a pioneer, enjoying advantages its neighbors lack. A lineage *level* lives in comfortable step with its time. A lineage *behind* is in danger but not doomed: it can close the gap far faster than a pioneer ever could, because the advance already exists in the world and can be learned, traded for, married into, captured, or stolen rather than invented from nothing. This asymmetry is deliberate — pioneering is slow and precious; catching up is hard but achievable — and it is what keeps a stumbling lineage from ever being permanently locked out of history. *"Falling behind is dangerous but never a dead end"* is a firm promise of the design, which is exactly what frees the player to take the risks that make the gap dramatic.

These three states are a **posture the player drifts into**, not a class they choose. A family that consistently pushes invention leads only intermittently (pioneering is high-effort; the lead slips without constant work); a family that neglects advancement spends a real share of its history behind, pressured but never trapped. Most generations, for most players, sit roughly level; the lead and the deficit are the dramatic exceptions posture makes more or less common.

**Thresholds persist; they are never staked on one fragile life.** Once the conditions for an advance exist, the *opportunity* endures rather than vanishing with one death. If a character poised at a threshold dies young of plague, the opening resurfaces in a later life — perhaps delayed, perhaps less ideally placed, but never permanently foreclosed. What a premature death costs is time and advantage, and dangerously it may let the World Era pull further ahead in the meantime — but never the future itself.

As eras advance, the lineage's **possibility space** expands permanently: new genetic traits enter the pool future heirs are born from, new crafts and social roles open, new kinds of choices appear. The narrow handful at the dawn of the bloodline blossoms, across a long playthrough, into a sprawling tree of human possibility the player has personally cultivated.

---

## 7. Inheritance: The Heart of the Game

When a character dies, Generational asks the question the entire design exists to pose: **who continues?** The two paths it offers are genuinely different ways to play, and neither is a reset.

### 7.1 Blood

If the character raised children, those children are heirs. A child of the body inherits the **strongest genetic legacy** — the physical gifts and predispositions accumulated across the whole bloodline, refined or coarsened by the parent's own life — along with a share of wealth and standing. Choosing blood is choosing to *deepen* a lineage: to compound genetic advantages generation after generation.

But blood is fragile. Children die young in harsh eras. A character may never have any. And a bloodline that pursues only its own perfection grows narrow, inbred, and brittle — strong in body, perhaps, but unloved and unremembered.

### 7.2 Legacy

A character who never had children, or lost them, is not necessarily the end of anything. The deepest bonds a character forms are tracked as **marks** (Section 8.2): people whose lives were genuinely altered by the character. When a bond runs deep enough it becomes **inheritable**, and that person — or even *their* descendant — may step forward to carry the story on.

The mark cannot be bought or rushed. It is earned only through choices that cost the character something real and change the other person's life lastingly. A coin tossed to a beggar means nothing. Years spent raising another man's son as your own means everything.

A legacy heir is profoundly different from a blood heir, but never a reset. They bring their **own** genome rather than the lineage's sculpted one; the lineage can spend Bearing to make that single heir broadly strong (per-heir rules in 7.4), but cannot hand them the *specific*, sculpted genome that only direct descent preserves. What they do *not* lose is everything the lineage has permanently earned: the full **possibility space** carries forward intact through a legacy heir exactly as through a child. The future descendants of a legacy heir can still be born with *Restless Mind* or *Iron Constitution*, because the family long ago earned the right for those traits to exist in its blood — the legacy heir simply re-seeds that earned potential into a new genome.

Beyond the possibility space, a legacy heir inherits the character's knowledge, culture, reputation, and the *memory of who they were* — the soldier who fell at the wall living on not in the boy's blood but in everything the boy was taught about him. And legacy carries its own *compounding* resource: where blood compounds the **genome**, legacy compounds **Bearing**. Choosing legacy is choosing to *spread* a lineage rather than deepen it — trading the slow perfection of the body for reach, resilience against extinction, and a different, equally permanent kind of strength.

### 7.3 What Passes, What Fades, What Transforms

Different inheritances obey different laws, and understanding them is the strategic spine of the game.

**Permanent.** Genetic gains, once won, belong to the bloodline and change only through breeding and lived experience — never stolen or lost, only redirected. The unlocked *possibility space* likewise never disappears. Banked **Bearing** is permanent. The one thing that can end these gains is extinction itself (Section 3): when a lineage dies out entirely, there is no bloodline left to hold them, and they end with it.

**Fades.** Reputation is loud at a death and quiet a generation later; a great name unspoken dims until it means nothing. Wealth can be squandered, stolen, taxed, or lost to a foolish heir. Material inheritance is always at risk in the gap between lives.

**Transforms.** Knowledge passed to a legacy heir becomes *teaching* — slightly lossy, filtered through one mind, sometimes distorted, occasionally improved. Reputation actively kept alive by descendants can crystallize from mere memory into living **tradition** — a permanent cultural fixture that no longer needs a single person to sustain it. The greatest legacies complete this transformation: a deed becomes a story, a story becomes a tradition, and a tradition becomes simply *who this family is*.

### 7.4 Two Axes of Power: The Mathematics of Blood and Legacy

The relationship between blood and legacy rests on P2: **two different axes of permanent progression, not a strong path and a weak one.** The difference between a balanced dual-path system and a punishing one lives entirely in the numbers. The concrete values below are **tuning targets** and live, with their exact figures, in the central constants table (Section 15); the prose here fixes the *relationships* between them, which are what the design commits to.

**Attributes and trait expression.** Every character has five base attributes — Resilience, Acuity, Creativity, Adaptability, Temperament — each on a 0–100 scale. Traits are not free bonuses; each has an **expression requirement** tied to an attribute, and delivers its full effect only when that attribute clears a threshold. *Restless Mind* keys off Acuity; below the threshold it manifests only as mild restlessness (flavor plus a minor contentment penalty), and above it the inventive bonus scales with the attribute. This creates a specific failure mode the system must prevent — an heir with a trait unlocked but no attribute to power it, a prodigy in name with a body that cannot deliver — and the Bearing rules exist precisely to ensure legacy never *forces* that outcome.

**Blood — compounding the genome, with control.** A blood heir is generated from a blend of both parents' attributes, each child attribute drawn near the parental average with small variance and a rare chance of a larger mutation. Careful breeding — choosing partners who are strong or carry complementary traits — lets a bloodline raise its average attributes per generation, concentrating excellence into the body. This is deep, powerful, and deliberately fragile: a single early death, a sterile generation, or an unlucky draw can stall or reverse the climb, and a line bred for one attribute grows narrow and brittle.

The decisive thing blood offers — the thing Bearing can never replicate — is **control**. Because a blood heir descends directly from the character just lived, the player chooses the partner, sees the parents' traits, and knows exactly which strengths are being concentrated. Blood lets the player *aim*: to build a specific genome, to chase a particular trait synergy, to sculpt a line of scholars or warriors or diplomats toward an intended shape. It is slow and risky, but *directed*. This is what keeps blood essential no matter how much Bearing accumulates.

**Legacy — compounding Bearing.** Bearing is a permanent, lineage-level resource — the accumulated cultural weight of every mark made, tradition founded, and deed remembered. It is earned in concrete amounts: a mark contributes Bearing scaled by its depth; founding a tradition banks a large fixed sum permanently; a remembered life adds a smaller amount at death proportional to its renown. Bearing does two things.

*First, Bearing seats a strong legacy heir — but a generic one.* A legacy heir does not arrive with a population-average genome. When the player chooses legacy, the lineage spends accumulated Bearing to raise *that single heir's* starting attributes at a defined exchange rate. This is the crucial boundary: **the Bearing boost is per-heir, not a permanent lineage modifier.** It elevates the one person being seated; it does not raise the bloodline's underlying genome and does not persist into that heir's own children, who are born from the heir's actual genome like anyone else. A player therefore cannot farm Bearing across generations to inflate a permanent genetic ceiling — each seating pays only for the heir in front of them.

The boost also, deliberately, **buys raw strength without control.** It raises attributes broadly toward a respectable level, but the player does not direct *how* — cannot concentrate points into one attribute, cannot hand-pick traits, cannot reproduce a specific genome they had been building. A legacy heir seated on great Bearing is reliably *good*; never the precisely *sculpted* champion directed breeding produces. Blood is the only path to a *targeted* genome; Bearing the only path to *guaranteed, risk-free* competence. A player leaning entirely on Bearing fields a long line of solid, interchangeable heirs and never the exceptional specialist patient breeding creates — and the late game's hardest challenges are built to demand exactly that specialist. A lineage of little Bearing seats a weak heir, exactly as a family of no standing would; that is the correct price of never having made marks.

*Second, Bearing pays out as immediate, felt power every generation.* It is not an abstract score saved toward a distant payoff. Inherited traditions grant permanent passive bonuses from the heir's birth; high Bearing opens starting positions, mentors, and opportunities unavailable to the obscure; a renowned lineage's heir begins already known, with doors open that a genetically superior but nameless character must spend a whole life prying at. The generation immediately after a legacy choice is therefore not a fund-the-future trough — it begins with concrete advantages in hand. The player feels powerful *in a different currency*, not powerless while saving up.

**Why weaving is the deep game.** Because the two axes sell different things — blood sells *control*, Bearing sells *risk-free competence* — the strongest dynasties alternate. A bloodline that spent generations sculpting a specialized genome but now stands at the brink of extinction can spend Bearing to seat a capable legacy heir and survive the gap, accepting that this heir is broadly strong rather than the precise specialist the line was building — then resume directed breeding from that heir's children to rebuild the targeted genome over a few generations. Conversely, a lineage rich in Bearing but never carefully bred uses its open doors and traditions to arrange the marriages that finally let it *aim* for the first time. Choosing legacy never erases permanent progress (possibility space and Bearing endure) but it does cost the *specific* genome only blood preserves. The strategic question is never "do I give up everything?" but "can I afford to trade my sculpted line for a safe, generic one this generation, and rebuild the edge later?"

The intended shape across a full multi-era playthrough: weaving outperforms committing to either; directed breeding reaches specialists the legacy axis cannot match; a player leaning entirely on Bearing hits a generic ceiling well below what blood achieves. The constants producing this shape are consolidated in Section 15.

---

## 8. Systems

### 8.1 Genetics and Traits

Every character is the meeting point of two forces: the **bloodline genome** — the slowly evolving genetic legacy of the whole lineage — and their **own expression**, the particular way that legacy surfaces in one person, shaped by the randomness of birth and bent further by the life they live.

The genome is built from the five heritable attributes, each with a small range of natural variation from parent to child. A blood heir inherits a blend of the parents' genomes, nudged by mutation and lived experience — the only path by which the player can *aim* the genome. A legacy heir brings their own genome, raisable to a respectable level for that one heir by spending Bearing (per-heir; 7.4). What a legacy heir always inherits is the lineage's **possibility space** — the full set of traits the family has ever unlocked — so their own children can still express every trait the bloodline earned. The body is a new draw; the *range of what that body can become* never resets.

Traits sit atop attributes as concrete, named expressions: *Iron Constitution*, *Quick Study*, *Silver Tongue*, *Restless Mind*. Early on, only primal traits appear. As eras advance and the right experiences accumulate, new traits unlock into the pool heirs are born from. Some traits are gifts, some burdens, many both depending on the life and era: a *Restless Mind* is a curse for a peasant and a blessing for an inventor.

### 8.2 Relationships, Marks, and the Survival Net

Relationships are the most important system in Generational, because they are the only thing standing between a lineage and extinction (P1). Every meaningful person in a character's life is tracked as a bond with a measurable depth and a particular nature — kin, friend, rival, lover, mentor, student, enemy.

**Three tiers of person-simulation.** To keep the game rich without exploding either simulation cost or the save file, people are modeled at one of three fidelities, and a person can be promoted between them:

1. **Ordinary bond** — the cheapest tier. A name, a type, and a weight. No attributes, no independent genome, no event stream of their own. Most people a character meets live and die here, and are discarded when the character dies.
2. **Mark** — a lightweight NPC. When a bond deepens past the mark threshold, that person is fleshed out with a concrete **attribute profile and trait set**, generated *at the moment the mark forms* from their context (their origin, their era, how they entered the story). A mark does **not** get its own played life or event stream while the main character is alive — but it carries a real genome from creation. This resolves the "where does a legacy heir's genome come from" question directly: it already exists, defined the moment the person became a mark. If that mark is later chosen as a legacy heir, Bearing raises the *expression* of that existing profile (7.4) rather than conjuring attributes from nothing.
3. **Chosen heir** — full fidelity. Only the heir the player actually selects (blood or legacy) is promoted to a fully simulated, played life with a complete Chronicle record (Section 14.5). This is the single most expensive tier, and it is reserved for the one life at a time the player is actually living.

**What happens to everyone not chosen.** When a character dies and the player picks one heir, the other candidates — non-chosen blood children, non-chosen marks — do not vanish and are not fully simulated. They collapse into **collateral kin**: compact records that (a) sit as branches in the family tree and (b) feed the collateral survival net below. They never receive a played life unless the active line later dies out and one of them is drawn as the rescuing heir, at which point that single kin is promoted to full fidelity.

**The mark threshold.** The system continuously evaluates each bond against a threshold that asks, in effect: *has this character permanently changed this person's life?* Saving a life crosses it. Raising a child not your own crosses it. A single act of kindness does not. This is what gives every social choice weight: the player is never merely deciding whether to help a stranger; they are deciding whether to plant a seed of their own immortality in someone else's life.

**Collateral heirs: a survival net with player agency, not a coin flip.** A lineage is not a single fragile thread — it is an extended family. When a character dies having secured neither a child nor a mark, the line does not automatically end: the extended family is checked for a collateral heir — a sibling's child, a cousin, a niece or nephew, an adopted kin raised within the family. Only when *no* collateral heir can be found does the lineage truly go extinct.

Crucially, whether a collateral heir *is* found is **not a flat dice roll**. It is a computed survival chance driven by state the player actually shapes across their lives:

- **Living kin count** — how many collateral kin records currently exist (more branches, more chances).
- **Kin-bond investment** — whether past characters spent choices tending relationships with siblings, cousins, and extended family, rather than treating them as scenery. A family that stays close is a family that steps forward.
- **Family Bearing** — a renowned lineage draws kin willing to carry a name worth carrying; an obscure one does not.

The rescue chance is a function of these inputs (shape and weights in Section 15). The headline balance target — that lineages survive a full multi-era arc **roughly two times in three** — is the *average outcome of typical play*, not a fixed per-death coin toss. A player who neglects kin entirely can drive their real survival odds well below that; a player who invests in family and standing can push them well above it. This is the difference the old design lacked: extinction becomes something the player can see coming and work against, rather than an arbitrary wipe at the end of a long run. It remains a genuine threat, never an unearned one.

Without this net, the compounding per-generation risk of a single life failing would drive nearly every lineage to extinction within a handful of generations, long before it could climb through history. With it, extinction is rare enough to be survivable and real enough to matter.

### 8.3 Skills, Knowledge, and Craft

Over a life, a character accumulates **knowledge** — practical skills, wisdom, learned techniques appropriate to their era. Knowledge is held separately from genetics because it travels differently: blood heirs receive a strong, direct transmission of what their parents knew; legacy heirs receive a *taught* version — filtered, slightly lossy, occasionally embellished or corrupted in the passing.

Knowledge is also the raw material of Lineage Era progression. The thresholds that let a family adopt or invent an advance are, mechanically, accumulations of knowledge crossing critical levels across multiple generations. A single brilliant life rarely carries the Lineage Era forward alone; it contributes to a rising tide a later life finally rides over the threshold. When the family instead closes a gap to a more advanced World Era, that same knowledge accumulates faster, because it can be learned from the outside rather than invented from nothing.

### 8.4 Wealth and Material Inheritance

Wealth is deliberately precarious. A character accumulates resources appropriate to their era — herds, land, coin, holdings, eventually corporations and beyond — and passes a portion to their heir. But the gap between lives is dangerous: wealth can be taxed, stolen, divided among rivals, squandered by a weak heir, or lost to upheaval. A lineage that defines itself by its hoard is always one bad generation from ruin. Wealth is a tool and an accelerant, never a foundation. The foundations are blood, knowledge, and name.

### 8.5 Reputation, Tradition, and Bearing

Reputation is the world's memory of the lineage, and it behaves like an echo: loud at first, fading unless something sustains it. A character builds reputation through deeds witnessed and remembered, and passes it as a starting standing. Left untended it decays — a great name three generations unspoken is just a name.

But reputation actively maintained can **crystallize into tradition.** When descendants keep a story alive — retelling a heroic death, honoring an ancestor's craft, upholding a founder's code — that reputation transforms into a permanent cultural fixture, no longer dependent on any single person. Tradition is the most durable thing a lineage can own, more permanent than wealth and more resilient than reputation, because it has become part of the family's identity. Renown and traditions together accumulate into the lineage's **Bearing** — the permanent cultural-progression axis of Section 7.4. Every tradition founded is Bearing banked forever.

### 8.6 World Events and the Era Engine

Around the intimate story of one life churns the wider world: harvests and famines, wars and plagues, the rise and fall of powers the lineage may never touch. The world generates its own pressures and opportunities, which flow into lives as events — the conscription that pulls a son into a war, the trade route that makes a family rich, the plague that tests a bloodline's resilience.

The era engine governs both clocks. It runs the **World Era** on an autonomous schedule — slow steady progress punctuated by sudden bursts when a neighbor's golden age or a spreading discovery vaults the world forward. Separately it tracks the lineage's own accumulated knowledge, stability, and circumstances, and opens **Lineage Era** thresholds by surfacing pivotal opportunities in living characters' paths — thresholds deliberately cheaper to cross when the family is behind a more advanced world (adopting existing technology) and slower when pioneering (inventing from nothing). Its most important job is managing the gap between the two clocks, since a lineage that falls far behind faces escalating pressure while one that pulls ahead enjoys a pioneer's spoils.

### 8.7 The Content Engine: Managing Combinatorial Cost Honestly

The single greatest production risk in a game of this scope is not technical but editorial, and this section states its true shape rather than claiming it away. A naive design would demand a unique hand-written event for every intersection of era, profession, trait, and circumstance — a matrix multiplying into tens of thousands of cells and a stalled project. Generational's architecture makes that matrix *unnecessary and bounded*, but it does **not** make content cost additive. It is honest to call it what it is: the design trades a runaway event-count problem for a large, finite, budgeted **writing-craft problem** (P4). This is the project's largest single investment, and the roadmap and cut-lines are built around it.

**The core technique: layered events with era-banded prose, not runtime slot-filling.** This distinction is everything. The brittle approach — stitching `[rival_name]` and `[challenge_method]` into one fixed sentence — breaks the literary illusion, because the human brain detects the seams within a few readings. Generational parameterizes at the level of *structure and outcome* while authoring the actual prose as complete, hand-written variants bound to each era band. A single logical event — "a rival challenges your standing" — is one node mechanically, but its surface text is a small set of fully written passages, one per era band, each natural prose for its world. The duel in the Iron Age and the smear campaign in the information age are *different written texts* sharing one mechanical skeleton, not one text with the weapon swapped. The engine weaves in only the lightest dynamic elements — a name, a relationship word — at grammatical seams where substitution is invisible, the way a novel uses a character's name without anyone noticing the "slot."

**The honest math.** If there are *B* logical beats and *E* era bands, the fully-banded corpus is *B × E* passages — a **product, not a sum**. What the architecture buys is not additivity but three things that make the product *finite, tiered, and parallelizable*:

1. **Beats have era ranges, not the full span.** Most beats do not span all eras. A beat about factory labor exists only from industry onward; a beat about first-contact with agriculture is early only. The real corpus is the sum over beats of *that beat's* band count, which is far smaller than *B × E*.
2. **Two authoring tiers.** A small **spine** of high-impact beats (ambition, betrayal, love, loss, rivalry, mentorship, grief, the marks) receives full per-band treatment — these carry the emotional weight and justify the cost. A larger body of **texture** beats receives lighter treatment: fewer bands, shorter passages, or coverage of era *groups* rather than single eras. Not every beat earns a bespoke sentence in every age.
3. **Data, not code.** Every event, condition, trait, and era lives in external, human-editable data loaded at runtime. Writers author and balance in parallel with engineering, and the library grows without recompilation — during development and through post-launch content packs.

**The budget is explicit, not "infinite."** Target corpus sizes per milestone are tuning/scoping targets in Section 15 and are treated as a hard production line item. The design's claim is *not* "content is free." It is: the content scope is knowable in advance, grows by writing new bands for existing beats rather than inventing new human drama, and is the correct place for an indie team to spend its scarcest resource — because the writing *is* the game.

**Writing the gap between the clocks.** The two-clock model raises an authoring problem the standard era-band approach cannot answer alone: what prose runs when the lineage's era and the world's era diverge — a Stone Age family bargaining with an Iron Age city, or scavenging a tool centuries beyond anything they could make? Banding to a single era fails, because no single era describes the scene: the character's mind and vocabulary belong to their *own* low era, while the artifacts and dangers belong to the *world's* higher one. Pulling the low band renders the advanced world invisible; pulling the high band puts modern thoughts in a primitive head.

The solution: treat era-gap situations as their **own category of event, indexed by the *pair* of clocks**. These **contact events** are written from a fixed point of view — always the voice of the *lineage's* era, the lower mind encountering the higher world — because that perspective is where the drama lives. The Stone Age scavenger does not narrate a "rifle"; they narrate a fire-stick that kills with a thunderclap, a thing of the gods, terrifying and coveted and not understood. Rendering the advanced artifact *through primitive eyes* is not a writing failure but the entire emotional point of falling behind.

Contact events are deliberately **tail content**. Large divergences — a gap of three or more eras — arise in only a minority of playthroughs (uncommon in careful play, perhaps a fifth of runs when a player falls badly behind or takes large risks). They are authored not for every pairing but in a few **bands of gap-magnitude** (a small gap, a moderate gap, a chasm), each capturing the felt experience of being that far behind regardless of exact eras. Worth authoring — among the most memorable moments the game can produce — but deserving only a small slice of the writing budget: a finite, high-impact garnish, rarely seen and never forgotten.

**Freshness without proportional cost.** A **weighting and recency system** suppresses recently seen events and favors those that engage the current character's distinctive traits and relationships, so a *Restless Mind* and an *Iron Constitution* genuinely encounter different lives from the same library — stretching perceived size far beyond raw count. Combined with the data-driven library, the goal is a world whose apparent depth scales well beyond the content authored: a finite, human-written corpus producing a combinatorial wealth of lived, specific moments.

---

## 9. UI/UX and Interaction Flow

Generational is a text-forward game, and its usability rests on how the written stream is presented and how the player moves through it. This section defines the interaction model the presentation layer must deliver on both desktop and mobile.

### 9.1 The Life Screen — the primary surface

The default view is a single continuous **reading column**: the life's unfolding text, scrolling as time advances, with the character's current age and life-stage always visible at the top and a compact lineage status strip (era gap, Bearing, wealth band, "grounded/ungrounded" and any active breeding intent) always visible but unobtrusive.

Text arrives in two registers, visually distinguished:

- **Narration** — quiet passages that advance time and set scene. These flow past under let-run without requiring input.
- **Choice moments** — the world stops. The passage ends with 2–5 authored options presented as tappable/clickable cards. On mobile these are full-width stacked buttons (the *Reigns* lesson: a choice must be resolvable one-handed with a thumb). Long-press / hover reveals any *known* consequence hints the character would plausibly foresee; unknown consequences stay hidden.

**Pacing controls** live as a persistent, low-friction control on the life screen, not buried in a menu, because switching between "live slowly" and "let run" is a moment-to-moment decision:

- A **live / let-run toggle** with a speed setting for let-run.
- A **stop-filter** popover exposing exactly the configurable categories from Section 5.1 (major life events, pivotal opportunities, deaths), plus the read-only indicators for the automatic stops (ungrounded continuity forks; breeding-intent partner forks) so the player understands *why* the game stopped when it did.
- A **breeding-intent selector** — set or clear the current target attribute/trait. Setting an intent is the explicit signal that partner choices should always interrupt let-run; this must be one tap to reach, because it is the player's main lever over the blood axis.

### 9.2 The Inheritance Screen — the pivot

On death, the reading column gives way to the **inheritance screen**: the completed life summarized (what it built, what it left, its final reputation and the Bearing it banked), followed by the **heir pool** as a set of candidate cards — blood children and inheritable marks side by side, each showing what that choice would carry forward and, for legacy candidates, the Bearing seating cost and the resulting attribute band. This screen is where the game's central decision is made, so it must make the *difference between the two axes legible at a glance*: a blood card foregrounds the sculpted genome and control; a legacy card foregrounds Bearing spend, generic strength, and inherited traditions.

If the heir pool is empty, this screen instead runs the collateral survival check (Section 8.2) transparently — showing the living-kin count, kin-investment, and Bearing that feed the odds — so that extinction, when it comes, is legibly the consequence of prior play rather than a black-box roll.

### 9.3 The Chronicle / Family Tree — the emotional payload

The **family tree** is the second major surface and the single most important visual artifact (Section 12). It is an explorable, always-available record of every life lived, every mark left, every branch that flourished or failed. Interaction requirements:

- **Zoomable across scales** — from the whole multi-century tree down to a single life's record.
- **Two node fidelities visible** — fully-recorded played lives (the active line and any past active lines) render as rich nodes openable to their life summary; lightweight collateral kin render as slimmer branch nodes without a full record unless promoted.
- **Legacy links are first-class** — a mark that carried the line forward is drawn as a distinct kind of edge (not a blood edge), so the player can *see* where the thread passed through a stranger. This is the visual embodiment of P1 and must never be hidden.
- **Tradition and era markers** — the tree is annotated with where traditions were founded and where era thresholds were crossed, turning it into a record of *how far the lineage came*, not just *who was related to whom*.

### 9.4 Onboarding

The founding-blood screen (Section 4) doubles as onboarding: few options, low stakes, teaching the attribute model before any life is at risk. The first life is lightly rail-guided to guarantee the player experiences one full birth→live→mark→death→inherit loop before the game opens up.

---

## 10. Worldbuilding

### 10.1 The World of the Lineage (Single-Player)

The world the lineage inhabits is grounded, historical, and human, and for the entire campaign it is the *only* world there is. It begins in the deep past of a recognizable Earth-like world — small bands surviving against weather and want — and moves through the genuine arc of civilization: the first settlements, the first cities, the first empires, the long medieval middle, the violent acceleration of industry, the compression of the information age, and onward toward a space-faring threshold. Geography, cultures, conflicts, and discoveries are drawn from the real shape of human history, reorganized into a world the player's own choices help author.

Crucially, there is no time travel, no science fiction, and no hidden cosmic frame anywhere in this campaign. The single-player game is a pure historical simulation of one family's passage through deep time, asking the player to believe in nothing stranger than ambition, scarcity, love, and consequence. Settlements appear where rivers and resources make sense. Conflicts arise from real pressures — hunger, ambition, faith, fear. Technologies emerge in plausible sequence, each resting on what came before. The world is coherent because it follows consequence, and the player, across a long enough lineage, becomes one of its causes.

### 10.2 The Summit: The End of the Journey

The campaign culminates as a lineage reaches the summit of its world's technology — genetic self-mastery, artificial minds, and the first true ventures beyond the home world. This summit is the campaign's natural and complete endgame, the payoff for everything built across the long climb. To carry a single thread of people across all of human history and watch them, at the last, reach for the stars is the full and finished arc. There is no twist beyond it and nothing the player must do afterward; reaching the summit is winning, in the only sense a game about continuation can have a victory.

At the very peak, a lineage may begin the most ambitious research its world has attempted — the first experimental work into the nature of time itself. Within this game, that research is the lineage's final, crowning achievement: the furthest a family can climb, the capstone of the possibility space, the last great mark a dynasty can make. It is presented as an ending, not a doorway the player is expected to walk through.

### 10.3 Future Vision (Out of Scope)

The fiction deliberately leaves one thread loose at the summit, as a seed rather than a promise. The time research completed at the peak hints — only hints — that a single timeline may not be all there is, and that one day, timelines that each spent millennia believing themselves alone might touch. This is the long-horizon vision for the universe: a possible future expansion, **Project Chronos**, in which matured lineages from many players' single-player histories meet across the fracture between worlds.

It is named here only to record the design's ultimate ambition and to plant the single-player seed honestly. It is explicitly **not part of this game's scope.** No multiplayer infrastructure, netcode, server persistence, or cross-timeline systems are designed, budgeted, or promised for the product this document describes. *Generational* is, in full, a complete single-player historical roguelite that begins at a Stone Age fire and ends at the summit of a world reaching for space. The game stands whole without it.

---

## 11. Narrative

**Premise.** You are not a person. You are a thread of people, pulled taut across the centuries — each life a single knot, each death a passing of the thread into another hand. You begin as raw genetic potential and rise, if you endure, from a Stone Age campfire to the day your lineage reaches for the stars. In between is everything: birth, work, love, war, grief, and the long, patient labor of building something that will outlast every one of the people who built it.

**Central conflict.** The deepest conflict is not against an enemy. It is against forgetting. Every life is a small struggle to matter enough to continue — to leave behind a child, a student, a saved life, a story worth retelling. The world is indifferent and time is corrosive; reputations fade, wealth scatters, bloodlines fail. To play is to push, life after life, against the entropy that erases ordinary people from history. Victory is not conquest. Victory is continuation.

**Character.** There is no single protagonist, and that absence is the point. The recurring character of Generational is the *lineage* itself — its accumulating traits, its hardening traditions, its name growing heavy with history. Individual characters are vivid and mortal, loved and lost in a session. The player's true relationship is with the thread that runs through all of them: the slowly emerging personality of a family the player has shaped, knot by knot, across a thousand years.

---

## 12. Art Direction

Generational is text-forward, and its visual identity should serve the written word rather than compete with it. The aim is the quiet authority of an illuminated chronicle — a sense that the player is reading a family's true history, written down and preserved across the ages.

The interface should feel like a living document: clean, literary typography carrying the bulk of the experience, framed by restrained ornamentation that *shifts with the era*. The same lineage's chronicle should look subtly different in the Stone Age than in the industrial age than in the far future — marginalia, textures, and typographic flourishes evolving as the family climbs, so the look of the page itself becomes a record of how far the lineage has come.

Color should be muted and parchment-warm in early eras, gradually cooling and sharpening toward the clinical precision of the future. Imagery, where it appears, should be evocative rather than literal — a sigil, a silhouette, a family tree rendered as a growing organic form — privileging mood over spectacle. The single most important visual artifact is the **family tree** (Section 9.3): an evolving, explorable record of every life lived. It should be beautiful enough that players return to it simply to remember.

**References in spirit:** the typographic restraint of *Reigns* and *Cultist Simulator*; the warmth of an old family bible's records page; the austere data-beauty of a well-kept genealogical chart.

---

## 13. Audio

Audio works almost entirely beneath conscious notice, because the player's attention belongs to the words. The score is ambient and era-aware — sparse percussion and bone flutes in the deep past, swelling toward orchestral and then electronic textures as the lineage climbs. Music marks the *eras* more than the moments, so crossing into a new age is something the player hears as well as reads.

Ambient soundscapes ground each era without demanding focus: wind and fire and distant animals early; the murmur of a city; the clamor of industry; the hum of machines. The most important audio is **feedback for meaning** — restrained, deliberate sounds marking the moments the game wants the player to feel: the soft finality of a death, the warm resonance of a mark being made, the quiet weighty tone of an era threshold crossed. These cues stay rare enough to stay powerful.

---

## 14. Technology

### 14.1 Recommended Engine

Generational is a text-and-data game, not a graphics-driven one, and its engine choice follows from that. The dominant cost is **systems, content, and persistence**: a large body of authored events, a simulation of heredity and relationships, and a save system robust enough to hold the full history of a lineage.

**Godot 4 (with C#)** is the strongest fit — lightweight, free of licensing friction for an indie, with excellent UI and rich-text tooling, clean desktop and mobile export, and a node-and-scene model that maps well to a UI-heavy application. **Unity (with C#)** is a viable alternative if the team's expertise leans that way, at the cost of more overhead than this game needs. A pure-code stack over a web or .NET UI layer is defensible given how little real-time rendering is required — but a game engine pays for itself in tooling, input handling, and cross-platform export. The recommendation is **Godot 4 with C#**, with the explicit understanding that the engine is the least important technical decision in the project; the architecture below is engine-agnostic by design.

### 14.2 Architecture

Three layers that know as little about each other as possible:

**The simulation core** is pure logic with no knowledge of display. It owns the character model, the bloodline genome and possibility space, the relationship and mark graph, the knowledge and reputation ledgers, the wealth state, the lineage's Bearing, and the era engine. It exposes a clean interface: feed it a choice, it advances the world and returns what changed. Keeping this layer free of any UI or engine dependency makes it independently testable — which matters enormously for a game whose fun lives in the balance of its numbers.

**The content layer** holds the game's vast authored material as *data, not code*: events, conditions, choices, and consequences in an external, human-editable format loaded at runtime, so writers and designers pour in and balance content without touching the simulation. A small expression system lets event conditions and outcomes reference simulation state (e.g. `requires era ≥ Bronze; requires trait Restless_Mind; on_choose: +knowledge.metallurgy, -wealth`).

**The presentation layer** subscribes to the simulation and renders it, holding no game truth of its own. This strict one-way flow — state in the core, the view only reflecting it — is what makes the same game trivially portable from desktop to mobile, since only this layer changes.

A lightweight **event bus** connects them: the simulation emits signals ("a mark was made," "an era threshold crossed," "a character died"), and the presentation and audio layers listen and react. This keeps the satisfying feedback moments (Sections 9, 13) decoupled from the logic that triggers them.

### 14.3 Core Data Model

At the center sits the **Character**: current age and life-stage, an own-expression of the five attributes, a set of expressed traits, and references into the lineage's shared ledgers. Around it:

- **Bloodline** — lineage-level state that persists across all generations: the heritable genome, the permanent and ever-growing possibility space, and the accumulated **Bearing**. These are the things that can never be lost.
- **Relationship Graph** — every meaningful bond as a typed, weighted edge, with three fidelity tiers (Section 8.2). The subset past the mark threshold is flagged inheritable. This graph is the source of truth for who may continue the lineage and for the collateral survival check.
- **Ledgers** — the fading and transforming inheritances (knowledge, reputation, wealth), each with its own rules for decay, transmission, and crystallization (knowledge → teaching, reputation → tradition).
- **Era State** — both clocks (autonomous World Era, earned Lineage Era), the accumulated conditions driving each, when thresholds open, and how wide the gap has grown.
- **Chronicle** — the append-only record of the lineage (Section 14.5), the data behind the family tree.

### 14.4 The Generation Cycle in Code

The core constructs a new character from the chosen heir. For a **blood heir**, it draws a genome blended from the parents (the player-directed path) and applies the possibility space. For a **legacy heir**, it takes that mark's *already-existing* lightweight genome (defined at mark formation, Section 8.2), raises its attribute expression generically by spending Bearing (a per-heir boost that never alters the underlying bloodline), and carries forward the same possibility space and inherited ledgers — so neither path discards the family's permanent progression; it only shifts which axis advances.

It then drives that character through their life-stages, at each step selecting eligible events from the content layer (filtered by both era clocks, traits, relationships, history, and the weighting/recency system), presenting them, and applying chosen consequences back into state. Throughout, it re-evaluates relationships against the mark threshold and promotes bonds between fidelity tiers as they deepen.

Under let-run, the pacing system applies the Section 5.1 rules: it flows freely while the character is grounded and no breeding intent is active, stops at continuity forks while ungrounded, and stops at partner/reproduction forks whenever a breeding intent is set. Pivotal lives always interrupt: when the Era State's accumulated conditions place a living character at a Lineage Era threshold, the engine injects a high-weight opportunity event and emits a bus signal the presentation layer uses to invite the player to slow down.

On death, it weighs the life, banks Bearing, writes the completed record into the Chronicle, and assembles the heir pool — blood and legacy alike. If that pool is empty, it runs the collateral survival check (Section 8.2), and only if that fails does it declare the lineage extinct.

### 14.5 Persistence and Scalability

A Generational save is not a snapshot — it is a *history* — so the Chronicle must be stored efficiently, and its growth is bounded by the fidelity tiers of Section 8.2:

- **The active generation** is held in full fidelity.
- **Past played lives** (the active line's ancestors, and any past active lines) are compressed into compact summary records once no longer current — preserving the family tree and the inheritance math while discarding moment-to-moment detail.
- **Collateral kin** are never full lives; they persist as lightweight stubs feeding the family tree and the survival net.

This tiering is what keeps even a thousand-generation save small and fast to load: only *one* life at a time is ever fully simulated, and the past collapses into summary behind it.

Because the simulation core is deterministic given its state and a seeded random source, saves can be compact (state plus seed), and the game's balance can be tested by replaying histories — a significant advantage for a small team tuning a deeply systemic game, and the mechanism behind the headless balance models in Section 16.

### 14.6 Scalability of Content

The data-driven content model (Sections 8.7, 14.2) has one technical consequence worth stating on its own: a tagging-and-condition system routes each authored piece automatically to the lives where it belongs, so the simulation core never needs to know how large the library has grown. This is what lets content scale — during development and through post-launch packs — without ever touching or destabilizing the core.

---

## 15. Balance Constants (Tuning Targets)

All numeric balance values live here, in one place, so the prose above can commit to *relationships* between systems without pretending any specific figure is final. Every value below is a **tuning target**, to be validated and adjusted against the headless balance models (Section 16). They are starting points for iteration, not shipped decisions.

### 15.1 Attributes and traits

| Constant | Target value | Notes |
|---|---|---|
| Attribute scale | 0–100 | Five attributes: Resilience, Acuity, Creativity, Adaptability, Temperament |
| Trait-expression threshold | `[TUNING TARGET ~40]` | Below: flavor + minor penalty; above: effect scales with attribute |
| Blood inheritance variance (per attribute) | `[TUNING TARGET ±8]` | Child attribute drawn near parental average |
| Large-mutation chance | `[TUNING TARGET, rare]` | Larger jump in either direction |
| Directed-breeding gain ceiling | Well above generic ceiling | Individual attributes pushable far past 60 with patient breeding |

### 15.2 Bearing and legacy seating

| Constant | Target value | Notes |
|---|---|---|
| Generic Bearing seating ceiling | `[TUNING TARGET ~60]` | Per-heir attribute band Bearing can buy; deliberately below sculpted-blood peaks |
| Bearing → attribute exchange rate | `[TUNING TARGET]` | Bearing spent per attribute point added to a single seated heir |
| Bearing per mark | Scaled by mark depth | `[TUNING TARGET]` |
| Bearing per tradition founded | Large fixed sum, permanent | `[TUNING TARGET]` |
| Bearing per remembered life at death | Smaller, ∝ renown | `[TUNING TARGET]` |
| Seating boost persistence | **Per-heir only** | Never alters bloodline genome; never inherited by that heir's children |

### 15.3 Survival net (collateral rescue)

| Constant | Target value | Notes |
|---|---|---|
| Full-arc survival rate (typical play) | `[TUNING TARGET ~2/3]` | *Average* outcome, not a per-death coin flip |
| Rescue-chance inputs | Living-kin count, kin-bond investment, family Bearing | Player-influenced; formula shape `[TUNING TARGET]` |
| Minimum floor / maximum ceiling on rescue chance | `[TUNING TARGET]` | Neglect can drop it well below average; investment can raise it well above |

### 15.4 Era engine

| Constant | Target value | Notes |
|---|---|---|
| World Era baseline drift | Slow steady | `[TUNING TARGET]` |
| World Era burst frequency / magnitude | Occasional, large | `[TUNING TARGET]` — must be big enough to open real gaps |
| Threshold cost — pioneering (invent) | High | `[TUNING TARGET]` |
| Threshold cost — adopting (behind a richer world) | Lower | `[TUNING TARGET]` — the "catch-up is achievable" promise |
| "Large gap" definition | ≥ 3 eras | Reached in `[TUNING TARGET ~1/5]` of runs |

### 15.5 Content corpus (production scoping)

These are **production line items**, not gameplay constants, and are the primary schedule risk (Sections 8.7, 16).

| Corpus element | MVP target | Full-game target | Notes |
|---|---|---|---|
| Spine beats (full per-band treatment) | `[TUNING TARGET]` | `[TUNING TARGET]` | Highest-craft authoring |
| Texture beats (lighter / era-grouped) | `[TUNING TARGET]` | `[TUNING TARGET]` | Fewer bands per beat |
| Era bands covered | 1–2 | Full historical span | Adds one band per existing spine beat per new era |
| Contact-event gap bands | 0 (post-MVP) | ~3 (small / moderate / chasm) | Tail content; small slice of budget |

---

## 16. Scope, Risks, and Cut Lines

This section names what can be cut under schedule pressure without breaking the pillars (Section 2), and what cannot. It exists so that a hard deadline forces a *deliberate* cut rather than a panicked one.

### 16.1 Load-bearing — cannot be cut without breaking a pillar

- **Both inheritance axes with real trade-offs (P2).** Shipping only blood, or only Bearing, or shipping them as strong-path/weak-path, destroys the central design. If only one axis can be tuned to feel good, the game is not this game.
- **The mark system and collateral survival net (P1).** Without inheritable marks, legacy is impossible; without the player-influenced survival net, extinction is either arbitrary (feels unfair) or absent (removes the stakes). The net's *player-agency inputs* are what make it more than a coin flip and must ship with it.
- **Two clocks with an uneven world (P3).** A single progression clock, or a smoothly-advancing world, collapses the gap that generates the drama.
- **Human-written era-banded prose for the spine beats (P4).** The spine is the emotional core; it cannot be replaced with runtime slot-filling without killing the chronicle feel.

### 16.2 Reducible — can be scoped down, in this order

1. **Contact events (era-gap content).** Tail content by design. Can ship absent in MVP and thin in v1; the gap still functions mechanically, it is only less richly narrated.
2. **Texture-beat breadth.** The number of texture beats and their per-era band coverage is the largest flexible content lever. Cut here before touching spine quality.
3. **Era count.** Ship fewer fully-realized eras rather than many shallow ones. The loop must be proven across at least one genuine threshold crossing (vertical slice), but the full Stone-Age-to-summit span can be delivered incrementally, including post-launch.
4. **Presentation richness of the family tree.** The tree must exist and show legacy links (P1); its zoom depth, annotations, and era-shifting ornamentation can be staged.
5. **Audio feedback breadth.** The three signature cues (death, mark, threshold) are load-bearing; ambient era beds can be reduced.

### 16.3 Primary risks

- **Content-craft burden (highest risk).** Per Section 8.7, corpus cost is a product, not a sum. Mitigation: strict spine/texture tiering, explicit corpus budgets (Section 15.5), data-driven authoring so writing runs parallel to engineering from day one, and treating writing headcount as a first-class production concern rather than an afterthought.
- **Two-axis balance (P2) collapsing into a dominant path.** Mitigation: a dedicated **headless balance model** for the Blood/Bearing economy and the survival net, replaying hundreds of lineages against the deterministic core (Section 14.5) as a regression bench, so that no content or tuning change silently makes one axis strictly better.
- **Gap dynamics (P3) feeling either trivial or unrecoverable.** Mitigation: a second headless model for the two-clock system, tuning burst frequency/magnitude and adopt-vs-pioneer threshold costs until "behind is dangerous but recoverable" holds across many runs.
- **Pacing acceleration frustrating sculpting players.** Mitigation: the breeding-intent system (Section 5.1) is itself the mitigation; it must be validated in playtest that a sculpting player never feels sped past a mating choice, and a survival player never feels nagged by breeding stops they did not ask for.

---

## 17. Roadmap

**Minimum Viable Product.** Prove the core loop is fun in the smallest form: a single early era (Stone Age through the dawn of agriculture), the full birth-live-die-inherit cycle, **both** inheritance paths (blood and legacy with the mark system and the survival net), basic genetics and a handful of traits, the extinction failure state, the breeding-intent pacing control, and a working family-tree chronicle. If a player will happily play "just one more life" in this slice, the game works.

**Vertical Slice.** A polished, representative wedge: two fully realized eras with a genuine threshold crossing between them, a deeper trait and relationship system, the reputation-into-tradition mechanic, era-aware presentation and audio, and enough authored spine content that no two lives feel identical. This build demonstrates the *feel* of climbing through history — and validates that the two-clock gap produces drama.

**Alpha.** All core systems implemented end to end across a meaningful span (roughly Stone Age through a medieval or early-modern ceiling), the full inheritance and decay rules, the era engine driving pivotal lives, the first contact events, and an event library large enough for long playthroughs. Feature-complete for the historical arc; rough in balance and polish.

**Beta.** Content-complete across the full historical span, balanced through iterative tuning against the two headless balance models (the Blood/Bearing economy plus survival net, and the two-clock gap model) run as regression benches so adding content never silently breaks balance. Blood and legacy tuned to genuine co-equality (P2); the gap tuned to real-but-recoverable drama (P3). Full UI and audio polish, save robustness proven across very long lineages, platform parity for desktop and mobile.

**Release.** A complete, deeply replayable single-player generational roguelite carrying a lineage from the Stone Age to the summit of a world reaching for space. Whole and finished at this scope; no online component required. Post-launch, the data-driven architecture supports ongoing single-player growth: new eras, cultures, and event packs. The multiverse vision — Project Chronos — remains a possible future sequel or major expansion, scoped as its own project if and when the single-player game has earned it, and deliberately excluded from this plan so the project stays buildable, finishable, and excellent at the thing it actually is.

---

*A life ends. A lineage continues. The universe never forgets.*
