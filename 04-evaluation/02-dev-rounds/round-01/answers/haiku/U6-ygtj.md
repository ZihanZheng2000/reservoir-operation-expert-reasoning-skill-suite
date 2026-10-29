# Advice on Multipurpose Reservoir Operating Scheme Selection

## 1. Framework for Comparing Schemes and Handling Trade-offs

### Defining the Conflicting Objectives

The four schemes present a fundamental conflict among reservoir objectives:
- **Flood control** (downstream safety, measured by flood-exceedance probability)
- **Hydropower generation** (revenue, measured in energy output)
- **Irrigation supply** (end-of-season storage availability)
- **Navigation** (minimum flow duration requirements)

Raising the operating level for hydropower necessarily reduces the flood-control buffer, increases flood risk, and may affect irrigation refill timing. These objectives are **non-compensable** — you cannot trade unlimited amounts of one for another without violating a safety threshold or institutional mandate.

### Recommended Comparison Approach

**Step 1: Safety First as a Non-Compensable Constraint**

Establish what flood-risk level is acceptable for the city and downstream communities. The current rule maintains a 1.0% annual probability of exceeding the safe flow threshold. This should be treated as a **binding constraint**, not a negotiable objective. Any scheme that raises this probability above an explicitly approved limit should be screened out before further evaluation.

The key question: *Is the city and flood-control agency willing to accept 1.3% (Scheme B) or is 1.0% a hard ceiling?* This decision must come from the decision-maker before mathematical ranking.

**Step 2: Build a Criteria System with All Four Objectives**

Create a decision matrix with criteria for each objective:
- **Flood safety:** Probability of exceeding safe-flow threshold (lower is better)
- **Generation:** Mean annual energy output (higher is better)  
- **Irrigation reliability:** End-of-season storage reliability (higher is better)
- **Navigation:** Mean days per year with insufficient flow (lower is better)

Do not collapse these into a single weighted score yet. The papers in the reference show that aggregation can mask critical information — a "best compromise" score may hide that one scheme fails catastrophically on navigation or irrigation while excelling on generation.

**Step 3: Identify the Noninferior (Pareto) Set**

Plot the schemes against pairs of criteria to identify which are clearly dominated:
- Scheme A: +0.3 GWh generation, same flood risk, -2% irrigation reliability, +2 days navigation deficit
- Scheme B: +0.5 GWh generation, +0.3% flood risk, +3% irrigation reliability, -3 days navigation benefit
- Scheme C: +0.2 GWh generation, -0.1% flood risk, -7% irrigation reliability, +6 days navigation deficit

Scheme B improves generation and irrigation while slightly raising flood risk. Scheme C raises flood risk and harms irrigation. Scheme A is a small gain everywhere except irrigation. **None is dominated across all criteria**, but the choice among them depends on what the decision-maker values most.

**Step 4: Test Ranking Stability**

The recommendations assume the four indicators are equally important. Sensitivity analysis should answer:
- What if flood safety is weighted 50% of the decision (vs. equal weight)?
- What if irrigation reliability is the top priority?
- How sensitive is the ranking to measurement uncertainty in the 40-year study?

The reference emphasizes that **equal weights are an assumption, not a default**, and should be stated explicitly.

### Known Limitation of This Study

**No uncertainty intervals are provided.** The reference material on evidence emphasizes that estimates without uncertainty bounds cannot support a robust decision:
- Do the differences between schemes (e.g., 10.3 vs 10.5 GWh) exceed the margin of error from the 40-year sample?
- How sensitive are flood-risk estimates to the modeling assumptions?
- Could sampling variability reverse the ranking?

This absence is a material gap. Before finalizing a choice, the commission should request 95% confidence intervals around each estimate, or at minimum a sensitivity test showing how robust the comparison is to ±10% perturbations in each indicator.

---

## 2. Recommendation and Basis

### Provisional Recommendation: **Scheme B, conditional on risk approval**

**Reasoning:**

Scheme B is the only alternative that improves both generation and irrigation reliability while keeping flood risk within a small increment (1.3% vs. 1.0%). For a multipurpose reservoir, this is the profile most likely to satisfy all stakeholders without forcing a zero-sum trade-off.

- **Generation:** +0.5 GWh (+5% over current rule) is a material revenue benefit for the hydropower company.
- **Irrigation reliability:** +3% (92% → 95%) provides a real improvement in supply certainty for the irrigation district.
- **Flood risk:** +0.3 percentage points (1.0% → 1.3%) is an increase, but **whether this is acceptable depends on the city's risk tolerance and the current standard.** A 0.3 pp change is often within the uncertainty of a 40-year hindcast study, but this needs validation.
- **Navigation:** -3 days (12 → 9 days) is a net improvement, a co-benefit.

**Schemes A and C should not be adopted:**
- **Scheme A:** Offers only marginal generation gain (+0.3 GWh) with no offsetting irrigation benefit and worse navigation. It is unlikely to justify the approval process.
- **Scheme C:** Worsens both flood control (0.9% vs 1.0%) and irrigation (85% vs 92%), harming two objectives while offering only +0.2 GWh generation. This is dominated and should be eliminated.

**Keep the current rule only if:**
- The city's risk-averse preference is so strong that even a 0.3 pp increase in flood probability is unacceptable, *and*
- The hydropower revenue is not critical to basin water-management sustainability.

### Required Conditions for Approval of Scheme B

1. **Flood-risk acceptance:** The city's flood-control authority must explicitly approve a 1.3% annual exceedance probability as consistent with levee design standards, insurance assumptions, or damage-acceptable protocols. This should be documented as a formal decision, not implicit.

2. **Upstream study gaps:**
   - Request 95% confidence intervals on all estimates from the 40-year model.
   - Sensitivity test: recompute flood risk under ±0.5σ perturbations in key model parameters (e.g., forecast error, spillway rating curve).
   - Cross-check the flood-risk estimate using a second, independent model or a simplified analytical bound (e.g., based on inflow tail statistics).

3. **Irrigation refill timing:** Clarify whether the end-of-flood-season storage reliability of 95% is sufficient given downstream demand patterns. If irrigation draw-down begins immediately after flood season, a higher end-of-season level may provide little real benefit.

4. **Pilot or phase-in:** Consider a 1–2 year pilot of Scheme B under enhanced monitoring, with pre-agreed decision criteria to revert to the current rule or adjust the operating level if flood-season experience contradicts the model.

---

## 3. Stakeholder Participation and Decision Process

### Agencies and Stakeholders to Involve

**Core decision-makers:**
1. **Basin Commission** (neutral chair, holds final authority)
2. **City Flood-Control Department** (downstream safety mandate; currently concerned)
3. **Hydropower Company** (proponent; owns generation interest)
4. **Irrigation District** (currently concerned; affected by storage levels)
5. **Navigation Authority or Port Authority** (affected by release timing and minimum flows)

**Supporting participants:**
6. **Environmental agency or water-quality regulator** (if ecology/temperature thresholds are affected by raised levels or altered release patterns)
7. **Weather/flood-forecast service** (to confirm the study's forecast-error assumptions and verify 40-year hindcast credibility)
8. **Independent technical review panel** (to audit model assumptions and uncertainty)

### Recommended Decision Process

**Phase 1: Information and Concern Gathering (Public Hearing)**
- Present the three alternatives and the current rule on a common decision matrix.
- Solicit written position statements from each agency on risk tolerance, minimum acceptable levels for their objective, and trade-off preferences.
- Ensure the flood-control department and irrigation district can articulate their concerns in technical detail, not just opposition.

**Phase 2: Technical Vetting**
- Independent review of the 40-year study, focusing on:
  - Uncertainty estimation (confidence intervals on estimates)
  - Flood-risk model assumptions and sensitivity
  - Representativeness of the 40-year sample for future climate or watershed changes
- Request the hydropower company and other study sponsors to release model code, data, and assumptions for scrutiny.

**Phase 3: Multi-Objective Ranking Workshop**
- Convene a working group (one representative from each agency + basin commission) to:
  - Agree on the criteria system (the four objectives above, or others if identified).
  - Discuss value trade-offs: *What is 1% irrigation reliability worth relative to 0.3 pp flood-risk increase?*
  - Generate a weighting scheme using structured methods (e.g., AHP with paired comparison, or simple scoring if consensus is strong).
  - Apply the weights to the study's estimates and identify the rank order.
- Document dissenting views and the decision basis transparently.

**Phase 4: Stakeholder Consultation and Approval**
- Present the ranked schemes and the basin commission's initial recommendation to elected officials, the public, and technical reviewers.
- Require explicit approval from the city (for flood risk) and the irrigation district (for storage impact) before a scheme is adopted.
- Record which agencies support, conditionally support, or oppose each alternative, and why.

**Phase 5: Adoption with Monitoring**
- Issue a formal operating manual amendment with the chosen scheme, including:
  - The approved flood operating level(s)
  - Decision thresholds for pre-release, stage-specific adjustments, and emergency overrides
  - Roles and approval authority for real-time operations
  - A post-event reanalysis protocol to validate that observed flood events match the model assumptions
- Establish a 2–5 year review cycle to compare actual operations and outcomes against the study predictions.

### Key Principles

- **Transparency:** All estimates, assumptions, and uncertainty should be public. Do not hide model parameters or confidence intervals in appendices.
- **Authority clarity:** State explicitly which agency has the final say on flood risk, which on generation, which on irrigation. A consensus-driven process is better than one where one agency can veto.
- **Reversibility:** Design the scheme with a reversion clause if flood-season events violate the assumed risk profile. Do not treat Scheme B as irreversible after one approval.
- **Documentation:** Keep a record of which agency accepted which risk, when, and on what basis. This protects future operators when disputes arise.

---

## Summary

Recommend **Scheme B**, contingent on the city's explicit acceptance of 1.3% annual flood-exceedance probability and subject to uncertainty analysis. Use a structured multi-objective framework to make trade-offs transparent, and ensure all four stakeholders (flood control, hydropower, irrigation, navigation) have a formal voice in the decision. The current rule should be retained only if risk tolerance is exceptionally conservative or if the technical uncertainty in Scheme B's estimates proves too large to resolve.
