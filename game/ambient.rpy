# Optional morning group scenes. Every day offers a fresh vignette in each area.
# An ambient interaction can make a favorable impression, but never replaces
# a private conversation or creates a completed romance by itself.

default vg_ambient_location = "garden"
default vg_ambient = {}
default vg_ambient_opening = ""
default vg_ambient_speaker1 = vg_livia
default vg_ambient_speaker2 = vg_claire
default vg_ambient_text1 = ""
default vg_ambient_text2 = ""
default vg_ambient_option1 = ""
default vg_ambient_option2 = ""
default vg_ambient_reply = ""

init python:
    def A(opening, first, first_line, second, second_line, option1, reply1, option2, reply2):
        return {
            "opening": opening,
            "first": first, "first_line": first_line,
            "second": second, "second_line": second_line,
            "options": ((option1, reply1), (option2, reply2)),
        }

    VG_AMBIENT = {
        "garden": [
            A("Maddie is balancing flowers on a low wall while Sydney supplies unsolicited commentary.",
              "maddie", "This is a floral arrangement, not a competitive sport.", "sydney", "Then why have you asked for a score twice?",
              "Ask Maddie about her favorite bloom.", "The tiny white ones. I know, shocking that I chose something subtle.",
              "Ask Sydney if she always teases an old friend.", "Only when I know she can give it back."),
            A("Sylvie has come to help Maddie with the garden cuttings. Sydney hovers just long enough to see they are comfortable.",
              "sylvie", "I prefer the flowers that look a little wild.", "maddie", "I was going to straighten those. Okay, I hear myself now.",
              "Ask Sylvie which stem she wants to keep.", "This one. It looks like it's thinking about leaving.",
              "Praise Maddie for letting the arrangement breathe.", "I'm growing as a person. Against all odds."),
            A("Mina is explaining a newly arranged tray to Sydney, who is making a conspicuous effort not to interrupt.",
              "mina", "I put the cups here because the handles won't knock together.", "sydney", "And I am discovering the value of simply listening.",
              "Tell Mina the solution is clever.", "Thank you. I like solving little problems.",
              "Thank Sydney for letting Mina make the call.", "It's her call to make. I'm learning."),
            A("Rain has left the garden smelling of damp leaves. Maddie and Sylvie are taking shelter under the arbor.",
              "maddie", "I thought she was avoiding me. Turns out she just likes the rain.", "sylvie", "And she talks through it beautifully.",
              "Ask Sylvie what she likes about the rain.", "It lets everything become quiet without feeling lonely.",
              "Ask Maddie if she enjoys a slower morning.", "I'm trying. I've only checked the clouds six times."),
            A("Sydney and Maddie are sorting a small pile of ribbons for ordinary House use. Their old social shorthand does most of the work.",
              "sydney", "That's the color you always choose when nervous.", "maddie", "I don't have a nervous color! I have several.",
              "Ask Sydney for the story behind the joke.", "She once color-coded an entire afternoon to avoid admitting she cared.",
              "Ask Maddie to pick one just because she likes it.", "Oh. That one. No explanation needed."),
            A("Maddie sets the last cuttings in water while Sylvie reads nearby. Neither seems inclined to improve the silence.",
              "sylvie", "She's getting better at not asking if I'm all right every minute.", "maddie", "I'm down to every five minutes. A triumph.",
              "Ask Sylvie if she'd like more quiet company.", "Yes. I think that would be nice.",
              "Tell Maddie her patience shows.", "You noticed? Wait, I'm doing it again, aren't I?"),
            A("For the last morning, the garden path has been swept but not fussed over. Sydney hands Maddie a sprig of greenery.",
              "maddie", "I was about to make everything perfect. Then I remembered we get to enjoy it too.", "sydney", "I've been trying to tell her for years.",
              "Tell Maddie the garden feels lived in.", "That's my favorite compliment anyone's given it.",
              "Ask Sydney whether she'll enjoy the evening too.", "I intend to. Possibly without organizing anyone."),
        ],
        "terrace": [
            A("Yara and Saba are sharing fruit while Nisha explains a rehearsal with extravagant gestures.",
              "nisha", "And then I turned, and that was when I knew it worked!", "yara", "Yes. I know because you have reached the ending three times.",
              "Ask Nisha to describe the feeling rather than the steps.", "Like finding the right word without searching for it.",
              "Ask Yara for her own account of the story.", "It was good. There, the entire report in three words."),
            A("Claire checks the shaded terrace, but Saba has already made a comfortable space for Safiya.",
              "claire", "I see my arrangements are being competently improved.", "saba", "Only made a little warmer, Claire.",
              "Compliment Claire's willingness to share the work.", "I am learning that delegation needn't be an admission of defeat.",
              "Thank Saba for thinking of Safiya.", "Comfort is usually made of small arrangements."),
            A("Nisha has drawn a little diagram on the tabletop. Yara studies it with an expression of severe skepticism.",
              "yara", "If this is an explanation of yesterday's dance, it requires fewer arrows.", "nisha", "It requires more imagination, Yara.",
              "Ask Yara to improve the diagram.", "I would begin by locating the feet.",
              "Ask Nisha to demonstrate with two fingers.", "There! Now you see why the arrows are essential."),
            A("Under the covered terrace, Saba holds a dry cloth while Claire moves the tea away from the rain.",
              "saba", "We have rescued the tea. The sky may keep the flowers.", "claire", "A very diplomatic division of responsibilities.",
              "Ask Saba to stay for a cup.", "With pleasure. I have nowhere urgent to be.",
              "Offer Claire the first dry chair.", "A gentlemanly impulse. I accept, darling."),
            A("Safiya brings a corrected note for Saba, who waits until she has finished explaining it.",
              "safiya", "The total was sound. My assumption was not.", "saba", "That is why you checked it. A worthwhile morning.",
              "Ask Safiya what she learned.", "Not to trust an elegant theory over a plain fact.",
              "Thank Saba for encouraging questions.", "She asks excellent ones. I only make room for them."),
            A("Yara is helping Claire lay out a modest supper arrangement, then pauses to admire the light across the floor.",
              "claire", "I believe we have finished. Yara, are you about to invent another task?", "yara", "I was about to enjoy a moment of peace. Shocking, I know.",
              "Invite Yara to enjoy the view.", "Now that is an assignment I can accept.",
              "Tell Claire the arrangement is sufficient.", "You are entirely right. How refreshing."),
            A("On the seventh morning, Saba and Yara have taken a quiet seat as Nisha finishes humming by the rail.",
              "saba", "The House has had a good week.", "yara", "No miracles. Just people making room for one another.",
              "Ask Saba what she'll remember.", "The moments nobody thought were important enough to count.",
              "Ask Yara what makes her smile.", "At present? The fact that you asked me here rather than to report something."),
        ],
        "library": [
            A("Safiya reviews a short note while Ione reads beside the window. The room is peaceful rather than hushed by rule.",
              "safiya", "There is a contradiction here. A useful one.", "ione", "Some contradictions are simply invitations to look more closely.",
              "Ask Safiya to explain her question.", "Happily. It begins with a word everyone assumes has only one meaning.",
              "Ask Ione which passage caught her eye.", "A gentle one. I can read it aloud."),
            A("Samira joins Ione with a small folded page. Neither seems in a rush to turn private aspiration into public ceremony.",
              "samira", "I like the discipline of a careful fold. It does not require an ornament to mean something.", "ione", "And it needn't require you to disappear.",
              "Ask Samira what the fold symbolizes to her.", "A choice I hope to make well, when it is mine to make.",
              "Ask Ione what she hopes Samira learns.", "That devotion can leave room for joy."),
            A("Safiya and Ione have disagreed about the ending of a story. They seem delighted to discover it.",
              "ione", "I thought it ended in mercy.", "safiya", "I thought it ended in courage. Perhaps both are possible.",
              "Ask Ione to defend her reading.", "Because no one was required to earn kindness first.",
              "Ask Safiya to defend hers.", "Because someone chose to act when it was difficult."),
            A("The rain has driven Sylvie into the library. Safiya makes room for her without comment.",
              "sylvie", "Books sound different when it's raining.", "safiya", "I think the rain gives every sentence a second rhythm.",
              "Ask Sylvie which book she brought.", "Something sad, but only in a beautiful way.",
              "Ask Safiya whether she'd read aloud.", "Only if everyone wishes it. I can be persuaded."),
            A("Samira and Safiya compare notes at the same table, but the conversation has wandered away from duty.",
              "samira", "I prefer things that can be kept private.", "safiya", "I prefer questions that become better when shared.",
              "Ask Samira what she'd choose to share.", "A favorite sentence. Perhaps with one person I trusted.",
              "Ask Safiya whether privacy can help scholarship.", "Certainly. A thought sometimes needs quiet before debate."),
            A("Ione and Samira have set out cups of tea before opening their books. Both look rather pleased with themselves.",
              "ione", "I remembered to drink it while warm.", "samira", "I believe this may count as progress for both of us.",
              "Share Ione's small celebration.", "A very small celebration, yes. I like it.",
              "Ask Samira to recommend something to read.", "Something short, perhaps. With room to think afterward."),
            A("On the seventh morning, Safiya closes a volume and Ione draws back the curtain to let in the light.",
              "safiya", "An ending can still leave a question worth keeping.", "ione", "Perhaps it can also leave someone less alone.",
              "Ask Safiya what question she'll keep.", "What makes a good life, beyond a well-ordered one?",
              "Ask Ione what she'll remember.", "Kindness that did not ask me to disappear."),
        ],
        "gallery": [
            A("Domitia observes Valeria inspecting a folded cloth. Neither woman has suggested it is a contest, which is unusual.",
              "domitia", "A precise fold is a good beginning, not a claim to authority.", "valeria", "How fortunate. I was considering a career in immaculate corners.",
              "Ask Domitia if she finds Valeria's progress encouraging.", "I do. I should say so more often.",
              "Ask Valeria whether she's pleased with the work.", "Very. It's possible to be proud without being unbearable."),
            A("Claire has asked Mina to bring an inventory, and Mina has marked a small discrepancy herself.",
              "mina", "I thought it was worth mentioning before someone asked.", "claire", "It certainly was. Thank you for the initiative.",
              "Ask Mina what she noticed.", "The same item had been counted twice. I checked to be certain.",
              "Thank Claire for listening to the correction.", "Of course. An office does not make me incapable of error."),
            A("Valeria offers Domitia a revised work list. Domitia reads it slowly, then hands it back without criticism.",
              "valeria", "Is silence a compliment today?", "domitia", "It is an opportunity to enjoy having done something well.",
              "Tell Valeria the restraint suits her.", "I am informed it is more becoming than my sharpest remarks.",
              "Tell Domitia the praise was well judged.", "Excess praise diminishes its value. This was sufficient."),
            A("During the rain, Claire and Domitia take shelter by the gallery arch. An argument over the placement of a bench has ended in laughter.",
              "claire", "We have compromised. A truly historic occasion.", "domitia", "I accepted the more sensible arrangement. Let us not exaggerate.",
              "Ask Claire how she managed the negotiation.", "By permitting both of us to believe we had won.",
              "Ask Domitia to admit the bench looks comfortable.", "It does. Your insistence is unbecoming."),
            A("Mina has delivered the week's neatest stack of copied notes. Valeria catches herself beginning to critique it.",
              "valeria", "I was going to mention one crooked margin. I have decided I like the rest better.", "mina", "Thank you. I can fix it later, if necessary.",
              "Ask Valeria what changed her mind.", "I discovered I could be right and still be unkind.",
              "Thank Mina for her careful work.", "I'm happy it helps."),
            A("Domitia places her earned red glove aside while speaking to Claire about the last evening's arrangements.",
              "domitia", "The rules are clear. No woman has authority simply because she wishes to exercise it.", "claire", "An excellent reminder, and one I take personally.",
              "Ask Domitia what careful authority requires.", "Judgment, restraint, and a willingness to be corrected.",
              "Ask Claire how her responsibilities feel today.", "Lighter because they are shared, not because they matter less."),
            A("The gallery is ready for its quiet evening. Valeria checks one last detail while Claire watches, amused.",
              "valeria", "I believe I have found a flaw. I also believe I can live with it.", "claire", "Then the week has taught us something after all.",
              "Ask Valeria to leave the flaw as a reminder.", "A very small rebellion against perfection. I might enjoy it.",
              "Invite Claire to admire what everyone accomplished.", "With pleasure. It has become a room people can inhabit."),
        ],
    }

    def vg_ambient_touch(key, location, day_number):
        renpy.store.vg_affinity[key] += 1
        memory = "ambient_%s_day_%s" % (location, day_number)
        if memory not in renpy.store.vg_memories[key]:
            renpy.store.vg_memories[key].append(memory)

label vg_casual_menu:
    "The morning offers a chance to share an easy conversation before choosing how to spend the afternoon."
    menu:
        "Visit the garden group":
            $ vg_ambient_location = "garden"
        "Join the terrace conversation":
            $ vg_ambient_location = "terrace"
        "Spend a while in the library":
            $ vg_ambient_location = "library"
        "Pass through the gallery":
            $ vg_ambient_location = "gallery"
        "Keep the morning to yourself":
            "You take a little time alone. No one insists that every hour be shared."
            return
    call vg_casual_play from _call_vg_casual_play
    return

label vg_casual_play:
    $ vg_ambient = VG_AMBIENT[vg_ambient_location][vg_day - 1]
    $ vg_ambient_opening = vg_ambient["opening"]
    $ vg_ambient_speaker1 = vg_speakers[vg_ambient["first"]]
    $ vg_ambient_speaker2 = vg_speakers[vg_ambient["second"]]
    $ vg_ambient_text1 = vg_ambient["first_line"]
    $ vg_ambient_text2 = vg_ambient["second_line"]
    $ vg_ambient_option1 = vg_ambient["options"][0][0]
    $ vg_ambient_option2 = vg_ambient["options"][1][0]
    if vg_ambient_location == "garden":
        scene vg garden
    elif vg_ambient_location == "terrace":
        scene vg terrace
    elif vg_ambient_location == "library":
        scene vg library
    else:
        scene vg study
    with dissolve
    "[vg_ambient_opening]"
    vg_ambient_speaker1 "[vg_ambient_text1]"
    vg_ambient_speaker2 "[vg_ambient_text2]"
    menu:
        "[vg_ambient_option1]":
            $ vg_ambient_reply = vg_ambient["options"][0][1]
            $ vg_ambient_touch(vg_ambient["first"], vg_ambient_location, vg_day)
            vg_ambient_speaker1 "[vg_ambient_reply]"
        "[vg_ambient_option2]":
            $ vg_ambient_reply = vg_ambient["options"][1][1]
            $ vg_ambient_touch(vg_ambient["second"], vg_ambient_location, vg_day)
            vg_ambient_speaker2 "[vg_ambient_reply]"
    return
