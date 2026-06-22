<!-- Hand-written mechanics page. Sourced from lib/damagetypeutility.lua, lib/weapongenerator.lua,
     lib/weapontype.lua, systems/resistancesystem.lua, systems/weaknesssystem.lua, and the turret
     generator. Damage/shield resolution itself is engine-side; the rules below are what the scripts set. -->
# Combat

This page covers how damage works in **Avorion**: the **damage types**, how they interact with
**shields** and **hull**, and how a weapon's power scales with **rarity** and **tech level**. For the
individual turret weapon types see **[Weapons](Weapons)**; for torpedoes see **[Torpedoes](Torpedoes)**;
for shield and defensive ship upgrades see **[Defensive systems](Defensive-systems)**.

> **In short:** enemies are protected by a **shield** (hit first) and then **hull**. Energy/Plasma strip
> shields; Physical/Anti-Matter wreck hull; Electric does both. So **bring the right damage type for the
> layer you're attacking**, and a mix to handle both. Beyond type, **tech level and rarity** are what make
> one weapon hit far harder than another — chase higher-tech gear as you head coreward.

## Shields vs. hull

Every armed ship has two health pools that are attacked in order:

- **Shield** – a regenerating bubble that absorbs hits first. While shields are up, most weapons hit
  the shield, not the hull. Some weapons **penetrate** or **deactivate** shields (see below).
- **Hull** – the blocks of the ship itself. Once shields are down, hits damage hull blocks directly,
  and destroying enough blocks destroys the ship.

A weapon's effect on each pool is set by two multipliers it is generated with:

| Multiplier | Effect |
|---|---|
| **Hull damage multiplier** | How much of the weapon's damage applies to **hull**. Physical-style weapons get ×1; Anti-Matter raises this far above 1. |
| **Shield damage multiplier** | How much of the weapon's damage applies to **shields**. Energy-style weapons get ×1; Plasma raises this far above 1. |

So "damage" on a turret is not a flat number against everything — the *type* decides whether that
damage lands well on shields, on hull, or both.

## Damage types

There are six damage types. Each weapon has one **base** type, and many weapons have a chance to roll
a bonus elemental type when generated (for example a chaingun has a small chance to become Anti-Matter,
Plasma or Electric).

| Damage type | Best against | Notes |
|---|---|---|
| **Physical** | Hull | Standard kinetic damage (chainguns, cannons, railguns, rockets). Full damage to hull, little to shields. |
| **Energy** | Shields | Beam-laser damage. Full damage to shields, weak against hull. |
| **Plasma** | Shields (heavily) | Carries a large **shield** damage multiplier (≈2.5×+). Melts shields, then is poor against hull. |
| **Anti Matter** | Hull (heavily) | Carries a large **hull** damage multiplier (≈2.5×+). Tears through hull once shields are down; bolters are pure Anti-Matter. |
| **Electric** | Both | Hits shields **and** hull equally (Tesla and Lightning guns). A flexible all-rounder. |
| **Fragments** | Fighters & torpedoes | The **point-defense** type. Hits both pools at ×1 but is generated only on Point Defense and Anti-Fighter weapons, which target small fast objects. |

The base damage type of each weapon, and its roll chances for a bonus type, are listed on
**[Weapons](Weapons)**.

### Shield piercing and special interactions

Some weapons and torpedoes ignore the normal shield-first rule:

- **Pulse Cannon** shots **penetrate shields** to hit the hull directly — at the cost of 25% lower base
  damage. Repair beams set to hull-repair also pierce shields to mend friendly hulls.
- **Railguns** have **block penetration** (passing through several blocks per shot, 3 up to `5 + 2 × rarity`),
  making them strong against deep targets and lined-up blocks.
- **Sabot** torpedoes penetrate shields; **EMP** torpedoes deactivate them; **Ion** and **Anti-Matter**
  torpedoes drain energy. See [Torpedoes](Torpedoes).

## Resistances and weaknesses

Ships can carry upgrades (and NPCs can spawn with traits) that change how damage types apply:

- **Resistance** reduces incoming damage of one type. The *Shield Ionizer* upgrade resists one of
  **Physical, Plasma, Electric or Anti-Matter**, cutting that type's damage by **4%–30%** depending on
  rarity.
- **Weakness** increases incoming damage of one type. The *Hull Polarizer* upgrade greatly raises hull
  durability but makes the ship take **much more** damage (up to ~3×) from one of **Energy, Plasma,
  Electric or Anti-Matter**.

Both are detailed on **[Defensive systems](Defensive-systems)**. The practical lesson: a target with a
resistance is best hit with a *different* damage type than the one it resists, and a target with a known
weakness should be hit with that exact type.

## How weapon power scales

Two factors set a freshly generated turret's strength before crafting bonuses:

### Tech level and sector DPS
Turrets are generated for a galaxy position. The further toward the **core** (and the higher the
**tech level**), the higher the base **DPS** the generator is given to work with. This baseline comes
from the game's sector balancing, so weapons found near the rim are weak and weapons found near the
center are strong. A weapon's listed DPS is spread across its fire rate: slow, hard-hitting weapons and
fast, low-per-shot weapons can share the same DPS.

### Rarity
Rarity multiplies a weapon's damage on top of its tech baseline. Armed weapons scale by
$\text{factor} = 1 + 0.4 \times \text{rarity value}$:

| Rarity | Rarity value | Damage factor (armed) |
|---|:--:|:--:|
| Petty | −1 | ×0.6 |
| Common | 0 | ×1.0 |
| Uncommon | 1 | ×1.4 |
| Rare | 2 | ×1.8 |
| Exceptional | 3 | ×2.2 |
| Exotic | 4 | ×2.6 |
| Legendary | 5 | ×3.0 |

Mining and salvaging lasers scale much more gently with rarity ($1 + 0.05 \times \text{rarity value}$),
because their value comes mostly from **efficiency**, not damage. Higher rarity also widens the random
range on a weapon's secondary stats (extra elemental damage, block penetration, etc.).

## See also

- [Weapons](Weapons) – every turret weapon type, with damage type, fire rate and range
- [Turret crafting](Turret-crafting) – building turrets at a Turret Factory and the stats each ingredient raises
- [Torpedoes](Torpedoes) – torpedo bodies, warheads and damage
- [Defensive systems](Defensive-systems) – shields, resistances, weaknesses and point defense
- [Ship generation](Ship-generation) – how NPC volume, HP and turret counts scale with distance from the core

---
*Combat & Weapons: [Combat](Combat) · [Weapons](Weapons) · [Turret crafting](Turret-crafting) · [Torpedoes](Torpedoes) · [Defensive systems](Defensive-systems)*
