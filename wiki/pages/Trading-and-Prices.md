<!-- Hand-written mechanics page. Sourced from tradingmanager.lua, factorymap.lua, economyupdater.lua, merchantutility.lua. -->
# Trading and Prices

**Trading** is the act of buying and selling [goods](Goods) at stations for credits. Every good has a fixed
**base price**, but the actual price you pay or receive at a station is modified by three things: the regional
balance of **supply and demand**, your **relations** with the station's faction, and the station's own **price
settings**. This page explains how those modifiers combine into a final price, how stations restock and consume
goods, and how NPC trade ships move cargo around the galaxy.

> **In short:** the same good is worth **different amounts in different sectors** because supply and demand
> are local (±30%). Buy where it's abundant, sell where it's scarce — that gap is your profit. **Good
> relations** earn you better prices (and a discount when buying); **hostile** relations make stations pay
> you less and charge you more. A station's current stock level does **not** move its price — only the
> regional supply/demand balance does.

## Overview

Each station **buys** a set of goods and **sells** a set of goods. You sell cargo to a station at its **buy
price** and purchase cargo from it at its **sell price**. A station will only trade a good if it has stock space
for it, the good is within its trade policies (legal/stolen/suspicious), and your relations are above any
threshold it enforces.

Prices are **local**: the same good can be worth very different amounts in two sectors, because supply and
demand are calculated from the factories, mines and consumers in the surrounding region. Buying where a good is
abundant and selling where it is scarce is the core of trade profit.

### Goods that cannot be traded normally

Stations never buy or sell raw resource items tagged ore or scrap through the normal trade menu – these are
handled by [resource depots](Refining) instead. Illegal, stolen and suspicious goods are only traded by stations
whose policies explicitly allow them.

## Price terms

| Term | Meaning |
|---|---|
| **Base price** | The good's fixed value (see [Goods](Goods)). Any good with a base price of 0 is treated as **500**. |
| **Buy price factor** | A per-station multiplier on the price the station **pays** when buying goods. Default **1.0**. |
| **Sell price factor** | A per-station multiplier on the price the station **charges** when selling goods. Default **1.0**. |
| **Supply & demand factor** | A regional multiplier, ranging **0.70–1.30** of base (±30%). See [Supply and demand](#supply-and-demand). |
| **Relation factor** | A multiplier based on your standing with the station's faction. See [Relations and prices](#relations-and-prices). |
| **Tax** | A fraction of the transaction paid to the station owner. Default **0%**. Owners of player stations can set this. |

## The price formula

*[📷 Screenshot needed — ASSETS.md: images/trading-station-menu.png]*

The final price of a single unit is:

$$\text{price} = \operatorname{round}\left(\text{base price} \times f_{sd} \times f_{rel} \times f_{factor}\right)$$

where $f_{factor}$ is the station's buy or sell price factor, $f_{sd}$ is the supply and demand factor, and
$f_{rel}$ is the relation factor. The supply and demand factor is built from a regional *price change* value
$\Delta_{sd}$:

$$f_{sd} = 1 + \Delta_{sd}$$

with $\Delta_{sd}$ bounded to the range $[-0.30, +0.30]$. Positive $\Delta_{sd}$ (more demand than supply)
raises the price; negative (a glut of supply) lowers it.

## Supply and demand

Supply and demand are computed across a region of **25 sectors** around each sector. The game scans every
factory, mine, consumer and seller in range and adds up their influence on each good. Producers add **supply**
of the goods they output; factories and consumers add **demand** for the goods they need. The net balance
(supply − demand) is converted into the price change $\Delta_{sd}$.

Influence falls off with distance – a factory in the same sector counts for much more than one near the edge of
the 25-sector radius. Consumers and sellers only influence goods within roughly half that radius.

The price change scales with how lopsided the balance is, and is **capped at ±30%**:

| Net imbalance (magnitude) | Price change |
|---|--:|
| 0 | 0% |
| up to 5 | up to ±7.5% |
| up to 12.5 | up to ±12.5% |
| up to 25 | up to ±17.5% |
| up to 50 | up to ±25% |
| up to 75 | up to ±30% |
| 75 or more | ±30% (capped) |

A station does not price against its own output: a factory's own supply or demand contribution is removed (at
1.25× weight) before its prices are calculated.

## Relations and prices

Relation-based pricing applies when trading with **AI faction** stations. Trading with your own faction (or your
alliance) costs nothing through the relation factor.

### When you sell goods to a station

You receive the station's **buy price**. Better relations mean the station pays you more; hostile relations mean
it pays far less.

| Relations with the faction | Relation factor (multiplier on what you're paid) |
|---|---|
| −100,000 to −10,000 | **0.10 → 1.00** (pays as little as 10% of value) |
| −10,000 to +80,000 | **1.00** (no change) |
| +80,000 to +100,000 | **1.00 → 1.05** (up to +5%) |

### When you buy goods from a station

You pay the station's **sell price**. Hostile relations make goods much more expensive; good relations earn you
a small discount.

| Relations with the faction | Relation factor (multiplier on what you pay) |
|---|---|
| −100,000 to −10,000 | **2.00 → 1.00** (up to double price) |
| −10,000 to +80,000 | **1.00** (no change) |
| +80,000 to +100,000 | **1.00 → 0.95** (up to 5% discount) |

Relations outside these ranges are clamped to the nearest value (e.g. relations below −100,000 keep the floor).
Completing trades also improves your relations with the station's faction, scaled by the value of the
transaction.

## Taxes

A station can charge a **transaction tax** – a fraction of each trade paid to the station's owner. For most NPC
stations this is 0%. Owners of [player- or alliance-owned stations](Player-stations) can set a tax to earn
passive income from trades carried out at their station.

## Refining and material prices

Resource depots and refineries use a separate set of factors when handling raw materials:

- **Refine fee** scales from **10% down to 1%** of the refined value as your relations rise from −25,000 to +100,000. Refining at your own faction's station is free. See [Refining](Refining).
- When **buying material** from a station, the price ranges from **1.5× down to 1.05×** as relations improve (and up to **2×** at hostile relations).
- When **selling material** to a station, you receive from **0.75× up to 0.95×** value as relations improve (and as little as **0.5×** at hostile relations).

## Stock and capacity

How much of a good a station can hold (its **max stock**) depends on its total cargo space divided evenly across
the number of goods it trades:

$$\text{max stock} = \frac{\text{cargo space} / (\text{goods bought} + \text{goods sold})}{\text{good volume}}$$

The result is rounded to the nearest 100 (when large) and capped at **50,000** units per good. Note that the
current stock level does **not** directly change a good's price – only the regional supply and demand does.

When a station has been out of view for a while, its stock is re-simulated toward a fresh random level on
reload: there is no change if it was unloaded for under 10 minutes, and a full reset after roughly 110 minutes.

## Consumption and population profit

[Player-owned trading stations](Player-stations) generate passive income from their population. Roughly every
**2 minutes**, the population consumes a batch of **10–60 units** of one of the goods the station buys, and pays
the owner **110%** of the station's buy price for it – a **10% profit margin** on goods the station has stocked.
Stations such as habitats, casinos and biotopes consume the consumer goods listed for their type (see
[Consumer goods](Consumer-goods)).

## NPC trade ships

The galaxy is kept alive by **NPC freighters** that fly between stations to buy and sell goods. A trade ship is
spawned for a station carrying (or coming to collect) a randomized amount of cargo, valued relative to the
richness of the sector, with an occasional high-value run worth several times more.

Trade ships are not spawned in war zones, in sectors where the player controls too many ships, for eradicated
factions, or between factions whose relations are below −40,000.

## See also

- [Goods](Goods) – the full commodity catalog and attributes
- [Production](Production) – factory recipes and yields
- [Refining](Refining) – turning ore and scrap into materials
- [Player stations](Player-stations) – owning and operating your own stations
- [Trade Contracts](Trade-Contracts) – sending captained ships out on automated trade routes

---
*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods) · [Trade Contracts](Trade-Contracts)*
