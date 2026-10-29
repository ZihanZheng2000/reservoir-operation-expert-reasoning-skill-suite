# V04 Study Design: Forecast-Error-Aware Joint Flood Operation of Guxian and Luhun Reservoirs

## 1. How I read the question

The question has two parts:

1. **Quantify:** how much does inflow forecast error change the flood risk at Guxian and at Luhun? Downstream risk at Heishiguan follows from the two releases, so it has to be part of the answer.
2. **Prescribe:** how should joint releases be coordinated once that error is taken into account, instead of planning on a single deterministic forecast per reservoir?

Part 1 needs a counterfactual comparison. I compare the risk that operators believe they face (deterministic plan, forecast taken as truth) with the risk they actually face (the same plan evaluated against realistic inflow uncertainty). Part 2 needs a decision method that uses that uncertainty, plus evidence that it does better than the current practice on events it was not tuned on.

The study has five steps: (A) build a defensible forecast-error model, (B) generate inflow scenarios for both reservoirs jointly, (C) propagate them through the reservoir and river system to risk metrics, (D) design and compare coordination strategies, and (E) stress-test on the 18 September 2021 flood and with sensitivity analysis.

## 2. Assumptions (stated, not invented facts)

- The forecast archive contains issued (or properly out-of-sample hindcast) forecasts at stated lead times, paired with hourly observations, for both reservoirs, and covers several flood events. If the forecasts are in-sample fits of the data-driven model, the error statistics will be too optimistic. I would check this first.
- Reservoir characteristics include, at minimum: level–storage curves, outlet discharge capacity as a function of level, characteristic levels (flood-limited level, flood-control high level, design/check flood levels), and the current operating rules and downstream safe discharge(s). I use these as given and do not assume their values.
- Flow at Heishiguan includes the releases routed down the Luohe and Yihe plus inflow from the intervening area below the dams, which no reservoir controls. I assume intervening flow can be estimated from observations (Heishiguan minus routed releases). It is not clear whether a forecast exists for it. If none does, it is another source of uncertainty that I must model and not ignore.
- Forecast lead times are roughly in the range of the basin response time (hours to a day or two). The useful decision horizon is set by this.
- The 2021 flood is either in the archive or available as a separate observed event. Whether it was used to train the forecasting model matters for how it can be used for testing (see §8).

## 3. Step A: Characterize forecast error

**Goal:** a statistical description of observed inflow given the deterministic forecast at each reservoir. It must be good enough to generate realistic inflow scenarios, especially for large floods.

What I would examine in the archive, and why:

| Property | Why it matters for flood risk |
|---|---|
| Error versus lead time | Uncertainty grows with lead time. Release decisions taken early carry the most error. |
| Error versus flow magnitude (heteroscedasticity, bias) | Data-driven models often underestimate peaks and are less accurate outside the training range. The brief explicitly says errors are larger in large floods. A single pooled error distribution would understate risk exactly when it matters. |
| Peak timing and peak magnitude errors separately | For routing and storage, a peak that arrives 3 h early is a different risk from one that is 20% too high. |
| Temporal autocorrelation of errors | Errors persist through an event. Sampling independent errors hour by hour would produce unrealistically smooth cumulative volumes and understate volume risk. Flood volume, not just peak, drives the reservoir's maximum level. |
| Cross-correlation of errors between Guxian and Luhun (and intervening area) | The same storm system drives both basins. If both forecasts under-predict together, the joint risk at Heishiguan is much higher than independent errors would suggest. This is central to the coordination question. |
| Rising limb versus recession | Errors and their consequences differ by phase. |

**Candidate error models** (choose by validation, not by preference):
- Transform-space error model: normal quantile transform or Box-Cox of forecasts and observations, then a conditional Gaussian or autoregressive error model with lead-time-dependent parameters. Standard, cheap, and handles heteroscedasticity.
- Hydrologic Uncertainty Processor / Bayesian joint probability style conditional distribution of observation given forecast.
- Copula-based joint model across lead times and across the two reservoirs, to capture the dependence structure, including tail dependence.
- Quantile regression (conditional on forecast magnitude and lead time) as a nonparametric check.
- Empirical alternative if the archive is rich enough: analog or block resampling of whole-event error trajectories, scaled to the current forecast. This keeps realistic temporal structure without parametric assumptions, but extrapolates poorly to floods larger than any in the archive.

**Validation of the error model** (leave-one-event-out over flood events, not random hours):
- Reliability: coverage of 50/90/95% intervals, PIT or rank histograms, stratified by lead time and by flow magnitude.
- Sharpness, and CRPS compared with climatology and with the raw deterministic forecast.
- Specifically, coverage of event peaks and event volumes on the largest events.
- Whether simulated scenarios reproduce the observed cross-basin dependence.

The main data limitation is that the archive will contain few large floods. The tail of the error distribution, which is the part that matters, is the most poorly constrained. I would therefore (i) pool information across lead times and magnitudes using a parametric model whose spread grows with magnitude, (ii) report results under alternative tail assumptions, and (iii) treat the 2021 event as a stress test, not as tuning data.

## 4. Step B: Generate joint inflow scenarios

For a given forecast issue time, sample N joint scenarios (Guxian inflow, Luhun inflow, intervening inflow) over the forecast horizon from the error model, conditional on the deterministic forecasts. N could be about 1,000 for risk estimation. For optimization, reduce to a representative set (e.g., 20–50) by scenario reduction or clustering, then check the result against the full set.

Four scenario designs, which make the dependence assumption explicit:
1. **Deterministic only.** Current practice.
2. **Ensembles with independent errors** at the two reservoirs.
3. **Ensembles with correlated errors** using the dependence fitted in Step A. This is the main case.
4. **Fully dependent errors** (comonotonic), as a bounding case.

Comparing 2–4 shows how much of the risk comes from errors coinciding across the two basins.

## 5. Step C: Propagate to risk at each reservoir and at Heishiguan

**System model:**
- Reservoir routing at hourly time steps by mass balance with the level–storage curve, and release limited by outlet capacity at the current level.
- Channel routing from each dam to the confluence and on to Heishiguan (e.g., Muskingum or lag-and-route, calibrated on historical hourly releases and Heishiguan flows), plus intervening inflow.
- Verify the routing model by reproducing observed Heishiguan hydrographs from observed releases before using it.

**Risk metrics** (computed over scenarios for each operating plan):
- At each reservoir: probability that the maximum level exceeds each characteristic level (flood-control high level; design/check flood level as the dam safety threshold), and the distribution of maximum level and of maximum storage used.
- At Heishiguan: probability that peak flow exceeds the safe discharge, and expected exceedance volume/duration.
- Tail measures: CVaR (expected outcome in the worst 5%) of maximum level and Heishiguan peak, because the rare outcomes drive consequences.
- Secondary: end-of-event storage relative to flood-limited level (water supply/hydropower benefit and readiness for a following flood), and release smoothness/rate-of-change limits.

**Answering "how much does forecast error change risk":**
- For the operating plan derived from the deterministic forecast (current practice), compute (a) the risk it implies when the forecast is taken as truth (usually zero exceedance by design), (b) its risk under the scenario ensemble, and (c) its outcome under the observed hydrograph for historical events.
- The gap between (a) and (b) is the **risk change attributable to forecast error**. Report it per reservoir, at Heishiguan, by lead time, and by flood magnitude class.
- Decompose the gap: Guxian error only, Luhun error only, both, plus intervening-flow error. Then show the contribution of cross-basin error correlation (scenario designs 2 versus 3).
- Use a perfect-forecast operation (observed inflow known in advance) as the lower bound. The difference between deterministic-plan and perfect-forecast outcomes is the cost of forecast error under current practice. The fraction of that cost recovered by the uncertainty-aware strategy in Step D is the value of using uncertainty information.

## 6. Step D: Coordination strategies to compare

All strategies run in a **rolling-horizon** framework. At each forecast issue time, plan releases over the horizon, implement the first period (e.g., the next 1–6 h), update with new observations and a new forecast, and replan. This is realistic and is itself a form of hedging. Ignoring updating would exaggerate the cost of uncertainty.

Strategies:
1. **Baseline: current rules / deterministic joint optimization.** Optimize joint releases against the single forecast, for example to minimize the Heishiguan peak subject to reservoir level limits.
2. **Deterministic with safety margin.** Same as 1, but with inflow inflated to a chosen forecast quantile, or with tightened level limits. This is a simple, operator-friendly heuristic and a fair competitor.
3. **Stochastic / chance-constrained joint optimization.** Choose releases that minimize, for example, the expected or CVaR Heishiguan peak, subject to P(max level > critical level) ≤ α at each reservoir and P(Heishiguan > safe discharge) ≤ β, evaluated over the scenarios. Solve with a scenario-based formulation, or with an evolutionary algorithm (e.g., NSGA-II) when nonlinear capacity curves make the problem hard.
4. **Multi-objective version** of 3. Produce a Pareto front between upstream risk (Guxian and Luhun maximum levels) and downstream risk (Heishiguan), and between flood risk and end-of-event storage. The trade-off itself is part of the answer: holding more water reduces downstream risk but raises dam-site risk, and forecast error changes where that trade-off sits.
5. **Optional: a robust variant** (minimize the worst case over a bounded uncertainty set), as a conservative reference.

The coordination levers I expect the optimization to use, and that I would explicitly look for in the results:
- **Storage-allocation balance:** share the attenuation burden according to each reservoir's remaining flood-control storage *relative to the uncertainty of its own inflow*, not relative to the forecast alone. The reservoir with the wider error band needs more reserve.
- **Peak desynchronization:** time releases so the routed contributions from Luohe and Yihe do not arrive at Heishiguan together, accounting for travel time and for intervening-flow timing.
- **Pre-release / hedging:** release earlier and moderately when the upper tail of the forecast distribution threatens the critical level. Trade a small, certain downstream flow increase for a large reduction in the probability of an uncontrolled spill later.
- **Compensation:** when one basin's flood turns out bigger than forecast, the other reservoir cuts its release to keep Heishiguan within limits, if it has room.

**Evaluation protocol.** Test each strategy on held-out historical flood events, re-forecasting at each issue time from the archive and simulating against observed inflows. Also evaluate it against the scenario ensemble. Report:
- the risk metrics from Step C;
- realized maximum levels and Heishiguan peaks on each event;
- the frequency of unnecessary releases (a cost of over-caution);
- end-of-event storage.

A strategy that lowers risk only by large unnecessary releases, or by sacrificing water supply storage, must be shown as such.

## 7. Provisional judgment and recommendation

**Provisional expectation on the size of the effect.**
- For moderate floods, forecast error probably changes risk little, because there is enough flood-control storage to absorb it.
- For large floods, I expect the deterministic plan to understate risk substantially. Errors are larger then, data-driven models tend to under-predict peaks, and both basins tend to be wrong in the same direction.
- I expect the largest underestimate at Heishiguan, where the two errors combine with intervening-flow error, and in the reservoir with the less reliable forecast or the smaller remaining flood storage.
- This is a hypothesis to test, not a result. The study is designed so it could come out otherwise, for example if errors turn out weakly correlated or if storage is large relative to error volumes.

**Provisional recommendation on coordination.**
- Replace single-forecast planning with rolling-horizon, scenario-based joint planning using chance constraints on dam-site levels and on Heishiguan flow.
- Allocate flood-control burden between Guxian and Luhun by uncertainty-adjusted spare storage.
- Use moderate pre-releases when the upper forecast quantile, not the median, threatens a critical level.
- Coordinate release timing so the two routed releases do not coincide at Heishiguan.
- As an operational fallback that is easy to adopt, recommend planning on an upper forecast quantile chosen by lead time, calibrated in this study. Do so only if the study shows it recovers most of the benefit of the full stochastic method.

**Key assumptions behind this:**
- the archive's error behavior represents future large floods;
- the error model reproduces cross-basin dependence;
- release constraints and downstream safe discharges are as given;
- operators can actually update releases at the planned frequency.

**What would confirm or change it:**
- Confirm: the ensemble shows a substantially higher exceedance probability than the deterministic plan implies for large events; the stochastic strategy lowers realized maximum levels and Heishiguan exceedances on held-out events, including 2021, without excessive unnecessary releases.
- Change: if errors are small relative to available flood storage, or uncorrelated between basins, the gain from coordination under uncertainty will be small. A simple margin rule (strategy 2) would then be the better recommendation, because it is easier to use.
- Change: if the error model is poorly calibrated in the upper tail (coverage failures on the largest events), the probabilistic risk numbers should not be trusted as absolute values. In that case I would report relative rankings of strategies and robust or bounding results instead.
- Change: if intervening-area flow dominates Heishiguan peaks, reservoir coordination has limited leverage. The recommendation would shift toward forecasting that flow and setting dam release ceilings conservatively.

## 8. Step E: The 18 September 2021 flood and sensitivity analysis

- **2021 as a stress test.** Replay the event hour by hour using the forecasts that were (or would have been) available at each issue time. Compare (i) the deterministic plan, (ii) the margin rule, (iii) the stochastic strategy, and (iv) perfect foresight on maximum levels at both reservoirs and the Heishiguan peak. Also check whether the observed hydrograph fell within the ensemble's predictive intervals at each lead time. If it fell outside, the error model's tail is too thin, and that is a key finding.
- **Leakage control.** If the 2021 flood was used to train the forecasting model or to fit the error model, its forecasts are not out-of-sample. I would then refit the error model without it, and state clearly which results are in-sample.
- **Sensitivity analyses:**
  - error-model form and tail assumption;
  - cross-correlation assumption (independent / fitted / fully dependent);
  - lead time and replanning interval;
  - risk tolerances α, β;
  - number of scenarios;
  - initial reservoir level at flood onset (start at flood-limited level versus higher);
  - routing-parameter uncertainty;
  - intervening-flow uncertainty.
- **Synthetic scaling.** Scale observed large-flood hydrographs (e.g., the 2021 event) up and down to see how the value of uncertainty-aware coordination changes with flood magnitude. Label these clearly as synthetic.

## 9. Deliverables and threats to validity

**Deliverables:**
1. A validated forecast-error model per reservoir, with cross-basin dependence and stated tail behavior.
2. A table and figures of the risk gap (deterministic-believed versus ensemble-evaluated versus realized) by reservoir, Heishiguan, lead time and magnitude, decomposed by error source.
3. A Pareto front of upstream versus downstream risk, and of flood risk versus retained storage, under uncertainty.
4. A comparison of coordination strategies on held-out events and on 2021.
5. Operational guidance: burden-allocation principle, pre-release trigger based on forecast quantile, and timing coordination, with the conditions under which they hold.

**Threats to validity:**
- Few large floods are available for estimating the error tail.
- Possible in-sample forecasts.
- Nonstationarity (e.g., the forecasting model is retrained over time, so archived errors may not represent current skill).
- Routing simplifications.
- Real operational constraints not in the data, such as gate-operation rules, downstream channel conditions and administrative dispatch rules.

Results should be framed as conditional on these. Claims about absolute probabilities should be weaker than claims about relative strategy rankings.
