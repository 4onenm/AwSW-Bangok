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

    import bangok_four.moredisplayables as md
    PersistentConditionalDisplayable = md.PersistentConditionalDisplayable
    LayeredImage = md.layeredimage.LayeredImage
    Always = md.layeredimage.Always
    Attribute = md.layeredimage.Attribute
    Condition = md.layeredimage.Condition
    PersistentConditionalLayer = md.PersistentConditionalLayer
    PersistentConditionalComposite = md.PersistentConditionalComposite

    import bangok_four.bangnokay as bangnokay

    @renpy.pure
    def bangnokay_quest_text(stage):
        if not stage:
            return _("Bang? No, Kay Mod Settings")
        if stage < 2:
            return _("No Bang, Kay?")
        if stage < 3:
            return _("We won't bang, okay?")
        if stage < 4:
            return _("Wait, no, no bang.")
        if stage < 5:
            return _("You're trying to turn this off?")
        if stage < 6:
            return _("But the foolish spirit!")
        return _("Okay, fine. Next click.")



init:
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
        default bangok_four_bangnokay_quest=0
        tag smallscreen2
        modal True
        window id "bangok_modsettings" at popup2:
            style "smallwindow_big2"
            if bangok_four_common.bangnokay.check():
                textbutton bangok_four_common.bangnokay_quest_text(bangok_four_bangnokay_quest):
                    yalign 0.06
                    xalign 0.5
                    text_size 44
                    action [
                        Function(bangok_four_common.bangnokay.set_bangnokay, (bangok_four_bangnokay_quest<6)),
                        SetScreenVariable('bangok_four_bangnokay_quest', ((bangok_four_bangnokay_quest+1)%7)),
                    ]
                    style "bangok_four_switch"
            else:
                textbutton "BangOk Mod Settings":
                    yalign 0.06
                    xalign 0.5
                    text_size 44
                    action Function(bangok_four_common.bangnokay.set_bangnokay, True)
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
                    if bangok_four_common.bangnokay.bangnokay_raw:
                        text "Cute Buttons:" xalign 0.5
                    else:
                        text "Fetishes:" xalign 0.5
                        text "If you do not know what an option means, leave it deselected (or look it up at your own peril).":
                            xalign 0.5
                            size 32

                    grid ((bangok_four_common.bangok_four.fetish_count(bangok_four_common.bangnokay.bangnokay_raw)+1)//2) 2:
                        align (0.5,0.5)
                        transpose True
                        spacing 10
                        for fetish in bangok_four_common.bangok_four.fetish_iter(bangok_four_common.bangnokay.bangnokay_raw):
                            vbox:
                                add fetish.get_switch(bangok_four_common.bangnokay.bangnokay_raw)
                                showif bangok_four_common.bangnokay.bangnokay_raw:
                                    text "[fetish.clean_label]"
                                showif not (bangok_four_common.bangnokay.bangnokay_raw):
                                    text "[fetish.label]"
                        if bangok_four_common.bangok_four.fetish_count(bangok_four_common.bangnokay.bangnokay_raw) % 2 == 1:
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

                showif persistent.bangok_dev == True and not (bangok_four_common.bangnokay.bangnokay_raw):
                    text "In-Development scenes may not have conclusions, and {i}will{/i} have paths leading to crashes.":
                        yalign 0.875
                        xalign 0.5
                        size 40

            showif persistent.bangok_dev == True and main_menu and not (bangok_four_common.bangnokay.bangnokay_raw):
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
    image bangok_grey = renpy.display.imagelike.Solid("#808080")

    image bangok_anon_o_ceiling = "bg/in/apts/o_ceil.png"
    
    image bangok_four_bryce1_apartment night = "bg/in/apts/pad_night.png"
    image bangok_four_bryce1_apartment night ceiling = "bg/in/apts/pad_night_ceil.png"

    image bangok_four_xipsum_bedroom normal = "bg/in/apts/ipsum_bedroom.png"
    image bangok_four_xipsum_bedroom_bed = "bg/in/apts/ipsum_bedroom_bed.png"
    image bangok_four_xipsum_bedroom ceiling = "bg/in/apts/ipsum_bedroom_ceiling.png"

    image bangok_four_xsebastian_cave2_dk = im.Recolor("bg/in/cave2_dk.png", 70, 70, 100, 255)

    image bangok_four_library night = im.Recolor("bg/in/bangok_library_night.png", 70, 70, 100, 255)
    image bangok_four_library outside night = im.Recolor("bg/out/town/town5.jpg", 60, 70, 100, 255)

    image bangok_anoney_library_corridor_night = "bg/in/bangok/library_corridor_night.png"
    image bangok_anoney_emeraroom_night = "bg/in/bangok/bangok_anoney_emeraroom_night.png"

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
        bangok_four_common.PersistentConditionalLayer(
            'bangok_cloacas', None,
            None, "cg/bangok/annaxdamion_lab/vaginal.png",
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
        bangok_four_common.PersistentConditionalLayer(
            ('bangok_balls', 'bangok_inflation'), "cg/bangok/annaxdamion_lab/dm_ballz_big.png",
            'bangok_balls', "cg/bangok/annaxdamion_lab/dm_ballz.png",
            None, None
        ),
    ])


    image bangok_four_brycexsebastian = bangok_four_common.LayeredImage([
        bangok_four_common.Always("cg/bangok/brycexsebastian_office/officecut.jpg"),
        bangok_four_common.Attribute('frame',        'frameA', "cg/bangok/brycexsebastian_office/frameA_base.png"),
        bangok_four_common.Attribute('frame',        'frameB', "cg/bangok/brycexsebastian_office/frameB_base.png"),
        bangok_four_common.PersistentConditionalLayer(
            'bangok_balls', "cg/bangok/brycexsebastian_office/frameA_balls.png",
            None, None,
            if_all=['frameA']
        ),
        bangok_four_common.PersistentConditionalLayer(
            'bangok_balls', "cg/bangok/brycexsebastian_office/frameB_balls.png",
            None, None,
            if_all=['frameB']
        ),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeclosed', "cg/bangok/brycexsebastian_office/bryceeyeclosed.png"),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeopen', "cg/bangok/brycexsebastian_office/bryceeyeopen.png"),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeroll', "cg/bangok/brycexsebastian_office/bryceeyeroll.png"),
        bangok_four_common.Attribute('brycemouth',   'brycesmile', "cg/bangok/brycexsebastian_office/brycesmile.png"),
        bangok_four_common.Attribute('cumspill',     'nocum',
            bangok_four_common.PersistentConditionalDisplayable(
                'bangok_balls', "cg/bangok/brycexsebastian_office/frameB_cumcoverup_balls.png",
                None, "cg/bangok/brycexsebastian_office/frameB_cumcoverup.png",
            ),
            default=True,
            if_all=['frameB']
        ),
        bangok_four_common.Attribute('cumspill',     'cum', renpy.display.layout.Null(), if_all=['frameB']),
        bangok_four_common.Attribute('cumspill',     'morecum', "cg/bangok/brycexsebastian_office/frameB_cumspill+.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebcheek',     'sebcheekbulge', "cg/bangok/brycexsebastian_office/frameB_sebcheekbulge.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebthroat',    'sebthroatbulge', "cg/bangok/brycexsebastian_office/frameB_sebthroatbulge.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebeye',       'sebeyeopen', "cg/bangok/brycexsebastian_office/frameB_sebeyeopen.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebeye',       'sebeyeshocked', "cg/bangok/brycexsebastian_office/frameB_sebeyeshocked.png", if_all=['frameB']),
    ])
    image bangok_four_brycexsebastian_lickpanel = bangok_four_common.PersistentConditionalComposite((1920,1200),
        (0,0),"cg/bangok/brycexsebastian_office/lickpanel.png",
        (0,0),bangok_four_common.PersistentConditionalDisplayable('bangok_balls', "cg/bangok/brycexsebastian_office/lickpanel_balls.png", None, None),
    )

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

    image bangok_anoney_emera_sofa = "cg/bangok/xemera2/bangok_anoney_emera_sofa.png"
    image bangok_anoney_emera_presenting = "cg/bangok/xemera2/bangok_anoney_emera_presenting.png"
    image bangok_anoney_emeramassage_night = "cg/bangok/xemera2/bangok_anoney_emeramassage_night.png"

    image bangok_four_remy4_cg tongue female = im.Scale("cg/bangok/remy4/Remy_oral_f.jpg", 3840,2160)
    image bangok_four_remy4_cg tongue male unprotected = im.Scale("cg/bangok/remy4/Remy_oral_m_crop.jpg", 2640,1568)
    image bangok_four_remy4_cg bottom = "cg/bangok/remy4/remy_bottom.jpg"


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
    s "Recalculating arrival coordinates.{cps=2}..{/cps} (Close all menus to continue.)"
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
