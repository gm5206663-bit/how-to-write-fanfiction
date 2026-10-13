# 06 · Automation — tools that enforce the laws

**Guide v3.0 · Law revision v5.4 · updated 2026-10-13.** One principle runs through every tool here: **the law is written down once and enforced by a script, so nobody has to remember it.** Standard library only — no frameworks, no lock-in; every tool runs anywhere Python 3.9 runs. A runnable miniature of the whole idea ships in this repo: [`examples/minigate.py`](../examples/minigate.py).

---

## The toolchain at a glance

| Tool | Does | Enforces | Receipt |
|---|---|---|---|
| `measure_prose.py` | floor/ceiling/60-cap measurement | clean-and-clear band, avg 14–18, over-60 = 0 | measured every chapter of the Grey Wolf rebuild |
| `style_gate.py` | line-level voice and repetition check | the style law, no repetitive skill lists | caught the rejected avg-6.8 style |
| `canon_copy_check.py` | verbatim-plagiarism sweep vs canon receipts | receipts, not transcription | threshold rebuilt from corpus evidence after a real leak |
| `banned_token_check.py` | token/value drift sweep | bans — incl. no valid "MASTERED terminal" | purges the dead mastery model on every run |
| `plain_word_check.py` | plain-register wordlist audit | a serial's plain-language law | Devouring Dragon's register |
| `check_panels.py` | panel ledger + frozen-meter drift guard | F22 + F7 | a frozen meter fails the build |
| `verify.py` | scene-skeleton verification | canon beats + confidence tags | per-chapter coverage docs |
| `mcu_verify.py` | eight film/TV gates | zero-digit, zero-CJK, no footers, ASCII | Stark Heir and MCU Eternal, every push |
| `scan_project.py` | deterministic scope-line tracker | scope discipline (write once) | introduced by the Adaptive Prodigy |
| `run_all.py` / `checks/run_all.sh` | the battery — every layer, one command | *must exit 0* | the green run that precedes every ship |
| `selftest.py` | proves each gate can fail | the contract of a gate | injected defects, caught and named |
| `status_gen.py` | rebuilds the inventory from the tree | generated, never hand-edited | lan_shen pattern |
| `build_oc_status.py` | builds the OC status sheet from authority files | one current-state sheet | Devouring Dragon |
| `build_site.py` | builds the reading site from chapters | publishing, no frameworks | the shelf's own builder |
| `ship_chapter.py` | the ship checklist, mechanical 80% | Ship Law | refuses "shipped" until each step verifies |
| `register.py` | measures every book and every tree on the account | counts are measured, never typed | THE-COMPLETE-REGISTER, 24 books · 377 ch · 1,624,963 words |
| sentinel (library) | independent health scan | coverage line, fail-loud | 26 of 26 ran, 26 pass (2026-10-13) |

## How the pieces fit

```
   chapters/*.md
        │
        ├─ measure_prose → style_gate → canon_copy_check → banned_token_check → plain_word_check
        ├─ verify (scene skeleton) · mcu_verify (film/TV)
        └─ check_panels (ledger + drift guard)
                 │
            run_all  ← the battery, one command, must exit 0
                 │
   status_gen / build_oc_status  → the state files rebuilt from the tree
                 │
        build_site / shelf sync  → the reader
                 │
          ship_chapter  → commit, push, stamp the live edge
```

## The gates that carry the most weight

**`measure_prose.py` — the prose gate.** Band 2,400–3,400; average 14–18; over-60 zero; the-way zero; bare zero. Its receipts are the per-chapter numbers of the Grey Wolf rebuild — every chapter IN band, all gates PASS — and the rejection that started it all (avg 6.8, median 5).

**`style_gate.py` — the voice wall.** Repetition and skill-list spam are *line-level* defects that a word-count gate cannot see: this one reads like a hostile editor. It was written because a structural verifier passed a chapter that violated four separate doctrines.

**`canon_copy_check.py` — the plagiarism sweep.** Compares the chapter's narration and dialogue against the canon receipts by n-gram runs, quoted-run length, and density ceiling. Its threshold has its own receipt: after Lan Shen V1's transcribed dialogue (785 verbatim words; every borrowed run between 8 and 14 words under a threshold of 15) it was **rebuilt from corpus evidence** and made a regression test. The lesson stands in the tool: *a threshold is a claim; measure it.*

**`banned_token_check.py` — the memory of the workshop.** Reads a list of tokens and *values* that must never appear again — dead models, superseded numbers, fourth-wall leaks. On its first run it found nine fourth-wall breaks in shipped prose and two current-state documents asserting superseded values. The evolution-chain fix lives here too: a valid "100% MASTERED terminal" fails the sweep; only the explanatory quote of the fix is allowed.

**`check_panels.py` — the drift guard.** Every meter, every printed number, checked against the serial's authority file. **A frozen meter fails the build.** This is what makes F22 safe: chapters may print zero panel lines precisely because the ledger is machine-verified.

**`selftest.py` — the gate's gate.** Injected defects must be **caught and named** — not merely caught. A suite that fails silently is worse than none; this one prints a table of what it injected and what was caught. Same contract at repo level: `python3 examples/minigate.py --selftest`.

**`ship_chapter.py` — the ship checklist.** Runs the mechanical pipeline (measure → gate → sync generated files → commit → push → stamp the live edge) and **refuses to print "shipped" until every automated step verifies.** The authored 20% — the chapter's own final read — is declared in the checklist, never silently skipped.

## The evolution-chain automation (F14 · F23 · F26)

Three specific checks keep the model from regressing:

1. **Law presence** — the evolution-chain law and the fusion law must be findable in the tree. A law that fell out of the docs fails the check.
2. **Ban sweep** — a valid "MASTERED terminal" may not appear anywhere; only the explanatory quote of the fix is allowed.
3. **Examples intact** — the canonical line (Basic Walking Low → Silent Wind Step Mid → Ghost Frost Storm Step High → Storm Frost Ghost Veil Top, every grade a different name) must survive in the docs; and the footwork union is checked as **one line**, not three (F26).

## The register and the sentinel — counting is a gate too

**`register.py`** measures every book and every chapter-bearing tree on the account and prints what it found — nothing on disk holding prose may be unnamed, whether it is a gated book, a shelf copy, an archive, or a classified sighting. It exists because the account's own tools had been registering *what they happened to look at, not what was there* — the largest serial in the account had never been seen by any of them. Its output is [`THE-COMPLETE-REGISTER.md`](https://github.com/gm5206663-bit/the-authors-desk) (2026-10-13: 24 books · 377 chapters · 1,624,963 words · coverage 59 of 59 trees — reconciled the same afternoon).

**The library's sentinel** is the independence layer: 26 checks including the *coverage line* — and the coverage line is the operative check. On 2026-10-13 it reported "25 of 26 checks ran"; the missing check was traced (a stale anchor had silently stopped one check from running), fixed, and hardened so a vanished precondition now **fails loudly** instead of skipping. **26 of 26 ran, 26 pass.**

## Build and share hygiene

- Archives with `tar`, not `rsync`; git identity re-exported every shell; tokens never in the tree (a privacy grep runs as a battery layer).
- Releases contain only what passed the gates; a zip's own build label (like `v2.5-footwork-fusion-clean`) is a build label, **not a version** — the version axes are in [`../VERSION_OF_RECORD.md`](../VERSION_OF_RECORD.md).
- The CI form of the battery ships as [`examples/github-actions-gate.yml`](../examples/github-actions-gate.yml): every push runs the gate, and a red gate blocks the merge. **This guide now walks it on itself** — its live gate is [`.github/workflows/verify.yml`](../.github/workflows/verify.yml): the demo gate's selftest plus a full markdown link sweep ([`tools/check_links.py`](../tools/check_links.py)) on every push.

---

*Rebuilt 2026-10-13 from the compressed originals; every tool, law link, and receipt preserved — see [`../DEEP-PASS-2026-10-13.md`](../DEEP-PASS-2026-10-13.md).*
