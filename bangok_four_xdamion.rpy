label bangok_four_xdamion_replay_start:
    scene black with dissolve
    $ renpy.pause (0.5)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.0)
    scene facin2 at Pan ((128, 250), (128, 250), 0.0)
    show damion face
    with fade
    jump bangok_four_xdamion_replay_merge

label bangok_four_xdamion:
    c "[player_name], ambassador from humanity to dragonkind."
    Dm arrogant "Tchk, of course. Immediately with a big fancy title. This whole thing is so blown out of proportion, it makes me wonder how many dicks you had to suck to be the one coming here."
    menu:
        "Uh...":
            Dm "Everyone's acting like it's some huge event that everyone should be celebrating.{w} Newsflash: Not everyone cares."
            Dm "Once both of you are gone, life will return to normal and we can all go back to what we actually should be doing."
            jump bangok_four_xdamion_canon_whatdidyouwant
        "I could suck yours if it'd help your mood.":
            $ renpy.pause (0.5)
            Dm "I..."
            $ renpy.pause (0.5)
            show damion face with dissolve
            $ renpy.pause (0.4)
            Dm face "Ha{w=0.4} ha.{w=0.4} Very funny."
            Dm normal "If you're a prime example of your species and still making jokes like that, I sincerely doubt things are going to go well between our species."
            menu:
                "You're not exactly a pinnacle of cooperation.":
                    $ evilpoints += 3
                    Dm arrogant "Oh? Let me spell it out simply enough for you to understand:{w} Not everyone cares."
                    Dm "Once both of you are gone, life will return to normal and we can all go back to what we actually should be doing."
                    show damion face with dissolve
                    jump bangok_four_xdamion_canon_whatdidyouwant
                "I'm serious.":
                    show damion face with dissolve
                    $ renpy.pause (0.3)
                    Dm face "..."
                    label bangok_four_xdamion_replay_merge:
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

                    if persistent.bangok_watersports == True:
                        jump bangok_four_xdamion_ws_fuck
                    else:
                        jump bangok_four_xdamion_fuck

label bangok_four_xdamion_fuck:
    show damion normal bangok:
        zoom 1.3
        anchor (0.5,1.0)
        pos (0.6,1.0)
    with dissolve
    $ renpy.pause(0.5)
    Dm arrogant bangok "Well?"

    menu:
        "Drop to your knees.":
            jump todo_out_of_content_bangok_four_xdamion
        "Offer your ass.":
            jump todo_out_of_content_bangok_four_xdamion
        "Offer your slick, needy hole.":
            jump todo_out_of_content_bangok_four_xdamion
        "Back out.":
            c "I... I'm not so sure--"
            Dm face bangok "Then I don't have time for this."
            hide damion with dissolve
            play sound ["fx/door/lock.ogg","fx/door/hallwaydoor.ogg"]
            $ renpy.pause(0.5)
            scene facin2 at Pan ((128, 250), (128, 250), 0.0) with wiperight
            play sound "fx/door/lock.ogg"
            m "Grabbing my arm, Damion dragged me back out of the lab and locked me outside."
            $ renpy.pause(0.5)
            c "(Damn it, I didn't ask him any questions!)"
            $ renpy.pause(0.5)
            m "Trying to put the weirdo from my mind, I walked off to find a more amenable line of investigation."
            play sound "fx/steps/clean2.wav"
            show black with dissolvemed
            $ renpy.pause (0.5)
            show town1 with dissolvemed
            jump chapter2sections

    jump todo_out_of_content_bangok_four_xdamion

label bangok_four_xdamion_ws_fuck:
    show damion normal bangok ws:
        zoom 1.3
        anchor (0.5,1.0)
        pos (0.6,1.0)
    with dissolve
    m "The smell of urine hit me immediately, wafting from his groin."
    c "Wh-- Are you dribbling piss on yourself?"
    Dm face bangok ws "Before you arrived, I was trying to stave off having to go to the bathroom, to complete what I was working on."
    Dm "Had I not needed to go, I probably wouldn't have answered your incessant knocking at all."
    Dm arrogant bangok ws "But since you're so eager to taste dragon cock, you might as well clean it up while you're down there."
    menu:
        "Drop to your knees.":
            show damion arrogant bangok ws:
                transform_anchor True
                ease 0.5 zoom 2.4
            show crapannalab:
                transform_anchor True
                ease 0.5 zoom 2.2
            with None
            $ renpy.pause (0.8)
            Dm "There's a good cocksucker."
            $ renpy.pause (0.5)
            Dm normal bangok ws "Well? Get started."
            $ renpy.pause (0.3)
            show black with dissolve
            $ renpy.pause (0.5)

            m "I took Damion's tangy, leaking cockhead into my mouth."
            m "No sooner had I taken him in than I felt his hands on the back of my head, abruptly pulling me as deep as my mouth could take him, forcing me to swallow a dribble of piss as I gagged."
            Dm face "Not so fleshy and malleable inside, huh?"
            m "Angling my head back, he aimed his cock downward. I only had a moment to suck in air before he sank his piss-stained rod deeper, into my throat, until my nose was pressing into his soggy slit."
            Dm arrogant "There we go."
            play soundloop "fx/faucet1.ogg" fadein 1.0
            queue soundloop "fx/faucet2.ogg" 
            m "Hot liquid jetted into my throat, almost faster than I would have been able to swallow."
            m "My mouth was coated in the dirty tang, his thick cock left coated with golden waste after leaking inside himself."
            m "His slit rubbed piss he'd dribbled into the rest of my face, leaving my nose thick with the unmistakeable scent, while a drop of golden evidence squeezed out to run down my chin."
            Dm face "{i}Fuck{/i} how I wish I could do {i}this{/i} to that bitch."
            if persistent.bangok_inflation == True:
                m "I felt ill, like I had swallowed a pitcher full, filled my stomach nearly to capacity with his waste, but more was still coming."
            play sound "fx/slap2.wav"
            m "Lungs begging for air, I slapped his leg, trying to get him to back off."
            play sound "fx/undress.ogg"
            stop soundloop fadeout 1.5
            m "He pulled my head back while still pissing, choking my throat full before spattering the bitter tang everywhere in my mouth."
            play sound "fx/spray.ogg"
            m "He finally ended with one last splash on my face as I struggled to swallow, spattering my nose, one cheek, and one closed eye with his golden waste."
            $ renpy.pause (0.5)
            m "Wiping my defiled face with a hand, I blinked my eyes open."
            show damion arrogant bangok
            hide black
            with dissolve
            Dm "Well, at least you make a good urinal."
            Dm "Now suck."
            $ renpy.pause (0.5)
            menu:
                "[[Suck.]":
                    pass
                "No. I'm done.":
                    $ renpy.pause (0.5)
                    Dm face "The ambassador gets a little piss in their eye, and that's the end of things?"
                    Dm arrogant "Fuck you too. You're the one who wanted this."
                    Dm normal "But fine. If my piss is all you're good for, then I don't have anything more for you."
                    hide damion with dissolve
                    play sound ["fx/door/lock.ogg","fx/door/hallwaydoor.ogg"]
                    $ renpy.pause(0.5)
                    scene facin2 at Pan ((128, 250), (128, 250), 0.0) with wiperight
                    play sound "fx/door/lock.ogg"
                    m "Grabbing my arm, Damion dragged me back out of the lab, then locked me outside."
                    $ renpy.pause(0.5)
                    c "H-Hey! What about my questions about..."
                    $ renpy.pause(0.5)
                    m "The closed and locked door stared back at me, impassively."
                    $ renpy.pause(0.5)
                    m "I wiped off my soiled face, cursed him under my breath, then walked off to find a more amenable line of investigation."
                    play sound "fx/steps/clean2.wav"
                    show black with dissolvemed
                    $ renpy.pause (0.5)
                    show town1 with dissolvemed
                    jump chapter2sections


            jump todo_out_of_content_bangok_four_xdamion


        "Offer your ass.":
            jump todo_out_of_content_bangok_four_xdamion
        "Offer your slick, needy hole.":
            jump todo_out_of_content_bangok_four_xdamion
        "Refuse.":
            c "I'm not drinking your piss, asshole."
            Dm face bangok ws "Then I don't have time for this."
            hide damion with dissolve
            play sound ["fx/door/lock.ogg","fx/door/hallwaydoor.ogg"]
            $ renpy.pause(0.5)
            scene facin2 at Pan ((128, 250), (128, 250), 0.0) with wiperight
            play sound "fx/door/lock.ogg"
            m "Grabbing my arm, Damion dragged me back out of the lab, locked me outside, then took off down the hallway."
            $ renpy.pause(0.5)
            c "(Should I wait for him? I still have my questions to ask...)"
            menu:
                c "(Should I wait for him?)"
                "Wait.":
                    $ renpy.pause (1.0)
                    c "..."
                    $ renpy.pause (1.0)
                    play sound "fx/steps/clean2.wav"
                    $ renpy.pause (1.0)
                    show damion face at center with dissolve
                    stop sound fadeout 0.5
                    Dm "You're still here."
                    jump bangok_four_xdamion_canon_whatdidyouwant
                "Give up.":
                    $ renpy.pause (0.5)
                    play sound "fx/steps/clean2.wav"
                    show black with dissolvemed
                    $ renpy.pause (0.5)
                    show town1 with dissolvemed
                    jump chapter2sections

label todo_out_of_content_bangok_four_xdamion:
    play sound "fx/system3.wav"
    s "TODO: Out of content. Roll back or prepare to crash."
    $ renpy.error("TODO: Out of content.")