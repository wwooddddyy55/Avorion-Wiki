<!-- Hand-written page. Sourced from lib/captaingenerator.lua (tier/level/perk/salary generation),
     lib/captainclass.lua (the 9 class IDs), lib/captainutility.lua (class properties & bonuses,
     PerkType list, salary tooltip, "Specializes when reaching level 5"). Player-facing numbers
     (salary constants, perk counts per tier) are taken directly from captaingenerator.lua. -->
# Captains

A **captain** is a hired NPC you place in command of one of your ships. A ship with a captain can be
given long-running **[fleet commands](Fleet-commands)** — mine, salvage, trade, scout, expedition and
so on — that it carries out on its own in the background while you fly something else, even in other
sectors. Captains have a **class** (their specialization), a **tier**, a **level**, and a handful of
**perks** that together decide how well, how fast, how safely and how cheaply they run those commands.

> Captains drive the *self-running* commands. The short, in-sector commands you give any ship (jump,
> attack, mine here, escort) are covered on **[Ship orders](Ship-orders)**.

> **In short:** a captain lets a ship **work on its own in the background** — mining, trading, scouting —
> even in other sectors. Their **class** decides what they're best at, their **perks** decide how fast,
> safe and cheap they run commands, and **tier + level** scale all of it. Match the class to the job (a
> Miner for mining, a Merchant for trade), favour captains with risk-lowering perks, and weigh their
> **salary** against what they earn you.

## Tier

Tier is the captain's overall pedigree, from **0 to 3**. It controls how many classes the captain has and
the mix of good and bad perks they roll with:

| Tier | Classes | Positive perks | Negative perks | Neutral perks |
|---|---|---|---|---|
| **0** | none (unspecialized) | 0–1 | 0–2 | 0–2 |
| **1** | one | 1–2 | 0–1 | 1–2 |
| **2** | one | 2–3 | **0** | 0–2 |
| **3** | **two** (primary + secondary) | 2–4 | **0** | 1–2 |

A **tier‑0** captain has no class yet. The game notes *"Specializes when reaching level 5"* — train one
up and it gains a class. Higher tiers come pre-specialized, and only a **tier‑3** captain has both a
primary and a secondary class. Tier is also shown by the wing emblems on the captain's badge.

## Level

A captain gains **experience** by completing commands and **levels up**, shown as stars on the badge.
Levelling makes a captain better at their class (for example a Miner/Scavenger's mining and salvaging
duration scales with both tier **and** level) and raises their salary. The freshly generated captains you
find in the world start at low levels; you raise them by putting them to work.

The **Educated** perk speeds this up and **Uneducated** slows it down (see [Captain perks](Captain-perks)).

## Classes

A captain's class is their job specialization and grants concrete ship bonuses plus an affinity for
certain commands. There are **nine** classes:

Commodore · Smuggler · Merchant · Miner · Scavenger · Explorer · Daredevil · Scientist · Xsotan Hunter

Each is detailed — with its exact bonuses and best commands — on **[Captain classes](Captain-classes)**.

## Perks

Every captain carries up to a few **perks**: small positive, negative or neutral traits such as *Navigator*
(faster commands), *Stealthy* (lower ambush risk), *Greedy* (higher salary) or *Lucky* (may find loot on a
command). Perks are the main reason two captains of the same class perform differently. The full list, what
each one does, and which perks cancel each other out is on **[Captain perks](Captain-perks)**.

## Salary

A captain draws a **salary** while employed. It's computed from tier, classes, perks and level:

```
salary = 15,000 base
       + 10,000 per class
       + 2,500 per positive perk
       − 2,000 per negative perk
       × level factor   (1.0 at level 0, scaling up to 2.0 at level 5)
       × 0.9 if Humble  /  × 1.1 if Greedy
(rounded to the nearest 100)
```

So a higher-tier captain with two classes and several positive perks is far more expensive than a raw
tier‑0 recruit — but also far more capable. The **Humble** perk shaves 10% off the wage; **Greedy** adds
10%.

## Risk: ambushes

Commands aren't free of danger. While a captained ship is off running a command it has a chance of being
**ambushed**, and the captain's class and perks move that chance up or down. Risk-lowering perks include
*Stealthy*, *Careful*, *Intimidating* and *Noble*; risk-raising ones include *Arrogant*, *Reckless*,
*Harmless* and *Commoner*. Some commands also offer a **Safe Mode** toggle that trades speed for safety.
The strength of any attackers can likewise be tuned by neutral perks (*Cunning*, *Harmless*, etc.).

## See also

- **[Captain classes](Captain-classes)** – the nine specializations and their bonuses
- **[Captain perks](Captain-perks)** – all 21 perks and their opposing pairs
- **[Fleet commands](Fleet-commands)** – the background commands captains run
- **[Ship orders](Ship-orders)** – the immediate, in-sector orders for any ship
- **[Trade Contracts](Trade-Contracts)** – automated trade routes flown by a Merchant captain
- **[Rift Expeditions](Rift-Expeditions)** – where a Scientist captain's bonus matters most: triple Rift Research Data per kill

---
*Fleet & Captains: [Captains](Captains) · [Captain classes](Captain-classes) · [Captain perks](Captain-perks) · [Fleet commands](Fleet-commands) · [Ship orders](Ship-orders)*
