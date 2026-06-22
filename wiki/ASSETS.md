# Wiki image assets

A checklist of screenshots and icons the wiki pages want. The pages contain **placeholders** that point to
the filenames below — capture each shot in-game, drop the file into `wiki/images/`, then replace the
placeholder line with the image (`![alt text](images/<name>.png)`).

## How images work on a GitHub wiki

- Image files live in the wiki repo. In this project, keep them under **`wiki/images/`**; when you publish,
  they go alongside the `.md` pages (see the publishing notes in `README.md`).
- Reference an image from a page with standard Markdown: `![Subsystem socket panel](images/system-upgrades-socket-panel.png)`.
- Prefer **PNG** for UI screenshots. Crop tightly to the relevant panel, and grab them at a high enough
  resolution to stay readable when scaled down. A short caption under each helps.

## Finding the placeholders

Each spot in a page is marked with a line like:

```
*[📷 Screenshot needed — ASSETS.md: images/system-upgrades-socket-panel.png]*
```

Search the `pages/` folder for `Screenshot needed` to find them all.

## Checklist

| File (`wiki/images/`) | Page | Where it goes | What to capture |
|---|---|---|---|
| `system-upgrades-socket-panel.png` | System upgrades | "How upgrades work" | The ship's subsystem socket panel with an upgrade's tooltip open, showing the three energy figures and the permanent-install preview. |
| `ship-stats-panel.png` | Ship stats | Intro | The Building Mode ship stats panel on the right, with the configuration cog visible and a spread of stats (mass, velocity, pitch/yaw/roll, processing power) shown. |
| `research-station-ui.png` | Research Station | "How it works / requirements" | The research window: the 3 required + 2 optional input slots and the single result slot, ideally mid-research. |
| `trading-station-menu.png` | Trading and Prices | "The price formula" | A station's trade menu showing a good's buy/sell price, with the supply/demand indicator visible. |
| `galaxy-map-regions.png` | Ship generation | "Distance from the core is the master dial" | The galaxy map zoomed out, showing the bright dense core vs. the sparse rim — to illustrate distance-based scaling. |
| `turret-factory-ui.png` | Turret crafting | "How crafting ingredients work" | The Turret Factory build screen with the ingredient list and the investable sliders for a weapon. |

## Nice-to-have (optional, not yet placeheld)

These would improve pages but don't have placeholders yet — add a placeholder line first if you capture one:

- A **captain badge** close-up (tier wings + level stars) for [Captains](pages/Captains.md).
- A **shield-vs-hull** health bar mid-fight for [Combat](pages/Combat.md).
- A **world boss** health-bar/arena shot for [World bosses](pages/World-bosses.md).
- The **strategy map** with ships under orders for [Ship orders](pages/Ship-orders.md).
- A **damage-type / weapon icon** set for the [Weapons](pages/Weapons.md) tables.
