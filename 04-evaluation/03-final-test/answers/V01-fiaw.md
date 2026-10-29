# V01: Forecast-informed dynamic flood-season level control at the Three Gorges Reservoir

## 0. Summary of the approach

The decision has two linked parts. On each day *t* I would:

1. **Decide which lead times can be trusted today.** For each lead time *L* = 1…7 days, estimate the probability that relying on today's forecast for that horizon leads to (a) failing to get back to 145 m before inflow exceeds 35,000 m³/s, or (b) having to release more than the safe discharge to get there. A lead time is trusted today if both probabilities are at or below the accepted risk level α. These probabilities depend on lead time and on today's forecast, because the error distribution changes with lead time, with flow magnitude and with whether the forecast is rising or falling.
2. **Set the allowable level.** Within the trusted horizon, the highest level the reservoir may hold today is the highest level from which, at the chosen risk quantile of the forecast inflows, it can still be drawn down to 145 m before the forecast flood, without releasing more than the safe discharge minus local inflow and after allowing for the 2-hour operating delay. This gives a daily upper bound Z_up(t, α). The operating level is then chosen between 145 m and Z_up(t, α) to maximize hydropower.

I would evaluate the rule by simulating the 2019 test season day by day against observed inflows. The two risks and the power output would be compared with the current 3-day / 148 m practice simulated in the same way. Repeating this for a range of α values gives a risk–benefit curve, which answers the agency's question about how the result depends on the risk it accepts.

## 1. Assumptions (stated because the brief does not specify them)

- **A1. Error history.** Forecast–observation pairs are available beyond the 2019 test window, ideally several previous flood seasons. The error model must be fitted on data outside the test period, or the 2019 evaluation is in-sample. If only 2019 exists, I would fit and test with leave-one-block-out cross-validation within the season and report the result as a much weaker test.
- **A2. Local inflow.** Inflow between the dam and the Jingjiang reach is not among the listed data. I need an estimate of it, either observed series or a design allowance, because the release limit at the dam is effectively 35,000 m³/s minus local inflow. If it is unavailable, I would use a conservative allowance and run a sensitivity test on it.
- **A3. Power model.** I assume a standard head-dependent power model: output = efficiency × head × turbine flow, with head from the level-storage relation and a tailwater–discharge relation. Turbine capacity limits and minimum-output / navigation constraints come from the current operating rules. If the agency's tailwater curve and unit limits are not in the supplied rules, I need them.
- **A4. Daily step.** With a daily step, the 2-hour delay is a small loss of drawdown time (about 2/24 of a day of release capacity). It still matters for the first day of a pre-release, and I would subtract it explicitly rather than ignore it.
- **A5. Flood onset.** "Before a flood arrives" means the day on which observed inflow first exceeds 35,000 m³/s, which is the same threshold that triggers pre-release in the current rules. I would check this definition with the agency, because it determines how upstream risk is counted.
- **A6. Design flood safety.** Raising the starting level must not reduce protection against the design flood (1-in-100 for the Jingjiang reach) or the check flood. Within this framework, real-time drawdown is what keeps that protection intact, so I would also check it separately (Section 6).

## 2. Step 1: Characterize forecast error by lead time

Data: daily deterministic forecasts for lead times 1–7 days, matched to observed inflows.

1. **Build the error dataset.** For each issue date and lead time, compute the error. I would use relative or log-ratio error rather than absolute error, because errors at the Three Gorges are likely to grow with flow magnitude. I would check this assumption with plots and switch to absolute error if it does not hold.
2. **Condition the errors.** Stratify or regress the errors on:
   - lead time;
   - forecast magnitude, for example below or above about 25,000 m³/s and near the 35,000 m³/s threshold;
   - forecast trend (rising or falling limb);
   - recent forecast performance, for example the error of yesterday's 1-day forecast, if errors are persistent.

   The aim is to find out whether a 5-day forecast is reliable on some days but not others. That is what "trusted on a given day" means, as opposed to a fixed lead time for the whole season.
3. **Keep the error structure across lead times.** The decision depends on the cumulative inflow volume over the drawdown window, not only the error on one day. Errors at different lead times within one forecast issue are correlated. I would therefore resample complete historical error vectors (lead times 1–7 from the same issue date) instead of drawing each lead time independently, or fit a copula across lead times if the sample is large enough. Treating them as independent would understate volume risk.
4. **Score the threshold forecasts.** For the 35,000 m³/s threshold at each lead time, tabulate hits, misses and false alarms, and compute probability of detection and false alarm ratio. The brief notes that false alarms happen. False alarms cost power through unnecessary pre-release but do not create flood risk. Misses (actual inflow above 35,000 when the forecast was below) are the safety-critical case, and they are the main input to upstream risk.

Output: for each day *t* and lead time *L*, a predictive distribution of the inflow trajectory over the next *L* days, conditional on today's forecast.

## 3. Step 2: Rule for the allowable level (Z_up)

For each day *t*, trusted lead time *L* and risk level α:

- Let Q_safe,dam(τ) = 35,000 − Q_local(τ) be the maximum allowable release at the dam on day τ.
- Let Q_in^(1−α)(τ) be the upper (1−α) quantile of inflow on day τ from the error model. Using an upper quantile is the conservative choice: higher inflow means less net drawdown.
- The drawdown volume available before the forecast flood day *d* (≤ *L*) is

  ΔV(t, L, α) = Σ_{τ = t+1 … d} [Q_safe,dam(τ) − Q_in^(1−α)(τ)] · Δt − (2 h delay loss).

  Only days on which the bracket is positive add to drawdown capacity.
- Then Z_up(t, L, α) = level from the level–storage curve at storage V(145 m) + ΔV, capped at a physical or regulatory ceiling.

**Order-of-magnitude check (approximate).** With falling-limb inflow of about 25,500 m³/s and a 35,000 m³/s limit, one day of drawdown removes about (35,000 − 25,500) × 86,400 ≈ 8 × 10⁸ m³. Local inflow reduces this. Three days gives about 25 × 10⁸ m³. The flood storage of 221.5 × 10⁸ m³ between 145 m and 175 m averages roughly 7 × 10⁸ m³ per metre, and less near 145 m where the reservoir area is smaller. So three days of drawdown corresponds to a rise of a few metres, which is consistent with the current 145–148 m band. This suggests the current rule is roughly a deterministic 3-day version of the same logic. Longer trusted lead times could in principle support several more metres, but only if their quantile inflows, not their point forecasts, leave enough drawdown margin. The actual numbers must come from the level–storage curve.

**Which lead time sets the bound.** A longer lead time gives more days of drawdown, but those days are added at higher uncertainty, so the upper quantile is further above the point forecast. Z_up(t, L, α) is therefore not necessarily increasing in *L*. Today's bound is

Z_up*(t, α) = max over trusted L of Z_up(t, L, α).

The trusted set is defined by the risk test in Step 3 below.

**Choosing the operating level.** Hold the level in [145, Z_up*(t, α)], chosen to maximize power subject to the existing graded release rules, navigation and minimum-output constraints. If the forecast shows a flood within the trusted horizon, the rule switches to pre-release toward 145 m at no more than Q_safe,dam. This keeps the structure of the current operating rules: pre-release, then the flood-control rules, then refill on the falling limb.

## 4. Step 3: Quantifying the two risks

The risks are estimated by Monte Carlo simulation, using many inflow trajectories drawn from the conditional error model (Step 2), simulated through the reservoir under the candidate rule:

- **Upstream risk R_up**: the probability that when realized inflow first exceeds 35,000 m³/s, the level is still above 145 m.
- **Downstream risk R_down**: the probability that the release needed to reach 145 m in time, or to manage the flood, exceeds Q_safe,dam on some day.

Both risks are estimated for each day and summarized over the season, for example as the maximum daily risk and the expected number of failure days per season. The agency should choose which summary is binding; I would report both.

**Lead-time trust test.** Lead time *L* is trusted on day *t* if, at the level Z_up(t, L, α), both R_up and R_down are at or below α. The Monte Carlo procedure therefore determines both outputs the agency asked for:

- which lead times are trusted;
- how high the level may be held.

**Baseline comparison.** The current 3-day / 148 m rule is evaluated with the same error model and simulation. Its risks (R_up,base and R_down,base) are not zero, because 3-day forecasts also miss. "Acceptable compared with current practice" then has a measurable meaning: the new rule's risks must not exceed the baseline's. Setting α equal to the baseline risk is the natural reference point on the risk curve.

## 5. Step 4: Test on 2019 (1 June – 23 July, daily decisions)

1. **Replay.** Simulate the season day by day using only the forecast available on that day (no look-ahead), then advance the reservoir with the observed inflow. Record level, release, spill, power, and any upstream or downstream failures. Run this for the baseline rule and for the new rule at each α.
2. **Ex-ante risk.** For each day of the season, also record the Monte Carlo risk estimates.
3. **Limits of the test.** A 53-day season gives very few flood-onset events, possibly none above 35,000 m³/s. The observed replay will therefore show a power gain, but it cannot by itself show that the risk is acceptable. "No failure observed" in 2019 is weak evidence. The risk claim has to rest on the error model and simulation, checked against out-of-sample history (A1). I would also stress-test with synthetic flood events, for example historical flood hydrographs inserted into the 2019 forecast–observation series with their matching forecast errors.
4. **Calibration check.** Test whether the predicted risk matches observed outcomes. For example, check that observed inflows exceed the (1−α) quantile at about rate α at each lead time, for instance with a probability integral transform histogram or a coverage table. If they exceed it more often, the error model is overconfident, and the lead times it trusts are too long.

## 6. Additional checks

- **Design flood routing.** Route the design flood (1-in-100) and check flood from Z_up starting levels, both with and without the forecast pre-release. Confirm that the Jingjiang protection standard and the 180.4 m check level are not compromised. If they are compromised without pre-release, the rule depends entirely on the forecast. That reliance must be stated, and it argues for a hard cap on Z_up.
- **False-alarm cost.** Count unnecessary pre-releases and the power they cost. A rule that trusts long lead times may lose power to false alarms, which partly offsets the gain from holding a higher level.
- **Power accounting.** Separate the two sources of gain: higher head, and water stored instead of spilled. If inflow is well above turbine capacity, spill continues regardless of level, and the gain comes mainly from head.
- **Sensitivity.** Vary the local inflow allowance, the error model choice (conditional or unconditional, resampled or parametric), the delay, and the definition of flood onset.

## 7. How the answer depends on accepted risk

Over a grid of α values, from below the baseline risk to moderately above it, I would report:

- the number of days on which each lead time is trusted;
- the distribution of Z_up* over the season and its mean;
- R_up, R_down and seasonal hydropower, and the reduction in spilled water.

These results would be presented as a risk–power curve with the baseline 3-day rule marked on it. The agency then chooses a point on the curve; the analysis does not choose it for them. I would point out where the curve flattens, meaning further risk buys little additional power, as a candidate operating point.

## 8. Provisional judgment

These expectations are provisional and must be confirmed by the analysis:

- **1–3 day lead times** are likely trusted on most days. That is the basis of current practice.
- **4–5 day lead times** are likely trusted on some days but not all. The most likely days are when forecast inflow is low to moderate and stable or falling, such as the falling stage near 25,000 m³/s, where errors are smaller and the drawdown margin to 35,000 m³/s is large. They are less likely to be trusted on rising limbs or when forecasts are near the threshold.
- **6–7 day lead times** are likely trusted only rarely for raising the level. They are still useful as an early warning to prepare for pre-release.
- **Result:** a dynamic level that often rises above 148 m on calm, falling-limb days. It would drop back to 145–148 m, or pre-release, whenever the trusted horizon shortens or a flood appears in the forecast. At α equal to the baseline risk, I would expect a measurable power gain with no greater risk than now. Larger gains would require accepting more risk.

**What would confirm or change this:**

- **Confirms it:** conditional error spreads at lead times 4–5 that are clearly smaller in low-flow, falling-limb conditions, and good calibration of the error model's predicted coverage.
- **Changes it:**
  - Errors that are large and not conditional at lead times above 3 would leave the trusted horizon at about 3 days and the gain small.
  - Misses that cluster just before flood onsets would push Z_up down.
  - A large local inflow would shrink the release margin.
  - Failure of the design flood routing check would require a hard cap.
  - Too little out-of-sample forecast history would mean any extended rule should be adopted only provisionally, with monitoring, rather than recommended outright.
