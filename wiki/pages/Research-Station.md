<!-- Hand-written mechanics page. Sourced entirely from
     data/scripts/entity/merchants/researchstation.lua.
     Item rules, rarity/type/weapon probability functions, tech caps, auto-research
     grouping, the guaranteed transformPatterns recipes and the teleporter-key safety
     check are all read straight from that file (line numbers cited inline). -->
# Research Station

A **Research Station** is a station that **rerolls equipment**. You feed it turrets, turret
blueprints, or system upgrades, its "research AI" consumes them, and it spits back a single **new,
randomly generated item** built from the properties of what you fed in. It is, in the game's own
words, *"basically a gamble"* — the station is Avorion's slot machine for gear. You hand over several
mediocre items in the hope of getting one better item back, with a real chance of also getting
something worse.

You would visit a Research Station to:

- **Upgrade rarity** — every item you feed in adds a chance the result comes out one rarity tier higher.
- **Clear out junk** — turn a pile of low-value drops into one item worth keeping (and the
  **Auto-Research** mode automates exactly this).
- **Reroll a system upgrade's stats** — feed in upgrades of a type you like to get a fresh roll of
  the same type.
- **Chase a few hidden, guaranteed recipes** (see [Hidden recipes](#hidden-recipes)).

Rarity throughout this page is the engine's `rarity.value`, which runs from **−1 (Petty)** to **5
(Legendary)** — the same scale used on the [System upgrades](System-upgrades) page:

| `rarity.value` | −1 | 0 | 1 | 2 | 3 | 4 | 5 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Rarity | Petty | Common | Uncommon | Rare | Exceptional | Exotic | Legendary |

## How it works / requirements

To research anything you must be **docked to the station** with a ship (`CheckPlayerDocked`,
research ~line 750), and your faction's relation to the station's owner must be above the
station's interaction threshold of **−30,000** (`interactionThreshold`, ~line 39) — i.e. not actively
at war.

The research window has two input groups and one output slot:

- **Required** — 3 slots that must all be filled.
- **Optional** — 2 extra slots you may also fill.
- **Result** — the single item the AI produces.

The Research button only lights up once the three required slots are full, and the station rejects
anything that isn't equipment (`refreshButton`, ~line 348). The **only valid input item types** are:

| Valid input | What it is |
|---|---|
| **Turret** | An assembled, installable turret |
| **Turret blueprint** (`TurretTemplate`) | A turret you can mass-produce at a [Turret Factory](Turret-crafting) |
| **System upgrade** (`SystemUpgrade`) | A subsystem module — see [System upgrades](System-upgrades) |

So you research with **3 to 5 items**, every one of which is a turret, a blueprint, or a system
upgrade. The minimum of three is enforced both in the UI and on the server (research, ~line 750:
*"You need at least 3 items to do research!"*). The items are **consumed** when the result is produced.

> The result lands in your inventory automatically. If your inventory is full it is **dropped into
> space** instead with a warning (research, ~line 800) — make room before researching something you
> care about.

### The rarity rule

All input items must be **within one rarity tier of each other** (`checkRarities`, ~line 410). If your
items span more than one tier the station refuses outright:

> *"Your items cannot be more than one rarity apart!"*

So you can mix, say, Rare and Exceptional items in one batch, but not Rare and Exotic.

## Rarity & output odds

When you research, the station rolls the result's **rarity** with a weighted random draw
(`getRarityProbabilities`, ~line 426). The rule is simple:

> **Each input item adds a flat 20% chance that the result is one rarity tier higher** than that item
> (capped at Legendary).

If you use fewer than five items, the **remaining probability is spread back across the inputs' own
rarities** — i.e. the leftover odds produce a result at the same rarity you put in. With a full five
items the entire 100% goes to the "one tier higher" outcome, so **five items guarantees a rarity
bump**.

Assuming all inputs share one rarity, the aggregate odds work out as:

| Items used | Chance result is +1 rarity tier | Chance result is same rarity |
|:--:|:--:|:--:|
| 3 (minimum) | 60% | 40% |
| 4 | 80% | 20% |
| 5 (maximum) | **100%** | 0% |

> **Tip:** Always fill all five slots when you can. Five items don't just raise the *average* result —
> they make the rarity upgrade **guaranteed**. The trade-off is that you're feeding the machine two
> extra items per roll.

Note the rarity can only ever move **up by one or stay the same** — the station never produces a
result *below* the rarity of your inputs, and never jumps two tiers at once. A Legendary input can
only ever yield Legendary (the +1 is capped).

## Output type — what you get back

The **type** of the result (turret, blueprint, or system upgrade) is itself a weighted random choice
across the types you fed in (`getTypeProbabilities`, ~line 460): each input item adds one "vote" for
its own type. Feed three turrets and you'll almost certainly get a turret; feed two blueprints and one
upgrade and the result is twice as likely to be a blueprint as an upgrade.

Assembled **turrets** and **turret blueprints** are counted as *separate* types here, so feeding
finished turrets biases the output toward a finished turret, while feeding blueprints biases it toward
another blueprint.

## Weapon vs. system upgrade results

Once the type is chosen, the station builds the actual item differently depending on which path it
took (`transform`, ~line 901).

### Weapon path (turret or blueprint result)

If the result is a turret or a blueprint, its characteristics are all derived from the **turret and
blueprint inputs** (both count):

- **Weapon type** (Chaingun, Laser, Railgun, …) — weighted random across the input weapons' types
  (`getWeaponProbabilities`, ~line 472).
- **Material** (Iron … Avorion) — weighted random across the input weapons' materials
  (`getWeaponMaterials`, ~line 491).
- **Tech level** — the **average tech** of the input weapons (`getWeaponTech`, ~line 507, rounded up),
  then bumped and capped.

The tech the AI aims for is `min(sector tech, average input tech + 10)`, then clamped by a hard cap
that depends on what's being produced (transform, ~lines 940–947):

| Result | Tech cap |
|---|:--:|
| **Turret blueprint** | **50** (blueprints above tech 50 can't be used by players) |
| **Assembled turret** | **52** |

The finished weapon is then created by the standard `SectorTurretGenerator` at that tech, rarity,
weapon type and material — so it is a **genuinely new turret**, not a copy of any input.

### System upgrade path

If the result is a system upgrade, the station picks **which upgrade script** by weighted random
across the input upgrades' scripts (`getSystemProbabilities`, ~line 522), then generates a **fresh
`SystemUpgradeTemplate` with a brand-new random seed** (transform, ~line 964). In other words you get
the **same kind** of upgrade as (one of) your inputs, but with **completely rerolled stats**. This is
the way to gamble on a better roll of a subsystem you already like — feed in copies of that subsystem
and the result is guaranteed to be the same type, freshly rolled.

## Auto-Research

The station has an **Auto-Research** mode (~lines 21–37, 553–714): a UI toggle that repeatedly grabs
batches of items you've marked as **trash** in your inventory, feeds them in three at a time, and
researches them automatically until it runs out of valid groups. It's the bulk way to grind a hoard of
junk drops down into fewer, better items without manual clicking.

You pick a **mode** from a dropdown that controls how the game is allowed to group your trash items
into valid trios (`getItemAutoResearchGroup`, ~line 642). Auto-Research still obeys the one-rarity-apart
rule — it scans from the **lowest rarity upward** and only ever combines items within one tier
(`findAutoResearchGroup`, ~line 600):

| Mode | What it groups into a research batch |
|---|---|
| **Same Item Types** | Identical items only — matching turrets together, matching blueprints together, matching subsystems together |
| **Same Turrets** | Only turrets, and only ones with the same weapon name |
| **Same Turret-Blueprints** | Only blueprints with the same weapon name |
| **Same Subsystems** | Only subsystems running the same script (same upgrade type) |
| **Any Turrets** | Any turrets together, regardless of type |
| **Any Turret-Blueprints** | Any blueprints together |
| **Any Subsystems** | Any subsystems together |
| **Any Combination** | Any mix of turrets, blueprints and subsystems together |

> Only items flagged as **trash** are ever consumed by Auto-Research, so mark your keepers as
> favourites (favourites can't even be dragged into the input slots) and they're safe. If no valid
> group of three trash items exists for the chosen mode, the station reports *"Not enough trash items
> available for current auto research mode."* and stops.

## Hidden recipes

Before the normal rarity/type roll, the station checks for a handful of **predetermined patterns**
(`transformPatterns`, ~line 862). If your inputs match one, that exact result is produced and the
random roll — **and the one-rarity-apart restriction** — is skipped entirely.

> **Secret — Legendary key:** Feed in **3 or more Legendary-rarity system upgrades** and the result is
> guaranteed to be a **Legendary `teleporterkey2` upgrade** (transform pattern, ~line 871).

> **Secret — Boss Caller:** Include all of the following among your inputs at once and the station
> guarantees a Legendary **Boss Caller** usable item (`staffbosscaller.lua`, ~line 890):
> - a **Point Defense Chaingun**-type weapon,
> - a **Laser**-type weapon,
> - a **Lightning Gun**-type weapon,
> - a **Railgun**-type weapon,
> - any item of **Exotic rarity or higher**, and
> - a **hacking upgrade** (the black-market subsystem).
>
> A single item can satisfy more than one of these (e.g. the Exotic-rarity item can be one of the
> weapons), so the combination fits within the five input slots.

> **⚠ Safety check — your keys are protected:** If **two or more teleporter-key** system upgrades are
> among the inputs, the station **refuses to research at all** (`cancelWithTooManyKeys`, ~line 851).
> This is a deliberate guard so you can't accidentally feed valuable keys into the machine and lose
> them. (A single key is allowed through.)

## Flavor text

The station's broadcast chatter (~lines 189–216) leans hard into the gambling-AI framing, and is worth
quoting for the in-universe flavour:

> *"Completely random AI-supported research, it's basically a gamble!"*

> *"Our research AI eats up objects and creates new ones based on the old ones — often better,
> sometimes worse!"*

> *"Don't you DARE hit that red button!"*

## See also

- [System upgrades](System-upgrades) – the subsystem modules you can feed in and reroll
- [Weapons](Weapons) – the turret weapon types the weapon path draws from
- [Turret crafting](Turret-crafting) – building the blueprints that researching turrets can produce
- [World bosses](World-bosses) – what the secret Boss Caller recipe summons
- [Special items](Special-items) – other activatable inventory items like the one Boss Caller

---
*Items & Special Objects: [Reconstruction kits](Reconstruction-kits) · [Maps and charts](Maps-and-charts) · [Deployable beacons](Deployable-beacons) · [Special items](Special-items) · [Research Station](Research-Station)*
