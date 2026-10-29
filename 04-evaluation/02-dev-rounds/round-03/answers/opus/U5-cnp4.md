# Recommendation: a graduated, coordinated version of (a)

**Preferred alternative (conditional): (a), as a graduated prerelease led by the upper reservoir.** The lower reservoir only raises its release enough to pass the extra upper water without storing it. Both releases stay well below the city's safe flow. Neither reservoir is drawn below its flood-limited level until the next forecast.

The numbers show three things:

- **The real choice is about the upper reservoir.** The lower reservoir will be almost empty of flood water before the flood reaches it, whatever we choose now.
- **Starting the upper prerelease now is the only way to use a gentle release.** After a 12-hour wait, the job needs a larger release and leaves almost no slack if the flood arrives early.
- **Prereleasing water that sits in the flood-control zone costs little.** This holds under the assumption below that the zone is a dedicated flood pool. If that assumption fails, the plan below caps the prerelease.

Option (b) adds almost nothing. Option (c) gives up margin to avoid a cost that is close to zero.

---

## 1. The deciding questions

1. **Can the upper reservoir make enough room before the flood arrives, and what does waiting 12 hours cost?** The upper reservoir is the tight one: 120 million m³ free against a forecast of 150–400.
2. **Can the extra released water pass through the lower reservoir and the city reach without raising city flow toward 6,000 m³/s?** This includes the case where the tributary storm overlaps with it.
3. **What does prereleasing cost if the flood is small or does not come?** This turns on whether the drained storage is a dedicated flood pool or storage that would otherwise be kept as water.

## 2. Key numbers (order of magnitude)

Conversion used: 1 m³/s held for 1 hour = 3,600 m³. So 1,000 m³/s for 1 hour ≈ 3.6 million m³.

**Current state**

| | Upper | Lower |
|---|---:|---:|
| Free flood-control storage | 0.40 × 300 = **120** million m³ | 0.85 × 500 = **425** million m³ |
| Occupied flood-control storage (water above the flood-limited level) | **180** million m³ | **75** million m³ |
| Current net drawdown | 1,500 − 1,200 = 300 m³/s ≈ 1.08 million m³/h | Inflow ≈ 1,500 (upper release from 18 h ago) + 300 (tributary) = 1,800 m³/s; net 2,500 − 1,800 = 700 m³/s ≈ 2.5 million m³/h |

**If nothing changes (the real content of option (c))**

- **Upper:** It gains 1.08 × 30 ≈ 32 million m³ by flood arrival, so it has about 152 million m³ free. That is still below even the low forecast of 150 plus a margin, and well below the central 250.
- **Lower:** It drains 75 million m³ in about 75 / 2.5 ≈ 30 h. So it reaches its flood-limited level at about the time the flood enters the upper reservoir, which is roughly 18 h before upper flood water can reach it.

So **the lower reservoir is already prereleasing in effect, and option (b) gains essentially nothing before the time it matters.** Its own flood space is not the problem: 500 million m³ of free space against a tributary surplus of at most (1,500 − 300) × 48 h ≈ 207 million m³, even if the storm lasts two days.

**Upper prerelease: when must it start? (the point of no return)**

Occupied storage at time t (hours from now) under current releases is 180 − 1.08t million m³. Releasing R m³/s from t to hour 30 removes (R − 1,200) × 0.0036 × (30 − t) million m³.

| Upper release during prerelease | Latest start that still reaches the flood-limited level by hour 30 |
|---|---|
| 3,000 m³/s (net 1,800) | t ≤ 2.7 h, so **now** |
| 4,000 m³/s (net 2,800) | t ≤ 13.6 h, so just after the next forecast and with no slack |
| 5,000 m³/s (net 3,800) | t ≤ about 18 h |

Waiting for the 12-hour forecast therefore turns a 3,000 m³/s prerelease into one of about 3,800–4,000 m³/s. It also removes almost all tolerance for a flood that arrives earlier than "about 30 h".

**The recommended plan by the numbers**

*Upper reservoir*
- Ramp from 1,500 to about 3,000 m³/s over the next few hours. Over 0–12 h the average release is about 2,800, a net of 1,600 m³/s, which drains about 69 million m³. Free space at hour 12 is then about 190 million m³ (63%).
- If the plan is continued at hour 12, 18 more hours at net 1,800 drain about 117 million m³. The reservoir reaches its flood-limited level at about hour 29 and has about 300 million m³ free at flood arrival. That is more than the central forecast and about three-quarters of the upper bound, before counting any release during the flood.

*Lower reservoir*
- Raise from 2,500 to about 3,000 m³/s now. The net is 1,200 m³/s, about 4.3 million m³/h, so it reaches its flood-limited level at about hour 17.
- From about hour 18 the higher upper release arrives, and lower inflow becomes about 3,000 + 300 = 3,300 m³/s. Match it at about 3,300–3,500 m³/s, so the lower reservoir holds 500 million m³ free when the storm and the flood reach it.

*City*
- About 3,000 m³/s from hour 10 and about 3,300–3,500 m³/s from hour 28. That is 55–58% of the safe flow, a margin of about 2,500 m³/s.

**Can the system handle the flood afterwards?**

Flood volume alone is not what threatens the city. The lower reservoir can release up to about 5,000 m³/s, which keeps a margin below 6,000. Over 72 h that passes 5,000 × 0.0036 × 72 ≈ 1,300 million m³, far more than 400 plus about 200 from the tributary.

Suppose the upper reservoir releases about 4,500 m³/s during the flood and the tributary peaks at 1,500. The lower reservoir then stores about 1,000 m³/s (3.6 million m³/h). Its 500 million m³ would last about 140 h, against a 72-hour flood.

The risk to the city therefore comes from three things, not from total volume:
- the **peak** and timing of the upper inflow,
- a **coincidence** of the tributary peak with the arrival of the upper flood release,
- unforecast **local inflow below the lower dam**.

The prerelease is what keeps the upper reservoir's own safety, and the lower reservoir's buffering role, out of trouble if the forecast's high end or a sharp peak occurs.

**Tributary timing, checked in three cases.** The storm that drives the upper flood probably also drives the tributary, so I treat them as correlated, not independent.

| Tributary peak | Timing | Lower inflow | Result |
|---|---|---|---|
| Early | Hours 30–48, overlapping prerelease water still arriving from the upper dam | 3,000 + 1,500 = 4,500 m³/s | The lower reservoir stores the excess over its release; it uses little of its 500 million m³ |
| With the upper flood release | From hour 48 | Upper release + 1,500 | The lower reservoir stores above its release; the upper reservoir should hold its release so that this sum stays near what the lower reservoir can pass (about 4,500 + 1,500) |
| Late, in recession | After the upper flood | — | No conflict |

The plan holds in all three cases. The coincidence case is the one that sets how much the upper reservoir must store rather than pass. That is a further reason to give the upper reservoir its full free space.

## 3. Why not (b) or (c)

| | (a) graduated, upper-led | (b) lower only | (c) wait 12 h |
|---|---|---|---|
| Upper free space at flood arrival (central plan) | about 300 million m³ | about 152 | about 300 only if the release is about 3,800–4,000 from hour 12; less if the flood is early |
| Lower free space when the flood reaches it | about 500 | about 500 | about 495–500 |
| Peak city flow during prerelease | about 3,300–3,500 | about 3,000 | about 4,100 (3,800 + 300 passed through), in hours 40–58, when the tributary storm may coincide |
| Tolerance for a flood that arrives early | Good | Poor at the upper reservoir | Poor: it has spent the window for a gentle release |
| Cost if the flood is small | Water from the flood-control zone only, which should be emptied anyway | Same, smaller | None now |
| Verdict | Preferred | Dominated by (a): it does not treat the upper reservoir, which is the constraint | Acceptable only if the drained storage has real water value (see the cost below) |

**The cost of acting if the flood does not come.** Storage above the flood-limited level should not be held as water outside a flood. Draining it restores the flood-control function and loses no conservation water. The man-made rise at the city is from 2,500 to about 3,000–3,500 m³/s. That is far below 6,000 and below what the forecast flood would produce naturally. So the regret of (a) is small. The regret of (c), if the flood is early or at the high end, is a loss of margin at the upper dam.

## 4. Actions to take now (within the hour)

1. **Upper dam:** ramp the release from 1,500 to about 3,000 m³/s within the permitted ramp rate. Do not go below the flood-limited level. Hold about 3,000 until the next forecast.
2. **Lower dam:** raise the release from 2,500 to about 3,000 m³/s now. Schedule an increase to about 3,300–3,500 m³/s from about hour 16–18, when the higher upper release arrives. Do not go below the flood-limited level.
3. **Interim cap on city flow during prerelease:** about 4,000 m³/s (two-thirds of the safe flow). This leaves room for unforecast local inflow and keeps the man-made rise modest.
4. **Warnings:**
   - The city, emergency services, and river users below the lower dam: flow rising from about 2,500 to about 3,000 m³/s from about hour 10, and to about 3,500 m³/s from about hour 28.
   - Users of the reach between the dams: higher flows from the upper dam beginning within hours.
   - Any other operators on the system.
5. **Monitoring:**
   - Hourly checks of upper inflow, the tributary gauge, and any gauge between the lower dam and the city.
   - Ask the forecasters for an interim update, the inflow hydrograph or at least its peak and timing, and a tributary rainfall forecast. Do not wait passively for the 12-hour issue.
6. **Equipment and staff:** confirm that all gates at both dams are available and that power and operators are in place for a 3–4 day event. Confirm the discharge capacity at the current heads.
7. **Decision record:** headquarters issues the dispatch order. Log the forecast it rests on, the release schedule, the review times (hour 12, hour 24), and the abort rule below.

**Abort rule if the flood arrives early.**
- The upper reservoir switches at once from prerelease to flood-control operation. It stores the peak above the release that the lower reservoir can pass.
- The lower reservoir cuts its release as needed to keep the city at or below the cap. Note that water released in the previous 10 h, about 3,000–3,500 m³/s, is already on its way to the city and cannot be recalled. It is well below 6,000, which is part of why the prerelease rates are kept moderate.

## 5. What would change the recommendation

**Move toward (c), slowing or stopping the upper prerelease:**
- The flood-control storage turns out to be joint-use, so drained water has real supply or power value. Then cap the upper prerelease at the volume the low-side forecast can refill (about 150 million m³), and revisit at hour 12.
- The hour-12 forecast drops the upper bound below about 150 million m³ or delays arrival beyond about 48 h. In that case keep emptying the flood zone at the normal rate, without urgency.
- A downstream or between-dam constraint, such as works in the channel or a lower channel capacity, makes 3,000–3,500 m³/s unsafe.

**Strengthen (a), with an upper release of about 4,000–5,000 and the lower reservoir drained to its flood-limited level faster:**
- The central volume rises above about 300 million m³ or the upper bound above 400.
- Arrival moves earlier than about 24 h.
- The forecast peak inflow at the upper reservoir rises above about 5,000–6,000 m³/s.
- The tributary forecast shows more than about 1,000 m³/s coinciding with the arrival of the upper flood release at the lower reservoir (from about hour 48).

**Shift the burden to the lower reservoir (toward (b)):** this applies only if the upper reservoir cannot raise its release, for example because of gate outages, ramp limits, or the reach between the dams. In that case the lower reservoir's 425–500 million m³ must absorb more, and the city cap should be tightened.

**Hard thresholds, at any time:**
- Forecast city flow above about 5,000 m³/s (about 85% of safe): cut the lower release and store.
- Upper level projected to exceed the top of the flood-control zone under the high-end (400) scenario: raise the upper release earlier, within what the lower reservoir can buffer.

## 6. Assumptions and the most important missing information

**Assumptions**
- Flood-control storage is the zone above the flood-limited level and should be empty outside floods. Drawing it down therefore costs little water.
- No significant local inflow between the lower dam and the city.
- Upper inflow stays about 1,200 m³/s until the flood arrives.
- The 150–400 range is a rough likely range, not a calibrated probability interval.
- The tributary storm is correlated with the upper flood.
- Ramp limits and channel capacity allow 3,000–3,500 m³/s.

**A data inconsistency to resolve.** A total inflow of 250 million m³ over 72 h averages only about 960 m³/s, which is below today's 1,200 m³/s inflow. The 250 figure must therefore be either the flood volume above base flow or a volume measured differently. I treated it as the volume the upper reservoir must handle.

**Missing information that matters most, and its effect:**
1. **Peak and shape of the upper inflow hydrograph.** The same volume can be harmless if it is spread out or tight if it is peaky. This sets how much the upper reservoir must store and whether its 300 million m³ is enough at the high end.
2. **Tributary forecast and timing relative to the arrival of the upper release.** This decides whether the lower reservoir must buffer a coincident peak.
3. **Local inflow below the lower dam.** This directly reduces the 6,000 m³/s allowance and the 10-hour response margin.
4. **Whether the drained storage has water value, plus ramp and channel limits.** This decides how large and how fast the prerelease may be.

The available information is enough for a conditional single choice. The decision to start the upper prerelease now is robust across the forecast range, because the upper free space (120) is below even the low forecast (150). Item 1 mainly changes how strong the plan should be, not whether to act. Item 4, if the storage has real water value, is the one item that could reverse the choice toward (c).

**Approval and record.** The flood-control headquarters authorizes the dispatch under the current flood-control plan or operating manual. The deviation from routine releases, the forecast it rests on, and every revision at each update are logged for review after the event.
