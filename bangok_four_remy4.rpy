init python in bangok_four_remy4_store:
    # Paths:
    # tongue
    path = None

    protection = False

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
    show grey with dissolvemed
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
            jump todo_out_of_content_bangok_four_remy4
        "[[Say nothing.]]":
            m "I couldn't help but let out a soft moan as he continued his teasing assault. His tail began to wag gently against the couch."
            Ry normal b "Do you want me to...?"
            c "Please..."
            Ry shy b "Are you sure? I don't--"
            m "I pulled away from his snout and looked him in the eyes, my own filled with desire."
            c "Yes."
            jump todo_out_of_content_bangok_four_remy4

    play sound "fx/undress.ogg"
    hide grey with dissolve
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
            jump todo_out_of_content_bangok_four_remy4
        "Continue.":
            $ renpy.pause (0.5)

    if bangok_four_remy4_store.path == "tongue":
        if bangok_four_playerhasdick == True:
            if bangok_four_remy4_store.protection == True:
                jump todo_out_of_content_bangok_four_remy4
                # jump bangok_four_remy4_male_protected_tongue_path
            else:
                jump bangok_four_remy4_male_unprotected_tongue_path
        else:
                jump bangok_four_remy4_female_tongue_path

    jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_male_unprotected_tongue_path:
    m "Taking my own shaft in hand, I sat at the edge of the armchair at the end of the coffee table, pushing the table out of the way a little with my foot so Remy could better access my body."
    m "Rolling off the couch, Remy approached me slowly, his eyes never leaving mine as he lowered himself onto crossed forelegs on the carpet in front of me."
    m "He eyed my erection with trepidation, comparing my human member's size to his own draconic expectations. I couldn't help but chuckle a little at his adorable expression."
    Ry shy b "More tongue, you said?"
    m "Lifting his chin with one hand, I gave his snout a soft pet with the other."
    c "Yes, right down here."
    m "Gently, I guided him down to my crotch, feeling his warm breath against my member as he hesitated again."
    c "May I guide you with your horns?"
    $ renpy.pause (0.8)
    Ry shy b "Yes."
    m "I took hold of his larger, higher horns, then tugged him closer. He took the invitation, accepting my fleshy tip between his scaly lips, then slathering it with attention from his tongue."
    c "So... different..."
    m "I groaned at the sensations he was causing, my body tensing up as he focused more of his attention on the sensitive underside of my cockhead."
    m "Then, eager for more, I guided him the rest of the way to my base, feeling his snout against my groin and his chin against my balls."
    m "He licked at my shaft's full length, tasting every inch as he went down. When he had fully explored all that was in his mouth, he opened a little wider and extended his tongue to begin gently exploring my balls."
    c "Remy..."
    m "I couldn't help but moan at the sight of him so intent on pleasing me like this. He looked up from what he was doing, his eyes full of concern for any discomfort I might be experiencing."
    c "Don't stop."
    m "Pushing and pulling him by his horns, I began to gently pump his scaly lips up and down my shaft with short, teasing strokes."
    m "His tongue continued to trace lazy patterns along the underside of my member, causing me to squirm slightly in response and pant with need."
    m "Wanting to draw this out, I pulled him off me completely, then set my saliva-slicked member atop his blushing snout."
    m "He continued to try to explore me, licking and nibbling at my balls with his tongue and lips, then sucking them into his mouth and gently massaging them with his tongue."
    m "Feeling my balls grow heavy with the need to release their contents, I decided to take matters into my own hands."
    m "Gently pulling away from his mouth, I began to jack off my shaft, pausing every now and then as he gave the tip or my balls a lick with his tongue."
    m "My body tensed up as I neared my climax, my breath coming in ragged, happy gasps as I tried to hold back."
    m "But then I couldn't. With a groan of relief, I released my load into his mouth and onto his face, spurting gooey ropes of cum over his snout and tongue."
    m "He froze up, blushing furiously as I graced his face with my appreciation."
    m "Then, when I had run dry, he swirled what had landed in his mouth on his tongue, licking a little more from the tip of his snout."
    Ry shy b "You... you taste a little saltier than we do."
    menu:
        "Kiss him":
            m "I laughed, then slipped forward off the couch to press my lips against his. Our tongues met, trading a little in my taste, and I hugged him tightly, his wings flapping helplessly as he struggled to escape my embrace."
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
    jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_female_tongue_path:
    m "I sat at the edge of the armchair at the end of the coffee table, pushing the table out of the way a little with my foot so Remy could better access my body."
    m "Rolling off the couch, Remy approached me slowly, his eyes never leaving mine as he lowered himself onto crossed forelegs on the carpet in front of me."
    m "He eyed my vulva with trepidation, comparing my human opening's size to his own draconic expectations. I couldn't help but chuckle a little at his adorable expression."
    Ry shy b "More tongue, you said?"
    m "Lifting his chin with one hand, I gave his snout a soft pet with the other."
    c "Yes, right down here."
    m "Gently, I guided him down to my crotch, feeling his warm breath against my mons."
    m "Then he moved forward himself, nestling his scaly snout between my thighs. My hips twitched at the contact, my breath catching as he began to explore my folds with his tongue."
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
    c "T-Too much."
    m "He stopped, looking up from what he was doing, his eyes full of concern for any discomfort I might be experiencing."
    c "No, I liked it. Just... slower."
    m "He nodded, slowing his movements and focusing on the area around my clit instead of directly on it. Then, he returned to deeper exploration of my depths, using the flat part of his tongue to massage my insides."
    m "I groaned, feeling my orgasm building within me."
    m "Finally, I cried out in ecstasy, my body shaking uncontrollably as wave after wave of pleasure washed through me. Even as I came down from my peak, Remy kept licking, prolonging my pleasure until I begged him to stop."
    m "I collapsed back against the chair, panting heavily as he retracted his snout from between my legs."
    m "Blinking up at me, his snout shiny with my fluids, he blushed furiously."
    m "After a moment, he pulled further away, cleaning his tongue on the roof of his mouth as I panted."
    m "He looked embarrassed, but also pleased with the result of his efforts."
    Ry shy b "How did that feel?"
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
    jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_suck_him:
    m "With a gentle push, I guided him to lie flat on his back."
    m "The sight of his throbbing erection standing tall and proud made my heart skip a beat."
    Ry shy b "Are you... going to...?"
    c "If you want me to."
    m "Wrapping my fingers around his shaft, I began to stroke him in time with the rhythm of his heartbeat, watching my fingers glide up and down his length over all his copious lubrication."
    m "My own desire grew the more I saw the pleasure I caused him, his pupils dilating and tongue flickering against his upper lip."
    m "Finally, I paused, looking up into his eyes and smiling as I spoke."
    c "Ready?"
    Ry smile b "Y-yes."
    m "I pressed my lips against his tip, immediately savoring the sweet taste of his pre and the warmth of his body, his veins throbbing beneath my touch."
    m "Swirling my tongue around his girth, I took in as much of him as I could, wanting to savor the moment and taste him properly."
    m "He moaned softly, his hips twitching a little as his erection jerked with pleasure from my ministrations."
    c "Keep going?"
    Ry smile b "... Yes."
    m "Nodding, I retreated from his tip, then settled into a slow rhythm of sucking and swallowing, bobbing my head in time to his heartbeat while maintaining eye contact with him throughout."
    m "Every few moments, I glanced up to meet his gaze, smiling at him and giving him the occasional reassuring pat on his thigh."
    m "Eventually, his body stiffened and he cried out softly, filling my throat with his hot seed. I choked, swallowing quickly as much as I could before pulling away entirely."
    m "Collapsing beside him, I wiped the corner of my mouth with the back of my hand, laughing lightly at the absurdity of the situation."
    m "He lay there beside me, panting heavily, his snout bright red where my cum had dripped from his nose and mouth."
    Ry shy b "Did... did you enjoy it?"
    m "Burying my head in my arm, I smiled."
    c "Absolutely."
    m "Our hearts pounded together, sweat covering our naked bodies in an intimate bond of shared lust and emotion."
    Ry shy b "Can I... can I get inside of you now?"
    m "Raising my head, I looked at him, seeing the vulnerability in his eyes and the eagerness in his voice."
    c "Please."
    m "He carefully positioned himself behind me, sliding a long, cool finger into my entrance."
    m "I gasped, my body shivering from the sudden chill."
    Ry shy b "Sorry... It's been so long, I forgot how cold it feels like this."
    m "Shrugging, I turned to look at him with a grin."
    c "Don't worry about it."
    m "Positioning ourselves once more, I braced my arms and knees against the floor and waited for him to enter me."
    m "Slowly, I felt the head of his penis press against my opening."
    Ry shy b "Am I... am I hurting you?"
    m "No,"
    jump todo_out_of_content_bangok_four_remy4


label todo_out_of_content_bangok_four_remy4:
    play sound "fx/system3.wav"
    s "You've reached the end of the content currently available for this character."
    s "Roll back or prepare to crash."
    $ renpy.error("End of content reached.")