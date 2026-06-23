<!-- Hand-written page. Sourced from the scripts under player/events/ (alienattack.lua,
     convoidistresssignal.lua, fakedistresssignal.lua, headhunter.lua, the spawn*.lua boss spawners,
     eventscheduler.lua, sectoreventstarter.lua) and lib/rewards.lua for the rescue payout. -->
# Events

**Events** are the things that happen *to* you in space without being a job you accepted: a distress
call on the radio, a pirate ambush, a roaming boss, or — if your reputation is bad enough — bounty
hunters coming for your head. They are scheduled by the game as you travel and play out in the sector
you're in. For accepted jobs see **[Missions](Missions)**; for the scripted main story see
**[Story missions](Story-missions)**.

## How events are scheduled

An **event scheduler** runs while you play and periodically rolls whether to start an event, and which
one, based on where you are and what's going on. Some events are **player-bound** (they follow you and
spawn things around your ship), others are **sector-related** (tied to the sector — passing traders,
local attacks). Missions can ask the scheduler to **suppress** player-bound or local events in their
target sector so a quest isn't interrupted, but sector-related events can still occur.

## Distress signals

You'll pick up **Mayday** calls naming a sector and a victim under pirate attack. Answering one takes
you to that sector — but the call may be genuine or a setup:

| Event | What it is |
|---|---|
| **Convoy Distress Signal** | A real convoy being attacked by pirates. Drive the pirates off and the survivors reward you (the standard rescue payout: credits, reputation, and a likely **system upgrade** or **Exceptional turret**). |
| **Fake Distress Signal** | A **trap**. The "victim" — sometimes a "rich trader" begging for help and promising a reward — is bait, and the sector is an ambush. Show up unprepared and the pirates spring on you. |

Because a genuine and a fake distress call sound almost identical, answering one is always a small
gamble — go in ready for a fight.

## Attacks and ambushes

| Event | What it is |
|---|---|
| **Alien (Xsotan) Attack** | Xsotan jump into your sector and attack. Won't fire if the sector already has Xsotan in it or if attack events are disabled there. The deeper toward the core, the more dangerous these get. |
| **Pirate Raid** | Pirates jump in to attack you or a sector. (The early-game version is also used as a tutorial — see [Missions](Missions).) |
| **Headhunters** | If a faction has turned on you, professional **bounty hunters** hunt you down (see below). |

### Headhunters

When you've made an enemy, **headhunters** come looking. They are triggered by sustained hostility:
you've been **at war** with a faction or your relations with them have dropped very low
(roughly **−80,000** or worse), and you've been in combat long enough (on the order of **~45 minutes**
of fighting). A hunting faction then sends **Bounty Hunter** ships after you. Make peace — or wipe out
the hunters — and the heat eventually clears (their faction relations toward you can reset to neutral).

The practical takeaway: grinding a faction's reputation deep into the negative, or declaring war, has a
cost — they will pay others to kill you.

## Roaming bosses

The galaxy seeds a number of **unique bosses** that you can stumble into (and that the story spawns).
They are tougher than normal sector enemies and drop better loot:

- **The Big AI** (and a corrupted variant) — a powerful AI ship.
- **Asteroid / Laser / Jumper / Shield bosses** — distinctive boss ships, several built around a
  gimmick (e.g. asteroids that feed a boss's shield or laser, which you must deal with to hurt it).
- **The Guardian** — the Xsotan boss at the galactic centre, the story's final fight (see
  [Story missions](Story-missions)).
- **Travelling Merchant** — not a fight: a roaming trader that shows up to buy and sell.
- **The Behemoth** — a galaxy-wide event distinct from the above: it roams between compass quadrants
  looking for an empty AI sector to wreck, giving players a limited window to fight it first. See
  [World and Sector Generation → Background systems](World-and-Sector-Generation#background-systems-that-keep-the-galaxy-alive).

> Some boss fights have a **mechanic** rather than being a pure slugfest — for example shooting the
> special **asteroids** that power a boss's shield or weapon before you can damage the boss itself.

## See also

- [Missions](Missions) – the jobs you accept, and the rescue/clear payouts events reuse
- [Story missions](Story-missions) – the scripted questline and its bosses
- [Combat](Combat) – damage types and how to actually win these fights

---
*Progression & Missions: [Missions](Missions) · [Story missions](Story-missions) · [Events](Events) · [Encyclopedia](Encyclopedia)*
