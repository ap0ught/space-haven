# Space Haven Mods

Source code for a small collection of Space Haven mods by Killparadise, plus an imported developer template for building Java-based Space Haven mods.

## Mods in this repository

- Improved Airlock
- Improved Shuttles
- Hyperdrive Mass Config *(not released to Nexus Mods)*
- Pack Wagon
- Less System Points
- Zero System Points *(deprecated)*
- SpaceHavenMods-Tron762 import set *(merged from `Tron762-SpaceHavenMods` branch)*

## Where these mods came from

Most of the mods in this repository were published on Nexus Mods and are tracked here as source XML patches plus loader metadata. The exceptions are:

- **Hyperdrive Mass Config**: source-only mod in this repository, noted in `info.xml` as not released to Nexus Mods.
- **Zero System Points**: older deprecated mod kept here for reference after **Less System Points** replaced it.

| Mod | Repository source | Published release | Status |
| --- | --- | --- | --- |
| Improved Airlock | [`Improved Airlock/`](./Improved%20Airlock/) | [Nexus Mods](https://www.nexusmods.com/spacehaven/mods/24) | Published |
| Improved Shuttles | [`Improved Shuttles/`](./Improved%20Shuttles/) | [Nexus Mods](https://www.nexusmods.com/spacehaven/mods/23) | Published |
| Pack Wagon | [`Pack Wagon/`](./Pack%20Wagon/) | [Nexus Mods](https://www.nexusmods.com/spacehaven/mods/22) | Published |
| Less System Points | [`Less System Points/`](./Less%20System%20Points/) | [Nexus Mods](https://www.nexusmods.com/spacehaven/mods/20) | Published |
| Hyperdrive Mass Config | [`Hyperdrive Mass Config/`](./Hyperdrive%20Mass%20Config/) | — | Repository-only |
| Zero System Points | [`Zero System Points/`](./Zero%20System%20Points/) | — | Deprecated |

## GitHub Pages showcase

A static site is available in [`docs/`](./docs/) and is ready to be published with GitHub Pages. It highlights each mod, its default changes, configuration options, and where to find the source.

## Developer template

This repository now also includes the upstream MIT-licensed [`SpaceHavenModTemplate`](./developer-tools/SpaceHavenModTemplate/) from the Spacehaven modding tools developers. The imported template keeps the original `LICENSE`, `README.md`, `pom.xml`, AspectJ examples, and game config helpers so it can be referenced locally from this repo.

The two bundled AspectJ jar files and the upstream `target/` build output were intentionally not copied into this repository snapshot; the template README already documents how to obtain those dependencies.

## Tron762-SpaceHavenMods attribution

The branch [`Tron762-SpaceHavenMods`](https://github.com/ap0ught/space-haven-mods/tree/Tron762-SpaceHavenMods) has been merged into this repository and imported under [`SpaceHavenMods-Tron762/`](./SpaceHavenMods-Tron762/). These files are attributed to the original `Tron762/SpaceHavenMods` mod collection and preserve its upstream README context.

Imported mods in this set include:

- CircleOfLife
- CompactWorkbenches
- FoodMod
- MoistureVaporator
- MoreWaterFromIce
- RefineryMod
