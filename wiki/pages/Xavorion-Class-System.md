<!-- Mod documentation. Code lineage (kept out of the reader-facing text on purpose):
     "Avorion Mods/2992808773/" (Xavorion: Class System, v2.5.2; modinfo: serverSideOnly=false,
     clientSideOnly=false, saveGameAltering=true; deps 2918443067 (shared Core lib) min 2.3.9,
     Avorion 2.0–2.5.*; NOT dependent on the Arms Generator engine, unlike Xavorion: Weaponry/Mining) —
     modinfo.lua; ShipBalancer/BalancerComponent.lua (staged tick: Idle/Prepare/ClassData/PlanData/Stats/
     Post/Apply/LatentApply; SetBoostOvercharge; OverrideIcon picks data/textures/icons/pixel/{military,
     civil}/m1.png…m8.png by ShipProperty.is_civil); ShipBalancer/Lib/ShipStats.lua (RebuildClassData/
     RebuildPlanData/RebuildStats, Gyro→DirectionalThruster replacement, ScoreRatio/ScoreWorkforceRatio,
     AI vs player vs Cohort branches); ShipBalancer/Lib/ShipsDatabase.lua + ShipsDatabaseProxy.lua (the
     8-row Class table: Volume/Velocity/Acceleration/Strafing/Yaw/Pitch/Roll/SpeedPlanFactor/
     AgilityPlanFactor/ShieldCooldown/ShieldRecharge/BoostVelocity per class, GetClassWeight Light/Medium/
     Heavy interpolation); ShipBalancer/Lib/{BalancerAPI,BalancerFunction,ShipBalancerStrategy}.lua (per-
     block PlanStats contribution by BlockType incl. directional-thruster axis split; Apply() writes
     Thrusters.baseYaw/basePitch/baseRoll/thrust, StatKey.Velocity/Acceleration bias, AI hard-set branch,
     @ThrusterBug strafing-Z-axis note); ShipBalancer/DroneBalancer.lua (flat fighter/drone stats, no class
     lookup); BuildModeUI/{BuildModeUI,ShipClassWidget,ShipStatsWidget,ShipStatsWidgetV2,View/
     ShipStatsView,View/ShipStatsViewV2}.lua (class progress bar, 7-row stat panel w/ p.p. labels, >100%
     pale-yellow highlight, Gyro-conversion banner, Player-Cohort "cannot be modified" lock); systems/
     {classmod,coresubsystem,enginebooster,overchargemodule,velocitybypass,weaknesssystem}.lua (new/
     reworked system-upgrade item definitions: Core Module, Engine Booster ×4, Overcharge ×3, Gyro Array
     ×4, Framework ×3; rarity formula RarityBonus=Rarity.value+2, Alpha=RarityBonus/9, price ~×2.5/rarity
     step); SystemUpgrade/UpgradeProperties.lua + Properties/ClassSystem/UP_{Velocity,Acceleration,Pitch,
     Yaw,Roll,Strafing}Power.lua + UP_ArcFlightBoost.lua (write ShipBalancer.*ScoreBonus values consumed by
     ShipStats; UP_StrafingPower.lua Apply/Remove are empty no-ops — inert); SystemUpgrade/Properties/
     Overcharge/UP_Overcharge{Turrets,Shields,Boosters}.lua (permanent-only, 0 effect when socketed);
     entity/{startbuilding,stationfounder,init}.lua (Build button hook, strips ship scripts on
     transformToStation, attaches BalancerComponent/DroneBalancer.Apply on spawn); ShipXAI/{XAIPlugins,
     Plugins/ClassSystem,Plugins/EnergySubsystem}.lua (NPC bridge + malformed-hull energy-bias safeguard;
     full Lua reimplementation of shield recharge delay/rate and the three Overcharge abilities, NPCs get
     half recharge delay + double recharge rate after a hit vs. players); player/init.lua (BuildModeUI is
     attached to the Player, not the ship); lib/shiputility.lua (renaming override, gated by
     ShipsModule.bShipUtilityRenaming); Config/ShipsModule.lua (AIMinimalPlanFactor difficulty floor,
     AISpeedMultiplier/AIAccelerationMultiplier/AIAgilityMultiplier). Image assets: see wiki/ASSETS.md. -->
# Xavorion: Class System

**Xavorion: Class System** (by **LM13**) is an *"extension to flight model, build mode and general
progression of ships"* — it's the foundation mod of the Xavorion suite. Unlike
[Xavorion: Weaponry](Xavorion-Weaponry) and [Xavorion: Mining](Xavorion-Mining), it has nothing to do with
turrets or the [XSF: Arms Generator](XSF-Arms-Generator) engine; it's entirely about **how big your ship
is, how that size sets its baseline flight stats, what the Building Mode stat panel shows you, and a
handful of new subsystem upgrades** built around flight and boosting.

> **In short:** every ship is sorted into one of **eight size classes (M1–M8)** purely by its **volume**
> (counting anything docked to it). That class sets a **baseline** for top speed, acceleration and turn
> rates — small ships are nimble but fragile, capitals are slow but tanky. Your build then pushes those
> baselines up or down: engines and thrusters add a **build score** on top of the class floor, and that
> score matters *more* on some classes than others. The Building Mode panel shows you exactly that, plus a
> handful of new system upgrades that boost flight stats directly, and a separate **Overcharge** trio that
> only kicks in while you're actively boosting.

## Ship classes: M1 through M8

Your ship's class is decided purely by **volume** — bigger hull, higher class — and it includes the volume
of anything currently **docked** to you, so a carrier with ships clamped to it can get bumped up a class
just by having them attached. Within a class, the panel further labels your ship **Light, Medium or
Heavy** depending on how close your volume sits to the next threshold up.

| Class | Role | Min. Volume | Velocity (m/s) | Acceleration (m/s²) | Yaw (rad/s) | Pitch (rad/s) | Roll (rad/s) |
|---|---|--:|--:|--:|--:|--:|--:|
| **M1** | Scout | 1 | 585 | 240 | 3.00 | 2.25 | 2.25 |
| **M2** | Interceptor | 500 | 570 | 172.5 | 2.50 | 2.03 | 2.10 |
| **M3** | Vanguard | 1,000 | 440 | 150 | 1.80 | 1.43 | 1.65 |
| **M4** | Corvette | 3,000 | 270 | 105 | 0.80 | 0.50 | 0.75 |
| **M5** | Frigate | 9,000 | 220 | 100 | 0.40 | 0.35 | 0.50 |
| **M6** | Cruiser | 25,000 | 180 | 100 | 0.08 | 0.06 | 0.12 |
| **M7** | Dreadnought | 75,000 | 150 | 90 | 0.06 | 0.04 | 0.06 |
| **M8** | Capital | 200,000 | 110 | 60 | 0.04 | 0.03 | 0.04 |

These are **floors before your build matters** — read on for how engines, thrusters and gyros push you
above them. Small ships are already close to their ceiling out of the box; bigger ones start much weaker
and lean far more on how well you build them.

## How your build pushes past the baseline

The class table only sets the floor. On top of it, the mod scores how well your block layout supports
each stat and adds a bonus scaled by that score — this is the same logic the
[Ship stats](Ship-stats#movement--handling) page describes for vanilla blocks, just rebuilt to plug into
the class baseline:

- **Engines** raise the score behind **Velocity**.
- A blend of **Engines and Thrusters** raises the score behind both **Acceleration** and **Strafing** —
  this mod ties Strafing to the same combined score as Acceleration, rather than scoring it purely off
  Thrusters as vanilla does.
- **Thrusters** raise the score behind **Yaw, Pitch and Roll**; **Directional Thrusters** only contribute
  to the axis they actually face (a thruster aimed left/right helps Yaw, one aimed up/down helps Pitch, one
  aimed forward/back helps Acceleration — pointing it the wrong way wastes the block for that stat).
- **Gyro Arrays** are automatically converted into Directional Thrusters the moment this mod takes over a
  ship, because Gyros otherwise cause wild, uncontrollable rotation speeds under the new flight math. If
  your current plan still has Gyros in it, Building Mode shows a bold warning telling you to **restart
  Build Mode** to finish the conversion — and not to overwrite or export your design until you do, since
  the converted plan won't behave the same in vanilla Avorion.

How much that build score is *worth* also depends on your class: on a Scout, the baseline is already
close to the ceiling, so a great build only adds a little. On a Cruiser, Dreadnought or Capital, turning
power in particular is **almost entirely** down to how you build your thrusters and gyros — the baseline
turn rate is just a floor, and a well-built capital can out-turn a poorly-built one by a wide margin. If
you're frustrated by a sluggish capital, the fix is in your thruster placement, not just bigger numbers.

## The Building Mode stat panel

*[📷 Screenshot needed — ASSETS.md: images/xavorion-class-system-buildmode-panel.png]*

Two HUD elements appear while you're in Building Mode:

- A **class bar** along the top, showing your ship's current class flanked by the class one tier below and
  one tier above, with a fill showing how far through the current class your volume sits.
- A **7-row stat panel**, each row showing the live value plus a colored progress bar. Push a stat **over
  100%** of its expected baseline and the bar turns **pale yellow** instead of green, so you can see at a
  glance when a stat is maxed out and further investment there is wasted:

| Row | What it tracks | Raised by |
|---|---|---|
| **Velocity** | Top forward speed (m/s) | Engines |
| **Acceleration** | How fast you reach top speed (m/s²) | Engines, Thrusters, forward/backward Directional Thrusters |
| **Deceleration** | How well you brake, shown as a ratio against your Acceleration target | Inertia Dampeners, forward/backward Directional Thrusters |
| **Yaw (Left/Right)** | Turn rate on the vertical axis | Thrusters, left/right Directional Thrusters |
| **Pitch (Up/Down)** | Turn rate on the side axis | Thrusters, up/down Directional Thrusters |
| **Roll** | Turn rate banking around your forward axis | Thrusters only |
| **Energy efficiency** | Produced vs. required power | Generators (Iron Solar Panels included) |

> The game explicitly warns that **low Deceleration cripples AI-controlled ships** — without enough brake
> thrust, an autopiloted ship (a captained fleet ship, an escort, anything you're not personally flying)
> can't actually reach the top speed its other stats promise, because it never manages to control its
> momentum. Don't skip Inertia Dampeners on ships you intend to fly hands-off.

**Escort and fleet ships you didn't build yourself are locked.** Trying to enter Building Mode on one of
these replaces the whole panel with a blocking **"This ship cannot be modified"** message — only ships you
personally designed can be edited here.

## NPCs and AI-flown ships play by different rules

A few asymmetries are deliberate, not bugs:

- **Empty or barely-built NPC hulls still move.** Player ships with too few engines/thrusters get
  penalized hard for it, but AI ships are guaranteed a **minimum baseline** regardless of how thin their
  build is (the floor rises with game difficulty), so a procedurally-generated enemy never ends up
  helplessly adrift.
- **AI ships get their target speed and turn rate set directly**, rather than easing toward it the way
  player ships do — there's no acceleration curve to exploit by, say, scanning an NPC mid-maneuver.
- **Shields behave differently after a hit.** Every ship has a **recharge delay** (how long shields wait
  after taking damage before recharging starts) and a **recharge rate** that both scale by class — bigger
  ships wait longer and recharge slower. Roughly, a Scout's shield is back to full a few seconds after the
  delay ends, while a Capital's takes well over two minutes. **NPC ships get half the recharge delay and
  double the recharge rate of an identical player ship** after being hit — an AI opponent's shield comes
  back noticeably faster than yours would in the same fight.

## Fighters and drones ignore the class table entirely

Carrier fighters and drones don't get looked up in the M1–M8 table at all — they always fly with the same
fixed speed, acceleration and strafing regardless of their design or size, and their turret slot counts get
a flat ×10 multiplier compared to a same-sized manned ship. Building a bigger or fancier fighter design
won't make it fly any differently; see [Fighters](Fighters) for what *does* change fighter performance
(squad composition, captain bonuses, weapon choice).

## New flight-power system upgrades

These upgrades write straight onto the same build-score the panel above tracks, so each one effectively
boosts one specific row of the stat panel without you having to add more blocks:

| Upgrade | Boosts | Notes |
|---|---|---|
| **Velocity Power** | Velocity's build score | |
| **Acceleration Power** | Acceleration's build score | |
| **Pitch Power** | Pitch's build score | |
| **Yaw Power** | Yaw's build score | |
| **Roll Power** | Roll's build score | |
| **Strafing Power** | — | Registered but currently **does nothing** — its effect is an empty placeholder in this version. Don't spend a slot on it. |
| **Arc Flight Boost** | Your short boost burst | Strengthens the same boost-speed multiplier the Booster Engine variant below also feeds into |

## Overcharge: power spikes that only work while boosting

A trio of upgrades, all carrying the same warning: **"Overcharge only applies during boost,"** and all of
them are effectively **permanent-install only** — socketing any of the three gives **zero** effect, you
have to commit it to get anything at all:

- **Overcharge Turrets** — multiplies your fire rate (up to roughly **×3**) for as long as you're boosting,
  at the cost of overheating much faster. Reduces overall power generation.
- **Overcharge Shields** — instantly refills your shield to full the moment you start boosting (up to
  roughly **×2.5** effective rate), but the system shuts down again as soon as you take damage. Also
  reduces power generation.
- **Overcharge Boosters** — a large extra burst of acceleration while boosting (up to roughly **×5**),
  pitched as enough to dodge an incoming torpedo. The size of the bonus **scales with your ship's class**
  — a Capital gets a far bigger flat speed bump from the same booster than a Scout would, since a flat
  percentage would barely register on a hull that slow.

All three also cut your power generation by up to a third or so at high rarity — budget for it before
relying on Overcharge in a fight.

## Reworked Engine Booster

The mod's version of the Engine Booster upgrade splits into four very different flavours instead of one
generic speed boost:

| Variant | Trade-off |
|---|---|
| **Hyperspace Engine** | Trades acceleration, top speed and hull strength for a much longer jump range, a shorter jump cooldown, and a cheaper jump |
| **Booster Engine** | Boosts acceleration and your short boost-burst strength, plus extra battery capacity/recharge for sustaining it — but costs some top speed and raises collision risk |
| **Feedback Engine** | Trades speed and hull strength for extra shield durability and recharge rate |
| **Hyper Engine** | Boosts both acceleration and top speed hard, at a steep cost to power generation |

The **Booster Engine** has an odd quirk: socketing it (instead of permanently installing it) actually
**doubles** its top-speed *penalty* compared to installing it — for this one variant, permanent install
isn't just stronger, it's strictly better in every way.

## Reworked Gyro Array

The Gyro Array upgrade also splits into four variants, each reshaping your Yaw/Pitch/Roll balance rather
than boosting all three evenly:

| Variant | Theme | Effect |
|---|---|---|
| **Fighter Gyro** | Aircraft-like | Less Yaw, much more Pitch and Roll |
| **Cruiser Gyro** | Naval-like | Much more Yaw, less Pitch and Roll |
| **Tracker Gyro** | Turret tracking | More Yaw and Pitch, less Roll |
| **Hyper Gyro** | All-rounder | More of all three, at a power-generation cost |

Socketing any of these instead of permanently installing one gives roughly a **third** of the bonus —
worth socketing to test, but install permanently once you've picked your favourite.

## Core Module and Framework upgrades

The **Core Module** is a **unique** upgrade slot (only one per ship) with four roles to pick from, and
every one of them does **nothing at all unless permanently installed** — socketing any Core Module gives
no bonus whatsoever:

| Variant | Grants |
|---|---|
| **Fighter MK** | Extra armed/auto turret slots, plus a sector scan range boost |
| **Scout MK** | A large galaxy-map and hidden-object scan range boost, plus sector scan range |
| **Hauler MK** | Extra civilian/auto turret slots and some defensive slots |
| **Defender MK** | Extra defensive/auto turret slots, plus extra shield durability |

The **Framework** upgrade reshapes your hull at a structural level, and is the cheapest of the new
upgrades by far:

| Variant | Effect |
|---|---|
| **Cargo Framework** | Extra cargo space, at the cost of some hull strength |
| **Hull Framework** | Pure extra hull strength |
| **Shield Framework** | Extra shield durability and recharge rate, at the cost of some hull strength (needs a Shield Generator on the ship to matter) |

## See also

- [Ship stats](Ship-stats) – the vanilla version of the Building Mode panel and what each block contributes
- [System upgrades](System-upgrades) – how socketing vs. permanently installing an upgrade works in general
- [Defensive systems](Defensive-systems) – shields, recharge delay and recharge rate in combat
- [Fighters](Fighters) – what actually changes a fighter's combat performance, since hull design doesn't
- [Xavorion: Weaponry](Xavorion-Weaponry) and [Xavorion: Mining](Xavorion-Mining) – the sibling mods that share the Xavorion suite's Core library but not this mod's flight/class systems

---
*Mods: [XSF: Arms Generator](XSF-Arms-Generator) · [Xavorion: Weaponry](Xavorion-Weaponry) · [Xavorion: Mining](Xavorion-Mining) · [Xavorion: Class System](Xavorion-Class-System) · [Xavorion: Encounters](Xavorion-Encounters) · [Xavorion: Combat AI](Xavorion-Combat-AI)*
