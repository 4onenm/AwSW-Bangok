# Flags used:
#  persistent.bangok_inflation - Inflation
#  persistent.bangok_knot - Knotting
#  persistent.bangok_watersports - Watersports

init python:
    bangok_four_bryce1_unplayed = True
    bangok_four_bryce1_protected = False
    bangok_four_bryce1_protected_a = False
    bangok_four_bryce1_protected_b = False
    bangok_four_bryce1_brycecame = False
    bangok_four_bryce1_playercame = False
    bangok_four_bryce1_playerstuffed = False
    bangok_four_bryce1_position_picka = None
    bangok_four_bryce1_position_pickb = None
    bangok_four_bryce1_wstiming = None
    bangok_four_bryce1_oralspot = None

init python in bangok_four_bryce1:
    fuckwomb = False
    knotpos = None

label bangok_four_bryce1_skipmenu:
    play sound "fx/system3.wav"
    s "Would you like to lewd Bryce?"
    menu:
        "Yes. I would like to lewd Bryce.":
            play sound "fx/system3.wav"
            if bangok_four_common.bangnokay.check():
                s "Too bad.{cps=2}..{/cps}{w=1.0}{nw}"
            else:
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                jump bangok_four_bryce1_apartment_decided
        "No. Not that far.":
            pass
    jump bangok_four_bryce1_skipmenu_return



label bangok_four_bryce1_ws_conversation:
    Br stern dk bangok "Mmh."
    Br "There's something I need to ask you before you start that."
    c "Huh?"
    Br "All that drinking earlier means I kinda gotta {i}go{/i}."
    if bangok_four_bryce1_playercame == True:
        Br smirk dk bangok "Just like you did."
    Br brow dk bangok "Does that... matter to you at all?"
    menu:
        "Go take care of your business.":
            $ brycemood -= 1
            Br brow dk bangok "Alright."
            call bangok_four_bryce1_ws_emptying_the_tank(True)
        "I might be interested.":
            Br smirk dk bangok "Before or after I blow?"
            menu:
                "Shower me.":
                    show bryce stern dk bangok with dissolve
                    $ renpy.pause(0.5)
                    Br "Uh, no. Can't do that one."
                    c "Why not?"
                    Br brow dk bangok "You're {i}already{/i} going to reek of me and alcohol. Not even sure an actual shower will get that off. Are you gonna be a good ambassador if they can smell urine on you, too?"
                    c "..."
                    Br stern dk bangok "Nothing outside tonight."
                    c "Fine."
                    menu:
                        "Before.":
                            $ bangok_four_bryce1_wstiming = "before"
                        "After.":
                            $ bangok_four_bryce1_wstiming = "after"
                        "Not interested anymore.":
                            $ brycemood -= 1
                            $ renpy.pause(0.8)
                            Br "If you say so. Let me go get it out, then."
                            call bangok_four_bryce1_ws_emptying_the_tank(True)
                            return
                "Before.":
                    $ bangok_four_bryce1_wstiming = "before"
                "After.":
                    $ bangok_four_bryce1_wstiming = "after"
            Br flirty dk bangok "You got it."
    return


label bangok_four_bryce1_ws_emptying_the_tank(feelbad=False, condom=False):
    hide bryce with dissolve
    c "(Now that I think about it, how do dragons use toilets?)"
    play sound "fx/door/door_open.wav"
    menu:
        c "(Should I follow him to watch?)"
        "Follow.":
            m "Curiosity getting the better of me, I wandered over to Bryce's open bathroom door."
            m "He stood up over the toilet, one forepaw on the tank, struggling to keep his balance and aim his erect cock into the bowl as he began to piss."
            play sound "fx/pour.ogg"
            m "Catching my footsteps, he looked gave me a wink."
            if condom:
                play soundloop "fx/faucet2.ogg" fadein 1.0
                m "The condom, still over his dick, bulged lewdly with urine as he pissed in it, right in front of me."
            else:
                play sound "fx/spray.ogg" fadein 0.5
                play soundloop "fx/faucet2.ogg" fadein 1.0
                m "In so doing, he lost focus on his aim and spattered the seat, the tank, and the floor with a stream of golden droplets."
            Br stern dk bangok "Damn."
            Br flirty dk bangok "Like to watch, huh?"
            $ brycemood += 1
            if not condom:
                play sound "fx/spray.ogg"
            m "My cheeks burned. Bryce arched his back, preening as adjusted his hips to get his cock back over the bowl for the last of his bladder's contents."
            stop soundloop fadeout 2.0
            Br "I'm guessing that's not how humans do it."
            if condom:
                play sound "fx/bubbles.ogg"
                m "Bryce shook his penis, the condom bobbing lewdly as it stretched to try to contain the liquid gold."
            else:
                m "Bryce shook his penis to free any last, clinging drops, then dropped his forepaws back to the somewhat damper floor."
            c "Depends on the toilet, but it's not that far off for peeing. Aim's a little better, when not drunk."
            Br smirk dk bangok "Huh."
            m "I followed him back out into his apartment's main living space."
        "Stay.":
            if feelbad:
                $ renpy.pause (2.0)
                m "I sat, naked, on a dragon's couch, holding a bottle of lube."
                $ renpy.pause (3.0)
                c "(Maybe I should have said something else? I don't know why I'm still thinking about it...)"
                $ renpy.pause (3.0)
            else:
                $ renpy.pause (2.0)
                c "..."
                $ renpy.pause (3.0)
                if bangok_four_playerhasdick:
                    if bangok_four_bryce1_playercame == True:
                        m "I played with my soft dick a little to pass the time."
                    else:
                        m "I played with my hard dick a little to pass the time."
                else:
                    m "I teased apart my slick vaginal lips to pass the time."
                $ renpy.pause (3.0)
    play sound "fx/door/doorclose3.wav"
    show bryce normal dk bangok with dissolve
    $ renpy.pause (0.5)
    Br flirty dk bangok "Where were we?"
    return

label bangok_four_bryce1_position(pos):
    python:
        if not bangok_four_bryce1_position_picka:
            bangok_four_bryce1_position_picka = pos
        elif not bangok_four_bryce1_position_pickb:
            bangok_four_bryce1_position_pickb = pos
        else:
            renpy.error("Neither you nor Bryce can go twice in one night!")
    return

label bangok_four_bryce1_setprotected(p):
    python:
        bangok_four_bryce1_protected = p
        if bangok_four_bryce1_position_pickb is not None:
            bangok_four_bryce1_protected_b = p
        elif bangok_four_bryce1_position_picka is not None:
            bangok_four_bryce1_protected_a = p
        else:
            renpy.error("Never should you be able to put on a condom before you know what sex act you're doing.")
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
            c "I haven't seen exactly what a dragon... you know. Looks like."
            Br "..."
            c "On humans it kinda hangs out. I was just looking for..."
            Br "..."
            c "..."
            if brycemood > 4 and not (bangok_four_common.bangnokay.check()):
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
            if brycemood < 6 or (bangok_four_common.bangnokay.check()):
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
        "Trying to wake you up.":
            c "That's a sensitive spot for humans. I thought poking it might..."
            $ renpy.pause(0.8)
            Br brow "..."
            $ renpy.pause(0.8)
            play sound "fx/tableslap.wav"
            Br laugh "That works, I suppose."
            if brycemood < 4 or (bangok_four_common.bangnokay.check()):
                show bryce stern with dissolve
            else:
                show bryce smirk with dissolve
            Br "So, what, is that normal among humans?"
            c "I mean, we'd have clothes protecting it."
            Br brow "Right, all your layers."
            if brycemood < 6 or (bangok_four_common.bangnokay.check()):
                Br stern "Well, I need to get home, you need to get home, let's just... focus on that."
                c "I'll help you walk home."
                $ renpy.pause(0.5)
                Br normal "Thanks."
            else:
                Br flirty "Y'know, I kinda want to see what's under yours, back at my place...?"
                c "Are you coming on to me?"
                Br smirk "Are you interested?"
                menu:
                    "Accept.":
                        show bryce flirty with dissolve
                        $ renpy.pause(0.5)
                        jump bangok_four_bryce1_apartment_decided
                    "Reject.":
                        $ brycemood -= 1
                        c "Let's just get you home, Bryce."
                        Br laugh "Fair enough!"
                        jump bangok_four_bryce1_nevermind







label bangok_four_bryce1_apartment:
    scene black with dissolvemed
    $ renpy.pause (0.6)
    scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0) with dissolvemed
    $ renpy.pause (0.5)
    show bryce normal dk bangok with dissolve
    m "Inside Bryce's dark apartment, the big dragon made a beeline for his couch."
    menu:
        "[[Interrupt him.]":
            pass
        "[[Go home.]":
            m "I didn't make it to the door."
            c "(No... think I'll just lie down here.)"
            jump bangok_four_bryce1_nevermind
    c "Bryce?"
    Br brow dk bangok "Mmh?"
    menu:
        "Nevermind.":
            c "(So... tired.)"
            m "I didn't make it to the door to leave."
            jump bangok_four_bryce1_nevermind
        "Want to do something stupid?":
            c "You're drunk. I'm drunk. And you're... very attractive."
            c "What do you say?"
            $ renpy.pause (0.4)
            if brycemood < 5 or (bangok_four_common.bangnokay.check()):
                play sound "fx/cartslide.ogg"
                hide bryce with dissolve
                m "By the time I finished asking the question, Bryce was already fast asleep on his couch."
                m "I gave up and turned for the door, then lost what little energy I had."
                c "(Maybe... I'll just sleep here.)"
                jump bangok_four_bryce1_nevermind
            else:
                pass

    Br flirty dk bangok "Alright. Fuck it. You're cute too."
    $ brycemood = 4

    if False:
        label bangok_four_bryce1_apartment_decided:
        scene black with dissolvemed
        $ renpy.pause (0.6)
        scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0) with dissolvemed
        $ renpy.pause (0.5)
        show bryce flirty dk bangok with dissolve

    play sound "fx/undress.ogg"
    if bangok_four_common.bangnokay.check():
        $ renpy.pause(0.8)
        jump bangok_four_bangnokay_kill_replay
    m "I struggled out of my clothes as fast as my lust-drunk state would allow."
    if bangok_four_malepartners + bangok_four_femalepartners < 1:
        c "(Is this really happening? Am I really going to fuck a dragon?)"
    show bryce at Position(ypos=1.1) with ease
    m "Bryce rolled his lower body onto its side, revealing the worryingly large shaft emerging between his legs."
    if persistent.bangok_balls == True:
        if persistent.bangok_inflation == True:
            m "As his muscles clenched, a scaleless sac emerged too, two round orbs larger than apples swinging down inside to plop wetly against the underside of his tail."
        else:
            m "As his muscles clenched, a scaleless sac emerged too, two round orbs larger than mandarins swinging down inside to plop wetly against the underside of his tail."
    c "Huh. Guess you don't get whiskey dick."
    Br brow dk bangok "What's that?"
    c "It's where alcohol makes it hard to... stay hard."
    Br "It's always hard."
    c "Huh."
    Br smirk dk bangok "That's mine. Now show me yours."
    if bangok_four_playerhasdick is None:
        menu:
            "Show him your dick.":
                $ bangok_four_playerhasdick = True
            "Show him your lack of dick.":
                $ bangok_four_playerhasdick = False

    if bangok_four_playerhasdick == True:
        jump bangok_four_bryce1_m
    else:
        jump bangok_four_bryce1_f

label bangok_four_bryce1_f:
    m "Teasing my vaginal lips apart, I gave him a winking look at my cunt."
    Br flirty dk bangok "Ah."
    Br smirk dk bangok "Want to keep things simple and just go for it?"
    menu:
        "Fuck yes.":
            $ bangok_four_malepartners += 1
            $ brycemood += 1
            jump bangok_four_bryce1_f_fuck
        "Mm. Actually...":
            show bryce brow dk bangok with dissolve
            $ bangok_four_bryce1_m2_size = True
            $ bangok_four_bryce1_m2_fit = True
            label bangok_four_bryce1_f_menu:
            menu:
                "I want to taste you.":
                    $ bangok_four_malepartners += 1
                    jump bangok_four_bryce1_oralbot
                "I want you in my ass.":
                    $ bangok_four_malepartners += 1
                    jump bangok_four_bryce1_analbot
                "I want your tongue in me.":
                    $ bangok_four_malepartners += 1
                    Br flirty dk bangok "Sure. But turnabout is fair play."
                    jump bangok_four_bryce1_f_tonguefuck
                "I'm not sure I can fit you." if bangok_four_bryce1_m2_fit:
                    call bangok_four_bryce1_m2_fit from bangok_four_bryce1_f_menu_fit
                    jump bangok_four_bryce1_f_menu
                "Okay, sure. Fuck me.":
                    $ bangok_four_malepartners += 1
                    show bryce smirk dk bangok with dissolve
                    jump bangok_four_bryce1_f_fuck

label bangok_four_bryce1_f_tonguefuck:
    call bangok_four_bryce1_position("oraltop")
    show bryce flirty dk bangok with dissolve
    show bryce at Position(ypos=1.3) with ease
    show bryce at Position(ypos=1.5) with ease
    m "Bryce got low in front of my crotch, hot breath washing over my dampening lips."
    if bangok_four_bryce1_position_picka != "oraltop":
        menu:
            "W-Wait! Protection!":
                $ brycemood -= 1
                show bryce brow dk bangok at Position(ypos=1.3) with ease
                Br "Are you kidding me?"
                c "We don't know what my stuff might do to you."
                Br stern dk bangok "Well, I've got some bad news for you. Oral so rarely causes complications for anyone here, I don't buy dental dams."
                Br "Ones my size aren't exactly cheap anyway."
                m "I paused a moment, considering my options."
                menu:
                    "Fuck it. Eat me anyway.":
                        Br brow dk bangok "You're sure?"
                        c "Yeah."
                        Br smirk dk bangok "You got it."
                        show bryce at Position(ypos=1.5) with ease
                        show bryce flirty dk bangok
                    "Skip this, then. I want you in my ass.":
                        $ bangok_four_bryce1_position_picka = "analbot"
                        Br smirk dk bangok "Alright. I've got condoms over there. Top drawer."
                        jump bangok_four_bryce1_analbot_fetchcondom
                    "Skip this, then. I want you in my cunt.":
                        $ bangok_four_bryce1_position_picka = "vag"
                        Br smirk dk bangok "Alright. I've got condoms over there. Top drawer."
                        jump bangok_four_bryce1_f_fuck_getprotection
                    "Maybe I'll suck you instead.":
                        $ bangok_four_bryce1_position_picka = "oralbot"
                        Br flirty dk bangok "Oh?"
                        play sound "fx/cartslide.ogg"
                        show bryce normal dk bangok at Position(xpos=0.4,xanchor='center') with dissolve
                        show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
                        m "Bryce settled back on the couch, bunching the rug and tugging the coffee table as his tail caught for a moment."
                        m "He splayed one hindleg out, giving me easy access to his shaft from beside the couch."
                        Br smirk dk bangok "Alright. I've got condoms over there. Top drawer."
                        jump bangok_four_bryce1_oralbot_getprotection
            "[[Enjoy.]":
                    pass
    show bryce at Position(ypos=1.51) with ease
    m "Pressing forward, Bryce opened his maw wide, surrounding my crotch as his tongue aimed for my love canal."
    m "The abrupt feeling of tongue and pinpricks of teeth was too much. I stumbled back, tripping and falling on the edge of the rug."
    play sound "fx/impact3.ogg"
    show bryce brow dk bangok at Position(ypos=1.2)
    show bangok_four_bryce1_apartment night at Pan((0,120), (0,120), 0.0)
    with vpunch
    Br "Whoops."
    c "Ow."
    Br "You okay?"
    c "Yeah."
    show bryce normal dk bangok at Position(ypos=1.2)
    show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
    with ease
    m "Picking myself up, I looked around the room for something to brace against for our next try."
    menu:
        "Wall.":
            $ bangok_four_bryce1_oralspot = "wall"
            c "Here, up against the wall."
            Br smirk dk bangok "If you say so."
            m "I leaned back against the wall slightly, spreading my legs to give Bryce easy access to my groin."
            $ renpy.pause (0.3)
        "Couch.":
            $ bangok_four_bryce1_oralspot = "couch"
            c "Here, what if I sit on your couch?"
            $ renpy.pause (0.5)
            Br brow dk bangok "A little further forward. I don't want my chin horn tearing my cushions."
            $ renpy.pause (0.3)
    Br flirty dk bangok "Alright. Now to see what a human tastes like."
    show bryce smirk dk bangok at Position(ypos=1.3) with ease
    show bryce smirk dk bangok at Position(ypos=1.5) with ease
    $ renpy.pause(0.3)
    m "Bryce nestled between my legs, the scales on his snout rubbing against my thighs."
    m "The cold air of the room was, in my crotch, replaced with warmth as he exhaled."
    show bryce smirk dk bangok at Position(ypos=1.51) with ease
    m "He opened his mouth again, doing a better job of keeping his teeth from my skin. I shuddered as his long tongue rubbed over my vaginal lips."
    c "W-Wow."
    show bryce flirty dk bangok with dissolve
    $ renpy.pause(0.3)
    show bryce flirty dk bangok at Position(ypos=1.52) with ease
    m "He dug deeper in, shoving his tongue into my private spaces and tasting around."
    m "His scaly lips rubbed my thighs and belly, the sharp points of his teeth just ghosting behind."
    if bangok_four_bryce1_oralspot == "couch":
        m "The pallete of sensations and hint of danger had my lower body numb and limp, sliding a little further out on his couch and onto his eager tonguefucking."
    else:
        m "The pallete of sensations and hint of danger had my legs weak, letting me slide a little further down the wall onto his eager tonguefucking."

    if persistent.bangok_watersports == True:
        m "As his tongue pulled forward and up, exploring toward the top of my lips, I felt a pouch of fluid within me compress, then begin to spill out into his mouth."
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        show bryce brow dk bangok with dissolve
        c "O-Oh fuck, Bryce I--"
        show bryce laugh dk bangok with dissolve
        play sound "fx/gulping.wav"
        m "I couldn't stop once I'd started. My cheeks flushed with embarassment. I was sure Bryce could tell what was going on, yet he continued to tonguefuck me, gulping down what I was pissing out."
        stop soundloop fadeout 1.5
        stop sound fadeout 0.5
        $ renpy.pause (1.5)
        m "Only when I was completely done did he withdraw his tongue, rising to give me a wink."
        show bryce flirty dk bangok with dissolve
        show bryce at Position(ypos=1.4) with ease
        Br smirk dk bangok "I have sex with drinking buddies all the time. You think you're the first one who's pissed in me?"
        Br flirty dk bangok "My tongue might even fit up there. Mind if I...?"
        # Just gonna borrow bangok_four_bryce1_wstiming != None here because it's no big deal. I'm sure I'll remember to set it back. :bryce_laugh:
        menu:
            "[[Let Bryce into your urethra.]":
                $ bangok_four_bryce1_wstiming = "before"
                c "I... sure."
                show bryce at Position(ypos=1.5) with ease
                m "Bryce sank back down to my crotch, hot breath meeting my flushed skin as his tongue poked around my vaginal entrance, looking for the smaller hole he wanted."
                m "I shuddered, electric sparks of pleasure dancing up my belly as he teased my clit."
                m "Then he found my pisshole."
                c "O-OH!"
                m "The fullness in my crotch was an altogether different kind as his tongue stretched wide a hole not meant for stretching."
            "[[Refuse.]":
                show bryce brow dk bangok with dissolve
                c "In humans, that's a Urinary Tract Infection waiting to happen. Is that more common among dragons?"
                Br "Quite a bit, yes. What's a...?"
                show bryce stern dk bangok with dissolve
                $ renpy.pause (0.3)
                m "He shook his head."
                Br normal dk bangok "Oh well."
                show bryce at Position(ypos=1.5) with ease
                m "Giving me just a moment to prepare, Bryce dove back into my crotch."

    show bryce laugh dk bangok with dissolve
    m "I arched my back, lost in what he was doing to my lower body. He carefully pressed even deeper, wet maw mating up against my lower body as he devoted as much tongue as he could inside me."


    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is not None:
        m "The feeling of needing to pee returned as his tongue easily wormed through my bladder's entrance, tasting me where no human could ever go."
        c "(I need to piss a dragon's tongue. Oh this is incredible.)"
    else:
        c "Ah!"
        m "My entire belly twinged, electrified as the tip of his tongue just barely flicked my cervix, the inner gate to my womb."

    if bangok_four_bryce1_oralspot == "wall":
        m "I slid a little further down the wall, getting so incredibly close. I wanted him just a little deeper."
    else:
        m "I was almost beyond conscious thought. I was so close, I just needed him a little deeper."
    menu:
        "[[Grab his horns.]":
            $ bangok_four_hornincident = True
            $ brycemood -= 2
            if bangok_four_bryce1_oralspot == "couch":
                play sound ["fx/hit2.ogg", "fx/cartdown.ogg"]
                show bryce stern dk bangok at Position(ypos=1.3) with vpunch
                m "Bryce jerked, yanking his tongue from inside me before slamming his nose into my stomach, shaking the couch. It was only luck that I wasn't cut by one of his teeth or by his nose horn."
            else: # bangok_four_bryce1_oralspot == "wall":
                play sound ["fx/hit2.ogg", "fx/impact3.ogg"]
                show bryce stern dk bangok at Position(ypos=1.3) with vpunch
                m "Bryce jerked, yanking his tongue from inside me before slamming his nose into my stomach, crushing me against the wall. It was only luck that I wasn't cut by one of his teeth or by his nose horn."
            c "F-Fuck!"
            $ renpy.pause (1.2)
            m "I shuddered as he glared at me, my near-orgasm ebbing slowly as my groin remained flushed with heat."
            c "Okay, don't touch the horns. Got it."
            Br brow dk bangok "No. Do. But {i}tell{/i} me. That's a delicate spot for us. Something yanking our horns the wrong way could tear them off our skull."
            c "I don't think I'm that strong."
            Br stern dk bangok "Neither do I. But I'm still going to respond if I'm not expecting that."
            m "After a moment longer of stern look, Bryce sank back down between my thighs."
            show bryce at Position(ypos=1.5) with ease
            show bryce laugh dk bangok with dissolve

            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is not None:
                m "He found my urethra again easily. The feeling of him sliding in a second time, un-pissing through my already stretched urethra, pushed me right back to where I had been and even a moment closer."
            else:
                m "His tongue slithered inside me again. It snaked around, sampling my arousal from my walls, but it wasn't as deep as it had been -- it wasn't at my womb's gate, like no human tongue ever could be."
            menu:
                "C-Can I grab your...":
                    $ brycemood += 1
                    m "His brief affirmative hum was all the approval I needed. I grabbed his horns, pulled his face and tongue just that little bit deeper, and came."
                "[[Push downward.]":
                    pass
        "[[Push downward.]":
            pass

    show black with fadequick
    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is not None:
        m "My empty love channel spasmed, juices of my arousal dripping down into the bottom of his maw as he speared my bladder on his tongue."
        hide black with dissolveslow
        m "He withdrew slowly, cautious not to cause any pain in my urethra now that my arousal was mostly drained. Even still the sensation left me a squirming mess."
        m "Then he slipped back into my vagina, licking up my juices."
    else:
        m "My love canal clenched around his tongue, milking his saliva as his tip once again made that cervical kiss."
        hide black with dissolveslow
        m "He remained at that depth a long moment, spasms inside of me prodding my cervix against his tongue again and again."
        m "Then he withdrew to lesser depths, licking up the fresh vaginal juices from my orgasm."
    c "C-Careful. I might... might still..."
    show bryce flirty dk bangok with dissolve
    show bryce normal dk bangok at Position(ypos=1.3) with ease
    m "Shooting me a wink, he withdrew completely."

    if bangok_four_bryce1_oralspot == "wall":
        m "My legs could barely hold me up against the wall. My mind was a scattered mess."
    else: # couch
        m "I slumped back against the couch, momentarily completely spent."

    m "A thin half-circle of red pinpricks circled my belly just over my navel, small scratches from the points of his teeth."

    show bryce brow dk bangok with dissolve
    show bryce at center with ease
    Br "You okay?"

    menu:
        "I'm never getting tongue from a human again.":
            Br stern dk bangok "What? What's wrong?"
            c "That... that was incredible."
            $ brycemood += 1
            Br flirty dk bangok "Oh."
            $ renpy.pause (0.5)
            Br smirk dk bangok "You going to be able to get up?"
            c "Might take me a moment."
        "Wh- You bit me!":
            $ brycemood -= 2
            Br stern dk bangok "I did not bite down. You drove your crotch into my teeth."
            Br brow dk bangok "I was doing my best to keep you safe from them, but there was only so much I could do."
        "Recovering.":
            pass
    m "Catching my breath, I struggled up."
    $ bangok_four_bryce1_wstiming = None

    Br smirk dk bangok "Now, I believe it's my turn?"
    label bangok_four_bryce1_f_preciprocity_menu:
    menu:
        "Oh, fuck me.":
            jump bangok_four_bryce1_f_fuck
        "Yep. Time for me to taste you.":
            jump bangok_four_bryce1_oralbot
        "Take my ass.":
            jump bangok_four_bryce1_analbot
        "Handjob okay?":
            jump bangok_four_bryce1_hand
        "I'm not sure I can fit you." if bangok_four_bryce1_m2_fit:
            call bangok_four_bryce1_m2_fit from bangok_four_bryce1_f_preciprocity_menu_fit
            jump bangok_four_bryce1_f_preciprocity_menu
        "I... think I'm done.":
            Br brow dk bangok "Excuse me?"
            c "I'm..."
            $ renpy.pause (0.8)
            c "I think I'm going to pass out now."
            Br stern dk bangok "Hey!"
            scene black with fade
            play sound "fx/impact3.ogg"
            jump bangok_four_bryce1_badmorning









label bangok_four_bryce1_f_fuck:
    call bangok_four_bryce1_position("vag")
    m "Bryce gestured to his couch."
    $ renpy.pause(0.5)
    scene bangok_four_bryce1_apartment night ceiling at Pan((0,360), (0,0), 2.0) with dissolve
    c "You coming?"
    show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=0.8) with dissolve
    Br flirty dk bangok "I will be."
    menu:
        "W-Wait! Protection!":
            m "I sat up, keeping him from getting on top of me."
            scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
            show bryce brow dk bangok
            with dissolvemed
            Br "Is that really necessary? We're different species. Kids aren't happening."
            menu:
                "[[Insist.]":
                    $ brycemood -= 1
                    call bangok_four_bryce1_setprotected(True) from bangok_four_bryce1_f_fuck_protected
                    c "We don't know what your fluids might do to me."
                    show bryce stern dk bangok with dissolve
                    m "Bryce groaned, then gestured to a nearby chest of drawers."
                    Br "Top, I think. Just hurry up."
                    label bangok_four_bryce1_f_fuck_getprotection:
                    play sound "fx/rummage.wav"
                    m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one at random."
                    if persistent.bangok_balls == True:
                        m "Tearing into the packaging, I returned with the necessary equipment and knelt to roll it down over his cock, right down to his slightly-slick balls."
                    else:
                        m "Tearing into the packaging, I returned with the necessary equipment and knelt to roll it down over his cock."
                "[[Take his load.]":
                    call bangok_four_bryce1_setprotected(False) from bangok_four_bryce1_f_fuck_rejectprotection
                    c "Fair point."
            Br flirty dk bangok "Now, where were we?"
            scene bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,0), 2.0)
            show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=0.8)
            with fade
            m "In a blink, I was back on the couch."
        "[[Spread your legs.]":
            call bangok_four_bryce1_setprotected(False) from bangok_four_bryce1_f_fuck_noprotection
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.6) with ease
    m "Bryce stood over me, winking again as I threw one leg over the couch back, and let the other drop off the front, trying to open enough room for him to get in."
    Br "Give me a sec to figure out how to aim this."
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
    m "Bryce clambered overtop me, hindlegs still on the floor while he braced his forelegs against the couch. The warmth radiating off his underbelly suffused my naked skin."
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
    m "His cock bounced lewdly off my legs as he aimed for what we both wanted."
    Br laugh dk bangok "There!"
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
    m "His large tip slipped inside my slick vagina easily, spearing me open and sending sparks of pleasure down my legs that left them limp."
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
    m "Whatever noise I made in response evidently worried Bryce, as he immediately tugged back out."
    Br stern dk bangok "[player_name]? Are you okay?"
    m "I nodded, throat working to find my voice again."
    $ renpy.pause(0.8)
    c "Y-Yeah. Keep going."
    label bangok_four_bryce1_f_fuck_merge:
    Br flirty dk bangok "Oh? Alright then."
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
    m "He pressed back up against, then inside my cunt in one smooth motion, whiting out every nerve south of my waist with another wave of pleasure."
    m "There he paused a moment, letting me adjust."
    $ renpy.pause(0.8)
    Br smirk dk bangok "Further?"
    menu:
        "P-please.":
            pass
        "Yes!":
            pass
        "You gonna go this slowly all night?":
            $ brycemood += 1
            play sound "fx/tableslap.wav"
            Br laugh dk bangok "Not if you keep saying things like that!"
            Br smirk dk bangok "But we'll take it easy for now. I don't want to hurt you."
    $ renpy.pause(0.5)
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.0) with ease
    m "He pushed further in, slower now. Electric sparks danced through my belly as every nerve pressed in against the sliding intruder."
    m "Then he reached something."
    c "S-Stop!"
    m "Bryce froze instantly, waiting for me to explain, or give him more instructions. I wiggled slightly, trying to get a feel for what was going on."
    m "With a start, I realized he was so deep, he was pressing up against my cervix!"
    if persistent.bangok_cervpen != True:
        c "I can't go deeper than this."
        jump bangok_four_bryce1_f_fuck_nowomb
    menu:
        "Press through, {i}carefully{/i}.":
            Br stern dk bangok "What is it?"
            c "Y-You're right up against my womb."
            Br brow dk bangok "You're sure you want me to keep going?"
            menu:
                "Yes.":
                    $ bangok_four_bryce1.fuckwomb = True
                    show bangok_four_bryce_underside_large:
                        ease 4.0 ypos (-2.1)
                    m "Moving with the uptmost care, Bryce gradually applied more pressure to my cervix."
                    m "I struggled to relax, to breathe, to not tense up while he entered my deepest center."
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.12) with ease
                    m "We both gasped when his tip was through."
                    menu:
                        "F-Fuck yes.":
                            pass
                        "Ow! Ow! T-Too much!":
                            $ brycemood -= 1
                            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.04) with ease
                            m "Bryce pulled back immediately, wrenching his tip back past my cervix, but letting the spasming inner sphincter close."
                            c "Agh. Fuck."
                            Br stern dk bangok "We're not going that deep again."
                            $ bangok_four_bryce1.fuckwomb = False
                            menu:
                                "But...":
                                    $ brycemood -= 1
                                    Br stern dk bangok "[player_name], that hurt you. Neither of us are sober enough to get you to a hospital."
                                    c "..."
                                "Thanks.":
                                    $ brycemood += 1
                            $ renpy.pause(0.8)
                            jump bangok_four_bryce1_f_fuck_postwomb
                        "I might be ruined for humans after this.":
                            Br stern dk bangok "Ruined? What do you mean?"
                            c "Your size is incredible. No humans are this large."
                            Br smirk dk bangok "Ah."
                            $ brycemood += 1
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.14) with ease
                    if persistent.bangok_balls == True:
                        if persistent.bangok_inflation == True:
                            m "He pressed deeper, until I felt the large, warm orbs of his balls resting on my buttcheeks, his thighs pressing up against mine."
                        else:
                            m "He pressed deeper, until I felt the warm orbs of his balls resting on my buttcheeks, his thighs pressing up against mine."
                    else:
                        m "He pressed deeper, until I felt the warm scales on his thighs pressing up against mine."
                    m "Every milimeter sliding past my cervix electrified my innards, even more pleasurable than his entry into my outer cunt."
                "No.":
                    $ bangok_four_bryce1.fuckwomb = False
                    c "I'm not sure. I don't know if I've ever..."
                    $ renpy.pause(0.8)
                    Br stern dk bangok "..."
                    $ renpy.pause(0.8)
                    Br "We'd better not risk it."
                    c "Okay."
        "I can't go deeper than this.":
            label bangok_four_bryce1_f_fuck_nowomb:
            $ bangok_four_bryce1.fuckwomb = False
            Br brow dk bangok "Am I hurting you being this deep?"
            c "N-No. But any farther and you'll be fucking my womb."
            Br stern dk bangok "Got it."

label bangok_four_bryce1_f_fuck_postwomb:
    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is not None:
        m "Bryce took a breath, wincing."
        Br brow dk bangok "Still want me to take a leak in you? I'm not as sure about it being safe in your..."
        menu:
            "Piss away. Right now.":
                label bangok_four_bryce1_f_fuck_postwomb_wsnow:
                $ bangok_four_bryce1_wstiming = "before"
                $ brycemood += 1
                Br smirk dk bangok "Alright."
                $ renpy.pause(0.3)
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                m "Bryce's shaft twitched, then expanded as he let his bladder go."
                Br laugh dk bangok "Ahhh..."
                if bangok_four_bryce1_protected == True:
                    if bangok_four_bryce1.fuckwomb == True:
                        m "Warmth blossomed in my deepest recesses, filling me with an indescribable contentment and ecstacy as Bryce urinated directly into the condom in my womb."
                    else:
                        m "Warmth blossomed in my deepest recesses, filling me with an indescribable contentment and ecstacy as Bryce's piss filled the condom's reservoir in what little space remained in my passage."
                        m "He shifted slightly, kissing his tip to my inner gate, urinating through, directly into my womb."
                        play sound "fx/bubbles.ogg"
                        m "The condom's reservoir followed, slipping inside and expanding outward."
                    if persistent.bangok_inflation == True:
                        m "His liquid just kept coming, filling my sacred temple like a toilet bowl.{w=0.5} I squirmed, unable to escape the glorious pressure as I was forced to expand around his stretching piss balloon."
                        $ bangok_four_bryce1_playerstuffed = True
                else:
                    if bangok_four_bryce1.fuckwomb == True:
                        m "Warmth blossomed in my deepest recesses, filling me with an indescribable contentment and ecstacy as Bryce urinated directly into my womb."
                    else:
                        m "Warmth blossomed in my deepest recesses, filling me with an indescribable contentment and ecstacy as Bryce's piss filled what little space remained in my passage, then leaked through my cervix and into my womb."
                        m "He shifted slightly, kissing his tip to my inner gate, urinating through, directly into my deepest recesses."
                    if persistent.bangok_inflation == True:
                        m "His liquid just kept coming, filling my sacred temple like a toilet bowl.{w=0.5} I squirmed, unable to escape the glorious pressure as I was forced to expand around his piss."
                        $ bangok_four_bryce1_playerstuffed = True
                stop soundloop fadeout 1.0
                Br smirk dk bangok "Damn. You're wild."
                Br flirty dk bangok "Might not have taken a piss since the shift started at the station. Hope you don't mind."
                $ renpy.pause(0.8)
                Br flirty dk bangok "Good?"
                m "I nodded, lost in the warmth and fullness."
                Br smirk dk bangok "Alright. Let's keep things moving."
            "After you cum.":
                $ bangok_four_bryce1_wstiming = "after"
                c "Let's, ah, make sure I can deal with that first."
                Br normal dk bangok "Sure. Think I can hold it."
            "M-Maybe not.":
                label bangok_four_bryce1_f_fuck_postwomb_emptytank:
                $ bangok_four_bryce1_wstiming = None
                Br stern dk bangok "Then I gotta go. Fast."
                if bangok_four_bryce1.fuckwomb == True:
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.04) with ease
                    m "His abrupt tug back past my cervix left me too weak to move, nor even think for a long moment."
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
                m "I lay, utterly blissed out as his column of man-meat tugged back out of me, leaving me soaked with anticipation, but empty."
                hide bangok_four_bryce_underside_large with easeoutbottom
                scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0) with fade
                m "When he had dragged himself completely free, thought returned to me, and my first thought was a weird one."
                call bangok_four_bryce1_ws_emptying_the_tank(False, bangok_four_bryce1_protected)
                if bangok_four_bryce1_protected == True:
                    m "The condom still hung from his dick, a bobbing, hypnotizing balloon full of piss."
                    menu:
                        "[[Drink it.]":
                            m "I pinched off his condom near the tip, then took the ring at the base and slid the whole thing off. The smell of urine hit like an aphrodisiac."
                            show bryce flirty dk bangok with dissolve
                            m "Before I could think about what I was doing, I had the ring in my mouth, and was lifting the balloon up over my head."
                            show bryce smirk dk bangok with dissolve
                            play sound "fx/water2.ogg"
                            if persistent.bangok_inflation == True:
                                queue sound "fx/gulpslow2.wav"
                                $ renpy.pause (9.0)
                                m "It was a huge volume. I had to pause and take a break partway through. When I finished, I felt packed with the warmth that had so recently left Bryce's bladder."
                            else:
                                queue sound "fx/gulping.wav"
                                $ renpy.pause (3.0)
                                stop sound fadeout 1.0
                            python:
                                brycemood += 1
                                bangok_four_bryce1_playerstuffed = True
                            Br flirty dk bangok "That was hot to watch."
                            m "Slurping the last from the now empty condom, I shoved it back down over his dick."
                            c "Stick that thing back in me."
                        "[[Replace it.]":
                            m "I pinched off his condom near the tip, then took the ring at the base and slid the whole thing off. The smell of urine hit like a wave."
                            m "Tying it, I rolled it aside across his floor. Then I wandered back to his condom drawers for another one."
                            c "Let's get back to it."

                scene bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,0), 2.0)
                show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=-1.5)
                with dissolvemed
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.0) with ease
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.1) with ease
                m "Bryce filled me again, completing the hole between my legs."
                if bangok_four_bryce1.fuckwomb == True:
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.14) with ease
                    m "Then he was back past my cervix, and coherent thought abandoned me for a long moment."

    elif persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is None:
        Br stern dk bangok "Mmh."
        Br stern dk bangok "Damn."
        c "Huh?"
        Br "All that drinking earlier means I kinda gotta {i}go{/i}."
        if bangok_four_bryce1_playercame == True:
            Br smirk dk bangok "Just like you did."
        Br brow dk bangok "Does that... matter to you at all?"
        menu:
            "What? {i}In{/i} me?":
                $ brycemood -= 2
                Br stern dk bangok "Not with that kind of reaction."
                jump bangok_four_bryce1_f_fuck_postwomb_emptytank
            "Go take care of your business.":
                $ brycemood -= 1
                jump bangok_four_bryce1_f_fuck_postwomb_emptytank
            "I might be interested.":
                Br smirk dk bangok "Now, or later? My bladder's leaning toward now."
                menu:
                    "Now.":
                        jump bangok_four_bryce1_f_fuck_postwomb_wsnow
                    "After you cum.":
                        $ bangok_four_bryce1_wstiming = "after"
                        c "Let's, ah, make sure I can deal with that first."
                        Br normal dk bangok "Sure. Think I can hold it."


    if persistent.bangok_balls == True:
        m "He sat like that for a long moment, hilted inside me as I spasmed around him, my clenching nudging his heavy orbs resting against my ass."
    else:
        m "He sat like that for a long moment, hilted inside me as I spasmed around him."
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.95) with ease
    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
        if bangok_four_bryce1_protected == True:
            m "Then he pulled back, stretching the condom through my cervix as his piss balloon refused to pull through."
            Br smirk dk bangok "Guess I better take it easy. Don't want to break that in you."
        else:
            m "Then he pulled back, unplugging my cervix and giving the piss inside somewhere else to go."
            Br smirk dk bangok "Guess I better take it easy. Don't want that spattering everywhere."
    else:
        if bangok_four_bryce1.fuckwomb == True:
            if bangok_four_bryce1_protected == True:
                m "Then he pulled back, leaving my inner gate clenching at nothing but the condom's reservoir."
            else:
                m "Then he pulled back, leaving my inner gate clenching at nothing but his very tip."
            Br laugh dk bangok "It's like you've got a mouth in there!"
            Br flirty dk bangok "Mind if I keep fucking it?"
        else:
            m "Then he pulled back, leaving my canal wide and aching for him."
            Br "Ready?"
    c "Y-Yeah."

    $ renpy.pause(0.5)

    if bangok_four_bryce1.fuckwomb == True:
        play soundloop "fx/rub2.ogg" fadein 1.0
        show bangok_four_bryce_underside_large:
            ease 0.5 ypos (-2.12)
            ease 0.7 ypos (-2.0)
            repeat
        $ renpy.pause(0.8)
        if persistent.bangok_balls == True:
            m "Bryce began to fuck me for real, slapping my asscheeks with his balls, keeping most of his shaft inside as he breached my womb again and again."
        else:
            m "Bryce began to fuck me for real, keeping most of his shaft inside as he breached my womb again and again."
        if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
            m "Piss leaked back and forth inside of me, less and less impeded by my innermost gate as his thrusts spread it wide."
    else:
        play soundloop "fx/rub2.ogg" fadein 1.0
        show bangok_four_bryce_underside_large:
            ease 0.5 ypos (-2.0)
            ease 0.7 ypos (-1.9)
            repeat
        $ renpy.pause(0.8)
        m "Bryce began to fuck me for real, spearing my love passage with gusto."
        if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
            m "Piss leaked back and forth inside of me, slowly less impeded by my innermost gate as his thrusts pushed the fluid through."

    m "I didn't stand a chance."
    $ bangok_four_bryce1_playercame = True
    show black with fadequick
    c "Ah! Bryce!"
    $ renpy.pause(0.8)
    hide black with dissolveslow
    $ renpy.pause(0.5)

    m "Coming down from my high took some time, as throughout he kept up his pace."
    $ renpy.pause(1.0)
    m "I was sure every muscle in my lower body would be inaccessible for days, as each thrust put yet another wave of pleasure crashing on the shores of my mind."

    if persistent.bangok_knot == True:
        if bangok_four_bryce1.fuckwomb == True:
            Br stern dk bangok "In or out?"
            c "H-Huh?"
            Br brow dk bangok "The knot! In or out?"
            $ renpy.pause(0.5)
            menu:
                "Y-You have a {i}knot{/i}?!":
                    $ bangok_four_bryce1.knotpos = "inoops"
                "In!":
                    $ brycemood += 1
                    $ bangok_four_bryce1.knotpos = "in"
                "Out!":
                    $ bangok_four_bryce1.knotpos = "out"
        else:
            m "Bryce leaned over me, hot, alcohol-drenched breath wafting over my hair."
            Br stern dk bangok "D-Damn it, I want to knot you."
            $ renpy.pause(0.8)
            menu:
                "Y-You have a {i}knot{/i}?!":
                    $ bangok_four_bryce1.knotpos = "out"
                "Th-Then do it!" if persistent.bangok_cervpen:
                    $ bangok_four_bryce1.knotpos = "in"
                "I wish...":
                    $ brycemood += 1
                    $ bangok_four_bryce1.knotpos = "out"
                "D-Don't!":
                    $ bangok_four_bryce1.knotpos = "out"
                "[[Say nothing.]":
                    $ bangok_four_bryce1.knotpos = "out"
    else:
        Br stern dk bangok "Not... Long..."
    stop soundloop fadeout 1.0
    play sound "fx/snarl.ogg"
    if bangok_four_bryce1.knotpos == "in" or (bangok_four_bryce1.knotpos is None and bangok_four_bryce1.fuckwomb == True):
        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.15) with ease
        if bangok_four_bryce1.fuckwomb == False:
            m "I yelped loudly, jolting backward as, with a snarl, Bryce barrelled through my unprepared cervix and came directly into my womb."
        else:
            if bangok_four_bryce1_protected == True:
                if persistent.bangok_balls == True:
                    m "Bryce came, prying my numb legs apart as he forced our hips together, slapping his churning balls against my rear, hilting me to fill his condom inside."
                else:
                    m "Bryce came, prying my numb legs apart as he forced our hips together, hilting me to fill his condom inside."
            else:
                if persistent.bangok_balls == True:
                    m "Bryce came, prying my numb legs apart as he forced our hips together, slapping his churning balls against my rear, hilting me to paint my womb white."
                else:
                    m "Bryce came, prying my numb legs apart as he forced our hips together, hilting me to paint my womb white."
    else:
        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.05) with ease
        if bangok_four_bryce1_protected == True:
            m "Bryce came, stopping with his cockhead in a tight kiss against my inner gate, then jerked back as he began to spurt into the condom reservoir."
        else:
            m "Bryce came, stopping with his cockhead in a tight kiss against my inner gate as he spurted white ropes through it to my womb."

    if bangok_four_bryce1.knotpos == "in" and bangok_four_bryce1.fuckwomb == False:
        play sound ["fx/hit1.ogg", "fx/hit2.ogg"]
        m "The pain was too much for me to take any enjoyment from. I slapped at his belly plates, trying to get him to notice me and pull back out."
    else:
        show black with fadequick
        m "The sensations pushed me over my edge yet again."
        $ renpy.pause(0.8)
        hide black with dissolveslow
        $ renpy.pause(0.5)

    if persistent.bangok_inflation == True:
        m "Bryce didn't slow down, his shaft continuing to twitch and deliver spurt after spurt of cum."
        if bangok_four_bryce1_protected == True:
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                m "The condom's reservoir bloated inside my womb, pressing against every inner recess I had as the cum and piss looked for room to fill me up further."
            else:
                if persistent.bangok_cervpen:
                    m "The condom's reservoir bloated inside my womb, pressing against every inner recess I had as the cum looked for room to fill me up further."
                else:
                    m "The condom's reservoir bloated inside my passage, pressing against every inner recess I had as the cum looked for room to fill me up further."
        else:
            $ bangok_four_bryce1_playerstuffed = True
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                m "Cum and piss saturated my womb, packing my most sacred place with nothing but Bryce's fluids."
            else:
                m "Cum saturated my womb, packing my most sacred place with nothing but Bryce's seed."

        if bangok_four_bryce1.knotpos == "in" and bangok_four_bryce1.fuckwomb == False:
            c "Bryce! {i}Please!{/i}"
        else:
            c "B-Bryce!"
        Br flirty dk bangok "A-Almost..."
        m "Looking down, I found myself almost beginning to look pregnant with dragon cock and fluids."

        if bangok_four_bryce1_protected == True and persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
            play sound "fx/bubbles.ogg"
            c "Ah!"
            m "The condom burst, cum and piss rushing immediately to pack my tubes, saturating my womb, flooding my most sacred places with nothing but Bryce's fluids."
            m "I looked clearly pregnant now, belly bulging upward with a blob of fluid and man meat."
            $ bangok_four_bryce1_playerstuffed = True

    $ renpy.pause(0.8)

    if bangok_four_bryce1.knotpos != "in" or bangok_four_bryce1.fuckwomb == True:
        show bangok_four_bryce_underside_large:
            ease 1.0 ypos -2.0
            ease 1.0 ypos -1.7
            ease 1.0 ypos -1.3
            ease 1.0 ypos -0.7
    else:
        show bangok_four_bryce_underside_large:
            ease 1.0 ypos -2.0
            ease 1.0 ypos -1.7
    m "After a long moment of climax inside me, Bryce worked his way back with his forelegs, keeping his hips and cock where they were as he curled over to look down at me."
    $ bangok_four_bryce1_brycecame = True


    if bangok_four_bryce1.knotpos == "in" and bangok_four_bryce1.fuckwomb == False:
        m "His face fell immediately."
        $ brycemood -= 3
        Br brow dk bangok "What?"
        Br stern dk bangok "Fuck. Fuck!"
        m "It was hard not to be on the verge of tears as I twitched a hand over my womb, as if that would get his cock back on the correct side of my innermost gate."
        c "J-Just get it out."

        m "He braced his forelegs against my shoulders and pulled, but that only wrenched another cry of pain from me as the bulge at his base threatened to tear my vaginal lips apart."
        Br stern dk bangok "Damn it, [player_name]. Why did you encourage me?"
        menu:
            "I'm sorry.":
                $ brycemood += 1
                c "I didn't mean... I didn't think..."
                c "I thought maybe I could..."
                c "But I can't..."
            "I didn't think you would!":
                $ brycemood -= 2
                c "Y-You're the one who fucked this up!"
                c "I was having a great time until y-you tried to split me open!"
                c "Get it out!"
            "Please...":
                $ brycemood -= 1
                c "It hurts."
        Br stern dk bangok "I'm trying."
        m "He dropped his angle and the pain lessened to a good degree, but his knot was still too much to remove."
        Br stern dk bangok "I don't think I can."
        menu:
            "Thanks... for trying.":
                c "It's... it's better."
                Br normal dk bangok "Enough to sleep with?"
                c "Maybe."
            "Fuck you.":
                $ brycemood -= 2
                Br stern dk bangok "If you hadn't encouraged me, we wouldn't be in this."
        Br brow dk bangok "I think our only option is to try to sleep it off."
        if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
            c "Don't you still need to piss?"
            if brycemood < 0:
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                m "No sooner had I asked the question than I felt a different viscosity of warmth injected into my plugged-up womb."
                Br stern dk bangok "Bad moment to ask."
                menu:
                    "Fuck you!":
                        $ brycemood -= 2
                        Br stern dk bangok "I tried to warn you when I asked before."
                        c "You weren't fucking hilted through my cervix!"
                    "Oh.":
                        $ renpy.pause(0.5)
                label bangok_four_bryce1_f_fuck_badknot_piss:
                if persistent.bangok_inflation == True:
                    m "I squirmed, the added pressure on my cervix from the injected piss causing fresh spasms. My movements only made things worse."
                    if bangok_four_bryce1_protected == True:
                        play sound "fx/bubbles.ogg"
                        c "Ah!"
                        m "The condom burst, cum and piss rushing immediately to pack my tubes, saturating my womb, flooding my most sacred places with nothing but Bryce's fluids."
                        m "I looked clearly pregnant now, belly bulging upward with a blob of fluid and man meat."
                        Br stern dk bangok "Sorry."
                stop soundloop fadeout 1.0
                menu:
                    "I think I might survive.":
                        $ brycemood += 1
                    "Never should have let you near my pussy.":
                        $ brycemood -= 2
            else:
                Br stern dk bangok "I do. Barely holding it."
                menu:
                    "Try to hold it?":
                        Br stern dk bangok "I'll try."
                    "Okay...":
                        Br normal dk bangok "You're sure?"
                        c "I don't see how it could make things worse."
                        $ renpy.pause(0.5)
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        $ renpy.pause(0.8)
                        jump bangok_four_bryce1_f_fuck_badknot_piss
        jump bangok_four_bryce1_tiedsleep

    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
        Br flirty dk bangok "Ready for part two?"
        if persistent.bangok_inflation == True:
            c "Uh."
        else:
            c "Mhmm."
        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
        m "With a grunt, Bryce leaned forward, then his cock twitched inside me again. A new, less viscous warmth began spreading in my most sacred places."
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        Br laugh dk bangok "Ahhh..."
        if persistent.bangok_inflation == True and bangok_four_bryce1_protected == True:
                play sound "fx/bubbles.ogg"
                c "Ah!"
                m "The condom burst, cum and piss rushing immediately to pack my tubes, saturating my womb, flooding my most sacred places with nothing but Bryce's fluids."
                $ bangok_four_bryce1_playerstuffed = True
        elif bangok_four_bryce1_protected == True:
            m "I moaned, body numb but for the feeling of bryce pissing in the balloon of defilement, so thinly separated from my innermost space."
        else:
            $ bangok_four_bryce1_playerstuffed = True
            m "I moaned, body numb but for the feeling of bryce pissing in my innermost temple until every surface inside was seeping in his urine."
        if persistent.bangok_inflation == True:
            m "I looked clearly pregnant now, belly bulging upward with a blob of fluid and man meat."

        stop soundloop fadeout 1.5
        m "Bryce worked his way back down to look me in the eyes."
        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.7) with ease
        Br flirty dk bangok "Might not have taken a piss since the shift started at the station. Hope you don't mind."

    if persistent.bangok_inflation == True:
        m "He rubbed my protruding belly with a paw."
        Br flirty dk bangok "Sure did fill you up, huh?"
        m "I couldn't answer as I lay basking under the warm fluid result of our coitus."

    if persistent.bangok_watersports and persistent.bangok_inflation and bangok_four_bryce1_protected:
        $ brycemood += 1
        Br stern dk bangok "Oh. Fuck. I think the condom broke."
        menu:
            "Obviously!":
                $ brycemood -= 2
                Br "I didn't exactly have control over its integrity."
                c "Not pissing in it could've saved it."
                Br "And who said they were okay with that?"
            "Damn.":
                Br "Yeah, sorry."
                Br flirty dk bangok "Good fuck, though?"
                m "I nodded."
            "That felt kinda good...":
                Br flirty dk bangok "Did it?"
    else:
        Br flirty dk bangok "Good?"
        m "I nodded."

    if persistent.bangok_knot == True and bangok_four_bryce1.knotpos == "in":
        Br flirty dk bangok "I hope you liked it, 'cause I don't think your pussy will stretch to let the knot back out anytime soon."
        jump bangok_four_bryce1_tiedsleep
    else:
        if brycemood < 0:
            jump bangok_four_bryce1_f_fuck_pullout
        else:
            Br "Want me to pull out? Or do you want to sleep like this?"
            menu:
                "Sleep like this.":
                    $ brycemood += 1
                    scene black with dissolveslow
                    m "Bryce slumped on top of me on the couch, taking care to shift me to the edge so he wouldn't crush me."
                    if bangok_four_bryce1_protected == False or (persistent.bangok_watersports and persistent.bangok_inflation):
                        m "He adjusted his hips too, pressing the tip of his shaft up against my cervix to help prevent leaks."
                    Br smirk dk bangok "Goodnight, [player_name]."
                    jump bangok_four_bryce1_morningcouch
                "Pull out.":
                    label bangok_four_bryce1_f_fuck_pullout:
                    scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
                    show bryce stern dk bangok
                    with dissolvemed
                    if (persistent.bangok_watersports and persistent.bangok_inflation and bangok_four_bryce1_protected) or not bangok_four_bryce1_protected:
                        # Broken condom or no condom
                        play sound ["fx/slide.ogg"] fadein 0.5
                        m "Bryce's shaft retreated from my depths, followed by a slow flow escaping my womb."
                        # TODO?: Cunnilingus?
                    elif persistent.bangok_inflation:
                        # FULL condom
                        play sound "fx/slide.ogg" fadein 0.5
                        m "Bryce tugged, but couldn't drag the condom's inflated reservoir past my cervix."
                        Br stern dk bangok "Damn. I'm not sure we can get that out without breaking it."
                        c "Hold on, just..."
                        m "I wrapped my arms around his broad shoulders."
                        c "Now lean back? Maybe with the back of the couch?"
                        play sound "fx/pour.ogg"
                        $ renpy.pause(3.0)
                        m "Fluid drained from my womb, through my cervix and into the condom around Bryce's shaft, spreading the condom against my walls even more tightly."
                        c "Pull."
                        play sound "fx/uncork.ogg"
                        m "I lost my grip as his shaft slid free, the feeling of the last bubble of fluid popping through my cervix enough to weaken me again, leaving me achingly empty when the feeling passed."
                    else:
                        # Regular used condom.
                        play sound ["fx/slide.ogg","fx/uncork.ogg"] fadein 0.5
                        if persistent.bangok_watersports and bangok_four_bryce1_wstiming is not None:
                            m "Bryce tugged himself free, the blob of cum and piss he'd deposited though my innermost gate into the condom's reservoir tugging through my cervix with a knee-shaking burst of pleasure."
                        else:
                            if persistent.bangok_cervpen:
                                m "Bryce tugged himself free, the blob of cum he'd deposited in the condom's reservoir tugging through my cervix with a knee-shaking burst of pleasure."
                            else:
                                m "Bryce tugged himself free, the blob of cum he'd deposeted in the condom's reservoir dragging through my passage with a knee-shaking slide of pleasure."
        if brycemood < 0:
            Br stern dk bangok "Floor's open. Or you can find your way home like that."
            m "I struggled even to get off the couch, my legs still too weak to support me."
            c "Floor is good..."
            play sound "fx/impact3.ogg"
            scene black with vpunch
            jump bangok_four_bryce1_morningfloor
        else:
            Br normal dk bangok "You want to stay on the couch there?"
            m "I nodded."
            c "Not sure I can move after that. Damn."
            Br flirty dk bangok "Well, I'm about ready to pass out."
            scene black with dissolveslow
            Br "Goodnight, [player_name]."
            c "G'night."
            jump bangok_four_bryce1_morningcouch


















label bangok_four_bryce1_m:
    show bryce brow dk bangok with dissolve
    $ renpy.pause(0.9)
    m "Bryce didn't look impressed."
    c "You're like twice my size. Of course you're bigger."
    if persistent.bangok_balls:
        Br "No, no. I get that. Where's your slit?"
        c "Slit? {w=0.8}I don't have one of those."
        Br smirk dk bangok "So your parts just hang out like that? Undefended? With that limp shaft?"
    else:
        Br "No, no. I get that. What's that underneath?"
        c "Hm? {w=0.8}Oh, balls. That's where the sperm comes from."
        Br smirk dk bangok "They just hang out like that? Undefended? Under that limp shaft?"
    c "Yeah. Though, uh, not s'posed to be limp right now. Whiskey dick, I guess."
    $ renpy.pause(0.5)
    Br flirty dk bangok "Are your balls sensitive?"
    c "... Not sure I like where this is going."
    show bryce at Position(ypos=1.3) with ease
    show bryce at Position(ypos=1.5) with ease
    m "Bryce stumbled a little closer, tongue out with a wide-grinned wink."
    menu:
        "[[Let him.]":
            pass
        "Watch the horns!":
            c "I'm kinda delicate!"
            Br smirk dk bangok "I'll be careful."
        "[[Stop him.]":
            m "I took a step back and Bryce abruptly stopped."
            show bryce at center with ease
            c "{i}Really{/i} sensitive. I don't think it's a good idea if you..."
            show bryce normal dk bangok with dissolve
            show bryce at Position(ypos=1.3) with ease
            $ renpy.pause(0.4)
            show bryce at center with ease
            Br smirk dk bangok "Alright."
            jump bangok_four_bryce1_m2

    show bryce flirty dk bangok with dissolve
    m "Bryce's hot, alcohol-tinged breath sent shivers through my groin.{w=0.3} Bypassing my man-meat, he wrapped his tongue around the base of my sack and tugged experimentally."
    m "Having that much bumpy tongue running over my balls was such a new and different experience, my shaft jumped to attention immediately, bopping his snout."
    show bryce smirk dk bangok at Position(ypos=1.3) with ease
    Br flirty dk bangok "Now you're hard."
    c "Yep. That, ah, that was new."
    Br laugh dk bangok "New for me too!"
    show bryce normal dk bangok with dissolve
    show bryce at center with ease
    if persistent.bangok_balls:
        Br normal dk bangok "Never seen things... just always outside like that. Dry skin tastes weird too."
    else:
        Br normal dk bangok "Never seen things... outside like that. Skin tastes weird too."
    c "Good weird or bad weird?"
    Br brow dk bangok "Different."

label bangok_four_bryce1_m2:
    Br normal dk bangok "What next? You want me on top? Or do you want to stick that little thing in me?"
    $ bangok_four_bryce1_m2_size = True
    $ bangok_four_bryce1_m2_fit = True
    label bangok_four_bryce1_m2_menu:
    menu:
        "I want to taste you.":
            $ bangok_four_malepartners += 1
            label bangok_four_bryce1_oralbot:
            call bangok_four_bryce1_position("oralbot")
            Br smirk dk bangok "Would you, now?"
            play sound "fx/cartslide.ogg"
            show bryce normal dk bangok at Position(xpos=0.4,xanchor='center') with dissolve
            show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
            m "Bryce settled back on the couch, bunching the rug and tugging the coffee table as his tail caught for a moment."
            m "He splayed one hindleg out, giving me easy access to his shaft from beside the couch."
            Br flirty dk bangok "Come on over."
            if bangok_four_bryce1_protected == False and not bangok_four_bryce1_playercame:
                m "My addled brain managed to push through an important thought before I followed his order."
                c "Wait, what about protection?"
                if bangok_four_playerhasdick == True:
                    Br brow dk bangok "You're kidding, right? Kids don't happen from oral. And we're both guys."
                else:
                    Br brow dk bangok "You're kidding, right? Kids don't happen from oral."
                Br smirk dk bangok "Unless there's something about humans I'm not understanding."
                c "No, it's basically like that."
                Br "Then what's the problem?"
                menu:
                    "[[Insist.]":
                        c "We don't know what your stuff might do to me."
                        if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                            c "I've seen a health aisle. You've got condoms."
                        else:
                            c "Your kind has condoms, right?"
                        show bryce stern dk bangok with dissolve
                        m "Bryce groaned, then gestured at a chest of drawers in a corner."
                        Br "Top. I think. Just hurry up."
                        label bangok_four_bryce1_oralbot_getprotection:
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.wav"
                        if bangok_four_playerhasdick == True:
                            m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one labeled safe for oral, then dug a little deeper for one my size, in case things went further."
                            m "Only after I dug to the bottom did I finally find a box of condoms closer to my scale, unopened."
                        else:
                            m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one labeled safe for oral."
                        m "Tearing into the packaging, I returned with the necessary equipment."
                        label bangok_four_bryce1_oralbot_condom:
                        m "I knelt next to bryce, feeling saliva building up in my mouth as I unrolled rubbery safety along his shaft."
                        Br flirty dk bangok "D-Damn. That's kinda teasing. Your hands are really smooth."
                        $ brycemood += 1
                    "[[Drink from the tap.]":
                        $ bangok_four_bryce1_protected = False
                        c "There isn't one, I guess."
                        m "I knelt next to Bryce, feeling saliva building up in my mouth from the anticipation."
            elif bangok_four_bryce1_protected:
                menu:
                    "[[Put a condom on him.]":
                        jump bangok_four_bryce1_oralbot_condom
                    "[[Drink from the tap.]":
                        $ bangok_four_bryce1_protected = False
                        m "I knelt next to Bryce, feeling saliva building up in my mouth from the anticipation."
                        Br brow dk bangok "Protection?"
                        c "Changed my mind. I want this."
                        if bangok_four_bryce1_position_picka in ["oraltopwall","oraltopcouch"]:
                            $ brycemood -= 3
                            Br stern dk bangok "And I wanted to taste your load too. But you wanted to protect me from it. How are you so sure mine won't hurt you?"
                            c "I suppose I'm not."
                            Br "..."
                            m "He didn't stop me as I leaned in closer."

            if bangok_four_bryce1_protected:
                m "Leaning over Bryce's belly and hindlegs, I gripped Bryce's shaft around the condom lightly near the base. I wasn't quite sure how rough I could be with it, with him being a different species."
            else:
                m "Leaning over Bryce's belly and hindlegs, I gripped Bryce's shaft lightly near the base. I wasn't quite sure how rough I could be with it, with him being a different species."

            Br laugh dk bangok "H-Hey! Don't {i}tickle{/i} it!"
            m "Tightening my grip, I gave an experimental pump up and down, before letting go and glancing up at him for approval."
            Br flirty dk bangok "B-Better."

            if not bangok_four_bryce1_protected:
                m "I locked eyes with the tip of his shaft, which had rewarded me with a glistening drop of pre."

            if persistent.bangok_watersports == True:
                call bangok_four_bryce1_ws_conversation from bangok_four_bryce1_oralbot_ws_conversation
                if bangok_four_bryce1_wstiming not in ["before","after"]:
                    show bryce normal dk bangok at Position(xpos=0.4,xanchor='center') with dissolve
                    show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
                    if bangok_four_bryce1_protected:
                        m "Bryce lay back down on the couch. As soon as he was settled, I pulled the condom back over his shaft."
                    else:
                        m "Bryce lay back down on the couch."

            m "Adjusting my position, I lay over one of his hindlegs to put my face even with his tip, while also being able to look up at his face."
            if bangok_four_bryce1_protected:
                m "Then my lips met his tip, slightly spreading the condom and tugging on the reservoir as I began careful exploration of how much I could fit."
            else:
                if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming not in ["before","after"]:
                    m "Then my lips met his tip. I could still pick up a little tang from his recent urination, and I wondered to myself why I asked him to get rid of the golden liquid."
                else:
                    m "Then my lips met his tip. His pre, far from my understanding of the human variety, was actually borderline sweet!"
                m "I sank downward a small amount, beginning a careful exploration of how much I could fit."
            if persistent.bangok_balls == True:
                if persistent.bangok_inflation == True:
                    m "As I explored his tip, I gently began lifting and massaging his warm, heavy balls. I could feel the weight of the seed inside as I toyed with them. Their scaleless surface was still slightly damp from the inside of his slit."
                else:
                    m "As I explored his tip, I gently began lifting and massaging his warm balls. I could feel that the scaleless surface was still slightly damp from the inside of his slit."
            m "His reaction was not what I was expecting."
            Br smirk dk bangok "If you want to take it this slowly, we could be here all night. You've barely even used your tongue yet."
            m "When I released his tip with a wet pop, his expression changed."
            Br brow dk bangok "What was that?"
            menu:
                "Suction.":
                    c "Human lips can seal pretty well. Guess you haven't felt that before, huh?"
                    Br flirty dk bangok "Guess not. But I'd like to feel it again."
                "You'll find out.":
                    $ brycemood += 1
                    Br flirty dk bangok "Feels good, whatever it is."
            $ renpy.pause (0.8)
            show bryce stern dk bangok with dissolve
            $ renpy.pause (0.3)
            m "His hindleg flexed under me and he grimaced."
            Br "We might need a different position. Here."
            play sound "fx/cartslide.ogg"
            show bryce normal dk flip bangok with dissolvemed
            m "Leaning back, I gave Bryce room as he turned to his side. The couch complained under his efforts."
            m "Now, though, his shaft swung pendulously out in front of me, easily accessible."
            Br flirty dk flip bangok "Better?"
            c "Much."

            if bangok_four_bryce1_protected:
                m "I took hold of his shaft again to steady it, then enveloped his whole head. The reservoir of the condom slid down my tongue as I did my best to sink my lips further down. It came to rest hanging somewhere in my throat, as his large head bumped the back of my mouth and I gagged."
            else:
                m "I took hold of his shaft again to steady it, then enveloped his whole head. The skin of his cockhead was smooth, almost already a little moist. He tasted like..."
                menu:
                    "Dragon.":
                        m "There really wasn't a better word I could use for it."
                    "Beer.":
                        m "There was an aftertaste of hops and alcohol to his shaft. I had to wonder if that was an affect of how much he drank, an accidental spill, or uncleaned residue of a previous drunken oral encounter."
                    "Slit juices.":
                        m "Slightly salty, the moistness came from some kind of lubricating agent already on his shaft. "
                    "Human fluids." if persistent.bangok_cloacas and bangok_four_bryce1_position_picka=="ptop" and not bangok_four_bryce1_protected_a:
                        m "Thanks to his shaft and ass sharing the same hole on his body, I could taste some of the result of my fucking him on his cock. That combined with his natural taste was an incomprable pallete."

            m "As I sucked in my cheeks, making a vacuum in my mouth around his head, Bryce kicked one of his legs into the air."
            Br laugh dk flip bangok "That! That's it!"
            m "I bobbed my head up, then down the short distance I could manage, trying to keep my seal."

            if persistent.bangok_watersports == True:
                if bangok_four_bryce1_wstiming == "after":
                    Br stern dk flip bangok "H-hold on. I need a sec to hold my piss."
                    Br flirty dk flip bangok "Unless you want it now?"
                    menu:
                        "Keep sucking.":
                            label bangok_four_bryce1_oralbot_ws_before:
                            $ bangok_four_bryce1_wstiming = "before"
                            show bryce laugh dk flip bangok with dissolve
                            if bangok_four_bryce1_protected:
                                menu:
                                    "Throat.":
                                        play soundloop "fx/faucet1.ogg" fadein 1.0
                                        queue soundloop "fx/faucet2.ogg"
                                        m "I pushed as far forward as I could without triggering my gag reflex, then {i}sucked.{/i}{w=0.5} Bryce's maw fell open in ectasy as his bladder let go, delivering golden liquid into my throat."
                                        m "But something was wrong. The condom's reservoir was still in my throat, but now it was inflating and sagging downward with the fluid put into it. It was blocking up my throat!"
                                        stop soundloop fadeout 6.0
                                        m "I grabbed Bryce's cock with both hands to secure the condom, then yanked my head back."
                                        play sound "fx/water1.ogg"
                                        m "The condom's bloated reservoir slapped agaisnt the side of the couch with a lewd splat as Bryce finished pissing."
                                        Br flirty dk flip bangok "Little too much?"
                                        m "I nodded, eyes watering, still trying to even my breathing and clear my throat of phlegm."
                                        Br stern dk flip bangok "Wait, are you okay?"
                                        c "Will be."
                                        python:
                                            brycemood -= 2
                                            renpy.pause (1.5)
                                        Br "Don't hurt yourself. I don't think either of us is sober enough to get you to a hospital."
                                        c "..."
                                        $ renpy.pause (0.8)
                                    "Mouth.":
                                        play soundloop "fx/faucet1.ogg" fadein 1.0
                                        queue soundloop "fx/faucet2.ogg"
                                        m "I pulled back so that just Bryce's tip remained in my mouth, expecting what was coming as I continued to suckle.{w=0.5} Bryce's maw fell open in ectasy as his bladder let go, delivering golden liquid into the condom's reservoir."
                                        m "I toyed with the expanding balloon of piss in my mouth for as long as that felt safe,{w=0.5}{nw}"
                                        stop soundloop fadeout 6.0
                                        play sound "fx/water1.ogg"
                                        m "I toyed with the expanding balloon of piss in my mouth for as long as that felt safe,{fast} then let it plop out of my mouth against the side of the couch with a lewd splat as Bryce finished pissing."
                                        Br flirty dk flip bangok "Little too much?"
                                        c "Yeah. But I kinda expected it. You're way larger than me."
                                Br smirk dk flip bangok "I think we're going to need a new condom."
                                menu:
                                    "Get a new condom.":
                                        m "After tugging off and tying off his piss balloon, I went back to the cabinet for another condom for the rest of our suck session."
                                        m "The smell of urine was still strong on his cockhead when I returned, until I rolled the new rubberized safety over it. I stuck it back into my mouth anyway, imagining I could lick and suck out more golden results -- even if that wasn't safe."
                                        $ renpy.pause(0.8)
                                        Br brow dk flip bangok "I don't think just the tip is going to do me."
                                    "Drink his cream from the tap.":
                                        $ bangok_four_bryce1_protected = False
                                        c "Actually, fuck it. I've changed my mind."
                                        $ brycemood += 1
                                        Br smirk dk flip bangok "Oh?"
                                        m "I tugged off and tied off his piss balloon, then aimed his shaft and took his whole head into my mouth unprotected."
                                        m "The unmistakeable tang of urine drowned out any other taste I could get, but a few drops still remained within his urethra, which I eagerly slurped out."
                                        Br flirty dk flip bangok "I-If that's what you want."
                                        show bryce stern dk flip bangok with dissolve
                                        m "He strained, delivering me a little trickle more of urine.{w=0.5} I flushed, thinking about the golden load still in the condom on the floor next to me."
                                        menu:
                                            "Drink his piss.":
                                                m "Bryce frowned as I abandoned his cock, until he saw what I was trying to do."
                                                Br flirty dk flip bangok "Like it that much, huh?"
                                                m "He proffered one of his hindlegs. I used one of its claws to poke a hole higher up in the shaft part of the condom. Then I upturned it into my mouth."
                                                show bryce smirk dk flip bangok with dissolve
                                                play sound "fx/water2.ogg"
                                                if persistent.bangok_inflation == True:
                                                    queue sound "fx/gulpslow2.wav"
                                                    $ renpy.pause (9.0)
                                                    m "It was a huge volume. I had to pause and take a break partway through. When I finished, I felt packed with the warmth that had so recently left Bryce's bladder."
                                                else:
                                                    queue sound "fx/gulping.wav"
                                                    $ renpy.pause (3.0)
                                                    stop sound fadeout 1.0
                                                python:
                                                    brycemood += 1
                                                    bangok_four_bryce1_playerstuffed = True
                                                Br flirty dk flip bangok "That was hot to watch."
                                                m "I wiped my mouth, then took his protruding cock in hand."
                                                c "Not done yet."
                                                m "Sucking on his head, I finally got to taste my first few drops of sweet, sweet pre from him, shockingly contrasting against the pallete-cleanser of piss."
                                                Br laugh dk flip bangok "Go for it."
                                            "Move on.":
                                                pass
                            else:
                                play soundloop "fx/faucet1.ogg" fadein 1.0
                                queue soundloop "fx/faucet2.ogg"
                                m "I pushed as far forward as I could without triggering my gag reflex, then {i}sucked.{/i}{w=0.5} Bryce's maw fell open in ectasy as his bladder let go, delivering golden liquid into my throat."
                                m "It was almost more than I could swallow, the warm stream sloshing back and coating my mouth in that unique tang. My body warmed, heat from Bryce transferred directly into my stomach."
                                stop soundloop fadeout 5.0
                                m "Unfortunately, all good things had to come to an end. He finished, then gave me a satisfied wink."
                                Br flirty dk flip bangok "Might not have taken a piss since the shift started at the station. Hope you don't mind."
                                Br flirty dk flip bangok "Good?"
                                m "I nodded, the head of his cock still in his mouth as I slurped at the tangy tip."
                                Br smirk dk flip bangok "Feel free to keep going."
                        "[[Give him a second.]":
                            show bryce stern dk flip bangok with dissolve
                            m "I stopped my ministrations, waiting for him to get a hold of himself."
                            $ renpy.pause(1.0)
                            Br flirty dk flip bangok "Alright, think you're good."
                elif bangok_four_bryce1_wstiming == "before":
                    Br flirty dk flip bangok "Mind if I take that leak now?"
                    jump bangok_four_bryce1_oralbot_ws_before

            show bryce normal dk flip bangok with dissolve
            m "I popped my mouth free again, getting some full breaths in as I figured out what to do with my hands."
            if bangok_four_bryce1_protected:
                m "I started by working up a fat dollop of spit to add to the surface of the condom, then spread it from his head down his length, easing the passage of my fingers."
            else:
                m "I started by spreading some of the mix of pre and saliva from his head down his length, easing the passage of my fingers slightly."
            m "Then I formed a tight ring with the thumb and index fingers of both hands, circling him."
            show bryce brow dk flip bangok with dissolve
            if persistent.bangok_balls == True:
                m "I took his head in my mouth again, then began to pump my hands and mouth at once. Each time my fingers reached his base, I gave his balls a teasing nudge, stroke, or fondle."
            else:
                m "I took his head in my mouth again, then began to pump my hands and mouth at once."
            show bryce laugh dk flip bangok with dissolve
            m "Bryce threw his head back, lost in the sensations I was providing him."
            c "Mmm. Mmmph?"
            Br flirty dk flip bangok "I don't know! N-Not long!"
            if bangok_four_bryce1_protected:
                m "I kept up my ministrations, treasuring every additional dollop of pre I worked forth into the condom's reservoir, and seeking to wedge ever more shaft into my mouth with each thrust downward."
            else:
                m "I kept up my ministrations, treasuring every additional dollop of pre I worked forth, and seeking to wedge ever more shaft into my mouth with each thrust downward."
            show bryce laugh dk flip bangok with dissolve
            $ bangok_four_bryce1_brycecame = True
            play sound "fx/snarl.ogg"
            if bangok_four_bryce1_protected:
                if persistent.bangok_balls:
                    m "Bryce's balls churned under my fingers. Then his first spurt ballooned the condom's tip abruptly. I let most of his tip out of my mouth, just kissing the very end and giving the reservoir room to expand."
                else:
                    m "Bryce's first spurt ballooned the condom's tip abruptly. I let most of his tip out of my mouth, just kissing the very end and giving the reservoir room to expand."
                m "Even still, it was a formidable load, more and more love-cream pressing the condom against my tongue and mouth's roof."
                play sound "fx/uncork.ogg"
                if persistent.bangok_balls:
                    m "I pulled the bloated reservoir out of my mouth, resting his cockhead against my cheek as I pumped him one-handed and fondled his balls with my other, milking out every last spurt of cum."
                else:
                    m "I pulled the bloated reservoir out of my mouth, holding his cockhead against my cheek as I continued pumping him, milking out every last spurt of cum."
                m "Eventually Bryce finished, slumping onto his back."
                Br flirty dk flip bangok "Damn... that was something else."
                if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
                    $ brycemood -= 1
                    Br stern dk flip bangok "Oh. Didn't think the cum alone would be too much."
                    c "I didn't either, but I can't exactly swallow the condom."
                    Br laugh dk flip bangok "True!"
                    Br normal dk flip bangok "Take it off? I really gotta go take that leak."
                    m "I tugged the condom free, the smell of Bryce's cum hitting me immediately from what remained on his tip, even as I tied off the protection."
                    menu:
                        "Drink his leak.":
                            c "Ah, fuck it."
                            m "I took his head again, grabbing his hips and tugging them as close as I could, nestling his tip at the back of my mouth and just into my throat. His cum, still smeared on his tip, tasted surprisingly sweet."
                            $ brycemood += 1
                            Br flirty dk flip bangok "You sure?"
                            m "A shiver ran through his body, and he winced."
                            Br laugh dk flip bangok "Too late now!"
                            play soundloop "fx/faucet1.ogg" fadein 1.0
                            queue soundloop "fx/faucet2.ogg"
                            m "Warm, golden liquid flooded my throat. It was all I could do to swallow it down as Bryce used my mouth as his urinal."
                            if persistent.bangok_inflation == True:
                                m "Swallowing the rapid stream normally was impossible. It sloshed back as I gagged, washing away the taste of cum in my mouth and replacing it with the tang of piss."
                                m "Not wanting to lose a drop around the seal of my lips, I shoved Bryce's cockhead further than I thought it could go, partway {i}into{/i} my throat, so that he could urinate directly into my guts."
                                $ bangok_four_bryce1_playerstuffed = True
                            else:
                                m "Swallowing the flow was nearly impossible. It sloshed back as I gagged, washing away the taste of cum in my mouth and replacing it with the tang of piss."
                            jump bangok_four_bryce1_oralbot_afterpissend


                        "Let him go.":
                            call bangok_four_bryce1_ws_emptying_the_tank(False)

                else:
                    m "I tugged the condom free, tying it off."
            else:
                label bangok_four_bryce1_oralbot_cum:
                if persistent.bangok_balls:
                    m "Bryce's first spurt hit me in the back of the throat when I was pulling back, dousing my mouth in thick, creamy seed from his churning balls."
                else:
                    m "Bryce's first spurt hit me in the back of the throat when I was pulling back, dousing my mouth in thick, creamy seed."
                m "I switched directions immediately, driving what I could and the next few spurts directly into my throat."
                m "Even still, it was a formidable load, more and more love-cream leaking past his head and filling my mouth with each blast."
                if persistent.bangok_inflation == True:
                    m "I felt light-headed, the seemingly endless stream of cum almost more than I could hold my breath through."
                    if persistent.bangok_watersports == True and bangok_four_bryce1_playerstuffed == True:
                        m "There was no question I wouldn't need to eat or drink after this for quite some time. My belly bulged visibly, stomach and gut packed full with piss and cum."
                    else:
                        m "There was no question I wouldn't need to eat or drink after this for quite some time. My belly bulged slightly, stomach bloated with cum from a much larger partner."
                $ bangok_four_bryce1_playerstuffed = True
                m "Eventually Bryce finished, slumping onto his back."
                Br flirty dk flip bangok "Damn... that was something else."
                if persistent.bangok_inflation == True:
                    m "I let his cock pop free of my lips, struggling to swallow the thick cream accumulated in every nook and cranny of my mouth.{w=0.5} Then, taking his shaft in hand, I began to lick at some of what I'd left stuck to his tip."
                else:
                    m "I let his cock pop free of my lips, swallowing the thick cream accumulated in every nook and cranny of my mouth.{w=0.5} Then, taking his shaft in hand, I began to lick at some of what I'd left stuck to his tip."

                if persistent.bangok_knot == True:
                    m "While he'd cum, a bulge had emerged near the base of his cock, one I hadn't noticed in the heat of the moment."
                    menu:
                        "[[Squeeze it.]":
                            Br laugh dk flip bangok "H-Hey!"
                            Br smirk dk flip bangok "A bit soon to try to get me going again."
                        "[[Leave it.]":
                            pass

                show bryce smirk dk flip bangok with dissolve
                if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
                    c "Got anything to wash this down with?"
                    Br "Plenty."
                    m "I took his head again, grabbing his hips and tugging them as close as I could, nestling his tip at the back of my mouth and just into my throat."
                    Br "Ready?"
                    $ renpy.pause(0.5)
                    show bryce laugh dk flip bangok with dissolve
                    play soundloop "fx/faucet1.ogg" fadein 1.0
                    queue soundloop "fx/faucet2.ogg"
                    m "My appreciative hum was cut off by the stream of warm, golden liquid. I sank even a little bit further on his cock, needy and excited by having the big dragon use me as nothing more than a cum rag and urinal."
                    if persistent.bangok_inflation == True:
                        m "Swallowing the flow normally was impossible with my guts as full as they were. It sloshed back as I gagged, washing away the taste of cum in my mouth and replacing it with the tang of piss."
                        m "Not wanting to lose a drop around the seal of my lips, I shoved Bryce's cockhead further than I thought it could go, partway {i}into{/i} my throat, so that he could urinate directly into my guts."
                        m "The pressure bulged out my belly as fluid shifted and flowed inside of me to accomodate."
                    else:
                        m "Swallowing the flow was nearly impossible. It sloshed back as I gagged, washing away the taste of cum in my mouth and replacing it with the tang of piss."
                    label bangok_four_bryce1_oralbot_afterpissend:
                    stop soundloop fadeout 3.0
                    m "Unfortunately, all good things had to come to an end. He finished, then gave me a satisfied wink."
                    Br flirty dk flip bangok "Might not have taken a piss since the shift started at the station. Hope you don't mind."
                    Br flirty dk flip bangok "Good?"
                    if persistent.bangok_inflation == True:
                        m "I nodded, the head of his cock still in my mouth to hold down the gifts he'd given."
                        m "A little piss dribbled out of my mouth as I let his shaft go and struggled to swallow. I bent to try to clean it up with my tongue."
                    else:
                        m "I nodded, the head of his cock still in my mouth."
                        m "Bryce gave one last dribble of pee across my tongue as I let his shaft leave my mouth. I tried to suckle on his tip for just that little bit more."
                if persistent.bangok_inflation == True:
                    Br smirk dk flip bangok "D-Don't. Gotta take a shower after this anyway, clean that tip off."
                    Br flirty dk flip bangok "You might need more than that."
                else:
                    Br smirk dk flip bangok "D-Don't. Gotta take a shower after this anyway, clean that tip off. You too, probably."
                m "When I released his cock completely, it sank partway back into his body, just barely peeking out from his slit."


            if not bangok_four_bryce1_playercame and not bangok_four_bryce1_protected and not (persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after"):
                play sound "fx/cartslide.ogg"
                show bryce normal dk bangok at center with dissolve
                if persistent.bangok_inflation == True and bangok_four_bryce1_playerstuffed:
                    m "Bryce rolled off the couch, then turned to face me. I struggled up off my knees, added liquid weight putting me a little off-balance."
                    Br flirty dk bangok "Really filled you up, didn't I?"
                    m "I patted my belly."
                else:
                    m "Bryce rolled off the couch, then turned to face me. I got up off my knees."

            if not bangok_four_bryce1_playercame:
                Br flirty dk bangok "That's me. Now how about you?"
                menu:
                    "I... think I'm done.":
                        Br brow dk bangok "Hm?"
                        c "I'm... pretty much satisfied. Think I'm going to pass out soon."
                        Br flirty dk bangok "You sure?"
                        c "Pretty much spent, yeah."
                        $ brycemood -= 1
                        Br normal dk bangok "If you say so."
                        pass
                    "Want to suck me back?" if bangok_four_playerhasdick == True:
                        jump bangok_four_bryce1_m2_bsucc_merge
                    "Can I fuck you?" if bangok_four_playerhasdick == True:
                        jump bangok_four_bryce1_ptop
                    "Eat me out?" if bangok_four_playerhasdick == False:
                        jump bangok_four_bryce1_f_tonguefuck

            label bangok_four_bryce1_bothdone:
            Br normal dk bangok "Well, that's you and that's me."
            c "Yeah."
            if brycemood < 0:
                Br brow dk bangok "Floor's open, if you can't make it home."
                c "Floor. Floor's good."
                Br "Sure."
                scene black with dissolveslow
                jump bangok_four_bryce1_morningfloor
            else:
                Br "I'll sleep on the floor, then. You can have the couch."
                label bangok_four_bryce1_couchsleepchoice:
                menu:
                    "Thanks.":
                        pass
                    "You don't have to sleep on the floor.":
                        Br brow dk bangok "The couch isn't {i}that{/i} spacious, I don't think."
                        c "We can share."
                        $ renpy.pause(0.9)
                        $ brycemood += 1
                        Br flirty dk bangok "Alright."
                scene black with dissolveslow
                jump bangok_four_bryce1_morningcouch


        "I want you in me.":
            $ bangok_four_malepartners += 1
            label bangok_four_bryce1_analbot:
            call bangok_four_bryce1_position("analbot")
            if bangok_four_playerhasdick == True:
                Br brow dk bangok "We can try. But, ah, where? I didn't see anything behind your \"balls\" when I was down there looking."
            elif persistent.bangok_cloacas == True:
                Br brow dk bangok "We can try. But, ah, is there really a difference? 's going in your cloaca either way."
                c "Not quite. Humans don't have those."
            else:
                Br normal dk bangok "Alright. Where's your ass?"
            c "It's further back. Here."
            scene bangok_four_bryce1_apartment night ceiling at Pan((0,360), (0,0), 2.0) with dissolve
            m "I lay down on Bryce's couch, lifting my legs to give him a better look."
            show bangok_four_bryce_underside_large dk flip at Position(yanchor='top',ypos=0.8) with dissolve
            Br "Huh. So it is."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.6) with ease
            if bangok_four_playerhasdick == True or persistent.bangok_cloacas == True:
                Br flirty dk bangok "Can't say I've ever seen that before."
            scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
            show bryce normal dk bangok at Position(ypos=1.1)
            with dissolve
            m "Moving back to let me sit up, Bryce handed me a bottle of lube."
            Br "If you think it'll fit. But it definitely won't without plenty of this."
            c "Right."
            if persistent.bangok_watersports == True:
                call bangok_four_bryce1_ws_conversation from bangok_four_bryce1_analbot_ws_conversation
            if bangok_four_bryce1_protected == False and not bangok_four_bryce1_playercame:
                m "Before I knelt down to start applying the lube to his cock, my addled brain pushed through an important thought."
                c "Oh, I almost forgot protection."
                Br stern dk bangok "Is that really necessary?"
                if bangok_four_bryce1_wstiming is not None:
                    Br smirk dk bangok "I thought you wanted my fluids inside you."
                    if bangok_four_playerhasdick == True:
                        Br brow dk bangok "Besides, we're both guys. Kids aren't happening."
                    else:
                        Br brow dk bangok "Besides, we're different species. Kids aren't happening."
                else:
                    if bangok_four_playerhasdick == True:
                        Br "We're both guys. Kids aren't happening."
                    else:
                        Br "We're different species. Kids aren't happening."
                Br brow dk bangok "Unless there's something about humans I really don't understand."
                menu:
                    "[[Insist.]":
                        $ brycemood -= 1
                        $ bangok_four_bryce1_protected = True
                        c "We don't know what your fluids might do to me."
                        show bryce stern dk bangok with dissolve
                        m "Bryce groaned, then gestured to a nearby chest of drawers."
                        Br "Top, I think. Just hurry up."
                        label bangok_four_bryce1_analbot_fetchcondom:
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.wav"
                        if bangok_four_playerhasdick == True:
                            m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one, then dug a little deeper for one my size, in case things went further."
                            m "Only after I dug to the bottom did I finally find a box of condoms closer to my scale, unopened."
                        else:
                            m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one at random."
                        m "Tearing into the packaging, I returned with the necessary equipment."
                    "[[Take his load.]":
                        $ bangok_four_bryce1_protected = False
                        c "Fair point."
            elif bangok_four_bryce1_protected:
                menu:
                    "[[Put a condom on him.]":
                        pass
                    "[[Take his load.]":
                        $ bangok_four_bryce1_protected = False
                        show bryce at center with ease
                        m "I knelt in front of Bryce, spurting a healthy dose of lube along the top of his impressive length."
                        Br brow dk bangok "Lube's supposed to go on the outside of the condom."
                        Br flirty dk bangok "Or did you change your mind?"
                        c "Well, what's the worst that could happen? Besides, I want what you're putting out."
                        $ brycemood += 1
                        Br smirk dk bangok "Fine by me."
                        jump bangok_four_bryce1_analbot_luberub

            show bryce at center with ease
            if bangok_four_bryce1_protected == True:
                m "I knelt in front of Bryce, unrolling the condom along his impressive length, before spurting a healthy dose of lube along the top."
            else:
                m "I knelt in front of Bryce, spurting a healthy dose of lube along the top of his impressive length."
            label bangok_four_bryce1_analbot_luberub:
            show bryce smirk dk bangok with dissolve
            play soundloop "fx/massage.ogg"
            m "Setting the bottle down, I spread the lube over and around his shaft, trying to make sure everything was fully covered, while also pushing a large dollop up toward the tip to help with entry."
            Br stern dk bangok "D-Damn your hands are soft."
            stop soundloop fadeout 1.0
            c "That should do it."
            scene bangok_four_bryce1_apartment night ceiling at Pan((0,360), (0,0), 2.0) with dissolve
            m "Anticipating what would come next, I lay back down on Bryce's couch, tossing one leg over the seatback and spreading the other away as far as I could."
            m "One of my still lube-covered hands, I rubbed over my asshole, both as a tease and to help prep the site."
            show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=0.6) with easeinbottom
            $ renpy.pause(0.8)
            Br stern dk bangok "You're sure about this?"
            c "Yep."
            Br brow dk bangok "You'll tell me if anything hurts? Anything feels off?"
            c "Mhmm."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.6) with ease
            Br flirty dk bangok "Then give me a second to figure out how to aim."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
            m "Bryce clambered overtop me, hindlegs still on the floor while he braced his forelegs against the couch. The warmth radiating off his underbelly suffused my naked skin."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
            if bangok_four_playerhasdick == True:
                m "The cold lube on the tip of his cock bumped up against my thighs, then slapped my balls as he tried to find my asshole."
            else:
                m "The cold lube on the tip of his cock bumped up against my thighs, then prodded my vagina as he tried to find my asshole."
                menu:
                    "Lower!":
                        pass
                    "[[Say nothing.]":
                        Br laugh dk bangok "There!"
                        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.8) with ease
                        m "His tip slipped inside my vagina easily, spearing me open and sending sparks of pleasure down my legs that left them limp."
                        Br brow dk bangok "That... was easier than I expected."
                        Br "Hold on."
                        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
                        Br stern dk bangok "[player_name], that was the wrong one, wasn't it?"
                        menu:
                            "Keep going there.":
                                c "That... I think that one thrust changed my mind."
                                jump bangok_four_bryce1_f_fuck_merge
                            "Yeah...":
                                $ brycemood -= 2
                                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
                                Br "I'm as into having fun with this as you are, but you need to talk to me and tell me these things."
                                c "Sorry."
                                Br stern dk bangok "Just focus next time. I don't want to hurt you because you kept your mouth shut."
                                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
                                m "He slid himself back between my legs, seeking out my ass again, this time with more care. Even still, he was quickly prodding against my vaginal opening again."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.8) with ease
            Br stern dk bangok "Why is this so damn difficult?"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.85) with ease
            m "Following my inner thighs, he managed to get his rigid cock nestled in my taint."
            c "Close."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
            if bangok_four_playerhasdick == True:
                m "He pushed and I yelped, the delicate patch of skin between my balls and ass pressing inward."
            else:
                m "He pushed and I yelped, the delicate patch of skin between my cunt and ass pressing inward."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.8) with ease
            Br brow dk bangok "You alright? What happened?"
            c "Lower. Lower than that."
            Br laugh dk bangok "If it's so small I can't find it, how am I gonna fit?"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.85) with ease
            m "He gave it another try, the tip of his shaft bouncing lewdly off one of my cheeks."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.82) with ease
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
            m "Grabbing hold, I guided him the remaining short distance, until his tip was applying just a little pressure to my rosebud."
            Br smirk dk bangok "Ready?"
            $ renpy.pause (0.3)
            c "Yeah."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.98) with ease
            m "The large amount of lube we'd applied was the only way he was able to enter. My ass stretched wide, just short of the point of pain as he pressed just his tip in."
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.0) with ease
            m "When my ring made it past the head and his width decreased slightly, I gasped."
            m "Bryce froze immediately."
            Br brow dk bangok "Problem?"
            c "N-No. It's..."
            $ renpy.pause (1.2)
            Br flirty dk bangok "Want some more?"
            m "I nodded, at a loss for words."
            show bangok_four_bryce_underside_large:
                ease 4.0 ypos (-2.2)
            $ renpy.pause (4.0)
            if bangok_four_playerhasdick == True:
                m "Bryce sank in slowly, showing the uptmost care despite our shared inebriation. The plates on his belly scraped past my own penis, the harsh stimulation adding yet more to the experience."
            else:
                m "Bryce sank in slowly, showing the uptmost care despite our shared inebriation. The plates on his belly scraped past my belly just centimeters from the lips of my front entrance, the harsh stimulation and anticipation of more to come adding to the experience."
            if persistent.bangok_balls:
                m "As the warm scales on his legs pressed up against my skin, his balls resting against my buttcheeks, I squirmed to try to part my own legs further, to get that little bit closer to take him fully."
            else:
                m "As the warm scales on his legs pressed up against my skin, I squirmed to try to part my own legs further, to get that little bit closer to take him fully."
            Br laugh dk bangok "So tight!"
            c "Y-You're so big!"
            Br flirty dk bangok "I hear that a lot."
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                if bangok_four_bryce1_protected == True:
                    m "Suddenly, I felt a warmth blossoming in my guts, along with the stretching of the condom's reservoir, spreading out from where I thought his tip might be."
                else:
                    m "Suddenly, I felt a warmth blossoming in my guts, spreading out from where I thought his tip might be."
                $ renpy.pause(0.5)
                Br laugh dk bangok "Ah... there we go."
                if bangok_four_bryce1_protected == True:
                    m "I squirmed a little more, turned on as Bryce used the condom in my ass as a urinal."
                else:
                    m "I squirmed a little more, turned on as Bryce used my ass as a urinal."
                stop soundloop fadeout 1.5
                if persistent.bangok_inflation:
                    m "Between his cock and piss, I felt stuffed. I was a little unsure how we'd even go about fucking with me this full."
                $ renpy.pause(0.8)
                Br flirty dk bangok "Might not have taken a piss since the shift started at the station. Hope you don't mind."
                $ renpy.pause(0.8)
                Br flirty dk bangok "How was that?"
                c "Mmh."
                $ renpy.pause(1.0)
            Br smirk dk bangok "How's that size now?"
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
                    Br laugh dk bangok "Have you?"
                    m "His laughter reverberated through where our bodies met, tingling in my innards."
                    Br smirk dk bangok "Then I guess you won't mind if we get moving."
            show bangok_four_bryce_underside_large:
                ease 3.5 ypos (-2.05)
            m "Bryce tugged back just as slowly as he'd entered, keeping the lube even on his shaft and my speared ass from feeling any significant shocks."
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                if bangok_four_bryce1_protected:
                    m "The condom's bloated reservoir followed through my innards, the sensation of dragging the shifting fluid mass inside me utterly maddening."
                else:
                    m "Piss followed his cockhead as he pulled back, the sensation of fluid flowing through my innards adding yet another bubbling layer on top of the thickness of his shaft."
            m "He stopped at his tip, waiting again."
            menu:
                "E-Easy.":
                    Br brow dk bangok "I'm taking this as slowly as I can."
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
                    Br smirk dk bangok "How is it?"
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
                    Br smirk dk bangok "Give me a sec."
                    m "Rather than pick up the pace, he spent a long, slow moment dragging his cock back out of my depths."
                    show bangok_four_bryce_underside_large:
                        ease 5.0 ypos (-2.0)
                    $ renpy.pause (5.0)
                    if bangok_four_playerhasdick == True:
                        m "As he did, he twitched his cock along the way, eventually finding that one pleasure button deep inside me."
                        show bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,30), 0.5)
                        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.05)
                        with ease
                        m "I bucked my hips, almost popping his tip free."
                        Br flirty dk bangok "So that's what that was."
                    else:
                        m "As he did, he twitched his cock along the way, sending small waves of pleasure through my insides."
                        c "F-Fuck, stop teasing!"
                        m "He did no such thing, just gently pulling his tip back against my rear entrance."
                    m "I moaned appreciatively."
                    Br smirk dk bangok "Okay. Here we go."
                    $ renpy.pause(0.3)
                "Oh fuck me already.":
                    $ brycemood += 1
                    show bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,30), 0.5)
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.05)
                    with ease
                    if persistent.bangok_balls:
                        m "I thrust my ass back against his cock, taking back a little bit of what he'd taken away and bumping his balls."
                    else:
                        m "I thrust my ass back against his cock, taking back a little bit of what he'd taken away."
                    Br flirty dk bangok "If you say so."

            play soundloop "fx/rub2.ogg" fadein 1.0
            show bangok_four_bryce_underside_large:
                ease 0.5 ypos (-2.15)
                ease 0.7 ypos (-2.1)
                repeat
            if persistent.bangok_balls:
                if persistent.bangok_inflation:
                    m "Bryce began to fuck me for real, sliding in and out, in and out with movements that spread me wide each way and slapped my rear with his large, heavy balls."
                else:
                    m "Bryce began to fuck me for real, sliding in and out, in and out with movements that spread me wide each way and slapped my rear with his balls."
            else:
                m "Bryce began to fuck me for real, sliding in and out, in and out with movements that spread me wide each way."
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                if bangok_four_bryce1_protected:
                    m "His piss balloon was shoved deeper into my gut, sticking in place with his pulls out that stretched the condom lewdly inside me."
                else:
                    m "His piss was shoved deeper into my gut, wet squelches almost audible outside me with each thrust."
            $ renpy.pause(3.0)
            m "It didn't take long before we were both emitting undignified noises."
            $ renpy.pause(0.9)
            if persistent.bangok_knot == True:
                Br stern dk bangok "In or out?"
                c "H-Huh?"
                Br brow dk bangok "The knot! In or out?"
                $ renpy.pause(0.5)
                menu:
                    "Y-You have a {i}knot{/i}?!":
                        $ bangok_four_bryce1.knotpos = "inoops"
                    "In!":
                        $ brycemood += 1
                        $ bangok_four_bryce1.knotpos = "in"
                    "Out!":
                        $ bangok_four_bryce1.knotpos = "out"
            else:
                Br stern dk bangok "Not... Long..."
            stop soundloop fadeout 1.0
            play sound "fx/snarl.ogg"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.15) with ease
            if not persistent.bangok_knot or (persistent.bangok_knot and bangok_four_bryce1.knotpos != "out"):
                if persistent.bangok_balls:
                    if bangok_four_bryce1_protected == True:
                        m "Bryce came, prying my legs further apart as he forced our hips together and slapped his churning balls against my ass, hilting me to fill his condom inside."
                    else:
                        m "Bryce came, prying my legs further apart as he forced our hips together and slapped his churning balls against my ass, hilting inside me to coat my insides white."
                else:
                    if bangok_four_bryce1_protected == True:
                        m "Bryce came, prying my legs further apart as he forced our hips together, hilting me to fill his condom inside."
                    else:
                        m "Bryce came, prying my legs further apart as he forced our hips together, hilting inside me to coat my insides white."
            else:
                if bangok_four_bryce1_protected == True:
                    m "Bryce came, prying my legs further apart as he jerked to a stop, coming a few inches short of hilting while he filled his condom inside me."
                else:
                    m "Bryce came, prying my legs further apart as he jerked to a stop, coming a few inches short of hilting while he coated my insides white."


            if bangok_four_playerhasdick == True:
                if not bangok_four_bryce1_playercame:
                    m "The twitching of his spurting cock pressed up against the pleasure button inside me. Before I could form coherent words, I, too, was over my edge and cumming onto both our chests."
                else:
                    if bangok_four_playerhasdick == True:
                        m "The twitching of his spurting cock pressed up against the pleasure button inside me, the overstimulation after my recent orgasm leaving me writhing."
            else:
                if not bangok_four_bryce1_playercame:
                    m "My anal passage spasmed back around him, the sensation of his spurts filling me combined with his size and the rough fucking enough to push me over the edge."
                else:
                    m "My anal passage spasmed back around him, the sensation of his spurts filling me combined with his size and the rough fucking enough to push me over the edge yet again."

            $ bangok_four_bryce1_playercame = True

            if persistent.bangok_inflation == True:
                m "Even after I was done, though, Bryce had a few spurts left in him."
                if bangok_four_bryce1_protected == True:
                    m "I realized with some alarm that I was feeling the condom continuing to bloat inside of me, pressing deeper down my canals into my guts."
                else:
                    m "I realized with some alarm that I was feeling {i}very{/i} full."
                    $ bangok_four_bryce1_playerstuffed = True
                c "B-Bryce!"
                Br flirty dk bangok "A-Almost..."
                m "Looking down, I found my belly was visually slightly larger than it should be."

            $ renpy.pause(0.8)
            show bangok_four_bryce_underside_large:
                ease 1.0 ypos -2.0
                ease 1.0 ypos -1.7
                ease 1.0 ypos -1.3
                ease 1.0 ypos -0.7
            m "After a long moment cumming inside of me, Bryce worked his way back with his forelegs, keeping his hips and cock where they were as he curled over to look down at me."
            $ bangok_four_bryce1_brycecame = True

            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                if bangok_four_bryce1_protected == True:
                    play sound "fx/bubbles.ogg"
                    m "The dam inside me burst, Bryce's cumload just a little more than the condom could take after his pissing in me."
                    m "Warmth suffused my insides, bubbling and sloshing as it spread to equilibrium within my guts, no longer contained."
                    $ bangok_four_bryce1_playerstuffed = True
            elif persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
                Br flirty dk bangok "Ready for part two?"
                if persistent.bangok_inflation == True:
                    c "Uh."
                else:
                    c "Mhmm."
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
                m "With a grunt, Bryce leaned forward, then his cock twitched inside me again. A new, less viscous warmth began spreading in my guts."
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                Br laugh dk bangok "Ahhh..."
                if persistent.bangok_inflation == True:
                    if bangok_four_bryce1_protected == True:
                        play sound "fx/bubbles.ogg"
                        m "The dam inside me burst, Bryce's additional pissload just a little more than the condom could take."
                        $ bangok_four_bryce1_playerstuffed = True
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
                stop soundloop fadeout 1.5
                m "When he worked his way back down to eye level with me, I could almost hear the sloshing from all his fluids."
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.7) with ease
                Br flirty dk bangok "Might not have taken a piss since the shift started at the station. Hope you don't mind."

            if persistent.bangok_inflation == True:
                m "He rubbed my protruding belly with a paw."
                Br flirty dk bangok "Sure did fill you up, huh?"
                m "I couldn't answer as I lay basking under the warm fluid result of our coitus."


            if persistent.bangok_watersports and persistent.bangok_inflation and bangok_four_bryce1_protected:
                $ brycemood += 1
                Br flirty dk bangok "Mm. I think the condom broke."
                menu:
                    "Obviously!":
                        $ brycemood -= 2
                        Br "I didn't exactly have control over its integrity."
                        c "Not pissing in it could've saved it."
                        Br "And who said they were okay with that?"
                    "Damn.":
                        Br "Yeah, sorry."
                        Br flirty dk bangok "Good fuck, though?"
                        m "I nodded."
                    "That felt kinda good...":
                        Br "Did it?"
            else:
                Br flirty dk bangok "Good?"
                m "I nodded."
            # menu:
            #     "[[Nod.]":
            #         pass
            #     ""
            #     "T-Too much." if persistent.bangok_inflation:
            #         $ brycemood -= 1
            #         Br flirty dk bangok "You knew what you were getting yourself into."
            if persistent.bangok_knot == True and bangok_four_bryce1.knotpos != "out":
                Br flirty dk bangok "I hope you liked it, 'cause I don't think your ass will stretch to let the knot back out anytime soon."
                if bangok_four_bryce1.knotpos == "inoops":
                    $ brycemood -= 1
                    c "What?!"
                    scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
                    show bryce brow dk bangok
                    with dissolvemed
                    play sound "fx/sheet.wav"
                    m "He backed off further, giving me room to get up on my elbows."
                    $ renpy.pause(0.5)
                    Br "I didn't exactly have a lot of time or room for thought, and you were being unclear."
                    menu:
                        "I didn't even know you had a knot!":
                            $ brycemood -= 1
                            Br stern dk bangok "You're interacting with another species, and didn't think to check a basic fact like this?"
                        "You should have left it ouside, then!":
                            $ brycemood -= 2
                        "It's okay.":
                            $ brycemood += 1
                            c "It was a misunderstanding. And as misunderstandings go, there are worse ones."
                            Br normal dk bangok "Not much to be done about it now. We might as well sleep it off."
                            jump bangok_four_bryce1_tiedsleep
                    Br stern dk bangok "Not much to be done about it now. We might as well sleep it off."

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
                    Br stern dk bangok "I wish we didn't have to sleep like this as much as you do."
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
                            Br smirk dk bangok "Goodnight, [player_name]."
                            jump bangok_four_bryce1_morningcouch
                        "Pull out.":
                            label bangok_four_bryce1_analbot_pullout:
                            scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
                            show bryce stern dk bangok
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
                                Br stern dk bangok "Damn. There's that size difference again."
                                c "Maybe if I push?"
                                Br brow dk bangok "Let me get a little more of the condom out first."
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
                        Br stern dk bangok "Floor's open. Or you can find your way home like that."
                        m "I struggled even to get off the couch, my ass complaining loudly at every movement."
                        c "Floor is good..."
                        play sound "fx/impact3.ogg"
                        scene black with vpunch
                        jump bangok_four_bryce1_morningfloor
                    else:
                        Br normal dk bangok "You want to stay on the couch there?"
                        m "I nodded."
                        c "Not sure I can move after that. Damn."
                        Br flirty dk bangok "Well, I'm about ready to pass out."
                        scene black with dissolveslow
                        Br "Goodnight, [player_name]."
                        c "G'night."
                        jump bangok_four_bryce1_morningcouch










        "I want to stick it in you.":
            $ bangok_four_malepartners += 1
            label bangok_four_bryce1_ptop:
            call bangok_four_bryce1_position("ptop")
            Br flirty dk bangok "Fine by me."
            play sound "fx/cartslide.ogg"
            show bryce normal dk bangok at Position(xpos=0.4,xanchor='center') with ease
            show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
            m "Bryce settled back on the couch, bunching the rug and tugging the coffee table as his tail caught for a moment."
            m "He spread his hindlegs with a wink."
            Br flirty dk bangok "What are you waiting for?"
            m "My addled brain managed to push through a few thoughts before I followed him over."
            if bangok_four_bryce1_protected_a:
                menu:
                    "[[Put on your condom.]":
                        $ bangok_four_bryce1_protected = True
                    "[[Bareback.]":
                        $ bangok_four_bryce1_protected = False
                c "Dry?"
                m "I squinted in the dark, completely missing any ass I could go for under his towering shaft."
                c "And, uh, where?"
            else:
                c "Dry? Without protection?"
                m "I squinted in the dark, completely missing any ass I could go for under his towering shaft."
                c "And, uh, where?"
                m "At the question of protection, he smiled lopsidedly."
                Br flirty dk bangok "C'mon. We're both guys. Kids aren't happening."
                menu:
                    "[[Insist.]":
                        c "No. Not without protection."
                        if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                            c "I've seen a health aisle. You've got condoms."
                        else:
                            c "Your kind has condoms, right?"
                        $ brycemood -= 1
                        show bryce stern dk bangok with dissolve
                        m "Bryce groaned, then gestured at a chest of drawers in a corner."
                        Br "Top. I think. Just hurry up."
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.wav"
                        m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. Only after I dug to the bottom did I finally find one closer to mine, unopened."
                        m "Tearing into the packaging, I returned equipped."
                    "[[Bareback.]":
                        $ bangok_four_bryce1_protected = False
                        c "Okay. Where?"
            m "Bryce twisted his head behind the couch, returning with a bottle of lube clenched in his maw."
            show bryce stern dk bangok with dissolve
            if persistent.bangok_balls == True:
                if persistent.bangok_cloacas == True:
                    m "With a grunt of effort, he curled forward to brace the bottle beneath his balls, then depressed the plunger to squirt a dollop right into the slit beneath them."
                else:
                    m "With a grunt of effort, he curled forward to brace the bottle beneath his balls, then depressed the plunger to squirt a dollop two plate ridges below where said balls emerged from his slit, which I could now see was also slightly spread."
            else:
                if persistent.bangok_cloacas == True:
                    m "With a grunt of effort, he curled forward to brace the bottle against his cock, then depressed the plunger to squirt a dollop at the base of where said cock emerged from his slit."
                else:
                    m "With a grunt of effort, he curled forward to brace the bottle against his cock, then depressed the plunger to squirt a dollop two plate ridges below where said cock emerged from his slit, which I could now see was also slightly spread."
            play sound "fx/box.wav"
            m "He tossed the bottle aside against the coffee table."
            Br smirk dk bangok "There. Any more questions?"
            if persistent.bangok_balls == True:
                m "I answered his question by straddling his tail, bracing against his hindlegs, then trying to decide again exactly where I was putting my shaft."
            else:
                m "I answered his question by straddling his tail, bracing against his hindlegs, then experimentally prodding the opening he'd indicated beneath his shaft."
                m "I missed."
                Br brow dk bangok "Further down. That spot's where mine comes out."
            menu:
                "Dock with him.":
                    if not bangok_four_bryce1_brycecame:
                        m "Bryce gasped, then clenched his teeth as I tried to press deeper next to his shaft."
                        $ brycemood -= 1
                        if persistent.bangok_balls == True:
                            Br stern dk bangok "Wrong side of my balls. Lower."
                        else:
                            Br stern dk bangok "What did I {i}just{/i} say?"
                        c "Uh."
                        menu:
                            "[[Dock him.]":
                                $ brycemood -= 1
                                play sound "fx/impact3.ogg"
                                show bryce at center
                                show bangok_four_bryce1_apartment night at Pan((0,0), (0,0), 0.0)
                                with vpunch
                                m "I sprawled across the floor, Bryce's kick leaving me out of breath and dizzy."
                                Br brow dk bangok "This isn't one-way. You want to get inside me, you gotta {i}listen{/i} to me."
                                Br brow dk bangok "Aim lower, okay? I'm way too pent up for what you're trying to pull."
                                play sound "fx/cartslide.ogg"
                                show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 2.0)
                                show bryce normal dk bangok at Position(xpos=0.45,xanchor='center',ypos=1.05)
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
                    else:
                        if persistent.bangok_balls == True:
                            m "I pressed in next to his shaft, experimentally exploring his genital slit. Bryce wriggled a little."
                            Br stern dk bangok "Wrong side of my balls. Lower."
                        else:
                            m "I pressed in deeper next to his shaft, doubling down on my mistake. Bryce wriggled a little."
                            Br stern dk bangok "Still wrong."
                        if brycemood < 2:
                            c "What if I want to fuck your genital slit?"
                            if brycemood < 0:
                                play sound "fx/impact3.ogg"
                                show bangok_four_bryce1_apartment night at Pan((0,0), (0,0), 0.0)
                                with vpunch
                                m "Bryce shoved me off with a leg."
                                Br "Then we can call this fraternization over."
                                show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 2.0)
                                with ease
                                m "I scrambled up."
                                c "Hey! I didn't suck you off for nothing!"
                                Br "You didn't do a very good job of that, either."
                                m "I advanced on Bryce's still-exposed hindquarters."
                                play sound "fx/impact3.ogg"
                                with vpunch
                                scene black with fade
                                jump bangok_four_bryce1_badmorning
                            else:
                                $ renpy.pause (1.2)
                                Br "Fine."
                        else:
                            c "Humans don't have these slits. I guess I'm just really curious what it feels like to fuck one."
                            c "May I?"
                            $ renpy.pause (0.8)
                            Br "Fine."
                        if not bangok_four_bryce1_protected:
                            Br brow dk bangok "But {i}don't{/i} cum inside it. Cleaning in there is a mess, and risks infections."
                            c "So pull out?"
                            Br stern dk bangok "Stick it in my ass. That's more what I was expecting."

                        m "Taking things slow, I sank myself into Bryce's genital slit, next to his retreated cock."
                        m "He'd been right. Even retreated into his body, his shaft remained as hard as it had been extended. The soft, warm walls pressing in against my dick from every direction except the round, hard surface of his cock was unlike anything I'd experienced."
                        m "To add to that, his cock and genital slit were {i}tight{/i}, squeezing my shaft between them and pulsing with every twich Bryce made as I sank in."
                        m "When I bottomed out, his tip digging into my pelvis, Bryce finally lost his grimace."
                        Br normal dk bangok "Alright. You can pick up your pace now."
                        m "I took a couple more slow, experimental thrusts first, seeking out the angle to fuck him at that would hurt his cock and mine the least."
                        play soundloop "fx/rub2.ogg" fadein 3.0
                        m "Then I started pumping, in and out of the tight, wet hole."
                        Br smirk dk bangok "This what you were looking for?"
                        m "I couldn't respond, too lost in the sensation of my cock being squeezed between his twitching shaft and pulsing wall as I moved in and out."
                        $ renpy.pause (0.8)
                        show bryce stern dk bangok with dissolve
                        m "His grimace returned as I slipped off to one side of his shaft, his tip jabbing my pelvis instead of my balls."
                        Br "How close are you?"
                        m "The answer was very close, enough that I had to start considering what was about to happen."
                        if bangok_four_bryce1_protected:
                            m "Was there enough room to cum? Or would that lead to cum spurting outside the condom?"
                        menu:
                            "[[Pull out.]":
                                stop soundloop fadeout 0.5
                                m "The yank out, combined with the chill air of the room, put me just over my edge."
                                menu:
                                    "Ass.":
                                        jump bangok_four_bryce1_ptop_asscum
                                    "Out.":
                                        play sound "fx/extinguish.ogg"
                                        show bryce brow dk bangok
                                        show black
                                        with dissolve
                                        if bangok_four_bryce1_protected:
                                            m "I steadied myself there, depositing my load into the condom's reservoir where it hung over Bryce's hindquarters."
                                            $ brycemood += 1
                                            if persistent.bangok_watersports == True:
                                                play soundloop "fx/faucet1.ogg" fadein 1.0
                                                queue soundloop "fx/faucet2.ogg"
                                                m "After a moment, I realized yet more fluid was draining out of me, ballooning the condom further."
                                                c "Uh."
                                                m "My cheeks flushed with embarassment."
                                                stop soundloop fadeout 1.5
                                                show bryce laugh dk bangok with dissolve
                                                m "Bryce bopped the full condom reservoir with a paw."
                                                Br "Too much to drink?"
                                                show bryce smirk dk bangok with dissolve
                                                Br "I sleep with drinking buddies all the time. That happens a lot."
                                                Br flirty dk bangok "Still, good call with the condom."
                                            else:
                                                label bangok_four_bryce1_ptop_protectedslitcum:
                                                m "Bryce bopped the full condom reservoir with a paw."
                                                Br flirty dk bangok "Alright. Good call with the condom, there. Saves us a lot of cleanup."
                                                c "Th-Thanks."
                                            m "Climbing off Bryce, I pulled off and tied off the condom, then sat heavily."
                                        else:
                                            m "I didn't have time to find his ass. I came, spurting thin ropes across his hindquarters and chest."
                                            hide black with dissolvemed
                                            if persistent.bangok_watersports == True:
                                                play soundloop "fx/faucet1.ogg" fadein 1.0
                                                queue soundloop "fx/faucet2.ogg"
                                                m "After a moment, I realized yet more fluid was draining out of me, running down Bryce's belly plates."
                                                c "Uh."
                                                m "My cheeks flushed with embarassment."
                                                stop soundloop fadeout 1.5
                                                if bangok_four_bryce1_wstiming not in ["before","after"]:
                                                    $ brycemood -= 1
                                                    Br stern dk bangok "..."
                                                $ brycemood -= 1
                                                Br "Well, I didn't expect to have to clean up a golden shower today."
                                            else:
                                                Br "Well, I didn't expect to have to clean up that much today."
                                            Br laugh dk bangok "Guess what's done is done."
                                            Br normal dk bangok "We'll both have to take the floor."
                                            show bryce normal dk flip bangok at center with dissolve
                                            m "Bryce rolled off the couch as I sat down, feeling light-headed from the exertion of fucking the big dragon."
                                        Br brow dk bangok "No, don't. I'll take the floor."
                                        jump bangok_four_bryce1_couchsleepchoice
                                    "Back in.":
                                        jump bangok_four_bryce1_docking_inside
                            "[[Cum inside.]":
                                label bangok_four_bryce1_docking_inside:
                                stop soundloop fadeout 0.5
                                play sound "fx/extinguish.ogg"
                                if bangok_four_bryce1_protected:
                                    show bryce smirk dk bangok
                                else:
                                    show bryce angry dk bangok
                                show black
                                with dissolve
                                m "I shoved in deep and came, sandwiched between Bryce's huge cock prodding my balls and his slit's inner wall."
                                if bangok_four_bryce1_protected:
                                    hide black with dissolvemed
                                    $ renpy.pause(0.3)
                                    if persistent.bangok_watersports == True:
                                        play soundloop "fx/faucet1.ogg" fadein 1.0
                                        queue soundloop "fx/faucet2.ogg"
                                        show bryce brow dk bangok with dissolve
                                        m "After a moment, I realized yet more fluid was draining out of me, bloating the condom and filling that tight space inside him."
                                        c "Uh."
                                        m "My cheeks flushed with embarassment."
                                        Br stern dk bangok "Too tight. Pull it out!"
                                        menu:
                                            "One sec...":
                                                m "The piss so soon after cumming was bliss in the tight space, and I didn't want to miss a single drop of the experience."
                                                stop soundloop fadeout 1.0
                                                play sound "fx/bubbles.ogg"
                                                m "... Until something gave way."
                                                show bryce stern dk bangok with dissolve
                                                Br "[player_name]!"
                                                play sound "fx/stones.ogg"
                                                m "I pulled out, but the damage had already been done. Clumps of cum and rivulets of piss ran down the deflating condom from where the tight space and high pressure had pinched it to the point of breaking, dripping into the mess I'd made of his genital slit."
                                                show bryce stern dk bangok with dissolve
                                                m "Though his cock was peeking out again -- he was aroused by the experience -- his face showed his cold anger."
                                                jump bangok_four_bryce1_ptop_unprotectedslitcum
                                            "[[Pull it out!]":
                                                stop soundloop fadeout 1.5
                                                m "I pulled the bloated condom free, where it hung and bobbed lewdly over Bryce's hindquarters."
                                                jump bangok_four_bryce1_ptop_protectedslitcum
                                else:
                                    hide black with dissolvemed
                                    show bryce stern dk bangok with dissolve
                                    $ renpy.pause(0.3)
                                    if persistent.bangok_watersports == True:
                                        play soundloop "fx/faucet1.ogg" fadein 1.0
                                        queue soundloop "fx/faucet2.ogg"
                                        $ renpy.pause (0.5)
                                        m "After a moment, I realized yet more fluid was draining out of me, bloating filling that tight space inside him."
                                        c "Uh."
                                        stop soundloop fadeout 1.5
                                        m "I finished pissing in him, guessing that likely wouldn't make things any worse than they already were."
                                        $ renpy.pause (0.5)
                                    play sound "fx/stones.ogg"
                                    m "When I pulled out, droplets of the mess I'd made of his genital slit ran down my dick and dripped back inside."
                                    m "Though his cock was peeking out again -- he was aroused by the experience -- his face showed his cold anger."
                                    label bangok_four_bryce1_ptop_unprotectedslitcum:
                                    $ renpy.pause (0.5)
                                    m "Bryce shoved me off with a leg and, before I could make an excuse, I tripped over his tail and hit the ground, hard."
                                    play sound "fx/impact3.ogg"
                                    show bangok_four_bryce1_apartment night at Pan((0,0), (0,0), 0.0)
                                    with vpunch
                                    jump bangok_four_bryce1_badmorning










                "[[Fuck him.]":
                    pass
            show bryce flirty dk bangok with dissolve
            if bangok_four_bryce1_protected == True:
                m "As the lube spread further around my condom, one of his hard belly plates ground against the bottom of my cock. Then all gave way to warm envelopment as I reached as far inside him as I could go."
            else:
                m "As the lube spread further around my shaft, one of his hard belly plates ground against the bottom of my cock. Then all gave way to warm envelopment as I reached as far inside him as I could go."
            if persistent.bangok_balls == True:
                m "As his balls rolled around his shaft, which prodded my torso, he grinned lewdly."
            else:
                m "As his shaft rubbed up my torso, he grinned lewdly."
            Br "That's the spot, huh?"
            m "I nodded, at a loss for words."
            Br smirk dk bangok "Well, have your fun."
            m "I tugged out, beginning to pump experimentally at first, keeping an eye on Bryce's face to make sure I wasn't causing him any more discomfort."
            play soundloop "fx/rub2.ogg" fadein 3.0
            show bryce flirty dk bangok with dissolve
            m "It didn't seem to fase him in the least. He shot me a teasing wink as I picked up the pace."
            m "Beneath his hard plates, his internal tissues were soft and hot. The pressure on my dick was light, a function of his ass's outermost sphincters more than the tightness of any internal anatomy."
            m "Of course, I wasn't just in this for myself. Though it was difficult to form a coherent thought beyond my next thrust, I put some words together."
            c "Are you feeling this at all?"
            Br laugh dk bangok "Kinda!"
            if not bangok_four_bryce1_brycecame:
                Br smirk dk bangok "You won't get me off with it, if that's what you're wondering."
                m "Taking that as a bit of a challenge, I moved one hand from bracing against his legs to sandwiching his shaft against my belly."
                play sound "fx/buck.ogg"
                show bryce stern dk bangok with dissolve
                m "Bryce bucked his hips against mine, clearly taken off-guard by the move."
                Br flirty dk bangok "D-Damn. That's a neat trick!"
                m "I didn't respond, his bucking back putting me near the edge of my peak."
            else:
                Br flirty dk bangok "Doesn't hurt in the least, if that's what you're wondering."
                if persistent.bangok_balls == True:
                    m "I took that as a sign of further encouragement, leaned forward while pushing his balls out of the way, and went to town."
                else:
                    m "I took that as a sign of further encouragement, leaned forward, and went to town."
                Br laugh dk bangok "Now I'm almost feeling it!"
            stop soundloop fadeout 0.5
            $ renpy.pause(0.5)
            show bryce smirk dk bangok with dissolve
            play sound "fx/rub1.ogg"
            $ renpy.pause(1.5)
            label bangok_four_bryce1_ptop_asscum:
            play sound "fx/extinguish.ogg"
            show black with dissolve
            if bangok_four_bryce1_protected == True:
                m "I came, depositing my load in the condom's reservoir, buried deep within Bryce's ass."
            else:
                m "I came, depositing my load as deep as I could go in Bryce's ass."
            $ bangok_four_bryce1_playercame = True
            hide black with dissolvemed

            if persistent.bangok_watersports == True:
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                show bryce brow dk bangok with dissolve
                m "After a moment, I realized yet more fluid was draining out of me."
                c "Uh."
                Br laugh dk bangok "Too much to drink?"
                m "My cheeks flushed with embarassment."
                stop soundloop fadeout 1.5
                Br smirk dk bangok "I do this with drinking buddies all the time. You're not the first to piss in me."

            if bangok_four_bryce1_protected == True:
                m "He shifted his hips, my body's fluid output sloshing lewdly around my penis's head inside the condom."
            else:
                m "He shifted his hips, my body's fluid output flowing lewdly around my penis, buried in his ass."

            if bangok_four_bryce1_brycecame:
                if brycemood > 0:
                    show bryce flirty dk bangok with dissolve
                else:
                    show bryce brow dk bangok with dissolve
                m "I pulled out, the exhaustion of the evening's fucking finally catching up with me."
                play sound "fx/cartslide.ogg"
                show bryce at center with ease
                m "Bryce rolled off the couch."
                jump bangok_four_bryce1_bothdone
            else:
                Br flirty dk bangok "That's you. Now how about me?"

                if bangok_four_bryce1_protected == True:
                    m "I pulled out first, considering my options as I tugged off and tied up my condom. My head was clearer, but I also felt lightheaded from the effort I'd just expended."
                else:
                    m "I pulled out first, considering my options. My head was clearer, but I also felt lightheaded from the effort I'd just expended."
                label bangok_four_bryce1_preciprocity_menu:
                menu:
                    "I... think I'm done.":
                        Br brow dk bangok "Excuse me?"
                        c "I'm..."
                        $ renpy.pause (0.8)
                        c "I think I'm going to pass out now."
                        Br stern dk bangok "Hey!"
                        scene black with fade
                        play sound "fx/impact3.ogg"
                        jump bangok_four_bryce1_badmorning
                    "Want to fuck me?":
                        jump bangok_four_bryce1_analbot
                    "I guess I could suck you.":
                        jump bangok_four_bryce1_oralbot







                    "Handjob okay?":
                        label bangok_four_bryce1_hand:
                        call bangok_four_bryce1_position("hand")
                        show bryce brow dk bangok with dissolve
                        c "I'm just... you're a little large."
                        Br "Of course. Handjob's fine if that's what you think is safe."
                        if bangok_four_bryce1_protected == True:
                            Br "Mind sheathing me in that condom you grabbed me?"
                            Br laugh dk bangok "Obviously my claws aren't a good idea for that."
                            Br normal dk bangok "And I don't want any more stains to clean out of my place."
                            c "Sure."
                        else:
                            Br normal dk bangok "Mind getting me a condom? Don't want any more stains to clean out of my place."
                            c "Sure. Where?"
                            Br "Drawers, over there. Top drawer, I think."
                            $ renpy.pause(0.3)
                            play sound "fx/rummage.wav"
                            $ renpy.pause(2.0)
                            stop sound fadeout 1.0
                            m "The condoms weren't hard to find. I returned with one his size, which most of the boxes were."
                        call bangok_four_bryce1_setprotected(True)
                        if persistent.bangok_balls == True:
                            m "Sitting underneath him, I unrolled the condom along his length, right down to his balls."
                        else:
                            m "Sitting underneath him, I unrolled the condom along his length."
                        Br smirk dk bangok "Alright. Go to town."
                        m "I gripped Bryce's shaft around the condom lightly near the base. I wasn't quite sure how rough I could be with it, with him being a different species."
                        Br laugh dk bangok "H-Hey! Don't {i}tickle{/i} it!"
                        m "Tightening my grip, I gave an experimental pump up and down, before letting go and glancing back toward his head for approval."
                        Br flirty dk bangok "B-Better."
                        play soundloop "fx/massage.ogg" fadein 8.0
                        m "Grabbing hold again, I resumed pumping over the slightly lubricated surface of the condom, tightening my grip until Bryce told me to stop."
                        show bryce laugh dk bangok with dissolve
                        m "He didn't, mouth just hanging open as he reveled in the sensation of my hands around him."
                        m "He even bucked against my hands, fucking my fingers a little as he enjoyed what I was giving him."
                        if persistent.bangok_watersports == True:
                            $ renpy.pause(0.8)
                            Br "Ah fuck."
                            stop soundloop fadeout 4.0
                            m "I loosened my grip significantly."
                            c "What's wrong?"
                            Br stern dk bangok "I gotta take a piss."
                            label bangok_four_bryce1_handjob_wsmenu:
                            menu:
                                "Let me get the condom off so you can use the toilet.":
                                    stop soundloop fadeout 0.5
                                    m "Tugging off the condom from the tip and ring, I let Bryce depart for the restroom."
                                    m "As he was walking off, I had another thought."
                                    call bangok_four_bryce1_ws_emptying_the_tank(False,False)
                                "If it's in the condom...":
                                    Br "It's about to be."
                                    m "I let go. Bryce shuddered, then his cock twitched as he released his fluid load into the condom."
                                    label bangok_four_bryce1_handjob_wsgoout:
                                    $ bangok_four_bryce1_wstiming = "before"
                                    play soundloop "fx/faucet1.ogg" fadein 1.0
                                    queue soundloop "fx/faucet2.ogg"
                                    Br laugh dk bangok "Ahhhh..."
                                    m "I watched, mesmerized as the condom's reservoir bloated with piss. {w=0.8}A few moments passed, the volume larger than any human's could be."
                                    stop soundloop fadeout 1.0
                                    $ renpy.pause(1.0)
                                    stop soundloop
                                    Br normal dk bangok "Alright. Where were we?"
                                    label bangok_four_bryce1_handjob_wscondomleft:
                                    if persistent.bangok_balls == True:
                                        m "The condom still hung from his dick, a bobbing, hypnotizing balloon full of piss even larger than either of his balls."
                                    else:
                                        m "The condom still hung from his dick, a bobbing, hypnotizing balloon full of piss."
                                    menu:
                                        "Drink it.":
                                            m "I pinched off his condom near the tip, then took the ring at the base and slid the whole thing off. The smell of urine hit like an aphrodisiac."
                                            show bryce flirty dk bangok with dissolve
                                            m "Before I could think about what I was doing, I had the ring in my mouth, and was lifting the balloon up over my head."
                                            show bryce smirk dk bangok with dissolve
                                            play sound "fx/water2.ogg"
                                            if persistent.bangok_inflation == True:
                                                queue sound "fx/gulpslow2.wav"
                                                $ renpy.pause (9.0)
                                                m "It was a huge volume. I had to pause and take a break partway through. When I finished, I felt packed with the warmth that had so recently left Bryce's bladder."
                                                $ bangok_four_bryce1_playerstuffed = True
                                                $ bangok_four_bryce1_position_pickb = "oralbot"
                                            else:
                                                queue sound "fx/gulping.wav"
                                                $ renpy.pause (3.0)
                                                stop sound fadeout 1.0
                                            $ brycemood += 1
                                            Br flirty dk bangok "That was hot to watch."
                                            m "Slurping the last from the now empty condom, I shoved it back down over his dick."
                                            c "Let's get back to it."
                                        "Replace it.":
                                            m "I pinched off his condom near the tip, then took the ring at the base and slid the whole thing off. The smell of urine hit like a wave."
                                            m "Tying it, I rolled it aside across his floor. Then I wandered back to his condom drawers for another one."
                                            c "Let's get back to it."
                                "What excellent timing. I could use a shower." if bangok_four_bryce1_wstiming is None:
                                    $ bangok_four_bryce1_wstiming = "after"
                                    Br stern dk bangok "Oh no. I'm not cleaning that up tonight."
                                    Br brow dk bangok "Besides, you're {i}already{/i} going to reek of me and alcohol. Not even sure an actual shower will get that off. Are you gonna be a good ambassador if they can smell urine on you, too?"
                                    c "..."
                                    Br stern dk bangok "Nothing outside tonight."
                                    c "Fine."
                                    jump bangok_four_bryce1_handjob_wsmenu
                                "Let me give you somewhere to go.":
                                    $ bangok_four_bryce1_wstiming = "before"
                                    $ brycemood += 1
                                    Br brow dk bangok "Hm?"
                                    m "Grabbing the condom by both the tip and ring, I tugged it completely off of Bryce's cock."
                                    m "Then I aimed his cock into my mouth, suckling on just the tip."
                                    Br stern dk bangok "You're sure?"
                                    menu:
                                        "Only fair.":
                                            pass
                                        "Yep.":
                                            pass
                                    m "I mumbled around a mouth full of just the tip of his cockflesh."
                                    m "Bryce shuddered, then his cock twitched as his stream hit my mouth."
                                    $ bangok_four_bryce1_wstiming = "before"
                                    play soundloop "fx/faucet1.ogg" fadein 1.0
                                    queue soundloop "fx/faucet2.ogg"
                                    Br laugh dk bangok "Ahhhh..."
                                    play sound ["fx/massage.ogg", "fx/massage.ogg", "fx/massage.ogg", "fx/massage.ogg"]
                                    m "I resumed pumping as he pissed in my mouth, wanting to give him the full suite of sensations I could muster."
                                    if persistent.bangok_inflation == True:
                                        m "Swallowing the rapid stream normally was impossible. It sloshed back as I gagged, coating my mouth in that unique tang. My body warmed, heat from Bryce transferred directly into my stomach."
                                        m "Not wanting to lose a drop around the seal of my lips, I sank Bryce's cockhead deeper than I thought I could take it, partway {i}into{/i} my throat, so that he could piss directly into my guts."
                                        $ bangok_four_bryce1_playerstuffed = True
                                    else:
                                        m "Swallowing the flow was nearly impossible. It sloshed back as I gagged, coating my mouth in that unique tang. My body warmed, heat from Bryce transferred directly into my stomach."
                                    stop soundloop fadeout 3.0
                                    m "As the stream began to lessen and I managed to catch my breath between swallows, Bryce's breath came heavy."
                                    Br stern dk bangok "Mmh. Keep that up and I might cum n-now."
                                    menu:
                                        "Give him a second.":
                                            stop sound fadeout 1.0
                                        "Now.":
                                            $ bangok_four_bryce1_protected = False
                                            show bryce laugh dk flip bangok with dissolve
                                            $ bangok_four_bryce1_brycecame = True
                                            play sound2 "fx/snarl.ogg"
                                            stop sound fadeout 4.0
                                            jump bangok_four_bryce1_oralbot_cum
                                    m "I let go, popping his cockhead out of my mouth and giving him a few seconds free of my hands to recover."
                                    $ renpy.pause(1.5)
                                    Br flirty dk bangok "Thanks. That... that was good stuff."
                                "Go for it.":
                                    m "I gave Bryce a few more pumps, showing I wasn't turned off by the piss, just didn't think I could safely handle it."
                                    m "Bryce shuddered, then his cock twitched as he released his fluid load into the condom."
                                    jump bangok_four_bryce1_handjob_wsgoout
                            play soundloop "fx/massage.ogg" fadein 3.0
                            m "I took his cock back in hand and, after a moment for him to adjust, resumed my previous pumping pace."
                        $ renpy.pause(1.4)
                        Br smirk dk bangok "D-Don't think I can ever take a dragon handjob again."
                        Br laugh dk bangok "Your smooth hands..."
                        play sound "fx/snarl.ogg"
                        stop soundloop fadeout 1.5
                        m "Abruptly, the condom's reservoir bloated, his first spurts spilling inside."
                        show bryce laugh dk bangok with dissolve
                        m "I gave a few more pumps, finishing him off completely as his mouth hung open."
                        $ renpy.pause(0.8)
                        Br smirk dk bangok "F-Fuck that was good."
                        if bangok_four_bryce1_playerstuffed == True:
                            m "Yet another fluid load bloated the condom in front of me. Did I even have room?"
                        else:
                            m "Bryce's cum balloon bobbed in front of me."
                        menu:
                            "Drink it.":
                                m "I pinched off his condom near the tip, then took the ring at the base and slid the whole thing off. The smell of cum was thick and heady."
                                show bryce flirty dk bangok with dissolve
                                m "Before I could think about what I was doing, I had the ring in my mouth, and was lifting the balloon up over my head."
                                show bryce smirk dk bangok with dissolve
                                if persistent.bangok_inflation == True:
                                    queue sound "fx/gulpslow2.wav"
                                    $ renpy.pause (9.0)
                                    if persistent.bangok_watersports == True and bangok_four_bryce1_playerstuffed == True:
                                        m "Even taking a break partway through, Bryce's cumload was just too much to pack in over his piss, and I had to surrender with the balloon only three quarters emptied."
                                        m "My belly bulged visibly."
                                        Br flirty dk bangok "You thirsty little thing."
                                    else:
                                        m "It was a huge volume. I had to pause and take a break partway through. When I finished, Bryce's seed packed me so full, I was sure my belly bulged slightly."
                                    $ bangok_four_bryce1_playerstuffed = True
                                    $ bangok_four_bryce1_position_pickb = "oralbot"
                                else:
                                    queue sound "fx/gulping.wav"
                                    $ renpy.pause (3.0)
                                    stop sound fadeout 1.0
                                $ brycemood += 1
                                Br flirty dk bangok "That was hot to watch."
                                m "I discarded the condom, feeling my consumption weighing on me, sapping what little of my energy remained."
                            "Take it off.":
                                m "I pinched off his condom near the tip, then took the ring at the base and slid the whole thing off. The smell of cum was thick."
                                m "Tying it off, I set the condom out of the way, where it wouldn't be stepped on."

                        if persistent.bangok_knot == True:
                            m "While he'd cum, a bulge had emerged near the base of his cock, one I hadn't noticed in the heat of the moment."
                            menu:
                                "Squeeze it.":
                                    Br laugh dk bangok "H-Hey!"
                                    Br smirk dk bangok "A bit soon to try to get me going again."
                                "Leave it.":
                                    pass


                        jump bangok_four_bryce1_bothdone


                    "I'm not sure I can fit you." if bangok_four_bryce1_m2_fit:
                        call bangok_four_bryce1_m2_fit from bangok_four_bryce1_preciprocity_menu_fit
                        jump bangok_four_bryce1_preciprocity_menu






        "I want you to suck me.":
            $ bangok_four_malepartners += 1
            Br flirty dk bangok "Sure. But turnabout is fair play."
            if False:
                label bangok_four_bryce1_m2_bsucc_merge:
                Br normal dk bangok "Fine with me."
            call bangok_four_bryce1_position("oraltop")
            show bryce flirty dk bangok with dissolve
            show bryce at Position(ypos=1.3) with ease
            show bryce at Position(ypos=1.5) with ease
            m "Bryce got low in front of my crotch, hot breath washing over my hardening shaft."
            if bangok_four_bryce1_protected:
                menu:
                    "[[Put on your condom.]":
                        c "W-Wait! Protection!"
                        show bryce brow dk bangok at Position(ypos=1.3) with ease
                        m "Bryce sighed, waiting a few moments for me to roll on the condom."
                        $ renpy.pause (0.3)
                        show bryce at Position(ypos=1.5) with ease
                    "[[Leave it off.]":
                        $ bangok_four_bryce1_protected = False
            elif not bangok_four_bryce1_brycecame:
                menu:
                    "W-Wait! Protection!":
                        show bryce brow dk bangok at Position(ypos=1.3) with ease
                        Br "Are you kidding me?"
                        c "We don't know what my stuff might do to you."
                        if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                            c "I've seen a health aisle here. You've got condoms."
                        else:
                            c "Your kind has condoms, right?"
                        show bryce stern dk bangok with dissolve
                        m "Bryce groaned, then gestured at a chest of drawers in a corner."
                        Br "Top. I think. Just hurry up."
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.wav"
                        m "There were a few different brands with \"actual size\" markings on the order of Bryce's scale. I picked one, just in case, then dug a little deeper for one my size."
                        m "Only after I dug to the bottom did I finally find a box of condoms closer to my scale, unopened."
                        m "Tearing into the packaging, I returned with the necessary equipment."
                        c "There."
                        Br smirk dk bangok "Finally."
                        show bryce at Position(ypos=1.5) with ease
                    "[[Enjoy.]":
                        pass
            show bryce at Position(ypos=1.51) with ease
            m "Pressing forward, he enveloped my entire cock in his mouth with one smooth motion, bumping up against my pelvis. I barely got a moment to enjoy the sensation, though, as..."

            play sound "fx/impact3.ogg"
            show bryce brow dk bangok at Position(ypos=1.2)
            show bangok_four_bryce1_apartment night at Pan((0,120), (0,120), 0.0)
            with vpunch
            m "I lost my balance, tripping to the floor."
            Br "Whoops."
            c "Ow."
            show bryce normal dk bangok at Position(ypos=1.2)
            show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
            with ease
            m "Picking myself up, I looked around the room for something to brace against for our next try."
            menu:
                "Wall.":
                    $ bangok_four_bryce1_oralspot = "wall"
                    c "Here, up against the wall."
                    Br smirk dk bangok "If you say so."
                    m "I leaned back against the wall slightly, spreading my legs to give Bryce easy access to my groin."
                    $ renpy.pause (0.3)
                "Couch.":
                    $ bangok_four_bryce1_oralspot = "couch"
                    c "Here, what if I sit on your couch?"
                    $ renpy.pause (0.5)
                    Br brow dk bangok "A little further forward. I don't want my chin horn tearing my cushions."
                    $ renpy.pause (0.3)
            Br flirty dk bangok "Alright. Now to see what a human tastes like."
            if bangok_four_bryce1_protected == True:
                $ brycemood -= 1
                Br brow dk bangok "Through a condom."
            show bryce smirk dk bangok at Position(ypos=1.3) with ease
            show bryce smirk dk bangok at Position(ypos=1.5) with ease
            $ renpy.pause(0.3)
            m "Bryce nestled between my legs, the scales on his snout rubbing against my thighs."
            m "The cold air of the room was, in my crotch, replaced with warmth as he exhaled."
            show bryce smirk dk bangok at Position(ypos=1.51) with ease
            m "Then he dove in, enveloping my cock and balls both in his warm maw."
            c "Mmh!"
            m "It was all I could do to sit still as his tongue wove around the base of my shaft, the tip tugging at my sac just enough to bounce and tease my balls."
            c "W-Wow."
            show bryce flirty dk bangok with dissolve
            $ renpy.pause(0.3)
            show bryce smirk dk bangok at Position(ypos=1.5) with ease
            m "Pulling back, the barest edges of his teeth and scaly lips scraped over the top of my cock and the bottom of my sack. I clenched my fists, just trying to keep my ass in place and not buck into his face."
            m "He let my balls drop free of his mouth, focusing the ministrations of his scaly lips and tongue on my shaft."
            m "It was decadant. But he wasn't all the way down in my groin; a tiny bit of my shaft remained outside his heavenly maw."
            menu:
                "[[Grab his horns.]":
                    $ bangok_four_hornincident = True
                    $ brycemood -= 2
                    if bangok_four_bryce1_oralspot == "couch":
                        play sound ["fx/hit2.ogg", "fx/cartdown.ogg"]
                        show bryce stern dk bangok at Position(ypos=1.3) with ease
                        m "Bryce jerked, releasing my cock as he slammed his muzzle into my chest, shaking the couch. It was only luck that I wasn't cut by one of his small chin and nose horns."
                    else: # bangok_four_bryce1_oralspot == "wall":
                        play sound ["fx/hit2.ogg", "fx/impact3.ogg"]
                        show bryce stern dk bangok at Position(ypos=1.3) with ease
                        m "Bryce jerked, releasing my cock as he slammed his muzzle into my chest, crushing me against the wall. It was only luck that I wasn't cut by one of his small chin and nose horns."
                    c "F-Fuck!"
                    $ renpy.pause (1.2)
                    c "Okay, don't touch the horns. Got it."
                    Br brow dk bangok "No. Do. But {i}tell{/i} me. That's a delicate spot for us. Something yanking our horns the wrong way could tear them off our skull."
                    c "I don't think I'm that strong."
                    Br stern dk bangok "Neither do I. But I'm still going to respond if I'm not expecting that."
                    m "After a moment longer of stern look, Bryce sank back down between my thighs."
                    show bryce at Position(ypos=1.5) with ease
                    show bryce flirty dk bangok with dissolve
                    m "As he set back to work, I was almost instantly back on the verge of facefucking him. His tongue slathered sparks of strong sensation into my groin, toying with my cock."
                    menu:
                        "C-Can I grab your...":
                            $ brycemood += 1
                            m "Taking his driving his face deeper into my crotch as a sign of encouragement, I grabbed Bryce's horns and thrust."
                        "[[Cum.]":
                            pass
                "[[Ask him to go deeper.]":
                    if bangok_four_bryce1_oralspot == "couch":
                        m "Bryce obliged, face pressing into my thighs and crotch while his chin horn almost cleaved my sack, and did poke the pillow."
                    else: # bangok_four_bryce1_oralspot == "wall":
                        m "Bryce obliged, face pressing my pelvis hard into the wall."
                    c "C-Careful!"
                    m "He made an uninteligible noise, the sound vibrating in his mouth around my cock."
                    m "That was all the endurance I had left."
                "I-I'm close!":
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
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                show bryce brow dk bangok with dissolve
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
                Br smirk dk bangok "I have sex with drinking buddies all the time. You think you're the first one who's pissed in me?"

            show bryce at Position(ypos=1.0) with ease
            if brycemood > 0:
                show bryce flirty dk bangok with dissolve
                m "Getting back to his feet, Bryce shot me a wink."
            else:
                show bryce stern dk bangok with dissolve
                m "Bryce got back to his feet."
            if bangok_four_bryce1_brycecame:
                jump bangok_four_bryce1_bothdone
            else:
                Br flirty dk bangok "That's you. Now how about me?"
                jump bangok_four_bryce1_preciprocity_menu




        "It's not that little..." if bangok_four_bryce1_m2_size:
            $ bangok_four_bryce1_m2_size = False
            c "I know it's probably smaller than you're used to, and probably not even enough to get you off--"
            # show bryce laugh dk bangok with dissolve
            # $ renpy.pause(0.8)
            Br smirk dk bangok "Don't worry. I've had smaller. You can use your hands or something if you can't do it with your tool."
            jump bangok_four_bryce1_m2_menu

        "I'm not sure I can fit you." if bangok_four_bryce1_m2_fit:
            call bangok_four_bryce1_m2_fit from bangok_four_bryce1_m2_menu_fit
            jump bangok_four_bryce1_m2_menu
            label bangok_four_bryce1_m2_fit:
                $ bangok_four_bryce1_m2_fit = False
                c "You're, uh..."
                Br flirty dk bangok "Not something you've seen before, huh?"
                c "Definitely."
                Br smirk dk bangok "And then, especially with my kind, they are... Well, I think you can see what I mean."
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
    if bangok_four_bryce1_playercame == False and bangok_four_bryce1_brycecame == False:
        Br stern "Not much."
    elif not bangok_four_bryce1_brycecame:
        Br stern "Not enough."
    else:
        Br stern "Too much."
    c "There was a drinking contest..."
    Br brow "Then you remember plenty."
    Br stern "Get your clothes and leave."
    c "Huh?"
    if bangok_four_bryce1_brycecame == False:
        Br "The contest was a stupid idea. That unreciprocated sex moreso."
    else:
        Br "The contest was a stupid idea. That inept attempt at sex moreso."
    c "Hang on, you were the one pushing the contest."
    Br "And you were the one pushing the sex. Bad ideas all around."
    c "That's easy to say after the fact."
    Br brow "Says the reason things went sideways."
    c "Excuse me? We were both drunk."
    Br stern "When we started last night, I thought I communicated pretty clearly that I expected things would be reciprocal."
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
    scene black with fade
    $ renpy.pause (1.5)
    scene pad at Pan ((0, 0), (0,360), 5.0) with dissolveslow
    play music "mx/campfire.ogg" fadein 2.0
    nvl clear
    window show
    n "I awoke looking at an unfamiliar ceiling."
    n "For a moment, I wondered where I was before the events of last night came back to me."
    if bangok_four_bryce1_playerstuffed or "analbot" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
        n "My innards complained loudly as I sat up, still disturbed by what I'd done to them. As I looked around, I realized I'd slept on Bryce's couch, naked."
    elif "vag" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
        n "My love passage complained loudly as I sat up, still disturbed by what I'd done to it. As I looked around, I realized I'd slept on Bryce's couch, naked."
    else:
        n "As I sat up and looked around, I realized I'd slept on Bryce's couch, naked."
    show bryce laugh at Position(ypos=1.2, xpos=0.55, xanchor='center') with dissolvemed
    n "Bryce sprawled in the gap between the couch and coffee table, drooling into the carpet. Some evidence of our wanton lust from the night before was still visible between his hindlegs, on his plates."
    window hide
    nvl clear

    c "Hey, Bryce."
    menu:
        "You are salivating.":
            $ brycemood -= 1
            m "The dragon moved and let out a groan before he opened his eyes."
            show bryce brow with dissolve
            Br "Just as you do, occasionally, I bet."
        "Wake up, fattie.":
            $ brycemood -= 2
            m "The dragon moved and let out a groan before he opened his eyes."
            show bryce stern with dissolve
            c "(That got him.)"
            Br "For your information, my kind does tend to look a little bigger than the others, but it also makes us the strongest."
            show bryce brow with dissolve
        "Good morning, sunshine.":
            $ brycemood += 1
            m "The dragon moved and let out a groan before he opened his eyes."
            show bryce normal with dissolve
    $ renpy.pause(0.9)
    show bryce brow with dissolve
    $ renpy.pause(0.5)
    m "Bryce seemed to mull his memories for a moment, then with a start began struggling to rise."
    show bryce stern at Position(ypos=1.2, xpos=0.45, xanchor='center') with ease
    show bryce at Position(ypos=1.2, xpos=0.55, xanchor='center') with ease
    m "I pushed my way up from the couch myself, then tugged his coffee table aside so he'd have room to roll over."
    show bryce at center with ease
    Br normal "Thanks."
    $ brycemood += 1
    $ renpy.pause (0.9)


    if False:
        label bangok_four_bryce1_morningfloor:
        scene black with fade
        $ renpy.pause(1.5)
        scene pad at Pan ((0, 0), (0,360), 5.0) with dissolveslow
        play music "mx/campfire.ogg" fadein 2.0

        nvl clear
        window show
        n "I awoke looking at an unfamiliar ceiling."
        n "For a moment, I wondered where I was before the events of last night came back to me."
        if bangok_four_bryce1_playerstuffed or "analbot" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            n "My innards complained loudly as I sat up, still disturbed by what I'd done to them. As I looked around, I realized I'd slept on Bryce's floor, naked."
        elif "vag" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            n "My love passage complained loudly as I sat up, still disturbed by what I'd done to it. As I looked around, I realized I'd slept on Bryce's floor, naked."
        else:
            n "As I sat up and looked around, I realized I'd apparently slept on Bryce's floor, naked."
        window hide
        nvl clear

        scene black with dissolve
        $ renpy.pause (0.5)
        scene cgbryce with dissolvemed
        $ renpy.pause(2.0)

        c "Hey, Bryce."
        menu:
            "You are salivating.":
                $ brycemood -= 1
                m "The dragon moved and let out a groan before he opened his eyes."
                scene pad at Pan ((0, 360), (0,360), 0.0)
                show bryce brow
                with dissolve
                Br "Just as you do, occasionally, I bet."
            "Wake up, fattie.":
                $ brycemood -= 2
                m "The dragon moved and let out a groan before he opened his eyes."
                scene pad at Pan ((0, 360), (0,360), 0.0)
                show bryce stern
                with dissolve
                c "(That got him.)"
                Br "For your information, my kind does tend to look a little bigger than the others, but it also makes us the strongest."
                show bryce brow with dissolve
            "Good morning, sunshine.":
                $ brycemood += 1
                m "The dragon moved and let out a groan before he opened his eyes."
                scene pad at Pan ((0, 360), (0,360), 0.0)
                show bryce normal
                with dissolve
                Br "Hey, [player_name]."
        show bryce laugh with dissolve
        m "The dragon rose from the couch with a nice morning stretch, rubbed his eyes, then held his head high as he let out a grunt and a big yawn."
        show bryce stern with dissolve
        m "Then he blinked, hard."



    Br brow "How much about last night do you remember?"

    menu:
        "I remember Bryce, it's fine.":
            c "We both chose to do that. And I, at least, had fun."
            m "Bryce relaxed immediately."
            Br normal "Ah."
        "I walked you home and that's it, right?":
            $ brycemood -= 1
            Br stern "This isn't a joke, [player_name]. Do you remember what happened between us?"
            c "Of course. I was just messing around."
            $ renpy.pause (0.8)
        "I can't believe that happened.":
            Br "In what way?"
            # menu:
            #     "How could you do that to me?":
            #         $ brycemood -= 3
            #         c "I was drunk and you took advantage of that to get in my pants."
            #         Br stern "That's not even close to how I remember it."
            #         c "And who are they going to believe? Humanity's poor, victimized ambassador, or the horny chief of police that pushed them into a drinking contest and took them back to his apartment instead of theirs?"
            #         Br brow "You were the one pushing things last night."
            #         Br stern "Why would you make this up?"
            #         c ""
            #     "That was amazing.":
            #
            c "That was amazing."
            $ brycemood += 1
            if brycemood > 2:
                show bryce smirk with dissolve
            else:
                show bryce brow with dissolve
            Br "It was definitely something."
        "My ass still hurts." if "analbot" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            Br laugh "I'm not surprised."
            Br normal "Are you going to be okay?"
            c "I think so."
        "I think I'll be walking funny today." if "vag" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            Br laugh "I'm not surprised."
            Br normal "Are you going to be okay?"
            c "I think so."
        "Bryce, the condom is still hanging from my pussy." if "vag" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb] and bangok_four_bryce1_protected and persistent.bangok_knot and bangok_four_bryce1.knotpos != "out" and not (persistent.bangok_watersports and persistent.bangok_inflation) and not bangok_four_bryce1_playerstuffed:
            Br smirk "It is?"
            m "Bryce looked."
            Br brow "Oh. Damn. It is."
            m "Leaning back on his couch, I tied off the slightly leaking end, then pulled the whole thing out of me."
            play sound "fx/uncork.ogg"
            $ renpy.pause (0.5)
            $ brycemood += 2
            Br laugh "I guess I forgot about that after knotting you, then passed out."
            c "Guess so."
        "Bryce, the condom is still hanging from my ass." if "analbot" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb] and bangok_four_bryce1_protected and persistent.bangok_knot and bangok_four_bryce1.knotpos != "out" and not (persistent.bangok_watersports and persistent.bangok_inflation) and not bangok_four_bryce1_playerstuffed:
            Br smirk "It is?"
            m "Bryce looked."
            Br brow "Oh. Damn. It is."
            m "Leaning back on his couch, I tied off the slightly leaking end, then pulled the whole thing out of me."
            play sound "fx/uncork.ogg"
            $ renpy.pause (0.5)
            $ brycemood += 2
            Br laugh "I guess I forgot about that after knotting you, then passed out."
            c "Guess so."

    if persistent.bangok_watersports and bangok_four_bryce1_playerstuffed:
        if "vag" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            m "My hand went to my womb as I felt last night's fluid results shifting around."
        else:
            m "My hand went to my gut as I felt last night's fluid results shifting around."
        if "analbot" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb] or "vag" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            m "Almost all of it was still inside!"
        else: # "oralbot" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            m "What had been in my stomach had gone straight to my bladder while I'd slept!"
        c "F-Fuck. Can I use your restroom?"
        Br brow "Of course."
        if brycemood > 0:
            if persistent.bangok_watersports == True and "oralbot" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
                Br flirty "Or you could let me have a taste."
                menu:
                    "[[Let Bryce drink your piss.]":
                        $ brycemood += 1
                        m "I stumbled over to Bryce, not sure how long I could hold it."
                        show bryce at Position(ypos=1.3) with ease
                        show bryce at Position(ypos=1.5) with ease
                        show bryce laugh with dissolve
                        m "He dropped, then opened his mouth wide, letting me piss right into the back of his throat."
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        if bangok_four_playerhasdick == True:
                            c "Ahh..."
                            m "My golden stream spattered against the back of his throat, which I could see working to swallow it as I went."
                            m "My cock hardened, aroused by getting to use the big, beefy police dragon as my own personal pisshole. As it twitched, a few rivulets ran down the sides of his muzzle."
                            stop soundloop fadeout 3.0
                            $ renpy.pause (2.5)
                            show bryce at Position(ypos=1.3) with ease
                            m "Bryce gave the tip of my dick a lick as he began to stand back up. {w=0.5}{nw}"
                            show bryce at center with ease
                            m "Bryce gave the tip of my dick a lick as he began to stand back up. {fast}Then wiped his mouth with a foreleg, licking that too."
                            $ renpy.pause(0.8)
                            c "So are we going for round two?"
                            Br laugh "Not a chance!"
                            Br smirk "I've gotta clean up, you've gotta do the same. People are going to notice if neither of us are at our jobs."
                            c "Damn."
                        else:
                            c "Ahh..."
                            m "I pressed my pussy into his maw, treating him like a massive, living toilet, on which I sat the wrong way."
                            m "Hot breath washed over my privates between his swallows. His teeth just teased my taint and lower belly, and his tongue dug up into me, seeking out more of my golden fluid."
                            stop soundloop fadeout 3.0
                            c "M-Mh!"
                            m "Other fluid joined my urine and his saliva as he kept searching."
                            label bangok_four_bryce1_morningride_menu:
                            menu:
                                "Y-You're getting me going!":
                                    show bryce flirty with dissolve
                                    m "Bryce winked up at me, knowing exactly what he was doing."
                                    jump bangok_four_bryce1_morningride
                                "C-Can I grab your horns?" if bangok_four_hornincident == True:
                                    $ brycemood += 1
                                    show bryce flirty with dissolve
                                    m "Bryce winked up at me. Taking that as approval, I grabbed his horns and pulled his face deeper into my crotch."
                                    jump bangok_four_bryce1_morningride
                                "[[Get off him.]":
                                    $ brycemood -= 1
                                    m "I got a hand on his muzzle and moved a half step back."
                                    c "B-Bryce, let's talk about this first!"
                                    m "A hot sigh washed over my lower belly, then Bryce withdrew his tongue and let me safely step clear."
                                    show bryce normal with dissolve
                                    $ renpy.pause(0.3)
                                    show bryce at Position(ypos=1.3) with ease
                                    $ renpy.pause(0.5)
                                    show bryce at center with ease
                                    m "I caught my breath."
                                    c "Is this you saying you want a round two?"
                                    Br flirty "I do wish."
                                    Br stern "But unfortunately, we've both got work to think about."
                                    Br smirk "I've gotta clean up, you've gotta do the same. People are going to notice if neither of us are at our jobs."
                                    c "Oh. Damn."
                                "[[Ride him.]":
                                    label bangok_four_bryce1_morningride:
                                    show bryce laugh with dissolve
                                    m "Legs weakening, I let more of my weight rest on his jaws, his teeth pressing slightly harder against my delicate skin."
                                    c "Ohgod."
                                    play sound "fx/cartdown.ogg"
                                    with vpunch
                                    m "Bryce pressed harder, causing me to stumble back a few steps until I landed heavily on the couch."
                                    show bryce flirty with dissolve
                                    m "His tongue dug deeper, now that he was no longer at risk of biting into me."
                                    m "The rough tastebuds now teasing in and out past my clit were too much."
                                    show black
                                    show bryce laugh
                                    with fadequick
                                    m "I clenched around his tongue in undulating waves, coming down blissfully slowly."
                                    hide black with dissolveslow
                                    $ renpy.pause(0.5)
                                    m "Bryce ran his tongue over my vaginal lips like a parting kiss as he drew his tongue back."
                                    show bryce smirk with dissolve
                                    show bryce at Position(ypos=1.3) with ease
                                    $ renpy.pause(0.3)
                                    show bryce at center with ease
                                    m "Then he got to his feet."
                                    menu:
                                        "F-Fuck. That was amazing.":
                                            $ brycemood += 1
                                            Br flirty "You bet."
                                        "Your turn?":
                                            Br laugh "Not a chance!"
                                    Br normal "Unfortunately, we've both got work."
                                    Br smirk "I've gotta clean up, you've gotta do the same. People are going to notice if neither of us are at our jobs."
                                    c "O-oh. Damn."
                                "[[Grab his horns and ride.]" if bangok_four_hornincident == False:
                                    $ brycemood -= 2
                                    play sound ["fx/hit2.ogg", "fx/impact3.ogg"]
                                    show bryce angry with vpunch
                                    show bryce stern at center
                                    show pad at Pan((0,120), (0,120), 0.0)
                                    with ease
                                    with vpunch
                                    m "Bryce jerked, yanking his head down and back before headbutting my delicate spot with the tip of his muzzle. My feet physically lifted off the floor before I tumbled to the ground, stunned by the drop."
                                    c "D-Damnit Bryce, what the hell?"
                                    Br "That's a delicate spot for us. Something yanking our horns the wrong way could tear them off our skull."
                                    c "I don't think I'm that strong."
                                    Br brow "Neither do I. But I'm still going to respond if I'm not expecting that."
                                    c "S-Sorry."
                                    $ renpy.pause (0.5)
                                    c "Ow."
                                    show pad at Pan((0,360), (0,360), 0.0) with ease
                                    m "I got back to my feet slowly, still shaking off the injury."
                                    c "So... did that tonguefucking mean you want a round two?"
                                    Br smirk "I'd have liked to."
                                    Br stern "But we've both got work to think about."
                                    Br smirk "I've gotta clean up, you've gotta do the same. People are going to notice if neither of us are at our jobs."
                                    c "Oh. Damn."

                        Br normal "Hey. Don't be too sad about it."
                        jump bangok_four_bryce1_morningcont
                    "[[Restroom. Now.]":
                        pass
            elif "vag" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
                Br flirty "Or you could let me have a taste."
                menu:
                    "[[Let Bryce drink his fluids back out.]":
                        $ brycemood += 1
                        m "I stumbled over to Bryce, not sure how long I could hold it."
                        show bryce at Position(ypos=1.3) with ease
                        show bryce at Position(ypos=1.5) with ease
                        show bryce laugh with dissolve
                        m "He dropped, then opened his mouth wide, letting me push the contents of my womb into the back of his throat."
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        play sound (["fx/stones.ogg"]*10) fadein 3.0
                        c "Ahh..."
                        m "I pressed my pussy into his maw. Hot breath washed over my privates between his swallows. His teeth just teased my taint and lower belly, and his tongue dug up into me, seeking out more of his seed."
                        stop sound fadeout 2.0
                        stop soundloop fadeout 1.0
                        c "M-Mh!"
                        m "Other fluid joined our coital results and his saliva as he kept searching, even as I ran out of what I could push."
                        jump bangok_four_bryce1_morningride_menu
                    "[[Restroom. Now.]":
                        pass
            # Feck. I don't know enough about rimming for this.
            # elif "analbot" in [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            #     Br flirty "Or you could let me lick it out."
            #     menu:
            #         "[[Let Bryce rim you.]":
            #             c "G-Gonna have to do it fast. I don't know how long I can..."
            #             show bryce at Position(ypos=1.3) with ease
            #             show bryce at Position(ypos=1.5) with ease
            #             m "He moved over and bent down, head snaking between my legs, which I spread to give him better access."
            #             c "H-Hey--"
            #             m "My complaint was cut off when I felt his large tongue slither into my ass, disturbing the fluid in my rear."

            #         "[[Restroom. Now.]":
            #             pass
        hide bryce with dissolve
        scene black with dissolve
        play sound "fx/door/doorclose3.wav"
        m "I scrambled into the restroom and dumped my excess fluid weight into the toilet."
        $ renpy.pause(1.8)
        scene pad at Pan ((0, 360), (0,360), 0.0)
        show bryce normal
        with dissolvemed
        Br "Better?"
        c "Yeah."

    label bangok_four_bryce1_morningcont:
    $ renpy.pause (1.0)

    if brycemood > 0:
        if brycemood > 4:
            Br flirty "You know, last night was up there with some of the best sex I've ever had."
            c "Really?"
            Br smirk "Really. You've got a lot of... unique properties."
        elif brycemood > 2:
            Br flirty "Last night was a good time."
            Br normal "I'm glad we did that at the end."
            c "I'm glad we did too."
            Br smirk "You've got a lot of... unique properties."
        else:
            Br normal "So... last night. There were a few misunderstandings, but I think it worked out."
            Br smirk "Certainly very unique."
        menu:
            "So you liked it just because I'm human.":
                $ brycemood -= 1
                Br brow "It's not just that."
                c "..."
                Br normal "Okay, so that may have been a major part of it."
            "You were great too.":
                $ brycemood += 1
                Br flirty "Is that so?"
            "[[Say nothing.]":
                pass

        Br brow "Thing is, I don't normally take relationships this fast. Not even when I plan for them to be one-night-stands."
        c "So it takes you two nights to have a one-night stand?"
        Br normal "Usually, yeah. That drinking contest was an especially stupid idea for me to propose, especially to you."
        c "Well, it's not like you forced me to participate, so I suppose I share some of the blame..."
        Br "Let's just pretend the drinking never happened, and maybe hold off on more sex until we've had time to cool off about what happened."
        c "Deal."
        Br normal "Don't take it the wrong way, though. I would like to invite you over sometime and show you there's more to the chief of police than getting drunk and having drunken sex."
        c "Like sober sex?"
        Br flirty "Not quite yet."
        Br normal "Let's scale back to \"friends\" for at least one encounter."
        c "Sure."
        Br smirk "You can find all your layers?"
        c "Yeah."
        stop music fadeout 1.0
        python:
            renpy.pause(1.0)
            brycestatus = "good"
            brycescenesfinished = 1
            persistent.bryce1skip = True
            bangok_four_bryce1_unplayed = False
        scene black with dissolveslow
        jump _mod_fixjmp
    else:
        Br stern "Last night, you and I had some serious miscommunications."
        c "Oh?"
        Br brow "I'm not saying I'm upset we did it, or that I didn't have a good time, but we were definitely too drunk to communicate properly."
        Br stern "The whole contest thing before that was a stupid idea too, and I shouldn't have suggested it, especially not to you"
        c "Well, it's not like you forced me to participate, so I suppose I share some of the blame..."
        show bryce normal with dissolve
        Br "Let's just pretend the whole thing never happened."
        menu:
            "Including the sex?":
                Br smirk "Let's just take some time to cool down on that front. That first time was a little too raunchy, even for me."
                Br stern "And we definitely need our next time to be mostly sober. If we do decide to have a next time."
                c "Deal."
            "Deal.":
                pass
        show bryce brow with dissolve
        Br "Wait... what time is it?"
        Br "Damn, I should really get cleaning up. I think I'll be a few minutes late for work. You know how to get back to your apartment from here, right?"
        c "I think so."
        show bryce normal with dissolve
        Br "Guess you should be going as well, kiddo. Maybe I'll see you some other time."
        stop music fadeout 1.0
        python:
            brycestatus = "neutral"
            brycescenesfinished = 1
            persistent.bryce1skip = True
            bangok_four_bryce1_unplayed = False
        jump _mod_fixjmp

label bangok_four_bryce1_bryce2fix:
    c "You didn't see the other night?"
    Br flirty "I was a little more focused on other parts."
    Br laugh "But seriously? Everything alive has a tail. How can you just not have one?"
    jump bangok_four_bryce1_bryce2fix_end
