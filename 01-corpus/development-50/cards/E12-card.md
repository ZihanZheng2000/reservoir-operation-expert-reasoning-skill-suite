# E12 Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: Wei, G., Liang, G., Ding, W., He, B., Wu, J., Ren, M., & Zhou, H. (2022), “Deriving optimal operating rules for flood control considering pre-release based on forecast information,” *Journal of Hydrology*, 615, 128665, DOI: 10.1016/j.jhydrol.2022.128665. Source: [E12.txt](../text/E12.txt). Reading scope: pp. 1–13, §§1–5 and supplied supplementary references.

## Paper identification

The paper develops a three-part framework for Nierji Reservoir: forecast-based early pre-release, multi-objective flood-control optimization including downstream resilience, and fuzzy optimum selection under forecast uncertainty and decision-maker preferences. It compares distribution-based uncertainty treatment with maximum/minimum-error rules and tests 1969 and 2013 flood hydrographs.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | Pre-release can enlarge flood-control capacity but over-release under uncertain forecasts can create water-shortage risk. Peak-only objectives also miss damage duration and system recovery. | pp. 1–3, §1. |
| Method overview | Identify forecast-error distribution, compute early pre-release to restore FLWL if no flood occurs, optimize peak level/flow and downstream resilience, then use fuzzy selection to choose satisfactory rules. | pp. 2–6, §§2.1–2.4. |
| Research significance | At Nierji, recommended pre-release rules spread releases, reduce downstream peak/risk, and improve modeled resilience without increasing reservoir risk; results are case-based and data are confidential. | pp. 9–12, §§4–5. |

## 2. How the authors reason

Reasoning overview: A forecast distribution is more representative than optimizing only perfect or extreme forecasts. Pre-release should be large enough to create space yet allow refilling to FLWL if the flood does not materialize. Flood damage is represented as a process, so resilience joins peak reservoir level and downstream flow as an objective. Because objectives conflict and preferences vary, Pareto solutions are filtered with fuzzy selection; the claim ends at simulated safety and resilience.

Reconstructed route: identify early pre-release trigger and restoration constraint; estimate forecast error distribution; formulate multi-objective operation and resilience metric; generate Pareto rules; evaluate forecast uncertainty and decision-maker preferences; select recommended rule; simulate representative/extreme forecast errors and compare traditional framework.

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. Define forecast-informed pre-release decision | Pre-release increases flood space but its uncertainty creates conservation risk. | **Trigger:** Forecast inflow is in early-flood discriminant range Qdown–Qup. **Inputs:** Forecast inflow, current storage, FLWL, minimum downstream demand. **Judgment/procedure:** Release now while requiring future inflow plus minimum-demand balance to restore FLWL if no flood occurs. **Branches:** Pre-release versus later detention when forecast exceeds Qup; potential restore if no flood. **Output:** Feasible early release. | §§2.1–2.2, pp. 2–4, Eqs. (1)–(5). Exact Qdown/Qup calibration is case-specific. |
| R2. Represent forecast uncertainty by its distribution | Maximum/minimum-error rules are safe but optimize rare extremes; distribution-based rules target the most probable forecast and assess the remaining risk. | **Trigger:** Need an operating rule under uncertain forecasts. **Inputs:** Forecast errors. **Judgment/procedure:** Fit maximum-entropy error distribution; identify mode δ0 and 99.99% interval δmin–δmax. **Output:** Forecast scenarios for optimization/evaluation. | §2.1, pp. 3 and 10–12. Distribution fitting details/data are limited in supplied text. |
| R3. Include process resilience in the objective | Flood damage depends on magnitude and duration, so minimizing only peak values is incomplete. | **Trigger:** Optimize flood-regulating stage. **Inputs:** Downstream flow time series, Qmin/Qmax, reservoir levels. **Judgment/procedure:** Define piecewise system performance and integrate it over the event; maximize resilience while minimizing maximum level and downstream peak. **Output:** Three-objective optimization problem. | §§2.3.1, pp. 4–5, Eqs. (6)–(10). Resilience is a modeled index, not observed damage. |
| R4. Resolve conflicting objectives/preferences | No single Pareto point is universally best; decision-maker priorities select among feasible rules. | **Trigger:** Pareto set generated. **Inputs:** Objective values, binary-contrast weights, preferences, forecast uncertainty. **Judgment/procedure:** Normalize objective values, apply fuzzy optimum selecting, and choose satisfactory rules (Q, Z, QZR, QZ, CFB variants). **Output:** Recommended operating rule(s). | §§2.3.2–2.4, pp. 5–6, Tables 3–4. Preference weights and fuzzy formulas are partly in supplement. |
| R5. Check safety and transfer limits | A chosen rule must be safe under forecast errors and show benefit versus current/traditional approaches. | **Trigger:** Validate recommendation. **Inputs:** Nierji design floods, observed 1969/2013 hydrographs, DBM forecasts, ±22%/19% errors, baselines. **Judgment/procedure:** Simulate level, downstream flow, flood duration/resilience and compare frameworks. **Output:** Case-bounded rule assessment. | §§3–5, pp. 7–12. Single-reservoir scope and multi-reservoir limitations are explicit. |

## 3. How the authors execute

Execution overview: The framework first estimates forecast error, computes pre-release by a water-balance restoration equation, and then optimizes operation over designed flood hydrographs with three objectives. Pareto solutions are normalized/weighted and fuzzily selected. The selected rules are simulated for Nierji design and historical flood hydrographs, under DBM/perfect/extreme error forecasts, and compared with no-pre-release and traditional extreme-error frameworks.

Reconstructed workflow: identify error distribution → determine pre-release trigger/volume → generate Pareto operation rules → fuzzy-select by preferences → run forecast-error and historical-event simulations → compare peak, resilience, risk, and release trajectories.

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. Fit forecast-error distribution | Use maximum entropy to characterize forecast errors. | **Trigger:** Before forecast-informed optimization. **Inputs:** Forecast/observed errors. **Procedure:** Estimate distribution, modal error, and 99.99% standard interval. **Output:** δ0, δmin, δmax scenarios. | §2.1, p. 3. Exact data and fit diagnostics are not fully supplied. |
| E2. Calculate early pre-release | Enlarge flood-control storage with an FLWL restoration safeguard. | **Trigger:** Forecast inflow lies between Qdown and Qup. **Inputs:** V(t), forecast inflows over T, FLWL storage, minimum downstream demand, Δt. **Procedure:** Use Eqs. (1)–(5) to select Qout(t); if no future flood, future inflow minus minimum demand restores VFLWL. **Output:** Pre-release volume and state. | §§2.2, pp. 3–4. Trigger thresholds and all constraints are case-specific. |
| E3. Optimize flood-regulating trajectories | Generate Pareto rules for upstream/downstream safety and resilience. | **Trigger:** Flood-regulating stage after pre-release. **Inputs:** Designed flood hydrographs, reservoir balance, downstream flow. **Procedure:** Minimize average maximum reservoir level and downstream peak, maximize integrated performance resilience; use decision variables for release/storage over six design periods. **Output:** Pareto solution set. | §§2.3, pp. 4–6, Eqs. (6)–(10). Optimization details/solver are incompletely reported in supplied text. |
| E4. Select preferred rules | Convert Pareto outcomes into preference-sensitive recommendations. | **Trigger:** Pareto set available. **Inputs:** Objective matrix, binary-contrast weights, decision-maker preferences, forecast-error scenarios. **Procedure:** Normalize objectives and apply fuzzy optimum selection; retain QZR, QZ, Q, Z, and CFB variants as relevant. **Output:** Recommended rule set. | Tables 3–4, pp. 9–10; supplementary details are referenced. |
| E5. Simulate and compare | Run rules under typical/extreme forecasts and historical hydrographs. | **Trigger:** Assess safety and practical performance. **Inputs:** Nierji 1969/2013 floods, DBM forecast, perfect forecast, ±22%/19% errors, baselines CB/CS and traditional framework. **Procedure:** Route releases and calculate maximum level, downstream peak/duration, resilience, and relative superiority. **Output:** Hydrographs and comparative metrics. | §§4.1–4.3, pp. 9–12. Authors report acceptable modeled safety, but no independent deployment validation. |

Extraction conventions: Ordering is the extractor’s reconstruction. The framework generates operating rules and simulated decisions; it does not document live authorization, fallback, or operator interaction procedures.

Micro-skill convention: Triggers, inputs, procedures, branches, outputs, checks, and assumptions are retained for later synthesis.

Human review: Awaiting review; no reviewer/date/feedback supplied.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| R1/E2 | Use forecast-triggered pre-release with a no-flood restoration constraint. | Nierji Qdown/Qup trigger and Eq. (4) release. |
| R2/E1 | Represent forecast uncertainty by a distribution and selected quantiles. | Maximum-entropy δ0 and 99.99% interval; comparison with ±22%/19% extremes. |
| R3/E3 | Optimize safety and process resilience jointly. | Maximum reservoir level, downstream peak, integrated performance resilience. |
| R4/E4 | Select an operational rule from conflicting Pareto objectives using preferences. | Fuzzy optimum selection and Q/Z/QZR/QZ/CFB rules. |
| R5/E5 | Stress-test and compare selected rules with baselines. | Nierji 1969/2013 and DBM/perfect/error forecasts. |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | Peak levels/flows, flood duration, performance-based resilience, and relative superiority are modeled indicators. | No observed damage, levee failure, or direct economic/ecological consequence is measured. |
| Model/simulation result versus deployment | Rules are simulated for Nierji hydrographs. | Data are confidential and no live operator deployment is reported. |
| Sensitivity/comparison versus independent validation | Error-distribution versus extreme-error framework, historical hydrographs, forecast variants, and Pareto/pre-release comparisons are included. | These do not constitute independent operational validation. |
| Assumption versus calibration | Maximum-entropy error fit, thresholds, objective weights, system-performance bounds, and forecast scenarios are assumptions/settings or fitted quantities. | Full data, calibration, and preference elicitation details are incomplete. |
| Case result versus general rule | Pre-release plus resilience objective improved modeled safety/utilization for Nierji. | Multi-reservoir transfer requires correlation, hydraulic connection, and capacity compensation treatment. |

## 6. Unreported or unresolved items

- Exact forecast-error samples, maximum-entropy fit, Qdown/Qup thresholds, model constraints, solver settings, and Pareto-generation details are incomplete.
- Fuzzy-selection formulas and preference weights partly rely on supplementary material not supplied in full.
- Resilience thresholds Qmin/Qmax and mapping to real damage are not empirically validated.
- Handling of forecast updates, failed forecasts, infeasible releases, missing data, and operator overrides is not reported.
- Data are confidential; no independent out-of-sample operational validation is available.

## 7. Final quality check

### Reasoning
The route explains why distributional uncertainty, early pre-release, process resilience, and fuzzy preference selection are combined.

### Execution
The route follows error fitting through release calculation, Pareto optimization, fuzzy selection, and forecast/historical simulations.

### Evidence
Rows cite supplied pages/equations/tables and distinguish resilience proxies, modeled scenarios, assumptions, and deployment limits.

### Reusability
Potential abstractions include restoration-constrained prerelease, error-distribution scenario generation, resilience-aware multi-objective optimization, preference-sensitive rule selection, and extreme-forecast stress tests. Nierji thresholds, data, weights, and rules are paper-specific.

