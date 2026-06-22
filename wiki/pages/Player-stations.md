<!-- Hand-written mechanics page. Sourced from tradingmanager.lua (settings, tax, stock, policies, offline sim, population profit) and productions.lua (cost formulas). -->
# Player stations

**Player stations** are stations owned by you or your alliance. They let you run your own production, trade and
services: a station can **buy** goods from passing traders and players, **sell** goods it stocks or produces,
consume goods for passive profit, and collect **tax** on trades made there. This page covers founding stations
and the settings that control how they trade. For the underlying price math see
**[Trading and Prices](Trading-and-Prices)**.

> **In short:** owning a station turns trade into **passive income** — even while you're away, it buys, sells,
> consumes goods for profit, and collects **tax** on trades made there. The catch is **upkeep and stock**: a
> factory stalls without its inputs, and a population station only profits while it's stocked with what its
> people consume. Start with a simple producer or a well-stocked trading post in a busy sector.

## Overview

Most stations can be founded by the player, including [factories](Production), trading posts, and population
stations such as habitats and casinos. Once founded, a station you own exposes a **trade configuration** that
lets you set its prices, tax, and trade policies. A station trades using a shared cargo bay: every good it buys
or sells draws from the same cargo space.

## Founding and upgrading

The cost to **found** a [factory](Production) depends on how much value its recipe adds – the difference between
the value of one cycle's outputs and its inputs:

$$\text{cost} = 2{,}500{,}000 + 3500 \times (\text{output value} - \text{input value})$$

with a minimum of **2,500,000** credits. **Upgrading** a factory to a larger size adds byproduct value to the
outputs and scales with the target size:

$$\text{upgrade cost} = 1000 \times \text{size} \times (\text{output value} + \text{byproduct value} - \text{input value})$$

Larger factories process proportionally more goods per cycle. See [Production](Production) for per-recipe build
costs.

## Trade settings

A station you own can be configured with the following settings. Defaults are the values a station starts with.

| Setting | Default | Effect |
|---|---|---|
| **Buy price factor** | 1.0 | Multiplier on the price the station **pays** when buying goods. Lower it to spend less; raise it to attract more sellers. |
| **Sell price factor** | 1.0 | Multiplier on the price the station **charges** when selling goods. Lower it to undercut competitors; raise it for more profit per unit. |
| **Tax** | 0% | Fraction of every transaction paid to you as the station owner. See [Tax](#tax). |
| **Buy from others** | On | Whether the station buys goods from other factions and players (not just your own faction). |
| **Sell to others** | On | Whether the station sells goods to other factions and players. |
| **Relations threshold** | None | A minimum relations level a faction must have to trade here. Below it, trade is refused. |
| **Trade policies** | All off | Whether the station will buy and/or sell **illegal**, **stolen** or **suspicious** goods. See [Trade policies](#trade-policies). |

These factors combine with the regional supply/demand and the trading faction's relations to set the final price
– see [the price formula](Trading-and-Prices#the-price-formula). The buy and sell price factors correspond
directly to the $f_{factor}$ term there.

## Tax

A station can charge a **transaction tax** – a fraction of each trade's value that is paid to the station's
owner, on top of (or instead of) the trade itself. The default for most stations is **0%**. Raising the tax on a
busy station earns passive income from every trade conducted there, though an excessive tax can discourage
traders. Tax collected is reported to the owner and tracked in the station's income statistics.

## Stock and capacity

A station's total cargo space is divided evenly across all the goods it trades, setting the **maximum stock** it
can hold of each good:

$$\text{max stock} = \frac{\text{cargo space} / (\text{goods bought} + \text{goods sold})}{\text{good volume}}$$

The result is rounded to the nearest 100 (when large) and capped at **50,000** units per good. Trading more
distinct goods therefore lowers the cap on each one. Note that current stock level does **not** directly change a
good's price – only regional [supply and demand](Trading-and-Prices#supply-and-demand) does.

## Population profit

A station you own that **buys** goods (such as a habitat, casino or biotope) earns passive income from its
population. Roughly every **2 minutes**, the population consumes a batch of **10–60 units** of one of the goods
the station has in stock and pays you **110%** of the station's buy price for it – a steady **10% profit
margin**. Keeping a [consumer station](Consumer-goods) well stocked turns it into a reliable money-maker on top
of normal trade.

## Trade policies

By default a station refuses to handle **illegal**, **stolen** or **suspicious** goods. You can enable each
policy independently for buying and for selling, allowing (for example) a station to buy stolen goods but not
sell them. Trading contraband can affect relations and attract unwanted attention.

Raw resources (ore and scrap) are **never** traded through the normal menu regardless of settings – they are
processed at resource depots instead. See [Refining](Refining).

## Offline simulation

When a sector containing your station has been **out of view** for a while, the station's stock is re-simulated
on reload rather than tracked continuously. There is **no change** if it was unloaded for under about 10
minutes, and stock drifts toward a fresh randomized level over roughly the next 100 minutes. This means a station
left alone will gradually fill or empty its holds based on what it produces and consumes.

## Income tracking

A station records running totals of the money it has **spent on goods**, **gained from goods**, and **gained
from tax**, so you can see at a glance whether a given station is profitable.

## See also

- [Trading and Prices](Trading-and-Prices) – how station prices are calculated
- [Production](Production) – factory recipes and build costs
- [Consumer goods](Consumer-goods) – what population stations consume, and the profit loop
- [Goods](Goods) – the commodity catalog
- [Refining](Refining) – processing ore and scrap

---
*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods) · [Trade Contracts](Trade-Contracts)*
