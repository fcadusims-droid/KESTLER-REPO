# Cars and Building

## Vehicle classes

Every car carries a **class**, assigned automatically from a computed performance index. The index is derived from power-to-weight ratio, drivetrain layout, aerodynamic load, tyre specification and braking capability — not from purchase price.

| Class | Name | Typical machinery |
|---|---|---|
| **D** | Street | Stock economy cars, base compacts, unmodified daily drivers |
| **C** | Tuner | Hot hatches, entry-level sport compacts, lightly built coupés |
| **B** | Sport | Sports coupés, muscle cars, seriously built compacts |
| **A** | Performance | High-end sports cars, heavily built B-class machinery |
| **S** | Supercar | Road-going supercars |
| **X** | Hypercar | Road-going hypercars and the most extreme builds in the game |

**Every car in the game is a road car.** There is no competition machinery anywhere: no GT cars, prototypes, single-seaters or purpose-built race chassis. The city sells road cars, and the festival is contested in road cars built for competition. Class X is the ceiling, and its ceiling is a hypercar with a number plate.

**Class is earned, not bought.** Installing parts raises the index; when it passes a class ceiling, the car moves up a class. A fully built C-class tuner becomes a B-class car and races B-class fields; it does not become an unbeatable C-class car.

**One index governs every restriction.** Crews use it to gate district events ([Street scene](../world/street-scene.md#territorial-rule)) and the festival uses it to assign competition classes ([Regulations](../festival/regulations.md#performance-classes)). Both read the same number.

**A car can be detuned.** Parts can be removed or swapped down to bring a car back under a class ceiling. This is legitimate: a B-class car at the top of its class beats an A-class car at the bottom of its own, and detuning is how a player enters a restricted event with a chassis they have over-built.

## Performance

Tunable systems: engine internals; forced induction (turbo and supercharger, with distinct delivery characteristics); suspension geometry and damping; brakes; tyre compound; transmission and individual gear ratios; differential; aerodynamics; exhaust; weight reduction; nitrous.

Every performance change has a corresponding behavioural change in the physics model. There is no purely numerical upgrade.

## Customisation

Customisation is deliberately total. The reference point is *Underground 2*: a car is not a stat block with a paint option but an object assembled from the engine bay to the boot, and most of what is installed is visible.

| Area | Contents |
|---|---|
| **Body** | Front and rear bumpers, hoods, side skirts, fenders, wide-body kits, spoilers and wings, roof scoops, mirrors, door handles, splitters, diffusers, exhaust tips, roof racks, hood pins, window tint. |
| **Finish** | Paint in gloss, matte, satin, metallic, pearl, candy, chrome and raw. Two-tone and multi-panel schemes. A vinyl and decal editor with layering, scaling, rotation, mirroring and per-layer colour. Livery import from the player's own saved designs. |
| **Lighting** | Headlight and taillight units, bulb colour and temperature, fog lamps, light bars, underglow neon, wheel-well neon, interior neon. |
| **Wheels and stance** | Wheel design, diameter, width, offset, tyre profile, brake caliper colour, ride height, camber, toe, track width. Stance is visible and physically real: the setting that produces the look changes how the car behaves. |
| **Interior** | Seats, harnesses, roll cage, steering wheel, shift knob, pedals, gauge cluster, dashboard trim, door cards, upholstery material and colour, headliner, floor mats, interior lighting. |
| **Engine bay** | Visible dress-up: intake piping, filters, valve covers, strut braces, radiator and intercooler hardware, wiring routing, painted and polished components. An engine swap is visible when the hood opens. |
| **Audio and boot** | Full boot build-outs in the *Underground 2* idiom: subwoofers, mid-range speakers, amplifiers, LCD screens, displayed nitrous bottles, wiring and trim panels, boot neon. Multiple boot layouts per car with different slot arrangements, including a custom layout with the largest display slots. |

## Presentation

Every build carries a **Presentation** rating from 1 to 6, computed from the visual and interior work installed: bodywork, finish, wheels and stance, interior, engine bay and boot all contribute. Damage reduces it ([Damage](driving-and-damage.md#damage-in-the-city)), and so does outdoor storage ([Property](property.md#indoor-and-outdoor-space)).

Presentation feeds three systems:

- **Riverside entry** — the Riverside check reads it alongside its coherence list ([Street scene](../world/street-scene.md#riverside--riverside)).
- **Magazine features** — magazines only approach cars above a Presentation threshold ([Magazines](magazines-and-photo-mode.md)).
- **Night meet dialogue** — NPC reactions to the car scale with it.

**Audio and interior parts cost weight.** A full boot build with subwoofers, amplifiers and screens adds real mass, carried high and behind the rear axle — the worst place in the car for it. The physics model simulates this: the balance shifts rearward, direction changes slow, and turn-in gets lazier.

A 6-Presentation show car can therefore be measurably slower than the same chassis stripped. Riverside and the magazines want one thing; the Old Guard's stopwatch wants the other; and moving one car between the two states costs days and labour ([Blueprints](#blueprints)). The player chooses which of the two a car is *for this week*, rather than toggling between them.

**Presentation does nothing in the festival.** It is not scored, read or referenced, and most of what produces it is prohibited there ([Regulations](../festival/regulations.md#visual-and-interior-regulations)). The rating exists entirely inside the city, the only place that cares what a car looks like.

## Cultural fit

Each district's culture has a recognised build language. A car built in a district's idiom is recognised by that district's NPCs: arriving at a Ridgeline meet in a coherent drift build produces different dialogue than arriving in an untouched showroom car.

Cultural fit gates no content. It lets the player's build speak in conversation without the player having to say anything.

## Blueprints

A **Blueprint** is a complete saved specification of a car: every installed performance part, tuning value, visual modification, paint, vinyl layout, wheel choice, ride height and alignment setting. Each car in the garage can hold several.

**Switching Blueprints is not a menu action.** Parts are physical objects that come off the car and go back on it. Times are in-game days on the running clock, and the car is unavailable until the work is done:

| Switch | Cost |
|---|---|
| Tuning values only — dampers, alignment, gearing, pressures | Free, instant |
| Wheels, tyres, minor bolt-on parts | 1 day, small labour charge |
| Body kit, aero, interior, boot build | 2 days, significant labour charge |
| Engine, forced induction, drivetrain | 3 days, heavy labour charge |

Labour is charged by the shop doing the work, at its rates and credit terms ([Shops and credit](relationships.md#shops-and-credit)), or by the discipline's mechanic during a festival season ([Mechanics](../festival/mechanics.md)). Workshop time runs on the game clock ([Time](time.md#what-takes-time)).

**This is what makes the Presentation trade-off real.** A show build and a race build are two states of one physical car. Owning both configurations is cheap; *being in both* is not. A player who wants to shoot a magazine cover on Tuesday and run an Old Guard circuit on Wednesday needs two cars, not two Blueprints.

Blueprints are also the unit of the game's online layer ([Blueprint Network](blueprint-network.md)).
