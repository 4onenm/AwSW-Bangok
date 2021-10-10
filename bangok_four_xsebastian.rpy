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
    Sb shy b dk "A-Are you being serious?"
    c "What can I say? You're an attractive dragon."
    jump bangok_four_xsebastian_outofcontent

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
        "[[Touch it.]":
            m "I didn't need my biology degree to figure out what it was, after our conversation earlier in the evening."
            m "Curiosity getting the better of me, I reached back, gently taking hold of his member and prying it away from my back."
            m "It was smooth, slightly tapered with a wider base than head, and a tip that bulged just slightly from the shaft, enough to give it a noticeable ridge, but not enough for said ridge to impede anything."
            m "Sebastian thrust back against my explorations, once, twice. Then he stiffened abruptly."
            m "I froze too, recognizing what I'd been doing tiptoed across the line of something wrong."
            $ renpy.pause (0.8)
            show sebastian drop b flip dk with dissolve
            m "Sebastian rolled away, scrambling for a little distance."
            Sb "D-Damnit!"
            Sb "This is all my fault. I- I took what you were saying the wrong way and... I- I didn't mean..."
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
                # "[[Hug him.]": # TODO: How does this merge back into the professional Seb we know in the rest of the story?
                #     play sound "fx/undress.ogg"
                #     show sebastian drop b flip dk
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
        c "I- I'm close--!"
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
            m "He pulled back, remaining spurts coating my passage and outer lips, dribbling a pool between my thighs."
            m "I put a hand on my warm belly, now slightly larger than it had been when we'd started."
        else:
            show sebastian smile b dk with dissolve
            m "Sebastian smiled down at me, then realized what he'd done."
            show sebastian shy b dk with dissolve
            Sb "S-Shoot, S-sorry I--"
            show sebastian at Position(xpos=0.5, ypos=1.1) with ease
            m "He pulled back, the retreat of his cock leaving me colder and empty."
        show sebastian at Position(xpos=0.6, ypos=1.1) with ease
        Sb "Oh no. Nonono. What have I done?"
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
    s "TODO: Implement aftersex."
    jump bangok_four_xsebastian_todaywasgreat_return



label bangok_four_xsebastian_outofcontent:
s "TODO: Out of content."
$ renpy.error("Out of content error.")