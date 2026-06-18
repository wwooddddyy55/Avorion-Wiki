<!-- Generated from data/scripts/lib/goodsindex.lua + merchantutility.lua via wiki/tools/_gen_refining.py. Do not hand-edit. -->
# Refining

**Refining** is the process of converting raw **ores** and **scrap** into usable **materials** – the metals
used to build ships and stations. Unlike [goods](Goods), ores and scrap **cannot be sold at stations**; they
must be refined first. Refining is done at a **Resource Depot**, or passively aboard a ship fitted with a
refinery, for a small fee that scales with your relations.

## Overview

Mining asteroids and salvaging wreckage fills your cargo bay with raw ore and scrap. These are dead weight
until refined: the refinery sorts everything in your hold by material type and converts it into the
corresponding refined material, which is then stored as a resource you can spend on building.

Stolen ore is never refined. **Rich** ores (found only in rifts) are kept separate from normal ore because
they yield far more material per unit (see below).

## Materials

There are seven materials, in ascending tier. Higher tiers are found deeper toward the galactic core and are
required for more advanced blocks and equipment. Each material has a standard ore, a rich rift ore, and a
scrap form that all refine into it.

| Tier | Material | Standard ore | Rich rift ore (4×) | Scrap |
|:--:|---|---|---|---|
| 1 | **Iron** | Iron Ore | Rift Iron Ore | Scrap Iron |
| 2 | **Titanium** | Titanium Ore | Rift Titanium Ore | Scrap Titanium |
| 3 | **Naonite** | Naonite Ore | Rift Naonite Ore | Scrap Naonite |
| 4 | **Trinium** | Trinium Ore | Rift Trinium Ore | Scrap Trinium |
| 5 | **Xanion** | Xanion Ore | Rift Xanion Ore | Scrap Xanion |
| 6 | **Ogonite** | Ogonite Ore | Rift Ogonite Ore | Scrap Ogonite |
| 7 | **Avorion** | Avorion Ore | Rift Avorion Ore | Scrap Avorion |

## Ores and scrap

The raw resources below are sorted by material tier. Standard ores and scrap refine 1:1 by material type;
**rich** rift ores yield **4×** as much material as the standard ore of the same metal.

| Resource | Material | Type | Base price | Volume |
|---|---|---|--:|--:|
| Iron Ore | Iron | Standard ore | 2 | 0.025 |
| Rift Iron Ore | Iron | Rich rift ore (4×) | 2 | 0.05 |
| Scrap Iron | Iron | Scrap | 4 | 0.04 |
| Titanium Ore | Titanium | Standard ore | 3 | 0.025 |
| Rift Titanium Ore | Titanium | Rich rift ore (4×) | 3 | 0.05 |
| Scrap Titanium | Titanium | Scrap | 5 | 0.04 |
| Naonite Ore | Naonite | Standard ore | 4 | 0.025 |
| Rift Naonite Ore | Naonite | Rich rift ore (4×) | 4 | 0.05 |
| Scrap Naonite | Naonite | Scrap | 7 | 0.04 |
| Trinium Ore | Trinium | Standard ore | 5 | 0.025 |
| Rift Trinium Ore | Trinium | Rich rift ore (4×) | 5 | 0.05 |
| Scrap Trinium | Trinium | Scrap | 10 | 0.04 |
| Xanion Ore | Xanion | Standard ore | 7 | 0.025 |
| Rift Xanion Ore | Xanion | Rich rift ore (4×) | 7 | 0.05 |
| Scrap Xanion | Xanion | Scrap | 13 | 0.04 |
| Ogonite Ore | Ogonite | Standard ore | 9 | 0.025 |
| Rift Ogonite Ore | Ogonite | Rich rift ore (4×) | 9 | 0.05 |
| Scrap Ogonite | Ogonite | Scrap | 18 | 0.04 |
| Avorion Ore | Avorion | Standard ore | 12 | 0.025 |
| Rift Avorion Ore | Avorion | Rich rift ore (4×) | 12 | 0.05 |
| Scrap Avorion | Avorion | Scrap | 24 | 0.04 |

## Refining fee

Refining at a Resource Depot costs a **fee** taken as a fraction of the refined materials' value. The fee
falls as your relations with the depot's faction improve, and refining at a station owned by your own faction
is **free**. The fee is:

$$\text{fee} = \operatorname{lerp}(\rho,\ -25{,}000,\ +100{,}000,\ 0.10,\ 0.01)$$

where $\rho$ is your relations value, clamped to the range below. In other words the fee runs from **10%**
at hostile relations down to **1%** at maximum relations:

| Relations with the depot's faction | Refine fee |
|---|--:|
| Your own faction / alliance | 0% (free) |
| −25,000 or lower | 10.0% |
| 0 (neutral) | 8.2% |
| +50,000 | 4.6% |
| +100,000 or higher | 1.0% |

## Conversion ratios

> **Note:** The exact amount of material produced per unit of ore or scrap is determined by the game engine
> and is not defined in the moddable script data, so it is not reproduced here. The rules that *are* defined
> in the scripts – which ore refines into which material, the 4× rich-ore yield, and the refine fee – are
> documented above.

## See also

- [Goods](Goods) – tradeable commodities (ore and scrap are listed under Raw resources)
- [Trading and Prices](Trading-and-Prices) – how relations and fees affect other transactions
- [Player stations](Player-stations) – building and operating your own stations

---
*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods) · [Trade Contracts](Trade-Contracts)*
