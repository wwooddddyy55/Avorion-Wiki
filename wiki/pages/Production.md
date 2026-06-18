<!-- Generated from data/scripts/lib/productionsindex.lua via wiki/tools/_gen_production.py. Do not hand-edit. -->
# Production

**Production** is the process by which **factories** and **mines** turn input [goods](Goods) into more
valuable output goods. Buying a factory's inputs cheaply and selling its outputs is a core source of credit
income, and chaining factories that feed each other is the basis of an industrial empire. This page lists
every production recipe in the game. For how the resulting goods are priced when traded, see
**[Trading and Prices](Trading-and-Prices)**.

## How factories work

Each factory runs a fixed **recipe**: it consumes a set of **ingredients** and produces one or more
**results**, sometimes alongside low-value **byproducts**. A factory only produces while it has all of its
required ingredients in stock; **optional** ingredients (marked *opt.* below, usually Energy Cells) speed up
or improve production but are not strictly required.

Larger factories process proportionally more goods per cycle. (The exact per-cycle timing and the
factory-size output multiplier are handled by the game engine and are not defined in the recipe data.)

## Factory types

Recipes come in several **styles**, which mostly affect appearance and how the factory is generated:

- **Mine** – extracts a raw good from an asteroid with no inputs (also **Oil Rig**).
- **Collector** – gathers gases or other goods from the environment with no inputs.
- **Factory** – the standard converter: consumes ingredients to make products.
- **Farm** / **Ranch** – agricultural producers (crops, livestock), usually needing Water.
- **SolarPowerPlant** – produces Energy Cells from sunlight.

## Factory cost

The cost to **found** a factory is based on how much value its recipe adds – the difference between the
value of one cycle's outputs and its inputs:

$$\text{cost} = 2{,}500{,}000 + 3500 \times (\text{output value} - \text{input value})$$

with a minimum of **2,500,000** credits. The cost to **upgrade** an existing factory to a larger size adds
byproduct value to the outputs and scales with the target size:

$$\text{upgrade cost} = 1000 \times \text{size} \times (\text{output value} + \text{byproduct value} - \text{input value})$$

The *Build cost* column below applies the founding formula using base good prices.

## Production recipes

All 125 production recipes. Quantities are per production cycle.

| Factory | Type | Requires | Produces | Byproducts | Build cost |
|---|---|---|---|---|--:|
| Aluminum Mine | Mine | — | 10× Aluminum | — | 9,500,000 |
| Ammunition Factory | Factory | 1× Steel<br>15× Chemicals<br>15× Paint | 5× Ammunition | 1× Toxic Waste | 21,428,000 |
| Ammunition Factory | Factory | 10× Lead<br>10× Aluminum<br>10× Steel<br>5× Adhesive<br>5× Energy Cell | 15× Ammunition S<br>10× Ammunition M<br>5× Ammunition L | — | 15,205,000 |
| Antigrav Generator Factory | Factory | 4× Electro Magnet<br>5× Servo<br>10× Wire<br>1× Antigrav Unit<br>1× Energy Generator | 1× Antigrav Generator | — | 74,134,500 |
| Antigrav Unit Factory | Factory | 2× Power Unit<br>2× Processor<br>1× Energy Cell *(opt.)* | 1× Antigrav Unit | — | 27,710,500 |
| Brewery | Factory | 150× Water<br>50× Wheat<br>10× Fungus | 30× Beer | — | 9,045,000 |
| Body Armor Factory | Factory | 2× Metal Plate<br>1× Coolant<br>1× Teleporter<br>1× Antigrav Unit<br>1× Carbon<br>1× Nanobot | 1× Body Armor | — | 98,410,500 |
| Book Factory | Factory | 20× Paper<br>1× Energy Cell *(opt.)* | 4× Book | — | 3,571,000 |
| Carbon Extractor | Factory | 52× Corn | 5× Carbon | — | 4,806,500 |
| Carbon Extractor | Factory | 95× Rice | 5× Carbon | — | 4,915,000 |
| Carbon Extractor | Factory | 64× Wheat | 5× Carbon | — | 4,750,500 |
| Carbon Extractor | Factory | 63× Potato | 5× Carbon | — | 4,610,500 |
| Cattle Ranch | Ranch | 15× Wheat<br>10× Oxygen<br>15× Water | 8× Cattle | 1× Bio Gas | 4,554,500 |
| Cattle Ranch | Ranch | 15× Corn<br>10× Oxygen<br>15× Water | 8× Cattle<br>2× Bio Gas | — | 5,783,000 |
| Chemical Factory | Factory | 5× Water<br>5× Nitrogen<br>5× Hydrogen<br>5× Oxygen<br>1× Bio Gas<br>1× Carbon<br>10× Energy Cell | 2× Chemicals<br>1× Adhesive<br>2× Coolant<br>2× Solvent<br>2× Acid | — | 6,112,000 |
| Clothes Factory | Factory | 80× Fabric | 100× Clothes | — | 12,720,000 |
| Coal Mine | Mine | — | 4× Coal | — | 5,300,000 |
| Cocoa Farm | Farm | 1× Energy Cell *(opt.)*<br>30× Water<br>2× Fertilizer | 20× Cocoa | 1× Oxygen | 4,082,000 |
| Coffee Farm | Farm | 1× Energy Cell *(opt.)*<br>35× Water<br>2× Fertilizer | 10× Coffee | 1× Oxygen | 4,187,000 |
| Computation Mainframe Factory | Factory | 2× Processor<br>1× Power Unit<br>1× Microchip<br>1× Display<br>15× Wire | 1× Computation Mainframe | — | 40,419,000 |
| Conductor Factory | Factory | 2× Zinc<br>2× Steel<br>1× Platinum<br>1× Gold<br>1× Energy Cell *(opt.)* | 20× Conductor | — | 5,671,000 |
| Copper Mine | Mine | — | 5× Copper | — | 8,625,000 |
| Corn Farm | Farm | 4× Energy Cell *(opt.)*<br>60× Water | 60× Corn | 4× Oxygen | 3,480,000 |
| Crystal Farm | Factory | — | 10× Crystal | — | 9,150,000 |
| Dairy Farm | Farm | 10× Cattle | 180× Dairy<br>10× Leather | — | 6,875,000 |
| Computer Component Factory | Factory | 15× Wire<br>7× Microchip<br>5× Semi Conductor<br>5× Copper<br>5× Platinum<br>5× Gold | 1× Display<br>1× Targeting Card<br>1× Processor | — | 40,114,500 |
| Display Factory | Factory | 1× Glass<br>5× Microchip<br>3× Semi Conductor<br>1× Plasma Cell | 1× Display | — | 11,722,500 |
| Drill Factory | Factory | 1× Laser Head<br>1× Processor<br>2× Steel<br>2× Diamond | 1× Drill | 1× Scrap Metal | 22,943,500 |
| Drone Factory | Factory | 1× Fuel<br>2× Plasma Cell<br>5× Metal Plate | 1× Drone | 1× Scrap Metal | 10,249,000 |
| Electro Magnet Factory | Factory | 1× Steel<br>1× Copper<br>2× Conductor<br>2× Transformator | 4× Electro Magnet | — | 4,428,500 |
| Electromagnetic Charge Factory | Factory | 10× Energy Container<br>6× Electro Magnet<br>2× Energy Tube<br>2× Transformator | 2× Electromagnetic Charge | — | 30,479,000 |
| Solar Power Plant | SolarPowerPlant | — | 25× Energy Cell | — | 6,875,000 |
| Energy Container Factory | Factory | 9× Energy Cell<br>9× Transformator | 3× Energy Container | — | 5,755,000 |
| Energy Generator Factory | Factory | 15× Energy Cell<br>10× Microchip<br>10× Conductor | 1× Energy Generator | — | 18,484,500 |
| Energy Inverter Factory | Factory | 1× Energy Tube<br>2× Conductor<br>2× Transformator | 4× Energy Inverter | — | 7,606,500 |
| Energy Tube Factory | Factory | 1× Plastic<br>1× Steel<br>1× Platinum<br>1× Neon<br>1× Steel Tube<br>1× Energy Cell *(opt.)* | 1× Energy Tube | — | 5,219,500 |
| Explosive Charge Factory | Factory | 4× Fluorine<br>1× Steel<br>2× Energy Cell<br>2× Plastic<br>2× Chemicals<br>2× Acid<br>2× Adhesive | 4× Explosive Charge | — | 8,201,500 |
| Fabric Factory | Factory | 15× Sheep | 30× Fabric | — | 5,230,000 |
| Fertilizer Factory | Factory | 2× Chemicals<br>3× Mineral<br>1× Energy Cell *(opt.)*<br>1× Solvent *(opt.)* | 11× Fertilizer | 1× Toxic Waste | 5,135,500 |
| Fertilizer Factory | Factory | 1× Plankton<br>4× Mineral<br>1× Energy Cell *(opt.)* | 9× Fertilizer | 1× Toxic Waste | 5,198,500 |
| Fish Farm | Factory | 23× Water<br>5× Wheat<br>5× Oxygen | 8× Fish<br>1× Bio Gas | 1× Plankton | 4,089,000 |
| Food Factory | Factory | 50× Wheat<br>10× Meat<br>10× Corn<br>10× Vegetable | 10× Food | — | 5,580,000 |
| Food Bar Factory | Factory | 1× Energy Cell *(opt.)*<br>50× Wheat<br>10× Corn<br>10× Rice | 10× Food Bar | — | 4,600,000 |
| Force Generator Factory | Factory | 4× Electro Magnet<br>10× Steel<br>10× Plastic<br>10× Nanobot<br>1× Energy Generator | 1× Force Generator | — | 52,084,500 |
| Fruit Farm | Farm | 4× Energy Cell *(opt.)*<br>80× Water | 40× Fruit | 4× Oxygen | 4,040,000 |
| Fuel Factory | Factory | 2× Energy Cell<br>1× Oil<br>1× Nitrogen<br>1× Fluorine | 1× Fuel | 1× Toxic Waste | 3,732,000 |
| Fungus Farm | Farm | 1× Bio Gas<br>5× Water<br>1× Mineral | 25× Fungus | 1× Toxic Waste | 3,679,500 |
| Fusion Core Factory | Factory | 1× Hydrogen<br>1× Gold<br>2× Plasma Cell<br>2× Transformator<br>2× Energy Tube | 2× Fusion Core | — | 12,727,000 |
| Fusion Generator Factory | Factory | 4× Fusion Core<br>10× Steel<br>15× Plasma Cell<br>2× Power Unit | 1× Fusion Generator | — | 42,032,500 |
| Gauss Rail Factory | Factory | 10× Energy Cell<br>6× Electro Magnet<br>2× Energy Tube<br>1× High Pressure Tube<br>1× Transformator | 2× Gauss Rail | — | 17,980,500 |
| Glass Manufacturer | Factory | 4× Ore<br>4× Crystal | 8× Glass | — | 3,956,000 |
| Noble Metal Mine | Mine | — | 1× Gold<br>1× Platinum | — | 7,225,000 |
| Gun Factory | Factory | 1× Steel<br>1× Ammunition<br>1× Aluminum<br>1× Plastic | 5× Gun | — | 8,660,000 |
| Gas Collector | Collector | — | 3× Helium<br>3× Hydrogen<br>3× Neon<br>3× Chlorine | — | 8,275,000 |
| Gas Collector | Collector | — | 3× Helium<br>3× Nitrogen<br>3× Neon<br>3× Chlorine<br>3× Fluorine | — | 9,745,000 |
| Gas Collector | Collector | — | 3× Helium<br>3× Hydrogen<br>3× Chlorine<br>3× Fluorine | — | 8,800,000 |
| High Capacity Lens Factory | Factory | 4× Glass<br>2× Carbon<br>2× Plastic<br>2× Diamond | 1× High Capacity Lens | — | 7,193,500 |
| High Pressure Tube Factory | Factory | 1× Steel<br>1× Aluminum<br>2× Carbon<br>2× Adhesive<br>2× Steel Tube | 3× High Pressure Tube | — | 7,452,500 |
| Jewelry Manufacturer | Factory | 2× Platinum<br>5× Gem | 4× Jewelry | — | 7,890,000 |
| Jewelry Manufacturer | Factory | 1× Gold<br>4× Diamond | 4× Jewelry | — | 7,540,000 |
| Laser Compressor Factory | Factory | 1× Plasma Cell<br>1× Transformator<br>1× Energy Tube<br>15× Wire | 1× Laser Compressor | 1× Scrap Metal | 9,059,000 |
| Laser Head Factory | Factory | 1× Glass<br>1× Conductor<br>15× Aluminum<br>1× Energy Cell *(opt.)* | 1× Laser Head | 1× Toxic Waste | 7,015,000 |
| Laser Modulator Factory | Factory | 4× Servo<br>2× Energy Tube<br>2× Transformator<br>4× Energy Cell | 1× Laser Modulator | — | 19,251,000 |
| Lead Mine | Mine | — | 10× Lead | — | 9,500,000 |
| Distillery | Factory | 10× Energy Cell<br>50× Wheat<br>250× Water | 5× Liquor | — | 11,897,500 |
| Luxury Food Factory | Factory | 1× Energy Cell *(opt.)*<br>50× Wheat<br>10× Fruit<br>6× Spices<br>7× Wine | 1× Luxury Food | — | 8,835,000 |
| Meat Factory | Factory | 10× Cattle | 85× Meat<br>10× Leather | — | 5,912,500 |
| Medical Supplies Factory | Factory | 5× Water<br>15× Chemicals<br>5× Fabric<br>5× Zinc<br>5× Chlorine | 4× Medical Supplies | — | 14,536,500 |
| Metal Plate Factory | Factory | 3× Steel<br>1× Silver | 2× Metal Plate | — | 4,085,500 |
| Microchip Factory | Factory | 4× Wire<br>12× Semi Conductor<br>4× Energy Cell *(opt.)* | 3× Microchip | — | 4,460,000 |
| Tesla Coil Factory | Factory | 10× Steel<br>3× Copper<br>2× Fusion Core<br>5× Plastic | 1× Military Tesla Coil<br>1× Industrial Tesla Coil | — | 23,132,500 |
| Mineral Extractor | Factory | — | 4× Mineral | — | 9,500,000 |
| Mining Robot Factory | Factory | 1× Power Unit<br>1× Processor<br>1× Display<br>5× Nanobot<br>2× Drill<br>1× Coolant<br>1× Teleporter | 1× Mining Robot | 1× Scrap Metal | 148,474,500 |
| Nanobot Factory | Factory | 15× Crystal<br>15× Semi Conductor | 5× Nanobot | — | 9,167,500 |
| Accelerator Factory | Factory | 3× Turbine<br>3× Plasma Cell<br>3× Fusion Generator<br>6× Energy Tube<br>6× High Pressure Tube<br>15× Conductor<br>9× Gauss Rail | 1× Neutron Accelerator<br>1× Proton Accelerator<br>1× Electron Accelerator | — | 378,820,000 |
| Oil Refinery | Factory | 5× Energy Cell<br>10× Raw Oil | 5× Oil | — | 4,950,000 |
| Ore Mine | Mine | — | 30× Ore | — | 9,850,000 |
| Gas Collector | Collector | — | 8× Oxygen<br>8× Hydrogen<br>8× Nitrogen | — | 10,060,000 |
| Paint Manufacturer | Factory | 1× Oil<br>1× Water<br>1× Chemicals<br>1× Solvent<br>1× Acid | 5× Paint | 1× Toxic Waste | 4,911,500 |
| Paper Factory | Factory | 30× Water<br>2× Wood | 40× Paper | — | 4,390,000 |
| Plankton Collector | Collector | — | 35× Plankton | — | 8,625,000 |
| Plant Farm | Farm | 6× Energy Cell *(opt.)*<br>30× Water | 60× Plant | 6× Oxygen | 2,290,000 |
| Plasma Cell Factory | Factory | 10× Energy Cell<br>1× Steel<br>1× Bio Gas<br>1× Neon<br>1× Helium | 10× Plasma Cell | — | 4,250,000 |
| Plastic Manufacturer | Factory | 3× Oil<br>3× Energy Cell *(opt.)* | 15× Plastic | — | 4,022,500 |
| Potato Farm | Farm | 6× Energy Cell *(opt.)*<br>30× Water | 35× Potato | 8× Oxygen | 2,290,000 |
| Power Unit Factory | Factory | 2× Transformator<br>2× Energy Cell<br>2× Plasma Cell | 1× Power Unit | — | 3,707,500 |
| Processor Factory | Factory | 7× Microchip<br>5× Semi Conductor<br>5× Copper<br>5× Platinum<br>5× Gold | 3× Processor | — | 31,049,500 |
| Protein Factory | Factory | 25× Meat<br>80× Dairy | 100× Protein | — | 5,842,500 |
| Oil Rig | Mine | — | 5× Raw Oil | — | 5,125,000 |
| Rice Farm | Farm | 4× Energy Cell *(opt.)*<br>40× Water | 76× Rice | 4× Oxygen | 2,990,000 |
| Rocket Factory | Factory | 1× Warhead<br>1× Fuel<br>1× Steel<br>1× Microchip | 1× Rocket | — | 13,752,500 |
| Rubber Factory | Factory | 1× Energy Cell *(opt.)*<br>3× Oil | 3× Rubber | 1× Toxic Waste<br>1× Acid | 4,383,000 |
| Satellite Factory | Factory | 2× Solar Panel<br>2× Processor<br>2× Display<br>1× Energy Container<br>1× Steel Tube | 1× Satellite | 1× Scrap Metal | 68,212,500 |
| Scrap Metal Trader | Factory | — | 60× Scrap Metal | — | 7,750,000 |
| Semi Conductor Manufacturer | Factory | 1× Steel<br>1× Silicon<br>1× Gold<br>1× Energy Cell *(opt.)* | 15× Semi Conductor | — | 4,278,000 |
| Servo Factory | Factory | 4× Steel<br>2× Aluminum<br>2× Conductor<br>1× Plastic | 2× Servo | — | 5,275,500 |
| Sheep Ranch | Ranch | 2× Energy Cell *(opt.)*<br>10× Oxygen<br>18× Wheat<br>12× Water | 15× Sheep<br>1× Bio Gas | 2× Fabric | 4,631,500 |
| Sheep Ranch | Ranch | 1× Energy Cell *(opt.)*<br>10× Corn<br>10× Oxygen<br>20× Water | 15× Sheep<br>1× Bio Gas | 2× Fabric | 4,715,500 |
| Silicon Mine | Mine | — | 4× Silicon | — | 9,500,000 |
| Noble Metal Mine | Mine | — | 1× Silver<br>1× Platinum | — | 6,175,000 |
| Noble Metal Mine | Mine | — | 1× Silver<br>1× Gold | — | 5,650,000 |
| Solar Cell Factory | Factory | 1× Zinc<br>2× Silicon<br>2× Platinum<br>1× Gold<br>1× Energy Cell *(opt.)* | 10× Solar Cell | — | 7,015,000 |
| Solar Panel Factory | Factory | 10× Solar Cell<br>1× Transformator | 1× Solar Panel | — | 9,356,500 |
| Spices Farm | Farm | 1× Energy Cell *(opt.)*<br>35× Water<br>5× Fertilizer | 12× Spices | 1× Oxygen | 5,548,500 |
| Steel Factory | Factory | 8× Ore<br>3× Coal<br>1× Carbon | 8× Steel | — | 4,715,500 |
| Steel Factory | Factory | 12× Scrap Metal<br>4× Coal | 6× Steel | — | 4,467,000 |
| Steel Tube Factory | Factory | 4× Steel<br>2× Aluminum | 3× Steel Tube | — | 4,614,000 |
| Targeting Card Factory | Factory | 1× Microchip<br>1× Copper<br>2× Processor | 2× Targeting Card | — | 26,244,000 |
| Targeting System Factory | Factory | 1× Targeting Card<br>1× Processor<br>3× Energy Cell<br>5× Conductor<br>5× Wire | 1× Targeting System | — | 32,173,000 |
| Tea Farm | Farm | 4× Energy Cell *(opt.)*<br>100× Water | 75× Tea | 4× Oxygen | 4,512,500 |
| Teleporter Factory | Factory | 1× Metal Plate<br>1× Power Unit<br>1× Antigrav Unit<br>2× Plasma Cell<br>1× Conductor<br>1× Transformator | 1× Teleporter | 1× Scrap Metal | 41,861,000 |
| Tools Factory | Factory | 1× Steel<br>1× Platinum<br>1× Silver<br>1× Aluminum<br>1× Energy Cell *(opt.)* | 10× Tools | — | 4,470,500 |
| Transformator Factory | Factory | 2× Steel<br>1× Plastic<br>1× Silicon<br>1× Silver<br>1× Energy Cell *(opt.)* | 10× Transformator | — | 4,421,500 |
| Turbine Factory | Factory | 4× Servo<br>10× Steel<br>3× Coolant<br>2× Power Unit | 1× Turbine | — | 19,240,500 |
| Vegetable Farm | Farm | 4× Energy Cell *(opt.)*<br>40× Water | 35× Vegetable | 4× Oxygen | 2,920,000 |
| Vehicle Factory | Factory | 1× Rubber<br>1× Power Unit<br>1× Energy Generator<br>5× Metal Plate<br>1× Antigrav Unit<br>1× Display | 1× Vehicle | 1× Scrap Metal | 79,584,000 |
| War Robot Factory | Factory | 1× Power Unit<br>1× Processor<br>1× Display<br>5× Nanobot<br>2× Gun<br>1× Teleporter<br>1× Coolant | 1× War Robot | 1× Scrap Metal | 94,683,000 |
| Warhead Factory | Factory | 5× Conductor<br>2× Chemicals<br>3× Metal Plate | 1× Warhead | 1× Scrap Metal | 8,135,000 |
| Ice Mine | Mine | — | 75× Water | — | 7,750,000 |
| Water Collector | Collector | — | 75× Water | — | 7,750,000 |
| Wheat Farm | Farm | 4× Energy Cell *(opt.)*<br>40× Water | 48× Wheat | 4× Oxygen | 2,864,000 |
| Wine Factory | Factory | 50× Fruit<br>10× Fungus | 25× Wine | — | 7,015,000 |
| Wire Manufacturer | Factory | 1× Plastic<br>1× Steel<br>1× Gold | 15× Wire | — | 3,938,500 |
| Wood Farm | Farm | 3× Energy Cell *(opt.)*<br>75× Water | 6× Wood | 3× Oxygen | 4,075,000 |
| Zinc Mine | Mine | — | 10× Zinc | — | 11,250,000 |

## See also

- [Goods](Goods) – the commodities produced and consumed here
- [Trading and Prices](Trading-and-Prices) – how outputs are priced when sold
- [Refining](Refining) – turning ores and scrap into materials
- [Consumer goods](Consumer-goods) – what population stations consume

---
*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods) · [Trade Contracts](Trade-Contracts)*
