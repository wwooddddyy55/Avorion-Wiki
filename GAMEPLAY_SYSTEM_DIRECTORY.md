## GAMEPLAY SYSTEM DIRECTORY

**Codebase:** Avorion v2.5.x  
**Total gameplay-relevant files catalogued:** ~695 (648 Lua, 45 XML blueprints, 1 SQLite DB)  
**Primary scripting language:** Lua 5.x  
**Root path convention:** All paths are relative to `Avorion/`

> **Exclusions applied:** `.png`, `.dds`, `.fbx`, `.wav`, `.ogg`, asset meshes, shader files, font assets, localization XMLs, and 155 patch-note `.txt` files have been omitted — they contain no gameplay math or rule definitions.

---

## Quick-Reference Priority Index

| Priority | Meaning |
|---|---|
| **[HIGH]** | Core gameplay rule, math formula, or critical data table — analyze first |
| **[MEDIUM]** | Secondary system or content definition — analyze after HIGH dependencies |
| **[LOW]** | Utility scaffold, boilerplate, or UI display helper — analyze last |

---

## 1. Economy & Trading

> Production chains, commodity pricing, factory yields, trade mechanics.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/lib/goods.lua` | Economy/Trading | Master goods/commodity definition table with trade values | **[HIGH]** |
| `data/scripts/lib/goodsindex.lua` | Economy/Trading | Index/lookup table for goods by ID | **[HIGH]** |
| `data/scripts/lib/productions.lua` | Economy/Trading | Factory production recipes and yield ratios | **[HIGH]** |
| `data/scripts/lib/productionsindex.lua` | Economy/Trading | Index of production chain definitions | **[HIGH]** |
| `data/scripts/lib/consumergoods.lua` | Economy/Trading | Consumer goods demand and consumption logic | **[HIGH]** |
| `data/scripts/lib/refineutility.lua` | Economy/Trading | Ore-to-material refinement ratio calculations | **[HIGH]** |
| `data/scripts/lib/tradingmanager.lua` | Economy/Trading | Core trade transaction execution logic | **[HIGH]** |
| `data/scripts/lib/tradingutility.lua` | Economy/Trading | Shared trade helper functions (price checks, availability) | **[MEDIUM]** |
| `data/scripts/lib/merchantutility.lua` | Economy/Trading | NPC merchant behavior utilities | **[MEDIUM]** |
| `data/scripts/lib/shop.lua` | Economy/Trading | Station shop inventory management | **[MEDIUM]** |
| `data/scripts/lib/stationextensions.lua` | Economy/Trading | Station type extension/specialization logic | **[MEDIUM]** |
| `data/scripts/lib/factorymap.lua` | Economy/Trading | Factory placement and distribution on the galaxy map | **[MEDIUM]** |
| `data/scripts/lib/sellabletradinggood.lua` | Economy/Trading | Sellable trading good item wrapper | **[MEDIUM]** |
| `data/scripts/lib/inventoryitemprice.lua` | Economy/Trading | Price calculation logic for inventory items | **[MEDIUM]** |
| `data/scripts/lib/tradeableinventoryitem.lua` | Economy/Trading | Base class for tradeable inventory items | **[MEDIUM]** |
| `data/scripts/sector/background/economyupdater.lua` | Economy/Trading | Per-sector economy tick loop (supply/demand updates) | **[HIGH]** |
| `data/scripts/entity/merchants/` *(38 files)* | Economy/Trading | Individual merchant station type scripts (turret, fighter, research, etc.) | **[MEDIUM]** |
| `data/scripts/player/background/simulation/tradecommand.lua` | Economy/Trading | Automated fleet trade order simulation | **[MEDIUM]** |
| `data/scripts/player/background/simulation/sellcommand.lua` | Economy/Trading | Automated fleet sell order simulation | **[MEDIUM]** |
| `data/scripts/systems/tradingoverview.lua` | Economy/Trading | Trading overview ship system component | **[MEDIUM]** |

---

## 2. Combat & Weapons

> Damage math, weapon type definitions, hit resolution, shield/armor interactions.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/lib/damagetypeutility.lua` | Combat Math | Damage type calculations (kinetic, energy, explosive, etc.) | **[HIGH]** |
| `data/scripts/lib/weapongenerator.lua` | Combat Math | Weapon stat generation and procedural balancing math | **[HIGH]** |
| `data/scripts/lib/weapontype.lua` | Combat Math | Weapon type enum/definition table | **[HIGH]** |
| `data/scripts/lib/weapontypeutility.lua` | Combat Math | Weapon type helper functions | **[MEDIUM]** |
| `data/scripts/lib/turretbalancinganalysis.lua` | Combat Math | Turret DPS/stat balance analysis utilities | **[HIGH]** |
| `data/scripts/lib/turretingredients.lua` | Combat Math | Turret crafting ingredient requirements | **[HIGH]** |
| `data/scripts/lib/sectorturretgenerator.lua` | Combat Math | Sector-level turret procedural generation | **[MEDIUM]** |
| `data/scripts/lib/torpedogenerator.lua` | Combat Math | Torpedo stat generation math | **[HIGH]** |
| `data/scripts/lib/torpedoutility.lua` | Combat Math | Torpedo utility functions (tracking, detonation) | **[MEDIUM]** |
| `data/scripts/systems/defensesystem.lua` | Combat Math | Defense system block mechanic | **[HIGH]** |
| `data/scripts/systems/resistancesystem.lua` | Combat Math | Damage resistance percentage system | **[HIGH]** |
| `data/scripts/systems/weaknesssystem.lua` | Combat Math | Damage weakness/vulnerability multiplier system | **[HIGH]** |
| `data/scripts/systems/shieldimpenetrator.lua` | Combat Math | Shield-piercing mechanic for weapons | **[HIGH]** |
| `data/scripts/systems/shieldbooster.lua` | Combat Math | Shield capacity/recharge booster system | **[HIGH]** |
| `data/scripts/systems/energytoshieldconverter.lua` | Combat Math | Converts excess energy to shield HP | **[HIGH]** |
| `data/scripts/weaponsounds/` *(23 files)* | Combat Math | Weapon type behavior definitions including fire rates and projectile types | **[MEDIUM]** |

---

## 3. Enemy AI & Boss Systems

> NPC decision trees, pursuit logic, world boss encounters, wave spawning.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/entity/ai/patrol.lua` | Enemy AI | Standard patrol route behavior state | **[HIGH]** |
| `data/scripts/entity/ai/patrolpeacefully.lua` | Enemy AI | Non-aggressive patrol behavior | **[HIGH]** |
| `data/scripts/entity/ai/evade.lua` | Enemy AI | Evasion/retreat behavior state | **[HIGH]** |
| `data/scripts/entity/ai/persecutor.lua` | Enemy AI | Enemy pursuit/aggro target-lock behavior | **[HIGH]** |
| `data/scripts/entity/ai/dock.lua` | Enemy AI | Entity docking behavior state | **[MEDIUM]** |
| `data/scripts/entity/ai/docktostation.lua` | Enemy AI | Station docking behavior state | **[MEDIUM]** |
| `data/scripts/entity/ai/trade.lua` | Enemy AI | NPC autonomous trade route behavior | **[MEDIUM]** |
| `data/scripts/entity/ai/tradeutility.lua` | Enemy AI | Trade AI utility functions | **[MEDIUM]** |
| `data/scripts/entity/ai/salvage.lua` | Enemy AI | Salvage collection behavior state | **[MEDIUM]** |
| `data/scripts/entity/ai/harvest.lua` | Enemy AI | Resource harvesting behavior state | **[MEDIUM]** |
| `data/scripts/entity/ai/mine.lua` | Enemy AI | Mining behavior state | **[MEDIUM]** |
| `data/scripts/entity/ai/refineores.lua` | Enemy AI | Ore refinement behavior state | **[MEDIUM]** |
| `data/scripts/entity/ai/landfighters.lua` | Enemy AI | Fighter landing/retrieval behavior | **[MEDIUM]** |
| `data/scripts/entity/ai/passgate.lua` | Enemy AI | Gate transit behavior | **[LOW]** |
| `data/scripts/entity/ai/flythroughgate.lua` | Enemy AI | Gate fly-through navigation | **[LOW]** |
| `data/scripts/entity/ai/passsector.lua` | Enemy AI | Sector transition behavior | **[LOW]** |
| `data/scripts/entity/enemies/worldboss.lua` | Enemy AI | World boss base combat and phase logic | **[HIGH]** |
| `data/scripts/entity/enemies/blinker.lua` | Enemy AI | Blinker enemy teleport-attack behavior | **[HIGH]** |
| `data/scripts/entity/enemies/summoner.lua` | Enemy AI | Summoner enemy minion-spawning mechanic | **[HIGH]** |
| `data/scripts/entity/enemies/lootgoon.lua` | Enemy AI | Loot-drop enemy behavior and drops | **[MEDIUM]** |
| `data/scripts/lib/persecutorutility.lua` | Enemy AI | Shared pursuit/aggro utility functions | **[HIGH]** |
| `data/scripts/lib/waveutility.lua` | Enemy AI | Enemy wave spawning math and timing | **[HIGH]** |
| `data/scripts/lib/worldbossutility.lua` | Enemy AI | World boss shared utility functions | **[HIGH]** |
| `data/scripts/lib/spawnutility.lua` | Enemy AI | General entity spawning utility functions | **[MEDIUM]** |
| `data/scripts/sector/worldbosses/ancientsentinel.lua` | Enemy AI | Ancient Sentinel world boss encounter logic | **[HIGH]** |
| `data/scripts/sector/worldbosses/cultship.lua` | Enemy AI | Cult Ship world boss encounter | **[HIGH]** |
| `data/scripts/sector/worldbosses/scrapbot.lua` | Enemy AI | Scrapbot world boss encounter | **[HIGH]** |
| `data/scripts/sector/worldbosses/jester.lua` | Enemy AI | Jester world boss encounter | **[HIGH]** |
| `data/scripts/sector/worldbosses/deathmerchant.lua` | Enemy AI | Death Merchant world boss encounter | **[HIGH]** |
| `data/scripts/sector/worldbosses/lostwmd.lua` | Enemy AI | Lost WMD world boss encounter | **[HIGH]** |
| `data/scripts/sector/worldbosses/lostwmdadditionaltorpedoes.lua` | Enemy AI | Lost WMD extra torpedo mechanic | **[HIGH]** |
| `data/scripts/sector/worldbosses/cryocolonyship.lua` | Enemy AI | Cryo Colony Ship world boss encounter | **[HIGH]** |
| `data/scripts/sector/worldbosses/collector.lua` | Enemy AI | Collector world boss encounter | **[HIGH]** |
| `data/scripts/sector/worldbosses/revoltingprisonship.lua` | Enemy AI | Revolting Prison Ship world boss encounter | **[HIGH]** |
| `data/scripts/sector/worldbosses/chemicalaccident.lua` | Enemy AI | Chemical Accident world boss/event | **[HIGH]** |
| `data/scripts/sector/background/spawnpersecutors.lua` | Enemy AI | Background persecutor spawning rules | **[HIGH]** |
| `data/scripts/sector/background/spawnbehemoth.lua` | Enemy AI | Behemoth enemy spawning trigger | **[HIGH]** |

---

## 4. Ship Building & Systems

> Block systems, TCS variants, boosters, upgrades, ship stat generation.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/lib/shipgenerator.lua` | Ship Building | Procedural ship generation math and assembly | **[HIGH]** |
| `data/scripts/lib/asyncshipgenerator.lua` | Ship Building | Non-blocking async wrapper for ship generation | **[MEDIUM]** |
| `data/scripts/lib/SectorGenerator.lua` | Ship Building | Sector-level ship/entity generation coordinator | **[HIGH]** |
| `data/scripts/lib/plangenerator.lua` | Ship Building | Blueprint plan generation logic | **[HIGH]** |
| `data/scripts/lib/plangeneratorbase.lua` | Ship Building | Base class for plan generators | **[MEDIUM]** |
| `data/scripts/lib/shiputility.lua` | Ship Building | Ship stat/configuration utility functions | **[MEDIUM]** |
| `data/scripts/lib/shipfounding.lua` | Ship Building | Ship founding/creation initialization | **[MEDIUM]** |
| `data/scripts/plangenerator/lib/generator.lua` | Ship Building | Core plan generator implementation | **[HIGH]** |
| `data/scripts/lib/sectorturretgenerator.lua` | Ship Building | Sector turret generation (NPC/station turrets) | **[MEDIUM]** |
| `data/scripts/lib/sectorfightergenerator.lua` | Ship Building | Sector fighter bay generation | **[MEDIUM]** |
| `data/scripts/lib/fighterutility.lua` | Ship Building | Fighter bay stat utility functions | **[MEDIUM]** |
| `data/scripts/lib/sellablefighter.lua` | Ship Building | Sellable fighter item definition | **[MEDIUM]** |
| `data/scripts/lib/sellabletorpedo.lua` | Ship Building | Sellable torpedo item definition | **[MEDIUM]** |
| `data/scripts/systems/basesystem.lua` | Ship Building | Base class for all ship system components | **[HIGH]** |
| `data/scripts/systems/militarytcs.lua` | Ship Building | Military Thruster Control System logic | **[HIGH]** |
| `data/scripts/systems/civiltcs.lua` | Ship Building | Civil Thruster Control System logic | **[HIGH]** |
| `data/scripts/systems/arbitrarytcs.lua` | Ship Building | Arbitrary TCS variant | **[HIGH]** |
| `data/scripts/systems/autotcs.lua` | Ship Building | Auto-switching TCS system | **[HIGH]** |
| `data/scripts/systems/behemothmilitarytcs.lua` | Ship Building | Behemoth-specific military TCS | **[HIGH]** |
| `data/scripts/systems/behemothciviltcs.lua` | Ship Building | Behemoth-specific civil TCS | **[HIGH]** |
| `data/scripts/systems/batterybooster.lua` | Ship Building | Battery capacity booster system | **[HIGH]** |
| `data/scripts/systems/energybooster.lua` | Ship Building | Energy generation booster | **[HIGH]** |
| `data/scripts/systems/enginebooster.lua` | Ship Building | Engine thrust/speed booster | **[HIGH]** |
| `data/scripts/systems/hyperspacebooster.lua` | Ship Building | Hyperspace range/speed booster | **[HIGH]** |
| `data/scripts/systems/shieldbooster.lua` | Ship Building | Shield capacity booster | **[HIGH]** |
| `data/scripts/systems/radarbooster.lua` | Ship Building | Radar/scanner range booster | **[MEDIUM]** |
| `data/scripts/systems/scannerbooster.lua` | Ship Building | Scanner detail booster | **[MEDIUM]** |
| `data/scripts/systems/lootrangebooster.lua` | Ship Building | Loot collection range booster | **[MEDIUM]** |
| `data/scripts/systems/excessvolumebooster.lua` | Ship Building | Excess volume utilization booster | **[MEDIUM]** |
| `data/scripts/systems/velocitybypass.lua` | Ship Building | Velocity cap bypass system | **[HIGH]** |
| `data/scripts/systems/cargoextension.lua` | Ship Building | Cargo capacity extension system | **[MEDIUM]** |
| `data/scripts/systems/miningsystem.lua` | Ship Building | Mining system component | **[MEDIUM]** |
| `data/scripts/systems/transportersoftware.lua` | Ship Building | Transporter beam system | **[MEDIUM]** |
| `data/scripts/systems/valuablesdetector.lua` | Ship Building | Valuables/anomaly detector system | **[MEDIUM]** |
| `data/scripts/systems/smugglerblocker.lua` | Ship Building | Smuggler detection/blocking system | **[MEDIUM]** |
| `data/scripts/systems/wormholeopener.lua` | Ship Building | Wormhole-opening system component | **[HIGH]** |
| `data/scripts/systems/fightersquadsystem.lua` | Ship Building | Fighter squad launch/retrieval system | **[HIGH]** |
| `data/scripts/systems/behemothcarriersystem.lua` | Ship Building | Behemoth carrier system logic | **[HIGH]** |
| `data/scripts/systems/behemothhyperspacesystem.lua` | Ship Building | Behemoth hyperspace system logic | **[HIGH]** |
| `data/scripts/systems/teleporterkey1.lua` — `teleporterkey8.lua` | Ship Building | 8 teleporter key variants (sector/gate access keys) | **[MEDIUM]** |
| `data/plans/` *(45 XML files)* | Ship Building | Ship and station blueprint definitions (bosses, NPCs, special structures) | **[HIGH]** |

---

## 5. Faction Relations & Warfare

> Faction standing math, reputation deltas, faction war mechanics, alliance system.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/lib/faction.lua` | Faction Relations | Faction data model and relations API | **[HIGH]** |
| `data/scripts/lib/relations.lua` | Faction Relations | Faction relation delta math (gains, penalties) | **[HIGH]** |
| `data/scripts/lib/factionpacks.lua` | Faction Relations | Faction pack/configuration definitions | **[HIGH]** |
| `data/scripts/lib/factioneradicationutility.lua` | Faction Relations | Faction wipe-out/eradication condition logic | **[MEDIUM]** |
| `data/scripts/lib/factionsmap.lua` | Faction Relations | Faction territory map data | **[MEDIUM]** |
| `data/scripts/server/factions.lua` | Faction Relations | Server-side faction initialization and seeding | **[HIGH]** |
| `data/scripts/sector/background/relationchanges.lua` | Faction Relations | Background processing of faction relation changes | **[HIGH]** |
| `data/scripts/sector/background/warzonecheck.lua` | Faction Relations | Warzone detection and state management | **[HIGH]** |
| `data/scripts/sector/factionwar/initfactionwar.lua` | Faction Relations | Faction war initialization and rule setup | **[HIGH]** |
| `data/scripts/sector/factionwar/factionwarbattle.lua` | Faction Relations | Active faction war battle logic | **[HIGH]** |
| `data/scripts/sector/factionwar/factionwarutility.lua` | Faction Relations | Faction war shared utility functions | **[MEDIUM]** |
| `data/scripts/sector/factionwar/temporarydefender.lua` | Faction Relations | Temporary defender spawn logic during faction war | **[MEDIUM]** |
| `data/scripts/sector/neutralzone.lua` | Faction Relations | Neutral zone rules and enforcement | **[HIGH]** |
| `data/scripts/alliance/init.lua` | Faction Relations | Player alliance system initialization | **[MEDIUM]** |
| `data/scripts/events/factionattackssmugglers.lua` | Faction Relations | Faction vs smuggler attack event trigger | **[MEDIUM]** |

---

## 6. World & Sector Generation

> Procedural universe layout, sector types, asteroid fields, gate networks, background simulation.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/server/generatesector.lua` | World Generation | Server-side sector generation entry point | **[HIGH]** |
| `data/scripts/lib/SectorGenerator.lua` | World Generation | Core sector content generation coordinator | **[HIGH]** |
| `data/scripts/lib/asteroidfieldgenerator.lua` | World Generation | Asteroid field density and composition math | **[HIGH]** |
| `data/scripts/lib/asteroidplangenerator.lua` | World Generation | Asteroid shape/plan procedural generation | **[MEDIUM]** |
| `data/scripts/lib/teleportergenerator.lua` | World Generation | Teleporter placement and generation logic | **[MEDIUM]** |
| `data/scripts/lib/ancientgatesmap.lua` | World Generation | Ancient gate network map data | **[HIGH]** |
| `data/scripts/lib/gatesmap.lua` | World Generation | Standard gate network map data | **[HIGH]** |
| `data/scripts/lib/passagemap.lua` | World Generation | Sector passage/tunnel map data | **[HIGH]** |
| `data/scripts/lib/factorymap.lua` | World Generation | Factory station distribution map | **[MEDIUM]** |
| `data/scripts/lib/sectornamegenerator.lua` | World Generation | Procedural sector name generation | **[LOW]** |
| `data/scripts/lib/namepool.lua` | World Generation | Name pool tables for procedural generation | **[LOW]** |
| `data/scripts/lib/galaxy.lua` | World Generation | Galaxy-level utility functions | **[HIGH]** |
| `data/scripts/galaxy/init.lua` | World Generation | Galaxy initialization and seeding | **[HIGH]** |
| `data/scripts/galaxy/server.lua` | World Generation | Galaxy server-side tick and management | **[HIGH]** |
| `data/scripts/galaxy/behemothevent.lua` | World Generation | Behemoth boss galaxy-level event trigger | **[HIGH]** |
| `data/scripts/sectors/` *(36 files)* | World Generation | Sector type template definitions (colony, asteroidfield, wormhole, gates, factoryfield, etc.) | **[HIGH]** |
| `data/scripts/sector/init.lua` | World Generation | Sector initialization script | **[HIGH]** |
| `data/scripts/sector/background/sectorcontentsupdater.lua` | World Generation | Background sector content refresh logic | **[HIGH]** |
| `data/scripts/sector/background/respawnresourceasteroids.lua` | World Generation | Resource asteroid respawn timer logic | **[HIGH]** |
| `data/scripts/sector/background/respawncontainerfield.lua` | World Generation | Container field respawn logic | **[MEDIUM]** |
| `data/scripts/sector/background/respawndefenders.lua` | World Generation | Defender NPC respawn logic | **[MEDIUM]** |
| `data/scripts/sector/background/respawnteleporter.lua` | World Generation | Teleporter object respawn logic | **[MEDIUM]** |
| `data/scripts/sector/background/rebuildstations.lua` | World Generation | Station rebuild/reconstruction logic | **[MEDIUM]** |
| `data/scripts/sector/background/gatecompatibility.lua` | World Generation | Gate compatibility checks between sectors | **[MEDIUM]** |
| `data/scripts/sector/background/escortjumpranges.lua` | World Generation | Escort mission jump range calculations | **[MEDIUM]** |
| `data/scripts/sector/background/wreckagecleanup.lua` | World Generation | Wreckage cleanup timer logic | **[LOW]** |
| `data/scripts/sector/background/radiochatter.lua` | World Generation | Background radio chatter flavor event | **[LOW]** |
| `data/scripts/sector/traders.lua` | World Generation | Passing trader NPC population logic | **[MEDIUM]** |
| `data/scripts/sector/passingships.lua` | World Generation | Background passing ship traffic logic | **[MEDIUM]** |
| `data/scripts/sector/points.lua` | World Generation | Sector interest point/landmark placement | **[MEDIUM]** |
| `data/scripts/sector/eventscheduler.lua` | World Generation | Sector event scheduling/timing system | **[HIGH]** |

---

## 7. Player Progression & Missions

> Mission types, rewards, objectives, building knowledge, tutorials.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/lib/mission.lua` | Player Progression | Mission base class and state machine | **[HIGH]** |
| `data/scripts/lib/structuredmission.lua` | Player Progression | Structured/multi-step mission framework | **[HIGH]** |
| `data/scripts/lib/missionutility.lua` | Player Progression | Shared mission helper functions | **[MEDIUM]** |
| `data/scripts/lib/rewards.lua` | Player Progression | Reward calculation and distribution math | **[HIGH]** |
| `data/scripts/lib/buildingknowledgeutility.lua` | Player Progression | Building knowledge unlock utility functions | **[HIGH]** |
| `data/scripts/player/missions/` *(13 files)* | Player Progression | Mission type definitions (tutorials, escort, explore, search & rescue, settler trek) | **[HIGH]** |
| `data/scripts/player/story/` *(21 files)* | Player Progression | Main story quest progression scripts | **[HIGH]** |
| `data/scripts/player/events/` *(14 files)* | Player Progression | Player-triggered events (alien attack, distress signal, headhunter, etc.) | **[MEDIUM]** |
| `data/scripts/items/buildingknowledge.lua` | Player Progression | Building knowledge item unlock mechanic | **[HIGH]** |
| `data/scripts/player/ui/encyclopedia/` *(4 files)* | Player Progression | In-game encyclopedia chapter content (basics, trade, resource management) | **[LOW]** |
| `data/scripts/lib/ordertypes.lua` | Player Progression | Fleet/ship order type enumeration | **[MEDIUM]** |

---

## 8. NPC Story & Named Characters

> Named story entities, boss characters, wormhole guardians, Xsotan, Swoks.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/entity/story/` *(32 files)* | NPC Story | Named story entity behaviors (Xsotan, Wormhole Guardians, Swoks, boss encounters, etc.) | **[HIGH]** |
| `data/scripts/lib/story/ai.lua` | NPC Story | "The AI" story entity utility functions | **[HIGH]** |
| `data/scripts/lib/story/xsotan.lua` | NPC Story | Xsotan story utility functions | **[HIGH]** |
| `data/scripts/lib/story/swoks.lua` | NPC Story | Swoks story entity utility | **[HIGH]** |
| `data/scripts/lib/story/the4.lua` | NPC Story | "The 4" story arc utility functions | **[HIGH]** |
| `data/scripts/lib/story/scientist.lua` | NPC Story | Scientist NPC story utility | **[MEDIUM]** |
| `data/scripts/lib/story/smuggler.lua` | NPC Story | Smuggler story NPC utility | **[MEDIUM]** |
| `data/scripts/lib/story/adventurerguide.lua` | NPC Story | Adventurer guide NPC utility | **[MEDIUM]** |
| `data/scripts/lib/story/operationexodus.lua` | NPC Story | Operation Exodus story arc utility | **[HIGH]** |
| `data/scripts/lib/story/laserbosslocation.lua` | NPC Story | Laser boss location tracking utility | **[HIGH]** |
| `data/scripts/lib/behemotheventutility.lua` | NPC Story | Behemoth event utility functions | **[HIGH]** |
| `data/scripts/lib/asyncxsotangenerator.lua` | NPC Story | Async Xsotan fleet generation | **[HIGH]** |
| `data/scripts/sector/story/aihealthbar.lua` | NPC Story | "The AI" boss health bar display logic | **[MEDIUM]** |
| `data/scripts/sector/story/bigaihealthbar.lua` | NPC Story | "Big AI" boss health bar display logic | **[MEDIUM]** |
| `data/scripts/sector/story/corruptedaihealthbar.lua` | NPC Story | Corrupted AI boss health bar display | **[MEDIUM]** |
| `data/scripts/sector/story/activateteleport.lua` | NPC Story | Story teleport activation logic | **[MEDIUM]** |
| `data/scripts/sector/story/respawnresearchsatellite.lua` | NPC Story | Research satellite respawn (story) | **[MEDIUM]** |
| `data/scripts/sector/xsotanswarm.lua` | NPC Story | Xsotan swarm sector behavior | **[HIGH]** |
| `data/scripts/sector/xsotanswarmmission.lua` | NPC Story | Xsotan swarm mission logic | **[HIGH]** |
| `data/scripts/sector/cultistbehavior.lua` | NPC Story | Cultist NPC sector behavior | **[MEDIUM]** |
| `data/plans/the_ai.xml` | NPC Story | "The AI" final boss ship blueprint | **[HIGH]** |
| `data/plans/big_ai.xml` | NPC Story | Large AI enemy ship blueprint | **[HIGH]** |
| `data/plans/big_ai_corrupted.xml` | NPC Story | Corrupted variant of Big AI blueprint | **[HIGH]** |
| `data/plans/behemoth1.xml` — `behemoth4.xml` | NPC Story | Behemoth boss ship blueprints (4 variants) | **[HIGH]** |
| `data/plans/cavaliersboss.xml` | NPC Story | Cavaliers boss blueprint | **[HIGH]** |
| `data/plans/laserboss.xml` | NPC Story | Laser Boss blueprint | **[HIGH]** |
| `data/plans/communeboss1.xml` — `communeboss3.xml` | NPC Story | Commune boss blueprints (3 variants) | **[HIGH]** |
| `data/plans/familyboss.xml` | NPC Story | Family faction boss blueprint | **[HIGH]** |

---

## 9. Fleet & Captain Systems

> Automated fleet orders, captain trait generation, background fleet simulation.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/lib/captaingenerator.lua` | Fleet/Captain | Captain stat and trait procedural generation math | **[HIGH]** |
| `data/scripts/lib/captainclass.lua` | Fleet/Captain | Captain class/specialization definitions | **[HIGH]** |
| `data/scripts/lib/captainutility.lua` | Fleet/Captain | Captain utility functions (skill checks, bonuses) | **[MEDIUM]** |
| `data/scripts/lib/asyncpirategenerator.lua` | Fleet/Captain | Async pirate fleet generation | **[MEDIUM]** |
| `data/scripts/player/background/simulation/` *(12+ files)* | Fleet/Captain | Fleet automation command scripts (mine, trade, salvage, patrol, escort, maintenance) | **[HIGH]** |
| `data/scripts/sector/background/boardingutility.lua` | Fleet/Captain | Boarding action utility functions | **[HIGH]** |
| `data/scripts/sector/background/escortjumpranges.lua` | Fleet/Captain | Escort fleet jump range logic | **[MEDIUM]** |

---

## 10. Items & Special Objects

> Inventory items, consumables, maps, reconstruction mechanics.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/items/buildingknowledge.lua` | Items | Building knowledge unlock item mechanic | **[HIGH]** |
| `data/scripts/items/reconstructionkit.lua` | Items | Player respawn/reconstruction item mechanic | **[HIGH]** |
| `data/scripts/items/coopreconstructionkit.lua` | Items | Co-op reconstruction kit variant | **[HIGH]** |
| `data/scripts/items/unbrandedreconstructionkit.lua` | Items | Unbranded reconstruction kit variant | **[MEDIUM]** |
| `data/scripts/items/unbrandedreconstructiontoken.lua` | Items | Unbranded reconstruction token item | **[MEDIUM]** |
| `data/scripts/items/aimap.lua` | Items | AI gateway map item (story progression) | **[HIGH]** |
| `data/scripts/items/corruptedaimap.lua` | Items | Corrupted AI map variant | **[HIGH]** |
| `data/scripts/items/factionmapsegment.lua` | Items | Faction territory map segment item | **[MEDIUM]** |
| `data/scripts/items/gatemapupdate.lua` | Items | Gate network map update item | **[MEDIUM]** |
| `data/scripts/items/recalldevice.lua` | Items | Teleport-to-home-sector item mechanic | **[MEDIUM]** |
| `data/scripts/items/energysuppressor.lua` | Items | Area-denial energy suppression item | **[MEDIUM]** |
| `data/scripts/items/commune3missionitem.lua` | Items | Commune faction mission item | **[MEDIUM]** |
| `data/scripts/items/messagebeaconspawner.lua` | Items | Message beacon placement item | **[LOW]** |
| `data/scripts/items/renamingbeaconspawner.lua` | Items | Sector renaming beacon item | **[LOW]** |
| `data/scripts/items/markerbuoyspawner.lua` | Items | Map marker buoy placement item | **[LOW]** |
| `data/scripts/lib/sellableinventoryitem.lua` | Items | Sellable inventory item base class | **[MEDIUM]** |
| `data/scripts/lib/reconstructionutility.lua` | Items | Reconstruction mechanic utility functions | **[HIGH]** |
| `data/scripts/lib/recalldeviceutility.lua` | Items | Recall device utility functions | **[MEDIUM]** |

---

## 11. Events & Encounter Spawning

> Dynamic event system, pirate attacks, ambushes, wave encounters.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/lib/eventutility.lua` | Events | Shared event system utility functions | **[HIGH]** |
| `data/scripts/events/pirateattack.lua` | Events | Standard pirate attack event logic | **[HIGH]** |
| `data/scripts/events/passiveplayerattack.lua` | Events | Passive threat attack event trigger | **[HIGH]** |
| `data/scripts/events/factionattackssmugglers.lua` | Events | Faction-vs-smuggler combat event | **[MEDIUM]** |
| `data/scripts/events/waveencounters/` *(sub-files)* | Events | Wave-based encounter scripts (pirate king, mothership, hidden treasure, etc.) | **[MEDIUM]** |
| `data/scripts/sector/eventscheduler.lua` | Events | Sector event scheduling and timing system | **[HIGH]** |
| `data/scripts/sector/deleteentitiesonplayersleft.lua` | Events | Entity cleanup when players leave sector | **[LOW]** |

---

## 12. DLC — Rift Expansion

> Rift run constraints, extraction mechanics, Rift sector behaviors.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/dlc/rift/lib/constraints/maxslotsconstraint.lua` | DLC/Rift | Maximum block slot constraint rule for Rift runs | **[HIGH]** |
| `data/scripts/dlc/rift/lib/constraints/` *(4 files)* | DLC/Rift | Rift run hard constraints (cargo, docking, mass, slots) | **[HIGH]** |
| `data/scripts/dlc/rift/lib/extractions/` *(4 files)* | DLC/Rift | Rift extraction type mechanics and reward math | **[HIGH]** |
| `data/scripts/dlc/rift/items/ripcord.lua` | DLC/Rift | Rift escape ripcord item mechanic | **[HIGH]** |
| `data/scripts/dlc/rift/items/xsotancore.lua` | DLC/Rift | Xsotan core item (Rift reward) | **[HIGH]** |
| `data/scripts/dlc/rift/items/` *(5 files)* | DLC/Rift | All Rift-specific items (research probe, extraction wormhole, etc.) | **[HIGH]** |
| `data/scripts/dlc/rift/sector/` *(9 files)* | DLC/Rift | Rift sector behaviors, effects, Xsotan spawners, mission limits | **[HIGH]** |
| `data/scripts/dlc/rift/lib/` *(22 files)* | DLC/Rift | Rift shared library (bonus system, guardian logic, utility functions) | **[MEDIUM]** |

---

## 13. Core Data Store

> Structured game balance tables stored outside of Lua scripts.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/data.db` | Core Data | SQLite database (732 KB) — likely stores game balance curves, stat tables, item configurations, and production data | **[HIGH]** |

> **Note:** Query `data.db` with any SQLite viewer. Table schema should be treated as ground truth for numeric balance values that Lua scripts read at runtime.

---

## 14. Shared Libraries & Utilities

> Cross-system scaffolding, OOP framework, XML parsing, dialog system.

| File Path | System Category | Predicted Function | Priority |
|---|---|---|---|
| `data/scripts/lib/class.lua` | Utility | OOP class system base for all Lua objects | **[LOW]** |
| `data/scripts/lib/callable.lua` | Utility | Callable object pattern utility | **[LOW]** |
| `data/scripts/lib/utility.lua` | Utility | General-purpose helper functions | **[LOW]** |
| `data/scripts/lib/randomext.lua` | Utility | Extended RNG utilities (weighted random, etc.) | **[MEDIUM]** |
| `data/scripts/lib/stringutility.lua` | Utility | String parsing and formatting helpers | **[LOW]** |
| `data/scripts/lib/xml.lua` | Utility | XML parsing utility for blueprint files | **[MEDIUM]** |
| `data/scripts/lib/queue.lua` | Utility | Queue data structure | **[LOW]** |
| `data/scripts/lib/ringbuffer.lua` | Utility | Ring buffer data structure | **[LOW]** |
| `data/scripts/lib/dialogutility.lua` | Utility | Dialog tree utility functions | **[MEDIUM]** |
| `data/scripts/lib/dialogsandbox.lua` | Utility | Dialog sandbox/testing environment | **[LOW]** |
| `data/scripts/lib/tooltipmaker.lua` | Utility | Tooltip text generation helper | **[LOW]** |
| `data/scripts/lib/uicollection.lua` | Utility | UI collection/list utility | **[LOW]** |
| `data/scripts/lib/sync.lua` | Utility | Client-server state synchronization utility | **[MEDIUM]** |
| `data/scripts/lib/defaultscripts.lua` | Utility | Default script attachment definitions | **[LOW]** |
| `data/scripts/lib/testsuite.lua` | Utility | Internal test suite framework | **[LOW]** |
| `data/scripts/lib/entity.lua` | Utility | Entity base class/wrapper | **[MEDIUM]** |
| `data/scripts/lib/player.lua` | Utility | Player base class/wrapper | **[MEDIUM]** |
| `data/scripts/utility/delayedexecute.lua` | Utility | Deferred execution scheduling utility | **[LOW]** |
| `data/scripts/commands/` *(4 files)* | Utility | Console/chat commands (addcrew, echo, knowledge, say) | **[LOW]** |

---

## Summary Statistics

| Category | File Count | Priority Level |
|---|---|---|
| Economy & Trading | ~62 | HIGH |
| Combat & Weapons | ~18 | HIGH |
| Enemy AI & Boss Systems | ~37 | HIGH |
| Ship Building & Systems | ~56 | HIGH |
| Faction Relations & Warfare | ~15 | HIGH |
| World & Sector Generation | ~57 | HIGH |
| Player Progression & Missions | ~55 | HIGH |
| NPC Story & Named Characters | ~35 | HIGH/MEDIUM |
| Fleet & Captain Systems | ~19 | MEDIUM |
| Items & Special Objects | ~20 | MEDIUM |
| Events & Encounter Spawning | ~25 | MEDIUM |
| DLC — Rift Expansion | 36 | HIGH/MEDIUM |
| Core Data Store | 1 | HIGH |
| Shared Libraries & Utilities | ~20 | LOW |
| **TOTAL** | **~460 categorized** | — |

> Remaining uncategorized files (~235) are primarily sub-files within the `entity/story/`, `player/story/`, `entity/merchants/`, and `player/background/simulation/` directories. These should be catalogued during deeper per-system analysis passes.
