---
section: "07 · Feasibility"
description: "Whether the design is legal to ship in the main markets, where it is not yet, what must change, and what the fan-made project itself may and may not do"
order: 47
---

# Legal Feasibility

This document asks two questions. Could the game these documents describe be shipped legally in the markets that buy the most games? And can this fan-made project be shown in a professional portfolio? It reads every system of the design against the law of the United States, the European Union, the United Kingdom, Brazil, and Japan, as those laws stood in October 2026.

**It is not legal advice.** It is a design review written by someone who is not a lawyer, from public sources, to find where the design needs a lawyer and what the safest version of each system looks like. Laws in this field are changing every year. Every point marked for counsel below must go to counsel before anything ships.

## The Verdict

**The game is legally viable, with eleven changes.** No system in the design is forbidden in any of the five markets. Four systems were built in ways the law now treats as risky, and each has a fix that keeps what the system is for:

1. **Echoes hidden among players.** From 2 August 2026, the EU AI Act requires that people be told when they interact with an AI system unless it is obvious. An Echo is built to be indistinguishable from a player. *Fix: the lobby says when a night holds Echoes; the report still says how many.*
2. **Proximity voice for minors.** The FTC's 2022 settlement with Epic Games treated voice chat that was on by default for children and teens as an unfair practice. Brazil's ECA Digital and the UK Online Safety Act push the same way. *Fix: age assurance at sign-up, and voice off by default under 18, turned on only with consent.*
3. **The voice calibration.** A stored model of how one person whispers and shouts could be argued to be a voiceprint, which Illinois law treats as biometric data at up to $5,000 per violation. *Fix: calibrate on the player's device, keep only three numbers, never keep audio.*
4. **No text in a night.** US law requires in-game communication to be accessible to players with disabilities. A night with voice only shuts out players who cannot speak or hear. *Fix: typed words are spoken aloud by the survivor's own voice in the world, and nearby speech is captioned for the player who needs it.*

The other seven changes are smaller and listed under What Changes. Two promises in the design are stronger than the law requires and are worth keeping as they are: no randomized or purchasable currency, and the offline guarantee.

**The fan-made project is safe to show, inside limits.** Capcom's fan content guidelines allow non-commercial fan works and forbid commercial use. A written design concept with no Capcom art, no sales, and a clear notice is the lowest-risk kind of fan work. It is still Capcom's intellectual property, and Capcom can ask for it to be taken down at any time (The Fan-Made Project, below).

## Markets Considered

| Market | Main laws read | Why it matters here |
|---|---|---|
| **United States** | FTC Act §5, COPPA and its 2025 amendments, CVAA, California's CCPA/CPRA and privacy and digital replica laws, Illinois BIPA, Tennessee's ELVIS Act | Largest console market; strictest enforcement on children and voice data |
| **European Union** | GDPR, AI Act, Digital Services Act, consumer law (Consumer Rights, Unfair Commercial Practices, Digital Content Directives), European Accessibility Act | Strictest rules on data, AI transparency, and moderation |
| **United Kingdom** | UK GDPR, Online Safety Act 2023 | Online safety duties apply directly to games with chat |
| **Brazil** | LGPD, ECA Digital (Law 15.211/2025), Marco Civil da Internet, Consumer Defense Code | Largest Latin American market; new and strict rules on minors |
| **Japan** | Act on the Protection of Personal Information (APPI), Payment Services Act | Capcom's home market |

China is left out: selling a game there needs a state licence and its own rules for minors, and the launch plan does not include it (`business-case.md`). The game is rated for adults in every market, as Resident Evil games are, but a rating does not keep minors out, and every law below treats it that way.

## The Risk Map

| Area | What in the design | Law | Risk | Change |
|---|---|---|---|---|
| Echoes among players | Echoes complete short queues, and nothing shows which survivors they are (`echoes.md`) | EU AI Act, Art. 50 | **High** in the EU | Lobby disclosure |
| Proximity voice and minors | Voice is how survivors talk, at every age (`the-living.md`) | FTC Act §5 (Epic order), COPPA, UK OSA, ECA Digital | **High** | Age assurance; voice off by default under 18 |
| Voice calibration | Each player records a whisper, a voice, and a shout (`presentation-and-technology.md`) | BIPA, COPPA 2025 (voiceprints), GDPR | **High** in Illinois | On device, three numbers, no audio |
| Accessible communication | No text chat in a night | CVAA | **High** in the US | Typed speech and captions, in the world |
| Behavioral data for Echoes | Every choice is recorded to build the Ways (`director-architecture.md`) | GDPR, LGPD, CCPA, APPI | Medium | Adults only; legitimate interest with an easy objection; impact assessment |
| A player's own Echo | A model of one player, shared with friends under their name | GDPR, LGPD, CCPA | Medium | Opt in, revocable |
| Voice moderation | Reports reviewed by Capcom (`the-service-and-promises.md`, Conduct) | GDPR, California CIPA, DSA | Medium | Record only on report, with notice; human review; reasons and appeal |
| Sanctions and the Doorstep Record | Voice and text removed; a public standing seal | DSA Arts. 17 and 20, UK OSA | Medium | Statement of reasons and appeal for sanctions |
| Dioramas | Player-made rooms shown to others | DSA, UK OSA | Medium | Notice-and-action for reports |
| Performers | Every voice, face, and movement performed and recorded by people; no digital replicas (`project-overview.md`, Performed by People) | SAG-AFTRA IMA 2025, likeness and publicity law, AI Act Art. 50 for the typed-speech voice | Low, if contracted right | Union-compliant contracts for every performer and scan; the typed-speech voice labeled as synthetic |
| The economy | Ribbons, Patron, refunds, minors' limits (`economy.md`) | Consumer law in all five markets, ECA Digital | Low | Brazil's 7-day withdrawal; cancellation as easy as sign-up |
| The offline promise | Every piece opens offline; nothing goes dark (`offline-and-ownership.md`) | EU consumer law | Low, and a strength | Keep it in pre-purchase information |
| Data transfers and logs | One service across regions | GDPR Ch. V, LGPD, Marco Civil Art. 15, APPI | Low | Standard transfer tools; 6-month access logs in Brazil |
| Exposure, the Crossing, Ribbons | Penalties and odds with no money at stake | Gambling and prepaid-currency law | Low | None |
| The fan-made project | Capcom's IP in a portfolio | Copyright, trademark, Capcom's guidelines | Low, if non-commercial | Keep it non-commercial and asset-free |

## The High Risks

### Echoes Among Players

**What the design does.** When a Survivor night cannot gather enough players, ΜΝΗΜΗ completes it with Echoes, up to a quarter of its survivors. During the night nothing shows which survivors are Echoes; afterward the After-Action Report says how many there were (`echoes.md`, When the Queue Runs Short).

**The law.** Article 50 of the EU AI Act, in force since 2 August 2026, requires that AI systems meant to interact directly with people be designed so that those people are informed they are interacting with an AI system, unless that is obvious to a reasonably well-informed person. The Commission's guidelines on Article 50, approved in July 2026, say single-player games may meet the "obvious" exception when no other person appears to be involved. They also say multiplayer modes in which an AI could be mistaken for a player may still need disclosure. An Echo is designed to be mistaken for a player.

**The fix.** Tell players before the night, without saying which survivors are Echoes. A night's lobby already shows a card for every player who will wake in it (`presentation-and-technology.md`, Matchmaking). When a night is completed with Echoes, the lobby also says so: **ECHOES PRESENT**. The After-Action Report keeps the count. Players then know they may meet an AI survivor, which is what the article requires, and the horror of not knowing which one remains. Whether a general notice is enough without marking each Echo is a question for counsel and for how the guidelines are applied.

**What does not change.** Offline nights, where every other survivor is an Echo and the player chose that, already meet the "obvious" exception.

### Proximity Voice and Minors

**What the design does.** Every survivor speaks through their own mouth to whoever is near, strangers included. Voice is how bargains, betrayals, and warnings happen (`the-living.md`).

**The law.**

- **United States.** In December 2022 Epic Games agreed to pay $275 million for COPPA violations and $245 million in refunds. The FTC treated Fortnite's voice and text chat, on by default, as an unfair practice that exposed children and teens to harassment. The order requires affirmative consent before those features are turned on, from a parent for children under 13 and from teens themselves for ages 13 to 17. The amended COPPA Rule, with compliance due 22 April 2026, adds voiceprints to children's personal information and requires a written retention policy.
- **Brazil.** The ECA Digital applies to products "likely to be accessed" by minors, electronic games among them, from March 2026. It requires reliable age verification, and self-declaration is expressly not enough. It also requires parental supervision tools, accounts under 16 linked to a legal guardian, the most protective privacy settings by default, and no design that encourages compulsive use. Fines reach 10% of the group's revenue in Brazil. Sanctions begin in November 2026.
- **United Kingdom.** The Online Safety Act covers games with voice chat, text chat, and matchmaking that connects strangers. Each service must assess the risk of illegal content and, where children can access it, of content harmful to children. Ofcom names grooming, harassment, and bullying as the main risks in games.

**The fix.**

- **Age assurance at sign-up,** by a method each market accepts. In Brazil that excludes self-declaration.
- **Voice off by default under 18,** turned on only with consent: a parent's under 13 (where the game admits them at all), the teen's own from 13 to 17. A survivor whose voice is off still gestures and calls, as a sanctioned player already does (`the-service-and-promises.md`, Conduct).
- **Under 16 in Brazil,** the account is linked to a guardian, who can see and change these settings.
- **The risk assessments** the UK and Brazil require, written before launch and kept up to date.

The game loses nothing it needs: its rating is adult, its audience is adult, and the night still works for a survivor who only gestures.

### The Voice Calibration

**What the design does.** Before their first night, each player speaks a whisper, an ordinary sentence, and a shout. That sets how the server reads their voice into Hush, Murmur, or Clamor (`presentation-and-technology.md`, Voice, in Practice).

**The law.** Illinois's Biometric Information Privacy Act treats a voiceprint as a biometric identifier. Collecting one requires written notice and consent, and damages are $1,000 per negligent violation and $5,000 per intentional or reckless one, before attorneys' fees. In *Delgado v. Meta*, a federal court let a voiceprint claim go forward on the reasoning that what matters is whether voice data *could* identify a person, not whether it was used to. The COPPA amendments name voiceprints as children's personal information. Under the GDPR, biometric data used to identify someone is special-category data.

**The fix.** Make the calibration incapable of identifying anyone.

- It runs on the player's own device.
- It keeps three numbers per player: where their whisper, voice, and shout sit. No audio, no spectrum, no model of the voice.
- The classifier on the server reads each phrase against those three numbers and keeps nothing.
- The privacy notice says so, and players in Illinois and in other biometric-law states give written consent anyway, as cheap insurance.

### Accessible Communication

**What the design does.** Voice is the only way survivors talk in a night. There is no text chat, because a typed word would be a radio no one else could hear (`presentation-and-technology.md`, Sound).

**The law.** The US Twenty-First Century Communications and Video Accessibility Act (CVAA) has applied to game software with communication features since 1 January 2019, when the FCC's waiver for games expired. In-game voice and text chat are advanced communications services. They must be accessible to people with disabilities where that is achievable, and developers must keep records of how they considered it. The industry's answers are text-to-speech and speech-to-text, such as the real-time transcription Microsoft built into the Xbox platform.

**The fix keeps the fiction.** A player who cannot speak types, and their survivor says the words aloud, from their own mouth, at Murmur unless the player marks it as a whisper or a shout. Everyone near hears a voice, never sees text. A player who cannot hear can turn on captions of the voices near them, placed where they come from. The rule that no typed word reaches anyone as text still holds. What changes is that a typed word becomes a spoken one, in a plain synthetic voice that imitates no performer and is the only synthetic voice in the game (`project-overview.md`, Performed by People).

## The Medium Risks

### Behavioral Data for the Echoes

**What the design does.** The server records every choice a survivor makes, as numbers, to find the Ways and fit the Echoes (`director-architecture.md`, The Echoes).

**The law.** This is profiling under the GDPR. It needs a legal basis, a clear notice, a right to object, and, at this scale, a data protection impact assessment (Arts. 6, 13, 21, 35). The LGPD, the CCPA/CPRA, and the APPI ask for the same in their own terms. Children's data carries extra limits everywhere.

**The fix.**

- **Legal basis: legitimate interest.** Building the bots that keep queues short is a reasonable expectation in an online game, if the notice says so plainly. It needs a balancing test on file.
- **The objection is the forget request.** `echoes.md` already lets any player ask ΜΝΗΜΗ to forget them, which removes their records at the next rebuild. That is the GDPR right to object, built into the fiction. It must also be reachable from the Service's privacy settings, in plain words.
- **Adults only.** No record from a player under 18 enters any Echo.
- **Impact assessment** before launch.

### A Player's Own Echo

**What the design does.** After fifty nights, ΜΝΗΜΗ builds an Echo of the player alone, and the player can share it with friends, under their name, in offline nights (`echoes.md`, Your Own Echo).

**The fix.** It is a profile of one person, shown to others under their name, so it is built only with the player's consent, asked once at fifty nights, and it can be withdrawn at any time. Withdrawing it deletes it. Sharing it is a second, separate choice.

### Voice Moderation

**What the design does.** Any player can report another for harassment or hate speech, and Capcom reviews every report (`the-service-and-promises.md`, Conduct). The design does not say what Capcom reviews.

**The law.** To review voice, something must be recorded. In California, recording a confidential communication without the consent of all parties is a crime under the Invasion of Privacy Act. Proximity voice among strangers may not be confidential, but the risk is real. In the EU, a recording is personal data. Activision's moderation of *Call of Duty* voice chat records flagged speech, and a human moderator reviews it before any action.

**The fix.**

- **A short rolling buffer.** The server keeps the last few minutes of voice near each player, in memory only, and discards it continuously.
- **Saved only on a report.** A report saves the buffer around it, for review and nothing else.
- **People decide.** A human moderator reviews every report before any sanction.
- **Notice.** The terms and the first-night notice say all of this.

### Sanctions, Appeals, and the Doorstep Record

**The law.** The EU Digital Services Act requires hosting services to give a statement of reasons when they restrict a user's content or account, and online platforms to offer a free internal complaint system (Arts. 17 and 20). Commentators read it to cover muting or banning players.

**The fix.** Every voice or text sanction comes with a statement of what was decided, why, on what evidence, whether it was automated, and how to appeal, and an appeal is reviewed by a person. The Doorstep Record is a rule of play, applied automatically from a public table, not a sanction (`survival.md`). It needs no appeal, but it should show each player the offences on their own record, so they can see it is accurate.

### Dioramas

**What the design does.** Players build rooms and show them on their Dossier (`cosmetics-and-dossier.md`, The Diorama).

**The fix.** Pieces come only from what the game ships, which limits what can be built, and Conduct already lets Capcom reset an offensive diorama. The DSA and the UK OSA add a notice-and-action process: a report button, a decision, a statement of reasons.

## The Low Risks

- **Performers.** Every voice, face, and movement in the game is performed by a person and recorded, and no performer is turned into a digital replica (`project-overview.md`, Performed by People). The replica rules of the 2025 SAG-AFTRA Interactive Media Agreement, ratified in July 2025 and running to October 2028 (written consent and a specific description for each replica, a report within 90 days of release, pay per generated line), of California's AB 2602, and of Tennessee's ELVIS Act therefore have nothing to apply to. What remains is ordinary: union-compliant contracts for every performer, and consent and pay for every face and body scanned. The one synthetic voice, the plain voice that speaks a player's typed words, imitates no one, so it is no replica; the AI Act's rules for synthetic audio are met by naming it as synthetic in the accessibility settings.
- **The economy.** Ribbons cannot be bought, sold, or traded, so they are not prepaid currency under Japan's Payment Services Act and are not the converted-currency pricing EU authorities criticize. Nothing random is sold, so loot-box laws do not apply. Two changes:
  - Brazil's Consumer Defense Code gives seven days to withdraw from a purchase made outside a store, beside the EU's fourteen.
  - Patron is cancelled in as few steps as it took to start, as US state auto-renewal laws and the EU's coming Digital Fairness Act expect.
- **The offline promise.** In June 2026 the European Commission declined to require that games stay playable after support ends. It pointed instead to existing consumer law, which requires clear information on how long a service will last before purchase. This design already promises more than any law requires: nothing owned is lost, and the game goes offline rather than dark (`offline-and-ownership.md`). That promise must appear in the information shown before purchase, because once made it binds.
- **Data transfers and logs.**
  - Transfers out of the EU use the EU-US Data Privacy Framework or standard contractual clauses, and transfers out of Brazil use the ANPD's standard clauses.
  - Brazil's Marco Civil requires application providers to keep access logs for six months, under confidentiality.
  - The ECA Digital requires foreign providers to name a legal representative in Brazil.
- **Exposure, the Crossing, odds.** No money is staked and nothing can be bought to change them. They are game rules, not gambling.

## What Changes

| # | Change | Where |
|---|---|---|
| 1 | The lobby says ECHOES PRESENT when a night holds Echoes | `echoes.md`, `presentation-and-technology.md` |
| 2 | Age assurance at sign-up; in Brazil, not by self-declaration | `the-service-and-promises.md` |
| 3 | Voice off by default under 18; on only with consent | `the-service-and-promises.md` |
| 4 | Accounts under 16 in Brazil linked to a guardian | `economy.md` |
| 5 | Voice calibration on the device, three numbers, no audio | `presentation-and-technology.md` |
| 6 | Typed words spoken by the survivor's voice; captions for nearby voices | `presentation-and-technology.md` |
| 7 | No record from a player under 18 enters an Echo; the forget request reachable from privacy settings | `echoes.md` |
| 8 | A player's own Echo built only with consent, shared only by a second consent | `echoes.md` |
| 9 | Voice saved only from a rolling buffer when a report is made; human review | `the-service-and-promises.md` |
| 10 | Statement of reasons and appeal for every sanction; a report button for dioramas | `the-service-and-promises.md` |
| 11 | Seven-day withdrawal in Brazil; Patron cancelled as easily as it started; no performer synthesized, and the typed-speech voice labeled as synthetic | `economy.md`, `presentation-and-technology.md`, `project-overview.md` |

## What Still Needs a Lawyer

- Whether a lobby notice is enough under Article 50, or each Echo must be marked.
- Which age assurance methods each market accepts, and what they cost per player.
- Whether the rolling voice buffer meets California's all-party consent rule with notice alone.
- The legitimate interest balancing test for the Echoes, in each EU member state where the game launches.
- The performers' contracts for ΜΝΗΜΗ's voices and for every actor whose face or body was scanned for the people of the records.
- The CVAA achievability record, kept from the first design decision onward.

## The Fan-Made Project

This section is about the documents themselves, not the game they describe.

**What they are.** A written design concept for a game set in Capcom's Resident Evil, using its characters, places, and history, made by one person with an AI assistant, for a professional portfolio, with no intent to sell it or to build it (`project-overview.md`).

**What Capcom allows.** Capcom's fan content guidelines, published on 4 November 2025, allow non-commercial fan works based on its IP: illustrations, fiction, and similar works. They generally prohibit commercial use, prohibit offensive works and works that could damage Capcom's reputation, and ask that fan content state it is based on Capcom's IP. Capcom may ask anyone to stop, and may act against malicious use. The guidelines do not mention portfolios or fan game designs.

**Where this project stands.**

- **Non-commercial.** Nothing is sold. Showing work in a portfolio to seek employment is not selling the work, but it is a use that benefits its author, so the safest reading is to keep it strictly free to view and never paid for in any form.
- **No Capcom materials.** The documents contain no Capcom art, logos, screenshots, footage, music, or code. The diagrams and the console are original. Keep it that way: no official logo, no game captures, no character renders.
- **Clearly unofficial.** The project overview, the one-pager, the diagram, and the console carry the notice that the project is fan-made and not affiliated with Capcom. Every new page should carry it too.
- **The title.** "Resident Evil Online" uses Capcom's trademark to say what the project is about. With the notice, and with no logo, it is unlikely to mislead anyone into thinking it is official. A portfolio that wants no doubt can present it as *a fan concept for Resident Evil*.
- **If Capcom asks.** Take it down at once. A fan work has no right to stay up against the owner's request.

**What would change the answer.** Selling it, crowdfunding it, building it as a playable game with Capcom's assets, or presenting it as official would each move it from a tolerated fan work to an infringement.

## Sources

- European Commission, AI Act Article 50 guidelines, as reported in *Same NPC, Different Rules*, Chambers. [Link](https://chambers.com/articles/same-npc-different-rules-how-a-player-s-age-changes-their-responsibilities-under-the-ai-act)
- Orrick, *6 Top Takeaways from the FTC's $520 Million Epic Games Settlements*, 2023. [Link](https://orrick.com/Insights/2023/02/6-Top-Takeaways-from-FTCs-Landmark-Epic-Games-Settlements)
- BBB National Programs, *Amended COPPA Rule Compliance Date*. [Link](https://bbbprograms.org/media/insights/blog/coppa-amended)
- Mayer Brown, *Enforcement of Brazil's ECA Digital*, April 2026. [Link](https://www.mayerbrown.com/fr/insights/publications/2026/04/enforcement-of-brazils-eca-digital-introduces-new-obligations-for-companies)
- Ofcom, *The Online Safety Act and Gaming*. [Link](https://www.ofcom.org.uk/online-safety/the-online-safety-act-and-gaming-know-the-risks-know-the-rules-know-how-to-comply)
- Barnes & Thornburg via Mondaq, *The Voiceprint You Didn't Mean to Create: Delgado v. Meta*. [Link](https://www.mondaq.com/unitedstates/employee-rights-labour-relations/1811384/the-voiceprint-you-didnt-mean-to-create-what-delgado-v-meta-means-for-employers)
- Kelley Drye, *Communications Accessibility in Games*. [Link](https://www.kelleydrye.com/viewpoints/client-advisories/communications-accessibility-in-games-what-game-developers-need-to-know.md)
- PCWorld, *Call of Duty's New AI Moderator Is Listening to Your Voice Chat*, 2023. [Link](https://www.pcworld.com/article/2050174/call-of-dutys-new-ai-moderator-is-listening-to-your-voice-chat.html)
- Esports Legal News, *Gaming Bans and the DSA*, 2025. [Link](https://esportslegal.news/2025/06/04/gaming-bans-and-gamer-and-dsa/)
- Frankfurt Kurnit Klein & Selz, *Inside the New SAG-AFTRA Interactive Media Agreement*. [Link](https://technologylaw.fkks.com/post/102mewu/inside-the-new-sag-aftra-interactive-media-agreement-new-standards-for-ai-and-di)
- Covington, *California Passes Digital Replica Legislation*, 2024. [Link](https://www.globalpolicywatch.com/2024/09/california-passes-digital-replica-legislation-as-congress-considers-federal-approach/)
- William Fry, *EU Declines Video Game Playability Mandate*, 2026. [Link](https://www.williamfry.com/knowledge/eu-declines-video-game-playability-mandate/)
- Heuking, *Digital Fairness Act: Implementation Obligations*, May 2026. [Link](https://www.heuking.de/en/news-events/newsletter-articles/detail/digital-fairness-act-implementation-obligations-companies-need-to-prepare-for.html)
- Automaton, *Capcom Publishes Fan Content Guidelines*, 2025. [Link](https://automaton-media.com/en/news/capcom-publishes-fan-content-guidelines-including-rules-against-offensive-fanart-and-commercial-use/)
- Brazil, *Marco Civil da Internet*, Law 12.965/2014, Art. 15.
