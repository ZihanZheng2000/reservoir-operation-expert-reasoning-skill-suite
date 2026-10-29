# Reservoir Flood-Operation Expert Skill

**从 50 篇论文中提炼专家的研究思路，写成 AI agent 可以使用的 skill，并在留出论文上做盲评检验。**

研究对象是洪水风险下的水库调度：汛限水位、预泄与回蓄、预报不确定性、风险评估、实时调度、梯级协调等。

## 主要结论

1. **专家做研究有稳定的顺序**：
   - 从 50 篇论文的 760 个步骤中，归纳出 9 个推理 pattern、11 个执行 pattern 和 104 个小 pattern。
   - 把推理和执行放到同一条时间线上，得到四段顺序：界定问题 → 认识不确定性与预报 → 设计并计算方案（先判断后计算，计算可以反复）→ 检验。
   - 图见 `05-results/figures/fig0`。
2. **skill 在留出论文上稳定胜出**：
   - 用 5 篇没有参与构建的论文，每篇分别写成简单版和详细版题目，由 Claude Opus 5.5 作答，两位裁判盲评。
   - 用 skill 的一组 8 个 case 胜出、0 个落败、2 个两位裁判意见不一；20 份判定中有 18 份偏向 skill。
   - 平均分从 7.56 提高到 8.04，提升最大的是可操作性（+1.6）。
   - 图见 `05-results/figures/fig1`、`fig2`。
3. **"裁判意见 + 人工判断"的迭代有效**：
   - 经过 3 轮开发测试，v1 → v3 后，各题的分差普遍扩大，原来没赢的梯级题 U5 变成 3/3 胜出。
   - 几个关键修改来自人的判断，而不是裁判。
   - 图见 `05-results/figures/fig3`、`fig4`；修改记录见 `03-skills/revisions/`。
4. **局限**：
   - skill 没有提高对论文自己研究路线的覆盖（RC 6.7 对 6.6）。它教会的是专家的流程和把关，不是论文作者式的方法创新。
   - 题目写得越详细，这方面的影响比 skill 更大。
   - 见 `06-discussion/`。

## 目录

| 层 | 目录 | 内容 |
|---|---|---|
| 1 | [`01-corpus/`](01-corpus/) | 55 篇论文（50 篇开发集、5 篇留出集）的筛选标准、清单（含 DOI）、card（结构化提取）和 card 提示词 |
| 2 | [`02-patterns/`](02-patterns/) | 760 个步骤、20 个大 pattern（AI 起草，人工改写）、1,074 条步骤编码、排序分析、104 个小 pattern、定稿的 taxonomy（中英文） |
| 3 | [`03-skills/`](03-skills/) | **定稿的 skill**（`reservoir-flood-expert/`），以及单元证据包、生成脚本、v1 → v2 → v3 修订记录和 human review 例子 |
| 4 | [`04-evaluation/`](04-evaluation/) | 7 道开发题、3 轮开发测试、最终留出测试（brief、reference、答案、判定、报告） |
| 5 | [`05-results/`](05-results/) | 汇报用图：fig0–fig4 |
| 6 | [`06-discussion/`](06-discussion/) | 讨论材料：D1 按 pattern 回读，D2 论文路线覆盖，D3 不同答题模型，D4 pattern 累积曲线，另有不配图的讨论笔记 |

每一层的 README 都写明：输入从哪里来、用什么方法（脚本或提示词）生成、怎样复现、有哪些已知缺口。

## 使用 skill

把 [`03-skills/reservoir-flood-expert/`](03-skills/reservoir-flood-expert/) 作为技能目录放到 agent 的 skills 路径下，例如 Claude Code 的 `.claude/skills/`。agent 先读 `SKILL.md`，在处理某个单元时，再按需读取 `references/` 中对应的参考资料。

适用于洪水风险下的水库调度研究和决策，包括研究设计、计算、复核别人的分析、判断说法、实时决策、方案选择和方法选择。不适用于泥沙、水质、结构设计等其他水库问题。

## 这个仓库没有包含的内容

- **论文原文**（`01-corpus/*/papers/*.pdf`）**和全文文本**（`01-corpus/*/text/*.txt`）：受版权保护，不上传，只在本地保存。论文可以按 [`01-corpus/selection/corpus-55.md`](01-corpus/selection/corpus-55.md) 中的 DOI 获取。card 和清单中指向原文的链接在仓库里会失效；`01-corpus/SHA256SUMS` 仍然列出这些文件，用来在本地核对。
- **盲评密钥**（`04-evaluation/**/blinding-key.json`）：不上传。答案文件名是随机编码，没有密钥就无法从原始判定还原哪份答案用了 skill；各轮的结果、报告和分析已经是揭盲后的版本。`04-evaluation/SHA256SUMS` 仍然列出这些文件。

## 规则

- 能用脚本生成的就用脚本，并保存脚本；用 LLM 生成的，保存提示词，并记录模型、日期和派发方式。
- 开发集（E01–E50）和留出集（V01–V05）分开存放，留出集不参与 pattern 和 skill 的构建。
- skill 只写 pattern 推导出来的内容；其他内容只有在裁判提出意见或人工给出意见之后才加入，并记录出处。

## 来源

本仓库是 2026-10-28 至 10-29 的重建版（v3）。工作在本地的 run 文件夹中进行（`artifacts/run-20261028-v3-rebuild/`），旧的研究过程保留在本地的 `artifacts/run-20260914-0925-50paper-patterns/`，这两个文件夹都没有上传。
