<!-- Hand-written mechanics page. Code lineage (kept out of the reader-facing text on purpose):
     Stat list & labels: Common/Game/CraftStatsOverview.cpp (mirrored in data/localization/template.pot
       ~lines 2490-2770) and the BlockStatistics API (Avorion/Documentation/BlockStatistics.html:
       mass, pitch, yaw, roll, thrust, gyroPower, inertiaDampening, momentOfInertia, centerOfMass,
       processingPower, durability, shield, energyYield, storableEnergy, cargoHold, hangarSpace,
       productionCapacity, radarRadius, hyperspacePower, volume, width/height/length).
     Block -> stat effects & placement rules: Common/Game/Blocks/Blocks.cpp strings
       (template.pot ~1517-1922): Engine "Increases acceleration and maximum velocity (diminishing
       returns)" / "Engines can only point backwards"; Thrusters "most leverage when built far at the
       outer edge" / "reduce drift"; Directional vs omni thruster trade-off (~1541, 1545); Gyro Array
       "Strength increases with better materials" / "same effect no matter where you place them";
       Inertia Dampener "create artificial subspace friction and help brake"; Integrity Field Generator
       "25% damage ... center to protect it"; Functional Hull "Contributes towards processing power";
       Armor "stop piercing projectiles, like railgun projectiles".
     Processing power / functional blocks / building knowledge cap:
       data/scripts/player/ui/encyclopedia/chapters/building.lua, items/buildingknowledge.lua.
     Low-brake warning text: template.pot ~23606. Inertia Dampeners are Iron-only: template.pot ~66278.
     Image assets: see wiki/ASSETS.md. -->
# Ship stats

Every block you place changes how your ship performs. The **ship stats** panel — shown on the right
while you're in **Building Mode** — is the running scoreboard for those changes: how fast you turn,
how hard you hit, how much you can carry, and whether your crew can even run the thing. This page
explains what each stat means and, more importantly, **how to improve it**.

> **In short:** stats come from **blocks**. Improve any stat by (1) adding or enlarging the right
> **functional block**, (2) building it from a **better material**, (3) **placing** it well, (4)
> slotting **[system upgrades](System-upgrades)**, and (5) keeping the **crew** that runs it staffed.
> Almost every movement stat is really a tug-of-war against one number: **Mass**.

*[📷 Screenshot needed — ASSETS.md: images/ship-stats-panel.png]*

You don't have to memorize the whole list. Click the **cog** beneath the panel to choose which stats
are shown, so you only watch the ones that matter for the ship you're building.

## Movement & handling

This is where most new players get stuck — a ship that won't turn or won't stop. All of it comes
back to **Mass** versus the blocks that push and turn you.

### Mass

**Mass** is the total weight of every block on the ship, and it's the denominator for *all* movement:
acceleration, top speed, braking, and turning all get worse as Mass climbs. Two levers bring it down:

- **Material.** Heavier-tier hull weighs more per cubic metre; lighter blocks (and structural/hollow
  blocks like Framework) weigh far less. Armor is the heaviest thing on most ships — use it where it
  earns its weight, not everywhere.
- **Don't over-build.** Empty volume you don't need is just mass you have to drag around.

### Velocity & Acceleration

- **Acceleration** — how quickly you reach speed.
- **Max Velocity** — your top forward speed.

Both come from **Engines**. Two rules matter: **engines can only point backwards** (they push you
forward, so they belong at the stern), and they have **diminishing returns** — doubling your engine
mass does *not* double your speed. Past a point you gain more by cutting Mass than by bolting on more
engine.

### Braking & drift

- **Braking thrust / Deceleration** — how fast you can stop.
- **Drift** — the sideways skid you feel when a heavy ship "swims" through a turn.

Both are handled by **Thrusters** and **Inertia Dampeners**. Inertia Dampeners create artificial
subspace friction to slow you down and pull you back onto your heading. If the game warns that your
**brake thrust is low**, you have three fixes: add Thrusters, add Inertia Dampeners, or build the
ship out of a **lighter material**. (Inertia Dampeners can only be built from **Iron** — see
[Building knowledge](Building-knowledge).)

### Turning: Yaw, Pitch & Roll

These three stats are your rotational speeds — how fast the ship spins on each axis:

| Stat | Axis | What it does |
|---|---|---|
| **Yaw (Left/Right)** | vertical axis | Turns the nose left and right |
| **Pitch (Up/Down)** | side-to-side axis | Tips the nose up and down |
| **Roll** | front-to-back axis | Banks the ship like a barrel roll |

Turning is driven by two block types, and they behave differently:

- **Gyro Arrays** turn the ship on every axis. Their strength **scales with the material** they're
  built from, and they have the **same effect no matter where you place them** — so put them
  anywhere convenient and protect them deep inside the hull.
- **Thrusters** also rotate the ship, but they work by **leverage**: the **farther from the centre of
  mass** you build them, the more turning force they give. Long ships turn best with thrusters out at
  the **nose, tail, and wingtips**.

The intuition behind the numbers: a long, heavy ship resists rotation (high *moment of inertia*), so
it needs more turning power for the same agility. Compact ships, or thrusters placed far out on the
extremities, turn much more sharply.

### Strafing

**Strafing** is sideways/vertical movement without turning, and it also comes from Thrusters. There
are two kinds, and it's a trade-off:

- **Directional Thrusters** push in two directions only and must be placed carefully, but they're
  **stronger** per block.
- **Omni-directional Thrusters** push every direction at once (full strafing) but are **weaker** in
  any single direction.

Both are **fragile** — keep them off your outer skin if you expect to take fire.

### Placement cheat-sheet

| Block | Best placement |
|---|---|
| **Engines** | At the **stern**, facing backward (they only push forward) |
| **Thrusters** | Far from the centre of mass — **nose, tail, wingtips** — for maximum turning leverage |
| **Gyro Arrays** | **Anywhere** (placement doesn't matter); build them from the best material you can |
| **Inertia Dampeners** | Anywhere; add them when braking or drift is poor |

## Power

A ship that runs out of energy stops moving and shooting, so the power budget is as real as the
weapons budget.

- **Generated Energy** — produced by **Generators**. This is your income.
- **Storable Energy** — your battery, raised by **Energy Containers**. This buffers spikes (boosting,
  firing) and is what shields and hyperspace draw down.
- **Required Energy** — the constant drain from shields, integrity fields, and installed
  **[system upgrades](System-upgrades)**.

If draw exceeds generation, your battery empties and systems shut off. Build more Generators (and a
bigger battery for bursty loads), or cut energy-hungry systems.

## Defense

- **Hull** — your raw hit points. *Every* block adds some, but **Armor** adds a lot and also takes
  reduced collision damage and **stops piercing projectiles** (like railgun shots) from punching
  deeper. See [Combat](Combat).
- **Shield** — a regenerating bubble around the whole ship from a **Shield Generator**. The
  **higher the material** it's built from, the stronger the shield. See [Defensive systems](Defensive-systems).
- **Durability / Integrity Field** — an **Integrity Field Generator** wraps nearby blocks so they
  take only **25% damage** and don't break off as easily. Build it **deep in the centre** so it's the
  last thing to die.

## Processing Power (P.P.)

**P.P.** stands for **Processing Power**, and it's the stat that decides how many
**[system upgrades](System-upgrades)** your ship can slot — each point of headroom unlocks
**subsystem sockets**.

- **Functional blocks** add Processing Power. Engines, thrusters, generators, computer cores,
  functional hull and the like all count; plain hull, armor, and purely decorative blocks don't. The
  Building Mode highlights exactly which of your blocks are functional.
- Once you hit your ship's **maximum** Processing Power you can keep building — just with
  **non-functional** blocks (armor, hull, decoration) that don't raise it further.
- That maximum is a **per-ship cap** set by your **[Building knowledge](Building-knowledge)** tier.
  Unlock higher-tier knowledge to raise the cap and fit more subsystems.

## Capacity & function

| Stat | Comes from | Notes |
|---|---|---|
| **Cargo Hold** | Cargo blocks | Required to carry trade goods and ore |
| **Hangar Space** | Hangars | Houses fighters; the stat shows a size range because fighters vary in size |
| **Crew Quarters** | Crew Quarters blocks | How many crew you can house |
| **Torpedo storage** | Torpedo Tubes & Storage | Tubes launch torpedoes; storage holds spares |
| **Production Capacity** | Assembly blocks | Speeds up factory and fighter production |
| **Turret slots / Fire Power** | Turret bases + subsystems | How many turrets you can mount and your total damage output |

## Crew requirements

Blocks don't run themselves. The panel lists how many of each crew role your ship **requires** versus
how many you actually have:

- **Gunners** — fire turrets.
- **Pilots** — fly the ship and improve handling.
- **Engineers** — keep the technical (functional) blocks running.
- **Mechanics** — repair and maintain.
- **Miners** — work mining systems.

Understaffing a role degrades the things that role runs, and crew draw a **Crew Pay** salary each
cycle. See [Captains](Captains) for crew staffing and morale.

## Size & navigation

- **Volume** and **W × H × L** — the ship's bulk and bounding dimensions. Bigger isn't free: it
  usually means more Mass and a wider target.
- **Radar Reach** — how far you detect objects in a sector.
- **Hyperspace Reach** — your jump range between sectors; **Hyperspace Cooldown** and **Jump Energy**
  are the recharge time and battery cost of a jump. All three are improved with the right
  [system upgrades](System-upgrades).

## How to improve any stat

When a number is too low, work down this list in order — the early levers are usually the cheapest:

1. **Add or enlarge the right functional block.** Slow? More engines. Won't turn? More gyros or
   edge-mounted thrusters. Out of power? More generators.
2. **Upgrade the material.** Better materials are lighter *and* stronger, and some blocks (gyros,
   shields) scale their strength directly with material tier.
3. **Place it well.** Engines at the stern, thrusters far from centre, integrity fields and fragile
   blocks deep inside.
4. **Cut Mass.** Every kilogram you remove improves acceleration, speed, braking, and turning at once.
5. **Slot [system upgrades](System-upgrades).** Subsystems boost velocity, energy, jump range, radar,
   cargo, and turret slots beyond what blocks alone provide.
6. **Staff the crew.** A perfectly built block still underperforms if no one is running it.

## See also

- [Building knowledge](Building-knowledge) — materials, the Processing Power cap, and subsystem sockets
- [System upgrades](System-upgrades) — the modules that push stats past what blocks give
- [Combat](Combat) and [Defensive systems](Defensive-systems) — how Hull, Shield and Fire Power play out in a fight
- [Captains](Captains) — crew roles, morale and pay
