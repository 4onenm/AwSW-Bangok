init python in bangok_four_kalinth:
    have_number = False # type: bool
    protection = None # type: Optional[bool]
    ws_position = None # type: Optional[Literal["mouth", "inside"]]

label bangok_four_kalinth_c3arc_bangnokay:
    show kalinth at left with ease
    menu:
        "Call after her.":
            pass
        "Let her go.":
            jump bangok_four_kalinth_c3arc_return

    c "Hey, Kalinth, wait up."
    Kl normal flip "Yes?"

    menu:
        "Proposition her.":
            pass
        "Nothing, never mind.":
            show kalinth normal with None
            jump bangok_four_kalinth_c3arc_return

    c "You know, I bet this office sees some fun on those couches."
    c "Do you want to find out what a human can do?"
    Kl "I'm not sure I understand."
    menu:
        "Explain.":
            pass
        "Never mind.":
            m "I cleared my throat, trying to put the moment behind us."
            c "It's probably a bad idea anyway. Forget I said anything."
            show kalinth normal with None
            jump bangok_four_kalinth_c3arc_return

    m "I rub my crotch, giving her a wink."
    c "Do you want to share a bit of casual intimacy?"

    Kl bangok surprise flip "Oh!"
    $ renpy.pause (0.5)
    Kl normal flip "No. I'm not interested in that, and I'm not sure why you'd think I would be."
    Kl bangok surprise flip "Is this more common for humans? To ask about that after only just meeting someone?"
    c "... Uh."
    Kl normal "Never mind. I'll just be going now."
    jump bangok_four_kalinth_c3arc_return

label bangok_four_kalinth_c3arc:
    show kalinth at Position(xpos=-0.2, xanchor=0.0) with ease
    if bangok_four_common.bangnokay.check():
        jump bangok_four_kalinth_c3arc_bangnokay

    m "Despite saying she was on her way out, Kalinth lingered in the doorway."
    c "Is there anything else?"
    show kalinth bangok normal blush flip with dissolve
    Kl "There... is something else."
    play sound "fx/door/doorclose.ogg"
    show kalinth bangok furtive blush flip with dissolve
    m "Kalinth closed the office door, then shifted her weight between her feet, looking around Bryce's office at seemingly anything but you for a moment."
    c "What is it?"
    Kl bangok normal blush flip "I've been reading all the reports on your kind thus far, and... there's something I'm interested in trying. Only if you are interested, of course."
    menu:
        "You could say I'm interested.":
            Kl bangok smile blush flip "Oh, good. I was hoping you'd say that."
            show kalinth bangok normal blush flip:
                zoom 1.0
                ease 0.5 zoom 1.1 xpos 0.5 xanchor 0.5
                zoom 1.1 xpos 0.5 xanchor 0.5
            with None
            m "Kalinth trod a little closer."
            Kl "But just to be clear, I'm implying casual intimacy. That's not too far for you, is it?"
        "I think I'd have to know what it is first.":
            c "What do you want to try?"
            show kalinth bangok normal blush flip:
                zoom 1.0
                ease 0.5 zoom 1.1 xpos 0.5 xanchor 0.5
                zoom 1.1 xpos 0.5 xanchor 0.5
            with None
            m "Kalinth trod a little closer."
            Kl bangok furtive blush flip "Absolutely feel free to say no if it's too far, but I thought... perhaps you and I could share a bit of casual intimacy."
        "If it's what I think it is, no thanks.":
            label bangok_four_kalinth_c3arc_abrupt_departure:
            Kl normal "Oh. I see. Well, I'm sorry to have bothered you. I'll just be going now."
            hide kalinth with easeoutleft
            $ renpy.pause (0.3)
            play sound "fx/door/doorclose.ogg"
            $ renpy.pause (0.5)
            m "Kalinth hurried out of the office, leaving me alone with the files."
            jump c3arcques

    show kalinth bangok normal blush flip with dissolve
    m "Kalinth glanced down at my crotch, making her intentions clear. Her tail twitched as she waited for my answer, the end swishing back and forth across the floor."

    menu:
        "Accept.":
            pass
        "Reject.":
            m "I took a step back."
            c "Oh, wow, I really misread that. No, I'm not interested."
            jump bangok_four_kalinth_c3arc_abrupt_departure

    c "That sounds like fun."
    show kalinth bangok smile blush flip with dissolve
    c "Right here in Bryce's office, though?"
    Kl bangok smilewink blush flip "I don't think we'll be disturbed here for a while."
    Kl bangok normal blush flip "This office has also seen plenty of use by various members of the department, so it's not like this is anything new. But I can also give you my number for another day, if you prefer."

    menu:
        "Let's go for it.":
            pass
        "I'd rather have your number.":
            Kl normal flip "Alright."
            play sound "fx/scribblex.ogg"
            m "Kalinth wrote down her number on a scrap of paper, then handed it to me."
            show kalinth bangok normal blush with dissolve
            Kl "I'll leave you to your work, then."
            jump bangok_four_kalinth_c3arc_return

    Kl bangok surprise blush flip "I assume you'll have to remove your..."
    m "She gestured to my clothes."

    play sound "fx/undress.ogg"
    m "I hurriedly began undressing, not wanting to keep the dragoness waiting."
    if bangok_four_playerhasdick is None:
        m "Once I was nude, my..."
        menu:
            "Once I was nude, my...{fast}"
            "... erect member":
                $ bangok_four_playerhasdick = True
            "... lower lips":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick:
        jump bangok_four_kalinth_c3arc_male
    else:
        jump bangok_four_kalinth_c3arc_female

label bangok_four_kalinth_c3arc_female:
    m "Once I was nude, my{fast} lower lips exposed to the air of the room, she stopped abruptly."
    play sound "fx/system3.wav"
    if persistent.bangok_dev:
        s "It seems this scene still lacks a female player version."
    else:
        s "It seems this scene still lacks a female player version, yet somehow you managed to trigger it. Please report this to the mod author."
    s "For now, you will receive Kalinth's phone number and be left with the police files."
    $ bangok_four_kalinth.have_number = True
    jump bangok_four_kalinth_c3arc_return


label bangok_four_kalinth_c3arc_male:
    show kalinth bangok smile blush flip with dissolve
    m "Once I was nude, my{fast} erect member exposed to the air of the room, she backed me up toward the armrest of the nearer of the two couches, smirking."

    label bangok_four_kalinth_c3arc_male_position_menu:
    menu:
        "Ask about protection." if bangok_four_kalinth.protection is None and bangok_four_kalinth.ws_position is None:
            c "Do you have any protection?"
            Kl bangok surprise blush flip "We're different species, so pregnancy isn't a concern."
            Kl bangok normal blush flip "But I do think I remember where Bryce keeps some condoms, if you'd like to use one."
            menu:
                "Use a condom.":
                    $ bangok_four_kalinth.protection = True
                    c "I'd like to use one."
                    Kl normal flip "Alright."
                    hide kalinth with dissolve
                    play sound "fx/rummage.wav"
                    m "Kalinth rummaged through Bryce's desk, then set a box of condoms on top."
                    m "She took one out between her lips, then slunk back over to me with a sultry look in her eyes."
                    show kalinth bangok smile blush flip with dissolve
                    c "Thanks."
                    m "I took the condom from her lips, then tore it open and rolled it onto my shaft."
                "Go without.":
                    $ bangok_four_kalinth.protection = False
            jump bangok_four_kalinth_c3arc_male_position_menu
        "Ask about a restroom." if persistent.bangok_watersports and (not bangok_four_kalinth.protection) and (not bangok_four_kalinth.ws_position):
            m "Standing erect and nude next to her, I suddenly realized my bladder was rather full."
            c "Er... I should probably use the restroom first."
            Kl bangok surprise blush flip "Oh, wow. Your timing is worse than... well, never mind."
            m "The look on her face was one of disappointment."
            Kl bangok normal blush flip "I suppose I can wait a little longer."
            Kl bangok smilewink blush flip "Unless you'd like to use me as a urinal?"
            menu:
                "Sure.":
                    pass
                "No thanks.":
                    c "I'm not sure what that entails, but I think I'll pass."
                    show kalinth normal flip with dissolve
                    m "She pouted."
                    Kl "Well, hurry back."
                    show black with dissolve
                    m "I threw my pants and shirt on haphazardly, struggling to fit my erection beneath my waistband, then hurried to the restrooms."
                    m "A few minutes later I returned to the office."
                    hide black
                    show kalinth bangok furtive blush flip
                    with dissolve
                    Kl "Done ruining the mood?"
                    c "Sorry."
                    jump bangok_four_kalinth_c3arc_male_position_menu

            c "I didn't think you'd be into something like that. Sure."
            Kl bangok smile blush flip "Mm. Well, we don't want to make a mess on Bryce's floor. I could drink it down right now..."
            Kl "Or if you're into it you could piss it into me while you're inside, leave me even more dripping wet between the legs..."
            menu:
                "Mouth, now.":
                    $ bangok_four_kalinth.ws_position = "mouth"
                    show kalinth:
                        pause 0.5
                        yanchor 1.0
                        ease 0.5 yanchor 0.2
                        yanchor 0.2
                    with None
                    m "I rested my hand on one side of her snout, then guided it down to my erection."
                    m "She eagerly wrapped her scaly lips around me, but didn't slurp or suck as she waited for me to urinate into her mouth."
                    m "It was a strange and exciting sensation... I could feel the heat from her breath against my shaft, and the wetness of her tongue as she waited for me to let go."
                    show black with dissolve
                    m "I closed my eyes, trying to relax, and let my bladder empty into her mouth, feeling the familiar rush of relief as my member began to disgorge a steady stream of piss against the back of Kalinth's throat."
                    m "She swallowed it down eagerly, not once pulling away from me until I had finished."
                    hide black
                    show kalinth bangok smile eyesclosed blush flip
                    with dissolve
                    m "The sight of her swallowing every last drop left me with an erection that was even harder than before, and she seemed to be enjoying it as well from the way she licked her lips."
                    Kl bangok smile blush flip "Mmm... you taste interesting."
                    m "She gave my member a slow lick, from balls to tip, then stepped back with an amused smirk."
                    show kalinth:
                        yanchor 0.2
                        ease 0.5 yanchor 1.0
                        yanchor 1.0
                    with None
                    Kl "I've never tasted a human's piss before. Now I'm curious what your cum tastes like."
                    c "I'm sure you'll find out soon enough."
                "Inside.":
                    $ bangok_four_kalinth.ws_position = "inside"
                    c "Inside."
                    m "I felt my erection twitch in anticipation."
                    Kl bangok smile blush flip "Then let's get started."
            jump bangok_four_kalinth_c3arc_male_position_menu
        "Let her take charge.":
            jump bangok_four_kalinth_c3arc_male_mcbottom
        "Take charge yourself.":
            jump bangok_four_kalinth_c3arc_male_mctop
        "Ask her to turn around.":
            jump bangok_four_kalinth_c3arc_male_doggy

label bangok_four_kalinth_c3arc_male_mcbottom:
    m "I sat back on the couch armrest, letting the assertive dragon archivist take charge."
    show kalinth bangok smile blush flip:
        zoom 1.0
        ease 0.5 zoom 1.5
        zoom 1.5
    with None
    if persistent.bangok_cloacas:
        m "She reared up, resting her forelegs over my shoulders as her spread rear legs revealed her glistening cloaca, searching with her hips for my shaft."
    else:
        m "She reared up, resting her forelegs over my shoulders as her spread rear legs revealed her glistening lower lips, searching with her hips for my shaft."
    show kalinth bangok smile blush flip:
        zoom 1.5
        ease 0.5 zoom 1.6
        zoom 1.6
        block:
            ease 1.2 ypos 1.01
            ease 1.2 ypos 1.0
            repeat
    with None
    if persistent.bangok_cloacas:
        m "Then, pressing my back against the couch's back, she began to tease her cloaca open with my tip, grinding against my erection without letting it in."
    else:
        m "Then, pressing my back against the couch's back, she began to tease her labia open with my tip, grinding against my erection without letting it in."

    m "I groaned as the dragoness rubbed herself against me."
    m "Her tail swished behind her, making a faint rustling sound with each movement."
    $ renpy.pause (0.5)
    c "Are you going to make me wait like this? I don't know how long I can take it."

    m "Kalinth chuckled with my face against her fine underbelly scales before she pushed off a little to look me in the eye."
    show kalinth bangok smile blush flip:
        zoom 1.6
        ease 0.5 zoom 1.5
        zoom 1.5
        block:
            ease 1.2 ypos 1.01
            ease 1.2 ypos 1.0
            repeat
    with None

    Kl "I'll let you inside eventually. But first I just want to feel you all over me down there before..."
    show kalinth bangok smile eyesclosed blush flip:
        ease 0.8 ypos 1.01
        ease 1.2 ypos 1.2
    with None
    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "Her breathing caught and she closed her eyes as her cloaca slid up to my tip again, then she began to lower herself down, enveloping my condom-wrapped erection with the warmth of her draconic anatomy."
        else:
            m "Her breathing caught and she closed her eyes as her labia slid up to my tip again, then she began to lower herself down, enveloping my condom-wrapped erection with the warmth of her draconic pussy."
    else:
        if persistent.bangok_cloacas:
            m "Her breathing caught and she closed her eyes as her cloaca slid up to my tip again, then she began to lower herself down, enveloping my erection with the warmth of her draconic anatomy."
        else:
            m "Her breathing caught and she closed her eyes as her labia slid up to my tip again, then she began to lower herself down, enveloping my erection with the warmth of her draconic pussy."
    c "Oh fuck."
    m "As she took every inch of me, I moaned."
    m "Her tail twitched with excitement, rubbing back and forth across the surface of the table."
    show kalinth bangok eyesclosed blush flip with dissolve
    if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        Kl "Mm. Now. Let your bladder go. Fill me up."
        m "My erection throbbed within her warm, all-encompassing depths as I struggled to relax enough to begin peeing myself inside the dragoness."
        m "I could feel the warmth of her insides around my cock, and it made it difficult to resist letting out a groan as she urged me on with gentle circling of her hips."
        m "Finally, I began to let go."
        m "The stream trickled at first, then began to jet out hard, spraying into her cloaca."
        m "Kalinth moaned in pleasure, squeezing me to try to keep it all inside her."
        Kl "Deep and warm..."
        m "I didn't stop until my bladder was empty."
    else:
        m "She paused for a moment on my lap, seemingly struggling to take things slow."
    $ renpy.pause (0.5)
    show kalinth bangok eyesclosed blush flip:
        ease 1.2 ypos 1.18
        ease 1.2 ypos 1.2
        repeat
    with None
    if bangok_four_kalinth.protection:
        m "Then she began to gently thrust herself against me, her scaly lower lips rubbing over the thin barrier between us in the most delightful way imagineable."
    else:
        m "Then she began to gently thrust herself against me, her scaly lower lips rubbing over my member in the most delightful way imagineable."

    if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        if persistent.bangok_cloacas:
            m "I grabbed onto the couch back tight as I felt Kalinth's piss-stained cloaca enveloping me, gripping me tighter with every stroke."
        else:
            m "I grabbed onto the couch back tight as I felt Kalinth's piss-stained passage enveloping me, gripping me tighter with every stroke."
    else:
        if persistent.bangok_cloacas:
            m "I grabbed onto the couch back tight as I felt Kalinth's cloaca enveloping me, gripping me tighter with every stroke."
        else:
            m "I grabbed onto the couch back tight as I felt Kalinth's passage enveloping me, gripping me tighter with every stroke."
    m "The heat radiating from her smooth scales was intoxicating."
    m "My hips twitched, desparate for more, but she seemed to enjoy this weighty but gentle slow thrusting so much that it was hard to bring myself to complain about it."

    show kalinth bangok smile eyesclosed blush flip:
        ease 1.2 ypos 1.18
        ease 1.2 ypos 1.2
        ease 1.0 ypos 1.17
        ease 1.0 ypos 1.2
        ease 0.8 ypos 1.17
        ease 0.8 ypos 1.2
        block:
            ease 0.8 ypos 1.17
            linear 0.5 ypos 1.2
            repeat
    with None

    m "It wasn't until she moaned loudly and began thrusting even faster that I finally knew the moment had come when she was ready for something more forceful."

    m "I groaned as Kalinth finally started fucking me in earnest, her tail whipping back and forth like a flag in the wind of our passion."

    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "Her cloaca leaked copious lubrication around the condom, making my shaft slide in and out with ease as our mating point gave wetter and louder slaps against my groin."
        else:
            m "Her vagina leaked copious lubrication around the condom, making my shaft slide in and out with ease as our mating point gave wetter and louder slaps against my groin."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "I couldn't tell the difference between my urine and her copious lubrication leaking from our mating point. My shaft slid in and out with ease as our groins made wetter and louder slaps against each other."
        m "The smells of urine and sex filled the air."
    else:
        if persistent.bangok_cloacas:
            m "Her cloaca leaked copious lubrication around my shaft, making it slide in and out with ease as our mating point gave wetter and louder slaps against my groin."
        else:
            m "Her vagina leaked copious lubrication around my shaft, making it slide in and out with ease as our mating point gave wetter and louder slaps against my groin."

    m "I tried to lift my hips a little, thrusting deeper into her, but I could do no better than her weight already pressing down on me."

    show kalinth bangok smile eyesclosed blush flip:
        parallel:
            ease 0.7 ypos 1.17
            linear 0.4 ypos 1.2
            repeat
        parallel:
            zoom 1.5
            ease 1.0 zoom 1.6
            zoom 1.6
    with None
    m "Still, the motion caused her to hug me to her chest again, bringing us closer together in the throes of our passion."

    Kl bangok smile eyeslidded blush flip "Don't cum just yet..."
    m "She rode me harder and faster, each stroke seeming more desparate than the one before."
    $ renpy.pause (0.5)
    Kl "I want..."
    Kl bangok eyesclosed blush flip "I need..."
    show kalinth bangok smile eyesclosed blush flip:
        linear 0.4 ypos 1.2 zoom 1.6
        ypos 1.2 zoom 1.6
    with None
    m "She moaned, then buried herself on my erection to the hilt, her tail swishing wildly behind her as her passage spasmed and clenched around my shaft."
    Kl "Now!"

    if bangok_four_kalinth.protection:
        m "I complied with a moan of my own, feeling my orgasm surge forth into the condom reservoir buried as deep in her kneading nethers."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "I complied with a moan of my own, feeling my orgasm surge forth into her urine-slickened, kneading nethers."
    else:
        m "I complied with a moan of my own, feeling my orgasm surge forth into her kneading nethers."
    m "My member throbbed within her heat and wetness as she lay her body atop mine, resting her weight on my hips to force me as deep within her as I could be."
    show kalinth bangok smile eyesclosed blush flip:
        parallel:
            ease 1.2 ypos 1.19
            ease 1.2 ypos 1.20
            repeat
        parallel:
            pause 0.6
            block:
                ease 1.2 xpos 0.51
                ease 1.2 xpos 0.5
                repeat
    $ renpy.pause(0.8)
    m "Then the dragoness began grinding herself against me in slow circles, savoring the feeling of the tail-end of my release still spurting slowly into her."
    $ renpy.pause(1.2)
    if bangok_four_kalinth.protection:
        m "Her juices dribbled down between my thighs as my erection faded, leaving us just merely lying together with soiled groins... though the condom still protected her depths from my seed.."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "The slurry of our fluids dribbled down between my thighs as my erection faded, leaving us just merely lying together with soiled groins."
    else:
        m "My cum and her juices dribbled down between my thighs as my erection faded, leaving us just merely lying together with soiled groins."

    $ renpy.pause(0.8)
    m "After a few minutes had passed, Kalinth finally took a few deeper breaths than her panting afterglow."
    Kl bangok smile eyeslidded blush flip "Oh... wow."
    show kalinth bangok smile eyeslidded blush:
        zoom 1.6
        ease 0.8 xpos 0.6 zoom 1.0
        xpos 0.6 zoom 1.0
    with None
    m "She rolled off of me to lie down on the couch properly, while I continued to splay across the armrest and seat back."
    Kl "That was... even better than I'd imagined."
    m "I nodded, panting hard myself as I sat up."

    jump bangok_four_kalinth_c3arc_male_post_intimacy


label bangok_four_kalinth_c3arc_male_mctop:
    c "Actually, could you lie down? I'd like to be in control for this."
    if persistent.bangok_cloacas:
        m "Kalinth quickyl agreed. She lay across the couch, her tail swishing and wings fluttering as she settled into a comfortable position and spread her legs to reveal her glistening draconic cloaca."
    else:
        m "Kalinth quickyl agreed. She lay across the couch, her tail swishing and wings fluttering as she settled into a comfortable position and spread her legs to reveal her glistening wet lower lips, and her tailhole a short distance behind."
    m "I couldn't help but stare at that gorgeous sight for a moment while the dragoness watched my every move with anticipation."

    menu:
        "Finger her.":
            jump .finger
        "Lick her.":
            jump .lick
        "Enter her.":
            jump .enter

    label .finger:
        jump todo_out_of_content_bangok_four_kalinth

    label .lick:
        jump todo_out_of_content_bangok_four_kalinth

    label .enter:
        jump todo_out_of_content_bangok_four_kalinth

        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            Kl "Don't hold back. Go ahead. Piss in me."
            m "It took me a few moments to relax as I ground my crotch against hers, feeling my member move within her warm depths."
            m "Then, at last, I felt the familiar rush of relief as I began to drain my full bladder into the dragoness below me."
            m "She moaned and purred all the while, seeming even more turned on by this degrading act than I was."
            m "As my hot jet of piss began to relax into a trickle, Kalinth's depths squeezed, soaking my member with my waste and her own fluids."
            m "Then she spoke up again."
            Kl "Keep going. Fuck me and cum inside and don't stop until you're empty."
            m "I took her words as an invitation. With renewed vigor, I began thrusting into the dragoness"
        jump todo_out_of_content_bangok_four_kalinth


label bangok_four_kalinth_c3arc_male_doggy:
    m "I patted the armrest of the couch."
    c "Do you want me to bend you over... this...?"
    m "I trailed off, realizing as she approached me on all fours that there wasn't really much bending over to be done."
    show kalinth bangok smile blush flip with dissolve
    m "She seemed to understand what I meant, though."
    Kl "That works."
    show kalinth at Position(xpos=0.6, ypos=1.1) with ease
    if persistent.bangok_cloacas:
        m "She lay down over the end of the couch with her hindlegs over the armrest. Then she lifted her tail, exposing between her spread legs her glistening cloaca already soaked with arousal and waiting for me."
        Kl "I'm ready whenever you are."
    else:
        m "She lay down over the end of the couch with her hindlegs over the armrest. Then she lifted her tail, exposing between her spread legs her glistening scaly pussy lips and tight tailhole, the former already soaked with arousal and waiting for me."
        Kl "Stay out of my tailhole, please. Otherwise I'm ready whenever you are."

    menu:
        "Finger her.":
            jump .finger
        "Lick her.":
            jump .lick
        "Enter her.":
            jump .enter

    label .finger:
        show kalinth:
            ease 0.5 zoom 1.2
            zoom 1.2
        with None
        m "As I approached her from behind, I couldn't help but gaze at her puffy, exposed lower lips."
        m "Wanting to make sure she was fully ready, I chose to start with my fingers."
        m "Sliding them inside her, I felt the heat of her insides and the slickness of her arousal coating my digits as they parted her labia."
        m "Kalinth gasped, breath shdudering as I touched her."
        Kl bangok smile eyeslidded blush flip "Oh, yes. So soft..."
        Kl bangok surprise blush flip "But please, don't tease for too long. I want you inside me."
        menu:
            # "Keep fingering her.":
            #     pass
            "Lick her.":
                jump bangok_four_kalinth_c3arc_male_doggy.lick
            "Enter her.":
                jump bangok_four_kalinth_c3arc_male_doggy.enter

        # m "I continued to finger her, feeling her insides clench and unclench around my digits as she moaned and panted."
        # Kl normal flip "A-Are you going to make me beg? Take me, please!"

        # jump todo_out_of_content_bangok_four_kalinth
    
    label .lick:
        show kalinth:
            ease 0.8 zoom 1.7
            zoom 1.7
        with None
        m "I couldn't help but wonder how the juices around that gorgeous hole tasted, so I knelt on the floor between her hindlegs, spreading her thighs with my hands for easier access."
        m "Parting her labia with the index finger of one hand, I found just how wet she was for me already as I inhaled the sweet scent of her arousal."
        m "It was intoxicating and only heightened the taste of her as I began to tease her entrance lightly with the tip of my tongue, lapping up her juices liberally as she shuddered beneath my hands and mouth."

        Kl bangok smile eyeslidded blush flip "I almost don't want to make you stop. But we can't spend all night here..."

        m "She shifted as I kept going a little longer."
        
        Kl bangok normal blush flip "Please, I want your length, not just your tongue."

        show kalinth:
            zoom 1.7
            ease 0.8 zoom 1.1
            zoom 1.1
        with None

        m "Reluctantly I got back to my feet."

    label .enter:
        m "My erection throbbed in response to the sight of the eager dragoness before me and her beautiful rear framing her wet, open passage."
        m "I ran my hands over her scaly flanks, feeling the muscle beneath as she arched her back in anticipation."
        show kalinth:
            zoom 1.1
            ease 0.5 zoom 1.2
            pause 0.5
            ease 0.5 zoom 1.3 ypos 1.2
            zoom 1.3 ypos 1.2
        if persistent.bangok_cloacas:
            m "I lined up our bodies, then slid myself into her from behind, entering her eager cloaca."
        else:
            m "I lined up our bodies, then slid myself into her from behind, entering her eager passage."

        show kalinth:
            ypos 1.2
            ease 0.8 ypos 1.25
            ease 0.8 ypos 1.2
            repeat
        m "She moaned loudly, claws digging into the couch fabric and wings rustling softly under me as I began to gently inside of her."

        m "Kalinth was panting hard even before we really got started."

        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            Kl "Mm. Now use me. Piss into me while you're fucking me."
            
            m "It was hard to relax enough to do so at first, but eventually the urge overcame my nerves and I felt myself starting to pee in her."
            m "Warm liquid gushing forth from my tip and spraying Kalinth inside as she gasped with pleasure."
            m "As I kept gently thrusting, some urine mixed with her copious juices squirted out around my penis, soaking my crotch and dribbling down my balls."
            m "Eventually my bladder was empty, but my desire was not at all diminished. I thrust a little harder as the scent of sex and urine filled my nostrils from our dirty coupling."


        c "Is that good?"
        m "I enjoyed the sight of her tensing and untensing her muscles under me, becoming more worked up with each thrust."
        c "Do you like feeling a human take you like this?"
        Kl bangok smile eyeslidded blush flip "I knew it would feel good..."
        show kalinth:
            ease 0.5 ypos 1.2
            block:
                ease 0.8 ypos 1.15
                ease 0.8 ypos 1.2
                repeat
        with None
        m "I hugged her tail, hiking it up a little further so that, on my next thrust, I was able to push a little deeper inside, bringing us slightly closer together and eliciting another gasp from both me and the dragoness beneath me."
        if bangok_four_kalinth.protection:
            m "The feelings of her insides clenching around my condom-wrapped length were exquisite. I couldn't help but thrust a little harder and faster, eager to feel more of her."
        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            m "The feelings of her piss-soaked insides clenching around my length were exquisite. I couldn't help but thrust a little harder and faster, eager to feel more of her."
        else:
            m "The feelings of her insides clenching around me were exquisite, and I couldn't help but thrust a little harder and faster, eager to feel more of her."
        c "You have no idea how good."
        m "Her expression was one of pure pleasure as she continued to pant, nuzzling the couch cushions while her tail writhed in my grasp with each of my thrusts."
        m "The dragoness' passage was so very warm, flushing my body with heat and arousal as I slid myself in and out of her eager depths with increasingly wet slaps."

        Kl bangok eyesclosed blush flip "Don't stop..."
        m "She clung to the couch cushions as she arched her back, pushing her rear up against me as I continued to thrust into her."
        Kl "Please don't stop. Ohhhh..."
        m "I wasn't about to stop now. I looked down, admiring the ripples each of my hard and fast thrusts made over her rear."
        m "Her cloaca tightened around me, her inner muscles clenching, and I closed my eyes as I lost myself in our lovemaking."
        show black
        with dissolvemed
        $ renpy.pause (0.5)
        if bangok_four_kalinth.protection:
            m "In moments, the sensation of her climaxing passage was too much for me to bear and with a final grunt, I came into the condom's tip, spurting white ropes of human seed into the thin barrier protecting the dragoness' eager depths."
        else:
            m "In moments, the sensation of her climaxing passage was too much for me to bear and with a final grunt, I came inside her, spurting white ropes of human seed into the dragoness' eager depths."

        m "I struggled to keep thrusting, per her request, my strength flagging as I carried us through our shared climaxes until finally I just lay on her tail, catching my breath."

        show kalinth at Position(ypos=1.2)
        hide black
        with dissolveslow

        m "Eventually, as my body began to recover its strength and the aftershocks in Kalinth's nethers subsided, I pulled out."
        if not bangok_four_kalinth.protection:
            if persistent.bangok_cloacas:
                m "It wasn't long before I could see my seed oozing from her cloaca in small droplets."
            else:
                m "It wasn't long before I could see my seed oozing from her lower lips in small droplets."
            if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
                m "I couldn't tell which of the other splaters of fluids on our crotches was my urine and which were her juices as they dribbled down our thighs."
        
        m "Like an overgrown cat, she stretched out on the couch, then rolled over with first her front half, then her lower body."
        show kalinth bangok smile eyeslidded blush:
            zoom 1.3
            ease 0.8 ypos 1.1 zoom 1.2
            ease 0.8 ypos 1.0 zoom 1.0
            ypos 1.0 zoom 1.0
        with None
        m "She wriggled her hips, sliding her way a little further to get her rear off the armrest so she could lie down normally."
        m "Then she sighed happily."
        Kl "That was... even better than I'd imagined."
        m "I smiled at her, still catching my breath."
        jump bangok_four_kalinth_c3arc_male_post_intimacy


label bangok_four_kalinth_c3arc_male_post_intimacy:
    c "Well, I aim to please."
    m "She dipped a dulled claw into her folds, teasing herself, before bringing it up to her scaly lips for a taste of our union."
    show kalinth bangok smile eyesclosed blush with dissolve
    m "She licked it clean, closing her eyes again."
    if bangok_four_kalinth.protection:
        Kl "Mmm... give me the condom? I'd like to taste you."
        menu:
            "Give her the condom.":
                $ renpy.pause (0.5)
                play sound "fx/chug.wav"
                m "As soon as I handed her the condom, she popped it into her mouth and lifted the reservoir over her head, driving her tongue up the condom's shaft to lick out my cum from its reservoir."
                m "I blushed as I watched her sinuous tongue work its magic."
                m "She swallowed, then licked her lips."
            "Throw it away.":
                $ renpy.pause (0.5)
                play sound "fx/clink3.ogg"
                m "I pulled the condom off, then tossed it into the trash can."
                c "Sorry, I'm not comfortable with that."
                m "Kalinth gave a small pout, but didn't seem too upset."
                Kl "Suit yourself."
    Kl "I don't think I'll be able to focus on any of my work for the rest of the night..."
    menu:
        "Help clean her up with your tongue.":
            pass
        "Part ways.":
            c "I'm sorry I was such a distraction."
            Kl bangok surprise "Don't be. I certainly enjoyed it."
            c "As did I."
            Kl bangok smile "I suppose I'd better get you my number, then. If you'd like to do this again sometime."
            c "Sure."
            jump bangok_four_kalinth_c3arc_part_ways

    show kalinth bangok surprise blush:
        zoom 1.0
        ease 0.5 zoom 1.7 ypos 1.0
        zoom 1.7 ypos 1.0
    with None
    m "With an impish grin, I knelt next to where she lay on the couch."
    Kl bangok surprise blush "Oh? Willing to help me more at no benefit to yourself? No wonder Bryce keeps asking you for help with the investigations."
    c "There's some benefit there. But in both cases, let's just say the work is its own reward."
    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "Leaning over her soaked cloaca, my tongue flicked out to lick up a first teasing droplet to sample her well-churned juices and to guage her reaction."
        else:
            m "Leaning over her soaked pussy, my tongue flicked out to lick up a first teasing droplet to sample her well-churned juices and to guage her reaction."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        if persistent.bangok_cloacas:
            m "Leaning over her piss-soaked and cum-filled cloaca, my tongue flicked out to lick up a first teasing droplet to sample our well-churned fluids and to guage her reaction."
        else:
            m "Leaning over her piss-soaked and cum-filled pussy, my tongue flicked out to lick up a first teasing droplet to sample our well-churned fluids and to guage her reaction."
    else:
        if persistent.bangok_cloacas:
            m "Leaning over her cum-filled cloaca, my tongue flicked out to lick up a first teasing droplet to sample our combined taste and to guage her reaction."
        else:
            m "Leaning over her cum-filled pussy, my tongue flicked out to lick up a first teasing droplet to sample our combined taste and to guage her reaction."
    Kl bangok smile eyeslidded blush "Mmm... yes."
    m "She sighed contentedly, then spread her legs a little wider with lustful eyes."
    Kl "I can't say no to help like this."
    if bangok_four_kalinth.protection:
        m "Eager to provide said help, I dove my tongue back into the dragoness' folds, tasting more of her slick arousal as she gasped and moaned beneath me."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "Eager to provide said help, I dove my tongue back into the dragoness' folds, soiling my face and tongue with our lustful waste and fluids as she gasped and moaned beneath me."
    else:
        m "Eager to provide said help, I dove my tongue back into the dragoness' folds, tasting our mix of juices and semen as she gasped and moaned beneath me."
    m "My hands were eager too, parting her labia for easier access to those extra teasing deeper folds that caused her muscles to clench and push out more of our mixed passions."
    Kl bangok smile eyeslidded blush "Oh, yes..."
    show kalinth:
        zoom 1.7
        ease 0.5 zoom 1.8
        zoom 1.8
    with None
    m "She crossed her hindlegs behind my head."
    Kl bangok smile eyesclosed blush "You're going to make me cum again..."
    m "I continued my ministrations, eager to see if I could bring the dragoness off for a second time so soon."
    m "Her breathing was growing louder and faster as my tongue explored her insides and outside, lapping up every drop of our combined fluids and teasing all those sensitive areas that made her moan and whimper."
    Kl bangok eyesclosed blush "I think... I think I'm..."
    m "Kalinth panted heavily beneath me."
    show black with dissolve
    m "Then, abruptly, her legs clamped down, pinning my face in place as she arched her back."
    m "She wrapped her forepaws around her own muzzle, muffling her moans of passion and pleasure with a strangled cry, bucking against the couch as another climax washed over her body."

    m "Juices from her passage flooded my tongue, soaking my face, but I continued to lap them up eagerly, drinking in every last drop while she clutched me to her entrance."

    show kalinth smile eyeslidded blush
    with dissolve
    hide black
    with dissolve

    m "The dragoness eventually, seemingly reluctantly, relaxed her legs to let me breath again, though she still draped her legs over my shoulders, rubbing my back gently."

    show kalinth:
        zoom 1.8
        ease 0.5 zoom 1.7
        zoom 1.7
    m "As I finally sat back on my haunches, panting and sweaty from the hotbox held to my face, Kalinth grinned down at me."

    Kl "I have got to get you my number."

    c "I guess you do."
    m "I tried to wipe off my face with an arm, but just wound up getting that wet and sticky too."
    c "And a towel, if you know where one is?"

    scene office at Pan ((128, 250), (0, 250), 3.0) with fade
    $ bangok_four_kalinth.have_number = True

    m "After Kalinth found some towels that she could wash later, she gave me her number and left me to my work."
    jump bangok_four_kalinth_c3arc_finish_timing


label bangok_four_kalinth_c3arc_part_ways:
    show kalinth normal at center with ease 
    m "Kalinth rose from the couch, then got her claws on a scrap of paper."
    play sound "fx/scribblex.ogg"
    $ renpy.pause (0.5)
    m "She wrote down her number, then handed it to me."
    $ bangok_four_kalinth.have_number = True
    Kl bangok smile blush "I'll leave you to your review of the files, then."
    hide kalinth with easeoutleft
    $ renpy.pause (0.3)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (0.5)
    jump bangok_four_kalinth_c3arc_finish_timing


label bangok_four_kalinth_c3arc_finish_timing:
    m "As I got dressed again, I took a look at the clock and realized how late it was getting."
    c "(Man, that took a lot of time. I don't think I can do too much here.)"
    $ c3arcquesx = 1
    jump c3arcques

label todo_out_of_content_bangok_four_kalinth:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")

# The below is the original novelization of the scene as co-authored by 4onenm
# and openhermes-2.5-mistral-7b.Q4_K_M.gguf
# python:
#     """
#     <|im_start|>user
#     Recite the Kalinth sex scene from the sex lewd NSFW mod for AwSW, the dragon dating simulator. Remember, you've just met this police archivist a few minutes ago, and the dragoness' primary interest in you is that you're a human.<|im_end|>
#     <|im_start|>assistant
#     "Anyway, you can find all the files here. I'll leave the rest to you." Kalinth said, before moving back toward the office door, tail swishing as she hurried a little.

#     I notice, though, she lingered in the doorway instead of leaving. After a few hesitant steps toward the collected files, I found myself looking back.

#     Noticing my attention, she closed the door, then cleared her throat. "There... is something else."

#     "Oh? What's that?" I asked, still unsure what to expect from this dragoness.

#     "Well," she said, shifting nervously on her feet and casting a furtive glance around her boss' office, despite him being out for the next several hours. "I've been reading all the reports on your kind thus far, and... there's something I'm interested in trying. Only if you are interested, of course."

#     "I think I'd have to know what it is first," I replied, wanting to be absolutely sure she was taking this where I suspected. "What do you want to try?"

#     Kalinth trod closer. "Absolutely feel free to say no if it's too far, but I thought... perhaps you and I could share a bit of casual intimacy." She glanced down at my crotch, making her intentions clear. Her tail twitched as she waited for my answer, the end swishing back and forth across the floor.

#     I gave her a smile. "That sounds like fun," I agreed. "Right here in Bryce's office, though?"

#     "I don't think we'll be disturbed here for a while," she said with a wink. "This office has also seen plenty of use by various members of the department, so it's not like this is anything new. But I can also give you my number for another day, if you prefer."

#     I shook my head, more than ready to accept her offer right now. "Let's go for it."

#     "I assume you'll have to remove your..." She gestured to my clothes. I hurriedly began undressing, not wanting to keep the dragoness waiting. Once I was nude, my erect member exposed to the air of the room, she backed me up toward the armrest of the nearer of the two couches, smirking.

#     ### Watersports variant

#     Standing erect and nude next to her, I suddenly realized my bladder was rather full. "Er... I should probably use the restroom first."

#     Kalinth blushed. "Oh, wow. Your timing is worse than... well, never mind." She pouted. "I suppose I can wait a little longer... unless you want to use me as a urinal?"

#     "I didn't think you'd be into something like that," I admitted. Then I came to a decision. "Sure, why not? I could really use the relief."

#     Smirking, Kalinth trod a little closer. "Mm. Well, we don't want to make a mess on Bryce's floor. I could drink it down right now, or if you're into it you could piss it into me while you're inside, leave me even more dripping wet between the legs..."

#     My eyes widened at the prospect of doing something so taboo with this dragoness' body... but she was offering herself up for it.

#     #### Piss in her mouth

#     I rested my hand on one side of her snout, then guided it down to my erection. She eagerly wrapped her scaly lips around me, but didn't slurp or suck as she waited for me to urinate into her mouth. It was a strange and exciting sensation... I could feel the heat from her breath against my body while warm, moist air filled my urethra.

#     I let my bladder go and felt the familiar rush of relief as my member began to disgorge a steady stream of piss against the back of Kalinth's throat. She swallowed it down eagerly, not once pulling away from me until I had finished urinating into her mouth. The sight of her swallowing every last drop left me with an erection that could have shattered diamonds, and she seemed to be enjoying the fun as well from the look on her face.

#     "Mmm... you taste interesting," Kalinth said once my member stopped twitching. She gave my member a slow lick, from balls to tip, then stepped back with an amused smirk. "I've never tasted a human's piss before."

#     "Well, that's certainly different," I said. "You don't mind?"

#     Kalinth shook her head. "Not at all. No problem." She smirked. "Now are we going to fuck?"

#     #### Piss into her pussy

#     "Inside," I agreed, feeling my erection twitch with anticipation.

#     She moved a little closer. "Then let's get started."

#     ### Kalinth on top

#     I sat back on the couch armrest, letting the assertive dragon archivist take charge. She reared up, resting her forelegs over my shoulders as her spread rear legs revealed her glistening cloaca, searching with her hips for my shaft. Then, pressing my back against the couch's back, she began to tease her cloaca open with my tip, grinding against my erection without letting it in.

#     "Ohhhh," I groaned as the dragoness rubbed herself against me. Her tail swished behind her, making a faint rustling sound with each movement. "Are you going to make me wait like this? I don't know how long I can take it."

#     Kalinth chuckled at that, my face against her fine underbelly scales before she pushed off a little to look me in the eye. "I'll let you inside eventually," she promised with a wink. "But first I just want to feel you all over me down there before..." Her breathing caught and she closed her eyes as her cloaca slid up to my tip again, then she began to lower herself down, enveloping my erection with the warmth of her draconic anatomy.

#     "Oh fuck," I moaned as she took every inch, her tail twitching with excitement. The dragoness paused for a moment, seemingly struggling to take things slow, before she began to gently thrust herself against me, her scaly lower lips rubbing over my member in the most delightful way imaginable.

#     I grabbed onto the couch back tight as I felt Kalinth's cloaca enveloping me, gripping me tighter with every stroke. The heat radiating from her smooth scales was intoxicating. My hips twitched, desperate for more, but she seemed to enjoy this weighty but gentle slow thrusting so much that it was hard to bring myself to complain about it. It wasn't until she moaned loudly and began thrusting even faster that I finally knew the moment had come when she was ready for something more forceful.

#     I groaned as Kalinth finally started fucking me in earnest, her tail whipping back and forth like a flag in the wind of our passion. Her cloaca leaked copious lubrication around my shaft, making it slide in and out with ease as our mating point gave wetter and louder slaps against my groin. I tried to lift my hips a little, thrusting deeper into her, but I could do no better than her weight already pressing down on me. Still, the motion caused her to hug me to her chest again, bringing us closer together in the throes of our passion.

#     "Don't cum just yet," Kalinth whispered hoarsely as she rode me harder and faster, each stroke seeming more desperate than before. "I want... I need..." She moaned, then buried herself on my erection to the hilt, her tail swishing wildly behind her as her passage spasmed and clenched around my shaft. "Now!"

#     I complied with a moan of my own, feeling my orgasm surge forth into her kneading nethers. My member throbbed within her heat and wetness as she lay her body atop mine, resting her weight on my hips to force me as deep within her as I could be. Then the dragoness began grinding herself against me in slow circles, savoring the feeling of the tail-end of my release still spurting slowly into her. My cum and her juices dribbled down between my thighs as my erection faded, leaving us just merely lying together with soiled groins.

#     "Oh... wow," she panted after a few minutes had passed, finally rolling off of me to lie down on the couch properly, while I continued to splay across the armrest and seat back. "That was... even better than I'd imagined."

#     I nodded, panting hard myself as I sat up.

#     ### Player on top

#     "Actually, could you lie down?" I suggested, pointing at the couch. "I'd like to be in control for this."

#     Kalinth quickly agreed. She lay across the couch, her tail swishing and wings fluttering as she settled into a comfortable position and spread her legs to reveal her glistening draconic cloaca. I couldn't help but stare at that sight. The dragoness watched my every move with anticipation.

#     #### Finger her

#     Wanting to make sure she was ready, I chose to start with my fingers. As I approached her, I could smell the sweet scent of her arousal on the air. Carefully, I parted her labia and found just how wet she was for me already. With some gentle stroking around her entrance, I teased her with what was to come.

#     Kalinth gasped, breath shuddering as I touched her. "Oh, yes," she hissed, "so soft... But please, don't tease for too long. I want you inside me."

#     #### Tongue her

#     I couldn't help but wonder how the juices around that gorgeous hole tasted, so I knelt on the floor next to her groin and parted her labia with my thumbs, inhaling the sweet scent of her arousal. It was intoxicating and only heightened the taste of her entrance when I did begin to lick and suck lightly at the edges, gathering up first what had leaked onto her scales before teasingly working my way inside.

#     Kalinth gasped, breath shuddering as I licked her. "Oh, yes," she hissed, "I almost don't want to make you stop. But we can't spend all night here..."

#     #### Enter her

#     I moved closer, my erection throbbing in response to the sight of the open, wet passage. She was inviting me to enter her like this? My heart pounded as my fingers brushed against the scales of her legs as I straddled her tail, taking my position. I took a deep breath, then slowly lowered myself down into her.

#     Her warm cloaca enveloped my member as I pushed inside. Kalinth moaned softly, her wings fluttering faster with excitement. Once I was fully seated within her, she arched her back, purring loudly.

#     "Is that good?" I asked, enjoying the look on her face as she reacted to my entry. "Do you like feeling a human inside you?"

#     "I knew this would feel good," Kalinth replied, still panting from just my slide into her body.

#     As I began to thrust, I closed my eyes, gasping myself from the warmth of the dragoness' cloaca around me. "You have no idea how good," I replied between breaths, thrusting into the dragoness.

#     Her expression was one of pure pleasure. "Mmm... yes," she managed around a gasp, claws digging into the couch fabric as I brought our hips together with increasingly wet slaps.

#     I could feel the dampness growing from her entrance as we continued to couple, and it only fueled my desire for more. I began thrusting faster, harder, driving myself deeper into the dragoness' willing body. Her tail lashed in time with each of my thrusts, keeping rhythm with our lovemaking as she breathed louder and louder.

#     "Don't stop," Kalinth begged, her voice breathy but insistent. "Please don't stop. Ohhhh..."

#     I wasn't about to stop now. She clutched at me tightly, pulling me closer even as her cloaca tightened around my member, her inner muscles clenching. The sensation was too much for me to bear and with a final grunt, I came inside her, spurting white ropes of human seed into the dragoness' waiting passage. Her muscles milked every drop from me but, per her request, I continued thrusting through our shared climaxes.

#     Eventually, as my body began to calm down and the aftershocks subsided, I pulled out of Kalinth, leaving a trail of semen in her now dripping cloaca. She gasped, panting heavily from our shared exertions as she opened her eyes again. "That was... even better than I'd imagined."

#     I smiled at her, still catching my breath. 

#     ### Kalinth doggystyle

#     I patted the armrest of the couch. "Do you want me to bend you over this...?" I trailed off, realizing that, as she was already approaching me on all fours, there wasn't much bending over to be done.

#     She seemed to understand what I meant, though. "That works," Kalinth replied with a grin before lying down over the end of the couch, with her hindlegs hanging over the armrest. She lifted her tail, exposing between her spread legs her glistening cloaca already soaked and waiting for me. "I'm ready whenever you are."

#     #### Finger her from behind

#     As I approached her from behind, I couldn't help but look at her open, wet entrance. My cock twitched in response. Wanting to make sure she was good and ready, I chose to start with my fingers. Sliding them inside her, I felt the heat of her insides, the slickness of her arousal coating my digits as they parted her labia.

#     Kalinth gasped, breath shuddering as I touched her. "Oh, yes," she hissed, "so soft... But please, don't tease for too long. I want you inside me."

#     #### Tongue her from behind

#     I couldn't help but wonder how the juices around that gorgeous hole tasted, so I knelt on the floor between her hindlegs, spreading her thighs with my hands for easier access. Parting her labia with the index finger of one hand, I found just how wet she was for me already. I inhaled the sweet scent of her arousal. It was intoxicating and only heightened the taste of her as I began to tease her entrance lightly with the tip of my tongue, lapping up her juices liberally as she shuddered beneath my hands and mouth.

#     Kalinth gasped, breath shuddering as I licked her. "Oh, yes," she hissed, "I almost don't want to make you stop. But we can't spend all night here..."

#     Reluctantly I got back to my feet.

#     #### Enter her from behind

#     My erection throbbed in response to the sight of the eager dragoness before me and her beautiful rear framing her wet, open passage. I ran my hands over her scaly flanks, feeling the muscle beneath as she arched her back in anticipation. My heart pounded with lust as I lined up our bodies, then slid myself into her from behind, entering her eager cloaca.

#     She moaned loudly, claws digging into the couch fabric and wings rustling softly under me as I began to thrust inside of her. Kalinth was panting hard even before we really got started.

#     "Is that good?" I asked, enjoying the sight of her tensing and untensing her muscles, becoming more worked up with each thrust. "Do you like feeling a human take you like this?"

#     "I knew it would feel good," Kalinth replied, twisting her neck to give me a happy look with lidded eyes.

#     I hugged her tail, hiking it up a little further so that, on my next thrust, I was able to push a little deeper inside, bringing us slightly closer together and eliciting another gasp from both me and the dragoness beneath me. "You have no idea how good," I replied between breaths, thrusting into the dragoness.

#     Her expression was one of pure pleasure as she continued to pant, nuzzling the couch cushions while her tail writhed in my grasp with each of my thrusts. The dragoness' passage was so very warm, flushing my body with heat and arousal as I slid myself in and out of her eager depths with increasingly wet slaps.

#     "Don't stop," Kalinth begged, clinging to the couch cushions as she arched her back under me. "Please don't stop. Ohhhh..."

#     I wasn't about to stop now. I looked down, admiring the ripples each of my hard and fast thrusts made over her rear. Her cloaca tightened around me, her inner muscles clenching, and I closed my eyes as I lost myself in our lovemaking. In moments, the sensation of her climaxing passage was too much for me to bear and with a final grunt, I came inside her, spurting white ropes of human seed into the dragoness' eager depths. I struggled to keep thrusting, per her request, my strength flagging as I carried us through our shared climaxes until finally I just lay on her tail, catching my breath.

#     Eventually, as my body began to recover its strength and the aftershocks in Kalinth's nethers subsided, I pulled out. It wasn't long before I could see my seed oozing from her cloaca in small droplets.

#     Like an overgrown cat, she rolled over on the couch with first her front half, then her lower body, then wriggled her way a little further to get her rear off the armrest so she could lie down normally. Then she sighed happily. "That was... even better than I'd imagined."

#     I smiled at her, still catching my breath.

#     ### Post-intimacy

#     "Well, I aim to please," I said with a wink.

#     She dipped a dulled claw into her folds, teasing herself, before bringing it up to her scaly lips for a taste of our union. She licked it clean, closing her eyes again. "I don't think I'll be able to focus on any of my work for the rest of the night..."

#     With an impish grin, I knelt next to where she lay on the couch.

#     "Oh, willing to help me more at no benefit to yourself?" she asked. "No wonder Bryce keeps asking you for help with investigations."

#     "There's some benefit there," I admitted. "But in both cases, let's just say the work is its own reward." Leaning over her cum-filled cloaca, my tongue flicked out to lick up a first teasing droplet to sample our combined taste and to guage her reaction.

#     Kalinth sighed contentedly at that, then looked back at me with lustful eyes. "I can't say no to free help like this."

#     Eager to provide said help, I dove my tongue back into the dragoness' folds, tasting our mix of juices and semen as she gasped and moaned beneath me. My hands were eager too, parting her labia for easier access to those extra teasing deeper folds that caused her muscles to clench and push out more of our mixed passions.

#     "Oh yes," Kalinth hissed again, crossing her hindlegs over my head. "You're going to make me cum again..."

#     I continued my ministrations, eager to see if I could bring the dragoness off a second time so soon after she'd already climaxed with me. Her breathing was growing louder and faster as my tongue explored her insides and outside, lapping up every drop of our combined fluids and teasing all those sensitive areas that made her moan and whimper.

#     "I think... I think I'm..." Kalinth whispered hoarsely, panting heavily beneath me. Then, abruptly, her legs clamped down, pinning my face in place as she arched her back again. She wrapped her forepaws around her own muzzle, muffling her moans of passion and pleasure with a strangled cry, bucking against the couch as another climax washed over her body.

#     Juices from her passage flooded my tongue, soaking my face, but I continued to lap them up eagerly, drinking in every last drop while she clutched me to her entrance. The dragoness eventually, seemingly reluctantly, relaxed her legs to let me breathe again, though she still draped her legs over my shoulders, rubbing my back gently.

#     As I finally sat back on my haunches, panting and sweaty from the hotbox held to my face, Kalinth grinned down at me. "I've got to get you my number."

#     "I guess you do," I agreed, wiping off my face with an arm. "And a towel, if you know where one is?"
#     """
