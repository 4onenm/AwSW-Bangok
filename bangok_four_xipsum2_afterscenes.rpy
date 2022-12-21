init python in bangok_four_xipsum2_sharing3_store:
    sharing3_cervpen = False

    unsanitary_pissed_in_ipsum = False


label bangok_four_xipsum2_ipsum_sharing1:
    $ renpy.pause(0.5)
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause(1.0)

    play sound "fx/phonering.ogg"
    scene o3 at Pan((0, 100), (0, 250), 3.0) with dissolveslow
    $ renpy.pause(1.3)
    play sound "fx/phonepickup.ogg"

    Ip normal bangok blush "Hello, [player_name]."
    c "Ipsum?"
    c "It's the middle of the night. What...?"
    if bangok_four_playerhasdick == True:
        m "I felt the rustling of fabric over my shaft and realized Ipsum must be looking at his end of his stimulating devices."
    else:
        m "I felt the rustling of fabric over my outermost folds and realized Ipsum must be looking at his end of his stimulating devices."

    if bangok_four_xipsum2_store.sharing > 1:
        Ip normal bangok blush "Well, Lorem wasn't interested. But asking him gave me a thought."
    Ip happy bangok blush "Since you're still wearing the briefs, is a human-style onahole available? Perhaps you'd like an... overnight visitation."

    menu:
        m "Do I want Ipsum to fuck me again?"
        "Accept.":
            Ip happy bangok blush "Happy to oblige."
            m "(Click.)"
            c "(He hung up?)"
            m "Air wafted over my nethers as he moved his end of the devices."

            jump todo_out_of_content_bangok_four_xipsum
        "Reject.":
            c "It's just comfortable evening-wear. Don't read too much into it."
            Ip sad "Oh."
            Ip think "Alright then. Do let me know when you are, {i}ahem{/i}, available."
            c "Yeah. Sure."
            Ip sad "Goodnight."

    $ renpy.pause(0.5)
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    jump _mod_fixjmp










label bangok_four_xipsum2_ipsum_sharing3:
    m "I began to go about my morning routine, preparing for the day of the fireworks."

    play sound "fx/phonering.ogg"
    scene o4 at Pan((0, 100), (0, 250), 0.0) with dissolveslow
    $ renpy.pause(1.3)
    play sound "fx/phonepickup.ogg"

    Ip happy bangok blush "[player_name]!"
    Ip normal "You remember how you agreed you might be interested in some other members of my lab having access to the, ah, thing?"
    m "My hand went to my crotch, where I was still wearing Ipsum's comfortable, modified swim briefs."
    c "Yes...?"
    Ip happy bangok blush "Are you available?"
    c "{i}Now?{/i}"
    Ip sad "Well, I just got into the lab, and I have a few eyes on me right now trying to tell if I'm being serious, so now would be preferable to later."
    c "(Well, later I'm going out to watch the fireworks, so if I want to be cleaned up, I'd better do this now.)"
    menu:
        "Accept.":
            $ renpy.pause(0.5)
        "Reject.":
            c "I'm sorry. I can't today."
            $ renpy.pause(0.5)
            Ip sad "Oh."
            $ renpy.pause(0.5)
            Ip think "Well, how does tomorrow look, then?"
            c "Maybe. I don't know."
            $ renpy.pause(0.5)
            Ip sad "I see. Well, talk soon, then."
            $ renpy.pause(0.5)
            m "(Click.)"
            $ renpy.pause(0.5)
            jump bangok_four_xipsum2_ipsum_sharing3_return

    Ip happy bangok blush "Thank you."
    if bangok_four_xipsum2_store.protection == True:
        m "His voice became more muffled, as he began speaking to someone else. I definitely heard something about condoms, though, which was a relief."
    else:
        m "His voice became more muffled, as he began speaking to someone else."
    # play sound "fx/undress.ogg"
    # m "Realizing I was probably about to be fucked three ways from Sunday, I hurriedly stripped out of my regular clothes, leaving just Ipsum's briefs."
    if bangok_four_playerhasdick == False:
        m "I felt the cold air of someplace else on my pussy and asshole, abruptly leaving me feeling completely nude, despite the tight briefs around my hips."
        m "I set the phone down, trying to keep my balance as I was startled by the sensation."
        m "Then spurts of lube fell across my front and rear entrances, followed by a rough, scaly hand rubbing it in, slipping inside my folds to spread it."
    else:
        m "I felt the cold air of someplace elese on my cock and asshole, abruptly leaving me feeling completely nude, despite the tight birefs around my hips."
        m "I set the phone down, trying to keep my balance as I was startled by the sensation."
        if bangok_four_xipsum2_store.protection == True:
            m "Then I felt a condom somewhat roughly unrolled down my cock, followed by spurts of lube across my ass and cock and a rough scaly hand pumping me and rubbing it in."
        else:
            m "Then spurts of lube fell across my ass and cock, followed by a rough scaly hand pumping me and rubbing it in."

    scene o4:
        ypos -456
    with ease

    m "My knees wobbled as I clutched my crotch, overcome by sensations before the fucking had even begun."

    if bangok_four_playerhasdick == False:
        if bangok_four_xipsum2_store.protection == True:
            m "Then the first condom-wrapped cock nestled into my folds and thrust, faster than I could deal with."
        else:
            m "Then the first cock nestled into my folds and thrust, faster than I could deal with."
        $ bangok_four_malepartners += 1
        play soundloop "fx/bangok_poundofsalt.ogg"
        m "Another joined it at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."
        $ bangok_four_malepartners += 1
    else:
        m "Then I felt scaly folds wrapping around my tip, before my shaft was shoved somewhere hard enough it hurt at the base of my length."
        $ bangok_four_femalepartners += 1
        if bangok_four_xipsum2_store.protection == True:
            m "A condom-wrapped cock prodded at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."
        else:
            m "A cock prodded at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."
        $ bangok_four_malepartners += 1

    play sound "fx/tableslap.wav"
    with vpunch
    m "I fell against the table with the telephone, struggling to pick it back up."
    c "S-Slower, Ipsum!"
    Ip normal bangok blush "Tone it down, a little. They're, ah, breakable."
    if bangok_four_playerhasdick == False and persistent.bangok_cervpen == True:
        Ip think "By the way, I have yet to ask, does your species have a cervix protecting your uterus? And if so, is it penetrable? How large a partner can you manage, and how deep might they go?"
        menu:
            "Y-Yes, we do! {i}Don't{/i}--":
                $ bangok_four_xipsum2_sharing3_store.sharing3_cervpen = False
            "D-Deep--!":
                $ bangok_four_xipsum2_sharing3_store.sharing3_cervpen = True

    m "Muffled voices responded to Ipsum, then the cock at my ass slipped through my fingers, and pressed inside me."
    play sound "fx/impact.wav"
    $ renpy.pause(0.3)
    with vpunch
    play soundloop "fx/bangok_poundofsalt.ogg"
    c "A-Ah!"
    if bangok_four_playerhasdick == False:
        m "My legs gave out, the fucking of both my holes by my remote suitors too much for me to bear."
    else:
        m "My legs gave out, the rough entrance of my ass too much to bear under the assailing of my shaft like a cheap dildo."

    m "I writhed on the floor, the phone out of reach on the table as my lower body was assaulted with pleasure."

    if bangok_four_playerhasdick == False:
        m "Thrust after thrust filled and emptied me, the two cocks sharing no cadence whatsoever as they each used me to climb toward their peaks."
        if bangok_four_xipsum2_store.protection == True:
            m "Then the one in my cooch began to twitch, and I felt warm, heavy ropes weighing down its condom reservoir."
            m "It pulled out, still cumming, but I got no respite as another, larger shaft took its place."
        else:
            m "Then the one in my cooch began to twitch, and I felt warm, heavy ropes of cum jet over my inner walls."
            if persistent.bangok_knot == True:
                m "A bulbous knot of flesh pressed at my outer folds, spreading my entrance just slightly further as the male injected his cum as deep as he could go without tying with me."
            if persistent.bangok_inflation == True:
                m "When the cock pulled out, a thick pool of cum rested against my innermost gate. Then another, larger cock took its place."
            else:
                m "The cock pulled out, leaving my passage slightly damper and stickier. Then another, larger cock took its place."
        $ bangok_four_malepartners += 1
    else:
        m "Juices flowed around my dick, dribbling down around my balls as the cunt on the far side squeezed and massaged me."
        m "I thrust, uselessly, from the simultaneous fucking of my ass and shaft. I couldn't force myself any further into what was already attached to my hips."

    if bangok_four_xipsum2_store.protection == True:
        m "Finally, the one in my ass stopped, pulses of his load travelling up his length to fill his condom's reservoir."
        m "I sighed as it slid out, taking its load with it, only to then feel a new head prodding at my weakened sphincter."
        $ bangok_four_malepartners += 1
        c "Ah-h!"
        m "This one stretched me wider. As it sank in, I realized it was going deeper, too."
    else:
        m "Finally, the one in my ass stopped, packets of his load travelling up his length to spray out into my rear."
        if persistent.bangok_inflation == True:
            m "Pulse after pulse spurt into me, leaving my ass feeling heavy and full."
        m "I sighed as it slid out, feeling its load settle inside me, only to then feel a new head prodding at my weakened sphincter."
        $ bangok_four_malepartners += 1
        c "Ah-h!"
        m "This one stretched me wider, scraping off my inner walls the seed of its predecessor. As it sank in, I realized it was going deeper, too."

    if bangok_four_playerhasdick == True:
        m "The cooch around my shaft shoved down, taking me completely and grabbing on, spasming and tugging, trying to milk me for every last drop."
        m "Somehow I held on, the rough treatment not quite enough to push me over that edge."
        m "After several seconds sitting on me, the wet passage disappeared, replaced by the cold of empty air."
        m "Then I felt a long, sinuous muscle wrap around my length, circling downward, until it was licking around my crotch, just lifting the tight fabric of the briefs."
        m "I groaned, so very close."
        stop soundloop fadeout 1.5
        m "Then the mouth disappeared, followed a few moments later by the guy in my ass pulling out."
        if bangok_four_xipsum2_store.protection == True:
            m "Someone stripped off my condom, the feeling almost putting me over that edge."
            m "They rolled a new one on, dribbled some lube."
        m "Then, abruptly, someone's loose ass wrapped around my length, as at the same time someone thrust into my rear."
        show black with dissolve
        play sound "fx/extinguish.ogg"
        m "I moaned, cumming hard, the cock in my ass twitching and spurting in perfect time."
        m "I realized, with a start, I'd just cum in myself!"
        hide black with dissolvemed
        if bangok_four_xipsum2_store.protection == True:
            m "Before I could think much about it, my shaft was tugged back out of me, my condom and load going with it."
        else:
            m "Before I could think much about it, my shaft was tugged back out of me, leaving a dribble of cum at my loosened sphincter."
        play sound "fx/bangok_poundofsalt.ogg"
        m "Then the large cock that had been plowing my rear returned, picking up right where it had left off."

        jump todo_out_of_content_bangok_four_xipsum_sharing3
    else:
        m "The two cocks rubbed together inside me, sandwiching my inner walls."
        m "I gave up holding back, moaning loudly as, with each of their uneven thrusts, they pressed pleasure from my passage, stretching me wide."
        if bangok_four_xipsum2_store.protection == True:
            m "Warmth blossomed in my passage as the one assailing my front entrance began to loose its load into its condom."
            m "It slid to a stop, serving for a long moment as an obstacle for the other to press against."
            m "Then it slid out, taking its load with it, leaving my cooch parted and cold."
        else:
            m "Warmth blossomed in my passage as the one assailing my front entrance loosed its load into me."
            m "Its seed layered over that of the first, slathering and soiling my passage."
            if persistent.bangok_inflation == True and persistent.bangok_cervpen == True:
                m "There was so much, my vagina alone couldn't handle it. As they sank in one last thrust, still releasing pulse after pulse, I gasped as it sprayed through my innermost gate, flowing into and staining my womb."
            m "Then, finished, it slid out, leaving my pussy parted and dripping."
        m "The next cockhead at my entrance, I could feel immediately, was barely going to fit if it could do so at all."
        $ bangok_four_malepartners += 1
        c "W-W-Wait--"
        m "My hands snapped to my crotch but, without my spine to guide my hand, I couldn't get under the waistband in time."
        stop soundloop fadeout 2.5
        m "The tip spread me open, stretching out the folds in my entrance and leaving me taut and full."
        m "Even the fucking of my asshole came to a faltering stop, as if the person engaged in that activity was looking over to watch what this cock would do to me."
        m "I could see the slightest bulge running up my belly, as I was forced open by this large shaft, inch by maddening inch."
        m "Squirming in ecstacy, I pressed the briefs into my crotch, wondering how far this cock could go on."
        if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.sharing3_cervpen == True:
            if bangok_four_xipsum2_store.protection == False:
                m "Like a plunger in a syringe, the cock scraped all the cum deposited before it off my walls, pressing it through my cervix in a lewd spray."
            m "I ran out of room, the thick cockhead butting up against my innermost gate. It hesitated, a moment, then seemed to obey my whispered prayer to keep going."
            m "Pain rapidly mixed with pleasure, the impossible penetration an unstoppable force against the weak defenses of my flesh."
            m "Bowing my cervix inward, the complete stranger's cock breached my womb."
            show white with dissolve
            $ renpy.pause(0.8)
            m "For several seconds I completely whited out, every nerve south of my navel awash with electric sparks from my complete and total filling."
            play soundloop "fx/bangok_poundofsalt.ogg" fadein 2.0
            hide white with dissolveslow
            m "I came back to the dull sensation of thrusting, my onahole of a canal an electric firestorm with every inch moved, while the motion in my rear was a more down-to-earth, filling feeling."
            $ renpy.pause(1.0)
        else:
            m "I ran out of room, the thick cockhead butting up against my innermost gate and eliciting a cry from my lips."
            m "It seemed to hear, as it backed off almost a full inch, before pulling out further and beginning to thrust."
            play soundloop "fx/bangok_poundofsalt.ogg" fadein 0.5

            m "I swooned under the two cocks' thrusts, until my speared canal finally spasmed and I passed over my peak."
            show white with dissolve
            $ renpy.pause(0.8)
            hide white with dissolveslow
            $ renpy.pause(1.0)

        m "The bulge in my belly moved, pistoning in and out with the thick shaft using my body for its pleasure."
        m "Then both shafts inside me began to pulse and twitch as they thrust, warmth spreading up their lengths to spurt out in thick ropes inside me."
        if bangok_four_xipsum2_store.protection == True:
            m "Their condom reservoirs bloated, the warmth contained, safe, and fulfilling. The shaft in my ass began to pull out, taking his with him while he was still cumming."
            if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.sharing3_cervpen == True:
                m "Meanwhile, the length penetrating my deepest center continued to thrust, seemingly oblivious to its own climax nestling in my most sacred place."
                if persistent.bangok_inflation == True:
                    m "The condom expanded with the size of the load, the balloon of cum growing until my womb had no choice but to expand, too, leaving me pregnant with a thick blob of cum, periodically expanding and contracting with the thrusts spearing my body."
            else:
                m "The shaft in my stretched vagina continued to thrust, seemingly oblivious to its own climax nestling at the end of my canal."
        else:
            m "Their cum mixed with the loads that had come before, leaving me saturated with virile seed."
            if persistent.bangok_inflation == True:
                if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.sharing3_cervpen == True:
                    m "My colon was packed full, my guts thick and heavy with dragon seed. My womb couldn't contain the directly-injected flow, the flood into my deepest recesses forcing to me expand until I appeared pregnant with a thick blob of cum."
                    m "The cock in my ass began to pull out, finished, but the girthy invader penetrating my womb continued to thrust, seemingly oblivious to its own climax bloating my most sacred place, periodically forcing me to expand, then contract with the flow of fluid."
                else:
                    m "My colon was packed full, my guts thick and heavy with dragon seed. With the girthy invader still pumping, the seed hadn't room to pool in my saturated canal. It sprayed through my innermost gate, flooding into my deepest recesses and forcing to me expand until I appeared pregnant with a thick blob of cum."
                    m "The cock in my ass began to pull out, finished, but, seemingly oblivious to its own climax, the girthy invader continued to thrust its cum through my cervix, bloating my most sacred place, periodically forcing me to expand, then contract with the flow of fluid."
        stop soundloop fadeout 0.5
        m "Then, finally, the massive cock in my pussy realized it was finished and dragged slowly from my nethers."
        if bangok_four_xipsum2_store.protection == True:
            if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.sharing3_cervpen == True:
                if persistent.bangok_inflation == True:
                    m "I cried out as the massive blob of cum tried to follow, my hips not wide enough to let it go all at once, even had it wanted to."
                    m "In the end elasticity won out, and the fluid flowed through my breached inner gate to the lower part of the condom and, eventually, out of me to the far side."
                else:
                    m "I cried out as his condom's reservoir tried to follow. My breached inner gate was still slightly too small, and forcing it felt like the stranger's cock would tear out part of my guts."
                    m "Elasticity won out, the blob of cum dragging maddeningly through my parted depths."
        else:
            if persistent.bangok_inflation == True:
                m "I groaned as the pressure receded from my womb, cum flowing out of my weakened defenses, slowly reducing the baby bump in my belly to a mere bump, until my abused outer folds were allowed to hang empty again."

        m "I wasn't done, though."

        m "The moment my holes were free again, I felt a smaller cock nestling in my gaping asshole, followed by a second in my loosened canal."
        $ bangok_four_malepartners += 1
        if bangok_four_xipsum2_store.protection == True:
            m "Unlike the others, these were just using, rather than abusing, my holes. I sighed with relief, rubbing my belly as I enjoyed this final, gentle double-fuck."
        else:
            if persistent.bangok_inflation == True:
                m "Unlike the others, these were just using, rather than abusing, my holes. They plugged in the heavy loads of seed left inside me, leaving me warm, contented, and full. I sighed with relief, rubbing my bulging belly as I enjoyed this final, gentle double-fuck."
            else:
                m "Unlike the others, these were just using, rather than abusing, my holes. They plugged in the heavy loads of seed left inside me, leaving me warm, contented, and full. I sighed with relief, rubbing my belly as I enjoyed this final, gentle double-fuck."

        m "Also unlike the others, after he came, spurting his paltry-by-comparison load of cum, he didn't pull out."
        if bangok_four_xipsum2_store.protection == False:
            if persistent.bangok_knot == True:
                m "His knots were just barely girthy enough to plug inside all the seed I'd collected, leaving me completed, rather than draining."
            else:
                m "His shafts were just barely girthy enough to plug inside all the seed I'd collected, leaving me completed, rather than draining."
        else:
            m "His condom reservoirs rested inside me, leaving my holes completed, rather than empty."

        m "I wanted to lie there and bask, but I could hear noise coming from the phone's reciever."
        if bangok_four_xipsum2_store.protection == False and persistent.bangok_inflation == True:
            m "Struggling to sitting upright, I felt the heavy loads of fluid inside me shift, then begin to drain despite the cocks still in me, puddling in the briefs beneath me, and passing through to the other side."
            m "I managed to reach onto the top of the table and pull down the phone reciever."
            Ip happy bangok blush "O-Oh! H-Hah, I thought... well, you must be pretty full over there."
            Ip normal bangok blush "Want me to see if a couple of the others will volunteer to be larger plugs?"
            c "I... I'm good, thanks."
        else:
            m "Struggling to sitting upright, I managed to reach onto the top of the table and pull down the phone reciever."
            Ip normal bangok blush "[player_name], whenever you'd like to respond, that'd be good."
            c "H-Here."
            Ip happy "Excellent!"



    Ip happy bangok blush "How did that feel?"
    c "I... I don't think I can walk for a bit."
    Ip normal bangok blush "In a good way, or...?"
    menu:
        "A good way, yeah.":
            $ renpy.pause(0.5)
        "Th-That was a lot. I'm going to need a while to recover.":
            $ renpy.pause(0.5)
    if bangok_four_xipsum2_store.protection == False and persistent.bangok_inflation == True:
        Ip normal bangok blush "Well, let me know when you make it to the bathtub to drain, and I'll pull out."
    else:
        Ip normal bangok blush "Well, let me know when you make it somewhere to drain, and I'll pull out."
    c "How magnanimous of you."
    if bangok_four_xipsum2_store.protection == False and persistent.bangok_inflation == True:
        c "(How am I going to even move? I'm so full...)"

    Ip sad "Oh, actually, I think I might have to go. Someone's here asking questions about the noise."
    c "W-Wait, Ipsum--!"
    m "(Click.)"

    m "I grunted, his cocks still inside me, as I wondered how I'd clean up to prepare for the day of the fireworks."
    $ renpy.pause(0.5)
    scene black with dissolve
    $ renpy.pause(1.0)
    scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
    jump bangok_four_xipsum2_ipsum_sharing3_return










label bangok_four_xipsum2_ipsum_sharing3_unsanitary:
    m "I began to go about my morning routine, preparing for the day of the fireworks."
    m "Something felt off, though, as I rolled out of bed to move about my apartment."
    if bangok_four_playerhasdick == True:
        m "I realized, with a start, that my ass was plugged with something, and my penis was surrounded by warm, shifting flesh!"
    else:
        m "I realized, with a start, that I could feel a cock in my ass, and another in my pussy!"
    $ bangok_four_malepartners += 1
    m "I scrabbled at the waistband, trying to pull the briefs down, only to realize they had been glued in place in my sleep."
    if bangok_four_playerhasdick == False:
        m "Worse still, something blocked my urethra, meaning even if I did want to piss in the magic briefs, I couldn't."

    c "(Damnit Ipsum, you naughty piece of dragon ass. I didn't agree to anything all-day like this!)"

    m "I stumbled over to the phone, planning to give Ipsum an earful."
    play soundloop "fx/phonering.ogg"
    c "(Come on...)"
    $ renpy.pause(1.0)
    c "(Really?)"
    $ renpy.pause(1.0)
    c "(Ipsum, don't do this to me and blow me off.)"
    $ renpy.pause(1.0)
    stop soundloop
    play sound "fx/phonepickup.ogg"
    $ renpy.pause(0.5)

    c "Ipsum, damnit, what the hell?"
    Lo think b "Huh? [player_name]?"
    c "Lorem?"
    Lo normal b "Yeah. Are you trying to reach Ipsum?"
    if bangok_four_playerhasdick == True:
        m "I tried to keep my voice under control as the cock inside my ass twitched."
    else:
        m "I tried to keep my voice under control as the cocks inside me twitched."
    c "Yes. Yes I am."
    Lo think b "He left for work really early this morning. I can call him and tell him to call you."
    c "Sure. Thanks."
    Lo think b "Okay."
    m "(Click.)"
    $ renpy.pause (0.8)
    if bangok_four_playerhasdick == True:
        m "I waited by the phone, trying not to think about the cock in my ass, as every shift in my weight caused me to clench down on it a little."
        if persistent.bangok_watersports:
            play soundloop "fx/faucet2.ogg" fadein 1.0
            m "Then I felt it twitch back, and a hot stream of liquid began to jet into my colon"
            c "(Agh. I-Ipsum...)"
            m "I flushed with embarassment as he used my ass as a urinal, pissing in me from afar as I stood in my living room."
        else:
            play sound "fx/extinguish.ogg"
            m "Then I felt it twitch back, and begin to pulse sticky ropes of cum into my colon."
            c "(Agh. I-Ipsum...)"
            m "I flushed with embarassment as he used my ass as a cumdump, dumping his load in me from afar as I stood unsatisfied in my living room."
    else:
        m "I waited by the phone, trying not to think about the cocks inside me, as every shift in my weight caused me to clench down on them a little."
        if persistent.bangok_watersports:
            play soundloop "fx/faucet2.ogg" fadein 1.0
            m "Then I felt them twitch back, and twin hot streams of liquid began to jet into my front and rear."
            c "(Agh. I-Ipsum...)"
            m "I flushed with embarassment as he used me as a living urinal, pissing in me from afar as I stood in my living room."
        else:
            play sound "fx/extinguish.ogg"
            m "Then I felt it twitch back, and begin to pulse sticky ropes of cum into my front and rear."
            c "(Agh. I-Ipsum...)"
            m "I flushed with embarassment as he used my holes as a cumdump, dumping his load in me from afar as I stood unsatisfied in my living room."
    $ renpy.pause(0.8)
    play sound "fx/phonering.ogg"
    $ renpy.pause(0.8)
    play sound "fx/phonepickup.ogg"
    stop soundloop fadeout 2.0

    if persistent.bangok_watersports:
        if bangok_four_playerhasdick == True:
            m "The phone finally rang, and I yanked it off the reciever the stream of liquid flowing into me came to an end."
        else:
            m "The phone finally rang, and I yanked it off the reciever as the streams of liquid flowing into me came to an end."
    else:
        if bangok_four_playerhasdick == True:
            m "The phone finally rang, and I yanked it off the reciever the pulses of seed flowing into me came to an end."
        else:
            m "The phone finally rang, and I yanked it off the reciever as the pulses of seed flowing into me came to an end."

    c "I-Ipsum?"

    Ip normal bangok blush "Oh, hello! What an unexpected surprise. Now, why would you be asking Lorem to call me to call you while I'm at work?"
    c "D-Damnit Ipsum, you know why!"
    Ip happy bangok blush "Oh yes, yes of course."
    m "I could hear Ipsum's shit-eating grin through the phone."
    if persistent.bangok_watersports:
        Ip happy bangok blush "The adhesive is soluble in even weak acids, so all you'd need do is... overflow."
    else:
        Ip happy bangok blush "The adhesive is soluble in even weak bases, so all you'd need do is... overflow."

    c "You've gotta be kidding me."
    if bangok_four_playerhasdick == True:
        m "I tried squeezing my rectal muscles, but with my hole stuffed with one of Ipsum's shafts, the fluid inside wasn't interested in escape."
    else:
        m "I tried squeezing my inner muscles, but with my holes stuffed with Ipsum's shafts, the fluid inside wasn't interested in escape."
    Ip normal bangok aheago briefs "Nnngh."
    Ip normal bangok blush "You may find that difficult so long as they keep obeying the signs."
    if bangok_four_playerhasdick == True:
        c "Signs? What signs? Who--? Where did you put my ass?! And my cock?!"
        Ip normal bangok blush "The latter I'm keeping safe with me."
        if persistent.bangok_watersports:
            Ip happy bangok blush "The former? Well, you didn't hear it from me, but I heard the production facility factory floor restroom has a new, realistic-looking mounting-stand-style urinal."
        else:
            Ip happy bangok blush "The former? Well, you didn't hear it from me, but I heard the production facility factory floor restroom has a new mounting stand for employees to blow off steam... with a very realistic looking hole."
    else:
        c "Signs? What signs? Who--? Where did you put my holes?!"
        if persistent.bangok_watersports:
            Ip happy bangok blush "Well, you didn't hear it from me, but I heard the production facility factory floor restroom has some new, realistic-looking mounting-stand-style urinals."
        else:
            Ip happy bangok blush "Well, you didn't hear it from me, but I heard the production facility factory floor restroom has some new, realistic-looking mounting stands for employees to blow off steam... with very realistic looking holes."
    Ip normal bangok blush "It should be busy down there in a few minutes, since their workday is just about to st--ah! Start."
    m "I felt the cock dragged out of my ass just as he gasped, confirming a suspicion I had."
    c "Are you fucking me right now?!"
    Ip normal bangok blush "I'm actually not. That would probably be your first visitor."
    m "I grunted as I felt the cock slowly pressed back inside, then yanked out again. My hole clenched."
    c "They're plugging me with your cocks!"
    Ip happy bangok blush "They're just obeying the signs."
    Ip normal bangok blush "I should go. My first break is in an hour, at which point I'll come shut that experiment down. Until then, have fun!"
    c "Ip--!"
    m "(Click.)"

    $ bangok_four_malepartners += 1
    if persistent.bangok_watersports == True:
        if bangok_four_playerhasdick == True:
            m "Then I felt another cock, slightly larger than his, prodding at my pucker."
            c "Oh n-no--"
            m "It pressed in, popping its tip through my tight ring before letting go."
            play soundloop "fx/faucet2.ogg" fadein 1.0
            m "Another hot stream of urine poured into my colon, causing my lower body to flush with heat."
            m "With my inner walls already saturated with Ipsum's pissload, though, the stranger's liquid waste quickly began to pool around his tip."
            stop soundloop fadeout 0.5
            m "He yanked his cock out of my ass, leaving gravity to dump his piss right back at him through my parted pucker."
        else:
            m "Then I felt Ipsum's cock slide back into my ass while his other pulled out of my pussy."
            m "A finger prodded at my front entrance, forcing me to clench and shiver. Then a cockhead slightly larger than Ipsum's pressed."
            c "Oh n-no--"
            m "It just popped its tip through into my canal before letting go."
            play soundloop "fx/faucet2.ogg" fadein 1.0
            m "Another hot stream of urine poured into my love passage, causing my lower body to flush with heat."
            m "With my inner walls already saturated with Ipsum's pissload, though, the stranger's liquid waste quickly began to pool around his tip."
            stop soundloop fadeout 0.5
            m "He yanked his cock out of my hole, leaving gravity to dump his piss right back at him through my parted lower lips."
    else:
        if bangok_four_playerhasdick == True:
            m "Then I felt another cock, slightly larger than his, prodding at my pucker."
            c "Oh n-no--"
            m "It pressed in, popping its tip through my tight ring before encountering Ipsum's sticky load."
            m "He paused for a second, then, evidently unsatisfied with getting sloppy seconds, yanked his tip back out of my ass."
        else:
            m "Then I felt Ipsum's cock slide back into my ass while his other pulled out of my pussy."
            m "A finger prodded at my front entrance, forcing me to clench and shiver. Then a cockhead slightly larger than Ipsum's pressed."
            c "Oh n-no--"
            m "It just popped its tip through into my canal before encountering Ipsum's sticky load."
            m "He paused for a second, then, evidently unsatisfied with getting sloppy seconds, yanked his tip back out of my hole."

    m "I shuddered, legs wobbling as he shoved Ipsum's cock back into place."

    $ renpy.pause (0.8)

    if bangok_four_playerhasdick == True:
        if persistent.bangok_watersports == True:
            m "As I stood for an embarassed moment, I could feel Ipsum's ass shifting around my cock as he went about his day in his lab."
            m "There was more than enough in my bladder to give him more than he'd given me, to at least force him through a taste of what he was putting me through."
            menu:
                "Retaliate.":
                    $ renpy.pause (0.5)
                    $ bangok_four_xipsum2_sharing3_store.unsanitary_pissed_in_ipsum = True
                    c "(Let's see how you like it.)"
                    play soundloop "fx/faucet2.ogg" fadein 2.0
                    m "I let go, only able to manage a trickle at first, then pushing until I was pissing hard and fast in Ipsum's ass."
                    m "I could imagine him standing there, flushed and embarassed by his coworkers as someone used {i}him{/i} as a urinal."
                    m "Unfortunately, like the stranger who'd just pissed in my ass, I realized too late I was pissing into someone standing upright."
                    stop soundloop fadeout 2.0
                    m "My warm liquid waste formed a puddle where Ipsum's ass squeezed my length, squelching lewdly about my cock as he moved."
                    m "Only leaving more flushed and aroused, I considered my next move."
                "Hold it.":
                    $ renpy.pause (0.5)
                    $ bangok_four_xipsum2_sharing3_store.unsanitary_pissed_in_ipsum = False
                    c "(I don't need to be that mean.)"
                    c "(Or maybe he likes it, and denying it will be more mean?)"

        m "Prodding around the adhesive ring holding the briefs' portal to my hole, I couldn't feel any give whatsoever."
    else:
        m "Prodding around the adhesive ring holding the briefs' portals to my holes, I couldn't feel any give whatsoever."

    if persistent.bangok_watersports == True:
        m "Clearly I either needed to collect a lot more and \"overflow,\" as Ipsum had put it, or I needed their piss to pour out of me more slowly so it didn't fall away from my hole before it could dribble from my holes to the edge of the portals."
        m "Either way, I couldn't spray it back out at my \"visitors\" without turning them off of \"using\" me, which would result in me being stuck like this for an hour or more."
    else:
        m "Clearly I needed to collect a lot more and \"overflow,\" as Ipsum had put it, so I needed to make myself more appealing."
        m "I couldn't leak loads it back out at my \"visitors\" without turning them off of \"using\" me, which would result in me being stuck like this for an hour or more."

    play sound "fx/steps/clean2.wav"
    scene black with dissolvemed
    m "I walked to the bathroom, considering how I'd want to arrange myself to take this prank."
    $ renpy.pause (0.5)
    scene bath with dissolve
    $ renpy.pause (0.5)

    # menu:
    #     "Bathtub, ass-up.":
    #         jump bangok_four_xipsum2_ipsum_sharing3_unsanitary_assup
    #     "Bathtub, lying down.":
    #         jump todo_out_of_content_bangok_four_xipsum_sharing3

label bangok_four_xipsum2_ipsum_sharing3_unsanitary_assup:
    $ renpy.pause (0.5)
    m "After a few moments consideration, I sat on the edge of the tub, then lay back with my head toward the facuet, keeping my ass up on the smooth curve of the back-reclining portion."

    m "As I was arranging my legs, I was interrupted by the slow slide of Ipsum's cock plug being pulled gradually from my ass, out to the tip."

    if bangok_four_playerhasdick == True:
        m "Then the tip popped out, and was replaced with another stranger's cockhead."
        m "I grunted as it entered, stretching me slightly larger than a human's would, the dragon's slit juices barely enough to lubricate his entry."
        m "Then the cock kept coming, sinking in inch by maddenning inch, until until a horizontal slit between hard plates rested against my rear."
    else:
        m "Then the cock plugging my pussy was dragged out the same way. Spotting what he really wanted, the guy shoved Ipsum's cock roughly back into my ass, then dragged out the one in my pussy entirely."
        m "Then I felt this stranger's cockhead at my front entrance."
        m "I grunted as it entered, stretching my entrance slightly more than a human's would."
        m "Then the cock kept coming, sinking in inch by maddenning inch, until until a horizontal slit between hard plates rested against my folds."
    $ bangok_four_malepartners += 1

    if persistent.bangok_watersports == True:
        c "(Oh no. I think this guy's not just interested in pissing and leaving.)"
    else:
        c "(Oh no. I think this guy's actually going to fuck me.)"
        c "(Wait, I need that.)"

    play soundloop "fx/bangok_poundofsalt.ogg" fadein 5.0
    m "He pulled out an inch, then thrust back in, then pulled out two inches, then thrust again."

    if persistent.bangok_watersports == True:
        m "Pretty soon, the invisible, nameless stranger was fucking my piss-stained hole for real, leaving me shivering and gasping from the sensations."
    else:
        m "Pretty soon, the invisible, nameless stranger was fucking my cum-stained hole for real, leaving me shivering and gasping from the sensations."
    stop soundloop fadeout 0.5
    m "Just as I was getting into it, though, he stopped, abruptly, then pulled out completely."
    $ renpy.pause (1.2)
    if bangok_four_playerhasdick == True:
        m "I held my crotch, wondering why the guy would stop halfway through. I thrust for some stimulation, but was unable to move my cock in Ipsum's ass with his ass already attached to my hips."
        $ renpy.pause (1.2)
        m "My silent question was answered a half dozen seconds later, when I felt a {i}much{/i} larger cock at my asshole."
    else:
        m "I held my empty crotch, wondering why the guy would stop halfway through."
        $ renpy.pause (1.2)
        m "My silent question was answered a half dozen seconds later, as Ipsum's cock plugging my asshole was dragged out."
        m "Then a {i}much{/i} larger cockhead took its place at my rear."
    $ bangok_four_malepartners += 1
    c "W-Wait! N-No! That'll never fit! That--"

    if persistent.bangok_watersports == True:
        m "The large cock pressed, just enough to bow my rosebud a little bit open around its tip. Then the jet of hot, golden liquid began to rush in."
        play soundloop "fx/faucet2.ogg" fadein 2.0
        m "The big dragon pissed like a racehorse, his urine following gravity's will to flow far into my guts before collecting in a warm, deep pool inside me."
        if persistent.bangok_inflation == True:
            $ renpy.pause (0.8)
            m "I moaned, suffused by the warmth and depth and weight of the flood."

        if bangok_four_playerhasdick == True:
            $ renpy.pause (1.2)
            m "After a few seconds, the big dragon pissing in me gave a short, abrupt thrust, straining my sphincter."
            stop soundloop fadeout 3.0
            m "Then his flow began to taper off, leaving my colon a urine-saturated and defiled mess."
            play soundloop "fx/bangok_poundofsalt.ogg" fadein 5.0
            m "No sooner had the big dragon pulled away than the cock that had been fucking me returned, thrusting into my newly-warmed inner walls, then picking up right where he'd left off."

            m "His thrusts were renewed and far less cautious, no longer afraid of getting caught fucking me."
            if persistent.bangok_inflation == True:
                m "They sent shudders through my body, disturbing the pissload deep within me."

            m "I arched my back, pushing my butt a little higher in the tub, into the stranger's assfucking."

            $ renpy.pause (0.8)
            stop soundloop fadeout 0.5
            play sound "fx/extinguish.ogg"
            if persistent.bangok_inflation == True:
                m "A few thrusts more, then the dragon came, rope after rope of sticky white seed sliding down my colon's walls to sink into the deep pool of piss the last dragon had left behind."
                m "The cum added to my liquid weight, leaving a visible bump in my warmed belly that I rubbed and massaged."
            else:
                m "A few thrusts more, then the dragon came, rope after rope of sticky white seed painting my colon's walls."

            m "His load came to an end.{w=0.5} A second passed.{w=0.5}{nw}"
            play soundloop "fx/faucet2.ogg" fadein 1.0
            m "His load came to an end. A second passed.{fast} Then I felt another hot, less-viscous stream jetting into my guts."
            m "His golden liquid washed down my inner walls, cleaning them of his cum for my next visitor."
            if persistent.bangok_inflation == True:
                m "I could feel the bump in my belly expanding, slightly, with yet another stream of fluid collecting in my flooded colon."
        else:
            $ renpy.pause (1.2)
            m "After a few seconds, the cock that had been fucking me returned, sliding easily into my aching, empty pussy."

            m "His thrusts were renewed and far less cautious, no longer afraid of getting caught fucking me."

            if persistent.bangok_inflation == True:
                m "They sent shudders through my body, disturbing the pissload still collecting deep within me."
            stop soundloop fadeout 0.5
            m "Finally, the big dragon finished using me as a living urinal, then stepped away."
            play soundloop "fx/bangok_poundofsalt.ogg" fadein 5.0
            m "Ipsum's ass-plugging cock slid back into me, trapping the golden load deep inside. The fucking of my pussy, however, continued."

            m "I arched my back, pushing my butt a little higher in the tub, into the stranger's fucking."

            $ renpy.pause (0.8)
            stop soundloop fadeout 0.5
            play sound "fx/extinguish.ogg"
            if persistent.bangok_inflation == True:
                m "A few thrusts more, then the dragon came, rope after rope of sticky white seed painting my canal's inner walls, seeping downward to pool against my innermost gate."
                m "The cum added to my liquid weight, leaving a visible bump in my warmed belly that I rubbed and massaged, heady with proximity to my own orgasm."
            else:
                m "A few thrusts more, then the dragon came, rope after rope of sticky white seed painting my canal's inner walls."

            m "His load came to an end.{w=0.5} A second passed.{w=0.5}{nw}"
            play soundloop "fx/faucet2.ogg" fadein 1.0
            m "His load came to an end. A second passed.{fast} Then I felt a hot, less-viscous stream spraying down the inner walls of my passage."
            m "His piss spattered around my spasming canal, washing my walls of his cum for my next visitor, yet defiling them at the same time."
            if persistent.bangok_inflation == True:
                m "I could feel the bump in my belly expanding, slightly, as all his ejected fluids pooled at the entrance to my deepest center."

        stop soundloop fadeout 1.0
        m "Unfortunately, he, too finished."
        $ renpy.pause (0.5)
        m "As he began to pull out, I gasped, squeezing him tightly, trying to reach orgasm of my own."
        m "I failed, forced to pant with pent-up need as Ipsum's cock was shoved back inside, plugging me."

        $ renpy.pause (0.8)
        m "I lay, steeping in the warm results of my newfound use as a draconic urinal."
        if persistent.bangok_inflation == True:
            m "Part of me worried the PH of cum would lower the PH of the piss, preventing it from dissolving the adhesive and freeing me once I finally did overflow."
            $ renpy.pause (1.2)
            m "Another part, basking in the sloshing and flowing at every tremor of my inner muscles, wasn't sure I should care."
        else:
            m "Part of me worried the PH of cum would lower the PH of the piss, preventing it from dissolving the adhesive and freeing me once I finally did overflow."
            $ renpy.pause (1.2)
            if bangok_four_playerhasdick == True:
                m "Another part, squeezing and massaging Ipsum's cock with my ass as if he had more to give, wasn't sure I should care."
            else:
                m "Another part, squeezing and massaging Ipsum's cocks with my holes as if he had more to give, wasn't sure I should care."
    else:
        m "The large head pressed, just enough to bow my rosebud a little bit open around its tip."
        m "After a few seconds, the big dragon trying to enter me gave a short, abrupt thrust, straining my sphincter."
        m "Then, thankfully, he backed off."

        if bangok_four_playerhasdick == True:
            play soundloop "fx/bangok_poundofsalt.ogg" fadein 2.0
            m "After a few seconds, the smaller dragonhood that had been fucking me returned, sliding easily into my now-slightly-more-stretched ass, then picking up right where he'd left off."
            m "His thrusts were renewed and far less cautious, no longer afraid of getting caught fucking me, rubbing at my colon's walls as he stretched my ass."
            if persistent.bangok_inflation == True:
                m "The fucking sent shudders through my body, disturbing Ipsum's heavy cumload and causing it to slide deeper within me."

            m "I arched my back, pushing my butt a little higher in the tub, into the stranger's assfucking."

            $ renpy.pause (0.8)
            stop soundloop fadeout 0.5
            play sound "fx/extinguish.ogg"
            if persistent.bangok_inflation == True:
                m "A few thrusts more, then the dragon came, rope after rope of sticky white seed sliding down my colon's walls to pool in my guts."
                m "I felt an added liquid weight warming my belly, which I rubbed and massaged with a hand."
            else:
                m "A few thrusts more, then the dragon came, rope after rope of sticky white seed painting my colon's walls."

            $ renpy.pause (1.2)
            m "I sighed with relief as he pulled out, clenching my asshole to try to recover some feeling."

            m "Then I felt the large dragonhood lining up again with my sphincter."
            c "W-w-wait--!"
            m "Somehow, it did wait, though I could feel it pressing against my hole in rhythmic motions, weakly humping where it could not fit."
            m "Then scales brushed my hole, and I realized the large dragon was jerking his length off into my ass."
            c "O-Oh. W-Well that's better than--"
            play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/extinguish.ogg"]
            m "The motions came faster, force increasing, then the dragon shoved against my hole, managing to ram three quarters of his tip inside, before jetting out his first sticky ropes."
            m "The big dragon came proportionate to his size, his load dwarfing the other two. Spurt after spurt flowed far into my guts before collecting in a warm, deep pool inside me."
            if persistent.bangok_inflation == True:
                $ renpy.pause (0.8)
                m "I moaned, suffused by the warmth and depth and weight of the flood."
            m "Finally, however, his pulses tapered off. He dribbled just a little bit more cum on my stretched sphincter muscle, before Ipsum's cock plug was replaced and pushed it back inside."
        else:
            m "I breathed a sigh of relief, catching my breath right up until I felt that large shaft's tip flattening my front entrance's folds."
            c "W-w-wait--!"
            m "Somehow, it did wait, though I could feel it pressing against my hole in rhythmic motions, weakly humping where it could not fit."
            m "Then scales brushed my hole, and I realized the large dragon was jerking his length off into my pussy."
            c "O-Oh. W-Well that's better than--"

            play soundloop "fx/bangok_poundofsalt.ogg" fadein 5.0
            m "The smaller shaft, that had been fucking me, returned. It slid easily into my aching, slightly stretched asshole."
            m "His thrusts were renewed and far less cautious, no longer afraid of getting caught fucking me."
            if persistent.bangok_inflation == True:
                m "The thrusts sent shudders through my body, disturbing Ipsum's heavy cumload and causing it to slide deeper within me."

            m "I arched my back, pushing my butt a little higher in the tub, into the stranger's assfucking."

            $ renpy.pause (0.8)
            stop soundloop fadeout 0.5
            play sound "fx/extinguish.ogg"

            if persistent.bangok_inflation == True:
                m "A few thrusts more, then the dragon came, rope after rope of sticky white seed sliding down my colon's walls to pool in my guts."
                m "I felt an added liquid weight warming my belly, which I rubbed and massaged with a hand."
            else:
                m "A few thrusts more, then the dragon came, rope after rope of sticky white seed painting my colon's walls."
            $ renpy.pause (0.5)
            m "As he began to pull out, I gasped, squeezing him tightly, trying to reach orgasm of my own."
            m "I failed, forced to pant with pent-up need as Ipsum's cock was shoved back inside, plugging my rear."

            m "At my front entrance, the larger dragon continued to pressure my labia, rubbing over my vagina as if doing so would solve his lack of lubrication."
            m "I pressed at the disk through the swim briefs, trying at least to get the large dragon's tip to rub my clitoris, but with the disk glued in place it was no use."
            play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/extinguish.ogg"]
            m "The rhythmic motions came faster, force increasing, then the dragon shoved hard against my taut entrance, managing to ram three quarters of his tip inside, before jetting out his first sticky ropes."
            m "The big dragon came proportionate to his size, his load dwarfing the others I'd had so far. Spurt after spurt of hot seed flowed far into my canal, before collecting in a warm, deep pool inside me."
            if persistent.bangok_inflation == True:
                $ renpy.pause (0.8)
                m "I moaned, suffused by the warmth and depth and weight of the flood."
            m "Finally, however, his pulses tapered off. He dribbled just a little bit more cum on my stretched vaginal entrance, before Ipsum's cock plug was replaced and pushed it back inside."


        $ renpy.pause (0.8)
        m "I lay, steeping in the warm results of my newfound use as a draconic cumdump."
        m "Part of me worried that, even with loads of that size, I may not collect enough seed to overflow and free myself."
        $ renpy.pause (1.2)
        if persistent.bangok_inflation == True:
            m "Another part, basking in the sloshing and flowing at every tremor of my inner muscles, wasn't sure I should care."
        else:
            if bangok_four_playerhasdick == True:
                m "Another part, squeezing and massaging Ipsum's cock with my ass as if he had more to give, wasn't sure I should care."
            else:
                m "Another part, squeezing and massaging Ipsum's cocks with my holes as if he had more to give, wasn't sure I should care."


    $ renpy.pause (1.0)
    m "I was startled from my lewd reverie by the cock in my rear dragging partway out, followed by a draft of air over my hole, as if someone had sniffed me."

    if not persistent.bangok_watersports:
        jump todo_out_of_content_bangok_four_xipsum_sharing3

    if bangok_four_playerhasdick == True:
        $ renpy.pause (1.0)
        m "A few seconds passed."
        $ renpy.pause (1.0)
        $ bangok_four_malepartners += 1
        m "Then I finally felt it fully removed, and a new cock at my ass."
        play sound ["fx/bangok_poundofsalt.ogg","fx/bangok_poundofsalt.ogg"] fadein 0.5
        m "It shoved through my weakened muscle fast and hard, jumping straight to fucking me."
        stop sound fadeout 1.0
        m "I didn't have long to enjoy the sensation, though, as after just ten thrusts, it stopped, then pulled out."
        play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/bangok_poundofsalt.ogg","fx/bangok_poundofsalt.ogg"] fadein 0.5
        $ bangok_four_malepartners += 1
        m "Another, different, slightly larger cock pressed to my hole, then followed the pattern of the first, pumping my rosebud with ten thrusts."
        stop sound fadeout 1.0
        m "Then it, too, stopped and pulled out."
        play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/bangok_poundofsalt.ogg","fx/bangok_poundofsalt.ogg"] fadein 0.5
        m "The first, or what I thought was the first, returned. It sank in, bottoming out in me before starting up its hard cadence again."
        stop sound fadeout 1.0
        m "When its ten was up, it pulled out."
        play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/bangok_poundofsalt.ogg","fx/bangok_poundofsalt.ogg"] fadein 0.5
        m "I grunted, panting with need as my ass was traded off again, wondering what game they were playing with me, and what liquid gifts I would earn when one of them lost."
        stop sound fadeout 1.0
        m "The second finished more gently, its last few thrusts slower, bottoming out in me, before pulling out slowly after his turn."
        play sound ["fx/rub2.ogg"] fadein 0.5
        m "The first rammed right in, fucking my ass raw to try to bring himself over his edge within his limit."
        stop sound fadeout 1.0
        m "He failed, pulling out for his partner to take over."
        $ renpy.pause(0.8)
        m "The second seemed to take the exact opposite approach, taking a few moments to even step back up to me, then sinking in slowly."
        $ renpy.pause(0.8)
        m "I felt like he was playing with me and his friend, his pace maddeningly, excruciatingly slow."
        $ renpy.pause(0.8)
        play soundloop "fx/faucet2.ogg" fadein 2.0
        m "Then I felt the jet of hot piss his slow pace was covering up, soaking into my already-saturated walls around his tip as he only narrowly avoided pulling out with each{w=0.5} slow{w=0.5} thrust."
        if persistent.bangok_inflation == True:
            m "The urine added to the pool inside me, backing up along my colon until the tip of his shaft was prodding my inner pool of urine with each thrust."
        stop soundloop fadeout 0.5
        m "Then, cutting himself off, he dragged out of me after his tenth thrust exceedingly slowly, making sure my loosened ring wiped his tip on the way out."
        if persistent.bangok_inflation == True:
            m "His friend's first thrust was right into the piss."
            $ renpy.pause(1.2)
            play soundloop "fx/faucet2.ogg" fadein 2.0
            m "After hesitating for several seconds, he let go too, pressing right up to my hole and pissing into my already packed colon."
            $ renpy.pause(0.8)
            m "I moaned, feeling my innards expand slightly as the slurry of strangers' piss and seed backed up further into my guts."
        else:
            m "The first thrust into my freshly-defiled inner walls and immediately felt the difference."
            $ renpy.pause(1.2)
            play soundloop "fx/faucet2.ogg" fadein 2.0
            m "After hesitating for several seconds, he let go too, pressing right up to my hole and pissing into my thoroughly-defiled colon."
            $ renpy.pause(0.4)
            m "I moaned, feeling yet another stranger's piss warming my saturated innards, dribbling down my inner walls."
        stop soundloop fadeout 0.5
        $ renpy.pause(1.2)
        play soundloop "fx/bangok_poundofsalt.ogg" fadein 1.0
        m "Then he stopped and, after a moment to recover and readjust his position, began to fuck me again."
        jump todo_out_of_content_bangok_four_xipsum_sharing3
    else:
        m "The one in my pussy followed, sliding partway out at someone's tug, before slipping the rest of the way under gravity and the slickness of my arousal alone."
        $ renpy.pause (1.0)
        m "A few seconds passed."
        $ renpy.pause (1.0)
        m "Then the cock in my ass was removed fully, and two new dragons began lining up with my holes."
        $ bangok_four_malepartners += 2
        
        $ renpy.pause (0.5)
        play soundloop "fx/bangok_poundofsalt.ogg" fadein 0.5
        $ renpy.pause (0.5)
        m "Giving me no prep time, once they were lined up, they thrust together."
        m "I moaned, kneading at my crotch as the slightly larger cock in my pussy set a slightly faster pace, pushing me toward that edge I had earlier been denied."
        m "Between the two of them, though, I wondered if they were playing some kind of game with my body, seeing who would be the first to cum in my stained holes."
        m "I wondered if I could tip the odds..."
        menu:
            "Ass.":
                $ renpy.pause (0.5)
                m "I squeezed with my ass, trying to give the cock fucking me there just that little bit extra."
                jump todo_out_of_content_bangok_four_xipsum_sharing3
            "Pussy.":
                jump todo_out_of_content_bangok_four_xipsum_sharing3
            "Cum.":
                $ renpy.pause (0.5)
                m "Throwing rational thought to the wind, I decided I didn't care which of them won. I just wanted to be used and filled."
                m "I spasmed around both cocks, lost in the hedonism of the double penetration."
                
                show white with dissolve
                m "Then I came, squeezing down hard, but unable to stop the merciless fucking with my abused, blissed-out muscles."
                stop soundloop fadeout 1.5
                m "Warmth blossomed in my love canal, sticky ropes pulsing from the twitching cock there. N"


        jump todo_out_of_content_bangok_four_xipsum_sharing3


    jump todo_out_of_content_bangok_four_xipsum_sharing3


label todo_out_of_content_bangok_four_xipsum_sharing3:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")