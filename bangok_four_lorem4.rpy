init python in bangok_four_lorem4_store:
    # Position enumeration
    # "ride" - Lorem rides the player cowgirl
    # "carry" - The player picks Lorem up, to be in control of the fuck.
    # "toy" - The player uses Lorem a bit harder.
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
            if bangok_four_common.bangnokay.check():
                Lo relieved "[player_name], we just had a pizza party. Isn't it a little soon for a sleepover?"
                c "What?"
                c "I mean, that's not what I was suggesting..."
                Lo think "What were you suggesting?"
                c "You and me... getting to know each other better?"
                Lo "But we already know each other."
                c "I mean, in a different way."
                Lo think blush "..."
                Lo relieved "No."
                Lo sad "Just because I have those parts doesn't mean I want to use them."
                c "Oh. {w=0.5}Uh. {w=0.5}Okay.{w}{nw}"
                Lo relieved "It's nothing against you, [player_name]. I just don't want to."
                c "I see."
                c "Well, I'm sorry I brought it up."
                Lo normal "It's fine."
                jump bangok_four_lorem4_feelbetter_return

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
        if persistent.bangok_dev == True:
            play sound "fx/system3.wav"
            s "Hello, dev tester! There {i}should{/i} be a female MC version of this scene here. Unfortunately, that's not something the author has experience with!"
            play sound "fx/system3.wav"
            s "We're working on a female version script! In the meantime, though, would you like to see this scene as a male? Let Lorem back out to maintain story consistency? Or see the in-development, incomplete female scene?"
            menu:
                "Yes, Let me see the scene as a male player.\n(Temporary, will revert after this scene.)":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

                    show black with dissolvemed
                    show lorem shy bangok peek with dissolve
                    hide black with dissolvemed

                    jump bangok_four_lorem4_maleplayer

                "Let me see the in-development female MC scene.":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                    jump bangok_four_lorem4_femaleplayer

                "No, let Lorem back out of it.":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

        $ renpy.pause (0.5)
        Lo relieved "No. I'm sorry, I'm just not feeling up to this."
        c "You don't have to apologize. I was just opening the possibility for you."
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
    $ bangok_four_femalepartners += 1
    menu:
        "Sounds good to me.":
            label bangok_four_lorem4_maleplayer_positionselect_ride:
            $ renpy.pause (0.5)
            $ bangok_four_lorem4_store.position = "ride"
            show o2 at Pan((100, 150), (100, 150), 0.1) with ease
            $ renpy.pause (0.3)
            m "I sat back down upon the couch, now in the nude, and spread my legs for Lorem to take a closer look."
        "I think I could pick you up, instead.":
            label bangok_four_lorem4_maleplayer_positionselect_carry:
            $ renpy.pause (0.5)
            $ bangok_four_lorem4_store.position = "carry"
            Lo shy bangok peek "O-Oh!"
            Lo normal bangok peek "I think I'd like that. Sure."
            Lo think bangok peek "But not quite yet. Let me take a closer look, first."
        "What if I held your hips from below?":
            $ renpy.pause (0.5)
            Lo bangok hidepeek "W-Wait, like using my body like a sex toy?"
            menu:
                "No, I meant like carrying you.":
                    jump bangok_four_lorem4_maleplayer_positionselect_carry
                "Nevermind. Lying back sounds good.":
                    show lorem think bangok peek with dissolve
                    jump bangok_four_lorem4_maleplayer_positionselect_ride
                "Would you want that?":
                    $ renpy.pause (0.5)
                    Lo blush "I..."
                    $ renpy.pause (0.5)
                    Lo "Kinda, yeah. Ipsum's not really large enough to handle me that way. Sometimes I think about all the big dragons I meet and just... wonder what it'd feel like."
                    Lo shy bangok peek "A-And to get to do that with a human?"
                    Lo normal bangok peek "So, yes."
                    menu:
                        "Okay.":
                            $ renpy.pause (0.5)
                            $ bangok_four_lorem4_store.cerv_pen = True
                        "You're sure?":
                            $ renpy.pause (0.5)
                            Lo relieved "No."
                            Lo sad "I'm a little sensitive down there to... depth."
                            menu:
                                "Then let's play it safe.":
                                    c "You should be in full control."
                                    Lo relieved "That makes sense."
                                    show lorem think bangok peek with dissolve
                                    jump bangok_four_lorem4_maleplayer_positionselect_ride
                                "I'll be careful about the depth.":
                                    $ renpy.pause (0.5)
                                    $ bangok_four_lorem4_store.cerv_pen = False
                                    show lorem think bangok peek with dissolve
                                    $ renpy.pause (0.5)
                                "It'll be fine, right?" if persistent.bangok_cervpen == True:
                                    $ renpy.pause (0.5)
                                    Lo think bangok peek "I mean, I want to try it. Going that deep? You look long enough, but..."
                                    menu:
                                        "Then let's do it.":
                                            $ renpy.pause (0.5)
                                            $ bangok_four_lorem4_store.cerv_pen = True
                                        "I don't want to do it if you're not sure it's safe.":
                                            $ renpy.pause (0.5)
                                            Lo relieved bangok peek "That's just it. I hear about it being done and dragons being fine, but I also hear it's extremely painful."
                                            menu:
                                                "Use Lorem as a fleshlight.":
                                                    $ renpy.pause (0.5)
                                                    $ bangok_four_lorem4_store.cerv_pen = True
                                                    c "We'll try it. If it's too painful, we'll stop."
                                                "Let them take it at their own pace.":
                                                    c "Let's play it safe. You should be in full control of this."
                                                    Lo relieved "That makes sense."
                                                    show lorem think bangok peek with dissolve
                                                    jump bangok_four_lorem4_maleplayer_positionselect_ride

                    Lo shy bangok peek "Okay."
                    show o2 at Pan((100, 150), (100, 150), 0.1) with ease
                    $ renpy.pause (0.3)
                    $ bangok_four_lorem4_store.position = "toy"
                    m "I sat back down upon the couch, now in the nude, and spread my legs for Lorem to take a closer look."


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
                        if bangok_four_xipsum.unplayed == False:
                            Lo relieved "Now that I think about it, I'm not sure Ipsum checked for urine compatibility, and the possibility of a condom full of it down there? I just don't think it's a good idea."
                        else:
                            Lo relieved "Now that I think about it, your warning about bacteria, and the possibility of a condom full of it down there? I just don't think it's a good idea."
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


    if bangok_four_lorem4_store.position in ["ride","toy"]:
        $ renpy.pause(0.5)
        show lorem happy bangok erect with dissolve
        show lorem:
            ypos 1.0
        with ease
        if persistent.bangok_cloacas == True:
            m "Lorem hopped forward to stand upright on my legs, revealing the full extent of the shaft now emerging from their cloaca."
        else:
            m "Lorem hopped forward to stand upright on my legs, revealing the full extent of the shaft now emerging from their slit."
        if bangok_four_lorem4_store.position == "ride":
            jump bangok_four_lorem4_maleplayer_ride
        else:
            jump bangok_four_lorem4_maleplayer_toy
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
        block:
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
        stop soundloop fadeout 1.0
        if persistent.bangok_inflation == True:
            show lorem normal blush eyes brows with dissolve
            m "As my stream petered out, Lorem's belly expanded slightly under their hand."
            Lo "I-It's stretching my womb."
        else:
            m "As my stream petered out, Lorem's breathing hitched."
            Lo blush "Th-That felt amazing."
        Lo blush "And you haven't even cum yet."
        c "Ready for more?"
        Lo normal blush "So ready."

        $ renpy.pause(0.3)
        show lorem blush:
            ypos 1.3
            block:
                ease 0.8 ypos 1.3
                pause 0.1
                ease 0.4 ypos 1.325
                pause 0.2
                repeat
        with None
        m "After taking a moment to catch their breath, Lorem eased back into gently fucking my shaft, now with my warm piss saturating their canal."
        if persistent.bangok_inflation == True:
            m "I could feel the fluid flowing inside, leaking from their womb then forced back inside by their downward thrusts."

    $ renpy.pause(0.8)
    if bangok_four_lorem4_store.lorem_pen == "stroke":
        m "They bucked their hips, slightly, fucking into my hand as I continued gently stroking their malehood."

    Lo "Nmh."
    $ renpy.pause(0.8)
    c "Close?"
    Lo normal blush "Y-Yeah. You?"
    c "Not quite."
    Lo blush "Mmnh."
    $ renpy.pause(0.3)
    show lorem blush:
        ease 0.6 ypos 1.3
        pause 0.1
        ease 0.3 ypos 1.325
        pause 0.1
        repeat
    with None
    m "After a moment of concerted effort they increased their pace, squeezing slightly more around me."
    c "Ohh..."
    m "Involuntarily, my lower muscles gave a twitch of approval."
    Lo sleep blush "Better?"
    c "M-Much."
    c "A-Almost--"
    show lorem shy:
        ease 0.3 ypos 1.325
        ypos 1.325
    with None
    play sound "fx/extinguish.ogg"
    show white with dissolvemed
    if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
        m "My peak snuck up on me. It was all I could do not to thrust as I twitched and pulsed thick ropes of seed into Lorem's piss-stained canal."
    elif bangok_four_lorem4_store.protection == True:
        m "My peak snuck up on me. It was all I could do not to thrust as I twitched and pulsed thick ropes of seed into my condom's tip, nestled deep in Lorem's undulating canal."
    else:
        m "My peak snuck up on me. It was all I could do not to thrust as I twitched and pulsed thick ropes of seed into Lorem's undulating canal."

    play sound "fx/varagrowl.ogg"
    show lorem sleep blush with dissolve
    if bangok_four_lorem4_store.lorem_pen == "stroke":
        m "Lorem came too, inner walls squeezing as their shaft spurt sticky whiteness across my chest and stroking hand."
    else:
        m "Lorem came too, inner walls squeezing as their shaft spurt sticky whiteness across my chest."

    if persistent.bangok_inflation == True:
        if bangok_four_lorem4_store.protection == True:
            m "My load felt larget than normal, cum bloating my condom's reservoir and flowing back around my head until I could almost see it in Lorem's lower body."
        elif persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
            m "My load felt larget than normal, cum mixing with the piss in Lorem's tight passage to form a slurry, which Lorem forced into their bloated womb with a long, slow downward thrust."
        else:
            m "My load felt larget than normal, cum packing the end of Lorem's tight passage full, before it was forced into expanding their womb with one last long, slow downward thrust."
        m "They rubbed their full belly, catching their breath."

    $ renpy.pause (0.4)
    hide white with dissolve
    $ renpy.pause (0.5)
    Lo shy "... Ah."
    Lo "I... I might need a hand standing up."

    if bangok_four_lorem4_store.lorem_pen == "stroke":
        m "I offered the hand I'd been stroking them with."
        c "I'd give you a hand, but it's a little sticky."
        m "Lorem hesitated, on the verge of laughing at the joke, but sighed instead."
        Lo relieved "[player_name]..."
        menu:
            "Lick it clean.":
                $ renpy.pause (0.5)
                show lorem shy with dissolve
                m "I brought my hand up to my mouth and licked, long and slow, while looking at Lorem's cute blush."
                m "Their cum was surprisingly sweet! I finished cleaning off my hand, then couldn't help myself taking a taste from my chest before finally wiping my saliva off on my side, leaving both hands free to help lift them off my softening shaft."
            "Have Lorem lick it clean.":
                c "You wouldn't mind helping, would you?"
                hide lorem with dissolve
                m "After a moment looking at me, Lorem began to collect the seed they'd gotten on my hand with their long tongue."
                m "They didn't take long to clean my hand, leaving both my hands free to help lift them off my softening shaft."
            "Wipe it on your chest and help.":
                $ renpy.pause (0.5)

    hide lorem with dissolve
    if bangok_four_lorem4_store.protection == True:
        m "I lifted Lorem up, my filled condom plopping onto my legs with my limp shaft as it slid free."
    elif persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
        if persistent.bangok_inflation == True:
            m "I lifted Lorem up, a small flow of my slurry of piss and cum following my limp shaft to run down their legs and drip onto mine."
        else:
            m "I lifted Lorem up, a small dribble of my slurry of piss and cum following my limp shaft to run down their legs."
    else:
        if persistent.bangok_inflation == True:
            m "I lifted Lorem up, thick rivulets of my seed following my limp shaft to run down their legs and drip onto mine."
        else:
            m "I lifted Lorem up, small rivulets of my seed following my limp shaft to run down their legs."

    m "Then I set them upright on the edge of the coffee table, holding them for a second to make sure they had their balance."
    jump bangok_four_lorem4_epilogue_merge


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
        Lo blush "Farther out. L-Lift me up more..."
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
                m "Lorem moaned as I pulled out, somehow remaining cognizant of their request not to put pressure on their cervix."
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

    label bangok_four_lorem4_epilogue_merge:

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


label bangok_four_lorem4_maleplayer_toy:
    show lorem shy bangok erect with dissolve
    show lorem:
        ypos 1.1
        ease 0.5 zoom 1.6
    with ease
    m "Taking hold of Lorem's hips, I guided them a few steps, until they stood between my legs, my tip rubbing against the base of their shaft and nestling in their slit's outermost folds."
    Lo "A-Alright. N-Now try picking me up a little?"
    show lorem:
        ypos 1.09
    with ease
    m "I hefted Lorem up a small ways, finding them slightly lighter than I expected, likely due to their bone structure being made for flying."
    Lo "A-Alright. You know what to do."

    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
        menu:
            "Hilt Lorem.":
                show lorem:
                    ypos 1.1
                with ease
                $ renpy.pause (0.3)
                m "I lined myself up with my new toy's tight slit."
                show lorem happy bangok shy:
                    ypos 1.2
                with ease
                m "Thrusting upward to get my tip in, I pulled down smoothly, sinking half my length or more inside Lorem."
                show lorem scared with dissolve
                m "Then I reached an obstruction."
                show lorem relieved shy:
                    ypos 1.21
                with ease
                Lo "OUGH!"
                m "My hips coming down from my thrust stopped abruptly against the couch cusion, ramming me further inside Lorem, past the obstruction, until their slick slit met my base, and their twitching shaft lay on my belly."
                $ renpy.pause (0.5)
                m "Enjoying the tight wetness stretched around my length, it took me a few moments to realize what I'd pushed through."
            "Ease in.":
                label bangok_four_lorem4_maleplayer_toy_ease_in:
                show lorem:
                    ypos 1.1
                with ease
                $ renpy.pause (0.3)
                m "I lined myself up with my new toy's tight slit, trying to temper my excitement with concern for not hurting them."
                show lorem happy bangok shy:
                    ypos 1.1
                    ease 2.0 ypos 1.21
                    ypos 1.21
                with None
                m "Then, gradually, I began to ease Lorem onto my shaft, enveloping myself in their tight canal."
                show lorem sleep blush with dissolve
                Lo "O-Ohh... I-Is this feeling for you--"
                Lo scared "OH!"
                m "At little more than half my shaft's length, I bumped against something inside them."
                Lo scared "A-Ah! T-Too far!"
                show lorem sad:
                    ypos 1.2
                with ease
                m "I lifted Lorem slightly."
                Lo relieved "That was my cervix."
                menu:
                    "That's what we're going through, right?" if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
                        $ renpy.pause (0.8)
                        Lo blush "W-Well..."
                        $ renpy.pause (0.8)
                        Lo normal blush "Yes. I want you all the way in."
                        show lorem sleep blush with dissolve
                        show lorem sleep blush:
                            ypos 1.2
                            ease 1.0 ypos 1.205
                            ypos 1.205
                        $ renpy.pause (0.8)
                        m "I gently eased Lorem back down, sliding slowly back to their inner gate."
                        show lorem think hard blush with dissolve
                        m "Lorem squirmed, inner walls undulating around my length spasmatically as I gently pulled their depths up against my hard insertion."
                        Lo normal blush eyes "Mnh!"
                        Lo shy "I-I, ah--!"
                        Lo blush "Nngh--"
                        show lorem relieved shy:
                            ypos 1.21
                        with ease
                        Lo "OUGH!"
                        m "Once I was through, I slid in completely, hilting Lorem's tight slit around my base and bringing their twitching shaft rubbing right up against my belly."
                    "Sorry about that.":
                        $ renpy.pause (0.8)
                        $ bangok_four_lorem4_store.cerv_pen = False
                        Lo sad "Yeah, that's definitely too deep for me."
                        $ renpy.pause (0.5)
                        Lo think blush "B-but what you already have inside..."
                        c "Want me to start moving?"
                        Lo normal blush "Please."
                    "Got it." if persistent.bangok_cervpen != True or bangok_four_lorem4_store.cerv_pen == False:
                        $ renpy.pause (0.5)
                        c "Want me to start moving?"
                        Lo normal blush "Please."

        if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
            c "Lorem?"
            Lo "I..."
            Lo "S-So big..."
            c "Like it?"
            show lorem shy with dissolve
            m "Lorem nodded, evidently beyond words."
    else:
        jump bangok_four_lorem4_maleplayer_toy_ease_in

    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
        $ renpy.pause (0.5)
        show lorem bangok aheago1 with dissolve
        show lorem bangok aheago1:
            ypos 1.2
        with ease
        m "Lorem's cervix squeezed around me, heightening my sensations as I began to pull back, but not quite out of Lorem's womb."
        show lorem bangok aheago2:
            ease 0.15 ypos 1.2
        with None
        m "Then I pulled back down, testing my wet new fleshlight."
    else:
        $ renpy.pause (0.5)
        Lo sleep blush "Mmmnh."
        show lorem sleep blush:
            ypos 1.19
        with ease
        m "Lorem panted, inner walls squeezing rhythmically as I gently lifted them almost entirely off my length."
        m "Then I pulled back down, testing my wet new shallow fleshlight."
        show lorem happy bangok shy2:
            ease 0.3 ypos 1.2
        with None

    Lo "H-Haaah... Ohhh I... Mmmh..."
    $ renpy.pause (0.5)

    if persistent.bangok_watersports == True and (bangok_four_lorem4_store.player_pissed is None or bangok_four_lorem4_store.player_pissed == "vag") and bangok_four_lorem4_store.protection == False:
        m "Then my bladder reminded me of its presence, with a twinge indicating it was near capacity."
        if bangok_four_lorem4_store.player_pissed == "vag":
            c "Is my little sex toy ready to be a little urinal?"
            if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
                m "Lorem moaned incoherently, which I took to be an affirmation."
            else:
                Lo "Mmnh. Yes."
        else:
            menu:
                "How does this sex toy feel about being a urinal?":
                    $ bangok_four_lorem4_store.player_pissed = "vag"
                    $ renpy.pause (0.5)
                    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
                        Lo "Mmnh. Yes."
                    else:
                        Lo blush "Oh, you mean..."
                        Lo think blush "Well, Ipsum does sometimes, too."
                        Lo "It's definitely... a... different experience."
                        Lo blush "Okay."
                "[[Hold it.]":
                    pass

    if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        show lorem relieved shy with dissolve
        if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
            m "My stream came hot and fast, spilling into my toy, flooding and defiling their penetrated womb."
        else:
            m "My stream came hot and fast, spilling into my toy, spattering over the already-slick walls of their canal."
        Lo bangok aheago1 "Ahhnn... Y-Yes! S-So much..."
        m "Lorem raised a hand to their lower stomach."
        if persistent.bangok_inflation == True:
            show lorem normal blush eyes brows with dissolve
            stop soundloop fadeout 1.0
            if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
                m "As my stream petered out, Lorem's belly expanded slightly under their hand, their womb forced to bloat with my piss."
            else:
                m "As my stream petered out, Lorem's belly expanded slightly under their hand, my piss leaking through into their womb until they could hold no more."
            Lo "F-Filling me! Mmmh..."
        else:
            m "As my stream petered out, Lorem's breathing hitched."
            Lo blush "Th-That felt amazing."
        c "Glad you liked that. Next it's my cum."
        Lo happy bangok shy "Y-Yes!"

    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
        show lorem bangok aheago1:
            ease 0.5 ypos 1.2
            ease 0.15 ypos 1.21
            repeat
        with None
        play soundloop "fx/rub2.ogg" fadein 1.5
        m "Squeezing Lorem's hips, I lifted them and yanked back down, getting into things with more vigor as my toy adapted to me."
        if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
            if persistent.bangok_inflation == True:
                m "Fucking into their piss-packed womb was like thrusting into a warm glass of water."
                m "It was Lorem's canal and cervix, stretched taut around my tip with with each lift up and my base with each pull down, that provided real stimulation."
                m "I could feel the piss flowing and leaking everywhere within them, saturating their female parts with my waste as they moaned around my shaft."
            else:
                m "Their piss-stained womb squelched lewdly around my cockhead, thoroughly saturated with my waste as they moaned around my shaft."
                m "For me, though, it was Lorem's canal and cervix that provided real stimulation."
                m "They stretched taut around my tip with with each lift up and my base with each pull down, leaving almost no room for the piss to leak around me as I fucked them."
        else:
            m "My deepest thrusts in kissed the back of Lorem's womb, penetrating them fully as they moaned around my shaft."
            m "For me, though, it was Lorem's canal and cervix that provided real stimulation."
            m "They stretched taut around my tip with with each lift up and my base with each pull down, like the lubed-up innards of a real sex toy."

        $ renpy.pause (0.8)
        show lorem bangok aheago2 with dissolve
        play sound "fx/varagrowl.ogg"
        play sound2 "fx/extinguish.ogg"
        m "Lorem came from the deep fucking, their malehood twitching as they strung ropes of sticky white across my chest."

        menu:
            "Give them a break.":
                stop soundloop fadeout 0.5
                show lorem bangok aheago2:
                    ease 0.25 ypos 1.21
                with None
                m "I pulled Lorem back to my base, enjoying the straining undulations of their canal as they tried to get me off."
                m "I was close, but not that close."
                $ renpy.pause (0.8)
                show lorem bangok aheago1 with dissolve
                $ renpy.pause (0.3)
                m "Eventually they came back from their high, gasping for breath."
                Lo happy bangok shy "Y-You're still so deep inside."
                Lo think blush "D-Did you...?"
                c "Not yet."
                Lo shy "S-So there's more?"
                if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag" and persistent.bangok_inflation == True:
                    m "Their stretched canal clenched weakly around me, wombful of piss shuddering."
                else:
                    m "Their stretched canal clenched weakly around me."
                Lo blush "Well, I don't want to leave you unsatisfied."
                c "You're sure? You don't need any more time?"
                Lo think hard blush "Y-You're not exactly giving me a break by being all the way in my womb."
                c "Fair enough."

                show lorem shy:
                    ypos 1.20
                with ease
                m "Gently, I began to lift them again, testing the waters and their arousal after their orgasm."
                show lorem blush:
                    ypos 1.21
                with ease
                Lo blush "Nnmh."
                Lo normal blush "You can go faster than that."
                show lorem shy:
                    ypos 1.20
                with ease
                show lorem shy:
                    ypos 1.21
                with ease
                $ renpy.pause (0.1)
                play soundloop "fx/rub2.ogg" fadein 2.5
                show lorem happy bangok shy:
                    ease 0.5 ypos 1.20
                    ease 0.15 ypos 1.21
                    repeat
                with None
                $ renpy.pause (0.8)
                m "Lorem's slick canal slid around my shaft as I pumped them up and down, squeezing and urging me closer to my release."
                $ renpy.pause (0.8)
                m "I thrust a little with my hips up into them, my edge moments away."
                $ renpy.pause (0.4)
            "Keep fucking.":
                m "Lorem's mouth hung open, lost in their ecstacy as I used their spasming canal to focus on myself."
                m "I was close, but not close enough I felt I could get off from their orgasm."

                show lorem relieved shy:
                    ease 0.5 ypos 1.19
                    ease 0.15 ypos 1.21
                    repeat
                with None
                m "Nearing my peak, I lifed Lorem off just a bit more, so that their stretched cervix closed around my tip and I got to spread it around me anew."
                m "Lorem twitched and shook, inner walls undulating around me, bringing me right up to my edge."
        
        label bangok_four_lorem4_maleplayer_toy_cerv_pen_orgasm:
        stop soundloop fadeout 0.5
        show lorem happy bangok shy:
            ease 0.15 ypos 1.21
        with None
        play sound "fx/extinguish.ogg"
        show black with dissolve
        if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
            if persistent.bangok_inflation == True:
                m "I pulled Lorem to my base and came, pushing pulses of seed up my twitching shaft to add to the piss inflating their womb."
                m "Spurt after spurt travelled up, until the liquid in their womb felt like a thick slurry and I felt their belly pressing back slightly against my hands on their hips."
            else:
                m "I pulled Lorem to my base and came, pushing pulses of seed up my twitching shaft to spurt over the piss defiling their womb."
        else:
            if bangok_four_lorem4_store.protection == True:
                m "I pulled Lorem to my base and came, pushing pulses of seed up my twitching shaft that spurt into my conndom's reservoir, nestled in the depths of their womb."
                if persistent.bangok_inflation == True:
                    m "Squished against their womb's rear wall, my cum flowed back around my head, until it felt like my condom was expanding to fill all room in the small space."
            else:
                m "I pulled Lorem to my base and came, pushing pulses of seed up my twitching shaft that spurt over the walls of their womb."
                if persistent.bangok_inflation == True:
                    m "Spattering back from their womb's far wall, my cum flowed back around my head, until it felt like my load had completely packed Lorem's small, innermost space."
        show lorem normal bangok bulge erect
        hide black
        with dissolveslow
        m "I came back down from my peak slowly, hilted in my smiling little toy."
    else:
        show lorem bangok aheago1:
            ease 0.5 ypos 1.19
            ease 0.15 ypos 1.2
            repeat
        with None
        play soundloop "fx/rub2.ogg" fadein 1.5
        m "Squeezing Lorem's hips, I began to tug them up and down at my own pace, getting into things with more vigor as my toy adapted to me."

        if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
            if persistent.bangok_inflation == True:
                m "I could feel my piss flowing and leaking everywhere within them, saturating their female parts and my legs with my waste as they moaned around my shaft."
            else:
                m "Their piss-stained canal squelched lewdly around my cockhead, becoming coated with my waste as they moaned around my shaft."
        else:
            m "Our mating poinnt squelched slightly with each pull down, becominng coated in our coital juices as they moaned around my shaft."

        m "It was all I could do not to pull them down further or too fast, as their tight hole quickly had me approaching my peak."
        m "They stretched taut around my tip with with each lift up, the clenching of their entrance squeezing in a way better than any real sex toy."

        Lo bangok aheago2 "Aaahn!"

        if persistent.bangok_cervpen == True:
            Lo aheago1 "D-Deeper!"
            m "I could feel I was almost kissing the end of their canal with each pull down. There wasn't much deeper I could go without pushing right into their womb!"
            menu:
                "[[Obey.]":
                    label bangok_four_lorem4_maleplayer_toy_late_pen:
                    $ bangok_four_lorem4_store.cerv_pen = True
                    m "After just a few more thrusts to prepare us both, I pulled Lorem down, then kept pulling."
                    stop soundloop fadeout 0.15
                    show lorem relieved shy:
                        ease 0.15 ypos 1.21
                        ypos 1.21
                    with None
                    play sound "fx/varagrowl.ogg"
                    play sound2 "fx/extinguish.ogg"
                    m "Lorem came instantly, their malehood twitching as they strung ropes of sticky white across my chest."
                    show lorem bangok aheago2 with dissolve
                    m "I held them there, fully speared on my shaft, with all the depth they could want as I rode out their orgasm."

                    if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
                        if persistent.bangok_inflation == True:
                            m "My tip pressed right into the back of their womb, surrounded with the piss I'd filled them with, while their cervix and canal squeezed eratically around the lower half of my shaft like some kind of large, wet, living cock ring."
                        else:
                            m "My tip pressed right into the back of their womb, while their cervix and canal squeezed eratically around the lower half of my shaft like some kind of large, piss-stained living cock ring."
                    else:
                        m "My tip pressed right into the back of their womb, while their cervix and canal squeezed eratically around the lower half of my shaft like some kind of large, wet, living cock ring."

                    m "Then, trying to lift them slightly, the sensation of their womb and canal all sliding around my shaft proved too much for me, too."
                    jump bangok_four_lorem4_maleplayer_toy_cerv_pen_orgasm
                "A-Are you sure?":
                    Lo bangok aheago2 "Yes!"
                    jump bangok_four_lorem4_maleplayer_toy_late_pen
                "Going as deep as I can!":
                    pass
            $ renpy.pause (0.8)

        Lo bangok aheago1 "F-Faster!"

        m "I gripped tighter, thrusting up a little into them as I struggled to hold back from taking them deeper than they were comfortable with."
        m "Both of us panted aloud, teetering on the verge of our respective peaks."

        stop soundloop fadeout 0.2
        play sound "fx/rub1.ogg"
        show lorem bangok aheago2:
            ease 0.2 ypos 1.19
            ease 0.15 ypos 1.2
            repeat
        with None
        $ renpy.pause (1.2)
        play sound2 "fx/extinguish.ogg"
        show lorem relieved shy:
            ypos 1.2
        with dissolve
        $ renpy.pause (0.3)

        play sound "fx/extinguish.ogg"
        show black with dissolve

        if persistent.bangok_watersports == True and bangok_four_lorem4_store.player_pissed == "vag":
            m "I came just after them, twitching and spurting into their urine-flooded depths as they sprayed sticky white ropes across my chest."
            if persistent.bangok_inflation == True:
                m "I could feel the pulses of my seed travelling up my length under my fingers before spurting out against their piss-stained innermost gate, packing solid their canal and tubes until it felt like they were expanding with my slurry of fluids."
            else:
                m "I could feel the pulses of my seed travelling up my length under my fingers before spurting out against their piss-stained innermost gate, coating their whole passage in my slurry of fluids."
        else:
            if bangok_four_lorem4_store.protection == True:
                m "I came just after them, twitching and spurting into my condom inside them as they sprayed sticky white ropes across my chest."
                if persistent.bangok_inflation == True:
                    m "Squished against their canal's innermost gate, my cum flowed back around my head, until it felt like my condom was expanding to fill all room in the small space."
            else:
                m "I could feel the pulses of my seed travelling up my length under my fingers before spurting out against their innermost gate, coating their whole passage in my appreciation of their feminine parts."
                if persistent.bangok_inflation == True:
                    m "With so little space, and so much taken up by my malehood, my cum had nowhere to go but deeper inside them, packing their womb and tubes with my seed."
        $ renpy.pause (0.3)
        show lorem normal bangok bulge erect
        hide black
        with dissolveslow
        m "I came back down from my peak slowly, still spearing open my smiling little toy."


    $ renpy.pause (0.8)
    if persistent.bangok_inflation == True:
        c "You felt amazing. Sure filled you up too, huh?"
        Lo shy bangok bulge erect "Yeah."
        Lo blush bangok bulge erect "That felt..."
        m "They let out a little gasp, inner walls clenching around me again."
        c "Oh, I uh... should probably pull out."
        Lo shy bangok bulge erect "Probably..."
        show lorem happy bangok shy bulge erect with dissolve
        $ renpy.pause (0.1)
        hide lorem with dissolve
    else:
        c "You felt amazing. So tight."
        Lo shy "T-Thanks."
        Lo blush "That felt a lot better than I was expecting."
        c "Oh, I uh... should probably pull out."
        Lo shy "Probably..."
        show lorem happy bangok shy with dissolve

    $ renpy.pause (0.1)

    if persistent.bangok_cervpen == True and bangok_four_lorem4_store.cerv_pen == True:
        if bangok_four_lorem4_store.protection == True:
            if persistent.bangok_inflation == True:
                m "I tried to lift them off of my shaft, but my condom's bloated reservoir was too large to slip out of Lorem's stretched womb."
                Lo scared "Nngh!"
                menu:
                    "Keep pulling.":
                        $ bangok_four_lorem4_store.condom_left_in = False
                        $ renpy.pause (0.5)
                        Lo relieved shy "Ough!"
                        Lo sleep blush "Ohhh..."
                        Lo normal blush eyes brows "... I wonder if that's what laying feels like."
                    "Leave it.":
                        $ bangok_four_lorem4_store.condom_left_in = True
                        $ renpy.pause (0.5)
                        m "I tugged on the condom, easing it off of my shaft so I could slip out of Lorem's passage."
                        Lo normal blush eyes "Nnh... What are you..."
                        m "Then I twisted off the end, to make sure it wouldn't leak inside them."
                        Lo think hard blush "Oh. That... could be hard to get out later."
            else:
                hide lorem with dissolve
                m "I lifted them off my shaft, sliding out of their breached innermost gate with the condom-wrapped blob of my seed."
                Lo relieved shy "Ough!"
                Lo sleep blush "Ohhh..."
        else:
            hide lorem with dissolve
            if persistent.bangok_inflation == True:
                m "I lifted Lorem's stuffed womb off my length and they gasped. A slick flow of my fluids followed my head, soaking into their stretched canal."
            else:
                m "I lifted Lorem's innnermost gate off my length and they gasped. A slow drip of my fluids followed my head, dribbling down into their stretched canal."
            Lo sleep blush "Ohhh..."
    else:
        hide lorem with dissolve
        if bangok_four_lorem4_store.protection == True:
            m "I lifted them off my shaft, sliding out of their spread canal with the condom-wrapped blob of my seed."
            Lo relieved shy "Ough!"
            Lo sleep blush "Ohhh..."
        else:
            if persistent.bangok_inflation == True:
                if persistent.bangok_cloacas == True:
                    m "I lifted Lorem's stuffed cloaca off my length. They gasped, legs shuddering, as a slick flow of my fluids followed my head, running over both of our lower bodies."
                else:
                    m "I lifted Lorem's stuffed vagina off my length. They gasped, legs shuddering, as a slick flow of my fluids followed my head, running over both of our lower bodies."
            else:
                if persistent.bangok_cloacas == True:
                    m "I lifted Lorem's spread cloaca off my length. They gasped, legs shuddering, as a slick flow of my fluids followed my head, running over both of our lower bodies."
                else:
                    m "I lifted Lorem's spread vagina off my length. They gasped, legs shuddering, as a slick flow of my fluids followed my head, running over both of our lower bodies."
            Lo sleep blush "Ohhh..."

    $ renpy.pause (0.5)

    m "Then, careful not to jostle their lower body, I seated them on the edge of the table."
    jump bangok_four_lorem4_epilogue_merge

label bangok_four_lorem4_femaleplayer:
    $ renpy.pause (0.5)
    Lo relieved "No. I'm sorry, I'm just not feeling up to this."
    c "You don't have to apologize. I was just opening the possibility for you."
    Lo sad "I appreciate that. But I don't really want to use my male side tonight, after admitting it's not all of me."
    Lo relieved "And I really don't want claws digging around inside me, no matter how short."
    m "Glancing at the last couple of leftover salad pizza slices gave me an idea of what I could do."
    c "That is fine, there are other things that we can do. I know that I can't provide a male side of my own, but I could make a substitute."
    c "Or there are always our mouths and tongues."
    if bangok_four_xipsum.unplayed == False:
        Lo think bangok peek "Ipsum said the samples he took from you when you two hooked up told him that \"hooking up\" without protection should be perfectly safe."
        Lo "The same should apply for us, too. Besides, I'm not sure there would be any dental dams in your apartment, and certainly not to fit a human."
    else:
        Lo think bangok peek "I mean, different dragon species can't get one another pregnant. You're an even more different species."
        Lo normal bangok peek "We don't need protection. Besides, I'm not sure there would be any dental dams in your apartment, and certainly not to fit a human."
    Lo "A substitute?"
    c "Yes, a toy?"
    Lo "Toy?"
    c "Do you have something you use for your female side when Ipsum is not available?"
    Lo "Oh you mean a pleasure stick. Yes I do have one of those, but it's at home, and if I am going home to get it then it would be too late to come back."
    c "So that is what dragons call them. I'll remember that. I was not able to bring any of my own through the portal, but I believe I can make a temperary one for tonight."
    c "Would you like that?"
    Lo think bangok peek "You can?"
    $ renpy.pause (0.5)
    Lo normal bangok peek "I'll stay to see what you come up with."
    m "I smiled, happy that I had convinced the small dragon to stay, for now."
    c "Great, give me a few minutes and I will be back."
    m "I went into the pantry, opened one of the top cupboards, and had a rummage in the box of vegetables that had been left by Remy when I had first moved in."
    m "Finding a cucumber with a similar size and length to smaller toys back home, I put the vegetable box back in the cupboard."
    m "Going into the nearby kitchen, I remembered the small toolbox under the sink that had a few basic tools for maintaince and took out a screwdriver."
    m "Using the screwdriver, I made a hole through the core of the fruit, then set it aside for later."
    if persistent.bangok_inflation == True:
        m "I found a large sized pan, filled it with water and placed it on the stove. I turned on the stove and set it to boil."
    else:
        m "I found a medium sized pan, filled it with water and placed it on the stove. I turned on the stove and set it to boil."    
    m "I returned to the living room."
    m "We have some time before the improvised pleasure stick will be ready."
    menu:
        "Get Lorem ready for the toy":
            c "Let me get you ready for the toy. I can stil see you are pretty tense from earlier. You should be relaxed to enjoy it."
            m "Lorem gave a nod."
            Lo "Thank you [player_name]."
            c "I will be turning you upside down, it is just easier to get to your parts given you are small."
            Lo "Go ahead, I am used to it when Ipsum does the same."
            m "Lorem had turned himself around on the couch, their legs resting against the back of the couch."
            m "Stopping in front of Lorem, I reached down and picked up the dragon under their calves."
            m "Sitting back on the couch, I put Lorem's legs on my shoulders, theire hands were on my legs doing a headstand."
            m "Now that I had a closeup view of their groin, I could see what I was working with."
            if persistent.bangok_cloacas == True:
                if (bangok_four_malepartners > 0) and (bangok_four_femalepartners == 0):
                    m "Lorem had a single vertical slit, unlike other male dragons I had been with before, I guess due to being a mixture of both genders. Their dick was poking out of the top of their slit, the lower part slightly parted to give a small peek at the passages inside."
                elif (bangok_four_femalepartners > 0) and (bangok_four_malepartners == 0):  
                    m "Their vertical slit was longer then what would be considered normal for their size, though as it had to hold both their male and female parts as well as anal passage it would need to be longer. Their dick was poking out of the top of their slit, the lower part slightly parted to give a small peek at the passages inside."
                elif (bangok_four_femalepartners > 0) and (bangok_four_malepartners > 0):
                    m "Having been with both female and male dragons, I saw that Lorem had a vertical slit like a female. It was longer then what would be considered normal for their size, though as it had to hold both their male and female parts as well as anal passage it would need to be longer. Their dick was poking out of the top of their slit, the lower part slightly parted to give a small peek at the passages inside." 
                else:
                    m "Given this was to be my first intimate moment with a dragon, I did not have a reference as to what a normal cloaca would look like. I saw that Lorem had a vertical slit. Their dick was poking out of the top of their slit, the lower part slightly parted to give a small peek at the passages inside."
                m "I bought my hands up to Lorem's slit, placing my thumbs on either side above their dick and pulled their cloaocal lips apart."
                m "I could see their vaginal passage to the lower end, taking up the majority of the slit, their much smaller anal vent was at the top end."
            else:
                m "Lorem's vagina was directly below their penis, which was sticking out like a large clit would in a human. their vaginal lips were spread open slightly due to their penis, giving a peek of their passageway beyond. A bit further down towards their tail was their anus."
                m "I bought my hands up to the dragon's vagina, placing my thumbs on either side above their dick and pulled their lips apart."
            m "Bringing my mouth towards the spread passage, I stuck my tongue out and began to run it over the inner lips."
            m "Lorem gave a shudder at the feeling of the texture of my tongue."
            m "I could feel their passageway relaxing and start to taste their arousal, not sure what I had been expecting, but it tasted sweet."
            m "Lorem began to let out a purr at how good it felt, given dragons had snouts to contend with, oral had never been something dragons were good at, the few times that Ipsum had tried it had not been as stimulating as this."
            m "I pushed my tongue further down their tunnel, lapping up more of their juices from their smooth walls."
            m "Their dick, resting between my breasts, was now steadily drippling pre. A mirror of the arousal coating their vaginal passage, as well as my face."
        "Share a hug":
            c "Lorem, have you ever had a hug?"
            Lo "A hug? No, is that a human thing?"
            c "Then allow me to give you one, you need it."
            m "Stopping in front of Lorem, I reached down and picked up the dragon under their shoulders."
            m "They weighed less then I had thought, though should have been expected due to being a flyer that they would have lighter bones."
            m "I sat back down and hugged the small dragon to my chest being careful of their wings, enjoying the warmth."
            m "One hand was on their back, the other on the back of their head, rubbing in small circles."
            m "Lorem went limp in my arms and began to purr, enjoying the affection. All the stress that had been pent up leading to the revelation this evening left the small dragon."
            m "They could tempererally forget the prejudice that was unjustified and enjoy this evening alone with a human that did not think any less of them even having known their secret."
            m "And no Ipsum to get in the way to 'study' them either."
         
    Lo "Thank you for this, [player_name]. It has been so long that anyone truly appreciated me for what I am. I know now that no matter what other dragons think at least someone is out there that accepts me for me."
    m "After a few minutes it was time to finish the preparation for the main activity."
    m "I sat Lorem back down on the edge of the couch and returned to the kitchen."
    m "The water was boiling and ready for the next part of the preparation."
    m "Getting a mixing bowl out of the cupboard as well as some flour, I poured most of the water into the bowl and placed the cucumber into the left over water to warm it up."
    m "I mixed in a small dusting of flour briskly so that the mixture would not have lumps; it needed to be smooth for what I planned on doing."
    # TODO: Add checks here for Anna2 players who found or bought condoms.
    if (bangok_four_femalepartners + bangok_four_malepartners > 1):
        m "As I had experienced im my time here, having sexual activities with friends was part of dragon culture, so a brief search around the apartment revealed an ample supply of condoms had been left, including many sizes able to accommodate any dragon."
    else:
        m "I was sure that, in case of a hankering diplomat, some form of protection would be available in case of sexual interludes. A brief search around the apartment revealed an ample supply of condoms had been left, including many sizes able to accommodate any dragon."
    m "I fished out one of the larger condoms and opened the packet."
    m "I pulled the central bulb with one hand and rolled the condom out, forming a long rubber sleave."
    m "Holding the enterence to the condom wide with one hand, I used my other to carefully pour the hot mixture into the condom."
    if persistent.bangok_inflation == True:
        m "The lower half of the condom was full of the fake cum."
        if bangok_four_bryce1_unplayed == False:
            m "The load in the condom reminded me how productive Bryce had been."
    else:
        m "About a quater of the condom was full of the fake cum."
    m "Retrieving the now warmed cucumber from the pan, I used the screwdriver again to carefully push the outer rim of the condom up the hole I had made earlier until it poked through the top."
    m "Pulling the rim of the condom back around the outside of the cucumber the substitute pleasure stick was ready, complete with fake cum in the filled condom hanging below."
    m "I returned to the living room, holding the toy."
    Lo "That is something I would never have thought to do with a cucumber. Normally I just chew on them because they are crunchy."
    Lo "The length is longer then what I am used to, I am not sure that I want to take it."
    if persistent.bangok_cervpen == True:
        menu:
            "Remind him this might be once-in-a-lifetime.":
                c "You did want to the experience of taking a human cock right?"
                Lo "O.. O.. Of course but..."
                c "Then the full lenth of it you will take."
                Lo "Yes I will do it."
                $ bangok_four_lorem4_store.cerv_pen = True
                c "Good. I promise it will be worth it."

            "Let Lorem choose.":
                c "Lets wait until you have it in you before making that choice, I promise that it will increase the pleasuer you will feel."
                c "And you will get the satisfaction of haven taken what would be a full length of a human."
                m "Lorrem nodded, some of the aprehensiveness he was showing when seeing the toy lessoning."
                $ bangok_four_lorem4_store.cerv_pen = False
    else:
        c "That is perfectly fine. This will be just about you, for now so let me know when you are happy with the depth." 
    if bangok_four_xipsum.clothesoff == False:
        Lo think bangok peek "If we are going to do this then it would be best for you to take those coverings off."
    else:
        Lo think bangok peek "I know I saw what was under your covers, but may I see it again? I'm not sure if..."
    c "You want me to strip?"
    Lo shy bangok peek "I am open about what I have between my legs, and I want you to be also."
    
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
    Lo normal bangok peek "Now that we are both being open about what we are, we can proceed."
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
    Lo "If I stand on your legs with you on the couch and put my hands on your shoulders, you will be able to control the toy?"
    m "I nodded."
    $ bangok_four_femalepartners += 1
    if persistent.bangok_cloacas == True:
        m "Lorem got on my legs and put their arms on my shoulders. Taking the toy below their spread legs with one hand, I glided my other hand to the base of their erect shaft and found the slit of their cloaca."
        m "I used my thumb and first finger to spread the lower part of the slit wide and brought the head of the toy to the wet enterence to push into their already slick passage."
    else:
        m "Lorem got on my legs and put their arms on my shoulders. Taking the toy below their spread legs with one hand, I glided my other hand to the base of their erect shaft and feeling slightly lower found the wet opening of their vagina."
        m "I used my thumb and first finger to spread the slit wide and brought the head of the toy to the wet enterence to push into their already slick passage."
    m "I began to push the toy in with relitive ease. Their relaxed passage spread as the toy continued pushing further inside, their arousal coating the toy in their fluids."
    m "Lorem gave a buck with their legs and took more of the toy inside."
    Lo normal blush "It's bigger than my own pleasure stick at home."
    c "In a good way, or...?"
    Lo blush "Yes. A very good way."
    Lo think blush "I'm honestly not sure I'll be able to fit it all in, but I want to give it a try."
    m "When about half of the shaft had been taken inside, I felt a slight resistance and Lorem let out a hiss."
    if persistent.bangok_cervpen == True:
        Lo relieved "That is my cervix."
        Lo think "I'm not sure if I want to take it any further. I heard once other dragons say that it is pleasurable, though. To go through."
        if bangok_four_lorem4_store.cerv_pen == True:
            Lo "I know I said earlier that I wanted to take it all, but now it is in me, maybe I will see how I feel later."
    else:
        Lo "That is my cervix. I can't take any more."
    m "I started to get into a rhythm, moving my hand either backwards or forwards depending on what direction their hips were going."
    m "Their passage had started to relax, having adjusted to the length of the toy that was currently in their dephs, although a good half remained outside their slit."
    
    if bangok_four_lorem4_store.cerv_pen == True:
        menu:
            "Surprise Lorem by forcing the toy through their cervix when they do not expect it": 
                show lorem:
                    ypos 1.1
                with ease
                $ renpy.pause (0.3)
                m "I gently pulled back a bit further then usual, pulling more of the toy out."
                show lorem happy bangok shy:
                    ypos 1.2
                with ease
                m "On the next down thrust by Lorem, I met it by pushing the toy sharply upward."
                show lorem scared with dissolve
                m "There was a small obstruction in their passage, the tip of the toy having found their cervix. Unfortunately, having already begun the thrust downwards, there was no way to stop in time."
                show lorem relieved shy:
                    ypos 1.21
                with ease
                Lo "OUGH!"
                m "Their hips continued to come down and with my hand firmly pushing the toy, there was only one place the toy could go." 
                m "Ramming the toy further inside Lorem, past the obstruction, until their slick slit met my hands holding the bottom of the toy, and their twitching shaft lay on my belly."
                $ renpy.pause (0.5)
                m "Reflexively, Lorem bought their legs together, their tunnel clammpng tight around the toy inside, trying to stop the penetration that had already happened."
                m "Their front claws were digging slightly into my shoulders, though the claws were blunt enough they only left slight marks."
                m "After a few seconds, their legs relaxed, the grip on my shoulders lessoning as the dragon let out a few deep breaths. The discomfort of the penetration dulling and giving rise to pleasure."

            "Loosen Lorem up to push the toy through.": 
                show lorem:
                    ypos 1.1
                with ease
                $ renpy.pause (0.3)
                m "I began to gently put slightly more force in my movements, feeling the toy reach their cervix at each thrust."
                show lorem happy bangok shy:
                    ypos 1.1
                    ease 2.0 ypos 1.21
                    ypos 1.21
                with None
                m "Then, gradually, I began to move my hand further down the toy, slightly incrasing the length that went into their passage."
                show lorem sleep blush with dissolve
                Lo "O-Ohh... I-Is the toy getting longer?--"
                Lo scared "OH!"
                m "I could feel the end of the toy making firm contact against their cervix on each stroke, each time I could feel the pressure starting to give."
                Lo scared "A-Ah! T-Too far!"
                show lorem sad:
                    ypos 1.2
                with ease
                m "I pulled the toy out of Lorem slightly, the end no longer at their cervix."
                Lo relieved "That was my cervix."
                c "That's what we're going through, right? If you want to take in the full length?"
                $ renpy.pause (0.8)
                Lo blush "W-Well..."
                $ renpy.pause (0.8)
                Lo normal blush "Yes. I it all the way in."
                show lorem sleep blush with dissolve
                show lorem sleep blush:
                    ypos 1.2
                    ease 1.0 ypos 1.205
                    ypos 1.205
                $ renpy.pause (0.8)
                m "I gently pushed back into their passage, sliding slowly to their inner gate."
                show lorem think hard blush with dissolve
                m "Lorem squirmed, inner walls undulating around my length spasmatically as I gently thrust up against the barrier that was slowly starting to give."
                Lo normal blush eyes "Mnh!"
                Lo shy "I-I, ah--!"
                Lo blush "Nngh--"
                show lorem relieved shy:
                    ypos 1.21
                with ease
                Lo "OUGH!"
                m "Once the toy was through, I slid it completely, hilting Lorem's tight slit around my hand at the bottom of the toy and bringing their twitching shaft rubbing right up against my belly."

            "Wait for Lorem to decide.":
                $ bangok_four_lorem4_store.cerv_pen = False
                pass
    
    if (persistent.bangok_cervpen == True) and (bangok_four_lorem4_store.cerv_pen == True):
        c "Lorem?"
        Lo "I..."
        Lo "S-So big..."
        c "Like it?"
        show lorem shy with dissolve
        m "Lorem nodded, evidently beyond words."
        $ renpy.pause (0.5)
        show lorem bangok aheago1 with dissolve
        show lorem bangok aheago1:
            ypos 1.2
        with ease
        m "Lorem's passage squeezed around the toy as I moved my hand further up reducing the distance the toy could be moved."
        show lorem bangok aheago2:
            ease 0.15 ypos 1.2
        with None
        m "I moved my arm along with their thrusts only allowing a small amount of movement, keeping the toy within their womb."
        Lo "H-Haaah... Ohhh I... Mmmh..."
        $ renpy.pause (0.5)
        show lorem bangok aheago1:
            ease 0.5 ypos 1.2
            ease 0.15 ypos 1.21
            repeat
        with None
        play soundloop "fx/rub2.ogg" fadein 1.5
        m "I started to gradually move my hand back down the toy, now that Lorem's cervix had stretched to conform to it I could pull out further, each thrust now taking the full length of the toy."
        m "The deepest thrusts made the toy stop as it kissed the back of Lorem's womb, penetrating them fully as they moaned."
        $ renpy.pause (0.8)
        show lorem bangok aheago2 with dissolve
        play sound "fx/varagrowl.ogg"
        play sound2 "fx/extinguish.ogg"

    else:
        $ renpy.pause (0.5)
        Lo sleep blush "Mmmnh."
        show lorem sleep blush:
            ypos 1.19
        with ease
        m "Lorem panted, inner walls squeezing rhythmically as the toy was pulled almost completely out."
        m "Then I pushed back up taking them to their requested deph, my hand stopping the toy before it hit their cervix."
        show lorem happy bangok shy2:
            ease 0.3 ypos 1.2
        with None
        Lo "H-Haaah... Ohhh I... Mmmh..."
        $ renpy.pause (0.5)
        show lorem bangok aheago1:
            ease 0.5 ypos 1.19
            ease 0.15 ypos 1.2
            repeat
        with None
        play soundloop "fx/rub2.ogg" fadein 1.5
        m "We both began to speed up our thrusts, their passage having stretched and become adapted to the size of and deph of the toy."
        m "Their enterence squelched slightly with each thrust, becoming coated in their coital juices as they moaned around the penetration."
        Lo bangok aheago2 "Aaahn!"
        if (persistent.bangok_cervpen == True) and (bangok_four_lorem4_store.cerv_pen = False):
            Lo aheago1 "D-Deeper!"
            m "I could feel I was almost kissing the end of their canal with each pull down. There wasn't much deeper I could go without pushing right into their womb!"
            menu:
                "[[Obey.]":
                    label bangok_four_lorem4_femaleplayer_toy_late_pen:
                    $ bangok_four_lorem4_store.cerv_pen = True
                    m "After just a few more thrusts to prepare us both, I pushed into Lorem hard as their legs came down down, forcing the toy through as the whole length was swallowed by their tunnel."
                    stop soundloop fadeout 0.15
                    show lorem relieved shy:
                        ease 0.15 ypos 1.21
                        ypos 1.21
                    with None
                    play sound "fx/varagrowl.ogg"
                    play sound2 "fx/extinguish.ogg"
                "A-Are you sure?":
                    Lo bangok aheago2 "Yes!"
                    jump bangok_four_lorem4_femaleplayer_toy_late_pen
                "Going as deep as I can!":
                    jump bangok_four_lorem4_femaleplayer_toy_no_pen
            $ renpy.pause (0.8)
        else:
            label bangok_four_lorem4_femaleplayer_toy_no_pen:
            Lo bangok aheago1 "F-Faster!"
            m "we sped our thrusts even more, the now thourighly slick toy making my hand slip, struggling to hold back from thrusting deeper than they were comfortable with."
            m "Both of us panted aloud, Lorem teetering on the verge of their respective peak."
            stop soundloop fadeout 0.2
            play sound "fx/rub1.ogg"
            show lorem bangok aheago2:
                ease 0.2 ypos 1.19
                ease 0.15 ypos 1.2
                repeat
            with None
            $ renpy.pause (1.2)
            play sound "fx/varagrowl.ogg"
            play sound2 "fx/extinguish.ogg"
    if persistent.bangok_cervpen == True:
        m "Lorem came from the deep thrusting, their malehood twitching as they strung ropes of sticky white across my chest. Their legs locked up, pleasure of their orgasm clouding their mind."
        m "I could feel the resistance in their tunnel as their vaginal passage gripped the toy, trying to milk it for the seed. My hands were stronger as I continued to thrust the toy through their spasming passage." 
        m "At the same time I reached my other hand down to the condom full of the still warm fake cum and began to squeeze it, forcing the cum up through the toy and into their womb at the end of each thrust."
        m "Lorem let out another growl as their orgasm continued, their dick still pulsed against my chest, though no more seed came out."
        if persistent.bangok_inflation == True:
            m "I continued to squeeze more of the fake cum from the condom, swelling their lower belly as their womb was forced to make room for the fake cum I was forcing in. A small amount had started to dribble around their clenched slit, their womb struggling to hold it all."
        else:
            m "I finished pushing in the last of the fake cum that I had made. A few dribbles could be seen around the end of the toy, the clenched slit ensuring the vast majority was held deep within their womb."
    else:
        m "Lorem came from the rapid thrusting, their malehood twitching as they strung ropes of sticky white across my chest. Their legs locked up, the pleasure of their orgasm clouding their mind."
        m "I could feel the resistance in their tunnel as their vaginal passage gripped the toy, trying to milk it for the seed. My hands were stronger as I continued to thrust the toy through their spasming passage." 
        m "At the same time I reached my other hand down to the condom full of the still warm fake cum and began to squeeze it, forcing the cum up through the toy and into their passage at the end of each thrust."
        m "Lorem let out another growl as their orgasm continued, their dick still pulsing against my chest, though no more seed came out."
        if persistent.bangok_inflation == True:
            m "I continued to squeeze more of the fake cum from the condom, swelling their lower belly as the fake cum was forced through their cervix with the thusts of the toy and the contractions of their passage. A small amount had started to dribble around their clenched slit, their womb struggling to hold it all."
        else:
            m "I finished pushing in the last of the fake cum that I had made. Given the depth of the toy, I was sure some fake cum had been forced deeper into them with the thusts of the toy and the contractions in their passage. A few dribbles could be seen around the end of the toy, their clenched slit ensuring the vast majority was held within their depths."
    $ renpy.pause (0.8)
    if persistent.bangok_inflation == True:
        Lo shy "T-Thanks."
        Lo blush bangok bulge erect "That felt..."
        if persistent.bangok_cervpen == True:
            m "They let out a little gasp, inner walls clenching around the toy that was still deeply embedded within them, plugging their overly-stuffed womb."
            menu:
                "Oh, I uh... should probably pull this out.":
                    pass
                "Do you want this left in for a while?":
                    $ bangok_four_lorem4_store.condom_left_in = True # Using same tag as visually will be the same so no need to use another tag.
                    m "Lorem's eyes lit up in need, and I let out a chuckle as I complied."
                    m "Using my fingers, I managed to push the remains of the condom bag that had held the fake cum into the bottom of the toy, plugging it."
                    m "Due to the expansion of their womb because of the fake cum, I could then push the toy even further in than before."
                    if persistent.bangok_cloacas == True:
                        m "Lorem let out another shudder from the increasing pressure on their womb as the end of the toy popped into them fully, their slit clamping down afterwards, keeping the toy inside."
                    else:
                        m "Lorem let out another shudder from the increasing pressure on their womb as the end of the toy popped into them fully, the enterence to their vagina clamping down afterwards, keeping the toy inside."
                    jump bangok_four_lorem4_femaleplayer_choices
        else:       
            m "They let out a little gasp, inner walls clenching around the toy that was still lodged with them, the end of the toy kissing their cervix and helping plug their stuffed womb." 
        c "Oh, I uh... should probably pull this out."
        Lo shy bangok bulge erect "Probably..."
        show lorem happy bangok shy bulge erect with dissolve
        $ renpy.pause (0.1)
        hide lorem with dissolve
        if persistent.bangok_cervpen == True:
            m "I slowly pulled out the toy. Lorem held their belly as the toy left the confines of their womb, allowing fake cum to soak into their now-stretched canal."
            if persistent.bangok_cloacas == True:
                m "As I finished pulling the toy from Lorem's stuffed cloaca they gasped, legs shuddering, as a slick flow of fake cum mixed with Lorem's fluids followed, running over both of our lower bodies."
            else:
                m "I finished pulling the toy from Lorem's stuffed vagina they gasped, legs shuddering, as a slick flow of of fake cum mixed with Lorem's fluids followed, running over both of our lower bodies."            
        elif persistent.bangok_cloacas == True:
            m "I pulled the toy slowly out of Lorem's stuffed cloaca. They gasped, legs shuddering, as a slick flow of fake cum mixed with Lorem's fluids followed, running over both of our lower bodies."
        else:
            m "I pulled the toy slowly out of Lorem's stuffed vagina. They gasped, legs shuddering, as a slick flow of fake cum mixed with Lorem's fluids followed, running over both of our lower bodies."
    else:
        Lo shy "T-Thanks."
        Lo blush "That felt a lot better than I was expecting."
        c "Oh, I uh... should probably pull out."
        Lo shy "Probably..."
        show lorem happy bangok shy with dissolve
        hide lorem with dissolve
        if persistent.bangok_cervpen == True:
            m "I slowly pulled out the toy. A slow drip of fake cum followed as the toy left the confines of their womb, dribbling down into their stretched canal."    
            if persistent.bangok_cloacas == True:
                m "I finished pulling the toy out of Lorem's spread cloaca. They gasped, legs shuddering as a small flow of fake cum mixed with Lorem's fluids followed, running over both of our lower bodies."
            else:
                m "I finished pulling the toy out of Lorem's spread vagina. They gasped, legs shuddering as a small flow of fake cum mixed with Lorem's fluids followed, running over both of our lower bodies."
        elif persistent.bangok_cloacas == True:
            m "I finished pulling the toy out of Lorem's spread cloaca. They gasped, legs shuddering as a small flow of fake cum mixed with Lorem's fluids followed, running over both of our lower bodies."
        else:
            m "I finished pulling the toy out of Lorem's spread vagina. They gasped, legs shuddering as a small flow of fake cum mixed with Lorem's fluids followed, running over both of our lower bodies."
    Lo sleep blush "Ohhh..."
    
label bangok_four_lorem4_femaleplayer_choices:
    m "I gently lifted them up from my legs and placed them back on the table."

label todo_lorem4_femaleplayer_out_of_content:
    play sound "fx/system3.wav"
    s "TODO: Out of content! Roll back or prepare to crash."
    $ renpy.error("Out of content.")