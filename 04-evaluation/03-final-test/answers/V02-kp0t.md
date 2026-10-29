# Real-Time Flood Release Decision Support for Daecheong: Plan and Provisional Recommendation

## 1. How I read the problem

There are four main features.

1. **The decision is a rolling hourly schedule.** Each hour operators issue a multi-hour release schedule and carry out only its first step, or the first few. This is model predictive control (MPC) in practice. The tool should copy that loop: re-optimise every hour over a short horizon, issue the schedule, carry out step 1, update the state from observations, and repeat.
2. **The reservoir has little room to absorb a flood.** The space between NHWL (76.5 m) and FWL (80.0 m) fills in about 6.5 h at the 200-year inflow. There is no restricted flood-season level, so an event can begin near NHWL. This gives very little time to correct mistakes. Release decisions in the first hours of a rising limb matter most. A tool that waits for certainty will be too late.
3. **Forecasts are short compared with events.** Rainfall forecasts cover 6 h, while events last 200–311 h and have several peaks. The optimiser can never see the whole event. So the terminal condition at the end of each short horizon, meaning what storage to aim for, carries much of the decision. That terminal condition must stand in for the water-supply objective after the event.
4. **The objectives are operators' unwritten preferences, and acceptance is the goal.** The sponsor wants schedules operators will accept. That makes this as much a preference-capture and validation problem as an optimisation problem. Stability of the schedule, persistence of gate states and turbine-first use are core requirements, not refinements.

**My provisional recommendation:** build a **rolling-horizon, multi-objective MPC** with these features:
- a **lexicographic (priority-ordered) or goal-programming objective** built from operator preferences;
- **explicit gate-state (binary) variables** with minimum-duration and switching penalties;
- **penalties on revisions** between consecutive issued schedules;
- a **storage-target terminal condition** that protects post-event supply;
- **forecast uncertainty handled by a small inflow ensemble** (scenario-based MPC), compared against a deterministic MPC with safety margins.

Demonstrate it in hindcast on the 2016, 2018 and 2020 events. Compare it with historical operation and with a perfect-foresight benchmark.

The reasons, assumptions and conditions that would change this are below.

## 2. Assumptions (stated, not given)

- **A1.** Yongdam's planned releases are known to Daecheong operators when they decide, as the brief says. For hindcasts I assume K-water can supply the historical hourly Yongdam releases. Then Daecheong inflow can be split into a known upstream part and an uncertain local part. If it cannot, I treat total inflow as uncertain, which is conservative.
- **A2.** Total release = turbine release (≤ 264 m³/s) + spillway release. Spillway capacity at each level comes from a rating relationship between level and maximum gated discharge. I assume K-water can supply that relationship. The brief gives only 11,680 m³/s total and more than 6,000 m³/s at NHWL.
- **A3.** The brief gives no downstream channel capacity or stage limit. So downstream protection appears only through peak outflow and smoothness. If K-water or downstream agencies have a safe-discharge threshold, it should become an explicit constraint.
- **A4.** Downstream demand (agreements with water users plus in-stream flow) is a known hourly or daily value. It is small compared with flood flows, so it binds mainly in recession and low-flow hours.
- **A5.** The post-event supply requirement can be expressed as a **target storage or level at event end**, for example near NHWL. The right value has to come from K-water's water-supply planning. I would not invent it.
- **A6.** Archived KMA 6-h rainfall forecasts for the three events may or may not be available. Archived *issued release schedules* may or may not be available either. Both strongly affect the design (see §5 and §7). I plan for both cases.
- **A7.** The hydropower objective is secondary to flood safety and supply. Turbines are preferred mainly because they avoid spillway use and earn revenue.

## 3. Data preparation (first work package)

1. **Rebuild and clean inflow.** Inflow is derived by water balance from hourly storage and outflow. Hourly storage changes from a level gauge with finite resolution produce noisy inflow series, sometimes with negative values and spurious spikes. Steps:
   - check the series for negative values and oscillations;
   - smooth it, for example with a centred moving average or a Kalman smoother, while preserving volume;
   - report how much this changes the peaks.

   This matters because "the inflow peak observed so far" is a constraint. A noise spike would loosen it falsely. In real time the tool can only use a causal (filtered) estimate, not a centred smoother. The hindcast must use the same causal estimate operators would have had.
2. **Split inflow.** Separate the Yongdam release (known) from local inflow (uncertain), if A1 holds.
3. **Check the level–storage curve.** Compare it with the records. The dam is more than 40 years old, so sedimentation may have changed the curve. If a recent survey exists, use it, and record which curve version was used.
4. **Describe the events.** For each event, record:
   - starting level relative to NHWL;
   - volume above turbine capacity;
   - timing and size of the peaks;
   - historical maximum level;
   - historical peak outflow divided by peak inflow;
   - spill hours;
   - number of gate changes;
   - end level.

   This gives the historical baseline and shows how hard each event is. For example, 2020 has a single large peak. 2016 and 2018 have several peaks, which test the dilemma of releasing for the current peak or keeping space for the next.

## 4. Formulation

### 4.1 Decision variables (per hour k in the horizon)

- Turbine release q_T(k) ∈ [0, 264].
- Spillway release q_S(k) ∈ [0, Q_S,max(h(k))].
- Gate state binary g(k) ∈ {0,1}, with q_S(k) ≤ g(k)·Q_S,max.
- Storage S(k), with level h(k) from the level–storage curve. Linearise piecewise if a mixed-integer linear program (MILP) is used.

### 4.2 Hard constraints

- Mass balance: S(k+1) = S(k) + [I(k) − q_T(k) − q_S(k)]·Δt.
- LWL ≤ h(k) ≤ FWL. In practice use FWL minus a safety margin as the operating ceiling (see §4.4).
- q_T + q_S ≥ downstream demand.
- Spillway capacity as a function of level.
- Non-anticipativity across scenarios when an ensemble is used: the first-step decision is the same in every scenario.

### 4.3 Objectives, in provisional priority order

Each comes from the brief:

1. **Dam safety:** keep the level below the operating ceiling. Treat this as hard, with a soft backup so the problem always has a solution.
2. **No amplification of the flood:** q_T + q_S ≤ the peak inflow observed so far, max_{τ≤t} Î(τ). This is a moving bound. In multi-peak events it starts low and rises when a larger peak arrives. Make it soft, with a heavy penalty, ranked below safety. If the reservoir is near the ceiling and inflow is still rising, releasing up to the current inflow is always allowed, so the bound only conflicts with safety in extreme cases. Report those cases rather than hide them.
3. **Limit spillway use:** penalise spill volume and peak spill. Turbine-first follows from this: any release up to 264 m³/s should go through the turbines. That can be enforced directly, q_S(k) > 0 ⇒ q_T(k) = 264, using one binary or a lexicographic stage.
4. **Supply after the event:** a terminal penalty on the gap between end-of-horizon storage and a target S*(t). See §4.5.
5. **Stability and gate persistence:**
   - penalty on |q(k) − q(k−1)| (ramping);
   - penalty on revisions, |q_t(k) − q_{t−1}(k)| for the hours the current schedule shares with the previous one;
   - penalty on gate switches |g(k) − g(k−1)|;
   - a minimum gate-open duration. Close the gates only when a "flood clearly ending" condition holds, for example inflow falling for N hours, the forecast below a threshold, and the level at or below target. That condition comes from operators.
6. **Hydropower:** a small reward for turbine energy. Head-dependent, but a linear approximation is enough.

**Why lexicographic or goal programming rather than one weighted sum:** operators reason in priorities ("never go near FWL; after that, don't spill more than needed; after that, keep it smooth"). Weights in one sum are hard to explain and behave oddly across events of different size. A lexicographic scheme solves stage by stage, allowing a small relaxation tolerance on each higher objective. Goal programming uses aspiration levels per objective. Both are easier to explain to operators and to tune with them. I would still test a well-tuned weighted MILP as an alternative. If its schedules are indistinguishable and it solves faster, simpler is better.

### 4.4 Safety margin below FWL

Storage fills in hours. So the operating ceiling should sit below FWL by a margin. The margin should cover:
- the volume one forecast error could add before the next decision;
- gate response time.

Set the margin from the forecast-error analysis in §5. Do not pick it ad hoc. Report how it trades against spill.

### 4.5 Terminal condition (the main link to the long event)

A 6–12 h horizon cannot see the end of a 300-h event. Without a terminal condition, the optimiser will either drain storage, which hurts supply, or hold it, which hurts safety. Options, in increasing complexity:

- **(a) Fixed target.** S* = storage at NHWL, or K-water's end-of-event target.
- **(b) State-dependent target.** S* is lowered while the forecast shows rain still to come (pre-release, to make room for the next peak) and raised toward the supply target during recession. The rule comes from operator interviews and is tuned on events.
- **(c) Value function.** A value-of-storage function from a long-horizon or stochastic dynamic programming (SDP) analysis over the flood season.

I would start with (b). It matches operator reasoning and is transparent. I would test (a) as the simple benchmark and keep (c) as a later extension. The multi-peak events (2016, 2018) are where (b) should beat (a): a fixed target refills between peaks and then has to spill hard on the next one.

### 4.6 Horizon length

Use the 6-h forecast horizon, possibly extended to 12–24 h with a persistence or recession assumption beyond 6 h, flagged as low-information. Test horizons of 6, 12 and 24 h. A longer horizon helps smooth ramps and plan gate states. But beyond 6 h it relies on poor inflow information. I expect 6–12 h to be the useful range. The sensitivity test will decide.

## 5. Forecast uncertainty

1. **Inflow forecast model.** KMA gives rainfall, not inflow, so a rainfall-to-inflow conversion is needed. This could be K-water's existing runoff model if one exists, or a simple data-driven model (an ARX model on recent inflow plus forecast rainfall) fitted on the record. Its 1–6 h error, by lead time and by event phase (rising limb versus recession), must be measured.
2. **Forecast cases for hindcasts:**
   - **Perfect forecast** over the horizon: an upper bound on MPC performance.
   - **Realistic forecast:** archived KMA forecasts run through the inflow model, if A6 holds.
   - **Synthetic forecast:** perfect forecast plus errors drawn from the fitted error model, growing with lead time, with timing and magnitude errors and autocorrelation. Used if archives are missing. Run many replicates to get distributions, not single results.
   - **Naive forecast:** persistence. A lower bound.
3. **Ways to handle uncertainty, to compare:**
   - deterministic MPC on the expected forecast, plus the safety margin of §4.4;
   - scenario (ensemble) MPC with about 10–30 inflow scenarios, a shared first step, and chance-style limits on the level (for example P(h > ceiling) ≤ ε) or a worst-case limit on the level only;
   - possibly a two-stage or tree MPC if scenario MPC looks promising.

   Provisional view: scenario MPC should matter most on rising limbs, where under-forecasting leaves too little time. Deterministic MPC with a margin may be nearly as good elsewhere and is easier to explain. Choose the simplest method whose performance on safety and spill is within tolerance of the best.
4. **Revision stability under noisy forecasts.** Forecast updates every hour will push the optimiser to revise its schedule. The revision penalty and the gate-persistence rules exist to damp this. Tune them so the schedule changes only when the forecast change matters, for example when it would move the projected peak level by more than a threshold.

## 6. Experiments

| Experiment | Purpose |
|---|---|
| E1. Historical replay (baseline) | Metrics of actual operation on 2016, 2018, 2020 |
| E2. Perfect-foresight full-event optimisation | Best achievable trade-off; shows how much the short horizon costs |
| E3. MPC with perfect 6-h forecast | Cost of the short horizon alone |
| E4. MPC with realistic or synthetic forecasts (many replicates) | Cost of forecast error; distribution of results |
| E5. Deterministic vs scenario MPC | Whether stochastic handling is worth the complexity |
| E6. Terminal-condition variants (a) vs (b) | Effect on multi-peak events and post-event supply |
| E7. Sensitivity | Horizon length; safety margin; penalty weights or tolerances; initial level (start at NHWL vs lower); gate minimum-duration rules |
| E8. Stress tests on scaled hydrographs | Behaviour toward the 200-year magnitude |

**Note on E8.** No 200-year or probable maximum flood (PMF) hydrographs exist. I would scale the observed hydrographs, for example 2020 peak × ~2.4 to reach about 10,700 m³/s, and also use 2016/2018 shapes. These must be labelled **stress tests, not design-flood analyses**. Scaling keeps observed shapes and timing, which may not be how a real 200-year event looks. They are for checking that the tool degrades gracefully: it opens gates early enough, does not breach the ceiling, and does not oscillate. They are not for certifying safety. If K-water has design hydrographs from the dam's safety review, use them instead.

**Metrics, reported per event and per replicate:**
- maximum level and minimum margin to FWL;
- peak outflow, peak outflow divided by peak inflow, and hours where outflow exceeded the inflow peak observed so far;
- spill volume, spill hours and peak spill;
- turbine use (share of hours at 264 m³/s when releasing more than 264), turbine energy;
- number of gate open/close changes, and the shortest gate-open spell;
- mean and maximum ramp, and mean and maximum revision between consecutive schedules for shared hours;
- end-of-event storage versus target;
- violations of minimum release;
- solve time per hour, which must be well under the decision interval.

## 7. Capturing and validating operator preferences (critical for acceptance)

1. **Structured interviews** with Daecheong operators before tuning:
   - their priority order;
   - what "flood clearly ending" means;
   - acceptable ramp sizes;
   - how far ahead they need stable schedules for downstream agencies;
   - how they handle the dilemma between successive peaks.

   These set the lexicographic order, tolerances and terminal rule.
2. **Learn from historical behaviour.** Fit the objective's weights or tolerances so MPC reproduces historical releases as closely as possible (inverse optimisation, or calibrating against actual outflows). Use this only as a starting point: matching history copies past habits, not necessarily good practice. If archived *issued schedules* exist (A6), they give much better information on revision behaviour than actual outflows alone.
3. **Acceptability review.** Show operators MPC schedules beside historical ones for the same situations, without labels if possible, at key moments (onset of a rising limb, between peaks, recession and gate closure). Collect ratings and reasons, and revise the objectives.
4. **Trade-off presentation.** For the main tensions, show a small set of options along the trade-off curve rather than one "optimum":
   - spill versus end storage;
   - stability versus responsiveness;
   - safety margin versus spill.

   Let operators choose the setting.

## 8. Key risks and how they could change the plan

- **Noisy inflow and a noisy "peak so far".** If smoothing changes the peaks a lot, the no-amplification constraint needs a tolerance band, or a definition based on a filtered estimate agreed with operators.
- **Forecast skill.** If the inflow forecast at 3–6 h is barely better than persistence, scenario MPC brings little. A deterministic MPC with a margin, plus robust rules on the rising limb, would be the recommendation.
- **Computation.** Binary gate variables with several scenarios could slow the MILP. Hourly operation gives ample time, but if needed, reduce scenarios or fix gate states heuristically.
- **Few events.** Three events give few independent test cases. Present results as a demonstration, not statistical proof. Report results per event and per replicate rather than pooled claims. Add more historical floods from the hourly record if K-water agrees, even smaller ones.
- **Age of the dam and structural limits.** Any gate-rate or structural limits from the dam's current safety status should be hard constraints. I would ask for them explicitly.
- **Downstream constraints.** If a downstream safe discharge exists (A3), it could be the binding constraint and would change the objective ranking.

## 9. What would confirm or change the provisional recommendation

The recommendation is confirmed if, across the three events and forecast replicates, MPC:
- stays below the operating ceiling;
- never exceeds the inflow peak observed so far, except where safety requires it;
- spills no more than historical operation, and ideally less, through better use of turbines and pre-release;
- reaches the end-of-event storage target;
- uses no more gate changes and revisions than history did;
- is rated by operators as acceptable or better than their own schedules in most reviewed situations.

**Things that would change it:**
- If operators reject optimised schedules mainly for being opaque, move toward an **optimisation-derived rule set** (rules extracted from MPC behaviour) or MPC with very strong stability penalties.
- If scenario MPC does not beat deterministic MPC with a margin, recommend the deterministic version.
- If the terminal rule dominates performance, invest in the value-function approach (c).
- If stress tests show the ceiling is breached under forecast error at large magnitudes, the margin has to grow or pre-release rules must be added. That issue would go back to K-water as an operating-policy question, not something the tool can solve alone.
