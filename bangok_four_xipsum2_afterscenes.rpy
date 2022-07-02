init python in bangok_four_xipsum2_sharing3_store:
    cervpen = False

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
        play soundloop "fx/bangok_poundofsalt.ogg"
        m "Another joined it at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."
    else:
        m "Then I felt scaly folds wrapping around my tip, before my shaft was shoved somewhere hard enough it hurt at the base of my length."
        if bangok_four_xipsum2_store.protection == True:
            m "A condom-wrapped cock prodded at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."
        else:
            m "A cock prodded at my ass, and I only barely got my hand through the waistband to poke at the head, blocking its entry."

    play sound "fx/tableslap.wav"
    with vpunch
    m "I fell against the table with the telephone, struggling to pick it back up."
    c "S-Slower, Ipsum!"
    Ip normal bangok blush "Tone it down, a little. They're, ah, breakable."
    if bangok_four_playerhasdick == False and persistent.bangok_cervpen == True:
        Ip think "By the way, I have yet to ask, does your species have a cervix protecting your uterus? And if so, is it penetrable? How large a partner can you manage, and how deep might they go?"
        menu:
            "Y-Yes, we do! {i}Don't{/i}--":
                $ bangok_four_xipsum2_sharing3_store.cervpen = False
            "D-Deep--!":
                $ bangok_four_xipsum2_sharing3_store.cervpen = True

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
                m "A bulbous knot of flesh pressed at my outer folds, spreading my entrance just slightly further as the male injected his cum as deep as he could go."
            if persistent.bangok_inflation == True:
                m "When the cock pulled out, a thick pool of cum rested against my innermost gate. Then another, larger cock took its place."
            else:
                m "The cock pulled out, leaving my passage slightly damper and stickier. Then another, larger cock took its place."
    else:
        m "Juices flowed around my dick, dribbling down around my balls as the cunt on the far side squeezed and massaged me."
        m "I thrust, uselessly, from the simultaneous fucking of my ass and shaft. I couldn't force myself any further into what was already attached to my hips."

    if bangok_four_xipsum2_store.protection == True:
        m "Finally, the one in my ass stopped, pulses of his load travelling up his length to fill his condom's reservoir."
        m "I sighed as it slid out, taking its load with it, only to then feel a new head prodding at my weakened sphincter."
        c "Ah-h!"
        m "This one stretched me wider. As it sank in, I realized it was going deeper, too."
    else:
        m "Finally, the one in my ass stopped, packets of his load travelling up his length to spray out into my rear."
        if persistent.bangok_inflation == True:
            m "Pulse after pulse spurt into me, leaving my ass feeling heavy and full."
        m "I sighed as it slid out, feeling its load settle inside me, only to then feel a new head prodding at my weakened sphincter."
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
        c "W-W-Wait--"
        m "My hands snapped to my crotch but, without my spine to guide my hand, I couldn't get under the waistband in time."
        stop soundloop fadeout 2.5
        m "The tip spread me open, stretching out the folds in my entrance and leaving me taut and full."
        m "Even the fucking of my asshole came to a faltering stop, as if the person engaged in that activity was looking over to watch what this cock would do to me."
        m "I could see the slightest bulge running up my belly, as I was forced open by this large shaft, inch by maddening inch."
        m "Squirming in ecstacy, I pressed the briefs into my crotch, wondering how far this cock could go on."
        if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.cervpen == True:
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
            if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.cervpen == True:
                m "Meanwhile, the length penetrating my deepest center continued to thrust, seemingly oblivious to its own climax nestling in my most sacred place."
                if persistent.bangok_inflation == True:
                    m "The condom expanded with the size of the load, the balloon of cum growing until my womb had no choice but to expand, too, leaving me pregnant with a thick blob of cum, periodically expanding and contracting with the thrusts spearing my body."
            else:
                m "The shaft in my stretched vagina continued to thrust, seemingly oblivious to its own climax nestling at the end of my canal."
        else:
            m "Their cum mixed with the loads that had come before, leaving me saturated with virile seed."
            if persistent.bangok_inflation == True:
                if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.cervpen == True:
                    m "My colon was packed full, my guts thick and heavy with dragon seed. My womb couldn't contain the directly-injected flow, the flood into my deepest recesses forcing to me expand until I appeared pregnant with a thick blob of cum."
                    m "The cock in my ass began to pull out, finished, but the girthy invader penetrating my womb continued to thrust, seemingly oblivious to its own climax bloating my most sacred place, periodically forcing me to expand, then contract with the flow of fluid."
                else:
                    m "My colon was packed full, my guts thick and heavy with dragon seed. With the girthy invader still pumping, the seed hadn't room to pool in my saturated canal. It sprayed through my innermost gate, flooding into my deepest recesses and forcing to me expand until I appeared pregnant with a thick blob of cum."
                    m "The cock in my ass began to pull out, finished, but, seemingly oblivious to its own climax, the girthy invader continued to thrust its cum through my cervix, bloating my most sacred place, periodically forcing me to expand, then contract with the flow of fluid."
        stop soundloop fadeout 0.5
        m "Then, finally, the massive cock in my pussy realized it was finished and dragged slowly from my nethers."
        if bangok_four_xipsum2_store.protection == True:
            if persistent.bangok_cervpen == True and bangok_four_xipsum2_sharing3_store.cervpen == True:
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
