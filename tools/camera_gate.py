#!/usr/bin/env python3
"""camera_gate.py — the narration gate (N1-N5).

Companion to `examples/minigate.py`. minigate checks the *ledger* (numbers,
canon claims, banned values). This checks the **voice**.

Five checks, all on the prose you actually ship:

  N1  no simile in narration      `like` / `as if` / `as though` outside speech
  N2  no interiority in narration felt / realized / wondered / seemed / thought about
  N3  dialogue share in band      default 45-70% of paragraphs
  N4  sentence average in band    default 8-14 words
  N5  spells announced, not narrated  `[Attribute] Magic: [Spell Name]!`

Why these and not "make it sound shonen": each one is a defect I shipped
myself, in a real chapter, and each one is decidable by a machine.

Usage:
    python3 tools/camera_gate.py chapters/
    python3 tools/camera_gate.py --selftest

The selftest is the point. A gate that has never been seen to fail is a gate
nobody has tested -- so every check here is proven on a fixture that commits
the defect.
"""
import os
import re
import sys

# ---- CONFIG: your serial's contract --------------------------------------
CONFIG = {
    "avg_min": 8.0,        # N4  shonen-source register; a literary source will want 14-18
    "avg_max": 14.0,
    "longest": 60,         # hard cap, any source
    "dialogue_min": 0.45,  # N3
    "dialogue_max": 0.70,
    "extensions": (".md",),
}

SIMILE = re.compile(r"\b(?:like|as if|as though)\b", re.I)                  # N1
INTERIOR = re.compile(                                                     # N2
    r"\b(?:felt|feels|realized|realised|wondered|wondering|seemed|"
    r"thought about|knew that|understood that|decided that)\b", re.I)
NARRATED_SPELL = re.compile(                                               # N5
    r"\b(?:cast|casts|casting|used|uses|using|fired|fires|shot|shoots|"
    r"threw|throws|summoned|summons|conjured|conjures)\s+"
    r"(?:a\s+|an\s+|his\s+|her\s+|their\s+)?[A-Za-z]+(?:\s+[A-Za-z]+)?\s+[Mm]agic\b",
    re.I)
WORD = re.compile(r"[A-Za-z']+")
SPEECH = ('"', "\u201c")


def strip_apparatus(text):
    """Drop fenced blocks, headings, captions and tables. Measure prose only."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    keep = []
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            continue
        if s.startswith(("#", ">", "|", "---", "***")):
            continue
        keep.append(s)
    return "\n".join(keep)


def paragraphs(prose):
    return [p.strip() for p in prose.split("\n") if p.strip()]


def narration(prose):
    """Every paragraph that is not speech -- the only place N1/N2 can fire."""
    return [p for p in paragraphs(prose) if not p.startswith(SPEECH)]


def sentences(prose):
    return [s for s in re.split(r"(?<=[.!?])\s+", prose.strip()) if s.strip()]


def words(s):
    return WORD.findall(s)


def check(text, name="chapter"):
    errs = []
    prose = strip_apparatus(text)
    paras = paragraphs(prose)
    if not paras:
        return [f"{name}: no prose found"], {}

    # N1 / N2 -- narration only. Dialogue is allowed to be lyrical; it is speech.
    for p in narration(prose):
        for label, pat in (("N1 simile in narration", SIMILE),
                           ("N2 interiority in narration", INTERIOR)):
            hit = pat.search(p)
            if hit:
                errs.append(f"{label}: {hit.group()!r} in {p[:60]!r}")

    # N3 -- dialogue share
    share = sum(1 for p in paras if p.startswith(SPEECH)) / len(paras)
    if not (CONFIG["dialogue_min"] <= share <= CONFIG["dialogue_max"]):
        errs.append(f"N3 dialogue share {share * 100:.0f}% outside "
                    f"{CONFIG['dialogue_min'] * 100:.0f}-{CONFIG['dialogue_max'] * 100:.0f}%")

    # N4 -- sentence average and cap
    ss = sentences(prose)
    wc = [len(words(s)) for s in ss]
    total = sum(wc)
    avg = (total / len(ss)) if ss else 0.0
    if not (CONFIG["avg_min"] <= avg <= CONFIG["avg_max"]):
        errs.append(f"N4 sentence average {avg:.2f} outside "
                    f"{CONFIG['avg_min']}-{CONFIG['avg_max']}")
    over = [w for w in wc if w > CONFIG["longest"]]
    if over:
        errs.append(f"N4 {len(over)} sentence(s) over {CONFIG['longest']} words, "
                    f"longest {max(over)}")

    # N5 -- a spell is announced in the source's format, never summarised
    for hit in NARRATED_SPELL.finditer(prose):
        errs.append(f"N5 spell narrated, not announced: {hit.group()!r} "
                    f"- write '[Attribute] Magic: [Spell Name]!'")

    stats = {"words": total, "paragraphs": len(paras), "sentences": len(ss),
             "avg": round(avg, 2), "longest": max(wc) if wc else 0,
             "dialogue": round(share * 100)}
    return errs, stats


# ------------------------------------------------------------------------- #
# selftest -- every check is proven on a fixture that commits its defect
# ------------------------------------------------------------------------- #

GOOD = """\
## ONE

A man stood behind a plough and held the handles.

"Good year," he said.

"Hup ho!"

The soil turned over. It went down the field in one black line.

"NOT YET!"

"I'm not giving up yet."

The birds came down behind it and took the worms out.

"One more time!"

"STOP PESTERING ME!"

She lifted her hand. Water came up out of nothing over her palm.

"WATER CREATION MAGIC: HOLY FIST OF LOVE!"

The water hit him in the chest and put him in the grass.

"Not yet, Sister. Not yet!"

He lay on his back and grinned at the sky.
"""


def selftest():
    cases = []

    def case(label, text, expect):
        errs, _ = check(text)
        cases.append((any(expect in e for e in errs), label,
                      [e for e in errs if expect in e][:1]))

    base, _ = check(GOOD)
    cases.append((not base, "clean canon-register chapter passes", base[:2]))

    case("N1 simile in narration is caught",
         GOOD + '\n\nThe gate opened like a mouth.\n', "N1")
    case("N2 interiority in narration is caught",
         GOOD + "\n\nHe felt the cold come up through his chest.\n", "N2")
    case("N5 narrated spell is caught",
         GOOD + "\n\nShe cast Water Magic and he fell down.\n", "N5")
    case("N3 all-dialogue chapter is caught",
         "\n".join(['"Yes."'] * 40), "N3")
    case("N3 a silent chapter is caught",
         "\n\n".join(["He walked up the road to the tower."] * 40), "N3")
    case("N4 long sentences are caught",
         GOOD + "\n\n" + " ".join(["word"] * 70) + ".\n", "N4")

    # N1/N2 must NOT fire on speech -- a character may talk like anything
    cases.append((
        not any("N1" in e or "N2" in e
                for e in check(GOOD + '\n\n"I felt like the sky was falling," she said.\n')[0]),
        "N1/N2 leave dialogue alone", []))

    # and a clean canon-register chapter must stay clean under the spell rule
    cases.append((not any("N5" in e for e in base), "N5 announced spell is clean", []))

    width = max(len(c[1]) for c in cases)
    failed = 0
    for ok, label, detail in cases:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            failed += 1
            for d in detail:
                print(f"        {d}")
    print()
    print(f"SELFTEST {'PASS' if not failed else 'FAIL'} — {len(cases) - failed}/{len(cases)}")
    return 0 if not failed else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    target = next((a for a in argv[1:] if not a.startswith("-")), ".")
    files = []
    if os.path.isdir(target):
        for dp, dns, fns in os.walk(target):
            dns[:] = [d for d in dns if d != ".git"]
            for fn in sorted(fns):
                if fn.endswith(CONFIG["extensions"]):
                    files.append(os.path.join(dp, fn))
    else:
        files = [target]
    if not files:
        print(f"camera_gate: no files under {target!r}")
        return 1

    bad = 0
    for f in files:
        errs, stats = check(open(f, encoding="utf-8").read(), os.path.basename(f))
        line = (f"  {os.path.basename(f)}: {stats.get('words', 0)} words · "
                f"avg {stats.get('avg', 0)} · longest {stats.get('longest', 0)} · "
                f"dialogue {stats.get('dialogue', 0)}%")
        print(line)
        for e in errs:
            print(f"    x {e}")
        bad += bool(errs)
    print()
    print(f"camera_gate: {len(files)} file(s), {bad} failing")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
