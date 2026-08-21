---
title: "Prompting"
type: note
stage: active
status: draft
created: 2026-08-21
updated: 2026-08-21
generated: { by: claude-code/fable-5, at: 2026-08-21T00:00:00Z }
verified: []
stale_after:
tags: [fagdag, workshop]
area:
source: https://www.notion.so/3c24dc662c228147b691d8df3bfc23f6
aliases: []
notion: { page_id: 3c24dc66-2c22-8147-b691-d8df3bfc23f6, url: https://www.notion.so/3c24dc662c228147b691d8df3bfc23f6 }
---

# Prompting

> [!callout icon=chat] **Én setning:** prompting er å briefe en ny kollega. Hva du vil ha, hvorfor, og hva som er bra nok.

## Hva er en god prompt?

> [!callout icon=light-bulb] **«Lag middag» taper for en oppskrift.** Jo mer du sier om hva du vil ha, hvorfor, og hva som er bra nok, jo bedre svar.

- **Det som virker på mennesker, virker på agenter.** Klart språk, klare forventninger, riktig kontekst.

- **Det som er ulikt:** den leser ikke mellom linjene. Det du ikke sier, gjetter den på. Si det.

- **Samtale eller én melding.** Det er lov å bruke tre meldinger på å lande hva du egentlig mener.

- **Modellene endrer seg.** Det som virket i fjor kan være unødvendig nå. Prøv deg fram, og spør agenten hva som virker.

- **Usikker på prompten din?** Skriv `fix-my-prompt` og lim inn prompten din, så får du en bedre tilbake, med én linje om hva som ble endret.

## Seks teknikker

Fra Anthropics AI Fluency-kurs, leksjon 7 ([12 minutter på YouTube](https://www.youtube.com/watch?v=2YCaBqP8muw)). Bland og bruk det du trenger.

> [!callout icon=target] **Først: si hva som er bra nok.** Hvordan ser ferdig ut? Hva kan den sjekke seg selv mot? «Et forslag til middag» er ikke et kriterium. «Tre retter, under 30 minutter, ikke det vi spiste i går, og si hvilke ingredienser jeg mangler» er det. De fleste dårlige svar er svar på en prompt uten kriterium.

1. **Gi kontekst.** Hva du vil ha, hvorfor, og hvem du er.
    Ikke «fortell meg om klimaendringer». Heller «jeg skal på intervju i Indonesia, har bakgrunn i økologi, og trenger de siste ti årenes utvikling der».


1. **Vis et godt eksempel.** Ett eller flere par av input og ønsket output.
    Den kopierer stilen og formatet ditt. Velg eksempler som dekker ulike tilfeller, ikke fem like.


1. **Si hva svaret skal være.** Format, lengde, språk, deler, harde krav.
    «Norsk, maks 200 ord, tre punkter, avslutt med ett spørsmål til meg.»


1. **Del opp i steg.** List rekkefølgen når det finnes mange gyldige veier.
    «Finn de tre mest solgte produktene, sammenlign kvartalene, pek på trender, foreslå årsaker.» I den rekkefølgen.


1. **Be den tenke først.** Faktorer, begrensninger og alternativer før den svarer.
    Nyere modeller gjør ofte dette selv. Be om det likevel. Resonnementet gjør feil lettere å se.


1. **Gi den en rolle.** Fagfelt, perspektiv eller tone.
    «Som UX-ekspert, foreslå tre forbedringer for tilgjengelighet.» «Forklar som en erfaren lærer til en smart tiåring.»


> [!callout icon=star] Vet du ikke hvordan du skal spørre? **Beskriv målet, og be den skrive prompten.** Eller skriv `fix-my-prompt` og lim inn prompten din. Du får en bedre en tilbake, klar til å lime inn, med én linje om hva som ble endret.

## Seks vanlige feil

<details><summary>Feilene, én for én</summary>

- **Tro at den leser tanker.** Det du ikke sa, gjetter den på.

- **Fem oppgaver i én melding.** Én ting om gangen.

- **Være vag om hva som er bra nok.** Si hvordan ferdig ser ut før den starter.

- **Ikke gi tilbakemelding.** «Nei, kortere, og dropp punkt to» er en fullverdig prompt. Har samtalen sporet av, start en ny.

- **Si «ikke».** «Ikke bruk punktlister» sier hva du ikke vil ha. Si «skriv det som tre korte avsnitt» i stedet.

- **Motstridende instrukser.** «Kort, men grundig» tvinger den til å gjette hvilken som vinner. Velg én.

</details>

> [!callout icon=compass] **Kalibrering, ikke regler.** Feilene kommer i par. For vag eller for detaljert. For lite kontekst eller alt du har. Gir opp etter ett forsøk, eller retter det samme fem ganger. Ferdigheten er å kjenne hvilken side du bommer på akkurat nå.

## Hallusinering

Når modellen sier noe som høres riktig ut, men ikke er det. Det beste forsvaret ligger i repoet: skriv `ask` og still spørsmålet, så merker den alltid hva som kom fra notatene dine og hva som er allmenn kunnskap.

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg hvordan jeg skriver en god prompt: si hva som er bra nok, de seks teknikkene fra AI Fluency, de vanlige feilene, og hva hallusinering er. Siden jeg leser: cortex/03_Resources/Fagdag/Prompting.md

---

Videre lesning: [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) i Claude-dokumentasjonen, og [Common workflows](https://code.claude.com/docs/en/common-workflows) for hvordan de samme teknikkene ser ut i Claude Code.
