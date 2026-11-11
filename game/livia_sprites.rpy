image livia listening = "images/livia/livia_01_listening_neutral.png"
image livia explaining = "images/livia/livia_02_explaining_neutral_speaking.png"
image livia considering = "images/livia/livia_03_considering_worried.png"
image livia unconvinced = "images/livia/livia_04_unconvinced_angry.png"
image livia knowing_challenge = "images/livia/livia_06_knowing_challenge_amused.png"
image livia hands_on_hips = "images/livia/livia_09_hands_high_on_hips_happy.png"
image livia fingertip_at_lip = "images/livia/livia_12_fingertip_at_lip_affectionate.png"

transform vg_dialogue_portrait:
    xalign 0.5
    yalign 1.0
    zoom 0.62

# Claire, Maddie, and Yara use full-body source art. Keep those images near
# native resolution and anchor them from the top so their upper-body framing
# matches Livia without changing or re-encoding the PNG files.
transform vg_fullbody_dialogue_portrait:
    xalign 0.5
    ypos 140
    yanchor 0.0
    zoom 1.15
