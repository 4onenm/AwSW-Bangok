init python:
    # Common game variables
    bangok_four_malepartners = 0
    bangok_four_femalepartners = 0
    bangok_four_playerhasdick = None
    bangok_four_hornincident = False


init python in bangok_four_xdamion_store:
    import pygame
    import math

    # Initial parallax code thanks to Aquapaulo
    #  https://github.com/aquapaulo/renpy-main-menu-parallax/blob/main/CODE.md
    class TrackCursor(renpy.Displayable):
        def __init__(self, child, posxmin=0, posxmax=100, posymin=0, posymax=100):
            super(TrackCursor, self).__init__(style='transform')

            self.child = renpy.displayable(child)

            self.mouse_x = None
            self.mouse_y = None

            self.actual_x = 0
            self.actual_y = 0

            self.posxmin, self.posxmax = posxmin, posxmax
            self.posymin, self.posymax = posymin, posymax

            self.last_at = 0

        def render(self, width, height, st, at):

            speed = 1.5


            if self.mouse_x is not None:
                at_change = at - self.last_at

                range_x = self.posxmax - self.posxmin
                range_y = self.posymax - self.posymin

                x = (self.mouse_x/renpy.config.screen_width)*range_x
                y = (self.mouse_y/renpy.config.screen_height)*range_y

                self.last_at = at
                self.actual_x = math.floor(self.actual_x + ((x - self.actual_x) * speed * (at_change)))
                self.actual_y = math.floor(self.actual_y + ((y - self.actual_y) * speed * (at_change)))

                self.actual_x = max(0,min(range_x, x))
                self.actual_y = max(0,min(range_y, y))
            else:
                x,y = self.actual_x, self.actual_y

            self.last_at = at

            cr = renpy.render(self.child, width, height, st, at)
            rv = renpy.Render(width, height)
            rv.blit(cr, (self.actual_x+self.posxmin, self.actual_y+self.posymin))

            if x != self.actual_x:
                renpy.redraw(self, 0)
            return rv

        def event(self, ev, x, y, st):
            super(TrackCursor, self).event(ev, x, y, st)

            if ev.type == pygame.MOUSEMOTION:
                if (x != self.mouse_x) or (y != self.mouse_y):
                    self.mouse_x, self.mouse_y = x, y
                    renpy.redraw(self, 0)

        def visit(self):
            return [ self.child ]


init:
    define bangok_four_bangnokay = False

    # Menu constants
    define bangok_four_menu_fetish_list = [
        ("Watersports", "bangok_watersports"),
        ("Inflation", "bangok_inflation"),
        ("Knotting", "bangok_knot"),
        ("Cloacas", "bangok_cloacas"),
        ("Cervical Penetration","bangok_cervpen"),
        ("Voyeurism", "bangok_voyeurism"),
    ]
    define bangok_four_menu_fetish_list_columns = ((len(bangok_four_menu_fetish_list)+1)//2)

    # Settings menu
    screen bangok_four_checkbox(label, id):
        hbox:
            spacing 10
            imagebutton:
                xcenter 0.5
                ycenter 0.5
                idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                action [MTSTogglePersistentBool(id),
                        Play("audio", "se/sounds/yes.wav")]
                hovered Play("audio", "se/sounds/select.ogg")
                focus_mask None
            text label


    screen bangok_modsettings tag smallscreen2:
        modal True
        window id "bangok_modsettings" at popup2:
            style "smallwindow"
            vbox:
                align (0.5, 0.5)
                if not persistent.nsfwtoggle:
                    text "This mod's content is primarily" xalign 0.5
                    text "---- Not-Safe-For-Work ----" xalign 0.5
                    text "Re-enable NSFW scenes or uninstall the mod." xalign 0.5
                    text "This mod does not guarantee all NSFW content is inaccessible\nwhile NSFW scenes are disabled, though an attempt was made." xalign 0.5
                else:
                    if bangok_four_bangnokay or persistent.bangok_four_bangnokay:
                        textbutton "Bang? No, Kay Mod Settings":
                            xalign 0.5
                            text_size 36
                            action [Play("audio", "se/sounds/yes.wav"), SetField(persistent, 'bangok_four_bangnokay', False)]
                            hovered Play("audio", "se/sounds/select.ogg")
                            style "menu_choice_button"
                        text "Cute Buttons:" xalign 0.5
                        grid 3 2:
                            align (0.5, 0.5)
                            transpose True
                            spacing 10
                            for label, id in [("Water Polo", "bangok_watersports"),("Balloons", "bangok_inflation"),("Knot Tying", "bangok_knot"),("Spelunking", "bangok_cloacas"),("Mining","bangok_cervpen"),]:
                                use bangok_four_checkbox(label, id)
                            null
                    else:
                        textbutton "BangOk Mod Settings":
                            xalign 0.5
                            text_size 36
                            action [Play("audio", "se/sounds/yes.wav"), SetField(persistent, 'bangok_four_bangnokay', True)]
                            hovered Play("audio", "se/sounds/select.ogg")
                            style "menu_choice_button"
                        text "Fetishes:" xalign 0.5
                        grid bangok_four_menu_fetish_list_columns 2:
                            align (0.5,0.5)
                            transpose True
                            spacing 10
                            for label, id in bangok_four_menu_fetish_list:
                                use bangok_four_checkbox(label, id)
                            if len(bangok_four_menu_fetish_list) % 2 == 1:
                                null
                    text "If you do not know what an option means, leave it deselected (or look it up at your own peril).":
                        xalign 0.5
                        size 38
                    vbox:
                        xalign 0.5
                        use bangok_four_checkbox("Dangerous: Enable In-Development Scenes", "bangok_dev")
                    showif persistent.bangok_dev == True:
                        text "In-Development scenes may not have conclusions, and {i}will{/i} have paths leading to crashes." xalign 0.5 size 40
                        showif main_menu:
                            textbutton "[[Replay first-boot experience.]" xalign 0.5 hovered Play("audio", "se/sounds/select.ogg") action [Hide("bangok_modsettings"), Play("audio", "se/sounds/close.ogg"), Start("bangok_four_mod_firstboot")]
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("bangok_modsettings"), Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button


    # Locations
    image bangok_anon_o_ceiling = "bg/in/apts/o_ceil.png"
    
    image bangok_four_bryce1_apartment night = "bg/in/apts/pad_night.png"
    image bangok_four_bryce1_apartment night ceiling = "bg/in/apts/pad_night_ceil.png"

    image bangok_four_xipsum_bedroom normal = "bg/in/apts/ipsum_bedroom.png"
    image bangok_four_xipsum_bedroom_bed = "bg/in/apts/ipsum_bedroom_bed.png"
    image bangok_four_xipsum_bedroom ceiling = "bg/in/apts/ipsum_bedroom_ceiling.png"

    image bangok_four_xsebastian_cave2_dk = im.Recolor("bg/in/cave2_dk.png", 70, 70, 100, 255)

    image bangok_four_library night = im.Recolor("bg/in/bangok_library_night.png", 70, 70, 100, 255)
    image bangok_four_library outside night = im.Recolor("bg/out/town/town5.jpg", 60, 70, 100, 255)

    image bangok_four_labdoor = "bg/in/bangok/labdoor.png"
    image bangok_four_labdoor dk = im.Recolor("bg/in/bangok/labdoor.png", 60, 70, 100, 255)
    image bangok_four_labdoor dk track = bangok_four_xdamion_store.TrackCursor(
        im.Recolor("bg/in/bangok/labdoor.png", 60, 70, 100, 255),
        posxmin=-320, posxmax=160,
        posymin=-40, posymax=40)


    # CGs
    image bangok_four_xipsum_afterglow = "cg/lorem-x-ipsum_purpleroom.png"

    image bangok_four_annaxdamion cloacal = "cg/bangok/annaxdamion_lab/base.png"
    image bangok_four_annaxdamion cloacal bulge = im.Composite(
        (1280,988),
        (0,0), "cg/bangok/annaxdamion_lab/base.png",
        (-68,130), "cg/bangok/annaxdamion_lab/cloacal_bulge.png",
    )
    image bangok_four_annaxdamion cloacal bulge cum = im.Composite(
        (1280,988), 
        (0,0), "cg/bangok/annaxdamion_lab/base.png",
        (-68,130), "cg/bangok/annaxdamion_lab/cloacal_bulge.png",
        (-68,130), "cg/bangok/annaxdamion_lab/cloacal_cum.png",
    )
    image bangok_four_annaxdamion cloacal cum = im.Composite(
        (1280,988), 
        (0,0), "cg/bangok/annaxdamion_lab/base.png",
        (-68,130), "cg/bangok/annaxdamion_lab/cloacal_cum.png",
    )
    image bangok_four_annaxdamion vaginal = im.Composite(
        (1280,988),
        (0,0), "cg/bangok/annaxdamion_lab/base.png",
        (-68,130), "cg/bangok/annaxdamion_lab/vaginal.png",
    )
    image bangok_four_annaxdamion vaginal cum = im.Composite(
        (1280,988),
        (0,0), "cg/bangok/annaxdamion_lab/base.png",
        (-68,130), "cg/bangok/annaxdamion_lab/vaginal.png",
        (-68,130), "cg/bangok/annaxdamion_lab/vaginal_cum.png",
    )
    image bangok_four_annaxdamion vaginal bulge = im.Composite(
        (1280,988),
        (0,0), "cg/bangok/annaxdamion_lab/base.png",
        (-68,130), "cg/bangok/annaxdamion_lab/vaginal_bulge.png",
    )
    image bangok_four_annaxdamion vaginal bulge cum = im.Composite(
        (1280,988),
        (0,0), "cg/bangok/annaxdamion_lab/base.png",
        (-68,130), "cg/bangok/annaxdamion_lab/vaginal_bulge.png",
        (-68,130), "cg/bangok/annaxdamion_lab/vaginal_cum.png",
    )


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

    image damion normal bangok = im.Composite(
        (709,827),
        (0,0),"cr/damion_normal.png",
        (0,0),"cr/bangok/damion_pen.png"
    )
    image damion normal bangok flip = im.Flip(renpy.display.image.ImageReference('damion normal bangok'),horizontal=True)
    image damion face bangok = im.Composite(
        (709,827),
        (0,0),"cr/damion_face.png",
        (0,0),"cr/bangok/damion_pen.png"
    )
    image damion face bangok flip = im.Flip(renpy.display.image.ImageReference('damion face bangok'),horizontal=True)
    image damion arrogant bangok = im.Composite(
        (709,827),
        (0,0),"cr/damion_arrogant.png",
        (0,0),"cr/bangok/damion_pen.png"
    )
    image damion arrogant bangok flip = im.Flip(renpy.display.image.ImageReference('damion arrogant bangok'),horizontal=True)

    image damion normal bangok ws = im.Composite(
        (709,827),
        (0,0),"cr/damion_normal.png",
        (0,0),"cr/bangok/damion_pen_ws.png"
    )
    image damion normal bangok ws flip = im.Flip(renpy.display.image.ImageReference('damion normal bangok ws'),horizontal=True)
    image damion face bangok ws = im.Composite(
        (709,827),
        (0,0),"cr/damion_face.png",
        (0,0),"cr/bangok/damion_pen_ws.png"
    )
    image damion face bangok ws flip = im.Flip(renpy.display.image.ImageReference('damion face bangok ws'),horizontal=True)
    image damion arrogant bangok ws = im.Composite(
        (709,827),
        (0,0),"cr/damion_arrogant.png",
        (0,0),"cr/bangok/damion_pen_ws.png"
    )
    image damion arrogant bangok ws flip = im.Flip(renpy.display.image.ImageReference('damion arrogant bangok ws'),horizontal=True)
    

    image lorem normal bangok erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_normal.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem normal bangok erect flip = im.Flip(renpy.display.image.ImageReference('lorem normal bangok erect'),horizontal=True)
    image lorem happy bangok erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_happy.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem happy bangok erect flip = im.Flip(renpy.display.image.ImageReference('lorem happy bangok erect'),horizontal=True)
    image lorem sad bangok erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_sad.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem sad bangok erect flip = im.Flip(renpy.display.image.ImageReference('lorem sad bangok erect'),horizontal=True)
    image lorem relieved bangok erect = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_relieved.png",
        (0,0), "cr/bangok/lorem_penis_armcovered.png"
    )
    image lorem relieved bangok erect flip = im.Flip(renpy.display.image.ImageReference('lorem relieved bangok erect'),horizontal=True)
    image lorem shy bangok erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_shy.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem shy bangok erect flip = im.Flip(renpy.display.image.ImageReference('lorem shy bangok erect'),horizontal=True)
    image lorem think bangok erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_think.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem think bangok erect flip = im.Flip(renpy.display.image.ImageReference('lorem think bangok erect'),horizontal=True)

    image lorem normal bangok peek = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_normal.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem normal bangok peek flip = im.Flip(renpy.display.image.ImageReference('lorem normal bangok peek'),horizontal=True)
    image lorem happy bangok peek = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_happy.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem happy bangok peek flip = im.Flip(renpy.display.image.ImageReference('lorem happy bangok peek'),horizontal=True)
    image lorem sad bangok peek = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_sad.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem sad bangok peek flip = im.Flip(renpy.display.image.ImageReference('lorem sad bangok peek'),horizontal=True)
    image lorem relieved bangok peek = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_relieved.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem relieved bangok peek flip = im.Flip(renpy.display.image.ImageReference('lorem relieved bangok peek'),horizontal=True)
    image lorem shy bangok peek = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_shy.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem shy bangok peek flip = im.Flip(renpy.display.image.ImageReference('lorem shy bangok peek'),horizontal=True)
    image lorem think bangok peek = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_think.png",
        (626,579), "cr/lorem_bangok_peek.png"
    )
    image lorem think bangok peek flip = im.Flip('lorem think bangok peek',horizontal=True)

    image lorem bangok hidepeek = "cr/lorem_bangok_hidepeek.png"
    image lorem bangok hidepeek flip = im.Flip("cr/lorem_bangok_hidepeek.png",horizontal=True)

    # Novel Ipsum emotions
    image ipsum look bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_look.png"
    )
    image ipsum normal bangok blush = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_normal_blush.png",
    )
    image ipsum normal bangok blush flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok blush'),horizontal=True)
    image ipsum happy bangok blush = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_happy_blush.png",
    )
    image ipsum happy bangok blush flip = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok blush'),horizontal=True)
    image ipsum normal bangok heady = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_heady.png",
    )
    image ipsum normal bangok heady flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok heady'),horizontal=True)
    image ipsum happy bangok heady = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_heady_grin.png",
    )
    image ipsum happy bangok heady flip = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok heady'),horizontal=True)
    # Ipsum pen art
    image ipsum normal bangok erect wrapped = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_normal.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum normal bangok erect wrapped flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok erect wrapped'),horizontal=True)
    image ipsum happy bangok erect wrapped = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_happy.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum happy bangok erect wrapped flip = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok erect wrapped'),horizontal=True)
    image ipsum sad bangok erect wrapped = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum sad bangok erect wrapped flip = im.Flip(renpy.display.image.ImageReference('ipsum sad bangok erect wrapped'),horizontal=True)
    image ipsum think bangok erect wrapped = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_think.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum think bangok erect wrapped flip = im.Flip(renpy.display.image.ImageReference('ipsum think bangok erect wrapped'),horizontal=True)
    # Ipsum swimwear art
    image ipsum normal bangok briefs = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_normal.png",
        (0,0), "cr/bangok/ipsum_briefs.png",
    )
    image ipsum normal bangok briefs flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok briefs'),horizontal=True)
    image ipsum normal bangok blush briefs = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_normal_blush.png",
        (0,0), "cr/bangok/ipsum_briefs.png",
    )
    image ipsum normal bangok blush briefs flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok blush'),horizontal=True)
    image ipsum normal bangok aheago briefs = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_aheago_1_drop.png",
        (0,0), "cr/bangok/ipsum_briefs.png",
    )
    image ipsum normal bangok aheago briefs flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok aheago briefs'),horizontal=True)
    image ipsum happy bangok briefs = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_happy.png",
        (0,0), "cr/bangok/ipsum_briefs.png",
    )
    image ipsum happy bangok briefs flip = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok briefs'),horizontal=True)
    image ipsum happy bangok blush briefs = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_happy_blush.png",
        (0,0), "cr/bangok/ipsum_briefs.png",
    )
    image ipsum happy bangok blush briefs flip = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok blush briefs'),horizontal=True)
    image ipsum sad bangok briefs = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_briefs.png",
    )
    image ipsum sad bangok briefs flip = im.Flip(renpy.display.image.ImageReference('ipsum sad bangok briefs'),horizontal=True)
    image ipsum think bangok briefs = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_think.png",
        (0,0), "cr/bangok/ipsum_briefs.png",
    )
    image ipsum think bangok briefs flip = im.Flip(renpy.display.image.ImageReference('ipsum think bangok briefs'),horizontal=True)
    image ipsum normal bangok briefs touch = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_normal.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
    )
    image ipsum normal bangok briefs touch flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok briefs touch'),horizontal=True)
    image ipsum normal bangok heady briefs touch = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_heady_blush.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
    )
    image ipsum normal bangok heady briefs touch flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok briefs touch'),horizontal=True)
    image ipsum happy bangok briefs touch = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_happy.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
    )
    image ipsum happy bangok briefs touch flip = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok briefs touch'),horizontal=True)
    image ipsum sad bangok briefs touch = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
    )
    image ipsum sad bangok briefs touch flip = im.Flip(renpy.display.image.ImageReference('ipsum sad bangok briefs touch'),horizontal=True)
    image ipsum normal bangok briefs touch glow = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_normal.png",
        (0,0), "cr/bangok/ipsum_briefs_glow.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
    )
    image ipsum normal bangok briefs touch glow flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok briefs touch'),horizontal=True)
    image ipsum normal bangok blush briefs touch glow = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_normal_blush.png",
        (0,0), "cr/bangok/ipsum_briefs_glow.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
    )
    image ipsum normal bangok blush briefs touch glow flip = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok blush briefs touch glow'),horizontal=True)
    image ipsum happy bangok briefs touch glow = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_happy.png",
        (0,0), "cr/bangok/ipsum_briefs_glow.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
    )
    image ipsum happy bangok briefs touch glow flip = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok briefs touch'),horizontal=True)
    image ipsum sad bangok briefs touch glow = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_briefs_glow.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
    )
    image ipsum sad bangok briefs touch glow flip = im.Flip(renpy.display.image.ImageReference('ipsum sad bangok briefs touch'),horizontal=True)
    image ipsum happy bangok blush briefs touch glow = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (0,0), "cr/bangok/ipsum_happy_blush.png",
        (0,0), "cr/bangok/ipsum_briefs_touch.png",
        (0,0), "cr/bangok/ipsum_briefs_glow.png",
    )
    image ipsum happy bangok blush briefs touch glow flip = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok blush briefs touch glow'),horizontal=True)



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

label bangok_four_mod_firstboot:
    $ _skipping = False
    stop music
    scene black with dissolve
    play sound "fx/system3.wav"
    s "Initializing modification \"BangOk\"{cps=2}...{/cps}{w=0.5}{nw}"
    s "Initializing modification \"BangOk\"... {fast}Done!"
    $ _skipping = True
    s "BangOk alters targetable coordinates to one of several different universes, with slightly differing draconic biologies and sexual fetish preferences."
    s "Would you like to configure these coordinates now, or accept the most-vanilla, most human-like defaults?"
    menu:
        "Yes, I'd like to configure my BangOk fetishes now.":
            show screen bangok_modsettings
        "No, I'll do it later from the settings menu.":
            pass
    s "Recalculating arrival coordinates.{cps=2}..{/cps}"
    play sound "fx/system.wav"
    s "Calculations complete."
    s "The BangOk module has been added to your {i}settings{/i} menu under {i}Mod Settings.{/i} You may alter your coordinates at {i}any time{/i}, though doing so in the midst of certain... activities may cause timeline instability."
    $ persistent.bangok_four_menu_firstboot_complete = True
    s "Returning to main menu initialization.{cps=2}..{/cps}{w=0.5}{nw}"
    jump bangok_four_mod_firstboot_return

label bangok_four_bangnokay_kill_replay:
    play sound "fx/system3.wav"
    s "Whoops! There is nothing to see here."
    play sound "fx/system3.wav"
    s "Let me just clean this up..."
    $ renpy.end_replay()
    jump ml_main_menu