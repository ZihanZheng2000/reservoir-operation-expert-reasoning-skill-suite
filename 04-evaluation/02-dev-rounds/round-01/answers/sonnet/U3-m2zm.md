# Review of the prerelease-rule evaluation (600 million m³ reservoir)

## 1. Provisional judgment

I would not recommend adoption on this evidence. The 18% reduction in maximum outflow under the 100-year design flood may be real, but the analysis does not support it, and the "95% confidence" claim is not a valid statement as made. The main problem is that the uncertainty model (pooled, independent, normal daily errors) is probably too optimistic about forecast skill exactly where it matters: large events, flood season, longer leads. A prerelease rule is a bet on forecasts, so its benefit is very sensitive to forecast error structure. The rule's downside (a prerelease that turns out to be unneeded, or too early) is not addressed at all.

The provisional judgment would change if the additional analyses below show the benefit holds with realistic, event-conditioned, autocorrelated errors, across many flood shapes, without unacceptable downside in non-flood or forecast-miss cases, and with a defensible validated simulation.

Assumptions: "maximum outflow" is peak release (or peak downstream flow) during the event; "current rule" is the operating rule in force; the 600 million m³ is total storage, and flood control storage, initial pool, and spillway/outlet capacity are not given and must be obtained.

## 2. Methodological problems and uncertainties

### 2.1 Error model

1. **Pooling across season, magnitude, and lead.** Forecast error variance and bias differ by season (snowmelt vs. convective vs. frontal storms), by flow magnitude (errors usually scale with flow; relative error may be roughly constant while absolute error grows, or the forecast may under-predict peaks), and by lead time (day-3 error is larger than day-1). A pooled distribution is dominated by the many low-flow, short-lead days and will understate the error in a flood at day 3. The tail relevant to a 100-year event is effectively unobserved.
2. **Normality.** Flood forecast errors are typically heavy-tailed, skewed, and heteroscedastic. A normal fit understates large misses, and may allow nonphysical negative flows. Goodness-of-fit in the bulk says nothing about the tail. Under-prediction of the peak (the dangerous direction) may be systematically larger than over-prediction, and bias (not symmetric zero-mean) may exist.
3. **Independent daily errors.** Forecast errors are strongly serially correlated within an event (a forecast that misses the storm rainfall misses it on all days, and the three lead days from one issue share the same driver, such as precipitation error). Sampling each day independently averages errors out and makes the forecast look much better than it is during an event; independent noise partly cancels, correlated error does not. This probably biases the result in favor of the new rule. Cross-lead correlation within a single issued forecast (the forecast hydrograph shape error) is also ignored.
4. **Sample size and representativeness.** 12 years contain a handful of flood events, probably none near 100-year magnitude. The extreme-tail error characteristics are extrapolated. Whether the 12 years include the flood types the design floods represent (volume vs. peak, single vs. multi-peak, antecedent wetness) is unknown. Also unknown: whether the forecast system changed during the 12 years (model versions, inputs), and whether the forecast was issued operationally or hindcast (hindcasts are typically more skillful than real-time).
5. **Forecast error definition.** Is the error on daily mean inflow, on peak, on volume, or on routed inflow? A rule that triggers on cumulative volume or timing depends on different error components than daily flow. Errors in timing (shifted hydrograph) are poorly captured by additive daily noise.
6. **Fit to the residual vs. the use.** Errors from a forecast conditioned on an observed state differ from errors in the design-flood setting, where the "true" inflow is a synthetic hydrograph and the forecast is manufactured around it. How the synthetic forecast is constructed (truth plus noise?) matters: real forecasts are not truth plus independent noise, and tend to under-represent the peak and lag the rise.

### 2.2 Simulation design

7. **Design-flood definition.** "100-year design flood" needs to be specified: peak-based or volume-based, which hydrograph shape, duration, and which probabilistic basis. One shape per return period is a single scenario; real 100-year events vary in shape, timing of peak, multiple peaks, and antecedent conditions. The rule may do well for a single-peaked design shape and poorly for a double-peaked flood or a long-volume flood. Whether the design flood itself was revised under climate non-stationarity is also unknown.
8. **Initial conditions and operating assumptions.** Starting pool level, flood-control-season rule curve, gate/outlet availability and failure, ramping limits, downstream constraints, and operator behavior (do operators actually follow the rule when the forecast looks uncertain?) all influence the result and are not stated. Starting from a favorable pool will inflate the benefit.
9. **Number of replicates and what is summarized.** 5,000 replicates per design flood is probably sufficient for the mean and central quantiles, but not necessarily for extreme tail quantiles of the outcome (the worst 1% is about 50 runs). Convergence has not been shown. More importantly, the statistic compared is unclear: the mean reduction? the median? paired per-replicate (same forecast error draw applied to both rules) or independent? Pairing is needed to isolate rule effect.
10. **Peak outflow is the wrong (or incomplete) single metric.** Minimizing the maximum outflow ignores: maximum reservoir level and the probability of exceeding the emergency/surcharge level or dam-safety limit; spill occurrence and timing; the downstream peak stage and damage (outflow combined with uncontrolled tributary flow); duration of high release; and the rate of change of release. A rule can reduce peak release while leaving the reservoir nearly full and exposing it to a second storm. The goal should be framed as risk to people and the dam, not a single peak number.
11. **Rule performance outside the design flood.** The new rule lowers releases ahead of an expected flood; if the flood does not come (false alarm), the reservoir is lower than needed. Water supply, hydropower, environmental flows, and refill reliability are affected, and prerelease can itself cause downstream flooding or bank damage if the release is large and the flood does not materialize. The evaluation covers only design floods; there is no assessment over the full inflow record, moderate events, droughts, or the non-flood season.
12. **Interaction with the rule's own mechanism.** If the rule responds to forecasts, the benefit is a function of forecast skill; the sensitivity of the benefit to error variance, bias, and correlation is the core quantity and is not reported. There is no sensitivity analysis.

### 2.3 The "95% confidence" claim

13. A confidence statement requires a defined population and an estimand. Here, 5,000 synthetic replicates from a fitted distribution give the spread due to simulated forecast noise given the assumed model. It does not include parameter uncertainty in the fitted error distribution (12 years), model-form uncertainty (normal, independence), design-flood uncertainty, hydrologic and hydraulic model uncertainty, or operational uncertainty. It is therefore at best a conditional statement ("in 95% of simulated forecast draws under the assumed error model, the new rule gave a lower peak"), not "95% confidence that the rule reduces the peak 18%".
14. The statement is ambiguous: is it 95% of replicates showing some reduction, an interval for the mean 18% reduction, or 95% of replicates showing at least 18%? These are different. A narrow interval from many replicates only reflects the simulation sample size and can be made arbitrarily narrow by running more replicates; it is not evidence about reality. It is also not a confidence interval in the frequentist sense, since no repeated sampling of real data is involved.
15. The 18% should be shown as a distribution (median, spread, worst-case, percent of replicates where the new rule is worse), not a point.

### 2.4 Model and data validity

16. **Hydrologic/hydraulic and reservoir model validation.** Has the simulation model been calibrated and validated against observed events (inflow routing, reservoir storage-elevation curve, outlet rating curves, downstream routing)? Peak outflow is sensitive to outlet capacity and gate operation details.
17. **Baseline fairness.** Was the "current rule" implemented as operators actually run it (including discretion, observed practice), or as a strict textbook version? Was it given the same forecast information? Was the new rule tuned on the same design floods and error data used to evaluate it (in-sample tuning, overfitting)? Is there any out-of-sample test?
18. **Backtest on historical record.** There is no mention of testing the rule on actual historical events with actual forecasts as issued. This is the most credible validation, even though events are few.
19. **Independence and conflicts.** The firm's role, assumptions documented, and whether the analysis is reproducible (code, data, seeds) by an independent party are not described.
20. **Non-stationarity.** Climate and land-use change may alter flood magnitude, seasonality, and forecast skill over the rule's life.

## 3. What I would require before recommending adoption

### 3.1 Re-do the forecast error characterization
- Obtain the full forecast archive as issued operationally (not hindcast), with metadata on forecast model versions; document changes in 12 years.
- Stratify errors by season (at least flood season vs. other), flow magnitude (e.g., quantile bins or relative-error scaling), and lead time (day 1, 2, 3). Test whether errors are better modeled as relative (multiplicative, log-space) rather than additive.
- Test distribution fit in the tails (QQ plots, tail-focused tests, compare with heavy-tailed alternatives such as Student-t, skew-t, generalized extreme value or Pareto tail, or empirical/bootstrapped residuals); report bias, especially peak under-prediction.
- Quantify temporal and cross-lead correlation (autocorrelation, cross-correlation, event-level error, timing error), and model them (for example, a multivariate or copula-based model, AR processes on residuals, or event-block bootstrap of real forecast-error trajectories).
- Use the actual historical forecast-versus-observation pairs from the largest events directly (replay) as a check on the synthetic generator.
- Quantify parameter uncertainty (bootstrap the 12 years, resampling by year or event, not by day).

### 3.2 Rebuild the simulation
- Define the design floods precisely: multiple hydrograph shapes, volumes, durations, peak timings, antecedent conditions, and return periods (e.g., 20, 50, 100, 200, and beyond-design); include a historical-largest event and a double-peak scenario; consider climate-adjusted floods as sensitivity.
- Use correlated, event-consistent synthetic forecasts, with the forecast generated as a function of the true hydrograph that reproduces observed forecast behavior (underestimated peak, lag).
- Use paired comparisons (same forecast realization for both rules) and report the distribution of differences, including the share of cases where the new rule is worse.
- Run enough replicates to show convergence of the tail metrics; report Monte Carlo error.
- Specify initial pool, rule curves, gate capacities and failure scenarios, ramping and downstream constraints, and operator override.

### 3.3 Broaden the performance metrics
- Maximum pool elevation, probability of exceeding flood control pool, emergency spillway or dam-safety level, spill volume and timing; maximum and duration of downstream flow and stage at critical locations; downstream damage proxies, including the case of coincident uncontrolled tributary flow.
- Downside metrics: false-alarm cost, water supply/hydropower/environmental reliability and refill probability over the full historical inflow record (continuous simulation, ideally many decades, plus stochastic generation), performance in moderate floods, multiple consecutive storms, and forecast failures.
- Robustness: how performance degrades with forecast error scaled up (for example x1.5, x2), with bias, with forecast outage (no forecast available), and with a missing or delayed forecast. A rule that gives away safety when the forecast is wrong is hard to defend; a fail-safe fallback to the current rule should be defined.

### 3.4 Validate the model and baseline
- Evidence of calibration and validation of the inflow, routing, storage, and outlet models on observed floods; an uncertainty or sensitivity assessment on rating curves and storage curves.
- Confirmation the baseline reproduces historical operation of the current rule (replay of past events, with past operator decisions).
- A true out-of-sample test: tune on part of the data and evaluate on withheld years or events; or demonstrate the rule has few tuned parameters.
- Backtest the new rule with the actual forecasts as issued for all major historical events, reporting what the rule would have done versus what happened.

### 3.5 Restate the uncertainty claim
- Replace "95% confidence" with a clearly defined statement: the estimand, the sources of uncertainty included, and a distribution or interval of the reduction under a range of plausible error models. Include parameter, model-form, and design-flood uncertainty. Report as scenario-conditioned results with a worst-credible case, not a single confidence number.

### 3.6 Institutional and implementation checks
- Review by the dam safety authority and the operators; consider regulatory constraints (many jurisdictions limit prerelease rates or require specific forecast reliability), downstream notification and flood-warning implications, and liability.
- Independent technical review and reproducibility (code, data, seeds, documented assumptions).
- Decision criteria agreed in advance: for example, the new rule must not increase the probability of exceeding the dam safety level under any credible error scenario, and must achieve a stated benefit under the stressed error model.
- If adopted, a staged implementation: pilot/shadow operation (run the new rule in parallel without acting on it for one or more seasons), defined triggers to revert to the current rule, post-event performance reviews, and periodic re-estimation of forecast error as the forecast system changes.

## 4. What would confirm or change the judgment

- **Confirm (move toward adopt):** the benefit persists (at least a meaningful share of 18%) with stratified, heavy-tailed, autocorrelated errors and parameter uncertainty; it holds across several hydrograph shapes and return periods; no worsening of maximum pool level or dam-safety exceedance in any credible scenario; downside costs in ordinary years are acceptable; a backtest on historical events is consistent; shadow operation shows the rule functions as intended.
- **Change (move toward reject or modify):** the benefit disappears or turns negative when errors are correlated or scaled up for large, long-lead events; the rule worsens maximum pool level or leaves the reservoir exposed to a second storm; false alarms cause unacceptable supply or downstream impacts; the result depends on tuning or on the favorable initial pool. In that case consider a modified rule (for example, with capped prerelease, thresholds on forecast confidence, or a fallback rule) rather than outright adoption.

## 5. Interim recommendation to the owner

Do not adopt on the present report. Commission the re-analysis above (priority order: error-model re-estimation with correlation and tails; paired multi-scenario simulation with safety-oriented metrics; model validation and backtest; restated uncertainty), and consider a shadow-mode trial. The current evidence is useful as an indication that prerelease may help, not as a basis for a safety-critical operating change.
