# 02 · The Workflow — from zero to a shipped serial

**Guide v3.0 · Law revision v5.4 · updated 2026-10-13.** Companion docs: the laws behind each step in [`01`](01_the_laws.md), the checks in [`03`](03_gates_and_audits.md), the templates in [`07`](07_share_kit.md).

---

## The shape of the whole thing

```
Stage 0  FOUNDATION STAGE   rulings first — zero chapters until the rulings are answered
Stage 1  THE DOCSET         ~20 files before chapter one — the serial's source of truth
Stage 2  ORE MINING         fetch and file the canon this serial will consume
Stage 3  THE CHAPTER LOOP   ORE → DRAFT → SELF-AUDIT → GATE → SYNC → SHIP — forever
Stage 4  REBUILD PROTOCOL   when the author says "clean and clear" — stop, audit, rebuild
Stage 5  PUBLISHING         reader site, state site, agent console
Stage 6  SHARE KIT          templates out, receipts in
```

---

## Stage 0 — Foundation stage: rulings first, prose second

A serial can exist, correctly, with **zero chapters on the page**. Stage zero means the author has answered questions and the answer is written down — that is a success state, not a delay (the Foundation-Stage law).

- Every ruling gets a number, a date, and the author's words — recorded verbatim in the rulings file.
- **Any ruling still open locks drafting.** The gate can check this mechanically: an unanswered ruling is a closed door.
- Serials that live here by design: *The Second Heartbeat* (butterfly registry and ripple rules before a word of prose), *Seed of Creation* (scaffolded, four rulings pending), *Clear Sky Lion* (stage 0 — rulings first, prose second, zero chapters by design).

Ask questions **before** writing, in writing. The Grey Wolf rebuild's first act was a question list, not a page.

## Stage 1 — The docset: the serial's source of truth

A gated serial needs roughly **twenty files** before chapter one. Not all serials carry all of them — the shape adapts — but the shape is always *the same kind of thing*: the current truth, in generated or maintained files, that chapters are written **out of**.

```
my_serial/
  README.md                premise (one paragraph) · reading order · live edge · next beat · map
  HANDOFF.md               cold-start brief: what is true NOW, authority order, which file wins on conflict
  STATUS.md                live inventory, auto-generated, never hand-edited
  LICENSE                  MIT for tooling; derivative-work notice for prose
  NOTICE.md                the fandom's IP disclaimer — fan-work terms
  foundation/
    FOUNDATION.md          base of base: serial, lessons, locks, world rules
    RULINGS_LOG.md         every author ruling, verbatim, numbered and dated
    SYSTEM_SPEC.md         the power system complete — rings, meters, grants, walls, the evolution chain
    STATUS_PANEL.md        THE single source of truth — see below
    METERS.md              every growth meter with its own pace law (F8)
    SKILLS_CANON.md        skills described the way the canon describes them (F19)
    PANELS.md              panel grammar + the ledger of every line ever printed
    TIMELINE.md            canon spine (receipted) + our road (dated) — the day map
    STORY_ARCS.md          the arc plan, marked against what shipped
    RELATIONSHIPS.md       cast web + the who-knows-what ignorance matrix
    CHARACTERS.md          cast, canon and ours, with current numbers
    CANON_GROUND.md        receipts: nothing enters a chapter unverified
    CODEX.md               file map + decision log
    RAILS.md               the serial's own laws of record
    OPEN_RULINGS.md        numbered decisions only the author can make
  chapters/                (empty until Stage 3 — and that is correct)
  canon_extract/chapters/  read-only receipts of the canon, never edited, never "corrected"
  canon_coverage/          per-chapter: which canon beats were consumed, with confidence tags
  tools/                   the gates (see 06) — style, panels, canon-copy, banned tokens, selftest…
  checks/run_all.sh        one command, every layer — must exit 0
  audits/                  dated audit records
```

Two files deserve their own paragraph:

**The status panel is the most important file in the serial.** Live edge, ranks, locks (what is fixed), bans (what is forbidden), relationships, next-chapter plan. When anything changes in the story, the panel changes the same turn. Everything else may be rebuilt from panel + chapters; **the panel may never be rebuilt from memory** (F7).

**The running inventory (`STATUS.md`) is generated, never hand-edited** — one command rebuilds it from the tree. A file that exists but is unregistered surfaces itself with a marker instead of hiding. Nothing hides.

## Stage 2 — Ore mining: fetch the canon before writing it

"Ore" is raw canon material gathered from primary text **before** drafting:

- Extract the canon chapters this arc will consume; keep an index of what is held and where from. Receipts are read-only: never edited, never silently corrected — if two readings exist, both are kept and the variance is logged.
- Convert secondary knowledge (wikis, summaries) into dated notes. **Secondary sources are ore, never law.** The canon ground file records what was verified, against what, when.
- Collect the *sound* of the source: speech patterns, running jokes, physical tells, the way the canon describes its own skills (F19) and its own beasts (F20). Style-matching starts here, not at the keyboard.
- **Never write from memory of the source.** Memory is where canon drift is born (F3).

For film/TV fandoms (see [`09`](09_mcu_adaptation.md)): ore means film beats, staged scene-by-scene in release order, receipts first — plural canon-side panels, and the camera law (P12).

## Stage 3 — The chapter loop

Per chapter, without exception:

```
   ┌──────────────────────────────────────────────────────────────┐
   │  1. ORE         read the canon chapters this one consumes    │
   │  2. DRAFT       write the chapter — prose law, panel rule    │
   │  3. SELF-AUDIT  check every law by hand; fix your own work   │
   │  4. GATE        run the machine checks — must exit 0         │
   │  5. SYNC        update EVERY state file, same turn           │
   │  6. SHIP        commit + push; stamp the live edge           │
   └──────────────────────────────────────────────────────────────┘
        ↑ repeat. small things become big things if you skip.
```

**1 · ORE.** Read/re-read the canon this chapter consumes; list it in the ledger. For dual-track serials: canon runs on the page, complete and unskipped, and the OC runs parallel on the same clock — butterflies are only logged where the tracks touch *on the page*.

**2 · DRAFT.** Write the chapter with the laws live in your hands: the evolution chain (techniques evolve; no terminal), the panel prose rule (a full panel only when something updates or is gained — **zero panel lines is a legal, deliberate number**), and clean-and-clear prose (band 2,400–3,400; average 14–18; no repetitive skill lists; mastery shown by daily-life action; lore in the footer, not the scene).

**3 · SELF-AUDIT.** Check every law by hand before the machine does — evolution chain (no terminal), fusion logic (movement+movement+body; mental+mental+mental; perception+perception+patience), panels (what printed, and does the ledger still match), prose (band/avg/caps), canon (nothing unverified), meters (every meter on its own pace).

**4 · GATE.** Run the machine checks. **Must exit 0.** A red gate is a stop, not a suggestion — and never lower a threshold to make a layer pass: fix the work if the work is wrong; fix the gate if the gate is wrong; do neither by accident.

**5 · SYNC.** Update **every** state file the same turn — panel, meters, skills, panels ledger, timeline, arcs, relationships, characters, canon ground, serial log, agent notes. Not "after the next chapter": the same turn. Later is how state rots.

**6 · SHIP.** Commit and push; stamp the live edge in the README and the panel. The ship script prints the mechanical checklist (measure → gate → sync generated files → commit → push → stamp) and refuses to say "shipped" until each automated step verifies — mechanical 80%, authored 20%, declared (the Ship Law).

## Stage 4 — The rebuild protocol

When the author says **"perfect rebuild"**, **"clean and clear"**, or **"no nonsense repetition"** — or flags a style with a number attached — the serial stops and rebuilds:

1. **Stop writing chapters.** Ask questions first. Check canon perfectly. No new prose until the foundations are approved (F6).
2. **Audit the project's own method** — how it writes, how it checks, what its panel says, what its audits missed. Correct completely; keep everything that works.
3. **Rebuild in passes.** Fix a layer, gate that layer, log the change, next layer. Never one giant silent edit.
4. **Purge superseded models.** When the model itself was wrong (e.g. the old mastery model), the fix is a law, a ban, and a sweep — not a note. All earlier references to the wrong model are corrected in the same pass.

The standard this protocol produced — the Grey Wolf's perfect rebuild — is the workshop's reference: prose inside the band every chapter, panels IN SYNC, locks applied, gates green, and the chapter whose average sentence was 6.8 median 5 (the rejected one) standing at avg 14–18 after rebuilding.

## Stage 5 — Publishing and state

- **Building the reader:** the shelf builds from the chapters with its own script; one static page, no frameworks, no tracking (see [`10`](10_storyos_and_control_centre.md)).
- **State for the account:** the Control Centre reads `state/` and generates its site and a plain-text bootstrap — a fresh agent reads one page and knows everything current.
- **State for the serial:** the inventory generator rebuilds `STATUS.md` from the tree every run — never hand-edited.
- **The ship script** carries the serial's whole mechanical checklist.

## Stage 6 — Share kit

- **Templates** (see [`07`](07_share_kit.md)): status panel, skills canon, meters, system spec, characters, panels, chapter, serial foundation — copy them into a new serial and fill rulings first.
- **Releases:** tag and zip only what the gates have passed; the zip's own build label is not a version — versions are the two axes in [`../VERSION_OF_RECORD.md`](../VERSION_OF_RECORD.md).

---

## The four advanced patterns

Four proven configurations; adopt the one your story needs.

1. **Dual-track canon-parallel (Lan Shen V2).** Canon runs complete and unskipped in the canon lead's own close-third; the OC lives parallel — same clock, same streets — and butterflies only exist where the tracks touch on the page. Needs a canon spine, a power law, and a knowledge firewall (what the OC knows, and when). *Nine layers, ALL GREEN.*
2. **Film-order dual-track (Stark Heir / MCU).** Canon consumed in film order, staged scene-by-scene, plural canon-side panels; the camera goes where canon goes; every touch of canon is registered in the T-registry. *(See [`09`](09_mcu_adaptation.md).)*
3. **Agent-driven near-daily (Golden Lion).** The serial advances daily with the agent driving between author rulings — safe only when the panel is the source of truth, possession is carded (base form, stack order, ring-orbit exposure), and the author's strikes are cheap to apply.
4. **Plain language + panel re-bind (Devouring Dragon).** A beast-voice serial: plain register, panels re-bound so the story is the beast's, pacing by compression (skip sameness, expand the butterfly), and the canon-voice rollout through three adaptation lenses.

Each pattern is one serial's earned answer, with receipts in [`04`](04_case_studies.md).

---

*Rebuilt 2026-10-13 from the compressed originals; every stage, pattern and receipt preserved — see [`../DEEP-PASS-2026-10-13.md`](../DEEP-PASS-2026-10-13.md).*
