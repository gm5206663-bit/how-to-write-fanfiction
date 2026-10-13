# 03 · Gates and Audits — the machine room

**Guide v3.0 · Law revision v5.4 · updated 2026-10-13.** A law without a check is a wish; this doc is the checks. Tools are catalogued in [`06`](06_automation.md).

---

## The contract of a gate

Three rules, learned the hard way, govern every gate in this system:

1. **A gate must selftest.** Every tool ships with a test suite that *injects known defects* and proves the gate catches and names them. A gate that has never been seen to fail is a gate nobody has tested.
2. **Never weaken a gate to pass it.** If the gate is wrong, fix the gate — with a receipt. If the work is wrong, fix the work. Never lower the threshold so the run goes green.
3. **Never trust only the project's own checker.** The strongest configurations run an *independent* scan on top (the shelf's sentinel, StoryOS's drift scan) because a project grading its own homework can be consistently wrong.

And one culture rule that only exists because it repeatedly mattered: **a coverage line is a claim — it gets checked like one.** When a run says "25 of 26 checks", the missing check is a bug until explained. (Two real catches: a sentinel reporting *25 of 26* — traced to a check quietly skipping; and an earlier sentinel which said *26 of 22*.) A check that silently skips is a check that lies.

## The gate battery — layers

Each serial carries its own count — ten, nine, eight, seven layers — but the core is the same:

| Layer | Gate | What it catches |
|---|---|---|
| 1 | **Prose measure** | band violations (2,400–3,400 w), average sentence out of 14–18, any sentence over 60, banned constructions (the-way, bare fragments) |
| 2 | **Style gate** | repetition and voice drift — repetitive skill lists, line-level sameness, the serial's own voice law |
| 3 | **Canon copy check** | verbatim borrowing from the source — n-gram runs against the canon receipts (long quoted runs, density ceilings) |
| 4 | **Banned tokens** | terms and *values* that must never appear in prose — dead models ("100% MASTERED" as valid), fourth-wall leaks, superseded numbers |
| 5 | **Plain word check** | register drift — the plain-language law for serials that carry one |
| 6 | **Panel drift guard** | a frozen meter or stale line — fails the build rather than letting state rot |
| 7 | **Scope line scan** | deterministic tracking of scope lines across files |
| 8 | **Selftest** | the gate suite itself — every injected defect must be caught and named |
| 9 | **Status generation** | rebuilds the serial's live inventory from the tree; an unregistered file surfaces itself, nothing hides |
| 10 | **Verify / MCU verify** | scene-skeleton verification (canon beats, confidence tags) and the film/TV gate (zero digits, zero CJK glyphs in an English-MCU text) |

**The battery is one command and must exit 0.** A red layer is a stop; a green run with a skipped layer is not green (see the coverage rule above).

## The prose gate — clean and clear

The author's standard, enforced by measurement:

- **Band:** 2,400–3,400 words per chapter.
- **Average sentence length:** 14–18 words.
- **Over 60:** zero sentences over 60 words.
- **The-way constructions:** zero. **Bare fragments:** zero.
- **No repetitive skill lists in the body** — mastery is shown by daily-life *action*; lore dumps live in the footer or the status file.

Why so specific: the rejected chapter that produced this law averaged **6.8** words per sentence (median **5**), repeated "100% evolving High" in nearly every sentence, and repeated the same four canon phrases ten times. The rebuild that followed is the standard — see the Grey Wolf study in [`04`](04_case_studies.md).

## The panel gate — F22 plus the drift guard

- **F22 (panel prose rule):** a full panel prints in a chapter **only on change** — a level, a ring, a bloodline beat. Ordinary chapters may print **zero panel lines** and that is legal and deliberate; the status file holds the detail.
- **Drift guard:** every meter and every printed number is checked against the serial's authority file. A frozen meter — a number that stopped moving though its feeders grow — **fails the build**. State may not rot silently.
- **The ledger stays IN SYNC either way:** the panel ledger records every line ever printed, whether the chapter printed three lines or none.

## The canon gate — receipts, not memory

- **Nothing enters a chapter unverified (F3).** The canon this chapter consumes is fetched, quoted into the receipts folder, and cited in the chapter's coverage doc.
- **Receipts are read-only.** Never edited, never silently corrected; if two readings of the same passage exist, **both are kept and the variance is logged**.
- **Secondary sources are ore, never law** — a wiki note is a lead to check, not a citation to trust.
- **The copy check closes the loop:** the gate compares the chapter's narration and dialogue against the receipts (n-gram runs, quoted-run length, density ceilings) and fails on borrowing. The check's threshold itself has receipts: it was rebuilt from corpus evidence after a real leak (see Lan Shen in [`04`](04_case_studies.md)).

## The evolution-chain gate (F14 · F23 · F26)

- **Law presence:** the evolution-chain law and the fusion law must be *findable in the tree* — a law that fell out of the docs fails the check.
- **Ban sweep:** a valid "100% MASTERED terminal" may not appear anywhere; only the explanatory quote of the fix is allowed. The sweep is how the old model is kept purged (F23).
- **Fusion discipline:** the skills canon must show **one footwork line** (not three), and each technique's lineage must match the per-technique map in [`01`, Appendix B](01_the_laws.md).
- **Grades honest:** grade claims must match the exact-figures section of the status panel — a grade is a reading, not a label.

## The film/TV gate (MCU)

`mcu_verify.py` runs **eight gates**, including the rules that make an MCU text feel like a screenplay transcription where it must and a novel where it should: **zero digits** (numbers are written out — "nineteen beats", not "19") and **zero CJK glyphs** in an English text; no chapter footers; ASCII discipline. The camera law (P12) is checked through the coverage docs and the T-registry: every canon touch registered, every scene staged in film order from plural canon-side panels.

## Audit culture — the dated record

Every pass leaves a dated audit. The record currently includes: the **full comparative audit** (2026-09-20, Lan Shen — where the transcribed-dialogue leak and the butterfly-ledger stall were found), the **deep and full audits** (2026-10-10, lan_shen), the **ranking/rebuild validations** (Grey Wolf), the **chapter-52 validation** (Fire Phoenix's pacing arc), the **sentinel coverage catch** (2026-10-13 — the "25 of 26" traced to a silently skipping check and fixed to fail loudly), and the account-wide **scope sweeps** recorded in each repo's audit trail.

Two lessons the audits keep re-teaching, now written into the code:

- **A false FAIL is worth ten false PASSes.** A scanner once failed a chapter over hard-coded filenames from another project; the fix (a generic check) was worth more than a green run would have been. (Dragon Prince Yuan, [`04`](04_case_studies.md) §13.)
- **Read the number, don't trust it.** Every count in this repo — chapters, words, gates, laws — is re-measured before it is quoted. When this guide says 31 laws, it means the pin block was parsed programmatically; when it says 26 of 26 checks, it means the run printed the coverage line.

---

*Rebuilt 2026-10-13 from the compressed originals; every gate, layer, and audit receipt preserved — see [`../DEEP-PASS-2026-10-13.md`](../DEEP-PASS-2026-10-13.md).*
