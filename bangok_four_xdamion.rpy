init python in bangok_four_xdamion_store:
    ass_offered = False

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
            Dm normal "If you're a prime example of your species and still making jokes like that, I sincerely doubt things are going to go well between our two kinds."
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
    if bangok_four_playerhasdick is None:
        m "At the sight of his exotic, tapered penis, I felt a welling of heat in my groin..."
        menu:
            m "At the sight of his exotic, tapered penis, I felt a welling of heat in my groin...{fast}"
            "...eliciting a twitch from my manhood.":
                $ bangok_four_playerhasdick = True
            "...causing a shiver in my love canal.":
                $ bangok_four_playerhasdick = False
    elif bangok_four_playerhasdick == True:
        m "At the sight of his exotic, tapered penis, I felt a welling of heat in my groin, eliciting a twitch from my manhood."
    else:
        m "At the sight of his exotic, tapered penis, I felt a welling of heat in my groin, causing a shiver in my love canal."
    $ renpy.pause(0.5)
    Dm arrogant bangok "Well?"

    label bangok_four_xdamion_fuck_positionmenu:
    menu:
        "Drop to your knees.":
            jump todo_out_of_content_bangok_four_xdamion
        "Offer your ass." if bangok_four_xdamion_store.ass_offered == False:
            $ bangok_four_xdamion_store.ass_offered = True
            m "I turned partway around, tugging at my waistband with a thumb."
            c "What if, instead, you filled my ass?"
            Dm face bangok "What the fuck?{w=0.5} Do I look like I want your crap on my penis?"
            Dm arrogant bangok "Suck me or get out."
            jump bangok_four_xdamion_fuck_positionmenu
        "Offer your slick, needy hole." if bangok_four_playerhasdick == False:
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
    
    if bangok_four_playerhasdick is None:
        m "Looking down at his exotic, piss-stained penis, I felt a welling of heat in my groin..."
        menu:
            m "Looking down at his exotic, piss-stained penis, I felt a welling of heat in my groin...{fast}"
            "...eliciting a twitch from my manhood.":
                $ bangok_four_playerhasdick = True
            "...causing a shiver in my love canal.":
                $ bangok_four_playerhasdick = False
    elif bangok_four_playerhasdick == True:
        m "Looking down at his exotic, piss-stained penis, I felt a welling of heat in my groin, eliciting a twitch from my manhood."
    else:
        m "Looking down at his exotic, piss-stained penis, I felt a welling of heat in my groin, causing a shiver in my love canal."
    $ renpy.pause(0.5)

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
            Dm normal "There we go."
            play soundloop "fx/faucet1.ogg" fadein 1.0
            queue soundloop "fx/faucet2.ogg"
            m "Hot liquid jetted into my throat, almost faster than I would have been able to swallow."
            m "My mouth was coated in the dirty tang, his thick cock left coated with golden waste after leaking inside himself."
            m "His slit rubbed piss he'd dribbled into the rest of my face, leaving my nose thick with the unmistakeable scent, while a drop of golden evidence squeezed out to run down my chin."
            Dm face "{i}Fuck{/i} how I wish I could do {i}this{/i} to that bitch."
            if persistent.bangok_inflation == True:
                m "I felt ill, like I had swallowed a pitcher full. He'd filled my stomach nearly to capacity with his waste, but still more was coming."
            play sound "fx/slap2.wav"
            m "Lungs begging for air, I slapped his leg, trying to get him to back off."
            play sound "fx/undress.ogg"
            stop soundloop fadeout 1.5
            m "He pulled my head back while still pissing, choking my throat full before spattering the bitter tang everywhere in my mouth."
            play sound "fx/spray.ogg"
            m "He finally ended with one last splash on my face as I struggled to swallow, spattering my nose, one cheek, and one closed eye with his golden waste."
            $ renpy.pause (0.5)
            m "Wiping my dripping face with a hand, I blinked my eyes open."
            show damion arrogant bangok ws
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
                    Dm face bangok ws "The ambassador gets a little piss in their eye, and that's the end of things?"
                    Dm arrogant bangok ws "Fuck you too. You're the one who wanted this."
                    Dm normal bangok ws "But fine. If my piss is all you're good for, then I don't have anything more for you."
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

            $ renpy.pause (0.5)
            show black with dissolve
            $ renpy.pause (0.5)
            m "After a few moments to catch my breath, I took his slick tip back into my mouth."
            m "As I began to explore with my tongue, I realized with some amount of surprise it almost felt like his tip was exploring back, his cockflesh malleable and motile, not hard like anything I'd experienced before."
            m "I suckled at his waste-coated teat for a few moments, until I felt a different taste on my tongue -- sweet drops of pre."
            $ renpy.pause (0.8)
            m "Impatiently, Damion took a hold on my head, pushing a little more of himself into my mouth."
            Dm normal bangok ws "Come on. Can't you do more than that?"
            $ renpy.pause (1.0)
            menu:
                "Try to take him deeper.":
                    m "I leaned forward a little into his pulling, accepting just a tiny bit more until his tip was at the back of my throat."
                    m "Having given him an inch, Damion took a mile."
                    Dm normal bangok ws "You want me in your throat again? Hold your breath, cocksucker."
                    m "Getting a better grip on my head, he lined himself up again, before thrusting into my vulnerable windpipe."
                    play sound "fx/bangok_poundofsalt.ogg"
                    if persistent.bangok_inflation == True:
                        m "I gagged, stomach full of his piss roiling as he took the pleasure he wanted from my throat."
                    else:
                        m "I gagged, airways blocked as he took the pleasure he wanted from my throat."
                    m "I could barely see him throwing his head back in ecstacy, as he pulled my face into his slit."
                    Dm face bangok ws "Fuuuck, human. It's like you were built to take my cock."
                    Dm arrogant bangok ws "Wouldn't it just be perfect if all this hubub, it was dragons who built humans to be their fucktoys?"
                    Dm "You sure are a prime example."
                    m "Finally letting me back off a bit, he waited, almost impatiently, as I caught my breath."
                    m "Then he pulled me back up his length, into his piss-stained groin."
                    Dm normal bangok ws "Fucking perfect."
                    Dm face bangok ws "Almost might--"
                    play sound "fx/snarl.ogg"
                    jump todo_out_of_content_bangok_four_xdamion

                "Use hands.":
                    jump todo_out_of_content_bangok_four_xdamion


            jump todo_out_of_content_bangok_four_xdamion


        "Offer your ass." if bangok_four_xdamion_store.ass_offered == False:
            $ bangok_four_xdamion_store.ass_offered = True
            m "I turned partway around, tugging at my waistband with a thumb."
            c "What if, instead, you filled my ass?"
            Dm face bangok "What the fuck?{w=0.5} Do I look like I want your crap on my penis?"
            Dm arrogant bangok "Suck me or get out."
            jump bangok_four_xdamion_fuck_positionmenu
        "Offer your slick, needy hole." if bangok_four_playerhasdick == False:
            m "I hopped up on the lab bench, sliding a hand under my waistband."
            c "Okay, how about you put that where it's supposed to go?"
            Dm face bangok ws "What are you...?"
            Dm normal bangok ws "Oh."
            Dm arrogant bangok ws "Oh you slutty bitch."
            Dm "Pants off. Strip."
            play sound "fx/undress.ogg"
            $ renpy.pause (0.5)
            m "I worked my waistband around my rear, wiggling on the lab bench until the cloth dropped over my knees, down around my ankles."
            show damion arrogant bangok ws:
                ypos 1.7
                transform_anchor True
                ease 0.5 zoom 2.4
            with ease
            m "Damion stepped over my pants, then kicked backward to yank my legs tighter around him, pulling me closer so that his soiled length rubbed my slick outer folds."
            m "His tip prodded the hem of my shirt, staining it with a drop of yellow."
            Dm "There's a good fucking urinal."
            Dm normal bangok ws "Hold tight and take it all. I don't want a spill down my legs."
            show damion normal bangok ws:
                ease 0.5 ypos 1.75
                ease 0.15 ypos 1.7
            m "Without waiting for confirmation he pulled back, then shoved his stinking length inside me."
            m "I yelped, my hole wholly unprepared for the smooth, sinuous transition from small tip to thick, stretching base."
            if persistent.bangok_cervpen == True:
                m "In no small part, the sensation that elicited the sound was the moment he ran out of depth within me, before he'd fully inserted."
                m "My breathing was hot and heavy, groin on fire as I felt his tip twitching around against my innermost gate, even as he stood still holding my hips."
                m "Then he found the center of my gate and pushed, and my breath was taken by a much louder exclamation."
            show damion face bangok ws with dissolve
            show black with dissolve
            m "Grabbing my head, he silenced me by shoving his lips against mine, tongue slipping into my open mouth to tangle with the one in my mouth."
            if persistent.bangok_cervpen == True:
                m "He pushed harder, ignoring my cervix's attempts to bar him entry to my most sacred temple."
                m "My legs twitched against his thighs as he forced his way into my womb, bottoming out with his wet slit against my stretched outer lips."
            else:
                m "Still sliding in, he bottomed out, wet slit against my stretched outer lips."

            play soundloop "fx/faucet1.ogg" fadein 1.0
            queue soundloop "fx/faucet2.ogg"

            if persistent.bangok_cervpen == True:
                m "Then, his lips still to mine, I felt a hot jet spray into my sacred temple, defiling the walls with his liquid waste."
                m "I melted into his grasp, the warmth in my deepest center spreading and suffusing my body with the knowledge I was his to use as he pleased, to piss in how he wanted."
                if persistent.bangok_inflation == True:
                    m "My womb wasn't even enough to contain his pissload. His urine saturated my tubes and pressed back against my dilated cervix, seeping into my passage and bloating my sacred temple with sacrelidge as he used me as his toilet."
            else:
                m "Then, his lips still to mine, I felt a hot jet against my inner walls, defiling my passage with his liquid waste."
                m "I melted into his grasp, the warmth in my love canal spreading and suffusing my body with the knowledge I was his to use as he pleased, to piss in how he wanted."
                if persistent.bangok_inflation == True:
                    m "There wasn't even room enough in my canal to contain his pissload. His urine saturated my tubes and pressed against my cervix, seeping into my deepest center as he used my sacred temple as a toilet."

            show damion normal bangok ws
            hide black
            with dissolve
            stop soundloop fadeout 0.5

            m "He broke the deep kiss, pulling back from me as I shivered in ecstacy. Then his stream of urine finally came to an end."
            if persistent.bangok_inflation == True:
                Dm arrogant bangok ws "Looking a little heavier there, urinal."
                Dm "You'd better still have room for my cum."
            else:
                Dm arrogant bangok ws "Squeeze tighter, urinal. Take my cum and keep it all inside."

            show damion normal bangok ws:
                zoom 2.4 ypos 1.7
                ease 0.5 zoom 2.3 ypos 1.75
                ease 0.15 zoom 2.4 ypos 1.7
                repeat
            with None
            play sound "fx/bangok_poundofsalt.ogg"

            m "He barely gave me a few moments before beginning to thrust, stretching my outer folds again and again around his thick base, before sliding out to leave me feeling almost empty and thrusting in again."
            if persistent.bangok_inflation == True and persistent.bangok_cervpen == True:
                m "There was nothing I could do to contain my wombful of his piss as, every time he pulled back, he left my innermost gate breached, allowing a small torrent of his golden gift to pour out into my quickly-soaked passage."
            elif persistent.bangok_inflation == True:
                m "There was nothing I could do to contain my wombful of his piss as, every time he pulled back, a small stream of his golden gift to leaked out of my bloated deepest center into my quickly-soaked passage."
            elif persistent.bangok_cervpen == True:
                m "There was nothing I could do to contain the pool of piss in my womb as, every time he pulled back, he left my innermost gate breached, allowing a small torrent of his golden gift to leak out into my quickly-soaked passage."
            else:
                m "No matter how I tried to squeeze, the steep taper of his member left me grasping at nothing, unable to hold back the warm pool of piss in my canal he thrust into over and over again."
            m "His deep thrusts spattered the dirty fluid over our thighs, eliciting a grunt of disapproval from him."
            Dm face bangok ws "I told you to fucking keep this in. Leak it all over my lab and you are going to have a problem."
            show damion normal bangok ws with dissolve
            show damion normal bangok ws:
                ease 0.5 zoom 2.35 ypos 1.72
                ease 0.15 zoom 2.4 ypos 1.7
                repeat
            with None
            m "I squeezed tighter with my weak legs, pulling him closer to try to reduce the pitch of his thrusts, to keep my outer folds stretched and sealed to him, as well as to pull myself closer to my own peak."
            Dm "Not long, slut. I'll... give you what you want."


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