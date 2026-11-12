# Velvet Gate — Ren'Py visual novel

A **private, canon-first** development repository for a relaxed seven-day villa-life visual novel. The player is Domine, returning to his members-only House and spending time with its fourteen established women. This is a character-driven experiment, not a continuation of the Roman treasury RPG.

## Current status

**Seven Lanterns demo v0.3 is in `game/`.** All fourteen women can be pursued during the seven-day week. Domine also chooses one private promotion, with twelve candidates across two starting tiers. Each woman has five distinct courtship chapters, two follow-up afternoons, and a personal ending alongside the twenty-eight day-specific group scenes.

All eight locations now have 1920 × 1080 environment art. Livia, Claire, Maddie, and Yara have 31 dialogue sprites between them; the other ten women remain text-only. The writing and Python logic have static tests, and Ren'Py 8.5.3 has compiled and launched the project successfully. **A saved SDK lint report and a documented full-week playthrough remain to be done.**

## Run the demo in Ren'Py

1. Install the current [Ren'Py SDK](https://www.renpy.org/latest.html) on your computer and open its Launcher.
2. Place the repository folder in your Launcher projects directory. The folder contains the complete `game/` project.
3. Select the project and choose **Launch Project**.
4. Use **Check Script (Lint)** and play through the week before sharing a build.

Use the repository's **Code → Download ZIP** option if you haven't cloned it locally. Avoid installing the old four-character prototype over this version.

## Start reading

1. [House rules](canon/HOUSE_RULES.md) — hierarchy and continuity invariants.
2. [Expanded estate plan](canon/ESTATE_LAYOUT.md) — approved geography, admission, housing, and circulation.
3. [Cast index](canon/CAST_INDEX.md) — all 14 women, their ranks by continuity, and their profiles.
4. [Relationships](canon/RELATIONSHIPS.md) — Witness pairings, Sydney/Maddie, and group dynamics.
5. [Character profiles](canon/characters/) — voice, behavior, visual anchors, things to avoid, and open questions.
6. [Sprite production standard](SPRITE_PRODUCTION.md) — framing, identity lock, naming, and QA for future character art.
7. [Background production notes](BACKGROUND_PRODUCTION.md) — shared visual language and briefs for the eight environments.
8. [Agent instructions](AGENTS.md) — how future coding/writing work should use the references.

## Game structure

- One optional **casual group conversation** per morning, then one **dedicated afternoon** with any of the fourteen women, followed by a brief evening beat.
- Livia and Claire discuss the possible promotion with Domine in private. On Day 6, he names one woman to advance a tier. Her new duty appears the next morning.
- One hidden numeric relationship value per woman: **Affinity**. Visits, romantic intent, reciprocity, and remembered moments are *story conditions*, not extra meters.
- Five substantial personal visits, including sincere interest and reciprocation, can secure a complete romance. Seven days cannot complete two romances. Sixth and seventh visits have new scenes instead of repeating the fifth.
- The promotion grants its recipient **+2 hidden Affinity** and a memory. A completed courtship gets priority. Affinity can tip the closing scene between unfinished connections, with a player choice if the leads are tied after the other criteria.
- Decisions and individual memories alter the tone and details of the closing scene. The interface never exposes affinity numbers.
- Private, members-only villa life; no financial-crisis plot or outsiders entering the estate.

See [demo mechanics](DESIGN_NOTES.md) for branching rules and test coverage.

## Tests

In a checkout with Python 3 available:

```bash
python3 -m unittest discover -s tests -v
```

The tests validate story data, route coverage, the promotion branches, and finale selection. Use the SDK's lint and a playthrough to verify script execution and screen rendering.

## Sources

This reference baseline was built from the user's Villa Canon Hub character pages and recoverable conversations, with direct corrections taking priority. Historical search coverage is incomplete; uncertain details are marked as open rather than fabricated.
