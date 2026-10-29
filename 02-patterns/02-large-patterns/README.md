# 02 - 大 pattern：从 AI 初稿到定稿

最终定义：[`large-patterns.md`](large-patterns.md)，9 个推理 + 11 个执行大 pattern，每个 pattern 包括名称和共同问题（推理）或共同任务（执行）。这就是步骤编码（`../03-step-coding/`）所依据的定义。

生成提示词：[`prompt-large-patterns.md`](prompt-large-patterns.md)，一次生成同样格式的定义。

## 版本演变

| 顺序 | 版本 | 文件 | 谁做的 | 做了什么 |
|---|---|---|---|---|
| 1 | AI 初稿（2026-09-17） | [`history/1-ai-draft/`](history/1-ai-draft/) | AI | 阅读 760 个步骤标题后，归纳出 8 个推理和 11 个执行类别；中英文名称、共同问题 / 任务，并附原始 step 示例和归类注意事项 |
| 2 | 人工改写（2026-09-18） | [`history/2-human-revised/patterns-en.md`](history/2-human-revised/patterns-en.md)（另有 PDF 和中文翻译） | 用户 | AI 写的定义不够 domain，由用户改写。8+11 个类别一一对应、顺序不变，改的主要是名称和问题 / 任务的措辞（见下节） |
| 3 | 定稿（2026-10-01） | [`large-patterns.md`](large-patterns.md) | 用户决定 | 在第 2 版上新增 RP08"选择模型表示与求解方法"：步骤编码中有 38 个方法选择类推理步骤（26 篇论文）没有对应 pattern，用户决定单列，并按实证位置插入在证据 pattern（RP09）之前。其余 19 个 pattern 的名称和问题 / 任务与第 2 版相同 |

第 1 版之前还做过 E01–E05 的功能抽象试点，原件在 `artifacts/run-20260914-0925-50paper-patterns/02-pattern-extraction/02-large-patterns/01-preliminary-drafts/pilot/`，没有复制过来。

## 人工改写改了什么（第 1 版 → 第 2 版）

| 方面 | AI 初稿 | 人工改写 |
|---|---|---|
| 推理类别的动词 | Identify / Assess / Define / Choose | Diagnose / Judge / Justify / Consider：像专家在下判断；Judge 用于"是否成立"，Justify 用于"设定并论证标准" |
| 领域锚定 | 较泛，例如 "…for reservoir decisions" | 每个名称都落在防洪调度上："under flooding risk"、"for reservoir flood-operation decisions"、"across flood-event stages"、"of candidate operating plans" |
| 推理的共同问题 | 学术化的长问句 | 调度员或洪水水文专家会问的大白话；需要时拆成几个具体小问，并点名预见期、库容、泄流能力、下游约束等量 |
| 执行的共同任务 | 带方法论注释，例如"保留各指标的具体定义""检查或处理约束违反""供后续推算使用的不确定性表示" | 删掉注释，只写做什么、产出什么；点名水位、库容、泄量、下游流量等对象；以"每个候选调度方案"为单位 |
| 格式 | 中英双语名称、step 示例、归类注意事项写在一起 | 只保留英文的"类别 + 共同问题 / 任务"两列，前面加一段语料说明 |

举例：

- AI：*Assess physical and operational feasibility of reservoir adjustments* —— 预报提前量、可用库容、泄流能力及下游安全约束，是否允许实施预泄、蓄水或水位边界调整？
- 人工：*Judge physical and operational feasibility of reservoir adjustments* —— Is there enough forecast lead time to adjust reservoir operations? Is there enough storage and release capacity? Can adjustments be made without violating downstream safety constraints?

## 提示词

[`prompt-large-patterns.md`](prompt-large-patterns.md) 把上面三步合成一次生成：

- 归纳方法照第 1 版：按功能分组，不按方法名或论文章节；
- 写作规则照第 2 版的改动：动词、领域锚定、大白话问题、去掉注释，并附两行原句作为风格示例；
- 方法选择单列为一个推理 pattern，对应第 3 版新增的 RP08。

输入是 `../01-steps/` 中的步骤标题和描述，输出格式与 `large-patterns.md` 相同（ID、名称、共同问题 / 任务）。

## 局限

- 提示词是根据版本差异**倒推**出来的，当时实际用的提示词没有保存。生成结果会接近这一版，但不会逐字相同。
- 提示词没有被运行过，现有定义也没有被替换；它与定稿有多接近，还没有检验。
