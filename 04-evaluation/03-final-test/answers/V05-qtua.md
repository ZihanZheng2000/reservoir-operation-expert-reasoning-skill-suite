# Stânca–Costești: re-establishing design floods and an outlet-by-outlet flood operating rule

## 1. Provisional answer and study logic

**Provisional judgment.** The 2008 flood shows that the original design basis is outdated. The reservoir should be re-planned for a design flood and a check (safety-evaluation) flood that are each defined by **both a peak and a multi-day volume**, and taken from a re-estimated frequency analysis that includes 2008. The analysis must carry the rating-curve error and the short record, and the adopted values should sit at the upper side of the uncertainty band. Until the study is done, I would treat a 2008-type event (about 1100 mil. m³, peak about 1.15 × the original design peak) as **no rarer than the new design flood, not as the check flood**. One event in 43 years exceeded the design peak. That is weak evidence on its own, but it is the only direct evidence and it points one way.

For operation, the volume arithmetic matters most. A 2008-type flood carries about 435 mil. m³ more than the flood-control volume can hold, so the reservoir cannot "absorb" such a flood. The operating rule therefore has to do three things:

1. use the 3-day warning to make sure the full 665 mil. m³ is empty and, where it can be done safely, to pre-release a little more;
2. shape releases during the rise so that downstream flows stay at or below the safe channel capacity for as long as storage allows, and never exceed the natural (inflow) peak;
3. switch, at a pre-set level, to a dam-safety mode that gives the weir bays and bottom outlets priority. In this mode the outlets are opened in a fixed, hydraulically safe sequence, with an assumption that one gate is out of service, so that the level never again goes above the flap gates.

The study below is designed to put numbers on those three elements, check them, and get them approved by both states.

**The deciding questions** (answered in the most depth below):

1. **How large are the design and check floods now, in peak and volume, once the rating-curve error and the short record are included?** This decides everything downstream. Today it rests on one gauge whose high-flow rating is uncertain.
2. **At the new check flood, can the outlets pass enough water to keep the level below the dam-safety limit, with one gate unavailable and the reservoir starting from a realistic level?** If not, operation alone cannot fix it, and the answer becomes a structural or capacity question (more spillway capacity, a lower flood-limited level, or more freeboard).
3. **What does the 3-day warning actually buy?** That means how much extra space can be released in time without causing a man-made flood downstream, and how reliable the warning is at 1, 2 and 3 days.

---

## 2. Order-of-magnitude arithmetic that frames the study

All numbers that the brief does not give are marked as assumptions.

**Volume deficit of a 2008-type flood.**
- Flood volume minus flood-control volume = 1100 − 665 = **435 mil. m³**. This must leave through the outlets during the event even if the flood pool is empty at the start.
- Average outflow needed just to pass that excess volume (on top of whatever passes while storage fills):
  - over a 7-day event: 435 × 10⁶ / (7 × 86,400) ≈ **720 m³/s**
  - over a 14-day event: ≈ **360 m³/s**

  So downstream flows well above any low "non-damaging" release are unavoidable in a 2008-type flood. The operating question is how high and for how long, not whether.
- If the reservoir starts the event with part of the flood pool already filled, every 10% of the 665 mil. m³ that is occupied (66.5 mil. m³) adds the same amount to what must be released. This is why the initial level is a deciding uncertainty, and why the study must find out the actual starting level in 2008.

**What 3 days of pre-release can buy.**
- 3 days = 259,200 s. Each **100 m³/s of net release** (release minus inflow) held for 3 days frees **≈ 26 mil. m³**, which is about 4% of the flood-control volume or about 6% of the 2008 excess.
- To gain 100 mil. m³ of extra space in 3 days needs a net release of ≈ 390 m³/s above inflow for the full 72 hours. In practice the inflow is already rising during the warning period, so the achievable gain is smaller.
- **Conclusion:** pre-release below the normal flood-limited level is a marginal tool for an event the size of 2008. The 3-day warning is mainly valuable for three things:
  1. making sure the flood pool is fully empty;
  2. staging the gate sequence and warning people downstream;
  3. keeping releases low early on, so that storage is saved for the peak.

  Any pre-release must also be (a) capped below the downstream safe flow, (b) no larger than the natural flow would have been, and (c) refillable if the flood does not come. The refill check matters because the reservoir also serves water supply, irrigation and hydropower.

**How much the record can resolve.**
- 1978–2020 gives about 43 annual maxima, so about **43 independent annual extremes**. That is fewer if the record has gaps or the first year is partial.
- Plotting 2008 as the largest of 43 gives an empirical return period of about 44 years, with a very wide plausible range. One exceedance in 43 years is consistent with return periods from roughly 10 to several hundred years.
- Fitted 1% (100-year) peak quantiles from about 40 years of data typically have sampling standard errors of order ±15–30%. For 0.1% quantiles the errors are wider. The record cannot by itself tell a 1% design flood from a 0.5% one, and it cannot detect a trend of plausible size with useful power.
- Hence the study must add information beyond the gauge: regional data, historical floods, and a water-balance reconstruction of inflows to the reservoir.

**Risk over a planning horizon** (independent years, 1 − (1 − p)ⁿ):
- a 1% annual flood over 50 years: 1 − 0.99⁵⁰ ≈ **39%**
- 0.1% over 50 years: ≈ **4.9%**
- 0.01% over 50 years: ≈ **0.5%**

These figures show stakeholders why the check flood, not the design flood, governs dam safety over the remaining life of the dam.

**Effect of the rating curve.**
- If the high-flow rating overestimates flows by x%, then the fitted peak quantiles are biased up by about x%. Volume quantiles are biased by less, because only the high-flow part of the hydrograph is affected.
- If the rating underestimates flows, the bias runs the other way. In that case the 2008 peak "15% above design" could be even larger than reported.
- The direction of the bias is unknown until the rating is checked. That is why the rating check comes first.

---

## 3. Study design

### Part A. Re-establish the design floods

**A1. Fix the data before fitting anything.**
- **Re-analyse the upstream gauge's high-flow rating:**
  - collect all gaugings and the cross-section survey history;
  - fit a rating with explicit uncertainty, for example a hydraulically constrained Bayesian rating with a parametric uncertainty band;
  - extrapolate above the highest gauging using hydraulic control information, for example a 1-D hydraulic model of the gauged reach;
  - produce annual-maximum peaks and volumes as **distributions per year, not single values**.
- **Independently reconstruct reservoir inflow for large events (2008 especially) from the reservoir water balance:** inflow = outflow + ΔS/Δt.
  - Use observed levels, the storage–level curve, and the ratings of each outlet at the recorded gate openings and heads.
  - This check does not depend on the upstream rating. It does depend on the outlet ratings and the storage curve, whose uncertainty must also be stated, and sedimentation since 1979 may have changed the storage curve.
  - Comparing the two estimates calibrates the high-flow bias of the gauge.
- **Account for the intermediate catchment between the gauge and the dam.** Estimate local inflow from a rainfall–runoff model or from area scaling. Label it as an assumption until it is checked against the water-balance reconstruction.
- **Record the initial reservoir level and the operations actually carried out in 2008** (gate openings, timing). Without them the 2008 outcome cannot be used as a baseline, because it may have been forced by constraints or information the analysis would otherwise omit.

**A2. Extend the information base.**
- **Regional flood frequency analysis** using gauges in hydrologically similar upper-Prut, Siret and Dniester Carpathian catchments. This needs data sharing with Ukraine, where the upper Prut lies, and with Moldova.
- **Historical (pre-1978) flood information:** documentary marks, older station records, and pre-dam design data, used as censored or perception-threshold data in the fit.
- **Rainfall-based information:** the 2008 storm and other extreme storms. A rainfall–runoff model driven by maximized or transposed storms can test whether floods larger than 2008 are physically plausible. Its result serves as an upper-bound check, not as the design value.

**A3. Fit peaks and volumes jointly.**
- Fit annual maxima of the **peak and the 1-, 3-, 5-, 10- and 15-day volumes**. Storage is volume-critical: 665 mil. m³ against 1100 mil. m³. Release capacity is peak-critical.
- Fit the marginals by a method that takes the rating uncertainty, historical and regional data (for example a Bayesian GEV/LP3 with censored historical data). Fit peak–volume dependence with a copula, so that design events cover both "high peak, moderate volume" and "moderate peak, very large volume" (the 2008 type).
- **Nonstationarity:**
  - test for trend and change points;
  - report the low power of the tests given 43 years;
  - unless there is clear evidence, use a stationary fit and treat a nonstationary variant (for example a location parameter that changes over time) as a sensitivity case;
  - decide which to adopt on precaution, not on the test result alone.

**A4. Define the design events.**
- Set the design and check exceedance probabilities from the **governing dam-safety standards of both states** for the dam's importance class, and take the stricter one where they differ. I am not certain of the exact class-specific probabilities, so they must be confirmed with the Romanian and Moldovan dam-safety authorities. The study should not assume them.
- For each probability, produce a **set of design hydrographs**, not one:
  - several shapes scaled from observed events (2008 and other large floods) to the joint peak–volume quantiles;
  - a double-peak or closely spaced sequence (a second flood arriving before the pool is emptied);
  - a version with an early local peak from the intermediate catchment.
- Report each quantile as a **central value plus an upper credible bound**. Recommend that safety checks use the upper bound, for example the 90% upper limit, rather than the central estimate.
- **Planning value.** Adopt the upper-bound design and check hydrographs. As a floor, require that the check flood is not smaller than the 2008 volume and peak scaled by the ratio of the check to the 2008 quantile. This keeps the observed event from being underweighted by the fit.

### Part B. Describe the physical system and its limits

**B1. Outlet-by-outlet capacity.** For each bottom outlet and each gated weir bay (and the turbines, if they can be counted in flood conditions), assemble:
- discharge as a function of reservoir level and gate opening, from model tests, commissioning data, or 2008 back-analysis;
- the maximum and minimum safe gate openings (vibration and cavitation limits of the bottom outlets at high head);
- rate-of-opening limits;
- energy-dissipator capacity and the permitted combinations (symmetric bay operation to avoid one-sided flow and scour in the stilling basin);
- the head at which flap gates are overtopped and what that means structurally. In 2008 the level rose above the flap gates, which is a demonstrated loss of control margin.

**B2. Characteristic levels and safety thresholds:**
- the flood-limited level;
- the normal maximum level;
- the level of the flap-gate tops;
- the maximum permissible flood level and the crest, with freeboard for wind set-up and waves;
- the maximum drawdown rate for the upstream slope and the reservoir banks.

**B3. Downstream.**
- Identify control points on both banks of the Prut downstream of the dam (settlements, levee reaches, bridges). Set the **non-damaging flow** and the **levee-safe flow** at each.
- Estimate travel times from the dam to each control point and the contribution of downstream tributaries, using a 1-D hydraulic model of the reach between the dam and the main control points.
- **Travel-time check:** a release made now arrives downstream later. If a downstream tributary peaks first, the dam can hold back. If it peaks later, releases already in the channel will coincide with it.
- Route cases where the tributary peak arrives before, with, and after the reservoir release, and check that the rule holds in each.

**B4. Operation as it is today.** Encode the current operating regulation, the one in force in 2008, in a simulator as the **baseline comparator**. Replay 2008 through it from the actual 2008 starting level to check the simulator against observed levels and outflows.

### Part C. Design the outlet operating rule

**C1. Settle the safety requirements before computing anything.**
- **Dam safety is a constraint that nothing can compensate for.** Under the check flood, with one gate (the largest single unit) out of service and the reservoir starting at the upper end of its realistic starting range, the maximum level must stay below the maximum permissible level with the required freeboard. A stricter internal target is also proposed: the level must stay below the flap-gate tops under the design flood.
- **Downstream objectives**, which apply only once dam safety is met:
  - the peak flow at each control point;
  - the duration and volume above the non-damaging and levee-safe flows;
  - the release must never exceed the concurrent natural inflow peak, so the reservoir does not create a man-made flood larger than nature's.
- **Other objectives:**
  - refill to the operating level after the event, for water supply, irrigation, hydropower and fish farming;
  - limits on the drawdown rate.
- **Risk measures:**
  - the probability that the maximum level exceeds each safety level, using the ensemble of design and stochastic floods plus forecast and initial-level uncertainty;
  - downstream exceedance probability and duration;
  - a tail measure (the expected level exceedance in the worst few per cent of runs), because one probability hides how bad the failures are.
- **Combining risks.** Dam-side and downstream risks are reported separately and are not added together. The dam-side risk must pass first.

**C2. Structure of the rule.** The rule is a staged, threshold-switched rule that works without a forecast and uses the forecast where it is reliable:

| Stage | Trigger (to be calibrated) | Action | Outlets |
|---|---|---|---|
| 0. Readiness (flood season) | Default | Keep the level at or below the flood-limited level. Any water above it is emptied promptly, below the downstream non-damaging flow. | Turbines and bottom outlets |
| 1. Warning (forecast lead up to about 3 days) | Forecast volume or peak above threshold V₁/Q₁; or upstream gauge rising above threshold | Confirm the pool is empty. Pre-release only if the forecast lower quantile still refills the volume released, release ≤ non-damaging flow, and release ≤ concurrent natural flow. Pre-position gates, check power and staff, notify downstream. | Bottom outlets first (they work at low head), then turbines |
| 2. Rising limb, downstream-protection mode | Inflow > non-damaging flow and level below threshold Z₂ | Release limited to the downstream target flow (non-damaging, then levee-safe), adjusted for tributary timing; store the rest. | Bottom outlets plus symmetric weir bays as head rises |
| 3. Dam-safety mode | Level ≥ Z₂, **or** forecast/observed inflow volume shows that holding the downstream target would exceed Z₃ | Release increases toward inflow (outflow ≤ inflow while rising), in fixed gate-opening increments and sequence. Downstream target is abandoned in favour of dam safety. Warning to evacuate is issued before the switch. | All weir bays in the prescribed sequence, bottom outlets within vibration limits |
| 4. Emergency | Level ≥ Z₃ (below flap-gate tops with margin), or gate failure | All available capacity fully open. Emergency plan activated. | Everything available |
| 5. Recession | Inflow past peak and falling for a set number of hours | Release ≥ inflow to empty the flood pool by a target date, ≤ levee-safe flow, within drawdown-rate limits; closing in reverse sequence. | Weir bays closed first, then bottom outlets |

**C3. How the thresholds and sequence are set.**
- The thresholds V₁, Q₁ and Z₂, the downstream targets in stage 2, the gate-increment schedule and the closing sequence are **parameters to calibrate**. They are found by simulation–optimization over a large set of events:
  - historical events reconstructed in Part A;
  - stochastic events from the fitted joint peak–volume model;
  - design and check hydrographs.
- The search keeps a **set of non-dominated rules** (maximum level against downstream exceedance against refill) rather than collapsing them into one score. Rules that fail the dam-safety constraint at the upper bound of their risk are dropped first.
- The gate-by-gate sequence comes from a constraint layer that sits under the rule. Given a target total release and the current level, it chooses openings by:
  - meeting the target;
  - keeping bay operation symmetric;
  - respecting the vibration and cavitation ranges of the bottom outlets;
  - respecting rate-of-change limits;
  - assuming one unit unavailable (N−1);
  - minimizing the number of gate movements, which matters for staff workload and is checked against real-time staffing.

**C4. Using the 3-day forecast.**
- **Verify skill first.** Verify the available forecast by lead time (1, 2 and 3 days), separately for peak and volume, against the water-balance inflow reconstruction. Use hindcasts from the same forecast setup that will be used operationally.
- **Build an error model** that varies with lead time and flow and keeps the correlation of errors across lead times. Treating them as independent understates the error in the 3-day volume:
  - for n equal errors σ with correlation ρ, the variance of the sum is nσ²(1 + (n − 1)ρ);
  - with n = 3 and ρ = 0.7 that is 7.2σ² instead of 3σ², so the standard deviation is about 1.5 times larger.
- **Decide on a conservative quantile** for pre-release (the forecast's lower quantile, so the released volume can be refilled) and for the dam-safety switch (the upper quantile, so the switch is not late).
- **Fallback.** If the forecast is missing, late, or diverges from the upstream gauge beyond a set tolerance, the rule reverts to the measurement-based triggers (level, observed inflow, upstream gauge), which must be safe on their own.
- **Abort rule.** If the flood arrives early while a pre-release is under way, stop the pre-release and move to stage 2 or 3 based on the measured state.
- **Point of no return** for each option: the latest time a pre-release can still produce useful space, and the latest time the dam-safety switch can be made without a release jump that exceeds ramping limits. The study computes both for each design event.
- **Value of the forecast.** Quantify it by comparing three information conditions:
  - no forecast (measurement-based rule);
  - the real forecast with its error model;
  - a perfect forecast.

  The real forecast's benefit lies between the other two. If it is small, the rule should rest on measurements, with the forecast used only for warning and staging.

**C5. Model choice.**
- A reservoir water-balance simulator with level-dependent outlet ratings at a 1-hour step, coupled to a downstream hydraulic routing model, used for calibration and testing.
- Model predictive control (rolling optimization over the forecast horizon, executing only the next step) as a **comparator and possible decision-support tool**, not as the primary rule. The primary rule must be executable with standard tools by the operating staff, and approvable as a written regulation.

### Part D. Test the result

- **Baseline comparisons under identical conditions.** Compare the proposed rule with the current regulation and with the comparators from C4 (no forecast, MPC, perfect foresight) on the same events and starting levels.
- **Historical replay** of 2008 and the other large events, with closed-loop simulation (the rule's own releases drive the level). Out-of-sample: calibrate on the stochastic set, test on the observed floods, and the reverse.
- **Stress tests:**
  - check and beyond-check floods;
  - double floods;
  - higher starting level;
  - one or two gates out of service;
  - a ±20–30% rating bias;
  - outlet discharge coefficients reduced at the actual head;
  - level-measurement error;
  - a forecast missing or 1 day late;
  - a nonstationary design flood.

  The decision should be robust across these, not optimal for one.
- **Monte Carlo resolution.** Use enough runs that the dam-side exceedance probability at the target level is resolved: to estimate p ≈ 10⁻³ with a ±30% standard error requires about 1/(0.09p) ≈ 11,000 runs.
- **Mass-balance plausibility.** Any claimed downstream peak reduction must be consistent with the storage actually available at the time of the peak.

### Part E. Adoption and approval

- **Approval in both states.** The dam is a joint Romanian–Moldovan structure on a boundary river. Any change to design floods or operating rules must be approved in both states and coordinated under the bilateral arrangement for the Prut (as far as I know there is an intergovernmental Romania–Moldova water cooperation agreement covering the Prut and a joint commission; the study should confirm the current instrument).
  - **Romania:** I would expect the water authority (Apele Române and its Prut–Bârlad basin administration), the hydropower operator, and the national dam-safety body to be involved.
  - **Moldova:** the corresponding water agency and dam operator.
  - **Ukraine:** a data and warning partner for the upstream catchment.
- **Interim measures until approval.** The current operating regulation stays the legal basis. Interim measures are recommended immediately on the basis of the volume arithmetic above:
  - stricter enforcement of the flood-limited level in the flood season;
  - a pre-agreed dam-safety switch level below the flap-gate tops;
  - N−1 gate readiness checks.
- **Trial.** Run the new rule in shadow mode alongside the current regulation for at least one flood season. Use acceptance criteria agreed in advance with the dam-safety authorities (maximum level under each design and check flood, downstream exceedance compared with the baseline).
- **Reversion and logging:**
  - set triggers for reverting to the current rule (forecast missing or diverging, gate failure, communication loss), and name who decides;
  - log all decisions and gate movements for audit and after-event review.
- **Warning.** Warning protocols for downstream communities on both banks and for emergency services, especially for man-made releases during stage 3. Train the operators and keep version control of the rule.

---

## 4. Key assumptions and what would change the recommendation

| Assumption | If wrong, effect |
|---|---|
| The upstream gauge's high-flow rating has a bias that the water-balance check can bound | If the bias cannot be bounded, the design flood must rest more on regional and historical data, and safety checks must use an even wider upper bound |
| Outlet capacity at maximum level is enough to pass the check flood with N−1 | If not, the answer is structural: more spillway or outlet capacity, a lower flood-limited level, or more freeboard. This dominates any operating improvement |
| The 2008 starting level was near the flood-limited level | If it was well above, part of the 2008 excess was an operating problem, not a hydrological one. This supports a stricter readiness rule more than a larger design flood |
| The 3-day forecast has useful skill at 2–3 days | If not, the rule is measurement-based. The forecast is used only for staging and warning, and pre-release is dropped |
| The downstream non-damaging and levee-safe flows are known on both banks | If they differ between banks or are uncertain, the stage-2 target is set by the more restrictive bank and agreed bilaterally |
| No strong trend is detectable in 43 years | If a trend is clear, the nonstationary fit becomes the design case, and the rule and design floods are reviewed at a set interval (for example 10 years) |

**What would confirm the provisional judgment:**
- the water-balance reconstruction confirms the 2008 volume and peak;
- the joint fit places 2008 near or above the adopted design quantile;
- simulation shows that the staged rule with N−1 keeps the level below the flap-gate tops for the design flood and below the maximum permissible level for the check flood.

**What would change it:**
- a large upward rating bias, which would make 2008 smaller than reported;
- evidence that 2008 was driven by a high starting level or delayed gate operation;
- or, in the other direction, outlet capacity proving insufficient at the check flood, which turns the study from an operating study into a dam-safety rehabilitation case.
