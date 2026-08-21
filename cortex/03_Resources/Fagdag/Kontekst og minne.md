---
title: "Kontekst og minne"
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
source: https://www.notion.so/3c24dc662c2281d984dcc2370fcdccfa
aliases: []
notion: { page_id: 3c24dc66-2c22-81d9-84dc-c2370fcdccfa, url: https://www.notion.so/3c24dc662c2281d984dcc2370fcdccfa }
---

# Kontekst og minne

> [!callout icon=brain] **Én setning:** hver samtale starter med tomt hode. Det den husker, er det som står i filer. Det er hele grunnen til at repoet er bygget som det er.

## Kontekstvinduet

**Kontekstvinduet** er alt agenten har i hodet akkurat nå: instruksjonene, samtalen, filene den har lest, svarene den har gitt. Det har en grense. Agenten jobber best når det er god plass.

- Når det fylles opp, blir svarene dårligere før de stopper. Det er ikke en feil. Det er sånn det virker.

- Skriv `/compact` i Claude Code, så oppsummerer den samtalen så langt og fortsetter med plass. Skriv `/clear`, så starter den på nytt. Det koster ingenting. `/compact` koster mer. I dette repoet leses profilen din inn på nytt etter begge.

- **Tommelfingerregel:** én oppgave per samtale, ny samtale når du bytter tema. Blir svarene rare etter en lang samtale, er det som regel derfor. Mer i [Tips og triks](https://www.notion.so/3c24dc662c2281598faadc46fe9a7590).

## Hvordan den husker fra gang til gang

To ting bærer kunnskap fra samtale til samtale. Begge er filer.

**Manualen** er instruksjonene agenten leser før den leser meldingen din. I repoet heter den `AGENTS.md`. `CLAUDE.md` peker bare dit, slik at Claude Code leser det samme som Codex og Cursor. Tenk på den som stillingsbeskrivelsen til den nye kollegaen.

|  | `AGENTS.md` | Notatene dine (`cortex/`) |
| --- | --- | --- |
| **Hvem skriver** | Følger med repoet | Agenten, på dine ord |
| **Hva** | Instruksjoner og regler | Kunnskap, beslutninger, det du fanget |
| **Når lastes det** | Alltid, hele filen | Profilen og avtalen hver gang; resten når den søker (`ask`, `infer`) |
| **Bruk til** | «Gjør alltid X», hvor ting ligger, konvensjoner | Alt du ellers måtte forklart på nytt |

### Profilen din

Det hjernen vet om deg står i ett notat, `[[About me]]`. Det er et **nav**: maks 40 linjer, lest i starten av hver samtale. Detaljene ligger i egne notater det lenker til, som `[[How I learn]]`, `[[How we work together]]` og `[[My news sources]]`. Kort nav, lange eiker. Da får den med seg det viktigste hver gang uten å fylle hodet.

Skriv `start` for å lage profilen. Skriv `mirror` for å se hva som står i den. Skriv `start` igjen for å rette.

<details><summary>For deg som koder: hvordan den garantert leser profilen</summary>

`brain/bin/context` kjører når en samtale starter og leser inn `[[About me]]`, de åpne gjetningene i `[[Assumptions]]` og en linje om siste aktivitet. Notatet er sannheten. Skriptet bare siterer det.

</details>

### Når skal noe inn i avtalen?

Ikke i `AGENTS.md`. Den filen er manualen som følger med repoet og byttes ut når du oppdaterer. Dine regler hører hjemme i `[[How we work together]]`, som agenten leser på nytt hver tur. Si «remember that», så foreslår den linjen. Du redigerer ingen fil selv.

- Agenten gjør samme feil for andre gang.

- Du skriver den samme rettelsen i chatten som du skrev forrige gang.

- En ny kollega hadde trengt samme kontekst for å være produktiv.

> [!callout icon=target] **Hold den kort.** For hver linje: ville det blitt feil hvis jeg fjernet denne? Hvis nei, fjern den. En prosedyre på mange steg hører hjemme i en skill, ikke i avtalen. Agenten behandler avtalen som kontekst, ikke som lov. Jo kortere og mer spesifikk, jo oftere blir den fulgt.

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg kontekstvinduet, hvorfor hver samtale starter tom, og hvordan AGENTS.md og notatene gir agenten minne. Siden jeg leser: cortex/03_Resources/Fagdag/Kontekst og minne.md

---

Videre lesning: [How Claude remembers your project](https://code.claude.com/docs/en/memory) og [Context window](https://code.claude.com/docs/en/context-window).
