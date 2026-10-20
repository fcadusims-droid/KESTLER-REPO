# Driving and Damage

## One driving model

A single simcade physics model governs every event in both halves of the game.

**Simulated with weight:**

- Mass distribution and its effect on rotation
- Weight transfer under braking, acceleration and lateral load
- Drivetrain layout (FWD / RWD / AWD) as a genuine behavioural difference
- Tyre grip as a function of compound, surface and load
- Aerodynamic downforce and drag, scaling with the square of velocity and becoming handling-relevant above roughly 140 km/h
- Power delivery curves, including turbo lag and supercharger linearity

**Abstracted everywhere:**

- Fuel is not modelled anywhere in the game.
- Mechanical failure from abuse never occurs mid-event.
- Recovery from a spin is more forgiving than a simulator would allow.

**Nothing in the physics model changes between city and festival.** A car that oversteers on a wet industrial road oversteers on a wet circuit, and the player's driving skill transfers to the festival completely.

## The simulation layer

**The handling model is identical in both halves; the simulation layer on top of it is not.** The city is arcade. The festival is *more* simulated, not fully simulated: it tracks more of the car's condition while it is driven, calibrated to races that last minutes rather than hours. It is not an attempt to be Gran Turismo or Forza Motorsport.

| | City | Festival |
|---|---|---|
| **Handling model** | Identical | Identical |
| **Tyre temperature** | Not simulated | Simulated. Cold tyres are slower through the opening lap; overdriving them costs grip. |
| **Tyre wear** | Not simulated | A gradual fade, not a cliff. Meaningful in long Sprints, marginal in a three-lap circuit race. |
| **Brake temperature** | Not simulated | Long formats only. Sustained heavy braking fades the brakes, and they recover. |
| **Fuel** | Not modelled | Not modelled. No fuel load, consumption or saving. |
| **Pit stops** | None | None. Every festival event runs green to chequered in a single stint. |
| **Damage during an event** | Visual only; no performance effect | Aerodynamic, mechanical and alignment damage degrade the car in real time |
| **Damage after an event** | Persists; costs money to repair | Persists; repaired by the discipline's mechanic |
| **Restarts** | Freely available, except in [Invitationals](street-events.md#invitationals) | Not available inside a session |
| **Setup** | Simplified presets plus manual tuning | The mechanic supplies a working baseline; the player adjusts a short list of meaningful values ([Mechanics](../festival/mechanics.md)) |
| **Regulation** | None ([Street culture](../world/street-scene.md#street-culture)) | Scrutineered before the event, spot-checked after ([Regulations](../festival/regulations.md)) |

**Where the line is drawn.** The festival simulates **what a driver can feel and act on from inside the car during the race**. It does not simulate what a professional engineering department would manage around the race.

| Simulated | Deliberately absent |
|---|---|
| Tyre temperature and the grip window | Fuel load, consumption and saving |
| Gradual tyre fade over a long run | Pit stops, stop windows, undercuts |
| Brake fade in the long formats | Tyre-change decisions |
| Live damage effects | Telemetry screens, data logging, engineer callouts |
| Slipstream | Balance-of-performance adjustment |
| Surface condition and weather | Component wear across a season |

**Strategy happens on the track, not on a pit wall.** The player never opens a strategy menu, chooses a stint plan, or watches a race from a timing screen. Every decision is made at speed with hands on the wheel ([Season](../festival/season.md#what-strategy-means)).

**Why it is split this way.** The city is where the protagonist is comfortable, and the game lets the player be comfortable there: get in, drive, win, leave; nothing is measured except whether you were first. The festival measures whether the tyres are ready, whether the contact was yours, whether the car was legal, and it measures in public. The step up is real and meant to be felt — but it is a step up in what the driver manages, not in what a team of engineers models.

Neither layer is the "real" one. The city is not a tutorial for the festival, and the festival is not the game's true form. They are two different relationships with the same car.

## Damage

Damage is persistent and visible everywhere, and never destructive. A car cannot be written off, totalled, or removed from the garage by impact; at worst it becomes badly beaten and expensive to restore.

### Damage in the city

Damage is **visual only during an event**. Panels deform, paint scars, glass cracks, bumpers hang off, and the car drives exactly as before. A street race is not decided by a dented wing.

Damage **persists after the event and costs money to repair**. It shows on the car in the world, at night meets, in magazine shoots, and in NPC reactions to the build. A player who races dirty drives a visibly wrecked car around a city that judges cars.

| Damage | City effect |
|---|---|
| Cosmetic | Visible. Reduces [Presentation](cars-and-building.md#presentation). |
| Aerodynamic | Visible. Reduces Presentation. No performance effect. |
| Mechanical | Visible under the hood. Reduces Presentation. No performance effect. |
| Alignment | Visible in stance. Reduces Presentation. No performance effect. |

### Damage in the festival

Damage is **live**. Aerodynamic damage costs downforce and adds drag; a frontal impact reduces power delivery and cooling; a heavy lateral hit introduces steering pull and uneven grip. All of it applies immediately, for the rest of the session, with no restart available.

This makes the festival's conduct multiplier ([Scoring](../festival/rank-and-championship.md#scoring)) bite twice: contact costs points *and* lap time in the same incident.

### Repair

- **In the city**, repair is done at any shop and costs money, scaling with damage severity and the value of the parts affected. Shop Standing applies to repair pricing and credit exactly as it does to parts ([Shops and credit](relationships.md#shops-and-credit)).
- **In the festival**, repair between rounds is handled by the discipline's mechanic, at a cost and speed set by their Expertise ([Mechanics](../festival/mechanics.md#expertise)).

**This is the mechanical consequence of Hostile Standing.** A racer who rams the protagonist for an entire event produces a repair bill in the city and a lost result in the festival. Relationships have a running cost, paid in a different currency on each side of the map.
