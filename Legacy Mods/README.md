# Legacy Mods

This directory contains placeholder snapshots of early community Space Haven mods originally created during the alpha/early-access era (2019–2021). They are imported here so they can be reviewed, cleaned up, and modernized for the **Space Haven 1.0** release.

## Included Mods

| Mod | Original Era | Focus | Status |
|-----|-------------|-------|--------|
| [Dream Ship Mod](Dream%20Ship%20Mod/) | Alpha (2019) | Custom starting ship layout | Needs 1.0 update |
| [10 Crew Start](10%20Crew%20Start/) | Alpha (2019) | Start with 10 crew members | Needs 1.0 update |
| [Couchsurfing](Couchsurfing/) | Alpha (2019) | Additional furniture/comfort items | Needs 1.0 update |
| [Eff's Larger Fleet](Eff's%20Larger%20Fleet/) | Early EA (~2020) | Expanded fleet/ship limits | Needs 1.0 update |
| [More Hyperdrive](More%20Hyperdrive/) | Early EA (~2021) | Additional hyperdrive options | Needs 1.0 update |

## Purpose

These mods were part of the earliest wave of Space Haven modding activity and represent functionality the community valued during alpha. Original source files may be incomplete or unavailable; each mod directory contains:

- **`info.xml`** — Mod metadata and configurable variables (placeholder values where original data is unknown).
- **`patches/`** — XML patch operations (placeholder stubs awaiting 1.0 data IDs).
- **`README.md`** — Per-mod notes including original description, known issues, and modernization tasks.

## How to Expand

1. Research the original mod's patch targets using the Space Haven 1.0 data files.
2. Replace placeholder `<Operation>` stubs in `patches/haven_<modName>.xml` with real XPath selectors.
3. Update `info.xml` version and description.
4. Remove the `LEGACY PLACEHOLDER` notice from the mod's README once the port is complete.
