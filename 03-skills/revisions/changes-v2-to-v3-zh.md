# Skill v2 → v3 修改记录

日期：2026-10-28 | 状态：已修改，未测试

## 起因

第二轮测试（Opus）中，7 道题里 C 赢了 6 道，只有 U5（梯级实时决策）没有赢：一位裁判判平局，另一位判 A 小胜。

诊断依据：`07-round-02/judgments/opus/U5-j1.md`、`U5-j2.md`。

- **A 组的优势在"系统联动"**：A 把支流当作头号不确定性，并分别按支流洪水早到、同时到、晚到三种情况做了演算检查。
- **C 组的优势在"时间"**：C 算出了不可回头点。但 C 没有按情景演算，下库的库容也没有扣除支流要占用的部分。
- **根本原因在 skill 本身**：
  - 与梯级有关的 4 条检查（RP01-C、RP03-F、RP05-D、EP09-D）都标成了 "Optional"。
  - skill 里没有解释 "Optional" 是什么意思，模型只能按字面理解成"可以跳过"。
  - 第 4 步又允许整个单元被跳过，两道口子叠在一起。
  - 这些检查标成 "Optional"，原本的意思是"证据少"（来自待定或单例的小 pattern），而不是"可做可不做"。

## 修改

| 位置 | 修改内容 | 依据 |
|---|---|---|
| 11 条检查的标签 | "Optional:" 改为 "When relevant:" | **用户意见（2026-10-28）**："optional 的意思是不是每篇文章都要去思考，但是如果涉及到相关内容，是要去考虑的，而且宁可多考虑，比不考虑强" |
| How to work 第 4 步 | 单元的跳过条件加上 "when unsure, consider it briefly"；并定义 "When relevant"：不是每个案例都要用，但只要案例涉及这个内容就必须考虑，拿不准时也要考虑 | 用户意见（同上）。第 4 步的措辞由用户指定："skip units that do not apply; when unsure, consider it briefly" |
| 2.3 新增 J23 | 有不受控的支流或区间来水汇入时，是否分别演算了它早于、同时于、晚于水库下泄到达三种情况？决策在每种情况下是否都成立？ | 第二轮 opus-U5-j1（"formal scenario-routing check… tributary timing (early, coincident, late)"）、opus-U5-j2（"no structured multi-scenario routing check"） |
| 3.3 新增 J24 | 多库系统中，联合防洪库容如何在各库之间分配（各库过流多少、蓄多少）？是否在各坝自身的安全限值和坝间河道过流能力之内？ | 第二轮 opus-U5-j2（"allocation rule for the joint flood-control storage… with dam-safety limits at both dams"、"channel capacity… between the dams"）、opus-U5-j1（"flow capacity… of the channel between the dams"） |
| 标题 | v2 改为 v3 | — |

**没有改的内容**：
- 其他检查的措辞都没有动。
- 11 份 references 都没有动，已用 `diff` 核对。
- SKILL.md 从 4,307 词增加到 4,454 词。

## 测试计划（用户决定）

- **只重跑 U5**，其他 6 道题沿用第二轮的结果。
- **C 组用 v3 回答 3 次**，降低偶然性。每次都与同一份 A 答案配对，由 2 位裁判评判，共 3 × 2 = 6 份判定。
- **判定标准**：3 次中至少赢 2 次，才算修好。
- **风险**：第 4 步收紧以后，其他题的答案可能变长。这一点留给 V01–V05 最终测试来检验。
