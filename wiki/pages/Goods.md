<!-- Generated from data/scripts/lib/goodsindex.lua via wiki/tools/_gen_goods.py. Do not hand-edit. -->
# Goods

**Goods** (also called **commodities** or **trading goods**) are bulk cargo items bought and sold at
stations for profit. Each good has a fixed **base price** and **volume**, and belongs to one or more
**production chains**. Goods are produced by [factories](Production), consumed by population stations, and
moved between sectors by traders. For how prices are calculated at a station, see
**[Trading and Prices](Trading-and-Prices)**.

## Good attributes

| Attribute | Meaning |
|---|---|
| **Base price** | The good's fixed value in credits, before supply/demand, relations and station modifiers. Any good with a defined value of 0 is treated as **500**. |
| **Volume** | Cargo space one unit occupies. Determines how much fits in a cargo bay and how much stock a station can hold. |
| **Tier** | Production/tech level, **0–9**. Higher-tier goods sit deeper in their production chain. Raw resources and special items have no tier. |
| **Importance** | An internal weighting used by factory generation; higher values appear more often as shared inputs (for example Energy Cell, Water, Steel). |
| **Category** | The production chain(s) the good belongs to: Basic, Consumer, Industrial, Military or Technology. |
| **Flags** | Special handling: **Illegal** (contraband), **Dangerous** (hazardous), and the runtime states **Stolen**/**Suspicious**. Stations only trade these if their policies allow it. |

## Production chains

Goods are grouped into five overlapping **production chains**. A chain describes which goods feed into which
products; a single good can belong to several chains (for example, Aluminum is used across all five).

- **Basic** – raw and refined fundamentals (metals, gases, crystals).
- **Consumer** – food, drink and lifestyle goods consumed by population stations.
- **Industrial** – intermediate manufacturing materials.
- **Technology** – high-tech components and devices.
- **Military** – weapons, ammunition and combat equipment.

See [Production](Production) for the full recipe list and [Consumer goods](Consumer-goods) for what each
station type consumes.

## Trade restrictions

Some goods cannot be traded freely:

- **Raw resources** (ores and scrap) are never bought or sold through the normal trade menu – they are processed at resource depots instead. See [Raw resources](#raw-resources) below and [Refining](Refining).
- **Contraband** (illegal goods) is only traded by stations with the matching policy, such as smuggler-friendly outposts. Selling it openly damages relations.
- **Dangerous** goods are legal but flagged hazardous.

**Contraband (illegal goods):** Acron Drug, Morn Drug, Slave.

**Dangerous goods:** Explosive Charge, Fluorine, Gun, Industrial Tesla Coil, Military Tesla Coil, Rocket, Toxic Waste, War Robot, Warhead.

## Raw resources

Ores and scrap are not traded at stations; they are refined into materials at resource depots. **Rich** rift
ores yield **4×** as much material as their standard counterparts. The refine fee scales with your relations
(see [Refining](Refining)).

| Resource | Base price | Volume | Refines into | Rich (4×) |
|---|--:|--:|---|:--:|
| Avorion Ore | 12 | 0.025 | Avorion | — |
| Iron Ore | 2 | 0.025 | Iron | — |
| Naonite Ore | 4 | 0.025 | Naonite | — |
| Ogonite Ore | 9 | 0.025 | Ogonite | — |
| Rift Avorion Ore | 12 | 0.05 | Avorion | Yes |
| Rift Iron Ore | 2 | 0.05 | Iron | Yes |
| Rift Naonite Ore | 4 | 0.05 | Naonite | Yes |
| Rift Ogonite Ore | 9 | 0.05 | Ogonite | Yes |
| Rift Titanium Ore | 3 | 0.05 | Titanium | Yes |
| Rift Trinium Ore | 5 | 0.05 | Trinium | Yes |
| Rift Xanion Ore | 7 | 0.05 | Xanion | Yes |
| Scrap Avorion | 24 | 0.04 | Avorion | — |
| Scrap Iron | 4 | 0.04 | Iron | — |
| Scrap Naonite | 7 | 0.04 | Naonite | — |
| Scrap Ogonite | 18 | 0.04 | Ogonite | — |
| Scrap Titanium | 5 | 0.04 | Titanium | — |
| Scrap Trinium | 10 | 0.04 | Trinium | — |
| Scrap Xanion | 13 | 0.04 | Xanion | — |
| Titanium Ore | 3 | 0.025 | Titanium | — |
| Trinium Ore | 5 | 0.025 | Trinium | — |
| Xanion Ore | 7 | 0.025 | Xanion | — |

## Complete goods list

All 136 normally-tradeable goods.

| Good | Base price | Volume | Tier | Importance | Category | Flags |
|---|--:|--:|:--:|--:|---|---|
| Acid | 402 | 1 | 3 | 2 | Industrial | — |
| Acron Drug | 6,000 | 0.1 | — | 0 | Consumer | Illegal |
| Adhesive | 402 | 0.25 | 3 | 3 | Industrial | — |
| Aluminum | 200 | 1 | 0 | 7 | Basic | — |
| Ammunition | 3,786 | 3 | 5 | 1 | Military | — |
| Ammunition L | 422 | 2.5 | 4 | 0 | Military | — |
| Ammunition M | 422 | 1.5 | 4 | 0 | Military | — |
| Ammunition S | 422 | 0.5 | 4 | 0 | Military | — |
| Antigrav Generator | 71,632 | 2.5 | 8 | 0 | Technology | — |
| Antigrav Unit | 25,391 | 2.5 | 7 | 4 | Technology | — |
| Beer | 216 | 0.5 | 4 | 0 | Consumer | — |
| Bio Gas | 213 | 1 | 2 | 3 | Basic | — |
| Body Armor | 95,906 | 1.5 | 9 | 0 | Military | — |
| Book | 319 | 0.2 | 3 | 0 | Consumer | — |
| Carbon | 423 | 1 | 2 | 5 | Basic | — |
| Cattle | 254 | 1.5 | 2 | 2 | Consumer | — |
| Chemicals | 402 | 1 | 3 | 6 | Industrial | — |
| Chlorine | 150 | 1 | 0 | 1 | Basic | — |
| Clothes | 102 | 1 | 4 | 0 | Consumer | — |
| Coal | 200 | 2 | 0 | 2 | Basic | — |
| Cocoa | 87 | 0.2 | 5 | 0 | Consumer | — |
| Coffee | 187 | 0.2 | 5 | 0 | Consumer | — |
| Computation Mainframe | 37,940 | 1 | 7 | 0 | Technology | — |
| Conductor | 168 | 0.15 | 4 | 9 | Industrial, Technology | — |
| Coolant | 402 | 0.5 | 3 | 4 | Industrial | — |
| Copper | 350 | 1 | 0 | 5 | Basic | — |
| Corn | 28 | 1 | 1 | 5 | Consumer | — |
| Crystal | 190 | 1.5 | 0 | 2 | Basic | — |
| Dairy | 19 | 1 | 3 | 1 | Consumer | — |
| Diamond | 750 | 0.05 | 0 | 3 | Basic | — |
| Display | 7,858 | 1 | 6 | 5 | Technology | — |
| Drill | 20,443 | 20 | 7 | 1 | Industrial | — |
| Drone | 7,754 | 10 | 5 | 0 | Technology | — |
| Electro Magnet | 483 | 0.75 | 5 | 4 | Industrial, Technology | — |
| Electromagnetic Charge | 13,985 | 1 | 6 | 0 | Military | — |
| Electron Accelerator | 125,431 | 12 | 8 | 0 | Technology | — |
| Energy Cell | 50 | 1 | 0 | 43 | Basic | — |
| Energy Container | 1,087 | 4.5 | 5 | 2 | Industrial, Technology | — |
| Energy Generator | 15,957 | 2 | 6 | 3 | Technology | — |
| Energy Inverter | 1,277 | 3 | 6 | 0 | Industrial, Technology | — |
| Energy Tube | 2,895 | 1.5 | 5 | 7 | Technology | — |
| Explosive Charge | 1,423 | 1.5 | 4 | 0 | Military | Dangerous |
| Fabric | 91 | 1 | 3 | 2 | Consumer | — |
| Fertilizer | 319 | 1 | 1 | 3 | Industrial | — |
| Fish | 152 | 0.5 | 2 | 0 | Consumer | — |
| Fluorine | 250 | 1 | 0 | 2 | Basic | Dangerous |
| Food | 300 | 0.5 | 4 | 0 | Consumer | — |
| Food Bar | 223 | 0.5 | 2 | 0 | Consumer | — |
| Force Generator | 49,576 | 4 | 7 | 0 | Technology | — |
| Fruit | 56 | 0.5 | 1 | 2 | Consumer | — |
| Fuel | 1,232 | 1 | 2 | 2 | Industrial | — |
| Fungus | 46 | 1 | 3 | 2 | Consumer | — |
| Fusion Core | 5,114 | 2.5 | 6 | 2 | Technology | — |
| Fusion Generator | 39,553 | 2.5 | 7 | 1 | Technology | — |
| Gauss Rail | 7,735 | 2 | 6 | 1 | Military | — |
| Gem | 400 | 0.05 | 0 | 1 | Basic | — |
| Glass | 182 | 1 | 1 | 3 | Industrial | — |
| Gold | 600 | 0.5 | 0 | 8 | Basic | — |
| Gun | 1,232 | 0.5 | 6 | 1 | Military | Dangerous |
| Helium | 50 | 1 | 0 | 1 | Basic | — |
| High Capacity Lens | 4,689 | 1 | 3 | 0 | Industrial, Technology | — |
| High Pressure Tube | 1,650 | 2 | 5 | 2 | Industrial, Technology | — |
| Hydrogen | 150 | 1 | 0 | 2 | Basic | — |
| Industrial Tesla Coil | 10,314 | 5.5 | 7 | 0 | Industrial, Technology | Dangerous |
| Jewelry | 1,260 | 0.2 | 1 | 0 | Consumer | — |
| Laser Compressor | 6,577 | 1.5 | 6 | 0 | Technology | — |
| Laser Head | 4,690 | 2 | 5 | 1 | Technology | — |
| Laser Modulator | 16,742 | 3 | 6 | 0 | Technology | — |
| Lead | 200 | 1 | 0 | 1 | Basic | — |
| Leather | 37 | 0.5 | 3 | 0 | Consumer | — |
| Liquor | 1,867 | 1.25 | 2 | 0 | Consumer | — |
| Luxury Food | 6,452 | 2.5 | 6 | 0 | Consumer | — |
| Meat | 37 | 0.5 | 3 | 2 | Consumer | — |
| Medical Supplies | 3,006 | 1 | 4 | 0 | Consumer, Technology | — |
| Metal Plate | 792 | 3 | 4 | 5 | Industrial | — |
| Microchip | 896 | 0.1 | 5 | 7 | Technology | — |
| Military Tesla Coil | 10,314 | 4.5 | 7 | 0 | Military | Dangerous |
| Mineral | 500 | 1.5 | 0 | 3 | Basic | — |
| Mining Robot | 145,977 | 8 | 9 | 0 | Industrial, Technology | — |
| Morn Drug | 5,000 | 0.1 | — | 0 | Consumer | Illegal |
| Nanobot | 1,338 | 0.5 | 5 | 4 | Technology | — |
| Neon | 200 | 1 | 0 | 2 | Basic | — |
| Neutron Accelerator | 125,431 | 15 | 8 | 0 | Technology | — |
| Nitrogen | 40 | 1 | 0 | 2 | Basic | — |
| Oil | 490 | 1 | 1 | 4 | Industrial | — |
| Ore | 70 | 2 | 0 | 2 | Basic | — |
| Oxygen | 80 | 1 | 0 | 6 | Basic | — |
| Paint | 481 | 1 | 4 | 1 | Industrial | — |
| Paper | 46 | 1 | 2 | 1 | Consumer | — |
| Plankton | 50 | 1 | 0 | 1 | Consumer | — |
| Plant | 14 | 1.5 | 1 | 0 | Consumer | — |
| Plasma Cell | 174 | 0.25 | 4 | 8 | Technology | — |
| Plastic | 137 | 0.5 | 2 | 9 | Industrial | — |
| Platinum | 750 | 0.5 | 0 | 7 | Basic | — |
| Potato | 24 | 1 | 1 | 1 | Consumer | — |
| Power Unit | 1,211 | 5 | 5 | 8 | Industrial, Technology | — |
| Processor | 7,858 | 0.1 | 6 | 8 | Technology | — |
| Protein | 34 | 0.1 | 4 | 0 | Consumer | — |
| Proton Accelerator | 125,431 | 15 | 8 | 0 | Technology | — |
| Raw Oil | 150 | 1 | 0 | 1 | Basic | — |
| Rice | 15 | 1 | 1 | 2 | Consumer | — |
| Rift Research Data | 5,000 | 0.5 | — | 0 | Technology | — |
| Rocket | 11,250 | 4 | 6 | 0 | Military | Dangerous |
| Rubber | 686 | 1 | 2 | 1 | Industrial | — |
| Satellite | 65,714 | 15 | 7 | 0 | Technology | — |
| Scrap Metal | 25 | 3 | 0 | 1 | Basic | — |
| Semi Conductor | 129 | 0.1 | 4 | 5 | Technology | — |
| Servo | 1,387 | 0.25 | 5 | 3 | Industrial, Technology | — |
| Sheep | 130 | 1 | 2 | 1 | Consumer | — |
| Silicon | 500 | 1 | 0 | 3 | Basic | — |
| Silver | 300 | 0.5 | 0 | 3 | Basic | — |
| Slave | 15,000 | 1 | — | 0 | — | Illegal |
| Solar Cell | 469 | 2 | 1 | 1 | Technology | — |
| Solar Panel | 6,858 | 6 | 5 | 1 | Technology | — |
| Solvent | 402 | 1 | 3 | 2 | Industrial | — |
| Spices | 268 | 0.3 | 5 | 1 | Consumer | — |
| Steel | 277 | 1 | 1 | 22 | Industrial | — |
| Steel Tube | 704 | 3 | 4 | 3 | Industrial | — |
| Targeting Card | 11,873 | 0.5 | 6 | 1 | Military | — |
| Targeting System | 29,674 | 0.75 | 8 | 0 | Military | — |
| Tea | 37 | 0.2 | 1 | 0 | Consumer | — |
| Teleporter | 39,365 | 12 | 8 | 3 | Technology | — |
| Tools | 214 | 0.4 | 4 | 0 | Industrial, Technology | — |
| Toxic Waste | 15 | 4 | — | 0 | Basic | Dangerous |
| Transformator | 209 | 0.2 | 4 | 11 | Industrial, Technology | — |
| Turbine | 16,729 | 7.5 | 6 | 1 | Industrial, Technology | — |
| Vegetable | 32 | 1 | 1 | 1 | Consumer | — |
| Vehicle | 77,087 | 25 | 8 | 0 | Industrial | — |
| War Robot | 92,186 | 8 | 9 | 0 | Military | Dangerous |
| Warhead | 5,630 | 3 | 5 | 1 | Military | Dangerous |
| Water | 20 | 0.35 | 0 | 24 | Consumer | — |
| Wheat | 23 | 1 | 1 | 9 | Consumer | — |
| Wine | 182 | 0.5 | 4 | 1 | Consumer | — |
| Wire | 95 | 0.5 | 4 | 6 | Industrial, Technology | — |
| Wood | 350 | 2.5 | 1 | 1 | Consumer | — |
| Zinc | 250 | 1 | 0 | 3 | Basic | — |

## See also

- [Trading and Prices](Trading-and-Prices) – how station prices are calculated
- [Production](Production) – factory recipes that produce these goods
- [Refining](Refining) – turning ores and scrap into materials
- [Consumer goods](Consumer-goods) – what each station type consumes

---
*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods)*
