# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This repository contains XML-based mods for the game **Space Haven**, targeting mod loader version `0.10.0` or higher. There is no build system, test suite, or package manager — mods are distributed as raw XML files packaged into archives.

## Mod Structure

Each mod is a top-level directory containing exactly:

- **`info.xml`** — Mod metadata (name, description, version, author, and configurable variables).
- **`patches/haven_<modName>.xml`** — One or more XML patch operations that modify game data at runtime.

### Variable Interpolation

Configurable values are declared in `info.xml` under `<config>` using `<var name="{varName}" default="...">...</var>`. These bracketed placeholders (`{varName}`) are interpolated into the corresponding patch XML files at load time. When adding or editing configurable values, keep the placeholder syntax consistent across `info.xml` and the patch file.

### Patch Operation Pattern

Patches use XPath selectors to target specific game elements and change attributes:

```xml
<Operation Class="AttributeSet">
  <xpath>/data/Element/me[@mid="..."]...</xpath>
  <attribute>attributeName</attribute>
  <value>{interpolatedVar}</value>
</Operation>
```

- `mid` = module/item ID (e.g., `120` for Airlock).
- `cid` = craft/vehicle ID (e.g., `20` for Shuttle).
- Both `/data/Element/me[...]` (ship modules) and `/data/Craft/craft[...]` (vehicles) are valid targets.

## Mod Inventory

| Mod | Status | Focus |
|-----|--------|-------|
| Improved Airlock | Active | Oxygen, inventory capacities |
| Improved Shuttles | Active | Crew, oxygen, carry capacities |
| Hyperdrive Mass Config | Unreleased | `massCapacity` of hyperdrives |
| Pack Wagon | Active | Storage capacities |
| Less System Points | Active | Configurable `systemPoints` for modules |
| Zero System Points | **DEPRECATED** | Hard-coded `systemPoints=0`; superseded by **Less System Points** |
| Legacy Mods/Dream Ship Mod | **LEGACY PLACEHOLDER** | Custom starting ship layout; needs 1.0 port |
| Legacy Mods/10 Crew Start | **LEGACY PLACEHOLDER** | Start with 10 crew; needs 1.0 port |
| Legacy Mods/Couchsurfing | **LEGACY PLACEHOLDER** | Extra furniture/comfort items; needs 1.0 port |
| Legacy Mods/Eff's Larger Fleet | **LEGACY PLACEHOLDER** | Expanded fleet limits; needs 1.0 port |
| Legacy Mods/More Hyperdrive | **LEGACY PLACEHOLDER** | Additional hyperdrive options; needs 1.0 port |

## Common Tasks

- **Create a new mod**: Add a new top-level directory with `info.xml` and `patches/haven_<name>.xml` following the existing conventions.
- **Update a patch**: Edit the corresponding `patches/haven_*.xml` and, if the value should be user-configurable, add a matching `<var>` entry in `info.xml`.
- **Package for distribution**: Zip the mod directory (e.g., `Improved Airlock/`). The `.gitignore` excludes `*.zip`, `*.7z`, and `*.rar` from version control.
