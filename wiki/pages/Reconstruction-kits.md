<!-- Hand-written page. Sourced from items/reconstructionkit.lua, items/coopreconstructionkit.lua,
     items/unbrandedreconstructionkit.lua, items/unbrandedreconstructiontoken.lua and
     lib/reconstructionutility.lua. Prices, stackable/droppable/depleteOnUse flags and the malus
     rules are read straight from those files (the 50% durability malus is the
     math.min(hpMalusFactor, 0.5) in each kit's activate). -->
# Reconstruction kits

**Reconstruction kits** bring a destroyed ship back from its wreckage instead of letting it stay gone.
When a ship of yours is blown up, it leaves a **wreckage** behind in that sector; activate a
reconstruction kit nearby and the ship is **reassembled on the spot** — but it comes back damaged and
needs further repairs. This is separate from your *own* respawn (which always happens at your
Reconstruction Site); kits are about saving the **ship**.

> Kits work off the wreckage, so they only function **in the same sector** the craft was destroyed in,
> while the wreckage is still there. A ship that was "lost in a rift" can't be reconstructed.

## What you always get back

However you reconstruct a ship, the result is the same handful of rules:

- The craft is **rebuilt where the wreckage is**, in the sector you're standing in.
- Its **cargo bay is emptied** — anything it was carrying is gone.
- It comes back with a **durability malus of at least 50%** (its maximum HP is roughly halved, or worse if
  it was already heavily damaged before it died). The tooltips spell this out: *"Disclaimer: Additional
  Repairs Necessary!"* You'll want to repair it at a shipyard or with a repair dock afterwards.
- Every kit is **consumed on use** ("Depleted on Use").

## The three kits

| Kit | In-game name | Price | Stacks? | Binds to | Notes |
|---|---|--:|:--:|---|---|
| Standard | *Q-n-D Reconstruction Kit* | 10,000 | Yes | One specific ship + owner | The normal bound kit |
| Co-op | *Co-'n-Op Reconstruction Kit* | 50,000 | No | Any ship, any player | Reconstructs whatever wreckage it finds |
| Unbound | *Unbound Q-n-D Reconstruction Kit* | 10,000 | Yes | Nothing yet — you bind it | Turns into a standard kit for your current ship |

### Standard kit — *Q-n-D Reconstruction Kit*

The everyday kit. It is **bound to one specific craft and its owner**: the kit knows the ship's name and
faction, and it will only rebuild *that* ship. To use it you must be **in the same sector as that ship's
wreckage**; otherwise it tells you *"Wreckage not found."* Bound kits are typically created at **Exotic**
rarity for a craft you own.

### Co-op kit — *Co-'n-Op Reconstruction Kit*

The multiplayer rescue kit. It isn't bound to anything and will reconstruct **any destroyed ship whose
wreckage is in the sector**. When several wrecks are present it **prioritises other players** (and their
alliances) over yourself — you're put last in line, so you can revive a teammate's ship before your own.
You must be **flying a ship** to use it (there's no reviving yourself out of nothing), and the
reconstructed ship also gets a slow **heal-over-time** as a small bonus. It does **not stack**, and costs
five times what the standard kit does.

### Unbound kit — *Unbound Q-n-D Reconstruction Kit*

A **blank** kit you bind yourself. Activate it **while sitting in a ship** and it converts into a standard
(bound) *Q-n-D Reconstruction Kit* for **that** ship, dropped into your inventory ready for later. Handy
for keeping spare insurance on a new ship without buying a fresh bound kit each time. It's a **Legendary**
item and stacks.

> There is also an *unbranded reconstruction token* script in the game files, but it's a dead
> backwards-compatibility stub that just forwards to the unbound kit — it's not a separate item you'll
> meet in normal play.

## See also

- [Combat](Combat) – how ships take damage and get destroyed in the first place
- [Defensive systems](Defensive-systems) – shields and resistances that keep a ship out of the wreckage stage
- [Maps and charts](Maps-and-charts) – other activatable inventory items
- [Special items](Special-items) – the Recall Device, which sends you to your Reconstruction Site

---
*Items & Special Objects: [Reconstruction kits](Reconstruction-kits) · [Maps and charts](Maps-and-charts) · [Deployable beacons](Deployable-beacons) · [Special items](Special-items)*
