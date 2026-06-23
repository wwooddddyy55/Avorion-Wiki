<!-- Hand-written mechanics page. Code lineage (kept out of the reader-facing text on purpose):
     Fighter stats & generation: data/scripts/lib/fightergenerator.lua (generateFighter/addWeapons/
       generateUnarmedFighter: durability = maxDurability × rarity-lerp(-1..5 → 0.2..1.0) × 1.2^material;
       turningSpeed 1..2.5; maxVelocity 30..60; 20% chance shield = maxDurability × 0.25..0.5;
       projectile fireRate >2 reduced to 1..2 and reach min(reach,350); weapon holdingForce ×0.4);
     data/scripts/lib/fighterutility.lua (getMaxDurability lerp by Balancing_GetSectorByTechLevel:
       hp 1200 near core → 200 far rim; getProductionTime tech/material/durability).
     Factory build: data/scripts/entity/merchants/fighterfactory.lua (tax 0.2; interaction threshold
       30000; types Combat Fighter / Boarding Shuttle via FighterType.Fighter/CrewShuttle, CrewShuttle
       rarity = Rarity(2); getMaxAvailablePoints = 10 + 5×rarity, getMaxInvestablePoints = 8 + rarity,
       maxPoints 9; getStats lerp size 2.0→1.0, durability/turn/velocity by points; addMaterialBonuses
       free points per material; makeFighter weapon damage ×0.4/turret.slots, fireRateFactor by cooling;
       getUnarmedTurretType mining/refiningMining/salvage/refiningSalvage/repair; plan ≤200 blocks).
     Buy/squad placement: data/scripts/lib/sellablefighter.lua (boughtByPlayer: Hangar(ship.index),
       hangar.freeSpace vs fighter.volume, getSquads/getSquadFreeSlots/fighterTypeMatchesSquad/addSquad/
       maxSquads/addFighter; canBeBought relation gates: Bad/Hostile none, Ceasefire no military,
       Rare→Good, Exceptional→Excellent, Exotic→Allied; resale price ÷8).
     Fighter Control System: data/scripts/systems/fightersquadsystem.lua (StatsBonuses.FighterSquads +
       ProductionCapacity when permanent; "Controls additional fighter squadrons (10 max)"; energy
       = squads × 600 MW ÷ 1.1^rarity). Modded squad system: see wiki/pages/Xavorion-Weaponry.md.
     Anti-fighter counters & Fragments damage: Weapons.md / Combat.md / Defensive-systems.md.
     Image assets: see wiki/ASSETS.md. -->
# Fighters

**Fighters** are tiny one-pilot craft launched from a ship's **Hangar**. Each one is, in effect, a
**single turret bolted to a small hull** — it carries that turret's weapon (at reduced power), flies on its
own AI, and fights, mines or salvages without you steering it. A ship that carries fighters is a **carrier**;
the fighters fly in **squads**, are crewed by **Pilots**, and return to the hangar when the carrier jumps or
the fight ends. This page explains what a fighter's stats mean, how to get and build one, and when they're
worth flying.

> **In short:** a fighter is a **turret on a small hull**. Get them three ways — **buy** them at an
> equipment dock, **build** them at a **Fighter Factory** from one of your own turrets, or **produce** them
> aboard a carrier. They hit harder, fly faster and survive longer with higher **tech, material and rarity**.
> How many you can field is set by your **Hangar space**, your **squads**, and a **Fighter Control System**
> ("Hydra") subsystem. Fighters excel at **automated mining/salvaging**, **swarming big slow ships** and
> **boarding** — but a screen of **point-defense and anti-fighter flak** shreds them, so don't send them at a
> target that's bristling with it.

*[📷 Screenshot needed — ASSETS.md: images/fighter-squad.png]*

## Fighter stats

A fighter's tooltip shows five numbers plus its weapon. Every one of them is driven by some mix of the
**tech level**, **material** and **rarity** of the turret (or design) it was made from — the same three dials
that drive turret power (see [Weapons](Weapons)).

| Stat | What it means | What drives it |
|---|---|---|
| **Durability** | The fighter's hit points. | **Tech** sets the base — roughly **1,200 HP** for high-tech fighters near the core down to **~200 HP** in the far rim. Then **× material** (each tier ≈ +20%) **× rarity** (Petty ≈ 0.2 → Legendary 1.0). High-tech + high-material + high-rarity fighters are *far* tougher. |
| **Shield** | A small regenerating buffer on top of HP. | Only **looted/bought** fighters roll one — a **20% chance** of a shield worth **25–50%** of the fighter's HP. Factory-built fighters have none. |
| **Maneuverability** | How fast it turns to track a target or dodge. | Rolls **1.0–2.5**; raised by build points and by nimble materials (Titanium, Trinium). |
| **Speed** | Top flight speed. | Rolls **30–60** (shown ×10 in the UI); raised by build points and by Xanion. |
| **Size** | The hangar volume each fighter eats. **Smaller is better** — small fighters let you pack more into the same Hangar. | Lower with more "Size" build points; **Iron** makes the smallest fighters. |
| **Weapon** | The turret's gun, **at reduced power**. | A fighter deals the source turret's damage **× 0.4 ÷ its slot count**, so a **1-slot** turret makes a much stronger fighter than a big multi-slot one of the same stats. Fast guns are throttled to **1–2 shots/s** and range is capped (~3.5 km). |

The takeaway: chase **high-tech, high-rarity** turrets for your fighters, prefer **low-slot** turrets as the
donor, and pick the **material** for the personality you want (below).

## Where fighters come from

There are three ways to get a fighter into your hangar:

- **Buy them** at an **Equipment Dock** or **Fighter Merchant**. Quick, but you take whatever's in stock, and
  **faction relations gate what you're allowed to buy** (see the table below).
- **Build them at a [Fighter Factory](#building-one-at-a-fighter-factory)** — turn one of *your own* turrets
  into a fighter to your specification. This is the main way to get exactly the fighter you want.
- **Produce them aboard a carrier.** A ship with a **Hangar** and enough **Production Capacity** (from
  Assembly blocks — see [Ship stats](Ship-stats)) rebuilds lost fighters over time from a stored blueprint.
  A higher-tech, tougher fighter takes longer to build.

### What you're allowed to buy

Buying fighters from an NPC faction is gated by your standing with them (armed "military" fighters are held to
a higher bar than unarmed ones):

| Your relation | What you can buy |
|---|---|
| **Bad / Hostile** | Nothing |
| **Ceasefire** | Unarmed fighters only — no military fighters |
| **Neutral+** | Up to **Uncommon** |
| **Good** | Up to **Rare** (military) |
| **Excellent** | Up to **Exceptional** (military) |
| **Allied** | Everything, including **Exotic** and **Legendary** |

See [Diplomacy and Reputation](Diplomacy-and-Reputation) for how relations move.

## Building one at a Fighter Factory

A **Fighter Factory** is a station that turns parts you supply into a finished fighter. You need decent
standing with its faction to use it. To build one you provide:

1. **A saved fighter design** — any ship/fighter blueprint of **200 blocks or fewer** (this is just the
   cosmetic hull; the factory scales it to fighter size).
2. **A turret** from your inventory — this is the heart of the fighter and sets its **tech, material, rarity**
   and **weapon**. Building the fighter **consumes the turret**.
3. **A type** — **Combat Fighter** (from an armed turret) or **Boarding Shuttle**.

You then spend a pool of **stat points** across **Size, Durability, Maneuverability and Speed**, and pay the
price (the factory adds a **20% tax** unless it's your own faction's station). *Pilots are not included* — you
crew the fighter separately.

**The point budget scales with the turret's rarity:**

- **Total points to spend** = `10 + 5 × rarity` (so a Common turret gives ~15, a Legendary one ~35).
- **Per-stat cap** = `8 + rarity` — you can't dump the whole budget into one stat.

**Material grants free bonus points**, so the turret's material gives each fighter a personality — the same
trade-off idea as turret materials:

| Material | Free bonus points |
|---|---|
| **Iron** | **+4 Size** (smallest fighters — pack more per hangar) |
| **Titanium** | +1 Durability, **+2 Maneuverability**, +1 Speed |
| **Naonite** | +2 Durability, +1 Maneuverability, +1 Speed |
| **Trinium** | **+3 Maneuverability**, +1 Speed |
| **Xanion** | +1 Durability, **+3 Speed** |
| **Ogonite** | **+5 Durability** (toughest) |
| **Avorion** | +2 to **all four** stats |

So if you want a swarm of tiny, durable, hard-hitting fighters, the donor turret's material matters as much as
its rarity.

## Fighter types

Not every fighter carries a gun. The type is decided by the **turret** you build it from:

- **Combat fighters** — built from an **armed** turret; they fight automatically.
- **Unarmed fighters** — built from an unarmed turret, inheriting its job: **mining**, **salvaging**,
  **refining-mining**, **refining-salvaging**, or **repair** fighters. These are how a carrier mines or
  salvages a whole field hands-free.
- **Boarding Shuttles** — carry crew to **board and capture** enemy ships (see [Combat](Combat)). They're a
  fixed **Uncommon** quality and don't need a turret.

A squad holds **one type only**, so keep your combat, mining and salvage fighters in separate squads.

## Squads, hangars & the Fighter Control System

Fighters are stored in a **Hangar** block, which provides **hangar space** (measured in volume — smaller
fighters fit more). Inside the hangar they're organised into **squads**:

- Each **squad** holds fighters of a **single type**, and you launch and command squads as units.
- A new fighter drops into a matching squad if there's room, or starts a new squad — up to your **squad
  limit**.
- The **Fighter Control System** subsystem (the *"Hydra"*, an upgrade you slot into a subsystem socket) raises
  that limit: it adds **fighter squadrons** (more with higher rarity), up to a hard cap of **10 squads**.
  **Permanently installing** it also grants **Production Capacity**, speeding up how fast the carrier rebuilds
  lost fighters. Its **energy draw scales with the squads it grants** (≈600 MW per squad, eased by rarity), so
  budget reactor power for it — see [System upgrades](System-upgrades) and [Ship stats](Ship-stats).

> The [Xavorion: Weaponry](Xavorion-Weaponry) mod ships its own version of this subsystem with a
> rarity-scaled production bonus — see that page if you play with the mod suite.

## Best uses & counters

**Where fighters shine:**

- **Automated mining & salvaging.** Mining/salvage fighters work a whole asteroid field or wreck site on
  their own while you do something else — the most popular reason to run a carrier early on.
- **Swarming big, slow ships.** A wing of fighters splits a capital's fire across many small, fast targets;
  individually weak, together they grind down a target that can't track them.
- **Boarding.** Shuttles let you **capture** ships instead of destroying them.
- **Hands-off fleet work.** A carrier captain (see [Captains](Captains) and [Fleet commands](Fleet-commands))
  can mine, salvage or patrol a sector with its fighters while you're elsewhere.

**Their weakness — and what kills them:** fighters are fragile and clustered, exactly what **point-defense**
and **anti-fighter** weapons are built to kill. **Point Defense Cannons/Lasers** and flak **Anti-Fighter
Guns** (using the **Fragments** damage type) shred a swarm in seconds — see [Weapons](Weapons) and
[Defensive systems](Defensive-systems). Don't throw fighters at a target screened with it; conversely, mount
point-defense on *your* ships to protect against enemy fighters and torpedoes.

## See also

- [Weapons](Weapons) — the turret types fighters are built from, plus the point-defense/anti-fighter guns that counter them
- [Combat](Combat) — damage types, the Fragments anti-fighter type, and boarding
- [Defensive systems](Defensive-systems) — point defense on the receiving end of a fighter swarm
- [Ship stats](Ship-stats) — Hangar Space, Production Capacity and crew (Pilots)
- [System upgrades](System-upgrades) — the Fighter Control System and other subsystems
- [Captains](Captains) and [Fleet commands](Fleet-commands) — running a carrier on autopilot
- [Xavorion: Weaponry](Xavorion-Weaponry) — the mod suite's fighter-squad subsystem

---
*Combat & Weapons: [Combat](Combat) · [Weapons](Weapons) · [Turret crafting](Turret-crafting) · [Torpedoes](Torpedoes) · [Defensive systems](Defensive-systems) · [Fighters](Fighters)*
