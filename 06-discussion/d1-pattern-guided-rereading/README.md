# D1：读一遍论文提取不全 pattern，按 pattern 回头再读能多找到一些

## 问题

我们的 pattern 来自对每篇论文做一次开放式提取：读一遍，写成 card，拆成步骤，再把步骤编码到 pattern。读一遍会不会漏掉论文实际用到的 pattern？如果拿着 pattern 清单回到原文逐条去找，能多找到多少？

## 做法

方案写于 2026-10-02，在运行之前。原文见 `protocol.md`。

- **样本**：从 50 篇开发集论文中随机抽 10 篇（seed 20261002）：E06、E10、E11、E23、E24、E26、E32、E35、E42、E44（`data/sample.json`）。
- **条件 A，一次提取**：现有开放式提取加步骤编码所得到的每篇论文的大 pattern，存在 `data/onepass.json`。2026-10-29 已核对，它与 v3 的步骤编码（`../../02-patterns/03-step-coding/step-pattern-matches.csv`，primary 和 secondary 都算）逐篇完全一致，共 121 处。
- **条件 B，按 pattern 回读**：每篇论文交给一个新的子代理。子代理读论文全文和 pattern 清单（`data/pattern-list.md`，含 20 个大 pattern 和它们的小 pattern），对每个大 pattern 判断"有 / 没有"。判定规则：
  - 只有论文自己做了这个判断或这项工作才算"有"，只在文献综述或展望里提到的不算；
  - 每个"有"都要附一段不超过 40 个词的原文引文；
  - 子代理看不到条件 A 的结果。

  输出在 `data/reread/Exx.json`。
- **核对**：回读新找到的每一处，都由项目编码者（当时的 Claude Code 主会话）对照引文判定是否成立。33 处中有 5 处不成立，予以剔除，理由见 `results.md`。

## 结果

| | 数量 |
|---|---:|
| 一次提取找到的 pattern | 121 |
| 回读新找到并核对成立的 | **+28（+23%）** |
| 回读新找到但核对不成立、已剔除的 | 5 |
| 一次提取找到、回读却没找到的 | 9 |
| 两者合并 | 149 |

- **一次提取只找到约 81%**（121/149）的 pattern；回读后多出 23%。
- **漏得最多的**：EP01 数据与基线（4 篇）、EP05 安全边界与可行性（4 篇）、RP02 决策相关的不确定性（3 篇）、RP08 模型与方法选择（3 篇）。
- **漏的是"出现了几次"，不是"有哪些 pattern"**：回读补上的 pattern，在其他论文的一次提取结果里都已经出现过；没有发现新的 pattern 类别。EP08 和 EP11 在这 10 篇中都没有出现。
- **两种读法各有遗漏**：一次提取找到的有 9 处回读没找到。所以回读不能取代一次提取，两者应当合用。

图：`figures/d1-rereading-by-paper`（按论文），由 `rereading_figures.py` 生成。

## 对讨论的意义

1. **pattern 体系是稳定的，但出现频次被低估了**：回读没有找出新的类别，说明 20 个大 pattern 的划分站得住；但每个 pattern 在多少篇论文中出现，是一次提取得出的下限，实际还要多两成左右。
2. **"证据少"的 pattern 可能只是读漏了**：skill 中标为 "When relevant" 的检查，来自出现篇数少的小 pattern。如果一次提取会漏，这些 pattern 实际出现的篇数可能更多。这也支持我们把 "Optional" 改为"只要涉及就必须考虑"（见 `../../03-skills/revisions/human-review-notes-zh.md` 例 2）。
3. **方法建议：两遍读**。第一遍开放式提取，归纳出 pattern；第二遍拿 pattern 清单回到原文逐条查找，并要求附原文引文、由人核对。后续扩充语料时可以采用这个流程。

## 局限

- **样本小**：只有 10 篇论文，各 pattern 的补充数大多是 1–4 篇，按 pattern 的比较只能看大致趋势。
- **读者和核对者都是 AI**：回读子代理用的模型当时没有记录；核对由 Claude Code 主会话完成，不是人工核对。
- **拿着清单读会诱导多判**：因此要求附引文并逐条核对，33 处新找到的中剔除了 5 处。
- **只比到大 pattern 一级**：没有比较小 pattern 和步骤一级的差异。
- **主线结果没有使用回读数据**：v3 的 pattern 频次和 skill 都基于一次提取。回读只在这里作为讨论材料。

## 文件

| 文件 | 内容 |
|---|---|
| `protocol.md` | 运行前写定的方案（英文） |
| `results.md`、`comparison-raw.md` | 结果表、剔除理由、需核对的回读引文清单 |
| `data/` | 样本、一次提取结果、pattern 清单、10 份回读输出（含引文） |
| `scripts-original/` | 当时运行用的脚本，原样保留。它们的路径指向旧 run，在这里不能直接运行 |
| `rereading_figures.py` | 本目录的作图脚本：`python rereading_figures.py data figures` |
| `figures/` | 一张图，PNG 和 SVG 格式 |

**来源**：`artifacts/run-20260914-0925-50paper-patterns/04-development-50-backtest/pattern-guided-rereading/`（2026-10-02）。2026-10-29 复制到这里，原处没有改动。
