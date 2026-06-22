<!-- Hand-written page. Code lineage (kept out of the reader-facing text on purpose):
     items/jumperbosscaller.lua (the Hyperspace Interrupter item: forced Legendary, price 50k,
       Depleted on Use, activate ~line 58, 25-min per-player cooldown jumperboss_last_called_timestamp),
     player/events/spawnjumperboss.lua (how Fidget is built/loaded: 30× volume, shields stripped,
       not boardable/dockable, loadout, legendary-loot + 2 extra Exotic-or-Legendary turrets),
     entity/events/jumperboss.lua (onDamaged ~line 60: electric=stun, else blink),
     items/equipmentmerchantcaller.lua ~line 194 (Trade Guild / Mobile Merchant sells the interrupter),
     entity/merchants/researchstation.lua ~line 890 (the staffbosscaller research recipe).
     NOTE: staffbosscaller.lua is NOT in the extracted files, so its behaviour is left unstated on purpose.
     Image assets: see wiki/ASSETS.md. -->
# Boss callers

**Boss callers** are activatable consumable items that **summon a boss fight on demand** instead of making
you wait for one to appear. You trigger one from your inventory and a specific boss spawns in your current
sector, ready to fight. They're Legendary one-shot items — used up the moment you activate them — aimed at
players who want to farm a particular boss's loot on their own schedule.

> **In short:** the **Hyperspace Interrupter** summons the teleporting boss **Fidget**. Fidget only holds
> still when hit with **Electric** damage (Lightning Guns) — every other hit just teleports it away. **Bring
> electric weapons**, stun it, and burn it down for a **guaranteed Legendary** drop. The interrupter has a
> **25-minute cooldown** and is sold by the Mobile Merchant you call with a Trade Guild Beacon.

There is a small family of boss-caller items. The one fully documented here is the **Hyperspace
Interrupter**, which calls in **Fidget**. A second variant — the **Boss Caller** produced by a hidden
[Research Station](Research-Station) recipe — exists but isn't yet documented; see
[The Research Station "Boss Caller"](#the-research-station-boss-caller) below.

## Hyperspace Interrupter

The **Hyperspace Interrupter** is the concrete boss caller. Its tooltip is blunt: *"Can be used to interrupt
the hyperspace jump of Fidget."*

| Property | Value |
|---|---|
| In-game name | **Hyperspace Interrupter** |
| Rarity | **Legendary** (always) |
| Price | 50,000 |
| Stacks? | No |
| Consumed on use? | **Yes** ("Depleted on Use") |
| Activation | Activated from the inventory |
| Cooldown | **25 minutes** between uses |

When you activate it:

- It **spawns Fidget** in your current sector.
- It **won't work inside a rift** — activating there silently fails.
- It enforces a **25-minute cooldown**. If you try again too soon, the game tells you the interrupter
  *"still needs about N min to track Fidget's ship."*

> The cooldown is stored per player, so the wait is on **you**, not on the item — a second interrupter won't
> skip the timer.

### Where it comes from

The interrupter is sold by the **Mobile Merchant** that the **Trade Guild Beacon** calls into a sector: that
merchant stocks a Legendary Hyperspace Interrupter as a front-of-shop utility item. So in normal play you
call the merchant, buy the interrupter, then use it to call the boss.

## Fidget — the boss it summons

Fidget is a ship of the faction **"The Pariah"**. It is **not** one of the hand-themed [world
bosses](World-bosses); it's a dedicated summoned encounter with one defining trick: **it keeps jumping
away.**

### The fight: stun it, don't just shoot it

The whole encounter is built around how Fidget reacts to being hit:

| You hit it with… | What happens |
|---|---|
| **Electric** damage | It gets **stunned for ~5 seconds** — its AI stops and it glows and throws sparks, held in place |
| **Any other** damage | It **blinks to a new random position** in the sector and taunts you |

So conventional guns alone are nearly useless: every non-electric hit just teleports Fidget somewhere else,
and the moment a stun wears off it jumps away again and turns aggressive. To kill it you have to **pin it
down with electric weapons** (Lightning Guns) and burn it while it's stunned.

> **Bring electric weapons.** Without a source of Electric damage to stun Fidget, you'll spend the whole
> fight chasing a boss that won't hold still — exactly what the item's name, "interrupter", refers to:
> shorting out its jump engine. Its own chatter spells it out: *"You'll need something better to
> short-circuit my jump engine!"*

### Fidget's loadout and stats

Fidget is built at **30× the normal sector ship size**, with its **shield generators stripped out**
(replaced by armor), and it is **not boardable and not dockable**. Its turrets:

| Turret | Count | Rarity |
|---|:--:|---|
| Cannon | 3 | Exceptional |
| Laser | 2 | Exotic |
| Rocket Launcher | 5 | Exceptional |
| Point Defense Chaingun | 2 | Exotic |

### Loot

On top of the standard **boss health bar** behaviour, Fidget is set up to drop well:

- It runs the shared **legendary-loot** drop, guaranteeing a Legendary turret.
- Its loot is seeded with **two extra turrets** (a Cannon and a Laser), each rolled at **Exotic** rarity,
  with a **20% chance to instead be Legendary**.

That guaranteed-plus-chance Legendary loot is the reason to call Fidget on purpose with an interrupter.

## The Research Station "Boss Caller"

The [Research Station](Research-Station) has a hidden recipe that produces a Legendary **Boss Caller** item
when you feed it a Point Defense Chaingun, a Laser, a Lightning Gun, a Railgun, an Exotic-or-better item,
and a hacking upgrade all at once.

> **Not yet documented:** this Boss Caller is a Legendary, player-activatable item of the boss-caller family
> — the same *kind* of item as the Hyperspace Interrupter — but **which boss it summons, its cooldown, and
> its exact rules are unconfirmed**, so this page doesn't state them.

## See also

- [Research Station](Research-Station) – the hidden recipe that yields the (undocumented) Boss Caller
- [World bosses](World-bosses) – the hand-themed bosses with guaranteed Legendary drops (Fidget is separate)
- [Weapons](Weapons) – Lightning Guns and the electric damage you need to stun Fidget
- [Combat](Combat) / [Defensive systems](Defensive-systems) – damage types and surviving Fidget's loadout
- [Special items](Special-items) – other activatable inventory gadgets

---
*Items & Special Objects: [Reconstruction kits](Reconstruction-kits) · [Maps and charts](Maps-and-charts) · [Deployable beacons](Deployable-beacons) · [Special items](Special-items) · [Research Station](Research-Station) · [Boss callers](Boss-callers)*
