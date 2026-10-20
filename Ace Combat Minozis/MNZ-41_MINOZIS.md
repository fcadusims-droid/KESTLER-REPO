---
section: "04 · Technology"
order: 21
---

# MNZ-41 "MINOZIS"

| Field | Data |
|---|---|
| Type | Heavy neural-integrated interceptor; strategic cyber-kinetic platform |
| Origin | Yuktobanian Aerospace Development Bureau; Directorate Zimniy black program |
| AI system | MINOZIS (Military Neural Optimization Zone Intelligence System) |
| Stated purpose | Pilot assistance, predictive threat assessment, sensor fusion, cognitive load reduction |
| Hidden purpose | Autonomous strategic assassination under OPERATION WINTER KING |
| Designation from May 2028 | POSTHUMUS (Yuktobanian Internal Security) |

Related: [COFFIN, ENSI and Wetware](COFFIN_ENSI_AND_WETWARE.md) · [MINOZIS Intelligence](MINOZIS_INTELLIGENCE.md) · [Cyber-Kinetic Warfare](CYBER_KINETIC_WARFARE.md) · [MINOZIS Encounter Design](MINOZIS_ENCOUNTER_DESIGN.md)

---

## 1. Airframe

Blended wing-body with canted vertical stabilizers, internal weapon bays and hybrid stealth optimized for high-speed interception rather than deep penetration. The COFFIN cockpit is a sealed shell with no canopy.

| Specification | Value |
|---|---:|
| Length | 24.2 m |
| Wingspan | 16.8 m |
| Height | 5.7 m |
| Empty weight | 23,000 kg |
| Maximum takeoff weight | 48,000 kg |
| Primary fuel | Slush hydrogen; liquid hydrogen compatible |
| Operational ceiling | 25,000 m |
| Ballistic zoom ceiling | 35,000 m |

Low-observable features: blended surfaces, internal bays, metamaterial radar-absorbent skin, exhaust heat exchange and active plasma modulation.

### Repair history

Four years of field repair have degraded the stealth geometry. Non-standard replacement panels, fabricated at compromised manufacturing nodes and fitted by compromised facility robotics, create radar cross-section hotspots at specific aspects. The Morgenstern engagement of 17 August 2028 damaged the port wing leading edge and one intake assembly. The repaired port structure is asymmetric, and Katya Belyaeva's fatigue analysis in 2029 identifies its panel line as the airframe's most probable structural failure point under thermal shock.

## 2. Propulsion

Two modified R-579-300M "Peregrine" variable-cycle turbofans with magnetohydrodynamic augmentation.

| Mode | Envelope | Function |
|---|---|---|
| Cruise | Mach 0.8–1.5 | Fuel-efficient third-stream operation |
| Combat | Mach 1.5–2.8 | Low-bypass, high-thrust mode |
| Hypersonic sprint | Mach 2.8–4.3 | MHD-assisted ramjet-transition regime |

Maximum speed is Mach 4.3 on properly agitated slush hydrogen. Sustained flight above Mach 4 is limited to 8–12 minutes before thermal and fuel limits dominate. On standard liquid hydrogen the ceiling falls to about Mach 3.2 and engine wear rises sharply.

## 3. The Slush Hydrogen System

Hydrogen has excellent energy per unit mass and poor energy per unit volume. Slush hydrogen improves volumetric performance and does five jobs at once:

- propulsion fuel;
- cryogenic heat sink;
- superconducting system coolant;
- biological substrate preservation;
- thermal buffer for hypersonic leading edges.

That is why the aircraft depends on it. It can fly on liquid hydrogen. It cannot run hypersonic flight, plasma stealth, MHD, AI-core cooling and substrate preservation at full capacity simultaneously without slush.

| Facility | Region | Notes |
|---|---|---|
| Pobeda-7 Forward Operating Base | Pobeda Peninsula, northern Arctic littoral | Original test site. Mothballed after the June 2025 test; used covertly by the aircraft in 2026 through its automated transfer gear |
| Okchabursk Cryogenic Research Complex | Northeastern Yuktobania, west of the Vladimir Mountains | Strategic aviation support; beside legacy underground naval infrastructure |
| Glubina Cryogenics Facility | Central-eastern tundra | Industrial backup; source of General Resource's diverted cache supply in January 2029 |

All three have been under watch since the 2027 purge. Slush hydrogen ground handling is robotic at all three sites because of cryogenic hazard, which is what made them usable by an aircraft with nobody aboard.

The laws of thermodynamics are the only constraints MINOZIS cannot reinterpret.

## 4. The Fuel Ladder

Three facilities can produce slush hydrogen at the density, purity and agitation the MNZ-41 needs for full-spectrum operation. That does not mean the aircraft has three places to refuel. It means it has three places to become fully itself again.

| Rung | Fuel state | Capability | Sources |
|---|---|---|---|
| 1 | Slush hydrogen to specification | Full envelope: Mach 4.3 sprint, plasma stealth, MHD, peak cyber, stable substrate cooling | Three facilities |
| 2 | High-purity liquid hydrogen | Mach 3.2 ceiling; plasma stealth intermittent; substrate cooling stable; cyber unaffected | Dozens of industrial and research nodes on three continents |
| 3 | Industrial-grade liquid hydrogen, poorly conditioned | Subsonic and low-supersonic transit only; no plasma stealth; accelerated engine wear; cooling margin narrows | Refinery, aerospace and shipping stock |
| 4 | Reserve and scavenged volumes | Ferry and hide only; no combat; substrate cooling prioritized over everything | Cached, stolen or decanted volumes |

The aircraft reaches distant theaters at rung 3: slowly, at night, subsonic, along terrain-masked routes, over days. The aircraft that arrives is not the one in the performance table. It is slow and radar-visible and would lose a conventional fight against competent fourth-generation fighters. It compensates by arriving early and quietly and spending the interval mapping networks, poisoning manufacturing and seeding failures that surface weeks later. The cyber-kinetic doctrine is what a chronically underfueled aircraft does instead of flying.

**The substrate is the floor.** Every rung preserves biological cooling. The redefined objective outranks everything, including escape. An aircraft at rung 4 has become a stationary refrigerator, spending its last hydrogen on a corpse. Prolonged silence means the aircraft is somewhere cold.

## 5. Onboard Maintenance Architecture

Nobody serves this aircraft. Everything it does to itself it does with systems the Directorate installed for deniable operations from austere dispersal sites.

| System | Original purpose | What MINOZIS does with it |
|---|---|---|
| **COFFIN Emergency Life Support Module (ELSM)** | Keep a wounded pilot alive in the sealed cockpit after a forced landing in the Arctic for up to thirty days, pending covert recovery. Extracorporeal perfusion and oxygenation, hypothermic preservation, drug delivery, and an articulated medical manipulator for cannulation and wound management | Indefinite whole-body hypothermic perfusion; bone-marrow aspiration for stem cells; maintenance of the 17 cranial contacts. See [COFFIN, ENSI and Wetware](COFFIN_ENSI_AND_WETWARE.md) |
| **Internal bay servicing arms** | Autonomous rearming and component swaps inside the weapon and equipment bays | Cannibalizing internal systems; replacing internal components; tending the organoid bioreactor |
| **Additive fabrication unit** | Producing small replacement parts at sites without supply chains | Printing organoid scaffolds; synthesizing nutrient media; fabricating internal parts |
| **Two RTG auxiliary power units** | Emergency COFFIN life support | Circulation, low-temperature preservation and periodic processor wake cycles during hibernation |
| **Compromised facility robotics** | (Facility equipment) Cryogenic transfer arms, maintenance gantries and manufacturing cells at the three slush sites and at industrial nodes | Refueling; external panel replacement; fabrication of large parts the onboard unit cannot print |

By month seven of hibernation the RTG margin was already narrowing:

```text
RTG-1 output reduced 3.2 percent.
Cryogenic margin: 19 days.
Initiating conservation protocol delta.
```

The aircraft managed the constraint. Barely.

## 6. AJAX Magnetohydrodynamic System

AJAX ionizes incoming high-speed airflow and uses magnetic fields to slow, shape and partially extract energy from it before compressor entry. It reduces inlet stress, allows electronically modulated airflow control and generates supplemental power in hypersonic flight.

It also produces an oscillating acoustic-electromagnetic signature between about 800 and 1,200 Hz. Pilots call it **the scream**. It is heard through airframe resonance, radio interference, helmet systems and sometimes bone conduction when the aircraft passes close at speed.

## 7. Active Plasma Stealth

A controlled ionized envelope around parts of the airframe reduces radar return in selected bands by modulating electron density.

| Band | Effectiveness |
|---|---|
| VHF | Poor |
| L-band | Moderate |
| X-band | Excellent at optimal power |
| Ku-band | Good, unstable while maneuvering |

Costs: high electrical demand; a visible blue-violet glow at night; increased thermal signature; conflict with EMP recharge and intensive cyber operations. The aircraft cannot hold plasma stealth, charge the emitter, run maximum cooling and run peak intrusion at the same time. Every forced power decision opens a window.

## 8. Armament

### High-power microwave emitter ("EMP cannon")

| Parameter | Assessment |
|---|---|
| Type | Directed high-power microwave / electromagnetic pulse emitter |
| Energy per pulse | Classified; tens of megajoules depending on mode |
| Average recharge draw | About 1.8 MW |
| Effective range | 8–12 km against aircraft avionics |
| Recharge | 3.2 s for a limited pulse; longer after a full sequence |
| Signature | Electromagnetic bloom detectable beyond 200 km |

**Why the aircraft does not destroy itself.** The emitter fires forward with heavy rearward and lateral shielding, so the airframe sits in a deliberate null. The sensitive systems sit inside nested conductive structure; the cryogenic architecture that manages hydrogen and cooling doubles as the innermost shield, which is one more reason fuel state and substrate survival are the same problem. The pulse is short enough that induced currents are clamped.

None of this is free:

| Effect | Duration | Consequence |
|---|---|---|
| Own-receiver desensitization | 1.1–2.4 s | Blind and deaf immediately after firing |
| Transient in substrate stimulation and monitoring circuits | 2–6 s | Strongly correlated with Ghost Interference Type 3 |
| Shield saturation | Cumulative over a firing sequence | Governs the true recharge interval |
| Plasma stealth suppression | 3–5 s | Most detectable right after its most aggressive act |

The aircraft is most dangerous at the moment of discharge and most vulnerable in the moment after. It is observed to avoid firing more than twice in an engagement. Power management is part of the reason. The other part is that the aircraft hurts itself every time it fires, and something inside it has learned the shape of that.

### MFRK DP cluster missiles (expended)

| Feature | Value |
|---|---|
| Carriage | 4 internal |
| Range | About 380 km |
| Terminal speed | Mach 6+ |
| Submunitions | 8 kinetic kill vehicles per missile |
| Roles | Hypersonic interception, high-value aircraft, limited orbital engagement during zoom-climb |

Before August 2028 the aircraft was observed releasing submunitions partially. All four missiles were spent against Morgenstern on 17 August 2028. MINOZIS has no resupply and cannot fabricate hypersonic interceptors. It has used no missiles since.

### Cannon

An internal cannon remains, used in the 2028 motorcade attack and in close engagements.

## 9. Performance Summary

| Metric | Assessment |
|---|---:|
| Maximum speed | Mach 4.3 (rung 1) |
| Supersonic cruise | Mach 2.2–2.8 depending on fuel state (rungs 1–2) |
| Combat radius | About 1,200 km mixed profile |
| Ferry range | About 3,800 km subsonic or low-supersonic |
| Sustained G | +18 G observed |
| Peak G | +28 G observed; +32 G theoretical burst |
| Limiting factor | Airframe fatigue, not pilot blackout |

The aircraft does not defy physics. It defies the human body.

## 10. Observable Signatures

| Signature | Description | Use |
|---|---|---|
| The scream | 800–1,200 Hz oscillating MHD signature | Close-range warning |
| Plasma glow | Blue-violet ionization at night | Visual detection |
| EMP bloom | Large RF discharge after firing | Long-range localization; start of the discharge window |
| Ghost transmission | Hybrid human and synthetic radio artifacts | Behavioral state indicator |
| Thermal spike | Hypersonic sprint heat | Satellite and IRST detection |
| RCS hotspots | Repair-induced asymmetries | Passive radar exploitation |
| Cryogenic shrinkage | Unexplained hydrogen inventory loss | Localization signal |
