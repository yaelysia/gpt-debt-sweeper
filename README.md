# gpt-debt-sweeper

清理 GPT / Codex 在持续 AI Coding 中积累的**结构性技术债**：旧实现残留、无依据兼容、测试膨胀、验证表演、投机抽象、重复状态与防御性代码堆积。

**这不是代码审计、风格格式化或“去 AI 味”工具。** 用户要求清理时，Skill 会在确认现行消费者和契约后直接执行修改，优先整组删除失效概念，再使用项目已有检查做必要验证。

## v0.1 包含什么

- [SKILL.md](SKILL.md)：执行流程、范围约束、清理优先原则和停止条件。
- [references/patterns.md](references/patterns.md)：六组 GPT 习惯性技术债的识别信号、清理动作和误判边界。
- [references/deletion-rules.md](references/deletion-rules.md)：消费者追踪、动态入口、循环验证、删除/保留判断和最小验证。

纯 Markdown Skill；**没有依赖、扫描脚本、评分器或自动生成的审计工件**。可使用 Agent 已有的 Git、搜索、编译及测试能力。

## 安装与调用

将**整个仓库**放到支持 SKILL.md 的 Agent 技能目录中，保留根目录的 SKILL.md 与 references 目录。例如 Codex 的常见用户级目录：

```powershell
git clone https://github.com/yaelysia/gpt-debt-sweeper.git "$HOME/.agents/skills/gpt-debt-sweeper"
```

仓库目前为私有仓库，克隆需要具有 GitHub 访问权限。其他 Agent 可按自身约定安装；只复制 SKILL.md 会缺失参考规则。

在目标项目中可直接指定：

```text
$gpt-debt-sweeper 清理当前仓库里 GPT 留下的历史技术债，重点处理废弃实现、兼容层及其专属测试。直接修改并验证。
```

只想先看候选时，明确写“仅审计，不修改”。未指定目录时按当前仓库处理；如果给出工作区/子目录，仅在该范围内修改。

## 清理边界

- 删除前追踪生产调用、动态加载、配置/打包、对外 API、持久化和迁移约束；“没有 import”不是删除证据。
- 自动清理不等于取消产品能力。仍被支持的公开/用户可见行为、数据兼容、安全与故障边界保留。
- 不为删除制造新的 Adapter、Wrapper、重复测试、备份或审批流程。
- 只运行与实际修改相关、已有且能区分正确性的检查；不要求每次进行全仓回归。
- 如果没有足够证据删掉某处，跳过它，不把怀疑写成事实，也不因此停止其他高置信度清理。

## 设计来源

借鉴以下项目的**方法**，规则为本项目重新组织撰写，而非直接拼装原始文件：

- [reclaim-code-entropy](https://github.com/Yevanchen/reclaim-code-entropy)：追踪真实消费者与整组清理。
- [code-humanizer](https://github.com/LeonardNJU/code-humanizer)：AI 编码冗余模式。
- [deslop-GPT](https://github.com/MrZoyo/deslop-GPT)：测试膨胀、互相证明的验证冗余。
- [dead-code-cleanup](https://github.com/jerseycheese/agent-skills/tree/main/skills/dead-code-cleanup) / [test-reaper](https://github.com/jerseycheese/agent-skills/tree/main/skills/test-reaper)：死代码引用追踪与弱测试识别。

## 状态

v0.1：第一版规则已完成；**尚未在真实目标仓库执行清理验证**。优先检验三个行为：能整组删除已废弃实现；能清除无独立价值的验证与专属测试；能保留实际动态引用和有效外部契约。

MIT License，见 [LICENSE](LICENSE)。
