init python in bangok_four_lorem3:
    wormtype = None # "legged" or "smooth"


label bangok_four_lorem3_intro:
    Lo think "We should probably head back before it gets too dark. But now that I think about it, we're not far from something else I wanted to try."
    c "Are we sure it's not underwater too?"
    Lo relieved "Ipsum told me about it yesterday."
    Lo think "I doubt it'd fall to ruin like this did."
    c "Okay, what is it?"
    Lo think "Well, it's..."
    $ renpy.pause (0.3)
    Lo shy "It's, ah, I'm not quite sure how to put it tactfully."
    $ renpy.pause (0.8)
    Lo "It's for decreasing, um, sexual sensitivity."
    Lo sad "I wanted to last a little longer the other day. Ipsum recommended this spot to me."
    menu:
        "How does it work?":
            $ renpy.pause (0.5)
        "I'm not feeling anything like that today.":
            $ renpy.pause (0.5)
            Lo think "That's fine. Not sure I wanted to do that anyway."
            jump bangok_four_lorem3_intro_return

    Lo shy "Well I didn't ask Ipsum too many questions..."
    Lo "I thought I'd go and either try it or not."
    Lo think "It's, uh..."
    Lo relieved "Worms. These sorta worm things."
    menu:
        "No thanks.":
            $ renpy.pause (0.5)
            Lo think "That's fine. Not sure I wanted to do that anyway."
            jump bangok_four_lorem3_intro_return
        "How, exactly?":
            $ renpy.pause (0.5)
            Lo think "I'm not completely sure. I guess we'll find out?"
            menu:
                "No thanks.":
                    $ renpy.pause (0.5)
                    Lo think "That's fine. Not sure I wanted to do that anyway."
                    jump bangok_four_lorem3_intro_return
                "I'll try it...":
                    $ renpy.pause (0.5)
        "I'm in.":
            $ renpy.pause (0.5)
    Lo shy "O-Oh? Okay."
    Lo normal "Great."
    c "Lead on."
    Lo "Sure."

label bangok_four_lorem3_wormscene:
    scene bangok_four_forest_clearing at Pan((716, 0), (0, 520), 6.0) with Fade(0.5,1.0,1.0)
    $ renpy.pause(4.5)
    show lorem think at right with dissolve
    Lo "Here. This is the spot."
    m "The patch of forest we were in looked much like any other part of the forest; I couldn't see any signs of anything."
    c "How can you tell?"
    hide lorem with dissolve
    play sound "fx/slide.ogg"
    $ renpy.pause(1.0)
    show lorem think at center with dissolve
    m "Lorem ducked down under the roots of the nearest tree, pulling out a metal box."
    c "More pizza vouchers?"
    Lo think "No. This should be the, ah, guide to the site. And some supplies donated by other users. Condoms and lube."
    Lo normal "Ipsum said it would be in the roots of the relevant tree, so... I guess we're here."
    c "Relevant tree?"
    scene bangok_four_forest_treehole at Pan((0, 0), (0, 837), 5.0) with Fade(0.5,1.0,1.0)
    m "While Lorem popped open the box, I took a closer look at the tree. A hole stood out to me, at a little over my knee height."
    m "In the shadow of the trunk inside the hole, I saw small white forms wriggling around."
    scene bangok_four_forest_clearing at Pan((0, 520), (0, 520), 0.0)
    show lorem relieved at center
    with Fade(0.5,1.0,1.0)
    Lo "Apparently this guide is a print-and-distribute sort of thing, for several, uh, sites."
    Lo think "Did you see any? And did it look like they had legs, or were they just smooth and slimy?"
    menu:
        "I think they had legs.":
            $ renpy.pause (0.5)
            $ bangok_four_lorem3.wormtype = "legged"
        "I think they were smooth.":
            $ renpy.pause (0.5)
            $ bangok_four_lorem3.wormtype = "smooth"
        "I don't think I can do this.":
            $ renpy.pause (0.5)
            Lo sad "H-Honestly? I feel the same way."
            Lo relieved "This guide gets graphic really quickly."
            hide lorem with dissolve
            play sound "fx/slide.ogg"
            m "Lorem put the guide back in the box, shut the lid, then slid it back into its hiding place under the tree."
            show lorem think at center with dissolve
            jump bangok_four_lorem3_intro_return

    play sound "fx/pages.ogg"
    Lo "O-Okay. That makes it... these ones."
    c "What do we do, exactly? Or what do they do?"

    Lo think bangok "W-Well, males can just stick their genitalia inside and... things happen."
    $ renpy.pause(0.3)
    Lo shy bangok "A-And putting just about any orifice up to the opening..."
    $ renpy.pause(0.8)
    Lo relieved bangok "I-I don't know. Apparently It's supposed to feel amazing. And it's safe becase o-once you're spent they'll just... leave and go back."
    Lo shy bangok "And sex with someone else with them is supposed to feel even more amazing?"
    Lo relieved "I'm not sure we should be doing this. I don't want to pressure you. W-We can just go home."
    menu:
        "Let's forget about it.":
            $ renpy.pause (0.5)
            Lo sad "Oh. Thanks."
            hide lorem with dissolve
            play sound "fx/slide.ogg"
            m "Lorem put the guide back in the box, shut the lid, then slid it back into its hiding place under the tree."
            show lorem think at center with dissolve
            jump bangok_four_lorem3_intro_return
        "I'll try it.":
            pass






label todo_out_of_content_bangok_four_lorem3:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")