# Standalone Paper Extraction Instructions and Template

This document is sufficient as the task-specific instruction for a sub-agent that receives one assigned paper as page-separated text. No previous conversation, E02 example, old extraction, or existing skill route is required. The completed extraction contains three substantive layers plus the supporting abstraction, evidence audit, and quality-check sections defined below; do not copy these instructions into the deliverable.

**Assignment inputs:** paper ID, page-separated paper text, output Markdown path, and output language (English unless specified). The parent agent supplies these values. Do not infer which paper to process from nearby files. The paper text itself is essential: this template is not a source of research evidence.

**Purpose:** Extract what one paper studies, its reasoning route, and its execution route within **Reservoir operation adjustment for flood risk management**. Preserve enough activity-level detail for later cross-paper synthesis of reasoning/execution patterns and a collection of reasoning and execution micro-skills. This task does not perform cross-paper synthesis, write final skills, replicate the model, or evaluate an agent.

**Scope and file ownership:** Read the assigned paper text and this template. Do not consult old extraction notes, other papers, existing RR/EX routes, or validation papers to fill gaps. Do not analyze images. Write only the assigned output. You are not alone in the workspace: do not revert others' edits or change shared templates, corpus records, other paper notes, or skill files. Do not overwrite an existing output unless the assignment authorizes revision. Follow applicable workspace instructions.

**Reading and extraction procedure:**

1. Verify the paper title and identity against the assigned text. Read the introduction, relevant methods, results, and discussion/conclusions; the abstract alone is insufficient. Record the actual page/section scope. Use only the supplied text and its page markers; if a passage is missing or ambiguous, mark it as unclear rather than guessing.
2. Identify the paper's operating problem, contribution, and method in brief. The established topic is already fixed; do not perform a new broad topic classification. A paper may support risk assessment or validation without directly proposing a new rule.
3. Reconstruct the paper-specific reasoning route: what judgments motivate its choices and why. Use logical dependencies, not merely section order. Separate author statements from your reconstruction and do not claim to recover private mental processes.
4. Reconstruct the execution route: concrete inputs, activities, outputs, checks, and dependencies. Identify loops and branches. Distinguish study setup and evaluation from recurring operational actions.
5. Embed details relevant to potential micro-skills in BOTH routes: trigger, inputs, judgment or procedure, branches when relevant, output, and checks or applicability conditions. Record the actual paper-specific mechanism rather than repeating generic field labels. Mark important missing details as unreported; do not invent them. Not every activity must become a skill.
6. Attach page/section and, when useful, figure/table/equation references to every substantive row. Summarize faithfully rather than copying long passages. Retain the difference between motivating baseline and tested comparator, hard constraints and soft targets, assumed and calibrated parameters, model risk indicators and observed outcomes, demonstrations and deployment, and sensitivity analysis and independent validation when those distinctions matter.
7. Read the completed tables against the paper once more. Correct unsupported content and numerical/definition errors before saving. If full text is incomplete or unreadable, disclose the limitation and mark the extraction partial instead of presenting it as complete.

**Granularity and length:** Layer 1 has exactly three concise rows: research object/problem, method overview, and significance. Use one or two sentences per row. Layers 2 and 3 carry the substantive detail. Each row should represent a meaningful judgment or activity with a distinct role, not every sentence or mathematical manipulation. The paper determines the number of steps. First write a coherent route narrative, then use the table to make its dependencies explicit. Keep functional abstraction separate from paper-specific realization. Include enough detail to explain what to do and what is produced without transcribing every formula.

**Self-check before delivery:**

- Research identification, three substantive layers, functional abstraction/paper-specific realization, evidence and inference audit, unresolved or unreported items, and final quality check are present in that order.
- Reasoning explains choices; execution describes concrete procedures. Their dependencies are consistent.
- Micro-skill detail is preserved in both layers without declaring a final skill collection.
- Every substantive row has traceable evidence, and inferred rationale is distinguishable from explicit statements.
- Definitions, numerical settings, and page references have been checked; unreported procedures have not been inserted as facts.
- No unsupported fixed-rule comparison, operational authorization, failure response, or universal superiority claim has been added.
- Human review remains "awaiting review" unless the parent provides actual review feedback. Self-check is not human approval.
- Save as UTF-8 and reopen the saved file. Confirm the requested language displays correctly, there are no replacement characters or runs of question marks caused by encoding loss, and the local PDF link resolves. Use a Unicode-safe writing method for Chinese; do not pass Chinese content through a shell pipeline with an unverified encoding.

**Return to parent:** Give the saved file path, reading scope, and any unresolved evidence/access issue. Stop after the assigned paper; do not begin other papers or update skills.

**Copy-ready assignment message:**

> Read and follow [absolute path to this template]. Extract paper [ID] from [absolute PDF path]. Write the three-layer note in [language] to [absolute output path]. [Create a new file / revise this specific existing file.] Use only the assigned source and template for research content. Other agents may be working in this workspace; own only this output and its paper-specific scratch files. Complete the template self-check and return the output path and any unresolved issues. Do not process other papers.

---

# [Paper ID] Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: [Authors, year, title, journal, DOI]. Source: [local PDF link]. Page references use PDF page numbers. Reading scope: [sections/pages reviewed].

## Paper identification

Title, authors, venue/year, topic relation, source-text scope, and page-reference convention.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | [System, operating problem, and decision the study supports.] | [Page, section, figure/table/equation where relevant.] |
| Method overview | [One or two sentences summarizing the main approach; leave workflow and parameters to the execution layer.] | [Location.] |
| Research significance | [Briefly explain how the study helps understand or improve flood-control operation; keep the claim within its evidence.] | [Supporting location and scope.] |

## 2. How the authors reason

Reasoning overview: [Explain the paper's decision logic in connected prose: what problem is framed, why the baseline is insufficient, what uncertainty or trade-off changes the decision, why the chosen adjustment follows, and where the claim stops.]

Reconstructed route: [Paper-specific sequence of judgments and choices, ordered by logical dependencies. Include branches or feedback where supported.]

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. [Judgment/action label] | [What the authors need to resolve, why it matters, and why they make the resulting research choice.] | **Trigger:** [When this judgment is needed.] **Inputs:** [Information required.] **Judgment/procedure:** [How information is interpreted or alternatives distinguished.] **Branches:** [Conditional choices, if reported.] **Output:** [Decision, clarification, or requirement passed to later steps.] | [Precise evidence location; identify explicit reasoning versus extractor reconstruction; conditions, checks, assumptions, and unreported details.] |
| R2. [Next dependency] | [Paper-specific reasoning.] | [Trigger, inputs, judgment, branches, and output as supported.] | [Evidence and boundaries.] |

Add, remove, or combine rows to match the paper. Do not require eight steps or fill every step of the previous pilot route. Extract reasoning details for potential small skills as well as the overall sequence; do not substitute method names for explanations of why a method is appropriate.

## 3. How the authors execute

Execution overview: [Explain the information flow and intermediate products in connected prose. Separate the main operational workflow from model setup, comparison, sensitivity, and evaluation branches.]

Reconstructed workflow: [Paper-specific activities and dependencies. State which activities repeat, branch, or belong to evaluation rather than operation.]

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. [Activity label] | [Concrete activity and its purpose. Link to the relevant reasoning step where useful.] | **Trigger:** [When needed.] **Inputs:** [Data, prior outputs, or specifications.] **Procedure:** [Actual operations, choices, branches, and parameter/threshold selection rationale.] **Output:** [Artifact or result and its downstream use.] | [How the result is checked; evidence location; assumptions, applicability, and missing implementation details. Distinguish case settings from reusable procedures.] |
| E2. [Next dependency] | [Paper-specific activity.] | [Trigger, inputs, procedure, and output as supported.] | [Checks, conditions, and evidence.] |

Add, remove, or combine rows to match the paper; do not require fifteen steps. Preserve details needed to reconstruct each potentially reusable activity without copying every equation or parameter. Use equation/table references for further detail. If parameter-selection rationale, checks, or other details are not reported, say so rather than inventing them.

Extraction conventions: Step labels and ordering are the extractor's reconstruction from identifiable evidence, not a claim about the authors' chronological mental process. Attach evidence to each entry rather than creating a fourth evidence layer. Distinguish explicit statements, performed activities, and inferred rationale. Use "not reported," "not applicable," or "unclear" accurately; absence is not contradiction. Formal direct/partial/absent support coding can be applied later against defined cross-paper patterns. Do not assume every article generates new rules, addresses every uncertainty, or covers authorization, fallback, and post-event learning. Preserve reported operational details when present.

Micro-skill convention: Capture activity-level detail in both reasoning and execution. These records are inputs to a future collection of independently callable micro-skills, not a single micro-skill or a predetermined list. Decide which activities become skills during cross-paper synthesis. A reasoning or execution activity may support multiple skills, and a skill may serve multiple route steps.

Human review: [Reviewer, date, and specific feedback or acceptance. Leave unreviewed entries marked as such.] R/E identifiers are local to this paper. Single-paper extraction does not establish recurring patterns or validate the resulting skills.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| [R/E identifier] | [General function that could recur across papers.] | [How this paper implements it; keep model names and parameters here.] |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | [What the metric actually represents.] | [What cannot be claimed.] |
| Model/simulation result versus deployment | [Supported result.] | [Deployment or real-world limit.] |
| Sensitivity/comparison versus independent validation | [What was tested.] | [What was not independently validated.] |
| Assumption versus calibration | [Reported assumptions and calibrated quantities.] | [Uncalibrated or missing details.] |
| Case result versus general rule | [Case-bounded conclusion.] | [Generalization limit.] |

## 6. Unreported or unresolved items

[List material missing procedures, parameters, evidence, or deployment details. Use “not reported,” “unclear,” or “not applicable” precisely.]

## 7. Final quality check

### Reasoning
[Confirm that the route answers why, uses functional step labels, and preserves causal dependencies and claim boundaries.]

### Execution
[Confirm that the route answers how, follows information flow, distinguishes the main workflow from evaluation branches, and records inputs, operations, outputs, and checks.]

### Evidence
[Confirm page/section traceability, explicit-versus-inferred distinction, and limits on proxy, model, sensitivity, and case claims.]

### Reusability
[State which abstractions may recur across papers and which details are paper-specific.]
