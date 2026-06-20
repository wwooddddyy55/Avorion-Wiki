<!-- Mod documentation. Sourced from "Avorion Mods/2992808396/" (XSF: Arms Generator, v2.5.3) Lua:
     modinfo.lua; data/scripts/ArmsGenerator.lua (GetScaledShotDamage, GetTurret pipeline);
     ArmsGenerator/ArmsLibrary.lua (WeaponTTK.Volume / ToDamage);
     ArmsGenerator/BarrelFunctions/BarrelFunction_Default.lua; .../MaterialFunctions/MaterialFunction_Default.lua;
     .../RarityFunctions/RarityFunction_Default.lua; .../CoolingFunction.lua;
     data/scripts/lib/{turretgenerator,weapongenerator,sectorturretgenerator,inventoryitemprice}.lua;
     and the shared FMath.ScalarCut in "Avorion Mods/2918443067/data/scripts/Core/CoreLibrary.lua".
     Formulas are written as monospace code blocks (not LaTeX) for portability. -->
# XSF: Arms Generator

**XSF: Arms Generator** (Workshop ID `2992808396`, by **LM13**) is the **turret-stat engine** of the
[Xavorion](Xavorion-Weaponry) mod suite. It is an *"advanced replacement for vanilla turret generator"*:
where the base game rolls a turret's stats from loose random ranges (see [Weapons](Weapons)), this mod
rebuilds every armed turret deterministically from four stacking **scaling functions** — **barrel**,
**material**, **rarity** and **tech** — driven by a per-weapon archetype defined in
[Xavorion: Weaponry](Xavorion-Weaponry).

This page documents the engine: how it overrides the vanilla generator, the order it applies its
stages, and the exact math each stage runs. For the weapon catalog those stages are applied to, see
[Xavorion: Weaponry](Xavorion-Weaponry). For vanilla turret generation and damage types, see
[Weapons](Weapons) and [Combat](Combat).

> **Mod metadata.** `version = "2.5.3"`, `serverSideOnly = false`, `clientSideOnly = false`,
> `saveGameAltering = true`. Dependencies: the XSF framework `2918443067` (min `2.3.9`) and
> `Avorion` `2.0`–`2.5.*`.

## How it overrides the vanilla generator

The mod ships files at the same script paths as the base game's generator libraries. Each one **backs
up the original function once**, then redefines it to branch on `ArmsGenerator.IsExtendedType(type)`:
an *extended* weapon type (one defined in the Xavorion turret database) is routed to the new engine;
anything else falls through to the saved vanilla function unchanged.

| Overridden file | Vanilla function wrapped | Backup name | Extended path |
|---|---|---|---|
| `lib/turretgenerator.lua` | `TurretGenerator.generateTurret` | `TurretGenerator._generateTurret` | `ArmsGenerator.GetTurret(...)` |
| `lib/weapongenerator.lua` | `WeaponGenerator.generateWeapon` | (per-type table) | `ArmsGenerator.GetFighterWeapon(...)` |
| `lib/sectorturretgenerator.lua` | `SectorTurretGenerator.generate` | — | extended sector roll |
| `lib/inventoryitemprice.lua` | `ArmedObjectPrice` | `_ArmedObjectPrice` | extended price (below) |

Because the fallback is preserved, vanilla turret types keep their original behaviour; only the
mod's own archetypes use the formulas below.

## The generation pipeline

`ArmsGenerator.GetTurret(rng, type, dps, tech, material, rarity, barrelType)` runs the stages in this
fixed order (from `ArmsGenerator.lua`):

```
1. GetTurretMetadata      -- deep-copy the archetype's base stats (+ any BarrelTweak override)
2. ApplyInputParameters   -- set ShotDamage = dps OR GetScaledShotDamage(...) ; fill Base/Max price
3. ApplyRarityScaling     -- RarityFunction (per-stat bonuses)
4. ApplyMaterialScaling   -- MaterialFunction (per-material multipliers)
5. ApplyTechLevelScaling  -- tech-level adjustments
6. ConvertToMultibarrel   -- BarrelFunction (barrels, penetration, auto-balance factors)
7. ApplyCooling           -- CoolingFunction (heat / drain / battery)
```

Stages 3–6 each dispatch to a *named* function chosen by the archetype's `Scaling*Function` field
(e.g. `"AC"`, `"RBE"`, `"RIL"`), falling back to the `_Default` implementations documented here when
the archetype doesn't name one.

## Base damage — the Time-To-Kill model

Every archetype declares its damage as `WeaponTTK.ToDamage(seconds, counterClass, fireRate)` rather than
a raw number. This converts *"destroy a ship of this class in this many seconds"* into a Tech-1, Iron,
per-shot damage value (`ArmsLibrary.lua`):

```
durability  = Volume[counterClass] * 4          -- vanilla "Volume * Material * 4" durability
damage      = durability / seconds              -- damage/sec needed to kill in `seconds`
damage      = damage / 5                         -- extended arms average ~5x base, so divide back
base_shot   = damage / fireRate                  -- spread across the weapon's shots per second
```

The per-class **Volume** table:

| Class | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| **Volume** | 100 | 500 | 1,000 | 3,000 | 9,000 | 25,000 | 75,000 | 200,000 |

So a weapon set to kill an M3 (`Volume 1000`) in 5 s at 1 shot/s starts at
`(1000*4 / 5) / 5 / 1 = 160` base damage per shot, *before* the tech/rarity multiplier below.

## Tech & rarity damage scaling

`ArmsGenerator.GetScaledShotDamage` multiplies that base by a tech factor and a rarity factor. The two
multipliers default to `7` and `2` but an archetype may override them (`TechDamageMult`,
`RarityDamageMult`); each has `1.0` subtracted, and a result below `0` is forced to `1.0`:

```
techMult   = (archetype.TechDamageMult   or 7) - 1.0      -- default 6
rarityMult = (archetype.RarityDamageMult or 2) - 1.0      -- default 1
if techMult   < 0 then techMult   = 1.0 end
if rarityMult < 0 then rarityMult = 1.0 end

techFactor   = techMult   * (tech / 52)          + 1.0     -- tech in 1..52
rarityFactor = rarityMult * ((rarity + 2) / 7)   + 1.0     -- rarity value in -1..5

final_shot = base_shot * techFactor * rarityFactor
```

With defaults this is `final = base * (1 + 6*(tech/52)) * (1 + 1*((rarity+2)/7))` — up to ~7× from tech
and ~2× from rarity. Archetypes that set their own multipliers scale differently: e.g. the laser line
uses `TechDamageMult = 3.0, RarityDamageMult = 1.5`, and the fighter proton torpedo uses
`9 / 2.5` (see [Xavorion: Weaponry](Xavorion-Weaponry)).

## Barrel functions

`BarrelFunction_Default.lua` turns a single archetype into one of four **barrel variants**. Each variant
fixes the **barrel count**, applies **block penetration**, and multiplies the base stats by a set of
**auto-balancing factors** (used only when the archetype/`BarrelTweak` hasn't already supplied an exact
value):

| Barrel | Barrels | Tracking | Recoil | Range | Accuracy | Velocity | ShotDamage | Volley/s | Reload | ShootTime |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **Heavy** | 1 | ×0.5 | ×5.0 | ×1.5 | ×1.15 | ×2.5 | ×5.0 | ×0.5 | ×1.5 | ×1.5 |
| **Medium** | 2 | ×0.75 | ×2.0 | ×1.2 | ×1.0 | ×1.5 | ×2.0 | ×0.75 | ×1.0 | ×2.0 |
| **Burst** | 3 | ×0.9 | ×VolleySize | ×0.8 | ×0.90 | ×1.5 | ×1.3333 | ×0.6 | ×2.0 | ×4.0 |
| **Gatling** | 4 | ×1.0 | ×1.0 | ×1.0 | ×0.95 | ×1.0 | ×1.875 | ×1.0 | ×2.0 | ×4.0 |

The factors are applied in this exact order (`_ApplyBarrelFactors`):

```
Tracking *= TrackingFactor ; Recoil *= RecoilFactor ; Range *= RangeFactor
Accuracy *= AccuracyFactor ; Velocity *= VelocityFactor
ShotDamage *= ShotDamageFactor ; VolleyPerSecond *= VolleyPerSecondFactor
ReloadTime *= ReloadTimeFactor ; ShootingTime *= ShootingTimeFactor
```

> **Block penetration.** `_AddPenetration(blocks)` sets `BlockPenetration = blocks - 1` with a **minimum
> of 3**, and (for penetrating barrels) sets both `ShieldDamageMultiplier` and `HullDamageMultiplier` to
> `4.0`. **Heavy** calls it with `10` → penetration **9**; **Medium** with `4` → penetration **3**.
> **Burst** also forces `ShieldPenetrationChance = 1.0`, a minimum `VolleySize` of `6`, and the burst-fire
> flag. Per-barrel shots are then `ShotsPerBarrel = VolleySize / Barrels`.

Accuracy is finally clamped to `0.1–1.0` and tracking to `0.01–3.0`.

## Material functions

`MaterialFunction_Default.lua` multiplies the post-barrel stats by per-material factors. Columns left at
`×1.0` for every material (Size, Slot, VolleySize) are omitted; the rest:

| Material | Crew | Tracking | Recoil | Range | Accuracy | Velocity | ShotDmg | Reload | ShootTime | Energy/s | Size | BasePrice |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **Iron** | ×0.5 | — | — | — | — | — | — | — | — | — | — | ×0.5 |
| **Titanium** | — | ×1.15 | — | ×1.15 | — | ×1.15 | — | — | — | — | — | ×1.0 |
| **Naonite** | ×2.0 | — | — | — | ×1.1 | ×1.1 | — | ×0.5 | ×2.0 | ×0.5 | — | ×1.5 |
| **Trinium** | — | — | ×2.0 | — | — | — | ×1.5 | — | ×0.5 | ×2.0 | — | ×1.5 |
| **Xanion** | — | — | — | ×0.8 | ×0.95 | — | ×0.75 | — | ×1.5 | — | — | ×2.5 |
| **Ogonite** | — | — | ×0.15 | — | — | — | ×1.25 | ×2.0 | — | ×0.5 | ×1.5 | ×2.0 |
| **Avorion** | ×3.0 | — | — | ×1.25 | ×1.1 | ×1.15 | ×1.15 | — | ×2.0 | ×2.0 | — | ×3.0 |

(Accuracy is a *multiplier* here — `×1.1` on a `0.9` base gives `0.99`.) The intent encoded in the file
comments: Iron is cheap, Titanium tracks/reaches farther, Naonite is cooling/energy-efficient but
crew-hungry, Trinium trades recoil for raw power, Xanion is glass-cannon fast, Ogonite is big and
low-recoil, Avorion is broadly superior but crew-, energy- and price-heavy.

## Rarity functions

`RarityFunction_Default.lua` uses **one function for all seven rarities** (Petty `-1` … Legendary `5`),
scaling each stat by the rarity's integer `value`:

| Stat | Formula | Range (Petty → Legendary) |
|---|---|---|
| **Range** | `Range *= (value*0.05) + 1.0` | −5% → +25% |
| **Accuracy** | `Accuracy += value*0.01` | −1pp → +5pp |
| **Velocity** | `Velocity *= (value*0.05) + 1.0` | −5% → +25% |
| **Fire rate** | `VolleyPerSecond *= (value*0.1) + 1.0` | −10% → +50% |
| **Reload** | `ReloadTime *= 1.0 - (value*0.1)` | +10% → −50% (lower is better) |
| **Shooting time** | `ShootingTime *= ((value+1)*0.25) + 1.0` | +0% → +150% |
| **Efficiency** | `Efficiency *= (0.3 * (value+2)/7) + 1.0` | up to +30% |

## Cooling systems

`CoolingFunction.lua` assigns the turret's heat/charge model from the archetype's `CoolingType`:

| Cooling type | Heat unit | Reservoir | Notes |
|---|---|---|---|
| **Heat** | `100 * 4` per second | `maxHeat = coolingPerSec * ReloadTime` | Standard heat build-up; heat/shot = `maxHeat/ShootingTime/fireRate + coolingPerShot`, clamped to `[0, maxHeat]`. |
| **Battery** | `EnergyPerSecond` (as the heat unit) | same shape as Heat | Energy-fed weapons (blasters, lasers, railguns). |
| **Drain** | `EnergyPerSecond * 0.83333` (`×4` if a beam) | `Heat = heatPerSec * 1.2` (120% charge) | Continuous-drain weapons (zappers). |

(Heat/shot is always clamped into `[0, maxHeat]` so a single shot can never exceed the reservoir.)

## Pricing

`inventoryitemprice.lua` overrides `ArmedObjectPrice` for extended types. It splits the price *span*
`Delta = MaxPrice - BasePrice` into three weighted parts using `FMath.ScalarCut(Delta, {10, 5, 3})` —
which divides a value into pieces **proportional to the weights** (total weight `10+5+3 = 18`):

```
Delta   = MaxPrice - BasePrice
part1   = Delta * 10/18      -- tech share
part2   = Delta *  5/18      -- rarity share
part3   = Delta *  3/18      -- material share

Price = BasePrice
      + (tech / 52)            * part1     -- tech in 1..52
      + ((rarity + 2) / 8)     * part2     -- rarity value in -1..5
      + ((material + 1) / 7)   * part3     -- material in 0..6
Price = max(Price, 100)
```

So tech contributes the largest slice of the price climb, rarity the next, material the least, and the
floor is 100 credits. `BasePrice`/`MaxPrice` come from each archetype (see the price columns in
[Xavorion: Weaponry](Xavorion-Weaponry)); a missing `MaxPrice` defaults to `BasePrice * 100`.

## See also

- [Xavorion: Weaponry](Xavorion-Weaponry) – the weapon archetypes this engine generates, plus fighters, shields and sounds
- [Weapons](Weapons) – the vanilla turret types and how base-game generation works
- [Combat](Combat) – damage types, shields vs hull, and how vanilla weapon power scales
- [Turret crafting](Turret-crafting) – building turrets and the stat each ingredient raises

---
*Mods: [XSF: Arms Generator](XSF-Arms-Generator) · [Xavorion: Weaponry](Xavorion-Weaponry)*
