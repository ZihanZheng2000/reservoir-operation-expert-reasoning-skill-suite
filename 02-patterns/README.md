# 02 - Patterns：从 50 张 card 归纳推理与执行 pattern

输入：`../01-corpus/development-50/cards/`（E01–E50，50 张 card）。V01–V05 不参与本层。

最终产物：[`06-taxonomy/pattern-taxonomy-zh.md`](06-taxonomy/pattern-taxonomy-zh.md)（英文版 `pattern-taxonomy-en.md`）。共 9 个推理 pattern（RP01–RP09）、11 个执行 pattern（EP01–EP11）、104 个小 pattern，2026-10-01 经用户确认定稿，是后续 skill 构建的固定输入。

来源：从 `artifacts/run-20260914-0925-50paper-patterns/` 的 `02-pattern-extraction/` 和 `04-development-50-backtest/semantic-map/` 中整理（2026-10-28）。只保留最终版本，原处未改动。

## 流程

```
50 张 card
 │ ① 拆分步骤（脚本）
 ▼
01-steps/          760 个步骤（344 推理 + 416 执行）
 │ ② 归纳大 pattern（AI 起草 + 人工改写 + 新增 RP08）
 ▼
02-large-patterns/ 9 个推理 + 11 个执行大 pattern 的定义
 │ ③ 逐步编码（Claude Code）→ 汇总（脚本）
 ▼
03-step-coding/    1,074 条步骤—pattern 匹配
 ├─④ 排序分析（脚本）→ 04-ordering/：推理与执行合在一条时间线上，分四段：界定问题 → 认识不确定性与预报 → 设计并计算方案（可反复）→ 检验；另有推理、执行各自的顺序图
 │ ⑤ 小 pattern 分组（Claude Code）→ 汇总（脚本）
 ▼
05-small-patterns/ 104 个小 pattern 及逐条分配
 │ ⑥ 整合定稿（用户确认）
 ▼
06-taxonomy/       定稿 taxonomy（中英文）
```

| 步骤 | 目录 | 怎么做的 | 能否用脚本复现 |
|---|---|---|---|
| ① 拆分步骤 | `01-steps/` | `build_steps.py` 从 card 表格中提取 R1…Rn、E1…En 行 | **能**。已核对，760 步中 751 步与原结果逐字段一致；其余 9 步是 2026-10-28 修复的拆分错误（公式中的 `|` 曾被当作表格分隔符），只影响这 9 步的描述、保留细节和证据边界字段，步骤编码不受影响 |
| ② 大 pattern | `02-large-patterns/` | AI 起草 8 个推理和 11 个执行类别；AI 写的定义不够 domain，由人工改写；步骤编码中发现 38 个方法选择步骤无处可归，用户决定新增 RP08。AI 初稿和人工改写稿保留在 `history/` | 不能逐字复现；`prompt-large-patterns.md` 是按这一过程倒推的提示词，可一次生成接近的结果 |
| ③ 步骤编码 | `03-step-coding/` | Claude Code 逐步判定 primary / secondary pattern 并写理由（方法与边界规则见该目录 README）；`build_matches.py` 汇总 | 编码本身不能重新生成；汇总**能**，已核对与原结果完全一致 |
| ④ 排序 | `04-ordering/` | 用 card 第 4 节的推理 / 执行配对把两层放到同一条时间线上，再做成对先后统计 + 精确 Kemeny 排序 + 300 次 bootstrap（`combined_order_analysis.py`）；另附推理、执行各自的分层顺序图 | **能**（合并顺序）。分层顺序图的脚本留在工作 run 中 |
| ⑤ 小 pattern | `05-small-patterns/` | Claude Code 用持续比较法分组，逐条写理由（`assign/*.py`）；`build_assignments.py` 汇总 | 分组本身不能重新生成；汇总**能**，已核对 20 张分配表与原结果一致 |
| ⑥ taxonomy | `06-taxonomy/` | 汇总大 pattern、小 pattern、顺序、边界规则和整合决定，用户确认定稿 | 否：文档。已核对 104 个小 pattern 的步数、论文数与分配表一致 |

## 复现

在各目录下依次运行（Python 3.13；作图需要 matplotlib）：

```
cd 01-steps          && python build_steps.py
cd 03-step-coding    && python build_matches.py
cd 04-ordering       && python combined_order_analysis.py && python draw_combined_order.py && python draw_combined_order.py --en
cd 05-small-patterns && python build_assignments.py
```

人工 / LLM 判断的部分（大 pattern 定义、`step-coding.csv`、`assign/*.py`）作为数据保存，脚本只负责从这些判断生成表格和统计。

## 已知局限

1. **大 pattern 的形成过程不能逐字复现**：AI 起草、人工改写，当时的提示词没有保存。现在保留了 AI 初稿和人工改写稿，并按两者的差异倒推了提示词（`02-large-patterns/prompt-large-patterns.md`）。
2. **单一编码者**：步骤编码和小 pattern 分组都只由 Claude Code 完成，没有做独立的二次编码。
3. **RP08 只有 primary 证据**，它与其他步骤的 secondary 关系没有编码。
4. **pattern 是按频率归纳的**：一个小 pattern 需要多篇论文支持才算成熟，单篇论文的独特做法往往被并入更一般的 pattern。所以 taxonomy 反映的是领域共识，不包含单篇论文的创新点。
5. **V01–V05 已暴露**：taxonomy 定稿前，V01–V05 的覆盖检查结果已经被看过。
6. 证据来自 card，反映的是论文写出来的研究过程；开发集以模型和模拟研究为主，实践类证据（EP11）很少。
