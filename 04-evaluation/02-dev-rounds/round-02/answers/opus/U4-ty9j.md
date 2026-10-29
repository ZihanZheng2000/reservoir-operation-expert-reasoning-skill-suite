# Advice on adopting the machine-learning release model

## Recommendation

**Do not adopt the model as a direct replacement for the current operating rule for the next flood season.** Keep the current rule as the legal and operational basis. Do three things now:

1. Commission an independent check of the 2023 claim.
2. Run the model in **shadow mode** next season. It runs in parallel and its recommendations are logged, but it does not control releases.
3. Start a staged evaluation that could lead to a formal rule revision, approved by the competent authority, if the model passes acceptance criteria agreed in advance.

The paper is a reason to investigate, not a basis for operation. It shows that, in one retrospective simulation built on the paper's assumptions, the model produced a release schedule with a peak outflow 30% below what operators actually released. It does not yet show that the model would have done that with only the information operators had at the time. It does not show the reduction was free of extra risk at the dam. And it does not show the model will behave safely in a different, larger, or worse-forecast flood, which is the case that matters for a flood rule.

## The deciding questions

Three questions decide this case. The rest of the advice supports them.

1. **Is the 30% reduction real and fairly attributed?** That means the model used only information available at decision time, its own releases fed back into the simulated reservoir state, it started from the same initial level, and it faced the same constraints the operators faced. If any of these fails, the 30% figure shrinks, possibly to nothing.
2. **What did the lower outflow cost?** A lower peak outflow means more water was stored, so the reservoir level rose higher. Downstream, the benefit depends on timing as well as the peak. A rule that lowers outflow by pushing the dam closer to its safety limits is not an improvement for a flood rule.
3. **Does the behaviour hold outside 2023?** That includes floods larger than any in 2010–2022, bad forecasts, missing data, and equipment problems. A data-driven model is least reliable exactly where a flood rule is most needed.

## What the current evidence supports

**Supported, provisionally:**
- Under the paper's simulation set-up, a different release schedule for the 2023 event could have produced a lower peak outflow. This suggests the 2023 operation may have left room for improvement, if the comparison was fair.
- The model is worth a serious evaluation. Testing on 2023 after training on 2010–2022 is a time-ordered holdout, which is the right kind of test, as long as 2023 was not used to tune or select the model.

**Not supported:**
- That the model is better than the current rule in general. The study used one event, and the comparison was against what operators actually did, not against the rule simulated under identical conditions.
- That the model is safe. The headline reports peak outflow only. Maximum reservoir level, flood-storage use, downstream control-point stages, and constraint compliance are not part of the reported claim.
- That the model works in real time. A retrospective simulation does not test data latency, forecast errors as issued, missing inputs, or operator interaction.
- That it would work in floods unlike those in its training years. This is a structural limit of a model trained on 13 years.

## Why the 30% figure needs checking: direction and size of each possible flaw

**1. Information leakage (biggest risk; would shrink the claim).** Check whether the simulation fed the model observed future inflows, or forecasts better than the ones operators actually received in 2023. With either input, the result measures perfect-foresight potential, not deployable performance. A fair test uses the forecasts as issued in real time, from the same forecast system, version, and issue times that would be used in operation. Perfect foresight is useful only as an upper bound.

**2. Mass balance (sets the physical ceiling).** Cutting peak outflow means storing the difference. The extra storage needed is roughly:

ΔV ≈ (reduction in outflow) × (duration of the high-outflow period) × shape factor (about 0.5 for a triangular peak).

The question gives no figures, so here is an illustration with assumed values: an actual peak outflow of 10,000 m³/s, cut by 30% (3,000 m³/s), over a high-outflow period of about 48 h (172,800 s).

ΔV ≈ 3,000 × 172,800 × 0.5 ≈ 2.6 × 10⁸ m³

That volume must have been available in the flood-control zone without the level going past the limits allowed at that stage. There are two ways it could have been available:
- **Higher level:** the model stored more and the level rose higher. This trades downstream relief for dam-side risk.
- **Earlier pre-release:** the model drew the reservoir down before the peak. That requires a forecast that was reliable early enough. The release time needed is about ΔV divided by (release capacity minus inflow). Check this against the forecast lead time that was actually reliable in 2023.

If neither the remaining storage nor a credible pre-release can supply ΔV with the real numbers, the claim is physically impossible as stated.

**3. Baseline confounding (could shrink the claim or show the comparison is unfair).** The operators' actual decisions may have been forced by things the simulation leaves out:
- instructions from a higher flood-control authority;
- downstream conditions such as levee status or tributary peaks;
- a gate or outlet out of service;
- an uncertain level reading;
- a high starting level inherited from earlier operation;
- forecasts that were wrong at the time.

Historical operation is context, not a controlled counterfactual. The proper comparator is the current rule, encoded and simulated with the same inflows, starting level, and constraints, alongside the historical record.

**4. Open-loop versus closed-loop (could invalidate the result).** Check whether the model's simulated releases updated the simulated storage and level, which then fed its next decision. If the model was instead fed the observed historical levels at each step, the "outflow" series is not physically consistent and the 30% is not a valid simulation result.

**5. The training-target paradox.** A model trained on 2010–2022 operations learns to imitate past operator behaviour. A model that imitates operators should not beat them by 30% on a new event unless one of three things is true:
- it had better information (see point 1);
- it was trained to optimize an objective rather than to imitate;
- 2023 was handled unusually badly.

The paper should say which. The answer changes how much the result can be generalized.

**6. Which outcome improved (could reverse the sign of the benefit).** Lower peak outflow at the dam does not automatically mean a lower flood peak downstream. If the model spread releases over a longer period, or released more on the rising limb, the reduced dam outflow could coincide with a tributary peak. The downstream peak could then stay the same or even rise. The benefit must be shown at the downstream control points, after accounting for travel time and local inflow.

## Why one event cannot settle the question

- **Sample size.** One test event gives no estimate of how often the model fails. With n independent test floods and zero failures, the approximate 95% upper bound on the failure rate is 3/n. Five large floods in 2010–2023 (an assumed number) would bound the failure rate only below about 60%. That is useless for a safety decision.
- **Range of floods covered.** The chance that 13 years of record contain at least one flood larger than the 100-year flood is 1 − 0.99¹³ ≈ 12%. The training data almost certainly contain nothing near the design or check flood. The model's behaviour there is extrapolation, and data-driven models can extrapolate badly. They can reduce releases when they should increase them, or behave erratically near the dam's limits.
- **One season of shadow operation is not enough either.** A single season may bring zero to two significant floods. Most of the evidence on rare floods must therefore come from historical replays and synthetic or design floods, not from live experience.

## Unresolved questions

1. What inputs did the 2023 simulation use: forecasts as issued, or observed future inflows? Was 2023 used in any way to tune or select the model?
2. Was the simulation closed-loop? Did it start from the same initial level as the actual operation? Was the simulator validated by replaying the actual 2023 releases and reproducing the observed levels?
3. Under the model, what were the maximum reservoir level, the flood storage used, the end-of-event storage, and the downstream control-point stages, compared with actual operation and with the current rule?
4. Which constraints did the model respect: discharge capacity at the actual head, gate availability, release ramping and drawdown-rate limits, safe downstream channel capacity, and any instructions from higher authority?
5. How does the model behave in floods larger than its training range, in successive or double-peaked floods, from a high starting level, with forecast errors as large as those that actually occur, and with missing or late input data?
6. Is its behaviour physically sensible? For example, release should not fall as inflow and level rise near the limit. Can operators understand why it recommends what it does?
7. Does it hurt other objectives, such as refilling at the end of the flood season, water supply, or hydropower?
8. Who has the authority to approve a change to the operating rule, what approval instrument is needed, and how long does approval take?

## Evaluations before any adoption

**A. Audit and reproduce the 2023 claim.** Weeks to a few months; can run in parallel with B.
- Obtain the code, the trained model, and the input data. Run the evaluation independently, either in-house or through a third party not involved in the paper.
- Validate the reservoir simulator: replay the actual 2023 releases and check that it reproduces the observed levels.
- Rerun 2023 closed-loop, with forecasts as issued and the actual starting level, under four comparators with identical inputs and constraints:
  - actual operation;
  - the current rule, simulated;
  - a simple forecast-informed rule;
  - a perfect-foresight optimum, as an upper bound only.
- Report full time series and the following outcomes: peak outflow, maximum level, flood storage used, downstream control-point peaks and timing, constraint violations, and end storage.
- Do the mass-balance check above with the real storage and capacity figures.

**B. Test on many floods.**
- Leave-one-flood-out (or leave-one-year-out) testing over all significant floods in 2010–2023, with no tuning on the held-out event.
- Compare the model with the simulated current rule event by event. Do not rely on averages, which hide bad events.

**C. Stress and safety tests.** These are the most important for a flood rule.
- Design floods scaled to the 100-year flood, the design flood, the check flood, and the probable maximum flood where it applies, with several hydrograph shapes and closely spaced successive floods.
- High starting levels.
- Realistic forecast errors, and also missed and false flood forecasts.
- Missing or late inputs and level-sensor error.
- One gate out of service.
- For every case, check that the maximum level stays within the limits set for the dam. Check that the model never pushes releases above the safe downstream capacity when the current rule would not. Check that it does not create man-made downstream rises above what the natural flood would have produced.

**D. Explain how it works.**
- Identify how the model obtains its benefit: earlier pre-release, holding more water, or smoothing the hydrograph.
- Check that operators and the dam-safety authority can understand and challenge its recommendations.
- If the benefit comes from a simple mechanism, such as earlier pre-release when a reliable forecast shows a large flood, a transparent rule built on that mechanism may give most of the benefit with less risk. That would be easier to approve.

**E. Operational readiness.**
- A real-time data pipeline, with latency and missing-data handling.
- Model version control and change control.
- Logging of every recommendation for audit.
- Cybersecurity and compute redundancy.
- A user interface for duty operators.
- Training for operators.

## Preparations and the adoption path

1. **Next flood season: shadow operation only.** The current rule governs. The model runs in parallel and its recommendations are logged next to the actual decisions and outcomes. Comparisons are reviewed after each event.
2. **Agree acceptance criteria in advance** with the dam-safety and flood-control authorities, before the results are known. A provisional set:
   - zero violations of hard limits (maximum levels, discharge capacity, ramping, safe downstream flow) in all historical and stress cases;
   - maximum level and downstream peaks no worse than under the simulated current rule in any tested event, judged by the worst case and not the average;
   - a consistent benefit across most held-out events;
   - safe behaviour when inputs fail.
3. **If the criteria are met: adopt in stages, not as a replacement.** First use the model as decision support inside the current rule's allowed envelope, with hard safety limits that always override it. Then, if justified, formally revise the operating rule or manual. That revision goes through the normal review and approval channel for the dam's operating rules and annual flood-control plan, with downstream agencies consulted. The current rule remains the legal basis until approval.
4. **Reversion rules.** Decide in advance what sends operation back to the current rule:
   - forecast missing, late, or diverging from observations beyond a set threshold;
   - the model recommending an action outside the envelope;
   - an equipment failure;
   - inflow beyond the range in which the model was tested.

   Name who decides, and log every reversion.
5. **Communication.** Brief downstream emergency services, other reservoir operators in the basin, and the public warning chain on any change in how releases are decided, especially if pre-releases become more frequent.
6. **After each event,** review the model's recommendations against what happened, and retrain or revise only under version control and with re-testing.

## Assumptions and what would change this advice

**Assumptions.** I assume the current rule is approved and has been operated without a major failure. I assume the paper reports only what the question states. I assume the 2010–2022 record contains only a handful of large floods. The illustrative numbers above are assumptions, not facts about this reservoir.

**What would move toward adoption:**
- The audit confirms the 2023 result with forecasts as issued and a closed-loop simulation.
- The extra storage was available without exceeding level limits.
- Held-out tests show consistent improvement.
- Stress tests show no worse safety than the current rule.

In that case, a decision-support role could begin the season after next, with a formal rule revision afterwards.

**What would end or shrink the proposal:**
- The result depended on observed future inflows.
- It raised the maximum reservoir level or downstream peaks.
- It fails stress tests beyond the training range.

In those cases the model should at most be treated as a research tool. The lesson from 2023 (for example, release earlier when reliable forecasts show a large flood) could instead be brought into a transparent revision of the current rule.
