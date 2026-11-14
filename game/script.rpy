# Velvet Gate: Seven Lanterns
# A standalone, text-first, seven-day Ren'Py game.
# Continuity follows ../canon/; scenes written here are game-only interpretations.

define vg_livia = Character("Livia", color="#c9b7ee", show_portrait="livia listening")
define vg_claire = Character("Claire", color="#e4c4a3", show_portrait="claire listening")
define vg_maddie = Character("Maddie", color="#efb5cf", show_portrait="maddie listening")
define vg_sydney = Character("Sydney", color="#9cc9de", show_portrait="sydney listening")
define vg_domitia = Character("Domitia", color="#e3ca9c", show_portrait="domitia listening")
define vg_ione = Character("Ione", color="#dddce9")
define vg_saba = Character("Saba", color="#d9b27b")
define vg_yara = Character("Yara", color="#b3d3bd", show_portrait="yara listening")
define vg_sylvie = Character("Sylvie", color="#baacd2")
define vg_nisha = Character("Nisha", color="#e6b49a", show_portrait="nisha listening")
define vg_valeria = Character("Valeria", color="#e6a4ad", show_portrait="valeria listening")
define vg_mina = Character("Mina", color="#badcde")
define vg_samira = Character("Samira", color="#c4bacb")
define vg_safiya = Character("Safiya", color="#bfcca7")

define vg_speakers = {
    "livia": vg_livia, "claire": vg_claire, "maddie": vg_maddie,
    "sydney": vg_sydney, "domitia": vg_domitia, "ione": vg_ione,
    "saba": vg_saba, "yara": vg_yara, "sylvie": vg_sylvie,
    "nisha": vg_nisha, "valeria": vg_valeria, "mina": vg_mina,
    "samira": vg_samira, "safiya": vg_safiya,
}

define vg_finale_portraits = {
    ("livia", "complete"): "livia fingertip_at_lip",
    ("livia", "incomplete"): "livia hands_on_hips",
    ("claire", "complete"): "claire affectionate",
    ("claire", "incomplete"): "claire happy",
    ("maddie", "complete"): "maddie happy",
    ("maddie", "incomplete"): "maddie affectionate",
    ("sydney", "complete"): "sydney affectionate",
    ("sydney", "incomplete"): "sydney listening",
    ("domitia", "complete"): "domitia affectionate",
    ("domitia", "incomplete"): "domitia held_look",
    ("yara", "complete"): "yara affectionate",
    ("yara", "incomplete"): "yara knowing_challenge",
    ("nisha", "complete"): "nisha affectionate",
    ("nisha", "incomplete"): "nisha happy",
    ("valeria", "complete"): "valeria happy",
    ("valeria", "incomplete"): "valeria affectionate",
}

# Environment art leaves the center clear for portraits and the lower area
# quiet enough for the dialogue window.
image vg atrium = "images/backgrounds/vg_atrium.png"
image vg study = "images/backgrounds/vg_study.png"
image vg terrace = "images/backgrounds/vg_terrace.png"
image vg garden = "images/backgrounds/vg_garden.png"
image vg library = "images/backgrounds/vg_library.png"
image vg music = "images/backgrounds/vg_music.png"
image vg chamber = "images/backgrounds/vg_chamber.png"
image vg evening = "images/backgrounds/vg_evening.png"

# Only affinity is a numeric relationship metric. All other values record story facts.
default vg_day = 1
default vg_affinity = {key: 0 for key in VG_ORDER}
default vg_visits = {key: 0 for key in VG_ORDER}
default vg_memories = {key: [] for key in VG_ORDER}
default vg_intent = {key: False for key in VG_ORDER}
default vg_mutual = {key: False for key in VG_ORDER}
default vg_current_key = "livia"
default vg_speaker = vg_livia
default vg_encounter = {}
default vg_opening = ""
default vg_visit_number = 0
default vg_first_option = ""
default vg_second_option = ""
default vg_choice_number = 0
default vg_line = ""
default vg_reply = ""
default vg_finalists = []
default vg_ending_data = {}
default vg_ending_kind = ""
default vg_ending_line = ""

screen vg_day_marker():
    zorder 80
    frame:
        xalign 0.02
        yalign 0.025
        background Solid("#11101bdb")
        padding (16, 11)
        vbox:
            spacing 2
            text "VELVET GATE" color "#ead5ad" bold True size 20
            text "Day [vg_day] of 7" color "#e2d8e9" size 16

screen vg_finalist_picker(keys, prompt="Several connections remain equally close. Whose company do you seek?", allow_back=False):
    modal True
    zorder 100
    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 650
        background Solid("#221b31f6")
        padding (30, 26)
        vbox:
            spacing 12
            text prompt color "#f4dfbc" size 23
            for key in keys:
                textbutton VG_NAMES[key] action Return(key)
            if allow_back:
                textbutton "Go back" action Return("")

label start:
    scene vg atrium
    with fade
    show screen vg_day_marker

    "VELVET GATE — SEVEN LANTERNS"
    "The sea breeze reaches the atrium before you do. The House has laid your place in the shade, with bread and water ready at your hand."
    "You are Domine, master of Velvet Gate. Livia, your Keeper, waits until you are seated before bringing Claire forward."
    vg_livia "You have seven afternoons free of urgent business, Domine. I took the liberty of preserving them." (show_portrait="livia explaining")
    "You can share a casual morning with the House each day, then give one woman your undivided afternoon. Seven days leave time for one close courtship, should it be returned."
    jump vg_day_loop

label vg_day_loop:
    if vg_day > 7:
        jump vg_finale
    call vg_morning
    call vg_casual_menu
    jump vg_focus_menu

label vg_morning:
    scene vg atrium
    with dissolve
    if vg_day == 1:
        "DAY ONE — Morning business"
        vg_claire "The Lower House is settled, Domine. I've set out the week's duties and left the music room free after the midday bell." (show_portrait="claire explaining")
        call vg_promotion_briefing from _call_vg_promotion_briefing
    elif vg_day == 2:
        "DAY TWO — Familiar company"
        vg_maddie "I said I'd be ready early. Sydney says my version of early is decorative." (show_portrait="maddie happy")
        vg_sydney "I said it with affection. Mostly." (show_portrait="sydney knowing_challenge")
    elif vg_day == 3:
        "DAY THREE — Things worth repeating"
        vg_yara "Nisha has suggested music with breakfast. I suggested we first survive breakfast." (show_portrait="yara unconvinced")
        vg_nisha "You could have said yes and saved us both time."
    elif vg_day == 4:
        "DAY FOUR — A spell of rain"
        "Rain closes the garden paths for an hour. The covered walks, however, belong to anyone willing to linger."
    elif vg_day == 5:
        "DAY FIVE — A gentler rhythm"
        vg_claire "The rooms are in order, and for once nobody is in a hurry. I almost distrust it." (show_portrait="claire knowing_challenge")
        vg_livia "Enjoy it before it becomes another duty." (show_portrait="livia knowing_challenge")
    elif vg_day == 6:
        "DAY SIX — What you remember"
        "A shared joke, a withheld confidence, a hand not quite withdrawn: the small events of the week have begun to accumulate."
    else:
        "DAY SEVEN — The final lantern"
        call vg_promotion_morning from _call_vg_promotion_morning
    return

label vg_focus_menu:
    scene vg atrium
    with dissolve
    "The afternoon is yours. Where will you spend it?"
    menu:
        "The Keeper's study — Livia, Claire":
            jump vg_pick_study
        "The terrace — Saba, Yara, Domitia, Valeria":
            jump vg_pick_terrace
        "The garden — Maddie, Sydney, Sylvie":
            jump vg_pick_garden
        "The library — Ione, Samira, Safiya":
            jump vg_pick_library
        "The music room — Nisha, Mina":
            jump vg_pick_music

label vg_pick_study:
    menu:
        "Livia — ask the Keeper to set her work aside":
            $ vg_current_key = "livia"
        "Claire — join the provisional Mistress of the Lower House":
            $ vg_current_key = "claire"
        "Look elsewhere":
            jump vg_focus_menu
    jump vg_focus_scene

label vg_pick_terrace:
    menu:
        "Saba — the shaded colonnade":
            $ vg_current_key = "saba"
        "Yara — the table overlooking the garden":
            $ vg_current_key = "yara"
        "Domitia — the sunlit gallery":
            $ vg_current_key = "domitia"
        "Valeria — the worktable of folded linens":
            $ vg_current_key = "valeria"
        "Look elsewhere":
            jump vg_focus_menu
    jump vg_focus_scene

label vg_pick_garden:
    menu:
        "Maddie — the flower beds":
            $ vg_current_key = "maddie"
        "Sydney — the blue-tiled bench":
            $ vg_current_key = "sydney"
        "Sylvie — the quiet arbor":
            $ vg_current_key = "sylvie"
        "Look elsewhere":
            jump vg_focus_menu
    jump vg_focus_scene

label vg_pick_library:
    menu:
        "Ione — the window seat":
            $ vg_current_key = "ione"
        "Samira — the reading alcove":
            $ vg_current_key = "samira"
        "Safiya — the copyist's table":
            $ vg_current_key = "safiya"
        "Look elsewhere":
            jump vg_focus_menu
    jump vg_focus_scene

label vg_pick_music:
    menu:
        "Nisha — the rehearsal floor":
            $ vg_current_key = "nisha"
        "Mina — the music shelves":
            $ vg_current_key = "mina"
        "Look elsewhere":
            jump vg_focus_menu
    jump vg_focus_scene

label vg_focus_scene:
    $ vg_visit_number = vg_visits[vg_current_key]
    $ vg_encounter = vg_get_chapter(vg_current_key, vg_visit_number)
    $ vg_opening = vg_encounter["opening"]
    $ vg_speaker = vg_speakers[vg_current_key]
    $ vg_line = vg_encounter["line"]
    $ vg_first_option = vg_encounter["choices"][0]["text"]
    $ vg_second_option = vg_encounter["choices"][1]["text"]

    if vg_current_key in ("livia", "claire"):
        scene vg study
    elif vg_current_key in ("saba", "yara", "domitia", "valeria"):
        scene vg terrace
    elif vg_current_key in ("maddie", "sydney", "sylvie"):
        scene vg garden
    elif vg_current_key in ("ione", "samira", "safiya"):
        scene vg library
    else:
        scene vg music
    with dissolve

    "[vg_opening]"
    vg_speaker "[vg_line]" (show_portrait=vg_encounter.get("portrait"))
    menu:
        "[vg_first_option]":
            $ vg_choice_number = 0
        "[vg_second_option]":
            $ vg_choice_number = 1
    $ vg_reply = vg_encounter["choices"][vg_choice_number]["reply"]
    vg_speaker "[vg_reply]" (
        show_portrait=vg_encounter["choices"][vg_choice_number].get("portrait", vg_encounter.get("portrait"))
    )
    $ vg_record_focus(vg_current_key, vg_visit_number, vg_choice_number, vg_encounter)

    if vg_mutual[vg_current_key] and vg_choice_number == 0:
        "For a moment, the conversation rests in a quiet understanding neither of you needs to announce."
    elif vg_choice_number == 0:
        "You leave with a particular moment to remember."
    else:
        "The afternoon passes pleasantly. Some things remain for another day."
    jump vg_end_day

label vg_end_day:
    if vg_day == 7:
        jump vg_finale
    scene vg evening
    with dissolve
    if vg_day == 3:
        vg_livia "I hope you are finding more than agreeable conversation, Domine. Agreement is the simplest thing to offer a master." (show_portrait="livia unconvinced")
    elif vg_day == 6:
        call vg_promotion_decision from _call_vg_promotion_decision
    else:
        "At dusk, the House settles into familiar sounds: sandals on stone, conversation in distant rooms, water in the garden."
    $ vg_day += 1
    jump vg_day_loop

label vg_finale:
    hide screen vg_day_marker
    scene vg evening
    with fade
    "The last afternoon slips toward dusk. Beyond the colonnade, the first lamps have been lit."
    $ vg_finalists = vg_best_connections(vg_affinity, vg_visits, vg_memories, vg_intent, vg_mutual)
    if not vg_finalists:
        vg_livia "A quiet week is not a wasted one, Domine. The House will still be here in the morning." (show_portrait="livia listening")
        "You leave the courtyard with the pleasant certainty that there are many people here you have yet to know."
        jump vg_credits
    if len(vg_finalists) > 1:
        "More than one connection holds the same place in your thoughts. The last choice belongs to you."
        call screen vg_finalist_picker(vg_finalists)
        $ vg_current_key = _return
    else:
        $ vg_current_key = vg_finalists[0]

    $ vg_speaker = vg_speakers[vg_current_key]
    $ vg_ending_data = VG_ENDINGS[vg_current_key]
    $ vg_ending_kind = "complete" if vg_is_complete(vg_current_key, vg_visits, vg_memories, vg_intent, vg_mutual) else "incomplete"
    $ vg_ending_line = vg_ending_data[vg_ending_kind]
    "[vg_ending_line]"
    if vg_current_key == "maddie" and "maddie_matching_dresses" in vg_memories["maddie"]:
        "You ask what Sydney did when she saw the matching dresses. Maddie's smile comes before her answer."
        vg_maddie "You remember exactly where I stopped. I was hoping you'd ask again." (show_portrait="maddie happy")
    if VG_PROMOTION_MEMORY in vg_memories[vg_current_key]:
        $ vg_line = VG_PROMOTION_STORIES[vg_current_key]["recall"]
        vg_speaker "[vg_line]"
    $ vg_line = vg_ending_data[vg_ending_kind + "_speech"]
    vg_speaker "[vg_line]" (show_portrait=vg_finale_portraits.get((vg_current_key, vg_ending_kind)))
    if vg_ending_kind == "complete":
        "The promise is mutual. This week closes one chapter, but not the bond you have chosen to begin."
    else:
        "There is warmth here, perhaps the beginning of something. Seven days cannot tell the whole story."

    if vg_ending_data["memory"] in vg_memories[vg_current_key]:
        $ vg_ending_line = vg_ending_data["recall"]
        "[vg_ending_line]"
    elif vg_ending_data["alternate_memory"] in vg_memories[vg_current_key]:
        $ vg_ending_line = vg_ending_data["alternate_recall"]
        "[vg_ending_line]"
    jump vg_credits

label vg_credits:
    "VELVET GATE — SEVEN LANTERNS"
    "An end to this week. Not an end to the House."
    "Replay to discover another woman's story, or choose differently to see a different kind of farewell."
    return
