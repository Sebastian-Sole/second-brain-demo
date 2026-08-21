---
title: "Når det skjærer seg"
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
source: https://www.notion.so/3c24dc662c2281d38f8dff0e3b39b7e1
aliases: []
notion: { page_id: 3c24dc66-2c22-81d3-8f8d-ff0e3b39b7e1, url: https://www.notion.so/3c24dc662c2281d38f8dff0e3b39b7e1 }
---

# Når det skjærer seg

> [!callout icon=first-aid] Siden du åpner **mens** du bygger. Hvert punkt er en frustrasjon vi har hørt, og det i repoet som skal fikse den.

<details><summary>**«Den leser ikke tankene mine.»**</summary>

Nei. Avtalen er at agenten spør når den ikke vet. Gjør den ikke det, si det: «spør meg før du antar». Profilen fra `start` og `interview` er det som gjør at den trenger å spørre mindre over tid. Kjør `start` på nytt om profilen er feil.

</details>

<details><summary>**«Den gjetter i stedet for å spørre.»**</summary>

Bedre å spørre enn å anta feil. Skriv `ask` og still spørsmålet, så viser den alltid hva som kom fra notatene dine og hva som ikke gjorde det. `infer` merker hver gjetning: det den vet, det den antar, og hva som ville fått den til å snu. Be om det samme i egne prompts.

</details>

<details><summary>**«Den krangler når jeg retter den.» / «Den bare beklager, og gjør det samme igjen.»**</summary>

Samme trekk, to utslag: den sier seg enig i stedet for å sjekke. Har du rett, står den på sitt. Tar du feil, sier den «du har helt rett».

- Be den **sjekke**, ikke bekrefte. «Se i notatet og si hva som faktisk står der», ikke «er ikke dette feil?».

- Ikke spør «er du sikker?». Den snur oftere enn den burde, også når den hadde rett. Vi gjør det samme: folk snur ofte et riktig svar når modellen presser tilbake.

- Rettet den på det samme to ganger? Slutt å rette. Ny samtale, med én setning om hvor dere var. Feilen ligger igjen i samtalen og drar den tilbake.

- En unnskyldning er ikke en fiks. Be om å se endringen, ikke en bekreftelse på at den er gjort.

</details>

<details><summary>**«Jeg må sjekke alt, så hva er poenget?» / «Den sier ferdig når det ikke er ferdig.»**</summary>

Riktig observasjon, feil konklusjon. Løsningen er at noe annet enn agenten sjekker. Teknisk: `doctor`, et skript, en test. Menneskelig: deg, én ting om gangen. Spør «hvordan ser ferdig ut?» før den starter.

</details>

<details><summary>**«Den glemmer. Jeg må forklare alt på nytt hver gang.»**</summary>

Notatene er hukommelsen, ikke samtalen. Skriv `capture` og lim inn beslutningen, så finner `ask` den igjen om tre uker. `new-idea` skriver en plan før den bygger, så neste samtale kan lese den.

</details>

<details><summary>**«Den skrev noe feil i notatene mine.»**</summary>

Si det i én setning, så flytter eller retter den det. Gjentar feilen seg, si «remember that», så foreslår den en regel i avtalen dere har. Og alt er i git: `git log` viser hva som skjedde, `git revert` angrer det. Se «When it gets something wrong» i `GUIDE.md`.

</details>

<details><summary>**«doctor sier [XX].»**</summary>

Den sier nøyaktig hva som er feil og hvordan du fikser det. Les linjen under `[XX]`. Står du fortsatt fast, lim hele utskriften inn til agenten og si «fiks dette».

</details>

---

## Det den aldri gjør

- Sletter notater. Gamle notater markeres og beholdes.

- Sender, endrer eller sletter noe du ikke ba om. Det følger ikke med noe som når e-post eller kalender. Vil du koble til noe, skriv `new-idea`.

- Kjører noe på klokka uten at du har satt det opp. Ingen cron, ingen bakgrunnsagent.

- Skriver noe om deg i profilen din som du ikke har sagt.

Hele listen står under «What it will never do» i `GUIDE.md`.

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg hva jeg gjør når AI-agenten min gjetter, krangler, glemmer, sier «ferdig» for tidlig eller skriver feil i notatene, og hva den aldri gjør. Siden jeg leser: cortex/03_Resources/Fagdag/Når det skjærer seg.md
