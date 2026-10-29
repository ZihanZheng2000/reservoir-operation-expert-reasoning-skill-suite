# V01 – Forecast-based dynamic control of the flood-season water level at Three Gorges

## 1. What the question really asks and how I frame it

The question has three parts:

1. **Rule design:** how to turn 1–7-day inflow forecasts into a daily rule for the flood-season water level that lets the level rise above 145 m.
2. **Safe upper level:** how high the level can be held without losing flood safety. The answer is probably a level that depends on the season and on the forecast, not one number.
3. **Evaluation:** whether the proposed rule is safe enough compared with current practice (145 m, rising to 148 m with a supporting 3-day forecast), and how much hydropower it adds.

The core logic is the standard one for dynamic control of the flood limited water level (FLWL). **Storage above 145 m is acceptable only if it can be released before the flood that needs that storage arrives.** It must be released without breaking the downstream safe discharge or the drawdown-rate limits, and it must allow for forecast error. So the safe height is set by four things: (a) how far ahead high inflows can be forecast reliably, (b) how much spare release capacity exists below the downstream safe flow during that lead time, (c) how large forecast errors are, especially underestimates of rising limbs and peaks, and (d) the volume–level relation above 145 m.

"Safe enough compared with current practice" needs an explicit test, decided before any simulation. I would use an **equal-or-lower-risk test**: for the same floods, the proposed rule must not produce higher peak reservoir levels, more frequent breaches of the flood-control limits, or higher downstream flows than (i) the design rule (strictly 145 m) and (ii) current practice (148 m with a 3-day forecast). Any risk increase that remains is reported as a number, not hidden. Setting the acceptable risk level is a decision for the operating and flood-control authorities. The study supplies a risk–benefit frontier for that decision.

## 2. Assumptions (stated, not invented facts)

- **Data:** the 2019 data are daily inflow forecasts at lead times of 1–7 days, issued daily for the flood season, plus the matching observed inflows. Which forecast system produced them, and whether it changed during the season, must be recorded.
- **Additional data, which must be obtained or the study cannot be done:**
  - level–storage curve;
  - discharge-capacity curves for the outlets and spillway;
  - tailwater rating;
  - turbine and unit characteristics (maximum turbine flow and output as a function of head);
  - the official flood-control rules: downstream compensation targets such as the Zhicheng/Shashi and Chenglingji control flows, the flood-control levels for 100-year and 1000-year floods, and the flood-season dates and sub-periods;
  - limits on the rate of level drawdown and on changes in outflow;
  - 2019 observed operation (levels, outflows, generation, spill);
  - design-flood hydrographs (typical historical flood shapes scaled to design frequencies) and, if possible, long historical inflow series.
- I do **not** assume specific values for the downstream safe discharge, the design flood-control levels, or turbine capacity. Figures I quote later are rough checks to be replaced by official values.
- **One season is very little evidence.** 2019 gives one sample of forecast-error behaviour and one hydrological year. Early in the study I would check how 2019 ranks in flood magnitude. If it was a moderate year, benefits measured on it may not hold in wet years, and the risk measured on it will understate the risk in large-flood years. The study must therefore test safety beyond the 2019 data (Section 5).

## 3. Step 1 – Characterize the forecasts (this determines everything else)

Using the 2019 forecast–observation pairs:

- **Error statistics by lead time (1–7 days):**
  - relative error, bias, root-mean-square error and Nash–Sutcliffe efficiency;
  - peak-timing and peak-magnitude errors for each flood event;
  - stratified by flow magnitude, because errors grow with flow and the high-flow tail matters most.
- **Error structure:**
  - whether errors scale with flow (heteroscedasticity);
  - autocorrelation across days;
  - correlation across lead times within one forecast issue;
  - asymmetry. Underestimation on rising limbs is the dangerous direction.
- **Effective lead time:** the longest lead time at which forecasts of high flows are still good enough to act on. I would define "good enough" before looking at results, for example: the upper quantile (say 90–95%) of underestimation at that lead time stays within the margin the rule can absorb. Days 1–3 are probably usable and days 4–7 probably only for early warning, but the data should decide this.
- **Error model** to generate many plausible forecasts for floods that were never forecast:
  - multiplicative, lead-time-dependent errors with autocorrelation and correlation across lead times, fitted to 2019;
  - bounds inflated to reflect uncertainty from a single season, for example by bootstrapping 2019 flood events and stress-testing with errors 1.5–2 times larger.

## 4. Step 2 – Design candidate operating rules

All candidates run on a daily step and are compared on identical inputs.

| Code | Rule | Purpose |
|---|---|---|
| R0 | Design rule: hold 145 m in the flood season | Safety reference |
| R1 | Current practice: 145 m, up to 148 m when the 3-day forecast supports it | Main comparison |
| R2 | Static raised FLWL: a fixed level of 146, 147, 148, 150, 152 … m | Shows what forecasts add over simply raising the level |
| R3 | **Proposed forecast-based dynamic rule** (detail below) | Main proposal |
| R4 | Rolling-horizon optimization (model predictive control) using the forecasts, with flood-safety constraints | Checks whether a smarter rule is worth its complexity |
| R5 | Rule R3 or R4 given perfect forecasts | Upper bound on the value of forecasts |

**How the proposed rule R3 works.** Each day *t*, the allowed upper level is set by **pre-release capacity**. The extra storage above 145 m that can be held is the volume that can be released over the effective lead time *L* without exceeding the downstream safe outflow, after a margin for forecast error:

`ΔV_allow(t) = min over k = 1..L of Σ_{j=1..k} [ Q_safe,j − Q̂_{t+j}·(1+e_q) ] · Δt` (capped by outlet capacity and ramp limits)

`Z_upper(t) = Z(V_145 + max(0, ΔV_allow)) `, limited by a hard ceiling `Z_cap(period)`.

- *Q_safe* is the release allowed by the downstream compensation rules. It accounts for intervening tributary inflow, such as from the Qingjiang, and for midstream stage targets.
- *Q̂* is the forecast inflow.
- *e_q* is a chosen quantile of the forecast underestimation error at each lead time. This sets the safety margin explicitly.

**Additional elements of R3:**

- **Drawdown trigger:** when the forecast peak or forecast volume exceeds a threshold, the rule switches to pre-release. It draws down toward 145 m at the maximum allowed rate, within the outflow ramp limits and the bank-stability limit on the rate of level fall.
- **Ceiling by sub-period:** the ceiling `Z_cap` is set separately for the pre-flood, main-flood and late-flood periods, because flood risk differs between them.
- **Operating within the allowed level:** the level is kept at the highest point consistent with turbine flow and the rule, so the plant uses extra head and stores water that would otherwise be spilled.

**Free parameters searched in the study:**

- effective lead time *L* (1, 2, 3, 5, 7 days);
- error quantile *e_q* (for example 50/80/90/95/99%);
- ceiling *Z_cap* (for example 146–155 m);
- drawdown trigger threshold.

**A rough feasibility check, to be redone with the official curves.** Storage between 145 and 175 m is on the order of 22 billion m³, so 1 m near 145 m holds very roughly 0.5–0.7 billion m³. Holding 5 m extra (about 3 billion m³) and releasing it within 3 days needs roughly 10,000–12,000 m³/s of spare release above inflow throughout those days. This is why the safe level is probably only a few metres in the main flood season. It is limited mainly by spare downstream capacity, not by total storage. It is also why the safe level should vary with the forecast: during low inflow there is large spare capacity, and when a big flood is forecast there is none.

## 5. Step 3 – Safety assessment (how high is safe, and is it as safe as current practice)

Performance on the 2019 season alone cannot show safety. I would use three tests, from realistic to extreme.

**Test A – 2019 hindcast with the real forecasts.**
- Run all rules R0–R5 through the 2019 season.
- Confirm that R3 drew down in time before each 2019 flood peak.
- Report the maximum level reached, peak outflow, and any day a downstream or ramp-rate limit was breached.
- This is necessary but weak evidence.

**Test B – Design floods with simulated forecast errors (Monte Carlo).**
- **Inputs:** design-flood hydrographs at standard frequencies (for example 5%, 2%, 1%, 0.1%) from several typical historical flood shapes, chosen to cover different peak timing and multi-peak sequences. Include a 1998-type flood with several peaks and an upper-Yangtze-dominated flood.
- **Starting conditions:** start each flood with the reservoir at the level R3 would hold at that time, up to `Z_cap`. This is the "flood arrives while the level is raised" case.
- **Forecasts:** generate thousands of forecast traces for each flood from the error model.
- **Rules simulated:** R0, R1 and R3/R4 with the official flood-routing rules: downstream compensation, then flood-control operation.
- **Metrics:**
  - distribution of maximum reservoir level and of maximum downstream flow at the control points;
  - probability of exceeding the design flood-control level for each frequency (for example the 100-year compensation level and the 1000-year level of 175 m);
  - probability that the reservoir is not back near 145 m when the flood rises;
  - number and size of breaches of the compensation targets.
- **Safety test:** for each frequency and each flood shape, R3's exceedance probabilities and peak values must not be statistically worse than R0, and at worst equal to R1, within a tolerance agreed in advance. The **safe ceiling** is the highest `Z_cap` (with matching *L* and *e_q*) that passes **every** flood shape and frequency. Because it is set by the worst case, the result is conservative.

**Test C – Stress tests.**
- forecast error enlarged 1.5–2 times;
- the forecast misses the peak entirely, or the peak arrives a day early;
- back-to-back floods with no time to recover;
- reduced outlet availability;
- upstream cascade reservoirs not coordinating;
- downstream conditions that cut spare release, such as high Dongting Lake or Chenglingji stage.

The report states where the rule fails, not only whether it passes.

**Risk-based summary.** For each candidate ceiling, report the change in flood-control risk relative to R0 and R1 (the change in each exceedance probability) together with the hydropower gain. This produces the **risk–benefit frontier**, which answers "how much higher is safe" for any risk tolerance the authorities choose.

**Secondary constraints**, checked and reported even though they are not the main focus:
- upstream backwater levels, such as at Chongqing, during high inflow with a raised starting level;
- extra sediment deposition in the fluctuating backwater zone, since the flood season carries most of the sediment load. A sediment-transport model or published sediment relations are needed; the 2019 data cannot answer this;
- navigation and the counter-regulation of the downstream Gezhouba reservoir.

If any of these sets a lower limit than flood safety, it becomes the binding ceiling.

## 6. Step 4 – Hydropower benefit

- **Plant model:**
  - simulate generation daily from head (reservoir level minus tailwater), turbine flow and efficiency;
  - apply the unit and plant output limits, which depend on head;
  - account for unit outages if records exist.
- **Calibration:** check the model against actual 2019 generation and spill.
- **Comparison:** compare rules within the model rather than against the actual records, so model error largely cancels out. Also report the gain over actual 2019 operation.
- **Metrics, for the flood season and through the refill period:**
  - generation (GWh);
  - spill volume;
  - spill avoided while the plant had spare turbine capacity;
  - mean head;
  - water consumption per kWh;
  - whether the reservoir reaches the normal pool level by the end of refill.
- **Separating the two sources of gain:**
  - (a) **Head effect:** the same water generates more energy at a higher level.
  - (b) **Spill-recovery effect:** water stored during moderate flows and flood recessions would otherwise have been spilled.

  Spill that happens when inflow exceeds full turbine flow cannot be avoided by a slightly higher level. So spill reduction will be much smaller than total spill, and the report must say so rather than counting all spilled water as recoverable.
- **Robustness:** report the gain for 2019 and, if longer inflow series are available, for wet, normal and dry years run with simulated forecasts. One year alone cannot give a general benefit figure.

## 7. Outputs that answer the question

1. **Forecast skill table:** skill by lead time, including the high-flow tail, and the chosen effective lead time.
2. **The rule:** the dynamic-FLWL rule R3 written as an operational procedure (formula, triggers and ceilings by sub-period) that an operator can apply each day.
3. **Safe ceiling:** the safe ceiling for each sub-period, with the binding constraint and the flood case that sets it.
4. **Risk comparison:** R3 compared with R0 and R1 for each design flood and stress test, showing the risk–benefit frontier.
5. **Hydropower gain:** the gain for 2019 and, if possible, for multiple years, split into head effect and spill-recovery effect, against both the R1 simulation and actual 2019 operation.
6. **Value of forecasts:** the gaps R2 to R3 (what forecasts add over a static raised level) and R3 to R5 (room left for better forecasts).

## 8. Provisional judgment

- **Rule:** forecast-based dynamic control should be able to hold the level above 145 m on most flood-season days. It would rise during low-to-moderate inflow periods, when spare release capacity is large. When the 2–3-day forecast shows a significant flood, it would draw down to 145 m.
- **Safe height:** I provisionally expect the safe ceiling in the main flood season to be modest, perhaps about 146–150 m. That is around or slightly above the current 148 m, but held on more days and with a rule-based drawdown. Higher ceilings may be acceptable in the pre-flood and late-flood periods. This expectation rests on the rough pre-release calculation and on effective lead times of about 3 days. It is a hypothesis to test, not a result.
- **Safety:** the proposed rule is likely to come out as safe as current practice only if the error margin *e_q* is set at a high quantile and the drawdown trigger is conservative. Without these, the main risk is a large forecast underestimate on a rising limb, which leaves too little time to draw down.
- **Hydropower:** I expect a positive but moderate gain in flood-season generation, mostly from extra head plus some recovered spill from flood recessions. Large-flood spill will remain.

**What would raise the ceiling or the benefit:**
- forecasts that stay skilful for high flows at 4–5 days;
- large spare downstream capacity on most days;
- 2019 turning out to be a typical rather than an easy year.

**What would lower it:**
- systematic underestimation of peaks;
- short effective lead time;
- binding downstream stage or compensation limits;
- sediment or backwater constraints that bind before flood safety does;
- Monte Carlo failures in multi-peak floods.

**Main limitation.** Evidence on forecast errors comes from one season. Any recommended ceiling should be treated as provisional until it is checked against forecasts from more years, or tried in a supervised trial operation with the drawdown trigger kept conservative.
