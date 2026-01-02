init python in bangok_four_remy4_store:
    path = None # type: Optional[Literal["tongue","vaginal","anal"]]

    inside_asked = False # type: bool

    protection = False # type: bool

    player_finished = False # type: bool
    remy_finished = False # type: bool
    remy_pissed = False # type: bool

# == No more tongue path ==
# Remy is on his back on the couch
# (Optional) Handjob Remy's shaft (no climax -- he asks for more and/or to satisfy you)
# (Optional) Lick Remy's shaft (no climax -- he asks for more and/or to satisfy you)
# (Optional) Frotting / Hotdogging (+climax jump over fuckings)
#  -> male assfuck
#  -> female vaginal receive
#  -> both anal receive
# Merge: Collapse on the couch in each others' arms

# == More Tongue path ==
#  -> male unprotected
#  -> male protected (TODO, just add a hint of player condom to unprotected and rewrite)
#  -> female
# Merge: kiss, compliment, taste
# if remy_finished: Conclude. Else: Remy's Rear

# == Remy's Rear == Remy turns around for the player to explore his other end
# (Optional) Rimjob (TODO: Need a contributor for this)
# (Optional) Sheath licking (+climax jump over fuckings)
#   -> male, fuck Remy's ass
#   -> both, handjob Remy while rimming
#   -> both, handjob Remy while sheath licking
#   -> female, another intro to getting fucked
#   -> both, another intro to anal getting fucked
# Merge: Splay out on the floor after completion, both on your back
# Remy decides he doesn't want to go home that night (but leaves before you get up to get to work for the day.)

label bangok_four_remy4_more:
    menu:
        "Ask if he wants to do more.":
            pass
        "Say something else.":
            $ renpy.pause (0.5)
            jump bangok_four_remy4_more_return
    c "Is this... all that happens?"
    Ry shy b "What do you mean?"
    c "Do you want to keep going?"
    Ry shy b "I..."
    if (bangok_four_common.bangnokay.check()):
        Ry shy b "More kissing? There is a certain novelty, but I'm not sure how many times we'll be able to explore that in one sitting."
        c "What? No, like..."
        m "I stared at Remy, not sure how the intelligent dragon could be so dense on this topic."
        c "Do you want to have sex?"
        show remy look b with dissolve
        m "To my confusion, Remy's face fell, sharply."
        Ry "[player_name], this is... only our third date, and we're different species. I'm certainly not ready for that yet."
        Ry "It would also be very improper given your position as ambassador and mine as liaison."
        c "Oh, well, I didn't mean--"
        Ry shy b "While I'm not... writing off the possibility, I think we should at least wait until the Reza situation is resolved."
        c "Okay, I understand."
        show remy look b with dissolve
        $ renpy.pause (1.0)
        m "He gave me another hard look, as if to make sure I understood, before speaking again."
        jump bangok_four_remy4_canon_shouldprobablygo
    m "I couldn't tell if it was my heartbeat or his I was hearing as he deliberated."
    $ renpy.pause (0.8)
    show remyrom at Pan((350, 326), (350, 320), 2.0) with fade
    $ renpy.pause (1.0)
    m "Then he leaned in to kiss me again."
    show black with dissolvemed
    $ renpy.pause (0.5)
    m "He leaned in more than last time, pressing me a little against the armrest of the couch, but still holding back, hesitant."
    $ renpy.pause (0.5)
    hide black
    hide remyrom
    with dissolveslow
    $ renpy.pause (0.5)
    m "Then he pulled away."
    Ry shy b "I'm sorry... I haven't thought about doing this with anyone I've met since..."
    show remy look b with dissolve
    m "He looked over at his tie, then shook his head."
    Ry normal b "No. I'm here now, and it would be selfish of me to push you away because I want to keep living in the past."
    c "I don't mind waiting, if that's what you need."
    Ry smile b "It really doesn't take much for you to try to make me happy, does it?"
    c "Not when it means making sure you feel comfortable."
    Ry normal b "It's okay. I want this too. I want... us."
    menu:
        "Accept.":
            pass
        "Give him space.":
            m "I sighed, trying to let go of my own hopes and worked-up energy as I put Remy's mental health first."
            c "Remy... I understand if you don't feel comfortable with that right now. It's okay..."
            show remy look b with dissolve
            m "He looked at me, his eyes growing newfound disappointment and worry."
            c "No, it's not because of that... Well, maybe a little bit, but mostly I just don't want to rush into something like this and hurt you."
            c "I pushed you too far asking for more after our kiss. I'm sorry."
            $ renpy.pause (0.8)
            Ry shy b "It's okay. You didn't push me at all. I'm just... maybe I'm not as ready as I thought I was, that's all."
            c "Put today on pause?"
            Ry smile b "That sounds like a good idea."
            c "Sure thing."
            jump bangok_four_remy4_canon_shouldprobablygo
        "Reject.":
            stop music fadeout 2.0
            m "I grimaced, frustrated that he was again bringing up his dead girlfriend, even after our day had been all about him recovering from her."
            Ry shy b "[player_name]?"
            c "I don't know if I can keep going like this. You're still holding on to her memory too tightly."
            Ry sad b "It's not that simple..."
            m "I stood up, my frustration and disappointment evident in my voice."
            c "Then maybe it's best we just stop now. I like you, but I don't want to be a substitute for someone who isn't even here anymore. Was kissing me right there just reminding you of her?"
            $ remystatus = "bad"
            Ry sad b "[player_name]... Please."
            hide remy with dissolve
            m "I turned away from him, unable to look at the pain in his eyes at my words."
            c "Just... give me some space. Come back when you're ready to really let go of her memory and focus on us."
            play sound "fx/undress.ogg"
            m "I heard him putting his tie back on, despite my request, then start toward the door, only moving partway before speaking."
            show remy sad b with dissolve
            Ry "... the fireworks?"
            c "Call me if you get out of this funk."
            hide remy with dissolve
            $ renpy.pause (0.5)
            play sound "fx/door/doorclose3.ogg"
            m "I closed the door after he left, then slumped against the inside and slid to a sitting position on the floor, finally letting my emotions overcome me."
            $ renpy.pause (2.0)
            $ remystatus = "bad"
            $ remyscenesfinished = 4
            jump _mod_fixjmp


    play sound "fx/kiss.wav"
    show remy shy b with dissolve
    m "I took the lead this time, hugging his neck and planting a kiss right on the tip of his snout, eliciting a beautiful blush that reached his ears."
    Ry "I-I don't know how far you plan on taking this. As a dragon, I'm a little bit larger than you are..."
    c "We'll make something work."
    Ry smile b "Well, if it's what you want, let's try something simple for now."
    Ry normal b "I'm not sure how far we can go with your clothes on you..."
    c "Let me take care of that."
    play sound "fx/undress.ogg"
    $ renpy.pause (1.0)
    m "I cautiously stripped, trying not to frighten him with how different my human body was from his draconic scales."
    Ry smile b "You're... perfect."
    Ry shy b "We could start by just... cuddling? Getting used to the feel of our bodies against each other like this?"
    c "That sounds wonderful."
    hide remy with dissolve
    m "Remy shifted onto his back on the couch, spreading his wings and four limbs out to accept me."
    m "Between his hindlegs, I could see the tip of something pink just peeking out. But for now, I focused on climbing onto his chest without hurting him or myself as I hugged just above his forelegs."
    show bangok_grey with dissolvemed
    play soundloop "fx/breathing.ogg" fadein 10.0
    m "As soon as I was safely nestled in a hug between his forelegs, he wrapped his wings around us both like a cocoon and pulled me even closer against his underbelly scales."
    Ry normal b "Is this okay? If it's too much..."
    c "It's perfect. Just... like this."
    $ renpy.pause (0.8)
    m "We lingered there for some time, his breathing and our heartbeats the only sounds as he gently nuzzled his snout against my head beneath his wings."
    m "His heat suffused the space, and slowly I began to feel my own body warm, my heart beating faster."
    if bangok_four_playerhasdick is None:
        m "Between my legs, I felt..."
        menu:
            m "Between my legs, I felt...{fast}"
            "My hardness.":
                $ bangok_four_playerhasdick = True
            "My wetness.":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick:
        m "Between my legs, I felt my hardness becoming difficult to ignore as I couldn't find a position it didn't press against his belly scales."
    else:
        m "Between my legs, I felt my wetness becoming difficult to ignore the heat in my crotch grew."
    m "Remy seemed to notice the way my breathing was changing and started to nuzzle more insistently at my neck."
    m "His warm tongue traced lazy patterns along the exposed skin, sending shivers down my spine."
    menu:
        "More of that, please...":
            $ renpy.pause (0.5)
            Ry shy b "More of...?"
            m "Lifting my head, I caught his chin with one hand and our lips met for another kiss."
            c "More tongue. Lower."
            Ry smile b "I'll do my best."
            $ bangok_four_remy4_store.path = "tongue"
        "Ready to move on?":
            $ renpy.pause (0.5)
            m "Remy nodded, eyes bright with anticipation and nerves."
            c "Then let's try something."
        "[[Say nothing.]":
            m "I couldn't help but let out a soft moan as he continued his teasing assault. His tail began to wag gently against the couch."
            Ry normal b "Do you want me to...?"
            c "Please..."
            Ry shy b "Are you sure? I don't--"
            m "I pulled away from his snout and looked him in the eyes, my own filled with desire."
            c "Yes."
            # TODO: Someday, maybe make this start tailplay

    play sound "fx/undress.ogg"
    hide bangok_grey with dissolve
    if bangok_four_remy4_store.path == "tongue":
        m "Remy unfolded his wings, allowing me to slip off of him, to examine what I'd be working with between his legs when we got back to him."
    elif bangok_four_remy4_store.path is None:
        m "Remy unfolded his wings, allowing me to slip off of him, to examine what I'd be working with between his legs."
    show remy shy b with dissolve
    if persistent.bangok_balls == True:
        m "A large, pinkish shaft glinted in the light of the room, its head already dribbling a droplet of thick, clear fluid. His balls were also quite large and plump, hanging low beneath it."
    else:
        m "A large, pinkish shaft glinted in the light of the room, its head already dribbling a droplet of thick, clear fluid."
    Ry shy b "You're... so beautiful like this."
    c "As are you."
    menu:
        "Ask about protection.":
            $ bangok_four_remy4_store.protection = True
            m "Before we could get too distracted by each other's bodies, I managed to push through a thought about protection."
            c "Er, we should probably put on protection..."
            Ry normal b "Differing dragon species cannot get one another pregnant, and I assume the same would extend to humans. Not that such is a concern between us. But if you would feel more comfortable with it, then I'll go get some."
            c "I think that might be a good idea... just in case."
            hide remy with dissolve
            c "Wait, you're not going to the store to get it, are you?"
            Ry normal b "No. There's some in your bathroom. One moment."
            show remy normal b with dissolve
            if bangok_four_playerhasdick == True:
                m "When Remy returned, he was carrying an alarmingly large bottle of lube in his mouth and pushing two boxes of condoms in front of him with his forepaws."
            else:
                m "When Remy returned, he was carrying an alarmingly large bottle of lube in his mouth and pushing a box of condoms in front of him with his forepaws."
            Ry "Now, where were we?"
        "Continue.":
            $ renpy.pause (0.5)

    if bangok_four_remy4_store.path == "tongue":
        if bangok_four_playerhasdick == True:
                jump bangok_four_remy4_male_tongue_path
        else:
            jump bangok_four_remy4_female_tongue_path

    m "I moved a little closer to Remy's hindquarters, spreading his legs a little wider to give me better access to his groin."
    if bangok_four_remy4_store.protection == True:
        m "Then, taking one of the large condoms from the box, I carefully unrolled it over his shaft, making sure it was secure."
    menu:
        "Pleasure him with your hands.":
            jump bangok_four_remy4_top_handjob
        "Pleasure him with your mouth.":
            jump bangok_four_remy4_top_blowjob
        "Climb on top of him.":
            jump bangok_four_remy4_top_climb_atop

label bangok_four_remy4_top_handjob:
    jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_top_blowjob:
    jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_top_climb_atop:
    $ renpy.pause (0.5)
    show remy shy b with dissolve
    m "As I moved to climb onto the couch with him, straddling his tail, Remy blushed furiously."
    if bangok_four_remy4_store.protection == False:
        Ry "H-Hold on. We... if you're going to do anything, we'll need lube."
        c "Do we have any here?"
        m "His blush only seemed to deepen as he answered."
        Ry "In your bathroom, under the sink on the right."
        c "I'll go get it."
        scene black with dissolve
        $ renpy.pause (0.5)
        scene bath with dissolve
        $ renpy.pause (0.5)
        play sound "fx/box.wav"
        m "The bottle of lube was exactly where he'd said. It seemed surprisingly large, until I remembered the size of dragonhoods it may need to be serving."
        scene black with dissolve
        $ renpy.pause (0.5)
        scene o4 at Pan((0,220), (0,250), 1)
        show remy shy ud
        with dissolve
        m "I returned to the living room with the lube, finding Remy had placed his shirt collar and glasses on the coffee table, out of harm's way."
    else:
        # Protected should've already gotten the lube
        play sound "fx/undress.ogg"
        hide remy with dissolve
        $ renpy.pause (0.5)
        m "Twisting over, Remy set his glasses and shirt collar aside on the coffee table, out of harm's way."
        show remy shy ud with dissolve
    Ry shy ud "Okay."
    scene black with dissolve
    show bangok_four_remy4_cg top:
        zoom 1.6
        xalign 0.5
        yalign 0.0
    with dissolvemed
    m "I had to place my hands on Remy's belly to steady myself. He didn't seem quite sure what to do with his own forepaws as he blushed up at me, leaving them hanging in the air."

label angok_four_remy4_top_climb_atop_late:
    show bangok_four_remy4_cg top:
        yalign 0.0
        linear 2.0 yalign 1.0
        yalign 1.0
    with None
    if bangok_four_playerhasdick == True:
        m "I looked down to where my dick and balls hung over Remy's, deciding what to do next."
    elif bangok_four_playerhasdick == False:
        m "I looked down to where my puffy, ready crotch hung over Remy's relatively enormous dragonhood, deciding what to do next."
    menu:
        "I need you inside me." if bangok_four_remy4_store.inside_asked == False:
            $ bangok_four_remy4_store.inside_asked = True
            show bangok_four_remy4_cg top:
                yalign 1.0
                linear 8.0 yalign 0.0
                yalign 0.0
            with None
            $ renpy.pause (0.5)
            m "... Remy's face fell."
            Ry look ud "[player_name], I don't want to dissuade you, but..."
            Ry shy ud "I also don't want to hurt you."
            Ry look ud "Are you sure...?"
            menu:
                "My pussy wants to try." if bangok_four_playerhasdick == False:
                    $ bangok_four_remy4_store.path = "vaginal"
                "My ass wants to try." if bangok_four_playerhasdick == True:
                    $ bangok_four_remy4_store.path = "anal"
                "I... No, maybe I'm not sure.":
                    Ry shy ud "That's ok!"
                    Ry "J-just don't hurt yourself."
                    Ry "I'm sure there are other things we can do."
                    jump angok_four_remy4_top_climb_atop_late
            m "I picked up the bottle of lube from the coffee table."
            c "We'll use plenty of this and stop if it goes too far."
            $ renpy.pause (0.5)
            Ry look ud "Okay..."
            $ renpy.pause (0.5)
            Ry shy ud "Then I want you to try, too."
            jump angok_four_remy4_atop_inside
        "Start with rubbing?":
            $ renpy.pause (0.5)
            Ry shy ud "S-sure."
            jump todo_out_of_content_bangok_four_remy4
        "Would you want me in your ass?" if bangok_four_playerhasdick == True:
            $ renpy.pause (0.5)
            m "Remy squirmed momentarily, as if unsure of his own feelings."
            m "Then, blushing, he nodded."
            Ry shy ud "I... wouldn't mind that."
            jump todo_out_of_content_bangok_four_remy4
        "Ask Remy to turn over.":
            jump todo_out_of_content_bangok_four_remy4

label angok_four_remy4_atop_inside:
    show bangok_four_remy4_cg top:
        yalign 0.0
        linear 2.0 yalign 1.0
        yalign 1.0
    with None
    if bangok_four_remy4_store.protection == True:
        m "I worked my way back on the couch a short way, squirting gobs of additional lube onto Remy's condom-wrapped shaft as I went."
    else:
        m "I worked my way back on the couch a short way, squirting gobs of lube onto Remy's shaft as I went."
    play soundloop "fx/massage.ogg" fadein 10.0
    show bangok_four_remy4_cg top:
        yalign 0.0
        linear 4.0 yalign 1.0
        yalign 1.0
    with None
    m "Then I set the bottle aside and began to rub it in, using both hands as I worked my way upward, back toward Remy's tip."
    m "He squirmed under the attention, panting heavily."
    stop soundloop fadeout 1.0
    m "I could feel his member twitching beneath my hands, growing harder and more insistent as I worked the cold lube in."
    if bangok_four_remy4_store.path == "vaginal":
        jump angok_four_remy4_atop_inside_vaginal
    else: # anal
        jump angok_four_remy4_atop_inside_anal

label angok_four_remy4_atop_inside_vaginal:
    m "I took my lube-slicked fingers and reached between my legs, smearing some of the lube into my wet, ready folds."
    m "My fingers slipped a little deeper and I tensed up, anticipating what was about to happen as spread lube around in my juices."
    m "Remy's lube-slicked member beneath me twitched against my lower belly, and I could feel the heat of his body between my legs."
    show bangok_four_remy4_cg top:
        zoom 1.6
        ease 0.5 zoom 2.0
        zoom 2.0
    with None
    m "Then, prepared, I moved that last bit forward onto his belly and picked up his tip, trying to align it with my ready, waiting hole."
    if bangok_four_remy4_store.protection == True:
        m "Despite all my preparation, I felt my folds pressed flat, stretched wide by just the tip of his condom-wrapped draconic cockhead."
    else:
        m "Despite all my preparation, I felt my folds pressed flat, stretched wide by just the tip of his draconic cockhead."
    m "He didn't seem to fit, feeling more like a fist pressed against my entrance rather than a penis."
    m "I squirmed, desperate to feel him inside me, but unable to push past the feeling of his tip sliding around in my outer folds and no deeper."
    Ry look ud "[player_name], I know you want to do this, but I'm so much larger than you are."
    Ry shy ud "Please be careful, and safe, and-- Ooooh..."
    m "I squeezed his cockhead just behind the tip, hard, pushing some more lube up toward his tip."
    show bangok_four_remy4_cg top:
        zoom 2.0
        ease 0.5 zoom 1.9
        zoom 1.9
    with None
    m "Then, with a gasp of effort, I pushed myself backward, finally managing to slip his slightly-squeezed tip into my tight, straining canal."
    show black with dissolveslow
    m "I closed my eyes. My outer folds stretched, his girth spreading me like no living being's ever before as I set my face down and just tried to adjust to having him inside."
    m "I didn't need to take any more of him to know there was zero chance I'd fit his entire length in my lifetime. My dragon lover was simply too large."
    hide black with dissolvemed
    m "Torn, I looked up into Remy's deep blue eyes. I wanted to give him this part of me, wanted us both to share our intimacy this way, but I simply wasn't sure how enjoyable I could make it if I was bottoming out partway."
    m "Remy's eyes held no judgement for my hesitation, just love, need, and concern."
    menu:
        "Give up.":
            jump todo_out_of_content_bangok_four_remy4
        "Keep going.":
            pass
    $ renpy.pause (0.5)
    m "During my hesitation, I found I'd clenched up too tightly to move."
    m "I found my voice, struggling not to sound like I was in any pain."
    c "Pass the lube?"
    show bangok_four_remy4_cg top:
        xalign 0.5
        linear 1.0 xalign 0.3
        xalign 0.3
    with None
    m "Remy did so, and I held it up behind myself."
    m "Blindly, I squirted some on my asscheeks, and on our coupling point, trying to make sure the way ahead was thoroughly lubed."
    play sound "fx/box.wav"
    show bangok_four_remy4_cg top:
        xalign 0.3,
        linear 0.5 xalign 0.5
        xalign 0.5
        zoom 1.9
        linear 4.0 zoom 1.5
        zoom 1.5
    with None
    m "Then I dropped the lube bottle, braced myself against Remy's belly, and pushed."
    c "Ohhhh..."
    Ry shy ud closed "Nnngh..."
    m "Slowly, my pussy began to slide and allow his girth through, my body almost beginning to relax as it realized the heights of pleasure this girth was about to bring me."
    m "Within a few moments he was deeper than my pelvis, and I moved my hand down to feel a bulge pushing its way up my belly toward my navel."
    Ry shy ud closed "Oh, [player_name]... [player_name]... You're so tight..."
    m "I made undignified gasps with every little bit of progress I made, stretching my love canal around him like a too-small glove."
    m "Then, abruptly, that fit stopped being so perfect."
    show bangok_four_remy4_cg top:
        yalign 0.0
        linear 0.5 yalign 1.0
        yalign 1.0
    with None
    c "F-Fuck!"
    m "I lay on Remy's belly wincing, my whole lower body smarting from Remy's contact with my cervix."
    Ry shy ud leye "Are you okay?"
    m "I rubbed my belly, feeling his girth inside me as, for a moment, I swooned."
    c "I... I will be okay."
    Ry look ud "That wasn't a very convincing answer."
    show black with dissolve
    m "I set my head against his belly as my lower muscles cramped."
    c "Still can't believe how big you are..."
    hide black
    show bangok_four_remy4_cg top:
        yalign 0.0
        linear 2.0 yalign 0.3
        yalign 0.3
    with dissolvemed
    Ry look ud "Then maybe we should st-- sto-- oooh..."
    Ry shy ud "Nnnngh..."
    m "I slid my way up his length a good distance, legs shuddering with exertion and ecstacy running through my lower body."
    c "Still think that?"
    show bangok_four_remy4_cg top:
        yalign 0.3
        linear 2.0 yalign 0.0
        linear 1.9 yalign 0.2
        linear 1.8 yalign 0.0
        linear 1.7 yalign 0.2
        linear 1.6 yalign 0.2
        linear 1.5 yalign 0.0
        linear 1.4 yalign 0.2
        linear 1.3 yalign 0.2
        linear 1.2 yalign 0.0
        linear 1.1 yalign 0.2
        linear 1.0 yalign 0.2
        linear 0.9 yalign 0.0
        linear 0.8 yalign 0.2
        linear 0.7 yalign 0.0
        block:
            linear 0.8 yalign 0.2
            linear 0.7 yalign 0.0
    with None
    Ry shy ud closed "Nnn.....noooooooh... Don't... stop..."
    m "As my taut lower lips slowly loosened, accepting their new fate, I gradually began to ride what of Remy, I could fit."
    m "I pressed on his belly for support, legs shuddering with every movement as I spread myself around his enormous member."
    if persistent.bangok_watersports == True:
        m "Remy winced as I gradually approached a rhythm."
        Ry shy ud leye "You're... pressing on my bladder..."
        menu:
            "[[Press elsewhere.]":
                pass
            "Then empty it in me.":
                $ renpy.pause (0.5)
                Ry shy ud "What?!"
                Ry shy ud "I don't..."
                m "Too lost in the throes of my own arousal to discuss it with him, I pressed a little harder, taking his length deep in me."
                c "Piss in me. Use me. F-Fuck Remy, I love you."
                Ry shy ud leye "I-- What?! No, I can't-- I mean, I wouldn't ask you to--"
                c "You wouldn't ask... but I want... I want you to."
                m "He lapsed into silence for a few moments, eyes closed, blushing furiously."
                Ry shy ud closed "... Nnn... okay..."
                m "I felt his muscles clench under my hands, his body shivering as he let his bladder go."
                m "A hot jet of Remy's piss rammed up inside me, splattering against my cervix. It burned like fire as it saturated my canal, defiling and marking me in the most intimate way possible."
                m "I shuddered and moaned unable to keep still around his cock. I felt it twitching inside me as its soiling stream of hot urine saturated every part of my pussy."
                if persistent.bangok_inflation == True:
                    m "But the flow didn't even slow down as the tiny space between his cock and my the end of my canal filled to capacity, his girth leaving it nowhere to go but deeper."
                    c "Oh f-fuck, that's so much... oh fuck."
                    m "Urine spurted through my cervix and flowed through my tubes. My womb filled, then swelled with Remy's piss, the pressure building within me as I sank a little lower onto him in blank ecstacy."
                    m "Heat suffused my body as my uterus bloated with his waste. My belly stretched to accommodate it, leaving me breathless until his urination slowly petered off."
                    m "Remy's eyes were wide open now as he looked down at me, and more specifically at my distended midriff I looked down at our bodies joined together and the mess he'd made of me."
                    c "Oh... oh fuck... I can't even..."
                    m "My eyes darted all around my belly. I felt hot, swollen and full in the most delightful way. I felt like Remy's personal toilet and it was amazing."
                    Ry shy ud "Are you okay? You look... [player_name] if you need to stop..."
                    m "I could feel his piss drowning my most intimate inner places, but it only made me want more. I wanted my uterus to be a slurry of Remy's waste and affection."
                    m "Slowly, clenching my muscles, I began to lift myself up Remy's cock despite my bulging stomach."
                    m "I began to ride on Remy again, feeling the head of his cock allow piss to seep out of my depths as he retreated before pushing it back into my womb like a piston as I sank back down."
                    m "Remy blushed, but his eyes were half lidded as I moved, showing he was enjoying the sensations just as much as I was."
                    c "Remy..."
                    m "I moved my hands a little further up his belly for support, slowly picking up the pace."
                    m "Gently and cautiously, he hugged me with his hindlegs, helping me along as we slowly fucked faster."
                    m "Urine began to seep out as my strokes became longer and faster, the smell of his waste finally hitting us both as we worked together."
                    Ry shy ud "You're... Oh [player_name]... I'm... You're..."
                    m "I could tell he was getting close as his hips shuddered, resisting thrusting up into me. I was close too."
                    m "Reaching down, I began to gently rub my clit against his immense girth sinking as low as I could take him."
                    m "He was so big inside me, filling me up in all the right places, stretching me to my blissful limit."
                    Ry shy ud closed "[player_name]... Oh [player_name]... I--"
                    m "He let out a muffled roar and squeezed me hard, then he tensed up, balls clenching, his body shuddering."
                    m "Thick hot ropes of cum shot deep within me as he came hard, spurting his hot seed into the end of my canal."
                    c "Remy!"
                    m "My orgasm hit, my pussy clenching what little it could around his girth. I came hard, taking him to my limit, squeezing his cum out into the limited space inside me."
                    m "Jets of seed pushed through my cervix from his twitching cock, injecting themselves into my wombful of piss as his fluids mixed in my body."
                    m "My swollen belly distended still further as he filled me with more and more of his thick load, forming a heavy slurry of wanton lust deep within my core."
                    m "But a painful cramp told me he'd gone too far..."




    jump todo_out_of_content_bangok_four_remy4

label angok_four_remy4_atop_inside_anal:
    m "I took my lube-slicked fingers and reached behind me, smearing some of the lube onto my own tight pucker."
    m "I could feel my body tensing up in anticipation as I worked the lube in."
    if bangok_four_playerhasdick == True:
        m "Remy's lube-slicked member was already pressing against my balls, and I could feel the heat of his body between my legs."
    else:
        m "Remy's lube-slicked member was already pressing against my mons, stimulating and slickening my clit as I prepared myself, and I could feel the heat of his body between my legs."
    show bangok_four_remy4_cg top:
        zoom 1.6
        ease 0.5 zoom 2.0
        zoom 2.0
    with None
    m "Then, prepared, I moved that last bit forward onto his belly and picked up his tip, trying to align it with my asshole."
    m "The head of his extremely well-lubed penis slipped out of my asscrack immediately, but I tried again, struggling to keep a grip on it to line up."
    m "Remy huffed hungrily, but peered over my back with some concern as he slipped out a second time."
    Ry normal ud "[player_name], maybe--"
    show bangok_four_remy4_cg top:
        zoom 2.0
        ease 0.5 zoom 1.9
        zoom 1.9
    with None
    if bangok_four_remy4_store.protection == True:
        m "With a gasp of effort, I pushed myself backward, finally managing to push my sphincter around just the tip of his condom-wrapped draconic cockhead."
    else:
        m "With a gasp of effort, I pushed myself backward, finally managing to push my sphincter around just the tip of his draconic cockhead."
    Ry shy ud closed "Ooooh..."
    m "My ass strained, his girth pushing me like no living being's ever before as I tried to take just another inch into me."
    m "I finally stopped to gasp for breath when his entire tip was inside, weighing whether it was safe to take this any further."
    m "If it wasn't, it surely meant giving up, because there was no chance my ass would allow this kind of stretching in a repetitive motion like fucking if he wasn't deeper."
    m "Remy looked at me with his deep blue eyes, love and need etched on his features."
    menu:
        "Give up.":
            jump todo_out_of_content_bangok_four_remy4
        "Keep going.":
            pass
    show bangok_four_remy4_cg top:
        xalign 0.5
        linear 1.0 xalign 0.3
        xalign 0.3
    with None
    m "Careful not to undo the progress I'd made, I shifted over to grab the lube bottle."
    m "Blindly, I squirted some on my asscheeks, and on our coupling point, trying to make sure the way ahead was thoroughly lubed."
    play sound "fx/box.wav"
    show bangok_four_remy4_cg top:
        xalign 0.3,
        linear 0.5 xalign 0.5
        xalign 0.5
        zoom 1.9
        linear 4.0 zoom 1.5
        zoom 1.5
    with None
    m "Then I dropped the lube bottle, braced myself against Remy's belly, and pushed."
    c "Ohhhh..."
    Ry shy ud closed "Nnngh..."
    m "Slowly, my sphincter began to slide and allow his girth through, my body tensing up as I tried to relax and take him in."
    m "I could feel a discomforting stretch in my lower belly as his tip finally pushed into my colon, but as I gently eased past it, the discomfort faded into a dull ache."
    m "Remy's member was so large, so hot, so insistent, that I couldn't help but gasp and groan as I pushed it deeper into me."
    Ry shy ud closed "Oh, [player_name]... You're so tight..."
    m "I could feel his member twitching and throbbing inside me, his heat suffusing my insides as I tried to adjust to the feeling of him filling me up."
    m "Remy's eyes were closed, his mouth open in a silent gasp of pleasure as he tried to hold back his own reactions."
    if bangok_four_playerhasdick == True:
        m "Then, finally, I felt my balls ghost over his scaly slit and, with a final grunt of effort, I pushed myself down into his lap."
    else:
        m "Then, finally, I felt my mons ghost over his scaly belly and, with a final grunt of effort, I pushed myself down into his lap."
    if persistent.bangok_balls == True:
        m "Remy's member was fully inside me, his balls pressed into my asscheeks as I sat down on his lap."
    m "Looking down, I realized with some alarm that I could see the faint outline of his member through my skin, the tip of it pressing against my belly from the inside."
    show bangok_four_remy4_cg top:
        yalign 1.0
        linear 1.0 yalign 0.0
        yalign 0.0
    with None
    m "But, raising my eyes to meet his, the expression of ecstacy, love, and need in his eyes was enough to make me forget any discomfort."
    Ry shy ud "Y-You did it..."
    c "It's a tight fit..."
    m "I took a moment more to catch my breath, rubbing his belly scales with my hands as I tried to adjust to the feeling of him inside me."
    c "But it feels amazing."
    m "Slowly, so as not to hurt myself, I began to rise and fall a short distance on his member, feeling his girth stretch me open and fill me up with every motion."
    show bangok_four_remy4_cg top:
        yalign 0.0
        linear 3.0 yalign 0.2
        linear 3.0 yalign 0.1
        linear 2.8 yalign 0.3
        linear 2.8 yalign 0.2
        linear 2.6 yalign 0.4
        linear 2.6 yalign 0.3
        linear 2.4 yalign 0.5
        linear 2.4 yalign 0.4
        linear 2.2 yalign 0.6
        linear 2.2 yalign 0.5
        linear 2.0 yalign 0.7
        linear 2.0 yalign 0.6
        linear 1.8 yalign 0.8
        linear 1.8 yalign 0.7
        linear 1.6 yalign 0.9
        linear 1.6 yalign 0.8
        linear 1.4 yalign 1.0
        linear 1.4 yalign 0.9
        linear 1.2 yalign 1.0
        linear 1.2 yalign 0.9
        block:
            linear 1.0 yalign 1.0
            linear 1.0 yalign 0.9
            repeat
    with None
    $ renpy.pause (2.0)
    m "Remy's eyes fluttered shut as I began to ride him, his breath coming in ragged gasps as he tried to hold back his own climax."
    m "His hips began to rock in time with my own, his member throbbing and twitching inside me as I tried to keep my own body from tensing up too much."
    m "My body was filled with the heat of his member, the stretch of his girth, and the pleasure of his insistent thrusts."
    Ry shy ud "Oh, [player_name]... [player_name]..."
    if bangok_four_playerhasdick == True and bangok_four_remy4_store.protection == True:
        m "As my own member rubbed against his scaly belly through my condom, and his enormous dragonhood ground against something deep inside me, I couldn't help but groan with need."
    elif bangok_four_playerhasdick == True:
        m "As my own member rubbed against his scaly belly, and his enormous dragonhood ground against something deep inside me, I couldn't help but groan with need."
    else:
        m "My nerves were alight with the pleasure of his member filling my insides, to the point I didn't even need to touch myself to feel the pleasure building."
        m "I groaned with need, trying to keep myself from rubbing my clit against his belly scales as I rode him."
    $ renpy.pause (0.5)
    c "Remy..."
    Ry shy ud leye "[player_name], I...!"
    m "His hips stilled as his body tensed, leaving only my tiring body to do the work."
    m "I could feel him holding back, resisting growing urges as he gripped the couch armrest behind him with his forepaws."
    menu:
        "I've got you. Let me make you cum.":
            m "Remy let out a wordless sound somewhere between a whine of desire and a sigh of relief."
            m "I forced myself to keep up the pace, the lube squelching wetly between us in my happy abandon."
            if persistent.bangok_balls == True:
                m "Then I felt a change in Remy: a tensing of his muscles, a clenching in his balls and a new throbbing in his shaft."
            else:
                m "Then I felt a change in Remy: a tensing of his muscles and a new throbbing in his shaft."
            m "I sank down to hilt Remy within me, almost losing myself again in the sensation of his member pressing against my belly from the inside."
            Ry shy ud closed "Oh, [player_name]..."
            if bangok_four_remy4_store.protection == True:
                m "With that final croon, I felt the first hot gob of cum spurt into the condom deep inside me, the gathering heat of his climax growing safely in the condom reservoir inside me."
            else:
                m "With that final croon, I felt the first hot gob of cum spurt deep inside me, suffusing me with the heat of his climax."
            show white with dissolve
            if bangok_four_playerhasdick == True:
                if bangok_four_remy4_store.protection == True:
                    m "Mindless with pleasure, I stroked myself a few short times, then came into my condom as well, joining Remy in twitching, spurting climax."
                else:
                    m "Mindless with pleasure, I stroked myself a few short times, then came all over our bellies, joining Remy in twitching, spurting climax."
            else:
                m "Mindless with pleasure, I slipped my fingers into my folds and came all over our bellies, joining Remy in twitching, spurting climax."
            hide white with dissolveslow
        "Don't hold back. Take me. Harder.":
            Ry shy ud closed "I-I don't want to hurt--"
            c "Please... I... I want...!"
            m "I begged, nearing a peak of my own."
            show bangok_four_remy4_cg top:
                linear 1.0 yalign 0.0
            with None
            m "Growling, Remy put his forepaws on my shoulders, stopping me with his dragonhood buried to the hilt in my backdoor.{w} He tensed his tail."
            show bangok_four_remy4_cg top:
                linear 0.4 yalign 0.1
                linear 0.7 yalign 0.0
                repeat
            with None
            m "Then he began to buck his hips, his member throbbing and twitching inside me as he tried to hold back his own climax through the pleasure of taking my body."
            m "Wet slaps filled the room of his hips against my rear. I couldn't help but moan at the sensations he was causing as my guts twisted around the thick shaft of his cock."
            m "I gasped, shuddering through each hard shove."
            show white with dissolve
            if bangok_four_playerhasdick == True:
                if bangok_four_remy4_store.protection == True:
                    m "Then I was cumming hard into my condom, unable to hold back any longer the clenching in my balls and the twitches and spurts of my exposed member as they slapped into his lower belly with every hard thrust."
                else:
                    m "Then I was cumming all over our bellies, unable to hold back any longer the clenching in my balls and the twitches and spurts of my exposed member as they slapped into his lower belly with every hard thrust."
            else:
                m "Then I was cumming all over our bellies, my labia slapping wetly against his lower belly with every hard thrust."
            show bangok_four_remy4_cg top:
                yalign 0.0
            with None
            Ry shy ud "[player_name]!"
            hide white with dissolve
            m "I came down from my climax right into the beginning of Remy's."
            if persistent.bangok_balls == True:
                m "He held me in place, throbbing cock hilted in my guts as his balls clenched against my ass and a shudder ran through his body."
            else:
                m "He held me in place, throbbing cock hilted in my guts as a shudder ran through his body."
            m "Then the base of his dragonhood pulsed, stretching my abused sphincter before his tip spurt the first hot stream of seed deep inside my body."
    if bangok_four_remy4_store.protection == True:
        m "I put a hand on my belly, panting happily as I felt the slight bulge of his tip and the warm spurts as he filled his condom inside me."
    else:
        m "I put a hand on my belly, panting happily as I felt the slight bulge of his tip and the warm spurts it was coating my insides with."
    if persistent.bangok_inflation == True:
        m "Only, as I felt my intestines growing hotter and heavier with seed, I realized that our size difference could have more consequences than the tight fit of his member."
        if bangok_four_remy4_store.protection == True:
            m "He kept cumming, the condom stretching painfully further through my colon as his seed was left with no alternative."
        else:
            m "He kept cumming, his seed unable to escape around his thick shaft stretching my sphincter taut."
        c "Remy!"
        m "My guts gurgled, my belly stretching slowly with Remy's enormous dragonload."
        if bangok_four_remy4_store.protection == True:
            m "Then, to my shock, I felt a popping sensation deep inside me. Thick, heavy wetness flooded my guts as the condom tore open."
            m "Remy's cum gushed through my intestines unprotected, the force leaving me gasping and gripping my belly as my belly had to deal with the pressure alone."
        m "I strained, feeling my insides stretched to my limits to contain Remy's love and affection spilled into me."
        if persistent.bangok_balls == True:
            m "But, thankfully his balls finally relaxed against my rear and his member stopped pulsing inside me."
        else:
            m "But, thankfully as his member finally stopped pulsing inside me."
        Ry shy ud "O-Oh no. I couldn't-- Are you okay?"
        if bangok_four_remy4_store.protection == True:
            c "The condom..."
        m "I held my swollen belly, wobbling every breath as the thick, creamy dragon cum settled and pooled inside me."
        if bangok_four_remy4_store.protection == True:
            m "I felt the condom slowly deflate, the weight of Remy's seed inside me slowly shifting and settling."
            Ry shy ud "I-It was a little past expiry, and I know I'm large but I didn't think..."
            Ry shy ud "Are you okay?"
        menu:
            "I think I'm going to be sick.":
                m "Remy's face fell, so I expanded on what I meant immediately."
                c "Remy, I love you, but I think I took that too far."
                m "My intestines cramped around the heavy weight of his seed, causing me to wretch and gasp through the pain of being stretched so far with so much cum inside of me."
            "I'm fine. Just... full.":
                m "Remy put a forepaw on my belly, feeling the weight of his seed inside me."
                Ry normal ud "Very full. And beautiful."
                m "I smiled at him, then winced as my intestines cramped around the heavy weight of his seed."
            "This feels amazing.":
                m "I guided Remy's scaly forepaws to my belly, placing my hands over his while letting him feel and massage my stuffed insides through the taut skin of my abdomen."
                Ry normal ud "So tight and warm and full... You're so beautiful."
                Ry shy ud "It felt so good that I can barely think right now. Are you sure you're okay?"
                m "I exhaled shakily as he slowly moved his forepaws up and down my belly in circular motions, massaging and squeezing the weight of his cum deep in my guts."
                m "Then my intestines cramped around the heavy weight of his seed and I winced, only steadying myself by leaning on his forepaws."
        c "Ow. H-Hold on."
        if persistent.bangok_knot == True:
            m "I tried to stand, to get off of him and get some relief, but my sphincter abruptly met resistance it couldn't stretch around."
            m "A thick knot had formed at the base of his shaft, locking us together and sealing his seed inside me."
            m "I groaned, the attempted movement causing my belly to gurgle and churn with the weight of his seed moving around his shaft."
        else:
            m "I tried to stand, to get off of him and get some relief, but my belly was too heavy and I sank the tiny distance I'd made back down his shaft, groaning as it churned my already full guts."
    else:
        if bangok_four_remy4_store.protection == True:
            m "He came far more than any human could, leaving a warm, heavy bubble deep inside me around the thick shaft of his dragonhood, all contained within the walls of the rubber."
            m "I could feel his member twitching and throbbing inside me, his heat suffusing my insides."
            m "Then his climax gradually, finally, began to subside, leaving me with the warmth of his love and affection deep inside me."
        else:
            m "He came far more than any human could, leaving a warm, seeping feeling deep inside me around the thick shaft of his dragonhood."
            m "I could feel his member twitching and throbbing inside me, his heat suffusing my insides."
            m "Then his climax gradually, finally, began to subside, leaving me with the warmth of his love and affection deep inside me."
        m "I caught him blushing furiously as he looked down at our coupling point, then back up at me."
        Ry shy ud "Was that... okay? I didn't hurt you, did I?"
        menu:
            "I'm fine. That was amazing.":
                pass
            "You were perfect.":
                pass
        m "I smiled at him, then winced as my intestines cramped around the thick heft of his shaft, still buried deep inside me."
        c "Ow. H-Hold on."
        if persistent.bangok_knot == True:
            m "I tried to stand, to get off of him and get some relief, but my sphincter abruptly met resistance it couldn't stretch around."
            m "A thick knot had formed at the base of his shaft, locking us together."
            m "I groaned, the attempted movement reminding my body of the size of cock I'd just taken."
        else:
            m "I tried to stand, to get off of him and get some relief, but after all my exertions and my world-shaking orgasm, my legs were simply too tired to lift me."
            m "I groaned, sinking back down his shaft the short distance I'd managed to move, feeling my insides complaining about the size of cock I'd just taken, now sliding through me again."
    c "I... don't think I can move for a bit."
    Ry shy ud "Oh. S-Sorry. I--"
    if persistent.bangok_inflation == True:
        m "Carefully, I leaned forward, laying my heavy belly down against his belly scales."
        m "Then, when I was mostly laying down, I wrapped my arms around his neck in a tight embrace."
    else:
        m "I leaned forward, laying down on his belly as I wrapped my arms around his neck in a tight embrace."
    c "You have nothing to be sorry for."
    $ renpy.pause (1.0)
    Ry shy ud "..."
    if persistent.bangok_watersports == True:
        jump angok_four_remy4_atop_inside_anal_ws_choice
    else:
        jump angok_four_remy4_atop_inside_anal_ending

label angok_four_remy4_atop_inside_anal_ws_choice:
    m "Despite my words, the silence felt decidedly tense from his side. I raised my head, giving him an inquisitive look."
    Ry look ud "Is this a bad moment to realize I haven't used the bathroom since before arriving today?"
    Ry shy ud "And you're lying on my bladder."
    m "I blushed too, realizing that with his length stuck inside me, there was just one place he could urinate."
    menu:
        "Can you hold it?":
            m "Remy's eyes widened, then he nodded."
            Ry shy ud "I'll try."
            jump angok_four_remy4_atop_inside_anal_ending
        "That is the hottest and most ill-timed thing I've ever heard you say." if persistent.bangok_inflation == True:
            $ renpy.pause (0.7)
            Ry shy ud "Hot?!"
            m "I chuckled, then winced as my belly cramped again around the weight of his seed."
            c "Remy, I would be honored to be your urinal. I'm just... already so full."
            Ry shy ud "I-- What?! No, I can't-- I mean, I wouldn't ask you to--"
            m "He lapsed into silence for a few moments, blushing furiously."
            Ry shy ud "Can you take it?"
            m "He rubbed my bulging belly with a forepaw."
            menu:
                "I'll try. Go ahead. Piss in me.":
                    pass
                "I can't. It'd be too much. Can you hold it?":
                    m "Remy's eyes widened, then he nodded."
                    Ry shy ud "I'll try."
                    jump angok_four_remy4_atop_inside_anal_ending
        "Okay, go ahead. I can take it." :
            $ renpy.pause (0.5)
            if persistent.bangok_inflation == True:
                Ry shy ud "I-I can't believe you're saying this. You're already so full. And what I'm asking you to do..."
            else:
                Ry shy ud "I-I can't believe you're saying this. I'm so embarrassed."
            menu:
                "I'd be honored to be your urinal.":
                    $ renpy.pause (0.5)
                "I'm not embarrassed." if persistent.bangok_inflation == False:
                    $ renpy.pause (0.5)
                "I wouldn't have said it if I didn't mean it.":
                    $ renpy.pause (0.5)
                "I want to feel you inside me in every way.":
                    $ renpy.pause (0.5)
                "If you've got to go, you've got to go.":
                    $ renpy.pause (0.5)
                "Okay, now I'm having second thoughts.":
                    Ry shy ud "I'm sorry. I shouldn't have asked you to--"
                    Ry shy ud "I'll try to hold it."
                    jump angok_four_remy4_atop_inside_anal_ending
            Ry shy ud "No, I--"
            Ry shy ud "I--"
            m "He lapsed into silence for a few moments, blushing furiously."
        "I'd be honored to be your urinal.":
            $ renpy.pause (0.5)
            Ry shy ud "I-- What?! No, I can't-- I mean, I wouldn't ask you to--"
            m "He lapsed into silence for a few moments, blushing furiously."
            menu:
                "I love you Remy. Every part of you.":
                    $ renpy.pause (0.5)
                "I want to feel you inside me in every way.":
                    $ renpy.pause (0.5)
                "I wouldn't have said it if I didn't mean it.":
                    $ renpy.pause (0.5)
                "Let's find out how much my body can take." if persistent.bangok_inflation == True:
                    $ renpy.pause (0.5)
            Ry shy ud "I-I can't believe you're saying this. You're already so full. And what I'm asking you to do..."
            c "I want this, Remy."
            Ry shy ud "I--"
    Ry shy ud "..."
    Ry shy ud "Thank you."
    m "He leaned down, nuzzling his snout against my neck and shoulder as he tried to relax enough to let go."
    m "After a few moments, he shuddered, and I felt the hot stream of his piss working its way up his enormous length still buried inside me."
    play soundloop "fx/faucet1.ogg" fadein 1.0
    queue soundloop "fx/faucet2.ogg"
    if persistent.bangok_inflation == True:
        m "With my guts already stuffed full of his seed, at first I couldn't even feel his piss coming out, as if he had hesitated at the last moment."
        m "But then, as he groaned and relaxed, I began to feel the hot urine mixing with his seed, filling me up even more."
        m "My belly gurgled again, swelling slowly still further as his cum was pushed deeper into me by the force of his urination."
        m "Then the gurgling stopped, and I realized there was simply no more room in my taxed intestines for any more liquid."
        c "Remy, I-- Urp!"
        m "I belched, holding my cramping, straining belly as cum flooded my stomach, rising up my throat while his piss continued to fill me from the inside."
        m "I couldn't breathe as I belched again, this time feeling heavy, creamy rivulets of cum dribble down my chin and chest."
        Ry shy ud "Oh, [player_name]! I'm so sorry!"
        m "I tried to speak, but the weight of his seed and piss inside me was too much, and I could only belch and gulp as I tried to keep from choking on the thick, creamy fluids."
        stop soundloop fadeout 5.0
        m "Remy's piss finally slowed, leaving me with a belly so full and heavy that I couldn't scarcely even think of moving."
        m "All I knew was that I was too full to breathe, and that some of it was going to come up any moment."
        Ry shy ud "[player_name]! I--"
        menu:
            "Vomit cum.":
                m "I tried to hold it back, but the weight of his seed and piss inside me was too much."
                m "I belched again, then vomited a thick, creamy stream of cum and piss all over Remy and couch."
                m "I gasped, then belched again, feeling the weight of his seed and piss inside me shift and settle as I emptied my stomach of the thick, creamy fluids."
                Ry look ud "Oh, [player_name]! [player_name], I didn't mean to-- Oh, [player_name]!"
                m "With some of the pressure relieved, I caught a ragged breath."
            "Kiss him.":
                m "Utterly overwhelmed by the sensations of being stuffed so full of his seed and piss, I caught Remy's snout with a hand and pulled him down into a deep, passionate kiss."
                m "And then the movement forced a torrent of cum up my throat, and I vomited a thick, creamy stream right into Remy's mouth."
                m "He gasped, then swallowed, then kissed me back, his tongue sliding into my mouth to share the thick, creamy fluids with me."
                m "As his tongue tried to explore down my throat, I gagged, then vomited again, the thick, creamy fluids spilling out of our locked mouths and down onto our chests, bellies, and the couch, despite his best efforts to swallow it all."
                m "Then, finally, the pressure eased, and I caught a ragged breath."
        c "F-Fuck... I'm so full..."
        m "I held my bloated stomach, swooning from the sensations of being stuffed so full of his seed and piss, only able to stay upright thanks to his thick dragonhood still holding me in place."
        Ry shy ud "I shouldn't have let myself get this pent up."
        Ry look ud "With our size difference... m-maybe we should get you to a hospital..."
        c "(I'm not even sure how we'd do that.)"
        m "Gingerly, I leaned forward to hug him again, struggling to keep the contents of my overstretched body down."
        c "I'm staying right here with you."
        Ry shy ud "..."
    elif bangok_four_remy4_store.protection == True:
        m "With his condom already stuffed full of his seed, at first I couldn't even feel his piss coming out, as if he had hesitated at the last moment."
        m "But then, as he groaned and relaxed, I began to feel the hot urine mixing with his seed, filling his condom up even more."
        m "I held my belly, feeling the condom slowly inflate with the weight of his seed and piss inside me, straining against the walls of my colon as his deep penetration left it very little room to grow."
        m "Then I felt a jet of hot fluid, a dribbling and leaking sensation that was definitely not contained by the condom."
        stop soundloop fadeout 4.0
        c "Remy, I-- Urp!"
        play sound "fx/bubbles.ogg"
        m "The condom burst, the weight of his seed and piss inside me too much for it to contain."
        m "I froze, my guts spasming as the thin, hot slurry of his cum and piss doused my insides, the heat now suffusing my body and soiling me in a way that would never truly wash out."
        Ry shy ud "Oh, [player_name]! The-- The condom--"
        Ry shy ud "I'm so sorry! I didn't mean to break it!"
        Ry look ud "But..."
        Ry shy ud "That did... it felt kind of good. For me."
        Ry shy ud "I'm so sorry, [player_name]."
        menu:
            "That's weird, Remy.":
                Ry shy ud "I'm sorry. I didn't mean to--"
                c "You keep saying that. Look, I'm not going to hold it against you now."
                c "Let's just never do that again."
                Ry shy ud "O-Okay. I'm sorry."
            "It felt good for me too.":
                Ry shy ud "It did?"
                Ry shy ud "..."
                Ry shy ud "I'm out now, but would you want to try that again? Sometime?"
                c "Maybe."
            "I think I might be sick.":
                Ry look ud "I'm so sorry--"
                c "Just stop apologizing. I'm not going to hold it against you now."
                c "Let's just never do that again. And stop talking about your piss in my guts right now."
                Ry shy ud "O-Okay. I'm sorry."
        m "I sighed, then, trying to show there were no hard feelings, I leaned forward to hug him again."
    else:
        m "His hot urine sprayed into my colon, washing away his cum until the two fluids had mixed into a thin slurry pooling in my guts."
        m "I held my belly, panting from the heat now suffusing my body."
        m "Feeling him use me like this, marking and soiling my insides as his in a way that would never truly wash out, I found my love and affection for Remy only redoubling."
        stop soundloop fadeout 4.0
        m "Remy's piss finally slowed, then stopped, leaving only a gentle dribbling sensation as the slurry of his cum and piss settled deep inside."
        m "Remy, too, panted with relief, but even still he looked apologetic."
        Ry shy ud "I'm so sorry, [player_name]. That was--"
        Ry look ud "I don't want to sound weird, but..."
        Ry shy ud "That felt so intimate and... good. It felt good for me."
        menu:
            "That's weird, Remy.":
                Ry shy ud "I'm sorry. I didn't mean to--"
                c "I don't think I want to do that again."
                Ry shy ud "O-Okay. I'm sorry."
            "It felt good for me too.":
                Ry shy ud "That's... good."
                Ry shy ud "..."
                Ry shy ud "I'm out now, but would you want to try that again? Sometime?"
                c "Maybe."
            "I hope you're not too embarrassed.":
                Ry shy ud "I'm not. I just... I don't know what to say."
                c "That's okay. I said it was okay and I meant it. I'm not going to suddenly hold it against you now."
                Ry shy ud "..."
        m "Trying to show there were no hard feelings, I leaned forward to hug him again."
    jump angok_four_remy4_atop_inside_anal_ending

label angok_four_remy4_atop_inside_anal_ending:
    show bangok_grey with dissolveslow
    if persistent.bangok_knot == True:
        m "He was silent for a long moment, then nuzzled his snout against my shoulder and back, returning the hug and cuddling me close as we waited for his knot to relax and release me."
    else:
        m "He was silent for a long moment, then nuzzled his snout against my shoulder and back, returning the hug and cuddling me close as we waited for me to recover enough to move."
    scene black with dissolveslow
    scene o4 at Pan((0,220), (0,250), 1)
    m "It took some work for us to separate, requiring us to move over to an empty space on the floor to get the leverage we needed."
    if persistent.bangok_watersports == True and bangok_four_remy4_store.remy_pissed == False:
        m "The moment we were separated, Remy rushed to the bathroom, leaving me to recover on my own for a few moments."
    elif persistent.bangok_watersports == True and bangok_four_remy4_store.remy_pissed == True and persistent.bangok_inflation == True:
        m "The moment we were separated, a torrent of cum and piss spilled out of my gaping ass, soaking Remy's crotch, my legs, and the floor."
        m "I groaned and shuddered with relief, my stomach cramping as my muscles were finally allowed to push the excessive liquids out of me."
    elif persistent.bangok_inflation == True:
        m "When we finally did, I felt a rush of relief as his seed began to pour out of my overstretched body, pooling on the floor beneath me."
    m "I felt wide open and empty without him inside me, but I was also relieved to have him out of me."
    m "We collapsed together on the floor, panting and exhausted from our new exertions despite the cuddling rest we'd just had."
    jump bangok_four_remy4_floor_cuddle_conclusion_late







label bangok_four_remy4_male_tongue_path:
    if bangok_four_remy4_store.protection == True:
        m "Taking the box of smaller condoms as Remy set it on the coffee table, I picked one out and tore it open, applying it to my member."
        m "Then I took a seat at the armchair at one end of the table, pushing the table out of the way a little with my foot so Remy could better access my body."
        play sound "fx/undress.ogg"
        hide remy with dissolve
        m "Remy pulled off his collar and set his glasses on the coffee table, out of harm's way."
        show remy shy ud with dissolve
        show remy:
            ypos 1.0
            ease 1.0 ypos 1.45
            ypos 1.45
        with None
        m "Remy approached me slowly, his eyes never leaving mine as he lowered himself onto crossed forelegs on the carpet in front of me."
        m "He eyed my wrapped erection with trepidation, comparing my human member's size to his own draconic expectations. I couldn't help but chuckle a little at his adorable expression."
    else:
        m "Taking my own shaft in hand, I sat at the edge of the armchair at the end of the coffee table, pushing the table out of the way a little with my foot so Remy could better access my body."
        play sound "fx/undress.ogg"
        hide remy with dissolve
        m "Remy pulled off his collar and set his glasses on the coffee table, out of harm's way."
        show remy shy ud with dissolve
        show remy:
            xpos 0.5
            ease 0.5 xpos 0.55
            xpos 0.55
            ypos 1.0
            ease 1.0 ypos 1.45
            ypos 1.45
        with None
        m "Then, rolling off the couch, Remy approached me slowly, his eyes never leaving mine as he lowered himself onto crossed forelegs on the carpet in front of me."
        m "He eyed my erection with trepidation, comparing my human member's size to his own draconic expectations. I couldn't help but chuckle a little at his adorable expression."
    Ry shy ud "More tongue, you said?"
    m "Lifting his chin with one hand, I gave his snout a soft pet with the other."
    c "Yes, right down here."
    m "Gently, I guided him down to my crotch, feeling his warm breath against my member as he leaned into my hand."
    Ry shy ud closed "Could you... guide me a little more? Grab my horns?"
    c "Sure."
    show remy:
        pause 0.4
        ypos 1.45
        ease 0.4 ypos 1.5
        ypos 1.5
    with None
    if bangok_four_remy4_store.protection == True:
        m "I took hold of his larger, higher horns, then tugged him closer. He took the invitation, accepting my rubber-wrapped tip between his scaly lips, then slathering it with attention from his tongue."
    else:
        m "I took hold of his larger, higher horns, then tugged him closer. He took the invitation, accepting my fleshy tip between his scaly lips, then slathering it with attention from his tongue."
    c "So... different..."
    m "I groaned at the sensations he was causing, my body tensing up as he focused more of his attention on the sensitive underside of my cockhead."
    scene black with dissolvemed
    m "Then, eager for more, I guided him the rest of the way to my base, feeling his snout against my groin and his chin against my balls."
    scene bangok_four_remy4_cg tongue male unprotected at Pan((0,0), (720,488), 8.0) with dissolvemed
    m "He licked at my shaft's full length, tasting every inch as he went down. When he had fully explored all that was in his mouth, he opened a little wider and extended his tongue to begin gently exploring my balls."
    c "Remy..."
    m "I couldn't help but moan at the sight of him so intent on pleasing me like this. He looked up from what he was doing, his eyes full of concern for any discomfort I might be experiencing."
    c "Don't stop."
    m "Pushing and pulling him by his horns, I began to gently pump his scaly lips up and down my shaft with short, teasing strokes."
    m "His tongue continued to trace lazy patterns along the underside of my member, causing me to squirm slightly in response and pant with need."
    if bangok_four_remy4_store.protection == True:
        m "I huffed needily, pushing my legs apart and pulling his head up and down my shaft with more force."
        c "Nngh... I'm close..."
        m "He looked up at me, then lavished my shaft with all the more attention, his tongue and lips working in tandem to bring me to the edge."
        c "Oh, Remy...!"
        show black with dissolve
        m "With a groan of relief, I released my load into his mouth, puffing up the condom's reservoir with my meager human load."
        m "Remy kept licking, but blushed furiously as I held his face to my crotch and pumped the last of my cum into the condom."
        m "Then, when I had run dry, he gently gripped the condom with his lips, pulling it off my member before plucking it from his mouth and setting it aside."
        menu:
            "Kiss him":
                m "I chuckled at his blushing, then slipped forward off the armchair to press my lips against his. Our tongues met, trading a little in the rubbery taste of the condom, and I hugged him tightly, his wings flapping helplessly as he struggled to escape my embrace."
                m "Feeling his body tense up in my arms and knowing what he'd just done for me, I knew I wanted more of him."
                m "When we finally broke the kiss, he was panting with need."
            "Compliment him":
                c "That was amazing. You're amazing."
                m "Embarrassed and yet pleased by my compliment, he looked away."
                c "I hope I can do nearly as well."
                m "He blushed harder and nodded."
    else:
        show black with dissolve
        m "Wanting to draw this out, I pulled him off me completely, then set my saliva-slicked member atop his blushing snout."
        m "He continued to try to explore me, licking and nibbling at my balls with his tongue and lips, then sucking them into his mouth and gently massaging them with his tongue."
        m "Feeling my balls grow heavy with the need to release their contents, I decided to take matters into my own hands."
        m "Gently pulling away from his mouth, I began to jack off my shaft, pausing every now and then as he gave the tip or my balls a lick with his tongue."
        m "My body tensed up as I neared my climax, my breath coming in ragged, happy gasps as I tried to hold back."
        m "But then I couldn't. With a groan of relief, I released my load into his mouth and onto his face, spurting gooey ropes of cum over his snout and tongue."
        m "He froze up, blushing furiously as I graced his face with my appreciation."
        m "Then, when I had run dry, he swirled what had landed in his mouth on his tongue, licking a little more from the tip of his snout."
        Ry shy ud "You... you taste a little saltier than we do."
        menu:
            "Kiss him":
                m "I laughed, then slipped forward off the armchair to press my lips against his. Our tongues met, trading a little in my taste, and I hugged him tightly, his wings flapping helplessly as he struggled to escape my embrace."
                m "Tasting the mix of salty and sweet on his tongue, I knew I wanted more of him."
                m "When we finally broke the kiss, he was panting with need, face still glistening with some of my cum."
            "Compliment him":
                c "That was amazing. You're amazing."
                m "Embarrassed and yet pleased by my compliment, he looked away."
                c "I hope I can do nearly as well."
                m "He blushed harder and nodded."
            "Taste your cum.":
                m "Reaching forward, I scooped up some of the cum still clinging to his snout and brought it to my lips."
                m "With a small nod of approval, I swallowed it down, savoring the flavor of our exchange."
                c "Now I can compare with yours."

    show o4 at Pan((0, 150), (0, 250), 3) with dissolve
    show remy shy ud at Transform(xanchor=0.5, yanchor=0.0, xpos=0.5, ypos=1.0)
    jump bangok_four_remy4_tongue_path_merge

label bangok_four_remy4_female_tongue_path:
    m "I sat at the edge of the armchair at the end of the coffee table, pushing the table out of the way a little with my foot so Remy could better access my body."
    play sound "fx/undress.ogg"
    hide remy with dissolve
    m "Remy pulled off his collar and set his glasses on the coffee table, out of harm's way."
    show remy shy ud with dissolve
    show remy:
        xpos 0.5
        ease 0.5 xpos 0.55
        xpos 0.55
        ypos 1.0
        ease 1.0 ypos 1.45
        ypos 1.45
    with None
    m "Rolling off the couch, Remy approached me slowly, his eyes never leaving mine as he lowered himself onto crossed forelegs on the carpet in front of me."
    m "He eyed my vulva with trepidation, comparing my human opening's size to his own draconic expectations. I couldn't help but chuckle a little at his adorable expression."
    Ry shy ud "More tongue, you said?"
    m "Lifting his chin with one hand, I gave his snout a soft pet with the other."
    c "Yes, right down here."
    m "Gently, I guided him down to my crotch, feeling his warm breath against my mons."
    scene black with dissolvemed
    m "Then he moved forward himself, nestling his scaly snout between my thighs. My hips twitched at the contact, my breath catching as he began to explore my folds with his tongue."
    scene bangok_four_remy4_cg tongue female at Pan((0,0), (720,588), 8.0) with dissolvemed
    m "His rough, hot tongue slid across my inner labia, tracing the outer surface of my vulva before delving deeper inside."
    c "Remy..."
    m "The sensation of his tongue sliding into me caused my body to respond almost immediately, my muscles tightening and my breath hitching as I tried to control my reactions."
    m "His long, dexterous tongue lapped at my inner walls, discovering new places to tickle my nerves."
    m "Feeling my body arch towards him, I reached down and guided his head further into place, wanting more."
    m "He obliged, pressing his snout against my clit while continuing to lap at my juices. My body shivered with pleasure, my hips rising and falling to meet the rhythm of his tongue."
    m "Every once in a while, he'd pull away, looking up at me, clearly seeking guidance on what I liked."
    c "Keep going."
    m "He resumed his ministrations, his tongue flicking and probing my most intimate areas, drawing more noises of pleasure from me."
    m "As he focused more of his attention on my clitoris, my body convulsed, shuddering from the stimulation his tongue provided."
    scene black with dissolve
    c "T-Too much."
    m "He stopped, looking up from what he was doing, his eyes full of concern for any discomfort I might be experiencing."
    c "No, I liked it. Just... slower."
    scene bangok_four_remy4_cg tongue female at Pan((780,488), (720,588), 8.0) with dissolvemed
    m "He nodded, slowing his movements and focusing on the area around my clit instead of directly on it. Then, he returned to deeper exploration of my depths, using the flat part of his tongue to massage my insides."
    m "I groaned, feeling my orgasm building within me."
    scene black with dissolve
    m "Finally, I cried out in ecstasy, my body shaking uncontrollably as wave after wave of pleasure washed through me. Even as I came down from my peak, Remy kept licking, prolonging my pleasure until I begged him to stop."
    m "I collapsed back against the chair, panting heavily as he retracted his snout from between my legs."
    scene o4 at Pan((0, 150), (0, 250), 3)
    show remy shy ud:
        xanchor 0.5
        yanchor 1.0
        xpos 0.5
        ypos 1.65
        linear 3.0 ypos 1.45
        ypos 1.45
    with dissolveslow
    m "Blinking up at me, his snout shiny with my fluids, he blushed furiously."
    show remy shy ud:
        ypos 1.45
        ease 0.7 ypos 1.25
        ypos 1.25
    m "After a moment, he pulled further away, cleaning his tongue on the roof of his mouth as I panted."
    m "He looked embarrassed, but also pleased with the result of his efforts."
    Ry shy ud "How did that feel?"
    menu:
        "Kiss him":
            m "I laughed, then slipped forward off the couch to press my lips against his. Our tongues met, trading a little in my taste, and I hugged him tightly, his wings flapping helplessly as he struggled to escape my embrace."
            m "When we finally broke the kiss, he was panting with need, face still glistening with my fluids."
        "Compliment him":
            c "That was amazing. You're amazing."
            m "Embarrassed and yet pleased by my compliment, he looked away."
            c "I hope I can do nearly as well."
            m "He blushed harder and nodded."
        "Taste your fluids.":
            m "Reaching forward, I spread some of the fluids still clinging to his snout onto my fingers, then brought it to my lips."
            m "With a small nod of approval, I slurped it down, savoring the flavor of my own essence."
            c "Now I can compare with yours."
    jump bangok_four_remy4_tongue_path_merge

label bangok_four_remy4_tongue_path_merge:
    show remy shy ud at center with ease
    m "His hindlegs were a little unsteady as he got to his feet."
    c "You've seen and tasted both ends of me now. What do you want to do next?"
    Ry normal ud "It sounds like you're the one with something in mind."
    menu:
        "Turn around for me.":
            $ renpy.pause (0.5)
            jump bangok_four_remy4_turn_around
        "I need you inside me.":
            jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_turn_around:
    show remy shy ud with dissolve
    $ renpy.pause (0.3)
    scene black with dissolvemed
    $ renpy.pause (0.5)
    scene bangok_four_remy4_cg bottom:
        zoom 1.8
        align (0.0,0.0)
        linear 8.0 xalign 0.5 yalign 1.0
        align (0.5,1.0)
    with dissolvemed
    $ renpy.pause (3.0)
    m "Remy lay on his belly on the couch, setting his wings over the couch back and crossing his forelegs just in front of the armrest."
    m "As I got on the couch behind him, he lifted his tail, revealing his tight, pink pucker winking out at me above his mostly-sheathed member."
    m "Despite his efforts to remain still, a few drops of draconic precum dripped from his tip, landing on the couch cushion beneath him."
    m "I couldn't help but reach out and touch his tail, feeling the soft scales and the warmth of his body beneath them."
    Ry shy ud "It's not... too different for you, is it?"
    menu:
        "Maybe a little bit.":
            c "But I'm more than willing to try."
        "Not at all.":
            c "You're just as you are, and I like you that way."
        "It's gorgeous.":
            $ renpy.pause (0.5)
    m "I spread his cheeks apart, feeling the muscle in his quadrupedal legs tense beneath my touch."
    Ry shy ud "Are you... going to...?"
    menu:
        "Lick his cloaca." if persistent.bangok_cloacas == True:
            jump bangok_four_remy4_rimjob
        "Lick his ass." if persistent.bangok_cloacas == False:
            jump bangok_four_remy4_rimjob
        "Lick his shaft's base." if bangok_four_remy4_store.protection == False:
            jump bangok_four_remy4_sheath_licking
        "Stroke his tip.":
            jump bangok_four_remy4_bottom_handjob

label bangok_four_remy4_rimjob:
    show bangok_four_remy4_cg bottom:
        align (0.5, 1.0)
        linear 2.0 align (0.625, 0.7)
        align (0.625, 0.7)
        zoom 2.0
        linear 0.7 zoom 3.0
    $ renpy.pause (0.5)
    if bangok_four_remy4_store.protection == True:
        m "Unable to resist the winking invitation of his tight ring of flesh, I grabbed one of the larger size condoms off the table, handing it to him."
        c "Can you cut this with your claws, down one side?"
        Ry shy ud "Why?"
        c "Makeshift dental dam. Unless you have an actual one around here."
        Ry shy ud "I don't think our species has any that would fit your face."
        m "Following my instructions, he opened the condom and unrolled it, then used his claws to rip through the ring at the base on one side before peeling it in half all the way up."
        m "I took the sheet of rubber from him, moving back to his rear, then spread the lubed side over his pucker before leaning in with my face and licking."
    else:
        m "Unable to resist the winking invitation of his tight ring of flesh, I leaned in, giving it..."
    m "Remy shuddered beneath me as I teased his hole, my tongue flicking back and forth across his anal opening."
    m "His muscles contracted under my tongue, and he let out a small moan of pleasure as he got into it."
    Ry shy ud "This is so different. You're so soft..."
    m "I could feel his body tense as I circled the rim of his ass with my tongue, making sure to take my time."
    m "His breathing started getting heavier, his muscles growing more relaxed and his hips pushing back into me as he got used to the sensations."
    m "I moved in further, pressing my lips against his rear entrance and gently suckling and nibbling on it."
    Ry shy ud leye "You're so good... Oh, [player_name]..."
    m "My hands wandered over his ass as he did his best to relax, using one to caress one buttcheek while the other explored higher, stroking his tail."
    Ry shy ud closed "Mmmnh..."
    if bangok_four_remy4_store.protection == True:
        m "My tongue explored every little wrinkle of Remy's pucker, sliding over every little scale that bordered it through the material of the condom."
        m "Then, finally, I gave his ass the kiss it so richly deserved. Gripping his hips, I pulled him back against my face as my tongue pushed a little of the condom into his ass, just enough to get inside and start licking properly."
    else:
        m "My tongue explored every little wrinkle of Remy's pucker, sliding over every little scale that bordered it."
        m "Then, finally, I gave his ass the kiss it so richly deserved. Gripping his hips, I pulled him back against my face as my tongue pushed a little of the condom into his ass, just enough to get inside and start licking properly."
    Ry shy ud "Oh, you're making that feel so good..."
    if bangok_four_remy4_store.protection == True:
        m "He was panting with pleasure, his claws gripping the armrest of the couch as I continued to eat out his ass through the dental dam. My hands were kneading his buttocks, my thumbs kneading the base of his tail."
    else:
        m "He was panting with pleasure, his claws gripping the armrest of the couch as I continued to eat out his ass. My hands were kneading his buttocks, my thumbs kneading the base of his tail."
    m "We stayed like that for a while, Remy just letting me lick him until he couldn't take it anymore."
    Ry shy ud closed "[player_name]... Please... I like this but I need more of you."
    show bangok_four_remy4_cg bottom:
        linear 1.0 zoom 2.0
        zoom 2.0
    with None
    m "Pulling back, I stroked Remy's shuddering flanks, trying to decide what to do next."
    menu:
        "Lick his shaft's base.":
            jump bangok_four_remy4_sheath_licking
        "Stroke his tip.":
            jump bangok_four_remy4_bottom_handjob_late

label bangok_four_remy4_sheath_licking:
    show bangok_four_remy4_cg bottom:
        linear 2.0 align (0.59,0.59)
        align (0.59,0.59)
    with None
    $ renpy.pause (0.5)
    m "Running my hands down his rear, I spread his mid-thighs wider, fully revealing the glistening slit from which his shaft peeked out."
    show bangok_four_remy4_cg bottom:
        zoom 2.0
        linear 1.0 zoom 3.0
        zoom 3.0
    with None
    m "Then I leaned in, placing my face right up that slit as I began to lick and suck on the fleshy bits within."
    Ry shy ud "Mmmmnh."
    m "Remy squirmed, panting harder as licked at his slit's slick contents."
    m "I slowed, worried I was going too fast for him."
    Ry shy ud leye "Keep going. Please."
    m "Taking his words as encouragement, I continued to lick and suck at his sheath, feeling his member twitch and throb beneath my ministrations."
    m "Then I dug a little deeper, sliding my tongue beneath his slit's fleshy folds while his shaft rubbed against my cheeks and chin."
    $ renpy.pause (0.5)
    Ry shy ud closed "Oh, [player_name]..."
    $ renpy.pause (0.5)
    menu:
        "Stroke him while licking.":
            $ renpy.pause (0.5)
            m "Struggling to keep my position without faceplanting forehead-first into his slit, I brought my hands between his legs, wrapping my fingers around his slick shaft."
            m "Remy whined, his body and dragonhood radiating heat and need, his length now fully unsheathed and throbbing with desire between my hands."
            m "I began to stroke him slowly at first, then faster as I felt his hips twitching against my face, as if he wanted to thrust into my gentle strokes."
            Ry shy ud leye "Nngh... [player_name], the couch... c-cushions..."
            m "I could feel his precum dripping onto my fingers as I worked him, his twitching and moaning reaching a crescendo as he neared his peak."
            menu:
                "Save the cushions with my mouth.":
                    jump todo_out_of_content_bangok_four_remy4
                "Keep going.":
                    m "Caring only about this moment here with him, I continued to stroke him, feeling his body stiffen and his breath catch as he came."
                    Ry shy ud closed "[player_name]...!"
                    m "His seed shot out in thick, hot ropes, splattering across my hands and arms and the couch beneath him as I continued to stroke him through his orgasm."
                    m "Finally, he collapsed back against the couch, panting heavily, his eyes closed and his body shivering with the aftershocks of his climax."
                    m "Then he finally opened his eyes and noticed the mess he'd made."
                "Pull away.":
                    show bangok_four_remy4_cg bottom:
                        zoom 3.0
                        linear 1.0 zoom 2.0
                        zoom 2.0
                    with None
                    m "I dropped everything I was doing, pulling away in an attempt to save the couch cushions from his seed."
                    m "I was too late."
                    Ry shy ud closed "Nngh... [player_name]..."
                    m "His twitching member spurted out thick, hot ropes of seed, splattering the couch cushion beneath his hindquarters."
                    m "After a few moments of panting, shivering climax, he collapsed back against the couch, still panting heavily."
            Ry shy ud "I'm sorry... I didn't mean to..."
            Ry look ud "I messed even this up, I--"
            menu:
                "Cut him off by kissing him.":
                    scene black with dissolve
                    m "Before he could finish his sentence, I'd closed the distance to his snout and pressed my lips against his."
                    m "He moaned softly, nuzzling his snout against my face as I kissed him."
                    m "Then I pulled away, looking him in the eyes."
                "Cut him off by licking his shaft.":
                    show bangok_four_remy4_cg bottom:
                        zoom 2.0
                        linear 0.5 zoom 3.0
                        zoom 3.0
                    with None
                    m "Before he could finish his sentence, I leaned in to kiss him on the one place I could most show there was no affection lost."
                    Ry shy ud leye "Nnh..."
                    m "He moaned softly, letting me continue to lavish him with attention for a few moments until I pulled away again."
                    show black with dissolve
                    $ renpy.pause (0.5)
                "Comfort him.":
                    show black with dissolve
                    $ renpy.pause (0.5)
            show bangok_four_remy4_cg bottom:
                zoom 2.0
                align (0.2, 0.5)
            with dissolve
            c "You didn't mess up anything. We'll clean it up together."
            m "He looked at me, his eyes full of gratitude and relief."
            show black with dissolve
            m "Then, to my surprise, he launched off the couch and hugged me, heedless of how much heavier he was than me."
            c "Remy!"
            show o4 at Pan((0, 250), (0, 250), 0) with vpunch
            jump bangok_four_remy4_floor_cuddle_conclusion
        "Keep licking.":
            $ renpy.pause (0.5)
            m "Remy huffed harder, his body and dragonhood radiating heat and need, his length now fully unsheathed and throbbing with desire."
            show bangok_four_remy4_cg bottom:
                zoom 3.0
                linear 1.0 zoom 3.2
                zoom 3.2
            with None
            m "Then, grabbing his hips, I pulled myself a little closer, trying to get my tongue as deep into his slit as I could."
            Ry shy ud leye "Nngh... [player_name], stop. That's... too much."
            show bangok_four_remy4_cg bottom:
                zoom 3.0
                linear 1.0 zoom 3.0
                linear 3.0 zoom 1.5
            with None
            m "Reluctantly, I pulled away, looking up at him with a question in my expression."
            c "Are you okay?"
            Ry shy ud "I liked it, but... it was a little too intense. At least all on its own."
            m "His hindquarters shivered with need."
            Ry normal ud "Let's try something else."
        "Pull away.":
            show bangok_four_remy4_cg bottom:
                zoom 3.0
                linear 1.0 zoom 1.5
                zoom 1.5
            with None
            m "I pulled away, looking up at him with a grin."
            m "Remy huffed, hindquarters shivering with need."

    menu:
        "[[Stroke him.]":
            jump bangok_four_remy4_bottom_handjob_late
        "I want you inside me.":
            jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_bottom_handjob:
    show bangok_four_remy4_cg bottom:
        linear 2.0 align (0.59,0.59)
        align (0.59,0.59)
    with None
    $ renpy.pause (0.5)
    m "Seeing his glistening tip and its leaking pre, I couldn't help but want it between my fingers."
    show bangok_four_remy4_cg bottom:
        zoom 2.0
        linear 2.0 zoom 2.2
        zoom 2.2
    with None
    m "Reaching down, I nudged his hindlegs a little further apart, then gently grasped his tip with one hand."
    m "A shudder ran through Remy's rear, right up his tail, fluttering his wings."
    m "Then I began to explore with my fingers, sliding them around the slick surface of his dragonhood's tip, caressing until I began to urge more from within his body."
    Ry shy ud closed "Hahh..."
    m "Remy hid his snout under a forepaw, panting as I began to stroke what of his shaft had emerged with one hand."
    m "More slid out of its hiding place, giving further distance for my fingers to glide over his slick shaft's surface from his slit all the way to his tip."
    m "Then it seemed I had coaxed all I could from him, and he began to huff with further need."
    jump bangok_four_remy4_bottom_handjob_merge

label bangok_four_remy4_bottom_handjob_late:
    show bangok_four_remy4_cg bottom:
        linear 2.0 align (0.59,0.59)
        align (0.59,0.59)
        zoom 2.0
        linear 2.0 zoom 2.2
        zoom 2.2
    with None
    $ renpy.pause (0.5)
    m "I reached between his hindlegs, spreading them slightly further from his engorged, glistening dragonhood."
    m "Then, gently, I began to caress his member with one hand, gliding my fingers over his slick shaft's surface from his slit all the way to his tip."
    m "He huffed and moaned, heady with need."


label bangok_four_remy4_bottom_handjob_merge:
    m "I could feel his member twitching and throbbing beneath my touch, his hips shaking as he tried to thrust into my hand."
    m "Deciding to oblige his desires, "

    jump todo_out_of_content_bangok_four_remy4


label bangok_four_remy4_floor_cuddle_conclusion:
    m "We lay on the floor together, his wings and tail wrapped around me as we cuddled and caught our breath in each others' embrace."
    label bangok_four_remy4_floor_cuddle_conclusion_late:
    stop soundloop fadeout 5.0
    $ renpy.pause (4.0)
    m "As our breathing faded into quiet, I felt the rise and fall of his warm chest against my arm, and never wanted to let go."
    m "Remy nuzzled the top of my head, then gave me a lick."
    Ry shy ud "[player_name]..."
    m "I looked up to meet his gaze."
    Ry shy ud "May I stay here, tonight?"
    c "Of course."
    scene black with dissolvemed
    m "He smiled as he dipped his head to nuzzle me again, and it was the happiest smile I'd ever seen on his white-scaled face."
    $ remystatus = "good"
    $ mp.remyromance = True
    $ mp.save()
    hide remy with dissolve

    stop music fadeout 2.0

    $ renpy.pause (2.0)

    $ remyscenesfinished = 4
    jump _mod_fixjmp

label todo_out_of_content_bangok_four_remy4:
    play sound "fx/system3.wav"
    s "You've reached the end of the content currently available for this character."
    s "Roll back or prepare to crash."
    $ renpy.error("End of content reached.")
