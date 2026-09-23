#!/usr/bin/env python3
"""minigate — a minimal chapter gate for fan fiction serials.

Demonstrates five checks every chapter should pass before shipping.
Standard library only (Python 3.9+). Adapt CONFIG to your serial, then:

    python3 minigate.py /path/to/your/serial     # run the gate
    python3 minigate.py --selftest              # prove the gate catches defects

Gate rules (see docs/03_gates_and_audits.md):
  1. a gate must selftest  2. never weaken the gate to pass it
  3. never trust only the project's own checker
"""
import os
import re
import sys
import tempfile

# ---- CONFIG: the contract of YOUR serial --------------------------------
CONFIG = {
    "chapters_dir": "chapters",
    "readme_file": "README.md",
    "banned_values": {                 # term -> values the prose must NEVER state
        "Dawnflame": ["1,120", "1120"],
        "Dawn-Iron": ["2,040", "2040"],
    },
    "live_edge_regex": r"Live edge:?\s*\*\*after Chapter\s*(\d+)",
    "chapter_regex": r"Chapter_(\d+)\.md$",
    "ledger_marker": "## Ledger",      # every chapter file must carry this footer
    "forbidden_before_chapter": {      # knowledge firewall: term -> first allowed chapter
        "Holy Spirit Cult": 40,
    },
}


def _say(passed, msg):
    print(("  PASS  " if passed else "  FAIL  ") + msg)
    return passed


def _chapters(root):
    cdir = os.path.join(root, CONFIG["chapters_dir"])
    if not os.path.isdir(cdir):
        return []
    files = [f for f in sorted(os.listdir(cdir)) if re.search(CONFIG["chapter_regex"], f)]
    return [os.path.join(cdir, f) for f in files]


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _num(path):
    return int(re.search(CONFIG["chapter_regex"], os.path.basename(path)).group(1))


# ---- checks: one defect class each --------------------------------------
def check_sequence(paths):
    nums = [_num(p) for p in paths]
    ok = bool(nums) and nums == list(range(1, len(nums) + 1))
    return _say(ok, f"chapters: {len(nums)} files, sequence 1..{len(nums)}, no gaps"), nums


def check_banned_values(paths):
    hits = []
    for p in paths:
        text = _read(p)
        for term, bad in CONFIG["banned_values"].items():
            for v in bad:
                if v in text:
                    hits.append(f"{os.path.basename(p)}: banned value for {term}: {v}")
    for h in hits:
        _say(False, h)
    return _say(not hits, "banned-value scan: clean")


def check_live_edge(root, nums):
    readme = _read(os.path.join(root, CONFIG["readme_file"]))
    m = re.search(CONFIG["live_edge_regex"], readme, re.IGNORECASE)
    claimed = int(m.group(1)) if m else -1
    actual = max(nums) if nums else 0
    return _say(claimed == actual, f"live edge: README claims Ch{claimed}, disk has Ch{actual}")


def check_ledger_footers(paths):
    missing = [os.path.basename(p) for p in paths if CONFIG["ledger_marker"] not in _read(p)]
    for f in missing:
        _say(False, f"{f}: missing '{CONFIG['ledger_marker']}' footer")
    return _say(not missing, "ledger footer present in every chapter")


def check_firewalls(paths):
    hits = []
    for p in paths:
        n, text = _num(p), _read(p)
        for term, first in CONFIG["forbidden_before_chapter"].items():
            if n < first and term.lower() in text.lower():
                hits.append(f"{os.path.basename(p)}: firewall breach — '{term}' before Ch {first}")
    for h in hits:
        _say(False, h)
    return _say(not hits, "knowledge firewalls: clean")


# ---- the gate ------------------------------------------------------------
def run_gate(root, quiet=False):
    if quiet:
        global _say
        _orig, _say = _say, lambda p, m: p
    try:
        print(f"minigate: {root}")
        paths = _chapters(root)
        ok, nums = check_sequence(paths)
        if not paths:
            print("GATE FAIL")
            return 1
        ok &= check_banned_values(paths)
        ok &= check_live_edge(root, nums)
        ok &= check_ledger_footers(paths)
        ok &= check_firewalls(paths)
        print("GATE PASS" if ok else "GATE FAIL")
        return 0 if ok else 1
    finally:
        if quiet:
            _say = _orig


# ---- selftest: a gate must prove it catches defects ----------------------
def _mkserial(chapters, readme_edge):
    d = tempfile.mkdtemp(prefix="minigate_")
    os.makedirs(os.path.join(d, "chapters"))
    for n, body in chapters:
        with open(os.path.join(d, "chapters", f"Chapter_{n:02d}.md"), "w", encoding="utf-8") as fh:
            fh.write(body)
    with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(f"Live edge: **after Chapter {readme_edge}**\n")
    return d


def _ch(n, ledger=True, extra=""):
    return (f"# Chapter {n}\n\nProse here.\n\n"
            + ("## Ledger\n- canon consumed: none\n" if ledger else "") + extra)


def selftest():
    defects = {
        "banned value":    _mkserial([(1, _ch(1, extra="Dawnflame 1,120"))], 1),
        "sequence gap":    _mkserial([(1, _ch(1)), (3, _ch(3))], 3),
        "stale live edge": _mkserial([(1, _ch(1)), (2, _ch(2))], 1),
        "missing ledger":  _mkserial([(1, _ch(1, ledger=False))], 1),
        "firewall breach": _mkserial([(1, _ch(1, extra="the Holy Spirit Cult"))], 1),
    }
    caught = sum(run_gate(d, quiet=True) == 1 for d in defects.values())
    clean = _mkserial([(1, _ch(1)), (2, _ch(2))], 2)
    clean_ok = run_gate(clean, quiet=True) == 0
    total = len(defects)
    print(f"selftest: {caught}/{total} defect classes caught; clean serial passes: {clean_ok}")
    ok = caught == total and clean_ok
    print("SELFTEST PASS" if ok else "SELFTEST FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(run_gate(root))
