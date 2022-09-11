##################### NOTICE #####################
# Per request from the commissioner of the artwork
#  forming the basis of this scene, absolutely no
#  watersports (nor any mention thereof) is to be
#  added to this scene.

init python in bangok_four_xdamion_store:
    unplayed = True
    peek_window = False


label bangok_four_annaxdamion:
    play soundloop "fx/bangok_poundofsalt.ogg" fadein 2.0
    m "As I walked up to Anna's partially-ajar door, I heard a rhythmic wet smacking coming from the lab."
    $ renpy.pause(0.8)
    c "(What is that...?)"

    if (persistent.bangok_four_bangnokay or bangok_four_bangnokay):
        stop soundloop fadeout 1.0
        play sound "fx/steps/clean2.wav"
        show black with dissolvemed
        m "Having no reason to pry into the private lives nor scientific experimentation of the dragons, I decided to come back a little later."
        jump bangok_four_annaxdamion_abort_merge

    menu:
        "Listen closer.":
            pass
        "Come back a little later.":
            jump bangok_four_annaxdamion_abort1

    m "I stepped a little closer to the door, listening to try to figure out what was going on."
    An disgust "Fucking-- Damion, don't bend my tail like that!"
    "???" "Afraid you'll discover you're into a bit of pain on top of--? Nngh."

    menu:
        "Peek.":
            pass
        "Come back a little later.":
            jump bangok_four_annaxdamion_abort1

    scene black with dissolvemed
    $ renpy.pause (0.5)
    if persistent.bangok_cloacas == True:
        scene bangok_four_annaxdamion cloacal:
            zoom 2.2
            anchor (0.0,0.0)
            pos (0.0,-0.5)
    else:
        scene bangok_four_annaxdamion vaginal:
            zoom 2.2
            anchor (0.0,0.0)
            pos (0.0,-0.5)
    show white:
        alpha 0.9
    show bangok_four_labdoor:
        anchor (0.0,0.0)
        pos (0.0,0.0)
    with dissolvemed

    $ renpy.pause (0.5)

    show bangok_four_annaxdamion:
        ease 3.0 zoom 1.1 pos (180, 0)
        block:
            ease 0.5 pos (175, 0)
            ease 0.15 pos (180, 0)
            repeat
    show bangok_four_labdoor:
        transform_anchor True
        ease 3.0 zoom 2.5 pos (-2880, -427)
        block:
            block:
                choice:
                    ease 0.8 pos (-2885, -427)
                choice:
                    ease 1.0 pos (-2885, -427)
                choice:
                    ease 1.2 pos (-2885, -427)
            pause 0.5
            block:
                choice:
                    ease 0.8 pos (-2880, -427)
                choice:
                    ease 1.0 pos (-2880, -427)
                choice:
                    ease 1.2 pos (-2880, -427)
            pause 0.5
            repeat
    show white:
        pause 2.0
        ease 1.3 alpha 0.0
    with None

    $ renpy.pause (2.5)

    An sad "Would you just cum already, so I can clean up and get back to work?"
    Dm arrogant "I'll cum in you when I'm good and ready."
    stop soundloop fadeout 1.0
    show bangok_four_annaxdamion:
        ease 3.0 zoom 1.1 pos (190, 0)
    with ease
    Dm normal "Now scoot forward. I want to be pressing down on you."
    An face "You already are!"

    menu:
        "Look closer through the door crack.":
            $ bangok_four_xdamion_store.peek_window = False

            show bangok_four_labdoor dk track with dissolve
            show bangok_four_labdoor dk track:
                ease 2.0 zoom 10.0 pos (-12550, -3000)
                zoom 10.0
                pos (-12550, -3000)
            show bangok_four_annaxdamion:
                ease 2.1 zoom 1.2 pos (200, 0)
                pause 0.3
                block:
                    ease 0.5 pos (205, 0)
                    ease 0.15 pos (200, 0)
                    repeat
            with None
            $ renpy.pause (2.0)

        "Peek through the window.":
            $ bangok_four_xdamion_store.peek_window = True

            show bangok_four_labdoor dk track with dissolve
            show bangok_four_labdoor dk track:
                ease 2.0 zoom 10.0 pos (-9650, -6900)
                zoom 10.0
                pos (-9650, -6900)
            show bangok_four_annaxdamion:
                ease 2.1 zoom 1.2 pos (200, 0)
                pause 0.3
                block:
                    ease 0.5 pos (205, 0)
                    ease 0.15 pos (200, 0)
                    repeat
            with None
            $ renpy.pause (2.0)
        "Come back a little later.":
            jump bangok_four_annaxdamion_abort2

    play soundloop "fx/rub2.ogg"
    $ renpy.pause (0.5)
    Dm arrogant "There we fucking go."
    An sad "Mmnnh."
    $ renpy.pause (1.6)

    Dm arrogant "Ahh. See? Isn't it nice when you spread for me?"
    An sad "..."
    Dm face "Ngh. Well, fun time's about to be over."
    if persistent.bangok_cloacas == True:
        Dm "Have fun cleaning this out of your cloaca."
    else:
        Dm "Have fun cleaning this out of your pussy."


    stop soundloop fadeout 0.5
    play sound "fx/rub2.ogg"
    show bangok_four_annaxdamion:
        ease 2.1 zoom 1.2 pos (200, 0)
    with ease
    $ renpy.pause (0.3)
    play sound "fx/extinguish.ogg"

    if persistent.bangok_cloacas == True:
        show bangok_four_annaxdamion cloacal cum with dissolvemed
    else:
        show bangok_four_annaxdamion vaginal cum with dissolvemed

    if persistent.bangok_inflation == True:
        Dm face "F-Fuck this is a big load."
        if persistent.bangok_cloacas == True:
            show bangok_four_annaxdamion cloacal bulge cum with dissolvemed
        else:
            show bangok_four_annaxdamion vaginal bulge cum with dissolvemed
        An disgust "Ah!"

    $ renpy.pause (0.5)
    Dm arrogant "Ah. There. Your problem now, for once."
    if bangok_four_xdamion_store.peek_window == True:
        An disgust "Damion."
        Dm arrogant "What?"
        An sad "I think I see someone at the door--"
        scene white
        show bangok_four_labdoor
        with dissolve
        m "I ducked down, trying to avoid being spotted, but it sounded like the damage had already been done."
        Dm face "I'll go look."
        show cgdamion at Pan((0, 100), (0, 150), 5.0) behind bangok_four_labdoor with dissolvemed
        m "Our eyes met through the window. There was no way he didn't see me."
        Dm arrogant "You left the fucking door partway open. Other than that? Nothing."
        play sound "fx/door/doorclose.ogg"
        scene facin2 at Pan ((128, 250), (128, 250), 0.0) with dissolve
        m "He pulled it closed, and his voice became muffled."
        play sound "fx/steps/clean2.wav"
        m "I hurried away from the door, not wanting to be caught by Anna peeking in on her tryst if this Damion didn't want me to be."
    else:
        An sad "Happy, Damion?"
        Dm "Happy enough, I suppose. At least enough not to mention--"
        An sad "Then get off of me. I need to go clean up."
        scene black with dissolve
        scene facin2 at Pan ((128, 250), (128, 250), 0.0) with dissolvemed
        m "I hurried away from the door as Damion got off of Anna, not wanting to be caught peeking in on this draconic mating habit."

    show anna sad at right with easeinright
    play sound "fx/door/doorclose.ogg"
    m "Having just gotten behind a pillar, I heard the door close back at the lab."
    show anna sad flip with dissolve
    show anna sad with dissolve
    show anna sad flip with dissolve
    $ renpy.pause (0.3)
    hide anna with easeoutright
    m "After looking for anyone who might see her, Anna rushed down the hall, toward the restroom."

    if bangok_four_xdamion_store.peek_window == True:
        $ renpy.pause (1.0)
        m "I hesitated there in the hallway. Did I still want to seek answers about Reza, like I was supposed to be doing, after I'd been caught watching them?"
        menu:
            "Go talk to Damion.":
                $ renpy.pause (0.5)
                play sound "fx/silence.ogg"
                queue sound "fx/knocking1.ogg"
                m "I walked over to the lab door and knocked."
                jump bangok_four_annaxdamion_talk_damion_caught
            "Leave.":
                play sound "fx/steps/clean2.wav"
                scene black with dissolveslow
                $ renpy.pause (0.5)
                m "There were other leads on Reza to pursue, but I might not survive the embarrassment of that conversation if I had to have it."
                $ renpy.pause (0.5)
                scene town1 with dissolvemed
                jump chapter2sections

    else:
        $ renpy.pause (1.0)
        play sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/knocking1.ogg"
        m "After waiting a little while to make sure she'd gone, I walked over to the lab door and knocked."
        c "(Anna might be busy for a little while. Maybe I can ask this Damion about Reza...)"

label bangok_four_annaxdamion_talk_damion_notcaught:
    play sound "fx/door/door_open.wav"

    scene black with dissolve
    $ renpy.pause (0.5)

    show cgdamion at Pan((0, 0), (0, 302), 5.0) with dissolvemed
    $ renpy.pause(1.0)

    Dm arrogant "Back for more already An--"
    Dm face "Oh."

    scene facin2 at Pan ((128, 250), (128, 250), 0.0)
    show damion arrogant
    with fade

    $ metdamion2 = True
    $ persistent.metdamion = True

    Dm arrogant "Can I help you?"
    c "Damion, right? I have a few questions about your lab."
    Dm face "Yes. Where I come from, people usually introduce themselves before they start asking questions, though."
    c "You don't know who I am?"
    Dm arrogant "Tchk, of course I know who you are, but that doesn't mean you don't need to learn some manners."
    Dm normal "I'm in a good mood right now. So go ahead, what do you want?"

    jump bangok_four_annaxdamion_canon_questions

label bangok_four_annaxdamion_talk_damion_caught:
    play sound "fx/door/door_open.wav"
    scene black with dissolve
    $ renpy.pause (0.5)
    show cgdamion at Pan((0, 0), (0, 302), 5.0) with dissolvemed
    $ renpy.pause(3.0)

    hide cgdamion
    scene facin2 at Pan ((128, 250), (128, 250), 0.0)
    show damion arrogant
    with fade

    $ metdamion2 = True
    $ persistent.metdamion = True

    Dm arrogant "Well, if it isn't the human voyeur."
    Dm arrogant "You need to be more careful with things like that. I don't mind, but that bitch would have had a fit."
    Dm normal "I assume that's not what you were originally here for, though."
    c "Do you mind if I ask a few questions about your lab?"
    Dm arrogant "Do you mind sucking my dick, since you liked looking at it so much?"
    menu:
        "I can do that.":
            $ renpy.pause (0.5)
            Dm "I..."
            $ renpy.pause (0.5)
            show damion face with dissolve
            $ renpy.pause (0.4)
            Dm face "Ha{w=0.4} ha.{w=0.4} Very funny."
            jump bangok_four_annaxdamion_to_xdamion
        "I... I guess?":
            $ renpy.pause (0.5)
            label bangok_four_annaxdamion_to_xdamion:
            Dm arrogant "I was joking. Unless you're actually serious."
            menu:
                "Accept.":
                    show damion face with dissolve
                    $ renpy.pause (0.3)
                    Dm face "..."
                    $ renpy.pause (0.8)
                    Dm normal "Fuck it. Get in here."

                    scene crapannalab:
                        zoom 1.2
                        anchor (0.5, 1.0)
                        pos (0.5, 1.0)
                    with wipeleft
                    play sound ["fx/door/hallwaydoor.ogg", "fx/door/lock.ogg"]
                    $ renpy.pause(0.5)

                    m "Damion closed and locked the door to the hallway, then backed me against a lab bench, dick already sliding from a slit on his lower body."

                    # NOTE: xdamion ws scenes not to be made accessible from this scene, per anna x damion cg commissioner wishes.

                    jump bangok_four_xdamion_fuck

                "Reject.":
                    Dm normal "Then don't waste any more of my time. Ask your questions."
                    jump bangok_four_annaxdamion_canon_questions
        "What the fuck?":
            pass
        "[[Stare blankly.]":
            pass
    $ renpy.pause (0.8)
    Dm face "I'm kidding, obviously."
    Dm normal "Ask your questions."

    jump bangok_four_annaxdamion_canon_questions


label bangok_four_annaxdamion_abort1:
    stop soundloop fadeout 1.0
    play sound "fx/steps/clean2.wav"
    show black with dissolvemed
    m "Having a good idea I didn't want to interrupt what I was hearing, I walked past the door without looking inside, figuring I could return when the lab sounded less busy."
    jump bangok_four_annaxdamion_abort_merge

label bangok_four_annaxdamion_abort2:
    stop soundloop fadeout 1.0
    play sound "fx/steps/clean2.wav"
    scene black with dissolvemed
    show facin2 behind black at Pan ((0, 250), (128, 250), 3.0) with None
    m "Not wanting to interrupt their fucking, I turned back and escaped while I could, figuring I could return when the lab was a little less busy."
    jump bangok_four_annaxdamion_abort_merge


label bangok_four_annaxdamion_abort_merge:
    m "I went for a lap around the floor. My simple lap of the building took quite a while, however, as I ran into a dead end, forcing me to go down a staircase and get lost in a maze of passages to complete the loop."
    hide black with dissolveslow
    m "I returned, eventually, to a properly-shut lab door."
    jump bangok_four_annaxdamion_return