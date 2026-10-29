# 03 - 步骤编码：每个步骤属于哪个大 pattern

## 文件

| 文件 | 内容 | 怎么来的 |
|---|---|---|
| `step-coding.csv` | 760 个步骤，每步一个 primary pattern、若干 secondary pattern、一句针对这一步的理由 | Claude Code 逐步编码（2026-09-30 至 10-01） |
| `build_matches.py` | 由 `step-coding.csv` 生成下面三张表 | 脚本 |
| `step-pattern-matches.csv` | 1,074 条正向匹配（primary 757 条，secondary 317 条），每条附 pattern 名称和理由 | 脚本生成 |
| `unmapped-steps.csv` | 3 个没有匹配任何 pattern 的执行步骤（E20-E11、E22-E11、E48-E8），只记录局限 | 脚本生成 |
| `pattern-coverage.csv` | 每个大 pattern 的论文数、步骤数、primary / secondary 匹配数 | 脚本生成 |

复现：`python build_matches.py`。

## 编码方法

- 编码者只读步骤内容（标题、描述、procedure），对照大 pattern 定义，为每步判定一个 primary（或"无匹配"）和若干 secondary，并写一句只适用于这一步的理由。
- 760 步分 10 批完成，全部编完后才汇总。
- **方法选择步骤：** 编码时，"为什么选这个模型 / 求解方法 / 表示形式"（例如 KKT 推导、SDE、贝叶斯网络、GA、PCA、LSTM）没有对应的推理 pattern，先记为无匹配。这类推理步骤共 38 个，来自 26 篇论文。用户据此决定新增 RP08"选择模型表示与求解方法"，38 步全部作为它的 primary 证据。RP08 与其他步骤的 secondary 关系没有编码。
- **只记录局限、不涉及执行的步骤：** 记为无匹配（即 `unmapped-steps.csv` 中的 3 步）。

## 边界规则（全部 50 篇统一使用）

- **EP04 vs EP07：** EP04 产出水位、库容、流量轨迹；统计超阈、计算风险 / 损失 / 指标属于 EP07。
- **EP02 vs EP03：** EP02 建立、校正、检验预报产品（包括检验合成集合的覆盖度）；EP03 拟合误差分布、抽样、生成情景。
- **EP06 vs EP05：** 建立并求解优化模型属于 EP06，其中的约束作为 secondary 计入 EP05；单独计算边界、筛选可行性属于 EP05。
- **RP06 vs RP09：** 设定目标、取舍和选择原则属于 RP06；与基线比较、敏感性分析、外推边界属于 RP09。

更多 pattern 之间的边界见 `../06-taxonomy/` 第 6 节。

## 局限

- 只有一个编码者（Claude Code），没有做独立的二次编码。
- 非盲：编码者在此之前看过 E01、E13、E42–E50 共 11 篇的部分归类。
- 编码结果保存为数据，每一步都有理由，可以逐条审查；但编码过程本身是 LLM 判断，不能用脚本重新生成。
