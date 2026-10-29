# Joint flood operation of Guxian and Luhun under forecast error: plan and provisional judgments

## 1. Provisional answers

1. **How much forecast error changes the expected reservoir levels.** For the 18 September 2021 event, my provisional judgment is that forecast error will change each reservoir's *maximum* level by a moderate amount, roughly decimetres to about a metre at the upper tail. It will not threaten the flood-control zone, because each reservoir's event volume is a fraction of its flood-control storage (see Section 3). Its effects on the *end-of-event level* and on the *Heishiguan peak* are likely larger and matter more for decisions. If a plan built on one deterministic forecast is executed without updating, an under-forecast leaves water above the flood-limit level that must be released into a recession already loaded by the other reservoir. An over-forecast leads to early over-release, which raises Heishiguan flows for no benefit and can leave a reservoir below the flood-limit level when the event ends. I will put numbers on these effects, as distributions and not single values, through the simulation in Section 4.
2. **Whether simple error assumptions understate the risk.** Provisionally, yes, and by a material factor. The usual assumption is zero-mean normal error with a constant relative spread, independent between time steps and between the two reservoirs. The forecast errors here are almost certainly (a) larger in relative terms at high flows than the archive's mostly sub-500 m³/s sample suggests, (b) strongly correlated across consecutive 6-h steps, because a deterministic model that misjudges a storm misjudges it for many hours, and (c) correlated between Lushi and Dongwan, because both forecasts use the same 2021 precipitation. Under illustrative values, treating correlated errors as independent understates the spread of flood-volume error by a factor of about 2.5 (Section 4.3). For storage, volume error matters more than error at a single peak.
3. **How to coordinate releases.** Guxian peaks about 20 h (about 3.3 decision steps) before Luhun. The coordination principle is to stagger, not to minimise each release separately:
   - Guxian stores hard while its own peak passes.
   - Luhun uses the lead time before its later peak for a limited pre-release, within the 3 m drawdown limit and the ramp limits, timed so that it reaches Heishiguan *before* Guxian's attenuated contribution does.
   - Luhun then stores through its own peak, while Guxian holds its release rather than starting evacuation.
   - Both reservoirs evacuate in a staggered recession, so that the combined Heishiguan flow stays at or below the controlled peak and no second peak forms.
   
   The return-to-flood-limit requirement is a central constraint, not a detail. It forces every stored cubic metre to pass Heishiguan within the event window, so it sets a floor on how low the Heishiguan peak can go.
4. **Picking one option.** Generate a non-dominated set of release schedules, evaluated over an ensemble of error scenarios. Then choose in four steps:
   - (i) Screen each option on hard safety: dam-safety level limit, end-level tolerance, release capacity, ramp and drawdown limits, and the Heishiguan safe discharge. Use the upper tail of each risk, not its mean.
   - (ii) Drop dominated options.
   - (iii) Merge options whose differences are within simulation and error-model uncertainty.
   - (iv) Rank the rest with explicit, published weights, and show that the ranking is stable when the weights and the error model change.
   
   The final choice goes to the responsible flood-control authority for consultation and approval.

## 2. The questions that decide the answer

- **A. How do forecast errors behave at flows of 1,000 to 2,700 m³/s, when the archive holds almost no such flows?** The answers to research questions 1 and 2 depend almost entirely on this extrapolation.
- **B. Which constraint actually binds: flood storage, release capacity at the current level, ramp limits, or the return-to-flood-limit requirement within the event window?** This decides whether "reservoir safety" means level rise or evacuation feasibility, and so what the coordination has to protect.
- **C. When does each reservoir's release reach Heishiguan, and when does local inflow arrive?** Staggering only works if the release timings at the confluence are known. A 20-h gap between inflow peaks at the dams is not the same as a 20-h gap at Heishiguan.

## 3. Mass balance first: what is at stake

**Event volumes against storage.**

| | Guxian | Luhun |
|---|---|---|
| Event inflow volume | 252.8 Mm³ | 154.2 Mm³ |
| Flood-control storage | > 1,000 Mm³ | > 1,000 Mm³ |
| Volume as share of flood storage | < 25% | < 15% |

Even if a reservoir stored its *whole* event volume, it would use less than a quarter of its flood-control zone. Forecast error cannot exhaust the flood-control zone for this event. The brief says reservoir safety conflicts with downstream protection. That conflict must therefore come from one or more of these:
- a reservoir-side level threshold below the top of the flood-control zone (for example, an operating ceiling during the event);
- release capacity that is limited at low heads;
- the requirement to return to the flood-limit level within the event window.

I would confirm which one with the agency before setting objectives. Until then I treat the maximum level and the end-level deviation as reservoir-side criteria, alongside capacity and ramp feasibility.

**The return-to-flood-limit constraint sets a floor on the Heishiguan peak.** Both reservoirs start and end at the flood-limit level, so the reservoirs' total release over the event equals their total inflow, 407 Mm³. Operation can only redistribute this volume in time. If the window from start to required return is T, the perfectly flattened reservoir contribution at Heishiguan is 407 Mm³ / T:
- T = 4 days: 407×10⁶ / 345,600 s ≈ 1,180 m³/s
- T = 5 days: ≈ 940 m³/s
- T = 6 days: ≈ 790 m³/s

Local inflow is added on top, and real ramp limits and timing push the achievable value higher. The length of the event window is therefore a policy variable as important as any release rule. I would report the Heishiguan peak against T explicitly.

**The evacuation time is the coupling.** Suppose Guxian holds about 120 Mm³ above the flood-limit level at its peak. This is an assumed planning value; the real figure comes from the optimisation. Suppose also that the Heishiguan allowance during recession is shared so that Guxian may release about 450 m³/s more than its recession inflow. Then evacuation takes 120×10⁶ / 450 ≈ 2.7×10⁵ s ≈ 74 h, or about 12 six-hour steps. Luhun's evacuation overlaps with this, so the two compete for the same Heishiguan allowance. That is why the recession must be scheduled jointly.

**Level effect of a volume error.** ΔZ ≈ ΔV / A, where A is the reservoir's surface area near the operating level, taken from the level-storage relation. As an illustration only, assume A = 50 km²; the real value comes from the level-storage curves. Then a 20 Mm³ error gives about 0.4 m and a 55 Mm³ error gives about 1.1 m. I would replace A with the slope of each level-storage curve over the relevant range.

## 4. Questions 1 and 2: how forecast error moves levels, and whether simple assumptions understate it

### 4.1 Check the forecast and the data before using them

- **Same forecast system.** The error archive at Lushi must come from the same deep-learning model, version, inputs and issue times that produced the 2021 forecasts. If it comes from an older or different forecast, its errors do not describe this forecast. If no matched archive exists, I would generate hindcasts with the current model over 2013–2020, using held-out years for the evaluation.
- **No archive at Dongwan.** There is no error archive for Luhun's forecast station. I would either build one from hindcasts, or transfer Lushi's error model to Dongwan and test that transfer as a sensitivity case. This is an assumption to state, not a fact.
- **What NSE > 0.95 means here.** NSE = 1 − MSE / var(obs), so RMSE ≈ √0.05 × sd(obs) ≈ 0.22 × sd(obs). This error is averaged over hydrographs dominated by low flows. It says little about error at the peak, in timing, or in flood volume, which are what drive storage. I would evaluate peak error, peak-timing error and volume error separately for each lead time.
- **Lead time.** Each forecast is issued at an upstream station. The usable lead time is the forecast horizon plus the travel time from the station to the dam. I would establish that lead time and compare it with what Luhun's pre-release needs. That pre-release must be completed, and its water must reach Heishiguan, before Guxian's attenuated peak arrives.
- **Interpolated observations.** The yearbook series were linearly interpolated to hourly values, which can clip peaks between reported points. I would check whether the 2021 peaks of 2,430 and 2,722 m³/s are reported values or interpolated ones. I would also aggregate to the 6-h decision step only after routing.

### 4.2 Error model: compare simple and realistic models directly

I define forecast error as relative error e = (Q_obs − Q_fc) / Q_fc, separately for each lead time in 6-h steps. I then build a ladder of error models, each adding one feature:

| Model | Marginal distribution | Dependence across lead times | Dependence between reservoirs |
|---|---|---|---|
| M0 (the "usual" assumption) | Normal, zero mean, one σ (from NSE or qualified rate) | Independent | Independent |
| M1 | Normal, σ grows with lead time and with flow level (heteroscedastic) | Independent | Independent |
| M2 | Best-fitting skewed or heavy-tailed marginal (screen normal, generalised logistic, mixture by AIC and K-S), conditioned on flow class | Independent | Independent |
| M3 | As M2 | Copula across lead times (t-copula, to allow tail dependence) | Independent |
| M4 | As M3 | As M3 | Lushi–Dongwan dependence (copula, or a shared rainfall-error factor) |

**Extrapolating to high flows.** Few archive flows exceed 1,000 m³/s, so an error distribution cannot be fitted directly in that range. Instead:
- Fit how σ and the bias depend on flow over the range where data exist (up to about 1,000 m³/s).
- Extrapolate that relationship, and carry the extrapolation factor as an explicit sensitivity parameter (for example 1×, 1.5× and 2× the extrapolated σ above 1,000 m³/s).
- Report how many independent flood events lie above 500 and above 1,000 m³/s. If there are about five, an observed error spread of ±40% at those flows has a sampling uncertainty comparable to its own size. No claim about the tail should rest on them alone.

**Checking the generated scenarios.** Before using any scenarios I check that each model reproduces the archive's error statistics, its lag correlations and its interval coverage (for example, what fraction of observations fall inside the 90% band). I also check the extreme events separately.

### 4.3 Order-of-magnitude estimate of the understatement (to be replaced by fitted values)

Take a rising limb plus peak of n = 8 six-hour steps (48 h), relative error σ = 0.15 per step at high flow, and lag correlation ρ = 0.8. These are illustrative values. Strong serial correlation is typical of a deterministic forecast that misjudges a storm.

- Variance of the summed error: nσ²(1 + (n−1)ρ) = nσ² × 6.6, against nσ² under independence.
- The spread of volume error is therefore √6.6 ≈ 2.6 times larger than independence implies.
- Relative volume error sd: σ√(6.6/8) ≈ 0.136, against σ/√8 ≈ 0.053.
- On Guxian's 253 Mm³: 1σ ≈ 34 Mm³ against 13 Mm³. The 95th percentile (1.645σ) is ≈ 57 Mm³ against 22 Mm³.
- With the illustrative A = 50 km², the 95th-percentile level error is ≈ 1.1 m against 0.4 m.

Correlation between the two reservoirs adds 2ρ_xy·σ_G·σ_L to the variance of the combined error at Heishiguan. This matters most for the downstream peak and for the shared recession allowance.

Heteroscedastic, heavy-tailed marginals widen the upper tail further. This holds only if high-flow errors are larger in relative terms than low-flow ones, which I expect but must verify.

### 4.4 Carrying the errors through to levels and Heishiguan flow

- **Simulator.** Run an hourly water balance for each reservoir, using the level-storage relation, release capacity as a function of level, the 6-h constant-release decision, ramp limits and the drawdown floor. Route each release to Heishiguan by Muskingum or by calibrated lag-and-attenuation, and add local inflow. Before any comparison, check the simulator against the observed 2021 levels and Heishiguan flows, given the recorded releases.
- **Scenarios.** Draw true inflows as Q_true = Q_fc(1 + e) from each error model M0–M4. Use about 10,000 scenarios per model when tail percentiles are to be compared: at p = 0.01 the binomial standard error is √(0.01×0.99/10,000) ≈ 0.001, or 10% relative, against 31% with 1,000 scenarios.
- **Two ways of executing the plan**, because they answer different questions:
  - **Open loop:** the schedule planned on the deterministic forecast is applied unchanged to each true inflow. Release capacity and the safety rule still override it if the level rises. This isolates how much a single-forecast plan exposes the reservoirs, and matches the current practice described in the brief.
  - **Closed loop:** every 6 h the plan is redone with an updated forecast and the actual state. This is the realistic exposure. The gap between the two is the value of updating.
- **Outputs**, per reservoir and per error model:
  - distribution of the maximum level, with mean, 95th and 99th percentiles, and CVaR of the worst 10%;
  - probability of exceeding the reservoir-side threshold;
  - distribution of the end-of-event level, and the probability of falling outside the tolerance on each side;
  - Heishiguan peak distribution, and time above the safe discharge.
- **The answer to question 2** is the difference in these tail measures between M0 and M3/M4, with the extrapolation factor varied. If M0 and M4 differ by less than the Monte Carlo standard error, the simple assumption is adequate for this event. I would state that result rather than force the opposite conclusion.

## 5. Question 3: coordinating releases on the 6-hour step

### 5.1 Representation

- **Decision variables:** releases R_G,t and R_L,t, held constant over each 6-h step.
- **State:** the storage of each reservoir.
- **Downstream flow:** Heishiguan flow = routed R_G + routed R_L + local inflow, computed hourly.
- **Constraints:**
  - each release ≤ capacity at the current level;
  - |R_t − R_{t−1}| ≤ the ramp limit for that reservoir;
  - level ≥ flood-limit level − 3 m;
  - end level = flood-limit level ± tolerance;
  - level ≤ the reservoir-side safety threshold, with an allowed exceedance probability.
- **Objectives**, kept separate and not summed into one score:
  - Heishiguan peak (expected value and CVaR across scenarios);
  - each reservoir's maximum level (CVaR and exceedance probability);
  - optionally, duration above the Heishiguan safe discharge, and end-level deviation, if it is not imposed as a hard constraint.

### 5.2 How the operation should proceed through the event (to be confirmed by optimisation)

1. **Before Guxian's peak.** Guxian makes at most a modest pre-release; its peak comes first, so its lead time is shortest. Luhun starts releasing early, using its roughly 20 extra hours of lead time, within the 3 m drawdown floor and the ramp limits. That water must reach Heishiguan before Guxian's attenuated peak does. Luhun's pre-release volume is capped by what it can be sure to recover from its own flood under a low-side forecast, so it still ends at the flood-limit level. It is also capped so that it does not raise Heishiguan above what the natural flood would have produced.
2. **Guxian's peak.** Guxian holds its release near the level that keeps Heishiguan at the target, storing most of its peak. Luhun reduces its pre-release as its own inflow rises.
3. **Luhun's peak.** Luhun stores, and Guxian does *not* start evacuating, so that the two contributions do not meet at Heishiguan. This step depends on the routed timings (question C). If the travel-time difference narrows the 20-h gap at Heishiguan to one or two steps, the roles shift towards more storage at both reservoirs together.
4. **Recession.** The two reservoirs evacuate in staggered order, with the Heishiguan allowance shared between them as in Section 3. Whichever reservoir holds more water, or is closer to its level threshold, goes first or gets the larger share. The combined Heishiguan flow is kept at or below the controlled peak, and each reservoir reaches its flood-limit level by the deadline.

This is a sharing rule for the joint flood-control storage. Each reservoir's own safety limit must hold whenever it is asked to store for the downstream point.

### 5.3 Adaptive execution

- **Rolling horizon.** Re-plan every 6 h over the remaining event and execute only the first step. Base the current release on a robust or two-stage formulation, so that one current decision is shared across the scenarios and later steps can branch.
- **Triggers to switch to a conservative mode** (the plan is redone on an upper forecast quantile instead of the central forecast):
  - observed inflow exceeds the forecast by more than a set margin for two consecutive steps;
  - the forecast is missing or late.
- **Fallback.** If a level approaches the reservoir-side threshold, switch to a level-based dam-safety rule (release up to capacity), whatever the downstream objective.
- **Point of no return for Luhun's pre-release.** Water released below the flood-limit level can only be recovered from the flood itself. If the updated forecast shrinks Luhun's flood, stop the pre-release at once. Set the stopping trigger so that the expected end level is still within tolerance under the low-side forecast.
- **Early arrival.** If the flood arrives earlier than forecast while Luhun is drawing down, stop the drawdown and shift to holding.

## 6. A defensible way to pick one option

Optimise over the scenario ensemble (for example NSGA-II/III, or an ε-constraint method on the Heishiguan peak against the maximum levels). This gives a non-dominated set. Then:

1. **Safety screen first, on the upper bound.** Discard every option that breaks any of these:
   - the reservoir-side level limit at the agreed exceedance probability;
   - the end-level tolerance;
   - the drawdown, ramp or capacity limits;
   - the Heishiguan safe discharge.
   
   Use the 95th or 99th percentile, or CVaR, for this test, not the mean. Benefits are not weighed until this screen is passed.
2. **Side-by-side table** of the surviving options: Heishiguan peak (mean and CVaR), maximum level of each reservoir (95th/99th percentile), exceedance probabilities, end-level deviation, time above safe discharge, and largest ramp used. State which options are dominated.
3. **Resolution check.** Merge options that differ by less than the Monte Carlo standard error, or by less than the spread between error models M3 and M4. Choosing between them would be choosing on noise. Within such a group, prefer the option with the smaller ramps and simpler release pattern.
4. **Compromise ranking.** Use TOPSIS (or a fuzzy optimum) with weights set openly with the agency. Test the ranking under randomly perturbed weights (for example ±20% Monte Carlo on the weights, reporting how often each option ranks first), under each error model, and under the scaled events in Section 7. Recommend an option only if it ranks first or near first across these tests. Otherwise present the two leading options with the trade-off stated.
5. **Approval.** The agency's flood-control decision-makers choose. As I understand it, flood dispatch on the Yiluo reservoirs is directed under the Yellow River Conservancy Commission's flood-control headquarters, in coordination with the Henan provincial authorities. Precise roles and instruments should be confirmed. They decide in consultation with the reservoir operators.

## 7. Tests before any recommendation is relied on

- **Baselines under identical conditions:**
  - the current single-forecast practice;
  - a no-forecast, level-based rule;
  - a perfect-forecast optimum, as an upper bound only, not a deployable plan.
  
  The gain from accounting for forecast error should lie between the no-forecast and perfect-forecast results. If it does not, something is wrong.
- **Beyond one flood.** A plan tuned on the 2021 event alone proves little. Test it on:
  - other yearbook floods, including events where Luhun peaks first or the two peaks nearly coincide;
  - the 2021 event scaled up (for example to the design floods of a few return periods);
  - local inflow arriving early, together with, or after the reservoir releases at Heishiguan.
  
  Keep at least one event out of all tuning.
- **Sensitivity** to the high-flow error extrapolation factor, the lag and cross-correlations, the ramp limits, the end-level tolerance and the event-window length T.
- **Mechanism check.** Confirm from trajectories that any Heishiguan peak reduction comes from staggering and from spreading release ahead of the peak. It must not come from a hidden violation, such as an end level outside tolerance in the tail scenarios.

## 8. Key assumptions and what would change the conclusions

- **Assumed:**
  - the surface areas used in the illustrations;
  - the illustrative error parameters (σ = 0.15, ρ = 0.8);
  - the evacuation numbers;
  - that the reservoir-side threshold lies well below the top of the flood-control zone.
  
  All are placeholders until the level-storage curves, the fitted error model and the agency's thresholds are in hand.
- **Would weaken the "simple assumptions understate risk" judgment:** a matched hindcast archive showing weak lag correlation, or relative errors at high flow no larger than at low flow.
- **Would change the coordination pattern:** routed travel times showing that the two peaks nearly coincide at Heishiguan, or substantial local inflow near the peak.
- **Would turn reservoir safety into the binding issue:** release capacity at the flood-limit level well below what evacuation needs, or a short event window T.
- **Adoption.** A change from deterministic to error-aware joint operation should first be trialled in shadow mode beside current practice for a flood season. It needs:
  - acceptance criteria agreed in advance with the dam-safety and flood-control authorities;
  - logged reversion triggers (forecast missing or diverging, gate failure);
  - warnings to downstream emergency services before any deliberate pre-release raises Heishiguan flows.
  
  Current practice remains the legal basis until the change is approved in the annual flood-control dispatch plan.
