---
title: "Harness-dokumentasjon"
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
source: https://www.notion.so/3c24dc662c2281c28a87d0ca35fcb5c0
aliases: []
notion: { page_id: 3c24dc66-2c22-81c2-8a87-d0ca35fcb5c0, url: https://www.notion.so/3c24dc662c2281c28a87d0ca35fcb5c0 }
---

# Harness-dokumentasjon

> [!callout icon=compass] **Harness** er alt rundt modellen: instruksjonene, mappene, skriptene, kommandoene. Repoet du fikk er en harness. Full detalj: `GUIDE.md` i repoet.

## Hva repoet består av

En **skill** er en oppskrift som bare leser og skriver notatene dine. Et **tool** når utenfor mappen: nettet, en tjeneste, maskinen. Begge er vanlige markdown-filer du kan åpne og lese.

| Del | Hva det er | Hvor |
| --- | --- | --- |
| **Agenten** | Claude Code eller Codex. Den har du installert selv. | utenfor repoet |
| **Manualen** | Én fil alle agenter leser først. `CLAUDE.md` peker bare hit. | `AGENTS.md` |
| **Skills** | Én fil per kommando. Når bare notatene dine. Ingen nett, ingen oppsett. | `brain/prompts/*.md` |
| **Tools** | Når ut av mappen: vær, sted, nyheter, undervisning. Fire stykker. Ingen trenger nøkkel eller oppsett. | `brain/tools/*.md` |
| **Skript** | Små hjelpere kommandoene bruker. `doctor` sjekker installasjonen. `sync` lagrer til git etter hver tur i Claude Code; i andre agenter kjører du den selv. | `brain/bin/` |
| **Hjernen din** | Notatene. Ren markdown, i git. | `cortex/` |

## PARA: hvor ting havner

Mappene sorterer etter om du skal gjøre noe med det nå, ikke etter tema. Da kan én hjerne holde jobb, sideprosjekt og livsadmin uten å bli et arkivskap med førti emnemapper.

> [!callout icon=lock] **Du skal aldri flytte filer selv.** Agenten bestemmer hvor ting havner, og `maintain` rydder etterpå. Havner noe feil, si det i én setning.

<details><summary>Mappene, én for én</summary>

| Mappe (under `cortex/`) | Innhold |
| --- | --- |
| `00_Inbox/` | Det den var usikker på. Skal være nesten tom. |
| `01_Projects/` | Ting med et mål og en slutt. |
| `02_Areas/` | Ting du har ansvar for hele tiden. Helse, økonomi, teamet. |
| `03_Resources/` | Selve kunnskapen, én idé per notat. Også profilen din, `[[About me]]`. |
| `04_Archive/` | Ferdige prosjekter, sovende områder. |
| `05_Attachments/` | Vedlegg. |
| `06_Sessions/` | Notater fra gamle kodeøkter. Dukker opp etter `ingest-sessions`. |
| `Daily/`, `Tasks/`, `raw/` | Ett notat per dag · ett per oppgave · urørte originaler |

Den ene forskjellen verdt å lære: Area vs. Resource.

- Et **Area** er et stående ansvar uten mållinje. Du kan ligge etter på det.

- En **Resource** er noe du leser heller enn handler på. Du kan ikke ligge etter på det.

«Maratontrening» er et Area. «Den artikkelen om VO2 max» er en Resource.

</details>

## Kommandoene, gruppert etter hva du vil

Du trenger ikke lære dem. Si hva du vil i én setning, så finner den riktig kommando selv. Men de finnes, og de heter:

### Første gang

- Skriv `start`. Den stiller seks spørsmål og skriver profilen din, `[[About me]]` og `[[How I learn]]`. Den bygger ingenting. Kjør den på nytt for å rette profilen.

- Skriv `teach me how this works` hvis du er usikker på hva du har installert.

### Legge inn

- Skriv `capture` og lim inn hva som helst: en tanke, en lenke, en beslutning. Den arkiverer det i dine ord. Dette er også det som skjer når ingen annen kommando passer.

- Skriv `task` for noe med en neste handling. Åpne, oppdatere, fullføre eller droppe.

### Hente ut

- Skriv `ask` og still spørsmålet. Svaret kommer fra dine egne notater, med lenker, og den merker hva som er ditt og hva som er allmennkunnskap.

- Skriv `brief` for en oppsummering av det siste: hva skjedde, mønstre, hva står fast, åpne tråder. Den henter vær og nyheter selv.

- Skriv `mirror` for å se alt hjernen mener om deg, linje for linje, med hvilket notat det kommer fra. Den endrer ingenting.

- Skriv `teach` og si hva du vil lære. Den finner ekte kilder på nettet og lager en leksjon tilpasset deg.

### Utenfor notatene

- Si «hva blir været» eller «nyheter», så bruker den `weather`, `location` eller `news` selv. Sammen med `teach` er det de fire toolene. De trenger bare nett.

### La den gjette

- Skriv `infer` og spør om noe notatene ikke sier rett ut. Den gjetter ut fra det som står, og merker hver gjetning. Den nekter før du har ti ekte notater.

- Skriv `review-assumptions` for å bekrefte eller avkrefte gjetningene, fem om gangen.

- Skriv `interview`, så er det hjernen som spør deg. Maks tre spørsmål.

### Skrive bedre

- Skriv `fix-my-prompt` og lim inn en prompt. Du får en bedre tilbake, klar til å limes inn, med én linje om hva som ble endret.

### Vedlikehold

- Kjør `./brain/bin/doctor` i terminalen. Den sjekker installasjonen og sier hva som må fikses.

- Skriv `maintain`. Den rydder notatene: avslutter dagen, tømmer innboksen, bygger indeksen på nytt.

- Skriv `ingest-sessions` for å gjøre gamle kodeøkter med Claude eller Codex om til søkbare notater.

- Skriv `new-idea` for å lage en ny evne. Se under.

<details><summary>For deg som koder: resten av `brain/bin/` og slash-kommandoene</summary>

`sync` kjører git pull og push etter hver tur i Claude Code. `run` starter en ny agent med en kommando som prompt, ment for en timer. `context` kjører når en samtale starter og leser inn profilen din. Pluss `feeds`, `weather`, `recent`, `check`, `agreement`, `friction`, `sessions`, `style`. Ingen av dem er kommandoer du skriver i chatten.

`.claude/commands/` er tynne innpakninger så `/capture` virker med autofullføring i Claude Code. De limer bare inn innholdet fra `brain/prompts/` eller `brain/tools/`.

</details>

## Legge til en ny evne

Skriv `new-idea` og beskriv hva du vil ha. Flyten er åtte faser: **Forstå → Utforsk (valgfri) → Enes → Planlegg → Gjennomgå → Bygg → Test (du, ikke den) → Finpuss.** Forstå, Gjennomgå og Test hoppes aldri over. Den hopper ikke rett til kode, og det er poenget.

## Koble til dine egne tjenester

Repoet har **ingen e-post- og ingen kalender-tool.** Det er med vilje. De når inn i de mest private kontoene du har, og hva et slikt tool får lov til bør du bestemme selv, ikke arve.

Vil du ha et, skriv `new-idea`. Den leder deg gjennom å koble kontoen til i agentens egne innstillinger og skriver tool-filen sammen med deg.

<details><summary>De tre reglene for alt du kobler til</summary>

Før noe kjører legger `new-idea` inn en sikkerhetsgjennomgang i tool-filen: hva den kan lese, hva den kan sende ut, og hva den gjør når en melding prøver å gi den instruksjoner. Tre regler gjelder uansett tjeneste:

- Den sender, endrer eller sletter aldri noe du ikke ba om i den meldingen, og så godkjente. Å lese krever ingen godkjenning. Alt som går ut krever begge deler.

- Ingenting den leser der skrives inn i notatene uten at du ber om det.

- Ingenting den leser der blir et faktum om deg. Den bestemmer ikke ut fra innboksen din hva du jobber med.

Se avsnittet «Connecting your own services» i `GUIDE.md`.

</details>

<details><summary>For deg som koder: hvorfor det er bygget sånn</summary>

- **Ikke låst til én leverandør.** Samme `AGENTS.md` for Claude, Codex, Cursor, Gemini.

- **Ingenting kjører på klokka.** Ingen cron, ingen bakgrunnsagent. Du ser alt som skjer.

- **Den merker sine egne slutninger.** Det agenten konkluderte står annerledes enn det den leste.

- **Alt er i git.** `git log` viser hva som skjedde. `git revert` angrer det.

Hele resonnementet står i `DESIGN.md`.

</details>

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg hva repoet består av: skills, tools, PARA-mappene og kommandoene. Siden jeg leser: https://www.notion.so/3c24dc662c2281c28a87d0ca35fcb5c0
