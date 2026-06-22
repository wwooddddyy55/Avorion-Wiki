<!-- Generated from data/scripts/lib/consumergoods.lua via wiki/tools/_gen_consumergoods.py. Do not hand-edit. -->
# Consumer goods

**Consumer goods** are [goods](Goods) that certain stations **consume** rather than resell. Population and
service stations – habitats, casinos, shipyards, military outposts and the like – constantly use up specific
goods, creating steady **demand** that raises local prices and gives traders a reliable place to sell.
Player-owned consumer stations turn this into passive income. For how that demand affects prices, see
**[Trading and Prices](Trading-and-Prices)**.

> **In short:** some station types (habitats, casinos, biotopes…) **use up** goods instead of reselling
> them. Own one, keep it **stocked** with what it consumes, and its population pays you a **~10% markup**
> every couple of minutes — steady passive income on top of normal trade. The tables below show which
> goods each station type wants.

## How consumption works

A consuming station buys its listed goods from passing traders and from you. Each consumer adds **demand**
for those goods to the surrounding region (within roughly half the economic influence radius), pushing their
local price up – the opposite of a factory that floods an area with supply. See
[supply and demand](Trading-and-Prices#supply-and-demand) for the underlying math.

## Population profit

When you **own** a station that buys goods (such as a habitat, casino or biotope), its population
periodically consumes some of the stocked goods and pays you for them at a markup. Roughly every **2
minutes**, a batch of **10–60 units** of one stocked good is consumed and the population pays **110%** of the
station's buy price for it – a steady **10% profit margin** on goods the station has on hand. Keeping a
consumer station well stocked therefore generates passive income on top of normal trade.

## Goods consumed by station type

The table below lists what each station type consumes. The classic **population stations** you can build for
profit – **Habitat**, **Biotope** and **Casino** – are marked.

| Station type | Population station? | Consumed goods |
|---|:--:|---|
| **Habitat** | Yes | Beer, Wine, Liquor, Food, Tea, Leather, Spices, Gem, Fruit, Cocoa, Coffee, Wood, Meat, Water, Fish, Book |
| **Biotope** | Yes | Food, Food Bar, Fungus, Wood, Glass, Sheep, Cattle, Wheat, Corn, Rice, Vegetable, Water, Coal, Plant, Fish |
| **Casino** | Yes | Beer, Wine, Liquor, Food, Luxury Food, Water, Gem, Medical Supplies |
| **Equipment Dock** | — | Fuel, Rocket, Tools, Laser Compressor, Laser Head, Fusion Core, Warhead, Satellite, Drone, Antigrav Generator, Ammunition, Ammunition S, Ammunition M, Ammunition L |
| **Shipyard** | — | Energy Tube, Aluminum, Display, Metal Plate, Fusion Core, Computation Mainframe, Medical Supplies, Industrial Tesla Coil, Antigrav Generator, Turbine, Energy Container |
| **Repair Dock** | — | Fuel, Steel, Wire, Metal Plate, Nanobot, Solar Cell, Solar Panel, Oxygen, Force Generator, Medical Supplies |
| **Military Outpost** | — | War Robot, Body Armor, Vehicle, Gun, Ammunition, Ammunition S, Ammunition M, Ammunition L, Medical Supplies, Explosive Charge, Electromagnetic Charge, Food Bar, Targeting System, Military Tesla Coil |
| **Research Station** | — | Turbine, High Capacity Lens, Neutron Accelerator, Electron Accelerator, Proton Accelerator, Fusion Generator, Antigrav Generator, Force Generator, Teleporter, Drill, Satellite |
| **Rift Research Station** | — | Rift Research Data, Turbine, High Capacity Lens, Neutron Accelerator, Electron Accelerator, Proton Accelerator, Fusion Generator, Antigrav Generator, Force Generator, Teleporter, Drill, Satellite |
| **Travel Hub** | — | Turbine, Neutron Accelerator, Electron Accelerator, Proton Accelerator, Fusion Generator, Force Generator, Plasma Cell, Energy Cell, Fusion Core |
| **Mine** | — | Mining Robot, Medical Supplies, Antigrav Unit, Fusion Generator, Acid, Solvent, Drill |

### Turret Factory

A **Turret Factory** is a special case: instead of a fixed list, each one randomly selects up to **15
distinct goods** from the weighted pool below when it is generated, so no two turret factories demand exactly
the same goods.

*Pool:* Aluminum, Ammunition M, Ammunition S, Conductor, Copper, Crystal, Electro Magnet, Electromagnetic Charge, Energy Cell, Energy Container, Energy Inverter, Energy Tube, Explosive Charge, Force Generator, Fuel, Gauss Rail, Gold, High Capacity Lens, High Pressure Tube, Industrial Tesla Coil, Laser Compressor, Laser Head, Laser Modulator, Lead, Military Tesla Coil, Nanobot, Plasma Cell, Rocket, Servo, Steel, Steel Tube, Targeting Card, Transformator, Warhead, Wire, Zinc.

## Goods reference

Reverse lookup – which station types consume each good. Useful for finding a buyer for surplus cargo.

| Good | Consumed by |
|---|---|
| Acid | Mine |
| Aluminum | Shipyard, Turret Factory |
| Ammunition | Equipment Dock, Military Outpost |
| Ammunition L | Equipment Dock, Military Outpost |
| Ammunition M | Equipment Dock, Military Outpost, Turret Factory |
| Ammunition S | Equipment Dock, Military Outpost, Turret Factory |
| Antigrav Generator | Equipment Dock, Research Station, Rift Research Station, Shipyard |
| Antigrav Unit | Mine |
| Beer | Casino, Habitat |
| Body Armor | Military Outpost |
| Book | Habitat |
| Cattle | Biotope |
| Coal | Biotope |
| Cocoa | Habitat |
| Coffee | Habitat |
| Computation Mainframe | Shipyard |
| Conductor | Turret Factory |
| Copper | Turret Factory |
| Corn | Biotope |
| Crystal | Turret Factory |
| Display | Shipyard |
| Drill | Mine, Research Station, Rift Research Station |
| Drone | Equipment Dock |
| Electro Magnet | Turret Factory |
| Electromagnetic Charge | Military Outpost, Turret Factory |
| Electron Accelerator | Research Station, Rift Research Station, Travel Hub |
| Energy Cell | Travel Hub, Turret Factory |
| Energy Container | Shipyard, Turret Factory |
| Energy Inverter | Turret Factory |
| Energy Tube | Shipyard, Turret Factory |
| Explosive Charge | Military Outpost, Turret Factory |
| Fish | Biotope, Habitat |
| Food | Biotope, Casino, Habitat |
| Food Bar | Biotope, Military Outpost |
| Force Generator | Repair Dock, Research Station, Rift Research Station, Travel Hub, Turret Factory |
| Fruit | Habitat |
| Fuel | Equipment Dock, Repair Dock, Turret Factory |
| Fungus | Biotope |
| Fusion Core | Equipment Dock, Shipyard, Travel Hub |
| Fusion Generator | Mine, Research Station, Rift Research Station, Travel Hub |
| Gauss Rail | Turret Factory |
| Gem | Casino, Habitat |
| Glass | Biotope |
| Gold | Turret Factory |
| Gun | Military Outpost |
| High Capacity Lens | Research Station, Rift Research Station, Turret Factory |
| High Pressure Tube | Turret Factory |
| Industrial Tesla Coil | Shipyard, Turret Factory |
| Laser Compressor | Equipment Dock, Turret Factory |
| Laser Head | Equipment Dock, Turret Factory |
| Laser Modulator | Turret Factory |
| Lead | Turret Factory |
| Leather | Habitat |
| Liquor | Casino, Habitat |
| Luxury Food | Casino |
| Meat | Habitat |
| Medical Supplies | Casino, Military Outpost, Mine, Repair Dock, Shipyard |
| Metal Plate | Repair Dock, Shipyard |
| Military Tesla Coil | Military Outpost, Turret Factory |
| Mining Robot | Mine |
| Nanobot | Repair Dock, Turret Factory |
| Neutron Accelerator | Research Station, Rift Research Station, Travel Hub |
| Oxygen | Repair Dock |
| Plant | Biotope |
| Plasma Cell | Travel Hub, Turret Factory |
| Proton Accelerator | Research Station, Rift Research Station, Travel Hub |
| Rice | Biotope |
| Rift Research Data | Rift Research Station |
| Rocket | Equipment Dock, Turret Factory |
| Satellite | Equipment Dock, Research Station, Rift Research Station |
| Servo | Turret Factory |
| Sheep | Biotope |
| Solar Cell | Repair Dock |
| Solar Panel | Repair Dock |
| Solvent | Mine |
| Spices | Habitat |
| Steel | Repair Dock, Turret Factory |
| Steel Tube | Turret Factory |
| Targeting Card | Turret Factory |
| Targeting System | Military Outpost |
| Tea | Habitat |
| Teleporter | Research Station, Rift Research Station |
| Tools | Equipment Dock |
| Transformator | Turret Factory |
| Turbine | Research Station, Rift Research Station, Shipyard, Travel Hub |
| Vegetable | Biotope |
| Vehicle | Military Outpost |
| War Robot | Military Outpost |
| Warhead | Equipment Dock, Turret Factory |
| Water | Biotope, Casino, Habitat |
| Wheat | Biotope |
| Wine | Casino, Habitat |
| Wire | Repair Dock, Turret Factory |
| Wood | Biotope, Habitat |
| Zinc | Turret Factory |

## See also

- [Goods](Goods) – the full commodity catalog
- [Trading and Prices](Trading-and-Prices) – how consumer demand affects prices
- [Production](Production) – factories that produce these goods
- [Player stations](Player-stations) – building and operating your own stations

---
*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods)*
