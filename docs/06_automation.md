# 06 · Automation — CI, self-syncing profiles, and safer tokens

The gates in this method are manual by default: *no green, no push*, run by hand. This page is the upgrade path to machines enforcing it — and exactly what each step needs from you, since GitHub gates some of it behind extra token permissions.

---

## 1. Live CI: every push runs the gate

The recipe ships in this repo at [`examples/github-actions-gate.yml`](../examples/github-actions-gate.yml). Copy it to `.github/workflows/gate.yml` in your serial's repo and every push and PR must pass the gate selftest.

**Why it isn't live on this repo:** pushing a `.github/workflows/` file with a **classic personal access token requires the extra `workflow` scope** (this repo's tooling token is `repo`-scoped only — the push was rejected by GitHub, which is the system working as designed).

To turn it on for your own workspace:
1. GitHub → Settings → Developer settings → Tokens (classic) → edit your token → check **`workflow`** (or mint a new one with `repo` + `workflow`).
2. Copy `examples/github-actions-gate.yml` to `.github/workflows/gate.yml` in the repo.
3. Push. From then on, Actions runs the gate on every push and every PR shows a green/red check.

**Fine-grained tokens** (recommended over classic): grant the token **Contents: read/write + Workflows: read/write** on exactly the repos it needs, set an expiration, and nothing else. A key that can only open two doors is a key worth losing.

## 2. A self-syncing profile README

Profiles drift — this workspace caught its own profile claiming Chapter 2 while Chapter 4 was live (three times in one week). The fix pattern:

1. Put markers in the profile README around the volatile block:

   ```
   <!-- live-edge:start -->
   | Serial | Era | Live edge |
   ...auto-updated rows...
   <!-- live-edge:end -->
   ```

2. A scheduled GitHub Action (needs the same `workflow` scope) that:
   - fetches each serial repo's panel or latest chapter list via the API,
   - regenerates the rows between the markers,
   - commits only if the content changed.
3. Result: the "Currently writing" table is always true, updated by the same events that make it true.

The Two-Copies Law still applies: the action reads the repos (the source of truth) and rewrites the profile (the derived copy) — one truth, one writer, no hand-edits.

## 3. Drift scans on a schedule

The same pattern catches stale panels and dead links workspace-wide:

- a nightly Action that runs every serial's gate and an independent drift scan (see [`03_gates_and_audits.md`](03_gates_and_audits.md)),
- a badge that goes red when any serial's README live-edge disagrees with its disk,
- a weekly link-checker on the profile and docs (dead badge services happen — this guide's own profile shipped two of them before a live check caught it).

## 4. Token hygiene (the standing rules)

1. **Scope to the job.** `repo` only opens all repos; fine-grained opens two. Prefer two.
2. **Expire everything.** A token with no expiration is a key taped under the doormat.
3. **Rotate after travel.** Any token pasted into a chat, script argument, or CI log gets revoked and re-minted. (`push_to_github.sh` already treats this as law: token as argument, never on disk.)
4. **Never weaken the gate to pass it** — and never widen a scope to dodge a design. If GitHub refuses your push, that refusal is information.

---

*Everything on this page is optional machinery. The method itself — laws, gates, panels, ledgers — runs on any machine, including none.*
