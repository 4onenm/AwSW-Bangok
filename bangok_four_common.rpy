init python:
    # Common game variables
    bangok_four_malepartners = 0
    bangok_four_femalepartners = 0
    bangok_four_playerhasdick = None
    bangok_four_hornincident = False

init python in bangok_four_common:
    import bangok_four
    renpy.pure('bangok_four_common.bangok_four.fetish_count')
    renpy.pure('bangok_four_common.bangok_four.fetish_iter')

    import bangok_four.trackcursor
    TrackCursor = bangok_four.trackcursor.TrackCursor

    import bangok_four.moredisplayables
    PersistentConditionalDisplayable = bangok_four.moredisplayables.PersistentConditionalDisplayable
    LayeredImage = bangok_four.moredisplayables.layeredimage.LayeredImage
    Always = bangok_four.moredisplayables.layeredimage.Always
    Attribute = bangok_four.moredisplayables.layeredimage.Attribute
    Condition = bangok_four.moredisplayables.layeredimage.Condition


init:
    define bangok_four_bangnokay = False

    # Settings menu
    style bangok_four_switch is image_button:
        activate_sound "se/sounds/yes.wav"
        hover_sound "se/sounds/select.ogg"

    style bangok_four_smallwindowclose is smallwindowclose:
        activate_sound "se/sounds/close.ogg"
        hover_sound "se/sounds/select.ogg"

    style bangok_four_close is button:
        activate_sound "se/sounds/close.ogg"
        hover_sound "se/sounds/select.ogg"

    screen bangok_modsettings():
        tag smallscreen2
        modal True
        window id "bangok_modsettings" at popup2:
            style "smallwindow_big2"
            if bangok_four_bangnokay or persistent.bangok_four_bangnokay:
                textbutton "Bang? No, Kay Mod Settings":
                    yalign 0.06
                    xalign 0.5
                    text_size 44
                    action SetField(persistent, 'bangok_four_bangnokay', False)
                    style "bangok_four_switch"
            else:
                textbutton "BangOk Mod Settings":
                    yalign 0.06
                    xalign 0.5
                    text_size 44
                    action SetField(persistent, 'bangok_four_bangnokay', True)
                    style "bangok_four_switch"


            if not persistent.nsfwtoggle:
                vbox:
                    text "This mod's content is primarily" xalign 0.5
                    text "---- Not-Safe-For-Work ----" xalign 0.5
                    text "Re-enable NSFW scenes or uninstall the mod." xalign 0.5
                    text "This mod does not guarantee all NSFW content is inaccessible\nwhile NSFW scenes are disabled, though an attempt was made." xalign 0.5
            else:
                vbox:
                    align (0.5, 0.3)
                    if bangok_four_bangnokay or persistent.bangok_four_bangnokay:
                        text "Cute Buttons:" xalign 0.5
                    else:
                        text "Fetishes:" xalign 0.5
                        text "If you do not know what an option means, leave it deselected (or look it up at your own peril).":
                            xalign 0.5
                            size 32

                    grid ((bangok_four_common.bangok_four.fetish_count(bangok_four_bangnokay or persistent.bangok_four_bangnokay)+1)//2) 2:
                        align (0.5,0.5)
                        transpose True
                        spacing 10
                        for fetish in bangok_four_common.bangok_four.fetish_iter(bangok_four_bangnokay or persistent.bangok_four_bangnokay):
                            vbox:
                                add fetish.get_switch(bangok_four_bangnokay or persistent.bangok_four_bangnokay)
                                showif bangok_four_bangnokay or persistent.bangok_four_bangnokay:
                                    text "[fetish.clean_label]"
                                showif not (bangok_four_bangnokay or persistent.bangok_four_bangnokay):
                                    text "[fetish.label]"
                        if bangok_four_common.bangok_four.fetish_count(bangok_four_bangnokay or persistent.bangok_four_bangnokay) % 2 == 1:
                            null

                hbox:
                    xalign 0.5
                    yalign 0.8
                    spacing 20
                    imagebutton:
                        idle im.Scale("ui/nsfw_chbox-unchecked.png", 55, 55)
                        hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 55, 55), 64, 64, 64)
                        selected_idle im.Scale("ui/nsfw_chbox-checked.png", 55, 55)
                        selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 55, 55), 64, 64, 64)
                        action MTSTogglePersistentBool('bangok_dev')
                        style "bangok_four_switch"
                        focus_mask None
                    text "Dangerous: Enable In-Development Scenes"

                showif persistent.bangok_dev == True and not (bangok_four_bangnokay or persistent.bangok_four_bangnokay):
                    text "In-Development scenes may not have conclusions, and {i}will{/i} have paths leading to crashes.":
                        yalign 0.875
                        xalign 0.5
                        size 40

            showif persistent.bangok_dev == True and main_menu and not (bangok_four_bangnokay or persistent.bangok_four_bangnokay):
                textbutton "[[Replay first-boot experience.]":
                    xalign 0.5 
                    yalign 1.1
                    action [Hide("bangok_modsettings"), Start("bangok_four_mod_firstboot")]
                    style "bangok_four_close"

            imagebutton:
                idle "image/ui/close_idle.png"
                hover "image/ui/close_hover.png"
                action [Hide("bangok_modsettings"), Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")]
                hovered Play("audio", "se/sounds/select.ogg")
                style "bangok_four_smallwindowclose"
                at nav_button

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
    image bangok_four_labdoor dk track = bangok_four_common.TrackCursor(
        im.Recolor("bg/in/bangok/labdoor.png", 60, 70, 100, 255),
        posxmin=-8, posxmax=42,
        posymin=-40, posymax=40)

    image bangok_four_officedoor = "bg/in/bangok/officedoor.png"
    image bangok_four_officedoor track = bangok_four_common.TrackCursor(
        "bg/in/bangok/officedoor.png",
        posxmin=0, posxmax=16,
        posymin=0, posymax=40)


    # CGs
    image bangok_four_xipsum_afterglow = "cg/lorem-x-ipsum_purpleroom.png"


    image bangok_four_annaxdamion = bangok_four_common.LayeredImage([
        bangok_four_common.Always("cg/bangok/annaxdamion_lab/base.png"),
        bangok_four_common.Always(
            bangok_four_common.PersistentConditionalDisplayable(
                'bangok_cloacas', None,
                None, "cg/bangok/annaxdamion_lab/vaginal.png",
            ),
            pos=(-68, 130)
        ),
        bangok_four_common.Attribute('bulge','bulge', "cg/bangok/annaxdamion_lab/bulge.png"),
        bangok_four_common.Attribute('cum', 'cum',
            bangok_four_common.PersistentConditionalDisplayable(
                'bangok_cloacas', "cg/bangok/annaxdamion_lab/cloacal_cum.png",
                None, "cg/bangok/annaxdamion_lab/vaginal_cum.png",
            ),
            if_not=['bulge'],
            pos=(-68, 130),
        ),
        bangok_four_common.Attribute('cum', 'cum',
            im.Composite((1280,988),
                (0,0),"cg/bangok/annaxdamion_lab/cloacal_cum.png",
                (0,0),"cg/bangok/annaxdamion_lab/vaginal_cum.png",
            ),
            if_all=['bulge'],
            pos=(-68, 130),
        ),
        bangok_four_common.Always(
            bangok_four_common.PersistentConditionalDisplayable(
                ('bangok_balls', 'bangok_inflation'), "cg/bangok/annaxdamion_lab/dm_ballz_big.png",
                'bangok_balls', "cg/bangok/annaxdamion_lab/dm_ballz.png",
                None, None
            ),
        ),
    ])


    image bangok_four_brycexsebastian = bangok_four_common.LayeredImage([
        bangok_four_common.Always("cg/bangok/brycexsebastian_office/officecut.jpg"),
        bangok_four_common.Attribute('frame',        'frameA', "cg/bangok/brycexsebastian_office/frameA_base.png"),
        bangok_four_common.Attribute('frame',        'frameB', "cg/bangok/brycexsebastian_office/frameB_base.png"),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeclosed', "cg/bangok/brycexsebastian_office/bryceeyeclosed.png"),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeopen', "cg/bangok/brycexsebastian_office/bryceeyeopen.png"),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeroll', "cg/bangok/brycexsebastian_office/bryceeyeroll.png"),
        bangok_four_common.Attribute('brycemouth',   'brycesmile', "cg/bangok/brycexsebastian_office/brycesmile.png"),
        bangok_four_common.Attribute('cumspill',     'nocum', "cg/bangok/brycexsebastian_office/frameB_cumcoverup.png", default=True, if_all=['frameB']),
        bangok_four_common.Attribute('cumspill',     'cum', renpy.display.layout.Null(), if_all=['frameB']),
        bangok_four_common.Attribute('cumspill',     'morecum', "cg/bangok/brycexsebastian_office/frameB_cumspill+.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebcheek',     'sebcheekbulge', "cg/bangok/brycexsebastian_office/frameB_sebcheekbulge.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebthroat',    'sebthroatbulge', "cg/bangok/brycexsebastian_office/frameB_sebthroatbulge.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebeye',       'sebeyeopen', "cg/bangok/brycexsebastian_office/frameB_sebeyeopen.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebeye',       'sebeyeshocked', "cg/bangok/brycexsebastian_office/frameB_sebeyeshocked.png", if_all=['frameB']),
    ])
    image bangok_four_brycexsebastian_lickpanel = "cg/bangok/brycexsebastian_office/lickpanel.png"

    image bangok_four_brycexsebastian animate bryceclosedsmile sebastianopen:
        "bangok_four_brycexsebastian frameA bryceeyeclosed brycesmile sebeyeopen"
        "bangok_four_brycexsebastian frameB bryceeyeclosed brycesmile sebeyeopen" with dissolve
        pause 1.5
        "bangok_four_brycexsebastian frameA bryceeyeclosed brycesmile sebeyeopen" with dissolve
        pause 1.5
        repeat
    image bangok_four_brycexsebastian animate bryceclosed:
        "bangok_four_brycexsebastian frameA bryceeyeclosed"
        "bangok_four_brycexsebastian frameB bryceeyeclosed" with dissolve
        pause 1.5
        "bangok_four_brycexsebastian frameA bryceeyeclosed" with dissolve
        pause 1.5
        repeat


    # People
    image adineshower blush = im.Composite(
        (3000,1688),
        (0,0), "cg/chap4/adineshower.jpg",
        (0,0), "cg/bangok/adineshower/adineshower_blush.png",
    )
    image adineshower think = im.Composite(
        (3000,1688),
        (0,0), "cg/chap4/adineshower.jpg",
        (0,0), "cg/bangok/adineshower/adineshower_think.png",
    )
    image adineshower thinkblush = im.Composite(
        (3000,1688),
        (0,0), "cg/chap4/adineshower.jpg",
        (0,0), "cg/bangok/adineshower/adineshower_blush.png",
        (0,0), "cg/bangok/adineshower/adineshower_think.png",
    )
    image adineshower annoyedblush = im.Composite(
        (3000,1688),
        (0,0), "cg/chap4/adineshower.jpg",
        (0,0), "cg/bangok/adineshower/adineshower_blush.png",
        (0,0), "cg/bangok/adineshower/adineshower_annoyed.png",
    )


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

    image bryce normal bangok foreleg flip = im.Composite((1152,969),(0,0),"cr/bryce_normal_flip.png", (0,0), "cr/bangok/bryce_foreleg.png")
    image bryce brow bangok foreleg flip = im.Composite((1152,969),(0,0),"cr/bryce_brow_flip.png", (0,0), "cr/bangok/bryce_foreleg.png")
    image bryce flirty bangok foreleg flip = im.Composite((1152,969),(0,0),"cr/bryce_flirty_flip.png", (0,0), "cr/bangok/bryce_foreleg.png")
    image bryce laugh bangok foreleg flip = im.Composite((1152,969),(0,0),"cr/bryce_laugh_flip.png", (0,0), "cr/bangok/bryce_foreleg.png")
    image bryce smirk bangok foreleg flip = im.Composite((1152,969),(0,0),"cr/bryce_smirk_flip.png", (0,0), "cr/bangok/bryce_foreleg.png")
    image bryce stern bangok foreleg flip = im.Composite((1152,969),(0,0),"cr/bryce_stern_flip.png", (0,0), "cr/bangok/bryce_foreleg.png")
    image bryce sad bangok foreleg flip = im.Composite((1152,969),(0,0),"cr/bryce_sad_flip.png", (0,0), "cr/bangok/bryce_foreleg.png")


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

    image lorem happy bangok shy = "cr/bangok/lorem_happy+blush.png"
    image lorem happy bangok shy flip = im.Flip("cr/bangok/lorem_happy+blush.png", horizontal=True)
    image lorem happy bangok shy2 = "cr/bangok/lorem_happy2+blush.png"
    image lorem happy bangok shy2 flip = im.Flip("cr/bangok/lorem_happy2+blush.png", horizontal=True)
    image lorem bangok aheago1 = "cr/bangok/lorem_aheago1.png"
    image lorem bangok aheago1 flip = im.Flip("cr/bangok/lorem_aheago1.png", horizontal=True)
    image lorem bangok aheago2 = "cr/bangok/lorem_aheago2.png"
    image lorem bangok aheago1 flip = im.Flip("cr/bangok/lorem_aheago2.png", horizontal=True)


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
    image lorem normal bangok bulge erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_normal.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem normal bangok bulge erect flip = im.Flip(renpy.display.image.ImageReference('lorem normal bangok bulge erect'),horizontal=True)
    image lorem happy bangok bulge erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_happy.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem happy bangok bulge erect flip = im.Flip(renpy.display.image.ImageReference('lorem happy bangok bulge erect'),horizontal=True)
    image lorem sad bangok bulge erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_sad.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem sad bangok bulge erect flip = im.Flip(renpy.display.image.ImageReference('lorem sad bangok bulge erect'),horizontal=True)
    image lorem relieved bangok bulge erect = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_relieved.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0), "cr/bangok/lorem_penis_armcovered.png"
    )
    image lorem relieved bangok bulge erect flip = im.Flip(renpy.display.image.ImageReference('lorem relieved bangok bulge erect'),horizontal=True)
    image lorem shy bangok bulge erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_shy.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem shy bangok bulge erect flip = im.Flip(renpy.display.image.ImageReference('lorem shy bangok bulge erect'),horizontal=True)
    image lorem think bangok bulge erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_think.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem think bangok bulge erect flip = im.Flip(renpy.display.image.ImageReference('lorem think bangok bulge erect'),horizontal=True)
    image lorem blush bangok bulge erect = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_blush.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )
    image lorem happy bangok shy bulge erect = im.Composite(
        (1240,650),
        (0,0),"cr/bangok/lorem_Happy+blush.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_penis.png"
    )

    image lorem normal bangok cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_normal.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem normal bangok cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem normal bangok cumleak'),horizontal=True)
    image lorem happy bangok cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_happy.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem happy bangok cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem happy bangok cumleak'),horizontal=True)
    image lorem sad bangok cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_sad.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem sad bangok cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem sad bangok cumleak'),horizontal=True)
    image lorem shy bangok cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_shy.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem shy bangok cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem shy bangok cumleak'),horizontal=True)
    image lorem think bangok cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_think.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem think bangok cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem think bangok cumleak'),horizontal=True)

    image lorem normal bangok pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_normal.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem normal bangok pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem normal bangok pissleak'),horizontal=True)
    image lorem happy bangok pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_happy.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem happy bangok pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem happy bangok pissleak'),horizontal=True)
    image lorem sad bangok pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_sad.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem sad bangok pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem sad bangok pissleak'),horizontal=True)
    image lorem shy bangok pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_shy.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem shy bangok pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem shy bangok pissleak'),horizontal=True)
    image lorem think bangok pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_think.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem think bangok pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem think bangok pissleak'),horizontal=True)

    image lorem normal bangok bulge cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_normal.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem normal bangok bulge cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem normal bangok bulge cumleak'),horizontal=True)
    image lorem happy bangok bulge cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_happy.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem happy bangok bulge cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem happy bangok bulge cumleak'),horizontal=True)
    image lorem sad bangok bulge cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_sad.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem sad bangok bulge cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem sad bangok bulge cumleak'),horizontal=True)
    image lorem shy bangok bulge cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_shy.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem shy bangok bulge cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem shy bangok bulge cumleak'),horizontal=True)
    image lorem think bangok bulge cumleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_think.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_cumleak.png"
    )
    image lorem think bangok bulge cumleak flip = im.Flip(renpy.display.image.ImageReference('lorem think bangok bulge cumleak'),horizontal=True)

    image lorem normal bangok bulge pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_normal.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem normal bangok bulge pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem normal bangok bulge pissleak'),horizontal=True)
    image lorem happy bangok bulge pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_happy.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem happy bangok bulge pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem happy bangok bulge pissleak'),horizontal=True)
    image lorem sad bangok bulge pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_sad.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem sad bangok bulge pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem sad bangok bulge pissleak'),horizontal=True)
    image lorem shy bangok bulge pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_shy.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem shy bangok bulge pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem shy bangok bulge pissleak'),horizontal=True)
    image lorem think bangok bulge pissleak = im.Composite(
        (1240,650),
        (0,0),"cr/lorem_think.png",
        (0,0),"cr/bangok/lorem_bulge.png",
        (0,0),"cr/bangok/lorem_pen_pissleak.png"
    )
    image lorem think bangok bulge pissleak flip = im.Flip(renpy.display.image.ImageReference('lorem think bangok bulge pissleak'),horizontal=True)

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
    image lorem think bangok peek flip = im.Flip(renpy.display.image.ImageReference('lorem think bangok peek'),horizontal=True)

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
        (0,0), "cr/bangok/ipsum_heady.png",
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
    image sebastian normal dk = im.Recolor("cr/sebastian_normal.png", 70, 70, 100, 255)
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
