# 文献检索与筛选标准（50 + 5 篇）

整理日期：2026-10-28。本文件把散落在原始记录中的检索与筛选规则汇总为一页，没有新增或修改任何标准。原始依据：

- [`search-log-2026-09-15.md`](search-log-2026-09-15.md)：检索与获取记录（原文件 `search-and-acquisition-log.md`）
- `../../../artifacts/run-20260914-0925-50paper-patterns/01-corpus/project-notes/2026-09-14-design-agreement.md` 与 `2026-09-15-agreed-work-roadmap.md`：设计共识（未复制，路径为原 run）
- [`../tools/historical-acquisition/collect.py`](../tools/historical-acquisition/collect.py)：实际执行的检索脚本

## 1. 研究主题边界

洪水风险与预报不确定性下的水库运行规则 / 程序调整（Reservoir operation adjustment for flood risk management）。干旱暂不纳入。

## 2. 检索

| 项目 | 内容 |
|---|---|
| 检索日期 | 2026-09-15 |
| 主检索源 | Crossref `/works` API，类型限 `journal-article`，出版日期截至 2026-09-15 |
| 每个查询取数 | 按相关度排序前 60 条 |
| 辅助来源 | OpenAlex（开放版本发现）；出版社、作者机构、NOAA、NSF 公共资料库（获取全文） |
| 既有文献 | 0902 run 快速候选表（20 条）和本地 PDF 库中标题含 flood / ensemble / inferred inflow 的条目，经 DOI 核对后并入候选池 |

7 个检索式（原样）：

1. `reservoir flood control forecast uncertainty`
2. `reservoir flood limited water level dynamic control risk`
3. `forecast informed reservoir operations prerelease`
4. `reservoir flood control robust stochastic optimization`
5. `reservoir flood control ensemble model predictive control`
6. `multi reservoir flood operation uncertainty risk`
7. `reservoir flood hedging operating rules forecast`

检索响应保存在 [`search-metadata/`](search-metadata/)（`query-*.json` 为检索结果，`doi-*.json` 为单篇 DOI 核对）。这不是穷尽式系统综述。

## 3. 筛选流程与数量

| 步骤 | 数量 | 记录 |
|---|---:|---|
| 检索 + 既有文献 DOI 去重 | 351 | [`candidates.json`](candidates.json) |
| 初步标题线索筛选（水库 / 坝 + 洪水 / 预报） | 193 | [`candidate-screening.txt`](candidate-screening.txt) |
| 题目 / 摘要判断后选入 | 55（50 开发 + 5 验证） | [`selection.json`](selection.json)、[`corpus-55.md`](corpus-55.md) |

## 4. 纳入标准

- 原始研究或运行实施案例，且与防洪决策有明确联系。
- 优先覆盖的子主题：汛限水位（含动态控制、分期）、预泄与回蓄、hedging、预报误差、多库风险、滚动优化 / MPC、决策偏好与方案选择。
- 不因"已有本地 PDF"而纳入。
- 0902 快速候选 20 条中 19 条纳入（P18 为综述，只作找文献的线索）；另纳入 0902 使用的 4 篇全文锚点。

## 5. 排除标准

- 纯预报研究，与运行无联系。
- 纯发电或供水调度（防洪只作为固定水位约束的也排除，例如原 E49 Yang et al. 2020，已移出）。
- 坝体结构设计。
- 明显不相关领域。
- 撤稿文章。

## 6. 开发集与验证集的划分

- 50 篇开发集（E01–E50）用于抽取、pattern 归纳和 skill 构建；5 篇验证集（V01–V05）不参与这些工作。
- 两集按 DOI、标题、版本去重，无重复。
- 验证集如被用于修订 skill，就记为"已暴露"，之后的独立验证需要另选文章。
- 隔离只针对本项目流程，不能证明基础模型预训练时没见过这些文章。

## 7. 获取后的文件核对

PDF 魔数、可解析页数、首页或前两页的 DOI / 标题匹配、正文文本可提取性、SHA256。这是文件身份核对，不是全文适用性审计。获取来源见 [`acquisition-results.json`](acquisition-results.json) 和 [`user-import-report-20260915.md`](user-import-report-20260915.md)（38 篇由用户经机构权限下载）。

## 8. 选入后的变更

| 日期 | 变更 | 记录 |
|---|---|---|
| 2026-09-15 | E49：Yang et al. 2020 → Huang et al. 2022（原文侧重供水 / 发电） | [`search-log-2026-09-15.md`](search-log-2026-09-15.md) |
| 2026-09-15 | E02：Zhao et al. 2011 → Zhu et al. 2017（用户指示，原文主题关联不足） | [`e02-replacement-record-20260915.json`](e02-replacement-record-20260915.json) |
| 2026-09-15 | 11 条题录的标题 / 年份校正 | [`bibliographic-corrections.md`](bibliographic-corrections.md) |

## 9. 可复现性缺口

- **193 → 55 这一步没有逐篇决策记录。** 只保存了每篇入选文献的主题标签（`selection.json` 的 `topic`）和一句纳入理由（`corpus-55.md`）。没有入选的 138 篇，排除理由未记录；也没有说明 55 篇是如何在子主题之间分配的。
- 纳入判断依据的是题目和摘要；全文适用性审核在原记录中标为"待后续"，没有单独的完成记录。
- 5 篇验证集是从同一候选池中挑选的，挑选规则未单独记录。
