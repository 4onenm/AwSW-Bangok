init python in bangok_four_xipsum2_store:
    protection = False

    scene_type = None
    # ponahole - Player is Ipsum's toy
    # idildo - Ipsum's cocks are player's toy
    # ionahole - Ipsum's ass is Player's toy

    scene_subtype = None
    # ponahole:
    #     dp
    #     anal1
    #     anal2
    #     vag1
    #     vag2
    # idildo:
    # ionahole:
    #     oral
    #     anal1
    #     anal2

    suck_spare = False
    # In scenes where only one of Ipsum's cocks are involved, allow the player to suck the spare.

    separate = False
    # True - Ipsum goes to the other room to fuck MC / be fucked by MC
    # False - Ipsum takes a seat on the couch with the MC to fuck/be fucked

    ws = False
    player_pissed = False

    ponahole_unasked = True
    idildo_unasked = True
    ionahole_unasked = True
    whychoose_unasked = True


    # sharing:
    has_both = False
    shared_with = None
    # This "sharing" enum covers extra use scenes.
    #  0 - Not shared.
    #  1 - The player only shared it with the target.
    #  2 - The player shared it with the target and a small group.
    #  3 - Free use for the target's friends.
    sharing = 0

    sharing_unsanitary = False


label bangok_four_xipsum2_answ_machine:
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.5)
    Ip happy "Hello, [player_name]! It's Ipsum, Lorem's roommate."
    Ip normal bangok blush "I've just developed something that, given our last encounter, I believe you will find quite stimulating."
    $ renpy.pause (0.5)
    Ip think "Whatever fits your schedule, of course. But it {i}may{/i} no longer be available after the coming fireworks."
    Ip normal "Call me back when you get the chance."
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.8)
    c "(Stimulating, huh?)"
    jump ml_answeringmachine_end

label bangok_four_xipsum2_replay_start:
    $ c4csplayed = 0
label bangok_four_xipsum2:
    stop music fadeout 1.0
    $ c4csplayed += 1
    $ chap4picka = "ipsum"
    play sound "fx/steps/clean2.wav"
    scene black with dissolveslow

    $ save_name = (_("Chapter 4 - Bangok Ipsum 2"))

    $ renpy.pause (1.0)
    scene loremapt at Pan ((0, 0), (128,62), 5.0) with dissolveslow

    play music "mx/snowflake.ogg" fadein 2.0

    play sound "fx/door/door_open.wav"

    $ renpy.pause (2.0)

    Ip happy "[player_name], welcome back."

    show ipsum happy bangok briefs at center with dissolve

    if persistent.bangok_four_xipsum2_skip == True and (not _in_replay):
        stop music fadeout 1.0
        $ renpy.pause (0.3)
        play sound "fx/system3.wav"
        call syscheck from _call_bangok_four_syscheck_xipsum2
        call skiptut from _call_bangok_four_skiptut_xipsum2
        if skipbeginning == False:
            if system == "normal":
                s "My records indicate you have already experienced this scene in a satisfactory manner. Would you like to skip to the end?"
            elif system == "advanced":
                s "It looks like you've seen this before. Skip to the end of this scene?"
            else:
                s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the end of this scene."
        $ skipbeginning = False
        menu:
            "Yes. I want to skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                scene black with dissolvemed
                play sound "fx/door/close2.wav"
                $ renpy.pause (2.0)
                $ persistent.skipnumber += 1
                call skipcheck from _call_bangok_four_skipcheck_xipsum2

                scene bangok_four_xipsum_bedroom ceiling:
                    alignaround (0,0)
                    # pos (0, -456)
                    pos (-128,0)

                show ipsum normal bangok blush flip:
                    zoom 1.8
                    alignaround (0.5,0)
                    xpos 0.18
                    ypos 0.6
                with dissolvemed

                play music "mx/snowflake.ogg" fadein 2.0
                jump bangok_four_xipsum2_skip
            "No. Don't skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                play music "mx/snowflake.ogg" fadein 2.0

    c "Hey Ipsum."

    menu:
        "What's this about?":
            $ renpy.pause (0.5)
        "You wear clothes now?":
            show ipsum think bangok briefs with dissolve
            $ renpy.pause (0.5)
            c "Well, pants. What are those, swimming briefs?"
            Ip think bangok briefs "Well, yes. With some modifications."
    Ip normal bangok briefs "As I implied in my call, this will be another encounter of a sexual kind. Are you okay with that?"
    c "I wouldn't be here if I wasn't."
    show ipsum happy bangok briefs with dissolve
    c "The implication was pretty clear."
    Ip happy bangok briefs "Good."
    Ip think bangok briefs "And before we go any further, I should ask if you would prefer to use protection."
    Ip normal bangok briefs "According to the results I obtained from our last meeting's samples, there is no strict chemical or biological issue I can detect with us having fun unprotected."
    Ip "Still, it is up to you."

    menu:
        "Yeah, I'd prefer protection.":
            $ renpy.pause (0.5)
            Ip normal bangok briefs "One moment, then."
            $ renpy.pause (0.3)
            show ipsum normal bangok briefs flip with dissolve
            $ renpy.pause (0.3)
            hide ipsum with easeoutright
            $ renpy.pause (0.3)
            play sound "fx/door/close2.wav"
            $ renpy.pause (1.0)
            play sound "fx/door/close2.wav"
            $ renpy.pause (0.5)
            show ipsum normal bangok briefs with easeinright
            $ renpy.pause (0.3)
            $ bangok_four_xipsum2_store.protection = True
            if bangok_four_playerhasdick == True:
                m "He handed me a condom packet, still wrapped in its foil cover."
            Ip happy bangok briefs "Where were we?"
        "Unprotected, sure.":
            $ renpy.pause (0.5)
            $ bangok_four_xipsum2_store.protection = False
            Ip normal bangok blush briefs "Excellent."

    c "What now?"
    Ip happy bangok briefs "Now, if you would, strip and put these on."
    play sound "fx/necklace.ogg"
    m "He handed me an identical-looking pair of swim briefs he'd had tucked into his waistband near his tail, which were surprisingly heavy for their size."
    m "I glanced inside. Apart from a pair of dark disks sewn in toward the bottom, likely the source of the weight, I couldn't find anything amiss."
    menu:
        "What are these going to do?":
            $ renpy.pause (0.5)
            Ip normal bangok briefs "You'd find out relatively quickly if you put them on."
            menu:
                "I'm not a fan of surprises, Ipsum.":
                    Ip think bangok briefs "Are you sure? Part of the stimulation is in not knowing what is going to happen."
                    c "Ipsum, I swear to--"
                    Ip sad bangok briefs "Fine, fine."
                    $ renpy.pause (0.3)
                    show ipsum sad bangok briefs touch with dissolve
                    $ renpy.pause (0.3)
                    play sound "fx/flicker.ogg"
                    $ renpy.pause (0.1)
                    show ipsum sad bangok briefs touch glow with None
                    m "As Ipsum reached into his briefs and fiddled with something, abruptly the disks in the pair he'd handed me lit up. I saw three of his fingers waggling through the center of one disk."
                    c "(Cameras and screens? I don't...)"
                    m "Then I realized his fingers were actually sticking out of the disk."
                    c "Woah!"
                    Ip happy bangok briefs touch glow "\"Woah,\" indeed."
                    Ip normal bangok briefs touch glow "Would you like to put them on, now?"
                    c "Y-Yeah, sure."
                    play sound "fx/undress.ogg"
                    $ renpy.pause (0.5)
                    queue sound "fx/leather.ogg"
                    $ renpy.pause (1.0)
                    if bangok_four_playerhasdick is None:
                        m "I stripped out of my clothes, then pulled the strange briefs most of the way up. I kept them off my waist, though, still looking down at the glowing disks past my..."
                        menu:
                            m "I stripped out of my clothes, then pulled the strange briefs most of the way up. I kept them off my waist, though, still looking down at the glowing disks past my..."
                            "...hardening cock.":
                                $ bangok_four_playerhasdick = True
                            "...dampening hole.":
                                $ bangok_four_playerhasdick = False
                    else:
                        m "I stripped out of my clothes, then pulled the strange briefs most of the way up. I kept them off my waist, though, still looking down at the glowing disks."
                "Alright, fine.":
                    jump bangok_four_xipsum2_surprise
        "[[Put them on.]":
            label bangok_four_xipsum2_surprise:
            $ renpy.pause (0.5)
            show ipsum normal bangok blush briefs with dissolve
            play sound "fx/undress.ogg"
            $ renpy.pause (0.5)
            m "I stripped out of my clothes, since it was nothing Ipsum hadn't seen last time. Then I stepped into the tight pair of swim briefs and pulled them up."
            play sound "fx/leather.ogg"
            $ renpy.pause (1.0)
            c "How's that?"
            Ip "Ideal."
            $ renpy.pause (0.3)
            show ipsum happy bangok briefs touch with dissolve
            $ renpy.pause (0.3)
            m "To my confusion, he reached inside of his briefs and fiddled with something."
            play sound "fx/flicker.ogg"
            $ renpy.pause (0.1)
            show ipsum happy bangok briefs touch glow with None
            if bangok_four_playerhasdick is None:
                m "Abruptly, I felt..."
                menu:
                    m "Abruptly, I felt...{fast}"
                    "Cold claws stroking my balls.":
                        $ bangok_four_playerhasdick = True
                    "Cold claws sinking into my lower lips' folds.":
                        $ bangok_four_playerhasdick = False
            if bangok_four_playerhasdick == True:
                m "Abruptly, I felt {fast}cold claws and scaly fingers stroking down the back of my balls."
            else:
                m "Abruptly, I felt {fast}cold claws and scaly fingers sinking into the folds of my lower lips."

            show loremapt at Pan ((0, 0), (128,72), 0.0) with vpunch
            m "I yelped, dropping to my knees and grabbing at the briefs, then yanking them down to discover what Ipsum had done."
            $ renpy.pause(0.3)
            m "Three of his fingers waggled out at me from one of the disks, which were now glowing."
            c "Woah!"
            Ip happy bangok briefs touch glow "\"Woah,\" indeed."
            show loremapt at Pan ((0, 0), (128,62), 0.0) with ease
            m "Mystery sensations explained, I got back to my feet, though kept the briefs pulled down a little so I could look at the strange disks."
    c "How do these work?"
    Ip think bangok briefs "Well, during all of my idle research into the black hole, wormhole theory on the portal, I discovered the Minister of Science had launched a secret program at the production facility attempting to replicate the portal technology, and..."
    Ip happy bangok briefs "The short answer is I have no idea. I may have \"borrowed\" them from another lab during the hubub of the police coming to raid a third party."
    c "... I see."
    Ip think bangok briefs "You can keep that secret, can't you [player_name]?"
    c "Sure."
    Ip happy bangok briefs "Excellent. Then, would you like something a little more substantive than my fingers?"
    if bangok_four_playerhasdick == False:
        Ip "Say, a pair of Ipsum-brand dildos. Or perhaps you might be willing to offer a human-brand onahole or two."
    else:
        Ip "Say, a pair of Ipsum-brand dildos. Or perhaps you might be willing to offer a human-brand onahole."

label bangok_four_xipsum2_scene_type_choice:
    menu:
        "You can turn my holes into your sex toy with this?" if bangok_four_playerhasdick==False and bangok_four_xipsum2_store.ponahole_unasked == True:
            $ bangok_four_xipsum2_store.ponahole_unasked = False
            $ renpy.pause(0.5)
            if persistent.bangok_watersports == True:
                Ip think bangok briefs "And my urinal, too, if you're so inclined to that sort of thing. All you'd need to do is keep the briefs on, and I should have full access."
            else:
                Ip think bangok briefs "Easily, yes. All you'd need to do is keep the briefs on, and I should have full access."
            Ip normal bangok briefs "Is that what you want?"
            menu:
                "Yes.":
                    $ renpy.pause(0.5)
                    $ bangok_four_xipsum2_store.ws = persistent.bangok_watersports == True
                    jump bangok_four_xipsum2_ponahole
                "I don't want to be your urinal, but I'm for the sex." if persistent.bangok_watersports == True:
                    $ renpy.pause(0.5)
                    $ bangok_four_xipsum2_store.ws = False
                    jump bangok_four_xipsum2_ponahole
                "Let me think about my other options.":
                    jump bangok_four_xipsum2_scene_type_choice
        "You can turn my ass into your sex toy with this?" if bangok_four_playerhasdick == True and bangok_four_xipsum2_store.ponahole_unasked == True:
            $ bangok_four_xipsum2_store.ponahole_unasked = False
            $ renpy.pause(0.5)
            if persistent.bangok_watersports == True:
                Ip think bangok briefs "And my urinal, too, if you're so inclined to that sort of thing. All you'd need to do is keep the briefs on, and I should have full access."
            else:
                Ip think bangok briefs "Easily, yes. All you'd need to do is keep the briefs on, and I should have full access."
            Ip normal bangok briefs "Is that what you want?"
            menu:
                "Yes.":
                    $ renpy.pause(0.5)
                    $ bangok_four_xipsum2_store.ws = persistent.bangok_watersports == True
                    jump bangok_four_xipsum2_ponahole
                "I don't want to be your urinal, but I'm for the sex." if persistent.bangok_watersports == True:
                    $ renpy.pause(0.5)
                    $ bangok_four_xipsum2_store.ws = False
                    jump bangok_four_xipsum2_ponahole
                "Let me think about my other options.":
                    jump bangok_four_xipsum2_scene_type_choice
        "Oh, fuck me. Human-brand onahole, sure." if bangok_four_xipsum2_store.ponahole_unasked == False:
            $ renpy.pause(0.5)
            if persistent.bangok_watersports == True:
                Ip normal bangok briefs "And about that little suggestion of using said onahole to... relieve myself?"
                menu:
                    c "(Do I want Ipsum pissing in me?)"
                    "Yes.":
                        $ renpy.pause(0.5)
                        $ bangok_four_xipsum2_store.ws = True
                    "No.":
                        $ renpy.pause(0.5)
                        $ bangok_four_xipsum2_store.ws = False
            if persistent.bangok_watersports == True and bangok_four_xipsum2_store.ws == False:
                Ip sad bangok briefs "Very reasonable. As you wish."
            else:
                Ip normal bangok briefs "I promise you won't regret it."
            jump bangok_four_xipsum2_ponahole
        "Ipsum-brand dildos sound amusing." if bangok_four_xipsum2_store.idildo_unasked == True:
            $ bangok_four_xipsum2_store.idildo_unasked = False
            $ renpy.pause(0.5)
            Ip happy bangok briefs "They do indeed."
            Ip normal bangok briefs "Is that what you want?"
            menu:
                "Yes.":
                    $ renpy.pause(0.5)
                    jump bangok_four_xipsum2_idildo
                "Let me think about my other options.":
                    jump bangok_four_xipsum2_scene_type_choice
        "I'll have two Ipsum-brand dildos, please." if bangok_four_xipsum2_store.idildo_unasked == False:
            jump bangok_four_xipsum2_idildo
        "What if I want an Ipsum-brand onahole?" if bangok_four_playerhasdick == True and  bangok_four_xipsum2_store.ionahole_unasked == True:
            $ bangok_four_xipsum2_store.ionahole_unasked = False
            $ renpy.pause(0.5)
            Ip think bangok briefs "I could be convinced, though I do somewhat prefer not to be merely the penentrated party."
            menu:
                "I could suck an Ipsum-brand dildo or two at the same time.":
                    $ renpy.pause(0.5)
                    Ip happy bangok briefs "Now, that is a convincing offer."
                    Ip normal bangok briefs "Is that what you want?"
                    menu:
                        "Yes.":
                            $ bangok_four_xipsum2_store.scene_subtype = "oral"
                            $ renpy.pause(0.5)
                            jump bangok_four_xipsum2_ionahole
                        "Let me think about my other options.":
                            jump bangok_four_xipsum2_scene_type_choice
                "I suppose a human-brand onahole might be available.":
                    $ renpy.pause(0.5)
                    Ip normal bangok briefs "Both ways at the same time. Interesting."
                    Ip "Is that what you want?"
                    menu:
                        "Yes.":
                            $ bangok_four_xipsum2_store.scene_subtype = "anal"
                            $ renpy.pause(0.5)
                            jump bangok_four_xipsum2_ionahole
                        "Let me think about my other options.":
                            jump bangok_four_xipsum2_scene_type_choice
                "Let me think about my other options.":
                    $ renpy.pause(0.5)
                    Ip think bangok briefs "As you wish."
                    jump bangok_four_xipsum2_scene_type_choice
        "Okay, one Ipsum-brand onahole for one human blowjob." if bangok_four_xipsum2_store.ionahole_unasked == False:
            $ renpy.pause(0.5)
            $ bangok_four_xipsum2_store.scene_subtype = "oral"
            jump bangok_four_xipsum2_ionahole
        "Okay, one Ipsum-brand onahole for one human-brand onahole." if bangok_four_xipsum2_store.ionahole_unasked == False:
            $ renpy.pause(0.5)
            $ bangok_four_xipsum2_store.scene_subtype = "anal"
            jump bangok_four_xipsum2_ionahole
        "Why do I have to choose?" if bangok_four_xipsum2_store.ponahole_unasked == False and bangok_four_xipsum2_store.idildo_unasked == False and bangok_four_xipsum2_store.whychoose_unasked == True:
            $ bangok_four_xipsum2_store.whychoose_unasked = False
            $ renpy.pause(0.5)
            Ip think bangok briefs "I only have two pairs of the device functioning at the moment, though I did \"borrow\" a few more."
            Ip normal bangok briefs "What we do with them is up to you."
            jump bangok_four_xipsum2_scene_type_choice

label bangok_four_xipsum2_ponahole:
    $ bangok_four_xipsum2_store.scene_type = "ponahole"
    if bangok_four_playerhasdick == False:
        Ip think bangok briefs "Now, what styles of hole are available? And how much can they... accomodate?"
        menu:
            "I have two holes down there, you have two penises.":
                $ bangok_four_xipsum2_store.scene_subtype = "dp"
                $ renpy.pause(0.5)
                Ip happy bangok briefs "Just what I was hoping you'd say."
            "Just my pussy, please, and just one.":
                $ bangok_four_xipsum2_store.scene_subtype = "vag1"
                c "I'm not sure how I feel about this yet."
                Ip "Fair enough."
            "Just my ass, please, and just one.":
                $ bangok_four_xipsum2_store.scene_subtype = "anal1"
                c "I'm not sure how I feel about this yet."
                Ip "Fair enough."
            "I think my pussy can fit both of what you're packing.":
                $ bangok_four_xipsum2_store.scene_subtype = "vag2"
                $ renpy.pause(0.5)
                Ip happy bangok briefs "Sounds like a durable product line, this human-brand."
                c "Okay, don't push that analogy too far."
            "I think my ass can fit both of what you're packing.":
                $ bangok_four_xipsum2_store.scene_subtype = "anal2"
                $ renpy.pause(0.5)
                Ip happy bangok briefs "Sounds like a durable product line, this human-brand."
                c "Okay, don't push that analogy too far."
    else:
        Ip think bangok briefs "Now, exactly how much do you think your style of hole can... accomodate?"
        menu:
            "One of your cocks.":
                $ bangok_four_xipsum2_store.scene_subtype = "anal1"
                c "Let's not stretch things."
                Ip "Fair enough."
            "Both of your cocks.":
                $ bangok_four_xipsum2_store.scene_subtype = "anal2"
                $ renpy.pause(0.5)
                Ip happy bangok briefs "Sounds like a durable product line, this human-brand."
                c "Okay, don't push that analogy too far."


    if bangok_four_xipsum2_store.scene_subtype in ["vag2","anal2"]:
        Ip sad bangok briefs "Well, speaking of that analogy..."
    else:
        Ip think bangok briefs "Next, the sex toy analogy was not merely in jest."

    Ip think bangok briefs "I was curious how well this would work out -- and how this would feel -- if we were in separate rooms."

    menu:
        "Separate rooms sounds interesting...":
            $ bangok_four_xipsum2_store.separate = True
            $ renpy.pause(0.5)
            Ip normal bangok briefs "So you want to try it?"
            c "I guess... yeah. Sure."
            Ip happy bangok briefs "Excellent. Then pull up your briefs, take a seat, and enjoy."

        "That doesn't really sound safe.":
            $ bangok_four_xipsum2_store.separate = False
            $ renpy.pause(0.5)
            Ip sad bangok briefs "It was just a thought."
            Ip think bangok briefs "Let me go fetch the lube, then, in case we need it."
            Ip normal bangok briefs "Pull up your briefs, take a seat, and I'll be right back."

    show ipsum normal bangok briefs touch glow flip with dissolve
    m "Ipsum reached inside his pair of briefs, and below me in mine I could see his fingers working at his side's disks."

    hide ipsum with easeoutright
    play sound "fx/door/close2.wav"

    $ renpy.pause (0.5)
    show loremapt at Pan((128,62),(0,0), 2.0) with ease
    $ renpy.pause (0.5)

    if bangok_four_playerhasdick == True:
        m "I sat on the couch with the briefs pulled up, hands on my crotch, feeling a little awkward as my shaft and balls hung through to open air on the far side, despite the briefs I was wearing."
        m "I jumped, clenching, as my balls were set down on something cold and metallic, wondering just what Ipsum was doing in there."
    else:
        m "I sat on the couch with the briefs pulled up, hands on my crotch, feeling a little awkward as my holes remained exposed to open air, despite the briefs I was wearing."

    if bangok_four_xipsum2_store.scene_subtype in ['dp','anal1','anal2']:
        m "Then, abruptly I felt the cold plastic nozzle of a lube bottle nestling in my crack, just over my asshole."
        c "Ah!"
        m "A thick dollop of chilly lube squirted over my rosebud, rubbed in a moment later by a scaly finger."

    if bangok_four_xipsum2_store.scene_subtype in ['dp','vag1','vag2']:
        m "Cold claws nestled around my outer lips, gently massaging and stimulating my hole, leaving me shivering and slick."

    if bangok_four_xipsum2_store.separate == False:
        $ renpy.pause (0.3)
        play sound "fx/door/close2.wav"
        $ renpy.pause (0.8)
        show ipsum happy bangok briefs at right with easeinright
        m "Ipsum returned, bearing the bottle of lube."
        Ip "Ready?"
        menu:
            "Can we do the separate rooms thing?":
                c "I think I've changed my mind."
                Ip normal bangok blush briefs "Absolutely."
                $ renpy.pause (0.3)
                Ip normal bangok blush briefs flip "Have fun."
                $ renpy.pause (0.3)
                hide ipsum with easeoutright
                play sound "fx/door/close2.wav"
                $ renpy.pause (0.8)
                $ bangok_four_xipsum2_store.separate = True
            "Yeah. You want to sit down, too?":
                $ renpy.pause (0.5)
    if bangok_four_xipsum2_store.separate == False:
        hide ipsum with dissolve
        $ renpy.pause (0.5)
        show ipsum happy bangok briefs touch flip:
            xanchor 0.0
            yanchor 1.0
            xpos 0.0
            ypos 1.25
            rotate -5
        with dissolve
        if bangok_four_xipsum2_store.protection == True:
            m "Ipsum pulled open the fly on his briefs, letting his hard, twin condom-wrapped shafts spill out into the open air."
        else:
            m "Ipsum pulled open the fly on his briefs, letting his hard, twin shafts spill out into the open air."

        menu:
            "Be gentle.":
                $ renpy.pause (0.5)
                Ip "Of course."
            "Are you going to stop teasing and fuck me?":
                $ renpy.pause (0.5)
                Ip "Soon enough."

        if bangok_four_xipsum2_store.scene_subtype in ['vag2','anal2']:
            m "Squeezing his twin shafts together, he brought the disk connected to my hole to their tips."
        elif bangok_four_xipsum2_store.scene_subtype in ['vag1','anal1']:
            m "With baited breath, I watched as he raised the disk linked to my hole to one tip."
        else: # dp
            m "One disk in each hand, Ipsum lifted them over his twitching shafts."

    if bangok_four_xipsum2_store.scene_subtype == 'dp':
        m "Then I felt his shafts at my front and rear entrances, small heads slowly sliding inside."
    elif bangok_four_xipsum2_store.scene_subtype == 'anal1':
        m "Then I felt his cockhead at my rear, its small head slowly sliding inside."
    elif bangok_four_xipsum2_store.scene_subtype == 'anal2':
        m "Then I felt his shafts at my rear, twin heads slowly elongating my sphincter as they together slid inside."
    elif bangok_four_xipsum2_store.scene_subtype == 'vag1':
        m "Then I felt his cockhead nestle between my lips, its small head slowly spreading me as he slipped into my canal."
    elif bangok_four_xipsum2_store.scene_subtype == 'vag2':
        m "Then I felt his shafts at my front entrance, twin heads slowly spreading my folds as they together stretched my hole to slide inside."
    else:
        $ renpy.error ("Impossible scene_subtype %s"%bangok_four_xipsum2_store.scene_subtype)

    m "I arched my back, the sensation of slow insertion without feeling him between my legs an uncanny, wild feeling."


    if '1' == bangok_four_xipsum2_store.scene_subtype[-1]:
        m "He poked around with just his tip for a moment, feeling out the difference between the angle of my hole and that of the disk."
        if bangok_four_xipsum2_store.scene_subtype == 'anal1':
            m "Then he pressed all the way inside, hilting my rear around him."
        else: #vag1
            m "Then he slid all the way inside, spreading my outer folds against his hard belly plates."
        c "Mmmh!"
    else: # vag2, anal2, or dp
        if bangok_four_xipsum2_store.scene_subtype == 'dp':
            m "He poked around with just his tips for a moment, feeling out the difference between the angle of my body and that of the disks."
            m "Then he slid all the way inside, spreading my outer folds and sphincter against his hard belly plates."
            c "Mmmh!"
        else:
            m "He poked around with just his tip for a moment, feeling out the difference between the angle of my body and that of the disk."

    if bangok_four_xipsum2_store.separate == False:
        Ip "How does that feel?"
        menu:
            "I-I've never felt anything like it.":
                $ renpy.pause (0.5)
                m "Ipsum grinned a little wider."
            "Like you should be moving faster.":
                $ renpy.pause (0.8)
                Ip "If you wanted control over our speed, perhaps you should have asked to have my cocks as your dildos to play with."
                $ renpy.pause (1.0)
                m "He waited, teasing me with a lack of motion."
                if '1' in bangok_four_xipsum2_store.scene_subtype:
                    if bangok_four_playerhasdick == True:
                        m "I clenched around him, unseen cock twitching as I struggled to find stimulation for myself."
                    elif bangok_four_xipsum2_store.scene_subtype == 'vag1':
                        m "I clenched, canal spasming around his length as I struggled to find stimulation for myself."
                    else:
                        m "I clenched, empty canal spasming as I struggled to find stimulation for myself."
                elif bangok_four_xipsum2_store.scene_subtype == 'dp':
                    m "I clenched, canal and ass spasming around his lengths as I struggled to find stimulation for myself."
                else:
                    m "I clenched, spasming canal near empty as I struggled to find stimulation from his mere tips."
            "Y-You're a little big with both." if '2' in bangok_four_xipsum2_store.scene_subtype:
                $ renpy.pause (0.5)
                Ip sad bangok briefs touch flip "Oh, really?"
                Ip sad bangok briefs touch flip "Then we can back off to just one."
                if bangok_four_xipsum2_store.scene_subtype == 'vag2':
                    Ip normal bangok briefs touch flip "Unless, that is, your rear entrance happens to be available?"
                menu:
                    "No, I can take this.":
                        c "Just take it easy. I know it looks..."
                        m "I nodded at the disk in his hand, into which his twin penises disappeared to nestle in my clenching hole."
                        c "I'm not a toy, okay?"
                        Ip normal bangok briefs touch flip "Of course."
                    "Sure, take my ass too." if bangok_four_xipsum2_store.scene_subtype == 'vag2':
                        python in bangok_four_xipsum2_store:
                            renpy.pause (0.5)
                            scene_subtype = 'dp'
                        Ip happy bangok briefs touch flip "As you wish."
                    "Just one, please. I can't stretch this much.":
                        python in bangok_four_xipsum2_store:
                            renpy.pause (0.5)
                            if scene_subtype == 'vag2':
                                scene_subtype = 'vag1'
                            else: # anal2
                                scene_subtype = 'anal1'
                        Ip normal bangok briefs touch flip "As you wish."

                if bangok_four_xipsum2_store.scene_subtype[-1] != '2':
                    m "I gasped with relief as Ipsum removed the pressure from my hole, giving me a chance to recover and clench freely."
                    if bangok_four_xipsum2_store.scene_subtype == 'dp':
                        m "Then he lifted a disk to the bottle of lube he'd brought, and I felt the plastic nozzle of the lube bottle nestling in my crack, just over my asshole."
                        c "Ah!"
                        m "A thick dollop of chilly lube squirted over my rosebud, rubbed in a moment later by his scaly finger."
                        m "He raised the lubed toy disk, my ass, to join my vagina over his twin shafts."
                        m "Then I felt his shafts at my front and rear entrances, small heads slowly sliding inside, with far less stretching than before."
                    elif bangok_four_xipsum2_store.scene_subtype == 'anal1':
                        m "Then I felt a single tip at my rear, slipping inside me much more easily as he tugged the disk linked to it onto his length."
                    elif bangok_four_xipsum2_store.scene_subtype == 'vag1':
                        m "Then I felt a single tip in my outer folds, slipping inside me much more easily as he tugged the disk linked to it onto his length."
                    Ip normal bangok briefs touch flip "Now?"
                    c "Mmh. Much better."

                    m "Keeping a slow pace, he slid a little bit further into me at a time, watching me to make sure I wasn't experiencing discomfort."
                    if bangok_four_playerhasdick == True:
                        m "I was, of course, from the maddeningly slow insertion as my shaft twitched with unsatiated need."
                    elif bangok_four_xipsum2_store.scene_subtype == 'dp' or bangok_four_xipsum2_store.scene_subtype == 'vag1':
                        m "I was, of course, from the maddeningly slow insertion as my canal clenched around him."
                    else:
                        m "I was, of course, from the maddeningly slow insertion as my empty canal clenched on nothing."
                    m "Finally he hilted himself inside me, hard plates pressing up against my flesh through the threshold of the disk."


    play soundloop "fx/bangok_poundofsalt.ogg" fadein 7.0
    if bangok_four_xipsum2_store.scene_subtype == 'dp':
        m "After a few moments, Ipsum began to fuck me for real, starting with slow, short movements of both disks evenly, then gradually expanding his motions to longer strokes, twice into my front for every once in my rear."
        $ renpy.pause (1.5)
        m "Though his dicks were duplicates, the one in my rear felt larger, filling me and pressing forward against the one entering my front for maddening stimulation whenever it was in, contrasted against the lackthereof for the alternating strokes he pulled it out."
        $ renpy.pause (1.5)
        m "I ground against the couch cusion, one hand pressing the disk against my crotch, the other the one against my ass, willing him to go deeper and harder as my peak rapidly approached."
    elif bangok_four_xipsum2_store.scene_subtype == 'anal1':
        m "After a few moments, Ipsum began to fuck me for real, length sliding easily into and out of my slickened rear."
        $ renpy.pause (1.5)
        if bangok_four_playerhasdick == True:
            m "My cock twitched and spasmed in empty air, helpless for stimulation as Ipsum's cock used my ass."
        else:
            m "I couldn't help the sensations, eventually reaching down to rub and fondle my outer folds, teasing my outer lips while Ipsum's cock used my ass."
        $ renpy.pause (1.5)
        m "I pushed my butt deeper into the couch, one hand pressing the disk against my butt, willing him to go deeper and harder as my arousal increased."
    elif bangok_four_xipsum2_store.scene_subtype == 'anal2':
        m "After a few moments, Ipsum began to fuck my ass for real. He started with slow, short movements of the disk, then gradually expanded into longer strokes."
        m "His lengths spread open my slickened rear in a way that felt physically impossible without the rest of him pushing into me, heavy under my legs."
        $ renpy.pause (1.5)
        if bangok_four_playerhasdick == True:
            m "My cock twitched and spasmed in empty air, helpless for stimulation as Ipsum's shafts reamed my ass."
        else:
            m "I couldn't help the sensations, eventually reaching down to rub and fondle my outer folds, teasing my outer lips while Ipsum's shafts reamed my ass."
        $ renpy.pause (1.5)
        m "I pushed my butt deeper into the couch, one hand pressing the disk against my butt, willing him to go deeper and harder as my arousal increased."
    elif bangok_four_xipsum2_store.scene_subtype == 'vag1':
        m "After a few moments, Ipsum began to fuck my pussy for real, length sliding easily into and out of my slick passage."
        $ renpy.pause (1.5)
        if bangok_four_xipsum2_store.separate == False:
            m "As I squirmed on the couch, I saw the corners of Ipsum's mouth ticking upward, enjoying the sensations he was bringing me, as much as the pleasure he was bringing himself with my body. The feelings on my end were inescapable and wonderful."
        else:
            m "As I squirmed on the couch, I wondered how this felt and looked for Ipsum -- a simple disk leading to my wet hole. I could only imagine the pleasure he was bringing himself with my body. The feelings on my end were inescapable and wonderful."
        $ renpy.pause (1.5)
        m "I ground against the couch cusion, both hands pressing the disk against my crotch, willing him to go deeper and harder as my peak rapidly approached."
    elif bangok_four_xipsum2_store.scene_subtype == 'vag2':
        m "After a few moments, Ipsum began to fuck my pussy for real. He started with slow, short movements of the disk, then gradually expanded into longer strokes."
        m "His lengths stretched open my outer folds in a way that felt physically impossible without the rest of him pushing into me, heavy under my legs."
        $ renpy.pause (1.5)
        if bangok_four_xipsum2_store.separate == False:
            m "As I squirmed on the couch, I saw the corners of Ipsum's mouth ticking upward, enjoying the sensations he was bringing me, as much as the pleasure he was bringing himself with my body. The feelings on my end were inescapable and wonderful."
        else:
            m "As I squirmed on the couch, I wondered how this felt and looked for Ipsum -- a simple disk leading to my tight hole. I could only imagine the pleasure he was bringing himself with my body. The feelings on my end were inescapable and wonderful."
        $ renpy.pause (1.5)
        m "I ground against the couch cusion, both hands pressing the disk against my crotch, willing him to go deeper and harder as my peak rapidly approached."
    else:
        $ renpy.error ("Impossible scene_subtype %s"%bangok_four_xipsum2_store.scene_subtype)

    if persistent.bangok_watersports == True and bangok_four_xipsum2_store.ws == True:
        stop soundloop fadeout 0.5
        $ renpy.pause (0.8)

        if bangok_four_xipsum2_store.scene_subtype == 'anal1':
            m "Then he stopped, hilted inside me, leaving me gasping in my seat."
        elif bangok_four_xipsum2_store.scene_subtype == 'anal2':
            m "Then he stopped, hilted inside me, leaving me shivering in my seat as my ass was given a few moments to rest."
        else:
            m "Then he stopped, hilted inside me, leaving me maddeningly close to, but short of my peak."

        if bangok_four_xipsum2_store.separate == False:
            Ip happy bangok blush flip "You know, I think I might just take advantage of that offer to relieve myself."

        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"

        if bangok_four_xipsum2_store.scene_subtype == 'dp':
            m "His twin shafts twitched, then hot, wet streams of watery liquid began to spray into my front and rear, saturating my twitching canal and my guts' lowest reaches."
            if bangok_four_xipsum2_store.separate == False:
                m "I flushed with heat, realizing Ipsum was taking me up on that offer of using my holes as his own, portable urinals."
        elif bangok_four_xipsum2_store.scene_subtype == 'anal1':
            if bangok_four_xipsum2_store.separate == False:
                m "Taking tight hold of his free shaft, Ipsum pinched the tip, preventing more than a few droplets of golden liquid from escaping there."
                m "I felt the rest, hot and wet, pouring into my ass, saturating my colon's walls and flowing around his invading length."
            else:
                m "His shaft twitched, then a hot, wet stream of watery liquid began to spurt inside me, saturating my colon's walls."
                m "I flushed with heat, realizing Ipsum was taking me up on that offer of using my ass as his own, portable urinal."
        elif bangok_four_xipsum2_store.scene_subtype == 'anal2':
            m "His twin shafts twitched, then hot, wet streams of watery liquid began to spray inside me, saturating my colon's walls."
            if bangok_four_xipsum2_store.separate == True:
                m "I flushed with heat, realizing Ipsum was taking me up on that offer of using my ass as his own, portable urinal."
        elif bangok_four_xipsum2_store.scene_subtype == 'vag1':
            if bangok_four_xipsum2_store.separate == False:
                m "Taking tight hold of his free shaft, Ipsum pinched the tip, preventing more than a few droplets of golden liquid from escaping there."
                m "I felt the rest, hot and wet, spraying into my canal, saturating my spasming inner walls and flowing around his invading length."
            else:
                m "His shaft twitched, then a hot, wet stream of watery liquid began to spurt inside my spasming canal, saturating my inner walls."
                m "I flushed with heat, realizing Ipsum was taking me up on that offer of using my pussy as his own, portable urinal."
        elif bangok_four_xipsum2_store.scene_subtype == 'vag2':
            m "His twin shafts twitched, then hot, wet streams of watery liquid began to spray inside my spasming canal, saturating my inner walls."
            if bangok_four_xipsum2_store.separate == True:
                m "I flushed with heat, realizing Ipsum was taking me up on that offer of using my pussy as his own, portable urinal."
        else:
            $ renpy.error ("Impossible scene_subtype %s"%bangok_four_xipsum2_store.scene_subtype)

        if bangok_four_xipsum2_store.separate == False:
            Ip normal bangok blush flip "Mmmh."

        stop soundloop fadeout 2.0

        if bangok_four_xipsum2_store.scene_subtype == 'dp':
            jump todo_out_of_content_bangok_four_xipsum
        elif bangok_four_xipsum2_store.scene_subtype == 'anal1':
            jump todo_out_of_content_bangok_four_xipsum
        elif bangok_four_xipsum2_store.scene_subtype == 'anal2':
            jump todo_out_of_content_bangok_four_xipsum
        elif bangok_four_xipsum2_store.scene_subtype == 'vag1':
            jump todo_out_of_content_bangok_four_xipsum
        elif bangok_four_xipsum2_store.scene_subtype == 'vag2':
            jump todo_out_of_content_bangok_four_xipsum
        else:
            $ renpy.error ("Impossible scene_subtype %s"%bangok_four_xipsum2_store.scene_subtype)



    jump todo_out_of_content_bangok_four_xipsum

label bangok_four_xipsum2_idildo:
    $ bangok_four_xipsum2_store.scene_type = "idildo"
    jump todo_out_of_content_bangok_four_xipsum

label bangok_four_xipsum2_ionahole:
    $ bangok_four_xipsum2_store.scene_type = "ionahole"
    $ bangok_four_xipsum2_store.ws = False
    if persistent.bangok_watersports == True and bangok_four_xipsum2_store.protection == False:
        if bangok_four_xipsum2_store.scene_subtype == "oral":
            Ip think bangok briefs "I'm almost sold. But what if, say, I were to need to relieve myself during this blowjob?"
            menu:
                "I'm interested, if I can do the same.":
                    $ renpy.pause (0.5)
                    $ bangok_four_xipsum2_store.ws = True
                    c "I wouldn't want to pay cleaning fees on this Ipsum-brand onahole for a moment of bladder weakness."
                    Ip happy bangok briefs "Don't worry. It's self-cleaning"
                    Ip "I'd say you have yourself a deal."
                "What, like piss in my mouth?":
                    $ renpy.pause (0.5)
                    Ip normal bangok briefs "Nevermind, forget that question."
                    Ip "Deal."
                "No.":
                    $ renpy.pause (0.5)
                    Ip normal bangok briefs "Fair enough."
                    Ip normal bangok briefs "Deal."
        else:
            Ip think bangok briefs "I'm almost sold. But what if, say, I were to need to relieve myself in this onahole?"
            menu:
                "I'm interested, if I can do the same.":
                    $ renpy.pause (0.5)
                    $ bangok_four_xipsum2_store.ws = True
                    c "I wouldn't want to pay cleaning fees on this Ipsum-brand onahole for a moment of bladder weakness."
                    Ip happy bangok briefs "Don't worry. It's self-cleaning"
                    Ip "I'd say you have yourself a deal."
                "What, like piss in my ass?":
                    $ renpy.pause (0.5)
                    Ip normal bangok briefs "Nevermind, forget that question."
                    Ip "Deal."
                "No.":
                    $ renpy.pause (0.5)
                    Ip normal bangok briefs "Fair enough."
                    Ip normal bangok briefs "Deal."


    else:
        Ip happy bangok briefs "Deal."

    if bangok_four_xipsum2_store.scene_subtype == "anal":
        Ip think bangok briefs "Although... can you stretch to accomodate both of my cocks? Or merely one?"
        menu:
            "One.":
                $ bangok_four_xipsum2_store.scene_subtype = "anal1"
                $ renpy.pause(0.5)
                Ip normal bangok briefs "Of course."
            "Both.":
                $ bangok_four_xipsum2_store.scene_subtype = "anal2"
                $ renpy.pause(0.5)
                Ip happy bangok briefs "Feeling adventurous?"
                c "Yeah. We'll give it a try."
    


    m "I looked down at the two disks stuck to the inside of my briefs. "
    c "So how do I...?"
    Ip normal bangok briefs "Allow me."
    show ipsum normal bangok briefs:
        ease 1.5 xanchor 0.5 xpos 0.6 zoom 1.25 ypos 1.1
    with None
    m "Ipsum stepped up to me, then brushed his hand past my hardening shaft to fiddle with the disks in my briefs."
    if bangok_four_xipsum2_store.scene_subtype == "oral":
        m "His hand came up holding both disks, now detatched from the briefs."
        show ipsum happy bangok briefs with dissolve
        m "Ipsum gave me a sly smirk."
        show ipsum sad bangok briefs with dissolve
        m "It vanished a moment later, as his twin cockheads peeked out from the lower of the two disks, causing him to nearly drop the disk resting on top."
        Ip "Whoops. This one, then, is how you'll be able to suck me."
        c "Thanks."
        Ip normal bangok briefs "And this is you new Ipsum-brand asshole toy."
    else:
        m "His hand came up holding the disk from the front, the other still left inside to line up with my rear."
        show ipsum happy bangok briefs with dissolve
        m "Then, with a sly smirk from Ipsum, I saw his twin cocks peeking through the disk in my briefs, slowly sliding through to their full length."
        Ip "Feel free to pull your briefs up, and I will re-aim as desired."
        Ip normal bangok briefs "Meanwhile, this is you new Ipsum-brand asshole toy."
    Ip think bangok briefs "I'll need to go fetch lube, but first I have one more question."
    Ip "How would you feel about taking  this sex toy analogy a little more literally?"
    Ip normal bangok briefs "Say, using each other from separate rooms?"

    menu:
        "Separate rooms sounds interesting...":
            $ bangok_four_xipsum2_store.separate = True
            $ renpy.pause(0.5)
            Ip normal bangok briefs "So you want to try it?"
            c "I guess... yeah. Sure."
            Ip happy bangok briefs "Excellent. Then take a seat on the couch and enjoy. I'll handle lubing your brand new product."

        "That doesn't really sound safe.":
            $ bangok_four_xipsum2_store.separate = False
            $ renpy.pause(0.5)
            Ip sad bangok briefs "It was just a thought."
            Ip think bangok briefs "Let me go fetch the lube, then, in case we need it."
            Ip normal bangok briefs "Take a seat, and I'll be right back."

    show ipsum normal bangok briefs touch glow flip with dissolve
    m "Ipsum reached inside his pair of briefs, and in the disk he'd handed me with access to his ass, I could see his fingers fiddling."
    hide ipsum with easeoutright
    play sound "fx/door/close2.wav"

    $ renpy.pause (0.5)
    show loremapt at Pan((128,62),(0,0), 2.0) with ease
    $ renpy.pause (0.5)


    if bangok_four_xipsum2_store.scene_subtype == "oral":
        play sound "fx/undress.ogg"
        m "Sitting on the couch, I kicked off the briefs I no longer needed, then examined the cocks Ipsum had given me to pleasure, and the hole I'd been given to play with."
        if persistent.bangok_cloacas == True:
            m "At the base of the disk allowing his shafts through, I could see the rim of the other disk, giving me access to his asshole stuffed in his cloaca with his twin lengths."
        else:
            m "There was a thin gap between his belly plates, allowing access to his asshole."
    else:
        play sound "fx/leather.ogg"
        $ renpy.pause (0.1)
        stop sound fadeout 0.5
        m "I tugged the briefs the rest of the way up, his damp cocks nestling lewdly in the small of my back as I awaited lubing down there, and Ipsum's fucking of my hole."
        m "In the meantime, I took a closer look at the disk giving me access to his asshole."
    m "As I watched, the disk exposing his ass lifted away a little, the plunger of a lube bottle entering the view and squirting."
    m "Some drops of the fluid dripped through the disk and onto my hand, as Ipsum began trying to spread it with a finger."

    menu:
        "Help him out.":
            m "I reached in, prodding past his belly plates and a little into his rear with one finger, helping push the lube inside."
            m "His finger retreated, then the lube bottle plunger returned, giving me another healthy dollop to spread around before disappearing again."
        "Do nothing.":
            m "He gave himself another healthy dollop, slathering it around until his adjacent bellyplates shone in the dim glow of the disk."
    if bangok_four_xipsum2_store.scene_subtype != "oral":
        m "His cocks retreated, sliding back down the small of my back and into the waistband of my briefs."
        m "Then I felt the plastic nozzle of the lube bottle nestling in my own crack."
        c "Ah!"
        m "Cold lube squirted over my asshole, rubbed in a moment later by a scaly finger."

    if bangok_four_xipsum2_store.separate == False:
        $ renpy.pause (0.3)
        play sound "fx/door/close2.wav"
        $ renpy.pause (0.8)
        show ipsum happy bangok briefs at right with easeinright
        m "Ipsum returned, bearing the bottle of lube."
        Ip "Ready?"
        menu:
            "Can we do the separate rooms thing?":
                c "I think I've changed my mind."
                Ip normal bangok blush briefs "Absolutely."
                $ renpy.pause (0.3)
                Ip normal bangok blush briefs flip "Have fun."
                $ renpy.pause (0.3)
                hide ipsum with easeoutright
                play sound "fx/door/close2.wav"
                $ renpy.pause (0.8)
                $ bangok_four_xipsum2_store.separate = True
            "Yeah. You want to sit down, too?":
                $ renpy.pause (0.5)
    if bangok_four_xipsum2_store.separate == False:
        hide ipsum with dissolve
        $ renpy.pause (0.5)
        show ipsum happy bangok briefs touch flip:
            xanchor 0.0
            yanchor 1.0
            xpos 0.0
            ypos 1.25
            rotate -5
        with dissolve
        if bangok_four_xipsum2_store.scene_subtype != "oral":
            if bangok_four_xipsum2_store.protection == True:
                m "Ipsum pulled open the fly on his briefs, letting his hard, twin condom-wrapped shafts spill out into the open air."
            else:
                m "Ipsum pulled open the fly on his briefs, letting his hard, twin shafts spill out into the open air."
        else:
            Ip "Well? I am at your mercy, o ambassador."

    if bangok_four_xipsum2_store.scene_subtype == "oral":
        if bangok_four_xipsum2_store.protection == True:
            m "I looked at the disks in my hands, one sprouting a pair of condom-wrapped shafts, the other displaying Ipsum's lube-sheened underbelly plates."
        else:
            m "I looked at the disks in my hands, one sprouting a pair of shafts, the other displaying Ipsum's lube-sheened underbelly plates."

    m "Deciding to get into him first, I brought Ipsum's asshole to the tip of my manhood, slipping between his plates and beginning to apply pressure to his rear sphincter."

    if bangok_four_xipsum2_store.separate == False:
        Ip sad flip "Nngh."
    m "Despite his generous lubing, it was still difficult to wedge my tip inside of him. I turned the disk, twisting my entry until his lube-slicked flesh gave."
    m "Having fit my head into his hole, I pulled the disk down, hilting myself to take full advantage of my new toy."
    Ip sad flip "Urgh!"
    if bangok_four_xipsum2_store.separate == True:
        m "Ipsum's yelp of alarm carried from the other room."

    m "I let the disk go, leaving myself hilted inside his tight, undulating insides to let him adjust."

    if bangok_four_xipsum2_store.scene_subtype == "oral":
        m "Taking pity on him, I decided to pick up the disk from which his cocks emerged and start that blowjob I had promised."
        m "It was like suckling on a pair of fleshy, pre-leaking dildos, as I took his tips into my mouth."

        if bangok_four_xipsum2_store.separate == False:
            Ip normal bangok blush flip "Mmh. Better."
            m "Spurred on by his encouragement, I pushed his penises slightly deeper into my mouth, swirling the heads around with my tongue."
        else:
            m "The taste, texture, and slight twitching helped keep me from forgetting these were real, as he leaked small dollops of pre into my mouth."
    elif bangok_four_xipsum2_store.scene_subtype == "anal1":
        if bangok_four_xipsum2_store.separate == False:
            Ip normal bangok blush flip "My turn, then."
            m "He lifted the disk in his hand to the tip of one of his shafts, then pressed his tip through."
        m "I felt a slippery, fleshy contact with the lube in my crack, Ipsum's tip quickly finding my rosebud."
        if bangok_four_xipsum2_store.separate == False:
            m "Giving me a devious look, he pulled the disk all the way to his base, not even taking a moment to push his tip through first, by itself."
        m "I yelped, hips bucking up from the couch as Ipsum's length rammed all the way inside, without even the mercy of working his tip through first."
        play sound "fx/bangok_poundofsalt.ogg" fadein 1.5
        m "He picked up a pace quickly, taking full advantage of my pliable human rear for his own gratification."
        c "N-{w=0.65}N-{w=0.65}Ngh."
        if bangok_four_xipsum2_store.separate == False:
            Ip "We did start this conversation on the premise of using each other as sex toys."
            Ip happy bangok blush flip "Enjoy yourself."
    else: # anal2
        if bangok_four_xipsum2_store.separate == False:
            Ip normal bangok blush flip "My turn, then."
            m "Squeezing his shafts together, he lifted the disk in his hand to the paired tips, then pressed through."
        m "I felt a slippery, fleshy contact with the lube in my crack, Ipsum's tips quickly finding my rosebud."
        if bangok_four_xipsum2_store.separate == False:
            m "He pressed, both hands on the disk as he shoved into my ass."
        m "I grunted, squirming on the couch as he began to shove inside, his twin bulges stretching my ass in a strange, elongated manner."
        c "I-Ipsum! You're gonna s-split me open!"
        if bangok_four_xipsum2_store.separate == False:
            Ip "Just returning the favor from your entry."
            Ip "We did start this conversation on the premise of using each other as sex toys."
            Ip happy bangok blush flip "Enjoy yourself."
            m "Thankfully, his relentless entry came to an end, as I felt one of his belly plates against my ass, through the disk."
        else:
            m "Away in the other room, he couldn't hear my complaint. Thankfully, his relentless entry came to an end, as I felt one of his belly plates against my ass, through the disk."
        m "Adjusting his grip, he began to pull himself back out, before switching directions and thrusting again over the lowest quarter of his shaft."

    m "Not wanting to be left out, I reached for my crotch, pulling on the disk to Ipsum's ass, drawing myself back out for another thrust."
    if bangok_four_xipsum2_store.separate == False:
        Ip normal bangok blush flip "A-Ah. Th-There we are."
    m "Ipsum's hole tugged on my length, in a way that I almost felt sad running out of length to pull out. Then I switched directions, pushing back inside, filling his rear once more."
    if bangok_four_xipsum2_store.scene_subtype == "oral":
        m "All throughout, I kept a hand on the disk sticking his cocks in my mouth, licking and suckling as I tried to bring him to his climax, so I could focus fully on reaming his ass."
    elif bangok_four_xipsum2_store.scene_subtype == "anal1":
        m "All throughout, Ipsum kept up his punishing pace on my ass, taking the pleasure he wanted and leaving my cheeks numb where they contacted the couch."
    else: # anal2
        m "All throughout, Ipsum kept up his slow sliding into and out of my rear, taking the pleasure he wanted with his twin lengths and leaving my cheeks numb where they contacted the couch."

    if persistent.bangok_watersports == True and bangok_four_xipsum2_store.ws == True and bangok_four_xipsum2_store.protection == False:
        stop soundloop fadeout 1.0
        if bangok_four_xipsum2_store.scene_subtype == "oral":
            m "Just as I was about to begin increasing my pace, Ipsum's shafts twitched, releasing a different, tangy flavor."
        else:
            m "Just as I was about to begin increasing my pace, Ipsum's thrusts slowed, then stopped, hilted inside me."
        if bangok_four_xipsum2_store.separate == False:
            Ip happy bangok blush flip "You know, I think I might just take advantage of that offer to relieve myself."

        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"

        if bangok_four_xipsum2_store.scene_subtype == "oral":
            m "I barely had time to move both hands to the twin dildos in my mouth, before jets of sour piss were flooding over my tongue and up against the back of my throat."
            m "I struggled to swallow it all down. Drops escaped my mouth between his shafts, getting on my hands and dribbling down my chin to my chest."
        elif bangok_four_xipsum2_store.scene_subtype == "anal1":
            if bangok_four_xipsum2_store.separate == False:
                m "Taking tight hold of his free shaft, Ipsum pinched the tip, preventing more than a few droplets of golden liquid from escaping there."
                m "I felt the rest, hot and wet, pouring into my ass, saturating my inner walls and flowing around his invading length."
            else:
                m "His shaft twitched, then a hot, wet stream of watery liquid began to spurt inside me, saturating my inner walls."
                m "I flushed with heat, realizing Ipsum was taking me up on that offer of using my ass as his own, portable urinal."
        else: # anal2
            m "His twin shafts twitched, then hot, wet streams of watery liquid began to spray inside me, saturating my inner walls."
            if bangok_four_xipsum2_store.separate == True:
                m "I flushed with heat, realizing Ipsum was taking me up on that offer of using my ass as his own, portable urinal."

        if bangok_four_xipsum2_store.separate == False:
            Ip normal bangok blush flip "Mmmh."

        stop soundloop fadeout 2.0

        if bangok_four_xipsum2_store.scene_subtype == "oral":
            m "His stream petered out, finally leaving me a chance to suck down a breath around his musky, warm waste product."
        elif bangok_four_xipsum2_store.scene_subtype == "anal1":
            m "His stream petered out, leaving my rectum feeling a little heavier than before, our mating point a little more nasty and wet, flowing as his cock moved around in the piss pool."
        else: # anal2
            m "As his stream petered out, I felt some of his piss squeezing back out, slipping through the small gap between my stretched spincter and his twin cocks."
            if persistent.bangok_cloacas == True:
                m "It dribbled down inside his cloaca, slickening further the point where I'd buried my cock in his ass."

        menu:
            "Return the favor.":
                $ bangok_four_xipsum2_store.player_pissed = True
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                m "Pulling his ass to my hilt, I let my own bladder go, urinating directly into Ipsum's guts."
                if bangok_four_xipsum2_store.separate == False:
                    Ip happy bangok blush flip "I suppose turnabout is fair play."
                else:
                    $ renpy.pause (0.8)

                m "I toyed with the disk, pulling Ipsum's ass off a little and giving short thrusts, to thoroughly splash my liquid gift as far inside him as I could."


                if bangok_four_xipsum2_store.separate == False:
                    Ip normal bangok blush flip "Mm. That'll take a while to clean out."
                else:
                    $ renpy.pause (0.8)

                stop soundloop fadeout 2.0

                m "I ran out of piss to give, but not before my cock and his rectum were thoroughly soaked."

                if bangok_four_xipsum2_store.separate == False:
                    Ip normal bangok blush flip "Let's pick back up."


                if bangok_four_xipsum2_store.scene_subtype == "oral":
                    m "I moaned, appreciatively, around the cocks in my mouth, then began to pull his ass back off my length, to resume a proper fucking."


            "Save it.":
                if bangok_four_xipsum2_store.scene_subtype == "oral":
                    m "Holding my bladder, I resumed my thrusts into Ipsum's tight rear."
                else:
                    m "Holding my bladder, I resumed my thrusts into Ipsum's tight rear and suckling on his now-piss-stained shafts."


        if bangok_four_xipsum2_store.scene_subtype == "anal1":
            play soundloop "fx/bangok_poundofsalt.ogg" fadein 0.5
            m "Abruptly, Ipsum pulled all the way out of my ass before ramming his other lubricated and slightly cooler length into place."
            m "I clenched, gasping, as he began fucking me with his un-piss-stained shaft, fouling that one with my dirty rear."
        elif bangok_four_xipsum2_store.scene_subtype == "anal2":
            m "Ipsum's twin lengths pulled back, allowing more dribbles of piss to escape, before he shoved again hard and deep, spattering his urine up and down my crack and his genital slit."

    if bangok_four_xipsum2_store.scene_subtype == "anal1":
        m "I grunted, gripping the disk to Ipsum's ass tighter as I began to fuck it faster, matching Ipsum's pace."
    else:
        play soundloop "fx/bangok_poundofsalt.ogg" fadein 1.0
        m "I grunted, gripping the disk to Ipsum's ass tighter as I began to fuck it faster."

    Ip happy bangok blush flip "Nngh!"

    if bangok_four_xipsum2_store.separate == True:
        m "Ipsum's grunt carried through the door, encouraging me to fuck him even harder."
    else:
        Ip normal bangok blush flip "I'm... happy to see you enjoy using me to such a degree."
        if bangok_four_xipsum2_store.scene_subtype == "oral":
            m "I moaned appreciatively around his lengths in my mouth."
        else:
            c "N-Not sure I'll want to give this hole back when I'm done with it."
            Ip happy bangok blush flip "M-Maybe you won't have to."
        Ip happy bangok blush flip "I'm not sure I want to give up this human-brand hole either..."

    if bangok_four_xipsum2_store.scene_subtype == "anal1" and bangok_four_xipsum2_store.separate == False and bangok_four_xipsum2_store.protection == False:
        m "I glanced over at Ipsum's free shaft, bobbing and twitching in the air while he stretched my ass over its twin."
        if persistent.bangok_watersports == True and bangok_four_xipsum2_store.ws == True:
            m "A sheen of piss and pre covered most of it, with a little more pre squeezing out with every one of his other shaft's thrusts into my ass."
        else:
            m "A sheen of slit juices and pre covered most of it, with a little more pre squeezing out with every one of his other shaft's thrusts into my ass."

        menu:
            "Suck it.":
                $ bangok_four_xipsum2_store.suck_spare = True
                show ipsum happy bangok heady with dissolve
                show black with dissolve
                m "Leaning over, I took Ipsum's spare length into my mouth, lapping up his fluids as I tried to drive him over his peak."
            "Ask him to stick it in, too.":
                Ip ipsum happy bangok heady "W-Well, if you insist."
                m "He pulled out, leaving my ass momentarily cold and empty."
                m "Then I felt both his heads prodding at my spread rosebud."
                c "Mngh!"
                m "It felt like his paired shafts were going to pry my ass apart, but they fit."
                m "With my ass already pre-stretched by his one, he quickly got back to his punishing pace, as I kept mine going, stretching his tight rear."
            "Let him handle it.":
                pass

    if bangok_four_xipsum2_store.separate == False:
        Ip happy bangok heady "Mmh. Be ready. I think... I may..."

    play sound "fx/snarl.ogg" fadein 0.5

    if bangok_four_xipsum2_store.separate == True:
        m "The sound he made as he orgasmed carried through the door."

    stop soundloop fadeout 0.5

    if bangok_four_xipsum2_store.protection == True:
        if bangok_four_xipsum2_store.scene_subtype == "oral":
            m "I gagged, thick blasts of cum abruptly bloating Ipsum's condom tips in my mouth."
            m "I hilted myself in Ipsum, then pulled his twin lengths from my mouth, watching with fascination as his twitching shafts filled their respective condom reservoirs, and then some."
        elif bangok_four_xipsum2_store.scene_subtype == "anal1":
            m "He stopped, hilted inside me, then his shaft twitched and pulsed, warm seed filling his condom reservoir as he came."
            if bangok_four_xipsum2_store.separate == False:
                m "I hilted myself in Ipsum, then looked over, watching with fascination as his spare shaft filled its condom reservoir too."
        else:
            m "Hilted inside, his shafts twitched and pulsed, filling twin warm balloons of sticky white within me."
    else:
        if bangok_four_xipsum2_store.suck_spare == True or bangok_four_xipsum2_store.scene_subtype == "oral":
            m "I gagged, thick blasts of cum coating my mouth and throat as I struggled to swallow."
            m "I hilted myself in Ipsum, focusing on getting down his cum before I could choke and leave a mess in his living room."

        if bangok_four_xipsum2_store.scene_subtype == "anal1":
            m "His shaft in my ass twitched and pulsed, painting my inner walls with warm ropes of sticky white."
            if bangok_four_xipsum2_store.suck_spare == False and bangok_four_xipsum2_store.separate == False:
                m "He gripped his other shaft tightly, trying to hold back his peak from that  outlet. Even still, a few jets pushed past his grip, spurting across the living room table."
        elif bangok_four_xipsum2_store.scene_subtype == "anal2":
            m "Hilted inside me, his shafts twitched and pulsed, painting my inner walls with warm ropes of sticky white."

    m "His inner muscles worked around my shaft, tight ass clamping even tighter in undulating waves as his body pushed his seed out his shafts."
    m "A few moments of that was all my endurance could take."
    play sound "fx/extinguish.ogg"
    show black with dissolve
    $ renpy.pause (0.3)
    if bangok_four_xipsum2_store.protection == True:
        m "I came, twitching and spurting, into the condom reservoir I'd buried deep in Ipsum's ass."
    elif persistent.bangok_watersports == True and bangok_four_xipsum2_store.player_pissed == True:
        m "I came, twitching and spurting, spraying my cum over the layer of piss I'd left deep in Ipsum's rear."
    else:
        m "I came, twitching and spurting, my sticky seed filling what little space remained in Ipsum's rear until it was sticking to my own tip."

    $ renpy.pause (1.0)
    if bangok_four_xipsum2_store.separate == False:
        show ipsum happy bangok blush flip
        hide black
        with dissolveslow
    else:
        show ipsum happy bangok blush briefs touch glow at right
        hide black
        with dissolveslow

    if bangok_four_xipsum2_store.suck_spare == True:
        m "I came back down from my high with Ipsum grinning down at me, in his lap."
        Ip "Nice touch at the end, there."
        m "Blushing, I let his cock back out of my mouth."
    elif bangok_four_xipsum2_store.separate == False:
        m "I came back down from my high with Ipsum grinning over at me, fingering the disk in his lap."
        Ip "And a happy ending for us both."
    else:
        if bangok_four_xipsum2_store.scene_subtype == "anal1":
            m "I came back down from my high with Ipsum grinning over at from the door, fingering the disk over one of his cocks."
        else:
            m "I came back down from my high with Ipsum grinning over at from the door, fingering the disk over his cocks."
        Ip "And a happy ending for us both."

    if persistent.bangok_watersports == True and bangok_four_xipsum2_store.ws == True and bangok_four_xipsum2_store.player_pissed == False:
        menu:
            "Relieve yourself.":
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                $ renpy.pause (0.3)
                if bangok_four_xipsum2_store.separate == True:
                    show ipsum normal bangok blush briefs touch glow at Position(ypos=1.05) with ease
                else:
                    show ipsum normal bangok blush flip with None
                m "Catching Ipsum off-guard, he pressed his thighs together, as I began to jet a stream of hot piss into his ass."
                Ip "Didn't see that one coming. Nnmh. Well done."
                c "Turnabout is fair play. You didn't give me a lot of warning."
                stop soundloop fadeout 1.0
                Ip "No, I suppose I didn't."

            "Let it be.":
                pass

    $ renpy.pause (0.5)
    if bangok_four_xipsum2_store.scene_subtype == "oral":
        c "So what now? Want me to pull out?"
        if bangok_four_xipsum2_store.separate == True:
            show ipsum normal bangok blush briefs with dissolve
            show ipsum normal bangok blush briefs at center with ease
            m "Walking a little unsteadily, Ipsum wandered a few steps to face me on the couch."
        else:
            hide ipsum with dissolve
            $ renpy.pause (0.3)
            show ipsum normal bangok blush briefs at center with dissolve
            m "Rising unsteadily, Ipsum wandered a few steps to face me on the couch."
        Ip "Not yet. I'm enjoying the feeling."
        c "Okay, but I'm going to get soft kinda fast."
    else:
        c "So what now? Want to pull out?"
        if bangok_four_xipsum2_store.separate == True:
            show ipsum normal bangok blush briefs with dissolve
            show ipsum normal bangok blush briefs at center with ease
            m "Walking a little unsteadily, Ipsum wandered a few steps to face me on the couch."
        else:
            hide ipsum with dissolve
            $ renpy.pause (0.3)
            show ipsum normal bangok blush briefs at center with dissolve
            m "Rising unsteadily, Ipsum wandered a few steps to face me."

        if persistent.bangok_knot == True:
            Ip "Can't, I'm afraid. Not for a while, at least."
            show ipsum normal bangok blush briefs touch glow with dissolve
            m "He tugged at the disk stuck to his crotch, and I felt large knots of flesh tugging in kind at my asshole."
            menu:
                "H-Hey!":
                    c "I didn't say you could do that!"
                    Ip normal bangok briefs "I apologize. I assumed that because it wouldn't affect your ability to leave today, it wouldn't have as great a concern for you."
                    m "He spread his arms, indicating the lack of connection between us."
                    c "... Huh."
                "Oh.":
                    pass
        else:
            Ip "Not yet. I'm enjoying the feeling."





label bangok_four_xipsum2_sharingchat:
    Ip normal bangok briefs "Now, important question: what would you like to have happen with this?"
    c "What do you mean?"
    Ip think bangok briefs "Well, you don't have to be anywhere near me for these to work. They appear to work independent of distance."
    Ip happy bangok briefs "That means you, could, say, take them home, and we could fuck more, all without you having to expend the effort to even go anywhere."
    Ip normal bangok briefs "At least until a few days after the fireworks, when I'm planning a distraction to slip these back where they came from."
    c "I see."

    menu:
        "Okay, I think I'll take these ends with me.":
            $ renpy.pause(0.5)
            $ bangok_four_xipsum2_store.shared_with = "ipsum"
            $ bangok_four_xipsum2_store.sharing = 1
            c "Getting to play with this more sounds fun."
            Ip happy bangok briefs "Excellent."
            $ renpy.pause(0.3)
            Ip think bangok briefs "And, say, what is your opinion on having anyone else have access to it? Like, Lorem?"
            c "I..."
            menu:
                "No. Please don't go lending out my genitals to your roommate.":
                    $ renpy.pause(0.5)
                    Ip happy bangok briefs "Spoilsport."
                    Ip normal bangok briefs "I jest. Of course I'll keep this just between us."
                    c "Thanks."
                    Ip normal bangok briefs "Oh no, thank you. After all, this is going to be quite a bit of fun for both of us."
                "I... suppose.":
                    $ renpy.pause(0.5)
                    $ bangok_four_xipsum2_store.sharing = 2
                    Ip happy bangok briefs "Mmhm. And, say, other members of my lab?"
                    menu:
                        "What? No!":
                            $ renpy.pause(0.5)
                            Ip sad bangok briefs "I kid, I kid."
                            Ip happy bangok briefs "Lorem and I are okay, though, yes?"
                            c "I mean, yeah, I guess I said you could. Fine."
                            Ip normal bangok briefs "Excellent."
                        "Is that something you can do?":
                            $ renpy.pause(0.5)
                            c "Aren't these supposed to be a secret? And didn't you steal this tech?"
                            Ip think bangok briefs "Well, \"borrowed,\" yes. But few even know the project exists. And I'd only share this with members of my lab who can keep a secret."
                            menu:
                                "No, thanks.":
                                    c "I'm not comfortable with people I don't even know fucking me."
                                    Ip happy bangok briefs "Lorem and I are okay, though, yes?"
                                    c "I mean, yeah, I guess I said you could. Fine."
                                    Ip normal bangok briefs "Excellent."
                                "Alright. Sounds fun, then.":
                                    $ renpy.pause(0.5)
                                    $ bangok_four_xipsum2_store.sharing = 3
                                    Ip happy bangok briefs "Excellent."
                                    if persistent.bangok_watersports == True:
                                        Ip think bangok briefs "What about using you for a... possibly unsanitary prank?"
                                        c "Uh... what kind of prank?"
                                        Ip normal bangok blush briefs "To tell you would spoil the surprise, wouldn't it?"
                                        if persistent.bangok_watersports == True and bangok_four_xipsum2_store.ws == True:
                                            Ip think bangok briefs "I suppose the clarifying question is, would you have a problem with complete strangers urinating in you?"
                                        else:
                                            Ip think bangok briefs "I suppose the clarifying question is, would you have a problem with complete strangers ejaculating in you unprotected?"
                                        menu:
                                            "Obviously, I'd have a problem with that!":
                                                $ renpy.pause(0.5)
                                                Ip sad bangok briefs "Nevermind, then. No harm, no foul."
                                                c "Seriously, Ipsum. Don't."
                                                Ip think bangok briefs "I won't. It was just an idea. I wasn't sure how far afield your tastes ran."
                                            "Now I'm too curious.":
                                                $ renpy.pause(0.5)
                                                $ bangok_four_xipsum2_store.sharing_unsanitary = True
                                                c "Who is this prank on?"
                                                Ip happy bangok blush briefs "You'll find out in a few days. Is that you agreeing to it?"
                                                c "I... guess it is."
            jump bangok_four_xipsum2_ipsum_sharing1
        "I... think I'm done with this tech.":
            $ renpy.pause(0.8)
            Ip sad bangok briefs "Ah."
            c "Don't get me wrong, it was interesting and all, and this was fun, but I'm not sure I want to keep playing with it."
            c "Using real people's genitals as sex toys isn't really appealing to me."
            Ip normal bangok briefs "Understandable. Whatever makes you comfortable."
            c "Thanks for this, though."
            Ip happy bangok briefs "Of course. Do take care."
            Ip normal bangok briefs "And be sure to check any pants you find yourself putting on in the future. Who knows what people might hide in them."
            c "Ha. Right."

    $ renpy.pause(0.5)
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    jump _mod_fixjmp


label todo_out_of_content_bangok_four_xipsum:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("Out of content.")