init:
    # Settings menu
    screen bangok_modsettings tag smallscreen2:
        modal True
        window id "bangok_modsettings" at popup2:
            style "smallwindow"

            vbox:
                align (0.5, 0.5)
                spacing 10

                if persistent.nsfwtoggle:
                    text "Fetishes:":
                        align (0.5, 0.5)

                    text "If you do not know what an option means, leave it deselected (or look it up at your own peril)."

                    null

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_watersports"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "Watersports"

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_inflation"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "Inflation"

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_knot"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "Knotting"

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_cloacas"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "Cloacas"

                    text "Development":
                        align (0.5, 0.5)

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_dev"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "In-Development Scenes"

                    if persistent.bangok_dev == True:
                        text "In-Development scenes may not have conclusions, and {i}will{/i} have paths leading to crashes."

                else:
                    text "This mod's content is primarily":
                        align (0.5,0.5)
                    text "---- Not-Safe-For-Work ----":
                        align (0.5,0.5)
                    text "Re-enable NSFW scenes or uninstall the mod.":
                        align (0.5,0.5)
                    text "This mod does not guarantee all NSFW content is inaccessible\nwhile NSFW scenes are disabled, though an attempt was made.":
                        align (0.5,0.5)

            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("my_cool_screen"), Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button

    # Locations
    image bangok_four_bryce1_apartment night = "bg/in/apts/pad_night.png"
    image bangok_four_bryce1_apartment night ceiling = "bg/in/apts/pad_night_ceil.png"


    image bangok_four_xipsum_bedroom normal = "bg/in/apts/ipsum_bedroom.png"
    image bangok_four_xipsum_bedroom_bed = "bg/in/apts/ipsum_bedroom_bed.png"
    image bangok_four_xipsum_bedroom ceiling = "bg/in/apts/ipsum_bedroom_ceiling.png"

    image bangok_four_xsebastian_cave2_dk = im.Recolor("bg/in/cave2_dk.png", 70, 70, 100, 255)

    image bangok_four_library night = im.Recolor("bg/in/bangok_library_night.png", 70, 70, 100, 255)
    image bangok_four_library outside night = im.Recolor("bg/out/town/town5.jpg", 60, 70, 100, 255)


    # CGs
    image bangok_four_xipsum_afterglow = "cg/lorem-x-ipsum_purpleroom.png"

    # People
    image anna bangok blush = "cr/anna_blush.png"
    image anna bangok blush flip = im.Flip("cr/anna_blush.png", horizontal = True)
    image anna bangok orgasm = "cr/anna_orgasm.png"
    image anna bangok orgasm flip = im.Flip("cr/anna_orgasm.png", horizontal = True)
    image anna bangok blushpalm = "cr/anna_blushpalm.png"
    image anna bangok blushpalm flip = im.Flip("cr/anna_blushpalm.png", horizontal = True)
    image anna bangok lipbite = "cr/anna_lipbite.png"
    image anna bangok lipbite flip = im.Flip("cr/anna_lipbite.png", horizontal = True)


    image bangok_four_bryce_underside_large dk = im.Recolor("cr/bryce_underside_large.png", 70, 70, 100, 255)
    image bangok_four_bryce_underside_large dk flip = im.Recolor(im.Flip("cr/bryce_underside_large.png",horizontal=True), 70, 70, 100, 255)

    image lorem bangok normal = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_normal.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok normal flip = im.Flip(renpy.display.image.ImageReference('lorem bangok normal'),horizontal=True)
    image lorem bangok happy = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_happy.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok happy flip = im.Flip(renpy.display.image.ImageReference('lorem bangok happy'),horizontal=True)
    image lorem bangok sad = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_sad.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok sad flip = im.Flip(renpy.display.image.ImageReference('lorem bangok sad'),horizontal=True)
    image lorem bangok relieved = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_relieved.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok relieved flip = im.Flip(renpy.display.image.ImageReference('lorem bangok relieved'),horizontal=True)
    image lorem bangok shy = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_shy.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok shy flip = im.Flip(renpy.display.image.ImageReference('lorem bangok shy'),horizontal=True)
    image lorem bangok think = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_think.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok think flip = im.Flip('lorem bangok think',horizontal=True)

    image lorem bangok hidepeek = "cr/lorem_bangok_hidepeek.png"
    image lorem bangok hidepeek flip = im.Flip("cr/lorem_bangok_hidepeek.png",horizontal=True)

    image ipsum normal bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_normal.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum normal flip bangok = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok'),horizontal=True)
    image ipsum happy bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_happy.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum happy flip bangok = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok'),horizontal=True)
    image ipsum sad bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum sad flip bangok = im.Flip(renpy.display.image.ImageReference('ipsum sad bangok'),horizontal=True)
    image ipsum think bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_think.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum think flip bangok = im.Flip(renpy.display.image.ImageReference('ipsum think bangok'),horizontal=True)

    image sebastian normal b dk = im.Recolor("cr/sebastian_normal_b.png", 70, 70, 100, 255)
    image sebastian shy dk = im.Recolor("cr/sebastian_shy.png", 70, 70, 100, 255)
    image sebastian shy b dk = im.Recolor("cr/sebastian_shy_b.png", 70, 70, 100, 255)
    image sebastian shy b flip dk = im.Recolor(im.Flip("cr/sebastian_shy_b.png", horizontal=True), 70, 70, 100, 255)
    image sebastian drop dk = im.Recolor("cr/sebastian_drop.png", 70, 70, 100, 255)
    image sebastian drop b dk = im.Recolor("cr/sebastian_drop_b.png", 70, 70, 100, 255)
    image sebastian drop b flip dk = im.Recolor(im.Flip("cr/sebastian_drop_b.png", horizontal=True), 70, 70, 100, 255)
    image sebastian smile dk = im.Recolor("cr/sebastian_smile.png", 70, 70, 100, 255)
    image sebastian smile b dk = im.Recolor("cr/sebastian_smile_b.png", 70, 70, 100, 255)

    image sebastian shy b sleep = "cr/sebastian_shy_b_sleep.png"
    image sebastian shy b sleep dk = im.Recolor("cr/sebastian_shy_b_sleep.png", 70, 70, 100, 255)

init python:
    bangok_four_malepartners = 0
    bangok_four_femalepartners = 0
    bangok_four_playerhasdick = None
    bangok_four_hornincident = False
