# Seven Lanterns — demo rules and review notes

## Scope

This **game-only** continuity is a seven-day introduction to the members-only villa. Domine is received as the House's highest authority. His place is prepared before he arrives. Livia serves as Keeper, and Claire is provisional Mistress of the Lower House. The First Witnesses begin at Tier 2, and the Second Cohort begins at Tier 1. [Cast index](canon/CAST_INDEX.md) · [House rules](canon/HOUSE_RULES.md)

The expanded estate records the standing residential plan. The advancement awarded in a playthrough belongs to the demo. [Expanded estate plan](canon/ESTATE_LAYOUT.md)

All fourteen established adult women may be approached from the first afternoon. The women go about the ordinary work, leisure, and friendships of the villa while Domine considers a promotion in private.

## Daily rhythm

1. **Morning:** short day-specific introduction and a choice of four casual group areas, or solitude. Each area has a different scene on every day, including friendships, Witness guidance, and rivalries.
2. **Afternoon:** choose one woman among all fourteen (organized across five rooms). That woman's next chapter is determined by *how many times you have visited her*, not by the calendar day.
3. **Evening:** brief scenes close Days 1–6, with the promotion decision on the sixth evening. The last afternoon leads into the romantic finale.

Every woman has five successive personal chapters, then two distinct follow-ups if you concentrate nearly the whole week on her. Early visits establish personality and a small shared history. Later ones offer an explicitly personal invitation and a mutually chosen response. No affection is owed because Domine has higher rank.

## The private promotion

| When | Story beat and player options |
| --- | --- |
| Day 1 | After Claire's routine report, Livia tells Domine privately that he can advance one woman. Domine, Livia, and Claire keep the decision among themselves. |
| Days 2–5 | Ordinary scenes offer glimpses of how the women handle their work and treat one another. Yara makes room for Nisha to rehearse, and Domitia waits to offer Claire a practical suggestion in private. |
| Day 6 | In the Keeper's study, Domine can hear either adviser, hear both in either order, or give Livia a name straightaway. The choice is between the six Tier 1 Initiates and the six Tier 2 First Witnesses. Livia tells the chosen woman privately. |
| Day 7 | The winner has a distinct first-duty scene. Domine then spends his final afternoon with the woman of his choice, and the week resolves the romantic connection separately. |

| Starting rank | Advancement | First morning in the role |
| --- | --- | --- |
| Tier 1 Initiate | Tier 2 House Servant | A regular post at the morning audience in the atrium and a plain House clasp. |
| Tier 2 First Witness | Tier 3 Chamber Attendant | An assigned chamber-service duty under Livia, preparing the room's lamps and linens. |

Domine makes a single award. Each candidate has her own response to the new duty and a personal callback if she is also the romantic finalist. [House rules](canon/HOUSE_RULES.md)

## Hidden relationship logic

| Internal state | Type | Purpose | Visible to player? |
| --- | --- | --- | --- |
| `vg_affinity[name]` | Number | Warmth from conversations and recognition. Ranks connections within the completed or unfinished group. | Hidden |
| `vg_visits[name]` | Count | Records focused afternoons, gates an ending, breaks a tie | No |
| `vg_memories[name]` | Set-like list of tags | Tracks concrete moments; gates deep connection and modifies epilogue | Through story callbacks only |
| `vg_intent[name]` | Boolean | Player has expressed interest beyond role or ceremony after a few visits | Through dialogue |
| `vg_mutual[name]` | Boolean | Woman has accepted a later, freely offered courtship | Through dialogue |
| `vg_promoted` | Character key | Records the woman chosen for advancement and selects her Day 7 duty. | Through story scenes |

**Affinity is the only numeric relationship metric.** There is no Trust score, Love score, Wealth, House Harmony, or global morality bar in this demo. Visits are a count of scenes, and memories are narrative flags, not second emotional meters.

Choices in personal scenes award two affinity points for attentive, individual interest (and record that scene's memory), or one for a courteous but less intimate reply. A group-scene choice awards one affinity point and an ambient memory. The values are never displayed, and neither choice is framed as cruel or bad.

Either promotion grants the recipient **+2 hidden Affinity** once and records a promotion memory for her closing dialogue. A **complete romantic ending** requires at least five focused visits, three distinct memories earned in personal scenes, a clearly expressed personal interest, and a later affirmative reciprocal moment. Sixth and seventh visits can recover a slow-blooming route.

## Finale branches

| Outcome | Closing scenes |
| --- | --- |
| Domine promotes the woman he completes a courtship with | Her new duty appears in the morning. In her romantic closing scene, she remembers that he chose her. |
| Domine promotes one woman and completes another courtship | The chosen woman's duty plays out in the morning. The completed courtship gets the romantic finale, even if the promotion raised someone else's Affinity higher. |
| The available courtships are unfinished | Affinity determines the warm closing scene, so a promotion can tip a close result. A focused visit or group interaction establishes the connection. |
| Affinity is tied | More focused visits take precedence, followed by more shared moments. If the tie holds, the player chooses the final companion. |
| A save contains no social encounters | The week closes on the House. Normal play includes one focused visit each day. |

Earlier memories can shape the closing dialogue. For example, Maddie can pick up the story about Sydney that she left unfinished during an earlier visit.

Since a full courtship consumes at least five of seven afternoons, two full routes cannot be completed during one run. That restriction belongs to the **demo**, not the planned longer game. A future long-form game could allow courtship of all fourteen over time.

## Character continuity review

- Sydney's old sorority-style bond with Maddie informs their casual scenes; Sydney also guides Mina as her Witness.
- Yara has dry humor, leisure, friends, and her own wishes. Her Door Girl assignment does not define her personality or her route.
- Ione has pale silver-white hair, and her storyline makes room for self-care rather than treating deprivation as proof of love.
- Sylvie's plain Tier 1 clothing constrains how she can show her style. Nisha chooses when to share her dancing. Samira is a Veiled Vow candidate.
- Valeria's edge is tempered by restraint; Domitia's pride does not become independent authority. Claire's office is still provisional.
- Mina is an adult with growing personal agency, not Livia's assigned attendant. Saba and Safiya are not automatically related.

The promotion and its scenes are specific to the demo. The cast profiles record the starting ranks and the established relationships.

## Verification and next editorial pass

- The automated suite covers all fourteen romances, both promotion tiers, one-time Affinity awards, the unfinished ending swing, the completed ending priority, and call targets.
- Ren'Py 8.5.3 has compiled and launched the project successfully. A saved SDK lint report and documented full seven-day playthrough are still required before sharing a build.
- All eight location backgrounds and the first four portrait sets are integrated. The next editorial pass is to adjust individual voices in play, refine pacing on the fifth visit, complete the remaining portrait sets when requested, and continue UI polish.
- Audio and voice production are intentionally deferred.
