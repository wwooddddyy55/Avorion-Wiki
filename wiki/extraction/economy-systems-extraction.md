# Avorion Economy & Trading — Technical Extraction (Raw Facts Database)

> **Purpose:** line-accurate dissection of the economy/trading Lua source for later wiki authoring.
> Every formula/claim cites `file:line`. This is a facts dump, not a guide.

## Conventions & Legend

- **`file:line`** — citation into the source tree under `data/scripts/`.
- **LaTeX** is rendered outside code blocks (per request); raw Lua appears in fenced blocks.
- **[ENGINE]** marks a symbol *not* defined in these 16 files — it is a C++/engine binding or lives in an
  unprovided script. Search the binaries / entity scripts for the exact name given.
- The shared interpolation helper is `lerp` (`lib/utility.lua:4`):

```lua
function lerp(factor, lowerBound, upperBound, lowerValue, upperValue, allowOverstepping)
```

It returns `lowerValue + (upperValue - lowerValue) * t` where, unless `allowOverstepping` is truthy,
`t` is **clamped** to `[0,1]`. Mathematically, with clamping (the default):

$$\operatorname{lerp}(f, a, b, v_a, v_b) = v_a + (v_b - v_a)\cdot \operatorname{clamp}\!\left(\frac{f-a}{b-a},\,0,\,1\right)$$

**Consequence:** every relation/supply price factor below saturates flat at its end-points (e.g. relations
worse than −100000 keep the floor value; better than +100000 keep the ceiling value).

### Files covered

| File | Role (as found in code) |
|---|---|
| `lib/goodsindex.lua` | Auto-generated master good table (`goods[name] = {...}`) |
| `lib/goods.lua` | Good ↔ engine-object conversion, spawn-list partitioning |
| `lib/productionsindex.lua` | Auto-generated recipe table (`productions[]`) |
| `lib/productions.lua` | Recipe indexing, mine detection, factory cost math |
| `lib/consumergoods.lua` | Per-station-type *lists* of consumed goods |
| `lib/refineutility.lua` | Gathers ore/scrap cargo amounts per material |
| `lib/tradingmanager.lua` | Commodity trade: pricing, transactions, tax, restock, consumption |
| `lib/tradingutility.lua` | Trade helpers, NPC trader spawning |
| `lib/factorymap.lua` | **Regional supply/demand engine** + factory prediction |
| `sector/background/economyupdater.lua` | Per-sector economy tick / async refresh |
| `lib/merchantutility.lua` | Material order price factors, refine tax, transaction tax payout |
| `lib/inventoryitemprice.lua` | Turret/fighter/torpedo value formulas |
| `lib/tradeableinventoryitem.lua` | Equipment-item trade wrapper + relation gates |
| `lib/sellabletradinggood.lua` | Cargo-good trade wrapper |
| `lib/shop.lua` | Equipment/turret/upgrade shop (not commodities) |
| `lib/stationextensions.lua` | Procedural station **geometry** (mislabeled in directory) |

> **Headline structural fact:** the supply/demand→price *math* the brief attributes to
> `tradingmanager`/`tradingutility` actually lives in **`factorymap.lua`**. Price resolution crosses three
> files:
> `tradingmanager:getBuyPrice/getSellPrice` → `Sector():invokeFunction("economyupdater.lua","getSupplyDemandPriceChange")`
> → `EconomyUpdater.getSupplyDemandPriceChange` → `FactoryMap:supplyToPriceChange`.

---

# 1. DATA DICTIONARIES & SCHEMAS

## 1.1 Commodity / Good schema

### `goodsindex.lua` — the raw record

The file is auto-generated (`goodsindex.lua:1` "This file was generated automatically with a tool.") and
declares one table literal per good. Representative record (`goodsindex.lua:3`):

```lua
goods["Acid"] = {name="Acid", plural="Acid", description="A tank filled with vitriolic acid.",
  icon="data/textures/icons/acid.png", mesh="data/meshes/trading-goods/acid.obj",
  price=402, size=1, level=3, importance=2, illegal=false, dangerous=false,
  tags={industrial=true}, chains={industrial=true,military=true}, }
```

Every key found in `goodsindex.lua` records:

| Key | Type | Meaning / observed range |
|---|---|---|
| `name` | string | Internal + display key (also the table key) |
| `plural` | string | Plural display form |
| `description` | string | Tooltip text |
| `icon` | string | Texture path |
| `mesh` | string | OBJ path; **`""`** for abstract goods (ores, metals, gases like Gold/Coal/Iron Ore) |
| `price` | number | Base credit value (see §1.2 for the `0 → 500` override) |
| `size` | number | Cargo volume per unit (0.025 ore … 25 Vehicle) |
| `level` | integer or `nil` | Tech/production tier 0–9; **`nil`** for ores, scrap, Slave, Toxic Waste, drugs, Rift Research Data |
| `importance` | integer | Weighting/sort hint; e.g. Energy Cell 43, Water 24, Steel 22, most end-products 0 |
| `illegal` | bool | Contraband flag |
| `dangerous` | bool | e.g. Explosive Charge, Fluorine, Gun, Rocket, Tesla Coils, Toxic Waste, War Robot |
| `tags` | table\<string,true\> | Category flags (see vocabulary below) |
| `chains` | table\<string,true\> | Production-chain membership (see vocabulary below) |

**`tags` vocabulary** (observed across `goodsindex.lua`): `basic, industrial, military, technology, consumer,
ore, scrap, rich, rift, iron, titanium, naonite, trinium, xanion, ogonite, avorion, mission_relevant, rare`.
- `ore` + material tag (`iron`/`titanium`/…/`avorion`) = refinable ore (e.g. `Iron Ore` line 68).
- `scrap` + material tag = refinable scrap (e.g. `Scrap Iron` line 120).
- `rich` + `rift` = rift ores; description states **"Yields 4x as much"** (e.g. `Rift Iron Ore` line 109) — the
  4× is text only; conversion happens [ENGINE]-side (see §3.1).

**`chains` vocabulary:** `basic, consumer, industrial, military, technology`. A good can belong to multiple
chains (e.g. `Aluminum` line 6 is in all five).

**Keys NOT present in `goodsindex.lua`** but added at runtime (see §1.1 next): `suspicious`, `stolen`, `color`.

### `goods.lua` — conversion + runtime augmentation

`tableToGood(s)` (`goods.lua:4-13`) builds the engine object and sets the extra flags:

```lua
local g = TradingGood(s.name, s.plural, s.description, s.icon, s.price, s.size)  -- [ENGINE] TradingGood ctor
g.mesh = s.mesh or ""
g.illegal = s.illegal or false
g.suspicious = s.suspicious or false   -- not in goodsindex; defaults false
g.stolen = s.stolen or false           -- not in goodsindex; defaults false
g.dangerous = s.dangerous or false
g.tags = s.tags or {}
```

`goodToTable(g)` (`goods.lua:15-31`) is the inverse and includes `illegal, stolen, suspicious, dangerous, tags`.

The build loop (`goods.lua:33-46`):
- **Zero-price override:** `if good.price == 0 then good.price = 500 end` (`goods.lua:35-37`).
- Attaches the converter as a method: `good.good = tableToGood` (`goods.lua:39`) — so `goods[name]:good()`
  yields the [ENGINE] `TradingGood`.
- **Back-compat aliases:** `goods["Silicium"] = goods["Silicon"]`, `goods["Aluminium"] = goods["Aluminum"]`
  (`goods.lua:43-44`).
- Sorts `goodsArray` by name.

**Spawn-list partitioning** (`goods.lua:53-72`): goods tagged `trinium/xanion/ogonite/avorion` are excluded
from `spawnableGoods`. Within the rest:
- `legalSpawnableGoods` = not `illegal`.
- `uncomplicatedSpawnableGoods` = not `suspicious` **and** not `illegal` **and** not `dangerous` **and** not `stolen`.
- `illegalSpawnableGoods` = `illegal` (built regardless of the material exclusion).

Accessors: `getGoodAttribute(name, attribute)` (`goods.lua:75-78`); `getTranslatedGoodName(name)` returns
`good:good():displayName(1)` (`goods.lua:80-83`, `displayName` is [ENGINE]).

## 1.2 Production / Recipe schema

### `productionsindex.lua` — the raw recipe records

Auto-generated (`productionsindex.lua:1`). Each entry (example `productionsindex.lua:14`):

```lua
table.insert(productions, {factory="${good} Refinery ${size}", factoryStyle="Factory",
  ingredients={{name="Energy Cell", amount=5, optional=0}, {name="Raw Oil", amount=10, optional=0}},
  results={{name="Oil", amount=5}}, garbages={}})
```

Schema:

| Key | Type | Notes |
|---|---|---|
| `factory` | string | Name template with `${good}` / `${size}` placeholders |
| `factoryStyle` | string | One of `Mine`, `Collector`, `Factory`, `SolarPowerPlant`, `Farm`, `Ranch` (observed) |
| `ingredients` | array | `{name, amount, optional}` — `optional` is `0` (required) or `1` (optional; e.g. Energy Cell) |
| `results` | array | `{name, amount}` — primary outputs |
| `garbages` | array | `{name, amount}` — byproducts (e.g. `Toxic Waste`, `Scrap Metal`, `Oxygen`) |

Notable recipe facts (for wiki tables):
- **Pure extractors** (no ingredients): Mines, Gas Collectors, Solar Power Plant (`Energy Cell` ×25,
  `productionsindex.lua:23`), Ice Mine (`Water` ×75, line 22), Crystal Farm, Scrap Trader (`Scrap Metal` ×60).
- **Multi-output** recipes exist: Chemical Factory → 5 outputs (line 46); Ammunition Factory → S/M/L (line 73);
  Accelerator Factory → Neutron/Proton/Electron (line 71); Tesla Coil Factory → Military+Industrial (line 80).
- **Garbage** examples: Rubber → Toxic Waste + Acid (line 32); Fuel → Toxic Waste (line 44); many
  Farms emit `Oxygen` as garbage (lines 96-107).

### `productions.lua` — indexing + derived data

On load (`productions.lua:38-58`):
- `production.index = i` assigned to every recipe.
- **Mine detection** (`productions.lua:41-45`):
  ```lua
  if (string.match(production.factory, " Mine") and not string.match(production.factory, "Mineral"))
          or string.match(production.factory, "Oil Rig") then
      production.mine = true
  end
  ```
- Builds `productionsByGood[result.name]` → list of producing recipes.
- `getMiningProductions()` (`productions.lua:60-77`) collects `mine`-flagged recipes, sorted by `index`
  (explicitly "to make it deterministic").

**Factory placement cost** (`productions.lua:79-100`):

Let $I=\sum_k \text{price}(\text{ingredient}_k)\cdot \text{amount}_k$ and
$R=\sum_k \text{price}(\text{result}_k)\cdot \text{amount}_k$, $\;\text{diff}=R-I$. Then

$$\text{cost} = 2\,500\,000 + \text{diff}\times 3500$$

(2.5M hard floor; `productions.lua:97-99`).

**Factory upgrade cost** (`productions.lua:102-127`): identical $I$/$R$ sums **plus garbages added to $R$**
(`productions.lua:118-121`), then

$$\text{upgradeCost} = \text{diff}\times 1000 \times \text{size}$$

Name formatting: `formatFactoryName(production, size)` / `getTranslatedFactoryName` (`productions.lua:7-36`) fill
`${good}`, `${plural}`, `${prefix}`, `${size}` from the first result's good.

---

# 2. THE MATHEMATICAL PRICE ENGINE

## 2.1 Price factors (`tradingmanager.lua`)

Defaults set in the constructor (`tradingmanager.lua:22-33`):

| Field | Default | Role |
|---|---|---|
| `buyPriceFactor` | `1` | Multiplier on price the station *pays* to buy goods |
| `sellPriceFactor` | `1` | Multiplier on price the station *charges* to sell goods |
| `tax` | `0.0` | Fraction of each transaction paid to the entity owner |
| `factionPaymentFactor` | `1.0` | Fraction of price the owner actually pays/receives directly |
| `supplyDemandInfluence` | `1.0` | Scales the supply/demand price swing |
| `stockInfluence` | `1.0` | Stored & synced but **never read in price math** (see §5.2) |
| `minimumCargoBay` | `25000` | — |

Setters: `setBuyPriceFactor` / `setSellPriceFactor` (`tradingmanager.lua:99-105`). Persisted in
`secureTradingGoods`/`restoreTradingGoods` (`tradingmanager.lua:158-229`) and pushed to clients in
`sendGoods`/`receiveGoods` (`tradingmanager.lua:366-397`). Exposed on the shop API as
`getBuyPriceFactor`/`setBuyPriceFactor`/… (`tradingmanager.lua:1951-1954`).

## 2.2 Final price composition

Both `getBuyPrice` (`tradingmanager.lua:1493-1563`) and `getSellPrice` (`tradingmanager.lua:1566-1614`)
produce price the same way:

$$\text{price} = \operatorname{round}\big(\text{good.price}\times f_{sd}\times f_{rel}\times f_{factor}\big)$$

where $f_{factor}$ is `buyPriceFactor` (buy) or `sellPriceFactor` (sell), and the reported `basePrice` is
$\operatorname{round}(\text{good.price}\times f_{factor})$. The supply/demand factor (`tradingmanager.lua:1556-1557`,
`1607-1608`):

$$f_{sd} = 1 + \big(\Delta_{sd}\times \text{supplyDemandInfluence}\big)$$

with $\Delta_{sd}$ returned by `economyupdater.lua::getSupplyDemandPriceChange` (the cross-file call at
`tradingmanager.lua:1551` / `:1602`; `[ENGINE]`-style call via `Sector():invokeFunction`). Each function
returns the tuple `price, basePrice, supplyDemandFactor, relationFactor, priceFactor`.

## 2.3 Supply & demand curve (`factorymap.lua:71-84`)

```lua
function FactoryMap:supplyToPriceChange(supply)
    if supply == 0 then return 0 end
    supply = -supply
    if supply < 0 then return -self:supplyToPriceChange(supply) end
    if supply >= 75   then return 0.30 end
    if supply >= 50   then return lerp(supply, 50, 75, 0.25, 0.30) end
    if supply >= 25   then return lerp(supply, 25, 50, 0.175, 0.25) end
    if supply >= 12.5 then return lerp(supply, 12.5, 25, 0.125, 0.175) end
    if supply >= 5    then return lerp(supply, 5, 12.5, 0.075, 0.125) end
    return lerp(supply, 0, 5, 0.05, 0.075)
end
```

The input is the regional **`sum`** (supply − demand). The `supply = -supply` line inverts sign, so the price
change rises when **demand exceeds supply** (negative sum → positive Δ → higher price) and falls when supply
dominates. The function is **odd** (negation branch). Writing $s$ for the (post-negation) magnitude, the
returned Δ for the supply-shortage side is piecewise-linear and **capped at 0.30**:

$$\Delta(s)=\begin{cases}
\operatorname{lerp}(s,0,5,0.05,0.075) & 0 \le s < 5\\[2pt]
\operatorname{lerp}(s,5,12.5,0.075,0.125) & 5 \le s < 12.5\\[2pt]
\operatorname{lerp}(s,12.5,25,0.125,0.175) & 12.5 \le s < 25\\[2pt]
\operatorname{lerp}(s,25,50,0.175,0.25) & 25 \le s < 50\\[2pt]
\operatorname{lerp}(s,50,75,0.25,0.30) & 50 \le s < 75\\[2pt]
0.30 & s \ge 75
\end{cases}$$

and $\Delta(-s) = -\Delta(s)$, $\Delta(0)=0$.

## 2.4 How the regional `sum` is built (`factorymap.lua`)

`SupplyType` enum (`factorymap.lua:43-50`): `FactorySupply=1, FactoryDemand=2, FactoryGarbage=3,
Consumer=4, Seller=5`.

`SupplyInfluence` weights (`factorymap.lua:52-57`):

$$w_{\text{FactorySupply}}=10,\quad w_{\text{FactoryDemand}}=-10,\quad w_{\text{FactoryGarbage}}=4,\quad
w_{\text{Consumer}}=-3,\quad w_{\text{Seller}}=3$$

`influenceRadius = 25` sectors (`factorymap.lua:41`). In `getSupplyAndDemand` (`factorymap.lua:227-304`),
with $r=25$, $r^2=625$, and `consumerRadius2 = r^2·0.25 = 156.25`:

**Distance weight** for factories (`factorymap.lua:249-253`), using $d$ = euclidean sector distance:

$$\text{factor}(d)=\begin{cases}
\operatorname{lerp}(d,\,0,\,0.85r,\,1.25,\,0.4) & d < 0.85r\;(=21.25)\\[2pt]
\operatorname{lerp}(d,\,0.85r,\,r,\,0.4,\,0.1) & 0.85r \le d \le r
\end{cases}$$

**Consumer/seller distance weight** (only when $d^2 \le 156.25$, `factorymap.lua:272-273`):

$$\text{factor}_c(d)=\operatorname{lerp}(d,\,0,\,0.5r,\,1.0,\,0.0)$$

Accumulation per good (`factorymap.lua:256-289`):
- Factory **ingredients** with `optional==0`: `demand += -w_FactoryDemand · factor = +10·factor`.
- Factory **results**: `supply += w_FactorySupply · factor = +10·factor`.
- Factory **garbages**: `supply += w_FactoryGarbage · factor = +4·factor`.
- **Consumptions**: `demand += -w_Consumer · factor_c = +3·factor_c`.
- **Sold** goods: `supply += w_Seller · factor_c = +3·factor_c`.

Final (`factorymap.lua:295-301`): `sum[good] = supply[good] − demand[good]`.

`EconomyUpdater.getSupplyDemandPriceChange(good, ownSupplyType)` (`economyupdater.lua:134-152`) removes the
station's *own* contribution before pricing:

```lua
local influence = self.map.SupplyInfluence[ownSupplyType] or 0
if ownSupplyType == FactorySupply or ownSupplyType == FactoryDemand then influence = influence * 1.25 end
sum = sum - influence
return self.map:supplyToPriceChange(sum)
```

i.e. a factory's own supply/demand is subtracted at **1.25×** its base influence so a station doesn't price
against itself.

## 2.5 Absolute caps & floors

- **Supply/demand swing:** $\Delta_{sd}\in[-0.30,\,0.30]$ (§2.3 cap). With `supplyDemandInfluence = 1.0`,
  $f_{sd}\in[0.70,\,1.30]$ — i.e. ±30% of base. (Scales linearly with `supplyDemandInfluence`.)
- **Relation factor, buying from others** (`getBuyPrice`, `tradingmanager.lua:1532-1545`):
  $$f_{rel}=\begin{cases}
  \operatorname{lerp}(\rho,-100000,-10000,0.1,1.0) & \rho < -10000\\
  1.0 & -10000 \le \rho < 80000\\
  \operatorname{lerp}(\rho,80000,100000,1.0,1.05) & \rho \ge 80000
  \end{cases}$$
  → range **[0.10, 1.05]**; if the seller *is* the station faction, $f_{rel}=0$ (`:1545`). Only applied when
  `Faction().isAIFaction` (`:1532`).
- **Relation factor, selling to others** (`getSellPrice`, `tradingmanager.lua:1584-1596`):
  $$f_{rel}=\begin{cases}
  \operatorname{lerp}(\rho,-100000,-10000,2.0,1.0) & \rho < -10000\\
  1.0 & -10000 \le \rho \le 80000\\
  \operatorname{lerp}(\rho,80000,100000,1.0,0.95) & \rho > 80000
  \end{cases}$$
  → range **[0.95, 2.0]**; self-faction → 0 (`:1596`).
- **Free-for-owner buy path** (`tradingmanager.lua:1500-1516`): if `factionPaymentFactor == 0`, buying from
  the station's own faction / its alliance members / a player owner in the buyer's alliance returns price `0`.
- Because `lerp` clamps (§Legend), all the above saturate flat beyond their endpoints.

> **No per-station stock-ratio term.** Neither `getBuyPrice` nor `getSellPrice` references `getStock`,
> `getMaxStock`, or `stockInfluence`. Price depends only on `good.price`, the **regional** supply/demand
> (`factorymap`), relations, and the manual factors. The brief's "stock vs max-stock price curve" does **not**
> exist in this code path (see §5.2 quirks).

## 2.6 Taxes & money flow

`transferMoney(owner, from, to, price, ...)` (`tradingmanager.lua:895-920`):
- `ownerMoney = price * factionPaymentFactor` (`:898`).
- Three branches by who the owner is (`:900-911`): owner-as-payer pays `ownerMoney`/receiver gets `price`;
  owner-as-receiver pays `price`/receives `ownerMoney`; neither → both move full `price`.
- Tax payout: `receiveTransactionTax(Entity(), price * self.tax)` (`:913`); logged
  `moneyGainedFromTax += round(price * tax)` (`:916-918`).

`receiveTransactionTax(station, amount)` (`merchantutility.lua:6-22`): rounds `amount`, looks up
`Faction(station.factionIndex)`, and calls `stationOwner:receive(msg, amount)` ([ENGINE] `Faction:receive`).
`factionReceiveTransactionTax` (`merchantutility.lua:24-39`) is the faction-direct variant.

**Material-order price factors** (used by resource/material trading, `merchantutility.lua`):
- `getMaterialBuyingPriceFactor` (`:55-77`): self/alliance → 1; else
  $\rho\ge 0:\operatorname{lerp}(\rho,0,100000,1.5,1.05)$; $\rho<0:\operatorname{lerp}(\rho,-10000,0,2,1.5)$.
- `getMaterialSellingPriceFactor` (`:79-100`): self/alliance → 1; else
  $\rho\ge 0:\operatorname{lerp}(\rho,0,100000,0.75,0.95)$; $\rho<0:\operatorname{lerp}(\rho,-10000,0,0.5,0.75)$.
- **Refine tax** `getRefineTaxFactor(stationFactionIndex, customerFaction)` (`:102-105`): self → 0; else
  $$\text{refineTax}=\operatorname{lerp}(\rho,-25000,100000,0.1,0.01)$$
  i.e. **10% → 1%** of value as you go from −25000 to +100000 relations.

**Relation gains on trade:** both buy and sell paths call
`relationsChange = GetRelationChangeFromMoney(price)` ([ENGINE]) then `changeRelations(...)`
(`tradingmanager.lua:1050-1055, 1155-1160, 1203-1204, 1242-1243`). In the player ship-trade paths the change
is multiplied by **1.5** (`:1052`, `:1157`).

**Trade relation gate:** if `relationsThreshold` is set and
`stationFaction:getRelations(shipFaction.index) < relationsThreshold`, the trade is refused
(`tradingmanager.lua:949-956, 1084-1090`).

## 2.7 Equipment-shop pricing (`shop.lua`)

Distinct from commodity trading; used for turrets/upgrades/usable items.
- `priceRatio` default `1.0` (`shop.lua:28`); UI shows "% OFF" / "+%" when `<1` / `>1` (`:672-677`).
- `getSellPriceAndTax(price, stationFaction, buyerFaction)` (`shop.lua:1756-1768`):
  `price = price * priceRatio`; `taxAmount = round(price * tax)`; if buyer == station faction, `price -=
  taxAmount` and `taxAmount = 0`.
- `getBuyPrice(price, ...)` (shop *buys from* player) `= price * 0.25` (`shop.lua:1770-1773`) — **25% buyback**.
  Code comment: `"must be adjusted in tooltipmaker.lua as well!"`.
- `sellToPlayer` (`shop.lua:1175-1267`): final `price = getSellPriceAndTax(item.price,…) * amount`; special
  offers apply an extra **×0.7** (`:1213`); `receiveTransactionTax(station, price * self.tax)` (`:1241`).
- Special offers: `specialOfferDuration = 20*60 + 1 = 1201s` (`shop.lua:21`); remaining time is
  `duration - (runtime mod duration)` (`:1139-1141`).

## 2.8 Inventory-item value formulas (`inventoryitemprice.lua`)

These compute the *base* `price` of turrets/fighters/torpedoes that then feed §2.7 (via
`tradeableinventoryitem:getPrice` → `round(ArmedObjectPrice(item))`, `tradeableinventoryitem.lua:101-106`).

`ArmedObjectPrice(object)` (`inventoryitemprice.lua:50-100`):

$$\text{base}=\frac{\text{dps}}{0.5+\text{slots}/2}\times 2$$

then sequential additive/multiplicative terms (`:60-95`):
- shield dmg: `+ base·(shieldDamageMultiplier−1)·0.5`; hull dmg: `+ base·(hullDamageMultiplier−1)·0.5`.
- shield penetration: `+ (base·hullDamageMultiplier)·shieldPenetration`.
- stone (mining) dmg: `+ base·hullDamageMultiplier·stoneDamageMultiplier·0.15`.
- repair: `+ hullRepairRate/slots·2.5` and `+ shieldRepairRate/slots·2.5`.
- ForceGun only: `+ holdingForce/7500`.
- reach: `value *= reach · (reachWeights[type] or 1)`.
- efficiency multipliers (`:82-86`):
  $$value \mathrel{*}= 1 + e_{stone}\big(1 + (1.2^{m}-1)\cdot 5\big),\qquad
    value \mathrel{*}= 1 + e_{metal}\big(1 + (1.1^{m}-1)\cdot 3\big)$$
  where $m=$ `material.value`, $e_{stone}=\max(stoneRaw,stoneRefined)$, $e_{metal}=\max(metalRaw,metalRefined)$.
- seeker rockets: `value *= 2`.
- `value = value * valueWeights[type] or 1` (per-WeaponType weights, `:9-33`).
- rarity: `added = max(0, rarity.value·(rarityWeights[type] or 0.1))`; `value += value·added`.
- floor: `value = max(value, 100)`.

`FighterPrice` (`:103-137`) and `TorpedoPrice` (`:139-198`) build on similar terms (size/durability/speed/
maneuver lerps for fighters; damage·reach/15000, penetration ×1.5, EMP flat +15000, etc. for torpedoes), both
with NaN/inf guards and `round(value/100)*100` quantization (fighter floor 1000, torpedo fallback 100000).

## 2.9 Trade wrappers

- `sellabletradinggood.lua` — cargo goods: `getPrice` = `good.price` (`:43-45`); `boughtByPlayer` checks
  `cargoBay.freeSpace ≥ good.size·amount` then `addCargo` (`:59-72`); `soldByPlayer` removes cargo (`:74-87`).
- `tradeableinventoryitem.lua` — equipment: `good = "Energy Cell"` and `goodsPrice = getPrice()` (`:23-24`),
  so some inventory items are **purchased with Energy Cell cargo** rather than credits
  (`boughtByPlayer` consumes `self.goodsPrice` Energy Cells, `:220-256`). `canBeBought` enforces relation/
  rarity gates (no buying during War; Allies buy anything; rarity ≥ Exotic needs allies; military/`WeaponsTrade`
  has stricter Ceasefire/Rare/Exceptional thresholds — `:172-218`).

---

# 3. FACTORY PERFORMANCE & REFINE UTILITY

## 3.1 Refine utility (`refineutility.lua`)

`getAmountsOnShip(craft, tag)` (`refineutility.lua:2-26`): builds a per-material array of length
`NumMaterials()` ([ENGINE]); iterates `craft:getCargos()`, skips `good.stolen`, and for goods with
`tags[tag]` **and not** `tags.rich` distributes the cargo amount into the slot whose material tag matches
(`Material(i-1).tag`, [ENGINE]). Returns `(amountsOnShip, totalAmount)`.

```lua
if tags[tag] and not tags.rich then
    for i = 1, NumMaterials() do
        local material = Material(i - 1)
        if tags[material.tag] then amountsOnShip[i] = amount; totalAmount = totalAmount + amount end
    end
end
```

Wrappers: `getOreAmountsOnShip` = tag `"ore"` (`:28-30`); `getScrapAmountsOnShip` = tag `"scrap"` (`:32-34`).
`getRiftOreAmountsOnShip` (`:36-60`) is separate and requires `tags.ore and tags.rich` (the rich rift ores
the standard functions deliberately exclude).

> **The actual ore→material conversion ratio is NOT in these files.** `refineutility.lua` only *counts* cargo
> by material. The conversion (and the "4× rich" multiplier asserted in rift-ore descriptions, §1.1) is applied
> [ENGINE]-side / in an unprovided refinery entity script. Refine *tax* is `getRefineTaxFactor`
> (`merchantutility.lua:102-105`, §2.6).

## 3.2 Stock capacity (`tradingmanager.lua:1444-1460`)

`getMaxStock(good)` is the per-good capacity cap:

```lua
local space = entity.maxCargoSpace        -- [ENGINE] Entity property
local slots = self.numBought + self.numSold
if slots > 0 then space = space / slots end
if space / good.size > 100 then
    return math.min(50000, round(space / good.size / 100) * 100)   -- rounded to 100, hard cap 50000
else
    return math.floor(space / good.size)
end
```

$$\text{maxStock} = \begin{cases}
\min\!\big(50000,\ \operatorname{round}(\tfrac{S}{100})\times 100\big) & S>100\\
\lfloor S \rfloor & S \le 100
\end{cases},\qquad S=\frac{\text{maxCargoSpace}/(\text{numBought}+\text{numSold})}{\text{good.size}}$$

`getStock(name)` returns `(getNumGoods, getMaxGoods)` (`:1392-1394`); `getNumGoods` reads
`entity:getCargoAmount(good)` ([ENGINE], `:1396-1407`).

## 3.3 Production speed / size scaling

> **Not present in the provided files.** `productions.lua`/`productionsindex.lua` hold only recipe *data* and
> the *money* cost formulas (§1.2). Production tick rate, factory-size output multipliers, and the actual
> craft/consume loop live in the unprovided entity script `data/scripts/entity/merchants/factory.lua` and in
> [ENGINE] (`FactoryPredictor.generateFactoryProductions` / `generateMineProductions`,
> `Balancing_GetSectorRichnessFactor`). Search those names for the speed/size math.

## 3.4 Stall / refusal conditions (commodity side)

Every check (besides "no ingredients", which lives in the [ENGINE] factory loop) that halts or refuses a
commodity transaction in the provided code:

- `isSoldBySelf` / `isBoughtBySelf` (`tradingmanager.lua:108-156`): refuses if good is `illegal`/`stolen`/
  `suspicious` and the matching policy is off; **always** refuses goods tagged `scrap` or `ore`
  ("This station doesn't sell/buy this." `:126-128, :151-153`).
- Stock cap: `buyFromShip`/`buyGoods` clamp to `getMaxStock(good) - getNumGoods(good.name)`; if 0, "not able to
  take any more" (`:980-988, 1184-1187`).
- Cargo space: player-owned stations clamp by `station.freeCargoSpace / good.size` (`:991-997`).
- `relationsThreshold` gate (§2.6).
- Can-pay: `canPay(price * factionPaymentFactor)` (buy, `:1193-1194`) / `otherFaction:canPay(price)`
  (sell, `:1232-1233`) — returns error codes `3`/`2`.
- Function return codes (`buyGoods`/`sellGoods`): `1` not bought/none to sell, `2` amount ≤ 0, `3` can't pay,
  `4` doesn't buy/sell from others or policy block, `5` missing faction, `0` success (`:1168-1251`).
- **Trader-spawn** gates (`tradingutility.lua:217-241`): `war_zone`, `no_trade_zone`, eradicated trading
  faction, or `tradingFaction:getRelations(station.factionIndex) < -40000`.

---

# 4. THE BACKGROUND SECTOR SIMULATION

## 4.1 Economy tick loop (`economyupdater.lua`)

Namespace `EconomyUpdater` with a singleton `self` holding `supply/demand/sum` (`economyupdater.lua:8-15`).
The header comment at `:8-9` warns the `-- namespace EconomyUpdater` line must not be removed.

- **Cadence** `getUpdateInterval` (`:17-23`): on the client, while no data is cached, **5s**; otherwise **300s**
  (5 min) on both sides.
- `initialize` (`:25-36`): server builds the `FactoryMap`, calls `refresh()`, and registers
  `onEntityCreated`; client calls `requestData()`.
- `updateServer(timeStep)` → `refresh()` (`:44-46`); `updateClient` re-requests data if empty (`:38-42`).

**Refresh trace** `refresh()` (`:69-87`):
1. `self.map:refreshCurrentSector()` snapshots local factories/consumers/sellers into a `setGlobal` blob
   (see §4.2).
2. Builds a sandbox Lua **string** that re-includes `factorymap` and defines `run(x,y)` returning
   `map:getSupplyAndDemand(x, y)`.
3. `async("onEconomyRefreshDone", code, x, y)` ([ENGINE]) runs it off-thread.
4. `onEconomyRefreshDone(supply, demand, sum)` (`:99-105`) stores results and
   `broadcastInvokeClientFunction("setData", supply, demand)`.

`immediateRefresh` (`:89-97`) is the synchronous variant. `onEntityCreated(id)` → if a `Station` is created,
`scheduleRefresh()` sets `waitingForRefresh` and schedules `deferredCallback(5, "deferredRefresh")`
(`:48-67`) — coalescing bursts of station spawns into one refresh after 5s.

`setData(supply, demand)` (`:119-132`) rebuilds `self.sum`: `sum[good] = supply[good]`, then for each demand
good `sum[good] = (sum[good] or 0) - demand[good]`.

## 4.2 Computing supply/demand when the player is absent (`factorymap.lua`)

`refreshCurrentSector` (`:144-210`) only works for the *loaded* sector — it queries live entities by script
(`productionScripts = factory.lua`; `consumerScripts = consumer/habitat/biotope/casino.lua`;
`sellerScripts = seller.lua`, with `turretfactoryseller.lua` **commented out**, `:124-137`), invoking
`getProduction` / `getConsumedGoods` / `getSellableGoods` on each, and stores the blob under
`setGlobal(makeKey(x,y))` where key = `"factory_map_<x>_<y>"` (`:140-142, 209`).

For **unloaded** sectors, `getData(x,y)` (`:331-340`) returns the cached global if present, else
`predictData(x,y)` (`:342-359`):
- `SectorSpecifics.determineFastContent(x, y, seed)` ([ENGINE]) decides if a sector is regular/offgrid.
- `sectorSpecifics:initialize(x,y,seed)` then `generationTemplate.contents(x,y)` ([ENGINE]) yields counts.
- `predictProductions` (`:429-451`) uses `FactoryPredictor.generateFactoryProductions` /
  `generateMineProductions` ([ENGINE]).
- `predictConsumptions` (`:361-410`) instantiates `ConsumerGoods.<Type>()` lists once per station of each type
  (habitats, biotopes, casinos, equipmentDocks, shipyards, repairDocks, militaryOutposts, researchStations,
  travelHubs, mines).
- `predictSellers` (`:412-427`) is effectively empty — turret factories are deliberately skipped
  ("massively inflated price and randomized selection", `:419-421`).

`getSupplyAndDemand` then aggregates over all sectors within `±influenceRadius` using the weights/distance
math in §2.4. `getAreaSupplyAndDemand` (`:306-329`) batches this for map overlays.

## 4.3 Consumer station consumption ("population uses up goods")

Two distinct mechanisms:

**(a) `consumergoods.lua` — *what* is consumed, not the rate.** Pure data: one function per station type
returning a flat list of good names: `Habitat` (`:4-23`), `Biotope` (`:25-43`), `Casino` (`:45-56`),
`EquipmentDock`, `Shipyard`, `RepairDock`, `MilitaryOutpost`, `ResearchStation`, `RiftResearchStation`,
`TravelHub`, `Mine`, and `TurretFactory`. `TurretFactory` (`:186-218`) is special: it randomly selects up to
**15 distinct** goods from a weighted pool via `randomEntry(random(), goods)` (up to 25 draws, `:204-209`).

> The **per-tick consumption rate** for NPC habitats/casinos/biotopes lives in the unprovided entity scripts
> (`data/scripts/entity/merchants/{consumer,habitat,casino,biotope}.lua`, named in `tradingutility.lua:14-25`
> and `factorymap.lua:127-132`). `consumergoods.lua` itself deletes nothing.

**(b) `tradingmanager:useUpBoughtGoods` — the player-station "population profit" loop** (`tradingmanager.lua:1322-1370`):

```lua
local tickTime = 120                       -- consumption tick = 120 seconds
self.useTimeCounter = self.useTimeCounter + timeStep
if self.useTimeCounter > tickTime then
    self.useTimeCounter = self.useTimeCounter - tickTime
    for i = 1, 5 do
        local amount = math.random(10, 60)
        local good = self.boughtGoods[math.random(1, #self.boughtGoods)]
        ...
        amount = math.min(inStock, amount)
        self:decreaseGoods(good.name, amount)
        local price = self:getBuyPrice(good.name)
        local received = price * 1.10 * amount         -- population PAYS 110% of buy price
        faction:receive(description, received)         -- profit logged = price * amount * 0.10
        break                                          -- only one good per tick actually fires
    end
end
```

Exact behaviour: every **120s** of station uptime, **one** randomly chosen bought good is consumed in a
random **10–60** unit batch (clamped to stock). The owner is paid
$$\text{received} = \text{buyPrice}\times 1.10 \times \text{amount},$$
i.e. a **10% markup** over the station's own buy price; the chat log explicitly reports the profit as
`price * amount * 0.10`.

> **Discrepancy with the brief:** the brief asks about a "5% profit margin"; the code uses **10%**
> (`1.10` / `0.10`, `:1349, :1358`). There is no 5% figure in these files.

**Stock back-fill on (re)load:** `simulatePassedTime(t)` (`tradingmanager.lua:332-360`) interpolates current
cargo toward a freshly rolled target (`getInitialGoods`) by
$$\text{factor} = \operatorname{clamp}\!\left(\frac{t - 10\cdot 60}{100\cdot 60},\,0,\,1\right)$$
(no change under 10 min absent; full reset after ~110 min). `getInitialGoods` (`:282-330`) rolls
`resourceAmount = random(1,5)` and sets bought/sold stock as random fractions of `getMaxStock` (bought:
`0..0.15·max` if scarce else `0.1..0.5·max`; sold: `0.4..1.0·max` if scarce else `0..0.6·max`), each capped by
`300k`/`500k × Balancing_GetSectorRichnessFactor(...) / price` ([ENGINE], `:302-303, :322-323`).

---

# 5. AUTOMATION & SCRIPT CORRELATIONS

## 5.1 Cross-file call map (exact function names)

- **Price resolution:** `TradingManager:getBuyPrice`/`getSellPrice`
  → `Sector():invokeFunction("economyupdater.lua", "getSupplyDemandPriceChange", goodName, ownSupplyType)`
  (`tradingmanager.lua:1551, 1602`)
  → `EconomyUpdater.getSupplyDemandPriceChange` (`economyupdater.lua:134`)
  → `FactoryMap:supplyToPriceChange` + `FactoryMap.SupplyInfluence` / `.SupplyType` (`economyupdater.lua:142-151`).
- **Economy refresh:** `EconomyUpdater.refresh`/`immediateRefresh` → `FactoryMap:refreshCurrentSector`,
  `FactoryMap:getSupplyAndDemand` (`economyupdater.lua:70-93`).
- **Prediction:** `FactoryMap:predictData` → `SectorSpecifics.determineFastContent` / `generationTemplate.contents`
  [ENGINE]; `FactoryMap:predictProductions` → `FactoryPredictor.generate{Factory,Mine}Productions` [ENGINE];
  `FactoryMap:predictConsumptions` → `ConsumerGoods.<Type>()` (`consumergoods.lua`).
- **Trade discovery:** `TradingUtility.getBuyableAndSellableGoods` calls, per station,
  `station:invokeFunction(script, "getBoughtGoods" | "getSoldGoods" | "getGoodByName" | "getStock" |
  "getBuyPrice" | "getSellPrice")` over `TradingUtility.getTradeableScripts()`
  (`tradingutility.lua:95-179`); the matching server-side implementations are `TradingManager:getBoughtGoods`,
  `getSoldGoods`, `getGoodByName`, `getStock`, `getBuyPrice`, `getSellPrice`.
- **Trader spawning:** `TradingUtility.spawnTrader` → `AsyncShipGenerator:createFreighterShip` [ENGINE] and
  `ship:addScript("merchants/tradeship.lua", …)` (`tradingutility.lua:217-309`); for immediate transactions it
  calls `station:invokeFunction(script, "buyGoods"|"sellGoods", good, amount, factionIndex)`.
- **Shop ↔ items:** `Shop:sellToPlayer`/`buyFromPlayer` → `item:boughtByPlayer`/`soldByPlayer` and
  `item:getRelationChangeType` on the wrappers (`SellableTradingGood` / `TradeableInventoryItem`); pricing via
  `Shop:getSellPriceAndTax`/`getBuyPrice` (`shop.lua:1175-1426, 1756-1773`).
- **Item value:** `TradeableInventoryItem:getPrice` → `ArmedObjectPrice` (`inventoryitemprice.lua`).
- **Tax payout:** `TradingManager:transferMoney` / `Shop:sellToPlayer` → `receiveTransactionTax`
  (`merchantutility.lua`).
- **Good conversion everywhere:** `goods[name]:good()` / `tableToGood` / `goodToTable` (`goods.lua`).

## 5.2 Developer quirks, legacy math & hidden limits

- **Zero-price floor:** any good with `price == 0` is silently bumped to **500** (`goods.lua:35-37`).
- **Legacy aliases:** `Silicium`→`Silicon`, `Aluminium`→`Aluminum` kept "for backwards compatibility"
  (`goods.lua:43-44`).
- **`stockInfluence` is dead in pricing:** declared (`tradingmanager.lua:32`), persisted (`:165, 207`), synced
  to clients (`:368, 384`) — but **never read** by `getBuyPrice`/`getSellPrice`. Stock does not move price.
- **"5%" is actually 10%:** population consumption pays a **10%** markup (`tradingmanager.lua:1349, 1358`).
- **Buyback = 25%:** `Shop:getBuyPrice` returns `price * 0.25` with a comment that the value
  *"must be adjusted in tooltipmaker.lua as well!"* (`shop.lua:1772`) — a manual-sync hazard.
- **Self-influence over-subtraction:** a factory's own supply/demand is removed at **1.25×** influence before
  pricing (`economyupdater.lua:143-146`).
- **±30% supply cap & sign trick:** `supplyToPriceChange` negates its input and is hard-capped at 0.30; the
  odd-function recursion handles the symmetric demand side (`factorymap.lua:71-84`).
- **Turret factories excluded from the economy map:** both the seller-script list (`factorymap.lua:135`) and
  `predictSellers` (`:419-421`) deliberately comment them out due to "massively inflated price and randomized
  selection".
- **`consumerRadius2 = radius2 * 0.25`:** consumers/sellers only influence within half the factory radius
  (`factorymap.lua:235`).
- **High-value transport roll:** `spawnTrader` gives a 20% chance to multiply the cap by `(1 + random()*4)`
  (up to 5×), with base `maxValue = Balancing_GetSectorRichnessFactor(x,y,50) * 750000`
  (`tradingutility.lua:251-256`).
- **Energy Cells as currency:** `TradeableInventoryItem` sets `good = "Energy Cell"` and charges
  `goodsPrice` Energy Cells for some items instead of credits (`tradeableinventoryitem.lua:23-24, 220-256`).
- **`stationextensions.lua` is mislabeled.** The directory predicts "station type extension/specialization
  logic", but the file only builds procedural **geometry** (`addConstructionScaffold`, `addProductionCenters`,
  `addFarmingCenters`, `addSolarPanels`, `addAsteroid`, `addCargoStorage` — all `BlockPlan` mesh assembly).
  `addCollectors(entity)` is an **empty stub** (`stationextensions.lua:6-8`).
- **German dev comments:** `productionsindex.lua:12-34` contains a German TODO/DONE design block
  (use-cases / requirements for deterministic factory prediction).
- **`minimumCargoBay = 25000`** declared but unused in the pricing/transaction paths shown
  (`tradingmanager.lua:33`).
- **Clamping everywhere:** because `lerp` clamps by default, all relation/supply bands saturate flat outside
  their endpoints (no extrapolation).

## 5.3 External (engine / unprovided-script) symbols to grep later

Constructors/objects: `TradingGood`, `Material`, `NumMaterials`, `MaterialType`, `CargoBay`, `Entity`,
`Faction`, `Player`, `Sector`, `Galaxy`, `Server`, `BlockPlan`, `Random`, `Seed`, `GameSeed`.
Economy/balance: `Balancing_GetSectorRichnessFactor`, `GetRelationChangeFromMoney`, `changeRelations`,
`RelationChangeType`, `RelationStatus`, `RarityType`, `WeaponType`/`WeaponTypes`, `FighterType`,
`InventoryItemType`, `SectorSpecifics`, `FactoryPredictor`, `AsyncShipGenerator`, `PlanGenerator`.
RPC/scheduling: `invokeFunction`, `invokeServerFunction`, `invokeClientFunction`,
`broadcastInvokeClientFunction`, `async`, `deferredCallback`, `getGlobal`, `setGlobal`, `callable`.
Unprovided entity scripts referenced: `entity/merchants/{factory, consumer, habitat, biotope, casino, seller,
turretfactoryseller, turretfactorysupplier, tradingpost, planetarytradingpost}.lua`,
`merchants/tradeship.lua`, plus `tooltipmaker.lua` (turret price sync).
