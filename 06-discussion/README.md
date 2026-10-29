# 06 - Discussion：讨论材料

这里放主线结果之外、适合在讨论部分展开的分析。每个主题一个子目录，各自写明来源、方法和局限。

| 主题 | 内容 | 要点 |
|---|---|---|
| [D1 按 pattern 回读](d1-pattern-guided-rereading/) | 对 10 篇开发集论文，比较"读一遍提取"和"拿着 pattern 清单回读"各找到多少 pattern | 一次提取只找到约 81% 的 pattern，回读多找到 23%；但没有发现新的 pattern 类别。说明 pattern 体系是稳定的，频次是下限；建议采用两遍读的流程 |
| [D2 论文路线覆盖（RC）](d2-reference-coverage/) | 最终测试中，论文自己的研究路线有哪些步骤被答案想到；详见 [`../04-evaluation/03-final-test/rc-analysis-zh.md`](../04-evaluation/03-final-test/rc-analysis-zh.md) | skill 没有提高对论文自己研究路线的覆盖；两组答案都没想到的，多是论文自己的创新；brief 写得越详细，覆盖越多，这个影响比 skill 更大 |
| [D3 不同答题模型](d3-answer-models/) | 第 1 轮开发题（skill v1）上，Opus 5.5、Sonnet 5.5、Haiku 4.5 三个模型用与不用 skill 的绝对得分 | 模型能力决定分数水平（Opus 7.7、Sonnet 7.3、Haiku 5.1），skill 的提升较小（+0.2 至 +0.5）；Haiku 用了 skill 后出现把 skill 当文献引用、编造事实的问题，CA 从 5.2 降到 4.4 |
| [D4 pattern 累积曲线](d4-pattern-accumulation/) | 从 50 篇论文中随机抽 n 篇，看能出现多少个大 pattern 和小 pattern | 一篇论文平均出现 12.3 个大 pattern、17.9 个小 pattern；5 篇能看到约 19/20 个大 pattern、60/104 个小 pattern；20 篇看到 97 个小 pattern，30 篇看到 101 个；小 pattern 已接近饱和（Chao1 估计约 104） |

**不画图的讨论点**见 [`discussion-notes-zh.md`](discussion-notes-zh.md)，用于写作和答问，不放进汇报：D5 LLM 裁判的可靠性、D6 skill 自己引入的系统性错误、D7 人在回路中的作用、D8 题目怎么问的影响、D9 泛化性和外部效度，以及局限和未来工作汇总。
