# Velvet Gate sprite production standard

Use this specification for future dialogue sprites. It preserves the approved
Livia-style upper-body presentation and prevents another mix of close portraits
and full-body art.

Character identity and clothing must follow the relevant profile in
[`canon/characters/`](canon/characters/), the ranks in
[`canon/CAST_INDEX.md`](canon/CAST_INDEX.md), and the current-scene privilege
rules in [`canon/HOUSE_RULES.md`](canon/HOUSE_RULES.md). Proposed future style
lanes are not automatically available in the seven-day demo.

## Master asset

Approve one neutral listening portrait before producing expressions or special
poses. Treat that image as the identity master for the rest of the set.

- **Format:** RGBA PNG with genuine transparency.
- **Canvas:** 1152 × 1536 pixels, portrait orientation.
- **Framing:** head through waist or upper thigh, matching Livia; never show the
  complete body or feet.
- **Placement:** centered, with the hair top roughly 50–90 pixels below the top
  edge. The figure should reach the bottom edge naturally.
- **Rendering:** photorealistic character cutout, clean antialiased edges, soft
  even light, and texture detail consistent with the existing portraits.
- **Background:** fully transparent. Do not bake in a room, gradient, glow,
  vignette, floor shadow, outline, or colored fringe.
- **Exclusions:** no text, logos, watermark, frame, cropped hair, accidental
  missing fingers, modern props, or unapproved jewelry and insignia.

Do not upscale a small draft into the master. Generate or edit at production
resolution, and keep rejected drafts outside `game/`.

## Identity lock

Every image after the master must preserve:

- face shape, apparent age, complexion, eye color, and distinctive features;
- hair color, texture, length, and approved arrangement;
- body proportions and camera distance;
- clothing construction, rank-appropriate accessories, and color palette;
- camera angle, light direction, contrast, and overall rendering style.

Change only the requested expression, hand position, or pose, and preserve the
master's player-directed gaze unless the scene calls for an exception. Compare
each candidate directly with the master before accepting it. If the identity,
costume, or framing drifts, reject the candidate rather than treating the drift
as a new character detail.

## Eye contact with the player

Dialogue portraits look directly at the player, using the camera lens as the
shared target for both eyes. This applies to listening, speaking, and all
baseline expressions. Keep that target fixed when changing the mouth, brows,
eyelids, or pose. For neutral speaking, start from the approved listening
portrait and change the mouth and jaw for speech. If the lids open wider or
the head tilts, check that the gaze still lands at the player's eye level.

Break eye contact only when the action or emotional beat specifically calls for
it. For example, a character can look at a tablet while reading it, turn her
eyes to someone else when addressing them, or look down when the scene calls
for her to avoid the player's gaze. Name the scene beat and the intended gaze
target or direction in the sprite brief. Use that variant for the beat and
return to a player-facing portrait when the character re-engages. Keep the
default gaze for general-purpose expressions such as `considering` and for
poses that simply hold a prop.

## Baseline expression set

Each standard set contains seven images and seven Ren'Py tags:

| Order | Tag | Direction | Filename suffix |
| --- | --- | --- | --- |
| 01 | `listening` | neutral, attentive, mouth closed | `01_listening_neutral` |
| 02 | `explaining` | composed speech, restrained gesture | `02_explaining_neutral_speaking` |
| 03 | `considering` | thoughtful or mildly worried | `03_considering_worried` |
| 04 | `unconvinced` | firm displeasure or skepticism | `04_unconvinced_angry` |
| 06 | `knowing_challenge` | knowing, amused challenge | `06_knowing_challenge_amused` |
| 09 | `happy` | character-specific open warmth | `09_happy` |
| 12 | `affectionate` | intimate warmth without generic seduction | `12_affectionate` |

Special poses are optional. Add one only when a written scene already needs it,
and give it a descriptive tag such as Yara's `held_look`, `private_aside`, or
`come_closer`. A special pose does not replace the seven-image baseline.

## Paths and naming

Use the lowercase character key everywhere:

```text
game/images/<key>/<key>_<filename-suffix>.png
```

Example:

```text
game/images/livia/livia_01_listening_neutral.png
```

Register the images in `game/cast_sprites.rpy` (or the character's existing
sprite file) with the stable dialogue tags above. Add the neutral portrait to
the `Character` definition:

```renpy
define vg_<key> = Character("Name", color="#hex", show_portrait="<key> listening")
```

New close-framed masters use `vg_dialogue_portrait`. Do not add the character to
the `vg_fullbody_dialogue_portrait` branch; that branch is a compatibility rule
for the existing Claire and Yara full-body source files. Maddie's dialogue
portraits use the close crop. Her optional head-to-toe variants live in
`game/images/maddie/fullbody/`, with `_fullbody` filenames.

Add complete and incomplete finale choices to `vg_finale_portraits`, and attach
specific route portraits with `portrait=` and `warm_portrait=` when the neutral
default does not fit the beat.

## Production prompt template

Use the approved master as the identity reference for every derivative image.
For a scene-specific gaze exception, replace the `Gaze` line with the intended
target or direction and the reason for looking away.

```text
Use case: identity-preserve
Asset type: transparent Ren'Py dialogue sprite
Primary request: create the <state> expression/pose for <character>
Input image: approved neutral master; preserve identity, costume, camera, and light
Style/medium: photorealistic character cutout matching the reference exactly
Composition/framing: 1152x1536; centered head-to-upper-thigh portrait; same scale
Gaze: keep both eyes fixed on the same camera-lens target at the player's eye
  level, matching the neutral reference through the expression or pose change.
  For neutral speech, change the mouth and jaw while preserving that gaze.
Constraints: change only <expression/pose> and any specified gaze exception;
  preserve all other visible details;
  genuine transparent background; clean alpha edges; no text or watermark
Avoid: full body, feet, scenery, glow, vignette, identity drift, costume drift,
  age drift, beauty-filter smoothing, extra accessories, malformed hands
```

Generate one state at a time. Approve it before using it as context for another
state; do not allow a flawed derivative to become the next identity reference.

## Acceptance checklist

Before wiring a set into the game:

1. Confirm every file is the expected pixel size and RGBA PNG.
2. Inspect transparency at all four corners and around hair, fingers, and fabric.
3. Compare the face, hair, costume, and apparent age with the approved master.
4. Confirm consistent head size and vertical placement across all seven files.
5. Compare the candidate and neutral master side by side in close crops at
   the same apparent face size. Start at native resolution so both irises,
   lids, and surrounding eye whites are visible. Confirm both eyes share the
   intended target. Look for slight upward, downward, or sideways drift,
   especially when a speaking pose opens the lids wider. Judge the gaze in
   the context of the head angle and lid shape. Recheck at the intended
   dialogue size. Revise any candidate that
   reads as looking past the player without a documented scene reason.
6. Confirm filenames and Ren'Py tags match this specification exactly.
7. Verify every image definition resolves and every referenced tag exists.
8. Preview all states at 1920 × 1080 with the dialogue box visible.
9. Check that hair and gestures stay on-screen and that the textbox hides only
   the intended lower portion of the portrait.
10. Run the static test suite and Ren'Py lint, then perform an in-game expression
    pass before committing.

Keep the original accepted PNGs unchanged after integration. If a revision is
needed, create and review a versioned candidate before replacing the approved
asset.

## Current eye-contact review (2026-11-11)

Rechecked all 31 source sprites with side-by-side eye crops against each
character's neutral listening portrait. Flagged one sprite for correction.

- **Maddie's original `maddie_02_explaining_neutral_speaking.png`.** The wider eye
  openings leave more white visible below the irises, making her gaze read
  slightly above the player. This is visible in the source art, and both
  Maddie states use the same Ren'Py portrait transform. The original prompt
  and edit history are unavailable in the repository, so the production
  trigger is unconfirmed. The approved replacement corrects the gaze and
  applies the younger look described below.
- **Borderline poses.** Claire's `considering` and `affectionate` and Maddie's
  `considering` still read as looking at the player. Claire's
  `knowing_challenge` keeps eye contact while holding the tablet. Yara's
  `come_closer`, `held_look`, and `private_aside` also keep eye contact.

## Maddie apparent-age review

Maddie's dialogue art should read consistently as a young adult, about 18–22.
Use the approved youthful face as the reference across expressions. Preserve
her freckles, skin texture, and expressive brows. Keep temporary expression
creases shallow enough that a sprite switch still reads as the same age.

The seven refreshed dialogue sprites use this age reference. The separate
full-body set uses the established blush slingbacks and a matching sash
length, measured from the bottom of the waist wrap to the longest tail.

| Sprite | Review of the previous art |
| --- | --- |
| `listening` | One of the closest age references. Relaxed brows and softer cheeks make it a good baseline for comparison. |
| `explaining` | The original's raised-brow lines and stronger under-eye and smile-fold shadows read older. The approved replacement softens those cues and keeps direct eye contact. |
| `considering` | A deep crease between the brows and stronger under-eye shadows make the worried pose read older. Keep a light furrow. |
| `unconvinced` | The deepest forehead and brow furrows. Soften the lines while retaining the knit brows and firm mouth. |
| `knowing_challenge` | Mild under-eye and mouth-corner shadow. Keep the smirk and its slight asymmetry. |
| `happy` | The grin creates the strongest eye-corner and smile folds. Soften their depth while keeping the full smile. |
| `affectionate` | One of the closest age references. The relaxed eyes and soft smile keep the cheek transitions gentle. |
