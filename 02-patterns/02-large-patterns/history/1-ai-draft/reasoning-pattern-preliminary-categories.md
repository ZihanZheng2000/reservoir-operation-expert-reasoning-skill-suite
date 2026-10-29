# 水库洪水风险管理的推理步骤：初步归类

研究主题：Reservoir operation adjustment for flood risk management。

依据：[E01–E50 的 344 条 reasoning step 标题](../../../01-steps/reasoning-steps.md)。本表是阅读标题后形成的初步归类，尚未逐条编码、核实支持程度或统计频次；候选类别不代表已验证的跨文章 pattern，也不表示每篇论文都应包含全部类别。表格顺序用于组织讨论，不预设统一的推理顺序。

| 候选主题（含英文名称） | 共同回答的问题 | 原始 step 示例 |
|---|---|---|
| 识别现行水库调度规则的局限（Identify limitations of existing reservoir operating rules） | 现行调度规则为什么难以兼顾洪水防御与水资源利用，哪些条件使调整成为必要？ | E07 R1: Diagnose the guide-curve trade-off；E15 R1: Identify the fixed-rule limitation |
| 判断影响水库防洪决策的关键不确定性（Identify decision-relevant uncertainty in reservoir flood operations） | 哪些预报误差、洪水演变特征或不确定性之间的依赖关系，会改变调度选择及洪水风险？ | E06 R2: Reject restrictive distribution/independence assumptions；E42 R1: Preserve heterogeneous forecast-error structure |
| 判断洪水预报的可靠性与调度信息时序（Assess forecast reliability and information timing for reservoir decisions） | 当前可获得的洪水预报能支持哪些调度决定，哪些决定应留待信息更新后再作出？ | E10 R1: Separate forecast stages by reliability；E34 R6: Restrict current decisions to information available now |
| 界定水库与下游洪水风险及其可接受边界（Define reservoir and downstream flood risk and acceptable limits） | 如何定义调度涉及的不安全事件或后果，并据此确定可接受风险、安全阈值或防洪标准？ | E28 R4: Define the risk event at the correct safety reference；E33 R5: Treat the flood-protection standard as the acceptable risk |
| 判断水库调度调整的物理与运行可行性（Assess physical and operational feasibility of reservoir adjustments） | 预报提前量、可用库容、泄流能力及下游安全约束，是否允许实施预泄、蓄水或水位边界调整？ | E01 R3: Use lead time and release capacity to define an admissible upper level |
| 明确水库防洪与用水目标的权衡及方案选择原则（Frame reservoir operating trade-offs and selection principles） | 如何处理水库安全、下游防洪、蓄水利用等目标之间的冲突，并确定方案比较和选择的原则？ | E20 R6: Select aggregation versus Pareto treatment based on objective comparability |
| 选择洪水过程中的调度适应与纠错逻辑（Choose adaptive reservoir operating and correction logic during floods） | 随洪水演变和预报更新，应何时预泄、回蓄、重新规划或逐步修正调度行动？ | E35 R7: Use feedback to correct forecast errors；E37 R8: Prefer gradual correction when a jump is unsafe |
| 确定调度调整的评价依据与适用边界（Define evidence and applicability boundaries for reservoir operation adjustments） | 如何判断预报是否改善调度表现，调整方案的安全与效益证据能支持哪些结论，又适用于哪些水库和洪水条件？ | E14 R5: Evaluate forecast quality and forecast value separately；E50 R7: Use attributes and diagnostics to qualify transferability |

后续逐条归类时，保留原始 step 与论文编号；对方法名称过于具体、含义不清或更接近执行操作的标题，回查对应提取说明。不同论文可能分别侧重调度规则设计、不确定性传播、预报评价或方案排序，允许形成条件性分支，不将所有主题强制组织为每篇必经的线性路线。
