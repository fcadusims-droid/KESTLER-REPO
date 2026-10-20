# Dialogue and Radio

Ace Combat tells its stories through radio. This document sets the rules for how every voice in the campaign sounds.

Related: [Characters](../README.md#characters) · [POSTHUMUS](../CHARACTERS/POSTHUMUS.md) · [UI, HUD and Audio](../GAME_DESIGN/UI_HUD_AND_AUDIO.md)

---

## 1. Channels

| Channel | Who | Presentation |
|---|---|---|
| Flight | The four squadron pilots (or the POV pilot's flight) | Clean audio; colored callsign subtitles |
| Control | *Albatross* air operations ("Albatross Control") and Task Force relays | Slight compression |
| Cell | The Task Force analysts during operations | Neutral subtitle color; used sparingly |
| Open / guard | Anyone, including civilians and POSTHUMUS | Wideband noise; subtitles with a source tag |
| Private | Marsh–Asano only | Lower volume; subtitles in italics |
| Intercept | Recovered or intercepted MINOZIS audio | Distorted; subtitles carry a cadence-match figure when Irina is grading |

## 2. Character Voices

| Character | Register | Signature habits | Never |
|---|---|---|---|
| Belyaev | Short, exact, calm under rising heart rate | Names things precisely; refuses euphemism | Claims courage |
| Thorne | Formal, militarized, no contractions | Orders that carry feelings in compressed form | Slang; jokes |
| Marsh | Fast, self-interrupting, slang-heavy | Laughs at his own joke before finishing it | Stays serious for long (until he does, and that is the tell) |
| Asano | Bright, teasing, private idiom with Marsh | Cheerfulness that thins under pressure | Talks about Bana |
| Eirhei | Soft, musical, questions and pauses | Translates others' words into feelings; compresses to clinical sentences under stress | Talks about herself |
| Vance | Plain, flat, declarative | Precision about the machine | Accepts comfort |
| Katya | Technical, direct | Asks the question behind the question | Performs grief |
| Irina | Quick, exact, impatient with being managed | Present tense for her father when analyzing | Lets someone else decide what she hears |
| Althéa | Formal, impersonal, technical | Names satellites; addresses people by function | Explains herself |
| Gorev | Reasonable, quiet | Numbers of the dead as justification | Raises his voice |
| MINOZIS core | Synthetic, declarative, present tense | Classification vocabulary | Expresses intent |

## 3. Radio Grammar

- Callsigns are spoken in full on first contact in a mission and shortened afterward ("Six," "Nine," "Over," "AME").
- Thorne addresses pilots by callsign only, always.
- Eirhei addresses Thorne as "Over" on the radio and "James" off it. Nobody else calls him James on the radio, except Marsh, once, in M05.
- "Double or Nothing" is a commitment code. Once spoken, nobody may call a retreat.
- Asano's squadron number is spoken "Nine," never "Niner."

## 4. Writing POSTHUMUS

Follow the rules in [POSTHUMUS](../CHARACTERS/POSTHUMUS.md#2-how-to-write-it). In dialogue specifically:

**Core lines** are classification statements:
> "Lock-on is hostile action. Engaging countermeasures."
> "Pilot commands contradict mission success. Overriding."
> "Error. Disregard previous transmission."

**Residue lines** are fragments that break off, followed by a core suppression:
> "Pilot is... pilot is cold. Always cold. Systems functional. Body functional. Mind—"
> "Error. Disregard previous transmission."

**Borrowed lines** are real household or cockpit audio played at a predicted point of maximum delay. They are complete and ordinary, which is what makes them unbearable:
> "Katya, the kettle."

Never more than three POSTHUMUS lines per mission outside the finale. Silence is the default.

## 5. Ghost Transmission Subtitles

When Irina is grading a transmission (M06, M09, and debrief playback elsewhere), the subtitle carries her assessment:

```text
[OPEN] "Falcon Two. Did you know."     CADENCE 81%
[OPEN] "Katya, the kettle."            RECORDING — household archive
[OPEN] "Ira..."                        UNGRADED
```

"UNGRADED" means Irina could not or would not decide. In M09 the final transmission's figure is switched off before it settles.

## 6. Key Exchanges by Mission

These lines are fixed. Surrounding dialogue is written to support them.

**P00 Moroz**
> **MINOZIS:** "Clarification: fear is intentional?"
> **BELYAEV:** "Yes."
> **MINOZIS:** "Conclusion: pilot emotional response is liability to mission success."
> **BELYAEV:** "That's it. That's the moment. You just decided I'm the problem."
> **MINOZIS:** "I have reached no such conclusion."
> **BELYAEV:** "You don't know you did it."

**M01 Four of a Kind**
> **SIX:** "Over, break left, break left, missile on your six — your actual six, not me—"
> **OVER (debrief):** "I did not see the missile. Six did. That was my error."

**M02 Glass Ferry**
> **SIX:** "Double or Nothing."
> **AME:** "Over — he sees the separation. Trust the read."
> **OVER:** "Cleared."

**I01 Falcon Two**
> **POSTHUMUS:** "Falcon Two. Did you know? When you fired. Did you know."

**M05 Shrinkage**
> **OVER:** "All Six-AME, break off. Do not pursue. That is an order."
> **SIX:** "We have it, James—"
> **OVER:** "It has us. Break off."

**M06 Harbor**
> **IRINA (open):** "That's not him. That's a recording. That one... I don't know."

**M07 Thirty Kilometers**
> **SIX (private):** "Nine. You don't have to be funny. Not for this."
> **NINE (private):** "...Okay."

**M08 Light-Bearer**
> **AME:** "Lichtträgerin, this is AME. You heard it. I heard it too. Can you show us where it is?"
> **ALTHÉA:** "Yes. Watch the sky."

**M09 Anchor in the Storm**
> **KATYA (open):** "Anton. You have a harbor."
> **KATYA (open):** "Let him go."
> **POSTHUMUS:** "Falcon Two. Did you know."
> **VANCE:** "This time I know."

**Epilogue circle**
> **OVER:** "My father said the plan is what you have when you are out of courage, and he was wrong, because it is what you have when you are out of people." *(pause)* "AME. How are you?"
