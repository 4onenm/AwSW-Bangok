init python in bangok_four_lorem4_store:
    # Position enumeration
    # "ride" - Lorem rides the player cowgirl
    # "carry" - The player picks Lorem up, to be in control of the fuck.
    position = None

    # Protection
    # None - not suggested
    # False - Rejected
    # True - Applied
    protection = None

    condom_left_in = False

    # Whether Lorem will have their penis on display for relevant scenes,
    #  and what the player might be doing with it.
    # None - no decision, merely hanging out
    # "stroke" - Player is toying with Lorem's shaft
    # "hidden" - Player asked Lorem to hide their shaft
    lorem_pen = None

    # Where the player has relieved themselves, if anywhere.
    # None - Still got a full bladder.
    # "toilet" - Wasted.
    # "throat" - Lorem's got a full belly.
    # "vag" - Lorem's got a full canal/womb.
    player_pissed = None

    # Whether the player plans to fuck Lorem's womb. True/False
    cerv_pen = False


    def lorem_filled_expression(emotion):
        if protection == True:
            if renpy.store.persistent.bangok_inflation == True and condom_left_in == True:
                im = 'lorem '+emotion+' bangok bulge erect'
            else:
                im = 'lorem '+emotion+' bangok erect'
        elif renpy.store.persistent.bangok_inflation == True:
            if renpy.store.persistent.bangok_watersports == True and player_pissed == "vag":
                im = 'lorem '+emotion+' bangok bulge pissleak'
            else:
                im = 'lorem '+emotion+' bangok bulge cumleak'
        else:
            if renpy.store.persistent.bangok_watersports == True and player_pissed == "vag":
                im = 'lorem '+emotion+' bangok pissleak'
            else:
                im = 'lorem '+emotion+' bangok cumleak'

        renpy.show(im, at_list=[renpy.store.center])


label bangok_four_lorem4_feelbetter:
    menu:
        "About making you feel better...":
            $ renpy.pause (0.5)
            Lo think "What do you mean?"
            c "Well, I may not be able to do anything about how your world is, and how other dragons are."
            c "But you don't have to go back to that right now. There's nothing I've been told saying I can't have guests overnight."
            $ renpy.pause (0.5)
            Lo "I don't..."
            $ renpy.pause (0.5)
            Lo shy bangok peek "W-Wait, you mean... You're suggesting you'd be willing to... with me..."
            Lo bangok hidepeek flip "E-Even though I..."
            $ renpy.pause (0.8)
            menu:
                "Accept.":
                    $ renpy.pause (0.5)
                    c "Let me just say it again to be clear: I don't mind."
                    c "It's just a part of who you are, and I'm okay with that -- with you."
                    $ renpy.pause (0.5)
                    Lo shy bangok peek "Um.{w=0.3} Well, in that case..."
                    jump bangok_four_lorem4
                "Reject.":
                    c "OH! No, no, that's not what I meant."
                    Lo relieved "Oh. Oh, right. That makes more sense."
                    if bangok_four_xipsum.loremin == True:
                        c "I'm not saying I'm opposed. Obviously there was last time. But I didn't mean to sound like I was pressuring you into anything right after you opened up to me."
                    else:
                        c "Maybe. Maybe at some point. But I didn't mean to sound like I was pressuring you into anything right after you opened up to me."
                    Lo "Yeah. I get it."
                    show lorem normal with dissolve
                    Lo "I think I'd rather go home for the night."
        "[[Say Nothing.]":
            pass
    jump bangok_four_lorem4_feelbetter_return

label bangok_four_lorem4:
    $ loremstatus = "good"
    if (bangok_four_playerhasdick is None) or (bangok_four_xipsum.loremin == False):
        Lo think bangok "I should probably ask whether you're... ah... what you have to work with."
        if bangok_four_playerhasdick is None:
            menu:
                "I have a penis.":
                    $ bangok_four_playerhasdick = True
                "I have a vagina.":
                    $ bangok_four_playerhasdick = False
            $ renpy.pause (0.5)
        elif bangok_four_playerhasdick == True:
            c "I have a penis."
        else:
            c "I have a vagina."

    show lorem shy bangok peek with dissolve

    if bangok_four_playerhasdick == True:
        jump bangok_four_lorem4_maleplayer
    else:
        $ renpy.pause (0.5)
        Lo relieved "No. I'm sorry, I'm just not feeling up to this."
        c "You don't have to apologize. I was just opening the possibility for you."

        if persistent.bangok_dev == True:
            play sound "fx/system3.wav"
            s "Hello, dev tester! {w}This isn't actually how this scene is planned long-term. There {i}should{/i} be a female MC version. Unfortunately, that's not something the author has experience with!"
            play sound "fx/system3.wav"
            s "We're waiting on a female version script (which {i}you{/i} could write!) In the meantime, though, would you like to see this scene as a male? Or accept the way things are going?"
            menu:
                "Yes, Let me see the scene as a male player.\n(Temporary, will revert after this scene.)":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

                    show black with dissolvemed
                    show lorem shy bangok peek with dissolve
                    hide black with dissolvemed

                    jump bangok_four_lorem4_maleplayer
                "No, let Lorem back out of it.":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

        Lo sad "I appreciate that. But I don't really want to use my male side tonight, after admitting it's not all of me."
        Lo relieved "And I really don't want claws digging around inside me, no matter how short."

        c "That's fine, Lorem."

        $ renpy.pause (0.3)
        show lorem sad with dissolve
        $ renpy.pause (0.8)
        show lorem normal with dissolve
        Lo "Thanks, though, for offering. It... means a lot to me that you're so comfortable with it."

        c "Of course."
        jump bangok_four_lorem4_feelbetter_return

label bangok_four_lorem4_maleplayer:
    if bangok_four_xipsum.clothesoff == False:
        Lo think bangok peek "Then, ah, if we're going to do something, may I see it?"
    else:
        Lo think bangok peek "I know I saw it before, but may I see it again? I'm not sure if..."
    c "You want me to strip?"
    Lo shy bangok peek "I just want to know,{w=0.3} uhm,{w=0.3} what I'm agreeing to before I make a decision."

    show o2 at Pan((0, 200), (0, 200), 0.0)
    show lorem:
        ypos 1.05
    with ease
    m "I stood from the couch, checked Lorem's face one more time for approval, then undressed."
    play sound "fx/undress.ogg"
    $ renpy.pause (1.0)
    show lorem think bangok peek with dissolve
    $ renpy.pause (0.5)
    show lorem normal bangok peek with dissolve
    Lo normal bangok peek "Alright. If you want to, then I want to, too."

    hide lorem with dissolve
    $ renpy.pause (0.3)
    show o2 at Pan((100, 120), (100, 120), 0.1) with ease
    $ renpy.pause (0.3)
    show lorem normal bangok peek at center:
        zoom 0.8
        xpos 0.6
        ypos 1.04
    with dissolve
    m "Lorem hopped to the table in front of me, pushing the remains of the pizza out of the way before turning to inspect me."
    show lorem think bangok peek with dissolve
    $ renpy.pause (0.5)
    Lo "You're quite a lot larger than I am. I don't want to be crushed, so do you mind sitting down so I could climb on and... ride?"
    menu:
        "Sounds good to me.":
            $ renpy.pause (0.5)
            $ bangok_four_lorem4_store.position = "ride"
            show o2 at Pan((100, 150), (100, 150), 0.1) with ease
            $ renpy.pause (0.3)
            m "I sat back down upon the couch, now in the nude, and spread my legs for Lorem to take a closer look."
        "I think I could pick you up, instead.":
            $ renpy.pause (0.5)
            $ bangok_four_lorem4_store.position = "carry"
            Lo shy bangok peek "O-Oh!"
            Lo normal bangok peek "I think I'd like that. Sure."
            Lo think bangok peek "But not quite yet. Let me take a closer look, first."
    show lorem normal bangok peek:
        ease 0.5 zoom 0.9 ypos 1.05
    m "Lorem stepped up to the edge of the table, then reached out to gently squeeze the tip of my not-quite-hard shaft."
    m "It twitched as the action elicited a rush of blood to my groin."
    if bangok_four_xipsum.clothesoff == False:
        Lo think bangok peek "Is it supposed to be that soft?"
        m "No. Once we get going a little more, and I get more aroused, I should get fully hard."
        $ renpy.pause (0.5)
    else:
        Lo think bangok peek "Ipsum mentioned something about bloodflow arousal, since you're a mamalian species."
    Lo "Maybe I could get you harder with my hands?"
    $ bangok_four_lorem4_store.protection = None
    label bangok_four_lorem4_maleplayer_startingposition:
    menu:
        "Or your mouth." if bangok_four_lorem4_store.protection is None or bangok_four_lorem4_store.protection:
            $ renpy.pause (0.5)
            Lo happy bangok peek "That I can do."
            jump bangok_four_lorem4_maleplayer_blowjobstart
        "You could use your mouth." if bangok_four_lorem4_store.protection == False:
            $ renpy.pause (0.5)
            Lo happy bangok peek "Oh?"
            jump bangok_four_lorem4_maleplayer_blowjobstart
        "Alright, yeah. A handjob to start.":
            $ renpy.pause (0.5)
            jump bangok_four_lorem4_maleplayer_handjobstart
        "We should probably get protection on." if bangok_four_lorem4_store.protection is None:
            $ renpy.pause (0.5)
            if bangok_four_xipsum.unplayed == False:
                Lo think bangok peek "Ipsum said the samples he took from you when you two hooked up told him that \"hooking up\" without protection should be perfectly safe."
                Lo "The same should apply for us, too."
                menu:
                    "I'd prefer to have it anyway.":
                        $ renpy.pause (0.5)
                        $ bangok_four_lorem4_store.protection = True
                    "In that case, unprotected.":
                        $ renpy.pause (0.5)
                        $ bangok_four_lorem4_store.protection = False
                        Lo normal bangok peek "Okay. Now about getting you more aroused..."
            else:
                Lo think bangok peek "I mean, different dragon species can't get one another pregnant. You're an even more different species."
                Lo normal bangok peek "We don't need it."
                menu:
                    "I'm worried about diseases, not pregnancy.":
                        $ renpy.pause (0.5)
                        $ bangok_four_lorem4_store.protection = True
                        c "A bacteria that's perfectly normal for me could be dangerous for your private bits -- or vice versa."
                        Lo relieved "Oh. That would be bad."
                    "In that case, unprotected.":
                        $ renpy.pause (0.5)
                        $ bangok_four_lorem4_store.protection = False
                        Lo normal bangok peek "Okay. Now about getting you more aroused..."

            if bangok_four_lorem4_store.protection == True:
                show lorem normal:
                    ypos 1.1
                with ease
                Lo "Alright, I'll go find some condoms."
                play sound "fx/run.ogg"
                hide lorem with easeoutleft
                stop sound fadeout 0.5
                $ renpy.pause (1.0)
                play sound "fx/run.ogg" fadein 0.5
                show lorem normal bangok peek flip at center:
                    zoom 0.9
                    xpos 0.6
                    ypos 1.1
                with easeinleft
                stop sound fadeout 0.1
                $ renpy.pause(0.2)
                Lo "Got one."
                show lorem think bangok peek:
                    ypos 1.05
                with ease
                m "Hopping up on the table, Lorem tore open the condom packet then, after a glance up at me to confirm, set the condom to my tip and rolled it down with their fingertips."
                Lo "There."
                Lo shy bangok peek "Now I'll just keep going with my hands...?"
    jump bangok_four_lorem4_maleplayer_startingposition

label bangok_four_lorem4_maleplayer_handjobstart:
    show lorem:
        ypos (1080+516)
        ease 0.5 zoom 1.2
    with ease
    if bangok_four_lorem4_store.protection == True:
        m "Lorem leaned further forward, balancing one hand against my hips while stroking their other down my condom-wrapped legnth."
    else:
        m "Lorem leaned further forward, balancing one hand against my hips while stroking their other down my slightly soft legnth."
    m "Not yet hard enough for the stroke, my cock twisted and bent back a little in their hand."
    show lorem shy bangok peek:
        ypos 1.05
        ease 0.5 zoom 0.9
    with ease
    m "Lorem yelped and hopped back, letting go."
    Lo "D-Did I break it? A-Are you okay?"
    c "What?"
    Lo think "Your baculum."
    c "Oh. Humans don't have one of those."
    Lo shy "You..."
    Lo relieved "Oh."
    show lorem shy bangok peek with dissolve
    $ renpy.pause(0.3)
    show lorem:
        ypos (1080+516)
        ease 0.5 zoom 1.2
    with ease
    m "Leaning back in, Lorem began to knead my shaft more gently, using smaller strokes and more pressure with the rough, scaly surface of their hand."
    m "My breath caught as, under their ministrations, my shaft twitched to full attention."
    Lo normal "That's feeling better."
    c "Y-Yeah."

    if bangok_four_lorem4_store.position == "ride":
        $ renpy.pause(0.5)
        show lorem happy bangok erect with dissolve
        show lorem:
            ypos 1.0
        with ease
        if persistent.bangok_cloacas == True:
            m "After a few more moments, Lorem braced their other hand on my hips, then hopped forward to stand upright on my legs, revealing the full extent of the shaft now emerging from their cloaca."
        else:
            m "After a few more moments, Lorem braced their other hand on my hips, then hopped forward to stand upright on my legs, revealing the full extent of the shaft now emerging from their slit."
        jump bangok_four_lorem4_maleplayer_ride
    else: # "carry"
        $ renpy.pause(0.5)
        jump bangok_four_lorem4_maleplayer_carry


label bangok_four_lorem4_maleplayer_blowjobstart:
    Lo shy bangok peek "I wasn't sure if you wanted that while soft-ish like this, but sure."
    show lorem:
        ypos (1080+780)
        ease 0.5 zoom 1.5
    with ease
    m "Lorem leaned forward off the table, grabbing my hips."
    if bangok_four_lorem4_store.protection == True:
        m "They took my wrapped tip between their finely pebbled lips with what seemed like practiced ease, before their tongue snaked out to dig and explore."
    else:
        m "They took my tip between their finely pebbled lips with what seemed like practiced ease, before their tongue snaked out to dig and explore."
    show lorem happy with dissolve

    m "It was all I could do not to thrust my hips forward. Lorem seemed to have planned for this, as their hands on either side of their head kept him easily at the same depth, licking and nibbling."

    menu:
        "{i}D-Deeper...{/i}":
            $ renpy.pause(0.5)
            show lorem blush:
                ypos (1080+516)
                ease 0.5 zoom 1.2
            with ease
            m "Lorem backed off with an awkward smile."
            Lo "Ipsum does say I'm good at that. But if you get off in my mouth, I don't get to have you where I want you."
            c "Fine..."
        "I th-think I'm hard now.":
            $ renpy.pause(0.5)
            show lorem:
                ypos (1080+516)
                ease 0.5 zoom 1.2
            with ease
            m "Lorem backed off with a wide smile."
            Lo "Ipsum does say I'm good at that."
        "{i}A-Ah{/i}! I forgot I have to piss!" if persistent.bangok_watersports == True:
            $ renpy.pause(0.5)
            show lorem think:
                ypos (1080+516)
                ease 0.5 zoom 1.2
            with ease
            m "Lorem backed off, releasing my shaft from their mouth."
            c "Do you mind? Or should I run over to the restroom?"
            Lo blush "Oh, you mean..."
            Lo think "Well, Ipsum \"forgets\" sometimes too."
            Lo "It's definitely... a... different experience."
            Lo normal blush "Can you hold it until you're, ah, between my legs?"
            menu:
                "You want it in there? Sure, I can hold it.":
                    $ renpy.pause (0.5)
                    if bangok_four_lorem4_store.protection == True:
                        Lo think "..."
                        c "Something wrong?"
                        Lo relieved "Now that I think about it, your warning about bacteria, and the possibility of a condom-ful of it down there? I just don't think it's a good idea."
                        c "So that's a no on this?"
                        Lo "Yeah."

                        show black with dissolve
                        play sound "fx/door/doorclose3.wav"
                        m "Jumping up, I scrambled into the restroom and poured my bladder into the toilet, replacing my condom after I was done."
                        $ renpy.pause(1.0)
                        $ bangok_four_lorem4_store.player_pissed = "toilet"
                        hide black
                        with dissolvemed
                        c "... so, where were we?"
                    else:
                        $ bangok_four_lorem4_store.player_pissed = "vag"
                        Lo normal "Thanks."
                "I gotta go now. Please may I use your mouth?":
                    if bangok_four_lorem4_store.protection == True:
                        Lo relieved "I don't want a condom full of piss blocking my throat."
                        menu:
                            "I'll take it off for this. Please?":
                                $ renpy.pause (0.5)
                                Lo blush "A-Alright."
                                m "I stripped off my condom, but Lorem still hesitated."
                            "[[Give up.]":
                                show black with dissolve
                                play sound "fx/door/doorclose3.wav"
                                m "Jumping up, I scrambled into the restroom and poured my bladder into the toilet, replacing my condom after I was done."
                                $ renpy.pause(1.0)
                                $ bangok_four_lorem4_store.player_pissed = "toilet"
                                hide black
                                with dissolvemed
                                c "... so, where were we?"
                                # play sound "fx/faucet2.ogg" fadein 0.8
                                # $ renpy.pause(0.5)
                                # show lorem shy with dissolve
                                # m "With a groan I let go of my bladder, pissing into the condom until the tip had become a warm, round bubble of liquid waste."
                                # $ renpy.pause(0.3)
                                # stop sound fadeout 0.5
                                # Lo "I'll go grab a new one."
                    if bangok_four_lorem4_store.player_pissed != "toilet":
                        Lo think "I'm not a huge fan of the taste, though. So, ah, could you, um...{w=0.3}{nw}"
                        Lo normal blush "I'm not a huge fan of the taste, though. So, ah, could you, um...{fast} pull me deeper by my horns? To make sure it just goes down my throat?"
                        if bangok_four_hornincident == True:
                            c "Isn't that a sensitive spot?"
                            Lo blush "Yes, but I want you to."
                        c "Sure. Yep. Just--"
                        show lorem:
                            ypos (1080+780)
                            ease 0.5 zoom 1.5
                        with ease
                        m "Taking a deep breath, Lorem dove down my hard shaft, taking the whole thing into their mouth."
                        $ bangok_four_lorem4_store.player_pissed = "throat"
                        show lorem sleep blush:
                            ypos (1080+810)
                        with ease
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        m "Letting out a moan, I pulled Lorem closer like they'd asked, then let my bladder go directly down their throat."
                        $ renpy.pause (2.0)
                        stop soundloop fadeout 0.8
                        m "Lorem took it all, swallowing actively until my stream turned into a trickle, then finally stopped."
                        show lorem normal blush:
                            ypos (1080+516)
                            ease 0.5 zoom 1.2
                        with ease
                        m "Then they pushed themselves back, as I gently released their horns."
                        $ renpy.pause (0.5)
                        Lo "More filling than Pantolli's."
                        if bangok_four_lorem4_store.protection == True:
                            if bangok_four_xipsum.unplayed == False:
                                m "The joke caught me off-guard, my reaction earning me a slightly wider smile from Lorem."
                            else:
                                Lo think "That might've been a bad idea, considering what you said about bacteria."
                                c "Maybe."
                            $ renpy.pause (0.5)
                            Lo think "Do you want that condom back on?"
                            menu:
                                "No point now.":
                                    $ bangok_four_lorem4_store.protection = False
                                "Yeah, I'm going to put it back on.":
                                    $ bangok_four_lorem4_store.protection = True
                            $ renpy.pause (0.5)
                        else:
                            m "The joke caught me off-guard, my reaction earning me a slightly wider smile from Lorem."


    if bangok_four_lorem4_store.position == "ride":
        $ renpy.pause(0.5)
        show lorem happy bangok erect with dissolve
        show lorem:
            ypos 1.0
        with ease
        if persistent.bangok_cloacas == True:
            m "Lorem hopped forward to stand upright on my legs, revealing the full extent of the shaft now emerging from their cloaca."
        else:
            m "Lorem hopped forward to stand upright on my legs, revealing the full extent of the shaft now emerging from their slit."
        jump bangok_four_lorem4_maleplayer_ride
    else:
        $ renpy.pause(0.5)
        jump bangok_four_lorem4_maleplayer_carry


label bangok_four_lorem4_maleplayer_ride:
    Lo happy bangok erect "Ready?"
    menu:
        "[[Stroke their shaft.]":
            $ renpy.pause (0.5)
            $ bangok_four_lorem4_store.lorem_pen = "stroke"
            m "Reaching forward, I gently took Lorem's shaft into my hand."
            Lo shy bangok erect "O-Oh!"
        "Yeah.":
            $ renpy.pause (0.5)
        "Why is your penis out?":
            $ renpy.pause (0.5)
            Lo think bangok erect "What?"
            $ renpy.pause (0.3)
            Lo relieved bangok erect "Oh."
            $ renpy.pause (0.3)
            Lo sad bangok erect "I only have so much room down there."
            Lo think bangok erect "Plus, when I'm this aroused, I kinda have to think about not pushing it out."
            Lo sad bangok erect "But if it's turning you off..."
            menu:
                "I'm kinda curious what you feel like, that tight.":
                    $ renpy.pause (0.3)
                    $ bangok_four_lorem4_store.lorem_pen = "hidden"
                    show lorem shy bangok erect with dissolve
                    c "If it's easier to have it out, I don't want to impose..."
                    Lo "O-Oh. I mean, we could try it."
                    Lo relieved bangok erect "Here I thought you were upset by it."
                    c "No, of course not. It's just another thing that makes you, you."
                    Lo normal bangok erect "Okay."
                "Not a problem at all. I was just wondering.":
                    $ renpy.pause (0.5)
                    $ bangok_four_lorem4_store.lorem_pen = None
                    Lo shy bangok erect "O-Oh."
                    Lo normal bangok erect "Okay. Good."
                "[[Stroke them.]":
                    $ renpy.pause (0.5)
                    $ bangok_four_lorem4_store.lorem_pen = "stroke"
                    m "Reaching forward, I gently took Lorem's shaft into my hand."
                    Lo shy bangok erect "O-Oh!"
                "Yeah, I'd prefer if you hide it.":
                    $ renpy.pause (1.0)
                    $ loremstatus = "neutral"
                    $ lorem4pick = "whattosay"
                    Lo relieved bangok erect "That's fair."
                    Lo sad bangok erect "Saying you don't mind is one thing. Having to interact with it like this?"
                    Lo relieved bangok erect "I get it."
                    $ renpy.pause (0.5)
                    Lo sad bangok peek "..."
                    $ renpy.pause (0.5)
                    Lo sad bangok peek "I'm sorry, [player_name]. I can't do this."
                    Lo "There's no way to hide it away completely."
                    Lo relieved bangok peek "Unless I'm not actually enjoying it, I'll get off too."
                    Lo sad "If what my male parts put out when I cum is going to upset you, then I should just go."
                    c "Lorem..."
                    jump bangok_four_lorem4_canon_callmelater

            if bangok_four_lorem4_store.lorem_pen == 'hidden':
                $ renpy.pause (0.3)
                show lorem think bangok erect with dissolve
                $ renpy.pause (0.5)
                show lorem think bangok peek with dissolve
                $ renpy.pause (0.5)
                show lorem normal bangok peek with dissolve
                Lo "There."

    if bangok_four_lorem4_store.lorem_pen == "stroke":
        show lorem shy bangok erect with dissolve
        $ renpy.pause(0.3)
        show lorem:
            ypos 1.2
        with ease
        $ renpy.pause(0.3)
        m "Their legs shaking a little under my ministrations, Lorem got on their knees atop my legs, lining themselves up with my tip."
    else:
        if bangok_four_lorem4_store.lorem_pen == "hidden":
            show lorem shy bangok peek with dissolve
        else:
            show lorem shy bangok erect with dissolve
        $ renpy.pause(0.3)
        show lorem:
            ypos 1.2
        with ease
        $ renpy.pause(0.3)
        m "Lorem got down on their knees atop my legs, lining themselves up with my tip."

    if bangok_four_lorem4_store.protection == True:
        m "Through the condom, I could feel my tip sliding against Lorem's moist slit as their breathing came faster."
    else:
        m "Lorem's slit was moist and slick, my tip sliding about a little against the outer opening as their breathing came faster."
    c "It's okay."
    Lo "I-I know. I'm just nervous."

    $ renpy.pause(0.8)
    if bangok_four_lorem4_store.lorem_pen is None or bangok_four_lorem4_store.lorem_pen == "stroke":
        show lorem:
            ease 1.5 ypos 1.3
        with None
        $ renpy.pause(0.5)
        m "After a few long moments they began to sink down onto me, spreading their tight slit taut around my hard length."
    else:
        show lorem:
            ease 1.0 ypos 1.25
        with None
        $ renpy.pause(0.5)
        m "After a few long moments they began to sink down onto me, pressing their impossibly tight slit taught against my tip."
        show lorem scared with dissolve
        m "The protruding tip of their dragonhood pressed against my head, blocking my entry as the rest of their snatch failed to stretch to accomodate."
        Lo "Nngh! T-Too big!"
        show lorem relieved bangok peek with dissolve
        $ renpy.pause(0.3)
        show lorem:
            ypos 1.2
        with ease
        m "Unwilling to risk injuring them, I grabbed Lorem's hips and helped them lift off of me."
        c "Are you okay?"
        Lo "Yeah. I just... can't fit you and my male parts at the same time."
        Lo sad bangok peek "I did warn you I don't have much room."
        c "That's fine. I was curious, now I know that doesn't work for you. Go ahead and let it back out."
        $ renpy.pause(0.3)
        show lorem think bangok peek with dissolve
        $ renpy.pause(0.3)
        show lorem think bangok erect with dissolve
        $ renpy.pause(0.3)
        c "Do you want to keep going?"
        Lo normal bangok erect "Yeah."
        show lorem:
            ease 1.5 ypos 1.3
        with None
        $ renpy.pause(0.5)
        m "Readjusting the position of their knees to line back up, they began to sink down onto me, spreading their tight entrance all-but taut around my hard length."
    show lorem blush:
        ypos 1.3
    with dissolve
    Lo "Mmh. Ohhh..."

    if bangok_four_lorem4_store.protection == True:
        m "They twisted a little as they sank down, inner walls massaging the upper half of my length and spreading their lubrication thoroughly over the condom's surface."
    else:
        m "They twisted a little as they sank down, inner walls massaging the upper half of my length and spreading their lubrication thoroughly across my cockflesh."

    menu:
        "How does it feel?":
            $ renpy.pause (0.5)
            if bangok_four_xipsum.loremin == True:
                Lo normal blush "You're bigger than Ipsum."
                c "In a good way, or...?"
                Lo blush "Yes. A very good way."
            Lo think blush "I'm honestly not sure I'll be able to fit all of you."
            if bangok_four_lorem4_store.lorem_pen == "stroke":
                Lo normal blush "Don't stop what you're doing with my male parts, though."
        "[[Give a small thrust.]":
            $ renpy.pause (0.5)
            show lorem scared:
                ease 0.3 ypos 1.31
                ease 0.5 ypos 1.25
            with None
            $ renpy.pause (1.0)
            show lorem scared:
                ypos 1.3
            with ease
            m "When I thrust, even with the slight amount of force, Lorem's legs gave a little and I sank in deeper, bumping up against something within them."
            Lo "C-Careful!"
            Lo relieved "I'm only so deep."
            Lo sad "Let me figure it out? Please?"
            c "Sorry."
            $ renpy.pause (0.5)
            show lorem blush with dissolve
            show lorem:
                ease 1.0 ypos 1.3
            with None
            $ renpy.pause (0.5)
            if bangok_four_lorem4_store.lorem_pen == "stroke":
                m "After a few moments, as I resumed stroking Lorem's shaft, they blushed, and I felt them clench lightly around me, mistake forgiven."
            else:
                m "After a few moments, Lorem sank slowly back to their previous depth, and I felt them clench lightly around me, mistake forgiven."
            show lorem:
                ypos 1.3
            with ease
        "[[Stroke their shaft.]" if bangok_four_lorem4_store.lorem_pen != "stroke":
            $ renpy.pause (0.5)
            show lorem blush with dissolve
            $ bangok_four_lorem4_store.lorem_pen = "stroke"
            m "Reaching forward, I gently took Lorem's shaft into my hand."
            Lo shy bangok erect "O-Oh!"
            Lo blush "K-Keep doing that."
        "{i}A-Ah{/i}! I forgot I have to piss!" if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed is None and bangok_four_lorem4_store.protection == False:
            $ bangok_four_lorem4_store.player_pissed = "vag"
            Lo blush "Oh, you mean..."
            Lo think blush "Well, Ipsum \"forgets\" sometimes too."
            Lo "It's definitely... a... different experience."
            Lo blush "Just give me a little longer, first? To get used to you?"
            c "O-Okay..."



    $ renpy.pause(0.3)
    show lorem blush:
        ypos 1.3
        ease 0.8 ypos 1.3
        pause 0.1
        ease 0.4 ypos 1.325
        pause 0.2
        repeat
    with None
    $ renpy.pause(1.0)
    m "They squeezed their legs together, pushing themselves a little up the upper half of my shaft before letting themselves slide back down."

    Lo "Y-Yeah.{w} Ohh.{w} This is...{w}"
    Lo normal blush "[player_name] I...{w} Thank you.{w}"

    $ renpy.pause(1.0)
    c "Same to you."
    c "We wouldn't be here, experiencing this together if you hadn't been brave enough to open up."
    Lo blush "Mmh.{w} Yeah.{w}"

    $ renpy.pause(1.0)

    if persistent.bangok_cervpen == True:
        menu:
            "Can you take me deeper?":
                $ renpy.pause(0.5)
                Lo relieved "Not while keeping use of my legs."
                Lo blush "That kind of thing is too much for me."
                c "Okay."
                $ renpy.pause (1.0)
            "[[Enjoy.]":
                $ renpy.pause (1.0)

    if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
        c "I-I've still gotta go."
        show lorem blush:
            ypos 1.3
        with ease

        m "Lorem came to a stop, steadying themself with hands on my chest."
        Lo "Okay. Start slow, though. I'm sensitive down there."

        $ renpy.pause(0.5)
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        show lorem relieved shy with dissolve
        m "Gently taking hold of their hips, I let my bladder go, leaking warm, golden liquid into Lorem's tight passage."
        Lo "OH! H-ha.{w} S-So warm."
        m "I gradually let my stream come out faster, as I felt my piss pooling around my tip."
        show lorem normal blush eyes with dissolve
        m "Lorem raised a hand to their lower stomach."
        Lo normal blush eyes "S-So much..."
        if persistent.bangok_inflation == True:
            show lorem normal blush eyes brows with dissolve
            stop soundloop fadeout 1.0
            m "As my stream petered out, Lorem's belly expanded slightly under their hand."
            Lo "I-It's stretching my womb."
        else:
            m "As my stream petered out, Lorem's breathing hitched."
            Lo blush "Th-That felt amazing."
        Lo blush "And you haven't even cum yet."
        c "Ready for more?"
        Lo normal blush "So ready."


    jump todo_out_of_content_bangok_four_lorem4


label bangok_four_lorem4_maleplayer_carry:
    show lorem shy bangok erect with dissolve
    show lorem:
        ypos 1.1
        ease 0.5 zoom 1.6
    with ease
    m "Leaning down, I scooped up Lorem under their arms, hoisting him up to my height."
    m "Between us, their dragonhood poked at my stomach, hard and wet. Mine rubbed one of their thighs."
    c "Ready?"
    m "Lorem got their arms up, gripping my shoulders."
    Lo normal bangok erect "Yeah."

    show lorem:
        ypos 1.09
    with ease
    m "I lifted Lorem up, lining up with the slick slit just behind where their shaft emerged."
    show lorem:
        ypos 1.09
        ease 1.5 ypos 1.21
    with None
    m "Then I let Lorem down, sinking inside their tight passage with ease and care."
    Lo sleep blush "Mmmmnh. Ohh..."
    m "Then, at little more than half my shaft's length, I bumped against something inside them."
    Lo scared "A-Ah! T-Too far!"
    show lorem sad:
        ypos 1.2
    with ease
    m "I lifted Lorem slightly, not trying to hurt them."
    Lo relieved "That was my cervix."

    if persistent.bangok_cervpen == True:
        $ bangok_four_lorem4_store.cerv_pen = False
        menu:
            "Can you take me any deeper?":
                $ renpy.pause(0.8)
                Lo sad "Well, no. I'm not really..."
                Lo think blush "Do you want me to?"
                Lo sad "I'm not really sure. I'm so sensitive there, I just ask Ipsum not to."
                Lo "Do you want to?"
                menu:
                    "Please?":
                        $ renpy.pause(0.5)
                        $ bangok_four_lorem4_store.cerv_pen = True
                    "You don't have to do anything you don't want to do.":
                        $ renpy.pause(0.5)
                        $ bangok_four_lorem4_store.cerv_pen = True
                        Lo relieved "But I want you to feel good from this, too."
                        c "Tonight's about you."
                        Lo blush "Not {i}just{/i} me."
                        Lo "I wouldn't get to do this with you if you didn't offer."
                        c "I'm feeling it too."
                        c "You're not doing anything wrong by saying no. I was just asking."
                        $ renpy.pause(0.5)
                        Lo think blush "..."
                        $ renpy.pause(0.5)
                    "Nevermind.":
                        Lo blush "Okay. Thanks."
            "Too sensitive for you?":
                Lo sad "Yeah, if you could avoid... you know..."
                c "Of course."
    else:
        c "Got it. Not that deep."



    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
        Lo think blush "Okay. I mean... I... I'll try it."
        Lo sad "But if it doesn't work for me, or doesn't fit..."
        c "Yeah, sure."
        Lo normal blush "Okay."

        show lorem blush with dissolve
        $ renpy.pause(0.5)
        show lorem blush:
            ease 1.0 ypos 1.21
        m "Adjusting my grip on Lorem, I gently began to pull them further down my length, until again I arrived at the obstruction within them."
        Lo scared "Mmmngh!"
        menu:
            "[[Continue.]":
                $ renpy.pause (0.5)
            "Are you okay?":
                $ renpy.pause (0.5)
                Lo scared "F-Fine? I-Is it almost--?"
                menu:
                    "Continue.":
                        $ renpy.pause (0.5)
                    "Stop.":
                        jump bangok_four_lorem4_maleplayer_carry_cerv_pen_abort
            "[[Stop.]":
                label bangok_four_lorem4_maleplayer_carry_cerv_pen_abort:
                $ bangok_four_lorem4_store.cerv_pen = False
                m "I lifted Lorem off, unwilling to press any farther when they were clearly in pain."
                show lorem relieved:
                    ypos 1.2
                with ease
                $ renpy.pause (0.5)
                Lo "Okay, that really hurt."
                c "I could see that."
                Lo sad "Maybe we don't do that again?"
                c "Definitely."
                Lo normal "Thanks."

    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
        m "Having finally applied enough force, Lorem's cervix began to give."
        Lo relieved shy "OUGH!"
        show lorem relieved shy:
            ypos 1.23
        with ease
        m "My cockhead pushed through, squeezed vice-like by their innermost gate as I pulled them fully around me."
        m "My hips spread their legs wide as their slippery, spread slit met my cock's base, my cockhead nestling in the far wall of their womb."
        c "Ohhh..."
        $ renpy.pause (0.5)
        c "Lorem?"
        Lo "I..."
        Lo "S-So big..."
        c "Like it?"
        show lorem shy with dissolve
        m "Lorem nodded, evidently beyond words."

    if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
        if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
            $ renpy.pause (0.5)
            c "... so I still have to go."
            Lo "O-Oh. Hm."
            Lo blush "N-Not sure I h-have room now."
            Lo think blush "But I don't want you to pull back out either."
            Lo think blush "I guess just s-start--"
            play soundloop "fx/faucet1.ogg" fadein 1.0
            queue soundloop "fx/faucet2.ogg"
            show lorem relieved shy with dissolve
            m "Nestled against the back of their womb as I was, my piss flowed back around my cockhead, thoroughly defiling their innermost walls with directly-injected liquid waste."
            Lo "S-So warm, a-and deep!"
            show lorem normal blush eyes with dissolve
            m "Lorem raised a hand to their lower stomach."
            Lo normal blush eyes "S-So much..."
            if persistent.bangok_inflation == True:
                show lorem sleep blush with dissolve
                m "As my stream of urine packed the last of the room in their womb, they let out a tiny little moan."
                stop soundloop fadeout 2.0
                m "Between us, I felt their belly expand slightly, and the warmth of my waste pressing outward against their scales."
            else:
                stop soundloop fadeout 2.0
                show lorem sleep blush with dissolve
                m "As my stream of urine petered out, leaving a deep pool within them, they let out a tiny little moan."
        else:
            $ renpy.pause (0.5)
            c "... so I still have to go."
            Lo "Ah. Okay. Start slow, though. I'm sensitive down there."

            $ renpy.pause(0.5)
            play soundloop "fx/faucet1.ogg" fadein 1.0
            queue soundloop "fx/faucet2.ogg"
            show lorem relieved shy with dissolve
            m "After a quick adjustment of my grip, I let my bladder go, leaking warm, golden liquid into Lorem's tight passage."
            Lo "OH! H-ha.{w} S-So warm."
            m "I gradually let my stream come out faster, as I felt my piss pooling around my tip."
            show lorem normal blush eyes with dissolve
            m "Lorem raised a hand to their lower stomach."
            Lo normal blush eyes "S-So much..."
            if persistent.bangok_inflation == True:
                show lorem normal blush eyes brows with dissolve
                $ renpy.pause(0.5)
                stop soundloop fadeout 1.0
                m "As my stream of urine continued, despite packing the end of their canal, they let out a tiny little moan."
                m "Between us, I felt their belly expand slightly and the warmth of my waste pressing outward against their scales."
            else:
                stop soundloop fadeout 1.0
            m "As my stream petered out, Lorem's breathing hitched."

        $ renpy.pause (1.0)
        Lo normal blush "Th-That felt amazing."
        c "Ready for more?"
        Lo blush "So ready."

    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
        show lorem shy:
            ease 1.0 ypos 1.208
            ease 0.5 ypos 1.21
            ease 0.5 ypos 1.208
            block:
                ease 0.15 ypos 1.21
                ease 0.5 ypos 1.208
                repeat
        with None
        m "I began, gently at first, to thrust into Lorem. Their tight inner walls stretched and molded around me, their cervix especially gripping the rim of my shaft's head every time I pulled back."
        show lorem happy bangok shy with dissolve
        if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
            if persistent.bangok_inflation == True:
                m "My length plugged their womb too tightly for any of my piss to leak out as I fucked them, but I could feel the fluid flowing in their packed space, forcing them to expand and contract with every thrust."
            else:
                m "My length plugged their womb too tightly for any of my piss to leak out as I fucked them, but I could feel the fluid sloshing about my cockhead in their utterly defiled innermost space."
        m "Lorem's arms around my neck began to limpen as they gave themselves further and further to my fucking."
        Lo happy bangok shy2 "This...{w} [player_name]...{w} never thought I'd feel...{w}"
        m "Their dragonhood twitched, leaking a sticky trail up and down beneath my navel as it rubbed between us."
        Lo happy bangok shy "S-So close. H-harder..."
        show lorem happy bangok shy:
            ease 0.15 ypos 1.21
            ease 0.5 ypos 1.205
            repeat
        with None
        m "I obliged their moaned request, increasing the pitch of my thrusts until their weakened cervix lost its grip, and on my next thrust I pushed through all over again."
        play sound "fx/varagrowl.ogg"
        play sound2 "fx/extinguish.ogg"
        show lorem bangok aheago1:
            ease 0.15 ypos 1.21
            ease 0.5 ypos 1.208
            repeat
        with None
        m "Lorem went limp in my hands but for their shaft, which began to pulse sticky jets up across our chests, and their spread hole, which clenched down in rolling spasms around my own twitching length."

        m "A few more thrusts, and I couldn't contain myself either."
        show lorem bangok aheago2:
            ease 0.15 ypos 1.21
            ypos 1.21
        with dissolve
        play sound2 "fx/extinguish.ogg"
        show black with dissolve
        hide lorem with None
        if bangok_four_lorem4_store.protection == True:
            m "I came, jetting pulse after pulse of my seed into my condom as I hilted myself in Lorem's womb."
            if persistent.bangok_inflation == True:
                m "It was more than the room Lorem had left. As my hot spurts bloated the condom reservoir, Lorem's tight innermost space, already stretched around my head, had to expand further to acccept my load."
                m "Their cock rubbed in their own seed between their slightly-bloated belly and mine."
        elif persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
            m "I came, jetting pulse after pulse of my seed against the deepest recesses of Lorem's defiled sacred center."
            if persistent.bangok_inflation == True:
                m "With my twitching cockhead plugging the only escape, Lorem's pregnancy of my fluids advanced, leaving them slightly rotund from my cock, seed, and waste."
                m "Their gasps and little noises under the pressure of the filling were exquisite."
        else:
            m "I came, jetting pulse after pulse of my seed against the deepest recesses of Lorem's womb."
            if persistent.bangok_inflation == True:
                m "It was more than the room Lorem had left. As my hot spurts shifted and flowed around my obstructing cockhead, Lorem's tight innermost space, already stretched around me, had to expand further to acccept my load."
                m "Their cock rubbed in their own seed, between their slightly-bloated belly and mine."
        m "Their grip on my neck limpened further, leaving their weight hanging almost solely from my arms and shaft, as our orgasms reached their end."

        m "I hurriedly dropped to my knees, easing them back onto the coffee table before I could accidentally drop them."
        if bangok_four_lorem4_store.protection == True:
            if persistent.bangok_inflation == True:
                m "Then I tried to ease out of them, but my condom's bloated reservoir was too large to slip out of Lorem's stretched cervix."
                Lo scared "Nngh!"
                menu:
                    "Keep pulling.":
                        $ bangok_four_lorem4_store.condom_left_in = False
                        $ renpy.pause (0.5)
                        Lo relieved shy "Ough!"
                        Lo sleep blush "Ohhh..."
                        Lo normal blush eyes brows "... I wonder if that's what laying feels like."
                        show lorem shy bangok erect at center
                        hide black
                        with dissolvemed 
                    "Leave it.":
                        $ bangok_four_lorem4_store.condom_left_in = True
                        $ renpy.pause (0.5)
                        m "I tugged on the condom, easing it off of my shaft so I could slip out of Lorem's passage."
                        Lo normal blush eyes "Nnh... What are you..."
                        m "Then I twisted off the end, to make sure it wouldn't leak inside them."
                        Lo think hard blush "Oh. That... could be hard to get out later."
                        show lorem shy bangok bulge erect at center
                        hide black
                        with dissolvemed
                $ renpy.pause (0.5)
            else:
                m "Then I eased out of them, pulling out of their breached innermost gate with the condom-wrapped blob of my seed."
                Lo relieved shy "Ough!"
                Lo sleep blush "Ohhh..."
                $ renpy.pause (0.5)
                show lorem shy bangok erect at center
                hide black
                with dissolvemed 
                $ renpy.pause (0.5)
        else:
            if persistent.bangok_inflation == True:
                m "Then I eased out of them, pulling out of their bloated womb with a small cascade of my fluids."
                Lo sleep blush "Ohhh..."
                $ renpy.pause (0.5)
                if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
                    show lorem shy bangok bulge pissleak at center
                    hide black
                    with dissolvemed
                else:
                    show lorem shy bangok bulge cumleak at center
                    hide black
                    with dissolvemed
            else:
                m "Then I eased out of them, pulling out of their breached innermost gate with a small cascade of my fluids."
                Lo sleep blush "Ohhh..."
                $ renpy.pause (0.5)
                if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
                    show lorem shy bangok pissleak at center
                    hide black
                    with dissolvemed
                else:
                    show lorem shy bangok cumleak at center
                    hide black
                    with dissolvemed
    else:
        show lorem shy:
            ease 1.0 ypos 1.197
            ease 0.5 ypos 1.2
            ease 0.5 ypos 1.197
            block:
                ease 0.15 ypos 1.2
                ease 0.5 ypos 1.197
                repeat
        with None
        m "I began, gently at first, to thrust into Lorem. Their tight inner walls stretched and molded around my length, gripping and squeezing just tightly enough to feel amazing, but weakly enough not to impede my progress."

        show lorem blush with dissolve

        if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
            if persistent.bangok_inflation == True:
                m "Fucking their piss-packed canal led to some of the fluid squeezing down my length, slickening our mating point and running down my legs."
            else:
                m "Fucking their piss-stained canal led to some few drops squeezing down my length, slickening our mating point with golden waste."

        m "Lorem's arms around my neck tightened, keeping me from pushing too far inside them."
        m "Their dragonhood twitched, leaking a sticky trail up and down beneath my navel as it rubbed between us."
        Lo normal bangok shy "Farther out. L-Lift me up more..."
        show lorem happy bangok shy:
            ease 0.15 ypos 1.2
            ease 0.5 ypos 1.195
            repeat
        with None
        m "I did as asked, lifting Lorem's hips almost off of my shaft with every thrust, before pulling them back gently, with gravity, until their arms caught."
        Lo "Ah...{w=0.65} Nhh...{w=0.65} Right...{w=0.65} There...{w}"
        m "Their tight passage squeezed all the harder, in undulating waves that slid, maddeningly in their stimulation, over all my tip's most sensitive areas."
        m "Their arms limpened, trusting me to go a little bit deeper, though still short of their innermost gate or my full length."
        Lo bangok aheago1 "[player_name]...{w=0.65} Nngh...{w=1.3} I...{w}"
        play sound "fx/varagrowl.ogg"
        play sound2 "fx/extinguish.ogg"
        show lorem bangok aheago2:
            ease 0.15 ypos 1.20
            ease 0.5 ypos 1.198
            repeat
        with dissolve
        m "Lorem went limp in my hands but for their shaft, which began to pulse sticky jets up across our chests, and their spread hole, which clenched down in rolling spasms around my own twitching length."
        m "A few more thrusts, and I couldn't contain myself either."
        show lorem bangok aheago2:
            ease 0.15 ypos 1.20
            ypos 1.20
        with None
        play sound2 "fx/extinguish.ogg"
        show black with dissolve
        hide lorem with None
        if persistent.bangok_inflation == True:
            if bangok_four_lorem4_store.protection == True:
                m "I came, twitching length jetting pulse after pulse of seed into my condom's reservoir against the end of their canal."
                m "It was more than the room Lorem had left. As I felt my cum pressing back against my tip, I forced myself to pull back before I hurt them."
                Lo sleep blush "Ohhh..."
                $ renpy.pause (0.5)
                show lorem shy bangok erect at center with dissolve
            elif persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
                m "I came, my twitching length stringing rope after rope of sticky seed into the pool of piss beneath Lorem's innermost gate."
                m "With my shaft plugging the only escape, the slurry of piss and newly-injected seed had nowhere to leak but into their urine-filled womb."
                m "Their gasps and little noises as they were forced to expand slightly around my liquid gifts were exquisite."
            else:
                m "I came, my twitching length stringing rope after rope of sticky seed across Lorem's innermost gate."
                m "It was more than the room Lorem had left. As my hot spurts packed what little space remainend in their passage, I felt it leaking deeper, into their womb, until that small space, too, was filled."
                m "Their cock rubbed in their own seed, between their slightly-bloated belly and mine."
        else:
            if bangok_four_lorem4_store.protection == True:
                m "I came, twitching length jetting pulse after pulse of seed into my condom's reservoir against the end of their canal."
                Lo sleep blush "Ohhh..."
                m "Lorem moanned as I pulled out, somehow remaining cognizant of their request not to put pressure on their cervix."
                $ renpy.pause (0.5)
                show lorem shy bangok erect at center behind black with dissolve
            elif persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
                m "I came, my twitching length stringing rope after rope of sticky seed across Lorem's piss-stainend innermost gate."
            else:
                m "I came, my twitching length stringing rope after rope of sticky seed across Lorem's innermost gate."

        m "Their grip on my neck limpened further, leaving their weight hanging almost solely from my arms and shaft, as our orgasms reached their end."

        m "I hurriedly dropped to my knees, easing them back onto the coffee table before I could accidentally drop them."
        if bangok_four_lorem4_store.protection == True:
            $ renpy.pause (0.5)
            hide black with dissolvemed
            m "My condom reservoir bobbed between us, at the end of my shaft."
        elif persistent.bangok_inflation == True:
            m "Then I eased out of them, pulling out of their stretched passage with a small cascade of my fluids."
            Lo sleep blush "Ohhh..."
            $ renpy.pause (0.5)
            if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
                show lorem shy bangok bulge pissleak at center
                hide black
                with dissolvemed
            else:
                show lorem shy bangok bulge cumleak at center
                hide black
                with dissolvemed
        else:
            m "Then I eased out of them, pulling out of their slickened passage with a small ooze of my fluids."
            Lo sleep blush "Ohhh..."
            $ renpy.pause (0.5)
            if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
                show lorem shy bangok pissleak at center
                hide black
                with dissolvemed
            else:
                show lorem shy bangok cumleak at center
                hide black
                with dissolvemed

    Lo "..."
    Lo "Wow."

    c "Yeah."

    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
        Lo "I think I need to ask Ipsum to go that deep again, sometime."
    else:
        if persistent.bangok_cloacas == True:
            Lo "I think I need to ask Ipsum to focus on just my cloaca more."
        else:
            Lo "I think I need to ask Ipsum to focus on just my vagina more."


    if persistent.bangok_inflation == True and (bangok_four_lorem4_store.protection == False or bangok_four_lorem4_store.condom_left_in == True):
        Lo "And to be this full..."

    c "Feels good, huh?"

    $ bangok_four_lorem4_store.lorem_filled_expression('happy')
    with dissolve

    Lo "This was amazing!"

    $ bangok_four_lorem4_store.lorem_filled_expression('shy')
    with dissolve

    Lo "I can't thank you enough for, ah, offering."

    c "I'd say what just happened was thanks enough."

    $ bangok_four_lorem4_store.lorem_filled_expression('sad')
    with dissolve

    Lo "N-No, I mean..."
    Lo "To be able to let go of my fear and just... say yes to something like... like this?"

    $ renpy.pause (0.5)

    c "As I said, you don't have to think about that whole outside world right now."

    $ bangok_four_lorem4_store.lorem_filled_expression('normal')
    with dissolve

    Lo "Right. Thanks."

    $ renpy.pause (0.5)

    $ bangok_four_lorem4_store.lorem_filled_expression('think')
    with dissolve

    Lo "I, ah, should probably use your restroom to clean up."

    c "Want any help getting there?"

    $ bangok_four_lorem4_store.lorem_filled_expression('shy')
    with dissolve

    Lo "S-Sure. Yeah. After that, I don't know if I'll be walking normally for a bit."

    c "Then do you want to stay the night afterward?"

    $ bangok_four_lorem4_store.lorem_filled_expression('think')
    with dissolve

    $ renpy.pause (1.0)

    $ bangok_four_lorem4_store.lorem_filled_expression('normal')
    with dissolve

    Lo "Sure."

    scene black with dissolveslow

    $ renpy.pause (1.0)

    Lo think "Um, just set me here? I don't want you to come in and then this turn into a multiple-rounds thing."

    c "Okay."

    jump bangok_four_lorem4_canon_fireworks


label todo_out_of_content_bangok_four_lorem4:
    play sound "fx/system3.wav"
    s "TODO: Out of content. Roll back or prepare to crash."
    $ renpy.error("TODO: Out of content.")