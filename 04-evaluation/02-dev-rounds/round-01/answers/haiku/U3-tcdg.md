# Expert Review: Consulting Firm's Prerelease Rule Analysis

## Executive Summary

The consulting firm's analysis has merit in using synthetic forecast scenarios to evaluate a new prerelease rule, but critical methodological problems undermine confidence in the "95% confidence" claim and the 18% outflow reduction conclusion. The forecast error model is oversimplified, key dependencies are not preserved in scenario generation, forecast reliability has not been verified, and robustness testing is absent. I cannot recommend adoption without substantial additional evidence.

---

## Identified Methodological Problems and Uncertainties

### 1. Forecast Error Model is Oversimplified

**Problem:** The firm fitted a single normal distribution to all 12 years of daily 3-day forecast errors, pooling across seasons, flow magnitudes, and forecast lead times. This violates what 50 papers in flood operation research found.

**Why it matters:**
- Forecast errors typically vary significantly by lead time, flow regime, and season
- A single pooled distribution will understate or overstate uncertainty at specific times and conditions
- Example from the literature: errors might be σ ≈ 20% at 1-day lead but σ ≈ 50% at 3-day lead; a pooled distribution loses this variation
- Biased or heavy-tailed errors (common in flood forecasts) misspecified as normal will give wrong tail probabilities

**What the literature shows:**
- Papers fit separate distributions per lead time, season, or flow regime (e.g., one for June, separate for July–September)
- Some used non-normal distributions (Wakeby, generalized logistic) selected by comparison of candidates
- Errors often decrease or change character as floods develop and forecasts update

### 2. Synthetic Scenarios Do Not Preserve Error Dependence

**Problem:** The firm generated 5,000 scenarios by sampling each day's error *independently*. Literature and error properties show this is incorrect.

**Why it matters:**
- Forecast errors are serially correlated: if a forecast is wrong on day 1, it is likely wrong on day 2 in a similar direction
- Independent daily errors will understate joint uncertainty over the 3-day window
- This leads to an optimistic (too narrow) distribution of possible inflow trajectories
- Real errors cluster; the model allows them to scatter randomly, masking the risk of sustained wrong forecasts

**What the literature shows:**
- Papers use copulas (Student-t or Gumbel) to model temporal dependence across lead times
- Correlations among adjacent errors often exceed 0.7
- Failure to preserve dependence underestimates tail risk (risk of multiple bad outcomes together)
- Example: if errors are independent, there is a small chance of −30% on each of three days; with dependence, sustained −30% error is more likely

### 3. Forecast Reliability and Timing Have Not Been Verified

**Problem:** No evidence is presented that 3-day inflow forecasts at this reservoir are reliable or that they occur early enough for operational benefit.

**Why it matters:**
- The rule depends on having usable forecast information; if forecasts are poor or late, the rule cannot work
- Operational value of a forecast is not the same as accuracy alone; even a moderately good forecast may be operationally useful if it arrives in time for action
- Without verification, the "confidence" claim has no anchor in real forecast performance

**What the literature shows:**
- Papers verify forecasts against observations using skill metrics (qualified rate α, R², NSE) by lead time
- They show that reliability changes with lead time and that usable horizons are often shorter than hoped
- Example: α = 92% at 1 day might drop to 75% at 3 days; a rule needs to know where the skill cliff is
- Papers also check: does the forecast cover the lead time needed to act? Does travel time or channel storage delay action?

### 4. Error Model Fit Was Not Tested

**Problem:** The firm "fitted a normal distribution" to the errors but provided no goodness-of-fit test.

**Why it matters:**
- Normal distributions have thin tails; flood errors often have fat tails (extreme events, underforecasting large inflows)
- A chi-square or Kolmogorov–Smirnov test could reject normality
- Misspecification of the error distribution changes risk estimates at the extremes, which is exactly what matters for a 100-year design flood

**What the literature shows:**
- Papers compare multiple candidate distributions (normal, generalized logistic, Wakeby, mixtures) and select by RMSE or AIC
- A single rejected distribution choice changed risk estimates by factors of 2–3 in some cases
- Visualization checks (Q–Q plots) often reveal that normal distribution underestimates tail probability

### 5. The "95% Confidence" Claim is Vague and Not Justified

**Problem:** The firm claims "95% confidence" in the 18% outflow reduction but does not explain what this means or how it was computed.

**Possible interpretations:**
- 95% confidence interval on the 18% reduction? (Not stated; what is the upper/lower bound?)
- 95% of the 5,000 synthetic scenarios showed improvement? (No breakdown given)
- A Bayesian credible interval? (No prior or posterior shown)
- A nominal 95% level assumed in the scenario sampling? (Not explained)

**Why it matters:**
- Without a clear definition, the confidence claim is unfalsifiable
- A scenario-based estimate requires a replication strategy (multiple seed values, Monte Carlo convergence checks, or bootstrap resampling) to quantify uncertainty; none is evident
- Adoption of the rule will affect thousands of people and potentially millions in damages; the confidence in the 18% figure must be explicit and defendable

**What the literature shows:**
- Papers document their confidence intervals and credible regions explicitly
- They often conduct sensitivity analysis (vary parameters ±10–20%, show how results change)
- They test robustness (holdout events, random seeds, scenario counts)
- Example: "The 18% reduction has a 90% credible interval of [12%, 24%] and is robust to ±20% error in the forecast uncertainty parameter"

### 6. No Baseline or Comparative Context

**Problem:** The claim compares the new rule to "the current rule" but provides no detail on what is being compared or under what conditions.

**Why it matters:**
- Improvement of 18% on what initial state? Same starting level for both rules?
- What is the current rule's safety margin? Does it fail the 100-year flood design?
- Is the 18% reduction in peak outflow, mean outflow, or maximum storage used?
- A 18% peak reduction that requires 10% more spillage or causes downstream erosion might be worse, not better

**What the literature shows:**
- Papers compare alternatives under identical conditions (same inflows, same initial storage, same horizon)
- They use three baselines: current rule, no-forecast (purely measurement-based), and perfect forecast
- The gap between current and perfect shows the upside; real improvement is less
- Example: if perfect forecast achieves 25% reduction and the new rule achieves 18%, the forecast is capturing 72% of potential value

### 7. No Testing on Historical Events or Varied Conditions

**Problem:** The analysis tested only on a single 100-year design flood scenario. No historical events, smaller floods, or successive floods were tested.

**Why it matters:**
- A rule that works on one design event may fail on others (fast-rising vs slow-rising, early peak vs late peak)
- Smaller floods are common; the rule might waste storage on them
- Sequential floods are realistic; the rule must handle refill and next-event preparation
- Design-flood performance is necessary but not sufficient; operational performance on actual events determines real-world benefit

**What the literature shows:**
- Papers test on 8–50 historical events, plus design floods scaled to multiple return periods
- They report mechanism changes (e.g., this rule preempitively spills on flood A but stores on flood B)
- Example: a rule tested on 100-year floods alone may overshoot storage on 10-year floods and suffer refill losses
- Cross-event testing is standard to show generalization

### 8. No Sensitivity or Stress Testing

**Problem:** The analysis presents one result (18% reduction) without testing robustness to changes in assumptions.

**Why it matters:**
- If the result depends heavily on one parameter (e.g., the 0.5 standard deviation assumed in the error model), small misspecification gives very different results
- Design-flood scenarios are hypothetical; stress tests (e.g., what if the error is ±30% instead of pooled σ?) show how critical the assumptions are
- With only one number and no bounds, there is no basis for judging whether 18% is a robust finding or a brittle artifact of the model choices

**What the literature shows:**
- Papers vary forecast uncertainty levels (e.g., σ = 10%, 20%, 50% m³/s) and show results at each level
- They test scenario count sensitivity (100 scenarios vs 5,000; does the result converge?)
- They vary policy parameters (release thresholds, prerelease timing)
- Example: "The 18% reduction holds under normal error (σ = 0.2) but drops to 8% if error is non-normal with 5% extreme tail probability"

---

## Additional Analyses, Verifications, and Evidence Required

### Required Before Recommendation:

#### 1. Forecast Verification at the Reservoir Site
- Assemble 3-day inflow forecasts and observations for a minimum of 3–5 years (longer is better)
- Calculate lead-time-dependent skill metrics: qualified rate (α), R², or NSE at 1-day, 2-day, and 3-day leads
- Test normality of errors by lead time (K–S test at p = 0.05 or chi-square)
- Document any seasonal variation in accuracy (are errors larger in one season?)
- Report: Do 3-day forecasts retain sufficient skill to support operation? Is the skill at 3 days adequate for the prerelease lead time needed?

#### 2. Correct Error Model and Scenario Generation
- Refit error distributions separately for each lead time (1-day, 2-day, 3-day errors as distinct)
- If seasonal variation exists, fit separate distributions for each season
- Fit multiple candidate distributions and select the best by chi-square or AIC
- Model temporal dependence: estimate correlation matrix or fit a copula model to errors across lead times
- Regenerate synthetic scenarios preserving this dependence (use copula sampling or conditional generation)
- Report: Does the new error model significantly change the risk estimates? Are confidence intervals wider?

#### 3. Test on Multiple Flood Scenarios
- Generate or select at least 20–30 historical or representative design events (100-year, 50-year, 10-year return periods; fast-rising and slow-rising shapes)
- Simulate the new rule on each event under the same initial storage and rules as the current baseline
- Record: maximum storage used, peak outflow, any threshold exceedances, refill time
- Compare against current rule on the same events
- Report: Does the 18% reduction hold across event types, or does it vary widely? On which event classes is the new rule superior?

#### 4. Test Sequential Flood Scenarios
- Test two or three consecutive flood events in quick succession (e.g., flood in May followed by flood in June)
- Verify that the rule refills adequately between events
- Verify that storage freed from the first event is available for the second
- Report: Does the rule's advantage persist, or does sequential risk increase?

#### 5. Robustness and Sensitivity Analysis
- Vary the forecast error standard deviation by ±25% and rerun the optimization. How much does the 18% change?
- Vary the number of synthetic scenarios (100, 1,000, 5,000, 10,000). Does the result converge?
- Test alternative error models (e.g., mixture distributions with a heavy tail) and report results
- Vary the design-flood magnitude by scaling (90-year, 100-year, 110-year equivalents). Does the rule remain stable?
- Report: Is the 18% reduction robust, or is it sensitive to model choices?

#### 6. Quantify Confidence Intervals
- Use bootstrap resampling or multiple random seeds to estimate confidence intervals on the 18% reduction
- Provide upper and lower bounds (e.g., "90% credible interval is [12%, 24%]")
- Explain the source of uncertainty: forecast error, design-flood variability, or both
- State the confidence level and method explicitly

#### 7. Comparison with Baselines
- Compute new rule performance under perfect forecasts (a theoretical upper bound)
- Compute new rule performance with no forecast (measurement-based decisions only)
- Show all three in one table with current rule as the reference
- Report: What fraction of the perfect-forecast potential is the new rule capturing?
- If the gap to perfect is large, investigate whether better forecast models or longer lead times could help

#### 8. Failure Mode and Risk Analysis
- Identify scenarios where the new rule underperforms (e.g., forecast failures, rapid inflow changes)
- Estimate the probability and consequences of these failures
- Compare with failure modes of the current rule
- Propose safeguards (e.g., measurement-based overrides, fallback to conservative release)
- Report: What is the worst-case outcome under the new rule? How does it compare to the current rule?

#### 9. Operational Feasibility and Stakeholder Review
- Verify that the prerelease volumes and timing are implementable given discharge-valve constraints and ramping limits
- Engage downstream agencies and flood-control stakeholders to confirm acceptance of the new release patterns
- Test the rule operationally (as a pilot on real forecasts over one season) if possible, before full adoption
- Document any operational constraints or institutional barriers
- Report: Is the rule executable under real operating conditions?

#### 10. Independent Review and Peer Verification
- Have the analysis reviewed by independent experts in reservoir flood operation and probabilistic forecasting
- Verify that the error model, scenario generation, and risk calculations follow current best practices
- Request a second opinion on the confidence claim and its defensibility
- Report: What are the peer reviewers' concerns, and how are they addressed?

---

## Summary of Required Evidence Before Adoption

The consulting firm's conclusion rests on three pillars that have not been validated:
1. **Forecast reliability** – verified only by pooled error statistics, not by lead-time-dependent skill or site-specific accuracy
2. **Error dependence** – not modeled; independent daily errors likely understate risk
3. **Rule robustness** – tested only on one design flood; no sensitivity analysis, no historical validation

### Key Questions the Owner Should Ask the Firm:

1. What is the 90% confidence interval on the 18% outflow reduction? How was it computed?
2. How well do the 3-day forecasts actually perform at this reservoir? What is the qualified rate at 3-day lead?
3. What happens to the 18% reduction if forecast errors are 25% larger or have a heavy tail?
4. How does the new rule perform on 10-year and 50-year floods, not just the 100-year?
5. Does the rule work if two large floods occur in the same season?
6. What is the worst-case outcome (peak outflow or storage) under the new rule compared to current operation?
7. Have independent experts reviewed the forecast error model and scenario generation method?
8. Is there a measurement-based fallback if the 3-day forecasts fail during an actual event?

---

## Provisional Recommendation

**Do not adopt the new rule based on this analysis alone.** The 18% reduction is plausible but not adequately supported. The analysis would benefit from:
- Correction of the forecast error model and scenario generation
- Validation on multiple historical and design floods
- Explicit confidence intervals and sensitivity tests
- Forecast verification at the specific site
- Independent expert review

**Conditional path forward:** Commission additional studies addressing points 1–3 above (forecast verification, error model correction, testing on multiple events) before revisiting the adoption decision. This can be done within 2–3 months if forecast data are available. If the revised analysis sustains the 18% claim under these tests, adoption is justified; if not, the analysis reveals the limitations and the owner can decide whether to pursue alternative rule improvements.

---

## Notes on Assumptions

This review assumes:
- The firm's claims about forecast data (12 years, 3-day lead time) are accurate
- The 600 million m³ storage and the design-flood scenario are correctly specified
- The new rule is operationally distinct from the current rule and can be tested separately
- The firm's simulation model (routing, storage-elevation curves, etc.) is correct, though this should be independently verified as well

