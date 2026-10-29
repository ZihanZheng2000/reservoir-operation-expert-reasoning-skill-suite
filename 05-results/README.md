# 05 - Results：汇报用图

2026-10-29 生成。图中文字为英文，配色为浅色主题。每张图都有 PNG（220 dpi，适合放进 PPT）和 SVG（矢量，可编辑）两种格式。数据全部来自 `../04-evaluation/` 中的盲评密钥和裁判判定，fig0 来自 `../02-patterns/04-ordering/`。

| 图 | 内容 | 支撑的结论 |
|---|---|---|
| `fig0-expert-research-order` | 推理与执行合在同一条时间线上的专家研究顺序（四段），是 `02-patterns/04-ordering/combined-order-en` 的幻灯片版。数字没有改动，但有以下调整：布局更紧凑，字号加大；不放图标题；左侧两条泳道标注为 Reason / Execute（竖排）；EP04 放在 EP03 下方；阶段之间各用一个水平箭头，放在阶段框的垂直中央，并标出百分比，其中第 1 段→第 2 段为 92%，其中第 2 段→第 3 段为 69%（低于 80%，用灰色表示），第 3 段→第 4 段为 97%；图例分两行，字号加大。由 `draw_order_slide.py` 生成 | 专家做研究有稳定的顺序，skill 按这个顺序搭建 |
| `fig1-final-test-by-case` | 最终测试 10 个 case（5 篇留出论文 × 简单版和详细版 brief）中 A 组和 C 组的平均分；右侧分列裁判 1、裁判 2 各自的判定（哪一方胜、明显胜或小胜），以及合并后的结果 | skill 在留出论文上 8 胜 0 负，2 个 case 两位裁判意见不一 |
| `fig2-final-test-by-criterion` | 最终测试 6 项评分的 A/C 对比，按简单版和详细版分两栏 | 可操作性（PR）提升最大，+1.6/+1.7；论文路线覆盖（RC）没有提升 |
| `fig3-dev-rounds-heatmap` | 开发题 U1–U7 × 3 轮的分差（C − A）和胜负 | 依据裁判意见和人工意见修订后，第 2 轮各题分差普遍扩大，U5 在第 3 轮修好 |
| `fig4-judgment-outcomes` | 各轮测试中每份判定的结果分布（明显胜 / 小胜 / 平局 / 输） | 每轮测试中，偏向 skill 的判定都占 79–100%；判"明显胜出"的票数在第 2 轮最多 |

原 fig5（不同答题模型）和 fig6（论文路线覆盖矩阵）已分别移到 [`../06-discussion/d3-answer-models/`](../06-discussion/d3-answer-models/) 和 [`../06-discussion/d2-reference-coverage/`](../06-discussion/d2-reference-coverage/)，所以这里没有 fig5 和 fig6。

## 复现

`make_figures.py` 是生成这些图的脚本，2026-10-29 在 run 文件夹 `artifacts/run-20261028-v3-rebuild/work/11-figures/` 中运行。它从 run 中各轮的文件夹读取数据，那些文件夹里的内容与 `../04-evaluation/` 相同。要在 v3 中运行，需要把脚本开头的路径改为 `../04-evaluation/` 下对应的目录。

`make_figures.py` 也生成 fig5 和 fig6。fig6 的覆盖编码是从 `../04-evaluation/03-final-test/rc-analysis-zh.md` 第 1 节手工转录到脚本里的，编码依据是裁判判定中的原话。

## 使用时注意

- 所有分数都是 LLM 裁判（Claude Opus 5.5）给的分，不是人工评分。
- 每轮测试基本只作答一次，样本量小；只有第 3 轮重复了 3 次。
- 有 skill 的答案平均长 32%。裁判 prompt 要求不因长度给分，但无法完全排除长度的影响。
