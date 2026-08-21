---
title: "Skills og kommandoer"
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
source: https://www.notion.so/3c24dc662c2281d38258e41074b0e9b6
aliases: []
notion: { page_id: 3c24dc66-2c22-81d3-8258-e41074b0e9b6, url: https://www.notion.so/3c24dc662c2281d38258e41074b0e9b6 }
---

# Skills og kommandoer

> [!callout icon=book] **Én setning:** en skill er en oppskrift i en markdown-fil. Agenten følger den når den passer, eller når du skriver navnet.

## Hva det er

Fire ord som går igjen. **Skills** er oppskrifter agenten følger, som `capture` og `ask`. **Tools** er det som når ut av mappen, som vær og nyheter. **Rutiner** er ting som kjøres på klokka. **Subagenter** er agenter som agenten starter for å gjøre en del av jobben. Kartet over repoet står i [Harness-dokumentasjon](https://www.notion.so/3c24dc662c2281c28a87d0ca35fcb5c0).

- En skill er en fil med instruksjoner. Ingen kode.

- Den lastes bare når den brukes. Lang referansetekst koster ingenting før du trenger den. Det er forskjellen fra `AGENTS.md`, som alltid er med.

- Lag en når du limer inn den samme sjekklisten for tredje gang, eller når en del av `AGENTS.md` har blitt en prosedyre i stedet for et faktum.

## I repoet

Hver skill er én fil i `brain/prompts/`. `capture`, `ask`, `brief`, `infer` og `new-idea` er alle skills. Du kan skrive navnet, eller bare si hva du vil. Agenten velger selv, i stillhet.

Åpne `brain/prompts/capture.md` og les den. Det er hele hemmeligheten.

<details><summary>For deg som koder: slash-kommandoene</summary>

`.claude/commands/` er tynne innpakninger som gjør at `/capture` virker med autofullføring i Claude Code. De limer bare inn innholdet fra `brain/prompts/` eller `brain/tools/`. Gemini har tilsvarende innpakninger i `.gemini/commands/`. Codex har ingen: der leser agenten `AGENTS.md` og du skriver navnet i en setning.

</details>

## Lage din egen

Den anbefalte veien: skriv `new-idea` og beskriv hva du vil ha. Den snakker med deg, planlegger og gjennomgår før den skriver filen. Til slutt gir den deg setningen du skal skrive for å teste, for det er du som tester. Resultatet havner i `brain/prompts/` (en skill) eller `brain/tools/` (et tool), og virker i alle agentene, ikke bare Claude Code.

<details><summary>For deg som koder: SKILL.md-snarveien</summary>

Den korte veien, bare for Claude Code: en fil på `.claude/skills/<navn>/SKILL.md`. Den virker ikke i Codex eller Cursor.

```
---
name: ukesrapport
description: Skriv ukesrapport fra Daily-notatene. Bruk når jeg ber om ukesrapport.
---

Les cortex/Daily/ for de siste 7 dagene.
Skriv tre avsnitt: hva skjedde, hva sto fast, hva er neste.
Maks 200 ord. Ikke finn på noe som ikke står i notatene.
```

`description` er det agenten bruker for å avgjøre når skillen passer. Skriv den som en setning om *når*, ikke bare *hva*.

</details>

> [!callout icon=graduate] **Forvirret?** Lim dette inn i samtalen med agenten din:
> /teach Forklar meg hva en skill er, hvordan kommandoene i brain/prompts/ virker, og forskjellen på new-idea og en SKILL.md. Siden jeg leser: https://www.notion.so/3c24dc662c2281d38258e41074b0e9b6

---

Videre lesning: [Extend Claude with skills](https://code.claude.com/docs/en/skills) og [Commands reference](https://code.claude.com/docs/en/commands).
