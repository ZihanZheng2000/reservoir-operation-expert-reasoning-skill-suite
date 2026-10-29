# Problem Brief V03: Real-Time Flood Release Decisions at Lishimen Reservoir

## 1. Background

Lishimen Reservoir sits on Shifeng Creek in the Jiaojiang River basin, East China. The Jiaojiang is the third major river in Zhejiang Province. Lishimen is the largest reservoir on Shifeng Creek. Its main purposes are flood control and irrigation, and it also serves water supply and hydropower.

Runoff in the basin comes mainly from rainfall, and runoff and rainfall vary together from year to year and within the year. The area is hit by typhoons. Heavy rainfall is concentrated in time, so floods rise and fall steeply and leave little warning time. They can threaten safety both upstream of the dam and downstream.

## 2. System characteristics

| Item | Value |
|---|---|
| Catchment area above dam | 296 km² |
| Main stream length above dam | 35.2 km |
| Total capacity | 179.3 million m³ |
| Flood control capacity | 35.7 million m³ in the text; 3140 × 10⁴ m³ in the table (sources differ) |
| Flood-limit water level (also the initial level) | 176.04 m |
| Initial storage | 12,180 × 10⁴ m³ |
| Upper flood-control level | 180.69 m (20-year return period) |
| Design flood level | 181.34 m (100-year return period) |
| Lower level limit | 160.97 m |
| Safe downstream discharge | 1000 m³/s |
| Minimum release | 0 m³/s |
| Generation flow | 20.4 m³/s |

## 3. Current operation and constraints

- **Decision step.** Releases are decided hour by hour, during the flood, before the true inflow is known.
- **Downstream limit.** Releases above 1000 m³/s expose the downstream to inundation.
- **Release bounds.** The lower release bound is set by the minimum ecological flow or base generation flow. The upper bound is the maximum discharge capacity of the outlet works at the current level.
- **Ramping.** The change in release between adjacent hours is limited.
- **Forecasts.** Short-term inflow forecasts are not operational yet. Any forecast will carry large errors, and the errors are largest for big floods.

## 4. Data available

- Hourly rainfall from six gauges (Xiatian, Tuoxi, Sixie, Fangqian, Sijiakeng, Lishimen), 1987-2020. Evaporation records are sparse.
- Observed reservoir inflow records. Based on data completeness, 22 flood events are usable. They range from about 5-year floods to nearly 100-year floods; the largest hourly inflow in the set is 2703 m³/s.
- The reservoir's level-storage and level-discharge capacity curves.
- **Test event:** flood No. 20040812, caused by Typhoon Rananim (No. 0413) in 2004. The flood ran from 15:00 on 12 August to 14:00 on 14 August (48 h). It was roughly a 100-year flood, with a basin-average maximum hourly rainfall of 30.8 mm.

The data are confidential.

## 5. Research question

The agency needs a defensible way to set hourly releases before the true inflow is known. The releases should:

- limit the risk of exceeding the upper flood-control level upstream;
- limit the risk of exceeding 1000 m³/s downstream;
- use the flood storage sensibly over the whole event, not so aggressively that the reservoir cannot absorb later inflow, and not so cautiously that storage sits idle.

The agency also wants to know how much forecast error degrades these outcomes, and it wants a defensible way to pick one operating plan.
