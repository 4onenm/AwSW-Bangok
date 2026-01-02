init python in bangok_four_xdamion_store:
    ass_offered = False

    position = None

    standing_unattempted = True


label bangok_four_xdamion_replay_start:
    scene black with dissolve
    $ renpy.pause (0.5)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.0)
    scene facin2 at Pan ((128, 250), (128, 250), 0.0)
    show damion face
    with fade
    if (bangok_four_common.bangnokay.check()):
        jump bangok_four_bangnokay_kill_replay
    jump bangok_four_xdamion_replay_merge

label bangok_four_xdamion:
    c "[player_name], ambassador from humanity to dragonkind."

    if (bangok_four_common.bangnokay.check()):
        Dm arrogant "Tchk, of course. Immediately with a big fancy title. This whole thing is so blown out of proportion, it makes me wonder how many coffees you had to deliver to be the one coming here."
        c "Hey, I'm nobody's suckup."
        Dm "You might look better doing some of that."
        menu:
            "Uh...":
                Dm "Everyone's acting like it's some huge event that everyone should be celebrating.{w} Newsflash: Not everyone cares."
                Dm "Once both of you are gone, life will return to normal and we can all go back to what we actually should be doing."
                jump bangok_four_xdamion_canon_whatdidyouwant
            "I could \"suck up\" to you if it'd help your mood.":
                $ renpy.pause (0.5)
                Dm "I..."
                $ renpy.pause (0.5)
                show damion face with dissolve
                $ renpy.pause (0.4)
                Dm face "Ha{w=0.4} ha.{w=0.4} Very funny."
                Dm normal "Frankly, the image of the great human ambassador sucking up to a lowly researcher is already amusing enough."
                Dm arrogant "No need to go through the song and dance."
                Dm arrogant "Let me spell this out simply enough for you to understand:{w} Not everyone cares."
                Dm "Once both of you are gone, life will return to normal and we can all go back to what we actually should be doing."
                show damion face with dissolve
                jump bangok_four_xdamion_canon_whatdidyouwant

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
    $ chap2damionquestions = 0
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
            $ bangok_four_xdamion_store.position = "oral"
            $ bangok_four_malepartners += 1
            show damion arrogant bangok:
                transform_anchor True
                ease 0.5 zoom 2.4
            show crapannalab:
                transform_anchor True
                ease 0.5 zoom 2.2
            with None
            $ renpy.pause (0.8)
            Dm "There's a good cocksucker."
            $ renpy.pause (0.5)
            Dm normal bangok "Well? Get started."
            $ renpy.pause (0.3)
            show black with dissolve
            $ renpy.pause (0.5)

            m "I took Damion's slick, tapered dragonhood into my mouth."
            m "As I began to explore with my tongue, I realized with some amount of surprise it almost felt like his tip was exploring back, his cockflesh malleable and motile, not hard and spongy like anything I'd experienced before."

            m "I suckled at his slit-juice-coated teat for a few moments, until I felt a different taste on my tongue -- sweet drops of pre."
            $ renpy.pause (0.8)
            m "Impatiently, Damion took a hold on my head, pushing a little more of himself into my mouth."
            Dm normal bangok "Come on. Can't you do more than that?"
            $ renpy.pause (1.0)
            menu:
                "Try to take him deeper.":
                    m "I leaned forward a little into his pulling, accepting just a tiny bit more until his tip was at the back of my throat."
                    m "Having given him an inch, Damion took a mile."
                    Dm normal bangok ws "You want me in your throat? Hold your breath, cocksucker."
                    m "I felt both his hands gripping the back of my head, abruptly pulling me as deep as my mouth could take him, spreading his pre on the back of my mouth as I gagged."
                    Dm face "Not so fleshy and malleable inside, huh?"
                    m "Angling my head back, he aimed his cock downward. I only had a moment to suck in air before he sank his slick, tapered rod deeper, into my throat, until my nose was pressing into his scale-lined slit."
                    Dm normal "There we go."
                    m "Getting a better grip on my head, he lined himself up again, before thrusting into my vulnerable windpipe."
                    play soundloop "fx/bangok_poundofsalt.ogg"
                    m "I gagged, struggling with blocked airways as he took the pleasure he wanted from my throat."
                    m "I could barely see him throwing his head back in ecstacy, as he pulled my face into his slit."
                    Dm face bangok "Fuuuck, human. It's like you were built to take my cock."
                    Dm arrogant bangok "Wouldn't it just be perfect if all this hubub, it was dragons who made humans to be their fucktoys? With time travel or some fuckery?"
                    Dm "You sure are a prime example."
                    stop soundloop fadeout 0.5
                    m "Finally letting me back off a bit, he waited, almost impatiently, as I caught my breath."
                    m "Then he pulled me back up his length, into his now saliva-slickened groin."
                    Dm normal bangok "Fucking perfect."
                    play soundloop "fx/bangok_poundofsalt.ogg"
                    m "He began to thrust again, bottoming out in me, rubbing my nose into his malleable slitflesh."
                    Dm face bangok "Almost might--"
                    stop soundloop fadeout 0.5
                    play sound "fx/snarl.ogg"

                    m "He sealed my face to his groin, cock twitching and pulsing as his body pushed spurts of seed down my abused throat."
                    if persistent.bangok_inflation == True:
                        m "It sank heavy and hot into my belly, spurt after spurt until I felt like I couldn't have swallowed another drop."
                    m "It slid down my throat, injected deep enough that all I could taste was his saliva-slicked cockflesh pulsing over my tongue."
                    show damion normal bangok
                    hide black
                    with dissolve
                    m "Then Damion pulled back, dribbling a last few tantalizing spurts across my tongue before wiping his unique tip on my cheek, staining it with his leftover seed."
                "Use hands.":
                    m "I wrapped a hand around his base, finding it easily sliding over his slit-juice-slicked length."
                    play soundloop "fx/bangok_poundofsalt.ogg" fadein 1.0
                    m "While still licking and swirling his tip in my mouth, I began to pump his shaft, getting at first one, then both hands dirty with working his shaft."
                    Dm face bangok "Want the reward without the challenge, huh?"
                    Dm arrogant bangok "Fine. I don't need your throat anyway."
                    stop soundloop fadeout 0.5
                    play sound "fx/slap1.wav"
                    m "He slapped my hand away."
                    Dm normal bangok "If all you're good for is as a receptacle, I'll handle that myself."
                    play soundloop "fx/bangok_poundofsalt.ogg" fadein 1.0
                    m "One hand on my head, he began to pump his member himself with his other hand."
                    $ renpy.pause (1.0)
                    Dm "Mm. Keep licking my tip like that and I might even let you swallow instead of dumping it on your face."
                    m "I swirled and suckled his unique tip, my tongue tangling with it as I struggled to get him off before thoughts about what I was doing could catch up with me."
                    $ renpy.pause (1.0)
                    Dm "Almost there, cocksucker..."
                    $ renpy.pause (0.8)
                    stop soundloop fadeout 0.5
                    play sound "fx/snarl.ogg"
                    m "Letting go of his shaft, he grabbed my head and pulled, shoving his cock against the back of my throat."
                    m "Jets of his thick, almost creamy seed exploded against the back of my mouth, flowing back over my tongue and teeth as I struggled to swallow."
                    if persistent.bangok_inflation == True:
                        m "Spurt after spurt blasted into my mouth, filling my cheeks as his load choked my throat full."
                    m "He changed his grip as his twitching slowed, putting a hand under my chin."
                    Dm normal "Swallow."
                    if persistent.bangok_inflation == True:
                        m "I gagged and choked, his tip against the back of my throat obstructing my gulps."
                        m "His seed sank heavy and hot into my belly, spurt after spurt until I felt like I couldn't have swallowed another drop."
                    else:
                        $ renpy.pause (0.8)
                    Dm arrogant bangok "Mmh."
                    m "He withdrew from my lips, his tip slathering a thin line of seed from my lips to my chin, staining it with his leftover cum."
                    hide black with dissolvemed
        "Offer your ass." if bangok_four_xdamion_store.ass_offered == False:
            $ bangok_four_xdamion_store.ass_offered = True
            m "I turned partway around, tugging at my waistband with a thumb."
            c "What if, instead, you filled my ass?"
            Dm face bangok "What the fuck?{w=0.5} Do I look like I want your crap on my penis?"
            Dm arrogant bangok "Suck me or get out."
            jump bangok_four_xdamion_fuck_positionmenu
        "Offer your slick, needy hole." if bangok_four_playerhasdick == False:
            $ bangok_four_xdamion_store.position = "vaginal"
            $ bangok_four_malepartners += 1
            m "I hopped up on the lab bench, sliding a hand under my waistband."
            c "Okay, how about you put that where it's supposed to go?"
            Dm face bangok "What are you...?"
            Dm normal bangok "Oh."
            Dm arrogant bangok "Oh you slutty bitch."
            Dm "Pants off. Strip."
            play sound "fx/undress.ogg"
            $ renpy.pause (0.5)
            m "I worked my waistband around my rear, wiggling on the lab bench until the cloth dropped over my knees, down around my ankles."
            show damion arrogant bangok:
                ypos 1.7
                transform_anchor True
                ease 0.5 zoom 2.4
            with ease
            m "Damion stepped over my pants, then kicked backward to yank my legs tighter around him, pulling me closer so that his slick, tapered length rubbed my dampening outer folds."
            m "His tip prodded the hem of my shirt, staining it with a drop of pre as his shaft rubbed over my pelvis."
            if persistent.bangok_inflation == True:
                Dm "There's a good slut. I'm gonna make you look stuffed with a clutch."
            else:
                if persistent.bangok_cervpen == True:
                    if persistent.bangok_cloacas == True:
                        Dm "There's a good slut. I'm gonna paint your cloaca white. Maybe even your womb, too."
                    else:
                        Dm "There's a good slut. I'm gonna paint your vagina white. Maybe even your womb, too."
                else:
                    if persistent.bangok_cloacas == True:
                        Dm "There's a good slut. I'm gonna paint your cloaca white."
                    else:
                        Dm "There's a good slut. I'm gonna paint your vagina white."

            menu:
                "W-Wait, protection!":
                    $ renpy.pause (0.5)
                    Dm face bangok "Are you fucking kidding me?"
                    Dm normal bangok "You must not have seen many dragon cocks, then. Mine isn't the most common style, which makes condoms that stay on {i}fucking expensive.{/i}"
                    Dm face bangok "Besides. It's not like I could actually stuff you with a clutch. You're, what, a mammal? A different fucking species, at least."
                    show damion normal bangok with dissolve
                    m "He began to line himself up, wet tip nestling into my outer folds."

                    menu:
                        "Get off me!":
                            $ renpy.pause(0.5)
                            play sound "fx/impact3.ogg"
                            show damion face bangok:
                                ypos 2.0
                            with vpunch
                            $ renpy.pause(0.8)
                            m "I shoved Damion back and he tripped over the pants around my ankles and slammed to the floor."
                            $ renpy.pause (0.8)
                            Dm "..."
                            $ renpy.pause (0.8)
                            Dm "Get out of my lab."
                            scene black with dissolve
                            jump bangok_four_xdamion_canon_interrogation_over
                        "[[Let him.]":
                            $ renpy.pause (0.5)
                "[[Moan appreciatively.]":
                    $ renpy.pause (0.5)
                "Fucking fill me.":
                    $ renpy.pause (0.5)

            show damion normal bangok:
                ease 0.5 ypos 1.72
                pause 0.2
                ease 0.15 ypos 1.7

            m "He pulled back, then slid himself inside. I yelped, my hole wholly unprepared for the smooth, sinuous transition from small tip to thick, stretching base."

            if persistent.bangok_cervpen == True:
                m "In no small part, the sensation that elicited the sound was the moment he ran out of depth within me, before he'd fully inserted."
                m "My breathing was hot and heavy, groin on fire as I felt his tip twitching around against my innermost gate, even as he stood still holding my hips."
                m "Then he found the center of my gate and pushed, and my breath was taken by a much louder exclamation."

            show damion face bangok with dissolve
            show black with dissolve
            m "Grabbing my head, he silenced me by shoving his lips against mine, tongue slipping into my open mouth to tangle with mine."
            if persistent.bangok_cervpen == True:
                $ bangok_four_xdamion_store.position = "womb"
                m "He pushed harder, ignoring my cervix's attempts to bar him entry to my most sacred temple."
                m "My legs twitched against his thighs as he forced his way into my womb, bottoming out with his scaly slit against my stretched outer lips."
            else:
                m "Still sliding in, he bottomed out, scaly slit against my stretched outer lips."

            show damion normal bangok:
                zoom 2.4 ypos 1.7
                ease 0.5 zoom 2.35 ypos 1.72
                ease 0.15 zoom 2.4 ypos 1.7
                repeat
            with None
            play sound "fx/bangok_poundofsalt.ogg"

            m "He barely gave me a few moments before beginning to thrust, stretching my outer folds again and again around his thick base, before sliding out to leave me feeling almost empty and thrusting in again."

            m "He broke the deep kiss, pulling back from me as his thrusting left me shivering in ecstacy."

            show damion normal bangok
            hide black
            with dissolve

            Dm arrogant bangok "Squeeze tighter, slut. Take my cum and keep it all inside."

            if persistent.bangok_cervpen == True:
                m "The stretching and shrinking of my cervix around his tapered tip left me too numbed out to consider his command. Even the short length that was able to punch into my deepest center was enough to leave my belly and thighs lost in a sea of electric, spasming pain and pleasure."
            else:
                m "The sliding of his slick length past my inner walls left me twitching and spasming. The unusual shape of his shaft slipped over different spots inside of me with every thrust, leaving me constantly guessing and surprised by his ceaseless fucking of my canal."

            show damion normal bangok with dissolve
            show damion normal bangok:
                ease 0.5 zoom 2.375 ypos 1.71
                ease 0.15 zoom 2.4 ypos 1.7
                repeat
            with None
            m "I squeezed tighter with my weak legs, pulling him closer to try to reduce the pitch of his thrusts, to keep my outer folds stretched and sealed to him, as well as to pull myself closer to my own peak."
            $ renpy.pause (0.8)
            Dm "Not long, slut. I'll... nngh... give you what you want."
            $ renpy.pause (0.8)
            Dm "Just..."
            show white with dissolve
            m "I went over my peak just before he did."
            stop soundloop fadeout 0.5
            play sound "fx/snarl.ogg"
            $ renpy.pause (0.2)
            show damion face bangok:
                ease 0.15 zoom 2.4 ypos 1.7
            with None

            if persistent.bangok_inflation == True and persistent.bangok_cervpen == True:
                m "Punching through my inner gate and stretching my outer lips taut, he twitched and pulsed, then released his jets of seed directly into my sacred temple."
                m "Rope after rope of cum layered over my innermost walls, until I could feel the thick load sliding and pooling, then pressing my filled womb outward."
                m "I moaned, belly expanding slightly as his spurts finally came to an end."
            elif persistent.bangok_inflation == True:
                m "Sealing his slit against my taut outer lips, he twitched and pulsed, then released jets of seed that packed the end of my canal, layering over my inner walls until no room remained but my womb."
                m "Then the jets of seed forced themselves deeper, spurting over my innermost walls and seeping through my filled tubes until my sacred temple was thoroughly marked by him."
            elif persistent.bangok_cervpen == True:
                m "Punching through my inner gate and stretching my outer lips taut, he twitched and pulsed, then released his jets of seed directly into my sacred temple. The cum layered over my innermost walls, marking my innermost walls."
            else:
                m "Sealing his slit against my taut outer lips, he twitched and pulsed, then released his jets of seed onto my spasming walls."


            hide white with dissolvemed

            $ renpy.pause (0.5)
            show damion arrogant bangok with dissolve
            m "He let me fall back against the lab bench with a smirk."
            show damion normal bangok with dissolve
            play sound "fx/rummage.wav"
            $ renpy.pause (0.1)
            stop sound fadeout 0.3
            m "Reaching to the side while still inside me, he pulled open a drawer, retrieving a black rubber stopper."
            if False: #persistent.bangok_knot == True:
                show damion normal bangok:
                    easeout 0.5 zoom 2.36 ypos 1.70
                with None
                m "Then he began to pull out and, after an inch or two and without warning, I felt a massive pain yanking on my stretched hole."
                c "AAH! H-Hey-- Stop, that's--"
                Dm face "Quit complaining. You fit my base, so this-- nnrgh."
                show damion normal bangok:
                    easeout 3.0 zoom 2.37 ypos 1.72
                with None
                m "I yelped as he tried to yank his knot free again, planting his hands on my legs and pushing himself back."
                c "Damion, I can't--"
                m "Ever so slowly, my hole stretched, revealing the bulge of flesh formed a few inches from his base after he came."
                show damion normal bangok:
                    easeout 0.15 zoom 2.35 ypos 1.72
                with None
                play sound "fx/uncork.ogg"
                m "Then he popped free, with a massive surge of relief that left my legs limp."
            else:
                show damion normal bangok:
                    easeout 1.0 zoom 2.35 ypos 1.72
                with None
                m "Then he slid out of me in one long motion, leaving his seed to dribble down toward my parted outer lips."

            if persistent.bangok_inflation == True:
                m "Before more than a small flow of his large load of cum could leak out of me, he shoved the stopper into my hole, blocking the worst of the mess within."
            else:
                m "Before more than a few drops of his cum could leak out of me, he shoved the stopper into my hole, blocking the worst of the mess within."
            Dm normal bangok "That'll keep you from making a mess of my lab."
            c "H-Hey!"
            m "I fumbled at my hole, able to feel the surface of the stopper past my outer lips, but unable to find an edge or pull it free."
            Dm "Just go somewhere that's not my lab and push. It's not like it can get lost up there."
            m "I clenched around the rough rubber object. It was, at least, keeping his seed inside of me."
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

    jump bangok_four_xdamion_satisfied

label bangok_four_xdamion_ws_fuck:
    show damion normal bangok ws:
        zoom 1.3
        anchor (0.5,1.0)
        pos (0.6,1.0)
    with dissolve
    $ chap2damionquestions = 0
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

    label bangok_four_xdamion_ws_fuck_positionmenu:
    menu:
        "Drop to your knees.":
            $ bangok_four_xdamion_store.position = "urinal"
            $ bangok_four_malepartners += 1
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
            m "His slit rubbed piss he'd dribbled into the rest of my face, leaving my nose thick with the unmistakable scent, while a drop of golden evidence squeezed out to run down my chin."
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
                    play soundloop "fx/bangok_poundofsalt.ogg"
                    if persistent.bangok_inflation == True:
                        m "I gagged, stomach full of his piss roiling as he took the pleasure he wanted from my throat."
                    else:
                        m "I gagged, piss-stained airways blocked as he took the pleasure he wanted from my throat."
                    m "I could barely see him throwing his head back in ecstacy, as he pulled my face into his slit."
                    Dm face bangok ws "Fuuuck, human. It's like you were built to take my cock."
                    Dm arrogant bangok ws "Wouldn't it just be perfect if all this hubub, it was dragons who made humans to be their fucktoys? With time travel or some fuckery?"
                    Dm "You sure are a prime example."
                    stop soundloop fadeout 0.5
                    m "Finally letting me back off a bit, he waited, almost impatiently, as I caught my breath."
                    m "Then he pulled me back up his length, into his piss-stained groin."
                    Dm normal bangok ws "Fucking perfect."
                    play soundloop "fx/bangok_poundofsalt.ogg"
                    m "He began to thrust again, bottoming out in me, rubbing my nose into his malleable slitflesh."
                    Dm face bangok ws "Almost might--"
                    stop soundloop fadeout 0.5
                    play sound "fx/snarl.ogg"

                    m "He sealed my face to his groin, cock twitching and pulsing as his body pushed spurts of seed down my defiled throat."
                    if persistent.bangok_inflation == True:
                        m "It sank heavy and hot into my belly of piss, spurt after spurt until I wasn't sure I'd be able to keep Damion's fluids down when he pulled out."
                    m "It slid down my throat, injected deep enough that all I could taste was his piss-stained cockflesh pulsing over my tongue."
                    show damion normal bangok ws
                    hide black
                    with dissolve
                    m "Then Damion pulled back, dribbling a last few tantalizing spurts across my tongue before wiping his unique tip on my clean cheek, staining it with seed and urine."
                "Use hands.":
                    m "I wrapped a hand around his base, finding it easily sliding over his piss- and slit-juice-slicked length."
                    play soundloop "fx/bangok_poundofsalt.ogg" fadein 1.0
                    m "While still licking and swirling his tip in my mouth, I began to pump his shaft, getting at first one, then both hands dirty with his leakage."
                    Dm face bangok ws "Want the reward without the challenge, huh?"
                    Dm arrogant bangok ws "Fine. I don't need your throat anyway."
                    stop soundloop fadeout 0.5
                    play sound "fx/slap1.wav"
                    m "He slapped my hand away."
                    Dm normal bangok ws "If all you're good for is as a receptacle, I'll handle that myself."
                    play soundloop "fx/bangok_poundofsalt.ogg" fadein 1.0
                    m "One hand on my head, he began to pump his member himself with his other hand."
                    $ renpy.pause (1.0)
                    Dm "Mm. Keep licking my tip like that and I might even let you swallow instead of dumping it on your face."
                    if persistent.bangok_inflation == True:
                        m "I swirled and suckled his unique tip, my tongue tangling with it as I struggled to get him off before my stomach full of his piss caught up with me."
                    else:
                        m "I swirled and suckled his unique tip, my tongue tangling with it as I struggled  to get him off before thoughts about what I was doing and what I'd just drank could catch up with me."
                    $ renpy.pause (1.0)
                    Dm "Almost there, urinal..."
                    $ renpy.pause (0.8)
                    stop soundloop fadeout 0.5
                    play sound "fx/snarl.ogg"
                    m "Letting go of his shaft, he grabbed my head and pulled, shoving his cock against the back of my throat."
                    m "Jets of his thick, almost creamy seed exploded against the back of my mouth, flowing back over my tongue and teeth as I struggled to swallow."
                    if persistent.bangok_inflation == True:
                        m "Spurt after spurt blasted into my mouth, filling my cheeks as his load choked my throat full."
                    m "He changed his grip as his twitching slowed, putting a hand under my chin."
                    Dm normal "Swallow."
                    if persistent.bangok_inflation == True:
                        m "I gagged and choked, my piss-filled stomach struggling to accommodate the added gulps of seed."
                        m "It sank heavy and hot into my belly of piss, spurt after spurt until I wasn't sure I'd be able to keep Damion's fluids down when he pulled out."
                    else:
                        $ renpy.pause (0.8)
                    Dm arrogant bangok ws "Mmh."
                    m "He withdrew from my lips, his tip slathering a thin line of seed from my lips to my chin."
                    hide black with dissolvemed

        "Offer your ass." if bangok_four_xdamion_store.ass_offered == False:
            $ bangok_four_xdamion_store.ass_offered = True
            m "I turned partway around, tugging at my waistband with a thumb."
            c "What if, instead, you filled my ass?"
            Dm face bangok "What the fuck?{w=0.5} Do I look like I want your crap on my penis?"
            Dm arrogant bangok "Suck me or get out."
            jump bangok_four_xdamion_ws_fuck_positionmenu
        "Offer your slick, needy hole." if bangok_four_playerhasdick == False:
            $ bangok_four_xdamion_store.position = "vaginalws"
            $ bangok_four_malepartners += 1
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
                ease 0.5 ypos 1.72
                pause 0.2
                ease 0.15 ypos 1.7
            m "Without waiting for confirmation he pulled back, then shoved his stinking length inside me."
            m "I yelped, my hole wholly unprepared for the smooth, sinuous transition from small tip to thick, stretching base."
            if persistent.bangok_cervpen == True:
                m "In no small part, the sensation that elicited the sound was the moment he ran out of depth within me, before he'd fully inserted."
                m "My breathing was hot and heavy, groin on fire as I felt his tip twitching around against my innermost gate, even as he stood still holding my hips."
                m "Then he found the center of my gate and pushed, and my breath was taken by a much louder exclamation."
            show damion face bangok ws with dissolve
            show black with dissolve
            m "Grabbing my head, he silenced me by shoving his lips against mine, tongue slipping into my open mouth to tangle with mine."
            if persistent.bangok_cervpen == True:
                $ bangok_four_xdamion_store.position = "wombws"
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
                    m "My womb wasn't even enough to contain his pissload. His urine saturated my tubes and pressed back against my dilated cervix, seeping into my passage and bloating my sacred temple with sacrilege as he used me as his toilet."
            else:
                m "Then, his lips still to mine, I felt a hot jet against my inner walls, defiling my passage with his liquid waste."
                m "I melted into his grasp, the warmth in my love canal spreading and suffusing my body with the knowledge I was his to use as he pleased, to piss in how he wanted."
                if persistent.bangok_inflation == True:
                    m "There wasn't even room enough in my canal to contain his pissload. His urine saturated my tubes and pressed against my cervix, spraying through into my deepest center as he used my sacred temple as a toilet."

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
                ease 0.5 zoom 2.35 ypos 1.72
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
                ease 0.5 zoom 2.375 ypos 1.71
                ease 0.15 zoom 2.4 ypos 1.7
                repeat
            with None
            m "I squeezed tighter with my weak legs, pulling him closer to try to reduce the pitch of his thrusts, to keep my outer folds stretched and sealed to him, as well as to pull myself closer to my own peak."
            $ renpy.pause (0.8)
            Dm "Not long, slut. I'll... nngh... give you what you want."
            $ renpy.pause (0.8)
            Dm "Just..."
            show white with dissolve
            m "I went over my peak just before he did."
            stop soundloop fadeout 0.5
            play sound "fx/snarl.ogg"
            $ renpy.pause (0.2)
            show damion face bangok ws:
                ease 0.15 zoom 2.4 ypos 1.7
            with None


            if persistent.bangok_inflation == True and persistent.bangok_cervpen == True:
                m "Punching through my inner gate and stretching my outer lips taut, he twitched and pulsed, then released his jets of seed into the urine already filling my womb."
                m "I mewled, the sludge of cum and piss pressuring my belly outward until I looked slightly pregnant, while the spasming of my internal muscles ensured every inch of my inner walls were fully defiled."
            elif persistent.bangok_inflation == True:
                m "Sealing his slit against my taut outer lips, he twitched and pulsed, then released jets of seed that packed the end of my canal, layering over my piss-stained walls until no room remained but my womb."
                m "Then the jets of seed forced themselves deeper, becoming a thinner sludge as they mixed with the piss bloating my sacred temple to expand me further, until I looked slightly pregnant."
            elif persistent.bangok_cervpen == True:
                m "Punching through my inner gate and stretching my outer lips taut, he twitched and pulsed, then released his jets of seed into my urine-stained womb, spraying his wasted cum over the sacrilege coating my innermost walls to further stain my deepest center."
            else:
                m "Sealing his slit against my taut outer lips, he twitched and pulsed, then released his jets of seed into my urine-stained passage, spraying his wasted cum over my inner walls to further stain my used canal."

            hide white with dissolvemed

            $ renpy.pause (0.5)
            show damion arrogant bangok ws with dissolve
            m "He let me fall back against the lab bench with a smirk."
            show damion normal bangok ws with dissolve
            play sound "fx/rummage.wav"
            $ renpy.pause (0.1)
            stop sound fadeout 0.3
            m "Reaching to the side while still inside me, he pulled open a drawer, retrieving a black rubber stopper."
            if False: #persistent.bangok_knot == True:
                show damion normal bangok ws:
                    easeout 0.5 zoom 2.36 ypos 1.70
                with None
                m "Then he began to pull out and, after an inch or two and without warning, I felt a massive pain yanking on my stretched hole."
                c "AAH! H-Hey-- Stop, that's--"
                Dm face "Quit complaining. You fit my base, so this-- nnrgh."
                show damion normal bangok ws:
                    easeout 3.0 zoom 2.37 ypos 1.72
                with None
                m "I yelped as he tried to yank his knot free again, planting his hands on my legs and pushing himself back."
                c "Damion, I can't--"
                m "Ever so slowly, my hole stretched, revealing the bulge of flesh formed a few inches from his base after he came."
                show damion normal bangok ws:
                    easeout 0.15 zoom 2.35 ypos 1.72
                with None
                play sound "fx/uncork.ogg"
                m "Then he popped free, with a massive surge of relief that left my legs limp."
            else:
                show damion normal bangok ws:
                    easeout 1.0 zoom 2.35 ypos 1.72
                with None
                m "Then he slid out of me in one long motion, leaving his fluids to dribble down toward my parted outer lips."

            if persistent.bangok_inflation == True:
                m "Before more than a small stream of his large load of piss and cum could leak out of me, he shoved the stopper into my hole, blocking the worst of the mess within."
            else:
                m "Before more than a few drops of his piss and cum could leak out of me, he shoved the stopper into my hole, blocking the worst of the mess within."
            Dm normal "That'll keep you from making a mess of my lab."
            c "H-Hey!"
            m "I fumbled at my hole, able to feel the surface of the stopper past my outer lips, but unable to find an edge or pull it free."
            Dm "Just go somewhere that's not my lab and push. It's not like it can get lost up there."
            m "I clenched around the rough rubber object. It was, at least, keeping his fluids inside of me."
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

    jump bangok_four_xdamion_satisfied

label bangok_four_xdamion_satisfied:
    if bangok_four_xdamion_store.position in ["urinal","vaginalws","wombws"]:
        Dm arrogant bangok ws "Well done, urinal. I'm satisfied."
    elif bangok_four_xdamion_store.position == "oral":
        Dm arrogant bangok "Well done, cocksucker. I'm satisfied."
    else:
        Dm arrogant bangok "Well done, slut. I'm satisfied."
    jump bangok_four_xdamion_canon_whatdidyouwant

label bangok_four_xdamion_questions_getup:
    $ bangok_four_xdamion_store.standing_unattempted = False
    if bangok_four_xdamion_store.position in ["urinal","oral"]:
        m "I moved to try to get to a less demeaning position than on my knees before him."
        m "Damion pushed me back."
    else:
        m "I moved to try to get to a less demeaning position than lying on his lab bench with my legs spread, but he caught my chest with a hand, and my pants caught around his legs."
    Dm arrogant "Oh no. I'm enjoying this image of the sexually-used human ambassador far too much. You stay right there."
    jump chap2facques

label bangok_four_xdamion_cleanup:
    Dm arrogant "Then I have one last task for you."
    if bangok_four_xdamion_store.position in ["vaginal","womb","vaginalws","wombws"]:
        if persistent.bangok_watersports == True and bangok_four_xdamion_store.position in ["vaginalws","wombws"]:
            show damion arrogant bangok ws:
                ease 0.5 zoom 2.2
            with None
        else:
            show damion arrogant bangok:
                ease 0.5 zoom 2.2
            with None
        m "He stepped back."
        Dm "Down on your knees."
        if persistent.bangok_watersports == True and bangok_four_xdamion_store.position in ["vaginalws","wombws"]:
            show damion arrogant bangok ws:
                ease 0.5 ypos 1.6
                ease 2.0 ypos 1.0
                ypos 1.0
        else:
            show damion arrogant bangok:
                ease 0.5 ypos 1.6
                ease 2.0 ypos 1.0
                ypos 1.0
        show crapannalab:
            pause 0.5
            ease 2.0 zoom 2.2
        with None
        m "Hesitantly I slipped from the lab bench, my legs weak from my recent rough fucking, then sank to my knees before him."
        if persistent.bangok_watersports == True and bangok_four_xdamion_store.position in ["vaginalws","wombws"]:
            if persistent.bangok_inflation == True:
                m "My heavy, few-month pregnancy of cum and piss nearly put me off balance as I, and it, settled."
            Dm arrogant bangok ws "Good slut."
            m "His cock hung before me, slathered in our coital juices and traces of his piss."
        else:
            if persistent.bangok_inflation == True:
                m "My heavy, wombful of cum nearly put me off balance as I, and it, settled."
            Dm arrogant bangok "Good slut."
            m "His cock hung before me, slathered in our coital juices."
    else:
        if persistent.bangok_watersports == True and bangok_four_xdamion_store.position in ["urinal","vaginalws","wombws"]:
            show damion arrogant bangok ws with dissolve
            m "I watched with a small thrill of trepidation as his cock re-emerged from his piss-stained slit, slick with my saliva and his juices."
        else:
            show damion arrogant bangok with dissolve
            m "I watched with a small thrill of trepidation as his cock re-emerged from his slit, slick with my saliva and his juices."


    m "He slapped it lightly against my cheek."
    Dm "Now lick it clean. All the way down."

    menu:
        "[[Lick.]":
            pass
        "I should probably be going...":
            Dm face bangok "Fine. Then get out."
            scene black with dissolve
            jump bangok_four_xdamion_canon_interrogation_over

    m "I lapped delicately at his length, trying to lap up anything he might consider a stain."
    if persistent.bangok_watersports == True and bangok_four_xdamion_store.position in ["urinal","vaginalws","wombws"]:
        Dm normal bangok ws "I said {i}all the way{/i}"
        show black with dissolve
        m "I felt his hand on the back of my head, then he was rubbing my face in his piss-soaked genital slit, cock pressed across the side of my head."
    else:
        Dm normal bangok "I said {i}all the way{/i}"
        show black with dissolve
        m "I felt his hand on the back of my head, then he was rubbing my face in his wet genital slit, cock pressed across the side of my head."

    m "Trying to obey his instructions, I extended my tongue, digging into Damion's slit, lapping up his slit juices and the results of our coitus."
    $ renpy.pause (0.5)
    m "A long, relaxed sigh hissed between Damion's teeth."
    Dm arrogant "Now the other side."
    $ renpy.pause (0.5)
    m "Though he'd removed his hand from my head, I kept my face in his slit, tonguing around beneath, then into the opposite side of his shaft's base."
    m "His shaft rubbed over my face as I moved, leaving my face sticky with his juices and my own saliva."
    Dm normal bangok "Hmh."
    Dm "That's enough."
    hide black with dissolvemed
    $ renpy.pause (0.5)

    if bangok_four_xdamion_store.position in ["vaginal","womb","vaginalws","wombws"]:
        Dm arrogant bangok "Alright. Get the fuck out of here before someone connects your stained face or leaking hole back to me."
        scene black with dissolvemed
        m "As I got back to my feet, I tried to remember the path to the closest restroom, where I could clean Damion's mess off, and try to get at least most of it out."
    else:
        Dm arrogant bangok "Alright. Get the fuck out of here before someone connects your stained face back to me."
        scene black with dissolvemed
        m "As I got back to my feet, I tried to remember the path to the closest restroom, where I could clean Damion's mess off."

    jump bangok_four_xdamion_canon_interrogation_over
