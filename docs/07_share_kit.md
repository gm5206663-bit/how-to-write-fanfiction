# 07 · Share Kit — templates, and how to use them

**Guide v3.0 · Law revision v5.4 · updated 2026-10-13.** The templates in [`../templates/`](../templates/) are the copy-paste contract of this method: each one is a working file from a real serial, genericised. Copy them into a new serial, fill the rulings first, and let the gates do the remembering.

---

## The nine templates

| Template | It becomes… | What it carries |
|---|---|---|
| [`STATUS_PANEL_TEMPLATE.md`](../templates/STATUS_PANEL_TEMPLATE.md) | the serial's `STATUS_PANEL.md` / `STATUS.md` | the single source of truth: identity card, exact figures, live edge, locks, next beat |
| [`SYSTEM_SPEC_TEMPLATE.md`](../templates/SYSTEM_SPEC_TEMPLATE.md) | `foundation/SYSTEM_SPEC.md` | the power system complete — rings, meters, grants, walls, evolution chain, fusion |
| [`METERS_TEMPLATE.md`](../templates/METERS_TEMPLATE.md) | `foundation/METERS.md` | every growth meter with its own pace law and its evolution line |
| [`SKILLS_CANON_TEMPLATE.md`](../templates/SKILLS_CANON_TEMPLATE.md) | `foundation/SKILLS_CANON.md` | skills described the way the canon describes them, with the per-technique evolution map |
| [`PANELS_TEMPLATE.md`](../templates/PANELS_TEMPLATE.md) | `foundation/PANELS.md` | panel grammar + the ledger of every line ever printed |
| [`CHARACTERS_TEMPLATE.md`](../templates/CHARACTERS_TEMPLATE.md) | `foundation/CHARACTERS.md` | cast, canon and ours, in full-status form |
| [`CHAPTER_TEMPLATE.md`](../templates/CHAPTER_TEMPLATE.md) | every `chapters/Chapter_NN.md` | the chapter skeleton: scene, footer, apparatus rules |
| [`SERIAL_FOUNDATION_TEMPLATE.md`](../templates/SERIAL_FOUNDATION_TEMPLATE.md) | `foundation/FOUNDATION.md` | the base of base: serial, lessons, locks, world rules |
| [`CANON_LEDGER_TEMPLATE.md`](../templates/CANON_LEDGER_TEMPLATE.md) | `foundation/CANON_LEDGER.md` | the receipts ledger — what canon was consumed, where it was fetched, when |

*The docset tree in [`02`](02_workflow.md) shows where each one lands.*

## How to use them

1. **Copy** `templates/` into your serial's `foundation/` — rename as you go (`STATUS_PANEL_TEMPLATE.md` → `STATUS_PANEL.md`, and so on).
2. **Rulings first.** Before any chapter: write the numbered rulings in your rulings file. **Any unanswered ruling locks drafting** — foundation stage is a stage, not a failure to start.
3. **Fill the docset**, adapting the fandom: the templates speak Soul Land and MCU because those are the worked examples; nothing in them requires either.
4. **Gate after every pass.** Run your battery; it must exit 0. A gate that fails wrongly gets fixed — with a receipt.
5. **Write the loop:** ORE → DRAFT → SELF-AUDIT → GATE → SYNC → SHIP. Repeat. Small things become big things if you skip.
6. **Adapt the demo gate** as a starting point for your own: [`../examples/minigate.py`](../examples/minigate.py) — five real checks, a config block to edit, and `--selftest` proving the gate can fail.

## What the templates deliberately contain

- **Placeholders that are honestly placeholders.** Where a real serial has numbers, the template has a shape — you cannot copy a wrong number by accident.
- **The evolution chain, marked per technique.** The skills canon template carries the per-technique map (never one line for everything — F26) so a new serial inherits the discipline, not just the words.
- **The F22 rule in the chapter skeleton.** The chapter template includes the panel rule — full panel only on update or gain; zero lines is legal — so every chapter starts with the right default.
- **The apparatus law.** Footers and state stamps stay out of the prose; the templates show where they live instead.

## Release hygiene

- Build the shareable zip with `tar`; keep git identity re-exported; **tokens never enter the tree** — the battery's privacy layer greps for them on every run.
- Release only what the gates have passed; the zip's build label is not a version — versions are the two axes in [`../VERSION_OF_RECORD.md`](../VERSION_OF_RECORD.md).
- Ship the templates with the docs they reference, so a reader never hits a dangling link (the PR checklist in [`../CONTRIBUTING.md`](../CONTRIBUTING.md) includes exactly this).

---

*Rebuilt 2026-10-13 from the compressed originals; template set and usage rules preserved — see [`../DEEP-PASS-2026-10-13.md`](../DEEP-PASS-2026-10-13.md).*
