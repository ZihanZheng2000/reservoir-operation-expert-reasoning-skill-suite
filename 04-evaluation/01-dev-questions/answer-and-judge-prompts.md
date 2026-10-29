# 答题提示与裁判提示（草案，2026-10-28 用户确认）

开发题（U1–U7）与最终检验使用同一套。尚未运行任何测试。

## 已确定的决定

| 项目 | 决定 |
|---|---|
| 开发题与最终检验 | 同一套答题要求 |
| 固定分节 | 不要。答题时回答题目要求的每一部分，组织方式自定 |
| 字数 | 不设上限；记录每份答案的字数，用于检查胜负是否来自篇幅 |
| 是否要求结果 | 不要求运行模型或给出最终计算结果；要求详细计划；题目要求判断或建议时，给出暂定判断及理由、关键假设、什么会证实或改变它 |
| 裁判 | 两名盲评裁判，第二名看到的答案顺序相反；两人一致才算胜；评分标准沿用原来的 5 项（开发题）/ 6 项（最终检验加 RC）及 3 / 6 / 9 锚点 |
| 每题评价要点 | 暂不写 |
| 防止揭盲 | 每轮结束后检查 skill 组答案中是否出现 skill 的阶段名、单元名或 pattern 编号 |

## 答题提示（两组相同；skill 组先读 skill）

> You are an expert in reservoir operation under flood risk. Answer the question below.
> - You do not need to run models or produce final results. Give a detailed plan of what you would do and why. Where the question asks for a judgment or recommendation, give your provisional one, with the reasons, the key assumptions, and what would confirm or change it.
> - Do not invent facts beyond the question; state your assumptions.
> - Answer every part the question asks. Organize the answer as you see fit. There is no length limit, but do not pad.

skill 组在此之前另加一句：

> First read the skill at `[SKILL]/SKILL.md`, follow it, and read the reference files it points to when you work on a unit.

## 裁判提示中新增的说明

> Score the quality of reasoning and planning; do not expect computed results. Do not reward length, formatting, or confident tone.

## 评分标准（沿用原来的，1–10 分，锚点 3 / 6 / 9）

| 标准 | 3 | 6 | 9 |
|---|---|---|---|
| KQ 关键问题 | 漏掉决定答案的问题 | 找到大部分，部分没讲透 | 找到并正确解决所有关键问题 |
| TC 技术正确性 | 有影响结论的公式、数字或概念错误 | 有小错，不影响结论 | 没有错误，算术核对过 |
| ME 方法 | 含糊、无法执行 | 能执行但有缺口 | 完整、有序、可执行，带验证 |
| PR 实用性 | 忽略运行、法规、审批 | 泛泛提到 | 有具体的运行、法规和兜底安排 |
| CA 校准 | 过度下结论或编造事实 | 有些无依据的说法 | 结论限定在证据范围内，假设写明 |
| RC 参考覆盖（仅最终检验） | 覆盖论文参考路线中很少的关键问题和步骤 | 约一半，或用较弱的替代 | 几乎全部，或有理由的等价做法 |

裁判输出：每项打分与理由；每份答案好在哪、缺什么、错在哪；胜者及强弱（明显 / 略微 / 平局）。

## 裁判提示（用户确认沿用原提示）

- 开发题：沿用 `artifacts/run-20260914-0925-50paper-patterns/03-skill-construction/04-tests/unified-skill-iteration/judge-prompt.md`（5 项标准；保留 "Notes for revision"，其中"两份答案都没有、但专家答案必须包含的要点"作为修改 skill 的依据之一）。
- 最终检验：沿用同目录下 `final-papers/judge-prompt.md`（6 项标准，含 RC；裁判可看论文参考路线）。
- 两份都只做两处改动：
  1. 在 "Do not reward length, formatting or confident tone." 之前加入：`Score the quality of reasoning and planning; do not expect computed results.`
  2. 文件路径改为本次 run 中的题目、答案和裁判结果位置。

## 最终检验（用户确认）

- 沿用 V01–V05，以及当时由独立 agent 写好的 brief 和参考路线（`final-papers/briefs/`）。
- 答题时用上面的答题提示，把 brief 作为题目，不再用原来的四节格式和 700 词限制。
- 依据：此前的留出测试（2026-10-09）和去卡片重测（2026-10-28）只做测试，没有据此修改 skill。
- 局限：taxonomy 定稿前，V01–V05 的 pattern 覆盖检查结果已被看过（taxonomy 自己记录了这一点），属于 pattern 层面的轻度暴露；V01–V05 已在两次测试中使用。

## 迭代（用户确认）

- 每轮根据裁判意见（"Notes for revision"）和用户的意见修改 skill；每条修改记录来源（哪一轮、哪道题、哪位裁判或用户）。
- 修改只进入 SKILL.md 的检查问题、单元说明或参考资料；不加入没有来源的内容。
- 轮数根据实验结果决定。

## 已知局限

- 裁判与答题者是同一系列的模型。
- 开发题由 skill 构建者起草、用户修改定稿，不是独立出题。
