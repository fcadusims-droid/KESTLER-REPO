---
section: "02 · Core Systems"
description: "The After-Action Report and its variants"
order: 22
---

# The After-Action Report

When a session ends, ΜΝΗΜΗ writes what happened. This is the only place in Resident Evil Online where the time a survivor lasted is shown as a number, and only once the night is over. Every connected report is a page of the Ledger.

```
AFTER-ACTION REPORT

TIME SURVIVED ............ 78:41
STRAIN ................... T-VIRUS (LATENT)
INFECTION REACHED ........ FEVER
TRIALS SATISFIED ......... 3
ELPIS .................... USED (SELF)
OBJECTIVES COMPLETED ..... 4
PUZZLES SOLVED ........... 2
ITEMS RECOVERED .......... 19
CREATURES PUT DOWN ....... 37
SURVIVORS ASSISTED ....... 2
EVENTS ENDURED ........... 6
DISTANCE TRAVELED ........ 8.7 KM
WOUNDS TAKEN ............. 11
COMPANION ................ ROBERT KENDO · EXTRACTED
SCENES WITNESSED ......... 2
RIBBONS EARNED ........... 160
FINAL RESULT ............. EXTRACTED · CURED
```

A survivor who was never infected:

```
STRAIN ................... NONE
FINAL RESULT ............. EXTRACTED · CLEAN
```

A survivor who turned and played on:

```
AFTER-ACTION REPORT

TIME SURVIVED ............ 64:44
STRAIN ................... T-PHOBOS (LATENT)
INFECTION REACHED ........ THRESHOLD
TURN ..................... LONG · QUIET
FORM TAKEN ............... AFFLICTED
TIME AS TURNED ........... 13:52
HUNTS .................... 2
SURVIVORS ELIMINATED ..... 1
RIBBONS EARNED ........... 131
FINAL RESULT ............. TURNED
```

A survivor whose Turn was Quick:

```
AFTER-ACTION REPORT

TIME SURVIVED ............ 44:10
STRAIN ................... T-VIRUS (LATENT)
INFECTION REACHED ........ THRESHOLD
TURN ..................... QUICK
FORM TAKEN ............... ZOMBIE
FINAL RESULT ............. LOST
```

The first Tyrant of a night, whose parasite never arrived:

```
FORM TAKEN ............... TYRANT-CLASS · NE-α DESTROYED
FINAL RESULT ............. TURNED
```

A survivor who simply died:

```
AFTER-ACTION REPORT

TIME SURVIVED ............ 23:15
STRAIN ................... UROBOROS (LATENT)
INFECTION REACHED ........ FRACTURE
CAUSE .................... KILLED BY A SURVIVOR
FINAL RESULT ............. LOST
```

A survivor of the Valley whose Plaga the machine burned out:

```
PLAGA .................... HATCHED · BURNED OUT
FINAL RESULT ............. EXTRACTED · CURED
```

A survivor who got out beside the virus says so, and what it cost (`economy.md`, Exposure):

```
EXPOSURE ................. 1 SQUADMATE · 1 STRANGER · -38%
FINAL RESULT ............. EXTRACTED · CLEAN · EXPOSED
```

A survivor who got out on an improvised way says which, and the odds it left with:

```
WAY OUT .................. HOSPITAL HELICOPTER · IMPROVISED · 90%
```

The Crossing says so either way:

```
WAY OUT .................. THE CROSSING · ON FOOT · 1%
CAUSE .................... TAKEN IN NO MAN'S LAND
```

A night that held Echoes adds one line to every report in it: ECHOES PRESENT, and how many.

A night in which a survivor's body reached a new stage of Hardening (`survivors.md`) adds one line to that survivor's report, in ΜΝΗΜΗ's words, and never the stage's name:

```
SUBJECT ACCLIMATION ...... THE HANDS WERE STEADIER TONIGHT.
```

A survivor who helped put down a Heavy, or got away from one, adds a line for each:

```
HEAVY PUT DOWN ........... TYRANT-CLASS
HEAVY ESCAPED ............ NEMESIS-T TYPE
```

A survivor a Warden held adds the line, and a survivor a Warden ended says why:

```
HELD BY A WARDEN ......... GRIEFER · NOTORIOUS
CAUSE .................... ENDED BY A WARDEN
```

An offline session writes the same report, marked OFFLINE, with the company its Echoes were drawn from.
