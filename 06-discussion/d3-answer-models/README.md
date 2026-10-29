# D3：不同答题模型用 skill 的效果

## 问题

同一个 skill，交给能力不同的模型使用，效果是否一样？

## 数据

- **测试**：第 1 轮开发测试（skill v1），7 道开发题 U1–U7。
- **答题模型**：Claude Opus 5.5、Sonnet 5.5、Haiku 4.5，每个模型都分别作答 A 组（不用 skill）和 C 组（用 skill）。
- **评判**：每道题由 2 位 Opus 5.5 裁判盲评，第二位裁判看到的答案顺序相反。
- **原始材料**：`../../04-evaluation/02-dev-rounds/round-01/`，包括答案、判定、`results.md`、`analysis-zh.md` 和 `round-01-report-zh.md`。
- **只有第 1 轮做了多模型对比**：用户决定（2026-10-28）不再采用 Haiku 的结果，之后各轮和最终测试只用 Opus。所以这里只有 v1 的数据，没有 v3 的。

## 结果

`figures/fig5-answer-models-round1`（PNG 和 SVG）：每个模型一栏，分别列出 A 组和 C 组的五项均值和各评分项得分。

| | Opus 5.5 | Sonnet 5.5 | Haiku 4.5 |
|---|---|---|---|
| 五项均值（A → C） | 7.7 → 8.2 | 7.3 → 7.7 | 5.1 → 5.3 |
| Calibration（A → C） | 7.9 → 8.4 | 7.6 → 7.9 | **5.2 → 4.4** |
| 偏向 C 的判定 | 11/14 | 11/14 | 7/14 |
| 题目层面 C 胜 / A 胜 / 意见不一 | 4 / 0 / 3 | 4 / 0 / 3 | 3 / 3 / 1 |

## 对讨论的意义

1. **模型能力决定分数高低，skill 是在这个基础上加一点**：Haiku 和 Opus 相差约 2.6 分，而 skill 带来的提升只有 0.2–0.5 分。skill 不能弥补模型能力的差距。
2. **能力较弱的模型反而会被 skill 带偏**：裁判指出，Haiku 的 C 组答案：
   - 把 skill 当成文献来引用（"50 篇论文发现……"），5 道题出现这个问题；
   - 泄露 skill 的内部编号（Stage 1–4、RP 编号）；
   - 编造题目里没有给出的系统和数值。

   因此它的 CA 不升反降。详见 `../../04-evaluation/02-dev-rounds/round-01/analysis-zh.md` 第 4 节。
3. **对 skill 设计的启发**：v2 加入了"不能把 skill 当文献引用""不要编造事实""完成前自查有没有泄露编号"这几条（`../../03-skills/revisions/changes-v1-to-v2-zh.md` 第 7、8、10 步）。它们正是针对上面这些问题写的。v2 之后没有再用 Haiku 测试，所以这些修改对弱模型是否有效，目前还不知道。

## 局限

- 只有 7 道题，每个模型只答一次。
- 只测了 v1。
- 裁判也是 Opus 5.5，可能偏向 Opus 的写法。

## 复现

图由 `../../05-results/make_figures.py` 中的 `fig_models()` 生成，当时在 run 文件夹 `artifacts/run-20261028-v3-rebuild/work/11-figures/` 中运行，2026-10-29 从 `05-results/figures/` 移到这里。
