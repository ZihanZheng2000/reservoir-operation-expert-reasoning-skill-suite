# E40 Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: Liu, Pan; Lin, Kairong; Wei, Xiaojing (2015). “A two-stage method of quantitative flood risk analysis for reservoir real-time operation using ensemble-based hydrologic forecasts.” *Stochastic Environmental Research and Risk Assessment*, 29, 803–813. DOI: 10.1007/s00477-014-0986-0. Source: [E40 text](../text/E40.txt). Reading scope: supplied text pages 1–11, including Sections 1–4, Tables 1–2, Figures 1–10, and the cited methods as presented. Page references use supplied PDF page markers. The OCR text contains visible mojibake and occasional equation corruption; terms and equations were normalized only where definitions were clear.

## Paper identification

The paper develops a two-stage flood-risk analysis for real-time reservoir operation driven by ensemble hydrologic forecasts. It counts failures during the forecast lead time and estimates residual risk after the forecast horizon using design flood hydrographs routed from the ensemble end states. The Three Gorges Reservoir 2010 flood is used to compare historical operation with a scenario-optimized operation for both release-control and water-level-control formulations, including hydropower production.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | Quantify upstream water-level and downstream-release risk throughout an operation horizon when inflow is uncertain and only forecast lead time is predictable. The method must account for both the forecasted and unpredicted portions of the flood. | pp. 2–4, Section 2; Fig. 1; Eqs. (1)–(9). |
| Method overview | Generate ensemble inflow scenarios, simulate reservoir operation, count scenario failures within the forecast horizon, route design floods from each ensemble end state for the unpredicted period, and combine the two dependent risk components as a yearly-scale failure ratio. | pp. 2–4, Sections 2.2–2.4; Eqs. (4)–(9). |
| Research significance | The method links real-time risk to flood-protection return periods and evaluates the trade-off between risk and hydropower. For the 2010 case, optimized operation raises hydropower while remaining at or below the stated 5% acceptable risk, subject to the paper’s case assumptions. | pp. 9–10, Table 2, Section 4. |

## 2. How the authors reason

Reasoning overview: The authors treat ensemble forecasts as a direct representation of inflow uncertainty, preserving marginal behavior and temporal persistence. A single risk calculation over the whole future is impractical because the forecast horizon ends before the operation horizon, so they split the future into a forecast lead-time and an unpredicted period. Forecast-period risk can be counted directly across scenarios; post-horizon risk is estimated from design-flood routing conditional on each scenario’s end water level. The two components are statistically related because scenarios that fail early are excluded from the residual-risk contribution. Operation alternatives are then judged by whether their yearly-scale risk is below a flood-standard benchmark while improving hydropower. The study does not claim deployment validation or a general economic optimum.

Reconstructed route: (1) define critical release and water-level events; (2) split the horizon at the forecast point; (3) generate/validate ensemble forecasts; (4) simulate operation under each scenario; (5) count lead-time failures; (6) route design floods from nonfailed scenario end states; (7) combine stage risks; and (8) compare historical and scenario-optimized operation under release- and level-control variants.

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. Represent inflow uncertainty by scenarios | Persistence in inflow is difficult for simple Monte Carlo descriptions, whereas ensemble forecasts directly provide hydrograph scenarios. | **Trigger:** operation decisions depend on uncertain future inflow. **Inputs:** parameter/precipitation uncertainty and raw forecasts. **Judgment/procedure:** use ensemble hydrographs as the uncertainty object. **Branches:** probabilistic forecasting and ESP are treated equivalently at the operator interface. **Output:** m forecast scenarios. | pp. 2–3 and 5–6, Sections 1, 3.1–3.2. The paper demonstrates probabilistic forecasting with parameter and precipitation uncertainty; full ESP alternatives are not executed. |
| R2. Split predictable and unpredicted time | Forecast skill ends at a horizon, but flood risk may continue afterward. Ignoring the latter would undercount risk. | **Trigger:** operation extends beyond available forecast lead time. **Inputs:** forecast horizon, scenario trajectories, design flood statistics. **Judgment/procedure:** divide into lead-time risk R1 and unpredicted-time risk R2, retaining dependence through scenario end states. **Output:** two linked risk terms. | pp. 2–4, Fig. 1 and Sections 2–2.4. The paper assumes the post-horizon design-flood representation is adequate for the unpredicted period. |
| R3. Set risk events and control mode | Release above Qc threatens downstream safety; water level above Zc threatens upstream/dam safety. Release-control and water-level-control models expose different risk sides. | **Trigger:** evaluate an operating policy. **Inputs:** release/water-level trajectories, Qc, Zc. **Judgment/procedure:** define a scenario as failed if any time step crosses the relevant threshold; choose fixed release or fixed level as the control formulation. **Output:** upstream or downstream risk statistic. | pp. 2–3, Eqs. (1)–(5), Section 3.3. The paper considers probability only, not consequence severity. |
| R4. Use protection standards as acceptable risk | Risk becomes actionable when expressed on the same yearly/return-period scale as flood protection standards. | **Trigger:** compare candidate operation with safety requirements. **Inputs:** derived yearly risk, design return period. **Judgment/procedure:** treat the design-flood frequency as acceptable risk benchmark. **Output:** acceptability comparison. | pp. 4 and 9–10, Sections 2.4 and 3.4. Economic justification of the benchmark is explicitly left for future work. |
| R5. Compare risk and hydropower jointly | The reservoir is multipurpose; maximizing flood safety alone may sacrifice energy. Scenario optimization therefore minimizes level/release objectives while maximizing generation, with assigned variance weights. | **Trigger:** choose among feasible operations under uncertain inflow. **Inputs:** ensemble scenarios, mass-balance/level/release constraints, generation function. **Judgment/procedure:** combine three objectives with weights 0.3, 0.3, 0.4 and select a reasonable Pareto solution. **Output:** optimized operating policy. | pp. 7–9, Sections 3.3.2 and Eqs. (16)–(18). The final Pareto choice is described as arbitrary/reasonable rather than derived from a formal stakeholder utility. |

## 3. How the authors execute

Execution overview: A rainfall–runoff and routing setup produces ensemble inflow forecasts for four sub-daily lead times. The reservoir is simulated with either prescribed releases or prescribed water levels. During the lead time, each scenario is marked once if it crosses the relevant critical threshold. At the horizon, every nonfailed scenario receives a design-flood routing risk conditional on its end water level; the resulting weighted average is combined with counted early failures. The TGR 2010 flood is then used to compare historical operation and an SSDP-derived scenario policy, with risks calculated under release-control and water-level-control views.

Reconstructed workflow: calibrate/validate hydrologic forecast model -> generate ensemble scenarios -> simulate operation -> count lead-time failures -> route design floods from end states -> combine risk -> optimize/compare operating schemes -> check risk against 5% benchmark and hydropower output.

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. Build ensemble inflow forecasts | Use a MISO model for Cuntan/Wulong inflow and an Xinanjiang rainfall–runoff model for the intervening basin. Apply parameter and precipitation uncertainty to produce scenarios. | **Trigger:** a forecast-driven operation case is prepared. **Inputs:** 6-hourly streamflow and rainfall, June–September data from 2003–2010. **Procedure:** calibrate on 2003–2007, validate on 2008–2010; use 19 model parameters and adaptive Metropolis sampling for parameter uncertainty, together with precipitation uncertainty. **Output:** ensemble inflow hydrographs. | pp. 4–6, Sections 3.1–3.2, Figs. 3–7, Eqs. (10)–(15). Median 90% interval R²/RE are reported as 0.96/0.02 calibration and 0.94/−0.01 validation. |
| E2. Simulate reservoir with scenario inputs | Apply ensemble inflows to the mass-balance reservoir routing model under release-control or water-level-control operation. | **Trigger:** an ensemble and a candidate operation are available. **Inputs:** I_t, R_t, V_t, losses, time interval, Rmin/Rmax, Vmin/Vmax, control trajectory. **Procedure:** route each scenario; if releases are fixed, calculate water levels; if levels are fixed, calculate releases. **Output:** m trajectories and scenario end levels. | pp. 2–4, Eqs. (1)–(3), Section 3.1. Exact time step and loss treatment are stated generally; losses are often ignored. |
| E3. Count forecast-horizon failures | Mark each scenario once if any lead-time release exceeds Qc or any water level exceeds Zc, then divide by m. | **Trigger:** scenario trajectories through the forecast horizon are available. **Inputs:** all time-step releases/levels and critical thresholds. **Procedure:** apply a binary any-crossing indicator; repeated crossings in one scenario still count once. **Output:** R1,down or R1,up. | pp. 3–4, Eqs. (4)–(5). This is a scenario-frequency risk, not a count of failure episodes. |
| E4. Estimate post-horizon risk conditionally | Route each design-flood hydrograph from each scenario’s end water level at the forecast horizon. | **Trigger:** the forecast horizon ends without a counted failure. **Inputs:** scenario end level Zi,tn, design flood hydrographs, critical release/level, reservoir routing. **Procedure:** calculate Rdown(Zi,tn) or Rup(Zi,tn); assume equal scenario probabilities unless otherwise specified; use the starting level at tn, not the initial level. **Output:** R2,down or R2,up. | pp. 3–4, Eq. (6)–(7), Fig. 1. The text says end level is assumed uncorrelated with forthcoming flood for this estimate; that is a material assumption. |
| E5. Combine the two risk stages | Add counted early failures and residual design-flood risks for scenarios that did not fail early. | **Trigger:** R1 and conditional R2 are available. **Inputs:** failure scenario set T, nonfailure end levels and conditional risks. **Procedure:** use Eqs. (8)–(9), summing one for early failures and R2 for scenarios outside T, then divide by m. **Output:** yearly-scale entire risk. | pp. 4, Eq. (8)–(9). The conditional dependence is represented by excluding T from the residual term. |
| E6. Define scenario-optimized operation | Use SSDP to formulate a deterministic optimization for each scenario while enforcing shared decisions across scenarios. | **Trigger:** ensemble scenarios can inform an alternative policy. **Inputs:** scenario inflows, reservoir constraints, objectives F1–F3. **Procedure:** minimize maximum/aggregate water level and discharge, maximize hydropower, assign weights 0.3/0.3/0.4, generate Pareto solutions, and select a reasonable solution. **Output:** optimized release/level policy. | pp. 7–9, Sections 3.3.2, Eqs. (16)–(18), Figs. 8–9. The exact SSDP discretization and selected Pareto criterion are not reported. |
| E7. Compare historical and optimized schemes | Calculate risk and hydropower for operated and optimized schemes under both control models. | **Trigger:** candidate policies are ready for case evaluation. **Inputs:** 2010 flood, critical values for 0.01%, 0.1%, 1%, and 5% design floods, policy trajectories. **Procedure:** evaluate release-control upstream risk and water-level-control downstream risk; compare energy and end water level. **Output:** Table 2 comparison. | pp. 9–10, Table 1–2, Fig. 10. Optimized release-control risk is 4.95% with 1.58 billion kWh; optimized level-control risk is 5.00% with 1.60 billion kWh. |

Extraction conventions: R/E identifiers and ordering are reconstructed from the article. Human review: awaiting review; no reviewer feedback supplied. Single-paper extraction does not establish recurring patterns or validate a skill collection.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| R1/E1 | Generate temporally coherent inflow scenarios from forecast and model uncertainty. | TGR MISO/Xinanjiang model, adaptive Metropolis parameter sampling, precipitation uncertainty, four sub-daily lead times. |
| R2/E3–E5 | Decompose risk at a forecast boundary and recombine conditional residual risk. | Count any threshold crossing before the horizon; route design floods from nonfailed scenario end levels afterward. |
| R3/E2 | Evaluate a policy through threshold-specific control modes. | Fixed releases expose upstream water-level risk; fixed levels expose downstream release risk. |
| R4/E6 | Optimize multipurpose operation across shared scenarios. | SSDP with water-level, discharge, and hydropower objectives weighted 0.3, 0.3, 0.4. |
| R4/E7 | Compare risk with an acceptable frequency benchmark and benefit output. | TGR 2010 operation compared with 5% design risk and hydropower generation. |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | Risk is defined as threshold-exceedance probability; hydropower generation is the benefit metric. | Flood damage, loss severity, and economic value of curtailed generation are not modeled. |
| Model/simulation result versus deployment | Historical and optimized policies are simulated for the 2010 TGR flood using ensemble scenarios and design hydrographs. | No prospective operational trial, independent event validation, or authorization procedure is reported. |
| Sensitivity/comparison versus independent validation | Historical versus optimized schemes and release- versus level-control views are compared; forecast model has calibration/validation periods. | The risk method itself is not independently validated; no sensitivity to ensemble size, horizon, weights, or design-hydrograph assumptions is reported. |
| Assumption versus calibration | Forecast model parameters are sampled and evaluated; constraints and hydropower relation are specified. | Post-horizon end-level independence, equal scenario probabilities, ignored losses, and objective weights are assumptions or case choices. |
| Case result versus general rule | The optimized scheme meets the stated 5% benchmark in the 2010 case and produces more energy than historical operation. | This does not establish universal acceptability or superiority for other floods, reservoirs, or risk standards. |

## 6. Unreported or unresolved items

- Ensemble size, MCMC burn-in/thinning, proposal settings, and detailed convergence diagnostics are not reported in the supplied text.
- The exact SSDP scenario-sharing formulation, discretization, Pareto-solution selection rule, and operational tie handling are not reported.
- The number and timing of design-flood hydrographs used for post-horizon routing and the interpolation procedure for R2 are only partially specified.
- The independence assumption between end water level and forthcoming flood is not empirically tested in the supplied text.
- The economic basis for the acceptable-risk benchmark and the assigned objective weights is not reported; the paper explicitly calls for further work on risk–profit trade-offs.
- Real-time operator authorization, fallback actions, and post-event updating are not reported.
- The text contains OCR/encoding damage in formulas, symbols, and some words. Main equations, tables, numerical outcomes, and page markers were readable; exact formula typography should be checked against the PDF if needed.

## 7. Final quality check

### Reasoning
The route explains why the paper uses ensemble scenarios, separates forecast and unpredicted time, carries end-state dependence into residual risk, and compares risk with hydropower benefit.

### Execution
The route follows forecast generation, reservoir routing, threshold counting, post-horizon design-flood routing, risk recombination, optimization, and case comparison. It records control branches and the reported checks.

### Evidence
Rows are traceable to pages, equations, figures, and tables. Model outputs, risk proxies, comparisons, and case-specific claims are bounded; unsupported deployment claims are not added.

### Reusability
Potentially recurring abstractions include ensemble-scenario construction, forecast-boundary risk decomposition, conditional post-horizon routing, any-crossing failure counting, and risk–benefit policy comparison. TGR data, 2010 flood, threshold values, hydrologic parameters, and optimized outputs are paper-specific.
