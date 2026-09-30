# VERSION_OF_RECORD.md — the single answer to "which version is this?"

**Added 2026-09-30 (add-only).** This file exists because the repo carried five
different version tags at once with no stated relationship between them, and
because the law count in the title did not match the law count in the file.
Where this file and any heading disagree, this file wins until the author
strikes it.

---

## The two axes — they were never the same number

The repo mixed two independent version lines into one heading, which is why
"v2.1" and "v5.1" appeared to contradict each other. They do not. They count
different things.

| Axis | Version of record | What it counts |
|---|---|---|
| **Guide edition** | **v2.1 Advanced Perfect Edition** | The shape of this repository — docs 01-10, templates, examples, the scoreboard. Bumps when the *guide* changes. |
| **Law revision** | **v5.4** | The F-series itself. Bumps when a *law* is struck, replaced or fused. |

So the correct full citation is:

> **Guide edition v2.1 Advanced Perfect Edition, law revision v5.4.**

Every "Evolution Chain Fix" tag in the repo refers to the **law** axis, not the
guide axis. The chain ran v5.0 → v5.1 (evolution chain, no terminal) → v5.2
(different name per grade) → v5.4 (footwork fusion). There is no v5.3 on record.

### Superseded tags found in the tree

| Tag | Occurrences | Status |
|---|---|---|
| `v5.1` | 171 | Superseded by v5.2 then v5.4. Content is still correct; only the tag is old. |
| `v2.1` | 86 | **Current** on the guide axis. |
| `v5.4` | 39 | **Current** on the law axis. |
| `v5.2` | 19 | Superseded by v5.4. |
| `v5.0` | 16 | Superseded. Still correct as a historical label for the perfect rebuild. |
| `v0.7.0` | 15 | Not this repo — Grey Wolf's own serial version. Leave alone. |
| `v2.0`, `v4.0`, `v1.0` | 6, 2, 1 | Historical. `v2.0` appears in "What v2.1 Adds Over v2.0", which is correct usage. |

The zip `how-to-write-fanfiction-v2.5-footwork-fusion-clean.zip` carries a
`v2.5` tag that appears nowhere else in the tree. It is a build label, not a
law revision. Left as-is; do not cite it as a version.

**No heading was mass-rewritten.** Retagging 171 occurrences of `v5.1` would
bury every real diff under cosmetic churn. The rule going forward: new content
cites **law revision v5.4**; existing content is left until it is touched for a
real reason, and retagged then.

---

## The law inventory, measured 2026-09-30

The title of `docs/01_the_laws.md` said **"25 laws"** and the README said
**"F0-F22"**. Both were stale. Measured from the compressed pin block plus a
full grep of the repo:

```
F-series in the pin (docs/01):  F0, F2-F20, F22                    = 21
F-series recorded elsewhere  :  F23, F26                           =  2
P-series                     :  P12 (MCU camera law)               =  1
Structural laws              :  StoryOS, Control Centre, Soul
                               Library, Dual-Track, Foundation-Stage,
                               Ship Law, Clean-and-clear            =  7
                                                                    ----
                                    ENTRIES OF RECORD                = 31
```

**Was:** "25 laws" / "F0-F22". **Now:** 31 entries of record, F-series running
F0-F26. **Reason:** the count had not been re-measured since F23 and F26 were
added to the templates and docs but never to the pin.

### Numbers never assigned

`F1`, `F21`, `F24`, `F25`, `F27+` — **zero occurrences anywhere in the repo.**
They are gaps, not lost laws. Do not fill them by renumbering: the numbers are
receipts, and a renumbered law loses the mistake that paid for it. New laws take
the next free number above F26.

### The two that were recorded but never pinned

Both already existed in the tree. They were **consolidated into
`docs/01_the_laws.md` verbatim**, not rewritten — AGENTS.md rule 4, author
rulings are never paraphrased into something better.

- **F23** — Evolution Chain Fix, `v5.1`. Present in `docs/05_glossary.md`
  (which correctly says "Locks F0-F23"), `docs/08_advanced_perfect_edition.md`,
  `docs/10_storyos_and_control_centre.md`. Absent from the pin. Same content
  family as F14/F18.
- **F26** — the footwork fusion complaint. Present in
  `SYSTEM_SPEC_TEMPLATE.md`, `STATUS_PANEL_TEMPLATE.md`,
  `SKILLS_CANON_TEMPLATE.md`, and in the Footwork Fusion Law section of
  `docs/01_the_laws.md` itself — cited as "User complaint (F26)" by a law that
  did not appear in its own numbered list.

---

## Still open — needs the author, not an agent

1. **Which version axis wins in headings?** This file proposes citing both
   (`v2.1 / law v5.4`). If the author would rather collapse to one number, say
   which and every heading gets retagged in one pass.
2. **Should `F1` and `F21` stay empty forever?** Recommended: yes, marked
   reserved-never-assigned so no future agent "finds" a gap and fills it.
3. **The Control Centre schema gap** (separate repo, filed as `note#32`):
   `PROJECT_STATUSES` in `schema.py` defines nine values, but
   `projects_registry.json` holds three outside that list — `blocked`,
   `complete`, `dropped`. Either add them with selftest cases or correct the
   three projects onto defined values. Both change a rule.

---

*Receipt: measured 2026-09-30 by grep and by parsing the compressed pin block
programmatically, not by reading the title and believing it.*
