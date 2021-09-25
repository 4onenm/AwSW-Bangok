# Flags used:
#  persistent.bangok_inflation - Inflation
#  persistent.bangok_knot - Knotting
#  persistent.bangok_rimming - Rimming
#  persistent.bangok_watersports - Watersports




label bangok_four_bryce1_ws_conversation:
    Br stern dk "Mmh."
    Br "There's something I need to ask you before you start that."
    c "Huh?"
    Br "All that drinking earlier means I kinda gotta {i}go{/i}."
    if bangok_four_bryce1_playercame == True:
        Br smirk dk "Just like you did."
    Br brow dk "Does that... matter to you at all?"
    menu:
        "Go take care of your business.":
            $ brycemood -= 1
            Br brow dk "Alright."
            label bangok_four_bryce1_ws_emptying_the_tank:
            hide bryce with dissolve
            play sound "fx/door/door_open.wav"
            $ renpy.pause (2.0)
            m "You sit, naked, on a dragon's couch, holding a bottle of lube."
            $ renpy.pause (3.0)
            c "(Maybe I should have said something else? I don't know why I'm still thinking about it...)"
            $ renpy.pause (3.0)
            play sound "fx/door/doorclose3.wav"
            show bryce normal dk with dissolve
            $ renpy.pause (0.5)
            Br flirty dk "Where were we?"
        "I might be interested.":
            Br smirk dk "Before or after I blow?"
            menu:
                "Shower me.":
                    show bryce stern dk with dissolve
                    $ renpy.pause(0.5)
                    Br "Uh, no. Can't do that one."
                    c "Why not?"
                    Br brow dk "You're {i}already{/i} going to reek of me and alcohol. Not even sure an actual shower will get that off. Are you gonna be a good ambassador if they can smell urine on you, too?"
                    c "..."
                    Br stern dk "Nothing outside tonight."
                    c "Fine."
                    menu:
                        "Before.":
                            $ bangok_four_bryce1_wstiming = "before"
                        "After.":
                            $ bangok_four_bryce1_wstiming = "after"
                        "Not interested anymore.":
                            $ brycemood -= 1
                            Br "If you say so. Let me go get it out, then."
                            jump bangok_four_bryce1_ws_emptying_the_tank
                "Before.":
                    $ bangok_four_bryce1_wstiming = "before"
                "After.":
                    $ bangok_four_bryce1_wstiming = "after"
            Br flirty dk "You got it."
    return

label bangok_four_bryce1_poke:
    m "In falling asleep, Bryce had slumped over partly on his side, giving me a better look underneath him than I've had so far."
    c "(Huh. Is there nothing there?)"
    m "Curiosity getting the better of me, I nudged one of Bryce's hindlegs aside, getting a closer look."
    m "Between his legs, the plates separated just slightly over a horizontal slit. As my hand brushed it, Bryce began to stir."
    show bryce stern with dissolve
    $ renpy.pause(0.3)
    if brycemood > 6:
        Br flirty "Was that what I thought it was?"
        Br smirk "I wasn't sure you--"
        show bryce stern with dissolve
        $ renpy.pause(0.4)
        Br "Ugh... Where are we?"
        c "Still in the bar."
        Br brow "And you were...?"
    elif brycemood < 1:
        Br "What was that?"
        c "Uh..."
        Br brow "I felt that. What were you just doing?"
    else:
        Br brow "Ugh... Where are we?"
        c "Still in the bar."
        c "Come on. Let's get you home."
        jump bangok_four_bryce1_apartment

    menu:
        "Nothing.":
            $ brycemood -= 3
            if brycemood > 3:
                Br stern "I'll have to take your word on that."
                c "Let me just help you home."
                Br brow "..."
                Br stern "Yeah, okay. I could use a hand."
                jump bangok_four_bryce1_apartment
            else:
                Br stern "The {i}fuck{/i} you were."
                c "..."
                Br "I think I can... find my own way. You should go."
                c "..."
                scene black with dissolvemed
                stop music fadeout 1.0
                $ brycestatus = "bad"
                $ leftbryce = True
                $ brycescenesfinished = 1
                jump _mod_fixjmp
        "I was just curious.":
            $ brycemood -= 2
            c "I haven't seen exactly what dragon... you know. Looks like."
            Br "..."
            c "On humans it kinda hangs out. I was just looking for..."
            Br "..."
            c "..."
            if brycemood > 4:
                Br "If I showed you, would you be interested in...{w=1.2}{nw}"
                Br flirty "If I showed you, would you be interested in{fast} trying it out?"
                menu:
                    "Accept.":
                        $ brycemood += 2
                        show bryce smirk with dissolve
                        show zhong shy b flip at left with easeinleft
                        Wr "Please, not in here. I have enough to clean as it stands."
                        Br normal "If you say so."
                        show zhong shy b
                        $ renpy.pause (0.3)
                        hide zhong with easeoutleft
                        Br flirty "I {i}think{/i} my place is closer, [player_name]."
                        c "Lead on."
                        jump bangok_four_bryce1_apartment_decided
                    "Reject.":
                        $ brycemood -= 2
                        Br stern "In that case, talk to one of the biologists at the production facility. Let me just..."
                        play sound "fx/chair.wav"
                        $ renpy.pause(1.5)
                        Br "..."
                        c "I'll help you walk home."
                        $ renpy.pause(0.5)
                        Br normal "Thanks."
                        jump bangok_four_bryce1_nevermind
        "What you think.":
            if brycemood < 6:
                Br stern "Then you should leave."
                c "..."
                Br "Now."
                scene black with dissolvemed
                stop music fadeout 1.0
                $ brycestatus = "bad"
                $ leftbryce = True
                $ brycescenesfinished = 1
                jump _mod_fixjmp
            else:
                Br smirk "I see."
                Br flirty "How about we try that again with me awake, at my place?"
                c "Sure."
                jump bangok_four_bryce1_apartment_decided







label bangok_four_bryce1_apartment:
    scene black with dissolvemed
    $ renpy.pause (0.6)
    scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0) with dissolvemed
    $ renpy.pause (0.5)
    show bryce normal dk with dissolve
    m "Inside Bryce's dark apartment, the big dragon made a beeline for his couch."
    menu:
        "[[Interrupt him.]":
            pass
        "[[Go home.]":
            m "I didn't make it to the door."
            c "(No... think I'll just lie down here.)"
            jump bangok_four_bryce1_nevermind
    c "Bryce?"
    Br brow dk "Mmh?"
    menu:
        "Nevermind.":
            c "(So... tired.)"
            m "I didn't make it to the door to leave."
            jump bangok_four_bryce1_nevermind
        "Want to do something stupid?":
            c "You're drunk. I'm drunk. And you're... very attractive."
            c "What do you say?"
            $ renpy.pause (0.4)
            if brycemood < 5:
                play sound "fx/cartslide.ogg"
                hide bryce with dissolve
                m "By the time I finished asking the question, Bryce was already fast asleep on his couch."
                m "I gave up and turned for the door, then lost what little energy I had."
                c "(Maybe... I'll just sleep here.)"
                jump bangok_four_bryce1_nevermind
            else:
                pass

    Br flirty dk "Alright. Fuck it. You're cute too."
    $ brycemood = 4

    if False:
        label bangok_four_bryce1_apartment_decided:
        scene black with dissolvemed
        $ renpy.pause (0.6)
        scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0) with dissolvemed
        $ renpy.pause (0.5)
        show bryce flirty dk with dissolve
    $ persistent.bangok_watersports = True
    $ persistent.bangok_inflation = True
    $ persistent.bangok_knot = True

    play sound "fx/undress.ogg"
    m "I struggled out of my clothes as fast as my lust-drunk state would allow."
    if bangok_four_firsttime == True:
        c "(Is this really happening? Am I really going to fuck a dragon?)"
    show bryce at Position(ypos=1.1) with ease
    m "Bryce rolled his lower body onto its side, revealing the worryingly large shaft emerging between his legs."
    c "Huh. Guess you don't get whiskey dick."
    Br brow dk "What's that?"
    c "It's where alcohol makes it hard to... stay hard."
    Br "It's always hard."
    c "Huh."
    Br smirk dk "That's mine. Now show me yours."
    menu:
        "Show him your dick.":
            jump bangok_four_bryce1_m
        "Show him your lack of dick.":
            scene black with None
            play sound "fx/system3.wav"
            s "Sorry ladies! 4onen isn't one and has no clue how to write this for you."
            $ renpy.error("InvalidWriterGenderError: Male writers writing for female receivers aren't great.")

label bangok_four_bryce1_m:
    show bryce brow dk with dissolve
    $ renpy.pause(0.9)
    m "Bryce didn't look impressed."
    c "You're like twice my size. Of course you're bigger."
    Br "No, no. I get that. What's that underneath?"
    c "Hm? {w=0.8}Oh, balls. That's where the sperm comes from."
    Br smirk dk "They just hang out like that? Undefended? Under that limp shaft?"
    c "Yeah. Though, uh, not s'posed to be limp right now. Whiskey dick, I guess."
    $ renpy.pause(0.5)
    Br flirty dk "Are your balls sensitive?"
    c "... Not sure I like where this is going."
    show bryce at Position(ypos=1.3) with ease
    show bryce at Position(ypos=1.5) with ease
    m "Bryce stumbled a little closer, tongue out with a wide-grinned wink."
    menu:
        "[[Let him.]":
            pass
        "Watch the horns!":
            c "I'm kinda delicate!"
            Br smirk dk "I'll be careful."
        "[[Stop him.]":
            m "I took a step back and Bryce abruptly stopped."
            show bryce at center with ease
            c "{i}Really{/i} sensitive. I don't think it's a good idea if you..."
            show bryce normal dk with dissolve
            show bryce at Position(ypos=1.3) with ease
            $ renpy.pause(0.4)
            show bryce at center with ease
            Br smirk dk "Alright."
            jump bangok_four_bryce1_m2

    show bryce flirty dk with dissolve
    m "Bryce's hot, alcohol-tinged breath sent shivers through my groin.{w=0.3} Bypassing my man-meat, he wrapped his tongue around the base of my sack and tugged experimentally."
    m "Having that much bumpy tongue running over my balls was such a new and different experience, my shaft jumped to attention immediately, bopping his snout."
    show bryce smirk dk at Position(ypos=1.3) with ease
    Br flirty dk "Now you're hard."
    c "Yep. That, ah, that was new."
    Br laugh dk "New for me too!"
    show bryce normal dk with dissolve
    show bryce at center with ease
    Br normal dk "Never seen things... outside like that. Skin tastes weird too."
    c "Good weird or bad weird?"
    Br brow dk "Different."

label bangok_four_bryce1_m2:
    Br normal dk "What next? You want me on top? Or do you want to stick that little thing in me?"
    $ bangok_four_bryce1_m2_size = True
    $ bangok_four_bryce1_m2_fit = True
    label bangok_four_bryce1_m2_menu:
    menu:
        "I want to taste you.":
            $ bangok_four_bryce1_position = "oralbot"
            label bangok_four_bryce1_oralbot_merge:
            Br smirk dk "Would you, now?"
            play sound "fx/cartslide.ogg"
            show bryce normal dk at Position(xpos=0.4,xanchor='center') with dissolve
            show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
            m "Bryce settled back on the couch, bunching the rug and tugging the coffee table as his tail caught for a moment."
            m "He splayed one hindleg out, giving me easy access to his shaft from beside the couch."
            Br flirty dk "Come on over."
            if bangok_four_bryce1_protected == False and not bangok_four_bryce1_playercame:
                m "My addled brain managed to push through an important thought before I followed his order."
                c "Wait, what about protection?"
                Br brow dk "You're kidding, right? Kids don't happen from oral. And we're both guys."
                Br smirk dk "Unless there's something about humans I'm not understanding."
                c "No, it's basically like that."
                Br "Then what's the problem?"
                menu:
                    "[[Insist.]":
                        c "We don't know what your stuff might do to me."
                        if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                            c "I've seen a health aisle. You've got condoms."
                        else:
                            c "Your kind has condoms, right?"
                        show bryce stern dk with dissolve
                        m "Bryce groaned, then gestured at a chest of drawers in a corner."
                        Br "Top. I think. Just hurry up."
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.ogg"
                        m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one labeled safe for oral, then dug a little deeper for one my size, in case things went further."
                        m "Only after I dug to the bottom did I finally find a box of condoms closer to my scale, unopened."
                        m "Tearing into the packaging, I returned with the necessary equipment."
                    "[[Drink from the tap.]":
                        $ bangok_four_bryce1_protected = False
                        c "There isn't one, I guess."

            if bangok_four_bryce1_protected:
                m "I knelt next to bryce, feeling saliva building up in my mouth as I unrolled rubbery safety along his shaft."
                Br flirty dk "D-Damn. That's kinda teasing. Your hands are really smooth."
                $ brycemood += 1
            else:
                m "I knelt next to Bryce, feeling saliva building up in my mouth from the anticipation."

            $ renpy.error("TODO: Player kneeling beside until Bryce gets close and asks for 69, unless player already came from something else.")


        "I want you in me.":
            $ bangok_four_bryce1_position = "analbot"
            label bangok_four_bryce1_analbot:
            Br brow dk "We can try. But, ah, where? I didn't see anything behind your \"balls\" when I was down there looking."
            c "It's further back. Here."
            scene bangok_four_bryce1_apartment night ceiling at Pan((0,360), (0,0), 2.0) with dissolve
            m "I lay down on Bryce's couch, lifting my legs to give him a better look."
            show bangok_four_bryce_underside_large dk flip at Position(yanchor='top',ypos=0.8) with dissolve
            Br "Huh. So it is."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.6) with ease
            Br flirty dk "Can't say I've ever seen that before."
            scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
            show bryce normal dk at Position(ypos=1.1)
            with dissolve
            m "Moving back to let me sit up, Bryce handed me a bottle of lube."
            Br "If you think it'll fit. But it definitely won't without plenty of this."
            c "Right."
            if persistent.bangok_watersports == True:
                call bangok_four_bryce1_ws_conversation from bangok_four_bryce1_analbot_ws_conversation
            if bangok_four_bryce1_protected == False and not bangok_four_bryce1_playercame:
                m "Before I knelt down to start applying the lube to his cock, my addled brain pushed through an important thought."
                c "Oh, I almost forgot protection."
                Br stern dk "Is that really necessary?"
                if bangok_four_bryce1_wstiming is not None:
                    Br smirk dk "I thought you wanted my fluids inside you."
                    Br brow dk "Besides, we're both guys. Kids aren't happening."
                else:
                    Br "We're both guys. Kids aren't happening."
                Br brow dk "Unless there's something about humans I really don't understand."
                menu:
                    "[[Insist.]":
                        $ brycemood -= 1
                        $ bangok_four_bryce1_protected = True
                        c "We don't know what your fluids might do to me."
                        show bryce stern dk with dissolve
                        m "Bryce groaned, then gestured to a nearby chest of drawers."
                        Br "Top, I think. Just hurry up."
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.ogg"
                        m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one, then dug a little deeper for one my size, in case things went further."
                        m "Only after I dug to the bottom did I finally find a box of condoms closer to my scale, unopened."
                        m "Tearing into the packaging, I returned with the necessary equipment."
                    "[[Take his load.]":
                        $ bangok_four_bryce1_protected = False
                        c "Fair point."
            show bryce at center with ease
            if bangok_four_bryce1_protected == True:
                m "I knelt in front of Bryce, unrolling the condom along his impressive length, before spurting a healthy dose of lube along the top."
            else:
                m "I knelt in front of Bryce, spurting a healthy dose of lube along the top of his impressive length."
            show bryce smirk dk with dissolve
            play soundloop "fx/massage.ogg"
            m "Setting the bottle down, I spread the lube over and around his shaft, trying to make sure everything was fully covered, while also pushing a large dollop up toward the tip to help with entry."
            Br stern dk "D-Damn your hands are soft."
            stop soundloop fadeout 1.0
            c "That should do it."
            scene bangok_four_bryce1_apartment night ceiling at Pan((0,360), (0,0), 2.0) with dissolve
            m "Anticipating what would come next, I lay back down on Bryce's couch, tossing one leg over the seatback and spreading the other away as far as I could."
            m "One of my still lube-covered hands, I rubbed over my asshole, both as a tease and to help prep the site."
            show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=0.6) with easeinbottom
            $ renpy.pause(0.8)
            Br stern dk "You're sure about this?"
            c "Yep."
            Br brow dk "You'll tell me if anything hurts? Anything feels off?"
            c "Mhmm."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.6) with ease
            Br flirty dk "Then give me a second to figure out how to aim."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
            m "Bryce clambered overtop me, hindlegs still on the floor while he braced his forelegs against the couch. The warmth radiating off his underbelly suffused my naked skin."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
            m "The cold lube on the tip of his cock bumped up against my thighs, then slapped my balls as he tried to find my asshole."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.8) with ease
            Br stern dk "Why is this so damn difficult?"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.85) with ease
            m "Following my inner thighs, he managed to get his rigid cock nestled in my taint."
            c "Close."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
            m "He pushed and I yelped, the delicate patch of skin between my balls and ass pressing inward."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.8) with ease
            Br brow dk "You alright? What happened?"
            c "Lower. Lower than that."
            Br laugh dk "If it's so small I can't find it, how am I gonna fit?"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.85) with ease
            m "He gave it another try, the tip of his shaft bouncing lewdly off one of my cheeks."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.82) with ease
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
            m "Grabbing hold, I guided him the remaining short distance, until his tip was applying just a little pressure to my rosebud."
            Br smirk dk "Ready?"
            $ renpy.pause (0.3)
            c "Yeah."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.98) with ease
            m "The large amount of lube we'd applied was the only way he was able to enter. My ass stretched wide, just short of the point of pain as he pressed just his tip in."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.0) with ease
            m "When my ring made it past the head and his width decreased slightly, I gasped."
            m "Bryce froze immediately."
            Br brow dk "Problem?"
            c "N-No. It's..."
            $ renpy.pause (1.2)
            Br flirty dk "Want some more?"
            m "I nodded, at a loss for words."
            show bangok_four_bryce_underside_large:
                ease 4.0 ypos (-2.2)
            $ renpy.pause (4.0)
            m "Bryce sank in slowly, showing the uptmost care despite our shared inebriation. The plates on his belly scraped past my own penis, the harsh stimulation adding yet more to the experience."
            m "As the warm scales on his legs pressed up against my skin, I squirmed to try to part my own legs further, get that little big closer to take him fully."
            Br laugh dk "So tight!"
            c "Y- You're so big!"
            Br flirty dk "I hear that a lot."
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                play soundloop ["fx/faucet1.ogg", "fx/faucet2.ogg"]
                if bangok_four_bryce1_protected == True:
                    m "Suddenly, I felt a warmth blossoming in my guts, along with the stretching of the condom's reservoir, spreading out from where I thought his tip might be."
                else:
                    m "Suddenly, I felt a warmth blossoming in my guts, spreading out from where I thought his tip might be."
                $ renpy.pause(0.5)
                Br laugh dk "Ah... there we go."
                if bangok_four_bryce1_protected == True:
                    m "I squirmed a little more, turned on as Bryce used the condom in my ass as a urinal."
                else:
                    m "I squirmed a little more, turned on as Bryce used my ass as a urinal."
                stop soundloop fadeout 1.5
                $ renpy.pause(0.8)
                Br flirty dk "Might not have taken a piss since the shift started at the station. Hope you don't mind."
                $ renpy.pause(0.8)
                Br flirty dk "How was that?"
                c "Mmh."
                $ renpy.pause(1.0)
            Br smirk dk "How's that size now?"
            m "Near his base was almost as wide as at his tip, spreading me open on his lovemaking."
            if persistent.bangok_knot == True:
                m "I could feel a little bit of something extra near the base, in the way his shaft's skin moved as my sphincter spasmed around it."
            menu:
                "[[Uninteligible.]":
                    pass
                "So full...":
                    pass
                "Love it.":
                    pass
                "Think I've had bigger.":
                    $ brycemood += 1
                    play sound "fx/tableslap.wav"
                    Br laugh dk "Have you?"
                    m "His laughter reverberated through where our bodies met, tingling in my innards."
                    Br smirk dk "Then I guess you won't mind if we get moving."
            show bangok_four_bryce_underside_large:
                ease 3.5 ypos (-2.05)
            m "Bryce tugged back just as slowly as he'd entered, keeping the lube even on his shaft, and my speared ass from feeling any significant shocks."
            m "He stopped at his tip, waiting again."
            menu:
                "E-Easy.":
                    Br brow dk "I'm taking this as slowly as I can."
                    c "Just another few slow ones. Still getting used to you."
                    $ renpy.pause(0.3)
                    show bangok_four_bryce_underside_large:
                        ease 4.0 ypos (-2.2)
                        pause 0.5
                        ease 4.0 ypos (-2.05)
                        pause 0.3
                        repeat
                    m "Bryce did as I'd asked, giving me a few more slow cycles of fullness and emptiness."
                    show bangok_four_bryce_underside_large:
                        ease 4.0 ypos (-2.2)
                    m "I writhed around the large shaft, all but losing myself in the sensations until he stopped again, hilted as deep as he'd managed to go."
                    label bangok_four_bryce1_analbot_adaptation:
                    Br smirk dk "How is it?"
                    menu:
                        "Still adapting.":
                            $ renpy.pause(0.3)
                            show bangok_four_bryce_underside_large:
                                ease 3.5 ypos (-2.05)
                                ease 3.5 ypos (-2.2)
                                ease 3.5 ypos (-2.05)
                                ease 3.5 ypos (-2.2)
                            $ renpy.pause(14.0)
                            jump bangok_four_bryce1_analbot_adaptation
                        "{i}More.{/i}":
                            pass
                    $ renpy.pause(0.5)
                    Br smirk dk "Give me a sec."
                    m "Rather than pick up the pace, he spent a long, slow moment dragging his cock back out of my depths."
                    show bangok_four_bryce_underside_large:
                        ease 5.0 ypos (-2.0)
                    $ renpy.pause (5.0)
                    m "As he did, he twitched his cock along the way, eventually finding that one pleasure button deep inside me."
                    show bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,30), 0.5)
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.05)
                    with ease
                    m "I bucked my hips, almost popping the tip free."
                    Br flirty dk "So that's what that was."
                    m "I moaned appreciatively."
                    Br smirk dk "Okay. Here we go."
                    $ renpy.pause(0.3)
                "Oh fuck me already.":
                    $ brycemood += 1
                    show bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,30), 0.5)
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.05)
                    with ease
                    m "I thrust my ass back against his cock, taking back a little bit he'd taken away."
                    Br flirty dk "If you say so."

            play soundloop "fx/rub2.ogg" fadein 1.0
            show bangok_four_bryce_underside_large:
                ease 0.5 ypos (-2.15)
                ease 0.7 ypos (-2.1)
                repeat
            m "Bryce began to fuck me for real, sliding in and out, in and out with movements that spread me wide each way."
            $ renpy.pause(3.0)
            m "It didn't take long before we were both emitting undignified noises."
            $ renpy.pause(0.9)
            if persistent.bangok_knot == True:
                Br stern dk "In or out?"
                c "H-Huh?"
                Br brow dk "The knot! In or out?"
                $ renpy.pause(0.5)
                menu:
                    "Y-You have a {i}knot{/i}?!":
                        $ bangok_four_bryce1_analknot = "inoops"
                    "In!":
                        $ brycemood += 1
                        $ bangok_four_bryce1_analknot = "in"
                    "Out!":
                        $ bangok_four_bryce1_analknot = "out"
            else:
                Br stern dk "Not... Long..."
            stop soundloop fadeout 1.0
            play sound "fx/snarl.ogg"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.15) with ease
            if not persistent.bangok_knot or (persistent.bangok_knot and bangok_four_bryce1_analknot != "out"):
                if bangok_four_bryce1_protected == True:
                    m "Bryce came, prying my legs further apart as he forced our hips together, hilting me to fill his condom inside."
                else:
                    m "Bryce came, prying my legs further apart as he forced our hips together, hilting inside me to coat my insides white."
            else:
                if bangok_four_bryce1_protected == True:
                    m "Bryce came, prying my legs further apart as he jerked to a stop, coming a few inches short of hilting while he filled his condom inside me."
                else:
                    m "Bryce came, prying my legs further apart as he jerked to a stop, coming a few inches short of hilting while he coated my insides white."

            if not bangok_four_bryce1_playercame:
                $ bangok_four_bryce1_playercame = True
                m "The twitching of his spurting cock pressed up against the pleasure button inside me. Before I could form coherent words, I, too, was over my edge and cumming onto both our chests."
            else:
                m "The twitching of his spurting cock pressed up against the pleasure button inside me, the overstimulation after my recent orgasm leaving me writing."

            if persistent.bangok_inflation == True:
                m "Even after I was done, though, Bryce had a few spurts left in him."
                if bangok_four_bryce1_protected == True:
                    m "I realized with some alarm that I was feeling the condom continuing to bloat inside of me, pressing deeper down my canals into my guts."
                else:
                    m "I realized with some alarm that I was feeling {i}very{/i} full."
                c "B-Bryce!"
                Br flirty dk "A-Almost..."
                m "Looking down, I found my belly was visually slightly larger than it should be."

            $ renpy.pause(0.8)
            show bangok_four_bryce_underside_large:
                ease 1.0 ypos -2.0
                ease 1.0 ypos -1.7
                ease 1.0 ypos -1.3
                ease 1.0 ypos -0.7
            m "After a long moment cumming inside of me, Bryce worked his way back with his forelegs, keeping his hips and cock where they were as he curled over to look down at me."

            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                if bangok_four_bryce1_protected == True:
                    play sound "fx/bubbles.ogg"
                    m "The dam inside me burst, Bryce's cumload just a little more than the condom could take after his pissing in me."
                    m "Warmth suffused my insides, bubbling and sloshing as it spread to equilibrium within my guts, no longer contained."
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
                Br flirty dk "Ready for part two?"
                if persistent.bangok_inflation == True:
                    c "Uh."
                else:
                    c "Mhmm."
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
                m "With a grunt, Bryce leaned forward, then his cock twitched inside me again. A new, less viscous warmth began spreading in my guts."
                play soundloop ["fx/faucet1.ogg", "fx/faucet2.ogg"]
                Br laugh dk "Ahhh..."
                if persistent.bangok_inflation == True:
                    if bangok_four_bryce1_protected == True:
                        play sound "fx/bubbles.ogg"
                        m "The dam inside me burst, Bryce's additional pissload just a little more than the condom could take."
                    m "I moaned, suffused with the feeling of fluid bubbling and sloshing within my innards to make room as yet more was drained in."
                    
                    stop soundloop fadeout 1.5
                    if bangok_four_bryce1_protected == True:
                        m "My belly pressed up against his, visibly rotund for all to see with Bryce's cum and piss as he used my guts like a urinal, my protection stripped away."
                    else:
                        m "My belly pressed up against his, visibly rotund for all to see with Bryce's cum and piss as he used me like a urinal."
                else:
                    if bangok_four_bryce1_protected == True:
                        m "I lay, breathing evening out, contented as Bryce used the condom inside me as a urinal."
                    else:
                        m "I lay, breathing evening out, contented as Bryce used my innards as a urinal."
                m "When he worked his way back down to eye level with me, I could almost hear the sloshing from all his fluids."
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.7) with ease
                Br flirty dk "Might not have taken a piss since the shift started at the station. Hope you don't mind."

            if persistent.bangok_inflation == True:
                m "He rubbed my protruding belly with a paw."
                Br flirty dk "Sure did fill you up, huh?"
                m "I couldn't answer as I lay basking under the warm fluid result of our coitus."

            
            if persistent.bangok_watersports and persistent.bangok_inflation and bangok_four_bryce1_protected:
                $ brycemood += 1
                Br flirty dk "Mm. I think the condom broke."
                menu:
                    "Obviously!":
                        $ brycemood -= 2
                        Br "I didn't exactly have control over it's integrity."
                        c "Not pissing in it could've saved it."
                        Br "And who said they were okay with that?"
                    "Damn.":
                        Br "Yeah, sorry."
                        Br flirty dk "Good fuck, though?"
                        m "I nodded."
                    "That felt kinda good...":
                        Br "Did it?"
            else:
                Br flirty dk "Good?"
                m "I nodded."
            # menu:
            #     "[[Nod.]":
            #         pass
            #     ""
            #     "T-Too much." if persistent.bangok_inflation:
            #         $ brycemood -= 1
            #         Br flirty dk "You knew what you were getting yourself into."
            if persistent.bangok_knot == True and bangok_four_bryce1_analknot != "out":
                Br flirty dk "I hope you liked it, 'cause I don't think your ass will stretch to let the knot back out anytime soon."
                if bangok_four_bryce1_analknot == "inoops":
                    $ brycemood -= 1
                    c "What?!"
                    scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
                    show bryce brow dk
                    with dissolvemed
                    play sound "fx/sheets.ogg"
                    m "He backed off further, giving me room to get up on my elbows."
                    $ renpy.pause(0.5)
                    Br "I didn't exactly have a lot of time or room for thought, and you were being unclear."
                    menu:
                        "I didn't even know you had a knot!":
                            $ brycemood -= 1
                            Br stern dk "You're interacting with another species, and didn't think to check a basic fact like this?"
                        "You should have left it ouside, then!":
                            $ brycemood -= 2
                        "It's okay.":
                            c "It was a misunderstanding. And as misunderstandings go, there are worse ones."
                            Br normal dk "Not much to be done about it now. We might as well sleep it off."
                            jump bangok_four_bryce1_tiedsleep
                    Br stern dk "Not much to be done about it now. We might as well sleep it off."
                    
                    if persistent.bangok_watersports == True:
                        c "That's easy for you to say, without an ass stuffed full of dragon cum, piss, and cock."
                    else:
                        c "That's easy for you to say, without an ass stuffed full of dragon dick and cum."


            
                label bangok_four_bryce1_tiedsleep:
                scene black with dissolveslow
                m "Bryce slumped on top of me on the couch, unable to do much else with our hips tied together."
                if brycemood >= 0:
                    Br "Goodnight, [player_name]."
                else:
                    Br stern dk "I wish we didn't have to sleep like this as much as you do."
                    c "Fuck you."
                    Br "You already did."
                jump bangok_four_bryce1_morningcouch
            else:
                if brycemood < 0:
                    jump bangok_four_bryce1_analbot_pullout
                else:
                    Br "Want me to pull out? Or do you want to sleep like this?"
                    menu:
                        "Sleep like this.":
                            $ brycemood += 1
                            scene black with dissolveslow
                            m "Bryce slumped on top of me on the couch, taking care to shift me to the edge so he wouldn't crush me."
                            if persistent.bangok_knot == True:
                                m "He adjusted his hips too, pressing the bulge of his knot up against my ass to help prevent leaks."
                            Br smirk dk "Goodnight, [player_name]."
                            jump bangok_four_bryce1_morningcouch
                        "Pull out.":
                            label bangok_four_bryce1_analbot_pullout:
                            scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
                            show bryce stern dk
                            with dissolvemed
                            if (persistent.bangok_watersports and persistent.bangok_inflation and bangok_four_bryce1_protected) or not bangok_four_bryce1_protected:
                                # Broken condom or no condom
                                play sound ["fx/slide.ogg","fx/spray.ogg"] fadein 0.5
                                m "Bryce tugged himself free, a small cascade of our fluid lovemaking spattering the ground by the edge of his couch."
                                # if persistent.bangok_rimming == True:
                                #     Br "Mind if I sample some of our results?"
                                #     c "How, exactly?"
                                #     Br "You've seen my tongue. Figure it out."
                                #     c "Alright."
                            elif persistent.bangok_inflation:
                                # FULL condom
                                play sound "fx/slide.ogg" fadein 0.5
                                m "Bryce tugged, but couldn't drag the condom's inflated reservoir through my guts."
                                Br stern dk "Damn. There's that size difference again."
                                c "Maybe if I push?"
                                Br brow dk "Let me get a little more of the condom out first."
                                play sound "fx/pour.ogg"
                                $ renpy.pause(3.0)
                                m "I could feel the fluid draining from my guts inside the condom, through my stretched asshole and into the part Bryce had gotten outside."
                                play sound "fx/uncork.ogg"
                                m "The last little bit popped free with a rush of air that left my guts feeling deflated and empty."
                            else:
                                # Regular used condom
                                play sound ["fx/slide.ogg","fx/uncork.ogg"] fadein 0.5
                                if persistent.bangok_watersports:
                                    m "Bryce tugged himself free, the blob of cum and piss he'd deposited in the condom's reservoir coming free with a satisfying pop."
                                else:
                                    m "Bryce tugged himself free, the blob of cum he'd deposited in the condom's reservoir coming free with a satisfying pop."
                    if brycemood < 0:
                        Br stern dk "Floor's open. Or you can find your way home like that."
                        m "I struggled even to get off the couch, my ass complaining loudly at every movement."
                        c "Floor is good..."
                        play sound "fx/impact3.ogg"
                        scene black with vpunch
                        jump bangok_four_bryce1_morningfloor
                    else:
                        Br normal dk "You want to stay on the couch there?"
                        m "I nodded."
                        c "Not sure I can move after that. Damn."
                        Br flirty dk "Well, I'm about ready to pass out."
                        Br "Goodnight, [player_name]."
                        c "'night."
                        jump bangok_four_bryce1_morningbed










        "I want to stick it in you.":
            $ bangok_four_bryce1_position = "cloacatop"
            Br flirty dk "Fine by me."
            play sound "fx/cartslide.ogg"
            show bryce normal dk at Position(xpos=0.4,xanchor='center') with ease
            show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
            m "Bryce settled back on the couch, bunching the rug and tugging the coffee table as his tail caught for a moment."
            m "He spread his hindlegs with a wink."
            Br flirty dk "What are you waiting for?"
            m "My addled brain managed to push through a few thoughts before I followed him over."
            c "Dry? Without protection?"
            m "I squinted in the dark, completely missing any ass I could go for under his towering shaft."
            c "And, uh, where?"
            m "At the question of protection, he smiled lopsidedly."
            Br flirty dk "C'mon. We're both guys. Kids aren't happening."
            menu:
                "[[Insist.]":
                    c "No. Not without protection."
                    if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                        c "I've seen a health aisle. You've got condoms."
                    else:
                        c "Your kind has condoms, right?"
                    $ brycemood -= 1
                    show bryce stern dk with dissolve
                    m "Bryce groaned, then gestured at a chest of drawers in a corner."
                    Br "Top. I think. Just hurry up."
                    $ bangok_four_bryce1_protected = True
                    play sound "fx/rummage.ogg"
                    m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. Only after I dug to the bottom did I finally find one closer to mine, unopened."
                    m "Tearing into the packaging, I returned equipped."
                "[[Bareback.]":
                    $ bangok_four_bryce1_protected = False
                    c "Okay. Where?"
            m "Bryce twisted his head behind the couch, returning with a bottle of lube clenched in his maw."
            show bryce stern dk with dissolve
            m "With a grunt of effort, he curled forward to brace the bottle against his cock, then depressed the plunger to squirt a dollop at the base of where said cock emerged from his slit."
            play sound "fx/box.wav"
            m "He tossed the bottle aside against the coffee table."
            Br smirk dk "There. Any more questions?"
            m "I answered his question by straddling his tail, bracing against his hindlegs, then experimentally prodding the opening he'd indicated beneath his shaft."
            Br brow dk "Further down. That spot's where mine comes out."
            menu:
                "[[Dock with him.]":
                    m "Bryce gasped, then clenched his teeth as I tried to press deeper next to his shaft."
                    $ brycemood -= 1
                    Br stern dk "What did I {i}just{/i} say?"
                    c "Uh."
                    menu:
                        "[[Dock him.]":
                            $ brycemood -= 1
                            play sound "fx/impact3.ogg"
                            show bryce at center
                            show bangok_four_bryce1_apartment night at Pan((0,0), (0,0), 0.0)
                            with vpunch
                            m "I sprawled across the floor, Bryce's kick leaving me out of breath and dizzy."
                            Br brow dk "This isn't one-way. You want inside me, you gotta {i}listen{/i} to me."
                            Br brow dk "Aim lower, okay? I'm way too pent up for what you're trying to pull."
                            play sound "fx/cartslide.ogg"
                            show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 2.0)
                            show bryce normal dk at Position(xpos=0.45,xanchor='center',ypos=1.05)
                            with ease
                            m "Bryce settled back onto the couch, spreading his legs for me again as we got back into position."
                            menu:
                                "[[Fuck him.]":
                                    pass
                                "[[Dock harder.]":
                                    play sound "fx/impact3.ogg"
                                    with vpunch
                                    scene black with fade
                                    jump bangok_four_bryce1_badmorning
                        "[[Listen to him.]":
                            pass
                "[[Fuck him.]":
                    pass
            show bryce flirty dk with dissolve
            if bangok_four_bryce1_protected == True:
                m "As the lube spread further around my condom, one of his hard belly plates ground against the bottom of my cock. Then all gave way to warm envelopment as I reached as far inside him as I could go."
            else:
                m "As the lube spread further around my shaft, one of his hard belly plates ground against the bottom of my cock. Then all gave way to warm envelopment as I reached as far inside him as I could go."
            m "As his shaft rubbed up my torso, he grinned lewdly."
            Br "That's the spot, huh?"
            m "I nodded, at a loss for words."
            Br smirk dk "Well, have your fun."
            m "I tugged out, beginning to pump experimentally at first, keeping an eye on Bryce's face to make sure I wasn't causing him any more discomfort."
            play soundloop "fx/rub2.ogg" fadein 3.0
            show bryce flirty dk with dissolve
            m "It didn't seem to fase him in the least. He shot me a teasing wink as I picked up the pace."
            m "Beneath his hard plates, his internal tissues were soft and hot. The pressure on my dick was light, a function of his ass's outermost sphincters more than the tightness of any internal anatomy."
            m "Of course, I wasn't just in this for myself. Though it was difficult to form a coherent thought beyond my next thrust, I put some words together."
            c "Are you feeling this at all?"
            Br laugh dk "Kinda!"
            Br smirk dk "You won't get me off with it, if that's what you're wondering."
            m "Taking that as a bit of a challenge, I moved one hand from bracing against his legs to sandwiching his shaft against my belly."
            play sound "fx/buck.ogg"
            show bryce stern dk with dissolve
            m "Bryce bucked his hips against mine, clearly taken off-guard by the move."
            Br flirty dk "D-Damn. That's a neat trick!"
            m "I didn't respond, his bucking back putting me near the edge of my peak."
            stop soundloop fadeout 0.5
            $ renpy.pause(0.5)
            show bryce smirk dk with dissolve
            play sound "fx/rub1.ogg"
            $ renpy.pause(1.5)
            play sound "fx/extinguish.ogg"
            show black with dissolve
            if bangok_four_bryce1_protected == True:
                m "I came, depositing my load in the condom's reservoir, buried deep within Bryce's ass."
            else:
                m "I came, depositing my load as deep as I could go in Bryce's ass."
            $ bangok_four_bryce1_playercame = True
            hide black with dissolvemed

            if persistent.bangok_watersports == True:
                play soundloop ["fx/faucet1.ogg", "fx/faucet2.ogg"]
                show bryce brow dk with dissolve
                m "After a moment, I realized yet more fluid was draining out of me."
                c "Uh."
                Br laugh dk "Too much to drink?"
                m "My cheeks flushed with embarassment."
                stop soundloop fadeout 1.5
                Br smirk dk "I do this with drinking buddies all the time. You're not the first to piss in me."

            if bangok_four_bryce1_protected == True:
                m "He shifted his hips, my body's fluid output sloshing lewdly around my penis's head inside the condom."
            else:
                m "He shifted his hips, my body's fluid output flowing lewdly around my penis, buried in his ass."
            Br flirty dk "That's you. Now how about me?"
            
            if bangok_four_bryce1_protected == True:
                m "I pulled out first, considering my options as I tugged off and tied up my condom. My head was clearer, but I also felt lightheaded from the effort I'd just expended."
            else:
                m "I pulled out first, considering my options. My head was clearer, but I also felt lightheaded from the effort I'd just expended."
            label bangok_four_bryce1_preciprocity_menu:
            menu:
                "I... think I'm done.":
                    Br brow dk "Excuse me?"
                    c "I'm..."
                    $ renpy.pause (0.8)
                    c "I think I'm going to pass out now."
                    Br stern dk "Hey!"
                    scene black with fade
                    play sound "fx/impact3.ogg"
                    jump bangok_four_bryce1_badmorning
                "Want to fuck me?":
                    jump bangok_four_bryce1_analbot
                "I guess I could suck you.":
                    jump bangok_four_bryce1_oralbot_merge
                "[[Finish him by hand.]":
                    $ renpy.error("TODO: S'more fucking.")
                "I'm not sure I can fit you." if bangok_four_bryce1_m2_fit:
                    call bangok_four_bryce1_m2_fit from bangok_four_bryce1_preciprocity_menu_fit
                    jump bangok_four_bryce1_preciprocity_menu






        "I want you to suck me.":
            $ bangok_four_bryce1_position = "oraltop"
            Br flirty dk "Sure. But turnabout is fair play."
            label bangok_four_bryce1_m2_bsucc_merge:
            show bryce flirty dk with dissolve
            show bryce at Position(ypos=1.3) with ease
            show bryce at Position(ypos=1.5) with ease
            m "Bryce got low in front of my crotch, hot breath washing over my hardening shaft."
            if bangok_four_bryce1_protected:
                c "W-Wait! Protection!"
                show bryce brow dk at Position(ypos=1.3) with ease
                m "Bryce sighed, waiting a few moments for me to roll on the condom."
                $ renpy.pause (0.3)
                show bryce at Position(ypos=1.5) with ease
            else:
                menu:
                    "W-Wait! Protection!":
                        show bryce brow dk at Position(ypos=1.3) with ease
                        Br "Are you kidding me?"
                        c "We don't know what my stuff might do to you."
                        if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                            c "I've seen a health aisle here. You've got condoms."
                        else:
                            c "Your kind has condoms, right?"
                        show bryce stern dk with dissolve
                        m "Bryce groaned, then gestured at a chest of drawers in a corner."
                        Br "Top. I think. Just hurry up."
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.ogg"
                        m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one, just in case, then dug a little deeper for one my size."
                        m "Only after I dug to the bottom did I finally find a box of condoms closer to my scale, unopened."
                        m "Tearing into the packaging, I returned with the necessary equipment."
                        c "There."
                        Br smirk dk "Finally."
                        show bryce at Position(ypos=1.5) with ease
                    "[[Enjoy.]":
                        pass
            show bryce at Position(ypos=1.51) with ease
            m "Pressing forward, he enveloped my entire cock in his mouth with one smooth motion, bumping up against my pelvis. I barely got a moment to enjoy the sensation, though, as..."
            
            play sound "fx/impact3.ogg"
            show bryce brow dk at Position(ypos=1.2)
            show bangok_four_bryce1_apartment night at Pan((0,120), (0,120), 0.0)
            with vpunch
            m "I lost my balance, tripping to the floor."
            Br "Whoops."
            c "Ow."
            show bryce normal dk at Position(ypos=1.2)
            show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
            with ease
            m "Picking myself up, I looked around the room for something to brace against for our next try."
            menu:
                "Wall.":
                    $ bangok_four_bryce1_position = "oraltopwall"
                    c "Here, up against the wall."
                    Br smirk dk "If you say so."
                    m "I leaned back against the wall slightly, spreading my legs to give Bryce easy access to my groin."
                    $ renpy.pause (0.3)
                "Couch.":
                    $ bangok_four_bryce1_position = "oraltopcouch"
                    c "Here, what if I sit on your couch?"
                    $ renpy.pause (0.5)
                    Br brow dk "A little further forward. I don't want my chin horn tearing my cushions."
                    $ renpy.pause (0.3)
            Br flirty dk "Alright. Now to see what a human tastes like."
            if bangok_four_bryce1_protected == True:
                $ brycemood -= 1
                Br brow dk "Through a condom."
            show bryce smirk dk at Position(ypos=1.3) with ease
            show bryce smirk dk at Position(ypos=1.5) with ease
            $ renpy.pause(0.3)
            m "Bryce nestled between my legs, the scales on his snout rubbing against my thighs."
            m "The cold air of the room was, in my crotch, replaced with warmth as he exhaled."
            show bryce smirk dk at Position(ypos=1.51) with ease
            m "Then he dove in, enveloping my cock and balls both in his warm maw."
            c "Mmh!"
            m "It was all I could do to sit still as his tongue wove around the base of my shaft, the tip tugging at my sac just enough to bounce and tease my balls."
            c "W-Wow."
            show bryce flirty dk with dissolve
            $ renpy.pause(0.3)
            show bryce smirk dk at Position(ypos=1.5) with ease
            m "Pulling back, the barest edges of his teeth and scaly lips scraped over the top of my cock and the bottom of my sack. I clenched my fists, just trying to keep my ass in place and not buck into his face."
            m "He let my balls drop free of his mouth, focusing the ministrations of his scaly lips and tongue on my shaft."
            m "It was decadant. But he wasn't all the way down in my groin; a tiny bit of my shaft remained outside his heavenly maw."
            menu:
                "[[Grab his horns.]":
                    $ brycemood -= 2
                    if bangok_four_bryce1_position == "oraltopcouch":
                        play sound ["fx/hit2.ogg", "fx/cartdown.ogg"]
                        show bryce stern dk at Position(ypos=1.3) with ease
                        m "Bryce jerked, releasing my cock as he slammed his muzzle into my chest, shaking the couch. It was only luck that I wasn't cut by one of his small chin and nose horns."
                    else: # bangok_four_bryce1_position == "oraltopwall":
                        play sound ["fx/hit2.ogg", "fx/impact3.ogg"]
                        show bryce stern dk at Position(ypos=1.3) with ease
                        m "Bryce jerked, releasing my cock as he slammed his muzzle into my chest, crushing me against the wall. It was only luck that I wasn't cut by one of his small chin and nose horns."
                    c "F- Fuck!"
                    $ renpy.pause (1.2)
                    c "Okay, don't touch the horns. Got it."
                    Br brow dk "No. Do. But {i}tell{/i} me. That's a delicate spot for us. Something yanking our horns the wrong way could tear them off our skull."
                    c "I don't think I'm that strong."
                    Br stern dk "Neither do I. But I'm still going to respond if I'm not expecting that."
                    m "After a moment longer of stern look, Bryce sank back down between my thighs."
                    show bryce at Position(ypos=1.5) with ease
                    show bryce flirty dk with dissolve
                    m "As he set back to work, I was almost instantly back on the verge of facefucking him. His tongue slathered sparks of strong sensation into my groin, toying with my cock."
                    menu:
                        "C-Can I grab your...":
                            $ brycemood += 1
                            m "Taking his driving his face deeper into my crotch as a sign of encouragement, I grabbed Bryce's horns and thrust."
                        "[[Cum.]":
                            pass
                "[[Ask him to go deeper.]":
                    if bangok_four_bryce1_position == "oraltopcouch":
                        m "Bryce obliged, face pressing into my thighs and crotch while his chin horn almost cleaved my sack, and did poke the pillow."
                    elif bangok_four_bryce1_position == "oraltopwall":
                        m "Bryce obliged, face pressing my pelvis hard into the wall."
                    c "C-Careful!"
                    m "He made an uninteligible noise, the sound vibrating in his mouth around my cock."
                    m "That was all the endurance I had left."
                "I- I'm close!":
                    pass
            
            play sound "fx/extinguish.ogg"
            show black with dissolve
            if bangok_four_bryce1_protected == True:
                m "I came, depositing my load in the condom's reservoir, resting on Bryce's tongue."
            else:
                m "I came, spurting into Bryce's mouth."
            $ bangok_four_bryce1_playercame = True
            hide black with dissolvemed

            if persistent.bangok_watersports == True:
                play soundloop ["fx/faucet1.ogg", "fx/faucet2.ogg"]
                show bryce brow dk with dissolve
                m "After a moment, I realized yet more fluid was draining out of me."
                c "Uh."
                if bangok_four_bryce1_protected == True:
                    m "My cheeks flushed with embarassment. I was sure Bryce could tell what was going on, yet he continued sucking on the condom."
                else:
                    play sound "fx/gulping.wav"
                    m "My cheeks flushed with embarassment. I was sure Bryce could tell what was going on, but it almost sounded like he was..."
                stop soundloop fadeout 1.5
                stop sound fadeout 0.5
                $ renpy.pause (1.5)
                show bryce at Position(ypos=1.3) with ease
                Br smirk dk "I have sex with drinking buddies all the time. You think you're the first one who's pissed in me?"

            show bryce at Position(ypos=1.0) with ease
            show bryce flirty dk with dissolve
            m "Getting back to his feet, Bryce shot me a wink."
            Br flirty dk "That's you. Now how about me?"
            jump bangok_four_bryce1_preciprocity_menu




        "It's not that little..." if bangok_four_bryce1_m2_size:
            $ bangok_four_bryce1_m2_size = False
            c "I know it's probably smaller than you're used to, and probably not even enough to get you off--"
            # show bryce laugh dk with dissolve
            # $ renpy.pause(0.8)
            Br smirk dk "Don't worry. I've had smaller. You can use your hands or something if you can't do it with your tool."
            jump bangok_four_bryce1_m2_menu

        "I'm not sure I can fit you." if bangok_four_bryce1_m2_fit:
            call bangok_four_bryce1_m2_fit from bangok_four_bryce1_m2_menu_fit
            jump bangok_four_bryce1_m2_menu
            label bangok_four_bryce1_m2_fit:
                $ bangok_four_bryce1_m2_fit = False
                c "You're, uh..."
                Br flirty dk "Not something you've seen before, huh?"
                c "Definitely."
                Br smirk dk "And then, especially with my kind, they are... Well, I think you can see what I mean."
                c "Mmm-hmmm."
                Br "You don't have to try that if you don't want to."
                c "Okay."
                return

label bangok_four_bryce1_badmorning:
    scene black with fade
    $ renpy.pause (1.5)
    scene pad at Pan ((0, 0), (0,360), 5.0) with dissolveslow
    play music "mx/campfire.ogg" fadein 2.0
    nvl clear
    window show
    n "I awoke looking at an unfamiliar ceiling."
    n "For a moment, I wondered where I was before some of the events of last night came back to me."
    n "As I got up and looked around, I realized that I'd apparently slept on the floor, naked."
    if bangok_four_bryce1_protected and not bangok_four_bryce1_playercame:
        n "A condom still hung from my limp dick, unfilled."
    window hide
    nvl clear
    show bryce brow with dissolve
    Br "Hey. You okay?"
    c "What did we do last night?"
    if bangok_four_bryce1_playercame == False:
        Br stern "Not much."
    else:
        Br stern "Not enough."
    c "There was a drinking contest..."
    Br brow "Then you remember plenty."
    Br stern "Get your clothes and leave."
    c "Huh?"
    if bangok_four_bryce1_playercame == False:
        Br "The contest was a stupid idea. That inept attempt at sex moreso."
    else:
        Br "The contest was a stupid idea. That unreciprocated sex moreso."
    c "Hang on, you were the one pushing the contest."
    Br "And you were the one pushing the sex. Bad ideas all around."
    c "That's easy to say after the fact."
    Br brow "Says the reason things went sideways."
    c "Excuse me? We were both drunk."
    Br stern "I was communicating my needs pretty damn clearly."
    c "That communication would have come across a lot better if I {i}hadn't been drunk.{/i}"
    Br "And that's somehow my fault?"
    stop music fadeout 3.0
    c "Not far from it. As an ambassador, I can't really say no to a social meeting with the chief of police."
    play sound "fx/tableslap.wav"
    m "Bryce's lashing tail nearly knocked his coffee table over."
    Br angry "You pressured {i}me{/i} for sex!" with vpunch
    c "..."
    Br "..."
    Br stern "This started with you touching me inappropriately when I was passed out."
    c "Because I was drunk, because of your stupid drinking contest."
    Br brow "So it's never your fault and it's always mine? That's just brilliant, it's anyone's fault but your own. Well done, [player_name]."
    Br stern "Pick up your layers and get out."
    m "He barely gave me enough time to grab my clothes before he was nosing me out his door with the sharp point on his snout, still naked."
    play sound "fx/door/doorclose3.wav"
    scene black with dissolve
    if bangok_four_bryce1_protected and not bangok_four_bryce1_playercame:
        m "The empty condom still hung from my limp dick."
    $ bangok_four_bryce1_unplayed = False
    $ brycestatus = "bad"
    $ brycescenesfinished = 1
    jump _mod_fixjmp


label bangok_four_bryce1_morningcouch:
label bangok_four_bryce1_morningfloor:
    scene black with fade
    $ renpy.pause(1.5)
    play sound "fx/system3.ogg"
    s "TODO: Morning scene"
    $ renpy.error("TODO: Morning scene")