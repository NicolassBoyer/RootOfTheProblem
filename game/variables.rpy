# Sound Effects for Characters
init python:
    preferences.text_cps = 40

    def vina_talking(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/SFX/Voices/Vina Voice.mp3", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def shadow_talking(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/SFX/Voices/ShadowEdge12 Voice.mp3", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def nor_talking(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/SFX/Voices/Nor Voice.mp3", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


# Characters
define mc = Character("[mc_name]")
define v = Character("Vina", callback=vina_talking, color="#4b65ad")
define n = Character("Nor", callback=nor_talking, color="#9d471f")
define se = Character("ShadowEdge12", callback=shadow_talking, color="#736568")
define s = Character("Superbug", color="#a19f13")
define mt = Character("Mother Tree", color="#a3ccd8")

define unknown = Character("???", callback=vina_talking, color="#5195c0")

# music
define music_ambience = "audio/music/AMBIENCE 1.mp3"
define music_ambience2 = "audio/music/AMBIENCE 2.mp3"
define music_character_creation = "audio/music/CHARACTER CREATION THEME.mp3"
define music_final_boss = "audio/music/FINAL BOSS THEME.mp3"
define music_good_ending = "audio/music/PACIFIST ENDING THEME.mp3"
define music_attack_ending = "audio/music/GOOD ENDING MELODY.mp3"
define music_infirmary = "audio/music/INFIRMARY + MAIN ROOM THEME.mp3"
define music_computer = "audio/music/ABANDONED LAB THEME.mp3"

define sound_click_slow = "audio/SFX/Button Slow.mp3"
define sound_click_normal = "audio/SFX/Button Normal.mp3"
define sound_click_fast = "audio/SFX/Button Fast.mp3"
define sound_clicks = [sound_click_slow, sound_click_normal, sound_click_fast]

define sound_action_button = "audio/SFX/RPG Fight/action button click.mp3"
define sound_boss_screech = "audio/SFX/RPG Fight/boss screech.mp3"
define sound_damage1 = "audio/SFX/RPG Fight/damage sound 1.mp3"
define sound_damage2 = "audio/SFX/RPG Fight/damage sound 2.mp3"
define sound_machine_gun = "audio/SFX/RPG Fight/machine gun.mp3"
define sound_whip = "audio/SFX/RPG Fight/whip.mp3"

# Image Effects
define hover_effect = im.Flip("click temp.png", vertical=True)
define scale_effect = im.FactorScale("click temp.png", 1.2)
define tint_effect = im.MatrixColor(
    "click temp.png",
    im.matrix.tint(1, 0.5, 1)
)

# Images
define icon_close = "exit button.png"
define icon_folder = "computer files.png"
define icon_checker = "file pic.png"
define icon_mug = "mug pic.png"
define icon_mug_egg = "mug easter egg.png"
define icon_paint = "mspaint icon.png"
define icon_text = "txt icon.png"
define icon_solitaire = "solitare icon.png"
define icon_trash = "computer trash.png"
define icon_virus = "virus icon.png"
define icon_webpage = "webpage icon.png"

define icon_close_mail = "mail sus.png"
define icon_open_mail = "open mail.png"

define app_folder = "file explorer.png"
define app_paint = "mspaint.png"
define app_real = "error for real.PNG"
define app_text = "txt page.png"
define app_web = "webpage.png"

define app_report = "report.png"
define app_report_redacted = "report redacted.png"

transform edge_position:
    xalign 0.25
    yalign 1.0



# Transforms
transform left_to_right:
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat
