<!-- Hand-written mechanics page. Sourced from lib/mission.lua, lib/structuredmission.lua,
     lib/missionutility.lua, lib/rewards.lua and the scripts under player/missions/. Reward numbers
     are the base values set in those scripts; in-game they are scaled by the sector reward factor
     (Balancing.GetSectorRewardFactor / Balancing_GetSectorRewardFactor), which rises toward the core. -->
# Missions

**Missions** are the optional jobs you pick up around the galaxy — wiping out pirates, escorting
settlers, hunting bounties, running deliveries. They pay **credits**, **reputation** with the
faction that posted them, and sometimes **materials**, **turrets** or **system upgrades**. This page
covers how missions work and lists the repeatable **side missions**. For the main questline see
**[Story missions](Story-missions)**; for the unscripted things that happen to you in space see
**[Events](Events)**.

> **In short:** missions are repeatable income **and** the reliable way to grind **reputation** with a
> faction. Pay scales as you move toward the **core**, so the same job is worth far more deeper in. Combat
> clear-out jobs are the dependable reputation grind; deliveries and escorts pay credits with less risk.
> Pick missions from the faction whose standing you want to raise.

## Where missions come from

Most side missions are posted on the **bulletin board** of a station — military outposts, factions'
stations and similar. You read the bulletin, accept the job, and it appears in your **Mission** tab.
A few missions instead start on their own (for example an **Urgent Delivery** radioed to your ship,
or a tutorial that triggers from something you just did).

Each accepted mission has:

- a **title** and a short **brief** (shown in the Mission tab list),
- a longer **description** that doubles as a checklist — its bullet points tick off (✓) as you
  complete objectives,
- usually a **target sector**, which the game highlights for you on the galaxy map and with a gold
  **on-screen arrow and target marker** when you are in the sector,
- often a **time limit**. If it runs out before you have met the goal the mission **fails**; if the
  goal is already met it completes.

If you have no mission currently tracked, an accepted mission with auto-tracking turns itself into
your tracked objective automatically.

## Mission outcomes

A mission ends in one of these states, each with its own banner:

| State | Banner | Meaning |
|---|---|---|
| Accomplished | **MISSION ACCOMPLISHED** | Objective met. Rewards are paid. |
| Finished | *(accomplished banner)* | Gracefully closed out (used by multi-step missions). |
| Failed | **MISSION FAILED** | Time ran out or a fail condition was hit. No reward; some missions apply a relations **punishment**. |
| Abandoned | **MISSION ABANDONED** | You dropped it from the Mission tab. Some missions cannot be abandoned. |
| Updated | **MISSION UPDATED** | Not an ending — shown when a multi-step mission advances to its next phase. |

## Rewards

Mission rewards are some mix of the following:

- **Credits** – the headline payout. Base values are listed below, but the game multiplies them by a
  **sector reward factor** that grows as you move toward the **core**, so the same job pays far more
  in the centre of the galaxy than at the rim.
- **Reputation** – relations with the faction that gave you the job (a few thousand points per
  mission). This is how you climb toward a faction's higher reputation tiers.
- **Materials** – some missions add raw materials scaled to where you are: jobs near the core pay
  out in **Avorion/Ogonite/Xanion**, jobs at the rim in **Iron/Titanium**.
- **Items** – the generic "thank-you" reward (used by rescue-type jobs) has about a **50% chance** to
  hand you a **system upgrade** and otherwise an **Exceptional-rarity turret**. If you own the
  *Black Market* or *Into the Rift* DLC, their upgrade pools are included.

## Side missions

These are the repeatable jobs you find around inhabited space. Credits shown are the **base** amount
before the sector reward factor.

| Mission | What you do | Base reward | Time limit |
|---|---|---|---|
| **Wipe out Pirates** | Clear a pirate-infested sector | 50,000 credits · +6,000 rep | — |
| **Wipe out Xsotan** | Clear a Xsotan-infested sector | 50,000 credits · +6,000 rep | — |
| **Bounty Hunt** (*WANTED*) | Track a wanted pirate across several sectors, then report back to a freighter | ~10,000+ credits · +7,000 rep | — |
| **Cover Retreat** | Hold off a pursuing fleet while allies escape | 50,000 credits · +7,500 rep | 30 min |
| **Settler Trek** | Protect a convoy of settlers from pirates | 60,000 credits · +6,000 rep | 60 min |
| **Free Slaves** | Rescue captives from traffickers and bring them home | +12,000 rep | 15 min |
| **Hide Evidence** | Salvage a wreck so nothing can be traced back to the client | 45,000 credits · +6,500 rep (paid by mail) | 30 min |
| **Search and Rescue** | Find and recover a stranded ship/crew | 10,000–60,000 credits · +6,000 rep | — |
| **Explore Sector** | Scout a sector and its objects | 40,000 credits | — |
| **Investigate Missing Freighters** | Pose as a freighter, follow the route, find and destroy the pirate base | variable | — |
| **Transfer Vessel** | Fly a client's ship to a buyer in another sector | varies (rep penalty if you fail) | 25 min |
| **A Lost Friend** | Recover a lost **captain** for a client and return them | ~ captain's salary in credits | — |
| **Urgent Delivery** | Deliver goods of "unknown origin" to a drop point | varies | 60 min |
| **Delivery / Organize Goods** | Fetch or gather requested goods for a station | varies | — |

> Combat-clearing jobs (**Wipe out Pirates/Xsotan**, **Cover Retreat**, **Settler Trek**) are the
> reliable reputation grind: predictable goals, solid rep, and credits that scale toward the core.
> **Free Slaves** pays no credits but the largest single rep boost.

## Tutorial missions

Early on the game feeds you a series of short **tutorial missions** that teach one system each and
then get out of the way. They are ordinary missions under the hood (and can be skipped):

| Tutorial | Teaches |
|---|---|
| **The Rules of the Trade** | Buying low and selling high between stations |
| **R-Mining Job** | Using R-mining (refinery) lasers |
| **Station Founding** | Founding and supplying your first station |
| **Ships, Strategies & Captains** | Strategy-mode map, captains and fleet orders |
| **Commanding Fighters** | Carriers, squadrons and fighter orders |
| **Let's Board!** | Boarding enemy ships to capture them |
| **Torpedo Tests** | Loading and firing torpedoes |
| **Pirate Raid** | Defending against a scripted pirate attack |
| **Emergency Call** | Using the emergency distress beacon |
| **Building Knowledge** | Unlocking the next building material — see **[Building knowledge](Building-knowledge)** |

## See also

- [Story missions](Story-missions) – the main artifact-and-barrier questline
- [Events](Events) – random encounters: distress signals, ambushes, bounty hunters, bosses
- [Building knowledge](Building-knowledge) – unlocking each ship-building material
- [Ship orders](Ship-orders) – the fleet commands you give captained ships

---
*Progression & Missions: [Missions](Missions) · [Story missions](Story-missions) · [Events](Events) · [Encyclopedia](Encyclopedia)*
