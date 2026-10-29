# Study design: staged (seasonal) flood-limited water levels versus a single fixed level

## 0. Provisional position

Staged flood-limited water levels (FLWL) are worth testing in a monsoon basin. The flood season is not uniformly dangerous: flood risk usually peaks in a core monsoon window, while the early and late parts of the nominal flood season carry lower flood risk but high water-supply value, because storage held back there is what irrigation and hydropower draw on later.

With the data currently listed, the study can support a screening-level conclusion and a conditional recommendation. It probably cannot support a firm recommendation to change the rule. The main gaps are:
- no confirmed information on downstream flood damage thresholds or the safe-discharge limit at the town;
- no confirmed information on uncontrolled inflow from the intermediate catchment;
- no confirmed record of actual historical operations (releases and levels);
- only 8 years of forecasts.

The design below uses what exists, states what each data gap does to the strength of the conclusion, and defines what evidence would be enough to recommend a change.

Key assumptions, to be confirmed with the reservoir operator:
- The reservoir has gated spillways or outlets, so releases are controllable up to the level-discharge capacity curve.
- The current rule has one FLWL held through a fixed flood-season date window.
- The town's damage onset is tied to a downstream flow or stage that can be estimated or obtained.
- Irrigation and hydropower demands are roughly known from the operating rule or operator records.

What would change the position:
- If inflow flood seasonality is not clearly separable (for example, large floods occur across the whole season), the case for staging weakens.
- If the reservoir's flood-control capacity is already marginal against the design flood, the case for any reduction of flood storage weakens.
- If operators already depart from the fixed FLWL in practice, the baseline must be the practised operation, not the written rule.

---

## 1. Research question

**Main question.** Can a seasonally staged FLWL, with a lower flood-control level in the core flood window and a higher level in the early and late flood season, increase the reservoir's water-use benefits (irrigation reliability, hydropower generation, end-of-season storage) while keeping flood risk to the reservoir and to the downstream town no higher than under the current single fixed FLWL?

**Sub-questions.**
1. Is there a statistically defensible seasonal structure in extreme inflow, and where are its boundaries? How uncertain are those boundaries, given 45 years and non-stationarity?
2. For candidate staged schemes, how do dam safety indicators and downstream flood indicators compare with the baseline across historical, perturbed and synthetic floods?
3. What is the gain in irrigation supply reliability, hydropower, and refill probability?
4. How much of any benefit depends on forecasts, and does it hold when forecast skill is poor, or when forecasts are not used?
5. How robust is the conclusion to inflow non-stationarity, extreme-flood tails, and forecast error?

**Success criterion in the design.** Flood safety is a constraint, not an objective traded off in a weighted score. A candidate scheme is first judged on whether it is non-inferior on flood safety; only then are the gains compared.

---

## 2. Data inventory, gaps, and what to request

### Available data and what each supports

| Data | Main use | Issues to check first |
|---|---|---|
| 45 yr daily inflow | Seasonality of floods; extreme-value analysis; resampling and synthetic flood generation; water balance and simulation | Whether inflow is observed or back-calculated from reservoir water balance (back-calculated series smooth peaks and have errors); homogeneity; upstream regulation or land-use change; missing values; the daily time step is coarse for flood peaks |
| Level-storage, level-discharge capacity | Simulation core; flood storage available at each level; spillway release limits | Date and survey of the curves (sedimentation reduces capacity; use a current curve); gate operation conditions |
| 8 yr forecasts, lead 1-5 d, daily updates, with observations | Forecast error characterization; forecast-informed operation tests | Only 8 years, so likely few or no extreme floods; whether forecasts are of inflow or of rainfall; whether they are deterministic; whether the observations are the same inflow series |
| Current operating rule | Baseline | Written rule versus practice |

### Data to ask for, in priority order

Where one of these cannot be obtained, the stated fallback applies.

1. **Historical operation records** (daily level, release, spill) for as many years as possible. These are needed to validate the simulator and to establish what operators actually do. Fallback: validate the simulator on water balance only, and treat the written rule as the baseline with that caveat stated.
2. **Downstream safe-flow or stage thresholds** at the town (channel capacity, levee level, damage-onset flow, and any official warning stage). Fallback: use sensitivity analysis over a range of thresholds and state results as exceedance of generic thresholds expressed as fractions of the historical peak. A recommendation cannot rest on this fallback alone.
3. **Downstream hydrology between the dam and the town**: gauge data at the town or intermediate gauge, tributary inflows, and a channel routing relation or travel time. Without these, the reservoir release is treated as the only contribution to the town's flow, which understates risk. Fallback: bound the effect with a range of assumed lateral inflow scenarios.
4. **Design flood, dam safety criteria, and official regulatory constraints** (including who must approve changes to the FLWL and the criteria used, for example design-flood and check-flood standards and any rule-curve approval process). This determines what "safe" means formally.
5. **Irrigation demand schedule and command-area information, hydropower plant characteristics** (head, efficiency, installed capacity, tariff or value of energy), minimum environmental or downstream release requirements, and any water-sharing agreements. Fallback: use the demands implied by the current rule, and report benefits in physical units (volume delivered, MWh) without monetizing.
6. **Longer or additional forecast archives, and rainfall data** (gauge or gridded) for the catchment. Fallback: run forecast-based schemes only as a sensitivity analysis.
7. **Reservoir sedimentation survey, and information about gate and outlet operation limits and gate failure or maintenance restrictions.**
8. **Climate-related information** (for example regional projections or published trend analyses) for a non-stationarity sensitivity test. This is optional.

---

## 3. Methods

### 3.1 Data preparation and diagnostics

- Clean inflow, and document how it was derived. If it is reconstructed from the water balance, quantify the effect on peak flows, for example by comparing with any available gauge records.
- Test for trends and change points in annual maxima, flood-season volume, and monsoon onset and withdrawal timing. A trend or shift would mean 45 years of history is not a stationary sample.
- Estimate flood seasonality from the inflow: for each year, record the timing of peaks over a threshold and of high-volume events, and describe the distribution of timing (for example, circular statistics for event dates, or counts of exceedances by pentad or dekad). Use these to propose candidate stage boundaries, and give uncertainty intervals on the boundary dates by bootstrap over years.
- Look at event type: separate short, sharp peaks from long, multi-peak volumes, because short-duration events and long-volume events interact differently with flood storage and with forecast lead time.
- Characterize forecast error by lead time, season, and flow magnitude: bias, RMSE, skill relative to persistence or climatology, error of peak timing and magnitude, and error conditional on large flows (the part that matters for flood decisions). Check whether error is larger in rising limbs and at peak. With only 8 years, report confidence intervals and state plainly how many large events the sample contains.

### 3.2 Simulation model

Build a daily reservoir simulator:
- water balance: storage = previous storage + inflow - release - evaporation (if known) - withdrawals;
- level from storage by the level-storage curve; maximum release limited by the level-discharge capacity at the current level, and by gate rules;
- an operating rule module that reproduces the current rule as the baseline;
- an irrigation and hydropower module driven by the demand and plant data;
- a downstream routing module to the town 40 km away, with travel time of roughly one day or less (to be calculated from channel data; this matters because a daily time step may be too coarse to represent peaks and release timing at 40 km, so consider a sub-daily check on the largest historical events if hourly data exist).

Validation: reproduce observed level and release history if operation records are available; if not, validate for internal consistency (mass balance, no violation of physical limits) and have the operator review whether the simulated baseline behavior looks plausible.

### 3.3 Candidate staged schemes

Define a small, structured family and avoid a free search that overfits 45 years:
- Number of stages: two or three (for example, early season, core season, late season).
- Parameters: stage boundary dates and the FLWL at each stage, within bounds set by the dam's safety limits and by the normal pool level. The core-season level should not exceed the current fixed FLWL.
- Transition rules: how the level is allowed to rise at a boundary, because raising the level requires filling, which depends on inflow, and filling too fast can leave the reservoir close to the new limit just before a flood. Specify filling rate limits and conditions such as "raise only if the forecast shows no significant inflow over the next N days" as a variant.
- Include the current fixed FLWL as the baseline and a trivial variant (the same FLWL but applied over a shorter window) as a simple comparison.

Optimize cautiously, with a constrained search over the small parameter family (grid or evolutionary algorithm), where the constraint is the flood-safety criteria and the objective is the water-use benefit. Use cross-validation by years (for example, leave-block-of-years-out) so that the selected parameters are tested on years not used for selection. Report the full tradeoff front, not only the chosen point.

### 3.4 Operation under forecast information (two tiers)

1. **Forecast-free** (rule-based on observed storage and inflow only). This is the primary comparison, because it does not depend on the quality of the forecasts and can be assessed over all 45 years.
2. **Forecast-informed** variants (for example, pre-release when a large inflow is forecast; allowing higher storage only when the near-term forecast is benign). Test these only over the 8 forecast years, plus a synthetic-forecast approach: for the other 37 years, generate synthetic forecast errors by sampling from the empirical error distribution by lead time, season and magnitude, preserving the autocorrelation between lead times and consecutive days. State that this is a modelled forecast, not an observation, and that extreme-event errors are poorly sampled.

Keep the conclusion layered: if a staged rule is safe without forecasts, the recommendation does not depend on forecast skill; if safe only with forecasts, the recommendation is conditional on the forecasting system being operated reliably, and the operator must have a fallback if forecasts are unavailable.

### 3.5 Flood stress testing beyond the 45-year record

Forty-five years cannot say much about floods with return periods of 100 years or more, which are exactly the events that govern dam and town safety. To test:
- Fit extreme-value distributions (annual maxima or peaks-over-threshold, and flood volumes at several durations) with uncertainty bounds, and generate design hydrographs of several return periods using the observed hydrograph shapes, as well as the official design flood if available.
- Generate synthetic multi-year inflow ensembles (for example, stochastic weather generator or block-bootstrap/resampling of seasons that preserves within-season structure) and run baseline and candidate rules through them.
- Place the largest historical floods and scaled versions (for example, 1.0x, 1.2x, 1.5x) at different times in the season, especially just after a stage boundary and at the highest level the new scheme allows. This "worst timing" test is the most relevant for staging: the risk of a staged scheme is a large flood arriving soon after the level has been raised.
- Add a degraded-operation test: late or missed releases, gate unavailability (one gate out), forecast failure, and delay in operator response. A rule that is safe only when everything works is a weaker candidate.
- Include a non-stationarity sensitivity: shift the flood timing and increase the magnitude of extremes by plausible amounts, and report at which point the staged scheme loses its safety non-inferiority.

---

## 4. Assessing the effect on flood safety

### Indicators

Dam and reservoir:
- maximum reservoir level and its exceedance of the normal-high or design flood level, and of the dam crest margin;
- frequency and duration of reaching the spillway crest, and of reaching levels above FLWL;
- maximum release and whether the release capacity is ever constrained by level.

Downstream:
- peak flow at the town and the frequency of exceeding the damage-onset threshold, and the thresholds above it;
- duration above threshold and flood volume above threshold;
- rate of change of release (rapid increases are a hazard to people and works below the dam);
- number of events where reservoir release adds to the flood peak rather than reducing it, that is, where the reservoir is "full" and passes inflow through.

Aggregate:
- annual probability of the town's flow exceeding thresholds, with uncertainty intervals;
- expected annual damage only if a stage-damage relationship is available (otherwise do not compute it).

### Comparisons and the non-inferiority test

- Compare each scheme with the baseline on matched inputs (same inflow series, same forecasts) so that differences are attributable to the rule.
- Define non-inferiority margins in advance, with the operator and regulator if possible (for example: no increase in the frequency of damaging downstream flow, no increase in the maximum reservoir level above the design limits, and no deterioration at any return period tested, within stated tolerances).
- Judge at the tail: results at the 20 to 50 years' return period level and beyond count more than averages. For rare events, rely on the synthetic and scaled tests and report uncertainty bands, not point estimates.
- Look at individual events: for each large historical flood, show the trajectory under baseline and under the staged scheme. This allows the operator to see why a difference occurs and gives an independent check on the model.

---

## 5. Assessing other operating objectives

- **Irrigation**: volume supplied versus demand by period, reliability (fraction of periods or years with full supply), shortfall magnitude and duration, and performance in dry years. Report particularly the sensitivity during the critical crop periods, which may coincide with the end of the flood season.
- **Hydropower**: energy generation (MWh), firm or dependable energy, head (since higher storage raises the head and efficiency), and spill without generation (wasted water). Value energy at a constant price if no price series is given, and report in physical units.
- **Storage and refill**: probability that the reservoir reaches the normal pool level (or the target level) at the end of the flood season, distribution of end-of-season storage, and the carry-over into the dry season.
- **Other constraints**: minimum downstream and environmental releases, water supply (if any), sedimentation effects (higher levels in the flood season can trap more sediment; qualitative at most unless data exist), and reservoir-margin and upstream submergence constraints (higher levels may inundate land or infrastructure upstream; check with the operator).
- Report the gains as distributions over years, not only means, and separately for dry, normal and wet years. A scheme that gains most in wet years where water was already adequate has less value than one that helps dry years.

Present the trade-off explicitly: flood safety indicator versus water-use gain across the candidate family, so that the reader can see where the safety margin is spent.

---

## 6. What results would be sufficient to recommend a change

I propose a tiered standard, to be agreed with the operator beforehand (the thresholds are provisional and set in advance, not after seeing results).

### Necessary conditions (all must hold)

1. **Simulator credibility**: the baseline simulation reproduces historical operation reasonably (if operation data exist), and the model's treatment of release capacity and routing to the town has been checked by the operator.
2. **Flood-safety non-inferiority across the full test set**: for the historical record, the scaled and synthetic floods, the worst-timing tests and the degraded-operation tests, the candidate does not increase the maximum reservoir level beyond design limits, does not increase the frequency or magnitude of downstream exceedance of the damage thresholds, and does not produce a new failure mode (for example, a release surge that exceeds the downstream safe limit) beyond the agreed margin. Where a result is unclear because of sampling uncertainty, the uncertainty interval must stay within the margin, not just the point estimate.
3. **Robustness**: the conclusion survives plausible variations in flood seasonality boundaries, magnitude of extremes (including non-stationarity), forecast error (if forecasts are used), and the downstream threshold range and lateral inflow assumptions.
4. **Out-of-sample support**: the benefit and the safety hold in years not used to select the stage parameters.
5. **Meaningful benefit**: the water-use gain is large enough in physical terms (for example, a stated increase in irrigation reliability or generation in dry and normal years, and a higher refill probability) to justify the regulatory effort and residual risk, with the threshold set with the operator.
6. **Operability**: the rule is simple enough to be applied by operators, with clear transition conditions, and it does not depend on a single point of failure; if it depends on forecasts, there is a defined fallback.

### What would justify only a weaker recommendation

- If safety holds only with forecast use, or only for part of the stress tests, or the downstream thresholds are assumed rather than provided: recommend a pilot or trial, or further data collection, not a rule change.
- If benefit is real but small or concentrated in a few years: report this and leave the decision to the operator.
- If the staged scheme is non-inferior only within a narrow window: recommend only a narrower adjustment (for example, a modest rise at the very beginning and end of the season).

### What would lead to not recommending a change

- Any candidate that gives a large gain but worsens tail flood risk or downstream exceedance beyond the margin.
- Flood seasonality not distinguishable from noise, or boundaries unstable across sub-periods.
- A trend indicating the flood season is getting less predictable.

### Status of the conclusion

Even if all the conditions are met, the study provides evidence for the decision, not the decision. Changing a flood-limited level is a regulatory and dam-safety matter, which needs the dam-safety authority and the operator's approval, and typically a trial operation period with monitoring. The study should state this and should not claim approval or deployment-readiness.

---

## 7. Plan of work

1. Meet the operator and obtain the data listed in section 2, and confirm the current rule, the actual practice and the safety criteria. Decide the non-inferiority margins and the benefit thresholds before analysis.
2. Data diagnostics: inflow quality, trend and change-point tests, seasonality estimation, forecast error characterization.
3. Build and validate the simulator and baseline.
4. Define the candidate family and run forecast-free simulations over the 45 years; compute safety and benefit indicators.
5. Run the stress tests (extreme-value design floods, scaled floods at worst timing, synthetic ensembles, degraded operation).
6. Run forecast-informed variants for the 8 forecast years plus synthetic forecast error for the others.
7. Robustness and sensitivity analysis; out-of-sample validation.
8. Synthesize: tradeoff fronts, event-level examples, a clear statement of which conditions in section 6 are met, which are not, and what the recommendation is (change, pilot, no change).

---

## 8. Main risks and limitations to state in the study

- 45 years do not constrain rare floods; the tail results depend on extreme-value fitting and synthetic methods and carry wide uncertainty.
- 8 years of forecasts probably contain few large floods; forecast value for the events that matter most cannot be established directly.
- Daily time step may miss peak timing and intra-day release behavior, and may understate downstream risk at a 40 km reach.
- Inflow records may be affected by reconstruction error and upstream changes.
- Without downstream threshold data, lateral inflow and operation records, the downstream safety results are conditional on assumptions.
- Optimizing a few parameters on one historical sample risks overfitting; the cross-validation and robustness tests are intended to limit this but do not remove it.
- Non-stationarity: the past 45 years may not represent the next several decades.
- The study cannot establish institutional acceptability or operator behavior in a real flood.
