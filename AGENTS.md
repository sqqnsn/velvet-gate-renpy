# Velvet Gate — agent instructions

This repository holds a Ren'Py villa-life visual novel and its working character bible.

## Before changing anything

1. Read `canon/HOUSE_RULES.md`, `canon/CAST_INDEX.md`, and the relevant character files.
2. For interactions involving multiple women, read `canon/RELATIONSHIPS.md`.
3. Respect the distinction between **established canon**, **game-writing interpretation**, and **open questions**. Do not present the latter two as established history.
4. Use each file's source links to check important ambiguities. Explicit corrections from Domine take precedence over earlier assistant-created descriptions.

## Continuity

- Domine is the player and the House's highest authority. Livia is Keeper and the highest internal authority beneath him; Claire is provisional Mistress of the Lower House, not the Keeper.
- The villa is strictly members-only. No non-member guests, public events, or outside banquets at the villa.
- Keep the Roman financial-crisis RPG and its financial ledger **separate** from the Ren'Py game's seven-day slice-of-life continuity.
- The core cast is the 14 women in `canon/CAST_INDEX.md`. Prospects or earlier concepts are not automatically current residents.
- Ranks and earned privileges matter. A work duty is not the same as a permanent office or a woman's whole personality.
- Introduce roles through scenes; never demand that a new player already know the lore.
- Preserve the individual's personality and agency. Attention or favor from Domine does not automatically entitle a relationship.
- Keep sensuality and romance character-driven; do not reduce women to visual archetypes or ethnic stereotypes.

## Writing and implementation

- Build a leisurely villa-life prototype: conversations, group dynamics, small choices, low-stakes events, and replayable routines.
- Let characters interact when the player is elsewhere.
- Distinguish everyone in **voice**, not merely in costumes or color palettes.
- Put reference documents outside Ren'Py's `game/` folder and runnable `.rpy` scripts inside it.
- Keep character/game state in Ren'Py `default` variables. Test with Ren'Py lint and a runtime playthrough when the SDK is available.
- Add new character traits as **proposal** first. Update canon only after the user approves them.
- Prefer small reviewable commits, cite key source pages in the reference files, and avoid overwriting a user's earlier prototype without inspection.
