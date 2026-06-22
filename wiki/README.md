# Avorion Wiki

Player-facing wiki pages for Avorion, written in **GitHub Flavored Markdown** for use as a **GitHub wiki**.
Pages are derived from the game's own scripts so the numbers stay accurate.

## Layout

```
wiki/
├── pages/        GitHub-wiki Markdown pages (.md)
├── extraction/   Line-accurate technical facts extracted from the game code
├── tools/        Python generators that build the data-heavy pages from source
├── ASSETS.md     Screenshot/icon checklist: what to capture and where each goes
└── images/       Image files referenced by pages as ![alt](images/<name>.png)
```

### pages/

| File | Page | Covers |
|---|---|---|
| `Home.md` | Home | Wiki landing page / index, learning path |
| `Getting-Started.md` | Getting Started | New-player on-ramp: the whole progression in one page, linking every topic |
| `_Sidebar.md` | (sidebar) | Navigation shown on every wiki page |
| `Trading-and-Prices.md` | Trading and Prices | Price formula, supply/demand, relations, tax, stock, NPC traders |
| `Goods.md` | Goods | Full commodity catalog, raw resources, contraband |
| `Production.md` | Production | Every factory recipe and build/upgrade cost formulas |
| `Refining.md` | Refining | Materials, ore/scrap → material mappings, the refine fee |
| `Consumer-goods.md` | Consumer goods | What each station type consumes; population profit; reverse lookup |
| `Player-stations.md` | Player stations | Founding, trade settings, tax, stock, policies, offline simulation |
| `Trade-Contracts.md` | Trade Contracts | Automated trade routes flown by a Merchant captain |
| `Combat.md` | Combat | Damage types, shields vs hull, rarity/tech scaling |
| `Weapons.md` | Weapons | Turret weapon types: damage type, fire rate, range, behaviour |
| `Turret-crafting.md` | Turret crafting | Per-weapon Turret Factory ingredients and the stat each raises |
| `Torpedoes.md` | Torpedoes | Torpedo bodies, warheads, damage profiles |
| `Defensive-systems.md` | Defensive systems | Shield boosters, resistances, weaknesses, point defense |
| `Missions.md` | Missions | How missions work, the side-mission catalog, rewards, tutorials |
| `Story-missions.md` | Story missions | The main artifact/barrier questline and its boss steps |
| `Events.md` | Events | Distress signals, ambushes, headhunters, roaming bosses, scheduling |
| `Building-knowledge.md` | Building knowledge | Material unlock tiers, prices, sockets, how to acquire each |
| `Ship-stats.md` | Ship stats | The Building Mode stat panel: what Mass, Pitch/Yaw/Roll, P.P. etc. mean and how each is improved |
| `Ship-orders.md` | Ship orders | The fleet order types you assign to ships |
| `Captains.md` | Captains | Captain tiers, levels, salary formula, ambush risk |
| `Captain-classes.md` | Captain classes | The nine class specializations and their ship bonuses |
| `Captain-perks.md` | Captain perks | All 21 perks, their effects, and opposing pairs |
| `Fleet-commands.md` | Fleet commands | The background captain commands: mine, trade, scout, expedition, etc. |
| `Encyclopedia.md` | Encyclopedia | The in-game help book: how to open it and its full table of contents |

GitHub turns a filename like `Player-stations.md` into the page title **"Player stations"**, and links such as
`[Player stations](Player-stations)` resolve to it. `Home.md` and `_Sidebar.md` are GitHub-wiki special pages.

The table above is a partial index; the `pages/` folder holds more pages (captains, enemies, ship/​system
generation, items, diplomacy, the mod pages, …). `Home.md` and `_Sidebar.md` are the authoritative, complete
index — every page is listed in both, grouped by section.

## Writing style (important)

These pages teach **players how the game works**, not how the code works. Two rules keep them that way:

1. **No code identifiers in reader-facing text.** Lua file names, function names, class/variable names and
   `~line` citations belong **only** in the `<!-- ... -->` source comment at the very top of each page (which
   is invisible when rendered on the wiki). In the body, use the in-game term instead — e.g. write
   "Military Turret Control System", not `militarytcs.lua`; "+4 armed turret slots", not
   `addMultiplyableBias(ArmedTurrets, 4)`. Keep the **data tables and the numbers** — players want those —
   just strip the code framing around them, and lead dense formulas with a plain-language takeaway.
2. **Open with a quick reference.** Most pages start with a `> **In short:** …` blockquote (or a lead "At a
   glance" table) giving the 30-second version before the detail. Add concise, practical tips ("best starter
   X", "use this against Y") grounded in the page's own numbers.

When adding a page, also register it in **both** `Home.md` and `_Sidebar.md`, give it a "See also" list and
the italic footer nav line for its section, and add any screenshots to `ASSETS.md` (see below).

## Publishing to a GitHub wiki

A GitHub wiki is its own git repository at `https://github.com/<user>/<repo>.wiki.git`. To publish, copy the
contents of `pages/` into a clone of that wiki repo (the `.md` files live at its top level), commit and push.
You can also paste a page's Markdown into the wiki web editor.

## Regenerating the data pages

`Goods`, `Production`, `Refining` and `Consumer-goods` are **generated** from the game source – do not hand-edit
their data rows. To rebuild after a game update:

```sh
# run from the repository root
python wiki/tools/_gen_goods.py
python wiki/tools/_gen_production.py
python wiki/tools/_gen_refining.py
python wiki/tools/_gen_consumergoods.py
```

The mechanics-prose pages — `Trading-and-Prices.md`, `Player-stations.md`, `Trade-Contracts.md`,
`Combat.md`, `Weapons.md`, `Turret-crafting.md`, `Torpedoes.md`, `Defensive-systems.md`, `Missions.md`,
`Story-missions.md`, `Events.md`, `Building-knowledge.md`, `Ship-orders.md`, `Captains.md`,
`Captain-classes.md`, `Captain-perks.md`, `Fleet-commands.md` and `Encyclopedia.md` —
are written by hand from the game scripts and have no generator.

## Dependency on the game files

The generators read the unpacked game scripts from `Avorion/data/scripts/...`. That `Avorion/` folder holds the
game's own files and is **git-ignored**, so it is not part of this repository. To regenerate the pages you must
have the Avorion game files unpacked into `Avorion/` at the repo root. The finished pages in `pages/` and the
facts in `extraction/` are committed, so they are usable without the game files – only regeneration needs them.

## Notes

- Math uses GitHub's `$...$` / `$$...$$` syntax (rendered with MathJax on GitHub).
- Individual goods are shown as plain text, not links, because there is one combined `Goods` catalog page rather
  than a page per commodity.
- GitHub wikis cannot sort tables (no client-side scripting), so the large catalog tables render as static
  tables.
