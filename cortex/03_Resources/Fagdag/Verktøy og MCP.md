---
title: "Verktøy og MCP"
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
source: https://www.notion.so/3c24dc662c22817c965ad1134437b1c4
aliases: []
notion: { page_id: 3c24dc66-2c22-817c-965a-d1134437b1c4, url: https://www.notion.so/3c24dc662c22817c965ad1134437b1c4 }
---

# Verktøy og MCP

> [!callout icon=hammer] **Én setning:** et verktøy er noe agenten kan *gjøre* utenfor samtalen: lese en fil, kjøre en kommando, hente været. MCP er standarden for å koble til flere.

## Verktøy

- Agenten har innebygde verktøy: lese og skrive filer, kjøre kommandoer i terminalen, søke på nettet.

- Alt den gjør, gjør den gjennom et verktøy. Derfor kan du se det. Derfor kan du si nei.

- Repoet har fire egne, i `brain/tools/`: `weather` henter været, `location` finner hvor du er, `news` leser nyhetskildene dine, `teach` lager en leksjon fra ekte kilder på nettet. Ingen trenger nøkkel eller oppsett. Bare nett.

- Hvert tool er en prompt som sier når og hvordan det brukes. To av dem (`weather`, `news`) har et lite skript i `brain/bin/` som gjør selve jobben.

- Det er **ingen e-post- og ingen kalender-tool.** Det er med vilje. Vil du ha et, skriv `new-idea`. Se «Koble til dine egne tjenester» i [Harness-dokumentasjon](https://www.notion.so/3c24dc662c2281c28a87d0ca35fcb5c0).

## Tillatelser

Første gang du starter agenten i mappen, spør den om du stoler på mappen. Svar ja. Grunnen er at `.claude/settings.json` i repoet har en liste over ting den får gjøre uten å spørre: repoets egne skript og ufarlige lesekommandoer. Før du sier ja, bruker den ikke den listen og spør om alt.

- **Alt annet spør den om.** Det er designet, ikke en irritasjon. Les hva den vil gjøre før du trykker ja.

## MCP

**Model Context Protocol** er en åpen standard for å koble agenten til andre systemer: Notion, Slack, en kalender, en database. En «MCP-server» er en liten tjeneste som forteller agenten hvilke verktøy den tilbyr. Koble til en når du tar deg selv i å lime inn data fra et annet verktøy i chatten.

Repoet bruker ingen MCP-servere. Skriptene i `brain/bin/` gjør jobben uten oppsett. MCP er neste steg når du vil ha kalenderen eller e-posten *inn* uten å eksportere. Da er `new-idea` veien: den kobler til og skriver sikkerhetsgjennomgangen før noe kjører.

<details><summary>For deg som koder: tillatelsesfilen og MCP</summary>

Samme fil har en liste over kall den alltid skal stoppe og spørre om (`ask` i filen): det som sender, sletter eller endrer i vanlige e-post- og kalenderkoblinger. Den gjelder selv om tool-filen glemmer det. Så lenge du ikke har slått av tillatelsesspørsmål.

Ting den aldri skal få gjøre kan du legge i `deny`. Det er en regel, ikke et ønske. `AGENTS.md` er kontekst agenten kan overse. `deny` er en vegg.

`claude mcp add <navn> <url>` i terminalen legger serveren til for deg lokalt. Med `-s project` havner den i `.mcp.json` i repoet, så et repo *kan* sende med en. Dette repoet gjør det ikke med vilje: det som når ut skal du koble til selv, med sikkerhetsgjennomgang fra `new-idea`.

</details>

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg hva et verktøy er for en agent, de fire toolene i repoet, tillatelseslisten i .claude/settings.json, og hva MCP er. Siden jeg leser: cortex/03_Resources/Fagdag/Verktøy og MCP.md

---

Videre lesning: [Connect to tools via MCP](https://code.claude.com/docs/en/mcp), [MCP quickstart](https://code.claude.com/docs/en/mcp-quickstart) og [Permissions](https://code.claude.com/docs/en/permissions).
