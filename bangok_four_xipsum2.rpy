init python in bangok_four_xipsum2_store:
    protection = False

    scene = None
    # Scenes:
    #    truedp - Ipsum takes f character's ass and pussy at the same time.
    #    assdp  - Ipsum fits both cocks in the player character's ass.
    #    ass    - Ipsum fits one cock in the player's ass and hotdogs with the other.
    #    df     - Ipsum and the player fuck each other simultaneously.

    has_both = False
    shared_with = None
    # This "sharing" enum covers extra use scenes.
    #  0 - Not shared.
    #  1 - The player only shared it with the target.
    #  2 - The player shared it with the target and a small group.
    #  3 - Free use for the target's friends.
    sharing = 0

    sharing_ws = False


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
            Ip happy bangok briefs "Where were we?"
        "Unprotected sounds fun.":
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

    menu:
        "Can you take both my ass and pussy comfortably with this?" if bangok_four_playerhasdick == False:
            $ renpy.pause (0.5)
            $ bangok_four_xipsum2_store.scene = "truedp"
            Ip normal bangok briefs "That was actually somewhat my hope in making them."
            jump bangok_four_xipsum2_truedp
        "I'd prefer you stick with just my ass, if that's okay." if bangok_four_playerhasdick == False:
            $ renpy.pause (0.5)
            Ip sad bangok briefs "I had hoped to try out whether this would help me deal with the gap between your reproductive passage and anus. Two cocks, two holes."
            Ip normal bangok briefs "But if anal play is what you would prefer."
            jump bangok_four_xipsum2_ass_split
        "Can we fuck each other at the same time with this?" if bangok_four_playerhasdick == True:
            $ renpy.pause (0.5)
            $ bangok_four_xipsum2_store.scene = "df"
            Ip normal bangok briefs "It's entirely possible!"
            Ip think bangok briefs "At least, I believe so. I did try to design in the possibility."
            jump bangok_four_xipsum2_df
        "You've got two cocks and I have one ass." if bangok_four_playerhasdick == True:
            $ renpy.pause (0.5)
            Ip normal bangok briefs "That is the case, yes."
            jump bangok_four_xipsum2_ass_split

label bangok_four_xipsum2_truedp:
    play sound "fx/leather.ogg"
    $ renpy.pause (0.1)
    stop sound fadeout 0.5
    m "I pulled up my briefs the rest of the way, nestling the disks against my front and rear entrances."
    m "With the disks active, I could feel his hard plates within their metal circumference, a tiny bit of his warmth radiating through into my crotch, even as he still stood a few feet away."
    $ renpy.pause (0.3)
    show ipsum happy bangok briefs touch glow with dissolve
    $ renpy.pause (0.3)
    m "Then he reached inside his briefs again, and I felt the air of the room against my lower holes. Scaly knuckles brushed over my pussy, then my ass, transferring a small amount of my lubrication."
    if bangok_four_xipsum2_store.protection == True:
        m "His condom-enwrapped tips nestled against my holes, sending electric sparks up into my center and down toward my weak knees."
    else:
        m "His tips nestled against my holes, sending electric sparks up into my center and down toward my weak knees."
    Ip "Ready?"
    m "I pressed the briefs more tightly against my holes, hoping to tease out just a taste of his lengths early."

    play sound "fx/slap1.wav"
    $ renpy.pause(0.0)
    show ipsum happy bangok blush briefs with None
    m "He let the waistband of his briefs snap back against his hips, forcing his cocks into me with startling speed."
    m "We both gasped. Even though I was prepared this time, my knees still wobbled, nearly sending me to the floor from the sensations."
    $ renpy.pause(0.8)
    Ip "That may be too fast for me. How do you feel?"
    c "I... I think I need..."
    m "I took a few steps toward the couch. As I did, my inner walls shifted around his shafts, sending yet another wave of pleasure through me."
    Ip normal bangok aheago briefs "Nnnngh."
    Ip normal bangok blush briefs "Y-Yes. I think I should join you sitting down."
    jump bangok_four_xipsum2_sit


label bangok_four_xipsum2_ass_split:
    Ip "Are you comfortable trying to fit both? Or just one?"
    menu:
        "One.":
            $ renpy.pause (0.5)
            $ bangok_four_xipsum2_store.scene = "ass"
        "Both.":
            $ renpy.pause (0.5)
            $ bangok_four_xipsum2_store.scene = "assdp"
    Ip think bangok briefs "Either way, we will need more lubrication than we have."
    Ip normal bangok briefs flip "One moment."
    $ renpy.pause(0.3)
    hide ipsum with easeoutright
    $ renpy.pause (0.3)
    play sound "fx/door/close2.wav"
    $ renpy.pause (1.0)

    m "After a couple seconds, I decided standing around in Ipsum's living room with my pants only half-pulled-down looked a little silly."
    if bangok_four_playerhasdick == True:
        m "I pulled the briefs up the rest of the way, tucking my cock over the waistband to keep it out of the way. With the disks inside now active, I felt the slightly cooler air of Ipsum's room blowing softly over my asshole."
    else:
        m "I pulled the briefs up the rest of the way. With the disks inside now active, I felt the slightly cooler air of Ipsum's room blowing softly over my holes."

    if bangok_four_xipsum2_store.protection == True:
        m "Then I felt a little more air, followed by the cold, lubed tips of Ipsum's pair of condom-wrapped cocks."
    else:
        m "Then I felt a little more air, followed by the lukewarm, lubed tips of Ipsum's pair of cocks."

    c "H-Hey--"

    if bangok_four_xipsum2_store.scene == "assdp":
        m "They squeezed together, both prodding at my rear entrance, seeking access."
        m "Slowly, with the help of his generous lubing, Ipsum's cocks began to squeeze inside my ass, stretching it."
        m "My legs wobbled, utterly perplexed by the elongation of my asshole with, from the perspective of the rest of my body, no discernible source."
        Ip normal bangok blush "Hahh... How does that feel?"
    else: # ass
        m "The cocks shifted, one prodding at my rear entrance, the other sliding up my crack, past my waistband."
        m "His tip began to enter my ass. Then..."
        play sound "fx/slap1.wav"
        m "An elastic snap came from the other room, followed by both cocks shoving hard."
        m "My legs wobbled, the penetration of my ass heady and wholly unexpected."
        Ip normal bangok blush "Hahh... How did that feel?"

    play sound "fx/door/close2.wav"
    $ renpy.pause (1.0)
    show ipsum normal bangok blush briefs with easeinright
    $ renpy.pause (0.3)
    m "He emerged from his room, one hand hanging around the edge of his briefs' waistband."
    if bangok_four_xipsum2_store.scene == "assdp":
        c "F-Feels amazing."
    else:
        c "A little too rough."
        Ip "Too fast for me, too."
    c "I..."
    m "My ass clenched around his cocks, and I stumbled toward the couch a few steps. It was bizarre, being free to move, but feeling the walls of my ass shifting around him as a result of my motion."
    Ip normal bangok aheago briefs "Nnnngh."
    Ip normal bangok blush briefs "Y-Yes. I think sitting down is a good idea."
    jump bangok_four_xipsum2_sit


label bangok_four_xipsum2_df:
    if bangok_four_xipsum2_store.protection == True:
        Ip normal bangok briefs "We will need some lubrication, however, and to apply your protection."
    else:
        Ip normal bangok briefs "We will need some lubrication, however."
    Ip happy bangok briefs touch glow "Finish putting your device on? And feed your penis through. I'd like to lubricate both of us at once."
    c "Oh?"
    m "Looking down, I finished pulling up the briefs, feeding my hardening cock through one of the disks into his waiting fingers."
    c "Ah! Th-That tickles!"
    $ renpy.pause (0.3)
    show ipsum happy bangok briefs touch glow flip with None
    m "Ipsum turned around, my cock still in his hand, then made for the door to his room."
    hide ipsum with easeoutright
    $ renpy.pause (0.3)
    play sound "fx/door/close2.wav"
    $ renpy.pause (1.0)
    if bangok_four_xipsum2_store.protection == True:
        m "If I thought just being held in his hand tickled, having him roll a condom down over my length was something else entirely."
        m "My knees wobbled, made weak by the sensations coming through my crotch as his fingers prodded around my base, making sure the condom was completely unrolled to my side."
    else:
        c "(He's not going to cut it off and keep it, right?)"
    $ renpy.pause (0.8)

    m "Then I felt a sliding motion along either side of my shaft's head, followed a wet feeling as something dribbled over it."
    m "I gasped, clutching my crotch as I realized he was lubing all three of our cocks together: mine and both of his."
    if persistent.bangok_cloacas == True:
        m "He pumped over our triplet of cocks a couple of times, then poked me further down, nestling my tip just between his bases."
    else:
        m "He pumped over our triplet of cocks a couple of times, then poked me further down, sliding my tip over one of his hard plates before nestling it into another horizontal opening."
    m "I couldn't help but let out an audible noise as his warm heat enveloped me."
    m "He responded through his door."
    Ip happy bangok blush "Feel that, do you?"
    Ip normal bangok blush briefs touch glow "How about this..."
    m "I felt his ass shift around me as he rearranged something down south."
    m "Then I felt his cockheads prodding up between my asscheeks."
    c "O-Oh!"
    m "One tip nestled against my rosebud, gently applying pressure on a layer of thick lube. The other rubbed further up, separating from the first as it aimed out my crack."

    play sound "fx/slap1.wav"
    
    m "An elastic snap came from the other room, followed by both cocks shoving hard."
    m "My legs wobbled, the penetration of my ass heady and fast, but a little painfully so."
    Ip normal bangok blush "Hahh... How did that feel?"

    m "I felt more movement as he began to walk, his leg and tail muscles tugging on his torso as he walked upright, all causing his warm inner walls to squeeze lewdly about my length."

    play sound "fx/door/close2.wav"
    $ renpy.pause (1.0)
    show ipsum normal bangok blush briefs at right with easeinright
    $ renpy.pause (0.3)
    m "He emerged from his room a little unsteadily, one hand hanging around the edge of his briefs' waistband."
    c "A little too rough."
    Ip "Too fast for me, too."
    c "I..."
    m "My ass clenched around his cocks, and my legs tensed from more sparks of pleasure from my length buried in him."
    m "I stumbled toward the couch a few steps. It was bizarre, being free to move, but feeling the walls of my ass shifting around him as a result of my motion."
    Ip normal bangok aheago briefs "Nnnngh."
    Ip normal bangok blush briefs "Y-Yes. I think sitting down is a good idea."
    jump bangok_four_xipsum2_sit



label bangok_four_xipsum2_sit:
    hide ipsum with dissolvemed
    $ renpy.pause(0.3)
    show loremapt at Pan((128,62),(0,0), 2.0) with ease
    $ renpy.pause(2.3)
    show ipsum happy bangok blush flip:
        xanchor 0.0
        yanchor 1.0
        xpos 0.0
        ypos 1.25
        rotate -5
    with dissolve
    if bangok_four_xipsum2_store.scene in ["assdp","truedp"]:
        m "We both reclined back on the couch. His cocks shifted inside me, held in place like dildos by the tight briefs around my waist."
    elif bangok_four_xipsum2_store.scene == "ass":
        m "We both reclined back on the couch. His cock shifted inside me, held in place like a dildo by the tight briefs around my waist, while his other rubbed lewdly against the small of my back, smearing lube."
    else: # df
        m "We both reclined back on the couch. His cock shifted inside me, held in place like a dildo by the tight briefs around my waist, while his other rubbed lewdly against the small of my back, smearing lube."
        m "I felt mine similarly rubbed inside his lithe frame as he settled, searching for a way to arrange his tail to sit comfortably on the couch, while also taking me in his ass."
    if bangok_four_xipsum2_store.scene == "truedp":
        m "The inner walls of my passage kneaded and massaged his length, milking him for stimulation now that he was fully inside."
    show ipsum normal bangok blush briefs touch glow flip with dissolve
    m "Ipsum slid his hand back inside his briefs, lifting his side of the disks away from his slit."
    m "In turn, his cocks slid out of me, leaving me aching for his next thrust."
    play soundloop "fx/bangok_poundofsalt.ogg"
    m "He began to fuck me for real, casually lifting and lowering the front of his briefs."
    if bangok_four_xipsum2_store.scene == "truedp":
        m "I squirmed, the lack of heat, weight, or hips between my legs confusing my senses as my pussy and ass were pressed open, again and again, in perfect time with one another."
    elif bangok_four_xipsum2_store.scene == "assdp":
        m "I squirmed, the lack of heat, weight, or hips between my legs confusing my senses as my ass was stretched open, again and again, by his thick pair of members."
    elif bangok_four_xipsum2_store.scene == "ass":
        m "I squirmed, the lack of heat, weight, or hips between my legs confusing my senses as my ass was pressed open, again and again, in perfect time with the one emerging from my waistband to slide up my back."
    else: # df
        m "I squirmed, assailed by sensations. There was no sense of heat, weight, or feeling of hips pressing between my legs, which confused my senses as my ass was pressed open again and again, in perfect time with the one emerging from my waistband to slide up my back."
        m "At the same time, his motion tugged my cock out of, then let it slide back into his ass, producing the sensation almost that I was fucking myself at his command."
    $ renpy.pause (0.5)
    show ipsum happy bangok blush briefs touch glow flip with dissolve
    if bangok_four_xipsum2_store.scene == "df":
        m "I tugged on my own waistband, pulling out of him a little farther, before sliding back in, eliciting a gasp from the smaller dragon."
        show ipsum normal bangok heady briefs touch flip with dissolve
    else:
        if bangok_four_playerhasdick == True:
            m "He reached over, then began to gently stroke my cock just down to my waistband -- while still fucking me."
        else:
            m "He reached over, slipping a hand beneath my waistband, then began to gently circle my labia with one clawtip -- while still fucking me."
    $ renpy.pause (1.0)
    
    Ip happy bangok blush briefs touch glow flip "How do you feel about exhibitionism?"
    c "W-What?"
    Ip normal bangok blush briefs touch glow flip "Would you, say, want to get caught like this?"
    menu:
        "Yes.":
            c "W-why are you--?"
            m "He interrupted me by thrusting harder for a moment."
            Ip happy bangok blush briefs touch glow flip "No reason."
            
            $ renpy.pause(1.0)

            stop music fadeout 0.5
            stop soundloop fadeout 0.5
            play sound "fx/door/door_open.wav"
            show ipsum normal bangok briefs flip with dissolve
            if bangok_four_xipsum2_store.scene in ["truedp","assdp"]:
                if bangok_four_playerhasdick == True:
                    m "Ipsum slipped my cock under my waistband and yanked his hand away from his own as we heard the sound of the door opening. My breath caught, his two shafts stopping, hilted inside of me."
                else:
                    m "Ipsum yanked his hand away from my crotch and his own as we heard the sound of the door opening. My breath caught, his two shafts stopping, hilted inside of me."
            elif bangok_four_xipsum2_store.scene == "ass":
                if bangok_four_playerhasdick == True:
                    m "Ipsum slipped my cock under my waistband and yanked his hand away from his own as we heard the sound of the door opening. My breath caught, his two shafts stopping, one hilted inside of me and the other in the small of my back."
                else:
                    m "Ipsum yanked his hand away from my crotch and his own as we heard the sound of the door opening. My breath caught, his two shafts stopping, one hilted inside of me and the other in the small of my back."
            else: # df:
                play sound2 "fx/slap1.wav"
                m "As we heard the sound of the door opening, Ipsum let his waistband fall shut with a snap, hilting himself inside me and rubbing his other shaft right up into the small of my back."
                m "My breath caught, and he slapped my hand away from my own waistband, struggling to school his expression as I also slid fully into him."

            Lo normal b "Hey Ipsum! I'm home!"
            show lorem think b:
                xanchor 0.7
                xpos 1.0
                yanchor 1.0
                ypos 1.15
            with easeinright
            Lo "Oh, [player_name]? You're here."
            Lo shy b "A-And your clothes are..."
            Lo relieved b "Ipsum, putting [player_name] in one of your swimming briefs doesn't hide that you were doing... things in the living room."
            Ip happy bangok briefs flip "I don't know what you're talking about."
            if bangok_four_xipsum2_store.scene == "df":
                m "I clenched my fists, left maddenningly close to my edge, but unable to risk any motion right in front of Lorem."
            else:
                m "I clenched my fists, left maddenningly close to my edge by him, being still inside me."
            Lo "I'll be in the kitchen, putting away some things, starting dinner, and not listening."
            $ renpy.pause (0.3)
            show lorem relieved b flip with None
            $ renpy.pause (0.3)
            hide lorem with easeoutright

            play music "mx/snowflake.ogg" fadein 3.0
            $ renpy.pause (1.5)
            
            Ip normal bangok blush briefs touch glow flip "What say we take this to my bedroom, now?"
            m "My breathing hitched as he gave a short thrust, daring me to make a noise."
            c "P-Probably best."

        "No.":
            stop soundloop fadeout 2.0
            if bangok_four_xipsum2_store.scene == "df":
                m "Ipsum withdrew his hand from my crotch, then gently let his waistband down, leaving us hilted inside one another."
            else:
                m "Ipsum withdrew his hand from my crotch, then gently let his waistband down, leaving himself hilted inside me."
            Ip "Then we should probably take this elsewhere. Namely, my bedroom."
            if bangok_four_xipsum2_store.scene in ["ass","df"]:
                m "I panted for breath, my body unwilling to come down from its current high with his shaft caressing my inner walls."
            else:
                m "I panted for breath, my body unwilling to come down from its current high with two shafts caressing my inner walls."
            c "S-Sure."

    $ renpy.pause(0.5)
    scene bangok_four_xipsum_bedroom ceiling:
        alignaround (0,0)
        # pos (0, -456)
        pos (-128,0)
    with wipeleft

    $ renpy.pause(0.3)
    m "Ipsum gathered my clothes and brought them with us as I took unsteady steps toward his room to eventually collapse on his bed."
    play sound "fx/door/close2.wav"
    m "He closed the door behind us."
    show ipsum normal bangok blush flip:
        zoom 1.8
        alignaround (0.5,0)
        xpos 0.18
        ypos 0.6
    with easeinbottom

    if bangok_four_xipsum2_store.scene == "df":
        m "He sat on the bed next to me, reaching into his waistband again."
    else:
        m "He sat on the bed next to me, reaching into his waistband again, and into mine."
    play soundloop "fx/bangok_poundofsalt.ogg"
    c "H-Hah."
    if bangok_four_xipsum2_store.scene == "df":
        m "I didn't even have the focus of mind to reach for my own cock, as his clenching and panting on top of his fucking of my ass was enough to keep me heady and blissed out."
    elif bangok_four_xipsum2_store.scene == "assdp":
        if bangok_four_playerhasdick == True:
            m "His shafts slid easily through my weakened sphincter muscle now, while his rough, scaly hand pumped my shaft."
        else:
            m "His shafts slid easily through my weakened sphincter muscle now, while his lone exploring finger focused on finding and sparking every nerve in my empty, aching passage's entrance."
    elif bangok_four_xipsum2_store.scene == "truedp":
        m "His shafts slid easily through my holes now, while his lone exploring finger focused on finding and sparking every nerve in my passage's entrance."
    else: # ass
        if bangok_four_playerhasdick == True:
            m "His lone shaft slid easily through my weakened sphincter muscle now, while the other rubbed up and down my crack and his scaly hand pumped my shaft."
        else:
            m "His lone shaft slid easily through my weakened sphincter muscle now, while the other rubbed up and down my crack and his lone exploring finger focused on finding and sparking every nerve in my empty, aching passage's entrance."
        
    Ip happy bangok heady flip "I'd call this experiment a complete success, wouldn't you?"
    if bangok_four_playerhasdick == True:
        m "His stroking and fucking had me oh-so-close to my peak, now, as the sensations kept piling on."
    else:
        m "He circled just shy of my clit, causing my inner walls to clench and spasm around him."
    c "Y-Yes!"
    Ip normal bangok heady flip "G-Good."
    Ip normal bangok aheago briefs flip "B-Becase I think we're about to--"
    show ipsum happy bangok aheago briefs flip:
        ypos 0.7
    with ease
    stop soundloop fadeout 0.5
    play sound "fx/slap1.wav"
    play sound2 "fx/snarl.ogg" fadein 0.5
    m "He let his waistband snap home with a slap, hilting inside of me, before doubling over and cumming."
    if bangok_four_xipsum2_store.scene == "truedp":
        if bangok_four_xipsum2_store.protection == True:
            m "I felt his shafts twitch, delivering his white seed to his condoms' reservoirs deep inside my canal and my ass."
        else:
            m "I felt his shafts twitch, then ropes of warm, white seed sprayed out deep within my canal and ass."
    elif bangok_four_xipsum2_store.scene == "assdp":
        if bangok_four_xipsum2_store.protection == True:
            m "I felt his shafts twitch, delivering his white seed to his condoms' reservoirs deep in my rear."
        else:
            m "I felt his shafts twitch, then ropes of warm, white seed sprayed out deep in my ass."
    elif bangok_four_xipsum2_store.scene == "ass" or bangok_four_xipsum2_store.scene == "df":
        if bangok_four_xipsum2_store.protection == True:
            m "I felt his shafts twitch, one deep in my ass, the other right up behind my cheeks. Then pulses of warm seed began to fill his condoms reservoirs'."
        else:
            m "I felt his shafts twitch, one deep in my ass, the other right up behind my cheeks. Then ropes of warm seed sprayed out, soaking into my ass and the bedcovers beneath my back."
    else:
        $ print(bangok_four_xipsum2_store.scene)
        $ renpy.error("Impossible xipsum climax: "+bangok_four_xipsum2_store.scene)


    if bangok_four_xipsum2_store.scene == "df":
        m "I was so close to release my body acted of its own accord. I caught his legs with mine, pulling his crotch against my nethers, even though we could get no closer than we already were, buried to the hilt inside one another."
        m "As he stumbled, his weight shifted and muscles tugged, shifting his inner walls about my length and giving me the last bit of stimulation I needed."
    else:
        m "I was so close to release my body acted of its own accord. I caught his legs with mine, pulling his crotch against my nethers, even though we could get no closer than his shafts already were."
        if bangok_four_playerhasdick == True:
            if bangok_four_xipsum2_store.protection == True:
                m "His scaly palm was forced up over my condom-wrapped head, stroking down behind my tip and down the bottom of my length, giving me the last bit of stimulation I needed."
            else:
                m "His scaly palm was forced up over my head, spreading my own leaking pre down my length as he managed a few more uneven pumps, giving me the last bit of stimulation I needed."
        else:
            m "His scaly, caressing finger rubbed across my clit, tugging at my stretched lips, and providing the last bit of stimulation I needed."
    show black with dissolve
    $ renpy.pause(0.3)
    if bangok_four_playerhasdick == True:
        play sound "fx/extinguish.ogg"
    c "Ah!"
    $ renpy.pause(0.5)
    hide black
    show ipsum happy bangok blush flip:
        ypos 0.6
    with dissolveslow

    $ renpy.pause(0.8)
    Ip "And there we are."

    if persistent.bangok_inflation == True:
        if bangok_four_xipsum2_store.scene == "truedp":
            if bangok_four_xipsum2_store.protection == True:
                m "I placed a hand on my belly, feeling warm and full from the balloons of cum now inflated in my ass and canal."
            else:
                m "I placed a hand on my belly, feeling warm and full from the load of cum now packing my canal and colon."
        elif bangok_four_xipsum2_store.scene == "assdp":
            if bangok_four_xipsum2_store.protection == True:
                m "I placed a hand on my belly, feeling warm and full from the balloons of cum now inflated in my colon, making me look heavy as if with a good meal."
            else:
                m "I placed a hand on my belly, feeling warm and full from the load of cum now packing my colon, thick and heavy like a good meal."
        elif bangok_four_xipsum2_store.scene in ["ass", "df"]:
            if bangok_four_xipsum2_store.protection == True:
                m "I placed a hand on my belly, feeling a mild sense of warmth and fullness from the lone balloon of cum inflated in my colon. The other rested in the small of my back, awkward and heavy."
            else:
                m "I placed a hand on my belly, feeling a mild sense of warmth and fullness from the helping of cum delivered via my ass. More squelched beneath me, rubbed into my back by my breaths as we came down together."
            

    m "I let my legs fall away from behind him, and he flicked at one of my feet with his tail."

    label bangok_four_xipsum2_skip:
    if not _in_replay:
        $ persistent.bangok_four_xipsum2_skip = True
    if persistent.bangok_knot == True:
        Ip normal bangok blush flip "Now, it'll be a little while before I can pull out--"
        c "Huh?"
        if bangok_four_xipsum2_store.scene in ["truedp","assdp"]:
            m "He tugged at his waistband, pulling on his cocks, and indicating the thick knots of flesh at the base of each of his shafts that tied him inside me."
        else: # "ass", "df"
            m "He tugged at his waistband, pulling on his cock in my ass, revealing the thick knot of flesh at the base that tied him inside me."
        menu:
            "H-Hey!":
                c "I didn't say you could do that!"
                Ip look bangok flip "I apologize. I assumed that because it wouldn't affect your ability to leave today, it wouldn't have as great a concern for you."
                c "What do you--"
                show ipsum:
                    ypos 0.7
                with ease
                if bangok_four_xipsum2_store.scene in ["truedp","assdp"]:
                    m "He stepped back, arms spread to show there was technically no direct connection between us, despite his twin cocks resting inside me."
                elif bangok_four_xipsum2_store.scene == "ass":
                    m "He stepped back, arms spread to show there was technically no direct connection between us, despite his cock in my ass, and his other sticking up my back like a tiny, lewd tail."
                else: # "df"
                    m "He stepped back, arms spread to show there was technically no direct connection between us, despite his cock in my ass, and mine in his."
                c "... Huh."
                show ipsum:
                    ypos 0.6
                with ease
            "Oh.":
                pass
    else:
        Ip normal bangok blush flip "Now, there's no reason for me to pull out immediately."
    Ip normal flip "I wanted to talk briefly about what you'd like to have happen with this."
    c "What do you mean?"
    Ip think flip "Well, the normal rules don't really apply, here. You don't need to be anywhere near the other end to make use of this -- at least so far as I have tested."
    Ip happy flip "That means you could, say, take what you're wearing home, and leave this end with me. We could call, or schedule times to use it."
    Ip normal flip "At least until a few days after the fireworks, when I have a distraction planned to slip these back where they came from."
    c "I see."
    menu:
        "Sure, you could keep that end.":
            $ renpy.pause(0.5)
            $ bangok_four_xipsum2_store.shared_with = "ipsum"
            $ bangok_four_xipsum2_store.sharing = 1
            Ip happy flip "Thank you."
            $ renpy.pause(0.3)
            Ip think flip "And, say, what is your opinion on having anyone else have access to it? Like, Lorem?"
            c "I..."
            menu:
                "No. Please don't go lending out my genitals to your roommate.":
                    $ renpy.pause(0.5)
                    Ip happy flip "Spoilsport."
                    Ip normal flip "I jest. Of course I'll keep this just between us."
                    c "Thanks."
                    Ip normal flip "Oh no, thank you. After all, this is going to be quite a bit of fun for both of us."
                "I... suppose.":
                    $ renpy.pause(0.5)
                    $ bangok_four_xipsum2_store.sharing = 2
                    Ip happy flip "Mmhm. And, say, other members of my lab?"
                    menu:
                        "What? No!":
                            $ renpy.pause(0.5)
                            Ip sad flip "I kid, I kid."
                            if bangok_four_xipsum2_store.protection == True:
                                Ip happy flip "Lorem and I are okay, though, yes? With protection?"
                            else:
                                Ip happy flip "Lorem and I are okay, though, yes?"
                            c "I mean, yeah, I guess I said you could. Fine."
                            Ip normal flip "Excellent."
                        "Is that something you can do?":
                            $ renpy.pause(0.5)
                            c "Aren't these supposed to be a secret? And didn't you steal parts to make it?"
                            Ip think flip "Well, yes. But few even know the project exists. And I'd only share this with members of my lab who can keep a secret."
                            menu:
                                "No, thanks.":
                                    c "I'm not comfortable with people I don't even know fucking me."
                                    if bangok_four_xipsum2_store.protection == True:
                                        Ip happy flip "Lorem and I are okay, though, yes? With protection?"
                                    else:
                                        Ip happy flip "Lorem and I are okay, though, yes?"
                                    c "I mean, yeah, I guess I said you could. Fine."
                                    Ip normal flip "Excellent."
                                "Alright. Sounds fun, then.":
                                    $ renpy.pause(0.5)
                                    $ bangok_four_xipsum2_store.sharing = 3
                                    Ip happy flip "Excellent."
                                    if persistent.bangok_watersports == True:
                                        Ip think flip "What about using you for a... possibly unsanitary prank?"
                                        c "Uh... what kind of prank?"
                                        Ip normal bangok blush flip "To tell you would spoil the surprise, wouldn't it?"
                                        Ip think flip "I suppose the clarifying question is, would you have a problem with complete strangers urinating in you?"
                                        menu:
                                            "Obviously, I'd have a problem with that!":
                                                $ renpy.pause(0.5)
                                                Ip sad flip "Nevermind, then. No harm, no foul."
                                                c "Seriously, Ipsum. Don't."
                                                Ip think flip "I won't. It was just an idea. I wasn't sure how far afield your tastes ran."
                                            "Now I'm too curious.":
                                                $ renpy.pause(0.5)
                                                $ bangok_four_xipsum2_store.sharingws = True
                                                c "Who is this prank on?"
                                                Ip happy bangok blush flip "You'll find out in a few days. Is that you agreeing to it?"
                                                c "I... guess it is."
            jump bangok_four_xipsum2_ipsum_sharing1
        "I'd honestly like to have both ends.":
            $ renpy.pause(0.5)
            $ bangok_four_xipsum2_store.has_both = True
            Ip think flip "Oh? What for?"
            c "Well, there's someone else I might like to use it with. If, you know, I could..."
            Ip "Few people even know the project exists, so I suppose as long as you're not showing it to anyone directly involved..."
            Ip normal flip "I assume you hadn't heard of it."
            c "Nope."
            Ip "Then you're probably fine to show it to this friend of yours. If you mention it's a secret, and don't mention where it came from, of course."
            c "Of course."
            Ip happy flip "I would like to have details, though, on how you end up using it."
            Ip normal flip "Once I can get some of these by, {i}ahem{/i}, more strictly intended methods, I certainly plan to toy with them frequently."
            Ip happy flip "Hearing others' use cases, you see..."
            m "He trailed off, guaging my reaction."
            c "... Maybe."
        "I... think I'm done, once I take this off.":
            $ renpy.pause(0.8)
            Ip sad flip "Ah."
            Ip normal flip "Well, you had fun with this experiment at least. That was my goal."
            Ip think flip "I'll talk to Lorem about including you in dinner, if you'd like."
            c "Sure. That sounds good."
            Ip happy flip "Excellent."
            Ip normal flip "And, perhaps, another round after dinner?"
            c "Oh, no. I think I'm good."
            Ip "Suit yourself."

    $ renpy.pause(0.5)
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    jump _mod_fixjmp

label bangok_four_xipsum2_ipsum_sharing1:
    $ renpy.pause(0.5)
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause(1.0)

    play sound "fx/phonering.ogg"
    scene o3 at Pan((0, 100), (0, 250), 3.0) with dissolveslow
    $ renpy.pause(1.3)
    play sound "fx/phonepickup.ogg"

    Ip normal bangok blush "Hello, [player_name]."
    c "Ipsum?"
    c "It's the middle of the night. What...?"
    if bangok_four_playerhasdick == True:
        m "I felt the rustling of fabric over my shaft and realized Ipsum must be looking at his end of his stimulating device."
    else:
        m "I felt the rustling of fabric over my outermost folds and realized Ipsum must be looking at his end of his stimulating device."

    if bangok_four_xipsum2_store.sharing > 1:
        Ip normal bangok blush "Well, Lorem wasn't interested. But asking him gave me a thought."
    Ip happy bangok blush "Since you're still wearing it, perhaps you'd like an... overnight visitation."

    menu:
        "Just how horny are you?":
            Ip think "This much, evidently."
            if bangok_four_playerhasdick == True:
                m "A clawed finger ghosted over my outer lips, leaving me shivering."
            Ip normal bangok blush "What do you say?"
            menu:
                "Accept.":
                    jump bangok_four_xipsum2_evening_accept
                "Reject.":
                    jump bangok_four_xipsum2_evening_reject
        "Accept.":
            label bangok_four_xipsum2_evening_accept:
            Ip happy bangok blush "Happy to oblige."
            m "(Click.)"
            c "(He hung up?)"
            m "Air wafted over my nethers as he moved his end of the devices."
            if bangok_four_playerhasdick == True:
                if bangok_four_xipsum2_store.protection == True:
                    m "Then a cold condom was unrolled down my shaft."
                else:
                    m "Then cold lubricant dribbled over my shaft."
                c "Ah!"
                m "Before I had a handle on the sensations in my groin, my shaft was enveloped by Ipsum's warm rear, sinking slowly inside."
            if bangok_four_playerhasdick == True or bangok_four_xipsum2_store.scene != "truedp":
                m "Then I felt his twin shafts at my rear."
                if bangok_four_xipsum2_store.scene != "assdp":
                    c "(W-Wait, I don't think I can--!)"
                m "He didn't thrust, instead applying pressure gently, waiting for my pucker to give."
                if bangok_four_playerhasdick == True:
                    m "I tensed, then found myself relaxing into the slow shifting of his body around my length, due to his breathing."
                else:
                    m "I tensed, then shivered as he reached a finger through to tickle my outermost folds."
                c "Ohhhh..."
                m "Ipsum sank inside me, spreading my hole evenly and slowly."
            else:
                m "Then his twin heads prodded once again at my two folds."
                c "Ohhhh..."
                if bangok_four_xipsum2_store.protection == True:
                    m "I arched my back as he filled me, gently, applying pressure slowly to slip inside on condom lubrication alone, rather than thrusting."
                else:
                    m "I arched my back as he filled me, gently, applying pressure slowly to slip inside on lubrication alone, rather than thrusting."
            m "Then his slit pressed against my rear, leaving me hilted in my empty bed."
            m "There he stopped. I felt tremors and tugging as he moved about in his home, but he wasn't fucking me, just visiting."
            m "Shifting around to try to find a comfortable position, I eventually drifted off with my legs spread, his shafts buried inside me."
            $ renpy.pause(0.3)
            scene black with dissolveslow
            $ renpy.pause(1.0)

            if bangok_four_xipsum2_store.protection == True:
                if bangok_four_playerhasdick == True:
                    m "When morning came, the only sign of his former presence was the condom I'd filled in him in my sleep."
                elif bangok_four_xipsum2_store.scene == "truedp":
                    m "When morning came, the only sign of his former presence was a warm feeling of contentment radiating from my pussy and ass."
                else:
                    m "When morning came, the only sign of his former presence was a warm feeling of contentment radiating from my ass."
            elif persistent.bangok_inflation == True:
                if bangok_four_playerhasdick == True:
                    m "When morning came, the only signs of his former presence were the mess of cum on my own cock, and the large, sticky load in my backdoor."
                elif bangok_four_xipsum2_store.scene == "truedp":
                    m "When morning came, the only sign of his former presence was the heavy sticky load weighing in my guts and canal."
                else:
                    m "When morning came, the only sign of his former presence was the heavy sticky load weighing in my rear."
            else:
                if bangok_four_playerhasdick == True:
                    m "When morning came, the only signs of his former presence were the mess of cum on my own cock, and the dregs of a load in my backdoor."
                elif bangok_four_xipsum2_store.scene == "truedp":
                    m "When morning came, the only signs of his former presence were the sticky loads in my ass and pussy."
                else:
                    m "When morning came, the only signs of his former presence were the dregs of a load in my backdoor."
        "Reject.":
            label bangok_four_xipsum2_evening_reject:
            c "It's just comfortable evening-wear. Don't read too much into it."
            Ip sad "Oh."
            Ip think "Alright then. Do let me know when you are, {i}ahem{/i}, available."
            c "Yeah. Sure."
            Ip sad "Goodnight."

    $ renpy.pause(0.5)
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    jump _mod_fixjmp

init python in bangok_four_xipsum2_sharing3_store:
    cervpen = False

label bangok_four_xipsum2_ipsum_sharing3:
    m "I began to go about my morning routine, preparing for the day of the fireworks."

    if persistent.bangok_watersports == True and bangok_four_xipsum2_store.sharing_ws == True:
        if bangok_four_playerhasdick == True:
            jump bangok_four_xipsum2_ipsum_sharing3_ws_male
        else:
            jump bangok_four_xipsum2_ipsum_sharing3_ws_female

    play sound "fx/phonering.ogg"
    scene o4 at Pan((0, 100), (0, 250), 0.0) with dissolveslow
    $ renpy.pause(1.3)
    play sound "fx/phonepickup.ogg"

    Ip happy bangok blush "[player_name]!"
    Ip normal "You remember how you agreed you might be interested in some other members of my lab having access to the, ah, thing?"
    m "My hand went to my crotch, where I was still wearing Ipsum's comfortable, modified swim briefs."
    c "Yes...?"
    Ip happy bangok blush "Are you available?"
    c "{i}Now?{/i}"
    Ip sad "Well, I just got into the lab, and I have a few eyes on me right now trying to tell if I'm being serious, so now would be preferable to later."
    c "(Well, later I'm going out to watch the fireworks, so if I want to be cleaned up, I'd better do this now.)"
    menu:
        "Accept.":
            $ renpy.pause(0.5)
        "Reject.":
            c "I'm sorry. I can't today."
            $ renpy.pause(0.5)
            Ip sad "Oh."
            $ renpy.pause(0.5)
            Ip think "Well, how does tomorrow look, then?"
            c "Maybe. I don't know."
            $ renpy.pause(0.5)
            Ip sad "I see. Well, talk soon, then."
            $ renpy.pause(0.5)
            m "(Click.)"
            $ renpy.pause(0.5)
            jump bangok_four_xipsum2_ipsum_sharing3_return

    Ip happy bangok blush "Thank you."
    if bangok_four_xipsum2_store.protection == True:
        m "His voice became more muffled, as he began speaking to someone else. I definitely heard something about condoms, though, which was a relief."
    else:
        m "His voice became more muffled, as he began speaking to someone else."
    # play sound "fx/undress.ogg"
    # m "Realizing I was probably about to be fucked three ways from Sunday, I hurriedly stripped out of my regular clothes, leaving just Ipsum's briefs."
    if bangok_four_playerhasdick == False:
        m "I felt the cold air of someplace else on my pussy and asshole, abruptly leaving me feeling completely nude, despite the tight briefs around my hips."
        m "I set the phone down, trying to keep my balance as I was startled by the sensation."
        m "Then spurts of lube fell across my front and rear entrances, followed by a rough, scaly hand rubbing it in, slipping inside my folds to spread it."
    else:
        m "I felt the cold air of someplace elese on my cock and asshole, abruptly leaving me feeling completely nude, despite the tight birefs around my hips."
        m "I set the phone down, trying to keep my balance as I was startled by the sensation."
        if bangok_four_xipsum2_store.protection == True:
            m "Then I felt a condom somewhat roughly unrolled down my cock, followed by spurts of lube across my ass and cock and a rough scaly hand pumping me and rubbing it in."
        else:
            m "Then spurts of lube fell across my ass and cock, followed by a rough scaly hand pumping me and rubbing it in."

    scene o4:
        ypos -456
    with ease

    m "My knees wobbled as I clutched my crotch, overcome by sensations before the fucking had even begun."

    if bangok_four_playerhasdick == False:
        if bangok_four_xipsum2_store.protection == True:
            m "Then the first condom-wrapped cock nestled into my folds and thrust, faster than I could deal with."
        else:
            m "Then the first cock nestled into my folds and thrust, faster than I could deal with."
        play soundloop "fx/bangok_poundofsalt.ogg"
        m "Another joined it at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."
    else:
        m "Then I felt scaly folds wrapping around my tip, before my shaft was shoved somewhere hard enough it hurt at the base of my length."
        if bangok_four_xipsum2_store.protection == True:
            m "A condom-wrapped cock prodded at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."
        else:
            m "A cock prodded at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."

    play sound "fx/tableslap.wav"
    with vpunch
    m "I fell against the table with the telephone, struggling to pick it back up."
    c "S-Slower, Ipsum!"
    Ip normal bangok blush "Tone it down, a little. They're, ah, breakable."
    if bangok_four_playerhasdick == False and persistent.bangok_cervpen == True:
        Ip think "By the way, I have yet to ask, does your species have a cervix protecting your uterus? And if so, is it penetrable? How large a partner can you manage, and how deep might they go?"
        menu:
            "Y-Yes, we do! {i}Don't{/i}--":
                $ bangok_four_xipsum2_sharing3_store.cervpen = False
            "D-Deep--!":
                $ bangok_four_xipsum2_sharing3_store.cervpen = True

    m "Muffled voices responded to Ipsum, then the cock at my ass slipped through my fingers, and pressed inside me."
    play sound "fx/impact.wav"
    $ renpy.pause(0.3)
    with vpunch
    play soundloop "fx/bangok_poundofsalt.ogg"
    c "A-Ah!"
    if bangok_four_playerhasdick == False:
        m "My legs gave out, the fucking of both my holes by my remote suitors too much for me to bear."
    else:
        m "My legs gave out, the rough entrance of my ass too much to bear under the assailing of my shaft like a cheap dildo."

    m "I writhed on the floor, the phone out of reach on the table as my lower body was assaulted with pleasure."

    if bangok_four_playerhasdick == False:
        m "Thrust after thrust filled and emptied me, the two cocks sharing no cadence whatsoever as they each used me to climb toward their peaks."
        if bangok_four_xipsum2_store.protection == True:
            m "Then the one in my cooch began to twitch, and I felt warm, heavy ropes weighing down its condom reservoir."
            m "It pulled out, still cumming, but I got no respite as another, larger shaft took its place."
        else:
            m "Then the one in my cooch began to twitch, and I felt warm, heavy ropes of cum jet over my inner walls."
            if persistent.bangok_knot == True:
                m "A bulbous knot of flesh pressed at my outer folds, spreading my entrance just slightly further as the male injected his cum as deep as he could go."
            if persistent.bangok_inflation == True:
                m "When the cock pulled out, a thick pool of cum rested against my innermost gate. Then another, larger cock took its place."
            else:
                m "The cock pulled out, leaving my passage slightly damper and stickier. Then another, larger cock took its place."
    else:
        m "Juices flowed around my dick, dribbling down around my balls as the cunt on the far side squeezed and massaged me."
        m "I thrust, uselessly, from the simultaneous fucking of my ass and shaft. I couldn't force myself any further into what was already attached to my hips."

    if bangok_four_xipsum2_store.protection == True:
        m "Finally, the one in my ass stopped, pulses of his load travelling up his length to fill his condom's reservoir."
        m "I sighed as it slid out, taking its load with it, only to then feel a new head prodding at my weakened sphincter."
        c "Ah-h!"
        m "This one stretched me wider. As it sank in, I realized it was going deeper, too."
    else:
        m "Finally, the one in my ass stopped, packets of his load travelling up his length to spray out into my rear."
        if persistent.bangok_inflation == True:
            m "Pulse after pulse spurt into me, leaving my ass feeling heavy and full."
        m "I sighed as it slid out, feeling its load settle inside me, only to then feel a new head prodding at my weakened sphincter."
        c "Ah-h!"
        m "This one stretched me wider, scraping off my inner walls the seed of its predecessor. As it sank in, I realized it was going deeper, too."

    if bangok_four_playerhasdick == True:
        m "The cooch around my shaft shoved down, taking me completely and grabbing on, spasming and tugging, trying to milk me for every last drop."
        m "Somehow I held on, the rough treatment not quite enough to push me over that edge."
        m "After several seconds sitting on me, the wet passage disappeared, replaced by the cold of empty air."
        m "Then I felt a long, sinuous muscle wrap around my length, circling downward, until it was licking around my crotch, just lifting the tight fabric of the briefs."
        m "I groaned, so very close."
        stop soundloop fadeout 1.5
        m "Then the mouth disappeared, followed a few moments later by the guy in my ass pulling out."
        if bangok_four_xipsum2_store.protection == True:
            m "Someone stripped off my condom, the feeling almost putting me over that edge."
            m "They rolled a new one on, dribbled some lube."
        m "Then, abruptly, someone's loose ass wrapped around my length, as at the same time someone thrust into my rear."
        show black with dissolve
        play sound "fx/extinguish.ogg"
        m "I moaned, cumming hard, the cock in my ass twitching and spurting in perfect time."
        m "I realized, with a start, I'd just cum in myself!"
        hide black with dissolvemed
        if bangok_four_xipsum2_store.protection == True:
            m "Before I could think much about it, my shaft was tugged back out of me, my condom and load going with it."
        else:
            m "Before I could think much about it, my shaft was tugged back out of me, leaving a dribble of cum at my loosened sphincter."
        play sound "fx/bangok_poundofsalt.ogg"
        m "Then the large cock that had been plowing my rear returned, picking up right where it had left off."

        jump todo_out_of_content_bangok_four_xipsum_sharing3
    else:
        m "The two cocks rubbed together inside me, sandwiching my inner walls."
        m "I gave up holding back, moaning loudly as, with each of their uneven thrusts, they pressed pleasure from my passage, stretching me wide."
        if bangok_four_xipsum2_store.protection == True:
            m "Warmth blossomed in my passage as the one assailing my front entrance began to loose its load into its condom."
            m "It slid to a stop, serving for a long moment as an obstacle for the other to press against."
            m "Then it slid out, taking its load with it, leaving my cooch parted and cold."
        else:
            m "Warmth blossomed in my passage as the one assailing my front entrance loosed its load into me."
            m "Its seed layered over that of the first, slathering and soiling my passage."
            if persistent.bangok_inflation == True and persistent.bangok_cervpen == True:
                m "There was so much, my vagina alone couldn't handle it. As they sank in one last thrust, still releasing pulse after pulse, I gasped as it sprayed through my innermost gate, flowing into and staining my womb."
            m "Then, finished, it slid out, leaving my pussy parted and dripping."
        m "The next cockhead at my entrance, I could feel immediately, was barely going to fit if it could do so at all."
        c "W-W-Wait--"
        m "My hands snapped to my crotch but, without my spine to guide my hand, I couldn't get under the waistband in time."
        stop soundloop fadeout 2.5
        m "The tip spread me open, stretching out the folds in my entrance and leaving me taut and full."
        m "Even the fucking of my asshole came to a faltering stop, as if the person engaged in that activity was looking over to watch what this cock would do to me."
        m "I could see the slightest bulge running up my belly, as I was forced open by this large shaft, inch by maddening inch."
        m "Squirming in ecstacy, I pressed the briefs into my crotch, wondering how far this cock could go on."
        if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.cervpen == True:
            if bangok_four_xipsum2_store.protection == False:
                m "Like a plunger in a syringe, the cock scraped all the cum deposited before it off my walls, pressing it through my cervix in a lewd spray."
            m "I ran out of room, the thick cockhead butting up against my innermost gate. It hesitated, a moment, then seemed to obey my whispered prayer to keep going."
            m "Pain rapidly mixed with pleasure, the impossible penetration an unstoppable force against the weak defenses of my flesh."
            m "Bowing my cervix inward, the complete stranger's cock breached my womb."
            show white with dissolve
            $ renpy.pause(0.8)
            m "For several seconds I completely whited out, every nerve south of my navel awash with electric sparks from my complete and total filling."
            play soundloop "fx/bangok_poundofsalt.ogg" fadein 2.0
            hide white with dissolveslow
            m "I came back to the dull sensation of thrusting, my onahole of a canal an electric firestorm with every inch moved, while the motion in my rear was a more down-to-earth, filling feeling."
            $ renpy.pause(1.0)
        else:
            m "I ran out of room, the thick cockhead butting up against my innermost gate and eliciting a cry from my lips."
            m "It seemed to hear, as it backed off almost a full inch, before pulling out further and beginning to thrust."
            play soundloop "fx/bangok_poundofsalt.ogg" fadein 0.5

            m "I swooned under the two cocks' thrusts, until my speared canal finally spasmed and I passed over my peak."
            show white with dissolve
            $ renpy.pause(0.8)
            hide white with dissolveslow
            $ renpy.pause(1.0)

        m "The bulge in my belly moved, pistoning in and out with the thick shaft using my body for its pleasure."
        m "Then both shafts inside me began to pulse and twitch as they thrust, warmth spreading up their lengths to spurt out in thick ropes inside me."
        if bangok_four_xipsum2_store.protection == True:
            m "Their condom reservoirs bloated, the warmth contained, safe, and fulfilling. The shaft in my ass began to pull out, taking his with him while he was still cumming."
            if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.cervpen == True:
                m "Meanwhile, the length penetrating my deepest center continued to thrust, seemingly oblivious to its own climax nestling in my most sacred place."
                if persistent.bangok_inflation == True:
                    m "The condom expanded with the size of the load, the balloon of cum growing until my womb had no choice but to expand, too, leaving me pregnant with a thick blob of cum, periodically expanding and contracting with the thrusts spearing my body."
            else:
                m "The shaft in my stretched vagina continued to thrust, seemingly oblivious to its own climax nestling at the end of my canal."
        else:
            m "Their cum mixed with the loads that had come before, leaving me saturated with virile seed."
            if persistent.bangok_inflation == True:
                if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.cervpen == True:
                    m "My colon was packed full, my guts thick and heavy with dragon seed. My womb couldn't contain the directly-injected flow, the flood into my deepest recesses forcing to me expand until I appeared pregnant with a thick blob of cum."
                    m "The cock in my ass began to pull out, finished, but the girthy invader penetrating my womb continued to thrust, seemingly oblivious to its own climax bloating my most sacred place, periodically forcing me to expand, then contract with the flow of fluid."
                else:
                    m "My colon was packed full, my guts thick and heavy with dragon seed. With the girthy invader still pumping, the seed hadn't room to pool in my saturated canal. It sprayed through my innermost gate, flooding into my deepest recesses and forcing to me expand until I appeared pregnant with a thick blob of cum."
                    m "The cock in my ass began to pull out, finished, but, seemingly oblivious to its own climax, the girthy invader continued to thrust its cum through my cervix, bloating my most sacred place, periodically forcing me to expand, then contract with the flow of fluid."
        stop soundloop fadeout 0.5
        m "Then, finally, the massive cock in my pussy realized it was finished and dragged slowly from my nethers."
        if bangok_four_xipsum2_store.protection == True:
            if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.cervpen == True:
                if persistent.bangok_inflation == True:
                    m "I cried out as the massive blob of cum tried to follow, my hips not wide enough to let it go all at once, even had it wanted to."
                    m "In the end elasticity won out, and the fluid flowed through my breached inner gate to the lower part of the condom and, eventually, out of me to the far side."
                else:
                    m "I cried out as his condom's reservoir tried to follow. My breached inner gate was still slightly too small, and forcing it felt like the stranger's cock would tear out part of my guts."
                    m "Elasticity won out, the blob of cum dragging maddeningly through my parted depths."
        else:
            if persistent.bangok_inflation == True:
                m "I groaned as the pressure receded from my womb, cum flowing out of my weakened defenses, slowly reducing the baby bump in my belly to a mere bump, until my abused outer folds were allowed to hang empty again."

        m "I wasn't done, though."

        m "The moment my holes were free again, I felt a smaller cock nestling in my gaping asshole, followed by a second in my loosened canal."
        if bangok_four_xipsum2_store.protection == True:
            m "Unlike the others, these were just using, rather than abusing, my holes. I sighed with relief, rubbing my belly as I enjoyed this final, gentle double-fuck."
        else:
            if persistent.bangok_inflation == True:
                m "Unlike the others, these were just using, rather than abusing, my holes. They plugged in the heavy loads of seed left inside me, leaving me warm, contented, and full. I sighed with relief, rubbing my bulging belly as I enjoyed this final, gentle double-fuck."
            else:
                m "Unlike the others, these were just using, rather than abusing, my holes. They plugged in the heavy loads of seed left inside me, leaving me warm, contented, and full. I sighed with relief, rubbing my belly as I enjoyed this final, gentle double-fuck."

        m "Also unlike the others, after he came, spurting his paltry-by-comparison load of cum, he didn't pull out."
        if bangok_four_xipsum2_store.protection == False:
            if persistent.bangok_knot == True:
                m "His knots were just barely girthy enough to plug inside all the seed I'd collected, leaving me completed, rather than draining."
            else:
                m "His shafts were just barely girthy enough to plug inside all the seed I'd collected, leaving me completed, rather than draining."
        else:
            m "His condom reservoirs rested inside me, leaving my holes completed, rather than empty."

        m "I wanted to lie there and bask, but I could hear noise coming from the phone's reciever."
        if bangok_four_xipsum2_store.protection == False and persistent.bangok_inflation == True:
            m "Struggling to sitting upright, I felt the heavy loads of fluid inside me shift, then begin to drain despite the cocks still in me, puddling in the briefs beneath me, and passing through to the other side."
            m "I managed to reach onto the top of the table and pull down the phone reciever."
            Ip happy bangok blush "O-Oh! H-Hah, I thought... well, you must be pretty full over there."
            Ip normal bangok blush "Want me to see if a couple of the others will volunteer to be larger plugs?"
            c "I... I'm good, thanks."
        else:
            m "Struggling to sitting upright, I managed to reach onto the top of the table and pull down the phone reciever."
            Ip normal bangok blush "[player_name], whenever you'd like to respond, that'd be good."
            c "H-Here."
            Ip happy "Excellent!"



    Ip happy bangok blush "How did that feel?"
    c "I... I don't think I can walk for a bit."
    Ip normal bangok blush "In a good way, or...?"
    menu:
        "A good way, yeah.":
            $ renpy.pause(0.5)
        "Th-That was a lot. I'm going to need a while to recover.":
            $ renpy.pause(0.5)
    if bangok_four_xipsum2_store.protection == False and persistent.bangok_inflation == True:
        Ip normal bangok blush "Well, let me know when you make it to the bathtub to drain, and I'll pull out."
    else:
        Ip normal bangok blush "Well, let me know when you make it somewhere to drain, and I'll pull out."
    c "How magnanimous of you."
    if bangok_four_xipsum2_store.protection == False and persistent.bangok_inflation == True:
        c "(How am I going to even move? I'm so full...)"

    Ip sad "Oh, actually, I think I might have to go. Someone's here asking questions about the noise."
    c "W-Wait, Ipsum--!"
    m "(Click.)"

    m "I grunted, his cocks still inside me, as I wondered how I'd clean up to prepare for the day of the fireworks."
    $ renpy.pause(0.5)
    scene black with dissolve
    $ renpy.pause(1.0)
    scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
    jump bangok_four_xipsum2_ipsum_sharing3_return
