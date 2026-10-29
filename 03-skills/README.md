# 03 - Skills：从 pattern 写成 skill

**输入**：`../02-patterns/` 定稿的 taxonomy（9 个推理 pattern、11 个执行 pattern、104 个小 pattern）、步骤清单和合并顺序。

**最终产物**：[`reservoir-flood-expert/`](reservoir-flood-expert/) —— skill v3，2026-10-29 由用户确认定稿。它与最终测试冻结的版本逐字节相同（`../04-evaluation/03-final-test/skill-tested.sha256`）。

**来源**：工作在 `artifacts/run-20261028-v3-rebuild/work/` 中完成（`03-skill-v1`、`06-skill-v2`、`08-skill-v3`）。这里只放定稿版本和修订记录；v1、v2 的全文留在 run 里。

## 结构

```
reservoir-flood-expert/
├─ SKILL.md        四段流程，共 11 个单元。每个单元包含：
│                  Think（推理大 pattern 的共同问题）、Do（执行大 pattern 的共同任务）、
│                  Checks（疑问句形式）、Details（链接到对应的 references 文件）
└─ references/     每个单元一份，内容是论文实际怎么做的，每句话都标注步骤 ID
```

- **四段**：界定问题 → 认识不确定性与预报 → 设计并计算方案（先判断后计算，可反复）→ 检验。来自 `../02-patterns/04-ordering/` 的合并顺序分析。
- **Checks 有两类**：
  - **pattern 来源的检查**：104 条，一个小 pattern 对应一条，标注 RP/EP 编号。其中 11 条证据较少（待定或单例），标为 "When relevant"：并非每个案例都需要，但只要涉及相关内容就必须考虑。
  - **测试修订的检查**：标注 J01–J24，其中新增 23 条，SKILL.md 中检查总数因此为 127 条。J11 不是新增的一条，而是对 RP07-E 的修改：由可选改为必选，并补上中止规则。这些检查都是在裁判或用户提出意见之后才加入的，每条的出处都记录在 `revisions/` 中。
- **原则（用户决定）**：
  - skill 只写 pattern 推导出来的东西；
  - 其他内容只有在裁判提出意见、或用户给出意见之后才加入；
  - agent 先用自己的专业判断推理，skill 只起补充和核对的作用。

## 怎么生成的

| 步骤 | 文件 | 方法 | 能否复现 |
|---|---|---|---|
| ① 单元证据包 | `evidence/`、`build_unit_evidence.py` | 把每个单元下各小 pattern 分到的全部论文步骤，连同 card 中的完整文本，汇集成一个证据包。11 个单元共 1,074 条 | **能**。2026-10-29 在 v3 中重跑，结果与原证据包完全一致 |
| ② references | `prompts/write-unit-reference.md` | 每个单元交给一个 Claude Opus 5.5 子代理（2026-10-28），它只读这份提示词和本单元的证据包。要求每句话都标注步骤 ID，不加入模型自己的知识 | 不能逐字复现。`check_references.py` 核对通过：小 pattern 全覆盖，所有引用都在证据包内 |
| ③ SKILL.md v1 | — | 由主会话按 pattern 编写。Think 和 Do 直接使用大 pattern 原文；Checks 由小 pattern 的名称和描述改写成疑问句 | 文档 |
| ④ v1 → v2 | `revisions/changes-v1-to-v2-zh.md` | 依据第 1 轮测试中 Opus 和 Sonnet 的裁判意见，以及用户的决定。How to work 从 6 步改为 10 步，新增 3 类题型的写法，新增 J 检查 | 修改记录 |
| ⑤ v2 → v3 | `revisions/changes-v2-to-v3-zh.md` | "Optional" 改为 "When relevant"，并修改第 4 步（用户意见）；依据第 2 轮 U5 的裁判意见新增 J23、J24 | 修改记录 |

**修订相关的其他文件**：
- `revisions/round-01-judge-extraction-opus-sonnet.md`：v2 修改所依据的裁判证据整理。
- `revisions/human-review-notes-zh.md`：人工审核改变了 skill 的两个例子（J13 的防洪库容；"Optional" 的含义），可以用在汇报中。

## 复现

```bash
python build_unit_evidence.py     # 重新生成 evidence/
python check_references.py        # 核对 references 与证据包
```

## 已知缺口

- **J02 的公式会被套错**。J02 写的是等相关误差之和的方差：nσ²(1+(n−1)ρ)。最终测试中，C 组把它用在逐时自相关的误差上，夸大了累积误差（V03-D、V04-S、V04-D）。按测试方案定稿后不再修改；如果再迭代，应改为"按误差的实际自相关结构计算"。
- **skill 没有提高对论文方法路线的覆盖（RC）**。它教的是专家流程和把关，没有教方法层面的提问。候选的补充方向见 `../04-evaluation/03-final-test/rc-analysis-zh.md` 第 5 节。这些候选来自留出论文，如果采用，需要另找新的留出论文来测试。
