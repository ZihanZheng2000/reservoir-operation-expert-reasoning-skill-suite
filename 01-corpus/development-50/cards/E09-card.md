# E09 Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: Hua, L., Wan, X., Wang, X., Zhao, F., Zhong, P., Liu, M., & Yang, Q. (2020), “Floodwater utilization based on reservoir pre-release strategy considering the worst-case scenario,” *Water*, 12, 892, DOI: 10.3390/w12030892. Source: [E09.txt](../text/E09.txt). Page references use PDF pages. Reading scope: pp. 1–17, including §§1–5; figures were used only through captions/text.

## Paper identification

This paper proposes a two-period capacity-constrained pre-release method for Xianghongdian Reservoir. It estimates dry-period and flood-forecast lead-time distributions, calculates added storage above the flood-limited water level (FLWL), then subtracts water that cannot be released under an immediate-flood/failed-forecast worst case. The supplied text is complete and page-separated.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | Fixed FLWL operation can waste floodwater in dry flood seasons, while raising storage through forecast-based utilization can increase flood risk. The study determines water-use and flood-control pre-release volumes and a safe upper bound under worst-case forecast failure. | pp. 1–4, §§1–2. |
| Method overview | Fit historical dry-period durations with negative-exponential and asymptotic-regression models, estimate natural flood forecast lead time from 10 events, calculate two-part excess storage, and test release time/safe storage over 50 dry-day/lead-time scenarios. | pp. 4–13, §§2.1–3.4. |
| Research significance | The method explicitly accounts for dry periods and insufficient release capacity: for the illustrative 5-day/6-hour scenario, total added storage is 63.4×10^6 m³ and worst-case safe added storage is about 23.0×10^6 m³. Results are Xianghongdian-specific. | pp. 10–15, Tables 4–7, §5. |

## 2. How the authors reason

Reasoning overview: The authors observe that capacity-constrained pre-release normally starts only when a large flood is forecast, overlooking water-use releases during a long dry interval. They divide pre-release into water-use and flood-control periods, use historical rainfall/flow statistics to supply missing duration information, and quantify how duration and lead time increase excess storage. Since rainfall forecasts can fail and discharge capacity may be too small, they evaluate an immediate-flood worst case and retain only the volume releasable within the effective lead time as safe.

Reconstructed route: identify the fixed-FLWL water-conservation conflict; define two release periods and their triggers; estimate dry-period and lead-time distributions; calculate total over-FLWL water for scenario combinations; test worst-case release time against available lead time; deduct unreleasable volume; inspect historical event benefits and state applicability limits.

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. Identify when water-use pre-release is valid | During a forecast dry period, inflow can be below utilization discharge, so releasing at that rate converts otherwise excess floodwater into conservation/hydropower use. Waiting for the next large-flood forecast can miss this opportunity. | **Trigger:** Reservoir is above/near planned upper FLWL and a dry interval is expected. **Inputs:** Inflow, utilization discharge, rainfall forecast/dry duration. **Judgment/procedure:** Start water-use pre-release when inflow is below utilization discharge; switch to flood-control pre-release when a large inflow is forecast. **Branches:** Dry forecast versus imminent flood forecast. **Output:** Two-period release plan. | §§1–2, pp. 3–4. Trigger details beyond the conceptual rule are not fully operationalized. |
| R2. Estimate duration/lead-time information conservatively | Duration and forecast lead time govern how much water can be released, but direct short-term dry-duration forecasts are unavailable. Historical data are used to approximate their distributions. | **Trigger:** Need scenario inputs for dynamic FLWL. **Inputs:** Rainfall series, historical floods and rainfall/flow pairs. **Judgment/procedure:** Count consecutive ≤3-mm dry days; compare negative-exponential fit with asymptotic regression; derive natural lead time as end of main rain to flood peak and fit a normal distribution. **Branches:** Select negative exponential as safer/conservative; use lead times up to effective 10 h. **Output:** Dry-duration and lead-time distributions. | §§2.1–2.2, pp. 4–6, 8–10. No real-time dry-period forecast model is built. |
| R3. Quantify allowable added storage | Water above FLWL is decomposed into utilization-period and flood-control-period volumes. Their sum depends on dry duration, inflows, discharge, safety margin, and lead time. | **Trigger:** Construct an operating scenario. **Inputs:** d, τ, qm(t), qin(t), qfl(t), downstream safety qA, discount β, discharge capacity g(Z). **Judgment/procedure:** Compute ΔWFU, ΔWFC, qc=min(βqA,g(Z)), and ΔWtotal. **Branches:** Vary d and τ; longer values increase planned storage in this case. **Output:** Planned over-FLWL volume and corresponding level. | §§2.3, 3.3, Eqs. (7)–(10), pp. 6, 10–11. These are modeled volumes, not authorization limits without further operational checks. |
| R4. Stress-test forecast failure and capacity | A forecast failure with the next flood arriving immediately is the adverse case for safe release. If all stored water cannot be removed within τ, retaining it would increase flood risk. | **Trigger:** Dry/delayed-flood assumption fails. **Inputs:** ΔWtotal, qA, g(Z), qfl, τ. **Judgment/procedure:** Release at min(qA,g(Z)); compare required time t with τ; deduct unreleased volume from ΔWtotal to obtain ΔWsafe. **Branches:** If t≤τ, no added original risk under the model; if t>τ, reduce safe volume. **Output:** Safe added storage and quantified burden. | §§2.4, 3.4, pp. 6–7, 11–13, Tables 5–6. All 50 tested scenarios exceeded lead time in the case. |
| R5. Judge practical benefit and boundaries | Dynamic storage benefit varies by actual flood and may be negative for small events when releases exceed inflow. A safe upper bound is therefore more useful than total planned volume. | **Trigger:** Interpret scenario and historical event results. **Inputs:** Six historical floods, scenario tables, model assumptions. **Judgment/procedure:** Compare real-time added storage and inspect duration/lead-time trade-offs and worst-case safe values. **Output:** Case feasibility claim and need for broader risk/benefit evaluation. | §§4–5, pp. 13–15. Four of six historical events had positive added storage; two were negative. Single-reservoir scope is explicit. |

## 3. How the authors execute

Execution overview: Historical rainfall (1956–2015) supplies dry-period observations; 10 flood events (2008–2016) supply natural lead times. The paper fits duration/lead-time distributions, fixes a 5-day water-use period and effective lead-time range 1–10 h for Xianghongdian, computes two-part added storage for 50 scenarios, and simulates maximum-capacity release under immediate flood failure. Six historical floods are then used for descriptive real-time added-storage checks.

Reconstructed workflow: collect and count dry intervals → fit/compare duration models → derive lead-time statistics → calculate utilization and flood-control volumes → enumerate d=1…5 and τ=1…10 h → calculate release time and safe volume under failed forecast → compare six events and discuss transfer.

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. Fit dry-period distribution | Count historical consecutive dry days and fit candidate distributions. | **Trigger:** Set water-use pre-release duration. **Inputs:** 9,180 flood-season daily rainfall records, 1956–2015; dry defined as ≤3 mm. **Procedure:** Count 1,200 continuous dry periods; calculate d0 and mean; fit negative exponential and asymptotic regression; compare across 10-year subsets. **Output:** Dry-duration distribution and selected 5-day upper water-use period. | Median is 4 days; probability of exceeding 5 days is about 50%; negative exponential is more conservative in low-frequency tail (pp. 8–10, Table 2). |
| E2. Estimate effective forecast lead time | Derive natural lead times from historical rainfall and flood peaks. | **Trigger:** Set flood-control pre-release horizon. **Inputs:** 10 floods, 2008–2016. **Procedure:** Measure interval from end of main rainfall to peak flow; compute mean and standard deviation; fit normal N(ET, ST²). **Output:** Lead-time distribution; effective upper bound 10 h after information/decision/transmission/gate-operation allowances. | Mean is 9.90 h and reported variance/standard deviation value is 5.30 h (p. 10); exact operational derivation of the 10-h bound is not detailed. |
| E3. Calculate two-period over-FLWL volume | Convert dry-period utilization and flood-control release differences into added storage. | **Trigger:** Each d/τ scenario. **Inputs:** d=1…5 days, τ=1…10 h, qm=200 m³/s, qA=2500 m³/s, β=0.5, inflow/flood process, capacity function. **Procedure:** Apply Eqs. (7)–(10), using qc limited by downstream safety and reservoir discharge capacity. **Output:** ΔWFU, ΔWFC, ΔWtotal, and implied water level. | Table 4 gives 50 values; 5-day/6-h yields 63.4×10^6 m³ and level 126 m, 1 m above FLWL (pp. 10–11). |
| E4. Run worst-case release calculation | Assume the next flood arrives immediately after over-storage and release at maximum safe rate. | **Trigger:** Complete failure of dry-weather forecast. **Inputs:** Total added volume, qA, g(Z), flood inflow, τ. **Procedure:** Apply Eq. (11) to estimate release time; if t>τ, calculate unreleased ΔW′ by Eq. (12) and safe ΔW by Eq. (13). **Output:** Release-time and safe-storage tables. | All 50 scenarios could not return to original FLWL within lead time; for 5-day/6-h, safe volume is 23.0×10^6 m³ and level 125.4 m (pp. 11–13). |
| E5. Check historical event behavior | Evaluate descriptive real-time benefit across selected floods. | **Trigger:** Assess whether modeled benefit appears in actual event records. **Inputs:** Six 1999–2006 flood hydrographs, start levels/storage. **Procedure:** Calculate real-time added storage from actual inflow/outflow; classify positive versus negative cases. **Output:** Table 7 event-level volumes and operational interpretation. | Four positive and two negative events; small floods can produce negative storage because power-generation release exceeded inflow (p. 13). No statistical validation is reported. |

Extraction conventions: Ordering is the extractor’s reconstruction. The proposed method quantifies a safe storage bound; it does not document an implemented controller, automatic trigger logic, or emergency authorization procedure.

Micro-skill convention: Activity-level triggers, inputs, calculations, branches, outputs, and checks are retained for later synthesis; no final skill collection is declared.

Human review: Awaiting review; no reviewer/date/feedback supplied.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| R1/E1 | Split adaptive pre-release according to hydrologic regime and use objective. | Water-use pre-release during forecast dry days; flood-control pre-release after large inflow forecast; qm=200 m³/s. |
| R2/E1–E2 | Infer operational horizons from historical event statistics. | ≤3-mm dry-day counts, negative-exponential/ARM comparison, rainfall-to-peak lead times, 5-day and 10-h bounds. |
| R3/E3 | Compute added storage from release opportunity and safety-limited flood routing. | Eqs. (7)–(10), β=0.5, qA=2500 m³/s, Xianghongdian inflows/capacity. |
| R4/E4 | Stress-test a plan under forecast failure and retain only timely releasable benefit. | Immediate next flood, release at min(qA,g(Z)), Eqs. (11)–(13), Tables 5–6. |
| R5/E5 | Check scenario benefit against event-level behavior and identify negative cases. | Six historical events and Table 7 added-storage values. |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | Added-storage volume, release time, reservoir level, and downstream safety discharge are modeled operational indicators. | No direct flood damage, downstream hydraulic impact, water-quality, or ecological consequence analysis. |
| Model/simulation result versus deployment | Method is calculated for Xianghongdian scenarios and historical event records. | No documented real-time deployment, operator trial, or observed safety outcome. |
| Sensitivity/comparison versus independent validation | Dry-distribution model comparison, d/τ scenario grid, worst-case stress test, and six-event descriptive check are included. | No independent validation, convergence study, or forecast-failure frequency assessment. |
| Assumption versus calibration | ≤3-mm dry threshold, 5-day duration cap, normal lead-time model, qA=2500, β=0.5, qm=200, 10-h effective lead time, and immediate-flood worst case are settings/assumptions; fits use historical series. | Discharge-capacity function details, fitted parameters beyond reported summaries, and uncertainty correlation are not fully reported. |
| Case result versus general rule | In this case, longer dry periods/lead times increase planned added storage, but safe storage is limited by release time and capacity. | Conclusions are single-reservoir and process-specific; two negative historical events show benefit is not universal. |

## 6. Unreported or unresolved items

- Exact daily inflow series, reservoir discharge-capacity curve g(Z), all intermediate volume calculations, and fitting diagnostics are not fully provided in the text.
- The effective 10-h lead-time bound includes communication and gate-operation allowances, but their numerical decomposition is not reported.
- No procedure handles forecast updates, conflicting rainfall/flood forecasts, missing data, gate failure, or escalation when t>τ.
- The worst case assumes immediate flood arrival and complete meteorological failure; probabilities of these conditions are not estimated.
- The paper does not independently validate the safe-storage rule or quantify downstream damages and ecological/economic trade-offs.

## 7. Final quality check

### Reasoning
The route explains why two release periods and a worst-case safe-volume correction are needed, while keeping the conservative selection and case limitations explicit.

### Execution
The route tracks rainfall/event data through distribution fitting, scenario volume calculations, failed-forecast release-time checks, and historical-event review, separating model scenarios from descriptive event analysis.

### Evidence
Rows reference supplied pages, sections, equations, and tables; modeled indicators, assumptions, and deployment limits are distinguished.

### Reusability
Potentially recurring abstractions include regime-based prerelease triggers, historical horizon estimation, constrained storage-volume calculation, worst-case timely-release correction, and event-level benefit checking. Xianghongdian thresholds, fitted durations, discharge capacity, and numerical results are paper-specific.

