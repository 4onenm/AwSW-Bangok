init:
    image bangok_four_bryce1_apartment night = "bg/in/apts/pad_night.png"
    image bangok_four_bryce1_apartment night ceiling = "bg/in/apts/pad_night_ceil.png"

    image bangok_four_bryce_underside_large dk = im.Recolor("cr/bryce_underside_large.png", 70, 70, 100, 255)
    image bangok_four_bryce_underside_large dk flip = im.Recolor(im.Flip("cr/bryce_underside_large.png",horizontal=True), 70, 70, 100, 255)

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

                    text "If you do not know what an option means, look it up or leave it deselected."

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


init python:
    # First time per run, obv.
    bangok_four_firsttime = True