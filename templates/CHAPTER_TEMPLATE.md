# Chapter Template

> The chapter file contract. The header declares what canon this chapter consumes; the footer is the gate receipt. Both are audited.

---

```
# Chapter <N> — "<Title>"

> **Canon consumed:** ch <A>–<B> (see ledger entries <###>–<###>)
> **Butterflies live in this chapter:** <B#, B#> (see ledger)
> **Continues from:** Chapter <N-1> — "<previous title>"

---

## Prose

<The chapter. Obey the prose method: plain language, registers,
dialogue floor ≥3 exchanges per scene, word floor <N> words.

Multi-Panel Law: canon beats shown on the page, never summarized away;
the OC stands beside canon, never on top of it.

Firewalls: the OC knows ONLY what the firewall table allows as of ch <N>.>

---

## Ledger

| # | Canon fact used | Source ch | Butterfly introduced |
|---|---|---|---|
| <###> | <fact> | <ch> | — |

## Self-audit (pre-gate, by hand)

- [ ] Every canon beat in range <A>–<B> is shown or consciously deferred (logged)
- [ ] OC does not center a canon character's moment
- [ ] All numbers match the status panel (dated <date>)
- [ ] No firewall term before its allowed chapter
- [ ] Voice check: canon characters sound like themselves
- [ ] Bends are earned by prior chapters and logged above

## Gate receipt

```
$ python3 checks/verify.py
  PASS  ...
GATE PASS   (exit 0)
```

**Status panel synced: YES/NO (must be YES, same-turn)**
```
