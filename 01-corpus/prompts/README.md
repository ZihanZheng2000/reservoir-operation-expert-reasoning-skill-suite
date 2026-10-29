# Paper card 提示词

## 文件

| 文件 | 内容 |
|---|---|
| [`card-prompt-en.md`](card-prompt-en.md) | 英文版抽取指令与模板。自包含：子代理只需要这份文件和一篇论文文本就能工作。55 张 card 都是英文的，结构与这份模板一致。 |
| [`card-prompt-zh.md`](card-prompt-zh.md) | 中文版，内容对应。 |

原位置：`artifacts/run-20260914-0925-50paper-patterns/01-corpus/development-50/templates/paper-extraction-template{,-zh}.md`，内容未改，只改了文件名。

## 怎么用

派给子代理的消息（摘自 `card-prompt-en.md` 末尾的 "Copy-ready assignment message"，方括号内替换为实际值）：

> Read and follow [absolute path to card-prompt-en.md]. Extract paper [ID] from [absolute path to the paper text or PDF]. Write the three-layer note in English to [absolute output path]. Create a new file. Use only the assigned source and template for research content. Other agents may be working in this workspace; own only this output and its paper-specific scratch files. Complete the template self-check and return the output path and any unresolved issues. Do not process other papers.

一篇论文一个子代理，互不共享上下文。模板要求只用该论文的文本，不看其他论文、旧抽取或 skill。

## 产出结构

一张 card 依次包括：论文识别、第 1 层（研究对象、方法概述、意义三行）、第 2 层推理路线、第 3 层执行路线、功能抽象与论文具体实现、证据与推断审计、未解决或未报告事项、最终质量检查。

## 可复现性缺口

- 生成这 55 张 card 时用的**模型、日期和派发方式没有记录**。只有 E01–E07 写了日期（2026-09-17）。
- card 头部格式有约 5 种（E01；E02–E07；E08–E22 和 E43–E50；E23–E42 和 V02–V05；V01），说明是分几批生成的，但批次和顺序没有记录。
- 原 held-out README 说 V01–V05 有"未提供 frozen patterns 时的原始抽取"（`raw-extractions/`），但这个文件夹不存在。现有 V 的 card 是"经过格式与一致性处理的正式抽取"，处理了什么没有记录。
- 所有 card 的人工审核状态都是 "awaiting review"，没有人工审核过。
- 模板的开发过程（E02 试做、两次 Luna 测试、人工审阅）保存在 `artifacts/run-20260914-0925-50paper-patterns/_archive/extraction-development-history/`，没有复制过来。

如果要完全可复现，建议用这份提示词、固定模型和固定日期重新生成 55 张 card，并记录每次派发。
