# Reservoir Operating Level Assessment: Can 154 m Serve as the Actual Upper Limit?

## Theoretical Maximum Allowable Level

### Feasibility-Based Calculation

The theoretical maximum level is determined by the capacity to draw down to the design flood-limited level (152 m) within the available lead time under the downstream safety constraint.

**Key constraints:**

1. **Effective lead time for drawdown:**
   - Forecast lead time: 36 hours
   - Decision + warning + gate adjustment: 8 hours
   - Effective drawdown time: 28 hours

2. **Downstream safety constraint:**
   - Safe discharge limit: 5,000 m³/s
   - Uncontrolled intervening catchment: up to 1,200 m³/s during storms
   - Maximum controllable dam release (worst case): 5,000 − 1,200 = 3,800 m³/s

3. **Volume calculation:**
   - Storage per meter between 152–154 m: 90 million m³/meter (180 MCM ÷ 2 m)
   - Volume releasable in 28 hours at 3,800 m³/s: 3,800 m³/s × 100,800 s = 383 MCM
   - Equivalent drawdown: 383 ÷ 90 ≈ **4.3 meters**
   - **Theoretical maximum level: 152.0 + 4.3 = 156.3 m**

### Physical Feasibility of 154 m

Operating at 154 m (180 MCM above FLWL) is **technically feasible** from a pure drawdown perspective:
- Required average release rate: 180 MCM ÷ 28 hours ÷ 3,600 s/h = **1,786 m³/s**
- This is well below the maximum controllable release of 3,800 m³/s
- Downstream impact with normal-range intervening inflow (500 m³/s): 1,786 + 500 = 2,286 m³/s, safely below 5,000 m³/s limit

**Provisional judgment: 154 m can serve as an actual operating upper limit, BUT only with robust safety margins, operational safeguards, and continuous monitoring.** The theoretical feasibility does not automatically make it safe without additional verification.

---

## Critical Safety Margins That Must Be Considered

### 1. Forecast Reliability and Lead-Time Decay

**Issue:** The 36-hour forecast lead time is valuable but not perfect, especially at longer leads.

**Margins needed:**
- Forecast skill varies with lead time; later portions (24–36 hours) typically have higher uncertainty
- A conservative operating rule should assume the worst-case forecast scenario within the high-uncertainty window
- **Suggested margin:** Reserve additional drawdown capacity for scenarios where the peak inflow is underforecast by 1 or 2 standard deviations (e.g., 20–30% underestimation)

**Implication for 154 m:** If the peak is underforecast by 30%, the operator may need to release faster than planned, approaching the downstream limit. The 154 m level should include a safety buffer to handle this.

### 2. Decision/Action Latency and Uncontrolled Inflow During Delay

**Issue:** The 8-hour delay (decision through gate adjustment) is substantial. During this period:
- Inflow continues at normal or elevated rates (1,500–3,000+ m³/s)
- No active control is being implemented
- Water level rises uncontrollably

**Quantification:**
- If inflow averages 2,000 m³/s during the 8-hour delay: 2,000 × 28,800 s = 57.6 MCM = 0.64 m rise
- This rise must be accommodated in the available drawdown window

**Margin needed:** The 154 m upper level should account for the "locked-in" water rise during the 8-hour dead time. The actual operating upper limit should be lower than the theoretical maximum by this amount.

**Revised practical maximum: 154.0 − 0.64 ≈ 153.4 m** (if 8-hour inflow averages 2,000 m³/s)

### 3. Downstream Safety Threshold Variability

**Issue:** The "safe discharge" of 5,000 m³/s is stated as a fixed limit, but in practice:
- Levee capacity is not a sharp threshold; there is a **fragility curve** (risk increases gradually above the nominal capacity)
- Intervening catchment inflow varies unpredictably; the 1,200 m³/s is a maximum, but actual storm-phase inflow is uncertain
- Any release strategy must stay comfortably below 5,000 m³/s, not just achieve it

**Safety margin:** Assume a **buffer of 500–1,000 m³/s** below the nominal safe discharge, giving an effective operational safe discharge of 4,000–4,500 m³/s.

**Impact on maximum level:**
- With 4,000 m³/s effective safe discharge and 1,200 m³/s uncontrolled inflow: max dam release = 2,800 m³/s
- Volume releasable in 28 hours: 2,800 × 100,800 = 282 MCM ≈ 3.1 m drawdown
- **Revised theoretical maximum with safety margin: 152.0 + 3.1 = 155.1 m**

### 4. Discharge Capacity Uncertainty

**Issue:** The 7,500 m³/s maximum release is stated at 152 m. But:
- Release capacity may depend on water level; higher levels may allow higher discharge, but this relationship must be verified
- The capacity is the stated design capacity, but actual performance under surge conditions is uncertain
- Gate operability and response time have limits

**Margin needed:** Assume only 90–95% of nameplate capacity is reliably available. Use 7,000–7,100 m³/s as the working maximum.

### 5. Forecast Update Lag and Trend Uncertainty

**Issue:** Forecasts are updated every 6 hours, but:
- There is a lag between forecast issuance and operational response
- A flood trend (intensity, timing) can shift between updates
- Early forecasts may miss rapid intensification

**Margin needed:** Assume that a flood forecast issued 24+ hours ahead could miss the peak by several hours or underestimate intensity by 20–30%. The operating rule must be conservative enough to handle a "surprise intensification."

---

## Verifications That Should Be Carried Out Before Setting 154 m as the Operating Upper Limit

### 1. **Feasibility Verification: Drawdown under Historical and Scenario Floods**

- **What to do:**
  - Simulate the drawdown from 154 m to 152 m for all major historical flood events in the record
  - Verify that the 28-hour window is sufficient for each event
  - Check whether downstream discharge ever exceeds 5,000 m³/s during the drawdown
  - Test against synthetic floods (e.g., 50-year, 100-year, 200-year peak inflows) to stress-test the rule

- **Key checks:**
  - Do any scenarios require releases exceeding 3,800 m³/s to stay within the 28-hour window?
  - Does the intervening catchment inflow ever spike unpredictably (e.g., local burst floods not captured in the main-basin forecast)?
  - Is 7,500 m³/s discharge capacity actually achievable at all water levels in practice?

- **Acceptance criterion:** 100% of historical major floods and 95%+ of synthetic scenario floods must be able to drawdown from 154 m to 152 m without exceeding downstream safe discharge.

### 2. **Forecast Skill Verification at 24–36 Hour Lead Times**

- **What to do:**
  - Obtain hindcast or reforecast data (actual vs. forecast inflows at 6-, 12-, 24-, and 36-hour leads) for at least 20–30 historical flood events
  - Calculate forecast error metrics (mean absolute error, bias, standard deviation) by lead time
  - Compute the probability of underforecasting peak inflow by 20%, 30%, and 50% at each lead time

- **Key checks:**
  - What is the forecast skill at 24–36 hours specifically? Is it Grade A (α > 90%) or lower?
  - How often is the peak flow underforecast by >20% at the 24–36 hour horizon?
  - Is there a systematic bias (e.g., consistent underestimation of monsoon-season storm intensity)?

- **Acceptance criterion:** Forecast skill should permit a conservative operating rule; if skill at 36-hour lead is only Grade C or lower, the feasible upper level must be reduced or lead-time-dependent margins must be larger.

### 3. **Downstream Fragility and Safety Margin Verification**

- **What to do:**
  - Obtain or develop a fragility curve for downstream flooding at the control section (probability of levee or channel damage vs. discharge rate)
  - Determine the actual "safe discharge" with consideration of risk aversion (not just the nominal capacity)
  - Quantify the relationship between dam release and downstream stage/flow (travel time, channel storage)

- **Key checks:**
  - Does 5,000 m³/s represent a hard cutoff or a nominal threshold with gradual risk?
  - What is the consequence of a 10%, 20%, or 30% exceedance of 5,000 m³/s for 1–6 hours?
  - How sensitive is the downstream level to the intervening catchment inflow? (If intervening inflow is 1,200 m³/s and highly variable, the margin of safety shrinks.)

- **Acceptance criterion:** Establish a conservative operational safe discharge (e.g., 4,500 m³/s to provide a 500 m³/s safety margin) and verify that drawdown rules maintain it under all operationally relevant scenarios.

### 4. **Operational Latency Verification**

- **What to do:**
  - Time the full decision-to-gate-adjustment process on several test cases
  - Verify the 8-hour estimate; if actual practice is faster, margins can be tighter; if slower, margins must widen
  - Identify the largest sources of latency (data processing, authorization, mechanical gate response)
  - Determine the variability: is 8 hours worst-case or typical?

- **Key checks:**
  - Under operationally realistic conditions (staffing, IT systems, communication protocols), how much faster or slower than 8 hours could the process be?
  - In emergencies, can the process be accelerated? By how much?
  - Is the 8-hour estimate validated under actual operational procedures, or is it an estimate?

- **Acceptance criterion:** Confirm that the 8-hour latency (or actual measured latency) is realistic and that all operating rules account for this deadtime.

### 5. **Joint Risk Assessment: Reservoir Level + Downstream Discharge**

- **What to do:**
  - Run a joint risk simulation:
    - For each historical or synthetic flood scenario:
      - Track the maximum water level reached if starting from 154 m
      - Track the maximum downstream discharge during the prerelease phase
      - Check whether both remain within acceptable bounds simultaneously
  - Calculate the combined probability of:
    - Reservoir level exceeding 155 m (or another safe structural limit)
    - AND downstream discharge exceeding 5,000 m³/s (or the operational threshold)
    - OR either happening at the same time

- **Key output:** A risk matrix or exceedance probability table showing the joint risk of structural/safety violations at 154 m vs. other candidate upper levels.

- **Acceptance criterion:** Agree on an acceptable joint risk (e.g., <1% annual probability of exceeding both limits simultaneously, or <5% annual probability of exceeding downstream limit).

### 6. **Sensitivity and Stress Testing**

- **What to do:**
  - Test the 154 m rule under stressed conditions:
    - Forecast bias: What if the forecast is consistently 10–20% too low for storm intensity?
    - Faster-than-expected peak: What if the peak arrives 6–12 hours earlier than forecast?
    - Higher uncontrolled inflow: What if intervening catchment delivers 1,500 or 1,800 m³/s instead of 1,200 m³/s?
    - Slower than expected gate operation: What if the 8 hours extends to 10 or 12 hours?
    - Blocked or reduced discharge capacity: What if the outlet can only deliver 5,500 m³/s (e.g., due to sediment, maintenance)?

- **Key output:** A sensitivity table or tornado diagram showing which uncertainty sources most threaten the feasibility of 154 m.

- **Acceptance criterion:** Identify which failure modes are plausible and frequent enough to require rule modification. If any single stress condition causes frequent violations, the upper level must be lowered.

### 7. **Coordination with Downstream Authorities**

- **What to do:**
  - Confirm with downstream dam operators, water-supply agencies, and flood-protection authorities:
    - Is 5,000 m³/s the true safety limit, or is a lower operational discharge preferred?
    - Are there ramping rate limits (e.g., rate of change of discharge)?
    - What is the warning protocol? (How is downstream warned of prerelease?)
    - What is the tolerance for brief exceedances (e.g., 5,200 m³/s for 2 hours is acceptable, but 6,000 m³/s for 4 hours is not)?

- **Key output:** A jointly agreed operational envelope specifying safe discharge, ramp rates, warning protocols, and tolerance thresholds.

### 8. **Seasonal and Non-Stationary Verification**

- **What to do:**
  - Examine whether 154 m is safe to hold all year, or whether the upper limit should vary seasonally:
    - Monsoon season (May–September): forecast skill, typical flood intensity
    - Pre-monsoon (March–April): dry season, different flood types
    - Post-monsoon (October–November): typical storm patterns and inflow variability
  - Check for climate/long-term trends: has flood intensity changed in the past 10 years? Is the 1,500 m³/s pre-flood inflow still typical?

- **Acceptance criterion:** Determine whether 154 m is safe year-round or whether seasonal adjustments are needed.

---

## Information Still Missing Before Final Operating Limit Can Be Set

### 1. **Discharge Capacity Rating Curve**
- Is 7,500 m³/s available at all water levels between 152 m and 154 m, or does capacity decrease at lower levels?
- What is the gate opening/closing rate, and can it deliver maximum discharge within the 28-hour window?

### 2. **Detailed Downstream Fragility and Consequence Model**
- What are the actual damage/risk consequences of exceeding 5,000 m³/s by 10%, 20%, or 50%?
- Is the 5,000 m³/s limit a levee-stability constraint, a channel-erosion constraint, or a policy preference?
- What is the acceptable risk of downstream exceedance per year or per decade?

### 3. **Historical and Forecast Performance Data**
- Hindcasts or reforecasts for at least 20–30 major historical floods, with observed vs. forecast inflows at 6/12/24/36-hour leads
- Actual operational latencies from recent prerelease events (is 8 hours realistic?)
- Actual intervening catchment hydrographs: how often does inflow reach 1,000, 1,200, or exceed 1,200 m³/s during storms?

### 4. **Structural and Engineering Limits**
- Is 154 m a structurally safe water level for the dam itself, or only a flood-control consideration?
- What is the PMF (probable maximum flood) scenario, and does the reservoir's structural capacity place a ceiling below or above 154 m?
- Are there any previous operating manuals or design documentation that sets design levels?

### 5. **Institutional and Regulatory Constraints**
- What does the dam-safety or water-management regulation specify for flood-limited levels and upper bounds?
- Are there agreements with other reservoirs in a cascade system that constrain this reservoir's operations?
- Is there a legal or policy requirement for a specific minimum flood pool or design return period?

### 6. **Real-Time Forecast and Monitoring Capability**
- What forecast model is used? What is its skill for this basin?
- Are the 36-hour forecast lead time and 6-hour update frequency actually available operationally, or are they planned/aspirational?
- Is there a measurement-based backup if forecasts fail (e.g., radar, upstream gauges)?

### 7. **Gate Operability and Failsafe Behavior**
- What happens if a gate jams or fails to open fully during a prerelease?
- Can the spillway gates also contribute, or is spillway overflow uncontrolled?
- What is the maximum sustained discharge if multiple outlets are used simultaneously?

### 8. **Intervening Catchment Uncertainty and Control**
- Is the 1,200 m³/s intervening inflow truly uncontrolled, or are there upstream structures that can mitigate it?
- What is the spatial distribution of this inflow? Does it concentrate at one point or spread across the reach?
- How much lead time is available to warn of intervening catchment flooding?

### 9. **Trade-offs with Other Objectives**
- Is hydropower generation affected by holding at 154 m vs. lower levels? What is the benefit/cost?
- Is water supply for the region affected?
- What is the cost of being wrong (over-preparing for false alarms; under-preparing for missed floods)?

### 10. **Adaptive Operating Rules and Real-Time Decisions**
- Should the 154 m upper limit be hard (must not exceed), or should there be a soft limit with conditional exceedance allowed if the forecast is very strong?
- How often should the rule be reviewed and updated in light of observed forecast performance?
- Should the upper level be time-varying (e.g., lower during the peak monsoon months)?

---

## Provisional Recommendation and Next Steps

### Can 154 m Serve as the Actual Operating Upper Limit?

**Verdict: Tentatively yes, but only with substantial verification and operational safeguards.**

**Reasoning:**
- Physically feasible to draw down in 28 hours without exceeding downstream safety limits (requires ~1,786 m³/s average release, well below the constraint)
- Provides operational flexibility over the lower design level of 152 m
- Aligns with the operator's objective to hold storage when no flood is imminent

**However:**
- The 8-hour decision latency, forecast uncertainty at the 24–36 hour horizon, and variability in intervening catchment inflow create real risks
- A safety margin of 0.6–1.0 m below 154 m is prudent
- **Recommended practical operating upper limit: 153.0–153.5 m** (instead of 154 m) to account for latency and forecast error

### Path Forward

1. **Gather the missing data** listed above (especially hindcast forecast skill, operational latency, downstream fragility)
2. **Run feasibility and risk simulations** on historical floods and synthetic scenarios (Verification 1, 3, 5)
3. **Engage downstream stakeholders** to confirm the safe discharge threshold and risk tolerance (Verification 7)
4. **Establish decision rules for different flood stages:**
   - If forecast peak inflow >X m³/s → start prerelease immediately (target 153.5 m before 24-h lead)
   - If peak arrives faster than forecast → expedited drawdown protocol
   - If forecast confidence is low (skill Grade C or worse) → use lower initial level (152.5 m)
5. **Document and field-test** the operating rule on at least 5–10 actual flood events before finalizing
6. **Revisit annually** after the monsoon season with actual performance data

The 154 m upper limit is not fundamentally unsafe, but 153.0–153.5 m is a more robust and defensible choice given current uncertainties.
