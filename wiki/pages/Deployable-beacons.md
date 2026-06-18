<!-- Hand-written page. Sourced from items/messagebeaconspawner.lua, items/renamingbeaconspawner.lua
     and items/markerbuoyspawner.lua. Prices, rarity (all Uncommon), the 20-buoy-per-sector cap, the
     sector-control requirement for renaming, and the "only the owner can edit" message rule are read
     from each item's create()/activate(). -->
# Deployable beacons

These are **placeable objects** you deploy from your inventory: you fly somewhere, activate the item, and
it spawns a small beacon or buoy that stays in the sector. They're all **Uncommon** rarity and **consumed
on use**, and they're about leaving information behind rather than fighting. There are three.

| Item | In-game name | Price | Stacks? | What it leaves behind |
|---|---|--:|:--:|---|
| Message beacon | *PCL Message Transmitter* | 30,000 | No | A beacon others can read a message from |
| Renaming beacon | *IGA-1510 Sector Label Applicator* | 50,000 | No | Renames the whole sector (permanent) |
| Marker buoy | *In-Sector Marker Buoy* | 5,000 | Yes | A simple marker at a spot in the sector |

## Message beacon — leave a note

Deploys a beacon carrying a **text message** that anyone in the sector can read. **Only the owner** of the
beacon can edit its message, so it's safe to use as a signpost or a note to other players without them
overwriting it. Visibility is **sector-wide**. The beacon is non-dockable and can't be transferred to
another faction.

## Renaming beacon — name a sector

Deploys a beacon that **renames the sector itself**, and the new name is **permanent**. The catch is
ownership: you can only deploy it in a sector **you or your alliance control**. Try it anywhere else —
uncontrolled space, an AI faction's sector, or inside a rift — and it refuses with *"Can't deploy beacon
in a sector that you don't control."* If you're renaming on behalf of your **alliance**, you also need the
*Manage Stations* alliance privilege.

## Marker buoy — flag a spot

The cheap, stackable one. It drops a plain **marker buoy** at a point in the sector to flag a location —
a stash, a rendezvous, a hazard. There's a hard cap of **20 marker buoys per sector**; beyond that it
refuses with *"Too many marker buoys."* The buoy is placed just in front of your ship and drifts very
slowly. Because it stacks and is cheap, it's the one you'll carry a bundle of.

> All three spawn the object **right next to your ship**, so you need to be flying a craft to deploy one.

## See also

- [Trading and Prices](Trading-and-Prices) – where these consumables are bought
- [Maps and charts](Maps-and-charts) – revealing space on the Galaxy Map instead of marking it in-sector
- [Player stations](Player-stations) – the bigger version of "controlling a sector"
- [Reconstruction kits](Reconstruction-kits) · [Special items](Special-items) – the other inventory gadgets

---
*Items & Special Objects: [Reconstruction kits](Reconstruction-kits) · [Maps and charts](Maps-and-charts) · [Deployable beacons](Deployable-beacons) · [Special items](Special-items)*
