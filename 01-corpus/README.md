# 01 - Corpus：55 篇论文、全文文本、paper card

本层是 v3 的起点：50 篇开发集（E01–E50）+ 5 篇验证集（V01–V05）的原文、全文文本、结构化抽取（paper card），以及筛选标准和抽取提示词。

来源：全部从 `artifacts/run-20260914-0925-50paper-patterns/01-corpus/` 复制（2026-10-28），原处未改动。文件内容未改，只改了部分文件名（见下文）。

## 目录

```
01-corpus/
├─ corpus-manifest.md / .csv   55 篇总表：题录、DOI、页数、SHA256、纳入理由，以及到 PDF / 文本 / card 的链接
├─ development-50/             开发集：用于抽取、pattern 归纳、skill 构建
│  ├─ papers/   E01.pdf … E50.pdf
│  ├─ text/     E01.txt … E50.txt      按页分隔（--- Page N ---）
│  └─ cards/    E01-card.md … E50-card.md
├─ heldout-5/                  验证集：不参与 pattern 归纳与 skill 构建
│  └─ papers/ text/ cards/     V01–V05，结构同上
├─ selection/                  检索与筛选
│  ├─ screening-criteria.md    ← 筛选标准汇总（从这里看起）
│  ├─ search-log-2026-09-15.md 原始检索与获取记录
│  ├─ candidates.json          351 条去重候选（Crossref 原始记录）
│  ├─ candidate-screening.txt  193 条通过标题初筛的候选
│  ├─ selection.json           55 篇选入记录（题录、split、topic）
│  ├─ corpus-55.md / .ris      原始 55 篇清单（文中 PDF 链接指向旧目录，已失效；请用 corpus-manifest.md）
│  ├─ search-metadata/         Crossref 检索与 DOI 核对的原始响应（86 个 json）
│  └─ 其余                     获取结果、题录校正、E02 替换、用户导入记录
├─ prompts/                    生成 paper card 的提示词（见 prompts/README.md）
├─ tools/
│  ├─ pdf_to_text.py           PDF → 文本（pypdf；重建并核对过，见下文）
│  ├─ build_manifest.py        生成 corpus-manifest
│  └─ historical-acquisition/  当时实际运行的检索 / 下载脚本，只作记录（路径仍指向旧目录，不能直接运行）
└─ SHA256SUMS                  本层所有文件的校验和
```

改名对照：`structured-extractions/Exx-extraction.md` → `cards/Exx-card.md`；`templates/paper-extraction-template.md` → `prompts/card-prompt-en.md`；`search-and-acquisition-log.md` → `selection/search-log-2026-09-15.md`。

## 怎么复现

| 步骤 | 输入 | 方法 | 可复现程度 |
|---|---|---|---|
| 1. 检索 | 7 个检索式 | Crossref API，见 `selection/screening-criteria.md` | 检索响应已保存；重新检索的结果会因数据库更新而变化 |
| 2. 筛选 | 351 → 193 → 55 | 标题初筛 → 题目 / 摘要判断 | **193 → 55 没有逐篇决策记录** |
| 3. 获取 | DOI | 开放获取 + 用户机构下载 | SHA256 已记录在 manifest 中，可以核对文件身份 |
| 4. 转文本 | PDF | `python tools/pdf_to_text.py --check` | **已核对**：55 篇去掉空白后内容完全一致；11 篇逐字节一致，44 篇只有标点和符号周围的空格不同（pypdf 版本不同所致，原版本未记录） |
| 5. 生成 card | 文本 + `prompts/card-prompt-en.md` | 每篇一个子代理 | **模型、日期、批次未记录**，见 `prompts/README.md` |

## 已知问题

1. 193 → 55 的筛选决定、验证集的挑选规则没有记录。
2. card 的生成过程（模型、日期、批次）没有记录；V01–V05 的原始抽取版本丢失。
3. 55 张 card 都没有经过人工审核。card 内部指向原文的链接（`../notes/paper-text/…`、`../inputs/…`）在原目录里就已经失效。为了让 card 和原文件逐字节一致，这里没有修改；对应的文本在同一集合的 `text/` 下。
4. V01–V05 已经在三次测试中用过（pattern 覆盖测试、原留出测试、2026-10-28 无卡片重测），而且在 taxonomy v2.0 形成之前已经暴露。作为独立验证集已不干净，后续独立验证需要新选文章。

## 环境

- Python 3.13，pypdf 6.14.2（`pdf_to_text.py`、`build_manifest.py`）
- 运行方式：在 `01-corpus/` 目录下执行 `python tools/<script>.py`
