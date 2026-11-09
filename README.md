# Velvet Gate — Ren'Py visual novel

A **private, canon-first** development repository for a relaxed seven-day villa-life visual novel. The player is Domine, returning to his members-only House and spending time with its fourteen established women. This is a character-driven experiment, not a continuation of the Roman treasury RPG.

## Current status

**Seven Lanterns demo v0.2 source is in `game/`.** All fourteen women can be pursued during a seven-day week. Every woman has five distinct courtship chapters, two follow-up afternoons, and a personal ending, alongside twenty-eight day-specific casual group scenes. The character bible remains a reference, not a set of retroactive story changes.

The writing and Python logic have static tests. **Ren'Py SDK lint and an actual interactive playthrough remain to be done**; the SDK was not available in the development environment.

## Run the demo in Ren'Py

1. Install the current [Ren'Py SDK](https://www.renpy.org/latest.html) on your computer and open its Launcher.
2. Create a new Ren'Py project (for example `VelvetGateSevenLanterns`) with a standard GUI theme.
3. In that new project's `game/` folder, **replace** the generated `script.rpy` with the one from this repository, and copy over `routes.rpy` and `ambient.rpy`. Retain the generated `screens.rpy`, `gui.rpy`, `options.rpy`, and standard GUI assets.
4. Launch the project. The demo uses solid-color backgrounds and text; no external art, audio, or plugins are required.
5. In the Launcher, select **Check Script (Lint)** before treating the game as ready to share.

Use the repository's **Code → Download ZIP** option if you haven't cloned it locally. Avoid installing the old four-character prototype over this version.

## Start reading

1. [House rules](canon/HOUSE_RULES.md) — hierarchy and continuity invariants.
2. [Expanded estate plan](canon/ESTATE_LAYOUT.md) — approved geography, admission, housing, and circulation.
3. [Cast index](canon/CAST_INDEX.md) — all 14 women, their ranks by continuity, and their profiles.
4. [Relationships](canon/RELATIONSHIPS.md) — Witness pairings, Sydney/Maddie, and group dynamics.
5. [Character profiles](canon/characters/) — voice, behavior, visual anchors, things to avoid, and open questions.
6. [Agent instructions](AGENTS.md) — how future coding/writing work should use the references.

## Game structure

- One optional **casual group conversation** per morning, then one **dedicated afternoon** with any of the fourteen women, followed by a brief evening beat.
- One hidden numeric relationship value per woman: **Affinity**. Visits, romantic intent, reciprocity, and remembered moments are *story conditions*, not extra meters.
- Five substantial personal visits, including sincere interest and reciprocation, can secure a complete romance. Seven days cannot complete two romances. Sixth and seventh visits have new scenes instead of repeating the fifth.
- A warm but incomplete path resolves toward the strongest relationship if the player spreads attention, with a player choice if leads tie.
- Decisions and individual memories alter the tone and details of the closing scene. The interface never exposes affinity numbers.
- Private, members-only villa life; no financial-crisis plot or outsiders entering the estate.

See [demo mechanics](DESIGN_NOTES.md) for branching rules and test coverage.

## Tests

In a checkout with Python 3 available:

```bash
python3 -m unittest discover -s tests -v
```

The tests validate story-data syntax, route coverage, all fourteen complete endings, ambient scenes, tie selection, and milestone logic. They cannot validate Ren'Py script syntax or screen rendering; run the SDK's lint and play the full seven days for that.

## Sources

This reference baseline was built from the user's Villa Canon Hub character pages and recoverable conversations, with direct corrections taking priority. Historical search coverage is incomplete; uncertain details are marked as open rather than fabricated.
