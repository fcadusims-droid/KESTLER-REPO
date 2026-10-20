---
section: "03 · Systems"
description: "The asynchronous online layer: sharing, applying, crediting and endorsing Blueprints."
order: 21
---

# Blueprint Network

## Principle

**The game has no competitive multiplayer**: no lobbies, no matchmaking, no real-time races against other players, no ghosts of other players on track, no shared world instances.

Its online layer is asynchronous and cooperative, in the *Death Stranding* sense: players are never present in each other's games, but the work they do persists and can be inherited by strangers. Player A builds a car. Player B, playing alone weeks later, downloads that build and races it. They never meet, never speak and never compete.

**Why it fits this game.** It is about a solitary protagonist who is good at exactly one thing, building cars, and who spends the story unable to ask anyone for help with what is actually wrong with him. The online system does the inverse: it lets players help each other with the one thing that can be handed over.

## What is shared

Only [Blueprints](cars-and-building.md#blueprints). No save data, money, progress or cars are transmitted.

A downloaded Blueprint is a **specification, not a car.** It tells the receiving game what the build is. It does not grant the chassis or the parts.

## Applying a downloaded Blueprint

The receiving player must:

1. **Own the same chassis.** Blueprints are chassis-locked.
2. **Own or buy every part it specifies.** The game shows a full parts manifest with a total cost and a single purchase action. Parts already owned are not charged again.
3. **Have the parts unlocked.** Parts gated behind city progression cannot be acquired early by downloading a Blueprint that uses them.

Once applied, the build is fully editable: a starting point, not a locked configuration.

**Blueprints transfer knowledge, never progress.** A new player can download the best drift setup in the game and still has to earn the car and the parts. Nothing is skipped except the trial and error of finding which damper setting works.

## Attribution and lineage

Every Blueprint permanently carries its author's name.

When a player sets a personal best, wins a festival event or takes a district using a downloaded Blueprint, the author's name is shown alongside the result. If that player modifies the build and re-uploads it, the new Blueprint credits both the original author and the editor.

Builds therefore accumulate **lineage**: a visible chain of everyone who touched a setup before it reached the current player. A drift Blueprint five revisions deep carries five names.

## Endorsements

The single unit of player-to-player feedback. There is no rating scale, no downvote and no comments: a player endorses a build or does not.

An endorsement:

- raises the author's **Builder Rank**;
- makes the Blueprint appear more often in other players' garage feeds;
- keeps the Blueprint in circulation longer. Builds nobody uses fall out of the feed over time; builds that keep being used persist indefinitely.

**Builder Rank has no effect on the single-player game.** It grants no money, parts, cars, REP or festival Rank. It is a reputation that exists entirely outside the protagonist's world and entirely between players.

## Where Blueprints appear

Always optional and never intrusive:

- **Garage feed.** When the player owns a chassis, community Blueprints for it can be browsed and filtered by discipline, class legality and endorsement count.
- **Shop terminals.** Independent shops display community builds that use parts they stock.
- **Festival registration.** When registering for a discipline, the game offers community Blueprints that are *legal for that class and regulation set* ([Regulations](regulations.md)) — the most practically useful surfacing point, and the one most likely to rescue a player whose team has nobody in the top eight of a weak discipline.

## Offline

The entire game is playable offline with no feature loss. Blueprints authored offline are queued and uploaded on the next connection. No content, event, car, part or ending is gated behind the online layer.
