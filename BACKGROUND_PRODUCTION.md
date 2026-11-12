# Velvet Gate background production notes

The eight `game/images/backgrounds/vg_*.png` files form one visual set for the
*Seven Lanterns* demo. They were generated with the built-in image-generation
workflow, reviewed as a group, and prepared as opaque 1920 × 1080 PNG files.

## Shared visual language

- Cinematic photorealistic environment art with a lightly painterly
  visual-novel finish.
- An elegant but lived-in Roman-inspired Mediterranean coastal villa: cream
  plaster, pale limestone, terracotta, restrained fresco and mosaic accents,
  bronze oil lamps, burgundy details, muted greenery, and sea blue.
- Standing eye-level camera and natural perspective.
- Keep the central 45 percent relatively uncluttered for sprites, the bottom 28
  percent low-detail and slightly darker for the dialogue box, and the top-left
  quiet for the day marker.
- No people, figures, faces, statues, readable text, logos, watermarks, modern
  objects, electric lighting, anachronistic furniture, or fantasy architecture.

The approved atrium established the palette and rendering style. Each later
location used it only as a style reference, not as a layout to copy.

## Location briefs

| File | Production brief |
| --- | --- |
| `vg_atrium.png` | Morning atrium with limestone columns, cream plaster, terracotta edges, a shallow impluvium, restrained mosaics, low benches, and bread and water placed to one side; calm sea-breeze daylight and a garden glimpse beyond. |
| `vg_study.png` | Livia's orderly northwest study opening to a shaded gallery, with a plain writing table, wax tablets, closed ledger, two seats, neat shelves, bronze lamps, burgundy drapery, and cool side light; private and disciplined rather than luxurious. |
| `vg_terrace.png` | Covered south-facing loggia over descending gardens and the sea, with shaded columns, warm tile, modest seating, fruit and tea to one side, and afternoon light crossing the open floor. |
| `vg_garden.png` | Shaded garden peristyle with a narrow reflecting pool, swept path, rain arbor, white flowers, rosemary, myrtle, olive greenery, colonnades, and a quiet bench; tended but lived in. |
| `vg_library.png` | Intimate library with scrolls and codices, window seat, two reading chairs, curtained alcove, unreadable open volume, warm garden light, and rain-ready shutters. |
| `vg_music.png` | Private rehearsal room with a large open mosaic floor, high plaster walls, colonnaded daylight, and a lyre, frame drum, and reed pipes stored along the side; never a public stage. |
| `vg_chamber.png` | Modest service-side chamber in early light with folded ivory linen, low bronze lamps, wooden draft screen, shuttered window, practical storage, and a prepared couch kept to the edge; quiet care rather than opulence. |
| `vg_evening.png` | Blue-hour courtyard with garden and sea beyond, an open central meeting space, and exactly seven warm oil lanterns along the walk; intimate and hopeful, with a dark simple textbox zone. |

## Preparation and acceptance

The generated 1672 × 941 sources shared an exact 16:9 composition. Final assets
were resized once with high-quality bicubic interpolation to 1920 × 1080 and
saved as opaque PNG files. Do not repeatedly rescale or recompress the accepted
files.

Before replacing a background, compare it with the entire set and verify:

1. the 1920 × 1080 dimensions and opaque output;
2. a clear central sprite area and quiet bottom textbox zone;
3. a quiet top-left corner for the day marker;
4. no people, readable marks, modern objects, or unintended public-villa cues;
5. continuity with the approved estate plan and the room's written scenes.

Create a versioned candidate and review it before replacing an accepted file.
