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
    jump todo_out_of_content_bangok_four_lorem4

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
                "You want it in your vagina? Sure, I can hold it.":
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

    jump todo_out_of_content_bangok_four_lorem4


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
        m "Through the condom, I could feel my tip sliding against Lorem's moist tip as their breathing came faster."
    else:
        m "Lorem's slit was moist and slick, my tip sliding about a little against the outer opening as their breathing came faster."
    c "It's okay."
    Lo "I-I know. I'm just nervous."

    $ renpy.pause(0.8)
    if bangok_four_lorem4_store.lorem_pen is None or bangok_four_lorem4_store.lorem_pen == "stroke":
        show lorem:
            ease 1.5 ypos 1.4
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
            ease 1.5 ypos 1.4
        with None
        $ renpy.pause(0.5)
        m "Readjusting the position of their knees to line back up, they began to sink down onto me, spreading their tight entrance all-but taut around my hard length."
    show lorem blush:
        ypos 1.4
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
                ease 0.3 ypos 1.41
                ease 0.5 ypos 1.3
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
                ease 1.0 ypos 1.4
            with None
            $ renpy.pause (0.5)
            if bangok_four_lorem4_store.lorem_pen == "stroke":
                m "After a few moments, as I resumed stroking Lorem's shaft, they blushed, and I felt them clench lightly around me, mistake forgiven."
            else:
                m "After a few moments, Lorem sank slowly back to their previous depth, and I felt them clench lightly around me, mistake forgiven."
            show lorem:
                ypos 1.4
            with ease
        "[[Stroke their shaft.]" if bangok_four_lorem4_store.lorem_pen != "stroke":
            $ renpy.pause (0.5)
            show lorem blush with dissolve
            m ""





















    jump todo_out_of_content_bangok_four_lorem4


label bangok_four_lorem4_maleplayer_carry:
    show lorem shy bangok erect with dissolve
    show lorem:
        ypos 1.0
        ease 0.5 zoom 1.6
    with ease
    m "Leaning down, I scooped up Lorem under their arms, hoisting him up to my height."
    m "Between us, their dragonhood poked at my stomach, hard and wet. Mine rubbed one of their thighs."
    c "Ready?"
    m "Lorem got their arms up, gripping my shoulders."
    Lo normal bangok erect "Yeah."
    jump todo_out_of_content_bangok_four_lorem4


label todo_out_of_content_bangok_four_lorem4:
    play sound "fx/system3.wav"
    s "TODO: Out of content. Roll back or prepare to crash."
    $ renpy.error("TODO: Out of content.")