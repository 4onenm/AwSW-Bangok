init python in bangok_four_remy4_store:
    path = None # type: Optional[Literal["tongue","vaginal","anal"]]

    inside_asked = False # type: bool

    protection = False # type: bool

    player_finished = False # type: bool
    remy_finished = False # type: bool

# == No more tongue path ==
# Remy is on his back on the couch
# (Optional) Handjob Remy's shaft (no climax -- he asks for more and/or to satisfy you)
# (Optional) Lick Remys shaft (no climax -- he asks for more and/or to satisfy you)
# (Optional) Frotting / Hotddogging (+climax jump over fuckings)
#  -> male assfuck
#  -> female vaginal receive
#  -> both anal receive
# Merge: Collapse on the couch in each others' arms

# == More Tongue path ==
#  -> male unprotected
#  -> male protected (TODO, just add a hint of player condom to unproteted and rewrite)
#  -> female
# Merge: kiss, compliment, taste
# if remy_finished: Conclude. Else: Remy's Reear
    
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
            jump todo_out_of_content_bangok_four_remy4

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

    m "I moved a little closer to Remy's hindquarters, spreading his legs a little wider to give me better access to his groin."
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
        scene bath with Fade(0.5)
        $ renpy.pause (0.5)
        play sound "fx/box.wav"
        m "The bottle of lube was exactly where he'd said. It seemed surprisingly large, until I remembered the size of dragonhoods it may need to be serving."
        scene o4 at Pan((0,220), (0,250), 1)
        show remy shy ud
        with Fade(0.5)
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
                "My pussy can take it.":
                    $ bangok_four_remy4_store.path = "vaginal"
                "My pussy wants to try.":
                    $ bangok_four_remy4_store.path = "vaginal"
                "My ass can take it.":
                    $ bangok_four_remy4_store.path = "anal"
                "My ass wants to try.":
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
        m "Then, finally, I fely my balls ghost over his scaly slit and, with a final grunt of effort, I pushed myself down into his lap."
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
        yalign 1.0
        linear 3.0 yalign 0.8
        linear 3.0 yalign 0.9
        linear 2.8 yalign 0.7
        linear 2.8 yalign 0.8
        linear 2.6 yalign 0.6
        linear 2.6 yalign 0.7
        linear 2.4 yalign 0.5
        linear 2.4 yalign 0.6
        linear 2.2 yalign 0.4
        linear 2.2 yalign 0.5
        linear 2.0 yalign 0.3
        linear 2.0 yalign 0.4
        linear 1.8 yalign 0.2
        linear 1.8 yalign 0.3
        linear 1.6 yalign 0.1
        linear 1.6 yalign 0.2
        linear 1.4 yalign 0.0
        linear 1.4 yalign 0.1
        linear 1.2 yalign 0.0
        linear 1.2 yalign 0.1
        block:
            linear 1.0 yalign 0.0
            linear 1.0 yalign 0.1
            repeat
    with None
    $ renpy.pause (2.0)
    m "Remy's eyes fluttered shut as I began to ride him, his breath coming in ragged gasps as he tried to hold back his own climax."
    m "His hips began to rock in time with my own, his member throbbing and twitching inside me as I tried to keep my own body from tensing up too much."
    m "My gut was filled with the heat of his member, the stretch of his girth, and the pleasure of his insistent thrusts."
    if bangok_four_playerhasdick == True:
        m "As my own member rubbed against his scaly belly, and his enormous dragonhood ground against something deep inside me, I couldn't help but groan with need."
    else:
        m "My nerves were alight with the pleasure of his member filling my insides, to the point I didn't even need to touch myself to feel the pleasure building."
        m "I groaned with need, trying to keep myself from rubbing my clit against his belly scales as I rode him."
    jump todo_out_of_content_bangok_four_remy4












label bangok_four_remy4_male_unprotected_tongue_path:
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
        "Lick his shaft's base.":
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
    m "Unable to resist the winking invitation of his tight ring of flesh, I leaned in, giving it..."
    jump todo_out_of_content_bangok_four_remy4
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
        linear 2.0 align 0.59
        align 0.59
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
            m "Remy huffed, hidnquarters shivering with need."

    menu:
        "[[Stroke him.]":
            jump bangok_four_remy4_bottom_handjob_late
        "I want you inside me.":
            jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_bottom_handjob:
    show bangok_four_remy4_cg bottom:
        linear 2.0 align 0.59
        align 0.59
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
        linear 2.0 align 0.59
        align 0.59
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


label bangok_four_remy4_floor_cuddle_conclusion:
    m "We lay on the floor together, his wings and tail wrapped around me as we cuddled and caught our breath in each others' embrace."
    stop soundloop fadeout 5.0
    $ renpy.pause (4.0)
    m "As our breathing faded into quiet, I felt the rise and fall of his warm chest against my arm, and never wanted to let go."
    m "Remy nuzzled the top of my head, then gave me a lick."
    Ry shy ud "[player_name]..."
    m "I looked up to meet his gaze."
    Ry shy ud "Can I stay here, tonight?"
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

# The below is a scene novelization as co-authored by 4onenm
# and openhermes-2.5-mistral-7b.Q4_K_M.gguf for use in generating ideas.
# <|im_start|>user
# Recite the Remy sex scene from the sex lewd NSFW mod for AwSW, the dragon dating simulator. Remember, Remy is the adorkable nerd dragon. This scene happens in the player's house, shortly after you and Remy share your first kiss together.<|im_end|>
# <|im_start|>assistant
# I took the lead this time, hugging his neck and planting a kiss right on the tip of his snout, eliciting a beautiful blush that reached his ears.

# "I-I don't know how far you plan on taking this," Remy fretted. "As a dragon, I'm a little bit larger than you are..."

# "We'll make something work," I reassured.

# Remy smiled. "Well, if it's what you want, let's try something simple for now. I'm not sure how far we can go with your clothes on you..."

# "Let me take care of that." I cautiously stripped, trying not to frighten him with how different my human body was from his draconic scales.

# "You're... perfect." Remy breathed. Then he blushed. "We could start by just... cuddling? Getting used to the feel of our bodies against each other like this?"

# "That sounds wonderful," I agreed.

# Remy shifted onto his back on the couch, spreading his wings and four limbs out to accept me. Between his hindlegs, I could see the tip of something pink just peeking out. But for now, I focused on climbing onto his chest without hurting him or myself as I hugged just above his forelegs. As soon as I was safely nestled in a hug between his forelegs, he wrapped his wings around us both like a cocoon and pulled me even closer against his underbelly scales. "Is this okay? If it's too much..."

# "It's perfect," I said, "Just... like this."

# We lingered there for some time, his breathing and our heartbeats the only sounds as he gently nuzzled his snout against my head beneath his wings. His heat suffused the space, and slowly I began to feel my own body warm, my heart beating faster. Between my legs, I felt my hardness becoming difficult to ignore as I couldn't find a position it didn't press against his belly scales.

# Remy seemed to notice the way my breathing was changing and started to nuzzle more insistently at my neck. His warm tongue traced lazy patterns along the exposed skin, sending shivers down my spine.

# "Ready to move on?" I asked, trying not to sound as breathless as I felt. Remy nodded, his eyes bright with anticipation and nerves. "Then let's try something."

# Remy unfolded his wings, allowing me to slip off of him, to examine what I'd be working with between his legs. A large, pinkish shaft glinted in the light of the room, its head already dribbling a droplet of thick, clear fluid. His balls were also quite large and plump, hanging low beneath it.

# "You're... so beautiful like this," Remy observed, exploring me with his eyes from my face down to the hard erection between my legs, then jumping back up to my face with a deepening blush.

# I smiled back. "As are you." Then I took his large draconic member in my hands, stroking the length from base to tip as he moaned softly with every stroke. His wings fluttered and twitched with anticipation.

# "Remy," I whispered into his ear, feeling the hard, slick flesh of his member beneath my hands. "I want you inside me."

# He let out a surprised gasp. "Y-You're sure? You can see how big... I mean..."

# "I know, but I need be sure I can satisfy you," I insisted with determination.

# Remy nodded nervously. "A-At least let me go find lubrication. L-Lots of..."

# I stepped back from the couch to let him get up, then examined the couch to try to pick a position while he moved to the bathroom to get the lube. Remy returned with some lubricant carried in his mouth.

# "Um... How do you want to start?" He asked, looking up at me nervously. "I mean... You're so much smaller than me..."

# I nodded and approached him. "Let's try it this way first." I said, guiding Remy onto his back with a gentle push on the couch cushions. Once he was settled, I sat astride his hips facing him, my erection pressing against his belly scales.

# "Do you want to touch yourself while I prepare?" I asked. "It may take me some time since this is my first time with your... size."

# He nodded and began to gently stroke himself with his hindlegs as I applied lube liberally to my asshole, then slowly worked a finger inside myself to spread it around the tight ring of muscle that would accept him.

# I could feel his growing heat beneath me as I prepared. I couldn't wait to feel it inside me... if I could fit his enormous length at all! But finally, I felt ready and positioned my tight human sphincter over the head of Remy's erection. I squirted a few more spurts of lube onto his tip, breathing hard as I anticipated the moment of penetration.

# "Are you... ready?" Remy asked nervously. His eyes behind his glasses were wide with eagerness and concern.

# I nodded, taking a deep breath. "Yes." And slowly lowered myself down on him. The head of his extremely well-lubed penis slipped out of my asscrack immediately, but I tried again, struggling to keep a grip on it to line up.

# Remy panted and blushed deeper, watching me with wide eyes. Then he took the initiative and gently held his shaft more firmly in place with his hindlegs, supporting my thighs with his forelegs. "Keep trying?" He suggested. "I-If it's too much..."

# "It's okay," I insisted. "Just... give me a moment." I took another deep breath and began to lower myself onto him again, slowly sinking down and stretching my sphincter around his girth. Then my sphincter began to relax. With a shudder of lust and arousal, I impaled myself on Remy's dragon cock, feeling the thick shaft stretch me out like no human dick ever could. It pushed through into my colon with just a little discomfort, straightening it out until I felt my belly bulge slightly from the inside. But I kept pushing, straining my poor sphincter around his girth until finally, I was sitting on Remy's lap, impaled completely by his dragon cock. My balls rested against his slit, and his balls agaisnt my rear. "Nngh. It's... in," I gasped, panting.

# "Y-You did it!" Remy marveled, awe-struck and blushing deeper than before. Then he wrapped me up in his wings again and pulled me into an embrace, burying his face in my neck as we both panted heavily. "This is... incredible," he murmured.

# "It's a tight fit," I agreed, trying to catch my breath. "But it feels amazing."

# Remy looked up at me from beneath the curve of his wings. His eyes were wide and filled with emotion, and his blush reached halfway down his neck. "I... want you so much right now..." He murmured. Then he began to thrust gently, lifting and lowering his hips to match my own shallow breaths.

# "R-Remy," I gasped. "T-Too much. We should probably change position if we're going to actually fuck."

# He nodded quickly, panting with arousal as he held me to his belly, then slipped off the couch. I grunted as he laid me on the couch cushions, pinning me beneath his weight and between the seat back and his hips. "Is this good?" He asked nervously.

# "Better," I agreed, rubbing his belly before reaching down to pull my thighs wider apart with a groan of discomfort. My asshole felt like it was being ripped open as he pushed into me again.

# "I-I don't want to hurt you..." Remy whimpered, panting heavily and looking at me nervously as his eyes traced the lines of my body beneath him.

# "You won't," I reassured him, reaching out to cup his face gently in my hands before pulling him into a kiss.

# When our lips broke, he gently began to push again. I moaned softly, feeling my sphincter stretch wide around his girth and my insides twist with the intrusion of his long shaft. Running a hand down my chest, I felt the bulge where his tip pressed against my belly from the inside. "Nngh... Remy," I gasped, panting as he thrust into me more deeply.

# Remy pulled back, hesitating. Then when he saw only affection and need in my eyes, he pushed forward again, this time slightly faster, slightly harder. I cried out softly with each new thrust, feeling his girth stretch the walls of my insides to their limits. But it felt so good! I almost didn't even feel his belly scales rubbing across my member as all I could focus on was the thick shaft of his cock filling me up from behind.

# "F-Feels... so... good..." I gasped, panting and moaning through every long, slow thrust. My heart raced with excitement and lust.

# Remy blushed deep red, his eyes wide and full of emotion as he looked into mine. His breathing was ragged too, matching my own. "I-It does... for me too..." He murmured, panting hard before kissing me again, our lips colliding in a passionate embrace.

# After a few more thrusts, Remy's hips began to move faster and harder. I grunted now, feeling his balls plap lightly against my rear as my guts twisted around the thick shaft of his cock. "Nnh!" I gasped, moaning through each hard shove past my prostate. Then I was cumming all over our bellies, unable to hold back my moans of lust and pleasure any longer.

# Remy's thrusting grew even more erratic as he neared his own climax, panting heavily with the effort of fucking me so deeply and passionately. "[player_name]... Oh [player_name]..."

# "I-it's okay," I moaned breathlessly, barely cogent in the throes of my orgasm as Remy thrust harder into me. "I want... I-I need..."

# Remy whimpered, then began thrusting even harder, his heavy balls slapping my rear. I felt my belly with a hand, felt his tip punishing my guts over and over for my lust. He reached the edge of climax soon after me, panting and moaning as our hips crashed together again for the last few times before he came. His balls clenched, hard shaft twitching and pulsing, then thick, hot jets of seed began spurting into my abused colon as Remy tried to muffle his own groans of pure pleasure.

# "NNGH!" I held my belly with both hands, feeling each pulse of cum deep inside me stuffing my intestines more full of his seed. "Remy... Aaahh..."

# Finally, our orgasms subsided as Remy collapsed against me, panting heavily and blushing a bright red under his white scales. He stayed buried in me a while longer before slowly withdrawing his enormous member from my battered asshole.
