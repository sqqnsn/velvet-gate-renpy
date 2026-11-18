# One private advancement in the seven-day demo.

default vg_promoted = None
default vg_heard_livia = False
default vg_heard_claire = False
default vg_promotion_name = ""
default vg_nominee = ""

init python:
    VG_PROMOTION_MEMORY = "promotion_recognition"
    VG_PROMOTION_BONUS = 2

    # Destination tiers. Claire has a provisional office and Livia is outside the ladder.
    VG_PROMOTION_TIERS = {
        2: ("sylvie", "nisha", "valeria", "mina", "samira", "safiya"),
        3: ("maddie", "sydney", "domitia", "ione", "saba", "yara"),
    }

    VG_PROMOTION_STORIES = {
        "sylvie": {
            "morning": "Sylvie has set the lamps in a row just beyond the reach of the morning draft. She watches the flame of the smallest one settle.",
            "greeting": "I like this hour, Domine. The whole room is still deciding how bright to be.",
            "recall": "I thought about what it took for you to see me in a room full of people. I was glad you did.",
        },
        "nisha": {
            "morning": "Nisha moves between the water and the wine with the economy of someone who has found the right count. Her fingers keep the beat against the empty tray.",
            "greeting": "There's a rhythm to this as well, Domine. It took me exactly three mistakes to find it.",
            "recall": "I was pleased you thought of me for the work. I wanted to tell you myself when the room was quiet.",
        },
        "valeria": {
            "morning": "Domitia pauses at the atrium linen long enough to examine the corners. She gives Valeria a single approving nod. Valeria's smile is a fraction wider when she turns to you.",
            "greeting": "The fourth corner is my favorite, Domine. It's the one people only inspect when they expect to catch you out.",
            "recall": "I wear a plain clasp surprisingly well, as it turns out. I wanted you to know your decision pleased me.",
        },
        "mina": {
            "morning": "Sydney comes by to help as usual, takes one look at the water and the cups Mina has laid out, and leaves her to it. Mina straightens the clasp at her shoulder.",
            "greeting": "I knew exactly what was mine to do this morning, Domine. It felt good.",
            "recall": "When Livia told me you'd chosen me, I thought of all the little things I hoped you'd seen. I'm glad you did.",
        },
        "samira": {
            "morning": "Samira has made the lamps easy to reach from your place. She waits just beyond their light before coming forward.",
            "greeting": "The atrium is quietest at this hour, Domine. I'm glad to be the one who makes it ready.",
            "recall": "I have kept the moment Livia told me to myself. I wanted you to know that I treasure it.",
        },
        "safiya": {
            "morning": "Safiya has set out the cups in the order you use them. The little tablet beside the tray gives Claire a clear account of what is ready for the next morning.",
            "greeting": "I watched which vessel you reached for first, Domine. The rest of the order followed from that.",
            "recall": "I like that you trusted me with something useful. I've been thinking about it since last night.",
        },
        "maddie": {
            "morning": "Maddie has arranged the clean linen and set the lamp where its light falls just short of the door. She glances at the fold one last time, then catches your eye and grins.",
            "greeting": "It's ready, Domine. I managed to leave it alone after the third adjustment. That's practically restraint.",
            "recall": "I keep trying to guess which moment made you decide I could do it. I really want to hear your answer someday.",
        },
        "sydney": {
            "morning": "Sydney has already drawn the screen against the draft. She notices you checking the shutter and allows herself a small, satisfied smile.",
            "greeting": "I thought you might want the light and a little less of the sea air, Domine.",
            "recall": "You saw the quiet work. I usually count on people noticing the clever part first. It meant something that you saw both.",
        },
        "domitia": {
            "morning": "The folded linen is exactly where Livia asked for it. Domitia gives her a precise account of the work, then turns her full attention to you.",
            "greeting": "There is considerable satisfaction in being trusted to get a small thing exactly right, Domine.",
            "recall": "Your confidence is an exacting gift. I was pleased to receive it, and I wanted to say so in person.",
        },
        "ione": {
            "morning": "Ione's silver-white hair catches the light as she checks the trimmed wicks. Her own cup stands beside the linen, half finished and still warm.",
            "greeting": "I found a good pace for the work, Domine. There was even time to drink my tea.",
            "recall": "Livia told me what you had entrusted to me. I carried the thought with me all morning. It was a quiet sort of happiness.",
        },
        "saba": {
            "morning": "Saba has moved the lamp to let the fresh linen catch the morning air. She finishes the last fold with steady hands, then turns to you with a smile.",
            "greeting": "The room has a gentler light at this hour, Domine. I thought you might enjoy it.",
            "recall": "There is a particular pleasure in being trusted to use one's judgment. I wanted to thank you for giving me that.",
        },
        "yara": {
            "morning": "Yara has kept the lamps low, just as you like them in the morning. She sets the last folded cloth in place as you arrive.",
            "greeting": "Livia left the level to my judgment, Domine. I remembered what you preferred.",
            "recall": "I liked having your confidence this morning. I was hoping you might spare a little more of your afternoon for me, too.",
        },
    }

    def vg_award_promotion(key):
        state = renpy.store
        if state.vg_promoted is not None or key not in VG_PROMOTION_STORIES:
            return
        state.vg_promoted = key
        state.vg_affinity[key] += VG_PROMOTION_BONUS
        state.vg_memories[key].append(VG_PROMOTION_MEMORY)

label vg_promotion_briefing:
    "Claire finishes her report. Livia waits until the last footsteps have receded along the colonnade."
    vg_livia "A small matter for the three of us, Domine. There is room to advance one woman this week. An Initiate could take a regular atrium post, or a First Witness could be trusted with chamber service." (show_portrait="livia explaining")
    vg_claire "You'll see them at their usual work. I can tell you how they get on in the Lower House when the time comes."
    vg_livia "I'll ask you for a name at the end of the week." (show_portrait="livia listening")
    return

label vg_promotion_decision:
    if vg_promoted is not None:
        return
    scene vg study
    with dissolve
    "At dusk, your place in Livia's study is ready. Claire sets her tablet aside as soon as you enter."
    vg_livia "Have you settled on someone, Domine?" (show_portrait="livia considering")
    jump vg_promotion_review

label vg_promotion_review:
    menu:
        "Hear what Livia has noticed." if not vg_heard_livia:
            vg_livia "Saba knows when a room needs quiet. Domitia has learned to bring a correction privately. I would trust either of them with chamber work." (show_portrait="livia explaining")
            vg_livia "Among the Initiates, Samira takes particular care over the things people seldom see. Sylvie has been coming early to trim the atrium lamps." (show_portrait="livia explaining")
            $ vg_heard_livia = True
            jump vg_promotion_review
        "Hear what Claire has noticed." if not vg_heard_claire:
            vg_claire "Yara has been finding room for Nisha's practice for weeks, Domine. She always asks in time for me to arrange it."
            vg_claire "Mina catches little things before anyone else has to. And Nisha comes back after practice to set the room right. Both would manage a regular post very well."
            $ vg_heard_claire = True
            jump vg_promotion_review
        "Name the woman who advances.":
            jump vg_choose_promotion

label vg_choose_promotion:
    menu:
        "Advance a Tier 1 Initiate to House Servant.":
            call screen vg_finalist_picker(VG_PROMOTION_TIERS[2], "Who will take the Tier 2 atrium post?", True)
        "Advance a Tier 2 First Witness to Chamber Attendant.":
            call screen vg_finalist_picker(VG_PROMOTION_TIERS[3], "Who will take the Tier 3 chamber assignment?", True)
        "Return to Livia and Claire.":
            jump vg_promotion_review
    $ vg_nominee = _return
    if not vg_nominee:
        jump vg_choose_promotion
    $ vg_award_promotion(vg_nominee)
    $ vg_promotion_name = VG_NAMES[vg_promoted]
    "Livia marks your choice in her ledger. Claire makes a note of the morning arrangements."
    vg_livia "I'll give [vg_promotion_name] your decision in private, Domine." (show_portrait="livia listening")
    return

label vg_promotion_morning:
    if vg_promoted is None:
        return
    if vg_promoted == "samira":
        "Your place at the morning audience is ready."
    elif vg_promoted in VG_PROMOTION_TIERS[2]:
        "Your place at the morning audience is ready. The new House Servant comes forward with a plain clasp at her shoulder."
    else:
        scene vg chamber
        with dissolve
        "In a chamber off the palace service passage, Livia has entrusted the morning lamps and linen to the new Chamber Attendant. The room is ready as you arrive."
    $ vg_opening = VG_PROMOTION_STORIES[vg_promoted]["morning"]
    $ vg_line = VG_PROMOTION_STORIES[vg_promoted]["greeting"]
    $ vg_speaker = vg_speakers[vg_promoted]
    "[vg_opening]"
    "You acknowledge her work and give her a moment to answer."
    if vg_promoted == "samira":
        vg_speaker "[vg_line]" (show_portrait="samira promoted")
    else:
        vg_speaker "[vg_line]"
    return
