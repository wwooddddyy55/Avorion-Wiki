<!-- Hand-written catalog page. Sourced from lib/weapontype.lua (the type list/armament) and
     lib/weapongenerator.lua (per-type fire delay, reach, projectile speed, damage type and special
     behaviour). Numeric ranges are the rand:getFloat()/getInt() spans the generator rolls within. -->
# Weapons

**Weapons** in Avorion are mounted as **turrets** (and as **fighters**, which carry a turret's stats).
Every turret is one of the weapon types below. A turret is **procedurally generated** from a galaxy
position, a **tech level**, a **[rarity](Combat#rarity)** and a **material**, so two turrets of the same
type can differ widely in damage, range and fire rate. This page lists each type's fixed character: how
it fires, its base **[damage type](Combat#damage-types)**, and its typical range and rate.

For how damage applies to shields and hull, see **[Combat](Combat)**. For building your own turrets, see
**[Turret crafting](Turret-crafting)**.

> **In short:** match the weapon to the target. **Against shields** use Energy/Plasma (Laser, Plasma Gun);
> **against hull** use Physical/Anti-Matter (Cannon, Bolter, Railgun); **against fighters and torpedoes**
> use Point Defense and Anti-Fighter guns; **all-rounders** are Electric (Tesla, Lightning). A weapon's
> listed numbers are *generation ranges* — real damage comes from its tech and rarity. See
> [Choosing a weapon](#choosing-a-weapon).

## Weapon attributes

| Attribute | Meaning |
|---|---|
| **Class** | **Armed** (offensive turrets), **Defensive** (point defense / anti-fighter, auto-targeting small threats), or **Unarmed** (mining, salvaging, repair, tractor). |
| **Mechanism** | **Projectile** (travels at a speed, can miss/lead) or **Beam** (hits instantly along its length; *continuous* beams stream damage, *pulsed* beams fire shots). |
| **Damage type** | The weapon's base [damage type](Combat#damage-types). Some types roll a chance of a bonus element (see [Elemental rolls](#elemental-damage-rolls)). |
| **Fire interval** | Seconds between shots. Lower = faster. Beams use a fixed 0.2 s internally. |
| **Range** | The weapon's reach, in in-game units. |
| **Projectile speed** | How fast shots travel (projectiles only). Slow shots must be led; fast shots are easier to land. |

> The numbers below are the **generation ranges** the game rolls within for a brand-new turret of that
> type. Actual damage is set separately by sector DPS, tech and rarity ([Combat](Combat#how-weapon-power-scales)),
> and crafting can shift fire rate, range and damage further ([Turret crafting](Turret-crafting)).

## Armed weapons

The main offensive turrets. One of these rolls randomly when a generic "armed" turret is generated.

| Weapon | Mechanism | Damage type | Fire interval (s) | Range | Proj. speed | Notable behaviour |
|---|---|---|--:|--:|--:|---|
| **Chaingun** | Projectile | Physical | 0.08–0.12 | 300–450 | 500–700 | Very high rate of fire; small chance of a burst (2–4 shots) or a bonus element. |
| **Bolter** | Projectile | Anti Matter | 0.10–0.30 | 650–700 | 800–1000 | Always Anti-Matter (heavy hull bonus); fast shots; can roll bursts. |
| **Plasma Gun** | Projectile | Plasma | 0.15–0.20 | 550–800 | 500–700 | Always carries a large shield-damage bonus; melts shields. |
| **Pulse Cannon** | Projectile | Physical | 0.05–0.20 | 450–750 | 700–800 | **Penetrates shields** to hit hull; base DPS reduced 25% to compensate. |
| **Cannon** | Projectile | Physical | 1.50–2.50 | 1100–1500 | 600–800 | Slow, hard-hitting; shells explode on impact (splash). |
| **Rocket Launcher** | Projectile | Physical | 0.50–1.50 | 1300–1800 | 150–200 | Longest range; explosive impact; **1-in-8** chance to be **seeking** (homing). |
| **Railgun** | Beam (pulsed) | Physical | 1.00–2.50 | 950–1400 | — | Near-perfect accuracy; **block penetration** (3 up to 5 + 2×rarity), hits multiple blocks in a line. |
| **Laser** | Beam (continuous) | Energy | 0.20 | 450–750 | — | Steady shield damage; 10% chance of a bonus Plasma roll. |
| **Lightning Gun** | Beam (pulsed) | Electric | 1.00–2.50 | 950–1400 | — | Hits shields and hull equally; long range; 10% Plasma chance. |
| **Tesla Gun** | Beam (continuous) | Electric | 0.20 | 250–350 | — | Short range, constant Electric damage to both pools; 10% Plasma chance. |

## Defensive weapons

These auto-target **fighters, torpedoes and other small fast objects** and use the **Fragments**
damage type. They are weak against ships but excellent screening tools.

| Weapon | Mechanism | Damage type | Fire interval (s) | Range | Proj. speed | Notable behaviour |
|---|---|---|--:|--:|--:|---|
| **Point Defense Cannon** | Projectile | Fragments | 0.075–0.10 | 700–750 | 1000–1100 | Very fast, very accurate (≈0.995); shreds fighters/torpedoes. |
| **Point Defense Laser** | Beam (continuous) | Fragments | 0.20 | 500–600 | — | Instant-hit point defense; low damage but never misses fast targets. |
| **Anti-Fighter Gun** | Projectile | Fragments | 2.00–2.50 | 300–350 | 300–400 | Flak: shells explode (radius ≈35) for area damage against fighter swarms. |

## Unarmed weapons

Utility turrets. They deal little or no combat damage and instead mine, salvage, repair or push.

| Weapon | Mechanism | Damage type | Fire interval (s) | Range | Purpose |
|---|---|---|--:|--:|---|
| **Mining Laser** | Beam (continuous) | Energy | 0.20 | 75 | Mines asteroids; yields **refined** material directly (efficiency ≈15%+). |
| **R-Mining Laser** | Beam (continuous) | Energy | 0.20 | 150 | "Raw" mining: longer reach, yields **raw ore** at much higher efficiency (≈63%+) for later refining. |
| **Salvaging Laser** | Beam (continuous) | Energy | 0.20 | 75 | Salvages wreckage into **refined** material (efficiency ≈12%+). |
| **R-Salvaging Laser** | Beam (continuous) | Energy | 0.20 | 150 | "Raw" salvaging: longer reach, yields **raw scrap** at higher efficiency (≈45%+). |
| **Repair Beam** | Beam (continuous) | Energy | 0.20 | 200–300 | Repairs a friendly ship's **hull or shield** (each beam does one or the other). Hull beams pierce shields. |
| **Force Gun** | Beam (continuous) | — | 0.20 | 450–550 | A **tractor beam**: no damage, applies holding force (≈1,500 up to ~1.5 million) scaling with tech and rarity, to pull objects. |

> **Mining vs. raw mining:** standard mining/salvaging lasers give you ready-to-use materials but in
> small amounts; the **R-** ("raw") variants extract far more, as ore/scrap that you then process at a
> refinery. See [Refining](Refining) for the ore-to-material step.

## Elemental damage rolls

Several armed weapons can roll a **bonus damage type** when generated, changing their base type:

| Weapon | Bonus roll |
|---|---|
| **Bolter** | 100% Anti-Matter (always). |
| **Plasma Gun** | 100% Plasma (always). |
| **Lightning Gun / Tesla Gun** | 100% Electric, plus 10% chance of additional Plasma. |
| **Laser** | 10% chance of Plasma. |
| **Cannon / Railgun / Rocket Launcher / Pulse Cannon** | 10% chance of Anti-Matter. |
| **Chaingun** | 7.5% Anti-Matter, else 7.5% Plasma, else 5% Electric. |

A bonus elemental roll adds a large multiplier against the relevant pool — Anti-Matter against hull,
Plasma against shields — so an elemental-rolled weapon of the same DPS is markedly better against the
right target. See [Damage types](Combat#damage-types).

## Choosing a weapon

There's no single best turret — pick by **what you're shooting** and **how you fly**:

- **Strip shields fast:** **Plasma Gun** (huge shield bonus) or **Laser** (steady, accurate Energy). Open
  with these, then switch to a hull weapon once shields drop.
- **Tear through hull:** **Bolter** (always Anti-Matter) and **Cannon** (slow, hard, splash). **Railgun**
  adds block penetration to hit deep, lined-up blocks — great against big ships.
- **One weapon for everything:** **Tesla** / **Lightning Gun** (Electric) hit shields and hull equally —
  flexible when you don't want to swap loadouts. Lightning reaches far; Tesla is short-range.
- **Shoot past shields:** **Pulse Cannon** penetrates shields to hit hull directly (at −25% base damage).
- **Kill fighters & torpedoes:** equip **Point Defense** (Cannon or Laser) and **Anti-Fighter** guns —
  they auto-target small fast threats your main guns can't track. Essential against carriers and torpedo
  bosses (see [Defensive systems](Defensive-systems)).
- **Beginner-friendly:** beams (Laser, Tesla) hit instantly and never need leading, so they're the easiest
  to land while you learn; slow projectiles (Cannon, Rocket) hit hard but must be aimed ahead of a moving
  target.
- **Mining vs combat:** mining and salvaging are done with the **unarmed** lasers above — keep a dedicated
  mining turret or ship rather than expecting combat guns to harvest.

Whatever the type, **higher tech level and rarity** matter more for raw damage than the type itself — see
[How weapon power scales](Combat#how-weapon-power-scales).

## See also

- [Combat](Combat) – damage types, shields vs hull, and how weapon power scales
- [Turret crafting](Turret-crafting) – building turrets and the stat each ingredient raises
- [Torpedoes](Torpedoes) – the other main weapon system
- [Defensive systems](Defensive-systems) – shields and point defense against these weapons
- [System upgrades](System-upgrades) – Turret Control Subsystems that add armed, unarmed and auto turret slots

---
*Combat & Weapons: [Combat](Combat) · [Weapons](Weapons) · [Turret crafting](Turret-crafting) · [Torpedoes](Torpedoes) · [Defensive systems](Defensive-systems)*
