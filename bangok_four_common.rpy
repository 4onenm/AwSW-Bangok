init:
    image bangok_four_bryce1_apartment night = "bg/in/apts/pad_night.png"
    image bangok_four_bryce1_apartment night ceiling = "bg/in/apts/pad_night_ceil.png"

    image bangok_four_bryce_underside_large dk = im.Recolor("cr/bryce_underside_large.png", 70, 70, 100, 255)
    image bangok_four_bryce_underside_large dk flip = im.Recolor(im.Flip("cr/bryce_underside_large.png",horizontal=True), 70, 70, 100, 255)

init python:
    # First time per run, obv.
    bangok_four_firsttime = True
    bangok_four_bryce1_unplayed = True
    bangok_four_bryce1_protected = False
    bangok_four_bryce1_playercame = False
    bangok_four_bryce1_position = None
    bangok_four_bryce1_wstiming = None
    bangok_four_bryce1_analknot = None