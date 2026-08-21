---
title: "Kom i gang"
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
source: https://www.notion.so/3c24dc662c2281449111d491617e2dc8
aliases: []
notion: { page_id: 3c24dc66-2c22-8144-9111-d491617e2dc8, url: https://www.notion.so/3c24dc662c2281449111d491617e2dc8 }
---

# Kom i gang

> [!callout icon=rocket] **Målet:** en assistent som svarer deg før presentasjonen er ferdig. Regn med et kvarter. Du trenger ikke kunne kode, og på vei 1 åpner du aldri en terminal. Står du fast, spør en av oss.

## Tre ting du trenger

| Du trenger | Hvorfor | Tid |
| --- | --- | --- |
| **Claude Code, installert** | Det er den som gjør jobben. [Desktop-appen](https://claude.com/claude-code) om du ikke vil se en terminal, CLI-en om du vil. Codex, Cursor og Gemini CLI fungerer også. | 5 min |
| **Et betalt abonnement** | Til agenten. Repoet koster ingenting. | fra ~$20/mnd |
| **Git** | Angreknappen din: alt agenten gjør i notatene kan spoles tilbake. På veien uten terminal setter du det ikke opp selv — agenten sjekker om det finnes, og loser deg gjennom den ene dialogboksen om det mangler. | 0–5 min |

En GitHub-konto er valgfri, men anbefalt. Den tar backup av hjernen din og lar deg lese notatene fra mobilen. Agenten hjelper deg med å koble den til i steg 4.

> [!callout icon=heart] **Du trenger ikke kunne git, programmering eller terminal.** Veien uten terminal åpner aldri en. Går noe galt senere, skriver du `doctor` i samtalen, så får du vite hva som er feil, på vanlig språk.

<details><summary>Terminal eller app?</summary>

- **Desktop-appen til Claude Code.** Beste valg om du ikke vil ha terminal. Åpne mappen som prosjekt. Samme kommandoer, samme repo, ingen forbehold.

- **Terminalen.** Det vi bruker selv. `claude` eller `codex` i mappen. Vei 2 nedenfor.

- **Claude Cowork og claude.ai.** Cowork leser ikke instruksjonene i mappen og lagrer ikke til git av seg selv. claude.ai når ikke mappen i det hele tatt. Bruk desktop-appen i stedet.

</details>

## Vei 1: Uten terminal (desktop-appen)

**1. Hent mappen.** Åpne [repoet](https://github.com/Sebastian-Sole/second-brain-demo) i nettleseren, klikk den grønne **Code**-knappen, så **Download ZIP**. Pakk ut, gi mappen et navn du liker — `min-hjerne` — og legg den et sted du finner den igjen, for eksempel i Dokumenter.

**2. Pek Claude Code på mappen.** Installer [desktop-appen](https://claude.com/claude-code) om du ikke har den, og åpne mappen som prosjekt. Første gang spør den om du stoler på mappen. **Svar ja.** Ellers bruker den ikke tillatelseslisten som følger med, og spør om alt.

**3. Skriv `doctor`.** Assistenten sjekker at alt er på plass og tar deg gjennom det som mangler, én ting om gangen, på vanlig språk. Be den fikse det den finner — blant annet skrur den på angreknappen (git), slik at alt den noensinne gjør i notatene dine kan rulles tilbake. Når `doctor` er fornøyd, er du klar.

**4. Backup på GitHub (valgfritt, anbefalt).** Lag et tomt, privat repo på [github.com/new](https://github.com/new) — ingen README, ingen .gitignore. Si så til agenten: «koble denne mappen til GitHub-repoet mitt», og lim inn lenken. Da er hjernen din sikkerhetskopiert og lesbar fra mobilen. `doctor` maser til dette er på plass.

## Vei 2: For deg som koder (terminal)

Klon, kutt kopien løs fra repoets historikk så notatene du skriver er dine, sjekk, kjør:

```
git clone https://github.com/Sebastian-Sole/second-brain-demo.git my-brain
cd my-brain
rm -rf .git && git init && git add -A && git commit -m "my second brain"
./brain/bin/doctor   # fiks alt som er merket [XX]
claude               # eller codex, eller det du installerte
```

`rm -rf .git` sletter repoets historikk, så du starter med din egen. Det rører ikke et eneste notat. Svar ja når Claude Code spør om du stoler på mappen. Backup er steg 4 ovenfor — for hånd:

```
git remote add origin https://github.com/<deg>/<ditt-repo>.git
git push -u origin main
```

## Uansett vei: si `start`

Skriv **`start`**. Den stiller seks spørsmål, ett om gangen. Svarene havner i to notater du kan åpne og redigere: `[[About me]]` og `[[How I learn]]`. Den foreslår også linjer til avtalen `[[How we work together]]`, som du godkjenner. Til slutt peker den på `new-idea`. Ikke hopp over dette. Du kan kjøre `start` på nytt senere for å rette profilen.

## Usikker på hva du installerte?

Skriv **`teach me how this works`**. Den forklarer hva du har installert, på ditt nivå, og kan lage en leksjon av det om du vil.

---

Neste: [[Harness-dokumentasjon]] forklarer hva du nettopp har installert. Eller bare begynn å snakke med den.

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg hvordan jeg kommer i gang: hente mappen, åpne den i Claude Code, la agenten kjøre doctor, og si start. Siden jeg leser: cortex/03_Resources/Fagdag/Kom i gang.md
