
# Table of contents:
# Anna oral: Line 208. Tags used: Cloacas
# Male player oral: Line 353
# Female player oral: Line 466. Tags used: Cerv pen
# Anna fingering: Line 523. Tags used: Cerv pen (Note: Scene is diffrent if done fingering in Anna2)
# Male player tailfuck: Line 839
# Female player tailfuck: Line 969. Tags used: Cerv pen
# Anna riding male player: Line 1179. Tags used: Knots
# Afterglow: Line 1275

init python in bangok_anon_anna4:

    unplayed = True

    anna4choices = 0

    annaride = False
    playerride = False

    annaoral = False
    playeroral = False
    annafinger = False
    tailfuck = False

    tailinwomb = False


label bangok_four_anna4_replay_start:
    scene black with dissolve
    play music "mx/anna4.ogg" fadein 2.0
    $ renpy.pause(0.5)
    scene o at Pan((0, 250), (0, 250), 0.1)
    show anna smirk
    with dissolvemed

    jump bangok_anon_anna4_start


label bangok_anon_anna4_skipmenu:

# Hook from:
# An face "Alright, alright. So fussy."

stop music fadeout 1.0
$ renpy.pause (0.3)
play sound "fx/system3.wav"
s "Watch BangOk scene or skip to end?"
menu:
    "Yes. I'd like to lewd Anna":
        play sound "fx/system3.wav"
        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
        play music "mx/anna4.ogg" fadein 2.0
        jump bangok_anon_anna4_start

    "No. Skip to the end.":    
        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
        scene black with dissolvemed
        $ renpy.pause (2.0)
        $ mp.annaromance = True
        $ mp.save()
        $ annastatus = "good"
        $ annascenesfinished = 4
        stop music fadeout 2.0
        $ renpy.pause (0.5)
        if chapter4unplayed == False:
            jump chapter4chars
        elif chapter3unplayed == False:
            jump chapter3chars
        elif chapter2unplayed == False:
            jump chapter2chars
        else:
            jump chapter1chars
        

label bangok_anon_anna4_start:

# An face "Alright, alright. So fussy."
An smirk "Now, let's get these off you."
m "Giving me a seductive look, Anna began to undress me. She started by unbuttoning my shirt, tossing it onto the couch."
c "Uh, shouldn't we at least go to the bedroom first?"
m "Wordlessly, Anna took ahold of my wrist and led me to the bedroom."
m "Then as soon as we got to the bedroom, she pushed me onto the bed and wasted no time, continuing to undress me."
play sound "fx/undress.ogg"
if bangok_four_playerhasdick == None:
    m "She proceeded to take off my pants, then underwear to reveal…"
    menu: 
        "My dick.":
            m "She proceeded to take off my pants, then underwear to reveal{fast} my dick."
            $ bangok_four_playerhasdick = True

        "My cunt.":
            "She proceeded to take off my pants, then underwear to reveal{fast} my cunt."
            $ bangok_four_playerhasdick = False

else:
    if bangok_four_playerhasdick == True:
        m "She proceeded to take off my pants, then underwear to reveal my dick."

    else:
        m "She proceeded to take off my pants, then underwear to reveal my cunt."

if bangok_four_anna2.unplayed == True:
    if bangok_four_playerhasdick == True: # Male and didn't do the Anna 2 scene
        An "You're definitely smaller than I'm used to, but I'm sure we'll still find a way to enjoy each other."
    else: # Female and didn't do the Anna 2 scene
        An "This isn't really what I'm used to, but I'm sure we'll still find a way to enjoy each other."

else: # Did the Anna 2 scene
    An "This time, we're not stopping when you're satisfied.{w} We're stopping when {i}I'm{/i} satisfied."

c "Wait… What about protection?"
An normal "The small amount of data I did get to look at from the tests I did on you showed specifically our immune systems are remarkably similar. So we're fine on that front."

if bangok_four_playerhasdick == True:
    An "You obviously can't get me pregnant, and I don't have any STDs."
else: 
    An "We obviously can't get each other pregnant, and I don't have any STDs."

c "I'm pretty sure I don't have any either."
An smirk "Then we're fine."

if bangok_four_playerhasdick == True:
    m "Unpromptedly, she took hold of my shaft, teasing me with long firm strokes."
    c "O-Oh!"
    m "She continued stroking me, then picking up her pace until I was fully erect."

else:
    m "Unpromptedly, she started lightly fingering me, teasing me by just barely penetrating my outer lips."
    c "O-Oh!"
    m "She continued, fingering me until I was properly aroused."

m "Then she backed off, smirking at me."
An "Since I'm feeling nice, I'll let you choose what we start with."


$ bangok_four_femalepartners += 1
$ bangok_anon_anna4.unplayed = False


label bangok_anon_anna4_beforemenu:

if bangok_anon_anna4.anna4choices == 1:
    An smirk "I'd say that was a good start."
    c "A good {i}start?{/i}"
    An "You didn't think we'd be doing so little, did you?"
    An "You're lucky I'm feeling so generous and letting you pick everything. So, what next?"

elif bangok_anon_anna4.anna4choices == 2:
    if bangok_four_playerhasdick == True: # If male and done two things jump to Anna riding the player
        An smirk "Alright, that's enough foreplay. Now the real fun can begin."
        jump bangok_anon_anna4_playerride
    
    else: # If female and done two things Anna comments baced and what you did and lets you pick a thrid and final choice
        if bangok_anon_anna4.annaoral == True and bangok_anon_anna4.annafinger == True:
            An smirk "I'd say I'm satisfied with that. Now it's your turn."

        elif bangok_anon_anna4.playeroral == True and bangok_anon_anna4.tailfuck == True:
            An smirk "Alright, you've had your fun. Now it's my turn."

        else:
            An smirk "That's both of us, but I could still go for a bit more."
            c "I might be able to as well…"
            An "What will it be then?"

elif bangok_anon_anna4.anna4choices == 3: # F/F excusive to get to this point
    m "Afterward, the two of us collapsed beside each other on the bed, basking in our afterglow."
    jump bangok_anon_anna4_afterglow 

else:
    pass



label bangok_anon_anna4_menu:

menu: 
    "Can I ride you?" if bangok_four_playerhasdick == True and bangok_anon_anna4.playerride == False:
        $ bangok_anon_anna4.playerride = True
        c "Can I ride you?"
        An smirk "Not a chance. I'm being the dominant one, whether you like it or not."
        jump bangok_anon_anna4_menu

    "Can you ride me?" if bangok_four_playerhasdick == True and bangok_anon_anna4.annaride == False:
        $ bangok_anon_anna4.annaride = True
        c "Can you ride me?"
        An smirk "I was already planning to."
        An bangok blush "But not yet. I want to make the most out of this, so you're going to have to wait until I say so."
        jump bangok_anon_anna4_menu

    "Can I eat you out?" if bangok_anon_anna4.annaoral == False:
        $ bangok_anon_anna4.annaoral = True
        $ bangok_anon_anna4.anna4choices += 1
        jump bangok_anon_anna4_anna_oral

    "Can you use your mouth?" if bangok_anon_anna4.playeroral == False:
        $ bangok_anon_anna4.playeroral = True
        $ bangok_anon_anna4.anna4choices += 1
        if bangok_four_playerhasdick == True:
            jump bangok_anon_anna4_player_m_oral
        else:
            jump bangok_anon_anna4_player_f_oral

    "Can I finger you?" if bangok_anon_anna4.annafinger == False:
        $ bangok_anon_anna4.annafinger = True
        $ bangok_anon_anna4.anna4choices += 1
        jump bangok_anon_anna4_anna_finger

    "Can you tailfuck me?" if bangok_anon_anna4.tailfuck == False:
        $ bangok_anon_anna4.tailfuck = True
        $ bangok_anon_anna4.anna4choices += 1
        if bangok_four_playerhasdick == True:
            jump bangok_anon_anna4_player_m_tail
        else:
            jump bangok_anon_anna4_player_f_tail



label bangok_anon_anna4_anna_oral:

c "Can I eat you out?"
if bangok_anon_anna4.playeroral == True and bangok_four_playerhasdick == False:
    An smirk "Since it's only fair you return the favor, go ahead."

elif bangok_four_anna2.lick == False:
    An smirk "Since you're so persistent in wanting to, go ahead."

else:
    An smirk "Alright, go ahead."

$ renpy.pause (0.2)
show anna:
    ease 1.0 xpos 0.2
$ renpy.pause(0.8)
show anna smirk flip:
    ypos 1.3 rotate -15
with dissolve

if persistent.bangok_cloacas == False:
    m "Anna proceeded to lie down on her back on the bed. Spreading her legs, she gave me an unobstructed view of her slit, and asshole, just below it."
else:
    m "Anna proceeded to lie down on her back on the bed. Spreading her legs, she gave me an unobstructed view of her slit."

m "I positioned myself between her legs, face inches from her slit. Anna wrapped her legs around the back of my shoulders, keeping me in place."
show anna bangok blush flip with dissolve
m "I began to tease her, gently licking outside her slit and the area immediately around it."
m "I continued my gentle teasing action, but then Anna put a hand on the back of my head and pushed my face into her."
An smirk flip "Enough of this gentle crap. You're going to have to pick up the pace if you're going to get me off."
m "Following Anna's orders, I picked up my pace, penetrating her slit with my tongue."
An "Good little human."
m "I started moving my tongue faster. Exploring her slick passage."
An bangok blush flip "Your tongue is shorter than a dragon's. It's much softer and thicker though."
m "Realizing this wouldn't be enough for Anna, I tried applying suction."
An bangok lipbite flip "Oh! What was that?"
m "Worried I accidentally hurt her, I stopped and started to lift my head to answer, but was quickly pushed back down."
An "No, don't answer.{w=0.8} W-Whatever it was, keep doing it."
m "I obliged, regaining my seal and inserting my tongue in her slit again."
An "Fuck, that's… definitely new."
m "Anna bit her lip as if she was trying to hold herself back. But the subtle noises coming from her and how wet she was told me all I needed to know."
An "Ngh…"
m "She pushed me even further into her. Her juices covering my tongue, mouth, and part of my face. I explored deeper, feeling her slit lightly clench down on my tongue."
if persistent.bangok_cloacas == True:
    m "I then shifted my attention to her anal passage. The suction and slight penetration caused her to shudder."
$ renpy.pause (0.5)
m "I kept up my action, getting a good taste of her slit juices, but then I was suddenly interrupted…"

play sound "fx/bed.ogg"
scene bangok_anon_o_ceiling at Pan((0,360), (0,120), 1.5) with dissolvemed
$ renpy.pause (1.7)
show anna smirk at Position(ypos=1.5) with easeinbottom
show anna:
    ease 1.2 ypos 1.4 zoom 1.3
$ renpy.pause (0.5)
m "Anna let me go and flipped both of us over. So she was now the one on top, and I was lying beneath her."
An "You've asked for this…"
show anna smirk at Position(ypos=1.1) with ease
$ renpy.pause (0.2)
show anna smirk:
    ease 1.5 zoom 1.7
m "Anna moved up me, putting her knees on either side of my head, and leaking slit right above my face."
An "Now, let's put that mouth of yours to work."
show anna:
    ease 1.5 ypos 1.05 zoom 2.3
m "She proceeded to put a hand around the back of my head again, simultaneously pulling me up to her and lowering herself down."
m "I regained my seal and continued where I'd left off."
An bangok lipbite "Ah! Damn… T-That's…"
m "Anna was at a complete loss of words from the completely new sensation I was providing her."
$ renpy.pause (1.5)

show anna:
    ease 1.3 ypos 1.0
    ease 1.3 ypos 1.05
    repeat

m "Trying to get the most out of this, Anna began to grind herself against my face. It made it more of a challenge to hold my seal, but I managed."
m "Suddenly, instead of pushing the back of my head, she grabbed my hair and started pulling me into her."
menu:
    "[[Stop her.]":
        play sound "fx/slap1.wav"
        show anna sad with dissolve
        show anna:
            ease 1.0 zoom 1.7 ypos 1.2
        m "I slapped her hand away and moved so I could speak."
        c "Please don't pull my hair like that. It's really painful."
        if bangok_four_hornincident == True:
            c "It would be like if I grabbed your horns and pulled you by them."
            An face "In hindsight, I really should have assumed that… Sorry."

        else:
            An face "In hindsight, I really should have assumed that considering grabbing someone by the horns is also rather unpleasant… Sorry."
            $ bangok_four_hornincident = True

        c "You can still push the back of my head. Just don't pull my hair."
        $ renpy.pause (0.5)
        show anna bangok blush with dissolve
        show anna at Position(ypos=1.0) with ease
        $ renpy.pause (0.2)
        show anna bangok blush with dissolve
        show anna:
            ease 1.2 zoom 2.3 ypos 1.05
        m "I moved back to my original position and Anna slowly picked up her pace again."
        show anna:
            ease 1.3 ypos 1.0
            ease 1.3 ypos 1.05
            repeat
        $ renpy.pause (2.2)
        An bangok lipbite "Mmhh…"
        
    "[[Let her.]":
        m "Her now doing this, I was even deeper inside her. My teeth just barely ghosting her slit, causing her to shudder."
        An "Nngh!"

m "I tried experimenting with using more suction, and an appreciative moan from Anna assured me it was the right thing to do."
An "F-Fuck… Almost…"
$ renpy.pause (3.0)
show anna:
    ease 0.6 zoom 2.5 ypos 1.15
show anna orgasm with dissolve
play sound "fx/snarl.ogg"
m "Suddenly Anna dropped most of her weight on me, and her canal clamped down on my tongue. She let out a roar, and soaked my face with her juices."
$ renpy.pause (2.0)
show anna bangok lipbite with dissolve
m "After coming down from her orgasm, her canals grip on my tongue relaxed, and she slowly got off of me."
$ renpy.pause (1.5)
scene black with fadequick
$ renpy.pause (0.3)
scene o at Pan((0, 250), (0, 250), 0.1) with dissolveslow
show anna smirk flip at Position(xpos=0.2) with dissolve
$ renpy.pause (0.5)
An "Now that...{w=0.5} was definitely something."
An bangok blush flip "Considering the size and shape of your tongue, that was much better than I thought it would be."
An smirk flip "Now, tell me… What the hell was that you did that suddenly made it so much better?"
c "Suction. Human lips can seal really well. So, I'm guessing you've never felt anything like that before?"
An "No, that was completely new."
$ renpy.pause (1.0)
show anna at center with ease
show anna normal flip with dissolve
$ renpy.pause (1.0)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_player_m_oral:

c "Can you use your mouth on me?"
An bangok blush "Alright. I guess I get to find out how much a human's taste differs from a dragon's."
$ renpy.pause (0.5)
play sound "fx/undress.ogg"
$ renpy.pause (1.0)
show anna at Position(xpos=0.6, ypos=1.1) with ease
show anna at Position(ypos=1.3) with ease
$ renpy.pause (0.5)
m "I sat on the edge of the bed as Anna got off and sunk to her knees in front of me."
show anna smirk with dissolve
show anna:
    ease 1.5 ypos 1.48
    ease 1.5 ypos 1.49
    repeat

m "Instead of taking me in her muzzle, she started teasing me by licking up and down the length of my member. Her tongue felt slightly coarse, but thankfully just enough to result in more pleasure than discomfort."
$ renpy.pause(3.5)
show anna bangok orgasm with dissolve
show anna:
    ease 1.0 ypos 1.5
m "Then she took me in her muzzle, and I got a thrill from the danger of her teeth just ghosting my tip and shaft."
m "She started by only taking me in a shallow amount. Her tongue wrapped around just past my tip, exploring and tugging on my member."
show anna:
    ease 1.0 ypos 1.52
m "Then she took me even deeper, her tongue forming a tight ring near the base of my length. I couldn't help but let out a quiet moan and thrust a little into her face."
m "She then placed her hands on my thighs. Simultaneously bracing herself and holding me in place."
show anna:
    ease 1.0 ypos 1.54
if bangok_four_anna2.doneoral == True:
    m "Then she took me in even deeper into her throat than last time. Her nose pressing into my groin and lips just grazing my balls."
else:
    m "Then she took me in even deeper into her throat. Her nose pressing into my groin and lips just grazing my balls."
c "O-Oooh…"
$ renpy.pause (1.0)
show anna:
    ease 1.0 ypos 1.51
m "Afterward, she started moving backwards, her tongue just passing back over my tip."
menu:
    "[[Grab her horns.]" if not bangok_four_hornincident:
        $ bangok_four_hornincident = True
        show anna disgust with dissolve
        m "Thinking Anna was already pulling away, I took hold of her horns and tried pulling her back into my groin. But she was having none of it and slapped my hands away."
        play sound "fx/slap1.wav"
        $ renpy.pause (0.2)
        show anna at Position(ypos=1.25) with ease
        An face "You could have at least asked to grab my horns first. With someone less experienced that wouldn't have ended well for you."
        c "What do you mean?"
        An sad "It's a sensitive area. There's a biological drive to keep them from getting ripped off our heads, so using them to control our head's motion is... undesirable."
        c "Right, sorry. Can I grab your horns then?"
        An normal "No, I'd prefer to be the one in control."
        $ renpy.pause (1.0)
        show anna bangok orgasm with dissolve
        show anna at Position(ypos=1.51) with ease
        m "Not too long after, Anna descended back onto my groin, taking my member back into her mouth."

    "C-Can I grab your horns…?":
        c "C-Can I grab your horns…?"
        m "Without moving any further up she dismissively shook her head, causing my member to partially exit her muzzle for a few brief moments."
        m "I was disappointed but respected Anna's wishes of not grabbing her horns.{w} My disappointment didn't last long though."

    "[[Enjoy.]":
        pass
    
play soundloop "fx/rub2.ogg" fadein 1.5
show anna:
    ease 0.75 ypos 1.52
    ease 1.0 ypos 1.50
    ease 0.4 ypos 1.52
    ease 0.6 ypos 1.50
$ renpy.pause (2.75)
show anna:
    ease 0.25 ypos 1.52
    ease 0.4 ypos 1.50
    repeat

$ renpy.pause (2.0)
m "Anna then picked up her pace, facefucking herself even faster onto my cock, and reforming the ring with her tongue."
m "With her lips closed over my member and the ring of her tongue, it was like my member was being fucked twice at once in her mouth."
m "I couldn't help but moan and throw my head back in pleasurable bliss."
c "A-Ah!"
m "Her tight tongue ring kept moving up and down my shaft, milking and tugging it, bringing me closer to my limit by the second."
$ renpy.pause (6.0)
stop soundloop fadeout 0.5
show anna bangok blush at Position(ypos=1.3) with ease
show anna smirk with dissolve
m "But just as I was about to reach my climax, Anna pulled away completely. She held the base of my shaft with a firm grip, only allowing a small drop of pre to leak out."
$ renpy.pause (1.5)
show anna at Position(ypos=1.1) with ease
show anna:
    ease 1.0 xpos 0.5 ypos 1.0

if bangok_anon_anna4.tailfuck == True:
    $ renpy.pause (2.5)
    c " Edging me {i}this{/i} much is just cruel."
    An smirk "Fine. If you're going to complain so much, then that's enough foreplay."
    jump bangok_anon_anna4_playerride

else:
    c "Hey!"
    An smirk "What? Have you not heard of edging before?"
    c "Well, I have…"
    An bangok blush "Then stop complaining that you get to enjoy this even more."

$ renpy.pause (1.0)
show anna normal with dissolve
$ renpy.pause (1.0)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_player_f_oral:

c "Can you use your mouth on me?"
if bangok_anon_anna4.annaoral == True:
    An smirk "Well, it's only fair that I return the favor, right?"
else:
    An bangok blush "That's probably what I have the least experience with, but I'm confident I can get you off regardless."

m "I sat on the edge of the bed as Anna got off and sunk to her knees in front of me."
show anna at Position(xpos=0.6, ypos=1.1) with ease
show anna at Position(ypos=1.3) with ease
show anna smirk with dissolve
show anna:
    ease 1.0 ypos 1.50
m "I spread my legs, giving Anna easy access to my groin, and almost immediately, she started teasing me by just licking my outer vaginal lips. Her tongue felt slightly coarse, but thankfully just enough to result in more pleasure than discomfort."
m "She then placed her hands on my thighs. Simultaneously, bracing herself and holding me in place, as she continued to tease me, only penetrating my pussy a shallow amount."
show anna at Position(ypos=1.51) with ease
m "Then she started going deeper, her tongue just brushing my clit as she went in, causing me to shudder and moan appreciatively."
c " A-Ah!"
m "She continued licking around that area for a decent amount of time, keeping up a maddeningly teasing sensation, making me desperately want her deeper."
show anna:
    ease 1.5 ypos 1.52
m "I started to push down into Anna's tongue, which she took as an invitation to go even deeper, opening her mouth wider as not to scratch me with her teeth."
m "She picked up her pace, licking and exploring inside my wet passage, trying to find that sweet spot in me."
if persistent.bangok_cervpen:
    m "Then the tip of her tongue just flicked my cervix, causing me to moan again. I threw my head back and was temporarily paralyzed due to the sheer pleasure."
    m "She continued flicking my cervix with her tongue. Each time sending a wave of pleasure through my body, and bringing me closer to my limit by the second."
    $ renpy.pause (2.5)
    show black with fadequick
    m "Suddenly, my canal clenched down on her tongue, soaking it with my juices. Despite the extra friction, Anna still managed to push the tip of her tongue against my cervix."

else:
    m "Then the tip of her tongue flicked against my deeper inner walls, causing me to moan again. I threw my head back and was temporarily paralyzed due to the sheer pleasure."
    m "She continued flicking deep within me with her tongue. Each time sending a wave of pleasure through my body, and bringing me closer to my limit by the second."
    $ renpy.pause (2.5)
    show black with fadequick
    m "Suddenly, my canal clenched down on her tongue, soaking it with my juices. Despite the extra friction, Anna still managed to push the tip of her tongue as deep as she could within me."

hide black with dissolveslow
$ renpy.pause (0.5)
m "Anna slowly withdrew her tongue while I was still in the aftershock of my orgasm."
show anna bangok blush with dissolve
show anna at Position(ypos=1.3) with ease
show anna at center with ease
show anna smirk with dissolve
$ renpy.pause (0.5)
An "So, how was that?"
c "I'll never be satisfied by another human eating me out again."
An "Glad to hear it."
$ renpy.pause (1.0)
show anna normal with dissolve
$ renpy.pause (2.0)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_anna_finger:

c "Can I finger you?"
if bangok_four_anna2.annacame == True:
    An smirk "Oh, I'll gladly go for a round two with your arm."
    show anna at Position(xpos=0.25) with ease
    show anna bangok blush flip with dissolve 
    m "Anna got off the bed and stood next to it, gesturing for me to get up too."
    An "Kneel here, and brace your elbow on the bed this time."
    c "Yes ma'am."
    An smirk flip "Good little human."
    show anna smirk with dissolve
    m "I knelt and braced my elbow as instructed. Anna lined her already wet slit up with my hand, one of her legs coming down in front of me, and the other on the bed supporting her."
    show anna:
        ease 1.2 ypos 1.01
    m "Instead of starting slowly as I expected, Anna immediately tried taking in my entire hand at once."
    c "W-Wait, shouldn't you be easing into it instead of trying to take my entire hand?"
    An "Why would I? You know I can take your whole arm. And after last time, you're not starting with teasing me again."
    m "I obliged, folding my thumb into my hand. Anna then began to sink herself down onto my hand, stopping as her slit closed over my wrist."
    show anna:
        ease 1.2 ypos 1.02
    $ renpy.pause (0.5)
    An bangok lipbite "Ngh…"
    m "Her slit clenched down on my wrist, and again, more of her fluids began to leak out of her and soak my hand and arm. Just like last time I spread the natural lubricant along my arm, preparing it for what was to come."
    show anna:
        ease 1.2 ypos 1.04
    m "Anna took even more of her arm inside her. The mussels in her passage began to lewdly squeeze and press in on my arm."

    if bangok_four_anna2.fisting == True:
        m "Just like last time, I made my hand into a fist."
        An "Mmh… Good…"
        $ renpy.pause (0.5)
        show anna:
            ease 1.2 ypos 1.02
            ease 0.4 ypos 1.06
        m "Anna then lifted herself up, and came back down fast."
        show anna bangok orgasm with dissolve
        An "A-Ah! F-Fuck!"

    else:
        m "Instead of doing what I did last time, I tried making my hand into a fist instead."
        An sad "What are you…?"
        m "Anna shifted around, trying to get a feel for the new position of my hand."
        An bangok blush "Hm."
        show anna:
            ease 1.0 ypos 1.02
            ease 0.4 ypos 1.06
        m "Anna lifted herself up. Then switched directions, coming down fast."
        show anna bangok orgasm with dissolve
        An "F-Fuck! Yes!"

    show anna bangok lipbite with dissolve
    show anna:
        ease 0.7 ypos 1.02
        ease 0.5 ypos 1.04
    show anna:
        ease 0.4 ypos 1.02
        ease 0.25 ypos 1.04
        repeat

    play soundloop "fx/rub2.ogg" fadein 3.0
    m "Anna began to fuck my wrist and arm again. But this time she didn't start as slowly nor needed time to adust."
    $ renpy.pause (2.5)
    m "Her inner muscles squeezed tightly in on my arm and her juices started to dribble even faster down my arm."

    if persistent.bangok_cervpen:
        m "Once again, my fist was being thrust against the resistance of her cervix. Each time my hand pushed a little further through."
        An "F-Fuck, a-almost…"
        $ renpy.pause (4.0)
        show anna bangok orgasm at Position(ypos=1.07) with ease
        stop soundloop fadeout 0.5
        play sound "fx/snarl.ogg"
        m "Suddenly, Anna thrust herself down even harder, punching my hand through her cervix again. Her canal clamped down on my arm, she roared, and her tail slapped against the bed."
        $ renpy.pause (2.0)
        show anna bangok lipbite with dissolve 
        $ renpy.pause(1.0)
        m "After her orgasm, Anna took a moment to rest and catch her breath."
        An smirk "I've said it before, but your arm really is something. I'm pretty sure I'll never get tired of doing that."
        $ renpy.pause (0.5)
        show anna bangok orgasm with dissolve
        show anna:
            ease 1.8 ypos 1.1
        $ renpy.pause(1.8)
        show anna bangok lipbite with dissolve
        show anna:
            ease 1.5 ypos 1.07
            ease 1.5 ypos 1.1
            ease 1.5 ypos 1.07
            ease 1.5 ypos 1.1
        m "She took as much of my arm as she could until my hand stopped against her womb. She continued to all but sit on my forearm, occasionally moving around and enjoying the sensation of me being so deep in her while she could."
        $ renpy.pause (3.5)
        show anna:
            ease 1.5 ypos 1.04
        $ renpy.pause (1.0)
        show anna bangok orgasm:
            ease 1.0 ypos 1.07
        $ renpy.pause(1.0)
        show anna bangok lipbite with dissolve
        m "After some time, she eventually did try and get up. Upon my hand leaving her cervix, she faltered, letting her weight fall back onto it. I helped the process along by pulling my arm out for her."
        $ renpy.pause(2.0)
        play sound "fx/uncork.ogg"
        show anna bangok blushpalm at Position(ypos=1.08) with ease
        An "Thanks."

    else:
        m "She kept thrusting even harder onto my arm, each time pushing herself a slight bit deeper each time."
        An "F-Fuck, a-almost…"
        $ renpy.pause (4.0)
        show anna bangok orgasm at Position(ypos=1.08) with ease
        stop soundloop fadeout 0.5
        play sound "fx/snarl.ogg"
        m "Suddenly, she thrust herself down even further. Her canal clamped down on my arm, she roared, and her tail slapped against the bed."
        $ renpy.pause (2.0)
        show anna bangok lipbite with dissolve 
        $ renpy.pause(1.0)
        m "After her orgasm, Anna took a moment to rest and catch her breath."
        An smirk "I've said it before, but your arm really is something. I'm pretty sure I'll never get tired of doing that."
        $ renpy.pause (1.5)
        show anna bangok lipbite with dissolve
        show anna:
            ease 1.5 ypos 1.05
            ease 1.5 ypos 1.08
            ease 1.5 ypos 1.05
            ease 1.5 ypos 1.08
        $ renpy.pause (2.5)
        m "She paused, hilted on my arm, enjoying the feeling of me being so deep inside of her, and moving around occasionally."
        $ renpy.pause (1.0)
        m "I felt a resistance deep inside her, just beyond my fist, one I assumed she wouldn't be tying to mess around with."
        $ renpy.pause (0.5)
        show anna:
            ease 1.7 ypos 1.05
        $ renpy.pause (2.5)
        m "After some time, she eventually did try to get up. She took her time, moving slowly and pausing part of the way through. I helped the process along by pulling my arm out for her."
        $ renpy.pause(2.0)
        play sound "fx/uncork.ogg"
        show anna bangok blushpalm at Position(ypos=1.03) with ease
        An "Thanks."


else:
    An normal "Alright. Just be careful with your nails. I don't want you to scratch me in there."
    c "Unless you're way more delicate than a human, I doubt that will be a problem."
    $ renpy.pause (0.7)
    show anna:
        ease 1.0 xpos 0.2
    $ renpy.pause(0.8)
    show anna flip:
        ypos 1.3 rotate -15
    with dissolve
    show anna smirk flip with dissolve
    $ renpy.pause(1.0)
    m "I approached Anna, who was now lying on her back on the bed, exposing her slit to me."
    m "Slowly, I pressed two fingers inside, continuing my small, gentle circles with the rest of my hand. Anna's legs shuddered slightly, where they were sticking up in the air."
    show anna smirk flip with dissolve
    $ renpy.pause (0.5)
    m "After giving her another moment with this gentle teasing, I added a third finger, finding it slipping in even more easily than the first two as her natural lubrication began to slicken her lips"
    An smirk flip "You were right. Your nails aren't a problem."
    An bangok blush flip "And your skin is much softer than any dragon's scales."
    m "I added a forth finger, which resisted slightly more. But with her natural lubrication it fit, followed by most of my palm."
    An bangok lipbite flip "Mm. Now you're in for it."
    An smirk flip "I want your arm. Let's see what the rest of that soft flesh feels like."
    c "O-Oh, Okay."
    An "Good little human."
    m "I slid in and out the four fingers I had so far, getting her used to the size until my hand was soaked and buried right up to the base of my thumb."
    An bangok blush flip "Let me get up. I have a different idea."
    m "I obliged, pulling out the part of me hand I'd gotten in. And soon after Anna stood up."
    $ renpy.pause (0.5)
    hide anna with dissolve
    $ renpy.pause (0.0)
    show anna bangok blush flip at Position(xpos=0.25, ypos=1.0) with dissolve
    show anna:
        ease 1.0 xpos 0.6
    $ renpy.pause (0.7)
    show anna bangok blush with dissolve
    An "Kneel here, brace your elbow on the bed, here."
    m "I kneeled down next to the bed. Once my hand was in place, Anna made sure my fingers were in the shape I'd used when penetrating her, and that I was keeping them that way."
    show anna at Position(xpos=0.25) with ease
    m "Then she turned around and lined her slick slit back up, one of her legs coming down right in front of me, the other on the bed supporting her."
    $ renpy.pause (0.5)
    show anna:
        ease 1.2 ypos 1.02
    show anna bangok lipbite with dissolve
    An "Nnh!"
    $ renpy.pause (0.5)
    m "The muscles in Anna's passage pressed in lewdly around my hand, squeezing more of her natural lubricant around my wrist and sending it running in small rivulets down my arm."
    $ renpy.pause (0.4)
    An bangok blush "Spread that around."
    m "I did as ordered, trying to more evenly distribute her juices on the next part of my arm. Anna shivered as the fingers of my other hand brushed her slit."
    An smirk "You're still braced against the bed, right?"
    c "Yeah."
    An bangok blush "Good."
    show anna bangok lipbite with dissolve
    show anna at Position(ypos=1.0) with ease
    show anna at Position(ypos=1.04) with ease 
    m "Anna lifted herself up, her clenching almost tugging my arm with her. Just before my fingers were about to leave, she reversed direction and pressed back down, fucking herself onto my hand as if it were a dildo."
    An "Ah!"
    if persistent.bangok_cervpen:
        m "We came up against resistance almost immediately, but this one came from within her."
    else:
        m "She paused, taking a momnent to adjust."

    show anna smirk with dissolve
    m "A glance back from her showed in her face. Whatever this felt like for her, it was a good feeling."
    m "Trying to make this more enjoyable for Anna, I tried turning my hand into a fist."
    $ renpy.pause (0.5)
    An sad "What are you…?"
    m "Shifting around me, Anna felt the additional room I'd bought her to take my arm."
    An bangok blush "Hm."
    show anna bangok lipbite with dissolve
    show anna:
        ease 1.0 ypos 1.02
    m "She lifted up, walls shifting and spreading around the ball of my fist inside her."
    m "Then she switched direction, pressing down fast."
    show anna bangok lipbite:
        ease 0.4 ypos 1.06
    $ renpy.pause (0.3)
    show anna bangok orgasm with dissolve
    An "F-Fuck! Yes!"
    play soundloop "fx/rub2.ogg" fadein 5.0
    show anna bangok lipbite with dissolve
    show anna:
        ease 1.0 ypos 1.02
        ease 1.0 ypos 1.04
        ease 0.7 ypos 1.02
        ease 0.5 ypos 1.04
    $ renpy.pause (3.0)
    show anna:
        ease 0.40 ypos 1.02
        ease 0.25 ypos 1.04
        repeat
    m "Anna began to fuck my wrist and hand, gently at first, then with increasing vigor."
    show anna bangok lipbite with dissolve

    if persistent.bangok_cervpen:
        m "Each time, she thrust my hand against the resistance inside of her harder."
        An "A-Almost..."
        $ renpy.pause(3.0)
        stop soundloop fadeout 0.5
        play sound2 "fx/snarl.ogg"
        show anna bangok orgasm:
            ease 0.3 ypos 1.07
        m "Abruptly, Anna thrust herself down hard enough to finally punch through the resistance. Her tail slapped the bed as a few more inches of my arm disappeared inside of her. The pressure on my hand lessened and the undulating pressure on my arm mounted, a wider section now stuffed into her tight passage."
        m "Anna remained there for several long moments, just catching her breath after the roar she'd done."
        show anna bangok lipbite with dissolve
        $ renpy.pause (1.5)
        An smirk "Phew… Now, that was something."
        An bangok blush "This wouldn't be safe to do with any dragon. Not without a protective cover, because of the scales and sharp claws."
        An smirk "Now, though?"
        show anna bangok orgasm with dissolve
        show anna:
            ease 1.5 ypos 1.1
        $ renpy.pause(1.5)
        show anna bangok lipbite with dissolve
        m "Anna sank further down my arm now soaked with her juices, until she all but sat on my forearm. There was another resistance inside of her, one I assumed she wouldn't be trying to batter through."
        m "For a few moments, she continued to sit with my hand in her womb, and enjoy the sensation of me being so deep in her while she could."
        $ renpy.pause(2.5)
        show anna bangok lipbite with dissolve
        show anna:
            ease 1.5 ypos 1.04
        $ renpy.pause(1.5)
        show anna bangok orgasm with dissolve
        show anna:
            ease 0.25 ypos 1.07
        $ renpy.pause (0.8)
        show anna bangok lipbite with dissolve
        m "After some time, she eventually did try and get up. Upon my hand leaving her cervix, she faltered, letting her weight fall back onto it. I helped the process along by pulling my arm out for her."
        $ renpy.pause(2.0)
        play sound "fx/uncork.ogg"
        show anna bangok blushpalm at Position(ypos=1.08) with ease
        An "Thanks."

    else:
        m "She kept thrusting even harder onto my arm, each time pushing herself slightly deeper."
        An "A-Almost…"
        $ renpy.pause(3.0)
        stop soundloop fadeout 0.5
        play sound "fx/snarl.ogg"
        show anna bangok orgasm:
            ease 0.3 ypos 1.08
        m "Suddenly, she thrust herself down even further. Her canal clamped down on my arm, she roared, and her tail slapped against the bed."
        $ renpy.pause (1.5)
        show anna bangok lipbite with dissolve
        $ renpy.pause (1.0)
        An smirk "Phew… Now, that was something."
        m "As Anna remeined hilted on my forearm, I felt a resistance deep inside her, one I assumed she wouldn't be trying to play with."
        $ renpy.pause (2.0)
        show anna bangok lipbite with dissolve
        show anna:
            ease 1.7 ypos 1.06
        $ renpy.pause (2.5)
        m "After some time, she eventually did try to get up. She took her time, moving slowly and pausing part of the way through. I helped the process along by pulling my arm out for her."
        $ renpy.pause(2.0)
        play sound "fx/uncork.ogg"
        show anna bangok blushpalm at Position(ypos=1.03) with ease
        An "Thanks."

    
$ renpy.pause (0.5)
show anna bangok blushpalm flip with dissolve
show anna at Position(xpos=0.35, ypos=1.02) with ease
$ renpy.pause (0.2)
show anna at Position(xpos=0.4, ypos=1.0) with ease
$ renpy.pause (0.2)
show anna at Position(xpos=0.5) with ease
$ renpy.pause (0.2)
m "After a few uneasy steps, she got back onto the bed, and I followed."
show anna bangok blush with dissolve
An "I need a bit longer to rest after that…"
$ renpy.pause (2.5)
An smirk "Phew… Okay."
$ renpy.pause (2.5)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_player_m_tail:

c "Can you tailfuck me?"
if bangok_four_anna2.tail == True:
    An smirk "So, you enjoyed that small amount I gave you last time enough that you want to know what my whole tail is like?"
    c "Well, not your {i}whole{/i} tail…"
    An bangok blush "Obviously. But more than just teasing you with just the tip."

else:
    An smirk "Oh. I didn't expect you to be into tailplay, given you humans' lack of one. I'm not complaining though."

$ renpy.pause (1.0)
play sound "fx/bed.ogg"
scene bangok_anon_o_ceiling at Pan((0,360), (0,120), 2.5) with dissolvemed
$ renpy.pause (2.5)
show anna smirk at Position(ypos=1.3) with easeinbottom
m "I proceed to lie on my back, and Anna positioned herself between my legs, with her tail pointing towards me."
An bangok blush "First things first…"
m "With a surprising amount of flexibility, Anna curled her tail back towards herself and between her legs. Then she guided it to her slick slit with one of her hands."
c "What are you…?"
An smirk "This won't be as enjoyable without some kind of lubrication, and I want to get something out of this too."
$ renpy.pause (0.5)
show anna bangok lipbite with dissolve
show anna:
    ease 1.2 ypos 1.285
m "Anna then pushed her tail deep inside herself, only slowing down upon reaching a thicker part of her tail."
An "Ngh…"
$ renpy.pause (1.0)
show anna:
    ease 1.0 ypos 1.27
    ease 0.9 ypos 1.3
show anna:
    ease 0.6 ypos 1.27
    ease 0.8 ypos 1.3
    repeat
$ renpy.pause (2.0)
m "She then started thrusting her tail in and out of her passage, literally fucking herself. Each time, more of her juices covered her tail, letting it slide in with less resistance each time."
$ renpy.pause (3.0)
show anna:
    ease 1.2 ypos 1.3
$ renpy.pause (0.5)
show anna smirk with dissolve
m "After continuing for a time, she slowly started to retrieve her now lubricated tail from inside her and aimed it back towards between my legs."
m "She held my waist with both of her hands and poked my asshole with her tail, the tip of it just barely pressing through."
An "Are you ready?"
c "Yes…"
$ renpy.pause (0.5)
show anna:
    ease 1.7 ypos 1.26
m "Starting off slowly, Anna pushed just the tip and a small amount of the length of her tail into me. Thanks to her natural lubrication it entered with ease."
$ renpy.pause (0.7)
show anna:
    ease 1.0 ypos 1.3
    ease 0.7 ypos 1.26
    ease 0.8 ypos 1.3
    ease 0.5 ypos 1.26
$ renpy.pause (0.7)
m "Almost immediately, she experimented with a few shallow thrusts. Catching me by surprise, I couldn't help but let out a slight moan."
c "O-Oh!"
m "Anna took that a sign to push deeper, and try to find the pleasure button within me."
show anna:
    ease 1.3 ypos 1.24
$ renpy.pause (2.5)
show anna:
    ease 1.7 ypos 1.3
$ renpy.pause (0.5)
m "After pushing deeper we reached a thicker part of her tail, which began to stretch my hole more. Then Anna started to pull back."
m "I was worried she was already pulling out, but then she started to fuck me for real, thrusting her tail back and forwards into me."
play soundloop "fx/rub2.ogg" fadein 4.0
show anna:
    ease 1.2 ypos 1.26
    ease 0.8 ypos 1.29
    ease 0.9 ypos 1.24
$ renpy.pause(3.0)
show anna:
    ease 0.5 ypos 1.29
    ease 0.3 ypos 1.22
    repeat
$ renpy.pause (1.5)
c "A-Ah!"
$ renpy.pause (2.0)
m "Now doing this, it didn't take long for Anna to find my sweet spot and bring me closer to my limit by the second."
m "Then she started going even deeper, to a point where her tail was stretching me out even more, just short of the point of pain. She went as far as she could before the lubrication of her juices stopped."
m "The entirety of my lower body was starting to feel numb, due to the speed and depth of her tail, but with each thrust of her tail, came a wave of pleasure being sent through me."
m "At this pace, I knew I couldn't hold on for much longer."
show anna:
    ease 0.5 ypos 1.28
    ease 0.3 ypos 1.2
    repeat
$ renpy.pause (5.5)
stop soundloop fadeout 3.5
show anna:
    ease 0.7 ypos 1.3
    ease 0.5 ypos 1.24
    ease 1.0 ypos 1.3
    ease 0.7 ypos 1.26
    ease 1.3 ypos 1.3
    ease 1.7 ypos 1.28
    ease 1.5 ypos 1.3
$ renpy.pause (3.0)
m "But just as I was about to reach my limit, Anna slowed down, then fully retracted her tail from me, letting my near-climax begin to slowly fade away."
$ renpy.pause (1.5)

scene black with fade
$ renpy.pause (0.3)
scene o at Pan((0, 250), (0, 250), 0.1)
show anna smirk at center
with dissolveslow

$ renpy.pause (1.0)
if bangok_anon_anna4.playeroral == True:
    $ renpy.pause (2.5)
    c "Edging me {i}this{/i} much is just cruel."
    An smirk "Fine. If you're going to complain so much, then that's enough foreplay."
    jump bangok_anon_anna4_playerride

else:
    c "Hey!"
    An smirk "What? Have you not heard of edging before?"
    c "Well, I have…"
    An bangok blush "Then stop complaining that you get to enjoy this even more."

$ renpy.pause (1.0)
show anna normal with dissolve
$ renpy.pause (1.0)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_player_f_tail:

c "Can you tailfuck me?"
An smirk "Oh. I didn't expect you to be into tailplay, given you humans' lack of one. I'm not complaining though."

$ renpy.pause (1.0)
play sound "fx/bed.ogg"
scene bangok_anon_o_ceiling at Pan((0,360), (0,120), 2.5) with dissolvemed
$ renpy.pause (2.5)
show anna smirk at Position(ypos=1.3) with easeinbottom
m "I proceed to lie on my back, and Anna positioned herself between my legs. She then held my waist with both of her hands and pointed her tail towards my already slick pussy."
An "Are you ready?"
c "Yes…"
$ renpy.pause (0.5)
show anna:
    ease 1.0 ypos 1.26
m "Anna then abruptly thrust her tail into me. Catching me by surprise, I let out a moan at the wave of pleasure sent through me."
c "A-Ah!"
m "I could feel my canal press inwards around her tail, coating it with even more of my juices, making her penetration of me even easier."
$ renpy.pause (0.5)
play soundloop "fx/rub2.ogg" fadein 6.0
show anna:
    ease 0.8 ypos 1.29
    ease 1.2 ypos 1.26
    ease 0.8 ypos 1.29
    ease 0.7 ypos 1.26
$ renpy.pause (3.5)
show anna:
    ease 0.8 ypos 1.29
    ease 0.5 ypos 1.25
    repeat
m "Then she picked up her pace, every thrust of her tail fucking me slightly deeper and faster."
m "At this new depth, she found my sweet spot, now bringing me even closer to my limit by the second."
c "Ngh…"
$ renpy.pause (4.5)
if persistent.bangok_cervpen:
    stop soundloop fadeout 3.5
    show anna:
        ease 0.8 ypos 1.29
        ease 1.2 ypos 1.25
        ease 1.3 ypos 1.29
        ease 1.6 ypos 1.25
    $ renpy.pause (3.0)
    m "Suddenly, her tail reached some resistance, not caused by her tail, but from inside me. Her tail was up against my cervix!"
    c "W-Wait. You're right up against my cervix."
    An bangok blush "I know."
    show anna:
        ease 1.7 ypos 1.24
    m "She poked just the tip of her tail through."
    An smirk "Do you want me to go through?"
    menu:
        "P-Please…":
            $ bangok_anon_anna4.tailinwomb = True
            c "Yes, p-please…"
            $ renpy.pause (0.5)
            show anna:
                ease 2.0 ypos 1.22
            $ renpy.pause (0.5)
            m "She obliged, slowly pushing even more of her tail through my cervix, sending another even stronger maddening wave of pleasure through me, leaving me unable to move due to the sheer pleasure."
            c "A-Ah! F-Fuck!"

        "Is it safe?":
            $ bangok_anon_anna4.tailinwomb = True
            c "Is it safe to go that deep?"
            An bangok blush "Of course, I've done it multiple times before."
            An smirk "Let's experiment with just a small amount to see what you think."
            show anna:
                ease 2.0 ypos 1.22
            $ renpy.pause (0.5)
            m "Anna then slowly pushed even more of her tail through my cervix, sending another even stronger maddening wave of pleasure through me, leaving me unable to move due to the sheer pleasure."
            c "A-Ah! F-Fuck!"
            $ renpy.pause (1.5)
            An "Do you want me to keep going?"
            $ renpy.pause (1.5)
            c "Y-Yes…"

        "This is deep enough.":
            $ bangok_anon_anna4.tailinwomb = False
            c "N-No, this is deep enough…"
            An bangok blush "If you say so."

    if bangok_anon_anna4.tailinwomb == True:
        $ renpy.pause (1.0)
        show anna smirk with dissolve
        play soundloop "fx/rub2.ogg" fadein 4.0
        show anna:
            ease 1.5 ypos 1.25
            ease 1.0 ypos 1.23
            ease 1.0 ypos 1.25
            ease 0.7 ypos 1.22
        $ renpy.pause (3.0)
        show anna:
            ease 0.7 ypos 1.25
            ease 0.4 ypos 1.2
            repeat
        m "Anna continued to fuck me with her tail, and with her past my cervix and now fucking my womb, it was even more stimulating than before. Her being so deep, we reached a much thicker portion of her tail, which started to stretch my outermost lips, just short of the point of pain."
        m "I didn't know how much longer I could last, but it wasn't long."
        $ renpy.pause (4.0)
     
    else:
        $ renpy.pause (1.0)
        show anna smirk with dissolve
        play soundloop "fx/rub2.ogg" fadein 4.0
        show anna:
            ease 1.5 ypos 1.29
            ease 1.0 ypos 1.27
            ease 1.0 ypos 1.29
            ease 0.7 ypos 1.25
        $ renpy.pause (3.0)
        show anna:
            ease 0.7 ypos 1.29
            ease 0.4 ypos 1.23
            repeat
        m "Anna continued to fuck me with her tail. But instead of going through my cervix, she started to coil her tail just before it, letting me take even more of it, and starting to stretch my outer lips, but just short of the point of pain."
        m "In this even more pleasurable position, I knew I wouldn't last much longer."
        $ renpy.pause (4.5)

    show black with fadequick
    stop soundloop fadeout 1.5
    m "Suddenly, my passage lewdly clenched down on her tail and soaked it with even more of my juices."
    if bangok_anon_anna4.tailinwomb == True:
        show anna at Position(ypos=1.2) with ease
    else:
        show anna at Position(ypos=1.23) with ease
    $ renpy.pause (1.5)
    hide black with dissolveslow
    m "Anna gave me a moment to come down after my orgasm before receiving her tail from me."
    if bangok_anon_anna4.tailinwomb == True:
        $ renpy.pause (0.5)
        show anna:
            ease 2.0 ypos 1.25
        $ renpy.pause (2.0)
        m "She made sure to take care as my cervix closed over her tail, yet the sensation still caused me to subtly gasp."
        show anna:
            ease 1.4 ypos 1.3
        $ renpy.pause (2.0)

    else:
        $ renpy.pause (0.5)
        show anna:
            ease 1.4 ypos 1.3
        $ renpy.pause (2.0)

else:
    stop soundloop fadeout 4.5
    show anna:
        ease 0.8 ypos 1.29
        ease 1.2 ypos 1.25
        ease 1.3 ypos 1.29
        ease 1.6 ypos 1.25
    $ renpy.pause (3.0)
    m "Anna tried pushing her tail deeper, but it reached some resistance, not caused by her tail, but from inside me. Her tail was up against my cervix!"
    c "W-Wait. You're right up against my cervix."
    An bangok blush "Alright, I won't go any deeper than this then."
    c "Y-Yeah, thanks…"
    $ renpy.pause (1.0)
    An smirk "Actually, I might have an idea."
    c "What are you…?"
    $ renpy.pause (0.5)
    show anna:
        ease 1.3 ypos 1.23
    m "Instead of trying to go deeper, Anna started coiling her tail instead, letting me take even more of it, and starting to stretch my outer lips, but just short of the point of pain."
    c "O-Oh!"
    $ renpy.pause (0.5)
    play soundloop "fx/rub2.ogg" fadein 5.0
    show anna:
        ease 1.0 ypos 1.29
        ease 0.7 ypos 1.25
        ease 0.7 ypos 1.29
        ease 0.5 ypos 1.25
    $ renpy.pause (3.0)
    show anna:
        ease 0.6 ypos 1.29
        ease 0.3 ypos 1.23
        repeat
    m "In this even more pleasurable position of Anna coiling her tail, I knew I wouldn't last much longer."
    $ renpy.pause (4.0)
    show black with fadequick
    stop soundloop fadeout 1.5
    show anna at Position(ypos=1.23) with ease
    m "Suddenly, my passage lewdly clenched down on her tail and soaked it with even more of my juices."
    $ renpy.pause (1.5)
    hide black with dissolveslow
    m "Anna gave me a moment to come down after my orgasm before receiving her tail from me."
    $ renpy.pause (0.5)
    show anna:
        ease 1.4 ypos 1.3
    $ renpy.pause (2.0)


    
scene black with fadequick
$ renpy.pause (0.3)
scene o at Pan((0, 250), (0, 250), 0.1)
show anna smirk at center
with dissolveslow
$ renpy.pause (0.5)
An "I'll take it that you enjoyed that?"
c "Far more than just enjoyed."
An "Good to hear."

$ renpy.pause (1.5)
show anna bangok blush with dissolve
$ renpy.pause (1.5)


jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_playerride:

c "(That's what she considers foreplay?)"
$ renpy.pause (1.0)
play sound "fx/bed.ogg"
scene bangok_anon_o_ceiling at Pan((0,360), (0,120), 2.0) with dissolvemed
$ renpy.pause (2.5)
show anna smirk at Position(ypos=1.25) with easeinbottom
show anna:
    ease 1.5 ypos 1.2 zoom 1.2
$ renpy.pause (1.0)
m "Shooting me a lust-fueled glare, Anna sat over me with me between her legs, lined up the tip of my shaft with her slit, then took ahold of my shoulders and held me down against the bed."
if persistent.bangok_knot == True and bangok_four_anna2.unplayed == False:
    An bangok blush "Just to confirm it, humans don't have knots, right?"
    c "Uh, no?"
    An smirk "Good."
    $ renpy.pause (0.5)

$ renpy.pause (1.5)
show anna:
    ease 1.3 ypos 1.24
m "Then she lowered her hips onto me. A bit disappointingly there wasn't much resistance, but inside her felt exceptionally wet and hot, she was clearly very much aroused from her perception of what was our previous foreplay."
show anna:
    ease 1.2 ypos 1.2
    ease 1.0 ypos 1.24
$ renpy.pause (0.5)
show anna:
    ease 1.0 ypos 1.2
    ease 0.8 ypos 1.24
    repeat
$ renpy.pause (1.0)
m "Then she began to properly ride me."
m "She started off slowly, and I couldn't help but thrust into her as she came down."
$ renpy.pause (4.0)
play soundloop "fx/rub2.ogg" fadein 5.0
show anna:
    ease 0.8 ypos 1.2
    ease 0.8 ypos 1.26
$ renpy.pause (1.5)
show anna:
    ease 0.7 ypos 1.2
    ease 0.5 ypos 1.28
    repeat
m "Then she started to pick up her pace, and leaned back so most of her body weight was on my pelvis, firmly holding me in place on the bed as she had her way with me."
m "She was now taking as much of me as my length would allow, and her sopping canal made my penetration of her near-effortless, and even more stimulating."
m "Every time she thrust down, I felt her hips slap against my own, sending waves of pleasure through me each time."
An bangok lipbite "Mmh…"
$ renpy.pause (3.0)
m "Then as she got more into it, I enjoyed the sensation of her slit beginning to tighten on my member as she rode me. I couldn't help but let out a moan of pleasure."
c "A-Ah!"
$ renpy.pause (4.5)
show anna:
    ease 0.5 ypos 1.2
    ease 0.3 ypos 1.28
    repeat
m "Suddenly, Anna's riding of me became a lot more wild and vigorous. She started to fuck me even faster, and her grip on my shoulders tightened to a point where her claws started digging into my skin, but thankfully not enough to hurt."
An "Ngh…"
m "I was now not only feeling the pleasure of being ridden, but a thrill of danger too."
$ renpy.pause (4.0)
m "Despite being intended for larger partners, I still felt her passage squeeze on my shaft, and her inner muscles massaging it with an all-encompassing warmth."
m "At that point, I knew I couldn't hold out for much longer."
c "A-Anna…"
An "Almost…"
$ renpy.pause (4.0)
play sound "fx/varagrowl.ogg"
m "Then, Anna let out a noise, not a moan, but a growl. Not one of aggression, rather of intensity, further solidifying the thrill of risk."
$ renpy.pause (3.5)
play sound "fx/extinguish.ogg"
show black with fadequick
m "I wasn't able to hold back from my climax anymore, and couldn't help but to shoot my load inside her."
$ renpy.pause (2.5)
hide black with dissolveslow
$ renpy.pause (0.5)
m "And the brief period I was still hard after my climax was enough for Anna to reach her limit too."
show anna:
    ease 0.4 ypos 1.28
stop soundloop fadeout 0.5
play sound "fx/snarl.ogg"
show anna bangok orgasm with dissolve
m "Anna then dropped her weight onto me and let out a roar. Her canal clamped down on my member and soaked it and my groin with her juices."
$ renpy.pause (2.0)
show anna bangok lipbite with dissolve
m "Then we just stayed there for a moment, Anna still on top of me, both of us basking in our afterglow."
$ renpy.pause (2.0)
scene black with fadequick
$ renpy.pause (0.3)
scene o at Pan((0, 250), (0, 250), 0.1) with dissolveslow
show anna smirk at center with dissolveslow
$ renpy.pause (0.5)
m "After Anna's passaged had fully relaxed, she got off of me, then collapsed next to me, leaving both of us lying side by side on the bed."
$ renpy.pause (1.5)

jump bangok_anon_anna4_afterglow



label bangok_anon_anna4_afterglow:

An smirk "Holy fuckeroly."
$ renpy.pause (1.5)
if bangok_four_anna2.unplayed == False:
    An "That was so much better than last time."
    if bangok_four_anna2.annacomment == "adorable":
        c "What was that you said about me not being able to get you off with, {i}just that thing?{/i}"
        An "Shut it."
    elif bangok_four_anna2.annacomment == "small":
        c "What was that you said about me being rather small?"
        An "Shut it."
    else:
        pass
        
    $ renpy.pause (1.0)
    c "What made it so much better this time?"
    if bangok_four_anna1_sexrequested == True:
        An sad "Well, last time was only for your end of the bet. I wasn't doing it for myself, I just wanted to get you off so you wouldn't complain too much and draw attention when you came in for those tests."
    else:
        An sad "Well, last time was really just random and spur of the moment. I wasn't really doing it for myself, I just wanted to make sure you were satisfied with your end of our deal so you wouldn't complain too much and draw attention when you came in for those tests."

    An smirk "This time though? Purely pleasure."

else:
    An "That was so much better than I thought it would be."
    if bangok_four_playerhasdick == True:
        c "What was that you said about me being smaller than you're used to?"
        An "Shut it."

An bangok blush "Honestly, I almost forgot how much better sex was when you're doing it out of want, not for part of a deal or to manipulate someone."
c "I'm not sure how to respond to that."
An normal "Then don't. I need to rest, I'm exhausted."

$ renpy.pause (2.5)
c "(We're just lying next to each other now, should I do something?)"
menu:
    "[[Do nothing.]":
        m "I didn't want to try and push anything and ruin the moment, so I just stayed on my side of the bed."
        m "And soon enough I drifted off to sleep, still feeling the warmth of our afterglow."
        scene black with dissolveslow
        $ renpy.pause (1.0)

    "[[Try to cuddle.]":
        m "I moved closer and rested my head on Anna's chest. She didn't say anything to encourage my advancement, yet she didn't object to it either."
        $ renpy.pause (2.0)
        show anna smirk with dissolve
        m "Then she tried to subtly wrap an arm around my back, which I took as a sign to continue."
        m "Now in a more comfortable embrace, and still feeling the warmth of our afterglow, I drifted off into a peaceful slumber."
        scene black with dissolveslow
        $ renpy.pause (1.0)
        play sound "fx/purr.ogg" fadein 3.0
        $ renpy.pause (7.0)
        stop sound fadeout 4.0

$ renpy.pause (3.0)

$ mp.annaromance = True
$ mp.save()
$ annastatus = "good"
$ annascenesfinished = 4
stop music fadeout 2.0
$ renpy.pause (0.5)
jump _mod_fixjmp

