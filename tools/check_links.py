#!/usr/bin/env python3
"""tools/check_links.py — every relative link in the guide resolves.

The guide's own rule applied to the guide's own files ("a law only counts
with a check"): for every markdown file, extract [text](target) links, skip
external URLs, pure anchors, and placeholder targets, and verify each
remaining target exists on disk.

Run:   python3 tools/check_links.py
Exit:  0 all links resolve · 1 anything broken (with the exact list)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def md_files():
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d != ".git"]
        for fn in fns:
            if fn.endswith(".md"):
                out.append(os.path.join(dp, fn))
    return sorted(out)


def main():
    checked = 0
    skipped = 0
    broken = []
    for path in md_files():
        text = re.sub(r"```.*?```", "", open(path, encoding="utf-8").read(), flags=re.S)
        for m in re.finditer(r"\]\(([^)]+)\)", text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                skipped += 1
                continue
            target = target.split("#")[0]
            if not target or "{{" in target or "<" in target:
                skipped += 1
                continue
            checked += 1
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.exists(resolved):
                broken.append(f"{os.path.relpath(path, ROOT)} -> {target}")
    print(f"LINKS: {checked} relative links checked, {len(broken)} broken"
          f" ({skipped} external/anchor/placeholder skipped)")
    for b in broken:
        print("  -", b)
    if broken:
        print("FAIL — fix the links above, then re-run.")
        return 1
    print("ALL GREEN — every relative link in the guide resolves.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
