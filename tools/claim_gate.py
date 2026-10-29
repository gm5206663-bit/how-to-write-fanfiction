#!/usr/bin/env python3
"""claim_gate.py — fail a chapter that invents canon instead of checking it.

The failure this exists to stop, seen in a real serial: six canon errors across
two chapters, written from memory while the author was told the source had been
checked. A fetched page does not protect a chapter written a day later from a
remembered detail.

Three checks, all mechanical:

  C1  SPELL REGISTRY   every shouted spell `TYPE: NAME!` must exist in the
                       registry, and must be spoken by the character who owns it.
  C2  CLAIM TRACE      every claim in the chapter's footer must cite a fact id in
                       the registry, and the line it quotes must be in the chapter.
  C3  NUMBER TRACE     a number attached to a canon character should be inside a
                       claimed sentence (reported; not fatal).

Registry shape -- two plain JSON files, no dependencies:

  canon/facts.json   {"facts":  [{"id":"C001","topic":"…","statement":"…","source":"…"}]}
  canon/spells.json  {"spells": [{"name":"…","attribute":"…","owner":"…","source":"…"}]}

Chapter shape -- a claim row per canon beat:

  - **CLAIM (C001):** "the exact line in the chapter that this fact paid for"

Usage:
  python3 tools/claim_gate.py chapters/*.md
  python3 tools/claim_gate.py --facts canon/facts.json --spells canon/spells.json chapters/
  python3 tools/claim_gate.py --selftest

Exit 1 on any C1/C2 failure.
"""
import json
import re
import sys
from pathlib import Path

SHOUT = re.compile(r'"([A-Z][A-Z ]{2,}):\s([A-Z][A-Z \'!—,-]{2,})')
CLAIM = re.compile(r"^\s*[-*]\s+\*\*CLAIM\s+\((\w+)\):\*\*\s*(.+?)\s*$", re.M)

NUMBER_WORDS = ("one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
                "thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|"
                "twenty|thirty|forty|fifty|hundred")

DEFAULT_FACTS = "canon/facts.json"
DEFAULT_SPELLS = "canon/spells.json"


def load_json(path):
    p = Path(path)
    if not p.exists():
        return None
    return json.loads(p.read_text())


def audit_chapter(path, facts, spells, people):
    """Return (errors, notes) for one chapter."""
    text = Path(path).read_text(errors="ignore")
    name = Path(path).name
    errors, notes = [], []

    # ---- C1 : every shouted spell is real, and belongs to its speaker --------
    for m in SHOUT.finditer(text):
        attribute, spoken = m.group(1).strip(), m.group(2).strip().rstrip("!.").strip()
        key = spoken.split("—")[0].strip()
        entry = claims_spell(spells, key)
        if entry is None:
            errors.append(f"{name}: C1 unregistered spell {attribute}: {key!r} "
                          f"— not in the spell registry")
            continue
        owner = entry.get("owner", "")
        if owner and people and owner in people:
            said_by = speaker_near(text, m.start(), people)
            if said_by and said_by != owner:
                errors.append(f"{name}: C1 {key!r} belongs to {owner} "
                              f"but appears to be spoken by {said_by}")

    # ---- C2 : every claim traces to a fact, and quotes the chapter ----------
    body = text.split("## Footer")[0] if "## Footer" in text else text
    for cid, quoted in CLAIM.findall(text):
        if facts is not None and cid not in facts:
            errors.append(f"{name}: C2 claim cites unknown fact {cid}")
            continue
        q = re.search(r'"([^"]{4,})"', quoted)
        probe = q.group(1) if q else quoted.strip()
        if probe and probe not in body:
            errors.append(f"{name}: C2 claim {cid} quotes a line that is not in the "
                          f"chapter: {probe[:60]!r}")
        else:
            notes.append(f"{name}: {cid} traced")

    # ---- C3 : numbers hung on canon characters get a note -------------------
    for person in people or []:
        for m in re.finditer(rf"\b{re.escape(person)}\b[^\n]{{0,60}}?\b({NUMBER_WORDS})\b", body):
            sentence = body[max(0, m.start() - 90):m.end() + 90]
            if "CLAIM" not in sentence and not re.search(r"\(C\d{3}\)", sentence):
                notes.append(f"{name}: C3 number near {person} is unclaimed: "
                             f"…{sentence.strip()[:80]}…")
    return errors, notes


def claims_spell(spells, key):
    if not spells:
        return None
    for entry in spells:
        if entry.get("name", "").strip().lower() == key.lower():
            return entry
    return None


def speaker_near(text, pos, people):
    """Who most plausibly says the line at pos — the nearest name in the 400 chars before it."""
    window = text[max(0, pos - 400):pos]
    best, best_at = None, -1
    for person in people:
        at = window.rfind(person)
        if at > best_at:
            best, best_at = person, at
    return best


def selftest():
    """A check that cannot fail is not a check."""
    import tempfile
    facts = {"C001": {"id": "C001", "topic": "t"}}
    spells = [{"name": "Magic Binding Iron Chain Formation", "owner": "Revchi"},
              {"name": "Demon-Slayer Sword", "owner": "Asta"}]
    people = ["Asta", "Revchi", "Yuno"]

    def run(text, f=facts, s=spells):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
            fh.write(text)
            tmp = Path(fh.name)
        errs, _ = audit_chapter(tmp, f, s, people)
        tmp.unlink()
        return errs

    cases = [
        ("C1 invented spell is caught",
         'He says, "WIND MAGIC: GALE BLADE!" and the road goes white.', "C1"),
        ("C1 canon spell on the wrong speaker is caught",
         'Asta lifted his hand. "CHAIN MAGIC: MAGIC BINDING IRON CHAIN FORMATION!"', "C1"),
        ("C2 claim citing a missing fact is caught",
         'Body text.\n\n## Footer\n\n- **CLAIM (C999):** "Body text."', "C2"),
        ("C2 claim quoting a line not in the chapter is caught",
         'Body text.\n\n## Footer\n\n- **CLAIM (C001):** "a line that is not here"', "C2"),
    ]
    bad = 0
    for label, text, expect in cases:
        hit = any(expect in e for e in run(text))
        print(f"  {'PASS' if hit else 'FAIL'}  {label}")
        bad += 0 if hit else 1

    clean = 'Revchi lifted the chain. "CHAIN MAGIC: MAGIC BINDING IRON CHAIN FORMATION!"\n\n' \
            '## Footer\n\n- **CLAIM (C001):** "Revchi lifted the chain."\n'
    errs = run(clean)
    print(f"  {'PASS' if not errs else 'FAIL'}  a traced chapter with a real spell passes")
    bad += 0 if not errs else 1

    print(f"\nclaim_gate selftest — {len(cases) + 1} case(s)")
    print("SELFTEST PASS" if not bad else "SELFTEST FAIL")
    return 0 if not bad else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()

    facts_path, spells_path = DEFAULT_FACTS, DEFAULT_SPELLS
    targets = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--facts":
            i += 1; facts_path = argv[i]
        elif a == "--spells":
            i += 1; spells_path = argv[i]
        else:
            targets.append(a)
        i += 1

    facts_raw = load_json(facts_path)
    spells_raw = load_json(spells_path)
    facts = {f["id"]: f for f in (facts_raw or {}).get("facts", [])} or None
    spells = (spells_raw or {}).get("spells") or None
    people = sorted({s.get("owner") for s in (spells or []) if s.get("owner")})

    files = []
    for t in targets:
        p = Path(t)
        files.extend(sorted(p.glob("*.md")) if p.is_dir() else [p])
    if not files:
        print("claim_gate: no chapters given")
        return 0

    errors, notes = [], []
    for f in files:
        e, n = audit_chapter(f, facts, spells, people)
        errors += e
        notes += n

    for n in notes:
        print(f"  note  {n}")
    for e in errors:
        print(f"  FAIL  {e}")
    print(f"\nclaim_gate: {len(files)} file(s) · {len(errors)} contradiction(s)")
    print("PASS" if not errors else "FAIL")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
