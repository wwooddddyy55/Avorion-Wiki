<!-- Data page. Sourced from lib/turretingredients.lua (per-weapon ingredient lists: amount,
     investable, minimum, and the weaponStat/turretStat each booster raises with its investFactor
     and changeType). Weapon types and classes from lib/weapontype.lua. -->
# Turret crafting

At a **Turret Factory** you can build your own turrets from **goods** plus a **material** and a base
turret/weapon. Each weapon type needs a fixed list of **ingredients**. Some ingredients are pure
build cost, but others are **investable**: adding more of them than the minimum **boosts a specific
stat** of the finished turret (fire rate, range, damage, and so on).

This page lists the ingredients for every weapon type and which stat each one raises. For what the
weapons themselves do, see **[Weapons](Weapons)**; for the goods, see **[Goods](Goods)**.

> **In short:** building your own turret lets you **pour extra goods into the stat you care about**. Each
> weapon's *investable* ingredients each pump one stat (damage, fire rate, range, or — on mining/salvaging
> lasers — efficiency). Decide the turret's job first, then max the matching ingredient: **damage** for
> burst/sniper guns, **fire rate** for sustained DPS and fighter defence, **range** for stand-off
> weapons, **efficiency** for harvesters. See [What to invest in](#what-to-invest-in).

## What to invest in

You can't max everything — investable goods are capped per ingredient — so invest toward the turret's
**role**:

- **Damage** — best on slow, hard-hitting guns (Cannon, Railgun, Bolter) where each shot already lands
  heavy; turns them into alpha-strike weapons.
- **Fire rate** — best on fast guns (Chaingun, Laser) and on **point-defense**, where more shots per
  second means more fighters and torpedoes swatted.
- **Range** — lets a weapon open fire before the enemy can, valuable on snipers and on ships that kite.
- **Efficiency** (mining & salvaging lasers) — the only stat that matters on harvesters: it directly
  raises how much ore/material you extract, so always max it on a mining or salvaging build.

Remember that **tech level and rarity** of the base turret set its raw power; crafting investment shifts
*which way* that power leans. A well-invested mid-tech turret can out-perform a careless high-rarity one
for its intended job.

## How crafting ingredients work

*[📷 Screenshot needed — ASSETS.md: images/turret-factory-ui.png]*

Each ingredient row has up to four numbers:

| Field | Meaning |
|---|---|
| **Amount** | The base quantity required to build the turret. |
| **Investable** | The maximum **extra** units you may add on top, to boost a stat. |
| **Min** | The minimum that must be present (some boosters can be dropped to 0). |
| **Boosts** | The turret stat this ingredient raises as you invest more of it. Blank = build cost only. |

Investing in a **Boosts** ingredient trades goods for performance: more *Servos* means a faster fire
rate, more *Laser Compressors* means more damage, and so on. A boost is either a **percentage** scaling
of the stat or a **flat** addition (noted below). Damage, range and fire-rate boosts are the usual
levers; mining/salvaging turrets instead invest into **efficiency**.

> Ingredient lists are by **weapon type** and do not change with rarity, but the *cost* of a turret
> scales with its tech level and rarity. A few boosts also scale their effect with the turret's rarity.

## Armed weapons

### Chaingun
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 15 | 10 | 3 | Fire rate |
| Steel Tube | 6 | 7 | — | Range |
| Ammunition S | 5 | 10 | 1 | Damage |
| Steel | 5 | 10 | 3 | — |
| Aluminum | 7 | 5 | 3 | — |
| Lead | 10 | 10 | 1 | — |

### Bolter
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 15 | 8 | 5 | Fire rate |
| High Pressure Tube | 1 | 3 | — | Range |
| Ammunition M | 5 | 10 | 1 | Damage |
| Explosive Charge | 2 | 4 | 1 | Damage |
| Steel | 5 | 10 | 3 | — |
| Aluminum | 7 | 5 | 3 | — |

### Plasma Gun
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Plasma Cell | 8 | 4 | 1 | Damage |
| Energy Tube | 2 | 6 | 1 | Range |
| Conductor | 5 | 6 | 1 | — |
| Energy Container | 5 | 6 | 1 | — |
| Power Unit | 5 | 3 | 3 | Max heat (cooling) |
| Steel | 4 | 10 | 3 | — |
| Crystal | 2 | 10 | 1 | — |

### Pulse Cannon
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 8 | 8 | 3 | Fire rate |
| Steel Tube | 6 | 7 | — | Range |
| Ammunition S | 5 | 10 | 1 | Damage |
| Steel | 5 | 10 | 4 | — |
| Copper | 5 | 10 | 3 | — |
| Energy Cell | 3 | 5 | 2 | — |

### Cannon
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 15 | 10 | 5 | Fire rate |
| Warhead | 5 | 6 | 1 | Damage |
| High Pressure Tube | 2 | 6 | 1 | Range |
| Explosive Charge | 2 | 6 | 1 | Damage |
| Steel | 8 | 10 | 3 | — |
| Wire | 5 | 10 | 3 | — |

### Rocket Launcher
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 15 | 10 | 5 | Fire rate |
| Rocket | 5 | 6 | 1 | Damage |
| High Pressure Tube | 2 | 6 | 1 | Range |
| Fuel | 2 | 6 | 1 | Range |
| Targeting Card | 5 | 5 | 0 | Homing/seeker *(flat)* |
| Steel | 8 | 10 | 3 | — |
| Wire | 5 | 10 | 3 | — |

### Railgun
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 15 | 10 | 6 | Fire rate |
| Electromagnetic Charge | 5 | 6 | 1 | Damage |
| Electro Magnet | 8 | 10 | 3 | Range |
| Gauss Rail | 5 | 6 | 1 | Damage |
| High Pressure Tube | 2 | 6 | 1 | Range |
| Steel | 5 | 10 | 3 | — |
| Copper | 2 | 10 | 1 | — |

### Laser
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Laser Head | 4 | 4 | — | Damage |
| Laser Compressor | 2 | 2 | — | Damage |
| High Capacity Lens | 2 | 4 | — | Range |
| Laser Modulator | 2 | 4 | 2 | — |
| Power Unit | 5 | 3 | 3 | Max heat (cooling) |
| Steel | 5 | 10 | 3 | — |
| Crystal | 2 | 10 | 1 | — |

### Lightning Gun
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Military Tesla Coil | 5 | 6 | 1 | Damage |
| High Capacity Lens | 2 | 4 | 1 | Range |
| Electromagnetic Charge | 2 | 4 | 1 | — |
| Conductor | 5 | 6 | 2 | — |
| Power Unit | 5 | 3 | 3 | Max heat (cooling) |
| Copper | 5 | 10 | 3 | — |
| Energy Cell | 5 | 10 | 3 | — |

### Tesla Gun
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Industrial Tesla Coil | 5 | 6 | 1 | Damage |
| Electromagnetic Charge | 2 | 4 | 1 | Range |
| Energy Inverter | 2 | 4 | 1 | — |
| Conductor | 5 | 6 | 2 | — |
| Power Unit | 5 | 3 | 3 | Max heat (cooling) |
| Copper | 5 | 10 | 3 | — |
| Energy Cell | 5 | 10 | 3 | — |

## Defensive weapons

### Point Defense Cannon
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 17 | 8 | 10 | Fire rate |
| Steel Tube | 8 | 5 | — | Range |
| Ammunition S | 5 | 5 | 1 | Damage |
| Steel | 3 | 7 | 3 | — |
| Aluminum | 7 | 5 | 3 | — |
| Lead | 10 | 10 | 1 | — |

### Point Defense Laser
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 17 | 8 | 10 | Fire rate |
| Laser Head | 2 | 2 | 1 | Damage |
| Laser Compressor | 2 | 1 | — | Damage |
| High Capacity Lens | 2 | 4 | — | Range |
| Laser Modulator | 2 | 4 | — | — |
| Steel | 5 | 10 | 3 | — |
| Crystal | 2 | 10 | 1 | — |

### Anti-Fighter Gun
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Servo | 17 | 8 | 10 | Fire rate |
| High Pressure Tube | 1 | 3 | — | Range |
| Ammunition M | 5 | 5 | 1 | Damage |
| Explosive Charge | 2 | 4 | 1 | Damage |
| Steel | 5 | 10 | 3 | — |
| Aluminum | 7 | 5 | 3 | — |

## Unarmed weapons

### Mining Laser
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Laser Compressor | 5 | 6 | 1 | Damage |
| Laser Modulator | 2 | 4 | 0 | Mining efficiency *(flat)* |
| High Capacity Lens | 2 | 6 | 0 | Range |
| Conductor | 5 | 6 | 2 | — |
| Steel | 5 | 10 | 3 | — |

### R-Mining Laser
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Laser Compressor | 5 | 6 | 1 | Damage |
| Laser Modulator | 2 | 4 | 0 | Raw mining efficiency *(flat)* |
| High Capacity Lens | 2 | 6 | 0 | Range |
| Conductor | 5 | 6 | 2 | — |
| Steel | 5 | 10 | 3 | — |

### Salvaging Laser
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Laser Compressor | 5 | 6 | 1 | Damage |
| Laser Modulator | 2 | 4 | 0 | Salvage efficiency *(flat)* |
| High Capacity Lens | 2 | 6 | 0 | Range |
| Conductor | 5 | 6 | 2 | — |
| Steel | 5 | 10 | 3 | — |

### R-Salvaging Laser
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Laser Compressor | 5 | 6 | 1 | Damage |
| Laser Modulator | 2 | 4 | 0 | Raw salvage efficiency *(flat)* |
| High Capacity Lens | 2 | 6 | 0 | Range |
| Conductor | 5 | 6 | 2 | — |
| Steel | 5 | 10 | 3 | — |

### Repair Beam
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Nanobot | 5 | 6 | 1 | Hull repair |
| Transformator | 2 | 6 | 1 | Shield repair |
| Laser Modulator | 2 | 5 | 0 | Range |
| Conductor | 2 | 6 | 0 | Energy use *(reduces drain)* |
| Gold | 3 | 10 | 1 | — |
| Steel | 8 | 10 | 3 | — |

### Force Gun
| Ingredient | Amount | Investable | Min | Boosts |
|---|--:|--:|--:|---|
| Force Generator | 5 | 3 | 1 | Holding force |
| Energy Tube | 2 | 6 | 1 | Range |
| Conductor | 10 | 6 | 2 | — |
| Steel | 7 | 10 | 3 | — |
| Zinc | 3 | 10 | 3 | — |

## See also

- [Weapons](Weapons) – what each crafted weapon type does in combat
- [Combat](Combat) – damage types and how weapon power scales
- [Goods](Goods) – the commodities used as ingredients
- [Production](Production) – factories that produce those goods

---
*Combat & Weapons: [Combat](Combat) · [Weapons](Weapons) · [Turret crafting](Turret-crafting) · [Torpedoes](Torpedoes) · [Defensive systems](Defensive-systems) · [Fighters](Fighters)*
