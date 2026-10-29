# Real-Time Flood Release Decisions at Lishimen Reservoir: Plan and Provisional Recommendation

## 0. Bottom line

- **How I would frame it.** This is a sequential decision problem under inflow uncertainty. At each hour the operator commits to a release using only what is known by then: the current level, recent inflow back-computed from the water balance, observed rainfall at six gauges, and possibly an uncertain forecast. The release is scored later against the true inflow. The three goals pull against each other: upstream level risk, downstream discharge risk, and storage use. So the main output should be a **trade-off set of operating policies, each tested under explicit forecast-error levels**, followed by a transparent selection rule. A single "optimal" hydrograph would not answer the question.
- **What I would compare.** (a) The current regulation rule as the baseline. (b) A perfect-foresight optimum as the upper bound. (c) An offline-optimized adaptive rule that needs no forecast. (d) Rolling-horizon model predictive control (MPC) driven by a forecast with controlled error. (e) The same MPC run on an ensemble of forecasts, with chance constraints.
- **Provisional recommendation.** Use an **optimized adaptive (level + observed inflow + observed rainfall) release rule as the operational default**. Treat **ensemble/chance-constrained MPC as the upgrade**, to be adopted only once a hindcast shows the forecast is skilful enough to beat the rule. Pick one plan from the Pareto set with a **priority-ordered, robustness-based rule**: dam safety first, then the downstream limit, then storage efficiency, and choose the most robust plan across error levels. Weighted scoring such as TOPSIS or entropy weights would serve only as a cross-check. The reason: forecasts are not operational, their errors are largest exactly in the floods that matter, and a 296 km² basin with steep floods gives little lead time. All of this favours a policy that degrades gracefully when the forecast is wrong.
- **Feasibility caveat to settle first.** The test event is roughly a 100-year flood. The upper flood-control level (180.69 m) is designed for the 20-year flood, and the design flood level (181.34 m) for the 100-year flood. For this event it may therefore be **physically impossible** to keep both the level at or below 180.69 m and the release at or below 1000 m³/s, even with perfect foresight. That has to be checked before any policy is judged (Section 2). If it is impossible, the agency must state which constraint gives way first. The analysis can show the cost of each choice, but it cannot make that choice for the agency.

## 1. Data checks and key assumptions

| Issue | What I would do | Why |
|---|---|---|
| Flood-control capacity is 35.7 Mm³ in the text but 31.4 Mm³ in the table | Do not pick either number. Compute usable flood storage directly from the level–storage curve as S(180.69) − S(176.04), and S(181.34) − S(176.04) for the design flood level. Check that S(176.04) matches the stated initial storage of 121.8 Mm³. Report which source value the curve supports. | The two values differ by about 13%. That is enough to change whether the test flood can be held below 1000 m³/s. Every risk result depends on this number, so it must come from one consistent curve. |
| Inflow series are back-computed (level change + outflow) | Check them for negative or oscillating hourly values and smooth them lightly, keeping event volume and peak timing. Check event volume against basin rainfall (runoff coefficient). | Hourly back-computed inflow is noisy. Noise in the "truth" would be scored as forecast error or as a constraint violation. |
| Ramping limit is not quantified | Get the value from the agency. Until then, run a sensitivity analysis over a plausible range. | Ramping limits how fast the reservoir can respond to a steep rise, which strongly affects both risks. |
| Maximum outlet capacity depends on level | Apply the level–discharge curve as a state-dependent upper bound in every model. | At the flood-limit level the outlet may not be able to release 1000 m³/s. That limits pre-release. |
| Lower bound: 0 vs 20.4 m³/s (generation flow) | Use max(ecological minimum, generation flow) as the base case and 0 as a sensitivity case. | This has little effect on flood outcomes, but the bound has to be stated. |
| Where does "1000 m³/s safe discharge" apply? | Assume it applies to the dam release. Flag that if the control point is further downstream, local inflow from the intervening area must be added. That inflow is not in the data. | If the control point is downstream, the dam release allowance shrinks during the storm, because local runoff peaks at the same time. |
| Evaporation is sparse | Ignore it within a flood event (2 days, heavy rain). Use it only, if at all, for a rainfall-runoff model's antecedent-moisture state. | It is negligible at event scale. |
| Confidential data | Keep all processing on agency or approved machines. Report results only in aggregate or normalized form if needed. | This is a requirement. |
| Starting state | The initial level is the flood-limit level of 176.04 m, as given. Pre-flood drawdown below 176.04 m toward the lower limit (160.97 m) is **out of scope by default**. I would treat it only as a scenario if the agency allows pre-release when a typhoon warning is issued. | Pre-release adds storage, but it costs irrigation and supply water and relies on a typhoon forecast that is not part of the brief. |

## 2. Step 1: Feasibility and benchmark with perfect foresight

For each of the 22 events, and especially the test event 20040812:

1. **Volume check.** Compute the inflow volume above 1000 m³/s, V_excess = Σ max(Q_in − 1000, 0)·3600, and compare it with usable flood storage (Section 1). If V_excess exceeds the storage up to 180.69 m, the two goals cannot both be met. The question then becomes how to split the overrun: hours and volume above 1000 m³/s, versus metres and hours above 180.69 m. Also check against 181.34 m. Exceeding the design flood level is a dam-safety issue and should be treated as a hard constraint.
2. **Perfect-foresight optimization.** Use LP/NLP or dynamic programming over the full event with the true inflow, subject to mass balance, outlet capacity, release bounds and ramping. Solve it for several objective priorities: minimize peak level, minimize peak release, and minimize a weighted combination. This gives the **best possible outcome** for each event. Every real-time policy is then measured as a gap to this bound. The bound is also the "zero forecast error" end point of the degradation curve.

This step tells the agency how much of any shortfall is caused by uncertainty and how much is simply physics.

## 3. Step 2: Building the information the operator would have

Releases are decided "before the true inflow is known". So I would model the information state explicitly:

- **Observed at hour t:** level, release, inflow back-computed up to t (possibly lagged and noisy), and hourly rainfall at six gauges up to t.
- **Forecast, which needs to be built because none is operational:** a rainfall-runoff model driven by observed gauge rainfall. Candidates are a conceptual model (for example the Xinanjiang saturation-excess model, the usual choice for humid Zhejiang catchments) with a unit hydrograph, and a data-driven model (for example gradient boosting or an LSTM on lagged rainfall and inflow). Calibrate with leave-one-event-out cross-validation over the 22 events, and **exclude the test event from calibration and tuning**.
  - With only observed rainfall, useful lead time is limited to roughly the basin response time. In a 296 km², 35 km catchment that is likely to be a few hours. I would estimate it from rainfall–inflow lag correlations rather than assume it.
  - Beyond that horizon the forecast also needs future rainfall, which is unavailable. I would represent it with "no further rain", "persistence" and scenario rainfall as bounding cases.
- **Hindcast error analysis.** Using the cross-validated hindcasts, measure error by lead time and by flood magnitude: bias, peak magnitude error, peak timing error, and autocorrelation. This tests empirically the brief's statement that errors are largest for big floods, and it calibrates the synthetic error model in Section 5.

## 4. Step 3: Candidate operating policies

| Policy | Description | Strength | Weakness |
|---|---|---|---|
| P0: Current regulation rule | Staged release by level band and inflow, as written in the reservoir's flood-control rules, which I would obtain from the agency | Baseline the agency already trusts | May be overly cautious or reactive |
| P1: Optimized adaptive rule | A parameterized release function of level, current estimated inflow, inflow trend and recent catchment rainfall: for example piecewise-linear release targets by level zone, with an inflow- and rain-dependent "anticipation" term. Parameters are optimized offline (multi-objective evolutionary search, e.g. NSGA-II or Borg) across all calibration events, including **scaled events** (Section 6). | Needs no forecast. Robust and transparent. Easy to put in an operating manual. | Cannot anticipate a peak before the rain is observed |
| P2: Deterministic MPC | Each hour, optimize releases over a horizon of H hours (H = forecast lead, about 6–12 h) given a point forecast. Apply only the first hour, then re-solve. Include a terminal storage cost so the plan does not empty or fill storage short-sightedly. | Uses forecast information. Handles ramping and capacity limits naturally. | Overconfident: optimizes against a forecast that may be badly wrong |
| P3: Stochastic / chance-constrained MPC | Like P2, but optimized over an ensemble of inflow traces drawn from the error model. Constraints are written as P(Z > 180.69) ≤ α_Z and P(Q_release > 1000) ≤ α_Q, or as CVaR objectives. | Directly answers "limit the *risk*". Lets risk tolerance be set explicitly. | More complex. Results depend on the error model being right. |

All policies use the same mass balance, curves, bounds and ramping. In every policy, releases above 1000 m³/s are allowed only when needed to protect the dam: the release ceiling becomes the outlet capacity once the projected level approaches 181.34 m. That mirrors standard practice: protect the downstream while the dam is safe, and protect the dam when it is not.

**How "use storage sensibly" enters.** Penalise holding storage above the flood-limit level early in the event while inflow is still rising, which is the aggressive failure. Also penalise releasing more than needed when the end-of-event level stays far below what was available, which is the cautious failure. Concretely, use two metrics. (i) **Storage utilisation ratio**: peak flood storage used ÷ usable flood storage. Near 1 without overrun is efficient. (ii) **Timing of storage use**: the fraction of flood storage already used at the time of the inflow peak. Too high means the reservoir cannot absorb the peak. Also require a recovery term: the level should be able to return to 176.04 m within an agreed time after the event, in case a second typhoon follows.

## 5. Step 4: Measuring how forecast error degrades outcomes

1. **Error model.** Generate perturbed forecasts from the true inflow, with errors that:
   - are multiplicative and grow with lead time;
   - grow with flow magnitude (heteroscedastic), matching the hindcast finding;
   - are autocorrelated in time (AR(1) in log space), not white noise;
   - include **peak magnitude bias** (underestimation is the dangerous case) and **peak timing shift** (±1–3 h).

   Calibrate the "realistic" error level to the hindcast statistics from Section 3. Then scale it from 0 (perfect) through realistic to about 2× realistic.
2. **Monte Carlo.** For each policy, event and error level, run many (for example 500–1000) closed-loop simulations. In each one the policy sees a new forecast every hour while the reservoir responds to the true inflow.
3. **Outputs.**
   - **Upstream:** P(Z_max > 180.69), mean and 95th-percentile exceedance depth and duration, and P(Z_max > 181.34).
   - **Downstream:** P(Q_max > 1000), and hours and volume above 1000.
   - **Storage:** utilisation ratio, utilisation at the peak, end-of-event level and recovery time.
   - **Operational:** ramping violations, which should be zero by construction, and the number of large release changes.
   - **Degradation curves:** each metric plotted against error level. Report the **value of forecast information** (no-forecast rule P1 vs perfect-forecast P2) and the **break-even error level**: the error level beyond which forecast-based MPC is no better, or is worse, than P1.
   - **Asymmetry:** separate under-forecast from over-forecast effects. Under-forecasts delay the release and put the level at risk. Over-forecasts trigger early high releases that use downstream capacity and waste stored water.

My **provisional expectation**, to be confirmed by these runs, is that MPC gives the clearest gains on moderate floods. For the largest floods, which have the largest errors, its advantage over a good adaptive rule shrinks or reverses, and the chance-constrained version (P3) degrades more gracefully than deterministic MPC (P2).

## 6. Step 5: Test design and robustness

- **Calibrate, tune and select** on the 21 non-test events using cross-validation. Run event 20040812 **only once, as an out-of-sample test**. Tuning on it would overstate performance.
- **Small-sample stress test.** 22 events is a small sample with only a few large floods. Augment it by scaling observed hydrographs (by peak, by volume, or with a common shape) to the 20-, 50- and 100-year design values and somewhat beyond. Include hydrographs with double peaks and late peaks, which are typical of typhoon rain. This guards against a rule that only works for the floods in the record.
- **Sensitivity analyses:** flood capacity of 31.4 vs 35.7 Mm³ (via the curve), ramping limit, minimum release, forecast lead time, and whether the 1000 m³/s limit is at the dam or downstream.

## 7. Step 6: Picking one operating plan

The optimization gives a Pareto set of policies, or policy parameterizations, trading off upstream risk, downstream risk and storage use. To choose one defensibly:

1. **Hard screens, which are non-negotiable:** P(Z > 181.34) must be essentially zero on all design and stress events up to 100-year. Ramping and capacity limits must be respected.
2. **Agency-stated risk tolerances:** for example "P(Z > 180.69) ≤ α_Z for floods up to 20-year" and "P(Q > 1000) ≤ α_Q for floods up to 20-year". For floods larger than 20-year, the agency should state which goal gives way first. I would present the trade-off curve so the agency makes that call, not the analyst.
3. **Among plans that pass**, choose by **robustness across error levels and events**, for example minimax regret against the perfect-foresight bound, or the best 90th-percentile performance. Do not choose by performance at the "realistic" error level alone, because that level is itself uncertain.
4. **Cross-check** with TOPSIS or entropy-weighted scoring and show whether the choice changes when the weights change. If it does change, report that the choice depends on the agency's preferences and should not be presented as objectively optimal.
5. **Transparency:** the chosen plan should come with a one-page operating chart (release vs level and inflow) or a clear MPC configuration, plus its test-event behaviour shown against P0 and the perfect-foresight bound.

## 8. Provisional judgments, assumptions, and what would change them

| Judgment | Key assumptions | Confirms it | Changes it |
|---|---|---|---|
| Default plan = optimized adaptive rule (P1); MPC (P3) as upgrade | Forecasts based on observed rainfall have short useful lead and large errors in big floods | The degradation curves show P2/P3 losing their advantage at realistic error for 50–100-year floods | Hindcasts show useful skill beyond the basin response time (for example with good quantitative precipitation forecasts), so P3 clearly beats P1 at realistic error. P3 would then become the default. |
| For the 100-year test flood, both targets may not be met together | Usable storage is about 31–36 Mm³; the peak inflow is far above 1000 m³/s (the largest hourly inflow in the dataset, 2703 m³/s, may or may not belong to this event) | The volume check (Section 2) shows V_excess > usable storage | The volume check shows the flood fits within storage. The problem then becomes purely about timing and uncertainty. |
| Chance-constrained MPC degrades more gracefully than deterministic MPC | The error model captures the bias and heteroscedasticity seen in the hindcasts | The Monte Carlo results | The hindcast errors turn out small or unbiased, so P2 ≈ P3 and the simpler P2 is preferable |
| Robustness-based selection is more defensible than weighted scoring | The agency values explainable decisions and has priority rules | The agency accepts the priority order | The agency already has formal weights or regulatory scoring, which would then be used, with sensitivity shown |

**Main limitations to state with the results:** small event sample; noisy back-computed inflow; ramping limit not yet known; the downstream control point possibly not at the dam; any forecast error model is a stand-in until real forecasts exist; and results for a single test event are illustrative, not proof.
