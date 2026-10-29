# Forecast-informed flood-season level for the Three Gorges Reservoir: study design

## 1. Provisional answer

**Recommended operation.** Replace the fixed 145 m level, and the current yes/no allowance up to 148 m, with a **forecast-conditioned upper bound** that is recomputed every day. The level may sit above 145 m only up to the height from which it can be **brought back to 145 m before a forecast flood needs the flood-control storage**. That drawdown must be computed with a conservative (upper) quantile of the forecast inflow, within the release, drawdown-rate and downstream limits. When the forecast shows a large flood inside the reliable lead time, the bound falls back to 145 m.

**How high, provisionally.** About **146.5–148 m in ordinary conditions, and 145 m whenever a large inflow is forecast**. Going above about 148 m only makes sense if two things hold:

- the 4–7-day forecasts prove reliable for high flows, and
- the allowed daily drawdown rate permits a 4–5 m drop inside that lead time.

From what is given, I do not expect both to hold. The binding limit is probably **time, not storage**: how many metres can be drawn down safely inside the lead time the forecast can be trusted for. The arithmetic is in section 3.

**Safety verdict.** The study can show "no worse than current practice" only through a stress test. That test routes design and historical floods with synthetic forecast errors fitted to the 2019 data. **One season of hindcasts cannot show safety on its own.** It holds too few independent large floods. The 2019 replay can show feasibility and the size of the benefit, not the safety level.

**Hydropower gain.** The ceiling is set by the extra head, about **3–5 % more flood-season generation** if the level were held 3 m higher all season. A realistic dynamic bound averages less, so I expect roughly 1–3 %. Storing water adds little by comparison. A 3 m rise holds about 2×10⁹ m³, which is small next to the volume spilled in a wet season. The claim that the higher level substantially cuts annual spill should be tested by mass balance, not assumed.

## 2. The questions that decide the answer

1. **Can the reservoir always get back to 145 m in time?** This depends on three things: the lead time over which forecasts of a large inflow are reliable, the daily drawdown rate allowed for bank stability, and the outflow downstream reaches can take during prerelease. It sets the ceiling.
2. **What does "safe enough" mean, and against what?** I propose a non-compensable criterion. The proposed rule must not raise any of these probabilities above their values under current practice (and under the static 145 m rule):
   - exceeding the reservoir's characteristic flood levels;
   - exceeding the Jingjiang (Shashi) safe level or flow;
   - losing compensation capacity for the Chenglingji/Dongting reach.

   The comparison uses the upper confidence bound of each estimate, not the central value. Hydropower is compared only among rules that pass.
3. **Can the data resolve the difference?** With one season of forecasts, the answer for rare floods is no. The design must generate the evidence (sections 5–6) and say plainly what 2019 alone can and cannot show.

## 3. Order-of-magnitude checks

**Assumptions.** These are planning values. Each must be replaced by the official curves and limits.

- Flood-control storage between 145 and 175 m: about 22.15×10⁹ m³. Static storage near 145–150 m: about 0.6–0.7×10⁹ m³ per metre. I use **0.65×10⁹ m³/m**, read from the static curve. TGR is a long river-channel reservoir, so the dynamic (backwater) storage at high inflow differs from this, and the study must use both.
- Turbine discharge capacity: roughly 30,000 m³/s. Installed capacity: 22.5 GW. Flood-season gross head near 145 m: about 75–80 m, which I believe is near or below the rated head (verify).
- Allowed daily drawdown: an unknown limit set for bank and landslide stability. I test **0.6 m/day and 1.0 m/day**.

**Volume at stake.** Raising 145 → 148 m stores 3 × 0.65×10⁹ ≈ **2.0×10⁹ m³**. That is about 9 % of the 145–175 m flood-control storage.

**Net release needed to remove it.**

| Drawdown time | Net release (outflow − inflow) |
|---|---|
| 3 days (2.59×10⁵ s) | 2.0×10⁹ / 2.59×10⁵ ≈ **7,700 m³/s** |
| 5 days | ≈ **4,600 m³/s** |
| 1 day | ≈ 23,000 m³/s (not credible) |

**Time limit from drawdown rate.**

- At 0.6 m/day, a 3-day lead time recovers at most 1.8 m, so the ceiling is about **146.8 m**. Recovering 3 m needs 5 days, which means relying on 5-day forecasts.
- At 1.0 m/day, 3 days recover 3 m, so the ceiling is about **148 m**. A 5 m rise to 150 m needs 5 days.

This is why I expect the ceiling to sit near the present 148 m, and to depend on the drawdown-rate limit more than on storage.

**Downstream limit during drawdown.** If inflow is already, say, 35,000 m³/s when drawdown starts, outflow must reach about 42,700 m³/s for 3 days. That exceeds turbine capacity, so the drawdown itself spills water. It also raises Jingjiang flows above the natural flow ahead of the flood peak. Prerelease must therefore start while inflow is lower, which again requires longer reliable lead times.

**Forecast-error aggregation.** The drawdown decision depends on the 1–3-day inflow volume, not on single days. The errors at leads 1–3 from one issue time are strongly correlated. With equal spread σ and pairwise correlation ρ = 0.7 (illustrative), the variance of the 3-day sum is 3σ²(1 + 2·0.7) = 7.2σ², against 3σ² if independence is assumed. The standard deviation is therefore √2.4 ≈ **1.55 times larger**. A margin sized on independent errors would be about a third too small.

**Hydropower ceiling.**

- When outflow is below turbine capacity, output scales with head. +3 m on 75–80 m is **+3.8–4 %**.
- When units are head-limited at large outflows (below rated head), output scales roughly with H^1.5. (78/75)^1.5 ≈ **+6 %**.
- Assume flood-season (June–September) generation of 40–50 TWh. Then a 3 m rise held all season gives at most about 1.5–2.5 TWh. A dynamic bound that averages about 1.5 m and drops to 145 m before floods gives perhaps 0.6–1.2 TWh.
- The stored volume itself, 2×10⁹ m³ at about 0.2 kWh/m³, is worth about 0.4 TWh, and only once. It counts only if that water would otherwise have been spilled, or would not have been available to fill the reservoir at the end of the season.

**What the higher level cannot do.** A 2×10⁹ m³ rise absorbs an excess of 7,700 m³/s over turbine capacity for only 3 days. In a wet season with weeks of inflow above turbine capacity, most spill is unavoidable at any feasible flood-season level. The study must report spill reduction separately from the head gain, so neither is credited to the other.

**Risk illustration.** This only shows how the risk should be combined; the numbers are not estimates.

- Suppose the rule fails to draw down in time with probability p_miss = 0.05 when a flood near the 100-year size arrives (annual probability 0.01). Suppose a failed drawdown always pushes the reservoir past the 100-year control level. Then the added annual exceedance probability is 0.01 × 0.05 = 5×10⁻⁴, and the 1 % standard becomes about 1.05 %.
- Over 50 years: 1 − 0.99⁵⁰ = 39.5 % rises to 1 − 0.9895⁵⁰ ≈ 41.0 %.
- Under the "no worse than current practice" criterion, an increase this size fails unless current practice has the same miss rate. The study must therefore estimate p_miss for both rules on the same floods.

## 4. Data: what is given, what is needed

**Given:**

- daily inflow forecasts at leads of 1–7 days for the 2019 flood season;
- the matching observed inflows.

**Must be added.** I assume these can be obtained from the operator and the basin authority.

- Static and dynamic level–storage curves, outlet and spillway capacities by head, unit characteristics, and the tailwater–outflow relation, including Gezhouba's effect.
- The current operating rules in executable detail:
  - the 145–148 m conditions and how a 3-day forecast "supports" a rise;
  - the compensation rules for Jingjiang and Chenglingji, with the storage layers used for each;
  - the release caps by level;
  - the rules on drawdown rate and outflow change;
  - navigation constraints.
- Downstream safety thresholds: Shashi/Zhicheng safe level and flow, the Chenglingji control level, and interval inflow between Yichang and the control points (Qingjiang and others).
- The design and check flood hydrographs (typical-year shapes scaled to the return periods) and a multi-decade daily (better, 6-hourly) inflow record.
- 2019 actual operation: levels, outflows, spill, generation, and grid or navigation instructions. This gives a context baseline and helps calibrate the simulator.
- Ideally, hindcasts from more years made with the **same forecast system and version** that will be used in operation. Without them, the error model rests on one season.

**Data caveats to state:**

- "Observed" TGR inflow is itself back-calculated from levels and outflows, so it carries error, especially in dynamic-storage conditions.
- Daily data hide peaks within the day.
- If the forecast system has changed since 2019, the conclusions apply only to the 2019 version.

## 5. Study design

### 5.1 Simulator and baselines

- Build a daily water-balance simulator, with a 6-hour version for design-flood stress tests. It needs level-dependent release capacity, ramping and drawdown-rate limits, unit dispatch with head-dependent output and the tailwater relation, and Muskingum-type routing from Yichang to Zhicheng/Shashi plus interval inflow.
- Check it against 2019 recorded levels and outflows, using recorded outflows as input.
- Encode the comparators in executable form:
  - **B0, static 145 m** (the design basis).
  - **B1, current practice**: 145 m, raised up to 148 m when the 3-day forecast supports it, under the operator's actual conditions.
  - **B2, 2019 historical operation.** This is context only, not a controlled counterfactual. Its starting levels and decisions reflect grid dispatch, navigation, upstream cascade releases and instructions that the simulation leaves out.
  - **B3, perfect forecast.** This is the non-deployable upper bound on what forecasts can add.

### 5.2 Forecast reliability by lead time

- From the 2019 pairs, compute bias, relative-error spread, qualified rate and NSE at each lead from 1 to 7 days. Stratify by flow, with high flows (for example above the turbine-capacity level) treated separately, and by rising versus falling limb.
- Check normality and test for under-forecasting of peaks.
- Estimate the correlation across leads for each issue time, and the serial correlation across issue days.
- Count how many distinct flood rises 2019 contains. That count, not the ~120 days × 7 leads, is the effective sample for high-flow error. Tail quantiles such as the 95th or 99th percentile at 3–7 days will be poorly constrained. Report confidence intervals on them.
- Decide which lead times support which action:
  - **1–3 days:** the drawdown commitment and the bound.
  - **4–7 days:** only an early warning that starts a precautionary drawdown or stops a rise. These leads must never be used to *permit* a higher level unless the error analysis shows reliability at high flows.

### 5.3 Error model and scenarios

- Fit relative-error marginals by lead time and flow class, joined by a copula, or a simple multivariate normal on transformed errors if fits allow. The model must reproduce the correlation across leads.
- Generate synthetic forecasts in two settings:
  - (a) the long historical record;
  - (b) design and check floods at a range of return periods, plus magnified historical floods. Include **successive flood waves** and early or coinciding Dongting and Qingjiang floods.
- Check that the scenarios match the 2019 statistics (coverage of observed values, rank histograms, spread against error).
- Inflate the error spread (×1.5, ×2) and vary the correlation in a sensitivity sweep, because one season cannot pin down the tails.
- Also sample non-forecast uncertainty that changes the outcome:
  - initial level within the allowed band;
  - interval inflow;
  - dynamic versus static storage;
  - discharge-capacity error;
  - level-measurement error.

### 5.4 Candidate operating rules

All candidates run in a closed loop. Each day the bound is recomputed from that day's forecasts, the day's release is executed, and the state is updated with the *observed* inflow.

- **R1, dynamic bound from 1–3-day forecasts.**

  V(Z_up) − V(145) ≤ Σ_{t=1..L} [Q_out,max(t) − Q̂_in^(p)(t)]·Δt

  where:
  - Q̂_in^(p) is the p-quantile (upper side) of forecast inflow;
  - Q_out,max is the smallest of three limits: outlet capacity, the downstream prerelease limit (net of interval inflow), and the natural flow that would have occurred, so the drawdown does not create a man-made flood;
  - the daily level drop is capped at the allowed rate;
  - drawdown must be finished before forecast inflow reaches the flow at which flood-control storage starts to be used.

  Z_up is also capped by an absolute ceiling (test 147, 148, 149, 150 m), and by the backwater and inundation check upstream.
- **R2, as R1 plus a 4–7-day early-warning trigger** that starts drawdown sooner or stops a rise.
- **R3, rolling optimization.** This is a scenario-based model-predictive scheme that maximizes generation under the same risk constraints. It serves as a benchmark that shows whether the simpler rule leaves much value unused. It is not necessarily the adoption candidate.
- **Stage logic, written into each rule:**
  - **Normal:** hold up to Z_up.
  - **Prerelease:** draw down toward 145 m at the limited rate when the forecast exceeds the trigger.
  - **Flood control:** the current compensation rules apply unchanged from 145 m.
  - **Recession:** empty the flood storage down to 145 m, or down to the new Z_up only once the reliable-horizon forecast shows no further flood. Never keep flood storage as "free water".
  - **Fallback:** revert to the B1 logic if the forecast is missing or late, or if observed inflow exceeds the forecast quantile by more than a set margin over consecutive days. Correct gradually rather than with a release jump.
  - **Abort rule:** if the flood arrives early during a drawdown, switch at once to the compensation rules at whatever level has been reached.
- **Tuning.** The parameters are the quantile p, L and the absolute ceiling. Keep the parameter count small, set the parameters from the error model and the design-flood stress test, and do not tune them on the 2019 replay.

### 5.5 Safety evaluation (applied first; non-compensable)

**Failure events, counted over the whole process and not only at the forecast peak:**

- the reservoir exceeds each characteristic control level: the 100-year compensation level, the design level of 175 m, and the check level of 180.4 m;
- Shashi exceeds its safe level, or Zhicheng its safe flow, for floods up to the 100-year design;
- for medium floods, compensation storage for Chenglingji is not available, judged by whether the Chenglingji control level is exceeded;
- the backwater level at upstream control sections exceeds the inundation lines;
- a man-made rise occurs: prerelease pushes downstream flows above what the natural flood would have produced;
- the drawdown-rate or ramping limit is breached.

**Estimation:**

- Run Monte Carlo over the design and historical floods with synthetic forecasts and N ≈ 10,000 error series per flood class. For a conditional probability near 0.01, the standard error is √(0.01·0.99/10⁴) ≈ 0.001, enough to separate rules that differ by a few tenths of a percent.
- Report each conditional probability with its confidence interval.
- Combine with the flood-occurrence probability into annual and 50-year risk, consistently.
- Report **p_miss**, the probability that a drawdown was needed but not completed, as the key diagnostic.

**Acceptance.** For each failure event, the upper confidence bound under R1, R2 and R3 must be ≤ the value under B1, and must meet the design standards. Do not accept rules that pass only on central estimates. Then sweep the ceiling and p, and report the highest bound that passes, with the reason it binds (drawdown rate, lead time or downstream limit).

### 5.6 Benefit evaluation (only for rules that pass)

- Flood-season generation, split into a **head effect** and a **stored-volume effect**.
- Spilled volume, and the energy that spill represents.
- Water level on the last day of the flood season, and the effect on end-of-season impoundment.
- Days above 145 m, number of prerelease events, and number of "false alarm" drawdowns. The cost of a false alarm is head lost for the days it takes to rise again.
- Indicators that are not flood-related but matter at TGR: sediment deposition from holding the level higher in the high-sediment season (the reason for the low flood-season level), and navigation and Gezhouba outflow fluctuation. These indicators are reported, not traded against safety.

### 5.7 Replay of 2019

- Run the rules day by day in a closed loop with the 2019 forecasts as issued.
- Show the trajectories (level, outflow, bound, forecast against observed), the drawdown episodes, any forecast misses, generation and spill, all against B0, B1 and B3 under the same initial level and the same constraints.
- This shows that the rule is workable and how large the gain is in one real season. It is **in-sample for the error model** and holds few large floods. Say so explicitly, and do not quote a risk from it.

### 5.8 Robustness

Sensitivity to:

- error inflation and correlation;
- drawdown rate (0.6 against 1.0 m/day);
- downstream prerelease limit;
- daily against 6-hour steps;
- static against dynamic storage;
- successive floods;
- the timing of Dongting and Qingjiang floods (early, together with, or after the TGR release);
- the upstream cascade's regulation, which changes both inflow and forecastability.

Also report the **forecast accuracy at which each rule stops passing**. This tells the operator what to monitor.

## 6. How the result will be presented

The main exhibit is a side-by-side table of B0, B1, R1 at its passing ceiling, R2, R3 and B3. The rows are:

- each failure probability with its confidence interval;
- p_miss;
- generation (head and volume effects);
- spill;
- end-of-season level;
- false-alarm drawdowns.

The table should state which rules are dominated and which rule is recommended. Trajectory plots for the 2019 floods and for the largest design-flood scenarios explain *why* each rule passes or fails.

## 7. Adoption

- **Who approves.** As far as I know, the TGR operating regulations and the annual flood-season operation plan are approved through the Ministry of Water Resources and the Changjiang Water Resources Commission, with the Yangtze flood-control and drought-relief headquarters directing flood operation. China Three Gorges Corporation runs the plant. The current rules stay the legal basis until an amended regulation or plan is approved.
- **What to agree in advance.** Agree the acceptance criteria of section 5.5 with these bodies before the study reports.
- **How to trial it.**
  - First, one flood season of **shadow operation**: compute the bound daily beside the current rule without acting on it, and log forecast against outcome.
  - Then, if approved, a documented temporary deviation within the existing 148 m allowance, before any change to the ceiling.
- **Reversion.** Revert to the current rule when the forecast is missing, late or diverging, or when equipment fails. The duty dispatcher decides under the headquarters' authority, and every decision is logged for audit and after-event review.
- **Who must be warned of prerelease.** Downstream provinces (Hubei, Hunan), emergency services, navigation authorities and the grid dispatcher.
- **Versions.** Keep version control of the forecast system, and re-verify the error model whenever the forecast system changes.

## 8. What would confirm or change the provisional answer

**Raise the ceiling (toward 149–150 m)** if all three hold:

- multi-year hindcasts show that 4–5-day forecasts of high flows are unbiased with tight upper quantiles;
- the allowed drawdown rate is about 1 m/day or more;
- downstream can accept prerelease flows early enough.

**Lower it to about 146–147 m, or confine the rise to periods after the main flood season,** if any of these holds:

- the drawdown rate is limited to about 0.6 m/day;
- 3-day forecasts under-predict rising limbs;
- inflating the error spread pushes p_miss above that of current practice;
- the Chenglingji compensation or the upstream backwater checks bind.

**Revise the hydropower estimate** if, once units are head-limited and spill timing are modeled, the gain falls toward the stored-volume effect alone (a few tenths of a TWh). In that case the change would not be worth the added operating complexity.
