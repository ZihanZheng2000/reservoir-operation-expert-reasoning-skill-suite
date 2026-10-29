# 水库洪水风险管理的执行步骤：初步归类

研究主题：Reservoir operation adjustment for flood risk management。

依据：[E01–E50 的 416 条 execution step 标题](../../../01-steps/execution-steps.md)。本表是阅读标题后形成的初步归类，尚未逐条编码、核实支持程度或统计频次；候选类别不代表已验证的跨文章 pattern，也不表示每篇论文都应包含全部类别。表格顺序用于组织讨论，不预设统一执行顺序。

| 候选主题（含英文名称） | 共同完成的任务 | 原始 step 示例 |
|---|---|---|
| 准备水库调度数据与现行规则基线（Prepare reservoir operating data and existing-rule baselines） | 汇集水文、库容、泄流及下游控制信息，明确初始状态与调度时域，并建立现行规则的比较基线。 | E01 E1: Assemble the TGR case and current-rule baseline；E18 E2: Establish site baseline and operating constraints |
| 构建并检验洪水与入库流量预报（Develop and verify flood and reservoir inflow forecasts） | 处理气象和水文输入，校准或训练预报模型，并检验调度所需预见期内的预报质量。 | E22 E2: Assemble and bias-correct NWP precipitation ensembles；E43 E2: Calibrate rainfall-runoff prediction；E23 E2: Verify forecast products before optimization use |
| 建模调度相关不确定性并生成情景（Model operational uncertainty and generate scenarios） | 拟合预报误差及其他不确定性，保留时序或变量间依赖关系，生成情景、集合或供后续推算使用的不确定性表示。 | E04 E5: Check serial dependence and fit joint copulas；E49 E2: Fit marginals and construct dependent uncertainty scenarios；E41 E2: Quantify forecast error as a fuzzy variable |
| 构建水库与下游洪水演算模型并传播不确定性（Model reservoir and downstream flood dynamics and propagate uncertainty） | 通过水量平衡、河道演算、系统模型或概率推断，将入流与调度行动转化为水位、流量及其不确定结果。 | E03 E3: Build the rolling two-stage water balance；E23 E4: Choose and embed downstream routing model；E30 E4: Recursively calculate level-error moments |
| 计算调度安全边界并检验可行性（Calculate operating safety bounds and check feasibility） | 将泄流能力、库容、预报提前量和风险要求转成可用运行边界，检查或处理候选调度方案的约束违反。 | E01 E4: Calculate the candidate upper bound from capacity-constrained pre-release；E03 E6: Test the reduced DC-FLWL feasibility conditions；E15 E6: Repair/rank constraint violations |
| 求解候选调度方案与规则参数（Solve for candidate operating plans and rule parameters） | 通过优化、解析推导、枚举或参数校准，形成候选泄流过程、蓄水分配、运行水位边界或调度规则。 | E02 E4: Trace the uncertain Pareto front；E05 E5: Derive and classify preference-dependent hedging rules；E46 E6: Calibrate rules sequentially with BOBYQA |
| 计算水库与下游洪水风险及运行效益（Calculate reservoir and downstream flood risk and operating benefits） | 从模拟或推断结果计算超限概率、损失或其他风险指标，以及蓄水利用、发电等效益；保留各指标的具体定义。 | E02 E5: Calculate alternative-specific exceedance risks；E25 E3: Evaluate failure and expected damage；E29 E6: Evaluate water-use and energy benefits |
| 组织评价指标并排序选择调度方案（Organize evaluation criteria and select operating alternatives） | 构建方案评价矩阵，处理指标冗余、权重与偏好，对可行方案进行比较、排序和选择。 | E02 E6: Assemble the stochastic MCDM decision matrix；E48 E4: Diagnose correlation and transform criteria；E38 E8: Rank schemes with weighted TOPSIS |
| 将调度结果转为分阶段行动并滚动更新（Translate operating results into staged actions and rolling updates） | 将求解结果转换为泄流或水位目标，按条件运行预泄、防洪、回蓄等分支，并在状态和预报更新后重新决策。 | E24 E5: Convert EFSM to release and storage decisions；E46 E2: Execute pre-release rule；E03 E10: Roll the horizon and update decisions |
| 开展调度方案对照、敏感性与稳健性检验（Compare and test reservoir operating policies） | 与现行规则或其他方法比较，并改变预报、洪水事件、时域和参数等条件，检验表现、失效情形及适用范围。 | E01 E9: Compare simulated schemes with the current rule；E10 E6: Stress forecast and horizon choices；E50 E10: Perform LOOCV and restrict the TOCS bound after failures |
| 推进调度会商、试点实施与规则修订（Conduct operational consultation, pilot implementation, and rule revision） | 在涉及实际管理流程的研究中，提交方案会商、实施和观测试点调整、复盘运行表现，并更新调度文件。 | E21 E5: Submit schemes for multi-department consultation；E18 E8: Temporarily implement and observe a pilot modification；E18 E11: Update WCM/WCP and preserve future adaptability |

## 后续归类时需要保留的区别

- **研究准备、运行循环与评价分支：**预报模型训练、调度参数校准、每时段行动和方案验证不必处于同一连续执行链中，应分别标记其作用。
- **模拟执行与实际实施：**标题中的 execute、apply 或 run 不能单独证明实际运行部署；涉及行动实施的归类需回查原始提取说明。
- **不同不确定性传播方法：**情景模拟、矩传播和概率网络推断可以承担相似功能，但不应全部改写为 Monte Carlo 情景生成。
- **风险指标与真实后果：**水位超限概率、模型损失、熵或韧性指标不能不加区分地合并为真实洪灾损失。
- **宽泛或多功能标题：**例如 E12 E5 “Simulate and compare” 应回查说明后编码；一个 step 可以对应多个候选类别，不能为凑单一类别而丢失功能。
- **条件性管理分支：**会商、试点和调度文件修订在部分论文标题中明确出现，应保留为条件性分支，不据此要求所有模型研究都覆盖这些环节。

下一步保留每条原始 step 和论文编号，再逐条标注候选类别及“可直接归类／需要回查／包含多个功能”。本表暂不展开 micro-skill 的输入、操作与输出规格。
