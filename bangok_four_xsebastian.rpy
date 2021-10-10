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
    m "I'm not sure how long I was out for, but I definitely managed at least a few winks."
    m "Sebastian, behind me, is like a space heater, shifting a little in his sleep, squeezing me close."
    m "His arm had tugged up my shirt, and in the small of my back, something moist prodded me."
    menu:
        "[[Touch it.]":
            m "I didn't need my biology degree to figure out what it was, after our conversation earlier in the evening."
            m "Curiosity getting the better of me, I reached back, gently taking hold of his member and prying it away from my back."
            m "It was smooth, slightly tapered with a wider base than head, and a tip that bulged just slightly from the shaft, enough to give it a noticeable ridge, but not enough for said ridge to impede anything."
            m "Sebastian thrust back against my explorations, once, twice. Then he stiffened abruptly."
            m "I froze too, recognizing what I'd been doing tiptoed across the line of something wrong."
            $ renpy.pause (0.8)
            show sebastian drop b dk with dissolve
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
        m "I was all but lost in the sensations, but I didn't want this to be about just getting me off."
        menu:
            "[[Stroke him.]":
                pass
            "[[Fuck him back.]":
                pass
            "[[Kiss his hand.]":
                pass
    else:
        m "He found his target when one of his claws sank into my folds, up to his first knuckle, before he realized he was inside me. My small gasp made him pull back immediately."






label bangok_four_xsebastian_outofcontent:
s "TODO: Out of content."
$ renpy.error("Out of content error.")