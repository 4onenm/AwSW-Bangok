init python in bangok_four_bryce4_store:
    player_alcohol_level = 0
    bryce_alcohol_level = 0
    bryce_ws = None

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
        $ mp.teetotaler = False
        $ mp.save()
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
    m "He helps me down to my knees on the unstable floor before releasing my arm, then laughing at my state."
    Br laugh "What was that about not being buzzed?"
    show black with dissolve
    $ renpy.pause (0.5)
    hide black with dissolve
    m "My vision swims. When my eyes focus again, Bryce has stepped forward, leaving me staring at his throbbing cock with his belly plates against the back of my head."
    if bangok_four_playerhasdick:
        m "I can feel hot breath between my legs, then a wet, sacly tongue licking my balls and just teasing the base of my dick."
    else:
        m "I can feel hot breath between my legs, then a wet, sacly tongue teasing the opening of my passage."
    c "Mmngh."
    m "He pauses."
    Br flirty "Hey, you were so eager to drink up from your other end. Don't you want to try my tap?"
    m "His hips shift, rubbing his cock against my cheek."
    m "Head spinning, I let his tip between my lips and suckle, the taste of his pre filling my mouth."
    m "He returns the favor, redoubling his own tonguing of my own genitals."
    $ renpy.pause (1.0)
    c "Glk!"
    m "Abruptly, he's at the back of my throat, hips hiking forward further."
    m "I don't even have time to gag as his enormous cock manages to slide all the way into my loose throat."
    Br pantflirt "Oh fuck, that feels so good."
    m "I can feel his girth bulging my neck. My knees slide on the floor until my feet are up against the tub, leaving me nowhere to back up to. His belly against my head prevents me from leaning away."
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

    label .wasted_ws:
        m "Then he pulls back, slowly all the way out of me with a wet schlurp."
        Br stern "Fuck, I need to piss."
        m "The brief pause as he doesn't move away leads even my addled brain to realize that he might mean on -- or even in -- me."
        menu:
            "Push his dick away.":
                m "I drunkenly toss a hand over my back, trying to slap his dick away from you before he can make you even more of a mess."
                m "Unfortunately, my hand lands on his slick, lubed tip limply, nudging it back down toward my hole."
                Br flirty "Oh, inside you, huh?"
                menu:
                    "N-nongh.":
                        Br brow "My bad. Lemme just go take care of this."
                    "Mmmng.":
                        jump .wasted_ws_inside
            "Hold his dick in place.":
                m "I drunkenly toss a hand over my back, trying to grab his dick and hold it in place."
                m "I succeed at finding it and grabbing it, tugging it up toward my back."
                Br flirty "Fuck, you just love to be a mess, huh?"
                jump .wasted_ws_outside
            "Pull his dick back in.":
                m "I drunkenly toss a hand over my back, trying to grab his dick and pull it back to my parted hole."
                m "I succeed at finding it and tugging, pulling an exhale from Bryce."
                Br flirty "Oh, inside you, huh?"
                jump .wasted_ws_inside

    label .wasted_ws_away:
        m "Bryce steps off of me, shuffling down to the faucet and drain end of the tub."
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        m "Then, without a word, he starts to piss on the side of the tub, just a couple of feet in front of my face."
        Br laugh "Ahh, that's better."
        m "My nose wrinkles, the strong smell of urine overwhelming anything else in my drunken stupor."
        m "It becomes clear after a moment that he's trying to aim for the drain, but that doesn't help the splatter from his hefty stream still getting a few droplets on my face."
        stop soundloop fadeout 1.0
        m "Then, with another exhale, he finishes up, before shuffling back over to me."
        Br flirty "Now, where were we?"
        m "I can only hope all the slickness on his tip is lube as he slides himself into me again."
        return

    label .wasted_ws_outside:
        $ bangok_four_bryce4_store.bryce_ws = "outside"
        m "Bryce steps forward, laying his lube-slickened rod over the top of my asscrack and lower back."
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        m "Then he twitches, and a jet of urine splatters my spine and face."
        Br laugh "Ahh, that's better."
        m "I close my eyes, gagging and coughing, but that only lets him get some of his stream into my nose and mouth."
        m "My back is soaked rapidly, hair drenched, and I moan at the deep debasement of being showered with his piss."
        stop soundloop fadeout 1.0
        if bangok_four_playerhasdick:
            m "As his stream begins to peter out, he shifts backward, getting the last of it all over my ass and balls."
            m "I shiver as the hot, wet liquid begins to cool, growing stickier by the moment as it runs down my spine, thighs, and hard member."
        else:
            m "As his stream begins to peter out, he shifts backward, getting the last of it all over my ass cunt."
            m "I shiver as the hot, wet liquid begins to cool, growing stickier by the moment as it runs down my spine and thighs."
        Br flirty "You're sure gonna need a shower in the morning, huh?"
        m "He lowered his head to just above my back, giving my spine a lick."
        Br smirk "And you'll probably still smell like my piss for a while."
        m "I can't help but gasp from his teasing. Then he steps forward, member teasing my hole, drawing another gasp from me."
        Br flirty "Now, where were we?"
        return


    label .wasted_ws_inside:
        if bangok_four_playerhasdick:
            $ bangok_four_bryce4_store.bryce_ws = "ass"
            m "He wastes no time, sliding his lubed rod back into my upturned rear."
            m "Then his girth throbs, and I feel a stream of watery heat jet into my guts."
            play soundloop "fx/faucet1.ogg" fadein 1.0
            queue soundloop "fx/faucet2.ogg"
            m "I yelp as Bryce's piss bubbles into me. My guts are already soaked with wine, leaving his piss nowhere to absorb, only a tube in which to pool."
            m "I can't help but gasp as the heat of his piss gathers in my upper gut, my upturned body letting it flow so deep into me."
            if persistent.bangok_inflation == True:
                m "But the end doesn't seem to come. My belly begins to sag, slightly, heavy with his waste as he just keeps going."
                stop soundloop fadeout 1.0
                m "I goran, hands going to my full midriff, as he finally begins to peter out."
            else:
                stop soundloop fadeout 1.0
                m "I moan as Bryce's stream begins to finally peter out, leaving me with a dragon's bladderful in my alcohol-addled guts."
            stop soundloop fadeout 1.0
            Br laugh "Ahh, that's better."
            m "He leans down over me, nuzzling the back of my neck."
            Br smirk "Bet you'll enjoy remembering this when that comes out, huh?"
            m "I huff at his teasing, then grunt as he pushes himself deeper into me, shaft disturbing my newly-stained guts."
            Br smirk "And you'll probably still smell like my piss for a while."
            return
        else:
            $ bangok_four_bryce4_store.bryce_ws = "vag"
            m "He wastes no time, sliding his lubed rod back through my slick lower lips."
            m "Then his girth throbs, and I feel a stream of watery heat flood my passage."
            play soundloop "fx/faucet1.ogg" fadein 1.0
            queue soundloop "fx/faucet2.ogg"
            m "I yelp as Bryce's piss stream momentarily hits my cervix. The lube leaves my passage slimy and slick, allowing the nasty fluid to quickly pool deep inside me, protecting that innermost gate with a defiling puddle of his waste."
            if persistent.bangok_inflation == True:
                m "He thrusts himself a little deeper, into his own piss, and I feel the pressure in my nethers spike."
                m "I groan as his stream squirts even deeper, the heat reaching my very core as his piss begins to fill my womb."
                stop soundloop fadeout 1.0
                m "I groan as Bryce's stream finally begins to peter out, leaving my womb stuffed full of a dragon's bladderful."
            else:
                stop soundloop fadeout 1.0
                m "I swear I can feel some seeping all the way into my womb as he thrusts himself a little deeper, his stream finally petering out."
            Br laugh "Ahh, that's better."
            m "He leans down over me, nuzzling the back of my neck."
            Br smirk "Bet you'll enjoy remembering this when that comes out, huh?"
            m "I huff at his teasing, then grunt as he pushes himself even deeper into me, shaft disturbing my defiled passage."
            Br smirk "And you'll probably still smell like my piss for a while."
            return
            
            

    label .male_player:
        m "His tip smears lube up my ass crack, then applies pressure to my sphincter."
        m "I grunt as Bryce's cock spears open my loosened asshole, the alcohol and lube easing his passage, but not eliminating the pain as my muscle is stretched wide."
        Br flirty "Fuck, that's the perfect fit."
        Br smirk "And your insides feel so wet. Wonder how that happened?"
        m "He pulls back before our hips meet, then thrusts forward again, pushing his girth deep into my ass as his hips finally press mine to the bathtub edge."
        m "I can't help but gasp as his rough thrust pushes against my prostate, leaving my member twitching."
        m "Bryce's scaly hips grind in small circles against mine, scraping my skin as his cock moves in response inside me."
        if persistent.bangok_watersports == True:
            call .wasted_ws from .male_player_ws
        m "Then he pulls back again, this time beginning to fuck me properly."
        m "The shudders from my prostate don't quite ripple through my alcohol-addled body, but I can feel my lower body taking his rhythm, my spread legs trembling."
        m "As he lays down across my back, his hips maintaining his pace, my arms are too weak to hold up my upper body against his weight, pressing my chest and face against the side of the tub."
        show grey:
            alpha 0.5
        with dissolve
        m "I moan underneath him, breath escaping me again. Then I let my eyes flutter closed in time to his thrusts, my body drifting into a haze of languid fucking."
        show black with dissolve
        if persistent.bangok_knot == True:
            $ renpy.pause (1.0)
            hide grey
            hide black
            with dissolvemed
            m "I came back to my senses a while later, my right side pressed against the cold tile of the bathroom floor."
            m "The first thing I noticed was the pain in my sphincter, my ass straining as something too-large was gently trying to pull out."
            if persistent.bangok_inflation == True:
                m "Then I felt the pressure against my belly as Bryce's paw rubbed gently over it, holding me in place against him on the floor. My gut visibly bulged, my insides stretched by the heavy weight of fluids I didn't remember getting there."
            else:
                m "Then I felt Bryce's paw gently rubbing my belly, holding me in place against him on the floor."
            jump .knot_aftermath
        jump .aftermath

    label .female_player:
        m "His tip smears lube up my taint as it twitches, then pushes through my outer folds."
        m "I gasp as Bryce's cock spears open my alcohol-loosened nethers, the lube easing his passage, but not eliminating the shock of the intrusion."
        Br flirty "Fuck, that's the perfect fit."
        Br smirk "And your insides feel so wet. You were waiting for this, weren't you?"
        m "He pulls back before our hips meet, then thrusts forward again, pushing his girth deep into my pussy, until he rammed right up against the end of my passage."
        c "Nnnngh!"
        Br laugh "Ah, shoot. I'm a little too big for you, huh?"
        if persistent.bangok_watersports == True:
            call .wasted_ws from .female_player_ws
        m "I whimper as he tests my limits, gently probing the end of my passage."
        if persistent.bangok_cervpen == True:
            Br smirk "You know, the alcohol might have loosened you up enough to get through."
            menu:
                "Mmmmmes.":
                    m "My moan is all I can manage, but it's all the encouragement Bryce needs."
                "Nnnngh...":
                    m "My mumbled protest is too slurred to register."
            Br flirty "Hold on."
            m "I feel one of Bryce's paws on my back, pinning me to the tub."
            m "Then his hips began applying more pressure to his legnth, pressing against my delicate innermost gate."
            m "I squirmed, gasps of pain turning to pants of the same as my physiology resisted his intrusion."
            c "Fffh-- Nnnngh-- Bffh--"
            Br stern "Come on, [player_name]. Give--"
            m "Bryce let up and changed angle slightly, then thrust forward again, his tip finding the center of my cervix."
            if persistent.bangok_watersports == True && bangok_four_bryce4_store.bryce_ws == "vag":
                m "My resistance broke, my piss-soaked cervix giving way as his tip rammed my urine-filled womb like a fist."
                m "I slurred out a yell of pain, one that rapidly turned to panting moans as the burning feeling of the piss on the forced intrusion gave way to the drunken pleasure of feeling him stretching my very core."
            else:
                m "My cervix gave, bowing inward before finally stretching open to admit Bryce's girth into my deepest center."
                m "I slurred out a yell of pain, one that rapidly turned to panting moans as I felt his thick length twitching in my very core."
            m "Bryce lay down across my back, growling with pleasure himself."
            Br flirty "You're so tight, [player_name]. You're going to love this."
            m "He began to move again, not pulling out past my cervix, but instead letting it pull at his tip with every withdrawl, before flipping it back with his next thrust."
            if persistent.bangok_watersports == True && bangok_four_bryce4_store.bryce_ws == "vag":
                m "I can feel my womb stretching as he thrusts, its urine filling having nowhere else to go to get out of the way of his thick length."
                m "I weakly put a hand on my belly, feeling my skin stretch slightly with each thrust."
                m "I don't know how I'll take his load, but I'm too far gone to stop him."
            m "His hips maintain his pace as he puts more weight on me, to the point my arms can't lift me up enough to get a full breath in, pressed as I am against the side of the tub."
            show grey:
                alpha 0.5
            with dissolve
            m "I moan underneath him, breath escaping me as I feel my womanhood turned figuratively inside out for his pleasure, and mine."
            m "My eyes flutter closed as, finally, orgasm overtakes me and my mind departs."
            show black with dissolve
        else:
            Br stern "Alright, no deeper than this, I think."
            m "Then he pulls back again, this time beginning to fuck me properly."
            m "His thick girth pulls at my pussy lips as he pistons in and out, imposing his pace on my trembling body."
            m "My nethers are on fire, his thrusts squeezing the sensitive front of my passage between him and the edge of the tub."
            m "As he lays down across my back, his hips maintaining his pace, my arms are too weak to hold up my upper body against his weight, pressing my chest and face against the side of the tub."
            show grey:
                alpha 0.5
            with dissolve
            m "I moan underneath him, breath escaping me again. Then I let my eyes flutter closed in time to his thrusts, my body drifting into a haze of languid fucking."
            show black with dissolve
        jump .aftermath

    label .knot_aftermath:
        c "Uurgh."
        Br brow "Hey, just keep resting. That wine really did a number on you, huh?"
        m "I try to form a response, but my mouth is dry and my tongue feels thick."
        Br normal "It's okay. You're fine. Just rest."
        show black with dissolvemed
        m "Feeling too weak to do otherwise, I let my head fall back against Bryce's neck again, willing the alcohol to wear off and my body to recover."
        jump .aftermath

    label .aftermath:
        stop music fadeout 2.0
        $ renpy.pause (1.0)
        hide grey
        hide black
        with dissolvemed
        m "I wake up later, my head pounding and my body aching."
        m "I try to move, but my muscles feel like they're made of lead."
        m "I look around. I'm on my back, in the bathtub, legs hiked wide on either side of the tub."
        if persistent.bangok_inflation == True:
            if bangok_four_playerhasdick:
                m "My belly is still warm and swollen with fluids, my gut cramping painfully as I move."
            else:
                m "My belly is still warm and swollen with fluids, my womb spasming painfully as I move."
        m "Bryce is nowhere to be seen."
        c "B-Bryce?"
        if bangok_four_playerhasdick:
            m "I try to sit up, but yelp as I feel something hard and round move in my ass."
            m "Reaching between my legs, I find the wine bottle, neck-first in my sphincter, partially filled with the debauchery leaking from my body."
            if persistent.bangok_inflation == True:
                if persistent.bangok_watersports == True && bangok_four_bryce4_store.bryce_ws == "ass":
                    m "Pulling it out releases a rush of still-warm, disgusting cum and urine from my aching sphincter, the watery mass staining my asscheeks as it flowed down toward the tub's drain."
                else:
                    m "Pulling it out releases a rush of warm, cloying cum from my aching sphincter, the viscous mass pooling around my asscheeks as it seeped out of me."
        else:
            m "I try to sit up, but yelp as I feel something hard and round move in my pussy."
            m "Reaching between my legs, I find the wine bottle, neck-first between my nether lips, partially filled with the debauchery leaking from my body."
            if persistent.bangok_inflation == True:
                if persistent.bangok_watersports == True && bangok_four_bryce4_store.bryce_ws == "vag":
                    m "Though it hadn't been doing terribly much to stop things leaking before, pulling it out releases a fresh rush of still-warm, disgusting cum and urine from my aching lips, the watery mass staining my thighs as it flows down toward the tub's drain."
                else:
                    m "Though it hadn't been doing terribly much to stop things leaking before, pulling it out releases a fresh rush of warm, cloying cum from my aching lips, the viscous mass pooling around my asscheeks as it seeped out of me."
        menu:
            "Drink from the bottle.":
                m "Horniness overriding common sense, I take a swig from the bottle."
                m "The fluids left behind are warm and foul, but the debauchery of the moment elicits a throb of need in my groin."
                m "I swallow, the taste of the cum thick in my throat."
                m "Reinvigorated by the memories of what I'd done, I drag my legs off the sides of the tub and sit up, wincing as I disturb my abused pelvis."
            "Rest and recover.":
                if persistent.bangok_inflation == True:
                    m "I let my head fall back against the tub's edge and put a hand on my belly, willing the mess to drain from my body and the growing headache to stay away."
                else:
                    m "I let my head fall back against the tub's edge, willing the aches to leave my body and the growing headache to stay away."
                m "It might have been minutes, or it might have been hours, but eventually I'm able to lower my legs from the sides of the tub and sit up, wincing as I disturbed my abused pelvis."

        if persistent.bangok_inflation == True:
            m "There's a scrawled note sitting on the edge of the sink, but I ignore it for now, stumbling to the toilet to try to keep any more mess from running down my legs."
            m "When I get back to the note, it reads:"
        else:
            m "There's a scrawled note sitting on the edge of the sink."
        m "Hey [player_name],\n You were leaking everywhere after I pulled out. I just tried to stop the flow.\n Called away on police business. Had to leave. Sorry.\nBryce."
        m "Squinting at the note takes a lot of effort, but I can make out Bryce's handwriting."
        m "I can also make out the growing pounding in my head, the alcohol from last night truly catching up with me."
        c "(Fuck, Bryce, that--)"
        m "I don't even finish the thought before my abused insides finally wake up to their pain and I heave into the sink."
        $ renpy.pause(0.5)
        nvl clear
        window show
        n "Recovery and cleaning up took a few more hours."
        n "I still had to make up my mind about whether last night was what I had wanted."
        n "Was it a mistake to get that far gone around him?"
        n "Was it something anyone was at fault for?"
        n "Or was it exactly what I'd wanted?"
        n "The only real remaining question was: would I see him at the fireworks?"
        n "Could I continue after that? Or was that too far?"
        $ renpy.pause(0.5)
        window hide
        nvl clear

        jump bangok_four_bryce4_shower_end

label bangok_four_bryce4_shower_end:
    $ mp.bryceromance = True
    $ mp.save()
    $ brycestatus = "good"
    stop music fadeout 2.0
    $ renpy.pause (0.5)
    $ brycescenesfinished = 4
    jump _mod_fixjmp

label todo_out_of_content_bangok_four_bryce4_shower:
    play sound "fx/system3.wav"
    s "Bryce4 Shower Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")
