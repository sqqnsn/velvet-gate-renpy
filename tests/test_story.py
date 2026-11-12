"""Static story-logic tests that run without an installed Ren'Py SDK.

They compile the normal Python blocks embedded in .rpy files and exercise the
same state functions that the Ren'Py script calls. They do not replace lint or
a playthrough in Ren'Py itself.
"""

import re
import struct
import textwrap
import types
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"


def load_init_blocks(path, namespace):
    lines = path.read_text(encoding="utf-8").splitlines()
    in_block = False
    block = []
    for line in lines + ["END"]:
        if line == "init python:":
            in_block = True
            block = []
        elif in_block:
            if line and not line.startswith((" ", "\t")):
                exec(compile(textwrap.dedent("\n".join(block)), str(path), "exec"), namespace)
                in_block = False
            else:
                block.append(line)


def create_namespace():
    namespace = {}
    load_init_blocks(GAME / "routes.rpy", namespace)
    load_init_blocks(GAME / "ambient.rpy", namespace)
    load_init_blocks(GAME / "promotion.rpy", namespace)
    order = namespace["VG_ORDER"]
    namespace["store"] = types.SimpleNamespace(
        vg_affinity={key: 0 for key in order},
        vg_visits={key: 0 for key in order},
        vg_memories={key: [] for key in order},
        vg_intent={key: False for key in order},
        vg_mutual={key: False for key in order},
        vg_promoted=None,
    )
    namespace["renpy"] = types.SimpleNamespace(store=namespace["store"])
    return namespace


class VelvetGateLogicTests(unittest.TestCase):
    def setUp(self):
        self.ns = create_namespace()
        self.store = self.ns["store"]

    def focus(self, key, choice):
        visit = self.store.vg_visits[key]
        chapter = self.ns["vg_get_chapter"](key, visit)
        self.ns["vg_record_focus"](key, visit, choice, chapter)

    def completed(self, key):
        return self.ns["vg_is_complete"](
            key, self.store.vg_visits, self.store.vg_memories,
            self.store.vg_intent, self.store.vg_mutual,
        )

    def finalists(self):
        return self.ns["vg_best_connections"](
            self.store.vg_affinity, self.store.vg_visits, self.store.vg_memories,
            self.store.vg_intent, self.store.vg_mutual,
        )

    def test_all_fourteen_characters_have_complete_content(self):
        order = self.ns["VG_ORDER"]
        self.assertEqual(14, len(order))
        self.assertEqual(len(order), len(set(order)))
        for field in ("VG_NAMES", "VG_SCENES", "VG_FOLLOWUPS", "VG_ENDINGS"):
            self.assertEqual(set(order), set(self.ns[field]), field)
        for key in order:
            chapters = self.ns["VG_SCENES"][key]
            followups = self.ns["VG_FOLLOWUPS"][key]
            self.assertEqual(5, len(chapters), key)
            self.assertEqual(2, len(followups), key)
            self.assertEqual(7, len({c["choices"][0]["memory"] for c in chapters + followups}), key)
            for chapter in chapters + followups:
                self.assertTrue(chapter["opening"] and chapter["line"], key)
                self.assertEqual(2, len(chapter["choices"]), key)
                for choice in chapter["choices"]:
                    self.assertTrue(choice["text"] and choice["reply"], key)
            end = self.ns["VG_ENDINGS"][key]
            self.assertEqual(
                {"complete", "complete_speech", "incomplete", "incomplete_speech", "memory", "recall", "alternate_memory", "alternate_recall"},
                set(end), key,
            )
            self.assertIn(end["memory"], [c["choices"][0]["memory"] for c in chapters], key)
            self.assertIn(end["alternate_memory"], [c["choices"][0]["memory"] for c in chapters], key)

    def test_every_woman_is_in_player_menus(self):
        script = (GAME / "script.rpy").read_text(encoding="utf-8")
        selectable = set(re.findall(r'vg_current_key\s*=\s*"(\w+)"', script))
        self.assertEqual(set(self.ns["VG_ORDER"]), selectable)

    def test_livia_has_portraits_for_every_personal_chapter_and_finale(self):
        chapters = self.ns["VG_SCENES"]["livia"] + self.ns["VG_FOLLOWUPS"]["livia"]
        for chapter in chapters:
            self.assertTrue(chapter["portrait"], chapter["opening"])
            self.assertTrue(chapter["choices"][0].get("portrait"), chapter["opening"])

        script = (GAME / "script.rpy").read_text(encoding="utf-8")
        self.assertIn('show_portrait="livia listening"', script)
        self.assertIn('("livia", "complete"): "livia fingertip_at_lip"', script)
        self.assertIn('("livia", "incomplete"): "livia hands_on_hips"', script)

    def test_all_backgrounds_are_wired_and_1920_by_1080(self):
        names = (
            "atrium", "study", "terrace", "garden",
            "library", "music", "chamber", "evening",
        )
        script = (GAME / "script.rpy").read_text(encoding="utf-8")

        for name in names:
            relative = f"images/backgrounds/vg_{name}.png"
            self.assertIn(f'image vg {name} = "{relative}"', script)
            path = GAME / relative
            self.assertTrue(path.is_file(), relative)
            with path.open("rb") as background:
                header = background.read(24)
            self.assertEqual(b"\x89PNG\r\n\x1a\n", header[:8], relative)
            self.assertEqual((1920, 1080), struct.unpack(">II", header[16:24]), relative)

    def test_every_woman_can_reach_her_own_romantic_ending(self):
        for key in self.ns["VG_ORDER"]:
            ns = create_namespace()
            st = ns["store"]
            for _ in range(5):
                visit = st.vg_visits[key]
                chapter = ns["vg_get_chapter"](key, visit)
                ns["vg_record_focus"](key, visit, 0, chapter)
            self.assertTrue(ns["vg_is_complete"](
                key, st.vg_visits, st.vg_memories, st.vg_intent, st.vg_mutual,
            ), key)
            self.assertEqual(5, st.vg_visits[key])
            self.assertEqual(10, st.vg_affinity[key])

    def test_casual_moments_cannot_replace_dedicated_courtship(self):
        for day in range(1, 8):
            self.ns["vg_ambient_touch"]("maddie", "garden", day)
        self.assertEqual(7, self.store.vg_affinity["maddie"])
        self.assertEqual(0, self.store.vg_visits["maddie"])
        self.assertFalse(self.completed("maddie"))

    def test_five_polite_visits_are_not_automatic_romance(self):
        for _ in range(5):
            self.focus("livia", 1)
        self.assertFalse(self.completed("livia"))
        self.assertFalse(self.store.vg_mutual["livia"])

    def test_extra_visits_can_salvage_a_slow_start(self):
        for _ in range(4):
            self.focus("yara", 1)
        for _ in range(3):
            self.focus("yara", 0)
        self.assertTrue(self.completed("yara"))
        self.assertEqual(7, self.store.vg_visits["yara"])

    def test_six_or_seven_visits_do_not_repeat_fifth_chapter(self):
        for key in self.ns["VG_ORDER"]:
            scenes = [self.ns["vg_get_chapter"](key, i)["opening"] for i in range(7)]
            self.assertEqual(7, len(set(scenes)), key)

    def test_only_one_full_romance_fits_seven_days(self):
        # A completed route needs five focused visits, so two need at least ten.
        self.assertGreater(5 * 2, 7)
        # Two competing leads with three and four visits remain incomplete.
        for _ in range(4):
            self.focus("livia", 0)
        for _ in range(3):
            self.focus("claire", 0)
        self.assertFalse(self.completed("livia"))
        self.assertFalse(self.completed("claire"))

    def test_ending_prefers_affinity_then_focus_then_memories(self):
        self.assertEqual([], self.finalists())
        self.focus("maddie", 0)
        self.focus("sydney", 0)
        self.assertEqual(["maddie", "sydney"], self.finalists())
        self.focus("sydney", 1)
        self.assertEqual(["sydney"], self.finalists())

    def test_both_tiers_cover_all_twelve_promotion_candidates(self):
        tiers = self.ns["VG_PROMOTION_TIERS"]
        self.assertEqual({"sylvie", "nisha", "valeria", "mina", "samira", "safiya"}, set(tiers[2]))
        self.assertEqual({"maddie", "sydney", "domitia", "ione", "saba", "yara"}, set(tiers[3]))
        stories = self.ns["VG_PROMOTION_STORIES"]
        self.assertEqual(set(tiers[2]) | set(tiers[3]), set(stories))
        for key, story in stories.items():
            self.assertEqual({"morning", "greeting", "recall"}, set(story), key)
            self.assertTrue(all(story.values()), key)

    def test_promotion_awards_two_affinity_once_at_either_tier(self):
        for winner, other in (("mina", "yara"), ("yara", "mina")):
            with self.subTest(winner=winner):
                ns = create_namespace()
                store = ns["store"]
                award = ns["vg_award_promotion"]
                award("claire")
                self.assertIsNone(store.vg_promoted)
                award(winner)
                award(winner)
                award(other)
                self.assertEqual(winner, store.vg_promoted)
                self.assertEqual(2, store.vg_affinity[winner])
                self.assertEqual([ns["VG_PROMOTION_MEMORY"]], store.vg_memories[winner])
                self.assertEqual(0, store.vg_affinity[other])
                self.assertEqual(0, store.vg_visits[winner])
                self.assertFalse(store.vg_intent[winner])
                self.assertFalse(store.vg_mutual[winner])

    def test_promotion_memory_cannot_supply_a_personal_milestone(self):
        for choice in (1, 1, 1, 0, 0):
            self.focus("mina", choice)
        self.assertTrue(self.store.vg_mutual["mina"])
        self.ns["vg_award_promotion"]("mina")
        self.assertFalse(self.completed("mina"))

    def test_completed_courtship_beats_a_higher_affinity_promotion(self):
        for choice in (0, 1, 1, 0, 0):
            self.focus("maddie", choice)
        for day in (1, 3, 6):
            self.ns["vg_ambient_touch"]("yara", "terrace", day)
        self.focus("yara", 0)
        self.ns["vg_award_promotion"]("yara")
        self.ns["vg_ambient_touch"]("yara", "terrace", 7)
        self.focus("yara", 0)
        self.assertTrue(self.completed("maddie"))
        self.assertGreater(self.store.vg_affinity["yara"], self.store.vg_affinity["maddie"])
        self.assertEqual(["maddie"], self.finalists())

    def test_promotion_can_tip_an_unfinished_ending(self):
        for _ in range(2):
            self.focus("maddie", 0)
        self.focus("yara", 0)
        self.focus("yara", 1)
        self.assertEqual(["maddie"], self.finalists())
        self.ns["vg_award_promotion"]("yara")
        self.assertEqual(["yara"], self.finalists())
        self.assertFalse(self.completed("yara"))

    def test_promotion_alone_does_not_select_a_romantic_finalist(self):
        self.ns["vg_award_promotion"]("yara")
        self.assertEqual([], self.finalists())
        self.ns["vg_ambient_touch"]("yara", "terrace", 7)
        self.assertEqual(["yara"], self.finalists())

    def test_ambient_has_fresh_seven_day_scenes_in_each_area(self):
        groups = self.ns["VG_AMBIENT"]
        self.assertEqual({"garden", "terrace", "library", "gallery"}, set(groups))
        order = set(self.ns["VG_ORDER"])
        for area, chapters in groups.items():
            self.assertEqual(7, len(chapters), area)
            for chapter in chapters:
                self.assertTrue(chapter["opening"])
                self.assertIn(chapter["first"], order)
                self.assertIn(chapter["second"], order)
                self.assertEqual(2, len(chapter["options"]))

    def test_label_calls_and_jumps_resolve(self):
        source = "\n".join(p.read_text(encoding="utf-8") for p in GAME.glob("*.rpy"))
        labels = set(re.findall(r"^label (\w+):", source, flags=re.MULTILINE))
        targets = re.findall(r"^\s*(?:call|jump) (\w+)(?:\s+from\s+\w+)?$", source, flags=re.MULTILINE)
        for target in targets:
            self.assertIn(target, labels, target)


if __name__ == "__main__":
    unittest.main()
