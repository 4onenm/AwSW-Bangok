init python in bangok_four_lorem3:
    wormtype = None # "legged" or "smooth"
    mc_position = None # "cock", "ass", or "vag"
    mc_protected = False # bool
    mc_wormsout = 0 # Z[0, ???)
    mc_wormsin = 0 # Z[0, ???)

    lorem_position = None # "cock", "oral"
    lorem_protected = False # bool
    lorem_wormsin = 0 # Z[0, ???)


    abort_target = None

screen bangok_four_lorem3_abortscreen:
    if bangok_four_lorem3.abort_target is None:
        $ renpy.error("bangok_four_lorem3.abort_target not set for bangok_four_lorem3_abortscreen")
    textbutton "Pull back":
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.6
        action [Hide('bangok_four_lorem3_abortscreen'),Jump(bangok_four_lorem3.abort_target)]




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

    Lo think bangok "Then... I guess..."
    Lo think bangok "Do you want to go first and then I'll stick my, um, thing in you?"
    Lo shy bangok "O-or do you want me to go first?"
    Lo shy bangok "Or should we both get some in different, um..."
    Lo relieved bangok "I don't know."

    menu:
        "I'll go first.":
            # Scene is locked behind having sex with Ipsum, so gender must be decided by now
            m "Hesitating for a few moments, I confirmed my decision to myself, then began to strip out of my clothing."
            if bangok_four_playerhasdick == True:
                Lo think bangok "Are you going to just stick your, ah, penis in it?"
                Lo shy bangok "O-Or let the little things climb up your ass?"
                menu:
                    "Dick.":
                        $ bangok_four_lorem3.mc_position = "dick"
                        Lo think bangok "Well..."
                        play sound "fx/pages.ogg"
                        $ renpy.pause(0.8)
                        Lo shy bangok "O-Oh!"
                        Lo relieved bangok "Y-You might want a condom for that. 'Cause if you don't they might..."
                        Lo shy bangok "...might go inside."
                        menu:
                            "Use a condom.":
                                $ bangok_four_lorem3.mc_protected = True
                            "Is that still safe?":
                                Lo think bangok "That's what the guide says. But I'm not sure I'd want to try that."
                                Lo shy bangok "You know. With mine."
                                menu:
                                    "Use a condom.":
                                        $ bangok_four_lorem3.mc_protected = True
                                    "Use site unprotected.":
                                        $ bangok_four_lorem3.mc_protected = False
                            "Use site unprotected.":
                                $ bangok_four_lorem3.mc_protected = False
                        
                        if bangok_four_lorem3.mc_protected == True:
                            m "Lorem handed me a condom packet from the box, but I found it concerningly small."
                            c "Are you sure this is a size that'll fit over my...?"
                            Lo think bangok "W-Well, the guide says if you're going to use one, you need to use the smallest that'll fit."
                            Lo shy bangok "O-Or they'll go underneath it and... y'know."
                            m "After a couple tries, and spreading a bit of my pre, I managed to wedge the condom ring over my head and start to unroll it down my shaft."
                        jump bangok_four_lorem3_mcgoes_stick_dick_in_crazy
                    "Ass.":
                        $ bangok_four_lorem3.mc_position = "holes"
                        jump bangok_four_lorem3_mcgoes_hole_filler
            else:
                $ bangok_four_lorem3.mc_position = "holes"
                Lo shy bangok "O-Okay."
                jump bangok_four_lorem3_mcgoes_hole_filler

        "I want to see you try it first.":
            jump bangok_four_lorem3_loremgoes


label bangok_four_lorem3_mcgoes_stick_dick_in_crazy:
    $ renpy.pause(0.5)
    scene bangok_four_forest_treehole at Pan((0, 0), (0, 837), 5.0) with dissolvemed
    m "I stepped up to the tree, leaning on the trunk to put my dick at the right height."
    m "Then I sank carefully into the hole, bumping the bark slightly with my head as I got into position."
    $ bangok_four_lorem3.abort_target = 'bangok_four_lorem3_mcgoes_stick_dick_in_crazy_abort'
    show screen bangok_four_lorem3_abortscreen
    $ renpy.pause(0.8)
    m "After a few moments, one of the small, wriggling worms seemed to take notice of the shadow that fell over its tree hole, and began to approach."
    $ renpy.pause(0.8)
    if bangok_four_lorem3.wormtype == "legged":
        if bangok_four_lorem3.mc_protected == False:
            m "It reared back, then clambered onto my cockhead, tiny legs feeling like dozens of pinpricks across my exposed skin."
        else:
            m "It reared back, then clambered onto my cockhead, tiny legs feeling like dozens of pinpricks across my skin through the condom."
        $ bangok_four_lorem3.mc_wormsout = 1
        m "Then it lifted off the ground of its little world, swinging the rest of itself back to grab on further down my shaft."
        m "It started moving, crawling up on top of my shaft, snaking down toward my base with its hundreds of tiny legs, each a pinprick adding up to a heady, electric sensation in my groin."
        Lo shy "Uhm. Wow."
        if bangok_four_lorem3.mc_protected == False:
            m "Then it pulled a tight 180, pricking its way back toward my head."
            m "It circled my tip once, winding tightly before rearing up over my exposed urethra."
            $ bangok_four_lorem3.mc_wormsout = 0
            $ bangok_four_lorem3.mc_wormsin = 1
            c "Nngh!"
            m "My cock twitched from the unusual penetration as the worm began wriggling into my channel. I could feel every leg rising and falling in rhythm, undulating inside my shaft."
            m "In a moment the worm disappeared, climbing completely inside my urethra and crawling its way down."
            Lo think "Are you ok?"
        else:
            m "I felt it tug at the ring of the condom with its little legs, and quickly rolled the condom a little tighter against my base to keep it out of the worm's reach."
            m "Turning away, the worm started a slow spiral up my shaft, pinpricks of legs moving centimeter by centimeter."
            Lo shy "H-How does that feel?"
        m "I thrust my hips against the sensation, dislodging another three worms I had missed crawling on the ceiling of the tree's opening."
        $ bangok_four_lorem3.mc_wormsout = 3
        m "They all latched on, hundreds more legs wrapping around my shaft than just the first alone."
        if bangok_four_lorem3.mc_protected == False:
            m "One immediately went for my tip, while the other two circled around underneath my shaft."
            m "I panted, hugging the tree, as the ones outside crawled over my channel and overtop the one already wriggling within me."
            m "The one inside was almost down to my base, poking and prodding at my channel as it worked its way inside my body."
            $ bangok_four_lorem3.mc_wormsout = 2
            $ bangok_four_lorem3.mc_wormsin = 3
            m "The one at my tip entered, followed immediately by another from directly inside the tree."
        else:
            jump todo_out_of_content_bangok_four_lorem3
    else: # smooth:
        if bangok_four_lorem3.mc_protected == False:
            m "It reared back, then touched to the side of my cockhead, feeling cold and slimy on my exposed skin."
        else:
            m "It reared back, then touched to the side of my cockhead, feeling cold and slimy even through the condom's skin."
        $ bangok_four_lorem3.mc_wormsout = 1
        m "It wriggled a little higher on the side of my shaft, seeming almost to stick to the surface as I struggled to keep my breathing even and my shaft in place."
        m "Then it swung up, slapping to the bottom of my shaft as its sticky, sliminess kept it held on."
        m "I let out a shuddering breath as it began to slither around to the top of my shaft, snaking down toward my base and leaving a cold trail of heady, electric need in my groin."
        Lo shy "Uhm. Wow."
        if bangok_four_lorem3.mc_protected == False:
            m "The worm curled up, then began slithering back up toward my cockhead, leaving another sticky trail on my skin as it worked its way back down my length."
            m "It circled my tip once, sticking tightly before rearing up over my exposed urethra."
            $ bangok_four_lorem3.mc_wormsout = 0
            $ bangok_four_lorem3.mc_wormsin = 1
            c "Nngh!"
            m "My cock twitched from the unusual penetration as the worm began wriggling into my channel. I could feel the sensation of its unusual cold and slimy skin now undulating inside my shaft."
            m "In a moment the worm disappeared, snaking completely inside my urethra and wriggling its way down."
            Lo think "Are you ok?"
        else:
            jump todo_out_of_content_bangok_four_lorem3
        m "I thrust my hips against the sensation, dislodging another three worms I had missed crawling on the ceiling of the tree's opening."
        $ bangok_four_lorem3.mc_wormsout = 3
        m "They all stuck tightly, holding on and beginning to slither around my shaft themselves."
        if bangok_four_lorem3.mc_protected == False:
            m "One immediately went for my tip, while the other two circled around underneath my shaft."
            m "I panted, hugging the tree, as the ones circling outside clung to the skin under my channel, right next to the one already wriggling within me."
            m "The one inside was almost down to my base, wriggling in and sliming my channel as it worked its way inside my body."
            $ bangok_four_lorem3.mc_wormsout = 2
            $ bangok_four_lorem3.mc_wormsin = 3
            m "The one at my tip entered, followed immediately by another from directly inside the tree."
        else:
            jump todo_out_of_content_bangok_four_lorem3

    m "I sank in deeper, hips against the bark as the wriggling mass pleasuring me thus far drove up my arousal."
    Lo relieved bangok "H-Hey! Now I can't see!"

    if bangok_four_lorem3.mc_protected == False:
        $ bangok_four_lorem3.mc_wormsout = 26
        m "Dozens more wriggled about my head inside the tree, fighting for the chance to crawl inside me."
        $ bangok_four_lorem3.mc_wormsin = 10
        m "A fourth and a fifth worked into my tip. Then I lost count, as the worms moved one after another after another to sink inside."
        if bangok_four_lorem3.wormtype == "legged":
            m "The first, now deep inside my body, pushed my pleasure button from the inside out, with a series of tight pinpricks that drove me over my peak."
        else:
            m "The first, now deep inside my body, pushed my pleasure button from the inside out, wriggling in against it with tight undulations that drove me over my peak."
        scene black with dissolve
        c "Ah!"
        m "... but no cum, no release came forth from my shaft."
        $ bangok_four_lorem3.mc_wormsout = 42
        $ bangok_four_lorem3.mc_wormsin = 15
        m "I writhed, unable to get release as yet more worms joined the task of pleasuring me."
        m "They crawled over each other on the surface of my shaft, spilling down toward my base as each struggled to be the next to join the long train worming yet deeper inside me."
        $ bangok_four_lorem3.mc_wormsin = 21
        m "Then I felt two push in at once, and swooned against the bark of the tree."
        Lo shy bangok "W-Woah. Your, uh, your \"scrotum\"..."
        m "I could feel what Lorem was referencing, as the first of the little worms squeezed from the tiny tubes deep in my body and into my balls."
    else:
        jump todo_out_of_content_bangok_four_lorem3

    if (bangok_four_lorem3.mc_protected == True) or (persistent.bangok_inflation == False):
        label bangok_four_lorem3_mcgoes_stick_dick_in_crazy_done:
        hide screen bangok_four_lorem3_abortscreen
        m "That was when my legs gave out from the intense sensations in my groin, dropping me from the hole in the tree."
        scene bangok_four_forest_clearing at Pan((0, 520), (0, 520), 0.0)
        show lorem shy bangok at center
        with vpunch
        jump bangok_four_lorem3_mcgoes_stick_dick_in_crazy_abort

    # Fill 'em up!
    if persistent.bangok_watersports == True:
        m "I also felt another squeezing, and a need to piss. I moaned as some of the worms picked the other path out of my prostate, wriggling up into my bladder to explore and defile the larger internal volume."

    $ bangok_four_lorem3.wormsout = 104
    if bangok_four_lorem3.wormtype == "legged":
        m "The pinprick of legs from the crawling critters had turned into a static mass of unending, electric sparks of pleasure thick enough over my genitals, I had to wonder if I could even see the flesh of my cock if I pulled it out of the tree, or if I'd only see the mass of tiny segmented legs."
        $ bangok_four_lorem3.wormsin = 42
        m "More worms joined the first within my balls, stretching and prodding my sack. The thousands of pinpricks and pinches of their wriggling segmented bodies around my sensitive organs left me with a desperate, unsatisfied need for release."
    else: # smooth
        m "The slimy stickiness from the wriggling worms felt like it had turned my crotch to jelly, kneading inside and out, all around. I had to wonder if I could even see the flesh of my cock if I pulled it out of the tree, or if I'd only see the semi-gelatinous mass of tiny, slithering creatures."
        $ bangok_four_lorem3.wormsin = 42
        m "More worms joined the first within my balls, stretching and prodding my sack. I couldn't count all the wriggling bodies inside, couldn't think enough to worry as their movements around my sensitive organs left me with a desparate, unsatisfied need for release."

    m "More still demanded entry at my tip, stretching my channel as clusters of three and four tried and failed to enter together, breaking into doubles and singles as they actually wormed their way inside me."

    if persistent.bangok_watersports == True:
        m "The overstimulation of the endless flow only seemed to worsen as more poured into my bladder, my increasingly bad need to piss multiplying the sensations elsewhere."

    $ wormsin = 104
    Lo shy bangok "Eeep! I-Is that supposed to happen?!"
    if bangok_four_lorem3.wormtype == "legged":
        m "My sack bloated, the prickly mass of critters too large to be contained any other way."
    else: # smooth
        m "My sack bloated, the slimy mass of critters too large to be contained any other way."
    m "Just when I thought there wasn't a way in the world to heighten my edge further, my cockhead expanded around a trio of worms forcing their way in at once, then a second and a third."

    $ wormsin = 154
    hide screen bangok_four_lorem3_abortscreen
    with dissolvemed

    if persistent.bangok_watersports == True:
        m "My bladder wasn't enough to contain the wriggling tide. As more worms forced their way in, I felt the bottom of my stomach begin to distend, navel pushed up and out by a bulging mass."

    m "I wasn't sure I could pull out now if I wanted to, the nerves in my legs failing from the unprecedented, stimulating use of my organs. Only leaning against the tree kept me upright and in place."

    Lo shy bangok "C-Can I touch your scrotum?"

    m "As I lay on the tree, panting into the bark with my cock still buried inside, the cold keratin of Lorem's claws lifted one of my balls."

    c "Ohhhhh!"

    m "Abruptly, one climax finally broke through, ripping down my distended, wriggling tube as I forced a couple of the worms back out in the highest peak I'd ever experienced."
    m "Then more worms filled the gap."

    Lo think bangok "Um..."
    m "Lorem climbed up my legs, until his cock rubbed between my thighs and under my bulging sack."
    Lo shy bangok "May I... may I try some and try... your ass?"
    m "It was hard to string together syllables into a word, much less more."
    menu:
        "{i}H-Help mee s-stoooop.{/i}":
            Lo shy bangok "Oh! Oh you're not--"
            m "He clawed his way up the tree next to me, then planted his feet on my shoulder. With a shove using his whole body, he pried my limp, blissed-out form off the tree bark where I could fall to the ground."
            scene bangok_four_forest_clearing at Pan((0, 520), (0, 520), 0.0)
            show lorem sad bangok at center
            with vpunch
            jump bangok_four_lorem3_mcgoes_stick_dick_in_crazy_abort
        "{i}Please.{/i}":
            pass



    jump todo_out_of_content_bangok_four_lorem3

label bangok_four_lorem3_mcgoes_stick_dick_in_crazy_abort:
    jump todo_out_of_content_bangok_four_lorem3



label bangok_four_lorem3_mcgoes_hole_filler:
    jump todo_out_of_content_bangok_four_lorem3


label bangok_four_lorem3_loremgoes:
    jump todo_out_of_content_bangok_four_lorem3


label todo_out_of_content_bangok_four_lorem3:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")