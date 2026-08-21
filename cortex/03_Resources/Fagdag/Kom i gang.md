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

> [!callout icon=rocket] **Målet:** en assistent som svarer deg før presentasjonen er ferdig. Regn med et kvarter om agenten alt er installert. Står du fast, spør en av oss.

## Tre ting du trenger

Terminalen er programmet der du skriver kommandoer. På Mac heter det Terminal. Trykk cmd + mellomrom, skriv Terminal, trykk Enter.

| Du trenger | Hvorfor | Tid |
| --- | --- | --- |
| **En AI-kodeagent, installert** | Det er den som gjør jobben. Vi anbefaler [Claude Code](https://claude.com/claude-code). Codex, Cursor og Gemini CLI fungerer også. | 5 min |
| **Et betalt abonnement** | Til agenten. Repoet koster ingenting. | fra ~$20/mnd |
| **Git og en terminal** | Git er angreknappen din. Alt agenten gjør i notatene kan spoles tilbake. På Mac: skriv `git` i terminalen. Får du en feilmelding, skriv `xcode-select --install`. | 5 min |

En GitHub-konto er valgfri, men anbefalt. Den tar backup av hjernen din og lar deg lese notatene fra mobilen.

> [!callout icon=heart] **Du trenger ikke kunne git eller programmering.** Du må være villig til å skrive noen få kommandoer én gang. Går noe galt senere, sier `doctor` (sjekken i steg 3) hva som er feil, på vanlig språk.

<details><summary>Terminal eller app?</summary>

- **Terminal.** Det vi bruker. Alt i repoet er laget for den. `claude` eller `codex` i mappen.

- **Desktop-appen til Claude Code.** Beste valg om du ikke vil ha terminal. Åpne mappen som prosjekt. Samme kommandoer, samme repo.

- **Claude Cowork og claude.ai.** Cowork leser ikke instruksjonene i mappen og lagrer ikke til git av seg selv. claude.ai når ikke mappen i det hele tatt. Bruk desktop-appen i stedet.

</details>

## 1. Hent repoet

1. Åpne [repoet](https://github.com/Sebastian-Sole/second-brain-demo) i nettleseren.

1. Klikk den grønne **Code**-knappen, så **Download ZIP**.

1. Pakk ut. Åpne Terminal, skriv `cd ` (med et mellomrom etter), dra mappen inn i vinduet og trykk Enter. Kjør så `git init && git add -A && git commit -m "my second brain"`.

<details><summary>For deg som koder: med git clone</summary>

Åpne terminalen og lim inn:

```
git clone https://github.com/Sebastian-Sole/second-brain-demo.git my-brain
cd my-brain
rm -rf .git && git init && git add -A && git commit -m "my second brain"
```

`rm -rf .git` sletter repoets historikk, så du starter med din egen. Det rører ikke et eneste notat.

</details>

## 2. Backup på GitHub (valgfritt, anbefalt)

Lag et tomt, privat repo på GitHub. Be agenten koble det til: «koble denne mappen til GitHub-repoet mitt», og lim inn lenken. Da er hjernen din sikkerhetskopiert og lesbar fra mobilen. `doctor` maser til dette er på plass.

<details><summary>For deg som koder: kommandoene</summary>

```
git remote add origin https://github.com/<deg>/<ditt-repo>.git
git push -u origin main
```

</details>

## 3. Sjekk at det virker

Skriv dette i terminalen, i mappen:

```
./brain/bin/doctor
```

Den sier hva som mangler og hvordan du fikser det. Fiks alt som er merket `[XX]`.

## 4. Start agenten

1. Skriv `claude` (eller `codex`) i terminalen, i mappen. Bruker du desktop-appen: åpne mappen som prosjekt.

1. Claude Code spør om du stoler på mappen. **Svar ja.** Ellers bruker den ikke tillatelseslisten som følger med, og spør om alt.

## 5. Si `start`

Skriv **`start`**. Den stiller seks spørsmål, ett om gangen. Svarene havner i to notater du kan åpne og redigere: `[[About me]]` og `[[How I learn]]`. Den foreslår også linjer til avtalen `[[How we work together]]`, som du godkjenner. Til slutt peker den på `new-idea`. Ikke hopp over dette. Du kan kjøre `start` på nytt senere for å rette profilen.

## 6. Usikker på hva du installerte?

Skriv **`teach me how this works`**. Den forklarer hva du har installert, på ditt nivå, og kan lage en leksjon av det om du vil.

---

Neste: [Harness-dokumentasjon](https://www.notion.so/3c24dc662c2281c28a87d0ca35fcb5c0) forklarer hva du nettopp har installert. Eller bare begynn å snakke med den.

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg hvordan jeg kommer i gang: hente repoet, kjøre doctor, starte agenten og si start. Siden jeg leser: https://www.notion.so/3c24dc662c2281449111d491617e2dc8
