<!-- Hand-written page. Sourced from items/factionmapsegment.lua, items/gatemapupdate.lua,
     items/aimap.lua and items/corruptedaimap.lua. Map names/prices/rarity tiers and what each tier
     reveals (Additional Sectors >= Rare, Sector Stations >= Exceptional, Full Territory >= Exotic)
     come from factionmapsegment's create(); the AI maps' spawn behaviour from their activate(). -->
# Maps and charts

**Maps** are activatable inventory chips that fill in your **Galaxy Map** without you having to fly there.
Most reveal a chunk of some faction's territory — sectors, gate connections, and (at higher quality) the
stations inside them. A couple of special "maps" instead point you at a story target. All of them are
read off a specific **AI faction's** territory, so a map is always *about* one faction.

## Faction territory maps

The common map item comes in **four quality tiers**, each a higher rarity that reveals more. The price
also scales with how rich the faction's home region is.

| Tier (rarity) | In-game name | Area revealed | Gate network | Adds off-grid sectors | Shows stations | Base price |
|---|---|---|:--:|:--:|:--:|--:|
| Common | *Traveler's Quadrant Map* | One quadrant | Yes | No | No | 10,000 |
| Rare | *Explorer's Quadrant Map* | One quadrant | Yes | Yes | No | 30,000 |
| Exceptional | *Faction Quadrant Map* | One quadrant | Yes | Yes | Yes | 250,000 |
| Exotic+ | *Faction Territory Map* | **Full territory** | Yes | Yes | Yes | 500,000 |

A **quadrant** is one corner (NW / NE / SW / SE) of the faction's territory, measured around its home
sector; the chip is fixed to whichever quadrant it was generated for. The **Exotic** version drops the
quadrant restriction and unveils the faction's **entire** territory at once. Prices in the table are the
base values — the actual price is multiplied by the region's richness factor, so deep-galaxy maps cost
more.

> Activating a map runs in the **background** ("Map information added to the Galaxy Map" when it
> finishes). You can't fire off several at once — start one and it blocks the next until it's done. Maps
> only read **AI faction** territory, and the faction's **home sector** is always marked for you.

### Faction Gate Map Update

A cheap companion chip (*Faction Gate Map Update*, price 10) that **refreshes the gate connections**
within a faction's territory for sectors you already know — it rewires the gate links on your Galaxy Map
to the current network ("Network Version 2.0", *"Courtesy of Galaxy Gates United"*). Use it when a
faction's gate layout has changed and your old map is stale. Like the territory maps it runs in the
background and is consumed on use.

## Story tracking chips

Two items look like maps but actually **summon and point you toward a large AI-controlled entity** for the
story. They're Legendary and consumed on use.

| Item | What it does |
|---|---|
| *Maintenance Chip MCAI04* | Reports the next AI's coordinates in chat and arms the spawn so the big AI shows up at your location. |
| *(corrupted chip, name shown as hex)* | The corrupted variant — same idea but spawns the **corrupted** AI, and refuses if one was spawned in the last hour. |

The corrupted chip's name and tooltip are deliberately rendered as **hexadecimal gibberish**
(`4d43 4149 3034`… decodes to "MC AI 04"), a flavour touch for a damaged/encrypted chip. Unlike the
plain chip it is **not** consumed on use and has no sell value, so it can be triggered repeatedly once its
cooldown is up.

## See also

- [Story missions](Story-missions) – the questline the AI-tracking chips feed into
- [Trading and Prices](Trading-and-Prices) – where faction maps are bought and sold
- [Reconstruction kits](Reconstruction-kits) – another family of activatable inventory items
- [Special items](Special-items) – the Recall Device and other one-off gadgets

---
*Items & Special Objects: [Reconstruction kits](Reconstruction-kits) · [Maps and charts](Maps-and-charts) · [Deployable beacons](Deployable-beacons) · [Special items](Special-items)*
