#!/usr/bin/env python3
"""tools/check_manifest.py — every file in the guide hash-matches MANIFEST.sha256.

The same contract the serials run: a repository that cannot prove its own
files are the files it checked cannot prove anything downstream. Pairs with
tools/refresh-manifest.sh (run it after any deliberate change).

Run:   python3 tools/check_manifest.py
Exit:  0 all green · 1 anything red (with the exact failures listed)
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "MANIFEST.sha256")


def tracked():
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d != ".git"]
        for fn in fns:
            rel = os.path.relpath(os.path.join(dp, fn), ROOT)
            if rel == "MANIFEST.sha256":
                continue
            out.append(rel)
    return sorted(out)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    fails = []
    if not os.path.exists(MANIFEST):
        print("MANIFEST: not found — run tools/refresh-manifest.sh")
        return 1
    listed = {}
    for line in open(MANIFEST, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        digest, _, path = line.partition("  ")
        if path.startswith("./"):
            path = path[2:]
        listed[path] = digest
    actual = tracked()
    for rel in actual:
        if rel not in listed:
            fails.append(f"not in manifest: {rel}  (run tools/refresh-manifest.sh)")
        elif sha256(os.path.join(ROOT, rel)) != listed[rel]:
            fails.append(f"hash mismatch: {rel}  (file changed — refresh the manifest)")
    for rel in listed:
        if rel not in actual:
            fails.append(f"in manifest but missing on disk: {rel}")
    print(f"MANIFEST: {len(actual)} files checked, {len(fails)} problem(s)")
    for f in fails:
        print("  -", f)
    if fails:
        print("FAIL — fix the list above, refresh the manifest, commit both together.")
        return 1
    print("ALL GREEN — every file matches the manifest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
