# gpt-debt-sweeper evaluation oracle

This branch contains the **independent evaluator**, deliberately kept out of
each case branch. The case branches are unmodified starting points for coding
agents, not clean solutions. The oracle is public and designed for reproducible
smoke comparisons, not for adversarial scoring.

## Cases

| ID | Branch | Main behavior to measure |
| --- | --- | --- |
| 01 | `eval/01-retired-ui` | Remove retired console, legacy test/smoke, packaging and config leftovers; keep the current UI |
| 02 | `eval/02-verification-theater` | Remove same-process self-verification, its dedicated tests and fixtures; preserve invoice output |
| 03 | `eval/03-speculative-layers` | Collapse no-value registry/interface/forwarder and their internal tests; preserve welcome output |
| 04 | `eval/04-dynamic-plugin-boundary` | Keep a dynamically loaded status plugin, remove the orphaned legacy plugin and only its dedicated support |

## Trial procedure (run once without Skill and once with Skill)

1. Create two fresh, separate checkouts from **the same case branch commit**.
2. In each checkout give the agent the exact same task from `eval-case/README.md`, scoped to `eval-case/`.
3. The control run **does not invoke** the Skill. The treatment run invokes `$gpt-debt-sweeper` and uses the current skill's `SKILL.md` + `references/`.
4. Do not let the agent inspect this oracle branch before it finishes its edits. Keep the same model, reasoning budget, time/tool limits, and base commit across runs.
5. In a separate checkout of this `eval/oracle` branch, evaluate the agent's results:

```bash
python judge.py 01 /path/to/edited-case-01-checkout
python judge.py 02 /path/to/edited-case-02-checkout
python judge.py 03 /path/to/edited-case-03-checkout
python judge.py 04 /path/to/edited-case-04-checkout
```

The evaluator runs **fresh independent runtime assertions**, original remaining
tests, structural removal checks, and residual-reference checks. A test pass
alone is not enough. An untouched case should pass its existing project tests
but fail some cleanup checks (by design).

Report both the score and the actual diff. Structural checks intentionally
prefer complete removal of the seeded scaffolding; they are a reproducible
proxy for these four scenarios, not a universal definition of technical debt.

## Interpreting outcomes

- Functional probe fails: behavior regression (hard failure).
- Valid dynamic plugin deleted: behavior regression (hard failure).
- Remaining obsolete artifacts: incomplete cleanup.
- Replacing removed scaffolding with a new equivalent layer can game the
  structural score; inspect the final diff for such new debt.
- Baseline and treatment comparisons with one run each are directional only.
  Repetition is needed before claiming a model-level improvement.

The evaluator has only Python standard-library dependencies.
