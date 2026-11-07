# Seven Lanterns — demo rules and review notes

## Scope

This **game-only** continuity is a seven-day, low-pressure introduction to Velvet Gate. The player is Domine, with Livia as Keeper and Claire as provisional Lower House Mistress. The six Tier-1 Witnesses and six Tier-0 Second Cohort women preserve their roles; no permanent promotion is made by a romantic ending. Only House members appear in the villa. The AD 33 treasury campaign is not imported.

All fourteen established adult women may be approached from the first afternoon. The small story is about spending time with someone who remains an individual beyond her duties. There is no imposed mystery or forced romance.

## Daily rhythm

1. **Morning:** short day-specific introduction and a choice of four casual group areas, or solitude. Each area has a different scene on every day, including friendships, Witness guidance, and rivalries.
2. **Afternoon:** choose one woman among all fourteen (organized across five rooms). That woman's next chapter is determined by *how many times you have visited her*, not by the calendar day.
3. **Evening:** time passes, with a modest midweek reflection and a members-only Day-7 supper.

Every woman has five successive personal chapters, then two distinct follow-ups if you concentrate nearly the whole week on her. Early visits establish personality and a small shared history. Later ones offer an explicitly personal invitation and a mutually chosen response. No affection is owed because Domine has higher rank.

## Hidden relationship logic

| Internal state | Type | Purpose | Visible to player? |
| --- | --- | --- | --- |
| `vg_affinity[name]` | Number | Warmth accrued through attentive or courteous choices; determines the strongest connection first | No |
| `vg_visits[name]` | Count | Records focused afternoons, gates an ending, breaks a tie | No |
| `vg_memories[name]` | Set-like list of tags | Tracks concrete moments; gates deep connection and modifies epilogue | Through story callbacks only |
| `vg_intent[name]` | Boolean | Player has expressed interest beyond role or ceremony after a few visits | Through dialogue |
| `vg_mutual[name]` | Boolean | Woman has accepted a later, freely offered courtship | Through dialogue |

**Affinity is the only numeric relationship metric.** There is no Trust score, Love score, Wealth, House Harmony, or global morality bar in this demo. Visits are a count of scenes, and memories are narrative flags, not second emotional meters.

Choices in personal scenes award two affinity points for attentive, individual interest (and record that scene's memory), or one for a courteous but less intimate reply. A group-scene choice awards one affinity point and an ambient memory. The values are never displayed, and neither choice is framed as cruel or bad.

For a **complete romantic ending**, a woman needs at least five focused visits, three distinct meaningful memories from personal scenes, a clearly expressed personal interest after the first few encounters, and a later affirmative reciprocal moment. Sixth and seventh visits can recover a slow-blooming route. A generic high number on its own is insufficient.

## Finale branches

- A strong, completed route reaches that woman's unique romantic closing scene.
- An affinity leader without the requisite moments receives her distinct **unfinished but hopeful** closing scene.
- When attention is widely split, the same incomplete rule applies to the strongest connection; there is no arbitrary penalty screen.
- If no one was approached, the game closes on a quiet general note. (In normal play there is one required afternoon daily.)
- Equal affinity scores are resolved by more focused visits, then more recorded moments; if still tied, the player chooses between those equally strong connections.
- Individual earlier memories can add a closing callback. This is where a choice matters *qualitatively*, not merely as a score.

Since a full courtship consumes at least five of seven afternoons, two full routes cannot be completed during one run. That restriction belongs to the **demo**, not the planned longer game. A future long-form game could allow courtship of all fourteen over time.

## Character continuity review

- Sydney's old sorority-style bond with Maddie informs their casual scenes; Sydney also guides Mina as her Witness.
- Yara has dry humor, leisure, friends, and her own wishes. Her Door Girl assignment does not define her personality or her route.
- Ione has pale silver-white hair, and her storyline makes room for self-care rather than treating deprivation as proof of love.
- Sylvie's personal style remains constrained by Tier 0; Nisha does not perform on command; Samira is **not** an initiated Veiled Vow member.
- Valeria's edge is tempered by restraint; Domitia's pride does not become independent authority. Claire's office is still provisional.
- Mina is an adult with growing personal agency, not Livia's assigned attendant. Saba and Safiya are not automatically related.

All new events and lines are **proposed game writing**, not new facts added to `canon/`.

## Verification and next editorial pass

- Automated static suite: 11 tests covering cast/route counts, reachable successes, incomplete endings, alternate visits, group-scene coverage, tie behavior and call targets.
- Ren'Py SDK lint and live seven-day playthrough are **still required** on a computer with the SDK installed.
- Suggested editorial pass: adjust individual voices in play, refine pacing on the fifth visit, then add portraits, location art, UI polish, and sound after mechanics feel right.
