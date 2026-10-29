# E41 Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: Jiang, Zhiqiang; Sun, Ping; Ji, Changming; Zhou, Jianzhong (2015). “Credibility theory based dynamic control bound optimization for reservoir flood limited water level.” *Journal of Hydrology*, 529, 928–939. DOI: 10.1016/j.jhydrol.2015.09.012. Source: [E41 text](../text/E41.txt). Reading scope: supplied text pages 1–12, including Sections 1–5, Figures 1–14, Tables 1–6, and the reported references. Page references use supplied PDF page markers. The OCR text has mojibake and equation-formatting corruption; definitions and numeric settings were retained only when unambiguous.

## Paper identification

The paper optimizes the upper bound of a dynamic flood-limited water level (FLWL) for FENGTAN Reservoir. It models flood-volume forecast error as a fuzzy variable with a Cauchy membership function, imposes credibility-based chance constraints on flood-regulation outcomes, solves them by fuzzy simulation across design-flood frequencies, and divides the flood season into three stages. It compares the resulting credibility-based risk with an extreme-risk calculation.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | Determine how high the initial operation water level (IOWL), as the upper limit of a dynamic FLWL bound, can be raised in each flood-season stage without exceeding the reservoir’s flood-control standard. | pp. 1–5, Sections 1 and 3.2–3.3; pp. 6–8, Section 4.2. |
| Method overview | Represent relative flood-volume forecast error as a fuzzy Cauchy variable, optimize IOWL with credibility chance constraints, and evaluate each candidate through fuzzy simulation over 14 design-flood frequencies and routed hydrographs. | pp. 3–7, Eqs. (5)–(12), Fig. 4. |
| Research significance | The FENGTAN case yields upper dynamic-control bounds of 202.5 m in May, 200.5 m in June–July, and 204 m in August–September, corresponding to increases of 4, 2, and 5.5 m over the original 198.5 m level while staying below the 0.1% standard in the reported checks. | pp. 7–11, Tables 4–6, Fig. 14 and conclusions. |

## 2. How the authors reason

Reasoning overview: A single FLWL can be too low for conservation or too high for flood safety because seasonal flood characteristics vary. The authors therefore seek a stage-specific upper bound. Forecast error is treated as fuzziness rather than randomness, because incomplete knowledge and subjective vagueness are considered relevant; credibility is selected over possibility because it is self-dual and interpreted as a confidence measure. The upper bound is chosen by maximizing IOWL subject to a credibility-based exceedance measure no greater than the design-flood frequency. FENGTAN’s flood season is split into May, June–July, and August–September so the resulting bounds reflect differing flood characteristics. Extreme-risk rates are then used as a separate plausibility check. The claim is a model-based case result; it does not establish performance under unmodeled hydrograph-shape uncertainty or deployment.

Reconstructed route: (1) identify the fixed FLWL/conservation trade-off; (2) choose fuzzy credibility for forecast error; (3) define a fuzzy chance-constrained IOWL maximization; (4) sample candidate IOWLs, flood frequencies, and fuzzy error realizations; (5) route zoomed design hydrographs and calculate exceedance credibility; (6) integrate/aggregate the credibility curve over frequencies and compare with the design standard; (7) select the highest feasible IOWL per season stage; and (8) compare with extreme-risk rates.

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. Make FLWL stage-specific | A whole-season fixed FLWL either reserves too much capacity and sacrifices benefits or is too high for flood prevention. Seasonal flood magnitude and timing differ. | **Trigger:** balance flood safety and conservation over a season. **Inputs:** seasonal rainfall, peaks, runoff, flood control standard. **Judgment/procedure:** divide the season and allow dynamic bounds with original FLWL as lower limit. **Output:** stage-specific upper-bound problem. | pp. 1–2 and 6–8, Sections 1 and 4.2.1; Table 2. |
| R2. Represent forecast error as fuzzy uncertainty | The authors distinguish randomness from fuzziness and argue that forecast error contains vagueness not fully represented by a probability distribution. Credibility is chosen because it is self-dual and gives differentiated confidence values. | **Trigger:** optimize FLWL under imprecise forecast error. **Inputs:** historical relative flood-volume forecast errors. **Judgment/procedure:** use a fuzzy variable with Cauchy membership; use credibility rather than possibility. **Output:** credibility distribution and chance constraint. | pp. 2–4, Section 2 and Section 3.1, Eqs. (1)–(7). Membership-function selection is partly judgmental and based on limited data. |
| R3. Formulate a safety-constrained benefit objective | Raising IOWL increases potential conservation/power benefit, but the maximum regulated level must remain below design flood level with specified credibility. | **Trigger:** choose the upper dynamic-control bound. **Inputs:** candidate IOWL, design level/storage, forecast-error variable, credibility limits. **Judgment/procedure:** maximize IOWL subject to Cr{Vmax ≥ Vdesign} ≤ α or Cr{Zmax ≥ Zdesign} ≤ α, plus downstream discharge constraint where applicable. **Output:** feasible optimum. | pp. 4–5, Section 3.2, Eqs. (8)–(11). α and β are stated as specified credibility values; the case applies the 0.1% flood standard. |
| R4. Use dense frequency coverage and fuzzy simulation | The credibility of exceedance must account for possible flood frequencies, and the routing function is too nonlinear for a closed-form fuzzy program. | **Trigger:** evaluate a candidate IOWL under uncertain forecast error. **Inputs:** candidate frequencies, design hydrographs, d-level cut samples, routing model. **Judgment/procedure:** use 14 frequency levels, sample errors from cut sets, route each zoomed hydrograph, calculate credibility curve and area K. **Output:** K for each IOWL/stage. | pp. 5–7, Section 3.3, Fig. 2–4; frequency list on p. 6. The authors state fine frequency division is important. |
| R5. Select the highest feasible IOWL per stage | K is compared with the design flood frequency; the highest IOWL whose K does not exceed the standard is selected conservatively. | **Trigger:** candidate K values are available. **Inputs:** K versus IOWL, Pdesign = 0.1%. **Judgment/procedure:** choose the largest feasible candidate; e.g., 202.5 m gives K = 0.0977% while 203 m gives 0.1040% in May. **Output:** upper dynamic bound. | pp. 7–8, Table 4–5, Fig. 11–14. The selection is grid-based over listed candidate levels. |
| R6. Check credibility results against extreme risk | Reservoir safety is treated as the primary concern, so an alternative extreme-risk calculation is used to test whether selected bounds remain below the standard. | **Trigger:** credibility-based bound needs a safety plausibility check. **Inputs:** selected IOWL, routed maximum-level distribution, Zdesign. **Judgment/procedure:** find frequency Pe at which maximum routed level reaches Zdesign; compare Pe with K and 0.1%. **Output:** verification table. | pp. 9–11, Eq. (13), Table 6. The paper calls this verification of rationality/feasibility, but it is not an independent observed-event validation. |

## 3. How the authors execute

Execution overview: Historical FENGTAN data define three seasonal stages and 26 forecast-error observations. The authors compare triangular and Cauchy membership functions and choose Cauchy based on fit/shape arguments. For each candidate IOWL and each of 14 flood frequencies, they sample error values from fuzzy d-level cuts, scale a typical design hydrograph by the error-adjusted forecast volume, perform flood regulation, and calculate credibility that maximum level/storage exceeds design. The area under the credibility-versus-frequency curve is K. The largest IOWL with K ≤ 0.1% is selected for each stage, then checked through an extreme-risk-rate calculation.

Reconstructed workflow: seasonal data/stage definition -> design-flood hydrograph construction -> error membership model -> candidate IOWL grid -> fuzzy error sampling and hydrograph scaling -> flood routing -> credibility curves and K -> stage-bound selection -> extreme-risk comparison.

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. Divide the flood season and prepare design floods | Use historical climate, rainfall, peak, and runoff characteristics to define May, June–July, and August–September stages. | **Trigger:** dynamic bounds must reflect seasonal flood behavior. **Inputs:** FENGTAN hydrologic history, representative 1995/5, 2003/7, and 1998/8 floods. **Procedure:** apply homogeneous frequency enlargement to generate DFHs at 14 frequencies: 0.01%, 0.02%, 0.05%, 0.1%, 0.125%, 0.2%, 0.25%, 0.4%, 0.5%, 0.6%, 0.7%, 0.8%, 0.9%, and 1%. **Output:** stage-specific DFH sets. | pp. 6–7, Section 4.2.1, Table 2, Figs. 6–8. Original FLWL/lower bound is 198.5 m; design level is 209.56 m at P = 0.1%. |
| E2. Quantify forecast error as a fuzzy variable | Compute relative volume error from actual and forecast flood volumes and construct triangular and Cauchy membership functions. | **Trigger:** define uncertainty input to chance constraints. **Inputs:** 26 floods since 2009, relative volume errors. **Procedure:** use e = (Wforecast − Wactual)/Wforecast × 100%; compare triangular parameters (−20, −4.33, 20) with Cauchy using average errors Ew+ = 0.086 and Ew− = −0.094 and weighting factor r = 2.333. **Output:** Cauchy membership/credibility distribution. | pp. 3–4, 6, Section 3.1 and Table 3/Figs. 9–10. The choice is based on limited observations and reported shape/stability considerations; no independent calibration is reported. |
| E3. Generate candidate IOWLs | Search a feasible grid above the original FLWL. | **Trigger:** numerical optimization is performed by sampling candidates. **Inputs:** original FLWL, feasible flood-regulation range. **Procedure:** evaluate 198.5, 199, 199.5, 200, 200.5, 201, 201.5, 202, 202.5, 203, 203.5, 204, and 205 m. **Output:** candidate IOWL set. | pp. 6–7, Section 4.2.3. The candidate grid and bounds are explicit; a continuous optimum between grid points is not computed. |
| E4. Run fuzzy simulation for each IOWL/frequency | Sample fuzzy error values and route adjusted design floods. | **Trigger:** one candidate IOWL and one design frequency are selected. **Inputs:** Wforecast, error samples ek from d-level cuts, DFH, IOWL, reservoir regulation model. **Procedure:** scale DFH by Wforecast(1 − ek/100), route from IOWL, obtain Vmax/Zmax/Qmax, evaluate membership and f(n(ek)), and repeat for N samples. **Output:** one credibility point for the frequency. | pp. 4–5, Section 3.3, Steps 1–9, Eqs. (9)–(12). Fuzzy simulation uses a stated large N but the numeric N is not given in the supplied text. |
| E5. Form K and test feasibility | Repeat across 14 frequencies, plot credibility against frequency, and calculate the area K. | **Trigger:** all sampled credibility points for a candidate are available. **Inputs:** Cr{f(n) ≥ 0} curve, frequency grid, design standard. **Procedure:** integrate/area-sum curve with coordinate axis; accept if K ≤ Pdesign. **Output:** feasible/infeasible candidate and stage-level risk measure. | pp. 5–7, Fig. 2–4 and Table 4. K is interpreted as credibility of exceedance over all possible flood frequencies; exact numerical integration method is not reported. |
| E6. Select stage bounds | Choose the largest feasible IOWL separately for each seasonal stage. | **Trigger:** K values for all candidates are available. **Inputs:** Table 4 K values and Pdesign = 0.1%. **Procedure:** May: select 202.5 m (0.0977% vs 203 m at 0.1040%); June–July: select 200.5 m (0.0990%); August–September: select 204 m (0.0981%). **Output:** dynamic bounds in Table 5/Fig. 14. | pp. 7–8, Tables 4–5, Fig. 14. The procedure is conservative relative to the discrete candidate grid. |
| E7. Verify with extreme-risk rate | For each IOWL, route floods of varying frequencies and find the frequency at which Zmax reaches 209.56 m. | **Trigger:** independently check the selected bounds. **Inputs:** routed maximum levels, Zdesign, frequency curve. **Procedure:** compute Pe = integral from Zdesign to infinity of f(Zmax) dZmax / equivalent frequency crossing; compare selected levels with K. **Output:** Table 6 extreme-risk rates and consistency statement. | pp. 9–11, Eq. (13), Table 6. Selected extreme rates are 0.09836% (May, 202.5 m), 0.09972% (June–July, 200.5 m), and 0.09813% (Aug–Sept, 204 m). |

Extraction conventions: R/E sequence is reconstructed from explicit methods and case results. Human review: awaiting review; no reviewer feedback supplied. Single-paper extraction does not establish recurring patterns or validate a skill collection.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| R1/E1 | Partition an operating season into regimes with distinct flood characteristics. | FENGTAN: May, June–July, August–September; homogeneous frequency enlargement of three representative floods. |
| R2/E2 | Convert forecast error with incomplete knowledge into a graded uncertainty representation. | Cauchy membership function fitted to 26 relative flood-volume errors; credibility distribution used in constraints. |
| R3/E3–E5 | Search a control-bound candidate against a risk-area criterion. | IOWL grid 198.5–205 m; fuzzy simulation over 14 frequencies; K compared with 0.1%. |
| R4/E4 | Propagate an uncertain flood-volume adjustment through flood regulation. | Scale each DFH using Wforecast(1 − e/100), route from candidate IOWL, calculate maximum level/storage/discharge. |
| R5/E6–E7 | Select the highest feasible bound and perform an alternate risk check. | Stage bounds 202.5/200.5/204 m; extreme-risk rates compared with credibility values. |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | Credibility K and extreme-risk rate represent modeled frequencies/credibilities of exceeding the design level. | They are not observed damage, overtopping, or economic-loss outcomes. |
| Model/simulation result versus deployment | Fuzzy simulation and flood routing show case-specific feasible IOWLs. | No operational deployment, operator authorization, or post-event performance evidence is reported. |
| Sensitivity/comparison versus independent validation | Triangular versus Cauchy membership shapes are compared; credibility bounds are checked against extreme-risk rates. | The alternative check uses related routing/model assumptions and is not independent empirical validation; no parameter sensitivity is reported. |
| Assumption versus calibration | 26 forecast-error observations inform average errors; DFHs and stage division use historical data. | Cauchy membership choice, weighting factor, fuzzy sampling settings, flood-shape preservation, and stage-level transfer of errors involve assumptions or incomplete calibration. |
| Case result versus general rule | FENGTAN stage-specific bounds meet the reported 0.1% standard under the model. | The bounds are not established for other reservoirs or for unmodeled forecast-volume/shape uncertainties. |

## 6. Unreported or unresolved items

- The numerical sample size N, d-level value, random-seed/convergence procedure, and numerical integration method for K are not reported.
- The exact flood-regulation routing equations/constraints and downstream safety handling are not fully reproduced in the supplied text.
- Only flood-volume forecast error is considered; flood peak, hydrograph shape, lag, model, and observation uncertainties are explicitly left for future work.
- The method used to estimate Cauchy membership parameters and the basis for r = 2.333 are only partly described/referenced.
- The candidate IOWL grid means an exact continuous optimum is not established.
- Real-time trigger, operator authorization, fallback action, and post-event learning procedures are not reported.
- The source text contains OCR/encoding corruption in equations and symbols. Major numeric tables, stage definitions, and conclusions were readable; exact formula typography should be checked against the PDF when needed.

## 7. Final quality check

### Reasoning
The route explains the seasonal FLWL trade-off, why credibility theory is chosen, how chance constraints define feasibility, and why extreme-risk calculations are used as a check.

### Execution
The route follows seasonal data preparation, fuzzy error construction, candidate search, frequency-by-frequency routing, K calculation, bound selection, and alternative risk checking. Inputs, procedures, outputs, and branches are recorded.

### Evidence
Rows cite pages, equations, figures, and tables. Modeled credibility/risk is distinguished from real consequences, related comparison from independent validation, and FENGTAN results from general rules.

### Reusability
Potentially recurring abstractions include seasonal regime partitioning, uncertainty representation by membership functions, chance-constrained control-bound search, uncertainty propagation through routing, and alternate risk verification. FENGTAN levels, 26-error sample, stage floods, Cauchy parameters, and final bounds are paper-specific.
