# Round-01 裁判意见综合分析（A = 无 skill，C = 有 skill）

由一个 Claude Opus 5.5 子代理生成（2026-10-28）：只读了 `judgments/` 下的 42 份裁判文件、`blinding-key.json` 和 `questions-en.md`，没有读答案、skill 或其他文件夹。子代理不能写文件，本文件由主会话按其返回内容原样保存。其中的位置效应统计与 opus-U6-j2 的算术更正已由主会话用脚本复核（见 `analysis-zh.md` §2）。

**揭盲规则**：j1 中 "Answer 1" 对应 key 的 answer1；j2 中 "Answer 1" 对应 key 的 answer2。每一条用两种方式核对：脚本按 key 映射；j2 正文里的文件名标注（如 "Answer 1 (U1-jqa3)"）和两位裁判对同一答案的内容描述是否一致。两种核对结果一致。出处标注为"模型-题号"（如 opus-U2），需要指明具体裁判时写成 opus-U2-j1。

## 0. 胜负总览（揭盲后）

| 模型 | U1 | U2 | U3 | U4 | U5 | U6 | U7 | C 胜 / A 胜 / 平 |
|---|---|---|---|---|---|---|---|---|
| opus | C,C | C,C | C,C | C,平 | A,C | A,C | C,C | 11 / 2 / 1 |
| sonnet | C,C | C(clear),C | A,C | A,C | C,平 | C,C | C,C | 11 / 2 / 1 |
| haiku | C,C | C(clear),C(clear) | A,A | A,A | C,A | A(clear),A(clear) | C(clear),C(clear) | 7 / 7 / 0 |
| 合计 | 6/0 | 6/0 | 3/3 | 2/3/1平 | 3/2/1平 | 3/3 | 6/0 | **29 / 11 / 2** |

每格依次为 j1、j2 的结果；未特别标注的都是 "slight"。

C 减 A 的五项总分差（14 份判定合计）：
- opus：+32（ME +10、KQ +7、TC +7、CA +6、PR +2）
- sonnet：+25（ME +8、KQ +7、TC +6、CA +4、PR 0）
- haiku：+15（ME +11、PR +8、KQ +7、TC 0、**CA −11**）

**解读证据前需要注意：**
- **位置效应**：j1 裁判有 17/21 次判 "Answer 2" 胜，j2 是 9/21。5 个两位裁判意见相反的格子（opus-U5、opus-U6、sonnet-U3、sonnet-U4、haiku-U5）全部是两位裁判都判位置 2 胜，应视为接近平局。
- **裁判自身的算术错误**：opus-U6-j2 指 C 的"50 年超越概率 48%"是错的、应为 52%。但 opus-U6-j1 和 sonnet-U6-j1 都给出 1−0.987^50 ≈ 0.48，C 原本是对的。C 在这份判定里 TC 被扣 1 分属于误扣。
- **几乎全是小差距**：42 份里只有 8 份是 "clear"。

## 1. C 组稳定优于 A 组的地方

### 1.1 用"无预报 / 实际预报 / 完美预报"给预报价值定上下界（最稳定的优势）

- **出处**：opus-U1、opus-U3、opus-U4、sonnet-U1、sonnet-U3、sonnet-U4、sonnet-U6、haiku-U3、haiku-U4
- **裁判对 C 的评价**：
  - opus-U1："a three-condition forecast comparison (none / actual / perfect)"；"separates the value of staging from the value of forecasts"
  - opus-U3："no-forecast and perfect-forecast bounds as a diagnostic"
  - sonnet-U3："information bounds (perfect and no forecast) and a fixed-margin control rule"
  - sonnet-U6："Bracketing the forecast value between a no-forecast run and a perfect-forecast run is a good verification step"
  - haiku-U4："It separates forecast value from model skill using no-forecast and perfect-forecast bounds"
- **A 组的相应缺失**：
  - opus-U3 A："lacks perfect-forecast and no-forecast bounds"
  - sonnet-U1 A："No perfect-foresight upper bound"
  - sonnet-U4 A："No no-forecast vs perfect-forecast bracket"

### 1.2 预泄 / 消落在有效预见期内的可行性检查（定性层面）

- **出处**：opus-U3、opus-U6、opus-U7、sonnet-U1、sonnet-U3、sonnet-U4、sonnet-U6、sonnet-U7、haiku-U1、haiku-U2
- **裁判对 C 的评价**：
  - opus-U3："physical feasibility of the prerelease within the effective lead time"
  - opus-U7："It makes the low-level capacity limit drive the timing of pre-release"
  - sonnet-U1："applies time/space/downstream/transition ceilings before optimization"
  - sonnet-U6："feasibility explicit: drawdown against forecast lead time, release capacity, downstream safe release, travel time, refill"
  - haiku-U2：C "correctly identifies the deciding structure: a 28 h effective window and a release capped at 5,000 − 1,200 = 3,800 m³/s"；A 用的是 8 h 窗口和 7,500 m³/s 的闸门能力
- **局限**：这些检查基本停留在定性层面，几乎没有算出具体数值（见第 3 节 M1）。

### 1.3 以现行规则为对照基准，并事先设定验收标准

- **出处**：opus-U1、opus-U2、opus-U3、opus-U4、sonnet-U1、sonnet-U2、sonnet-U4、sonnet-U7、haiku-U4
- **裁判对 C 的评价**：
  - opus-U1："It diagnoses whether the fixed level binds before claiming gains"
  - opus-U2："A benchmark-based acceptance rule (risk no greater than the current 152 m rule)"；A 则 "No acceptance criterion or benchmark for choosing the final level"
  - opus-U3："an acceptance criterion fixed in advance with the dam-safety authority"
  - opus-U4："acceptance criteria expressed as exceedance probabilities of the design and check levels … no worse than the current rule"
  - sonnet-U2："Benchmarking against the 152 m rule"
  - sonnet-U4："An explicit executable-rule comparator under identical initial state"

### 1.4 模型 / 模拟器自身的验证与稳健性步骤

- **出处**：opus-U4、opus-U6、opus-U7、sonnet-U4、sonnet-U7、haiku-U7
- **裁判对 C 的评价**：
  - opus-U4："validates the simulator by replaying the recorded 2023 releases against observed levels"；"constraint violations count as failures, not clipped after the fact"
  - opus-U7："Rounding to a gate setting, then a full nonlinear re-check on all 51 members … is the right operational loop"；"checks hindcast/operational forecast-system consistency"
  - sonnet-U7："a tree-size/horizon sweep; explicit pass criteria; recommendation stability across cycles"
  - haiku-U7："Non-anticipative first-stage release with recourse"；A 则 "a single rate or ramp across 10 days is open-loop"

### 1.5 判断有界：安全不可补偿、证据分级、承认"不能下结论"

- **出处**：opus-U1、opus-U4、sonnet-U1、sonnet-U2、sonnet-U6、haiku-U1
- **裁判对 C 的评价**：
  - opus-U1："the current data support 'promising' only"；"Safety is a hard filter and benefits cannot buy it back"
  - opus-U4："lists exactly what is and is not supported"
  - sonnet-U1："a negative result is explicitly valid … grades conclusions by evidence level"
  - sonnet-U2："Clean separation of the theoretical ceiling from the operating limit"
  - haiku-U1：C "treats safety as non-compensable"；A 则 "pre-judges the study"

### 1.6 部分题目中：机理解释和分阶段采用更具体（不稳定）

- **出处**：opus-U6（"Mechanism reasoning that explains the pattern in the table"）、sonnet-U4（"Diagnosis of the 2023 trajectory"）、sonnet-U2（"A fallback rule that is itself tested"）、opus-U7（"Staged adoption under a documented temporary deviation"）、sonnet-U6（"temporary modification of the operating manual"）
- **反例**：在 opus-U4、sonnet-U3、sonnet-U4-j1、haiku-U4 中，A 的治理和运行条款反而更具体。

## 2. C 组做得更差或犯错的地方

### 2.1（a）可能由 skill 引起的问题

#### 2.1.1 把 skill 内容当成文献引用（opus 没有；sonnet 3 题；haiku 5 题；A 组从未被指出）

- **haiku-U1**："refers to 'the papers' without any basis"；"it cites 'the papers' that do not exist in the prompt"
- **haiku-U3**：
  - "'This violates what 50 papers in flood operation research found' is an unsupported appeal to authority"
  - "presents illustrative numbers as literature findings"
- **haiku-U4**："repeatedly asserts 'standard practice in the literature / papers do X' without support"
- **haiku-U6**："It cites 'the papers in the reference' and 'the reference material', which do not exist in the question"（两位裁判都指出）
- **haiku-U7**："literature claims ('E17-R2', 'no SDP instances in the literature')"
- **sonnet-U3**："vague appeals to 'papers have reported...' … without citations"（两位裁判都扣了 CA）
- **sonnet-U4**："'Papers in this field show benefits can be ... negative'"
- **sonnet-U7**："twice cites 'papers' … with no source"（两位裁判都扣了 CA）

#### 2.1.2 泄露 skill 内部编号 / 术语

- **haiku-U7**："unexplained references ('E23-R4', 'E17-R2')"
- **haiku-U5**："It cites unexplained internal codes (RP05-B and similar)"
- **haiku-U4**："'Stage A/B/C screening' are used as generic labels without content"

#### 2.1.3 虚构具体事实或数值，并当作证据呈现（主要是 haiku-C）

- **haiku-U7**："a named forecast system (HEFS); a hydraulic model (SOBEK); 'NSE ≈ 0.97 on similar systems'"
- **haiku-U1**："it invents a forecast period ('2015–2023')"
- **haiku-U3**："a made-up credible interval of [12%, 24%]"
- **haiku-U5**："It fabricates tributary timing and a forecast split"

A 组也有虚构，例如 haiku-U2 的 A 编造了三峡先例。

#### 2.1.4 被清单带偏：做了通用检查项，却漏掉或"假设掉"本题的决定性问题

- **haiku-U4**（C 两次都输）：C 把实时预报可用"lists … as an *assumption*, which assumes away the deciding question"，也没有先做影子运行。
- **haiku-U6**（C 两次 clear 输）："It states the right principle: flood risk is non-compensable … It then recommends the one scheme that breaks the current flood-risk level"
- **sonnet-U3-j1**（C 输）："No hindcast-versus-operational distinction … No in-sample tuning … No block or event bootstrap … No pre-agreed acceptance criteria, shadow mode or revert triggers"
- **sonnet-U4-j1**（C 输）："no simple-heuristic or MPC baseline … The pilot and fallback provisions lack concrete exclusion thresholds"
- **opus-U3-j1**：C "does not quantify the independence effect"
- **opus-U5-j1**（C 输）：C 没有把汛限以上的蓄水视为按规程应腾空的部分；j2 的看法相反。
- **opus-U6-j1**（C 输）：C 缺非支配性比较表，也没考虑连续洪水。

### 2.2（b）一般性技术错误（C 组）

- **haiku-U1**：分期方向颠倒，"sets the FLWL *higher* in June–August and *lower* in May and Sept–Oct"
- **haiku-U2**：没有扣除入库流量，"This error changes a conclusion"
- **haiku-U5**：消落 194 Mm³，超过被占用的 75 Mm³ 防洪库容；把支流算进了上库入流
- **haiku-U6**：把方案 C 的风险读反；"0.3 billion kWh is written as '0.3 GWh'"
- **haiku-U7**：称问题"convex"，但模型中含机会约束；蒙特卡洛的算术有误
- **sonnet-U2**：库容–面积关系的方向写反；690 应为约 675 m³/s
- **sonnet-U5**：47 应为约 56 M m³；默认汛期还能回蓄
- **opus-U5**：方案 (c) 的追赶流量写成 3,500–4,000 m³/s，应为约 3,200–3,400

A 组同类错误（对照）：
- haiku-U2 A：8 h / 7,500 m³/s
- haiku-U5 A：把"预泄会腾出库容"说反了
- haiku-U1 A：0.9 写成 2.25
- opus-U1 A：把不保守的做法说成 "conservative"
- sonnet-U5 A：约 4,000 m³/s，应为约 2,330

## 3. 两组都漏掉、裁判反复指出的要点（计数单位："题×模型"组合，共 21 个）

| 编号 | 主题 | 组合数 |
|---|---|---|
| M1 | 数量级算例缺失：预泄 / 消落体积 = 净泄量 × 有效时间，并与库容比较；用质量守恒核验"削峰 X%" | 12 |
| M2 | 正式审批路径 / 法定运行依据（具体国家机构；获批前现行规则仍是法定依据；规程或手册修订） | 19 |
| M3 | 概率 / 抽样算术：1−(1−p)^n；蒙特卡洛标准误；有限记录的二项标准误；重现期与超越概率换算；独立误差导致低估 √3 或 1+2ρ 倍 | 12 |
| M4 | 没有计算传播时间 | 7 |
| M5 | 没有从抬高后的水位起调设计 / 校核洪水 | 8 |
| M6 | 中止 / 回退协议与误报代价 | 9 |
| M7 | 分期 / 动态汛限水位作为标准工程路线 | 5 |
| M8 | U5 特有：上游暴雨与区间支流同源；汛限以上蓄水按规程应腾空；利用两次预报更新构成决策树 | 3 |
| M9 | U4 特有：2023 年实际峰值是否超过安全泄量；起调水位；"学运行人员却胜过运行人员"的悖论 | 3 |
| M10 | U7 特有：回报预报与业务预报的集合配置不一致；残差法得到的支流序列混入误差；闸门开度–水头关系；30 分钟计算预算 | 3 |

M1–M4 都是"该算的没算"。这个问题在 C 组同样存在，没有因为有 skill 而改善。

## 4. 按模型

- **opus-C**（11 / 2 / 1）：
  - 长处："先诊断再设计"；按情景表折算到体积和水位；分门控的评估顺序；闸门取整后复核
  - 没有 skill 副作用（"No numbers are invented"）
  - 输的两次都出现在两位裁判意见相反、且都判位置 2 的格子里
- **sonnet-C**（11 / 2 / 1）：
  - 长处："决策结构化"：开头列出 3 个决定性问题；可行性上限；盈亏平衡表；逐项通过标准
  - 问题：3 题出现无出处的 "papers…"；U3 和 U4 的治理条款不如 A 具体；有小算术错误
- **haiku-C**（7 / 7）：
  - 赢：靠结构正确而 A 结构错误（U2、U7、U1）
  - 输：都与 skill 副作用加核心错误有关（U3、U4、U6）
  - CA 合计 −11；7 题中有 6 题出现文献、参考或编号问题
  - 小结：skill 给了正确的检查清单（ME +11、PR +8），但没能阻止方向性错误，还让模型把 skill 当成了外部证据。

## 5. 按题目

- **U1（C 6/6）**：前置诊断（固定汛限是否起约束作用、消落能否在预见期内完成）、三档预报对照、证据分级。两组都缺风险组合算例和印度的审批体系。
- **U2（C 6/6）**：理论上限与运行上限分开、盈亏平衡表、以 152 m 规则为基准。haiku-C 抓对了窗口和下游约束，但漏减了入流。两组都缺中止协议和审批依据。
- **U3（C 3/6，haiku-C 0/2）**：C 在上下界和可行性上占优，但常漏掉独立误差的定量、回报预报与业务预报的区别、块自助法和治理条款。haiku-C 因虚构文献而输。
- **U4（C 2 胜 3 负 1 平）**：opus 和 sonnet 的 C 有回放验证和上下界，但 A 的治理条款更全。haiku-C 把事后入流的问题"假设掉"了。6 份判定都指出缺质量守恒算例。
- **U5（C 3 胜 2 负 1 平）**：结论高度依赖裁判和答案位置。真正的分水岭（汛限以上蓄水应腾空、支流同源遭遇、上库大坝安全）两组都没有稳定抓住。
- **U6（C 3 胜 3 负）**：sonnet-C 两胜；opus 一胜一负（其中一次是误扣）；haiku-C 两次 clear 输。三个模型都缺二项标准误、超越概率换算和法定审批。
- **U7（C 6/6）**："非预期首阶段 + 场景树 + 闸门取整 + 全模型复核 + 回退"的结构。haiku-C 泄露了编号并虚构了 HEFS / SOBEK；sonnet-C 有无出处的 "papers"。

## 6. 整体判断与建议（子代理原文要点）

**整体判断**：
- skill 在 opus 和 sonnet 上带来稳定但小幅的提升，在 haiku 上净效果接近零。
- 提升来自检查框架；"算出来"的能力没有提升。
- 主要副作用是来源混淆和清单挤掉决定性问题。

**建议**：
1. 禁止把 skill 当文献引用，禁止输出内部编号，禁止补出题目未给的产品、数据期或数值。
2. 增加强制的数量级算例和公式模板。
3. 增加概率与样本分辨率算例。
4. 增加方向性自检，并核对结论与自设约束是否一致。
5. 先列出本题的决定性问题，再做通用检查；补齐审批与回退的具体内容。

**评测方法**：
- 两位裁判结论相反时计为平局，或增加第三位裁判。
- 抽查裁判给出的算术更正。
