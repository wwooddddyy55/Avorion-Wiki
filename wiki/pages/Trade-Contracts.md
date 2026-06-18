<!-- Hand-written mechanics page. Sourced from player/background/simulation/tradecommand.lua,
     procurecommand.lua, sellcommand.lua, commandtype.lua, and lib/captainutility.lua. -->
# Trade Contracts

A **trade contract** is a background order you give to one of your own ships, captained by a
**Merchant**, to fly an automated buy-low / sell-high trade route across a region of the galaxy
while it is out of your view. You pay an up-front **down payment** for the captain to buy goods
with, and the ship returns over several flights delivering profit. It is opened from the galaxy
map as the **"Trading Contract"** order and is one of several [fleet orders](#related-fleet-orders).

## Overview

When you assign the order you pick a **region** to operate in (the order analyses every reachable,
revealed sector in that area for profitable routes), choose one of up to **four** suggested trade
routes, and set a **down payment** with a slider. The captain then flies between the cheapest and
most expensive sectors for that good, buying and selling automatically, and pays you the profit
after each round trip (**flight**). The contract ends when the route's available goods are
exhausted, when a rival merchant outbids you, or when you recall the ship.

Only a captain with the **Merchant** class can fly a trade contract — any other class is rejected
with *"I don't know enough about trading."* The ship must also have free cargo space.

## Order attributes

| Attribute | Meaning |
|---|---|
| **Down payment** (deposit) | Credits handed to the captain up front to buy goods with. Set with a slider; minimum is 10% of a flight's purchase cost, maximum is what one full cargo hold can buy. Unspent credits are returned. |
| **Goods Total** | Total quantity of the good available on the route before it is exhausted. Determined by sector richness and a random fluctuation; capped at **25,000** units. |
| **Profit / Flight** | Credits earned per completed round trip, shown as a range. |
| **Flight Time** | Duration of a single round trip (see [formula](#flight-time)). |
| **Flights** | How many round trips are needed to fulfil the whole contract. More flights means more risk of losing the contract. |
| **Attack chance** | Risk the ship is ambushed while away. Rises with the value of the down payment; lowered by assigning escorts. |

The order suggests up to **four** routes at once, picked as: highest single-good profit, highest
profit per cargo volume, highest price margin, and the next-highest profit. Each route line shows
the good's base price, its price margin %, the best buy/sell price deviations found in the area,
the quantity transportable per flight, and the profit per unit.

## How routes are found

The region scan (`factorymap.lua`) reads every factory, mine and consumer in the selected area and
computes, for each good, the **cheapest sector to buy** (largest negative price deviation) and the
**most expensive sector to sell** (largest positive deviation). A route is viable only if buy and
sell sectors differ in price, both are revealed and reachable, and neither is held by a faction
you are **at war** with. Per-unit profit is:

$$\text{profit/unit} = \operatorname{round}\!\big(\text{base price} \times (\Delta_{high} - \Delta_{low})\big)$$

where the deviations are clamped to $\Delta_{low} \ge -0.20$ and $\Delta_{high} \le +0.20$.

## Profit and quantity

Goods carried per flight is the smallest of three limits — the ship's free cargo space, what the
down payment can buy, and what the route has left:

$$\text{per flight} = \min\!\left(\left\lfloor\tfrac{\text{free cargo}}{\text{good volume}}\right\rfloor,\ \left\lfloor\tfrac{\text{deposit}}{\text{buy price}}\right\rfloor,\ \text{goods total}\right)$$

$$\text{flights} = \left\lceil \tfrac{\text{goods total}}{\text{per flight}} \right\rceil
\qquad
\text{profit/flight}_{\max} = \text{per flight} \times (\text{sell price} - \text{buy price})$$

The displayed profit-per-flight range runs from **90%** of that maximum up to the maximum. Each
completed flight pays a random amount in that range (rounded down to a whole multiple of the
quantity carried). On the **final** flight, the unspent **down payment is returned** on top of the
profit. Completing a contract also slightly improves your **relations** with the dominant faction
in the area (15% of a normal trade's relation gain, because the captain did the work).

### Flight time

$$\text{flight time} = \big(720 + 60 \times \text{jumps}\big) \times \text{modifiers} + 300\ \text{seconds}$$

where `jumps` is the route length (straight-line distance × 1.3) divided by the ship's hyperspace
range. Carrying **stolen or illegal** cargo adds a **×1.15** slowdown unless the captain is a
[Smuggler](#captain-class-effects). Captain perks further scale the time.

## Losing the contract

A trade route can only be flown a limited number of times. If a contract needs many flights, the
customer grows impatient and may award the remaining goods to a rival — you still keep the down
payment and the last shipment's profit. From flight **3** onward (while below the maximum), there
is a **35% chance per flight** the contract is handed off early. The order's assessment warns you
in advance based on the projected flight count:

| Projected flights | Risk of losing the contract |
|---|---|
| **≤ 3** | None — *"With so few flights, the customer should not get impatient."* |
| **> 3** | Small chance |
| **> 5** | Likely *(yellow warning)* |
| **> 10** | Very likely; probably can't fulfil it at all *(orange warning)* |

A bigger cargo hold lowers the flight count and therefore the risk.

## Recalling (cancelling) a contract

| When you recall | Outcome |
|---|---|
| Less than ~35% into the first flight, nothing bought yet | **Full down payment returned**; route freed immediately. |
| After buying, but mid-route | Goods delivered to the ship's hold; **remaining deposit returned** (deposit minus what was spent on goods); route unavailable for `min(2h, 20min + 40min × flights)`. |
| Between flights, goods not yet bought | **Full down payment returned**; route unavailable for `min(2h, 40min × flights)`. |

While a contract is active or on cooldown the route is **"depleted"** and unavailable to your other
ships; routes free up again after roughly **2 hours**.

## Captain class effects

The captain must be a **Merchant**. Captain class and perks modify outcomes:

| Class | Effect on trade contracts |
|---|---|
| **Merchant** | Required to run the order. Holds a license for dangerous/suspicious goods. |
| **Smuggler** | Immune to the ×1.15 slowdown for carrying stolen/illegal cargo. |
| **Explorer** | On finishing a contract, marks up to **5** newly discovered sectors on your map. |

Individual perks adjust buy price, sell price (profit), flight time, and ambush risk — for example a
"more profits, buys goods for less" perk improves both ends of the trade.

## Maximising profit

The contract math rewards a few specific choices. In rough order of impact:

### 1. Cargo hold size is the biggest lever
Goods carried per flight is capped by your free cargo space, and the number of flights is
`ceil(goods total ÷ per flight)`. A bigger hold means **more profit per flight** *and* **fewer
flights**, which directly lowers the chance of losing the contract (35% per flight from flight 3
onward). The game even says so when you fail: *"With a larger cargo bay, that could've been us."*
Send your **biggest freighter** with a Merchant captain, not a small ship.

### 2. Max the down payment slider
The down payment is returned (minus what's spent on goods), and pushing the slider to maximum fills
the cargo hold — fewest flights, highest profit per flight. The only cost of a large, valuable run
is a higher **ambush chance**, so on big contracts assign **escorts** rather than under-funding.

### 3. Prefer routes with high profit *per volume*
Of the four suggested routes, the one with the best **profit per cargo unit** lets you carry more
value in the same hold, cutting the flight count and the loss risk. For a size-limited ship,
profit-density beats raw per-unit profit. Aim for projected **flights ≤ 3** (no impatience risk).

### 4. Reveal more sectors before assigning
Routes only form between **revealed sectors that contain stations**, and sectors held by factions
you're **at war with** are skipped. The more of the region you've explored, the more (and better)
routes the scan finds. An **Explorer** captain expands this for free by marking new sectors on
completion.

### 5. Run several ships on different routes
A route is **occupied for ~2 hours** once a contract uses it, locking out your other ships. Spread
contracts across **different goods and regions** instead of stacking one route. Richer (more
central) regions offer a larger **Goods Total** per contract, so pair high-richness areas with your
largest holds.

### 6. Cancel before goods are bought
If you must recall, do it in the **first ~35% of the first flight**, before the captain buys
anything — you get the **full down payment back** and the route frees immediately. Recalling after
purchase forfeits the spent deposit (you get the goods instead) and locks the route for up to 2
hours.

### 7. Match the captain to the cargo
Merchant perks that grant *"more profits / buys goods for less"* widen your margin directly;
*"faster"* perks raise throughput. A **Smuggler** captain avoids the ×1.15 slowdown when hauling
stolen or illegal goods. Completing contracts also nudges your **relations** up with the area's
dominant faction — handy for picking where to operate.

## Related fleet orders

Trade is one of several background simulation orders you can give a captained ship from the galaxy
map. The closest economic siblings:

| Order | What it does |
|---|---|
| **Trade** (this page) | Buys low and sells high on a route within a region. Needs a Merchant captain. |
| **Procure** | A **"Procurement Contract"** — sends the ship to buy a chosen good in the area and bring it back, rather than running a sell route. |
| **Sell** | Sells goods already in the ship's cargo hold at the best stations in the region. |
| **Supply** | Supplies goods to stations in the area. |

Other available orders include **Mine**, **Salvage**, **Refine**, **Scout**, **Expedition**,
**Maintenance**, **Travel**, and **Escort**.

## See also

- [Trading and Prices](Trading-and-Prices) – how station buy/sell prices are calculated
- [Goods](Goods) – the commodity catalog and attributes
- [Production](Production) – factory recipes that create the supply/demand routes feed on
- [Player stations](Player-stations) – owning stations that generate trade

---
*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods) · [Trade Contracts](Trade-Contracts)*
