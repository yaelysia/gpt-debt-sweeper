# gpt-debt-sweeper

清理 GPT / Codex 在持续 AI Coding 中积累的**结构性技术债**：旧实现残留、无依据兼容、测试膨胀、验证表演、投机抽象、重复状态与防御性代码堆积。

**这不是代码审计、风格格式化或“去 AI 味”工具。** v0.2 默认采用两阶段：先只读地从现行生产路径、重复职责、历史演进及测试/工具链中挖掘**工程概念级技术债簇**，再核实它们是否值得继续维护并直接执行清理。

## v0.2 包含什么

- [SKILL.md](SKILL.md)：双阶段执行、三种调用模式、范围约束和独立完成条件。
- [references/patterns.md](references/patterns.md)：四条结构性挖掘路径及六组 GPT 习惯性技术债信号。
- [references/deletion-rules.md](references/deletion-rules.md)：继续维护的价值判断、消费者追踪、可达冗余、循环验证与最小验证。

纯 Markdown Skill；**没有依赖、扫描脚本、评分器或自动生成的审计工件**。可使用 Agent 已有的 Git、搜索、编译及测试能力。

## 安装与调用

推荐通过 [Skills CLI](https://github.com/vercel-labs/skills) 安装，工具会识别仓库根目录的 `SKILL.md` 并保留 `references/` 规则文件：

```bash
# 交互式安装（选择目标 Agent）
npx skills add yaelysia/gpt-debt-sweeper

# 全局安装到 Codex，适用于所有项目
npx skills add yaelysia/gpt-debt-sweeper -g -a codex -y

# 仅列出仓库中可安装的 Skill，不安装
npx skills add yaelysia/gpt-debt-sweeper --list
```

也可以手动克隆到 Agent 支持的技能目录（如 Codex 的 `~/.agents/skills/gpt-debt-sweeper`）；只复制 `SKILL.md` 会缺失引用的规则文件。

支持三种模式：

```text
# 默认：先只读挖掘，再直接清理
$gpt-debt-sweeper 对当前仓库执行完整技术债清理。

# 仅挖掘：输出候选簇，不修改文件
$gpt-debt-sweeper 仅挖掘当前仓库的技术债，不修改代码。

# 仅清理：使用本次对话已确认的候选集合
$gpt-debt-sweeper 根据前面挖掘出的技术债候选执行清理和验证。
```

在目标项目中也可明确限定重点：

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

## 评测案例（实验分支）

为比较启用与不启用 Skill 的清理效果，仓库另设四个互不影响的初始测试分支：

- [01 旧 UI 与打包残留](https://github.com/yaelysia/gpt-debt-sweeper/tree/eval/01-retired-ui)
- [02 自我证明的验证膨胀](https://github.com/yaelysia/gpt-debt-sweeper/tree/eval/02-verification-theater)
- [03 单实现抽象层膨胀](https://github.com/yaelysia/gpt-debt-sweeper/tree/eval/03-speculative-layers)
- [04 动态插件与误删边界](https://github.com/yaelysia/gpt-debt-sweeper/tree/eval/04-dynamic-plugin-boundary)

[独立评分器和操作说明](https://github.com/yaelysia/gpt-debt-sweeper/tree/eval/oracle) 位于 `eval/oracle` 分支。每个案例的原始功能测试应通过，但尚未完成清理；评分器将分别检查真实行为、残留和误删。测试案例分支保持原样，通过全新工作树进行对照，不要直接在案例基线分支上提交清理结果。

## 状态

v0.2：加入**挖掘与删改严格分段**、四条结构性发现路径、概念簇清理单位，以及对仍可达但无独立维护价值的结构的判定。现有四个小型评测案例可用于检验误删和完整收尾；**v0.2 尚未经过独立真实项目 A/B 对照验证**。

MIT License，见 [LICENSE](LICENSE)。
