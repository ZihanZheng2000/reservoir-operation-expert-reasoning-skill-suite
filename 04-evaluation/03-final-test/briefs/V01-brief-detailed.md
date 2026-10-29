# Problem Brief V01: Flood-Season Water Level Control at the Three Gorges Reservoir

## 1. Background

The Three Gorges Reservoir (TGR) on the upper Yangtze River, China, controls about 1.0 × 10⁶ km², 56% of the Yangtze basin. Its main purposes are flood control and hydropower generation, with navigation and ecology as further considerations. Its main flood-control task is to raise the flood protection standard of the downstream Jingjiang reach to 1-in-100 years.

Under China's Flood Control Act, a reservoir must normally stay at or below its flood limit water level (FLWL) during the flood season. Reservoirs therefore often spill water during the season and have too little left to store once it ends. Holding the level within a range above the FLWL, adjusted in real time using forecasts, is a recognized way to make more use of floodwater.

## 2. System characteristics

| Item | Value |
|---|---|
| Control area | 1.0 × 10⁶ km² |
| Total storage | 393 × 10⁸ m³ |
| Flood protection storage | 221.5 × 10⁸ m³ |
| Design FLWL | 145 m |
| Normal water level | 175 m |
| Check flood level | 180.4 m |
| Downstream safe discharge | 35,000 m³/s (also the maximum navigable flow) |

## 3. Current operation and constraints

- **Flood-season level.** The FLWL may rise only from 145 m to 148 m, and only on the basis of a 3-day forecast. Large volumes are still spilled each year, for example about 500 × 10⁸ m³ in 2020.
- **Release rules.** The rules are graded by inflow. When a forecast shows inflow will exceed 35,000 m³/s while current inflow is still below it, operators release water in advance (pre-release). During the flood itself, the existing flood-control rules apply. On the falling limb, the reservoir may store water again, provided power output and navigation are maintained.
- **Timing.** Gate operation and transmission of information take about 2 hours.
- **Inflow.** Inflow averages about 25,500 m³/s during the falling stage of floods. Local inflow also enters between the dam and the protected reach.
- **Refill.** The basin is water-rich, so failing to refill by the end of the season is not regarded as a practical concern.

## 4. Data available

The Bureau of Hydrology of the Changjiang Water Resources Commission supplies:

- deterministic daily inflow forecasts with lead times of 1 to 7 days, issued daily;
- the matching observed daily inflows;
- the reservoir's level–storage relation and the current operating rules.

Forecast errors grow with lead time. Some forecasts have exceeded 35,000 m³/s when the actual inflow stayed below it.

The test period is the 2019 flood season, 1 June to 23 July. Decisions are made once a day.

## 5. Research question

Longer-lead forecasts could justify holding a higher flood-season level and generating more power, but they are less accurate. The agency needs a defensible, real-time way to decide:

- which lead times can be trusted on a given day;
- how high the level may be held as a result.

Two risks must be quantified and kept acceptable compared with current 3-day practice:

- **Upstream risk:** the reservoir fails to draw down to 145 m before a flood arrives.
- **Downstream risk:** releases exceed 35,000 m³/s.

The option chosen should also increase hydropower output. The agency wants to know how the answer changes with the level of risk it is willing to accept.
