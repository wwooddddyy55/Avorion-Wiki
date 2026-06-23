<!-- Data page. Sourced from lib/torpedoutility.lua (Body and Warhead tables, damage types) and
     lib/torpedogenerator.lua (stat formulas, damage formula, body/warhead spawn weighting, rarity
     distribution). Numbers are what those scripts compute. -->
# Torpedoes

**Torpedoes** are large, single-use guided munitions, separate from turret [weapons](Weapons). They are
fired from **torpedo launchers** and stored in **torpedo tubes/storage**, fly to the target under their
own power, and detonate for a big burst of damage. Every torpedo is a combination of a **body** (its
flight characteristics) and a **warhead** (its damage profile and special effect).

A torpedo's name reflects both halves — e.g. *"Eagle-Class Plasma Torpedo"* pairs the **Eagle** body
with a **Plasma** warhead. This page lists both catalogs and how a torpedo's stats are derived.

## How torpedo stats are derived

When a torpedo is generated it is given a base **DPS** and **tech level** from its galaxy position
(further toward the core = stronger), a **rarity**, a body and a warhead. From those:

| Stat | How it's set |
|---|---|
| **Durability** | $(2 + \text{tech}/10) \times (\text{rarity value} + 1) + 4$ — how much punishment the torpedo can take before being shot down. |
| **Max velocity** | $250 + 100 \times \text{body velocity rating}$ (so 350 / 450 / 550). |
| **Turning speed** | $0.3 + 0.1 \times (2 \times \text{agility rating} - 1)$ — agility 1/2/3 → 0.4 / 0.6 / 0.8. |
| **Range (reach)** | $(\text{body reach rating} \times 4 + 3 \times \text{rarity value}) \times 150$. |
| **Size** | body size × warhead size (rounded). Bigger torpedoes take more storage space. |
| **Base damage** | $\text{damage} = \text{DPS} \times (1 + 0.25 \times \text{rarity value}) \times 10$, then split into shield and hull damage by the warhead's multipliers below (rounded to the nearest 100). |

So **shield damage** ≈ base damage × warhead shield factor, and **hull damage** ≈ base damage × warhead
hull factor.

## Bodies

The **body** sets how the torpedo flies — speed, agility, range and physical size. Faster, more agile,
longer-reaching bodies are larger and appear closer to the galaxy core. Body color is a flavour grouping
(blue = slow, red = medium, yellow = fast).

| Body | Velocity rating | Agility rating | Reach rating | Size | Group |
|---|:--:|:--:|:--:|--:|---|
| **Orca** | 1 | 1 | 4 | 1.0 | Blue |
| **Hammerhead** | 1 | 2 | 5 | 1.5 | Blue |
| **Stingray** | 1 | 3 | 6 | 2.5 | Blue |
| **Ocelot** | 2 | 1 | 5 | 1.5 | Red |
| **Lynx** | 2 | 2 | 6 | 2.5 | Red |
| **Panther** | 2 | 3 | 7 | 3.5 | Red |
| **Osprey** | 3 | 1 | 6 | 2.5 | Yellow |
| **Eagle** | 3 | 2 | 7 | 3.5 | Yellow |
| **Hawk** | 3 | 3 | 8 | 5.0 | Yellow |

Higher ratings are strictly better (faster / more agile / longer-ranged) but cost more **size**, so a
high-end body holds fewer in storage. The best bodies (Hawk, Eagle, Panther) only generate in
deeper-core sectors.

## Warheads

The **warhead** sets the damage type, the shield/hull split, and any special effect. The multipliers
below scale the torpedo's base damage against each pool.

| Warhead | Damage type | Hull ×| Shield ×| Size | Special effect |
|---|---|--:|--:|--:|---|
| **Nuclear** | Physical | 1.0 | 1.0 | 1.0 | Balanced all-rounder. |
| **Neutron** | Physical | 3.0 | 1.0 | 1.0 | Heavy anti-hull. |
| **Fusion** | Energy | 1.0 | 3.0 | 1.0 | Heavy anti-shield. |
| **Tandem** | Physical | 1.5 | 2.0 | 1.5 | **Damages shield and hull at once.** |
| **Kinetic** | Physical | 2.5 | 0.25 | 1.5 | Damage scales with **impact velocity** (flies twice as fast); anti-hull ram. |
| **Ion** | Energy | 0.25 | 3.0 | 2.0 | **Drains target energy**; strong vs shields. |
| **Plasma** | Plasma | 1.0 | 5.0 | 2.0 | Massive anti-shield. |
| **Sabot** | Physical | 2.0 | 0.0 | 3.0 | **Penetrates shields** — ignores them and hits hull directly. |
| **EMP** | Electric | 0.0 | 0.025 | 3.0 | **Deactivates shields** rather than damaging them. |
| **Anti-Matter** | Anti Matter | 8.0 | 6.0 | 5.0 | Enormous damage to both pools; **drains stored energy**. The premium warhead. |

As with bodies, the heavier/more specialised warheads (Anti-Matter, EMP, Sabot, Plasma, Ion) generate
nearer the core and add the most **size**, so they take the most storage room.

## Choosing a torpedo

- **Against shields:** Plasma (raw damage), Fusion, or Ion (also drains energy). **EMP** turns shields
  off outright, and **Sabot** simply ignores them.
- **Against hull:** Neutron, Kinetic, or — once shields are down — **Anti-Matter** for the biggest hit.
- **Don't know / both:** Nuclear (balanced) or **Tandem** (hits shield and hull together).
- **Body:** prefer higher **velocity** and **agility** so the torpedo reaches a maneuvering target
  before point defense shoots it down — but watch the **size**, which limits how many you can carry.

> Torpedoes are vulnerable in flight: **Point Defense** and **Anti-Fighter** turrets ([Weapons](Weapons))
> target and destroy them, and their **durability** decides how much fire they survive. EMP/Sabot/Plasma
> warheads paired with a fast body are the usual answer to a well-defended target.

## Rarity

Found torpedoes follow the standard rarity weighting (lower rarities are far more common):

| Rarity | Relative weight |
|---|--:|
| Common | 128 |
| Uncommon | 32 |
| Rare | 16 |
| Exceptional | 8 |
| Exotic | 1 |
| Legendary | 0.1 |

Higher rarity raises base damage (+25% of base per rarity step), durability and range.

## See also

- [Weapons](Weapons) – turret weapons, including the point defense that shoots torpedoes down
- [Combat](Combat) – damage types and shield/hull interactions the warheads exploit
- [Defensive systems](Defensive-systems) – shields, shield piercing and point defense
- [Goods](Goods) – warhead-related military goods

---
*Combat & Weapons: [Combat](Combat) · [Weapons](Weapons) · [Turret crafting](Turret-crafting) · [Torpedoes](Torpedoes) · [Defensive systems](Defensive-systems) · [Fighters](Fighters)*
