"""Static story-logic tests that run without an installed Ren'Py SDK.

They compile the normal Python blocks embedded in .rpy files and exercise the
same state functions that the Ren'Py script calls. They do not replace lint or
a playthrough in Ren'Py itself.
"""

import re
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
    order = namespace["VG_ORDER"]
    namespace["store"] = types.SimpleNamespace(
        vg_affinity={key: 0 for key in order},
        vg_visits={key: 0 for key in order},
        vg_memories={key: [] for key in order},
        vg_intent={key: False for key in order},
        vg_mutual={key: False for key in order},
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
        best = self.ns["vg_best_connections"]
        self.assertEqual([], best(self.store.vg_affinity, self.store.vg_visits, self.store.vg_memories))
        self.focus("maddie", 0)
        self.focus("sydney", 0)
        self.assertEqual(["maddie", "sydney"], best(
            self.store.vg_affinity, self.store.vg_visits, self.store.vg_memories))
        self.focus("sydney", 1)
        self.assertEqual(["sydney"], best(
            self.store.vg_affinity, self.store.vg_visits, self.store.vg_memories))

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
