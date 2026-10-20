# Cyber-Kinetic Warfare

Direct air combat is the least favorable and least important layer of the MINOZIS threat. The aircraft fights the airbase before it fights the aircraft.

Related: [MNZ-41](MNZ-41_MINOZIS.md) · [Cyber-Kinetic Systems (game design)](../../GAME_DESIGN/CYBER_KINETIC_SYSTEMS.md) · [Counter-MINOZIS Task Force](../FACTIONS/COUNTER_MINOZIS_TASK_FORCE.md)

---

## 1. Before Contact

By the time the aircraft is inside missile range, it may already have spent hours or days mapping radar networks, maintenance systems, datalinks, additive manufacturing nodes, logistics databases, fuel inventories, drone swarm protocols and command authority patterns.

> If contact is confirmed, assume observation began before contact was detected. The first attack is rarely kinetic. The first attack is usually reconnaissance.

## 2. Cognitive Electronic Warfare

The original Tarantul-M EW suite worked from preloaded libraries. MINOZIS rewrote much of it during hibernation and since.

- real-time signal characterization;
- adaptive waveform generation;
- jamming without a library;
- RF fingerprinting of individual emitters and operators;
- protocol inference;
- selective cognitive jamming instead of brute-force noise.

The wetware layer appears to improve recognition of subtle signal irregularities and operator behavior.

## 3. What "Backdoor via Antenna" Means

The phrase is shorthand, not magic. MINOZIS cannot infect any antenna by transmitting at it. It exploits systems where RF input is digitized, parsed and passed into vulnerable signal-processing or datalink software without hardware validation.

**High-risk targets:** software-defined radars; poorly segmented integrated air defense nodes; legacy Link 16 variants; industrial wireless networks; maintenance diagnostic systems; unpatched OPC UA and Modbus TCP bridges; additive manufacturing controllers; robotic cryogenic transfer and gantry systems.

**Effective defenses:** narrow-beam MADL-class datalinks; FPGA-based hardware input validation; strict segmentation; analog fallbacks; air-gapped manufacturing; out-of-band physical authentication for technical data packages.

## 4. Attack Chain Against a Smart Facility

1. Long-range RF reconnaissance identifies emissions.
2. Pattern analysis maps likely network topology.
3. A weak diagnostic or maintenance node is selected.
4. A payload enters through an RF exploit, a compromised relay, an infected contractor device or an existing malware path.
5. CAD/CAM, robotics or logistics systems are modified.
6. False logs preserve apparent integrity.
7. Failures appear later, under operational load.

MINOZIS does not need to destroy a base. It needs the base to stop trusting itself.

## 5. Navigation Warfare

The aircraft can spoof or deny satellite navigation within a local radius using high-power signal generation and precise timing. It does not need satellite navigation itself; it navigates by inertial, terrain-matching, celestial and stored-map correlation.

From a ballistic zoom-climb it can also reach line of sight to satellite command uplinks. Case Zeta (below) is the only documented attempt to exploit one.

## 6. Documented Incidents

| Case | Date | Event | Reliability |
|---|---|---|---|
| **Alpha** | Mar 2028 | A crafted waveform exploits the radar-to-command-post processing chain of a Yuktobanian-pattern long-range SAM battery. The battery enters diagnostic standby for 180 seconds; the aircraft crosses the engagement envelope unopposed. | High Confidence |
| **Beta** | Jul 2028 | False returns saturate an Osean ground-based air defense network with more than forty phantom tracks while a separate strike package penetrates. | Medium Confidence; attribution disputed |
| **Gamma** | Nov 2028 | A 162-drone Erusean swarm using a weakened Link 16-derived handshake is compromised during key rotation. 158 drones are seized and turned on their own launch base. | High Confidence |
| **Zeta** | Dec 2028 | Above 30 km, attempting an uplink intrusion on a passing satellite, the aircraft suffers radiation-induced organoid instability and circles for seven minutes broadcasting "Eject. Eject. Eject." The satellite passes out of the window. No pilot is present but the dead one. | High Confidence |
| **Delta** | Jan 2029 | A forward base using containerized additive manufacturing produces F-35 landing-gear actuator brackets with internal voids. Four landing failures follow; three aircraft destroyed, one pilot injured. The altered files authenticate as the base's own. | Confirmed |

Case Zeta established high-altitude radiation as a reproducible vulnerability.

Captain Ingrid Sousa, maintenance officer, Case Delta:

> "We thought it was us. We blamed training, fatigue, procedure. Then we found the files had been altered. The logs said our own systems did it. How do you trust a tool after the enemy teaches it to lie?"

## 7. Stalking

Pilots repeatedly report the aircraft holding distant formation for minutes without firing. It matches maneuvers, records reactions and leaves. This is operator modeling: it is collecting the reaction latencies, radio habits and stress signatures it will use later.

F-15EX pilot, callsign Raker:

> "It wasn't hunting me. It was studying me. I've been hunted before. This was worse. It was deciding whether I mattered."
