# 04 - Evaluation：skill 的开发测试与最终测试

**被测对象**：`../03-skills/reservoir-flood-expert/`。

**测试形式**：A 组（不用 skill）和 C 组（用 skill）两两对比。每题由两位裁判盲评，第二位看到的答案顺序相反。只有两位裁判都判同一方胜，才算该方赢。

**模型**：
- 裁判全部是 Claude Opus 5.5。
- 第 1 轮的答题模型是 Opus 5.5、Sonnet 5.5 和 Haiku 4.5，之后只用 Opus 5.5。
- 用户决定：Haiku 的结果不采用，因为这个旧模型基本不具备独立做科研的能力；Sonnet 只作参考。

**来源**：`artifacts/run-20261028-v3-rebuild/work/`。这里保留了答案、判定、盲评密钥、脚本和报告。每次测试冻结的 skill 只保留 sha256，v1 和 v2 的全文留在 run 里。

## 结构

| 目录 | 内容 |
|---|---|
| `01-dev-questions/` | 7 道开发题 U1–U7（中文版经用户审定，另有英文版），以及答题和裁判 prompt |
| `02-dev-rounds/round-01/` | skill v1，3 个答题模型 × 7 题 |
| `02-dev-rounds/round-02/` | skill v2，只测 Opus × 7 题。A 组沿用第 1 轮的答案（内容逐字节相同，换了新的随机文件名） |
| `02-dev-rounds/round-03/` | skill v3，只测 Opus × U5，C 组独立作答 3 次 |
| `03-final-test/` | skill v3，留出论文 V01–V05 × 两种 brief（简单版和详细版）× A/C，只测 Opus |

## 结果汇总（Opus）

| 测试 | skill | C 胜 / A 胜 / 意见不一 | 偏向 C 的判定 | 平均分 A → C |
|---|---|---|---|---|
| 第 1 轮 | v1 | 4 / 0 / 3 | 11/14 | 7.73 → 8.19 |
| 第 2 轮 | v2 | 6 / 0 / 1（U5 意见不一） | 12/14 | 7.46 → 8.53 |
| 第 3 轮（只测 U5） | v3 | 3 / 0 / 0 | 6/6 | 7.77 → 8.03 |
| **最终测试** | **v3** | **8 / 0 / 2** | **18/20** | **7.56 → 8.04** |

最终测试的要点（详见 `03-final-test/final-report-zh.md`）：
- PR（可操作性）提高 1.6 分，提升最大。
- RC（论文路线覆盖）没有提升：6.7 对 6.6；在简单版 brief 上，C 还略低（6.2 对 6.6）。
- CA 略低（8.2 对 8.0），C 的答案长 32%。
- 两种 brief 版本上的胜负相同。

## 各轮的关键文件

- **第 1 轮**：
  - `protocol.md`：运行记录
  - `results.md`：胜负和得分
  - `round-01-report-zh.md`：报告
  - `analysis-zh.md`、`analysis-judge-notes-zh.md`：详细分析
  - `analysis-tables.md`：分析表
- **第 2 轮**：`round-02-report-zh.md`、`results.md`、`analysis-tables.md`
- **第 3 轮**：`round-03-report-zh.md`、`results.md`
- **最终测试**：
  - `protocol.md`：运行前写定的测试方案
  - `briefs/`：15 个文件，包括 5 篇 × 简单版和详细版 brief、5 份 reference（只给裁判看），以及 brief 的写作说明
  - `results.md`：胜负和得分
  - `final-report-zh.md`：报告
  - `rc-analysis-zh.md`：RC 分析

## 关于脚本

`setup_*.py`、`tally.py`、`analyze.py` 是在 run 文件夹中运行时的原样记录。各轮的 setup 脚本会从 `05-round-01/setup_round.py` 导入 prompt，所以放在 v3 里不能直接运行。

- **要复现统计**：在 run 文件夹中运行对应目录下的 `tally.py`。
- **要重新出题**：使用 `01-dev-questions/answer-and-judge-prompts.md` 中的 prompt 原文。

## 已知局限

- 每个版本基本只作答一次（只有第 3 轮重复了 3 次），样本量小。
- 第 1 位裁判有位置偏好（第 1 轮中，21 次里有 17 次选了排在第二个位置的答案）。
- 裁判是相对打分：完全相同的 A 答案，在不同轮次中得分会变。
- C 组的答案更长。第 1 轮中长度与分差的相关系数 r = 0.24（21 个组合）；第 2 轮 r = 0.79，但只有 7 个点。
- 最终测试的 reference 是旧测试由子代理读论文写成的，裁判没有读原文。主会话核对过 reference 与新 brief 的研究问题是一致的。
