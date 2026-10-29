# E10 Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: Wang, J., Zhao, T., Zhao, J., Wang, H., & Lei, X. (2021), “Improving real-time reservoir operation during flood season by making the most of streamflow forecasts,” *Journal of Hydrology*, 595, 126017, DOI: 10.1016/j.jhydrol.2021.126017. Source: [E10.txt](../text/E10.txt). Reading scope: pp. 1–13, §§1–5 and Appendix.

## Paper identification

The paper defines a reliable forecast horizon (RFH) and develops a three-stage operation rule (Three-OR) for Wan’an Reservoir. It allocates flood-control storage across current, short-term reliable, and uncertain mid-term stages by minimizing dependent levee-failure risk, then uses nested KKT allocations for the current release. Results use 12 floods with 6-hour operation intervals.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | Multipurpose flood operation must balance levee safety with hydropower/water capture while forecast uncertainty grows with lead time. Existing one-/two-stage rules treat the whole forecast too uniformly. | pp. 1–3, §1. |
| Method overview | RFH separates nowcast, short-term, and mid-term uncertainty; a convex three-stage risk optimization allocates storage, with an inner two-stage KKT rule selecting current versus near-future release. | pp. 2–7, §§2.1–2.4. |
| Research significance | In Wan’an simulations, Three-OR reduced releases above the 8,800 m³/s flood-conveyance capacity to zero for all 12 floods while increasing average generation versus current operation; conclusions depend on assumed forecast-error model and human correction. | pp. 7–11, §§3–5. |

## 2. How the authors reason

Reasoning overview: Forecast sources have different uncertainty and usable horizons, so allocating storage requires recognizing stage-specific risk. The model minimizes the probability of cumulative dependent levee failure, treating the current stage’s failure as affecting later stages. Convexity permits KKT conditions to turn marginal-risk comparisons into endpoint or interior allocations. The paper frames Three-OR as a decision-support rule; the RFH threshold (20% relative error) is acknowledged as non-authoritative.

Reconstructed route: distinguish forecast stages and define RFH; model forecast-error uncertainty and downstream failure risk; allocate storage between RFH and outer stage; allocate RFH storage between current and second stage; branch on KKT boundary/interior conditions and on detention versus prerelease sign; apply physical constraints repeatedly; compare rules, error scenarios, RFH lengths, and flood patterns.

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. Separate forecast stages by reliability | Nowcasts are shortest but most reliable; mid-term forecasts extend horizon but carry greater uncertainty. A single stationary error assumption discards useful information. | **Trigger:** Choose operation horizon and uncertainty model. **Inputs:** Historical forecast errors and lead times. **Judgment/procedure:** Define RFH where nowcast/short-term relative error is generally <20%; divide current, second, and third stages. **Output:** Stage-specific uncertainty coefficients and horizon. | §§2.1–2.2, pp. 2–4. 20% threshold is explicitly a paper choice and not authoritative (p. 11). |
| R2. Formulate dependent flood-risk objective | Storage should be allocated to minimize total downstream levee-failure probability, accounting for survival through earlier stages. | **Trigger:** Optimize flood-control storage allocation. **Inputs:** Forecast releases/inflows, intermediate flow, FCC, Gaussian error σ, FLWL/MWL/end storage. **Judgment/procedure:** Use R1+(1−R1)R2+(1−R1)(1−R2)R3; treat catastrophic damage as fixed, so probability substitutes for economic loss. **Output:** Convex three-stage allocation problem. | Eqs. (1)–(7), pp. 3–5. Fixed damage and Gaussian error are assumptions. |
| R3. Allocate storage across RFH and outside RFH | Relative marginal risk indicates whether storage should be moved earlier or later, subject to FLWL/MWL bounds. | **Trigger:** Solve outer two-stage model. **Inputs:** s12, s3, stage risks and densities, storage bounds. **Judgment/procedure:** Apply KKT; if lower bound active, allocate more to later stage; if upper bound active, allocate all available to RFH; otherwise equalize marginal risks. **Output:** s12 and s3. | §§2.3.2, pp. 5–6, Eqs. (11)–(16). KKT sufficiency follows stated convexity. |
| R4. Allocate RFH storage to current action | Within RFH, current versus second-stage risk determines detention or prerelease allocation. | **Trigger:** Outer allocation is available at each operation time. **Inputs:** s12, current/second forecast flows, risk densities. **Judgment/procedure:** For s12≥0, allocate detention under KKT; for s12<0, allocate prerelease; endpoint branches select stage with larger marginal risk, interior branch equalizes it. **Output:** s1 and s2, especially current s1. | §2.3.3, pp. 5–7, Eqs. (17)–(25). |
| R5. Recompute and adapt through flood | A one-step release is selected from the current allocation and then recomputed as new information arrives. | **Trigger:** Each 6-hour operation interval until flood ends. **Inputs:** Current state, s1, physical FLWL/MWL/spill constraints. **Judgment/procedure:** Calculate release via routing and constraints; advance to next operation. **Output:** Release/storage trajectory. | §2.4, p. 7, Fig. 4. Human correction of release fluctuations is mentioned (p. 9). |
| R6. Evaluate by safety/utilization trade-off | Compare FCC exceedance and generation across operation rules and perturbations to determine where stage-aware forecasts help. | **Trigger:** Validate proposed rule in case simulation. **Inputs:** 12 floods, COR, Two-OR, forecast-error scenarios, RFH lengths, amplified floods. **Judgment/procedure:** Compare peak/volume types, error differences, RFH extension, and baseline rules. **Output:** Case-bounded performance findings. | §§3–5, pp. 7–11. No independent deployment validation. |

## 3. How the authors execute

Execution overview: Historical forecast-error coefficients define a piecewise uncertainty curve and RFH. At each 6-hour step, the outer optimization allocates storage between RFH and stage 3; the inner optimization allocates RFH storage between current and stage 2; routing converts current storage into release under FLWL, MWL, and spill constraints. The process repeats until each flood ends, then is compared with COR/Two-OR and sensitivity scenarios.

Reconstructed workflow: estimate stage errors/RFH → calculate stage risk distributions → solve outer KKT → solve inner KKT → route and release → roll forward → aggregate FCC exceedance and generation → compare scenarios/rules.

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. Define RFH and uncertainty | Set RFH=24 h (K=4 at 6-hour operation) and coefficients a0=.1, a1=.2, b0=.008. | **Trigger:** Configure Three-OR. **Inputs:** Historical forecast errors. **Procedure:** Use piecewise σ(t)=a(t)Qin(t), with current/second/third stage coefficients. **Output:** Stage uncertainty and risk distributions. | Table 1, pp. 3–4, 7. Forecast errors are assumed normal; intermediate inflow is roughly considered. |
| E2. Solve outer allocation | Allocate storage to RFH versus stage 3. | **Trigger:** Start each release decision. **Inputs:** Forecast sums, FCC, intermediate flows, σd12/σd3, S0/Slim/Smax/Send. **Procedure:** Minimize dependent risk; apply KKT boundary/interior conditions. **Output:** s12 and s3. | Convexity is asserted/proved in Appendix; equations 11–16 and constraints 13. |
| E3. Solve inner allocation | Determine current-stage flood-control storage and release/pre-release. | **Trigger:** Outer solution available. **Inputs:** s12 and current/second flow forecasts. **Procedure:** Minimize R1+(1−R1)R2; branch s12≥0 detention versus s12<0 prerelease; use KKT marginal-risk rules. **Output:** s1, s2 and current action. | Eqs. 17–25, pp. 5–7. Second-stage storage is averaged conservatively across intervals. |
| E4. Route and update | Convert current storage allocation into physical release and next state. | **Trigger:** Current s1 selected. **Inputs:** Reservoir balance, FLWL 85 m, EWL 88 m, MWL 93.6 m, spill capacity, maximum hydropower discharge 2,800 m³/s. **Procedure:** Route inflow and release; enforce physical constraints; repeat until flood ends. **Output:** Storage/release hydrograph. | Fig. 4 and Table 1. Some routing/intermediate-flow details are simplified. |
| E5. Compare operation rules | Evaluate 12 typical Wan’an floods. | **Trigger:** Completed trajectories. **Inputs:** COR, Two-OR, Three-OR, FCC 8,800 m³/s, generation. **Procedure:** Compute FCC exceedance frequency and power generation; inspect release/water-level plots. **Output:** Rule comparison. | Three-OR average FCC exceedance 0% versus COR 11.11%; generation 187.94 versus 175.95 kW·h (Table 5, pp. 8–11). |
| E6. Stress forecast and horizon choices | Test forecast-error differences, RFH 30/36/60 h, amplified floods, and flood-pattern groups. | **Trigger:** Assess sensitivity and applicability. **Inputs:** Scenario coefficient sets, altered RFHs, 1.5× floods, 12 flood shapes. **Procedure:** Recalculate operations and compare safety/utilization. **Output:** Conditional guidance: RFH extension helps large-flood control, otherwise utilization. | §§4.1–4.4, pp. 9–11. Scenarios are model sensitivity/comparison, not independent validation. |

Extraction conventions: Ordering is the extractor’s reconstruction. Three-OR is simulated decision support; operator correction, missing-data response, and deployment authorization are not specified.

Micro-skill convention: Both routes preserve triggers, inputs, procedures, branches, outputs, checks, and assumptions for later synthesis.

Human review: Awaiting review; no reviewer/date/feedback supplied.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| R1/E1 | Segment forecasts by reliability and express lead-time uncertainty. | 24-h RFH, three stages, piecewise normal error coefficients. |
| R2–R4/E2–E3 | Allocate shared flood storage by dependent marginal risk under bounds. | Nested outer/inner KKT optimization; detention/prerelease sign branches. |
| R5/E4 | Apply a rolling short-horizon action under physical constraints. | 6-hour Wan’an routing with FLWL/MWL/EWL, spill and hydropower limits. |
| R6/E5–E6 | Evaluate safety/utilization under baselines and forecast perturbations. | COR/Two-OR comparisons, 12 floods, error/RFH/flood-pattern scenarios. |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | FCC exceedance, levee-failure probability, water level, release, and generation are modeled indicators. | No observed levee damage, hydrodynamic damage, or ecological outcome is measured. |
| Model/simulation result versus deployment | Three-OR is applied to 12 simulated flood hydrographs. | No live operator deployment; authors explicitly mention possible human correction. |
| Sensitivity/comparison versus independent validation | Rule comparisons, forecast-error scenarios, RFH extensions, amplified floods, and flood-pattern grouping are reported. | No independent event/out-of-sample validation; baseline forecasts and uncertainty are stylized. |
| Assumption versus calibration | 20% RFH criterion, normal errors, coefficients, 6-h interval, FCC and levels are settings/assumptions; coefficients are said to be estimated historically. | Exact historical estimation, forecast correlation, and economic loss valuation are not fully reported. |
| Case result versus general rule | Stage-aware Three-OR improves modeled Wan’an safety/utilization under tested conditions. | Effects depend on flood shape, forecast-error differences, RFH, and reservoir constraints. |

## 6. Unreported or unresolved items

- Full forecast-error datasets, coefficient-estimation procedure, forecast correlation, and RFH-selection uncertainty are not supplied.
- Operational handling of infeasible KKT allocations, missing forecasts, gate limits, and operator overrides is not specified.
- The objective fixes catastrophic damage, so the rule is not a full economic optimization.
- Intermediate inflow/routing is roughly represented; no hydraulic damage or independent validation is reported.
- The paper notes release-trajectory fluctuation and human correction but gives no formal correction protocol.

## 7. Final quality check

### Reasoning
The route explains stage segmentation, dependent risk objective, nested marginal-risk allocation, and conditional RFH logic.

### Execution
The route follows error/RFH setup through outer/inner KKT solutions, routing, rolling updates, and evaluation branches.

### Evidence
Rows cite supplied pages/equations/tables and preserve assumptions, simulation limits, and sensitivity/comparator boundaries.

### Reusability
Potential abstractions include forecast-stage segmentation, dependent risk allocation, nested current/future storage decisions, constrained rolling routing, and scenario-based evaluation. Wan’an parameters and stylized error model remain paper-specific.

