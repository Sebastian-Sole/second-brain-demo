---
title: "Subagenter"
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
source: https://www.notion.so/3c24dc662c228134b9b3fab68f784fc5
aliases: []
notion: { page_id: 3c24dc66-2c22-8134-b9b3-fab68f784fc5, url: https://www.notion.so/3c24dc662c228134b9b3fab68f784fc5 }
---

# Subagenter

> [!callout icon=rocket] **Én setning:** en subagent er en agent agenten starter, med eget tomt hode, for å gjøre en avgrenset jobb og komme tilbake med bare svaret.

## Hvorfor agenten bruker dem

Skill, tool, rutine og subagent er forklart i [Skills og kommandoer](https://www.notion.so/3c24dc662c2281d38258e41074b0e9b6).

- **Plass.** Et søk gjennom femti filer fyller hovedsamtalen med ting du aldri ser på igjen. En subagent gjør søket i sitt eget vindu og leverer oppsummeringen.

- **Begrensning.** En subagent kan få færre verktøy. En som bare skal lese, kan ikke skrive.

- **Pris og fart.** Rutinejobber kan gå til en raskere og billigere modell.

## Når du møter dem

Claude Code har innebygde subagenter den bruker selv: én som utforsker filene, én som planlegger. Du trenger ikke sette opp noe. Du ser det som «agent» i terminalen mens den jobber.

Lag din egen først når du tar deg selv i å starte samme type arbeid med samme instruksjoner om og om igjen. I dette repoet trenger du det ikke for å komme i gang.

## Rutiner

Beslektet, men ikke det samme. En **rutine** er noe som kjøres på klokka, uten at du sitter der. Repoet kjører ingenting på klokka, med vilje. Ingen cron, ingen bakgrunnsagent. Du ser alt som skjer.

`brief` er laget for å kjøres for hånd. Aldri sett noe på en timer på en konto med e-post eller kalender koblet til.

<details><summary>For deg som koder: det som er ment for en timer</summary>

`doctor --check` og `brain/bin/run maintain` er de to linjene laget for det. Den første endrer aldri noe.

</details>

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg hva en subagent er, hvorfor den får sitt eget kontekstvindu, og forskjellen på en subagent og en rutine. Siden jeg leser: cortex/03_Resources/Fagdag/Subagenter.md

---

Videre lesning: [Create custom subagents](https://code.claude.com/docs/en/sub-agents).
