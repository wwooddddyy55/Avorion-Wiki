# Avorion Wiki

This repository contains a community-style wiki for the game [Avorion](https://store.steampowered.com/app/445220/Avorion/), covering topics like combat, weapons, trading, fleets, captains, missions, and more. The pages live under [`wiki/pages`](wiki/pages).

## About this project

This wiki was created as an experiment to test the capabilities of **Claude Code**, Anthropic's CLI-based AI coding assistant. The goal was to see how well an AI agent could research game mechanics, extract and organize data from game files, and produce structured, readable documentation with minimal manual writing.

**This is not an official or authoritative source.** Content was generated with AI assistance and may contain inaccuracies, outdated information, or misinterpretations of game data. Always cross-check important details against the official game, the [official Avorion wiki](https://avorion.fandom.com/), or in-game testing.

## How it was made

- **Claude Code** was used as the primary tool to explore Avorion's game files, extract structured data, and write the wiki pages found in `wiki/pages`.
- Some data extraction was scripted — see [`wiki/tools`](wiki/tools) for Python generator scripts used to pull information like goods, production chains, and refining data directly from game files.
- Raw extraction notes are kept in [`wiki/extraction`](wiki/extraction) for reference/traceability back to source data.
- Pages were written iteratively, one topic area at a time (see the commit history for the order topics were added).

## Repository structure

```
wiki/
├── pages/        # The actual wiki content (Markdown pages)
├── tools/        # Scripts used to generate/extract data from game files
└── extraction/   # Raw notes/output from data extraction passes
```

## Purpose

This project exists primarily as a demonstration and testing ground for AI-assisted documentation workflows — exploring how far a coding agent can go when applied to research and content-generation tasks outside of traditional software engineering.
