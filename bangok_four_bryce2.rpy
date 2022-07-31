init python:
    bangok_four_bryce2_unplayed = True

init python in bangok_four_bryce2_store:
    forepaw_tickle = False


    hindpaw_tickle = False
    hindpaw_suckle = False
    hindpaw_lick = False
    hindpaw_massage = False


    player_came = False
    bryce_came = False
    cumlube = False


label bangok_four_bryce2_skipmenu:
    play sound "fx/system3.wav"
    s "Would you like to lewd Bryce's feet?"
    menu:
        "Yes. I would like to lewd Bryce's feet.":
            play sound "fx/system3.wav"
            if bangok_four_bangnokay or persistent.bangok_four_bangnokay:
                s "Too bad.{cps=2}..{/cps}{w=1.0}{nw}"
            else:
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                scene black with dissolvemed
                $ renpy.pause (1.0)

                $ persistent.skipnumber += 1
                call skipcheck from _bangok_four_call_skipcheck_bryce2_1

                $ bryce2mood += 1

                scene pad at Pan ((0, 360), (0,360), 0.0)
                show bryce brow bangok foreleg flip
                with dissolvemed

                play music "mx/campfire.ogg" fadein 2.0
                jump bangok_four_bryce2_explorepaw
        "No. Not that far.":
            pass
    jump bangok_four_bryce2_skipmenu_return


label bangok_four_bryce2_explorepaw:
    $ renpy.pause (0.5)
    m "I slid my hand lower on Bryce's foreleg, feeling the rough bumps and scales on his foreleg protecting the thick knots of muscle that gave him his strength."
    show bryce brow bangok foreleg flip with dissolve
    m "He let me pick up his leg as I nearly reached the floor, giving me his forepaw with a look."
    $ renpy.pause (0.8)
    c "Gorgeous."
    if bangok_four_bryce1_unplayed == False and persistent.nsfwtoggle == True:
        Br laugh bangok foreleg flip "Okay, I thought we specified no sex this time."
        Br smirk bangok foreleg flip "It almost sounds like you're hitting on me."
    else:
        Br laugh bangok foreleg flip "Okay, you don't have to go that hard on the flattery."
        show bryce smirk bangok foreleg flip with dissolve

    menu:
        "I can't compliment a good-looking dragon?":
            $ renpy.pause (0.5)
            $ bryce2mood += 1
            Br flirty bangok foreleg flip "Well, I suppose I can't stop you."

        "[[Kiss his foot.]":
            $ renpy.pause (0.5)
            show bryce brow bangok foreleg flip with dissolve
            play sound "fx/kiss.wav"
            $ renpy.pause (1.1)
            $ bryce2mood -= 1
            Br brow bangok foreleg flip "... Uh. Huh."

        "Hey, I'm just saying. About the case, though...":
            jump bangok_four_bryce2_explorepaw_end

    m "Feeling around a little further, my fingers brushed over the smooth palm of his paw -- or sole of his foot, if that's what I should be calling it."
    c "So what do you call these? Feet? Or paws? Forepaws?"

    Br brow bangok foreleg flip "Whatever's easiest at the moment, I guess. I don't think too hard about it."
    c "When is \"forepaw\" easier to say than \"foot\"?"
    Br laugh bangok foreleg flip "I don't know. I just said I don't think too much about it."
    m "His tail flicked as he shifted his weight."
    Br normal bangok foreleg flip "You're, ah, taking quite an interest in that, huh?"
    m "I hadn't noticed, but while we'd talked, I'd been unconsciously kneading his paw in my hand, feeling out more of the intricate biological joints in his scales where his toes met the body of his food."

    menu:
        "[[Give him his foot back.]":
            c "Oops, sorry."
            label bangok_four_bryce2_explorepaw_exit:
            show bryce normal with dissolve
            m "Bryce shifted a little away, pressing his forepaw into the floor with his other forepaw."
            Br normal "No scales off my back."
            c "Anyway, about the case..."
            $ bryce2mood -= 1
            jump bangok_four_bryce2_explorepaw_end

        "[[Tickle him.]":
            $ renpy.pause (0.5)
            $ bangok_four_bryce2_store.forepaw_tickle = True
            m "Holding his forepaw in place from the top with one hand, I flicked the fingers of my hand across the palm of his paw."
            show bryce brow bangok foreleg flip with dissolve
            $ renpy.pause (0.8)
            Br "Uh. What are you doing?"
            c "Tickling you?"
            Br "On my forepaw?"
            Br smirk bangok foreleg flip "You know I hold and move stuff all the time with that, right? It's not exactly ticklish."
            c "Oh."
            Br laugh bangok foreleg flip "But now I know that turnabout's fair play, huh? Your feet are pretty ticklish?"
            c "Uh."
            Br smirk bangok foreleg flip "Relax. I can't get to them through whatever you're wearing over them."
            Br brow bangok foreleg flip "Plus I wouldn't want to cut you down there. Might make some awkward questions."

            m "Speaking of awkward, I was still holding his foot."
            menu:
                "[[Give him his foot back.]":
                    $ renpy.pause (0.5)
                    jump bangok_four_bryce2_explorepaw_exit
                "Want a foot massage?":
                    $ renpy.pause (0.5)
                    Br "... a foot massage?"
                    c "I mean, it's the least I could do after, uh, trying to tickle you."
                    Br laugh bangok foreleg flip "Ha! Okay, sure I guess."
                    Br normal bangok foreleg flip "Not like I'm going to turn that down. I mean, free? Can't beat that price."

        "Uh. Do you want me to stop?":
            $ renpy.pause (0.5)
            Br "No."
            Br brow bangok foreleg flip "I mean, I don't want to make you do it or anything... I'm kinda enjoying it."
            Br laugh bangok foreleg flip "Heck. I can't remember the last time I've had a good foot massage."
            Br normal bangok foreleg flip "So, yeah, keep doing what you're doing, if you want to."
            menu:
                "Stop.":
                    $ renpy.pause (0.5)
                    jump bangok_four_bryce2_explorepaw_exit
                "Continue.":
                    pass

        "I guess I am.":
            $ renpy.pause (0.5)
            Br "Well, don't let me stop you. I'm kinda enjoying it."

    $ renpy.pause (0.5)
    $ bryce2mood += 1
    m "I added my other hand, intentionally now squeezing with both thumbs, feeling the structure of his bones beneath his scales."
    $ renpy.pause (1.5)
    Br laugh bangok foreleg flip "Mmh, that's good."
    $ renpy.pause (1.0)
    show bryce normal flip with dissolve
    m "Squeezing through his scales was hard work, and I switched to Bryce's other forepaw before my hands could get too sore."
    c "You keep these really clean."
    Br "Yeah. Keep the floor clean too, 'cause why would I want to live in a mess?"
    Br "Combine that with me have a little time off right now, which is why I invited you over instead of heading back out to the crime scenes."
    Br stern flip "Haven't actually been outside yet today, 'cause I'm worried I'd just go right back to work and not get any rest in."
    $ renpy.pause (0.5)
    Br brow flip "You know, I didn't invite you over just to let you give me massages. I'm supposed to be hosting. That means entertaining you, not the other way around."
    Br normal flip "I'm good on the massages if you are."
    if persistent.nsfwtoggle:
        menu:
            "Kiss his foot.":
                $ renpy.pause (0.5)
                show bryce brow bangok foreleg flip:
                    xalign 0.3
                with dissolve
                $ renpy.pause (0.3)
                show bryce brow bangok foreleg flip:
                    zoom 1.0
                    ease 0.5 zoom 1.5
                    zoom 1.5
                with None
                $ renpy.pause (0.5)
                play sound "fx/kiss.wav"
                $ renpy.pause (1.0)

            "Let his foot go.":
                jump bangok_four_bryce2_hosting_challenge_exit
    else:
        label bangok_four_bryce2_hosting_challenge_exit:
            c "Yeah, that's probably fair."
            c "Still gotta say: you have some good looking legs, Bryce."
            Br laugh "Thanks."
            jump bangok_four_bryce2_explorepaw_end

    $ renpy.pause (0.5)
    c "I'd say I'm pretty entertained right now."
    if bryce2mood < 0:
        show bryce stern with dissolve
        m "Bryce pulled his foot back with a glare."
        Br "You know what? No. You've insulted me enough already. You can stop being a creep over my legs or you can leave. Make your choice."
        menu:
            "Protest.":
                c "Oh come on. \"Creep\"? I gave you free foot massages."
                if bangok_four_bryce1_unplayed == False:
                    Br "Exactly. I made it clear I wanted to take things more slowly, and one of the first things you do is start rubbing your hands and mouth all over my legs."
                else:
                    Br "Exactly. I invited you over to just be two friends hanging out, getting to know each other, and one of the first things you do is start rubbing yourself all over my legs."
                c "You invited me to!"
                Br "I invited you to feel me flex my leg."
                Br brow "I'd say you overstayed your welcome after that when you put your mouth on me."
                Br stern "No offense, I don't know if this is just a human thing or just you, but I don't want to see where a jerk like you tries to take things."
                jump bangok_four_bryce2_canon_jerk_ending
            "Apologize.":
                c "I'm sorry. I thought you were into the foot stuff, and maybe my comment earlier was a little out of line..."
                Br brow "I mean, maybe I was, but after the insult it felt weird, even with your complimennts on my muscles."
                show bryce at center with ease
                m "I moved away, giving Bryce some space."
                c "Alright. Other topics..."
                jump bangok_four_bryce2_explorepaw_end
                # c "Let's, uh, just try to forget that happened. Please? There's plenty else we could talk about, like... like the case."
                # Br stern "I appreciate your apology, but I'm still not really feeling this."
                # c "But--"
                # Br brow "No offense, but rubbing all over other people when given a simple invitation to touch you makes you kind of a jerk."
                # menu:
                #     "Protest.":
                #         jump bangok_four_bryce2_canon_jerk_ending
                #     "Leave.":
                #         jump bangok_four_bryce2_canon_jerk_ending_departure
                # jump bangok_four_bryce2_explorepaw_end
            "Leave.":
                jump bangok_four_bryce2_canon_jerk_ending_departure
    else:
        Br flirty bangok foreleg flip "So that's where this is going."
        if bangok_four_bryce1_unplayed == False:
            Br stern bangok foreleg flip "So much for taking things slow after last time."
            c "I mean, we don't have to go that far."
            Br brow bangok foreleg flip "That's what my feet are doing for you though, right?"
            $ renpy.pause (0.8)

    if bryce2mood < 1:
        m "Bryce tugged his paw back gently."
        Br normal flip "Let me just shut that down right now. I'm not feeling it."
        c "Oh."
        if bangok_four_bryce1_unplayed == False:
            Br laugh flip "I told ya, I wanted to take things slower."
        else:
            Br laugh flip "I don't jump into things that fast."

        Br normal flip "Let's save fooling around with feet for another time."
        c "Alright."
        show bryce at center with ease
        m "I moved away, giving Bryce some space."
        c "Alright. Other topics..."
        jump bangok_four_bryce2_explorepaw_end

    Br laugh bangok foreleg flip "Ah, heck it."
    Br smirk bangok foreleg flip "I've got two more feet that need attention, huh?"

    show black with dissolvemed
    play sound "fx/cartslide.ogg"
    m "Bryce settled on his back on his couch, the springs complaining under his weight."
    m "I caught one of his hindlegs as he braced the other on the couch, quickly running my hands up to the object of interest on his hindleg."
    m "Bryce's hindpaw was structured much like his forepaw, though I could feel a joint missing or moved where on his forepaw he could fold one toe over opposably."
    m "The foot, and leg muscles behind it, seemed more human than I expected, if I disregarded the scales, claws, and only three toes."
    if bangok_four_bryce2_store.forepaw_tickle == True:
        Br smirk "Now, don't get any ideas about tickling me down there. I've still got three legs and a tail free."
        c "The big police chief is afraid of a little tickle?"
        Br laugh "I'm afraid of knocking you over or something."

label bangok_four_bryce2_hindpaw_menu:
    if sum([bangok_four_bryce2_store.hindpaw_tickle,bangok_four_bryce2_store.hindpaw_suckle,bangok_four_bryce2_store.hindpaw_lick,bangok_four_bryce2_store.hindpaw_massage]) < 3:
        menu:
            "Tickle." if bangok_four_bryce2_store.hindpaw_tickle == False:
                $ renpy.pause (0.8)
                $ bangok_four_bryce2_store.hindpaw_tickle = True
                play sound "fx/tableslap.wav"
                Br laugh "O-Okay! D-damnit you got me."
                m "Bryce's tail flicked back and forth. He was clearly struggling not to hit the coffee table again."
                Br stern "L-look, just-- He-- S-Stop that before I knock you over. D-Don't want to hurt ya by accident."
            "Massage." if bangok_four_bryce2_store.hindpaw_massage == False:
                $ renpy.pause (0.4)
                $ bangok_four_bryce2_store.hindpaw_massage = True
                m "Holding Bryce's foot in both hands, I kneaded the sole with my thumbs, working out the structure beneath."
                Br laugh "Mmmh. That's the spot."
            "Suck a claw." if bangok_four_bryce2_store.hindpaw_suckle == False:
                $ renpy.pause (0.5)
                $ bangok_four_bryce2_store.hindpaw_suckle = True
                m "I took one of Bryce's claws into my mouth, running the cold keratin across my tongue as I worked my way down to where the claw emerged."
                Br smirk "H-Huh. That's a feeling."
                m "I let his claw go."
                c "Good feeling?"
                Br smirk "Pretty good, yeah. Just, like, the little bit of contact around the tip of my toe, base of the claw. Dunnno how to describe it."
            "Lick the pad." if bangok_four_bryce2_store.hindpaw_lick == False:
                $ renpy.pause (0.5)
                $ bangok_four_bryce2_store.hindpaw_lick = True
                m "My tongue rubbed across Bryce's smooth scales on the sole of his foot, pounded smooth by years of supporting his weight and motion."
                m "Bryce shifted tail flicking."
                Br brow "That tickles a little. Can't really feel it, though."
        jump bangok_four_bryce2_hindpaw_menu

    show bryce laugh
    hide black
    with dissolvemed

    if bangok_four_bryce2_store.hindpaw_tickle == True:
        m "As I switched to Bryce's other hindleg to apply the same treatments, (sans tickling,) Bryce let out a breath."
    else:
        m "As I switched to Bryce's other hindleg to apply the same treatments, Bryce let out a breath."

    if bangok_four_bryce1_unplayed == False:
        Br laugh "I know I said no sex, but damnit if you worshiping my feet like that isn't getting me going."
    else:
        Br laugh "I didn't invite you over for this kind of thing, and heck, it might be a diplomatic incident, but damnit if you worshiping my feet like that isn't getting me going."

    Br smirk "What about my feet pressing you into something else of mine? Or I could put my feet on something of yours?"

    $ bangok_four_bryce2_unplayed = False
    if bangok_four_playerhasdick is None:
        m "It was hard to ignore the..."
        menu:
            m "It was hard to ignore the...{fast}"
            "... tent in my pants":
                $ bangok_four_playerhasdick = True
            "... damp spot forming in my pants":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick == True:
        m "It was hard to ignore the tent in my pants at Bryce's suggestion."
    else:
        m "It was hard to ignore the damp spot forming in my pants from Bryce's suggestion."

    menu:
        "Could you rub me off with your feet?":
            $ renpy.pause (0.5)
            Br laugh "Sure."
            Br smirk "As long as you're gonna help me out afterward."
            c "Deal."

            show black with dissolve

            play sound "fx/undress.ogg"
            $ renpy.pause (0.8)
            m "I stripped off my shirt, kicked away my shoes, then struggled out of my pants."
            jump bangok_four_bryce2_footjob


        "I'd love to worship more of you.":
            $ renpy.pause (0.5)
            Br flirty "C'mere."
            show black with dissolve

            play sound "fx/undress.ogg"
            $ renpy.pause (0.8)
            m "I stripped off my shirt, kicked away my shoes, then struggled out of my pants."
            m "I knelt next to him, examining to what I was about to give my fastidious attention."
            jump bangok_four_bryce2_worship


label bangok_four_bryce2_footjob:
    m "Bryce worked his legs, trying to comfortably put his feet at my crotch height while he reclined on his couch."
    if bangok_four_playerhasdick == True:
        m "I examined his scaly walking pads, heady with arousal from what I was about to do."
        Br brow "Sorry for my claws being sharp, but you know the job I'm in doesn't exactly allow for me to cut them back."
        c "I'm not exactly fucking your claws, right?"
        Br laugh "Fair enough!"
        show bryce normal with dissolve
        if bangok_four_bryce2_store.cumlube == True:
            m "I pressed his feet together around my length, toes toward my tip, squeezing up and down to spread his cum out over his soles and my length."
            m "Then he gently began to move, his slickened feet moving easily up until he was just gripping my tip, then back down to press on both sides of my rock-hard shaft."
        else:
            m "I pressed his feet together around my length, toes toward my tip, feeling the just-slightly-rough texture of his soles squeezing in around my privates."
            m "Then he gently begann to move, his textured pads scraping over my rock-hard shaft in a way that left my knees weak from the overstimulation."
        m "As he pushed back down, the force of his feet bumping my pelvis almost put me just past off-balance, only caught by his quick thinking to tug me forward again with his toes gripped around my tip."
        c "O-Ow! H-Hey, don't rip it off!"
        Br laugh "Sorry."
        Br smirk "Trying not to knock you over and all."
        m "As he loosened up his toes, blood flowed back into the end of my member, leaving my groin flushed with heat, and a new idea in my head."
        # menu:
        #     "Fuck his toes.":
        c "Could you interlace your toes again?"
        Br brow "Hm?"
        m "Bryce did as asked, wrapping his toes and claws together in a dense knot of scales and keratin."
        m "His legs clearly strained at the angle."
        Br laugh "Testing the limits of my articulation, here."
        c "It'll be worth it."
        if bangok_four_bryce2_store.cumlube == True:
            m "Tugging his cum-sticky feet slightly further apart, I opened a small hole framed by a couple toes, then thrust in."
            m "The feeling was exquisite. I kneaded the top of his feet, pressing his soles into my pelvis as his toes clenched around my length."
        else:
            m "Tugging his feet slightly further apart, I opened a small hole framed by a couple toes, then thrust in."
            m "The coupling was rough, but pressed in all the right places. I kneaded the top of his feet, holding his soles against my pelvis as his toes clenched around my length."
        play soundloop "fx/rub2.ogg" fadein 0.5
        $ renpy.pause (0.5)
        m "I began to thrust for real, fucking between his toes as he chuckled beneath me."
        Br smirk "C-Can't say I've ever felt that before."
        $ renpy.pause (0.8)
        Br pant "Right there in the little spots between my toes. Mmnh."

        if bangok_four_bryce2_store.cumlube == True:
            m "Bryce's cum squelched less and less against my crotch as I neared my release, the hole made by his interlaced toes kneading the top and bottom of my shaft with the tips where they turned from scales to keratin, even as his feet separated a little from my pace."
        else:
            m "I had no words as I neared my release, the hole made by his interlaced toes kneading the top and bottom of my shaft with the tips where they turned from scales to keratin, even as his feet separated a little from my pace."

        #     "Fuck the arch of his feet.":
        #         jump todo_out_of_content_bangok_four_bryce2


        stop soundloop fadeout 0.5
        play sound "fx/rub1.ogg" fadein 0.5
        queue sound "fx/extinguish.ogg"
        $ bangok_four_bryce2_store.player_came = True
        $ renpy.pause (1.8)

        if bangok_four_bryce2_store.cumlube == True:
            m "My load was paltry in comparison to what Bryce's had been, but still left a few white ropes around his genital slit, where he pointed my shaft as I came."
        else:
            if bangok_four_bryce2_store.bryce_came == "outside" or bangok_four_bryce2_store.bryce_came == "cleaned":
                m "Bryce tugged my shaft downward as I came, stringing my white ropes of seed across his genital slit, joining the remains of what he'd already left behind."
            else:
                m "Bryce tugged my shaft downward as I came, stringing my white ropes of seed across his genital slit in a display of affection for his exquisite footwork."

        $ renpy.pause (0.8)
        Br laugh "I've gotta have you over for more \"foot massages.\""
        if bangok_four_bryce2_store.bryce_came == False:
            m "I could see Bryce's pink cockhead peeking from his slit."
            Br smirk "Well, you really got me going now."
            Br flirty "Gonna help with that?"
            jump bangok_four_bryce2_worship

    elif bangok_four_playerhasdick == False:
        m "I examined his scaly walking pads, heady with the choices before me."
        Br brow "Sorry for my claws being sharp, but you know the job I'm in doesn't exactly allow for me to cut them back."
        Br stern "It's, ah, probably not a good idea for you to put any of them in you, considering that's not safe even for female dragons."
        c "Makes sense."
        show bryce normal with dissolve
        # Maybe another scene, or another writer, can spread these out.
        # But I don't want to write two versions of four more ways of fucking his feet rn.
        # label bangok_four_bryce2_footjob_f_menu:
        #     menu:
        #         "Rub his sole over your crotch.":
        #         "Grind on his toe knuckles.":
        #         "Grind on the sides of his feet.":
        #         "Fuck his heel.":
        if bangok_four_bryce2_store.cumlube == True:
            m "I pressed his feet together, then pressed his soles to my mound, squeezing his cum between his feet and my wet, needy hole."
        else:
            m "I pressed his feet together, then pressed his soles to the slick slit between my legs, massaging my mound with his flat, scaly pads."
        m "His force back was minimal as I began to grind myelf lightly across his feet, seeking more stimulation."
        c "Making me do all the work?"
        Br laugh "I'd do more, but I don't want to kick you across the room on accident."
        Br smirk "Besides, it looks like you're having fun this way."
        jump todo_out_of_content_bangok_four_bryce2
    else:
        $ renpy.error ("Excuse the binary, but you must either have a penis or not have one.")

    Br laugh "Man, what a time."

    $ bryce2mood += 4
    show bryce:
        zoom 1.0
        xalign 0.5
    hide black
    with dissolvemed

    jump bangok_four_bryce2_canon_beer


label bangok_four_bryce2_worship:
    m "Bryce splayed his hindlegs, welcoming me in to his crotch."
    if bangok_four_bryce2_store.player_came:
        m "My juices glistened on his plates, around a horizontal slit where I could see a small pinkish tip peeking from inside him."
        m "Then one of his legs wrapped around the back of my head, the side of his foot pressing against my cheek as he pulled me face-first against that slit, rubbing my own juices in my face, and my nose and mouth against his tip."
        m "His other heel I could feel on my back, pulling me upward into his first hindleg's embrace."
        $ renpy.pause (0.5)
        m "Obediently I began to lap and lick, cleaning up my own juices while trying to entice more of his shaft from where his feet held me."
    else:
        m "At a horizontal slit between two of his belly plates, I could make out a small pinkish tip, just peeking out from inside him."
        m "Then one of his legs wrapped around the back of my head, the side of his foot pressing against my cheek as he pulled me face-first against that slit, rubbing my nose and mouth against his tip."
        m "His other heel I could feel on my back, pulling me upward into his first hindleg's embrace."
        $ renpy.pause (0.5)
        m "Obediently I began to lap and lick, trying to entice more of his shaft from where his feet held me."

    Br pantflirt "Nngh."

    m "More of his dragonhood emerged, rubbing up the side of my cheek as I kissed and suckled, licking my way around its base with my eyes closed, fully dominated by this larger creature's powerful legs."
    m "I felt his toes curl, one claw brushing my forehead."

    $ renpy.pause (0.5)
    Br smirk "Now that you've had both, which is better? My feet, or my cock?"
    menu:
        "Feet.":
            $ renpy.pause (0.5)
            Br flirty "Well, allow me to show you more of the latter."
        "Cock.":
            $ renpy.pause (0.5)
            Br laugh "Agreed, but you're showing me the fun I can have with the rest of me."
        "[[Moan.]":
            $ renpy.pause (0.5)
            m "I moaned into Bryce's crotch, and he let out another guffaw."
            Br laugh "Bit of both, then?"

    $ renpy.pause (0.5)
    Br smirk "I wasn't really sure my legs could even hold you like this."
    m "His foot rubbed into my face, and heel into my back, as he tugged me up his shaft. Thick dragonflesh rubbed past my face as he brought my lips near to his tip."
    m "Then his forepaws came down around my head, tugging me the last little distance to put his length just below my mouth, the rest rubbbing down my chest."
    m "It also put his forepaws within range of my eager tongue."
    menu:
        "Lick his feet.":
            $ renpy.pause (0.5)
            Br laugh "H-Hey!"
            Br smirk "Oh you like that, huh?"
            m "He rubbed his forepaws on my face."
            Br smirk "Get me off and I'll let you lick the cum from these."
        "Suckle on his cock.":
            pass

    $ renpy.pause (0.5)
    m "I took his tip into my mouth, tasting gloriously sweet drops of pre at the end of his draconic member, saturating my tongue with a different flavor thann the roughness of his hard scales, or the slick flesh of his length."
    m "I bobbed my head beneath his feet, rubbing his cock against my chest, eager for the result, to bring pleasure to the large dragon."

    Br pant "Ohhh. G-Getting close now."
    menu:
        "Let Bryce cream himself.":
            $ bangok_four_bryce2_store.bryce_came = "outside"
            m "Bryce felt me pull back from his tip, and brought his forepaws down from my head just in time to block the blast."
            play sound "fx/snarl.ogg"
            m "Cum splashed across his forepaws and belly, some spatters even reaching as far back as my face where I continued to lap at the base of his tip."
            if persistent.bangok_inflation == True:
                m "Spurt after spurt came out, until a white puddle was running down Bryce's belly toward the couch."
            m "Then the pulses came to an end and Bryce let up with his hindlegs."
        "Swallow.":
            $ bangok_four_bryce2_store.bryce_came = "inside"
            play sound "fx/snarl.ogg"
            m "Thick cum spattered the back of my mouth, then Bryce's hips bucked, trying to push his whole head into my mouth."
            m "At this angle, held in place by his gripping feet, it was a struggle to swallow."
            m "I sputtered as a second and third pulse filled my mouth, cum leaking from my lips, only to be caught by one of his forepaws."
            if persistent.bangok_inflation == True:
                m "I kept struggling to swallow, but the volume was so much, soon I felt a spurt escape my nose, my throat packed with Bryce's seed."
            m "Then the pulses came to an end, Bryce let up with his hindlegs, and I was able to fully swallow down what remained of his creamy accolade of my worship."

    Br pant "Haaa..."
    Br flirty "Left quite a mess on my forepaws."
    if bangok_four_bryce2_store.bryce_came == "outside":
        Br flirty "All over my belly, too."
    Br smirk "Gonna help clean that up?"

    menu:
        "[[Scoop some on your groin as lube.]" if bangok_four_bryce2_store.player_came == False:
            $ renpy.pause (0.5)
            $ bangok_four_bryce2_store.cumlube = True
            Br flirty "If you like my seed that much, maybe I should've just put this rod of mine inside you."
            c "But then I wouldn't get to play with these."
            Br smirk "Oh?"
            jump bangok_four_bryce2_footjob
        "[[Scoop some on his hindpaws as lube.]" if bangok_four_bryce2_store.player_came == False:
            $ renpy.pause (0.5)
            $ bangok_four_bryce2_store.cumlube = True
            Br laugh "What are you trying to do, make me leave a bunch of footprints under a UV light?"
            c "Nope. Just making these more fun to play with."
            Br smirk "Oh?"
            jump bangok_four_bryce2_footjob
        "[[Help lick it up.]":
            $ renpy.pause (0.5)
            if bangok_four_bryce2_store.bryce_came == "outside":
                if persistent.bangok_inflation == True:
                    m "I caught the puddle on Bryce's belly before it could dribble down to the ccouch, collecting with a hand until I could get my face in position to start licking up his cum."
                    m "Bryce's belly plates moved beneath my lapping tongue as he lay back and enjoyed my work, while his sticky forepaws awaited my ministrations."
                    m "Finished enough with his belly I didn't think what was left would run anywhere, I took Bryce's front feet and held them next to each other, lapping up with my already cream-covered tongue."
                else:
                    m "I took Bryce's sticky front feet and held them next to each other, lapping up the thick ropes of white."
            else:
                if persistent.bangok_inflation == True:
                    m "Holding bryce's sticky front feet next to each other, I licked slowly at the thick ropes of white, finding it difficult to swallow too much, as I already felt full from the main course."
                else:
                    m "Holding bryce's sticky front feet next to each other, I lapped up what I'd spilled, cleaning the pads of his feet of his mess."
            m "When I finished, the flat, scaly pads of Bryce's forepaws had a glistening, polished shine."
            Br laugh "If only I could get you to tongue-bath all of me like that."

            $ bangok_four_bryce2_store.bryce_came = "cleaned"
        "Sorry, Bryce. I don't know if I can help with that.":
            $ renpy.pause (0.5)
            Br laugh "Ah, heck it. Worth a shot to see you using that mouth of yours on me some more."
            m "Bringing his forepaws up to his maw, Bryce licked up his own ejaculate, making quick work of what might've taken me several minutes."
            if bangok_four_bryce2_store.bryce_came == "outside":
                m "Then he curled forward, doing the same for what had landed on his belly plates, though he missed many more spots, and it was too late to stop some from dripping into the couch."

            $ bangok_four_bryce2_store.bryce_came = "cleaned"

    if bangok_four_bryce2_store.player_came == False:
        Br smirk "Guess now it's time for me to give you a hand. Or foot. Or feet."
        menu:
            "Yep.":
                $ renpy.pause (0.5)
                jump bangok_four_bryce2_footjob
            "Actually, I think I'm good.":
                $ renpy.pause (0.5)
                Br laugh "\"Good\" is definitely how I'd describe you."
                Br brow "You, ah, don't regret that though, right?"
                c "Not at all. Just... not looking for reciprocation."
                Br normal "Alright. Whatever makes you happy."
    else:
        Br laugh "Man, what a time."

    $ bryce2mood += 4
    show bryce:
        zoom 1.0
        xalign 0.5
    hide black
    with dissolvemed

    jump bangok_four_bryce2_canon_beer


label bangok_four_bryce2_show_bryce_no_tail:
    m "I turned around, showing Bryce the lack of appendage."
    Br laugh "I don't believe it. How did I not see that a few minutes ago?"
    c "I was distracting you a bit."
    Br smirk "A bit, I guess."
    Br brow "There was also all that stuff you were wearing. Why do you cover it all up, anyway?"
    c "It's a human thing. We usually don't show our bodies to strangers."
    Br normal "So, friends are fine?"
    c "That would be an unusual friendship. Let's just say that displaying that area usually implies... what we did."
    Br flirty "Is that so?"
    $ bryce2mood += 1
    jump bangok_four_bryce2_show_bryce_no_tail_end

label bangok_four_bryce2_talking_otherthings:
    Br flirty "... and other things."
    jump bangok_four_bryce2_talking_otherthings_return


label todo_out_of_content_bangok_four_bryce2:
    play sound "fx/system3.wav"
    s "Out of content. Roll back or prepare to crash."
    $ renpy.error("Out of content.")