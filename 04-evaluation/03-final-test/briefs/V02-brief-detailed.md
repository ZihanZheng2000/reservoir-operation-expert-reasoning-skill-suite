# Problem Brief V02: Real-Time Flood Release Decisions at the Daecheong Reservoir

## 1. Background

The Daecheong multipurpose reservoir lies in the upper Geum River basin, central South Korea. It serves flood control, water supply to contracted users, in-stream flow and hydropower. It was built more than 40 years ago. K-water (Korea Water Resources Public Corporation) sponsors the work and supplies the data.

The upstream Yongdam multipurpose reservoir releases directly into the Daecheong basin. Operators decide Yongdam's releases first, and Yongdam usually releases little during floods, so its planned releases can be treated as known.

Every hour, operators issue a release schedule for the next several hours and carry out only its first step (sometimes a few). What operators want during a flood is not written in regulations but rests on experience. Release optimisation tools are rarely used.

## 2. System characteristics

| Item | Value |
|---|---|
| Flood water level (FWL) | EL. 80.0 m |
| Normal high water level (NHWL) | EL. 76.5 m |
| Low water level (LWL) | EL. 60.0 m |
| Spillway crest level | EL. 64.5 m |
| Total storage | 1,490 × 10⁶ m³ |
| Spillway capacity | 11,680 m³/s (more than 6,000 m³/s already at NHWL) |
| Turbine capacity | 264 m³/s |
| 200-year frequency flood | 10,700 m³/s |

## 3. Current operation and constraints

- **Small flood storage.** At the 200-year inflow, the flood-control storage fills in about 6.5 h. There is no restricted flood-season water level.
- **Levels.** The water level must stay between LWL and FWL.
- **Minimum release.** Total release must meet downstream demand: amounts agreed with water users plus the in-stream flow.
- **Water after the flood.** Enough water must be held to supply contracted users once the event ends.
- **Turbines.** The average hourly flood-season release (2015–2020) is 150 m³/s. Operators prefer turbines to the spillway, to reduce downstream flood risk and earn hydropower revenue.
- **Gates and schedules.** Frequent gate operation causes wear and human error; once gates are open, operators prefer to keep them open until the flood is clearly ending. Sudden schedule changes make conditions harder to predict for downstream flood-control agencies.

## 4. Data available

- Hourly storage and outflow records from K-water (also public on its website). Inflow is not measured but derived from these by water balance, so it already includes evaporation and seepage.
- The reservoir's level–storage relation.
- The Korea Meteorological Agency issues 6-hour quantitative rainfall forecasts every hour, so inflow forecasts are short relative to flood events and uncertain.
- Historical flood events:

| Period | Duration | Peak inflow | Peaks |
|---|---|---|---|
| 2–11 July 2016 | 197 h | 3,655 m³/s | two |
| 25 Aug–7 Sep 2018 | 311 h | 2,590 m³/s | three |
| 1–12 Sep 2020 | 269 h | 4,468 m³/s | one |

Hydrographs for the 200-year flood and the probable maximum flood are not available.

## 5. Research question

The sponsor asks for a decision-support approach that produces hourly release schedules operators would find acceptable. The schedules should:

- keep peak outflow below the inflow peak observed so far and limit spillway use;
- keep water levels safely below FWL while holding enough water for supply after the event;
- avoid abrupt or frequent changes to announced schedules and to gate open/closed states;
- use turbines fully before the spillway.

The approach should be demonstrated on the long, multi-peak events above under forecast uncertainty.
