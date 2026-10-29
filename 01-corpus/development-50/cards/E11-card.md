# E11 Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: Wan, W., Lei, X., Zhao, J., Wang, M., Khu, S.-T., & Wang, C. (2021), “A forecast-skill-based dynamic pre-storm level control for reservoir flood-control operation,” *Water*, 13, 556, DOI: 10.3390/w13040556. Source: [E11.txt](../text/E11.txt). Reading scope: pp. 1–20, §§1–5; figures/tables used through supplied captions/text.

## Paper identification

The paper proposes dynamic pre-storm level (D-PSL) control based on forecast skill, forecast flood volume over multiple periods, reservoir capacity, and downstream conveyance. It derives a risk-consistent pre-storm storage level, selects the minimum among 1-, 2-, 3-, and 5-day calculations, and evaluates it for the Three Gorges Reservoir using historical and simulated floods.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | Fixed FLWL wastes storage when forecast floods are modest, but relaxing it can threaten flood safety. The study seeks a pre-storm storage level that preserves design flood-control risk while using forecast skill. | pp. 1–4, §§1–2.1. |
| Method overview | Estimate forecast-error variance from skill, set a dynamic design-period flood quantile, calculate D-PSL for several maximum-period flood forecasts, and choose the minimum level; evaluate against simulated/observed flood sets. | pp. 5–8, 10–18, §§2.2–3.4. |
| Research significance | D-PSL equals traditional FLWL when skill is poor and rises with skill in the modeled Three Gorges case, enabling more storage while retaining a probabilistic flood criterion. | pp. 17–18, §5. |

## 2. How the authors reason

Reasoning overview: Forecast errors are not stationary across lead times, and a flood’s peak timing is less important for large reservoirs than period volume. The authors define a design-period flood quantile so the probability that forecast error exceeds its bound matches the design standard. Storage below this derived level is sufficient to release/contain the forecast period flood at the downstream safety discharge. Multiple period windows are considered because different windows may be controlling; taking the minimum is conservative.

Reconstructed route: choose period-volume representation; quantify forecast skill/error; map design probability to an error threshold; derive period-specific D-PSL from capacity, release, and forecast volume; select the minimum across windows; simulate operation and test impacts of flood magnitude, capacity, reservoir size, and forecast skill.

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. Choose volume-based control target | Large reservoirs can smooth intraday peaks, so maximum 1–5 day flood volume is a useful forecast target for pre-storm storage. | **Trigger:** Need a forecast-linked pre-storm level. **Inputs:** Forecast period flood volumes and downstream safety release. **Judgment/procedure:** Use maximum period volumes rather than only peak flow; consider 1,2,3,5-day windows. **Output:** Candidate period controls. | §§1–2.1, pp. 1–4. Applicability is explicitly focused on reservoirs adequate to regulate peaks. |
| R2. Convert forecast skill into an acceptable error bound | A design flood probability must remain unchanged under uncertain forecast. | **Trigger:** Set dynamic design-period flood. **Inputs:** Forecast skill Cp, variance of observed period volume, desired design exceedance Pdes. **Judgment/procedure:** Use σ²ε=(1−Cp)var(Vts), then choose δP,ts from the forecast-error quantile so Prob(εts≥δP,ts)=Pdes. **Output:** Error allowance and dynamic design volume. | §§2.2, pp. 5–6, Eqs. (1)–(5). Normal error is assumed for illustration. |
| R3. Derive period-specific D-PSL | Storage must support the design-period inflow after accounting for releasable volume and reservoir capacity. | **Trigger:** For each period forecast. **Inputs:** Capacity K, maximum safe release volume rts, forecast/design flood volume. **Judgment/procedure:** Compute S0,ts=K+rts−fdes,ts and express as water level; keep level no higher than D-PSLts. **Output:** Candidate D-PSL for each period. | §§2.2, pp. 6–8, Eqs. (6)–(9). Detailed notation is supplied in the text; operational gate behavior is not. |
| R4. Select controlling period | A single forecast period may miss a controlling accumulation pattern. | **Trigger:** Candidate levels from several windows available. **Inputs:** D-PSL1d, D-PSL2d, D-PSL3d, D-PSL5d. **Judgment/procedure:** Choose the minimum candidate to satisfy all considered periods. **Output:** Event-specific D-PSL. | §2.2, pp. 7–8, Eq. (8). Conservative minimum is paper-specific. |
| R5. Evaluate robustness and benefit | The value of D-PSL depends on forecast skill, conveyance capacity, reservoir size, and flood pattern. | **Trigger:** Assess whether relaxation helps without excessive risk. **Inputs:** Historical/simulated floods, capacities, skill levels, reservoir capacity ratios. **Judgment/procedure:** Simulate operation and compare selected D-PSL with FLWL and design levels; inspect overlap among period controls. **Output:** Conditional performance and limitations. | §§3–5, pp. 9–18. Larger simulated events and capacity changes alter outcomes. |

## 3. How the authors execute

Execution overview: The method estimates period-flood statistics and forecast skill, constructs 10,000 synthetic forecast floods using an AR(1) model with Pearson type III period volumes, calculates dynamic design period volumes and D-PSLs, and simulates reservoir operation for 12 selected floods at Three Gorges. The paper examines forecast-skill/capacity/reservoir-size scenarios and compares D-PSL with current FLWL-based control.

Reconstructed workflow: estimate forecast error/skill → generate or select period flood forecasts → compute design flood quantile → calculate period-specific D-PSLs → select minimum → route under maximum safety release → summarize level/capacity and operation implications.

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. Estimate forecast skill/error | Quantify skill for each period volume and infer forecast-error threshold. | **Trigger:** Prepare D-PSL calculation. **Inputs:** Historical forecast/actual period volumes, Cp, var(Vts), Pdes. **Procedure:** Use Eqs. (1)–(5), with normal error representation. **Output:** δP,ts and fdes,ts. | Forecast skill is varied from zero to perfect in scenarios; exact operational forecast product and calibration are not fully described (pp. 5–6, 12–13). |
| E2. Build flood-volume scenarios | Extend observed period-volume combinations beyond the historical return-interval range. | **Trigger:** Need broad flood-frequency coverage. **Inputs:** Historical independent period-flood series. **Procedure:** Fit/use AR1 vector model for Pearson III period floods and simulate 10,000 forecast floods; classify by design frequency. **Output:** Forecast event ensemble. | §§3.1–3.2, pp. 9–11. Simulations include rare synthetic combinations; they are not observations. |
| E3. Calculate candidate and selected D-PSL | Translate forecast/design flood volume, safe release, and capacity into levels. | **Trigger:** Each forecast event and skill scenario. **Inputs:** K, rts, fdes,ts, water-level-volume curve. **Procedure:** Apply Eq. (7) for 1/2/3/5 days, then Eq. (8) minimum. **Output:** Event-specific pre-storm level. | 12 selected TGR floods and multiple skill/capacity scenarios are shown in §§3.2–3.4; D-PSL is bounded by pre-release capacity and design flood. |
| E4. Simulate operation under D-PSL | Route forecast flood with maximum safety release to inspect storage trajectories. | **Trigger:** D-PSL chosen. **Inputs:** Flood hydrograph/period volume, FLWL/design levels, downstream conveyance. **Procedure:** Pre-release/retain water to D-PSL and route through storm-control period. **Output:** Reservoir level, release, and control performance. | Figs. 1, 3, 6–8 and pp. 7–8, 13–17. Intraday routing simplifications apply. |
| E5. Compare scenarios and current practice | Evaluate flood-control risk and water-use opportunity. | **Trigger:** Completed simulations. **Inputs:** D-PSL versus traditional FLWL, forecast skill, capacity and reservoir-size ratios, flood groups. **Procedure:** Compare levels, release capacity, chosen period, and storage benefits. **Output:** Conditional guidance. | §§3.2–3.4, pp. 10–18. No live deployment or independent validation. |

Extraction conventions: Ordering is the extractor’s reconstruction. D-PSL is a modeled pre-storm control level; the paper does not specify all real-time gate authorization/fallback procedures.

Micro-skill convention: Rows retain trigger, inputs, procedure, branches, outputs, checks, and assumptions for future synthesis.

Human review: Awaiting review; no reviewer/date/feedback supplied.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| R1/E1 | Select forecast horizon representation matched to reservoir response. | 1/2/3/5-day maximum flood volumes for large TGR. |
| R2/E1 | Translate skill and target reliability into an error quantile. | Cp-based σ²ε and Pdes quantile δP,ts under normal error. |
| R3–R4/E3 | Convert forecast/design volume and safe release into a conservative pre-storm level. | S0,ts=K+rts−fdes,ts; minimum of four D-PSLs. |
| R5/E4–E5 | Evaluate adaptive level under capacity, size, flood, and skill scenarios. | TGR, 10,000 AR1 simulations, 12 floods, capacity/skill/size analyses. |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | Reservoir levels, release capacity, period volumes, and design exceedance probabilities are modeled indicators. | No direct flood damage or hydraulic consequence model. |
| Model/simulation result versus deployment | D-PSL is calculated and simulated for TGR. | No operational deployment or operator acceptance is reported. |
| Sensitivity/comparison versus independent validation | Forecast-skill, capacity, size, flood-pattern, period-window, and synthetic-flood comparisons are included. | Simulated/selected cases do not provide independent field validation. |
| Assumption versus calibration | Normal forecast error, AR1/Pearson III synthetic model, target probability, period windows, and safety release are assumptions/settings; skill is estimated from forecast statistics. | Forecast-error nonnormality, dependence, and full calibration details are not established. |
| Case result versus general rule | Better skill permits higher D-PSL in modeled TGR; poor/unknown skill returns toward traditional FLWL. | Applicability requires adequate reservoir capacity, forecasts, and suitable volume representation. |

## 6. Unreported or unresolved items

- Full forecast datasets, forecast-error distributions beyond the normal illustration, Cp estimation, and Pdes values are not fully reported.
- Exact AR1 fitting, synthetic-simulation diagnostics, release-routing implementation, and gate/ramping constraints are incomplete in supplied text.
- The method assumes enough active storage to regulate peaks and does not model direct damages or human operational overrides.
- Handling of forecast updates, forecast failure, missing data, conflicting period controls, and post-event learning is not specified.

## 7. Final quality check

### Reasoning
The route explains why period-volume forecasts, skill-based error bounds, and minimum multi-window D-PSL are used, with case and assumption limits.

### Execution
The route follows skill estimation through synthetic/selected floods, level calculation, routing, and scenario evaluation.

### Evidence
Rows cite supplied pages/equations/figures and separate modeled indicators, simulations, assumptions, and deployment limits.

### Reusability
Potential abstractions include horizon selection, skill-to-quantile conversion, conservative multi-window level control, and capacity/skill sensitivity assessment. TGR dimensions, flood statistics, and coefficients remain paper-specific.

