<!-- Hand-written mechanics page. Code lineage:
     systems/basesystem.lua (parent class: install lifecycle, bonus helpers, tooltip/energy framework),
     systems/militarytcs.lua, civiltcs.lua, arbitrarytcs.lua, autotcs.lua (Turret Control Subsystems),
     systems/batterybooster.lua, energybooster.lua, enginebooster.lua, hyperspacebooster.lua,
     systems/radarbooster.lua, scannerbooster.lua, excessvolumebooster.lua, cargoextension.lua,
     systems/velocitybypass.lua, wormholeopener.lua,
     curve constants confirmed against each script; bonus application (addBaseMultiplier etc.) is engine-side. -->
# System upgrades

**System upgrades** are the modules you slot into a ship's subsystem sockets to change its stats — turret
slots, energy, speed, jump range, radar, cargo and more. Every upgrade is one Lua script that inherits from
`basesystem.lua`; the parent class handles installation, energy draw, persistence and tooltips, while each
script overrides a handful of functions to declare *what* it does. Upgrades are rolled from a **seed** and a
**rarity**, and most behave very differently when **permanently installed** versus simply socketed.

Rarity throughout this page is the engine's `rarity.value`, which runs from **−1 (Petty)** to **5
(Legendary)**:

| `rarity.value` | −1 | 0 | 1 | 2 | 3 | 4 | 5 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Rarity | Petty | Common | Uncommon | Rare | Exceptional | Exotic | Legendary |

## Upgrade architecture (`basesystem.lua`)

When an upgrade is installed the engine calls `initialize(seed, rarity, permanent)`, which stores the three
values and invokes the script's own `onInstalled(seed, rarity, permanent)`. Removal triggers `onRemove` →
`onUninstalled`. State survives save/load through `secure()` (returns `{seed, rarity, permanent}`) and
`restore()`, and client/server stay in sync via `remoteInstall` / `remoteInstallCallback`.

### Applying bonuses

`onInstalled` declares stat changes by calling one of four helpers, each of which registers a bonus key with
the entity (and is a no-op on the client). The distinction matters for predicting an upgrade's effect:

| Helper | Effect on the stat | Used for |
|:--|:--|:--|
| `addBaseMultiplier(stat, f)` | $\text{new} = \text{old} \times (1 + f)$ | percentage boosts (energy, velocity, scanner…) |
| `addMultiplier(stat, f)` | $\text{new} = \text{old} \times f$ | scaling a stat down/up to a fraction |
| `addMultiplyableBias(stat, f)` | adds $f$ to the base **before** multipliers | flat counts that should still scale (turret slots) |
| `addAbsoluteBias(stat, f)` | adds $f$ **after** multipliers | flat additions (cargo m³, jump cooldown seconds) |

So a battery booster's `addBaseMultiplier(EnergyCapacity, 0.30)` means *+30 %*, whereas a TCS's
`addMultiplyableBias(ArmedTurrets, 4)` means *+4 slots* that the ship's own multipliers can still amplify.

### Energy and price

Each script defines `getEnergy(seed, rarity, permanent)` (in watts) and `getPrice(seed, rarity)`. Most set
`FixedEnergyRequirement = true`, telling the engine the draw is constant so it needn't be re-read every frame.
The base class renders three energy figures in the tooltip — current, base-install, and permanent-install — so
you can see how much extra power a permanent install will cost before you commit. Prices almost universally
scale as a geometric series in rarity, typically $\times 2.5^{\,\text{rarity.value}}$.

### Declared properties

Scripts flip class-level flags to change handling: `Unique = true` (only one per ship),
`PermanentInstallationOnly = true` (cannot be slotted normally at all), and `MissionRelevant = true`. The
tooltip framework (`getTooltipLines`, `getComparableValues`, `getDescriptionLines`, `getName`, `getIcon`)
turns these into the comparison arrows and the greyed-out *"Permanent Installation Only"* preview block you see
when inspecting an upgrade.

## The TCS matrix — Turret Control Subsystems

The four **Turret Control Subsystems** all add turret *slots* via `addMultiplyableBias`, but each targets a
different turret class and uses its own constants. Three quantities drive every TCS:

- **base slots** — granted whether socketed or permanent,
- **bonus slots** — extra armed/unarmed slots unlocked **only** by a permanent install,
- **defensive (PDC) and auto-turret slots** — also **permanent-only**, the auto count being a random roll.

### Military & Civil TCS

These two are structurally identical — Military feeds `ArmedTurrets`, Civil feeds `UnarmedTurrets` — and share
the same slot math:

$$\text{base} = \max(1,\ \text{rarity.value} + 1)$$
$$\text{bonus}_{\text{perm}} = \max\!\left(1,\ \left\lfloor \tfrac{\text{rarity.value}+1}{2} \right\rfloor\right), \qquad
\text{pdc}_{\text{perm}} = \left\lfloor \tfrac{\text{base}}{2} \right\rfloor$$
$$\text{auto}_{\text{perm}} = \max\!\bigl(0,\ \operatorname{randInt}(\max(0,\text{rarity.value}-1),\ \text{total}-1)\bigr)$$

| Rarity | Slots socketed | Armed/Unarmed (permanent) | + Defensive (perm) | + Auto (perm, random) |
|:--:|--:|--:|--:|--:|
| Petty (−1) | 1 | 2 | 0 | 0–1 |
| Common (0) | 1 | 2 | 0 | 0–1 |
| Uncommon (1) | 2 | 3 | 1 | 0–2 |
| Rare (2) | 3 | 4 | 1 | 1–3 |
| Exceptional (3) | 4 | 6 | 2 | 2–5 |
| Exotic (4) | 5 | 7 | 2 | 3–6 |
| Legendary (5) | 6 | 9 | 3 | 4–8 |

- **Military** energy $= \text{slots} \times 300\text{M} / 1.2^{\,\text{rarity.value}}$ W, price
  $= 6000\,(\text{slots} + 0.5\,\text{auto}) \times 2.5^{\,\text{rarity.value}}$.
- **Civil** energy $= \text{slots} \times 200\text{M} / 1.2^{\,\text{rarity.value}}$ W, price
  $= 5000\,(\text{slots} + 0.5\,\text{auto}) \times 2.5^{\,\text{rarity.value}}$.

Note the energy *falls* with rarity (the $1.2^{\text{rarity}}$ divisor outpaces the slot growth), so a
high-rarity TCS is more slot-per-watt efficient.

### Arbitrary TCS

Grants `ArbitraryTurrets` slots that accept **any** turret (armed or unarmed) — the premium, do-anything
controller. It has **no** defensive (PDC) slots, a smaller bonus, and a gentler energy divisor of **1.1**:

$$\text{base} = \max(1,\ \text{rarity.value}), \quad
\text{bonus}_{\text{perm}} = \max\!\left(1, \left\lfloor \tfrac{\text{rarity.value}}{2} \right\rfloor\right), \quad
\text{auto}_{\text{perm}} = \max\!\bigl(0, \operatorname{randInt}(\max(0,\text{rarity.value}-2),\, \text{total}-1)\bigr)$$

| Rarity | Slots socketed | Arbitrary (permanent) | + Auto (perm, random) |
|:--:|--:|--:|--:|
| Petty (−1) | 1 | 2 | 0–1 |
| Common (0) | 1 | 2 | 0–1 |
| Uncommon (1) | 1 | 2 | 0–1 |
| Rare (2) | 2 | 3 | 0–2 |
| Exceptional (3) | 3 | 4 | 1–3 |
| Exotic (4) | 4 | 6 | 2–5 |
| Legendary (5) | 5 | 7 | 3–6 |

Energy $= \text{slots} \times 350\text{M} / 1.1^{\,\text{rarity.value}}$ W; price
$= 7500\,(\text{slots} + 0.5\,\text{auto}) \times 2.5^{\,\text{rarity.value}}$ — the costliest TCS per slot,
reflecting its flexibility.

### Auto TCS

Adds only `AutomaticTurrets` slots (for [auto-firing turrets](Weapons)). Its defining quirk: a permanent
install simply **doubles** the slot count rather than adding a separate bonus pool.

$$\text{slots} = \max(1,\ \text{rarity.value} + 1), \qquad
\text{slots}_{\text{perm}} = 2 \times \text{slots}$$

| Rarity | Auto slots socketed | Auto slots (permanent) |
|:--:|--:|--:|
| Petty (−1) | 1 | 2 |
| Common (0) | 1 | 2 |
| Uncommon (1) | 2 | 4 |
| Rare (2) | 3 | 6 |
| Exceptional (3) | 4 | 8 |
| Exotic (4) | 5 | 10 |
| Legendary (5) | 6 | 12 |

Energy $= \text{slots} \times 200\text{M} / 1.2^{\,\text{rarity.value}}$ W; price
$= 5000\,\text{slots} \times 2.5^{\,\text{rarity.value}}$.

## Booster scaling mechanics

Most boosters share one recipe in their `getBonuses(seed, rarity, permanent)` function. The seed makes the
roll deterministic per item, the value scales with rarity, and a permanent install multiplies the result:

$$\text{value} = \Bigl(\underbrace{\text{base}}_{\text{flat}} + (\text{rarity.value}+1)\cdot \text{step}
   + \operatorname{rand}(0,1)\cdot(\text{rarity.value}+1)\cdot \text{span}\Bigr)\times 0.8 \;\big/\; 100$$

$$\text{value}_{\text{permanent}} = 1.5 \times \text{value}_{\text{socketed}}$$

That **×1.5** is the universal rule: a permanent install gives 150 % of the socketed value — i.e. **+50 %**
extra — for the common boosters below. Many boosters carry **two** stats and roll whether you get one or both:

$$P(\text{both}) = \max(0,\ \text{rarity.value}\times 0.25)$$

so a Petty/Common roll almost always grants only one of the two stats, while Exotic (4) and above always grant
both. The per-booster constants:

| Booster | Stat A (`step` / `span`) | Stat B (`step` / `span`) | Perm × | Energy draw | One-of-two |
|:--|:--|:--|:--:|:--|:--:|
| **Battery** | Energy Capacity (15 / 10) | Recharge (4 / 4) | 1.5 | none | rarity × 0.25 |
| **Generator** | Generated Energy (10 / 8) | Recharge (4 / 4) | 1.5 | none | rarity × 0.25 |
| **Engine** | Velocity (3 / 4) | Acceleration (5 / 4) | 1.5 | $(v+a)\times1.5\text{G}$ | rarity × 0.25 |
| **Cargo Extension** | Cargo % (4 / 4) | Cargo flat m³ (50 / 50) | 1.5 | $v\!\cdot\!1.5\text{G} + \text{flat}\!\cdot\!0.01\text{G}$ | 50 / 50 |
| **Radar** | Radar range | Deep-scan range | 1.5 / **2** | $r\!\cdot\!75\text{M} + h\!\cdot\!150\text{M}$ | rarity × 0.25 |
| **Scanner** | Scanner range (15 / 15) | — | **2** | $s\times550\text{M}$ | always on |

(`base` flat values: Battery/Generator energy & charge start at 15 %; Engine velocity 3 %, accel 6 %; Cargo %
starts 10 %, flat starts 20; Scanner starts 5 %. "M" = million W, "G" = billion W.)

### Reading the curve — worked example

For a **Rare (rarity.value = 2)** Battery Booster's energy-capacity stat, with the random roll at its midpoint
($\operatorname{rand}=0.5$):

$$\bigl(15 + (2+1)\cdot 15 + 0.5\cdot(2+1)\cdot 10\bigr)\times 0.8 = (15 + 45 + 15)\times 0.8 = 60\%$$

Socketed that is **+60 % energy capacity**; permanently installed it becomes $60 \times 1.5 = \mathbf{+90\%}$.
Price scales further as $\times 3.0^{\,\text{rarity.value}}$ for the battery (most boosters use $2.5$).

### Boosters that break the pattern

- **Radar Booster** (`radarbooster.lua`) rolls integer ranges rather than percentages:
  $\text{radar} = \max(0,\operatorname{randInt}(r,\,2r)) + 1$ and
  $\text{deep} = \max(0,\operatorname{randInt}(r,\,1.5r)) + 1$ (with $r=$ rarity.value). A permanent install
  multiplies normal radar by **×1.5** but **deep-scan by ×2**. Deep-scan reveals mass-bearing sectors as
  yellow blips on the [map](Maps-and-charts).

- **Scanner Booster** (`scannerbooster.lua`) skips the ×0.8 trim, uses flat step
  $(\text{rarity.value}+2)\times15\%$, and a permanent install multiplies by **×2** (not ×1.5). It boosts the
  range from which you read other ships' cargo and exact HP.

- **Hyperspace Booster** (`hyperspacebooster.lua`) is the most complex: it picks **1–3** distinct bonuses by
  weighted random (more bonuses at higher rarity) from cooldown reduction, charge-energy reduction, radar
  range, and — at rarity ≥ 1 — **jump range**. A coin-flip "mega-reach" variant trades all cooldown reduction
  for a big flat range bump ($\text{reach} = (\max(1,\text{rarity.value}+1)\cdot2 + \text{rarity.value})$ with
  a `HyperspaceCooldown` absolute bias). Jump range and the radar ×1.5 are **permanent-only**; socketed, the
  cooldown factor is forced to 0. Energy
  $= |\text{cd}|\cdot2.5\text{G} + \text{reach}\cdot125\text{M} + \text{radar}\cdot75\text{M}$.

### Excess Volume Booster — "Stabilizing Mainframe Wiring"

`excessvolumebooster.lua` is flagged `PermanentInstallationOnly = true`: it cannot be socketed normally at
all. It adds a single step of `ExcessProcessingPowerSteps`, granting **+117.2k** processing power (socket
equivalent **+1**) — but **only** while the ship already has the full **15 subsystem sockets** available. Flat
price **1,000,000** credits, no energy cost. It is the late-game reward for a maxed-out hull that wants to
behave as if it had a 16th socket.

### Velocity Security Control Bypass

`velocitybypass.lua` is effectively permanent-only — its `onInstalled` returns immediately unless `permanent`.
When permanently installed it grants a flat $+10{,}000{,}000$ `Velocity` absolute bias (an enormous speed cap
lift) at the cost of **leaking generator energy**:

$$\text{leak} = \frac{\bigl(6 - (\text{rarity.value}+1)\bigr)\times 8 + \operatorname{randInt}(0,10)}{100}$$

Higher rarity *reduces* the leak — a Petty bypass bleeds roughly **48–58 %** of generated energy, while a
Legendary one bleeds only **0–10 %**. Price $= 15000 \times 2.5^{\,\text{rarity.value}}$. A pure speed-demon
module: weeee.

### Wormhole Opener — "Xsotan Technology Fragment"

`wormholeopener.lua` (`MissionRelevant = true`) is a [story](Story-missions) item, not a stat booster. At
**Legendary** rarity it becomes the **Wormhole Power Diverter**: installed, it registers a dialog hook so you
can *[Harness Wormhole Power]* from a Wormhole Guardian, and draws 250 MW. At any lower rarity it is an inert
**Xsotan Technology Fragment** (0 W). Flat price 5,000; made stackable through a dummy comparable value.

## Standard slotting vs. permanent installation

The single most important decision for any upgrade is whether to **socket** it (reversible, removable, weaker)
or **permanently install** it at an [Equipment Dock](Trading-and-Prices) (consumes the upgrade, irreversible,
full strength). The pattern across all systems above:

| Upgrade family | Socketed gives | Permanent adds |
|:--|:--|:--|
| Common boosters (battery, generator, engine, cargo) | the base rolled value | **×1.5** the value (+50 %) |
| Scanner / Radar deep-scan | base value | **×2** the value |
| Turret Control Subsystems | base slots only | bonus armed/unarmed + defensive + auto slots |
| Hyperspace Booster | cooldown/charge/radar only | unlocks jump range, +50 % radar, cooldown bias |
| Velocity Bypass · Excess Volume | nothing (inactive) | the entire effect |

Permanent installs also raise the energy draw (the tooltip's *Energy Consumption* delta line), so a power-tight
ship should budget for it. Because the bonus is keyed to the upgrade's stored `seed`, two upgrades of the same
name and rarity can roll different exact values — always compare the tooltip arrows before committing one
permanently.

## See also

- [Ship generation](Ship-generation) – how the craft these upgrades go into are built and scaled
- [Building knowledge](Building-knowledge) – subsystem sockets, processing power and what unlocks them
- [Weapons](Weapons) – armed, unarmed, defensive and auto turrets the TCS modules enable
- [Defensive systems](Defensive-systems) – the shield, resistance and anti-boarding upgrades
- [Combat](Combat) – where turret slots, energy and speed translate into effectiveness

---
*Progression & Systems: [Ship generation](Ship-generation) · [System upgrades](System-upgrades) · [Building knowledge](Building-knowledge)*
