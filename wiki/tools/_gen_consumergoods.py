import re

src = open("Avorion/data/scripts/lib/consumergoods.lua", "r", encoding="utf-8").read()

station_goods = []
for m in re.finditer(r'function\s+ConsumerGoods\.(\w+)\s*\((.*?)\)(.*?)\n\s*end', src, re.S):
    key = m.group(1)
    body = m.group(3)
    names = re.findall(r'"([^"]+)"', body)
    seen = set()
    uniq = []
    for n in names:
        if n not in seen:
            seen.add(n)
            uniq.append(n)
    station_goods.append((key, uniq))


def display(key):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', key)


POP_STATIONS = {"Habitat", "Biotope", "Casino"}
TURRET = "TurretFactory"

rev = {}
for key, names in station_goods:
    for n in names:
        rev.setdefault(n, set()).add(display(key))

L = []
W = L.append
W("<!-- Generated from data/scripts/lib/consumergoods.lua via wiki/tools/_gen_consumergoods.py. Do not hand-edit. -->")
W("# Consumer goods")
W("")
W("**Consumer goods** are [goods](Goods) that certain stations **consume** rather than resell. Population and")
W("service stations – habitats, casinos, shipyards, military outposts and the like – constantly use up specific")
W("goods, creating steady **demand** that raises local prices and gives traders a reliable place to sell.")
W("Player-owned consumer stations turn this into passive income. For how that demand affects prices, see")
W("**[Trading and Prices](Trading-and-Prices)**.")
W("")
W("> **In short:** some station types (habitats, casinos, biotopes…) **use up** goods instead of reselling")
W("> them. Own one, keep it **stocked** with what it consumes, and its population pays you a **~10% markup**")
W("> every couple of minutes — steady passive income on top of normal trade. The tables below show which")
W("> goods each station type wants.")
W("")
W("## How consumption works")
W("")
W("A consuming station buys its listed goods from passing traders and from you. Each consumer adds **demand**")
W("for those goods to the surrounding region (within roughly half the economic influence radius), pushing their")
W("local price up – the opposite of a factory that floods an area with supply. See")
W("[supply and demand](Trading-and-Prices#supply-and-demand) for the underlying math.")
W("")
W("## Population profit")
W("")
W("When you **own** a station that buys goods (such as a habitat, casino or biotope), its population")
W("periodically consumes some of the stocked goods and pays you for them at a markup. Roughly every **2")
W("minutes**, a batch of **10–60 units** of one stocked good is consumed and the population pays **110%** of the")
W("station's buy price for it – a steady **10% profit margin** on goods the station has on hand. Keeping a")
W("consumer station well stocked therefore generates passive income on top of normal trade.")
W("")
W("## Goods consumed by station type")
W("")
W("The table below lists what each station type consumes. The classic **population stations** you can build for")
W("profit – **Habitat**, **Biotope** and **Casino** – are marked.")
W("")
W("| Station type | Population station? | Consumed goods |")
W("|---|:--:|---|")
for key, names in station_goods:
    if key == TURRET:
        continue
    pop = "Yes" if key in POP_STATIONS else "—"
    W("| **%s** | %s | %s |" % (display(key), pop, ", ".join(names)))
W("")
turret = next((names for key, names in station_goods if key == TURRET), [])
W("### Turret Factory")
W("")
W("A **Turret Factory** is a special case: instead of a fixed list, each one randomly selects up to **15")
W("distinct goods** from the weighted pool below when it is generated, so no two turret factories demand exactly")
W("the same goods.")
W("")
W("*Pool:* " + ", ".join(sorted(turret)) + ".")
W("")
W("## Goods reference")
W("")
W("Reverse lookup – which station types consume each good. Useful for finding a buyer for surplus cargo.")
W("")
W("| Good | Consumed by |")
W("|---|---|")
for good in sorted(rev):
    W("| %s | %s |" % (good, ", ".join(sorted(rev[good]))))
W("")
W("## See also")
W("")
W("- [Goods](Goods) – the full commodity catalog")
W("- [Trading and Prices](Trading-and-Prices) – how consumer demand affects prices")
W("- [Production](Production) – factories that produce these goods")
W("- [Player stations](Player-stations) – building and operating your own stations")
W("")
W("---")
W("*Economy & Trading: [Goods](Goods) · [Trading and Prices](Trading-and-Prices) · [Production](Production) · [Refining](Refining) · [Player stations](Player-stations) · [Consumer goods](Consumer-goods)*")

open("wiki/pages/Consumer-goods.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote wiki/pages/Consumer-goods.md | station types=%d unique goods=%d" % (len(station_goods), len(rev)))
