init python:
    bangok_four_xsebastian_unplayed = True
    bangok_four_xsebastian_depth = 0
    bangok_four_xsebastian_playerfirst = False
    bangok_four_xsebastian_badtouch = False

label bangok_four_xsebastian_replay_start:
    play music "mx/feelings.ogg" fadein 2.0
label bangok_four_xsebastian_todaywasgreat:
    $ mp.sebastianromance = True
    $ mp.save()
    scene bangok_four_xsebastian_cave2_dk
    show sebastian normal b dk:
        xanchor 0.5
        yanchor 1.0
        zoom 1.7
        xpos 0.8
        ypos 1.4
        # rotate 35
    with dissolveslow
    c "Really, thank you Seb. Being able to get out of the apartment, get away from this morning... it means a lot."
    $ renpy.pause (2.0)
    Sb "I agree. This has been a pretty nerve-wracking assignment. That we could step away and talk about it was good."
    Sb "Given the sensitive nature of what happened, you and my colleagues are the only people I can talk to."
    Sb drop b dk "And I can't talk to them about being nervous."
    $ renpy.pause (1.5)
    Sb normal b dk "Thank you for listening."
    $ renpy.pause (0.5)
    c "It's no problem, really. You're the sweetest dragon I've met here so far. You're not only protecting me all day, but even offering your own body to keep me warm."
    $ renpy.pause (0.7)
    Sb shy b dk "Heh. I suppose I am."
    $ renpy.pause (0.8)
    m "I felt the warmth of seb's neck and head increase."
    c "(Is he blushing? Huh.)"
    c "That's, ah, not how I meant it."
    Sb shy b dk "Right. Of course not."
    menu:
        "But if you feel that way...":
            $ renpy.pause (0.5)
            jump bangok_four_xsebastian_path1
        "Good night, my adorable blanket.":
            $ renpy.pause (0.5)
            jump bangok_four_xsebastian_path2
        "We should probably actually get to sleep.":
            $ renpy.pause (0.5)
            Sb normal b dk "Sure. Good night."
            scene black with dissolvemed
            jump bangok_four_xsebastian_todaywasgreat_return

label bangok_four_xsebastian_path1:
    c "I would gladly accept if that's how you feel. I should give my thanks for being so nice to me."
    Sb smile b dk "Heh... [player_name], it's my job."
    $ renpy.pause(0.8)
    Sb shy b dk "A-Are you being serious?"
    $ renpy.pause(1.2)
    Sb "D-Do you really want to...?"
    c "What can I say? You're an attractive dragon."
    $ renpy.pause(0.6)
    if bangok_four_bangnokay or persistent.bangok_four_bangnokay:
        jump bangok_four_xsebastian_badnight
    m "He fell silent for a long moment. Then I felt something prod my butt through my pants."
    Sb "I..."
    show sebastian at Position(xpos=0.7) with ease
    m "I rolled over, feeling about for the intruding bump. When I got a hand on it, I found the moist shaft of meat to be attached to Seb."
    c "Do you want this?"
    $ renpy.pause(1.2)
    Sb "Yes, i-if you--"
    show sebastian at Position(ypos=1.3) with ease
    show sebastian at Position(ypos=1.2) with ease
    show sebastian at Position(ypos=1.1) with ease
    show sebastian at Position(ypos=1.0) with ease
    m "I worked my way lower down our rock bed, giving myself easier access to his cock."
    m "Gently, I began to explore it, getting an idea of what I'd be working with."
    m "It was smooth, slightly tapered with a wider base than head, and a tip that bulged just slightly from the shaft, enough to give it a noticeable ridge, but not enough for said ridge to impede anything."
    m "Sebastian thrust back slightly against my explorations."
    menu:
        "I'll just use my hands, okay?":
            $ bangok_four_xsebastian_depth = 0
        "May I taste you?":
            $ bangok_four_xsebastian_depth = 1
        "F-Fuck I want you in my throat.":
            $ bangok_four_xsebastian_depth = 2
    Sb drop b dk "U-Up to you."
    show sebastian shy b dk with dissolve
    if bangok_four_xsebastian_depth == 0:
        m "I tightened my grip, beginning to pump a little more vigorously."
        m "My fingers slid easily along his length, their passage smoothed by a natural lubricant already coating it from his slit."
        m "I played with the slight ridge on his head each time I reached it, which drew small hitches in Sebastian's breathing."
    elif bangok_four_xsebastian_depth >= 1:
        show black with dissolve
        m "I leaned forward, taking Sebastian's tip just slightly into my mouth, twirling my tongue about it as I learned his taste."
        menu:
            m "He tasted like..."
            "Dragon.":
                m "There really wasn't a better word I could use for it."
            "Slit juices.":
                m "The lubricant already on his shaft was slightly salty. As I licked around, though, I got a droplet of rich, sweet pre."
        if bangok_four_xsebastian_depth == 2:
            m "I bobbed my head down, testing his lubricant with the rest of my mouth, before descending far enough to feel his shaft against the back of my throat."
            m "Sucking down air, I went all the way, trying to push him into my throat."
            Sb drop b dk "Ah!"
            m "His shaft did not bend to make the passage into my throat."
            m "I came up coughing."
            hide black with dissolve
            Sb "You aren't realy going to be able to work my baculum that way."
            menu:
                "Your what?":
                    Sb "My penis bone."
                    c "You have a bone in your penis?"
                    jump bangok_four_xsebastian_path1_baculum
                "Oh, you have a baculum?":
                    label bangok_four_xsebastian_path1_baculum:
                    Sb normal b dk "Yes. I think all dragon species do."
                    c "I'll have to keep that in mind."
            m "I adjusted my position, moving my torso back to look up into his crotch, straightening the path from my mouth down my neck."
            m "Unfortunately, as I grabbed his shaft and it bobbed in front of my face, I quickly realized that left me with no control over his depth, nor effective way to guide him in."
        hide black with dissolve

    show sebastian drop b dk with dissolve
    m "Sebastian winced."
    Sb "[player_name], I..."
    m "I let him go, worried I was doing something wrong."
    $ renpy.pause (0.8)
    Sb smile b dk "I'd like to return the favor."
    Sb shy b dk "If th-that--"
    play sound "fx/zip.ogg"
    c "That sounds great."
    if bangok_four_xsebastian_depth == 2:
        Sb smile b dk "If you do still want to take me in your throat, you'll probably have to lie your head over the edge of the rocks, here."
    else:
        Sb smile b dk "We'll probably be more comfortable if I'm on top, since your body is flat and mine is..."
        c "Right."
    play sound "fx/undress.ogg"
    show black with dissolvemed
    m "We adjusted our position, and I pulled my pants down a bit to give Sebastian easier access to...{nw}"
    if bangok_four_playerhasdick is None:
        menu:
            m "We adjusted our position and I pulled my pants down a bit to give Sebastian easier access to...{fast}"
            "My already-hard shaft.":
                $ bangok_four_playerhasdick = True
            "My already-slick hole.":
                $ bangok_four_playerhasdick = False
    show black with dissolve
    if bangok_four_playerhasdick == True:
        m "We adjusted our position and I pulled my pants down a bit to give Sebastian easier access to{fast} my already-hard shaft."
        m "He wasted no time in repaying what I'd given him, bracing against my thighs and coiling his tongue around my cock."
    else:
        m "We adjusted our position and I pulled my pants down a bit to give Sebastian easier access to{fast} my already-slick hole."
        m "He took advantage immediately, scaly head diving between my thighs to kiss my hole, before digging his tongue inside."
    m "The long muscle of taste buds was unlike anything I'd experienced outside dragonkind."


    menu:
        "[[Enjoy it.]":
            $ renpy.pause(0.5)
            $ bangok_four_xsebastian_playerfirst = True
            m "For a long moment I lay back, basking in the incredible new sensations from my crotch."
            m "It was difficult to remember I had obligations too, with Sebastian bringing me rocketing toward my peak."
            m "His cock bounced off my face, reminding me of its presence."
        "[[Pay it forward.]":
            $ renpy.pause(0.5)
            $ bangok_four_xsebastian_playerfirst = False

    if bangok_four_xsebastian_depth == 0:
        m "I took Sebastian's cock in my hands, pumping him and squeezing that spot where his shaft turned into his tip."
        m "He moaned into my crotch, the combination of sensations evidently pushing him toward his peak as well."
    elif bangok_four_xsebastian_depth == 1:
        m "I guided his cock into my mouth, slurping at his tip for fresh droplets of pre."
        m "Then I swirled his tip around with my tongue, ghosting my teeth over the shaft."
        m "The easiest spot to grip his dick with my tongue was that small ridge where it turned into his tip, so I dug my tastebuds in there, digging out an extra dose of slit juices."
        m "He moaned into my crotch, the sensations evidently pushing him toward his peak as well."
    else: # == 2
        m "I guided his cock into my mouth. He barely gave me a moment to enjoy the taste before he pressed his hips forward, burrowing his tip in my neck."
        m "I bucked my crotch into his face, the sensation of my throat being entered racheting up the sensations in my groin."
        m "He moaned back, evidently quickly approaching his peak as well."
    
    if bangok_four_xsebastian_playerfirst == True:
        jump bangok_four_xsebastian_path1_1
    else:
        jump bangok_four_xsebastian_path1_2

label bangok_four_xsebastian_path1_1:
    m "His moan was the last of my endurance."
    if bangok_four_playerhasdick == True:
        play sound "fx/extinguish.ogg"
        m "I spurted into Sebastian's throat, falling limp as his tongue continued to slurp around my shaft, collecting every drop I put out."
    else:
        m "My passage clenched around Sebastian's tongue, then my thighs squeezed his head in too, leaving him nothing to do but to continue ravishing me with his tongue."
    if bangok_four_xsebastian_depth > 0:
        m "His cock came free of my mouth as I lost myself to the orgasm."
    $ renpy.pause(1.2)
    m "Once the crashing waves of pleasure faded, Seb pulled back, getting off of me for a moment."
    show sebastian smile b dk at Position(xpos=0.8, ypos=1.4)
    hide black
    with dissolvemed
    m "He licked his lips, the front of his muzzle glistening enough I could almost see it in the dark."
    Sb "Wow, you must really like dragons huh?"
    menu:
        "You have no idea...":
            pass
        "I really like {i}you{/i}.":
            pass
    $ renpy.pause (0.5)
    Sb shy b dk "I'm... flattered."
    $ renpy.pause (0.8)
    Sb smile b dk "You know, there's more to like yet."
    c "Oh?"
    hide sebastian with dissolve
    m "He tugged me up from the bed of rocks, guiding me to my hands and knees."
    m "Then I felt him pulling apart my cheeks."
    c "O-Oh!"
    m "Cupping my cheeks in his hands, his two cold thumbclaws prodded either side of my asshole."
    m "I expected him to enter with his well-lubricated shaft, but instead I felt his warm breath replacing the cold of the cave over my delicate rosebud."
    menu:
        "Yes.":
            $ renpy.pause (0.5)
            m "His scaly lips pressed to my hole, rubbing for a moment as he found his place, before his tongue slithered out to lick, then drive inside."
            m "I clenched around his tongue, the exploration unlike any I'd experienced before among humanity."
            m "When Seb withdrew, it was with a lick that swirled around much of my taint and crack."
            Sb shy b dk "That's a taste I can get behind..."
            Sb drop b dk "Pun not intended."
        "N-Not my ass!":
            $ renpy.pause (0.5)
            Sb drop b dk "Oh. If you say so."
            if bangok_four_playerhasdick == False:
                $ renpy.pause (0.6)
                m "He dropped his aim, spreading my thighs wider as he adjusted his position and grip."
                $ renpy.pause (0.6)
                m "His wet cock prodded my thighs as he got it nestled into the lips of my ready and soaked love canal."
                $ renpy.pause (0.6)
                Sb shy b dk "Better?"
                m "I pushed back against him, taking his tip inside."
                play soundloop "fx/rub2.ogg" fadein 2.0
                m "Taking that as permission, he slid the rest of the way in easily, picking up a smooth pace, in and out."
                $ renpy.pause (0.8)
                m "I leaned forward into the bed of rocks, taking the gentle fucking with soft gasps and moans."
                $ renpy.pause (1.5)
                stop soundloop fadeout 0.5
                m "He leaned over me, hugging my back as he stopped deep inside."
                play sound "fx/extinguish.ogg"
                m "Then warmth blossomed within me."
                m "His shaft pulsed, rope after rope of seed deposited in my hole."
                if persistent.bangok_inflation == True:
                    m "His cock kept twitching, the pressure of cum building up inside until it was spilling into my womb."
                    c "S-Seb!"
                    Sb "S-Shoot, S-sorry I--"
                    if persistent.bangok_knot == True:
                        m "I gasped as a large, hard knob at his base pulled through my lips, stretching me wide enough I was at first worried it'd be too big to slide out."
                    m "He pulled back, remaining spurts coating my passage and outer lips, dribbling small rivulets down my thighs."
                    m "I put a hand on my warm belly, now slightly larger than it had been when we'd started."
                else:
                    Sb "S-Shoot, S-sorry I--"
                    show sebastian at Position(xpos=0.5, ypos=1.1) with ease
                    if persistent.bangok_knot == True:
                        m "I gasped as a large, hard knob at his base pulled through my lips, stretching me wide enough I was at first worried it'd be too big to slide out."
                    m "He pulled back, the retreat of his cock leaving me colder and empty."
                jump bangok_four_xsebastian_vaginalsexend
            else:
                m "He thought about things for a moment."
                Sb drop b dk "Here, lie down the way you had been."
                c "Throatfucking?"
                Sb smile b dk "If you'll have it."
                c "Sure." # Because I'm not writing any other ways this scene goes down.
                play sound "fx/undress.ogg"
                show black with dissolvemed
                m "I lay down on the rocks with my head over one edge, and Seb pressed his moist cock back up against my lips."
                m "I suckled on his head as he pushed it in. He stopped abruptly."
                Sb shy b dk "Wh-What is that?"
                m "I let his cock pop free of my mouth."
                c "Suction?"
                $ renpy.pause (0.3)
                Sb shy b dk "Can you do that when I'm in your throat?"
                c "Maybe."
                $ renpy.pause (0.3)
                m "I took Sebastian back into my mouth. He kept going, pushing to the back of my throat, then beyond."
                m "I swallowed, trying to provide suction even with Sebastian's cock blocking my airways."
                Sb shy b sleep dk "Ah!"
                m "That pulled him over the edge immediately."
                jump bangok_four_xsebastian_oralinside
        "No rimming, please.":
            $ renpy.pause (0.5)
            Sb drop b dk "Oh. If you say so."
    $ renpy.pause (0.8)
    m "He adjusted his position and his grip, the scales on his chest momentarily brushing my back."
    $ renpy.pause (0.6)
    m "Then I felt his moist cockhead prodding my backdoor."
    Sb drop b dk "Ah-h."
    m "I clenched intentionally, tightening his entry. He pressed forward through the resistance, the pressure exquisite for us both."
    $ renpy.pause(0.5)
    Sb drop b dk "Ah- C-Can you actually take me in here? Is this hurting you?"
    $ renpy.pause(0.7)
    m "It took a few breaths to relax after my clenching. When I did, he slipped in the rest of the way, until his thighs rested on mine."
    $ renpy.pause(0.8)
    Sb smile b dk "Alright."
    if persistent.bangok_watersports == True:
        play soundloop "fx/faucet1.ogg" fadein 2.0
        queue soundloop "fx/faucet2.ogg"
        Sb drop b dk "Oh f-fuck."
        m "It took me a moment to realize what was spilling into me was not, in fact, ropes of sticky cum."
        Sb drop b dk "Sorry, I-- You're like someone else I know and I thought I could hold it..."
        m "Realizing Sebastian was using my ass to relieve himself, I pushed back, encouraging him."
        Sb shy b dk "O-Oh?"
        stop soundloop fadeout 1.0
        m "He finished a few moments later, but his piss remained, nestled safely inside me."
        Sb shy b dk "I... guess I should get moving..."
        play soundloop "fx/rub2.ogg" fadein 2.0
        m "He picked up a smooth pace, in and out, inward thrusts pushing his piss further into my guts with lewd squelches."
    else:
        play soundloop "fx/rub2.ogg" fadein 2.0
        m "He picked up a smooth pace, in and out."
    $ renpy.pause (0.8)
    m "I leaned forward into the bed of rocks, taking the assfucking to repay Sebastian for his glorious oral."
    $ renpy.pause (1.5)
    stop soundloop fadeout 0.5
    m "He leaned over me, hugging my back as he stopped deep inside."
    play sound "fx/extinguish.ogg"
    m "Then warmth blossomed within me."
    m "His shaft pulsed, rope after rope of seed deposited in my ass."
    if persistent.bangok_inflation == True:
        m "By the time the pulses slowed, I felt stuffed, like I'd eaten enough for the entire next day."
    if persistent.bangok_knot == True:
        c "Okay. We should probably lie back down to sleep. You want to pull out?"
        $ renpy.pause (0.8)
        Sb drop b dk "Um."
        m "Sebastian adjusted his feet backward slightly, and I immediately felt the problem bulging against my asshole."
        c "Ah-! O-okay, just-- just leave it."
        c "You, ah, could have mentioned that."
        Sb drop b dk "Sorry."
    else:
        m "Sebastian pulled out, still hugging me, a small dribble running down my taint."
    m "We rolled to one side, leaving him once again up against my back."
    show sebastian normal b dk:
        xanchor 0.5
        yanchor 1.0
        zoom 1.7
        xpos 0.8
        ypos 1.4
        # rotate 35
    with dissolve
    jump bangok_four_xsebastian_aftersex

label bangok_four_xsebastian_path1_2:
    if bangok_four_xsebastian_depth < 2:
        m "I took his shaft in both hands, stroking him forward and back with a tight ring of my fingers."
    else:
        m "I wrapped a hand around what little of his shaft wasn't buried deep in my throat, stroking with a tight ring of my thumb and index fingers."
    if persistent.bangok_cloacas == True:
        m "As Sebastian bucked into my face, my hand ring momentarily entered his slit, brushing against a tight asshole behind his cock."
    else:
        m "As Sebastian bucked into my face, the back of my hand brushed against a tight asshole, a little further back from his cock."
    m "Wanting to get him off before I got off, I pressed a finger inside, searching for the oh-so-useful pleasure button that hid there in human males."

    Sb shy b dk "Nngh!"
    if bangok_four_xsebastian_depth == 1:
        m "I had only a moment to choose."
        m "Did I want to swallow Sebastian's seed? Or could that be dangerous to me? Would it be better to get it all over my face? Or would the cleanup make it difficult to hide what we'd done?"
        menu:
            "In.":
                $ bangok_four_xsebastian_depth = 2
            "Out.":
                m "I pulled Sebastian's cock out of my mouth just in time."
                $ bangok_four_xsebastian_depth = 0

    if bangok_four_xsebastian_depth == 2:
        m "Sebastian's mouth popped free of my crotch as he thrust into my face and hand, shoving into my neck."
        label bangok_four_xsebastian_oralinside:
        play sound "fx/extinguish.ogg"
        m "His cock twitched deep in my throat, then spurt thick seed directly down, into my stomach."
        if persistent.bangok_inflation == True:
            m "I could only struggle to hold him close as he drained spurt after spurt into me, each forcing the last down until I felt full and light-headed."
            $ renpy.pause(0.8)
            c "(At least I won't need to eat for a bit?)"
        m "As his stringing ropes slowed he withdrew, leaving me struggling to swallow the last leftovers in my throat."
    elif bangok_four_xsebastian_depth == 0:
        play sound "fx/extinguish.ogg"
        m "Sebastian's mouth popped free of my crotch as he bucked into my face and hand, splattering my face with sticky ropes."
        m "It got everywhere; my nose, eyes, mouth, even a few droplets on my ear as his twitching cock strung creamy decorations across my face."
    else:
        $ renpy.error("Impossible bangok_four_xsebastian_depth")
    $ renpy.pause(0.5)
    play sound "fx/undress.ogg"
    m "Then, spent, Sebastian lay down next to me."
    show sebastian shy b dk:
        xanchor 0.5
        yanchor 1.0
        zoom 1.7
        xpos 0.8
        ypos 1.4
    hide black
    with dissolve
    $ renpy.pause(0.8)
    show sebastian smile b dk with dissolve
    Sb "Wow, I... I never thought a human would want to do such a thing with a dragon. Let alone be so good at it."
    if bangok_four_playerhasdick == True and bangok_four_xsebastian_playerfirst == False:
        show sebastian at Position(xpos=0.6) with ease
        m "I pushed myself up, unsatisfied cock twitching."
        c "Just you wait. I'm going to show you how you really breach a bastion."
        show sebastian shy b dk with dissolve
        Sb "O-Oh! Sorry, I forgot you..."
        show sebastian smile b dk with dissolve
        m "I lifted one of his legs aside, preparing to press as deeply as I could."
        if persistent.bangok_cloacas == True:
            m "I aimed my saliva-slicked shaft up to his asshole I had discovered earlier, just behind his own."
        else:
            m "I aimed my saliva-slicked shaft up to his asshole I had discovered earlier."
        m "Then I pushed inside of him."
        Sb drop b dk "Oh!"
        if bangok_four_xsebastian_depth == 0:
            m "As aroused as I was with Seb's load drying on my face, it was hard for me to take entering him slowly."
        else:
            m "As aroused as I was with Seb's load warming my belly, it was hard for me to take entering him slowly."
        play soundloop "fx/rub2.ogg" fadein 1.0
        show sebastian smile b dk:
            ease 0.15 xpos 0.604
            ease 0.5 xpos 0.6
            repeat
        with None
        m "He didn't seem to mind in the slightest as I started up my pace immediately, pushing to the hilt in his tight hole with my first thrust, and every one after."
        $ renpy.pause (0.4)
        m "His own cock re-emerged fully from its slit, slapping against my leg with every one of my thrusts."
        m "I took hold of it, stroking him to give him something more out of this as well."
        if persistent.bangok_knot == True:
            m "Since he'd cum, some kind of bulb had formed around his base -- what I realized had to be a knot. I gave it a squeeze and he gasped."
        show sebastian shy b dk with dissolve
        $ renpy.pause (1.2)
        show sebastian shy b sleep dk with dissolve
        m "It didn't take long to discover that I could squeeze his shaft to make him clench down on my own, bringing both of us to yet greater heights."
        $ renpy.pause (1.5)
        Sb shy b dk "[player_name]..."
        $ renpy.pause (0.3)
        show sebastian drop b dk at Position(xpos=0.6) with ease
        stop soundloop fadeout 1.0
        play sound "fx/rub1.ogg"
        $ renpy.pause(0.5)
        show sebastian shy b dk with dissolve
        play sound "fx/extinguish.ogg"
        show black with fadequick
        m "I thundered into him, plowing his legs wide before blasting inside."
        m "In my hand, his cock twitched too, a meagre dribble compared to his last go, but an orgasm nonetheless."
        show sebastian shy b sleep dk with dissolve
        hide black
        with dissolveslow
        $ renpy.pause(0.8)
        m "Sebastian lay, blissed out, as I slipped my cock from his ass and fell to the bed of rocks next to him."
        m "Then he cracked his eyes open with a smile."
        Sb smile b dk "Bastion breached."
        if mcwon == True:
            c "You'll tell them about how won at Bastion Breach now, right?"
            $ renpy.pause (1.2)
            Sb "Maybe."
        if persistent.bangok_watersports == True:
            menu:
                "Now, should I flood the fortress?":
                    $ renpy.pause (0.5)
                    Sb shy b dk "But you already came. What do you mean?"
                    Sb drop b dk "Oh. You're just like..."
                    $ renpy.pause(0.9)
                    Sb smile b dk "Sure. I can take it."
                    c "On you or in you?"
                    show sebastian normal b dk with dissolve
                    $ renpy.pause(0.6)
                    Sb drop b dk "In. Easier to deal with cleanup and won't leave much evidence."
                    $ renpy.pause(0.4)
                    play soundloop "fx/faucet1.ogg" fadein 2.0
                    queue soundloop "fx/faucet2.ogg"
                    show sebastian shy b dk with dissolve
                    c "Ahh..."
                    $ renpy.pause(0.5)
                    m "I let my bladder go in Sebastian's ass, washing deeper the cum I'd already deposited in him."
                    $ renpy.pause(1.2)
                    stop soundloop fadeout 1.0
                    $ renpy.pause(1.6)
                    Sb smile b dk "Better?"
                    c "Yeah."
                "[[Pull out.]":
                    $ renpy.pause (0.5)
    elif bangok_four_playerhasdick == False and bangok_four_xsebastian_playerfirst == False:
        c "Yeah..."
        Sb drop b dk "Oh. Did you...? I don't think I heard you get off did I--"
        c "Don't worry about it."
    else:
        c "Well, there you have it."
    jump bangok_four_xsebastian_aftersex

label bangok_four_xsebastian_path2:
    $ renpy.pause (1.5)
    m "Sebastian was definitely blushing, but said nothing."
    m "In the now-warmer embrace of his arms, I drifted off to sleep."
    show black with dissolveslow
    $ renpy.pause (1.0)
    hide black
    show sebastian shy b sleep dk
    with dissolveslow
    m "I was not sure how long I was out for, but I definitely had managed at least a few winks."
    m "Sebastian, behind me, was like a space heater, shifting a little in his sleep, squeezing me close."
    m "His arm had tugged up my shirt, and in the small of my back, something moist prodded me."
    menu:
        "[[Touch it.]" if (not _in_replay) and not (bangok_four_bangnokay or persistent.bangok_four_bangnokay):
            $ bangok_four_xsebastian_badtouch = True
            m "I didn't need my biology degree to figure out what it was, after our conversation earlier in the evening."
            m "Curiosity getting the better of me, I reached back, gently taking hold of his member and prying it away from my back."
            m "It was smooth, slightly tapered with a wider base than head, and a tip that bulged just slightly from the shaft, enough to give it a noticeable ridge, but not enough for said ridge to impede anything."
            m "Sebastian thrust back against my explorations, once, twice. Then he stiffened abruptly."
            m "I froze too, recognizing what I'd been doing tiptoed across the line of something wrong."
            $ renpy.pause (0.8)
            show sebastian drop b flip dk with dissolve
            m "Sebastian rolled away, scrambling for a little distance."
            Sb "D-Damnit!"
            Sb "This is all my fault. I-I took what you were saying the wrong way and... I-I didn't mean..."
            m "He curled into himself against the rockface."
            $ renpy.pause (0.8)
            Sb "(I propose one easy guard duty night and now I'm going to lose my job. I can't believe I did that.)"
            $ renpy.pause (0.8)
            jump bangok_four_xsebastian_path2_2_menu
        "Uh... Seb?":
            $ renpy.pause(0.8)
            c "Sebastian... Seb."
            Sb "Hmmh? What's going on?"
            $ renpy.pause(1.2)
            show sebastian shy b dk with dissolve
            $ renpy.pause(0.3)
            show sebastian shy b flip dk with dissolve
            Sb "Oh. Oh no. A-Ah [player_name], I'm sorry I didn't mean..."
            # $ renpy.pause (0.8)
            # Sb "(I propose one easy guard duty night and now I'm going to lose my job. I can't believe I did that.)"
            label bangok_four_xsebastian_path2_2_menu:
            menu:
                "It's okay. I'm interested.":
                    $ renpy.pause (0.5)
                    c "If that's what you want, I mean, sure."
                    c "We don't have to tell anyone. I'll leave it out of my reports if you leave it out of yours."
                    jump bangok_four_xsebastian_path2_1_1
                "[[Hug him.]" if bangok_four_xsebastian_badtouch == True:
                    $ renpy.pause (0.5)
                    play sound "fx/undress.ogg"
                    show sebastian drop b flip dk:
                        ease 1.0 xpos 0.6
                    with None
                    $ renpy.pause(0.3)
                    play sound "fx/undress.ogg"
                    $ renpy.pause(0.7)
                    m "I knelt behind Sebastian, wrapping my arms around him to try to calm him down."
                    show sebastian shy b flip dk:
                        ease 0.4 xpos 0.7
                    with None
                    m "He jerked away, throwing my arms off."
                    label bangok_four_xsebastian_badnight:
                    Sb "I-I can't do this... I'm sorry."
                    c "Wait--!"
                    show sebastian shy b dk with dissolve
                    hide sebastian with easeoutleft
                    m "Before I could lay another hand on him, Sebastian bolted from the cave, strong legs pounding into the earth, claws leaving scratches on the exposed rock."
                    m "I tried to get up and follow, but immediately found myself tripping over the rough stone floor in the dark."
                    c "(No way I'll be able to follow him outside if I can't even get there.)"
                    $ renpy.pause(0.8)
                    play sound "fx/undress.ogg"
                    m "I sat back down on our bed of rocks, waiting. For what, I wasn't sure."
                    $ renpy.pause(3.0)
                    show sebastian normal b flip dk at left with easeinleft
                    m "Then I saw a shadow darker than the darkness of the cave, keeping its distance from me, moving slowly."
                    show sebastian normal b flip dk:
                        xanchor 0.5
                        ease 1.0 xpos 0.4
                        ease 1.0 xpos 0.6
                        ease 1.0 xpos 0.8
                    with None
                    $ renpy.pause(3.5)
                    show sebastian normal b dk with dissolve
                    c "Sebastian?"
                    m "He sat against the wall, as far from me as he could be while still being as deep in the cave as I was."
                    c "Sebastian, I..."
                    Sb "Just sleep."
                    $ renpy.pause(0.5)
                    m "I lay back down on the bed of rocks."
                    $ renpy.pause(0.5)
                    c "Goodnight."
                    $ persistent.sebastianfail = True
                    jump bangok_four_xsebastian_todaywasgreat_return
                "[[Pretend to be asleep.]":
                    $ renpy.pause (0.5)
                    m "I lay still, realizing how frightening this must be for him and not wanting to make it any worse."
                    m "Maybe if he thought I was still asleep, he'd calm down and forget about it?"
                    $ renpy.pause (0.8)
                    Sb "(Is... Is [player_name] not awake?)"
                    $ renpy.pause (0.8)
                    Sb drop b flip dk "(Not awake. I imagined it.)"
                    $ renpy.pause (0.8)
                    Sb shy b flip dk "(I must have imagined them saying...)"
                    $ renpy.pause (0.8)
                    Sb drop b flip dk "(I'll just sleep over here. [player_name] looks fine with the temperature now.)"
                    $ renpy.pause (1.2)
                    Sb "(Thank goodness. Asleep. I'm fine.)"
                    $ renpy.pause (0.8)
                    m "The echoes of Sebastian's warmth on my back, I drifted back into an uneasy sleep."
                    scene black with dissolvemed
                    jump bangok_four_xsebastian_todaywasgreat_return



        "[[Go back to sleep.]":
            m "Careful not to wake Seb, I tucked my shirt back in and pushed from my mind thoughts of what the moist spot might be."
            scene black wtih dissolveslow
            m "Before long, sleep had taken me once again."
            jump bangok_four_xsebastian_todaywasgreat_return


label bangok_four_xsebastian_path2_1_1:
    Sb shy b dk "B-But... wait, you are?"
    c "I mean, at the very least we should compare. Our cultural exchange has already gone this far."
    Sb drop b dk "I..."
    if bangok_four_bangnokay or persistent.bangok_four_bangnokay:
        jump bangok_four_xsebastian_badnight
    Sb shy b dk "I have to admit I'm curious. O-Obviously I've never seen a human's..."
    play sound "fx/zip.ogg"
    if bangok_four_playerhasdick is None:
        menu:
            "My shaft is already hard.":
                $ bangok_four_playerhasdick = True
            "My hole is already slick.":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick == True:
        m "My shaft is already hardening as I tug it from my pants for Seb to see."
    else:
        $ renpy.pause(0.3)
        play sound2 "fx/undress.ogg"
        m "I tugged my pants down, enough that Sebastian could easily see my arousal."
    
    m "Only neither of us could see anything."
    c "Oh, right, it's a bit dark. Should we relight one of the torches?"
    Sb drop b dk "No! S-Someone might see us."
    c "Oh. Well. You could explore by touch, then. If you'd like..."
    show sebastian shy b dk with dissolve
    show sebastian at Position(xpos=0.6) with ease
    $ renpy.pause(0.6)
    m "Sebastian's claws were like icicles against the exposed skin of my thighs, as he searched for my reproductive organ."
    if bangok_four_playerhasdick == True:
        m "When his palm bumped into my cock, his hand reflexively closed around it. I gasped, quietly, from the rough texture of his scales and icy surface of his claws."
        m "He immediately let go again."
        Sb "I... You're sure you're okay with this?"
        c "Absolutely."
        $ renpy.pause (0.5)
        m "Cautiously, he took my shaft in hand again, then began to gently slide his hand up and down, exploring my shape and softness."
        $ renpy.pause (0.5)
        m "My breath came faster, the rough surface of his hand leaving me achingly hard."
        $ renpy.pause (0.5)
        Sb smile b dk "Is this... does this feel good for you?"
        c "Yeah."
        $ renpy.pause (0.5)
        m "The nature of his movements changed. He wasn't just exploring me, now. He was pumping me."
        $ renpy.pause (0.5)
        Sb "Do you want me to keep going?"
        c "Mhmm."
        m "He tightened his grip, fucking his hand with my cock. I thrust back, aching with need."
        show sebastian shy b dk with dissolve
        m "Then he pulled his hand away, confidence faltering."
        Sb "I... ah..."
        $ renpy.pause (0.5)
        c "No. Feel free to keep going."
        Sb "I wanted to ask. May I... take you in my..."
        $ renpy.pause (0.3)
        m "He didn't specify where, but in my lust-addled state I didn't much care."
        c "Yes."
        show sebastian at center with ease
        m "Sebastian climbed on top of me. The tip of my shaft bapped into something moist -- Sebastian's own."
        m "Before I could ask what he was doing, the head of my aching cock was pressed against a hole. I thrust only slightly, but it was enough to press inside."
        Sb drop b dk "Oh!"
        show sebastian at Position(ypos=1.05) with ease
        m "Sebastian pressed a little further down, my shaft disappearing easily into what I could only assume was his ass."
        m "Warmth clenched at and surrounded my tip, all the heat he'd given me before through scale-to-clothes contact concentrated in our aroused groins."
        show sebastian smile b dk:
            ease 0.15 ypos 1.08
            ease 0.5 ypos 1.05
            repeat
        play soundloop "fx/rub2.ogg" fadein 1.0
        m "Before long he was moving, fucking himself deeper onto my shaft."
        m "I was all but lost in the sensations, but I didn't want this to be about just him getting me off."
        menu:
            "[[Stroke him.]":
                $ renpy.pause(0.5)
                m "It took me a moment to find in the dark even as it slapped against my stomach, but I managed to get my hand around Sebastian's dick. His up-and-down motions fucked it forward and backward in my grip, stimulating him for every motion he made."
                m "Sebastian picked up his pace slightly, leaning forward into the sensations."
                $ renpy.pause(1.2)
                c "(If he cums, he's going to get it all over my only shirt.)"
                m "With my free hand, I went at the buttons, trying to clear a runway for him to shoot into."
                $ renpy.pause(0.8)
                m "Before I could manage the highest buttons, Seb's clenching dragged me over my own peak."
                show sebastian shy b dk:
                    ease 0.3 ypos 1.1
                with None
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                $ renpy.pause(0.2)
                show black with fadequick
                $ renpy.pause(1.0)
                show sebastian smile b dk
                hide black
                with dissolvemed
                m "When I came back down, Seb was still moving his hips a little, lightly fucking my hand as his ass milked me for every drop."
                m "Now that he wasn't moving up and down, I could manage to give him more direct pumps with my hand."
            "[[Fuck him back.]":
                $ renpy.pause(0.5)
                m "Reaching up, I got my hands onto his hips, pulling myself up and him further down with each thrust, so every one hilted me inside him and slapped his cock against my chest."
                show sebastian shy b dk with dissolve
                $ renpy.pause(0.8)
                show sebastian smile b dk with dissolve
                m "He kept up his pace, meeting my mating thrusts with all the same enthusiasm."
                $ renpy.pause(1.2)
                c "(If he cums, he's going to get it all over my only shirt.)"
                m "I took one of my hands away, tugging at my buttons to try to clear a runway for him to shoot into."
                $ renpy.pause(0.8)
                m "Before I could manage the highest buttons, Seb's clenching dragged me over my own peak."
                show sebastian shy b dk:
                    ease 0.3 ypos 1.1
                with None
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                $ renpy.pause(0.2)
                show black with fadequick
                $ renpy.pause(1.0)
                show sebastian smile b dk
                hide black
                with dissolvemed
                m "When I came back down, Seb was still moving his hips a little, frotting against my belly as his ass milked me for every drop."
                m "I took his shaft in hand, pumping him in thanks for what he'd given me."
            "[[Kiss his hand.]":
                $ renpy.pause(0.5)
                show sebastian shy b dk with dissolve
                m "I caught his hand in the dark, tugging him slightly forward as I brought it and my lips together."
                m "His heat immediately flooded the spot, and I had little doubt a flush would be visible there if either of us could see in the darkness."
                $ renpy.pause(0.8)
                m "I kissed his hand, again and again, practically suckling on his rough scales."
                $ renpy.pause(0.9)
                c "(If he cums, he's going to get it all over my only shirt.)"
                m "With my free hand, I went at the buttons, trying to clear a runway for him to shoot into."
                $ renpy.pause(0.8)
                m "Before I could manage the highest buttons, Seb's clenching dragged me over my own peak."
                show sebastian shy b dk:
                    ease 0.3 ypos 1.1
                with None
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                $ renpy.pause(0.2)
                show black with fadequick
                $ renpy.pause(1.0)
                show sebastian smile b dk
                hide black
                with dissolvemed
                m "When I came back down, Seb was still moving his hips a little, frotting against my belly as his ass milked me for every drop."
                m "I took his shaft in hand, pumping him in thanks for what he'd given me."

        m "Apparently, that was all the endurance he had left."
        show sebastian shy b dk
        $ renpy.pause(0.3)
        play sound "fx/extinguish.ogg"
        Sb "Ah!"
        m "Sticky spurts splattered across my mostly-bare chest, hitting my pecs, my shirt collar, neck, and even stringing across my mouth."
        m "I licked my lips, finding his cum sweeter than I understood humans' to be. I kept pumping, tugging more of the creamy treat onto my chest."
        $ renpy.pause(0.8)
        Sb drop b dk "S-Sorry. I didn't mean to get it all over your..."
        c "I think you missed most of my shirt."
        $ renpy.pause(0.8)
        m "Sebastian's weight rested completely on me, my softening shaft still buried inside him. I gave one of his legs a pat with my hand that wasn't sticky with his cum."
        c "You weren't kidding about those strong legs."
        Sb shy b dk "Yeah..."
        $ renpy.pause(1.2)
        show sebastian shy b dk at Position(ypos=1.0) with ease
        m "He pushed back to his feet in one easy motion, leaving my shaft to plop free."
        Sb "... I just had a human cum inside me. I... I just came on a human."
    else:
        m "He found his target when one of his claws sank into my folds, up to his first knuckle, before he realized he was inside me. My small gasp made him pull back immediately."
        Sb "I... You're sure you're okay with this?"
        c "Absolutely."
        $ renpy.pause (0.5)
        m "Cautiously, he slid a single claw back into my folds, the rough scales on his hand leaving shivers in my thighs."
        m "He searched up and down, exploring just barely inside. The icy surface of his claw brushed my clit. My legs tensed, fresh lubrication dribbling around his claw as I prepared for more."
        if persistent.bangok_cloacas == True:
            Sb drop b dk "Wait, your ass isn't in here too?"
            c "No. It's further back."
            Sb smile b dk "Hm."
        else:
            show sebastian smile b dk with dissolve
        m "He slipped a second claw in with his first. The contrast between the one my body had warmed and the one that had been chilling outside sent fresh sparks of pleasure up my canal, and I moaned quietly."
        show sebastian shy b dk with dissolve
        $ renpy.pause (0.8)
        c "No. Feel free to keep going."
        Sb "I wanted to ask. May I... take you with..."
        $ renpy.pause(0.5)
        m "He needn't have asked; in my lust-addled state I was all for it."
        c "Yes."
        play sound "fx/undress.ogg"
        m "I kicked my pants the rest of the way off one of my legs, giving him room to get in."
        show sebastian at Position(xpos=0.5, ypos=1.1, xanchor='center') with ease
        m "Sebastian climbed on top of me, the claws he'd prodded with leaving cold trails on my thighs as he spread me apart. Something wet poked just under the hem of my shirt, smearing a trail from my navel to my love passage as he tried to line up."
        m "As soon as I felt his head against my lips, I pushed my hips onto it with what little leverage I had."
        Sb drop b dk "Oh!"
        show sebastian at Position(xpos=0.48, ypos=1.13) with ease
        m "He slid in, his arousal and mine making the passage of his cock easy. I panted, sparks flying inside."
        $ renpy.pause(0.8)
        show sebastian at Position(xpos=0.45, ypos=1.15) with ease
        m "After giving me a moment, Sebastian pushed further in, his slit pressing into my own. My legs spread wide to reach around his, rough scales against my smooth thighs."
        $ renpy.pause(0.8)
        show sebastian smile b dk:
            ease 0.15 xpos 0.45 ypos 1.15
            ease 0.5 xpos 0.48 ypos 1.13
            repeat
        play soundloop "fx/rub2.ogg" fadein 2.0
        m "Seb began to move, pulling out to his tip then sliding back to his base."
        $ renpy.pause(1.2)
        if bangok_four_malepartners > 0:
            m "I clenched around him, massaging his cock inside of me. His smooth, slick shaft was a completely different experience to anything I'd had before."
        else:
            m "I clenched around him, massaging his cock inside of me. His smooth, slick shaft was a completely different experience to anything but other dragons."
        $ renpy.pause(1.3)
        m "My peak crept up without warning."
        c "I-I'm close--!"
        $ renpy.pause(0.2)
        show black with fadequick
        m "My lower body squeezed, sucking and milking Sebastian for his seed even as he continued thrusting."
        $ renpy.pause(0.5)
        stop soundloop fadeout 0.5
        play sound "fx/extinguish.ogg"
        m "Warmth blossomed inside of me a moment later, as I dragged Seb over his peak with me."
        show sebastian shy b sleep dk at Position(xpos=0.48, ypos=1.15)
        hide black
        with dissolveslow
        $ renpy.pause(0.3)
        if persistent.bangok_inflation == True:
            m "His cock kept twitching, rope after rope spurting inside until it was spilling into my womb."
            c "S-Seb!"
            show sebastian smile b dk with dissolve
            $ renpy.pause(0.4)
            show sebastian shy b dk with dissolve
            Sb "S-Shoot, S-sorry I--"
            show sebastian at Position(xpos=0.5, ypos=1.1) with ease
            if persistent.bangok_knot == True:
                m "I gasped as a large, hard knob at his base pulled through my lips, stretching me wide enough I was at first worried it'd be too big to slide out."
            m "He pulled back, remaining spurts coating my passage and outer lips, dribbling a pool between my thighs."
            m "I put a hand on my warm belly, now slightly larger than it had been when we'd started."
        else:
            show sebastian smile b dk with dissolve
            m "Sebastian smiled down at me, then realized what he'd done."
            show sebastian shy b dk with dissolve
            Sb "S-Shoot, S-sorry I--"
            show sebastian at Position(xpos=0.5, ypos=1.1) with ease
            if persistent.bangok_knot == True:
                m "I gasped as a large, hard knob at his base pulled through my lips, stretching me wide enough I was at first worried it'd be too big to slide out."
            m "He pulled back, the retreat of his cock leaving me colder and empty."
        show sebastian at Position(xpos=0.6, ypos=1.1) with ease
        label bangok_four_xsebastian_vaginalsexend:
        Sb shy b dk "Oh no. Nonono. What have I done?"
        c "Hey, relax. We both wanted this. I can find a morning-after pill or something."
        Sb drop b dk "I mean, most dragon species aren't genetically compatible. That's even more likely with the differences between my species and yours."
        Sb shy b dk "But I can't get over the fact: I just came in a human."

    c "Yep."
    m "Before he could start to overthink it like when we'd woken up, I set a hand on his shoulder."
    c "And you were adorable throughout."
    $ renpy.pause(1.3)
    Sb drop b dk "I'm not sure that's the word I want applying to my sexcapades."
    c "Last I checked, we're not applying any words to it, because we're leaving it out of our reports."
    Sb "R-Right."
    $ renpy.pause (0.8)
    show sebastian normal b dk:
        xanchor 0.5
        yanchor 1.0
        zoom 1.7
        xpos 0.8
        ypos 1.4
    with ease
    m "After a moment, Sebastian lay back down next to me."
    jump bangok_four_xsebastian_aftersex


label bangok_four_xsebastian_aftersex:
    $ bangok_four_xsebastian_unplayed = False
    $ bangok_four_malepartners += 1
    Sb drop b dk "Whew... who would have thought us and humans can be this compatible."
    c "It was certainly a wonderful experience. I'm glad you said yes to it."
    c "Speaking of, how come you got so relaxed about it so quickly?"
    Sb smile b dk "Heh, you see, fooling around with certain friends is quite a common thing for me."
    c "Oh? Is that how most dragons are?"
    Sb normal b dk "Not really. I've just been lucky to have met one or two... like-minded friends in this town."
    c "Ooh, is it someone I know?"
    Sb shy b dk "I won't comment on that."
    Sb "But yeah, I was still worried at first because, quite frankly, you're a huge responsibility. It's not every day that a human shows up in our town, you know. And with everything else going on..."
    $ renpy.pause(1.2)
    Sb drop b dk "I was tasked with guarding you and I need to do my job right. This definitely isn't how you're supposed to treat an ambassador."
    c "Hey, the ambassador has felt very safe and cared for this entire time. You did a {i}fantastic{/i} job, Seb."
    Sb shy b dk "I'm flattered."
    Sb normal b dk "But still... please don't tell anyone about what happened here. I'm certainly not gonna mention it in my report."
    c "If anyone asks, I'll say you went above and beyond in your service."
    Sb smile b dk "Heh. And I'll say you did great at improving the tense relations between our species."
    c "Sounds like a deal."
    Sb normal b dk "But we really should get some actual sleep now."
    play sound "fx/undress.ogg"
    scene black with dissolve
    m "Sebastian tugged me closer, wrapping more of his smaller body over my exposed flesh."
    Sb "Good night."
    c "Sweet dreams."
    jump bangok_four_xsebastian_todaywasgreat_return

# TODO: Morning scene? Watersports?