init python in bangok_four_bryce4_store:
    unplayed = True

label bangok_four_bryce4_bangnokay:
    Br smirk "Yeah, romantic is a way they could go."
    Br normal "Speaking of, you know, when you slept over last time and we shared the couch, I took it as a sign."
    Br "Did that mean anything to you? Or was that just two friends sharing a couch that was clearly too small for two people who just wanted to stay friends?"

    menu:
        "It didn't mean what you thought it meant.":
            $ renpy.pause (0.5)
            Br laugh "Whoops. That's my bad, then. Guess you humans don't do things the same way as far as that goes." 
            Br normal "Probably for the best we figured that out, huh?"
            jump b4jump
        "It meant exactly what you thought it meant.":
            $ renpy.pause (0.5)
            Br laugh "Oh, it did?"
            Br smirk "Glad I wasn't overthinking things, huh?"
        "It didn't mean anything, but we can still make this a romantic evening.":
            $ renpy.pause (0.5)
            Br smirk "Oh, really?"
            c "I didn't know you were interested."
            Br laugh "I am. Just maybe overthinking a little."
        "I was thinking about sex with you all that night.":
            $ renpy.pause (0.5)
            jump bangok_four_bryce4_bangnokay_rejection

    menu:
        "Yeah, overthinking can be a pain.":
            $ renpy.pause (0.5)
            Br normal "No kidding."
            jump b4jump
        "Nothing to overthink. I'd love to get closer to you.":
            $ renpy.pause (0.5)
            Br brow "Ah, closer how?"
            c "Maybe I get another bottle of wine, see where the evening takes us..."
            jump bangok_four_bryce4_bangnokay_rejection

label bangok_four_bryce4_bangnokay_rejection:
    Br stern "Oh, uh..."
    Br normal "I'm open to exploring whatever this is, but that's a bit of a jump."
    c "Wait, you weren't bringing up the fireworks as a way to lead into sex?"
    Br laugh "No, not at all. I was just thinking about the other night, trying to suss things out."
    c "I see."
    Br smirk "I don't hold it against you, though."
    Br "I'm not surprised you can't resist my pinnacle of masculinity."
    c "See, that right there sounds like an innuendo."
    Br laugh "Heck, I'm not too good at this."
    show bryce normal with dissolve
    jump b4jump

label bangok_four_bryce4_replaylabel:
    scene o2 at Pan((0, 250), (0, 250), 0.1)
    show black
    with dissolvemed
    play music "mx/shoal.ogg" fadein 2.0
    $ renpy.pause (1.0)
    Br laugh "You know, those fireworks are often a couple thing..."

    if bangok_four_common.bangnokay.check():
        show bryce laugh
        with dissolvemed
        c "I'm not surprised. They can set the mood for a romantic evening."
        jump bangok_four_bryce4_bangnokay
    $ renpy.pause (1.0)
    show brycerom at Pan ((500,0), (400, 300), 7.0) with fade
    $ renpy.pause (7.5)
    menu:
        "Reject.":
            c "Bryce, what are you doing?"
            hide brycerom
            show bryce brow
            with fade
            c "Is that what a romantic evening is for you?"
            Br laugh "Hey, we already had wine earlier, so I figured I'd speed up the process."
            c "Seriously, is this how you dragons date?"
            $ renpy.end_replay()
        "Accept.":
            jump bangok_four_bryce4_accept_return

label bangok_four_bryce4_intro:
    # c "No, that was fine. Don't stop."
    # Br flirty "Not something you've seen here before, huh?"
    # c "Not like that."
    # Br smirk "And then, especially with my kind, they are... Well, I think you can see what I mean."
    # c "Mmm-hmmm."
    # Br laugh "Do you just want to stand there and keep staring?"
    # c "No."
    # Br flirty "Then why don't you come a little closer?"
    # c "Alright."
    show bryce normal with dissolve
    m "I stepped closer, a little confused as he sat back down on the couch."
    c "What happened to going to the bedroom?"
    Br normal "Well, I don't want to get wine all over your bed."
    Br smirk "And I may be thinking of some very dumb places to put that bottle."
    play sound "fx/glassdown.wav"
    m "He gestured at the bottle with a hindleg as I set it on the coffee table, giving me another glimpse of his crotch in the process."
    Br flirty "That can wait, though. I've already shown you mine. You wanna get those clothes of yours out of the way?"
    menu:
        "That's a little forward.":
            $ renpy.pause (0.5)
            Br smirk "Says the one who stood in the doorway ogling my crotch for a while."
            c "You're the one who put it on display."
            Br laugh "Yeah, and you said you liked what you saw."
            c "I did."
            show bryce smirk with dissolve
            $ renpy.pause (0.5)
            play sound "fx/undress.ogg"
            m "Hesitantly, I stripped out of my shirt, then my pants, baring my body to Bryce."
        "I guess I can't say no to that.":
            $ renpy.pause (0.5)
            Br smirk "Good choice."
            $ renpy.pause (0.5)
            play sound "fx/undress.ogg"
            m "I stripped out of my shirt, then my pants, baring my body to Bryce."
    if bangok_four_playerhasdick is None:
        menu:
            m "My..."
            "My penis...":
                $ bangok_four_playerhasdick = True
            "My lower lips...":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick:
        m "My penis stiffened in anticipation, already thinking about what we might be about to do together."
        if bangok_four_bryce1_unplayed == True and bangok_four_bryce2_unplayed == True and bangok_four_bryce3_store.unplayed == True:
            Br smirk "Guessing you're a guy, then."
        else:
            Br laugh "Hello again, handsome."
    else:
        m "My lower lips throbbed in anticipation, already thinking about what we might be about to do together."
        if bangok_four_bryce1_unplayed == True and bangok_four_bryce2_unplayed == True and bangok_four_bryce3_store.unplayed == True:
            Br brow "Does something come out of that, or...?"
            c "No. It's not a slit for a penis."
            Br flirty "Oh."
        else:
            Br flirty "Damn, you look better with those off."

    c "Now who's ogling who?"
    show bryce flirty with dissolve
    m "Bryce shifted his hindquarters, definitely putting his own draconic member on display between his legs on purpose."
    Br flirty "I'm ogling you, of course."
    m "Even though sitting on it he filled most of the couch, I sank down to take a seat next to his head."
    c "I'm ogling you too."
    Br smirk "Good. I like that."
    m "His hot, wine flavored breath washed over me, his face scarcely an inch from mine."
    menu:
        "Kiss him.":
            play sound "fx/kiss.wav"
            hide bryce with fade
            m "I puckered my lips and pressed them to his."
            m "Rather than kiss back, though, Bryce stiffened and just let me plant my lips on him, until I pulled back."
            show bryce brow with dissolve
            c "Did I do something wrong?"
            Br laugh "No, no. You did nothing wrong. I just..."
            Br brow "Honestly, I'm a lot more familiar with the sexual side of things than lovey-dovey stuff."
            Br stern "Caught me off guard."
            $ renpy.pause (0.5)
            c "You don't need to be guarded with me."
            Br laugh "I'm literally responsible for your safety."
            show bryce normal with dissolve
            c "Right now, it's just you and me."
            m "I leaned in a bit."
            c "Want to try again?"
            Br smirk "Sure."
            hide bryce with fade
            m "This time, Bryce pushed against me, his lips pressing me back against the arm of the couch, and his supporting arm snaking around my back."
        "Lean into him.":
            pass
        "Fondle his thigh.":
            pass
        "Fondle his \"thigh\".":
            pass

label todo_out_of_content_bangok_four_bryce4:
    play sound "fx/system3.wav"
    s "Bryce4 Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")