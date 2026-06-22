<!-- Hand-written mechanics page. Code lineage (kept out of the reader-facing text on purpose):
     systems/basesystem.lua (parent class: install lifecycle initialize/onInstalled/onRemove/onUninstalled,
       secure/restore, remoteInstall, bonus helpers addBaseMultiplier/addMultiplier/addMultiplyableBias/addAbsoluteBias,
       getEnergy/getPrice, tooltip framework, flags Unique/PermanentInstallationOnly/MissionRelevant/FixedEnergyRequirement),
     systems/militarytcs.lua, civiltcs.lua, arbitrarytcs.lua, autotcs.lua (Turret Control Subsystems;
       stats ArmedTurrets/UnarmedTurrets/ArbitraryTurrets/AutomaticTurrets),
     systems/batterybooster.lua, energybooster.lua, enginebooster.lua, hyperspacebooster.lua,
     systems/radarbooster.lua, scannerbooster.lua, excessvolumebooster.lua (ExcessProcessingPowerSteps),
       cargoextension.lua, velocitybypass.lua, wormholeopener.lua.
     Curve constants confirmed against each script; bonus application is engine-side.
     Image assets: see wiki/ASSETS.md. -->
# System upgrades

**System upgrades** are the modules you slot into a ship's subsystem sockets to change its stats — turret
slots, energy, speed, jump range, radar, cargo and more. Each upgrade is rolled from a **rarity** and a
hidden **seed**, so two upgrades of the same name and rarity can roll slightly different values. Most
behave very differently depending on whether you **socket** them (reversible, weaker) or **permanently
install** them (consumed, irreversible, stronger).

> **In short:** higher rarity = bigger bonus. **Permanent installation** is the big lever — it boosts most
> boosters by **×1.5 (+50%)**, doubles scanner/deep-scan, and unlocks the extra turret slots, jump range
> and effects that socketing alone won't give. It costs the upgrade and raises energy draw, so commit your
> best rolls. Always compare the tooltip arrows before permanently installing.

Rarity runs from **Petty** to **Legendary**. Many formulas below scale with a **rarity value** that runs
from −1 to 5:

| Rarity value | −1 | 0 | 1 | 2 | 3 | 4 | 5 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Rarity | Petty | Common | Uncommon | Rare | Exceptional | Exotic | Legendary |

## How upgrades work

*[📷 Screenshot needed — ASSETS.md: images/system-upgrades-socket-panel.png]*

Slotting an upgrade applies its bonuses; removing it reverses them. The exact numbers are locked to the
item's hidden seed, which is why two upgrades with the same name and rarity can differ — always read the
tooltip.

A bonus stacks in one of a few ways, and the difference matters when you predict an upgrade's effect:

- **Percentage boosts** (energy, velocity, scanner range…) raise the stat by a percent of its current
  value.
- **Turret-slot bonuses** are flat *+N slots*, but they're added **before** your ship's own multipliers, so
  hull bonuses can still amplify them.
- **Flat additions** (cargo m³, jump cooldown seconds) are applied **after** multipliers — a fixed amount
  that nothing scales.

**Energy and price.** Each upgrade draws power, and a **permanent install draws more** — the tooltip shows
the current draw, the base-install draw and the permanent-install draw so you can budget before committing.
Prices climb steeply with rarity (roughly **×2.5 per rarity step**).

**Special handling.** Some upgrades are **unique** (only one per ship), some are **permanent-install only**
(can't be socketed at all), and a few are **story items** rather than stat boosters — the tooltip greys out
options that don't apply.

## Turret Control Subsystems (TCS)

The four **Turret Control Subsystems** all grant turret *slots*, but each targets a different turret class.
Three things drive every TCS:

- **base slots** — granted whether socketed or permanent,
- **bonus slots** — extra armed/unarmed slots unlocked **only** by a permanent install,
- **defensive (point-defence) and auto-turret slots** — also **permanent-only** (the auto count is a random
  roll).

### Military & Civil TCS

Structurally identical — **Military** grants armed-turret slots, **Civil** grants unarmed-turret slots:

| Rarity | Slots socketed | Armed/Unarmed (permanent) | + Defensive (perm) | + Auto (perm, random) |
|:--:|--:|--:|--:|--:|
| Petty | 1 | 2 | 0 | 0–1 |
| Common | 1 | 2 | 0 | 0–1 |
| Uncommon | 2 | 3 | 1 | 0–2 |
| Rare | 3 | 4 | 1 | 1–3 |
| Exceptional | 4 | 6 | 2 | 2–5 |
| Exotic | 5 | 7 | 2 | 3–6 |
| Legendary | 6 | 9 | 3 | 4–8 |

Energy draw actually **falls** as rarity rises (it outpaces the slot growth), so a high-rarity TCS is more
slot-per-watt efficient. Military draws a little more power and costs a little more than Civil for the same
rarity.

### Arbitrary TCS

Grants slots that accept **any** turret, armed or unarmed — the premium, do-anything controller. It has
**no** defensive slots and a smaller permanent bonus, but the flexibility makes it the costliest TCS per
slot:

| Rarity | Slots socketed | Arbitrary (permanent) | + Auto (perm, random) |
|:--:|--:|--:|--:|
| Petty | 1 | 2 | 0–1 |
| Common | 1 | 2 | 0–1 |
| Uncommon | 1 | 2 | 0–1 |
| Rare | 2 | 3 | 0–2 |
| Exceptional | 3 | 4 | 1–3 |
| Exotic | 4 | 6 | 2–5 |
| Legendary | 5 | 7 | 3–6 |

### Auto TCS

Adds only [auto-firing turret](Weapons) slots. Its quirk: a permanent install simply **doubles** the slot
count rather than adding a separate bonus pool.

| Rarity | Auto slots socketed | Auto slots (permanent) |
|:--:|--:|--:|
| Petty | 1 | 2 |
| Common | 1 | 2 |
| Uncommon | 2 | 4 |
| Rare | 3 | 6 |
| Exceptional | 4 | 8 |
| Exotic | 5 | 10 |
| Legendary | 6 | 12 |

## Boosters

Most boosters share one recipe: the bonus scales with rarity, a hidden seed makes the exact roll
deterministic per item, and a **permanent install multiplies the result by ×1.5 (+50%)**. Many boosters
carry **two** stats and roll whether you get one or both — at low rarity you usually get just one, while
**Exotic and above always grant both**.

Per-booster values (the "step / span" numbers set how fast each stat grows with rarity and how wide its
random roll is):

| Booster | Stat A (step / span) | Stat B (step / span) | Permanent × | Energy draw | Both stats? |
|:--|:--|:--|:--:|:--|:--:|
| **Battery** | Energy Capacity (15 / 10) | Recharge (4 / 4) | 1.5 | none | from Uncommon up |
| **Generator** | Generated Energy (10 / 8) | Recharge (4 / 4) | 1.5 | none | from Uncommon up |
| **Engine** | Velocity (3 / 4) | Acceleration (5 / 4) | 1.5 | yes | from Uncommon up |
| **Cargo Extension** | Cargo % (4 / 4) | Cargo flat m³ (50 / 50) | 1.5 | yes | random |
| **Radar** | Radar range | Deep-scan range | 1.5 / **2** | yes | from Uncommon up |
| **Scanner** | Scanner range (15 / 15) | — | **2** | yes | always on |

### How the roll reads — a worked example

For a **Rare** Battery Booster's energy-capacity stat with the random roll at its midpoint, the bonus works
out to **+60% energy capacity** when socketed. Permanently installed, the same roll becomes **+90%** (the
×1.5 rule). Battery prices climb a bit faster with rarity than other boosters.

### Boosters that break the pattern

- **Radar Booster** rolls whole-number ranges instead of percentages. A permanent install multiplies normal
  radar by **×1.5** but **deep-scan by ×2**. Deep-scan reveals mass-bearing sectors as yellow blips on the
  [map](Maps-and-charts).
- **Scanner Booster** has a single stat and a permanent install multiplies it by **×2** (not ×1.5). It
  boosts the range from which you can read other ships' cargo and exact hit points.
- **Hyperspace Booster** is the most varied: it picks **1–3** bonuses (more at higher rarity) from cooldown
  reduction, charge-energy reduction, radar range, and — from Uncommon up — **jump range**. A coin-flip
  "mega-reach" variant trades all cooldown reduction for a big flat range bump. **Jump range and the radar
  bonus are permanent-only**; socketed, you get no cooldown benefit either.

### Excess Volume Booster — "Stabilizing Mainframe Wiring"

**Permanent-install only.** It grants **+117.2k processing power** (the equivalent of one extra subsystem
socket) — but **only** while your ship already has the full **15 subsystem sockets**. Flat **1,000,000**
credits, no energy cost. It's the late-game reward for a maxed-out hull that wants to behave as if it had a
16th socket.

### Velocity Security Control Bypass

Effectively **permanent-only**. It lifts your ship's **speed cap enormously** at the cost of **leaking
generator energy**. Higher rarity *reduces* the leak — a Petty bypass bleeds roughly **48–58%** of
generated energy, while a Legendary one bleeds only **0–10%**. A pure speed-demon module.

### Wormhole Opener — "Xsotan Technology Fragment"

A [story](Story-missions) item, not a stat booster. At **Legendary** rarity it becomes the **Wormhole Power
Diverter**: installed, it lets you *[Harness Wormhole Power]* from a Wormhole Guardian. At any lower rarity
it's an inert **Xsotan Technology Fragment**.

## Socketing vs. permanent installation

The single most important decision for any upgrade is whether to **socket** it (reversible, removable,
weaker) or **permanently install** it at an [Equipment Dock](Trading-and-Prices) (consumes the upgrade,
irreversible, full strength):

| Upgrade family | Socketed gives | Permanent adds |
|:--|:--|:--|
| Common boosters (battery, generator, engine, cargo) | the base rolled value | **×1.5** the value (+50%) |
| Scanner / Radar deep-scan | base value | **×2** the value |
| Turret Control Subsystems | base slots only | bonus armed/unarmed + defensive + auto slots |
| Hyperspace Booster | cooldown/charge/radar only | unlocks jump range, +50% radar, cooldown bias |
| Velocity Bypass · Excess Volume | nothing (inactive) | the entire effect |

Permanent installs also raise the energy draw, so a power-tight ship should budget for it. Because each
roll is keyed to the upgrade's seed, two upgrades of the same name and rarity can differ — **always compare
the tooltip arrows before committing one permanently.**

## See also

- [Ship generation](Ship-generation) – how the craft these upgrades go into are built and scaled
- [Building knowledge](Building-knowledge) – subsystem sockets, processing power and what unlocks them
- [Weapons](Weapons) – the armed, unarmed, defensive and auto turrets the TCS modules enable
- [Defensive systems](Defensive-systems) – the shield, resistance and anti-boarding upgrades
- [Combat](Combat) – where turret slots, energy and speed translate into effectiveness

---
*Progression & Systems: [Ship generation](Ship-generation) · [System upgrades](System-upgrades) · [Building knowledge](Building-knowledge)*
