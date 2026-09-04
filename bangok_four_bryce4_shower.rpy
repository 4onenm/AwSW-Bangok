init python in bangok_four_bryce4_store:
    player_alcohol_level = 0
    bryce_alcohol_level = 0

label bangok_four_bryce4_shower_intro:
    Br flirty "I promise you won't regret it."
    $ renpy.pause (0.5)
    hide bryce with dissolve
    play sound "fx/steps/clean2.wav"
    scene black with dissolve
    $ renpy.pause (0.5)
    scene bath with dissolve
    $ renpy.pause (0.5)
    show bryce smirk flip at left with dissolve
    m "Bryce dropped the basket on the counter next to the sink, the wine bottle clunking against the lube bottles."
    Br flirty flip "Who gets to enjoy first? You? Me? 50/50?"
    menu:
        "Your idea. You go ahead and bend over.":
            jump todo_out_of_content_bangok_four_bryce4_shower
        "Can't let you guzzle it all. I'll have it.":
            jump bangok_four_bryce4_shower_intro.player_bottle
        "Those condoms... wanna drink it outta me?":
            jump todo_out_of_content_bangok_four_bryce4_shower

    label .player_bottle:
        m "I got down on my knees, then bent over the side of the bathtub, exposing my ass to my draconic partner."
        c "Bottoms up!"
        Br laugh "Hah. Yeah, it sure is."
        m "I can hear Bryce uncork the bottle behind me with his claws."
        Br flirty "Don't be too greedy. You tell me when."
        menu:
            "Just a taste.":
                $ bangok_four_bryce4_store.player_alcohol_level = 1
            "Try to stop when it's halfway.":
                $ bangok_four_bryce4_store.player_alcohol_level = 2
            "Enjoy the whole bottle.":
                $ bangok_four_bryce4_store.player_alcohol_level = 3
        m "The room-temperature glass against my tight sphincter makes me clench up."
        if bangok_four_playerhasdick:
            m "I can feel more of the glass and Bryce's scaly forepaw brushing my ballsack as he gets it lined up."
        m "The neck of the bottle is narrow enough, though, for Bryce to press the mouth into me without much challenge."
        m "Then he lifts it, and the wine sloshes over the tissues of my rectum, for a moment cooling my heated insides, before the warmth of the alcohol hits me."
        if bangok_four_bryce4_store.player_alcohol_level < 2:
            c "Th-that's enough for me."
            Br laugh "C'mon, that's barely anything."
            m "As he complains, I feel the muscles in my lower body loosening, the effects of more and more setting in."
            c "That's enough."
            m "Reluctantly, Bryce twists the bottle and pulls it out with a wet pop, spilling only a couple of drops down my taint."
            m "I shiver, feeling the wine soaking into my guts."
            m "Then I struggle back to my feet."
            Br smirk "Well, you went through about half of it."
            c "(It definitely looks less than halfway, but I'm not gonna argue.)"
            jump todo_out_of_content_bangok_four_bryce4_shower
        c "O-Oh man, that's... that's fast."
        m "I can feel the alcohol loosening the muscles in my lower body, and Bryce pushing the neck of the bottle further into me."
        c "H-Hey!"
        Br laugh "Your ass is just slurping it all up."
        if bangok_four_bryce4_store.player_alcohol_level < 3:
            c "Half, ok, half!"
            if bangok_four_playerhasdick:
                m "With another chuckle, Bryce pulled the bottle out, spilling a splash of wine down over my scrotum and junk."
            else:
                m "With another chuckle, Bryce pulled the bottle out, spilling a splash of wine down between my thighs."
            m "I shiver, feeling the wine soaking into my guts."
            m "Then I struggle back to my feet."
            Br smirk "Well, I think you went through about half of it."
            c "(It looks slightly over halfway, but I'm not gonna argue.)"
            jump todo_out_of_content_bangok_four_bryce4_shower
        jump bangok_four_bryce4_shower_wasted
        c "Use some lube, if you're gonna push it in more."
        m "My rectum is flush with wine now, and I can feel the burn of the alcohol bubbling deeper into my guts."
        Br brow "I take it you're not leaving me any?"
        m "Despite his question, I can feel him lean on my back as he grabs something, then a squirt of cold lube onto my bottle-stuffed anus."
        m "Then he pushed the bottle in further, and I groan as I feel my loosened muscles giving way."
        m "The burn of the alcohol fades into panting need as Bryce twists the bottle, trying to get more inside of me."
        m "Then the glugging sound of the bottle pouring into my rectum stops, as there's no more wine left in the bottle."
        m "I groan as Bryce thrusts the bottle in and out of me a few times, shaking out every last drop."
        m "I can't even tell how much of the bottle is getting inside me, whether I'm past the neck or not. I'm just enjoying the sensation."
        m "Then he pulls the bottle out with a wet pop, leaving my insides soaked with wine and my sphincter parted and lightly damp with lube."
        Br smirk "Well, you went through the whole bottle."

label bangok_four_bryce4_shower_wasted:
    Br laugh "So much for not being greedy."
    c "Hey, it felt good. What can I say?"
    m "Exhaling contentedly, I began pushing myself up from the side of the tub, toward my feet."
    c "Doesn't even feel that bad. I don't think I'm buzzed--"
    m "Abruptly, the floor shifts under my feet, and I nearly trip over the side of the tub before Bryce's mouth clamps down on my arm, catching me."
    c "O-Oh-- uhh--"
    Br laugh "What was that about not being buzzed?"
    show black with dissolve
    $ renpy.pause (0.5)
    hide black with dissolve
    m "My vision swims. When my eyes focus again, I'm on my knees, under Bryce, staring at his throbbing cock with his belly plates against the back of my head."
    if bangok_four_playerhasdick:
        m "I can feel hot breath between my legs, then a wet, sacly tongue licking my balls and just teasing the base of my dick."
    else:
        m "I can feel hot breath between my legs, then a wet, sacly tongue teasing the opening of my passage."
    c "Mmngh."
    m "He pauses."
    Br flirty "Hey, you were so eager to drink up from your other end. Don't you want to try my tap?"
    m "His hips shift, rubbing his cock against my cheek."
    m "Head spinning, I let his tip between my lips and suckle, tasting his pre filling my mouth."
    m "He returns the favor, redoubling his own tonguing of my own genitals."
    $ renpy.pause (1.0)
    c "Glk!"
    m "Abruptly, he's at the back of my throat, hips hiking forward further."
    m "I don't even have time to gag as his enormous cock manages to slide all the way into my throat."
    Br pantflirt "Oh fuck, that feels so good."
    m "I can feel his girth bulging my throat. There's nowhere to back up to against the side of the tub, and his belly against my head prevents me from leaning away."
    m "Even if I could breathe, I wasn't sure my spinning head would have been able to come up with any other options."
    m "When his hips let up the pressure and his cock slides out, I can feel something else following it up."
    show black with dissolve
    $ renpy.pause (1.0)
    hide black with dissolve
    m "When I can focus again, I'm bent over the side of the tub once more. A tangy stench hits my nose as I try not to think about what probably just came out of my stinging mouth."
    c "Uuugh. F-Fuuuuck mnnngh."
    m "I groan, finally processing what had just happened with Bryce's member all the way down my throat. I clearly wasn't in a headspace to make good decisions."
    Br laugh "\"Fuck me\"? That's what I'm trying to do. You probably shouldn't have had that much wine all at once, though."
    m "I feel his belly plates scraping against my back, his hips aligning with mine."
    if bangok_four_playerhasdick:
        m "A moment later, it sinks in that the cold sensation running down my ass crack, taint, and ballsack is more lube."
    else:
        m "A moment later, it sinks in that the cold sensation running down my taint, nether lips, and thighs is more lube."
    menu:
        "Mmmmnogh":
            $ renpy.pause (0.5)
            m "My slurred protest goes unanswered as Bryce's cock prods my legs."
        "Mmmmnyes":
            $ renpy.pause (0.5)
            m "My slurred encouragement goes unanswered as Bryce's cock prods my legs."
        "Shhhtah":
            $ renpy.pause (0.5)
            m "My slurred protest goes unanswered as Bryce's cock prods my legs."
        "Mmmmnah":
            $ renpy.pause (0.5)
            m "My slurred protest goes unanswered as Bryce's cock prods my legs."
        "Heeeygh":
            $ renpy.pause (0.5)
            m "My slurred speech goes unanswered as Bryce's cock prods my legs."
    if bangok_four_playerhasdick:
        jump .male_player
    else:
        jump .female_player

    label .male_player:
        m "His tip smears lube up my ass crack, then applies pressure to my sphincter."
        m "I grunt as Bryce's cock spears open my loose asshole, the alcohol and lube easing his passage, but not eliminating the pain as my muscle is stretched wide."
        Br flirty "Fuck, that's the perfect fit."
        Br smirk "And your insides feel so wet. Wonder how that happened?"
        m "He pulls back before our hips meet, then thrusts forward again, pushing his girth deep into my ass as his hips finally press mine to the bathtub edge."
        m "I can't help but gasp as his rough thrust pushes my prostate, my member twitching."
        m "Bryce's scaly hips grind against mine, scraping my skin as his cock moves inside me."
        m "Then he pulls back again, this time beginning to fuck me properly."
        m "The shudders from my prostate don't quite ripple through my alcohol-addled body, but I can feel my lower body taking his rhythm, my spread legs trembling."
        m "As he lays down across my back, his hips maintaining his pace, my arms are too weak to hold up my upper body against his weight, holding my chest and face against the side of the tub."
        show black:
            alpha 0.5
        with dissolve
        m "I moan underneath him, breath escaping me again. Then I let my eyes flutter closed in time to his thrusts, my body drifting into a haze of languid fucking."
        show black:
            alpha 1.0
        with dissolve
        $ renpy.pause (1.0)
        hide black with dissolvemed
        m "I came to a while later, my right side pressed against the cold tile of the bathroom floor."
        if persistent.bangok_knot == True:
            m "The first thing I noticed was the pain in my sphincter, my ass straining as something too-large was gently trying to pull out."
        else:
            m "The first thing I noticed was the pain in my gut, something hard and slick shoved deep inside, holding my sphincter slightly open."
        if persistent.bangok_inflation == True:
            m "Then I felt the pressure against my belly as Bryce's paw rubbed gently over it, holding me in place against him on the floor. My gut visibly bulged, my insides stretched by the heavy weight of fluids I didn't remember getting there."
        else:
            m "Then I felt Bryce's paw gently rubbing my belly, holding me in place against him on the floor."
        jump .aftermath


    label .female_player:
        m "His tip smears lube up my taint as it twitches, then pushes through my outer folds."

    label .aftermath:
        c "Uurgh."
        Br brow "Hey, just keep resting. That wine really did a number on you, huh?"
        m "I try to form a response, but my mouth is dry and my tongue feels thick."
        Br normal "It's okay. You're fine. Just rest."
        show black with dissolvemed
        m "Feeling too weak to do otherwise, I let my head fall back against Bryce's neck again, willing the alcohol to wear off and my body to recover."
        $ renpy.pause (1.0)
        hide black with dissolvemed

        m "I wake up later, my head pounding and my body aching."
        m "I try to move, but my muscles feel like they're made of lead."
        m "I look around. I'm still on the floor of the bathroom, but Bryce is gone."    
        c "Agh!"
        m "I try to sit up, but immediately regret the action as something hard shifts in my belly."
        c "W-What..."
        if bangok_four_playerhasdick == True:
            m "I reach down over my sticky ass, prodding my stinging anus, and find something hard and round sticking out."
            c "Oh no..."
            m "I try to pull it out, but it's stuck."
            m "Bryce shoved the fucking wine bottle into my ass."
        else:
            if persistent.bangok_inflation == True:
                m "My belly is still painfully distended, my core stretched by some kind of heavy fluids."
                m "But there's something else painfully holding my passage open, pressing back against the pressure trying to escape my cervix."
            else:
                m "My belly has a visible bump, something hard and round inside me. I can feel it painfully pressing against my cervix."
            m "I reach around the bump, down to my nethers, and find something hard and round sticking out."
            c "Oh no..."
            m "I try to pull it out, but at this angle it's not moving."
            m "Bryce shoved the fucking wine bottle into my pussy."
        m "I groan in pain, trying to process the fragments I could remember of what I assumed was last night."
        m "Then I spotted the sticky note on the drawer, and the two bottles of lube left on the sink counter."
        c "(What could he have written to justify this?)"
        m "Hey [player_name],\n You were leaking everywhere after I pulled out; just tried to stop the flow.\n Called away on Reza case business, so I had to leave. Sorry.\n Bryce."
        c "Bryce, you fucker."
        m "It takes me a minute to work up the energy to try to pull myself up the counter through my pounding headache, but I manage."
        m "Finally on my feet, I grab the lube, then start doing what I have to do."
        $ renpy.pause (1.0)
        m "When the bottle finally pulls free, clattering down inside the bathtub, I yell in pain and relief."
        if persistent.bangok_inflation == True:
            if bangok_four_playerhasdick == True:
                m "I feel a gush of relief as the pressure in my bowels is released, fluid spilling out of my gaping ass into the bathtub."
            else:
                m "I feel a gush of relief as the pressure in my womb is released, fluid spilling out of my gaping cunt into the bathtub."
        else:
            if bangok_four_playerhasdick == True:
                m "I feel an ache in my bowels as the pressure is released. A dribble of fluids follows, hardly the \"leaking everywhere\" his note claimed."
            else:
                m "My cervix aches like a bruise as the pressure is released. A dribble of fluids follows, hardly the \"leaking everywhere\" his note claimed."
        if persistent.bangok_watersports == True:
            m "Then I pinch my nose, the scent of urine hitting my nostrils harder than the scent of sex as I realize how watery the fluid is."
            c "F-fuck, he pissed in me too?!"
        m "I sit on the edge of the tub for a while, trying to catch my breath and willing my body to calm down."
        m "Then I snag the sticky note, flipping it over to look for any other detail."
        m "All I find is a phone number scrawled on the other side, probably to reach him while he's out."
        c "(No question I need to call him after this.)"
        m "After a few more moments, I finally limp my way out of the bathroom, my head pounding and my body aching as I stumble nude into the living room."
        # TODO: Phone call sounds
        Br brow "I'll be right back, Sebastian."
        Br normal "[player_name], that you?"
        menu:
            "Tell him you're fine.":
                c "Yeah, it's me."
                Br normal "How are you?"
                c "I'm... I got the bottle out. Lots of aches."
                Br brow "That all? I was kinda worried we'd overdone it."
                c "I guess. I don't know, I just... I don't feel good."
                Br normal "Well, I'm glad you're okay."
                c "I just need to rest."
                Br normal "See you at the fireworks?"
                c "Yeah, sure. If nothing ambassador-related comes up."
                Br normal "Got it."
                $ renpy.pause (1.0)
                m "We both paused, awkwardly."
                Br normal "Talk to you later?"
                c "Bye."
                # TODO: Hang up sound
                $ renpy.pause (1.0)
                c "(I want to punch myself. Why did I even call to say that?)"
                m "Groaning, I stumble toward the bedroom to recover whatever sleep I can, in the hopes my headache subsides."
                jump .end
            "Express calmly that fucking hurt.":
                c "Yeah, it's me."
                Br normal "How are you?"
                c "Bryce."
                Br normal "What's wrong?"
                c "You left the wine bottle in me."
                Br brow "Yeah?"
                c "Bryce, I barely remember last night, but I think that's bigger than your dick. It's definitely bigger than my arm."
                $ renpy.pause (0.5)
                Br brow "..."
                $ renpy.pause (0.5)
                Br stern "Fuck, [player_name], I did not think that through."
                c "I don't care. That could have seriously physically hurt me."
                c "And I mean more than the psychological pain of waking up on the bathroom floor with that in me."
                c "It hurt getting it out. It hurt getting fucked that roughly last night."
                c "I was way too far gone for half of what we did."
                Br stern "I know. I'm sorry."
                c "You know--"
                m "For a moment, anger almost got the better of me."
                c "Why did you do it if you knew it was too much?"
                Br brow "I... I thought I was following your lead."
                c "I was the one who was too far gone."
                Br stern "Obviously thinking it through now..."
                c "Obviously."
                $ renpy.pause (0.5)
                Br stern "..."
                $ renpy.pause (0.5)
            "Give him a piece of your mind.":
                c "Fuck you, Bryce."
                Br brow "What?"
                c "The fucking wine bottle? Really? You shoved that in me?!"
                Br stern "Didn't I say in the note--"
                c "That's bigger than your dick, Bryce! It's bigger than my fucking arm!"
                m "My head throbs, my voice too loud for my own ears. I hope it's half as loud to him."
                c "What if I couldn't get it out? What if it had broken inside me, and ripped up my insides?!"
                Br stern "I'm sorry. I didn't think--"
                c "Sorry?"
                c "Fucking sorry?!"
                c "Bryce, you used me like a sex toy while I was wasted, and then you left me alone to deal with a risk of {i}serious fucking injury{/i}!"
                Br stern "I didn't mean to hurt you--"
                c "You didn't mean to? You didn't mean to?! You're a fucking idiot!"
                m "Abruptly, Bryce matched my energy."
                Br angry "What should I say? I just told you, I didn't think it through!"
                Br angry "You wanted the whole bottle! I thought you were a responsible adult, who saw where encouraging that night of debauchery would lead."
                c "That went out the fucking window when I was too drunk to stand up!"
                c "I wasn't encouraging you to fucking hurt me! Much less bend me over the tub and use me as a hole for your fucked-up levels of lust!"
                Br brow "Because presenting my dick on the couch wasn't supposed to lead to it inside you?"
                Br angry "Are you not going to take any fucking responsibility for your part?"
                Br angry "I apologized for what was my mistake; can you stop being a child throwing a damn tantrum?"
                menu:
                    "Rage.":
                        c "So you consider me a child? Are you into fucking people who can't take responsibility for their actions?!"
                        Br angry "I'm saying you're acting like one, you--"
                        c "I don't care what you're thinking. You're a fucking idiot who could have hurt me. Who used me."
                        Br stern "I already fucking said--"
                        c "Save it. I can't-- can't fucking do this."
                        jump .stay_away
                    "Reflect.":
                        $ renpy.pause (1.0)
                        m "Your shared heaving breathing over the phone slows as you take a few moments to lower your energy."
                        c "I'm... I was scared and fucking alone, waking up like that. I felt betrayed and used and... and I felt dismissed by your first apology."
                        Br stern "I understand. I..."
                        Br brow "I didn't... what I thought I was doing was avoiding leaving you in what I thought was even worse."
                        Br stern "I was just thinking of you waking up somewhere in your house in a puddle of my fluids, alone."
                        Br brow "I thought if I plugged it somehow, it'd be less mess for you and it wouldn't be... I don't know..."
                        Br laugh "Chose a really shitty way to avoid hurting you, huh? Not thinking about how big that was compared to your body."
                        Br stern "I'm really sorry. I didn't mean to hurt you."
                        m "I said nothing for several seconds, processing his excuse."
            "Tell him you didn't consent to that.":
                c "Bryce... what the fuck did you do?"
                Br brow "What?"
                c "I barely remember last night, and I woke up on my bathroom floor with a wine bottle bigger than my arm shoved inside me."
                Br stern "Your arm... Oh fuck, [player_name], I didn't think it was that big."
                c "It's not about the size, Bryce. It's about the fact that I didn't say you could do that, could hurt me like that."
                Br brow "It wasn't supposed to hurt. Listen, I thought--"
                c "That's why you ask, Bryce! You don't rape people with objects while they're blacked out."
                m "The R-word seemed to stun Bryce, who didn't respond while my breathing hitched."
                c "I don't know what to say. I don't know what to think. I don't know how to feel about this."
                Br stern "I'm sorry. I didn't mean to hurt you. I... fuck, [player_name]. I'm really sorry."
                m "I said nothing for several seconds, processing his apology."
        Br brow "Where... do we go from here?"
        menu:
            "Reconcile.":
                c "I... need you to understand I'm not as durable as you are. If we keep going down this road of more than friends, you can't treat me like that."
                c "I need you to respect that I'm not you, and I'm not yours. Treat me like a person, no matter what the situation."
                Br stern "I will. I promise."
                c "I need a little time to recover from this."
                m "I swallowed, my throat still dry."
                c "But I want to see you at the fireworks."
                Br brow "You do?"
                Br stern "[player_name], I know I fucked up. I'm sorry. You don't have to force yourself if you're not ready."
                c "If some ambassador duty comes up, I'll let you know."
                c "But I don't want this to fuck up what we were building."
                Br normal "I'll... see you there, [player_name]."
                c "See you around."
                $ brycestatus = "good"
            "Just friends.":
                c "I don't think we can be more than friends anymore. I don't know if I can trust you with that much of me."
                m "I swallowed, my throat still dry."
                c "I can't cross that line with you anymore. Friends, maybe. More than friends, no."
                Br stern "I... understand."
                c "But friends can go to the fireworks, right?"
                Br stern "[player_name], I know I fucked up. I'm sorry. You don't have to force yourself to go to the fireworks with me."
                c "Simple question, Bryce."
                Br brow "Yeah, it can be a friends thing."
                c "Then if no ambassador duties come up, I'll let you know."
                Br brow "Oh."
                Br normal "I'll... see you there, [player_name]."
                c "See you around."
                $ brycestatus = "neutral"
            "Break it off.":
                jump todo_out_of_content_bangok_four_bryce4_shower
            "Stay away.":
                label .stay_away:
                c "I can't trust you anymore."
                c "Fuck, we've already been through so much. I just don't understand how you could do this to me."
                Br stern "I..."
                Br stern "I'm not going to argue."
                Br brow "I'm sorry."
                c "Good. Stay sorry. I need space away from you."
                Br stern "The Reza investigation?"
                c "If I have to, I'll be professional."
                c "Otherwise, stay the hell away from me."
                Br stern "I... understand."
                $ brycestatus = "bad"
    label .end:
        jump todo_out_of_content_bangok_four_bryce4_shower


label todo_out_of_content_bangok_four_bryce4_shower:
    play sound "fx/system3.wav"
    s "Bryce4 Shower Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")
