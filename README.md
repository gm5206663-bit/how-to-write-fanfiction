<p align="center">
  <img src="assets/banner.png" alt="A writing desk at night: a glowing book, five golden spirit rings, a phoenix quill and blue-silver grass" width="100%">
</p>

# How to Write Gated Fan Fiction

**A production system for long-form fan fiction that stays true to its source — for hundreds of thousands of words.**

<p align="center">
  <a href="https://github.com/gm5206663-bit/how-to-write-fanfiction/releases"><img src="https://img.shields.io/badge/guide%20edition-v3.0-brightgreen?style=flat-square" alt="Guide v3.0"></a>
  <a href="https://github.com/gm5206663-bit/how-to-write-fanfiction/discussions"><img src="https://img.shields.io/badge/discussions-open-9cf?style=flat-square&logo=github" alt="Discussions"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT"></a>
</p>

> **Guide edition v3.0 · Law revision v5.4 · rebuilt 2026-10-13.** The two version axes are explained in [`VERSION_OF_RECORD.md`](VERSION_OF_RECORD.md) — where they disagree with any heading, that file wins.

---

## What this is

**This is not a vibe guide.** It is the working system behind a workshop of gated serials — every chapter machine-checked against its own laws before it ships. As of the 2026-10-13 measurement, the account holds **22 registered books · 375 chapters · 1,617,455 words**, of which the public library shelf carries **18 serials · 312 chapters · 1,351,161 words**. The method is proven across **16 Soul Land (斗罗大陆) serials plus Supergirl and two MCU serials**, and it is written to be **fandom-neutral** — the Soul Land and MCU work is the worked example, not the requirement.

Treat fan fiction like software. Give it a source of truth, tests, and state panels — and a story can grow forever without rotting.

## The problem: how fan fiction dies

Most long fan fiction dies one of five deaths. This method makes each death *structurally impossible* by attaching a law to it and a check that enforces the law.

| # | The death | The law | The check that enforces it |
|---|---|---|---|
| 1 | **Canon drift** — the fic contradicts or forgets the source | Canon-First Creation · Ledger-Canon: receipts, not memory | canon spine + canon ledger + gate scan + verbatim-plagiarism sweep (n-gram runs vs canon receipts) |
| 2 | **OC takeover** — the world bends around your original character | Multi-Panel Law: *canon always shown, never skipped; the OC added, never centered* | panel audit per chapter + panel ledger IN SYNC + drift guard that fails the build on a frozen meter |
| 3 | **Power inflation** — the OC becomes a god by chapter 20 | Unfixed Law: *power is a baseline, never a ceiling; traits are dated states* | status panel as single source of truth + banned-value scan |
| 4 | **Voice drift** — canon characters stop sounding like themselves | Style-match + personality-first | style gate with a prose band, average sentence length, and hard caps |
| 5 | **State rot** — the fic's own numbers no longer match its own text | Ship Law: update *everything* the same turn, or refuse to ship | generated status files + selftest + independent drift scan |

Each of those five deaths has a chapter of its own here — §1 in [`docs/01_the_laws.md`](docs/01_the_laws.md), the checks in [`docs/03_gates_and_audits.md`](docs/03_gates_and_audits.md), and the serials that paid for them in [`docs/04_case_studies.md`](docs/04_case_studies.md).

## The big idea in thirty seconds

1. **A source of truth per serial** — one status panel stating everything current; if a number isn't in it, the number doesn't exist yet.
2. **Receipts, not memory** — nothing enters a chapter unverified. Canon is fetched, quoted, and filed before it is written.
3. **A law only counts with a check** — every rule that matters is enforced by a script that can *fail*. A gate that has never been seen to fail is a gate nobody has tested.
4. **Update everything the same turn** — a chapter is not shipped until every state file agrees with it. "Later" is how state rots.
5. **One copy of one thing** — a document kept in two places will be wrong in one of them.

## How to read this repo

| Doc | Read it when |
|---|---|
| [`01 · The Laws`](docs/01_the_laws.md) | You want the constitution — all 31 entries of record, what each one says, the check that enforces it, and which serial paid for it |
| [`02 · The Workflow`](docs/02_workflow.md) | You are starting a serial — foundation docset, ore mining, and the six-step chapter loop |
| [`03 · Gates and Audits`](docs/03_gates_and_audits.md) | You want the machine room — the gate layers, what each one catches, and the selftest culture |
| [`04 · Case Studies`](docs/04_case_studies.md) | You want the proof — thirteen serials, what each taught, with numbers |
| [`05 · Glossary`](docs/05_glossary.md) | A term is unfamiliar (band, locks, ore, butterfly, drift guard…) |
| [`06 · Automation`](docs/06_automation.md) | You want your rules enforced by code, not memory |
| [`07 · Share Kit`](docs/07_share_kit.md) | You want the templates and a release checklist |
| [`08 · Advanced Edition`](docs/08_advanced_perfect_edition.md) | You want the technique-evolution and fusion laws in full |
| [`09 · MCU Adaptation`](docs/09_mcu_adaptation.md) | Your fandom is film/TV — camera law, film order, plural panels |
| [`10 · StoryOS and Control Centre`](docs/10_storyos_and_control_centre.md) | You want to publish: readers, state sites, and an agent console |
| [`templates/`](templates/) | You are ready to build the docset — nine copy-paste starting files |
| [`examples/minigate.py`](examples/minigate.py) | You want a working gate in one file — stdlib only, selftest included |

## Start in five minutes

```bash
# 1. Prove the demo gate catches defects (and passes clean prose):
python3 examples/minigate.py --selftest

# 2. Copy the contract into your serial:
cp -r templates/ my_serial/foundation/

# 3. Fill the rulings first — foundation stage is a stage, not a failure to start.
#    Drafting opens when the rulings are answered (see docs/02, Stage 1).

# 4. Chapter loop, forever:  ORE → DRAFT → SELF-AUDIT → GATE → SYNC → SHIP
```

## The scoreboard (measured 2026-10-13)

| Serial | Chapters | Words | Gates | What it taught |
|---|---:|---:|---|---|
| The Adaptive Prodigy | 116 | 523,356 | ten-layer, ALL GREEN | built the system; the two-copies law |
| Fire Phoenix | 52 | 270,659 | per-chapter validation | the five-copies disaster; pacing law (compress the routine, expand the butterfly) |
| The Unraveled Tide | 24 | 80,127 | run_all battery | the multi-panel law's home |
| Devouring Dragon | 24 | 65,081 | 8-tool battery, sentinel 26 PASS | plain-language law; panel re-bind; the canon-voice rollout |
| The Grey Wolf | 10 | 25,792 | run_all 4 steps, panel 10 IN SYNC | the perfect-rebuild standard: clean-and-clear prose, F0–F26 locks |
| Lan Shen (V2) | 7 | 32,211 | nine layers, ALL GREEN | dual-track canon-parallel; date arithmetic as the highest-yield check |
| One in a Thousand | 7 | 63,691 | gate PASS | the OC as the actor; canon complete but told tight |
| Stark Heir | 5 | 27,673 | mcu_verify 8 gates | MCU film order; camera law; plural panels |
| Fire Dragon Lizard | 5 | 18,605 | chapter gate | a complete small book |
| The Golden Lion | 8 | 22,487 | sl2-goldenv 8 PASS | agent-driven near-daily shipping; possession carding |
| Blue Silver (parked) | 15 | 34,711 | seven-gate maturity | small and gated can coexist; rebuild protocol |
| Supergirl — Adrian Vale | 17 | 61,986 | CI gates on every push | the 70-sentence ruling: a serial's compressed voice is the author's call |
| MCU Eternal — Varun | 3 | 9,212 | mcu_verify 8 gates | talent embodied, never named |
| Dragon Prince Yuan | 1 | 3,706 | gate PASS | a false FAIL is worth ten false PASSes |

**Combined:** 375 chapters across 22 registered books, 1,617,455 words — every shipped chapter gate-checked. The library shelf publishes 18 serials · 312 chapters · 1,351,161 words as one reading site.

## The law inventory

**31 entries of record:** F0–F26 (the soul-beast constitution, gaps at F1/F21/F24/F25 reserved forever) + P12 (camera law, for film/TV fandoms) + 7 structural laws (StoryOS · Control Centre · Soul Library · Dual-Track · Foundation-Stage · Ship Law · Clean-and-clear). The full list, each with its check and its receipts, is [`docs/01_the_laws.md`](docs/01_the_laws.md); `VERSION_OF_RECORD.md` carries the measured inventory and the history of how it was counted.

**Every law was paid for by a mistake.** The numbers are receipts — F26 exists because of one specific complaint, and it says so. That is why gaps stay gaps and laws are never renumbered.

---

## House rules

Add-only spirit (corrections supersede; they don't rewrite history) · claims carry receipts · a law without a check is a wish · be kind — fan fiction is love made public. Contributions welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License and provenance

MIT for everything here ([`LICENSE`](LICENSE)). This guide is fandom-neutral: your fandom's own rules for fan work outrank anything in it. Soul Land (斗罗大陆 / Douluo Dalu) and all related characters belong to Tang Jia San Shao and the original rights holders; everything in the workshop is non-commercial derivative fan work ([`NOTICE.md`](NOTICE.md)).
