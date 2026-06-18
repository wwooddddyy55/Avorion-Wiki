<!-- Hand-written page. Sourced from items/recalldevice.lua (+ lib/recalldeviceutility.lua),
     items/energysuppressor.lua and items/commune3missionitem.lua. The recall device's 10-minute
     cooldown, hyperspace-engine requirement, one-way 2-minute wormhole and Adventurer mail gift, plus
     the suppressor's 10h duration and the mission item's bound/undroppable flags, are read from those
     files. -->
# Special items

A few activatable items don't fit the map / beacon / reconstruction families. They're one-off gadgets with
their own rules.

## Xsotan Wormhole Device (the Recall Device)

A **panic button that sends you home.** Activate it and it opens a **one-way wormhole** to your
**Reconstruction Site** (your respawn sector) and pulls your ship through. The tooltip is written as if the
device is barely-understood junk (*"Is this thing even working..?"*), but it works.

How it behaves:

- It's **bound to you** and can't be traded or dropped.
- You must be **flying a ship** with a **hyperspace engine** that is **fully recharged** and **not blocked
  or distorted** (so you can't escape mid-jam). Using it **exhausts** the engine.
- There's a **10-minute cooldown** between uses.
- The wormhole is **one-way** and stays open for **2 minutes** — "using the recall device should be a
  commitment." Only you (and your alliance) can travel through it.
- It does nothing if you're already **in** your Reconstruction Site sector.

You **receive it as a gift**: once you qualify (your respawn sector differs from your home sector, or
you've found story artifacts) **the Adventurer mails it to you**, describing it as a *"Strange Xsotan
Device..?"* it can't make sense of.

## Energy Suppressor Satellite

A deployable **area-denial / stealth** satellite. Activate it and it spawns an Iron satellite in front of
your ship that **suppresses energy signatures in the sector**, hiding activity *"from persecutors"* for
**10 hours**. It's **Exceptional** rarity, costs **100,000**, stacks, and is consumed on use — useful for
lying low or covering an operation in a sector.

## Mission items (Data Chip)

Some quests hand you a plain **mission item** — a *Data Chip* / *"Mysterious Package"* — that exists only
to be carried and delivered. It is **bound to you**, **can't be sold or dropped**, and **can't be
activated** by hand (*"Don't peek…"*); the relevant mission consumes it at the right step. The Commune
questline's chip is one example. Treat these as quest baggage, not as gear — don't expect them to *do*
anything in your inventory.

> Because mission items are flagged untradeable and undroppable, they can't clutter the economy or be lost
> by accident, but they will sit in your inventory until the quest that wants them advances.

## See also

- [Story missions](Story-missions) – where mission-item chips come from and go
- [Missions](Missions) – the wider mission system
- [Combat](Combat) – when a Recall Device is the better part of valour
- [Reconstruction kits](Reconstruction-kits) – the *ship's* counterpart to your own recall home

---
*Items & Special Objects: [Reconstruction kits](Reconstruction-kits) · [Maps and charts](Maps-and-charts) · [Deployable beacons](Deployable-beacons) · [Special items](Special-items)*
