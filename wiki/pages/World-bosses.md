<!-- Hand-written page. Sourced from the boss encounter scripts under data/scripts/sector/worldbosses/
     (ancientsentinel.lua, cultship.lua, scrapbot.lua, jester.lua, deathmerchant.lua, lostwmd.lua,
     lostwmdadditionaltorpedoes.lua, cryocolonyship.lua, collector.lua, revoltingprisonship.lua,
     chemicalaccident.lua) and the shared lib/worldbossutility.lua. Display names and special-loot
     drops are read directly from each script. -->
# World bosses

**World bosses** are unique, hand-themed boss ships seeded into the galaxy. Each one is a set-piece: a
distinctive ship, a custom arena, a signature mechanic, and a **guaranteed special drop** — usually a
Legendary turret or a system upgrade you can't reliably get elsewhere. They all share the world-boss
template (huge, double damage, point-defence and anti-fighter guns, a boss health bar, **~60-minute
respawn**, and a beacon left on death) described under
[Special enemies → What makes a "world boss"](Special-enemies#what-makes-a-world-boss).

> These are **not** the same set as the roaming bosses on [Events](Events) (the Big AI, the Guardian,
> the asteroid/laser/shield bosses). Those come from the event system; the ones below are the
> dedicated `worldbosses` encounters with fixed identities and signature loot.

## The bosses

| Boss (in-game name) | Theme | Signature mechanic | Special drop |
|---|---|---|---|
| **Sentinel** *(Ancient Sentinel)* | An ancient automated defence fort, hull replaced with **stone** plating | Heavy **cannon + point-defence** loadout, 1.5× turrets | **Military Targeting** system upgrade |
| **Opportunity** *(Cult Ship)* | A doomsday cult's colony ark, twice normal size | Big and tanky; summons **2 minion ships** | **Hyperspace Booster** system upgrade |
| **Jackpot the Scrap God** *(Scrapper 5000)* | A rogue salvage robot in a hexagonal **laser-fence** arena | Laser + point-defence-laser loadout inside the fence | **Super Salvaging Laser** (Legendary turret) |
| **The Jester** *(Jester)* | A paint-mad crew; the whole ship and arena are **randomly recoloured** | Exotic mixed guns plus **Party Trumpets** | **Party Trumpet** (Legendary turret) |
| **The Merchant** *(Death Merchant)* | A pirate posing as a rich trader; freighter twice normal size | Laser loadout; summons **4 minion ships** | **Trading Overview** system upgrade |
| **Exterminatus** *(Lost WMD)* | An automated doomsday weapon platform bristling with launchers | **Torpedo spam** — every launch also flings extra tracking torpedoes (see below) | **Seeker Cannon** (Legendary turret) |
| **Hope I** *(Cryo Colony Ship)* | A frozen-sleep ark gone paranoid; high hull, lower firepower | Rail-gun loadout, tanky | **Energy Booster** system upgrade |
| **The Collector** *(Collector)* | An ex-Xsotan hunter who steals ship parts, in a ring arena | Rail-gun + plasma mix; summons **3 minion ships** | **Launcher Battery** (Legendary turret) |
| **Complex HSP** *(Revolting Prison Ship)* | A prison overrun by its inmates; **striped hull**, dead suppressor satellites | Bolters + point-defence | **Auto-Targeting** system upgrade |
| **Chemical Transport** *(Chemical Accident)* | A hazmat freighter after a spill; toxic-barrel, fog-filled arena | Custom **Firefly Plasma** guns (~2.5× damage) | **Firefly Plasma Gun** (Legendary turret) |

## Notes on specific fights

**Exterminatus (Lost WMD)** is the mechanical standout. It starts loaded with torpedoes, and a helper
script makes **every torpedo it launches spawn additional homing torpedoes** — Plasma, Sabot and
Kinetic warheads — that lock onto player and alliance ships in the sector. Left alone it becomes a
relentless missile platform, so its anti-torpedo point-defence and your own [Defensive systems](Defensive-systems)
matter a lot here. Watch the warhead types: Sabot pierces shields, so shields alone won't save you.

**Minion bosses** (Opportunity, The Merchant, The Collector) bring escorts that turn aggressive the
moment the fight starts. The boss health bar tracks the boss itself, but you'll usually want to thin the
escorts first so you aren't taking fire from every angle while you chip the main target.

**Themed arenas** aren't just decoration: the Scrapper's laser fence, the Prison Ship's burned-out
**Energy Signature Suppressor** satellites, and the Chemical Transport's leaking toxic barrels all set
the scene and, in the barrels' case, fill the sector with hazard clutter you'll be manoeuvring through.

## Farming

Because a downed world boss **respawns after ~60 minutes** and drops ~6 Rare-or-better items *plus* its
signature reward, the ones with a Legendary turret (Scrapper 5000, Jester, Lost WMD, Collector,
Chemical Accident) are worth revisiting — the special drop is guaranteed each kill. Bookmark the sector
with the beacon the boss leaves behind.

## See also

- [Special enemies](Special-enemies) – the shared world-boss rules, plus summoners, blinkers and loot goons
- [Enemy AI](Enemy-AI) – the behaviour states the bosses and their minions run
- [Rift Expeditions](Rift-Expeditions) – the DLC's own unique boss, the Xsotan Rift Guardian, guarding the way out of a rift
- [Events](Events) – the *other* roaming bosses (Big AI, Guardian, asteroid/laser/shield bosses)
- [Combat](Combat) / [Defensive systems](Defensive-systems) – damage types, point defence and surviving torpedo spam
- [Weapons](Weapons) / [Torpedoes](Torpedoes) – what the Legendary drops actually do

---
*Enemies & Bosses: [Enemy AI](Enemy-AI) · [Special enemies](Special-enemies) · [World bosses](World-bosses)*
