# 02 · The Workflow — from empty folder to living serial

Six stages. The heart of the method is the loop in Stage 3 — everything before it exists only to make that loop safe to run forever.

---

## Stage 0 — Choose your lane

Decide **before writing a word**:

| Decision | Question | Example (Soul Land) |
|---|---|---|
| **Era / branch** | Which part of the source timeline? | Soul Land 2 (The Unrivaled Tang Sect era) |
| **Entry point** | Where does chapter 1 sit on the canon spine? | Canon ch 62–64, with a 4-year pre-canon butterfly |
| **Divergence policy** | How far will you follow canon before bending? | Follow canon by default; bend only when earned + logged |
| **Relation to other fics** | Same universe as your other serials, or separate? | Default: separate universe |

Write these as **numbered rulings** in `foundation/OPEN_RULINGS.md`. Any ruling the author hasn't answered = **drafting locked**. This is not bureaucracy — it's how you avoid rebuilding chapter 30 later.

## Stage 1 — The foundation docset

A gated serial needs roughly ten files before chapter 1:

```
my_serial/
  README.md                  one-paragraph premise + read order
  HANDOFF.md                 cold-start brief for any future collaborator/agent
  foundation/
    RAILS.md                 the serial's own laws of record
    OPEN_RULINGS.md          numbered decisions only the author can make
    CANON_SPINE.md           dated, sourced canon events this fic touches
    POWER_LAW.md             ranks, ages, costs, ceilings
    KNOWLEDGE_FIREWALLS.md   what the OC must not know yet (and from when)
    STATUS_PANEL.md          THE single source of truth for live state
    SERIAL_LOG.md            append-only: every session, every ruling
    CANON_LEDGER.md          every canon fact consumed + every butterfly
  chapters/
    (nothing yet)
  checks/
    verify.py                the gate (+ its selftest)
```

**The status panel is the most important file in the serial.** Live edge, ranks, locks (what's fixed), bans (what's forbidden), relationships, next-chapter plan. When anything changes in the story, the panel changes the same turn. Everything else may be rebuilt from the panel + chapters; the panel may never be rebuilt from memory.

## Stage 2 — Ore mining

"Ore" is raw canon material gathered **from primary text** before drafting:

- Extract the canon chapters this fic will consume; keep an `INDEX.txt` of what's held and where it came from.
- Convert wiki/secondary knowledge into **dated notes** — secondary sources are ore, never law.
- Record the good lines: speech patterns, running jokes, physical tells. Style-match starts here, not at the keyboard.

**Never write from memory of the source.** Memory is where canon drift is born.

## Stage 3 — The chapter loop

Per chapter:

1. **ORE** — read/re-read the canon chapters this chapter consumes. List them in the ledger.
2. **DRAFT** — write the chapter. Obey the prose method (registers, dialogue floor, word floor). Canon beats shown on the page; the OC beside them, never on top.
3. **SELF-AUDIT** — by hand, against every law. *Small things become big things*: a wrong number in chapter 7 is a continuity crisis in chapter 70. Fix your own garbles **before** the machine sees them — a gate is a safety net, not an editor.
4. **GATE** — run `verify.py`. It must exit 0. If it fails, fix the chapter or update the panel — never weaken the gate to pass.
5. **SYNC** — same-turn: status panel (edge, ranks, locks), canon ledger (facts consumed, butterflies added), serial log (what happened this session), continuation prompt (what's next), chapter footer (gate receipt).
6. **SHIP** — commit with a message that says what happened: `CH 3 SHIPPED — Monsters Run: …`. The commit log becomes the serial's heartbeat.

## Stage 4 — Publishing and state

When the serial outgrows a folder:

- **Control Centre pattern** ([the-universal-storyline-creation](https://github.com/gm5206663-bit/the-universal-storyline-creation)): state lives in data files (`state/*.json`); the site and the plain-text handoff are **generated** from them. You never edit the outputs — you change the state. One read and a stranger reaches correct state.
- **StoryOS pattern** ([storyos-site](https://github.com/gm5206663-bit/storyos-site)): publish the workspace as a reader + agent console — every file with its sha256, the gate's live output, and an **independent** drift scanner that does not trust the project's own checker. Two checkers that disagree is the most honest alarm system I've found.
- **Archive hygiene**: superseded material is never deleted, it is *moved with a dated receipt* to `_archive/` and marked DO-NOT-READ-AS-CURRENT. Provenance survives; staleness doesn't propagate.

## The rebuild protocol (when you inherit a mess)

If you already have chapters but no foundation:

1. Reconstruct the **status panel** from the chapters (not from memory).
2. Extract the **canon ledger** from what the chapters actually used.
3. Write the **banned-values list** from every number the prose states — then mark which are wrong.
4. Build the gate. Run it. **Do not fix the chapters yet** — first read the full failure list. Fixing before understanding is how you create new inconsistencies.
5. Fix in passes, gate after every pass, and log every change.

---

*Next: how to actually build the gate → [`03_gates_and_audits.md`](03_gates_and_audits.md).*
