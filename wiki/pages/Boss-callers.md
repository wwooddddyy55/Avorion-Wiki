<!-- Hand-written page. Sourced from items/jumperbosscaller.lua (the Hyperspace Interrupter item),
     player/events/spawnjumperboss.lua (how Fidget is built and loaded), and
     entity/events/jumperboss.lua (the fight's stun/jump mechanic and chatter). The Trade Guild
     Beacon source (items/equipmentmerchantcaller.lua) is cited for where the interrupter is sold,
     and entity/merchants/researchstation.lua for the staffbosscaller research recipe. The
     staffbosscaller.lua script itself is NOT in the extracted files, so its behaviour is left
     unstated on purpose. -->
# Boss callers

**Boss callers** are activatable consumable items that **summon a boss fight on demand** instead of
making you wait for one to appear. You trigger one from your inventory and a specific boss spawns in
your current sector, ready to fight. They're Legendary one-shot items — used up the moment you activate
them — aimed at players who want to farm a particular boss's loot on their own schedule.

The game ties this behaviour to a small family of `...bosscaller.lua` item scripts. Only one of them is
present in the extracted game files and can be documented in full: the **Hyperspace Interrupter**, which
calls in the teleporting boss **Fidget**. A second variant (`staffbosscaller.lua`) is referenced by the
[Research Station](Research-Station) as a hidden recipe result, but its script isn't in the extracted
files — see [The Research Station "Boss Caller"](#the-research-station-boss-caller) below.

## Hyperspace Interrupter

The **Hyperspace Interrupter** (`jumperbosscaller.lua`) is the concrete boss caller. Its tooltip is
blunt about what it does: *"Can be used to interrupt the hyperspace jump of Fidget."*

| Property | Value |
|---|---|
| In-game name | **Hyperspace Interrupter** |
| Rarity | **Legendary** (always — forced in `create`) |
| Price | 50,000 |
| Stacks? | No |
| Consumed on use? | **Yes** ("Depleted on Use") |
| Activation | Activated by the player from the inventory |
| Cooldown | **25 minutes** between uses |

When you activate it (`activate`, ~line 58):

- It **spawns Fidget** in your current sector.
- It **won't work inside a rift** — activating there silently fails.
- It enforces a **25-minute per-player cooldown**. If you try again too soon, the game tells you the
  interrupter *"still needs about N min to track Fidget's ship."*

> The cooldown is stored per player (`jumperboss_last_called_timestamp`), so the wait is on **you**, not
> on the item — a second interrupter won't skip the timer.

### Where it comes from

The interrupter is sold by the **Mobile Merchant** that the **Trade Guild Beacon**
(`equipmentmerchantcaller.lua`) calls into a sector: that merchant stocks a Legendary Hyperspace
Interrupter as a front-of-shop utility item (`equipmentmerchantcaller.lua`, ~line 194). So in normal
play you call the merchant, then buy the interrupter to call the boss.

## Fidget — the boss it summons

Fidget is a ship of the faction **"The Pariah"** (`spawnjumperboss.lua`). It is **not** one of the
hand-themed [world bosses](World-bosses); it's a dedicated summoned encounter with one defining trick:
**it keeps jumping away.**

### The fight: stun it, don't just shoot it

The whole encounter is built around its `onDamaged` reaction (`jumperboss.lua`, ~line 60):

| You hit it with… | What happens |
|---|---|
| **Electric** damage | It gets **stunned for ~5 seconds** — its AI stops and it glows and throws sparks, held in place |
| **Any other** damage | It **blinks to a new random position** in the sector and taunts you |

So conventional guns alone are nearly useless: every non-electric hit just teleports Fidget somewhere
else, and the moment a stun wears off it immediately jumps away again and turns aggressive. To actually
kill it you have to **pin it down with electric weapons** (Lightning Guns) and burn it while it's
stunned.

> **Bring electric weapons.** Without a source of Electric damage to stun Fidget, you'll spend the whole
> fight chasing a boss that won't hold still. This is exactly what the item's name — "interrupter" —
> refers to: shorting out its jump engine. Its own chatter spells it out: *"You'll need something better
> to short-circuit my jump engine!"*

### Fidget's loadout and stats

Fidget is built at **30× the normal sector ship volume**, with any **shield generators stripped out**
(replaced by armor), and it is **not boardable and not dockable** (`spawnjumperboss.lua`). Its turrets:

| Turret | Count | Rarity |
|---|:--:|---|
| Cannon | 3 | Exceptional |
| Laser | 2 | Exotic |
| Rocket Launcher | 5 | Exceptional |
| Point Defense Chaingun | 2 | Exotic |

### Loot

On top of the standard **boss health bar** behaviour, Fidget is set up to drop well
(`spawnjumperboss.lua`):

- It runs the shared **legendary-loot** script, guaranteeing a Legendary turret drop.
- Its loot is seeded with **two extra turrets** (a Cannon and a Laser), each rolled at **Exotic** rarity,
  with a **20% chance to instead be Legendary**.

That guaranteed-plus-chance Legendary loot is the reason to call Fidget on purpose with an interrupter.

## The Research Station "Boss Caller"

The [Research Station](Research-Station) has a hidden recipe that produces a Legendary
`UsableInventoryItem` from `internal/common/items/staffbosscaller.lua` — what the wiki calls the
"Boss Caller" — when you feed it a Point Defense Chaingun, a Laser, a Lightning Gun, a Railgun, an
Exotic-or-better item, and a hacking upgrade all at once (`researchstation.lua`, ~line 890).

> **Source caveat:** `staffbosscaller.lua` is **not present in the extracted game files.** From the
> Research Station code we only know it's a Legendary, player-activatable item of the boss-caller family.
> Which boss it summons, its cooldown, and its exact rules **can't be verified here**, so this page does
> not state them. It is the same *kind* of item as the Hyperspace Interrupter — a Legendary consumable
> that calls a boss — but the specifics are unconfirmed.

## See also

- [Research Station](Research-Station) – the hidden recipe that yields the unverified `staffbosscaller` Boss Caller
- [World bosses](World-bosses) – the hand-themed bosses with guaranteed Legendary drops (Fidget is separate from these)
- [Weapons](Weapons) – Lightning Guns and the electric damage you need to stun Fidget
- [Combat](Combat) / [Defensive systems](Defensive-systems) – damage types and surviving Fidget's loadout
- [Special items](Special-items) – other activatable inventory gadgets

---
*Items & Special Objects: [Reconstruction kits](Reconstruction-kits) · [Maps and charts](Maps-and-charts) · [Deployable beacons](Deployable-beacons) · [Special items](Special-items) · [Research Station](Research-Station) · [Boss callers](Boss-callers)*
