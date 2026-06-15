init python in bangok_four_bryce4_store:
    unplayed = True

    moment_alone = None

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
    m "Bryce shifted his hindquarters, definitely putting his own draconic member on display between his hindlegs on purpose."
    Br flirty "I'm ogling you, of course."
    m "Even though he filled most of the couch sitting on it, I sank down to take a seat next to his front end."
    c "I'm ogling you too."
    Br smirk "Good. I like that."
    m "His hot, wine flavored breath washed over me, his face so very close to mine."
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
            m "This time, Bryce pushed against me, his lips pressing me back against the arm of the couch, and his supporting foreleg snaking around my back."
            m "I didn't have room to pull away, if I'd even wanted to, as his scaly lips parted, our mouths interlocking as his tongue pushed into mine."
            m "It was a sloppy kiss, maybe even drunken as I tasted the wine from his mouth. But it was also all the passion I could want."
            show bryce flirty with fade
            m "I had to tap out for air, finally breaking our intertwining. He still kept his snout just a handsbreadth from mine."
            Br smirk "Better?"
            m "My knees pulled a little together, trying to deal with all the bloodflow going south to my groin."
            c "Way better."
        "Lean into him.":
            m "Nestling my head under his chin, I leaned into him, feeling my bare skin against his scaly neck, his breath warm against my shoulder."
            m "He wrapped his foreleg around my waist, pulling me in even closer."
            Br normal "I, uh... not sure what position we're moving to, here."
            c "Cuddling."
            label bangok_four_bryce4_intro_cuddle_jump:
            Br laugh "Oh, okay."
            show bryce smirk with dissolve
            $ renpy.pause (0.5)
            play sound "fx/undress.ogg"
            show black with dissolve
            m "Abruptly, Bryce lifted himself forward, slumping more of his body on top of mine, pinning me against the arm of the couch."
            c "H-Hey!"
            m "His chuckle reverberated through my body as he settled on top of me."
            Br laugh "Pretty sure when we were sharing the couch, we cuddled a lot closer to this."
            m "I exhaled, feeling his belly plates all down my upper body, his scales warming to my skin rapidly."
            Br flirty "But now that your clothes aren't in the way..."
            if bangok_four_playerhasdick:
                m "His forepaw around my body shifted, letting one of his claws ghost up the underside of my hard manhood."
            else:
                m "His forepaw around my body shifted, letting one of his claws ghost up my thigh to rub my wet slit."
            m "I couldn't help but shiver, feeling him touching me there."
        "Fondle his thigh.":
            m "I pulled one of his forelegs up into my lap, not minding in the slightest as he slipped another behind my back."
            m "I ran my hand up and down his thigh, feeling the scales and muscles beneath."
            if bangok_four_bryce2_unplayed == False:
                Br flirty "Thinking about the last time you went fondling my legs?"
                c "I might've been."
                Br smirk "Well, if that's where you want to go, I'm not going to stop you."
            Br flirty "You like some big strong legs, huh?"
            menu:
                "All of you is big and strong.":
                    $ renpy.pause (0.5)
                "I won't deny it.":
                    $ renpy.pause (0.5)
                "Maybe I just wanted a nice cuddle?":
                    $ renpy.pause (0.5)
                    jump bangok_four_bryce4_intro_cuddle_jump
            m "Bryce's hindquarters shifted uncomfortably."
            Br smirk "Can't wait to show you just how big some parts can be."
        "Fondle his \"thigh\".":
            m "I leaned in at an angle that, at first, might've been mistaken for a hug."
            m "But, as I ran my hand down over his underbelly, toward his hindquarters, I was quite sure he knew where I was going."
            m "I could feel his breath hitch as I wrapped my hand around his member, finding it slick, hot, and ready."
            Br laugh "H-Hey, okay. We're both on the same page, but you don't have to climb over my back to get there."
            m "Moving a foreleg around my waist, he shifted me back onto my seat on the couch."

    play sound "fx/boxdive.ogg"
    show bryce laugh with dissolve
    m "Then Bryce hopped up, member bobbing as he bumped the coffee table in the process."
    Br normal "I don't think we're going to get far without lube, though."
    Br smirk "Don't say anything. I may or may not have stashed something outside your bedroom window."
    hide bryce with dissolve
    if bangok_four_bryce3_store.unplayed == False:
        c "(Of course he did.)"

    # TODO: Possibly add options for the player to do without Bryce, e.g. masturbate, wonder how Bryce knew the player's bedroom, etc.

    show bryce smirk with dissolve
    m "Bryce returned rapidly, carrying a basket in his mouth full of what looked like condom packages and a couple different bottles of lube."
    if bangok_four_bryce3_store.unplayed == False:
        m "Some sand clung to the bottom, telling me it was the same basket from the BBQ."
    else:
        m "Some bits of sand clung to the bottom, telling me he had been outside someplace."

    m "He set the basket down on the coffee table, next to the still-sealed wine bottle, then shot me a wink."





label todo_out_of_content_bangok_four_bryce4:
    play sound "fx/system3.wav"
    s "Bryce4 Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")