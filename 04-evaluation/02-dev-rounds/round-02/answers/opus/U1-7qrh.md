# Study design: staged (seasonal) flood-limited water levels for a monsoon multipurpose reservoir

## 0. Framing and provisional position

The current rule holds one flood-limited water level (FLWL) for the whole flood season. In a monsoon basin, flood magnitude is strongly seasonal: the large floods come in the core monsoon months, and the early months (onset) and late months (withdrawal and recession) usually carry smaller floods. A single FLWL is set by the core-monsoon design flood, so it keeps more flood space than needed in the shoulder periods. The reservoir then often fails to fill to full reservoir level (FRL) by the end of the monsoon, which costs irrigation supply and hydropower head and energy in the dry season.

**My provisional expectation, to be tested:** raising the FLWL in the late monsoon (the recession period) is the most likely safe and valuable change, because that is when refill is decided and when floods are typically smaller. Raising it in the early monsoon is less certain, because the monsoon onset date varies a lot from year to year and early storms can be large. The core-monsoon FLWL probably stays at or near the current value. This could be wrong. It would be overturned if the seasonal flood analysis shows no clear drop in flood magnitude in the shoulder periods, or if the largest historical or design floods can occur late in the season (for example from post-monsoon depressions or cyclones, which are possible on east-coast basins).

**Key constraint on what the study can claim:** the data listed are enough to judge **reservoir-side** safety (peak reservoir level against the design levels). They are **not** enough to judge **town-side** safety. That needs the downstream safe discharge, the flow from the catchment between the dam and the town, and the travel time. The study design below therefore makes the claim it can support depend on which extra data are obtained (Section 7).

---

## 1. Research question

**Main question.**
Can the single fixed FLWL be replaced by a staged FLWL schedule (for example early, main and late monsoon stages, each with its own FLWL and fixed transition dates or transition rules) that:

- (a) keeps the same or better flood protection for the dam and the downstream town as the current rule, measured against the same design standards; and
- (b) improves irrigation supply reliability and hydropower output, mainly through more storage at the end of the monsoon?

**Sub-questions.**

1. **Seasonal structure.** Do the 45 years of inflow show distinct flood sub-seasons with clearly different flood magnitudes? Are the boundaries between sub-seasons stable over time, and how much do they vary from year to year?
2. **Seasonal design floods.** What is the design flood for each sub-season, set so that the combined risk across all stages is no greater than the annual design standard?
3. **Seasonal FLWL.** For each stage, what is the highest FLWL that still passes that stage's design flood within the reservoir-level and downstream-release limits?
4. **Performance.** Compared with the current rule, how do candidate staged schedules change flood risk and the benefits to the other objectives? How robust are those changes to uncertainty?
5. **Forecasts (secondary).** Can the 1–5-day forecasts safely support a pre-release from a raised FLWL down to a lower one when a large flood is predicted? Can they support dynamic control within a stage?

The scope is deliberately limited. The main contribution is **fixed seasonal staging**. Forecast-informed dynamic control is treated as an extension, because 8 years of forecast archive is short for judging how forecasts behave in rare large floods.

---

## 2. Data

### 2.1 Available data and how each is used

| Data | Use | Limitations to check |
|---|---|---|
| 45 yr daily inflow | Seasonality analysis, seasonal flood frequency, multi-day flood volumes, long-term simulation, stochastic inflow generation | Daily averaging hides the instantaneous peak. Inflow is often back-calculated from the reservoir water balance, which makes it noisy. Check for gaps, upstream regulation and trends. 45 years is short for 1-in-100-year or rarer floods. |
| Level–storage curve | Water balance in routing and simulation | Which survey year? Sedimentation may have reduced storage. Get the latest capacity survey if one exists. |
| Level–discharge capacity curve | Maximum release at each level (spillway and outlets) for routing | Need to know gate operating constraints, rate-of-opening limits and whether outlets and powerhouse flow are included. |
| 8 yr forecasts and observations, 1–5 day lead | Forecast error by lead time and flow size; whether pre-release is feasible | Few large events. Was the forecast system the same over the 8 years? Is the data deterministic or ensemble? |
| Current operating rule | Baseline. Gives the fixed FLWL, FRL, maximum water level (MWL), release rules and any downstream constraints written into it | Find out the basis of the current FLWL: which design flood and which standard. |

### 2.2 Data needed and how important each is

**Critical (without these, town safety cannot be claimed):**

- **Downstream safe discharge** at the town (bankfull or no-damage flow), or a stage–discharge relation at the town plus its flood stage.
- **Flow from the catchment between the dam and the town** (about 40 km). Use gauge records if they exist. Otherwise use rainfall and catchment area to estimate it. Also the **travel time** from dam to town, which is likely under a day and so not resolved by daily data.
- **Design standards:** the dam's design flood (for example the probable maximum flood (PMF) or standard project flood (SPF) per Indian Central Water Commission (CWC) or Bureau of Indian Standards (BIS) practice), the town protection standard, the MWL, freeboard and the top-of-dam level.
- **Sub-daily flood hydrographs** (hourly or 3-hourly) for the largest historical events, or at least peak-to-daily-mean ratios. These are needed to turn daily flood volumes into realistic peaks for routing.

**Important for the benefit side:**

- Irrigation demands by month (command area, cropping pattern), environmental and other releases, and evaporation.
- Hydropower plant data: installed capacity, turbine discharge range, head–efficiency, tailwater curve, and any firm-power requirement.
- Historical reservoir levels and releases (to calibrate and check the simulation against actual operation).

**Helpful:**

- Basin rainfall (to build a longer flood record, to understand storm types, and to estimate flow from the catchment between the dam and the town).
- Monsoon onset and withdrawal dates from the India Meteorological Department (IMD) (to test whether transition dates should be fixed or tied to onset).
- Climate projections (for stress tests).

If the critical downstream data cannot be obtained, the study must say so and narrow its claim (Section 7).

---

## 3. Methods

### Step 1. Data checks and baseline

- Check inflows for quality, gaps, homogeneity and trends (Mann–Kendall and Pettitt tests on annual and seasonal maximum flows and volumes). Check for upstream regulation that changed flows over time. If there is a clear trend or change point, use only the stationary part of the record or use non-stationary methods.
- Write down the current rule exactly as a simulation model: FLWL, gate operation, release limits and how refill is handled.
- Check the model by simulating historical operation and comparing with observed levels and releases, if those can be obtained.

### Step 2. Dividing the flood season into stages

- Use several methods and check that they agree:
  - the timing of annual and peak-over-threshold maxima (circular statistics on flood dates; empirical distribution of flood occurrences by date);
  - statistical partitioning of the daily flow series by period (for example Fisher optimal partition, change-point analysis);
  - fractal or cluster-based approaches if useful;
  - physical reasoning about the monsoon regime (onset, active and break spells, withdrawal, post-monsoon depressions).
- Keep it to 2–3 stages. More stages make the rule hard to operate and the sample for each stage too small.
- **Test how stable the boundaries are:** split the record into sub-periods (for example the first 22 and last 23 years) and check whether the boundaries shift. Also check year-to-year variation in onset and withdrawal. If the onset varies too much, consider a rule where the transition depends on an observed condition (for example the monsoon onset declared by IMD, or a basin rainfall trigger), rather than on a calendar date.
- Leave a buffer around each transition: move from a higher to a lower FLWL early, and from a lower to a higher FLWL late.

### Step 3. Seasonal design floods

- For each stage, take the largest flow peak (or daily flow) and the largest 1-, 3-, 5- and 7-day flood volumes in each year. Fit distributions (GEV, LP3, Pearson III, following Indian practice). Compare with peak-over-threshold methods because stage samples can be small. Report confidence intervals (for example by bootstrap).
- **Combine the risks consistently.** If the stages are treated as independent, the annual non-exceedance probability equals the product of the stage non-exceedance probabilities. The stage design frequencies must be set so that the combined risk is no greater than the annual standard.
  - The conservative default is to keep the **annual** design return period for each stage, which gives a combined risk slightly above the annual target; make this choice explicit.
  - Alternatively, give each stage a share of the annual risk so the total matches the target.
  - Report both, because this choice directly controls how much the FLWL can be raised.
- Make sure the seasonal design flood in each stage never falls below the largest flood actually observed in that stage, adjusted for transition buffers.
- **Design hydrographs.** Build them for each stage by scaling typical observed flood hydrographs to the design peak and volumes (scaling by the same factor, or separately for peak and volume). Use several typical hydrographs, because hydrograph shape strongly affects the routed peak level. Use sub-daily shapes if they can be obtained.
- **Dam safety check.** Keep the current PMF/SPF check for dam safety. Be cautious about applying a seasonal PMF: unless there is a well-supported seasonal estimate of probable maximum precipitation (PMP), check every stage's FLWL against the full PMF, or at least against the largest storm physically possible in that period.

### Step 4. Finding the seasonal FLWL by routing the design flood

- For each stage and each candidate FLWL, route the stage design hydrographs through the reservoir using the existing release rules. These rules include limiting release to the downstream safe discharge, after allowing for flow from the catchment between the dam and the town, until a set trigger level is reached, and opening further only above it.
- The highest acceptable FLWL for a stage is the highest level from which:
  1. the routed peak level stays at or below the design flood level / MWL with the required freeboard;
  2. the release, combined with the flow from the catchment between the dam and the town at the town, stays within safe discharge for the town's design flood; and
  3. the dam passes the PMF check.
- Allow for operational realities: gate opening rate, decision delays (6–24 hours), gate failure (for example one gate stuck, if the regulator requires that check), and limits on how fast the reservoir level may fall.
- The staged schedule cannot be less safe than the current rule in the core monsoon. So the core-season FLWL should come out at or below the current FLWL, unless the current value is shown to be conservative.

### Step 5. Long-term simulation of candidate rules

- **Candidates:**
  - the current fixed FLWL (baseline);
  - several staged schedules (the routing-derived maximum and more conservative versions);
  - optionally, a staged schedule with forecast-based pre-release.
- **Historical simulation over the 45 years:** a daily water balance with irrigation and hydropower releases, evaporation and spill. This gives benefit metrics and historical flood performance.
- **Stochastic simulation:** generate long synthetic inflow series (for example 1,000–10,000 years). Use a seasonal or periodic model that keeps the day-to-day persistence and the size of extremes (for example a periodic autoregressive model with extremes handled separately, or block bootstrap with perturbation). Also run event-based Monte Carlo of flood hydrographs. These are needed because 45 years cannot resolve the probability of 1-in-100-year or rarer events.
- **Optional:** an optimization (for example multi-objective evolutionary search over stage boundaries and stage FLWLs) to map the trade-off between flood risk and benefit. The goal is to show where the candidate schedules sit on that frontier, not to take an optimized rule straight into a recommendation.

### Step 6. Forecast analysis (secondary)

- Measure forecast skill by lead time and flow size. Look at bias, relative error, hits, misses and false alarms for flows above thresholds, and above all **under-forecasting of large events**. Fit an error model (for example the relative error distribution by lead time).
- **Pre-release feasibility test.** If a stage's FLWL is raised by ΔH, the extra storage ΔV must be releasable within the reliable forecast lead time without the release exceeding downstream safe discharge. Roughly, ΔV ≤ (Q_safe − Q_intermediate − Q_inflow during drawdown) × usable lead time. This gives a forecast-based upper limit on ΔH that does not rely on the seasonal design flood.
- Test against forecast error: simulate the cases where the forecast under-predicts at the 90–99th percentile of error. With 8 years of data, say plainly that the tail of the error distribution is poorly known. Do not use forecast-based raising as the main safety argument unless the error tail is well supported.

---

## 4. Assessing the effect on flood safety

Compare each candidate against the **current rule**, using the same inputs, model and standards.

**Metrics:**

- Peak reservoir level for each stage's design flood and for the annual design flood; margin to MWL and to the top of the dam; PMF check.
- Annual and seasonal probability that the reservoir exceeds the FLWL, the design flood level and the MWL (from stochastic simulation).
- Probability and duration of the town flow exceeding safe discharge (release plus flow from the catchment between the dam and the town, lagged by travel time). Also the expected number of days per year above safe discharge.
- Highest flow at the town for the largest historical events (replay each event starting from the raised FLWL as well as from the observed initial level).
- Event-based risk: the worst plausible starting condition. For example, a stage's design flood arrives just after the switch to a higher FLWL, or two floods arrive back to back without time to empty the flood space.

**Safety criterion (the key condition for a recommendation):**

- No increase in flood risk to the dam or town that would be meaningful in practice or exceed what regulators accept, beyond the stated tolerance, after allowing for uncertainty.
- "Equal risk" must be checked on the combined annual risk across stages, not only stage by stage.

**Stress tests:**

- Transition dates shifted by ±1–3 weeks.
- Design floods taken at the upper confidence bound.
- Different hydrograph shapes.
- Sedimentation-reduced capacity.
- Climate-driven increases in extremes (for example +10–20% on peaks).
- Gate failures and decision delays.
- Two floods in a row.

---

## 5. Assessing the effect on other objectives

**Metrics:**

- **Refill:** probability of reaching FRL (or a target storage) by the end of the monsoon; average and 10th-percentile end-of-season storage.
- **Irrigation:** reliability (time-based and volume-based), resilience, vulnerability (deficit size) and how often deficits occur in critical crop stages.
- **Hydropower:** average annual energy, firm or dependable energy (for example 90% dependable), energy in the dry season, and the effect of head.
- **Water lost:** spill volume, especially non-flood spill.
- **Trade-offs:** irrigation against hydropower releases under the higher storage; any effect on environmental flows.

**Reporting:** show the distribution of benefits over historical and synthetic years, not only means. Show how the benefit depends on the hydrological year (dry, normal, wet). The benefit should be biggest in dry or late-failing monsoon years, so check that it is.

---

## 6. Uncertainty and robustness

- Sources of uncertainty:
  - the parameters of the flood frequency fit (bootstrap);
  - the stage boundaries;
  - the shape of the design hydrograph;
  - the conversion from daily to peak flow;
  - flow from the catchment between the dam and the town;
  - forecast error;
  - capacity curve changes from sedimentation;
  - non-stationarity.
- Combine them in Monte Carlo runs where possible. Otherwise run a structured sensitivity analysis.
- Report robustness: whether the recommended schedule stays safe and beneficial across all plausible scenarios, or only some. A recommendation should favor schedules that are "safe in all, beneficial in most" over schedules optimal for the central estimate.

---

## 7. What results would be sufficient to recommend a change

A recommendation to change the current rule needs **all** of the following.

1. **Clear and stable sub-seasons.** The stage boundaries are statistically supported, agree across methods and sub-periods, and are physically sensible. Shoulder-stage design floods are materially smaller than the core-stage design flood, beyond the overlap of confidence intervals.
2. **Flood safety no worse than the current rule.**
   - For every stage, routing the stage design flood (at the agreed standard, with the combined risk accounted for) from the proposed FLWL keeps:
     - the peak level within the design flood level and MWL with freeboard;
     - town flows within safe discharge for the town standard;
     - the dam safe under the PMF check.
   - The stochastic simulation shows no meaningful increase in the probability of exceeding these thresholds compared with the current rule.
   - These results hold under the stress tests, at least for transition timing, upper-bound design floods and hydrograph shape.
3. **Benefit that is material and robust.** There is a clear improvement in end-of-season storage, irrigation reliability and/or dependable energy. It is large enough to matter operationally (to be set with the operators), and it holds across the historical and synthetic simulations and the sensitivity cases.
4. **A rule that can be operated.**
   - Clear transition dates or triggers, with buffers.
   - Drawdown rules for the move from a higher FLWL to a lower one.
   - It is physically possible to return to a lower FLWL within the available lead time without exceeding safe downstream discharge.
   - It is consistent with CWC/BIS reservoir-operation guidance and the dam's safety documents.
5. **Data sufficiency for the claim made.** The town-safety claim rests on actual downstream data: safe discharge, flow from the catchment between the dam and the town, and travel time.

**Graded claim levels, depending on data obtained:**

- **Level A (all critical data obtained):** recommend a specific staged schedule for adoption, subject to review by the dam owner and regulator, and possibly a trial period of monitored operation.
- **Level B (reservoir and design-standard data obtained, downstream data missing):** the conclusion is limited to "staging is safe for the dam and beneficial; town safety still needs to be checked". Do not recommend adoption.
- **Level C (only the currently listed data):** the study can show the seasonal flood structure and the possible benefit, and give conditional FLWL ranges. It is a feasibility or screening study, not a basis for changing the rule.

**Results that would argue against a change:**

- No clear seasonal drop in flood size.
- Large floods can occur in the shoulder periods.
- Stage boundaries are unstable.
- The benefit disappears under realistic irrigation and hydropower demands (for example the reservoir already refills in most years).
- Safety depends on forecast accuracy that the 8-year archive cannot support.

In those cases the recommendation should be to keep the current rule. An alternative would be a more limited change, for example only a late-season refill rule.

---

## 8. Main assumptions

- Monsoon floods in this basin are seasonal, with smaller floods at the start and end of the season. This is to be tested, not assumed.
- The current fixed FLWL was set from an annual design flood and design standard that can be found.
- The downstream town's protection depends on keeping release plus flow from the catchment between the dam and the town below a safe discharge.
- The study is advisory. Any rule change needs approval by the dam owner and the regulator.
