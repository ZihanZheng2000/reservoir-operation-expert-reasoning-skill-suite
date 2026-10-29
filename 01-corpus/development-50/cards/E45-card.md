# E45 Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: Xiaoqi Zhang, Pan Liu, Chong-Yu Xu, Bo Ming, Aili Xie, and Maoyuan Feng (2018), “Conditional Value-at-Risk for Nonstationary Streamflow and Its Application for Derivation of the Adaptive Reservoir Flood Limited Water Level,” *Journal of Water Resources Planning and Management*, 144(3), 04018005, DOI: 10.1061/(ASCE)WR.1943-5452.0000906. Source: [E45 source text](../text/E45.txt). Page references use the source-text page markers. Reading scope: pages 1–9, including Introduction, Methodology, optimal model, Three Gorges case study, results, discussion, and Conclusions.

## Paper identification

The paper proposes conditional value-at-risk (CVaR) for flood-damage assessment under nonstationary streamflow and applies it to adaptive flood-limited water-level (FLWL) design for China’s Three Gorges Reservoir. It compares a stationary conventional FLWL with nonstationary adaptive schemes constrained by cumulative risk and, in one scheme, multi-year CVaR.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | The study supports adaptive reservoir FLWL decisions when annual flood exceedance probabilities change over time. It seeks to increase hydropower generation without exceeding the stationary baseline’s cumulative flood-risk probability or conditional flood-damage-loss threshold. | pp. 1–4, Introduction, Methodology, and Equations (1)–(9). |
| Method overview | It defines VaR and CVaR for flood damage, derives a multi-year nonstationary CVaR by probability-weighting annual CVaR values, and embeds CVaR and cumulative-risk constraints in a nonlinear adaptive-FLWL optimization solved with NSGA-II. | pp. 2–5, Equations (3)–(12) and flowchart Figure 2. |
| Research significance | For the TGR scenario from 2020–2039, risk-only adaptation (B1) raises average annual hydropower by 6.29% but exceeds the stationary CVaR threshold; adding the CVaR constraint (B2) raises generation by 4.91% while keeping modeled cumulative risk and CVaR near or below the baseline. | pp. 6–8, Figures 5–7, Table 2, Conclusions. |

## 2. How the authors reason

Reasoning overview: The authors argue that stationary flood-risk probabilities are insufficient when streamflow is nonstationary, and that probability alone omits the magnitude of consequences. CVaR is selected to represent the expected loss in the tail beyond a confidence threshold. A stationary conventional FLWL supplies a risk and CVaR benchmark; adaptive FLWLs are then raised or lowered according to nonstationary flows, but only within cumulative-risk and loss constraints. The authors interpret CVaR as stricter than unconditional expected loss for this decision, while acknowledging a constant unit-loss-cost assumption and the case-specific scenario.

Reconstructed route: identify nonstationarity; distinguish hazard probability from consequence magnitude; define annual and multi-year CVaR; establish stationary generation/risk/CVaR benchmarks; optimize adaptive FLWL under risk alone; add CVaR as a second constraint; compare generation, risk, and loss; infer when the extra constraint changes the chosen boundary.

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. Diagnose stationarity and consequence gap | Changing climate and human activity can make flood probabilities time-varying. A threshold-exceedance probability alone does not express the size of flood damage when the threshold is exceeded. | **Trigger:** annual maximum streamflow is nonstationary or consequence magnitude matters. **Inputs:** time-varying exceedance probabilities, loss distribution, planning horizon. **Judgment/procedure:** separate flood hazard probability from damage-loss severity. **Branches:** stationary and nonstationary probability formulas. **Output:** need for a risk measure that carries tail magnitude. | pp. 1–2, Introduction and Equations (1)–(2). This is methodological motivation, not proof of a particular climate mechanism in the case. |
| R2. Choose CVaR and derive a horizon measure | CVaR is selected because it averages losses beyond VaR. Annual CVaR values are combined with the probability of an exceedance in each year to form CVaR over n years under nonstationary probabilities. | **Trigger:** compare candidate FLWLs over a planning horizon. **Inputs:** loss function, confidence level, annual probabilities, annual CVaR. **Judgment/procedure:** set alpha plus cumulative risk equal to one and use the probability-weighted formula in Equation (6). **Branches:** stationary equal-probability formula versus nonstationary time-varying formula; independent annual-event assumption. **Output:** CVaR_n alpha threshold and candidate loss measure. | pp. 2–3, Equations (3)–(6). Independence and Bernoulli occurrence assumptions are explicit; loss continuity and calibration details are limited. |
| R3. Establish a stationary benchmark | Conventional FLWL under stationary conditions provides the baseline generation, cumulative risk, and beta_n alpha CVaR threshold. This benchmark defines the maximum acceptable risk/loss for nonstationary adaptation. | **Trigger:** evaluate whether adaptation increases risk or loss. **Inputs:** observed 1882–2010 inflows, conventional operation, FLWL-performance relationship. **Judgment/procedure:** set FLWL to 145.0 m, derive annual generation and beta_n alpha at 98% confidence over 2020–2039. **Output:** Scheme A baseline. | pp. 4–6, Table 1 and Scheme A description. The benchmark is model-based and depends on observed-data generation relationships. |
| R4. Optimize adaptive FLWL with risk only | If nonstationary annual maximum means decline, higher FLWLs can increase generation while maintaining cumulative risk at or below the stationary benchmark. Scheme B1 tests this adaptive opportunity without a CVaR constraint. | **Trigger:** inflow distribution changes over time. **Inputs:** nonstationary streamflow scenario, flood routing, FLWL decision blocks, risk threshold, water balance and capacity limits. **Judgment/procedure:** use five-year blocks as decision variables and maximize average annual generation subject to cumulative risk. **Output:** B1 adaptive FLWL schedule and generation/risk/CVaR results. | pp. 4–6, Equation (8), Figure 5. The scenario is supplied in Appendix S3, not fully reproduced; B1’s loss can exceed the stationary CVaR benchmark. |
| R5. Add tail-loss protection | Because B1’s CVaR_n alpha exceeds the stationary benchmark despite satisfying probability risk, the authors add CVaR as a second constraint. This limits the boundary increase when the tail-loss consequence grows. | **Trigger:** risk probability passes but CVaR exceeds beta_n alpha. **Inputs:** B1 candidate, nonstationary CVaR, stationary beta_n alpha. **Judgment/procedure:** enforce both cumulative risk and CVaR_n alpha constraints in the same adaptive optimization. **Branches:** if B1 CVaR is already below the benchmark, B1 remains applicable; otherwise FLWL is reduced. **Output:** B2 schedule. | pp. 6–8, Equation (9), Figure 6 and Table 2. The conditional rule is explicit; practical loss valuation remains dependent on a constant unit cost. |
| R6. Interpret the stricter metric and claim scope | The comparison with unconditional expected value suggests CVaR is more sensitive to FLWL changes at high confidence. The authors conclude that CVaR gives a more reliable constraint for this nonstationary adaptive-FLWL problem. | **Trigger:** choose a risk metric for adaptive operation. **Inputs:** B1/B2 expected loss, CVaR, generation, risk trajectories. **Judgment/procedure:** compare metrics and inspect whether the loss threshold is exceeded. **Output:** preference for CVaR-constrained adaptation in this case. | pp. 7–8, Figure 7 and Conclusions. No observed damage validation or deployment study establishes universal superiority. |

## 3. How the authors execute

Execution overview: The authors define stationary and nonstationary exceedance probabilities, a flood-damage loss function, annual CVaR, and a horizon CVaR. They use observed TGR data to establish the FLWL-to-generation relationship and a conventional benchmark. Nonstationary scenarios are routed through the reservoir model while NSGA-II searches five-year-block FLWL decisions under water-balance, storage, release, cumulative-risk, and optionally CVaR constraints. They then compare Scheme A, B1, and B2 by FLWL, hydropower generation, cumulative flood risk, CVaR, and unconditional expected loss.

Reconstructed workflow: define probability/loss measures -> calculate stationary baseline -> generate nonstationary inflow scenario -> optimize B1 -> calculate CVaR and compare to baseline -> optimize B2 with both constraints -> compare outputs and limitations.

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. Define probability and loss measures | They formulate stationary risk as 1 minus the probability of no exceedance over n years and nonstationary risk as the sum of first-exceedance probabilities. VaR is the loss threshold and CVaR is the expected loss beyond it. | **Trigger:** quantify risk over a design life. **Inputs:** annual exceedance probabilities, loss distribution, confidence alpha. **Procedure:** apply Equations (1)–(5) and set alpha + R = 1. **Output:** annual risk, VaR, CVaR, and confidence-linked loss thresholds. | pp. 2–3. The derivation assumes independent annual events; the supplied text does not provide a full empirical damage calibration. |
| E2. Aggregate CVaR over the planning horizon | For n years, the authors combine annual CVaR values weighted by each year’s exceedance probability and normalize by cumulative risk. | **Trigger:** compare candidate FLWL schedules over multiple years. **Inputs:** p_i, annual CVaR_i, cumulative risk R. **Procedure:** use Equation (6) under stationary or nonstationary probability sequences. **Output:** CVaR_n alpha. | p. 3, Equation (6). Independence and Bernoulli occurrence assumptions are stated; dependence and time-varying loss-cost uncertainty are not modeled. |
| E3. Establish Scheme A | Using observed TGR inflows from 1882–2010 and conventional generation operation, they tabulate average annual generation for FLWLs 140–155 m and select 145 m as the conventional baseline. They derive beta_n alpha = 33.06 c billion yuan at 98% confidence over 2020–2039 and stationary cumulative risk 1.98%. | **Trigger:** create the comparison benchmark. **Inputs:** observed inflows, conventional FLWL, generation operation, loss function. **Procedure:** route/operate the reservoir for the FLWL and calculate generation and CVaR. **Output:** Scheme A generation, risk, and beta threshold. | pp. 5–6, Table 1 and Figure 4. The unit cost c is treated as constant; Appendix loss-function details are not in the supplied text. |
| E4. Build and route nonstationary scenarios | They use a nonstationary annual-maximum streamflow scenario for 2020–2039 and treat each consecutive five-year period as one FLWL decision variable. | **Trigger:** adapt FLWL to changing inflow. **Inputs:** scenario inflows, initial/physical reservoir conditions, five-year decision blocks. **Procedure:** route each candidate FLWL schedule and compute annual generation and first-exceedance risk. **Output:** nonstationary risk and generation for candidate schedules. | pp. 4–6, Figure 5. Scenario-generation details are in Appendix S3 and are not fully reproduced; exact optimization settings are not reported. |
| E5. Solve B1 risk-constrained adaptation | NSGA-II searches for the adaptive schedule maximizing mean annual generation while enforcing cumulative nonstationary risk no greater than the stationary benchmark, plus water balance, storage, and release limits. | **Trigger:** obtain an adaptive schedule under probability protection. **Inputs:** candidate FLWL blocks, routed flows, Equation (8), Equations (10)–(12). **Procedure:** evaluate objective and constraints for candidate schedules; retain a B1 solution. **Output:** FLWLs 147.4, 148.4, 149.7, and 151.5 m for 2020–2024 through 2035–2039; generation +6.29%, risk 1.94%, CVaR_n alpha 33.13 c billion yuan. | pp. 5–7, Figure 5 and Table 2. B1 meets probability restriction but exceeds Scheme A CVaR; this is the key diagnostic. |
| E6. Solve B2 with CVaR protection | They add Equation (9) to B1’s constraints and solve the same adaptive problem. | **Trigger:** B1’s tail loss is above the stationary threshold. **Inputs:** B1 route, beta_n alpha, nonstationary CVaR, probability and physical constraints. **Procedure:** retain only schedules satisfying both risk and CVaR limits. **Output:** FLWLs 145.3, 147.3, 149.3, and 151.4 m; generation +4.91%, risk 1.939%, CVaR_n alpha 33.05 c billion yuan. | pp. 6–8, Figure 6 and Table 2. Results are model outputs for the chosen scenario and confidence level. |
| E7. Compare metrics and infer operating implication | They compare CVaR, unconditional expected loss, risk probability, FLWL, and generation across Schemes A, B1, and B2. | **Trigger:** select the adaptive operating design and risk metric. **Inputs:** Figures 5–7 and Table 2. **Procedure:** inspect whether each schedule passes both baseline thresholds and quantify generation changes. **Output:** conclusion that CVaR is a stricter/useful constraint for this case. | pp. 7–8. No observed post-event damage, field adoption, or independent validation is reported. |

Extraction conventions: Step labels and ordering are the extractor's reconstruction from identifiable evidence, not a claim about private author cognition. Explicit formulas and performed optimization are distinguished from inferred rationale.

Micro-skill convention: The entries preserve activity-level details for later cross-paper synthesis; they do not declare a final skill collection.

Human review: Awaiting review; no external reviewer feedback was supplied.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| R1–R2 / E1–E2 | Convert time-varying exceedance and tail loss into a horizon risk metric. | Nonstationary first-exceedance probabilities and probability-weighted CVaR_n alpha are derived. |
| R3 / E3 | Establish a stationary performance and risk benchmark. | TGR FLWL 145.0 m, 1882–2010 observed inflows, 2020–2039 beta threshold. |
| R4–R5 / E4–E6 | Optimize adaptive operating boundaries under nested safety constraints. | NSGA-II searches five-year FLWL blocks under risk, CVaR, water-balance, storage, and release limits. |
| R6 / E7 | Compare tail-risk and expected-loss metrics before selecting a policy. | B1 versus B2 shows probability-only adaptation can exceed the stationary CVaR threshold. |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | CVaR is a modeled flood-damage-loss measure; risk probability, generation, and FLWL are modeled decision outputs. | No observed flood damages, actual economic losses, or public safety outcomes are validated. |
| Model/simulation result versus deployment | Reservoir routing and optimization produce scenario comparisons. | No adaptive FLWL deployment or real-time operational test is reported. |
| Sensitivity/comparison versus independent validation | Schemes A, B1, and B2 and expected-loss/CVaR comparisons are performed. | This is not independent validation of nonstationary scenarios, loss functions, or NSGA-II solutions. |
| Assumption versus calibration | Observed inflows underpin the generation relationship; independent annual events, Bernoulli occurrence, and a constant unit loss cost are assumed. | Loss-cost calibration and dependence/nonstationarity-model validation are unreported. |
| Case result versus general rule | The CVaR-constrained adaptive-FLWL logic is a transferable formulation. | Numerical gains and threshold behavior are specific to TGR, the selected scenario, confidence level, and 2020–2039 horizon. |

## 6. Unreported or unresolved items

- Nonstationary scenario-generation details are delegated to Appendix S3 and are not fully present in the supplied text.
- The flood-damage loss-function construction and unit cost are not fully reproduced; the unit cost is assumed constant.
- NSGA-II population, stopping, constraint-handling, and reproducibility settings are not reported.
- Dependence among annual flood events and uncertainty in nonstationary parameter estimates are not evaluated.
- CVaR is validated against modeled loss, not observed flood damage or deployment outcomes.

## 7. Final quality check

### Reasoning
The route explains why nonstationary probability and tail loss require separate controls, how the stationary benchmark is used, and why adding CVaR changes the adaptive boundary.

### Execution
The route follows probability/loss definitions through baseline construction, scenario routing, B1/B2 optimization, and metric comparison, with the optimization and interpretation branches separated.

### Evidence
Page, equation, figure, and table references are attached to substantive claims; CVaR and risk are kept as model measures rather than observed consequences.

### Reusability
Reusable abstractions include horizon risk construction under nonstationarity, stationary-baseline calibration, nested probability/tail-loss constraints, and adaptive boundary optimization. The TGR data, loss units, confidence level, scenario, and numerical FLWLs are paper-specific.
