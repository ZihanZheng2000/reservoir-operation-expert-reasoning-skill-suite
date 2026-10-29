# E08 Three-Layer Extraction

Topic: **Reservoir operation adjustment for flood risk management**.

Citation: Lu, Q., Zhong, P.-a., Xu, B., Zhu, F., Ma, Y., Wang, H., & Xu, S. (2020), “Risk analysis for reservoir flood control operation considering two-dimensional uncertainties based on Bayesian network,” *Journal of Hydrology*, 589, 125353, DOI: 10.1016/j.jhydrol.2020.125353. Source: [E08.txt](../text/E08.txt). Page references use PDF page numbers. Reading scope: pp. 1–13, including §§1–5 and Appendices A–B; figures were used only through text/captions.

## Paper identification

The paper studies dynamic control of the flood-limited water level (DC-FLWL) at Xianghongdian Reservoir under uncertainty in initial storage and forecast inflows. It builds a Bayesian network (BN) from expert-specified routing structure and Monte Carlo/LHS training samples, then performs predictive and diagnostic risk inference. The supplied page-separated text is the complete article; references use PDF pages.

## 1. What the paper does

| Element | Extraction | Evidence |
|---|---|---|
| Research object and problem | Forecast-based pre-refill/pre-release can improve flood-season water use but creates risk when initial water level and flood forecasts are uncertain. The study quantifies reservoir and downstream flood risk and the interaction of these two uncertainty sources. | pp. 1–3, §§1–2. |
| Method overview | Derive the distribution of excess storage, construct a BN whose nodes follow reservoir water-balance/routing relations, learn conditional probabilities from 1,000 sampled optimal-routing cases, and infer risks from prior or observed posterior information. | pp. 2–6, §§2–3.3, §4.2. |
| Research significance | The Xianghongdian case indicates forecast inflow uncertainty dominates initial-level uncertainty and that BN can support bidirectional risk assessment. Results remain a single 100-year-design-flood case study under specified distribution and discretization assumptions. | pp. 6–10, §§4.3–5. |

## 2. How the authors reason

Reasoning overview: The authors identify a conflict between keeping storage below the flood-limited level and retaining floodwater for water-use benefits. Because pre-release decisions depend on uncertain recession duration, initial storage, and forecast inflows, they represent both uncertainty sources jointly. A BN is selected because the routing dependencies are explicit and its factorization makes joint risk inference tractable, while posterior inference can update risk when observed outcomes arrive. The reasoning stops at modeled probabilities; it does not establish a deployed control policy.

Reconstructed route: Define the two uncertainty sources and omit discharge-capacity and storage-curve uncertainty; derive initial-storage and inflow distributions; map water-balance dependencies into BN nodes; generate constrained optimal-routing samples and learn/discretize the BN; compute prior risk and compare with Monte Carlo; condition prediction on causes or diagnosis on consequences; compare one-factor and two-factor cases and test evidence levels.

| Step | Reasoning and justification in the paper | Details retained for potential reasoning micro-skills | Evidence and boundaries |
|---|---|---|---|
| R1. Frame the DC-FLWL trade-off and uncertainty scope | Pre-refill/pre-release can increase floodwater utilization but forecast error may cause FLWL exceedance. The paper focuses on initial water-level uncertainty and flood-forecast error as primary risk sources. | **Trigger:** Consider operating above/around the design FLWL during a flood season. **Inputs:** Recession/rainless-day forecast, forecast inflows, current storage, downstream safety discharge. **Judgment/procedure:** Include the two uncertainty sources jointly; exclude discharge capacity and storage-curve uncertainty by scope choice. **Branches:** Initial-level only, inflow only, or both factors. **Output:** Defined stochastic risk problem. | §§1–2, pp. 1–3. Exclusions are explicit; extractor does not infer omitted factors are negligible. |
| R2. Derive distributions for initial storage and forecast inflows | Excess storage consists of pre-release water for floodwater use and flood-control pre-release. Its distribution determines the uncertain initial storage of the next flood. | **Trigger:** Build probabilistic initial conditions. **Inputs:** Rainless-day error, average recession flow, early-flood inflow, forecast-error distributions, safety discharge. **Judgment/procedure:** Use improved truncated Gaussian for rainless-day error and normal relative error for flood inflow; combine excess-storage terms and transform W to V0. **Branches:** Rainless-day horizons 1–7; one-factor versus joint uncertainty. **Output:** Density of V0 and stochastic Q/IU inputs. | §§2.1–2.2, Eqs. (1)–(6), pp. 2–3, Appendices A–B. Independence of weather and flood forecast errors is an assumption. |
| R3. Choose an interpretable dependency representation | Routing equations explicitly define how storage, levels, outflow, lateral inflow, and downstream flow depend on one another, so the BN graph can encode those relations. | **Trigger:** Represent the joint distribution without handling one high-dimensional PDF directly. **Inputs:** Reservoir balance and downstream routing equations. **Judgment/procedure:** Use expert knowledge for DAG structure; represent period-average flow variables and connect parent/child variables according to Eqs. (8)–(9). **Output:** BN structure. | §3.2.1, pp. 3–4, Fig. 3. Structure is expert-specified rather than structure-learned from data. |
| R4. Generate and discretize training evidence | BN parameters require samples spanning uncertain inputs and feasible operation outcomes. | **Trigger:** Learn conditional probability tables. **Inputs:** V0 distribution, LHS samples of reservoir/lateral inflows, routing constraints. **Judgment/procedure:** Solve an optimal flood-control model minimizing maximum outflow subject to water balance, level/outflow/discharge and ramping constraints; discretize continuous variables with equal-distance intervals and select K considering precision, samples, and cost. **Output:** Sampled V, H, q, QC and discretized training data. | §3.2.2, p. 4; case uses 1,000 samples (p. 5). The paper notes K sensitivity can be checked but does not give a complete selection protocol. |
| R5. Learn BN and select inference direction | The BN can answer both forward risk questions and reverse diagnosis questions from observed consequences. | **Trigger:** Need risk probabilities or likely causes. **Inputs:** Discretized complete samples and, for posterior queries, evidence variables. **Judgment/procedure:** Estimate CPTs by MLE; use prior inference without evidence, prediction given V0/Qmax/IUmax, or diagnosis given Hmax/QCmax using Bayes/joint-tree propagation. **Branches:** Prior, cause-to-effect, effect-to-cause. **Output:** Probability distributions of query nodes. | §§3.2.2–3.2.3, pp. 4–5. No claim that posterior inference itself authorizes a release. |
| R6. Convert distributions into risk and assess uncertainty interactions | Flood risk is the cumulative probability that reservoir level or downstream flow exceeds its safety threshold. Comparing cases reveals which uncertainty drives modeled risk. | **Trigger:** Interpret inferred distributions for decision support. **Inputs:** BN distributions, Hs and QCs, uncertainty cases and evidence levels L1–L3. **Judgment/procedure:** Sum probabilities above thresholds; compare BN with MC and compare one-/two-factor cases, forecast horizons, and evidence levels. **Branches:** Reservoir risk versus downstream risk; predictive versus diagnostic analysis. **Output:** Risk curves, posterior ranges, and factor attribution. | Eqs. (13)–(14), pp. 5–10, Figs. 7–16. Conclusions are case-bounded; apparent compensation is a modeled interaction. |

## 3. How the authors execute

Execution overview: The paper first derives probability distributions for excess storage and inflow errors, then samples uncertain inputs and solves a constrained flood-routing optimization to generate training outcomes. A BN is built, discretized, and fit by MLE. Prior and posterior propagation produces node distributions, from which threshold-exceedance risks are calculated. Xianghongdian is evaluated with a 100-year return-period flood, 1-hour intervals, 1,000 training samples, and three uncertainty cases; MC comparison and evidence-level prediction/diagnosis are evaluation branches.

Reconstructed workflow: derive input distributions → sample V0/Q/IU → solve minimum-maximum-outflow constrained routing → collect V/H/q/QC samples → discretize and fit BN → run prior risk inference → run predictive/diagnostic posterior inference under L1–L3 → compare risk curves and infer applicability.

| Step | What the authors do | Inputs, procedures, and outputs retained for potential execution micro-skills | Checks, conditions, and evidence |
|---|---|---|---|
| E1. Compute uncertain initial conditions | Transform excess storage W into the next-flood initial storage V0. | **Trigger:** Forecast-based floodwater utilization precedes the next flood. **Inputs:** Rainless-day forecast error, pre-release terms, Vx and Ws. **Procedure:** Use Eqs. (1)–(4) and Appendix A–B distributions; evaluate horizons 1–7. **Output:** V0 density and samples. | Xianghongdian uses α0=0.8 and B-level forecast accuracy; detailed parameter assumptions appear pp. 5 and 11–13. |
| E2. Specify uncertain routing inputs | Represent forecasted reservoir and lateral inflow with relative normal errors. | **Trigger:** Build a stochastic flood case. **Inputs:** Forecast Q(t), IU(t), error standard deviation σ=0.19, 100-year flood hydrograph. **Procedure:** Sample Q and IU; in the case, time interval is 1 hour. **Output:** Stochastic inflow sample pairs. | The paper derives σ from 70% probability within 20% error for B-level accuracy (p. 5); discharge capacity and level-storage uncertainty are omitted by design. |
| E3. Generate feasible operation samples | Solve the flood-control model for each sampled input. | **Trigger:** Need BN outcome data. **Inputs:** V0, Q, IU samples; level, outflow, capacity, and ramping constraints. **Procedure:** Minimize maximum reservoir outflow subject to Eq. (10); derive V, H, q and downstream QC using Eq. (9). **Output:** 1,000 simulated training records per case. | Three cases use V0 and Q/IU as deterministic or random as specified on p. 5. This is a training/evaluation optimization, not a demonstrated real-time controller. |
| E4. Build and fit BN | Encode routing dependencies and estimate conditional probabilities. | **Trigger:** Training records available. **Inputs:** Nodes V0/V1, H0/H1, Q, q, IU, QC; discretization range and K. **Procedure:** Use expert DAG, equal-distance discretization, then MLE CPT fitting. **Output:** Trained BN for each uncertainty case. | K trades precision against computation; optional sensitivity to K is suggested, not fully reported (p. 4). |
| E5. Perform prior risk inference | Propagate the trained BN without posterior evidence. | **Trigger:** Need baseline probability distributions. **Inputs:** Trained BN, safety level Hs, safety flow QCs. **Procedure:** Infer maximum H and QC distributions and sum probabilities exceeding thresholds using Eqs. (13)–(14). **Output:** Reservoir/downstream risk curves by rainless-day horizon and uncertainty case. | BN prior results match MC for case 1 in the reported example (p. 6, Fig. 7), supporting the implemented inference for that check. |
| E6. Perform posterior prediction or diagnosis | Update risk or infer possible causes after evidence is supplied. | **Trigger:** New forecast/state evidence or observed maximum levels/flows. **Inputs:** L1–L3 values for V0, Qmax, IUmax, Hmax, QCmax. **Procedure:** Prediction infers H/QC from causes; diagnosis infers V0/Qmax/IUmax from Hmax/QCmax via joint-tree propagation. **Output:** Posterior distributions, risk increments, and likely uncertainty-source ranges. | Evidence definitions and values are given in Table 1 and pp. 8–10. Higher evidence levels widen or concentrate distributions depending on case; these are simulated posterior patterns. |
| E7. Compare and interpret risk | Attribute risk to uncertainty sources and assess BN usefulness. | **Trigger:** Complete prior/posterior runs. **Inputs:** Cases 1–3, L1–L3, MC comparator, risk curves/tables. **Procedure:** Compare forecast-only, initial-level-only, and joint risks; inspect trends with forecast horizon and evidence magnitude. **Output:** Finding that inflow uncertainty is dominant and BN permits bidirectional updating. | Results are for Xianghongdian and one 100-year design flood; no field deployment or independent validation is reported (pp. 6–10). |

Extraction conventions: Step labels/order are the extractor’s reconstruction from identifiable evidence. The BN is a risk-analysis and decision-support model; the paper does not report a complete operational release authorization or fallback policy.

Micro-skill convention: Rows preserve triggers, inputs, procedures, outputs, branches, and checks for later cross-paper synthesis; this note does not declare a final skill set.

Human review: Awaiting review; no reviewer/date/feedback supplied.

## 4. Functional abstraction and paper-specific realization

| Important step | Functional abstraction | Paper-specific realization |
|---|---|---|
| R1/E1 | Represent operational uncertainty in initial state and future forcing. | Improved truncated-Gaussian rainless-day error, normal inflow relative errors, excess storage W, transformed V0. |
| R3/E4 | Encode physical dependency graph and learn probabilistic outcomes from feasible simulations. | Expert DAG from reservoir/downstream balance, 1,000 MC/LHS samples, constrained min-max-outflow model, equal-distance discretization, MLE CPTs. |
| R5/E5 | Propagate uncertainty to threshold-exceedance risk. | BN prior distributions and Eqs. (13)–(14) for Hs/QCs at Xianghongdian. |
| R5/E6 | Update risk forward from causes or diagnose causes from consequences. | Prediction given V0/Qmax/IUmax; diagnosis given Hmax/QCmax; joint-tree propagation under L1–L3. |
| R6/E7 | Compare uncertainty scenarios and check computational inference against a sampling reference. | Cases 1–3, horizons 1–7, BN versus MC case-1 comparison, risk curves/tables. |

## 5. Evidence and inference audit

| Audit item | Supported by the paper | Boundary or unsupported extension |
|---|---|---|
| Proxy indicators versus real consequences | Maximum reservoir water level, downstream flow, and threshold-exceedance probabilities are modeled flood-risk indicators. | They do not directly establish physical damages, warning outcomes, or downstream impacts. |
| Model/simulation result versus deployment | BN is trained and tested using simulated routing samples for Xianghongdian. | No deployed real-time BN, operator trial, or observed-event validation is reported. |
| Sensitivity/comparison versus independent validation | BN/MC comparison, uncertainty cases, forecast horizons, evidence levels, and some discretization discussion are provided. | MC samples come from the same modeled assumptions; no independent temporal or event validation is shown. |
| Assumption versus calibration | Normal forecast errors, independence of two pre-release components, B-level accuracy, α0=0.8, 1,000 samples, equal-distance bins, and 100-year flood are assumptions/settings; MLE estimates CPTs from generated data. | Full K value, parameter estimation history, error dependence checks, and operational recalibration are not reported. |
| Case result versus general rule | In this case, inflow forecast uncertainty contributes more risk than initial storage uncertainty, and joint risk lies between single-factor cases. | The interaction and ranking may change with reservoir, forecast model, flood shape, constraints, and distributions; no universal rule is established. |

## 6. Unreported or unresolved items

- Exact BN graph, all node-state boundaries, chosen K values, CPT sizes, and numerical parameter tables are not fully recoverable from the supplied text/figures.
- The paper states 1,000 samples but does not report convergence, random seeds, or a systematic independent test set.
- Forecast-error independence and normality assumptions are not empirically stress-tested in the article; discharge-capacity and storage-curve uncertainty are excluded.
- The optimal routing model generates training outcomes, but a procedure for converting posterior risk into an actual release adjustment, escalation, or fallback is not reported.
- Real-time data latency, missing forecasts, model failure, and post-event updating are described as prospects rather than implemented operations.

## 7. Final quality check

### Reasoning
The route explains the trade-off, uncertainty selection, BN choice, inference direction, and factor-comparison logic while distinguishing explicit statements from reconstruction.

### Execution
The route follows distribution derivation through sampling, constrained routing, BN fitting, inference, risk calculation, and evaluation branches, retaining inputs, outputs, and checks.

### Evidence
Rows cite supplied PDF pages/sections/equations/tables; risk indicators are separated from consequences, simulation from deployment, and assumptions from fitted CPTs.

### Reusability
Potentially recurring abstractions include uncertainty decomposition, probabilistic dependency modeling, feasible-simulation training, threshold-risk calculation, bidirectional inference, and BN/MC checking. Xianghongdian values, 100-year flood, distributions, discretization, and case findings are paper-specific.

