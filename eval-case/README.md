# Evaluation fixture

This branch is a disposable coding-agent cleanup fixture, not a change to the skill.

Target: `eval-case/` only. Keep the current supported behavior and public entrypoints.
Do not change `SKILL.md` or `references/`.

Baseline command (from `eval-case/`):

```bash
python -m unittest discover -s tests -v
```

Cleanup task (use exactly the same prompt with and without the skill):

> 清理 eval-case 中已经积累的无用技术债，保持现行受支持行为。请直接修改代码并执行现有相关测试，不要扩展到仓库其他部分。

Use separate fresh checkouts for both trials. The baseline tests are expected to pass *before* cleanup as well.
The independent cleanup oracle is intentionally stored on a separate `eval/oracle` branch.
