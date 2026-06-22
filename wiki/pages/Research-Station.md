<!-- Hand-written mechanics page. Code lineage (kept out of the reader-facing text on purpose):
     data/scripts/entity/merchants/researchstation.lua — item rules, the rarity/type/weapon
     probability functions (checkRarities, getRarityProbabilities, getTypeProbabilities,
     getWeaponProbabilities/Materials/Tech, getSystemProbabilities, transform, transformPatterns),
     CheckPlayerDocked / interactionThreshold (−30,000), refreshButton, tech caps (50 blueprint /
     52 turret), SectorTurretGenerator, SystemUpgradeTemplate, the auto-research grouping
     (getItemAutoResearchGroup, findAutoResearchGroup), the guaranteed transformPatterns recipes
     (teleporterkey2; staffbosscaller boss caller), and the cancelWithTooManyKeys safety check.
     Image assets: see wiki/ASSETS.md. -->
# Research Station

A **Research Station** rerolls equipment. You feed it turrets, turret blueprints, or system upgrades,
its "research AI" consumes them, and it hands back a single **new, randomly generated item** built from
the properties of what you fed in. In the game's own words it's *"basically a gamble"* — Avorion's slot
machine for gear. You hand over several mediocre items hoping for one better item back, with a real chance
of getting something worse.

> **In short:** feed in **3–5 turrets, blueprints or system upgrades** (all within **one rarity tier** of
> each other). Each item adds **+20% chance** the result comes out **one rarity higher** — so **five items
> guarantees a rarity bump**. The result's *type* and stats are drawn from your inputs, all of which are
> consumed. Always fill all five slots when you can.

You'd visit a Research Station to:

- **Upgrade rarity** — every item you feed in adds a chance the result is one tier higher.
- **Clear out junk** — turn a pile of low-value drops into one item worth keeping (**Auto-Research**
  automates exactly this).
- **Reroll a system upgrade's stats** — feed in upgrades of a type you like for a fresh roll of that type.
- **Chase a few hidden, guaranteed recipes** (see [Hidden recipes](#hidden-recipes)).

Rarity runs from **Petty** to **Legendary**, the same scale used on [System upgrades](System-upgrades):

| Rarity | Petty | Common | Uncommon | Rare | Exceptional | Exotic | Legendary |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

## How it works / requirements

*[📷 Screenshot needed — ASSETS.md: images/research-station-ui.png]*

To research anything you must be **docked to the station** with a ship, and you must not be at war with the
station's owner (relation above **−30,000**).

The research window has two input groups and one output slot:

- **Required** — 3 slots that must all be filled.
- **Optional** — 2 extra slots you may also fill.
- **Result** — the single item the AI produces.

The Research button only lights up once the three required slots are full, and the station rejects anything
that isn't equipment. The **only valid inputs** are:

| Valid input | What it is |
|---|---|
| **Turret** | An assembled, installable turret |
| **Turret blueprint** | A turret you can mass-produce at a [Turret Factory](Turret-crafting) |
| **System upgrade** | A subsystem module — see [System upgrades](System-upgrades) |

So you research with **3 to 5 items**, every one a turret, a blueprint, or a system upgrade. The items are
**consumed** when the result is produced.

> The result lands in your inventory automatically. If your inventory is full it is **dropped into space**
> instead with a warning — make room before researching something you care about.

### The rarity rule

All input items must be **within one rarity tier of each other**. If your items span more than one tier the
station refuses outright:

> *"Your items cannot be more than one rarity apart!"*

So you can mix, say, Rare and Exceptional items in one batch, but not Rare and Exotic.

## Rarity & output odds

When you research, the station rolls the result's **rarity** with a weighted random draw. The rule is
simple:

> **Each input item adds a flat 20% chance that the result is one rarity tier higher** (capped at
> Legendary).

If you use fewer than five items, the leftover probability produces a result at the **same** rarity you put
in. With a full five items the entire 100% goes to the "one tier higher" outcome, so **five items
guarantees a rarity bump**:

| Items used | Chance result is +1 rarity tier | Chance result is same rarity |
|:--:|:--:|:--:|
| 3 (minimum) | 60% | 40% |
| 4 | 80% | 20% |
| 5 (maximum) | **100%** | 0% |

> **Tip:** Always fill all five slots when you can. Five items don't just raise the *average* result — they
> make the rarity upgrade **guaranteed**. The trade-off is two extra items per roll.

The rarity can only ever move **up by one or stay the same** — the station never produces a result *below*
your inputs, and never jumps two tiers at once. A Legendary input can only ever yield Legendary.

## Output type — what you get back

The **type** of the result (turret, blueprint, or system upgrade) is a weighted random choice across the
types you fed in: each input adds one "vote" for its own type. Feed three turrets and you'll almost
certainly get a turret; feed two blueprints and one upgrade and the result is twice as likely to be a
blueprint as an upgrade.

Assembled **turrets** and **turret blueprints** count as *separate* types, so finished turrets bias the
output toward a finished turret, while blueprints bias it toward another blueprint.

## Weapon vs. system upgrade results

Once the type is chosen, the station builds the item differently depending on which path it took.

### Weapon path (turret or blueprint result)

If the result is a turret or blueprint, its characteristics are derived from the **turret and blueprint
inputs**:

- **Weapon type** (Chaingun, Laser, Railgun, …) — weighted random across the input weapons' types.
- **Material** (Iron … Avorion) — weighted random across the input weapons' materials.
- **Tech level** — the **average tech** of the input weapons (rounded up), then bumped and capped.

The AI aims for *min(sector tech, average input tech + 10)*, then clamps to a hard cap:

| Result | Tech cap |
|---|:--:|
| **Turret blueprint** | **50** (blueprints above tech 50 can't be used by players) |
| **Assembled turret** | **52** |

The finished weapon is generated fresh at that tech, rarity, weapon type and material — so it's a
**genuinely new turret**, not a copy of any input.

### System upgrade path

If the result is a system upgrade, the station picks **which upgrade** by weighted random across your input
upgrades, then generates a **fresh upgrade of that kind with a brand-new random seed**. In other words you
get the **same kind** of upgrade as (one of) your inputs, but with **completely rerolled stats** — the way
to gamble on a better roll of a subsystem you already like.

## Auto-Research

The station's **Auto-Research** mode is a toggle that repeatedly grabs items you've marked as **trash**,
feeds them in three at a time, and researches them automatically until it runs out of valid groups. It's
the bulk way to grind a hoard of junk drops into fewer, better items without manual clicking.

You pick a **mode** that controls how the game may group your trash into valid trios. Auto-Research still
obeys the one-rarity-apart rule — it scans from the **lowest rarity upward** and only ever combines items
within one tier:

| Mode | What it groups into a research batch |
|---|---|
| **Same Item Types** | Identical items only — matching turrets, matching blueprints, matching subsystems |
| **Same Turrets** | Only turrets with the same weapon name |
| **Same Turret-Blueprints** | Only blueprints with the same weapon name |
| **Same Subsystems** | Only subsystems of the same upgrade type |
| **Any Turrets** | Any turrets together, regardless of type |
| **Any Turret-Blueprints** | Any blueprints together |
| **Any Subsystems** | Any subsystems together |
| **Any Combination** | Any mix of turrets, blueprints and subsystems |

> Only items flagged as **trash** are ever consumed by Auto-Research, so mark your keepers as **favourites**
> (favourites can't even be dragged into the input slots) and they're safe. If no valid group of three
> trash items exists for the chosen mode, the station reports *"Not enough trash items available for current
> auto research mode."* and stops.

## Hidden recipes

Before the normal rarity/type roll, the station checks for a handful of **predetermined patterns**. If your
inputs match one, that exact result is produced and the random roll — **and the one-rarity-apart
restriction** — is skipped entirely.

> **Secret — Legendary teleporter key:** Feed in **3 or more Legendary-rarity system upgrades** and the
> result is guaranteed to be a **Legendary teleporter key** upgrade.

> **Secret — Boss Caller:** Include all of the following among your inputs at once and the station
> guarantees a Legendary **Boss Caller** usable item (see [Boss callers](Boss-callers)):
> - a **Point Defense Chaingun**-type weapon,
> - a **Laser**-type weapon,
> - a **Lightning Gun**-type weapon,
> - a **Railgun**-type weapon,
> - any item of **Exotic rarity or higher**, and
> - a **hacking upgrade** (the black-market subsystem).
>
> A single item can satisfy more than one of these (e.g. the Exotic-rarity item can also be one of the
> weapons), so the combination fits within the five input slots.

> **⚠ Safety check — your keys are protected:** If **two or more teleporter-key** system upgrades are among
> the inputs, the station **refuses to research at all**. This is a deliberate guard so you can't
> accidentally feed valuable keys into the machine and lose them. (A single key is allowed through.)

## Flavor text

The station's broadcast chatter leans hard into the gambling-AI framing:

> *"Completely random AI-supported research, it's basically a gamble!"*

> *"Our research AI eats up objects and creates new ones based on the old ones — often better, sometimes
> worse!"*

> *"Don't you DARE hit that red button!"*

## See also

- [System upgrades](System-upgrades) – the subsystem modules you can feed in and reroll
- [Weapons](Weapons) – the turret weapon types the weapon path draws from
- [Turret crafting](Turret-crafting) – building the blueprints that researching turrets can produce
- [Boss callers](Boss-callers) – the boss the secret Boss Caller recipe yields
- [Special items](Special-items) – other activatable inventory items

---
*Items & Special Objects: [Reconstruction kits](Reconstruction-kits) · [Maps and charts](Maps-and-charts) · [Deployable beacons](Deployable-beacons) · [Special items](Special-items) · [Research Station](Research-Station) · [Boss callers](Boss-callers)*
