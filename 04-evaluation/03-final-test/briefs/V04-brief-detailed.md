# Problem Brief V04: Joint Flood Operation of the Guxian and Luhun Reservoirs

## 1. Background

The Yiluo River Basin (18,563 km2) is a tributary basin in the lower reaches of the Yellow River, China. It is crucial for flood control at the Huayuankou section, a key control point on the lower Yellow River. Two large reservoirs operate in parallel: Guxian on the Luohe River and Luhun on the Yihe River. Both serve flood control, hydropower generation and water supply. The two rivers join above the Heishiguan hydrological station, the first station below the confluence and the downstream flood control point.

## 2. System characteristics

| Item | Guxian | Luhun |
|---|---|---|
| River | Luohe | Yihe |
| Reservoir class | Large type-I | Large type-I |
| Flood control storage | > 1 billion m3 | > 1 billion m3 |
| Upstream forecast station | Lushi | Dongwan |

Flow at Heishiguan is the sum of both releases after they travel down their rivers, plus local inflow entering between the dams and the station.

## 3. Current operation and constraints

- **Planning practice.** Operators plan joint releases from a single forecast hydrograph for each reservoir.
- **Decision step.** Releases are set on a 6-hour step.
- **Start and end levels.** Each reservoir starts the event at its flood-limit level and should return to it, within a small tolerance, by the end of the event.
- **Release limits.** Each release is limited by the reservoir's release capacity at the current water level, and release changes between adjacent periods are limited.
- **Drawdown limit.** The water level may not fall more than 3 m below the flood-limit level.

## 4. Data available

- Hourly observed flood records from the Hydrological Yearbook of the Yellow River Basin (Ministry of Water Resources). Original series were interpolated linearly to an hourly step.
- Deterministic inflow forecasts for each reservoir, taken from its upstream station. They come from a deep-learning forecast model trained on flood data from 2013 to 2020, with 2021 precipitation as the forecast basis. Its average NSE is above 0.95.
- An archive of past forecasts paired with observations at Lushi, which shows how forecast errors behaved. Most recorded flows are below 500 m3/s, and flows above 1000 m3/s are rare.
- Reservoir characteristics: level-storage relations, release capacities and flood-limit levels.
- A design event, the flood of 18 September 2021, one of the largest in the basin in the past decade. Peak inflow was 2430 m3/s at Guxian (total volume 252793215 m3) and 2722 m3/s at Luhun (total volume 154162635 m3). The Guxian peak came about 20 h before the Luhun peak. It came mainly from the upstream basins, so the reservoirs could regulate it, and it is large enough that reservoir safety conflicts with downstream protection.

## 5. Research question

The agency wants to know three things:

1. How much does forecast error, especially during large floods, change the reservoir water levels that should be expected?
2. Do the usual simple assumptions about forecast error understate this risk?
3. How should releases from the two reservoirs be coordinated, on the 6-hour step, so that the Heishiguan peak stays low while each dam stays safe and returns to its flood-limit level by the end of the event?

The agency also needs a defensible way to pick one from the competing options.
