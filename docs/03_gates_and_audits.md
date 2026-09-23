# 03 · Gates and Audits — how to build your own checker

A **gate** is a small program that must exit 0 before a chapter ships. This page tells you what it checks and how to build one. A complete working example lives at [`examples/minigate.py`](../examples/minigate.py) (~100 lines, stdlib only, with selftest).

---

## What a gate checks

| Check | Catches | Real bug it caught in my serials |
|---|---|---|
| **Banned-value scan** | prose stating numbers the panel has superseded or banned | stale copies of a project presented `Dawnflame 1,120` / `Dawn-Iron 2,040` as current — values the live panel explicitly banned |
| **Live-edge consistency** | README/panel claiming a different chapter than the disk | two archived copies frozen at Ch 31 while the serial was at Ch 52 |
| **Sequence integrity** | missing/duplicate chapter numbers | chapter files renamed by hand, leaving gaps |
| **Ledger footer** | chapters shipped without recording canon consumed + butterflies | whole chapters consuming canon with zero ledger trail |
| **Knowledge firewall** | the OC knowing something before the chapter that allows it | a reincarnator OC casually knowing cult secrets 40 chapters early |
| **Panel/wordcount floors** | chapters under the serial's own minimums | scenes that quietly thinned out mid-arc |

## The three rules of gates

1. **A gate must selftest.** Before trusting a checker, feed it known-bad input and prove it fires. My gates run a defect-class selftest (10/10 classes caught on the real ones; 5/5 on the minigate example). A check that has never caught anything is decoration.
2. **Never weaken the gate to pass it.** If the gate fails, the chapter is wrong or the panel is stale. Fix the *work*, not the *test*. The moment you edit a check "just to get through", the gate is dead and every future pass is a rubber stamp.
3. **Never trust only the project's own checker.** A checker shares the project's blind spots — if the scanner hard-codes the wrong filenames, it reads zero firewalls and says PASS (this happened: a project declared its firewalls in a file the scanner didn't know, the gate reported "0 firewalls", and a human almost believed it). The fix: an **independent drift scanner** built on different assumptions, run side-by-side. Two checkers that disagree is the most honest alarm in the system.

## Building your gate: the minimal recipe

```
CONFIG   = your serial's contract: banned values, firewall terms, floors, file layout
CHECKS   = pure functions: take the repo root, return pass/fail per rule
GATE     = run all checks, print PASS/FAIL lines, exit 0 only if all pass
SELFTEST = build tiny throwaway serials, each with exactly one defect,
           assert the gate fails on every one — and passes on a clean one
```

Design notes that matter:

- **Checks read files, never memory.** The gate's opinion of "current" comes from disk and the panel, not from what you remember writing.
- **One defect class per check.** When the gate fails, the message should name the file and the exact reason — a gate that says "something is wrong" is a gate you learn to ignore.
- **Exit codes are the contract.** `0` = ship. Non-zero = the loop is not finished. Wire it into your commit habit: *no green, no push.*
- **Keep it stdlib-only.** A checker with dependencies is a checker that breaks on a new machine. Mine run on bare Python 3.9+.

## The human audit (the other half)

The machine catches mechanical lies: wrong numbers, stale edges, missing ledgers. It cannot catch:

- **Voice** — does this canon character sound like themselves? (style-match, ore notes)
- **Centering** — did the OC quietly take over a canon moment? (panel audit)
- **Earned bends** — is this butterfly caused by the story so far, or by what I want to happen next?

That's the self-audit step: read your own chapter *as a reader who loves the source*, against every law, before the gate ever runs. Machine for facts, human for truth.

## Drift scanning (advanced)

When the workspace grows beyond one serial:

- Re-scan **everything** on a cadence, not just the serial you're writing.
- Compare generated artifacts (site, handoff text) against source state — regenerated-if-drifted, never hand-edited.
- Log every scan result with a date. A drift log is a serial's medical record: you want to see the moment things went wrong, not discover it a month later.

---

*Working example, ready to adapt: [`examples/minigate.py`](../examples/minigate.py) → run `python3 minigate.py --selftest` and watch it prove itself.*
