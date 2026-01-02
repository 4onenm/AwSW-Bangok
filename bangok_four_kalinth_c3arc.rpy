init python in bangok_four_kalinth:
    have_number = False # type: bool
    protection = None # type: Optional[bool]
    ws_position = None # type: Optional[Literal["mouth", "inside"]]
    kalinth_ws_position = None # type: Optional[Literal["mouth", "surprise"]]

label bangok_four_kalinth_c3arc_bangnokay:
    show kalinth at left with ease
    menu:
        "Call after her.":
            pass
        "Let her go.":
            jump bangok_four_kalinth_c3arc_return

    c "Hey, Kalinth, wait up."
    Kl normal flip "Yes?"

    menu:
        "Proposition her.":
            pass
        "Nothing, never mind.":
            show kalinth normal with None
            jump bangok_four_kalinth_c3arc_return

    c "You know, I bet this office sees some fun on those couches."
    c "Do you want to find out what a human can do?"
    Kl "I'm not sure I understand."
    menu:
        "Explain.":
            pass
        "Never mind.":
            m "I cleared my throat, trying to put the moment behind us."
            c "It's probably a bad idea anyway. Forget I said anything."
            show kalinth normal with None
            jump bangok_four_kalinth_c3arc_return

    m "I rub my crotch, giving her a wink."
    c "Do you want to share a bit of casual intimacy?"

    Kl bangok surprise flip "Oh!"
    $ renpy.pause (0.5)
    Kl normal flip "No. I'm not interested in that, and I'm not sure why you'd think I would be."
    Kl bangok surprise flip "Is this more common for humans? To ask about that after only just meeting someone?"
    c "... Uh."
    Kl normal "Never mind. I'll just be going now."
    jump bangok_four_kalinth_c3arc_return

label bangok_four_kalinth_c3arc:
    show kalinth at Position(xpos=-0.2, xanchor=0.0) with ease
    if bangok_four_common.bangnokay.check():
        jump bangok_four_kalinth_c3arc_bangnokay

    m "Despite saying she was on her way out, Kalinth lingered in the doorway."
    c "Is there anything else?"
    show kalinth bangok normal blush flip with dissolve
    Kl "There... is something else."
    play sound "fx/door/doorclose.ogg"
    show kalinth bangok furtive blush flip with dissolve
    m "Kalinth closed the office door, then shifted her weight between her feet, looking around Bryce's office at seemingly anything but you for a moment."
    c "What is it?"
    Kl bangok normal blush flip "I've been reading all the reports on your kind thus far, and... there's something I'm interested in trying. Only if you are interested, of course."
    menu:
        "You could say I'm interested.":
            Kl bangok smile blush flip "Oh, good. I was hoping you'd say that."
            show kalinth bangok normal blush flip:
                zoom 1.0
                ease 0.5 zoom 1.1 xpos 0.5 xanchor 0.5
                zoom 1.1 xpos 0.5 xanchor 0.5
            with None
            m "Kalinth trod a little closer."
            Kl "But just to be clear, I'm implying casual intimacy. That's not too far for you, is it?"
        "I think I'd have to know what it is first.":
            c "What do you want to try?"
            show kalinth bangok normal blush flip:
                zoom 1.0
                ease 0.5 zoom 1.1 xpos 0.5 xanchor 0.5
                zoom 1.1 xpos 0.5 xanchor 0.5
            with None
            m "Kalinth trod a little closer."
            Kl bangok furtive blush flip "Absolutely feel free to say no if it's too far, but I thought... perhaps you and I could share a bit of casual intimacy."
        "If it's what I think it is, no thanks.":
            label bangok_four_kalinth_c3arc_abrupt_departure:
            Kl normal "Oh. I see. Well, I'm sorry to have bothered you. I'll just be going now."
            hide kalinth with easeoutleft
            $ renpy.pause (0.3)
            play sound "fx/door/doorclose.ogg"
            $ renpy.pause (0.5)
            m "Kalinth hurried out of the office, leaving me alone with the files."
            jump c3arcques

    show kalinth bangok normal blush flip with dissolve
    m "Kalinth glanced down at my crotch, making her intentions clear. Her tail twitched as she waited for my answer, the end swishing back and forth across the floor."

    menu:
        "Accept.":
            pass
        "Reject.":
            m "I took a step back."
            c "Oh, wow, I really misread that. No, I'm not interested."
            jump bangok_four_kalinth_c3arc_abrupt_departure

    c "That sounds like fun."
    show kalinth bangok smile blush flip with dissolve
    c "Right here in Bryce's office, though?"
    Kl bangok smilewink blush flip "I don't think we'll be disturbed here for a while."
    Kl bangok normal blush flip "This office has also seen plenty of use by various members of the department, so it's not like this is anything new. But I can also give you my number for another day, if you prefer."

    menu:
        "Let's go for it.":
            pass
        "I'd rather have your number.":
            Kl normal flip "Alright."
            play sound "fx/scribblex.ogg"
            m "Kalinth wrote down her number on a scrap of paper, then handed it to me."
            show kalinth bangok normal blush with dissolve
            Kl "I'll leave you to your work, then."
            jump bangok_four_kalinth_c3arc_return

    Kl bangok surprise blush flip "I assume you'll have to remove your..."
    m "She gestured to my clothes."

    play sound "fx/undress.ogg"
    m "I began undressing, not wanting to keep the dragoness waiting."
    if bangok_four_playerhasdick is None:
        m "As I removed my shirt, I could feel in my pants my..."
        menu:
            "As I removed my shirt, I could feel in my pants my...{fast}"
            "... length hardening":
                $ bangok_four_playerhasdick = True
            "... lower lips slicken":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick:
        jump bangok_four_kalinth_c3arc_male
    else:
        jump bangok_four_kalinth_c3arc_female

label bangok_four_kalinth_c3arc_female:
    m "As I removed my shirt, I could feel in my pants my lower lips slicken in anticipation of what was to come."
    m "Kalinth moved closer, tail wagging slightly as she watched me remove my bra to reveal my breasts."
    Kl bangok surprise blush flip "So that's what you've been hiding."
    c "Oh, right, you're a reptile. You wouldn't have much familiarity with these."
    m "I took hold of my chest, squeezing my breasts together for her to see."
    c "We call these breasts, or mammaries if you prefer the technical term."
    c "They produce milk for feeding babies, but they're also very sensitive."
    Kl bangok smile blush flip "Can I touch you? You as a whole look so soft without scales or any fur besides what's atop your head."
    c "Yeah, let's get used to each other before we go any further."
    m "After a few moments of looking at each other and trying to decide how we'd fit together, we moved in for a hug."
    show kalinth bangok smile blush flip:
        zoom 1.0
        ypos 1.0
        ease 1.0 zoom 2.0 ypos 1.5
        zoom 2.0 ypos 1.5
    with None
    $ renpy.pause (0.3)
    show black with dissolve
    m "My arms wrapped over her shoulders and wing joints, while her forelegs pulled the small of my back against her chest."
    m "I could feel the heat of her body through her scales and the leathery texture of her wings as they gently folded around me."
    c "Your scales are firmer than I thought they'd be, but they're not unpleasant. So smooth."
    m "Kalinth hummed."
    Kl bangok eyesclosed blush flip "And you're so warm and soft, letting so much of your body heat out."
    Kl bangok smile eyesclosed blush flip "This explains a little Sebastian's old stories about using Mouflons as pillows, especially with those headrests on your chest."
    m "Kalinth ran a forepaw up my back, up to my head to ruffle my hair."
    Kl bangok smile flip "What is this called?"
    c "Hair."
    m "I nuzzled closer into her chest as she began to stroke my hair, straightening out the mussing she'd done a moment ago."
    c "It's a little like fur, but it's not as thick or as soft."
    c "Stroking it is considered affectionate in most human cultures, and you're doing a really good job of it."
    m "She continued to stroke my hair, our chests moving together as we breathed."
    m "Wanting to return some of the affection, I unclasped my hands behind her neck, gently rubbing her scales down over her neck and belly."
    m "Kalinth hummed again. I could feel the vibrations through her chest."
    Kl bangok smile eyesclosed blush flip "Don't stop that. It feels so nice..."
    m "We stayed like that for a while, just enjoying each other's touch and warmth."
    m "Then I began to work my hands down her body, exploring every bump in her scales, brushing my own breasts against her chest as I did."
    Kl bangok blush flip "Let's see what you're hiding down below too..."
    m "I felt her other strong forepaw slide down my back, then into the waistband of my pants, making me shiver."
    m "She couldn't manage to get them down."
    Kl normal flip "How do you get this... thing off?"
    c "Oh, let me take care of that."
    hide black with dissolve
    m "I pulled back my arms and stepped back, getting enough room to reach down and undo the fastener of my pants."
    m "I then left it to her to pull them down, revealing my panties."
    Kl bangok surprise flip "Another thing? How many layers of clothes do you wear?"
    m "Deftly, she slid one claw into the joint where my pelvis met my thigh, then pulled my panties down as well, finally revealing my glistening sex to her explorations."

    if persistent.bangok_cloacas:
        Kl bangok surprise blush flip "Oh... you're different down below too."
        Kl bangok normal blush flip "Well, I suppose that's to be expected."
        show kalinth bangok normal blush flip:
            zoom 2.0
            ypos 1.5
            ease 1.0 zoom 1.0 ypos 1.0
            zoom 1.0 ypos 1.0
        with None
        m "In the interest of fairness, Kalinth moved back and reached between her own legs, spreading her horizontal lower lips to show me her cloaca while I stepped out of my pants and panties."
        c "You look different too. You have just one hole down there? That's interesting."
        Kl "What's so special about it?"
        c "I'm a biologist first, so I'm curious about the differences between our species."
        c "But I'm also just curious... do males of your species ever accidentally stick it in the wrong part?"
        Kl bangok furtive blush flip "..."
        c "The part just peeking out, as well."
        m "I spread my own lower lips, highlighting my delicate nub."
        c "We call this the clitoris. It's usually the most stimulating part for human women."
        c "But what feels nice for you?"
        Kl bangok normal blush flip "I think you're making this more complicated than it needs to be."
        c "Well, you're so much bigger than I am. I want to make sure I'm focusing on the right areas."
        c "I've heard of human guys with smaller genitalia than just the nub above your urethra."
    else:
        Kl bangok surprise blush flip "Oh... we're not so different after all."
        c "In what sense? We could hardly be farther apart in terms of skin and skeletal morphology."
        Kl bangok smile blush flip "I meant that you have a pussy just like me... and you're just as wet as I am."
        show kalinth bangok normal blush flip:
            zoom 2.0
            ypos 1.5
            ease 1.0 zoom 1.0 ypos 1.0
            zoom 1.0 ypos 1.0
        with None
        m "In the interest of fairness, Kalinth moved back and reached between her own legs, spreading a vertical slit between her legs to show me her vagina while I stepped out of my pants and panties."
        m "Within the outer slit formed by her scales, plump flesh formed into a vagina resembling a big plum with a little blueberry for her clitoris."
        c "(Well, maybe \"little\" is the wrong word to describe that.)"
        c "You're so much bigger than I am."
        c "I've heard of human guys with smaller genitalia than just your clit."
    Kl bangok furtive blush flip "Are human males really that small? My condolences..."
    c "Not necessarily. Humans can generally get up to ten inches in length, though the average is usually just over half that."
    c "For other primates, like gorillas, it's far, far less."
    c "Most human women aren't fond of extra large sizes anyway. Reaching our cervix can be very painful."
    if persistent.bangok_cervpen:
        c "Though I can be different. Sometimes I do like it... very big."
        Kl bangok normal blush flip "Oh my."
    if bangok_four_malepartners > 1 or not getattr(renpy.store,"chap2storehealth",True):
        c "From other dragons, I've seen human guys clearly got the short end of the stick."
        Kl bangok surprise blush flip "So you're bisexual {i}and{/i} have already had sex with another dragon?"
        Kl "Haven't you only been here... a week? A week and a half?"
    if not getattr(renpy.store,"chap2storehealth",True):
        c "I mean, er, I saw the condoms on sale at the store. Ones that could fit over my arm."
        Kl bangok smile blush flip "Ah, that makes more sense."
    else:
        Kl "Are humans really that frisky?"
        c "I think it's more that we're curious. We like to explore and experiment."
        Kl bangok smile blush flip "Well, I suppose I can't fault you for that. I'm curious too. I want to see what you can do."

    $ renpy.pause (0.5)

    m "As the conversation trailed off, Kalinth gave a meaningful look toward the couch, flicking her tail back and forth."

    menu:
        "Should we use protection?":
            $ renpy.pause (0.5)
            Kl normal flip "We're whole different species... and the same sex. How would we get hatchlings?"
            c "That's a fair point, but what about diseases? There's no telling with the difference in our biologies."
            Kl normal flip "I suppose you're right. I know where Bryce keeps condoms, but we're facing a distinct lack of dental dams."
            c "We can unravel a condom and use one of those as a makeshift dental dam."
            c "(That makeshift protection won't be fantastic. Am I just overcomplicating things?)"
            menu:
                c "(That makeshift protection won't be fantastic. Am I just overcomplicating things?){fast}"
                "Use protection.":
                    c "I'd like to use one."
                    Kl normal flip "Alright."
                    hide kalinth with dissolve
                    play sound "fx/rummage.wav"
                    m "Kalinth rummaged through Bryce's desk, then set a box of condoms on top."
                    m "She took one out between her lips, then slunk back over to me with a sultry look in her eyes."
                    show kalinth bangok smile blush flip with dissolve
                    c "Thanks."
                    m "I took the condom from her lips, then tore it open and unrolled it dangling from my fingers."
                    m "Holding it taut, I let her delicately puncture it with a claw, cutting open one side as much as she could so we could lay it flat."
                    c "I think that's good enough."
                    $ bangok_four_kalinth.protection = True
                "Go without.":
                    c "Nevermind. If you're not worried about it, I'm not either."
        "Okay, let's get started.":
            pass

    m "We moved over to the couch, but neither of us sat down as we caught each others' gazes."
    Kl "I'm not quite sure... would you prefer to take the lead, or should I?"
    menu:
        "Let her make the next move.":
            jump todo_out_of_content_bangok_four_kalinth
        "Ask her to turn around.":
            m "Placing a hand on her smooth belly, I gave her a gentle rub."
            c "Can you lay down on the sofa for me?"
            jump bangok_four_kalinth_c3arc_female_mctop

label bangok_four_kalinth_c3arc_female_mctop:
    play sound "fx/undress.ogg"
    show kalinth bangok smile blush with dissolve
    if persistent.bangok_cloacas:
        m "Kalinth quickly agreed. She lay back on the couch, her tail swishing and wings fluttering as she settled into a comfortable position and spread her legs to reveal her glistening draconic cloaca."
    else:
        m "Kalinth quickly agreed. She lay back on the couch, her tail swishing and wings fluttering as she settled into a comfortable position and spread her legs to reveal her glistening wet lower lips, and her tailhole a short distance behind."
    m "I couldn't help but stare at that gorgeous sight for a moment while the dragoness watched my every move with anticipation."

    m "As I approached her from her rear, I couldn't help but gaze at her puffy, exposed lower lips."
    m "Wanting to make sure she was fully ready, I chose to start with my fingers."
    m "Sliding them inside her, I felt the heat of her insides and the slickness of her arousal coating my digits as they parted her labia."
    m "Kalinth gasped, breath shuddering as I touched her."
    Kl bangok eyeslidded blush "Please, don't tease for too long. I want to feel more of you."

    m "I knelt down on the couch, straddling her tail to get a better view from right above her gorgeous underside."
    m "Then I leaned down, hugging her tail against me, curling my legs around it until I felt it slithering and struggling against my belly."
    Kl bangok surprise "What are you doing?"
    m "Her tail moved a little more against me, and Kalinth seemed to relax into my taking control."
    Kl bangok smile eyeslidded blush "Oh, don't stop... You feel so soft there."
    m "With my position on the couch now firmly in place, I spread her thighs a little to take hold of her labia, gently squeezing those lower lips together like a burger."
    if bangok_four_kalinth.protection:
        m "I spread the makeshift dental dam over that juicy patty, wrapping it for the customer's convenience."
        m "Then I lowered my face to said burger, inhaling the sweet scent of her arousal."
        m "The burger analogy broke down as I took a bite with the wrapper still on."
        m "I nuzzled lightly with the tip of my tongue the gap between buns as she shuddered beneath my hands and mouth."
    else:
        m "Then I lowered my face to said burger,then I found just how wet she was for me already as I inhaled the sweet scent of her arousal."
        m "It was intoxicating and only heightened the taste of her as I took a bite of her burger."
        m "I nuzzled lightly with the tip of my tongue at the gap between the buns, lapping up her juices liberally as she shuddered beneath my hands and mouth."
    m "Kalinth moaned, her tail twitching with excitement as I continued to nibble at her outer entrance."
    $ renpy.pause (0.5)
    Kl bangok normal blush "I almost don't want to make you stop... but we can't spend all night here. Other responsibilities..."
    $ renpy.pause (0.5)
    m "She shifted as I continued for a little longer before pulling back."
    m "Hearing her reluctant voice, I decided to move past the teasing and get to the main course."
    if bangok_four_kalinth.protection:
        m "I parted her soft buns beneath the dental dam, exposing through the slightly transparent material the damp blue depths, with her clitoris poking back at me."
    else:
        m "I parted her soft buns, revealing her damp blue depths within, with her clitoris looking back at me."
    c "Don't worry, I'll make sure to satisfy you quickly."

    m "Kalinth chuckled."
    Kl bangok normal blush "You sound quite conf--"
    m "I lowered myself further down now to nuzzle my whole face into her warm folds."
    if bangok_four_kalinth.protection:
        m "I pressed my tongue out against the dental dam, lapping at the entrance of her tight canal as best I could and quickly smearing my own face with my saliva as she softly squeezed down on me."
    else:
        m "I lapped at the entrance to her tight canal as she softly squeezed down on me."
    Kl bangok eyesclosed blush "...{fast}fident..."
    m "Kalinth shuddered, her tail twitching against my belly as I heard her give a soft, encouraging moan."
    if bangok_four_kalinth.protection:
        m "I continued my work upward, leaving her depths both to get a breath and to begin to stimulate the area around her urethra and clitoris."
    else:
        m "I continued my work upward, circling her urethra with my tongue, leaving her depths both to get a breath and to begin to stimulate her clitoris just a little."
        m "I dipped back down for a moment, though, as I felt her release a little gush more of her sweet, sweet nectar in my mouth."

        if persistent.bangok_watersports:
            show kalinth bangok normal blush with dissolve
            m "I got a glimpse up at Kalinth's face as she shifted uncomfortably. Noticing I had noticed, she explained."
            Kl normal "I'm sorry for bringing this up now... but I was so in the mood that I forgot I needed to go to the bathroom."
            Kl bangok furtive blush "You're making me really excited... Do you want to stop? Because, you know..."
            m "I raised my head, my face dripping with her slick draconic juices, and thought about what she was saying."
            menu:
                "Can you hold it in?":
                    Kl "I... think I can. I will try to hold it in. Just don't go {i}too fast{/i} on me. You could say I'm ready and armed."
                    c "(That's not exactly reassuring...)"
                    menu:
                        c "(That's not exactly reassuring...){fast}"
                        "[[Giggle.]":
                            m "I couldn't help myself. The thought of being suddenly interrupted later seemed so funny."
                            m "Kalinth joined in."
                            Kl bangok smile blush "Well, I suppose that means it wouldn't be the worst thing if I fail?"
                            c "No, but please give it a try."
                            $ bangok_four_kalinth.kalinth_ws_position = "surprise"
                        "Okay, let's keep going.":
                            $ bangok_four_kalinth.kalinth_ws_position = "surprise"
                        "Can you hold it in, please?":
                            show kalinth normal with dissolve
                            m "Kalinth huffs."
                            Kl "Alright. I'll put a little more effort into it."
                            c "Thanks."
                "Don't worry about it. If you need to, go.":
                    Kl smile blush "Oh, thank you. I thought you would be understanding. But please do continue you felt great down there."
                    $ bangok_four_kalinth.kalinth_ws_position = "surprise"
                "I think I'd enjoy that.":
                    $ bangok_four_kalinth.kalinth_ws_position = "mouth"
                    Kl smile blush "Oh good. I had thought you might be into it, given you're kinky enough to have sex across species..."
                    show black:
                        alpha 0.5
                    with dissolve
                    m "I spread her puffy lips apart again, then plunged my face back down into her depths, searching for her urethra with my tongue."
                    m "When I found it I pushed my face forward, giving it a kiss as my nose rubbed against her clit."
                    Kl eyeslidded blush "You really want this, don't you? I'll help you out a little bit."
                    show black:
                        alpha 1.0
                    with dissolve
                    m "I felt her strong arms on my head, pushing me further into her crotch. I sucked down a full breath through my nose before I was immersed in her nethers, then suckled on her piss-hole."
                    Kl eyesclosed blush "Ohh..."
                    m "I closed my eyes and let the warm trickle enter my mouth. It wasn't nearly as bitter nor sour as I had feared."
                    play soundloop "fx/faucet1.ogg"
                    queue soundloop "fx/faucet2.ogg"
                    m "Then the trickle turned into a stream..."
                    m "Then the trickle turned into a stream...{fast} then into a whole river, filling my mouth completely as I struggled to swallow it all."
                    Kl bangok smile eyeslidded blush "Feeling good down there?"
                    m "I gagged, but covered it over with a thumbs-up."
                    c "(Why did I do this? It's like a pre-flare beer drinking competition...)"
                    c "(I always wondered how those guys managed to swallow gallons.)"
                    m "Lacking any other choice as the pressure in my mouth increased, I stopped swallowing in individual gulps, my throat instead opening up to let the stream flow down into my stomach."
                    if persistent.bangok_inflation:
                        $ renpy.pause (3.0)
                        m "Her urine was filling my stomach to an alarming degree, but I couldn't stop it."
                        $ renpy.pause (3.0)
                        m "I could feel my stomach beginning to stretch, my body struggling to contain the liquid as it continued to flow down my throat."
                        c "(How much more is there?!)"
                    Kl bangok eyesclosed blush "Hold on... I'm nearly finished..."
                    stop soundloop fadeout 5.0
                    m "Finally, I felt her river turning back into a trickle. I swallowed the last of hurriedly, trying to clear my mouth to take a breath as soon as I could."
                    if persistent.bangok_inflation:
                        c "(Ugh, is my belly sloshing? I don't know if I can keep this down...)"
                    m "After I gave her urethra one last lick to suck up the last of her urine, her hands finally released me."
                    hide black with dissolve
                    m "I popped up, gasping for air."
                    m "It took me a few moments to recover and be certain none of it came back up. To my surprise, I noticed that between the two of us, I hadn't spilled a drop."
                    c "(I guess a spill like that would have been awkward to explain...)"
                    Kl bangok smile blush "Thank you. I really needed that."
                    menu:
                        "My pleasure.":
                            Kl "All that? Well, I'm glad you enjoyed it."
                        "How much did you drink? Was that intentional?!":
                            Kl "Nothing out of the ordinary, no. I was just emptying my bladder."
                            if persistent.bangok_inflation:
                                m "I held my slightly distended belly, feeling the liquid sloshing around from my sitting up. Then my insides gurgled as it began seeping deeper into my guts."
                                c "(That bladder must have been huge...)"
                        "For that, now it's my turn.":
                            jump todo_out_of_content_bangok_four_kalinth
                        "[[Say nothing.]":
                            Kl bangok normal blush "I'm sorry. I didn't mean to make you uncomfortable."
                            if persistent.bangok_inflation:
                                m "I held my slightly distended belly, feeling the liquid sloshing around from my sitting up. Then my insides gurgled as it began seeping deeper into my guts."
                            Kl "I was just... emptying my bladder. I didn't realize quite how much that would be for you."
                            Kl "Although, you handled it very well for your size."
                            if persistent.bangok_inflation:
                                c "(I don't feel like I did... Urgh...)"
                    m "I took a deep breath, then let it out slowly, settling the volume of liquid inside me."
                    m "Then I looked down at Kalinth's nethers, still glistening with her arousal and ready for me to explore."
                    c "Let's keep going."
            m "I dipped back down, nestling my face back into her folds, then working my way up her inner surfaces again."
        # Watersports interlude 1 end

    m "Then I reached the top and popped her blueberry into my mouth."
    m "Knowing its sensitivity for humans, I was extra careful here, giving it only the gentlest swirl with my tongue."
    m "Kalinth moaned in response, her wings fluttered, and she wrapped me around with her hindlegs and grabbed my head with her forepaws."
    Kl bangok eyesclosed blush "Whatever you're doing, don't stop..."
    m "I felt her forepaws ruffle my hair as I continued my actions."
    if bangok_four_kalinth.protection:
        jump todo_out_of_content_bangok_four_kalinth
    else:
        m "Her warmth and the subtle pebbling of her labia scales felt incredible on my face, her slickness only emphasizing the contrast of her scales and inner flesh."
        Kl bangok smile eyeslidded blush flip "You're making me really wet... Ohh don't forget to breathe..."

    jump todo_out_of_content_bangok_four_kalinth






label bangok_four_kalinth_c3arc_male:
    show kalinth bangok smile blush flip with dissolve
    m "As I removed my shirt, I could feel in my pants my length hardening."
    m "Once I was nude, my erect member exposed to the air of the room, she backed me up toward the armrest of the nearer of the two couches, smirking."

    label bangok_four_kalinth_c3arc_male_position_menu:
    menu:
        "Ask about protection." if bangok_four_kalinth.protection is None and bangok_four_kalinth.ws_position is None:
            c "Do you have any protection?"
            Kl bangok surprise blush flip "We're different species, so pregnancy isn't a concern."
            Kl bangok normal blush flip "But I do think I remember where Bryce keeps some condoms, if you'd like to use one."
            menu:
                "Use a condom.":
                    $ bangok_four_kalinth.protection = True
                    c "I'd like to use one."
                    Kl normal flip "Alright."
                    hide kalinth with dissolve
                    play sound "fx/rummage.wav"
                    m "Kalinth rummaged through Bryce's desk, then set a box of condoms on top."
                    m "She took one out between her lips, then slunk back over to me with a sultry look in her eyes."
                    show kalinth bangok smile blush flip with dissolve
                    c "Thanks."
                    m "I took the condom from her lips, then tore it open and rolled it onto my shaft."
                "Go without.":
                    $ bangok_four_kalinth.protection = False
            jump bangok_four_kalinth_c3arc_male_position_menu
        "Ask about a restroom." if persistent.bangok_watersports and (not bangok_four_kalinth.protection) and (not bangok_four_kalinth.ws_position):
            m "Standing erect and nude next to her, I suddenly realized my bladder was rather full."
            c "Er... I should probably use the restroom first."
            Kl bangok surprise blush flip "Oh, wow. Your timing is worse than... well, never mind."
            m "The look on her face was one of disappointment."
            Kl bangok normal blush flip "I suppose I can wait a little longer."
            Kl bangok smilewink blush flip "Unless you'd like to use me as a urinal?"
            menu:
                "Sure.":
                    pass
                "No thanks.":
                    c "I'm not sure what that entails, but I think I'll pass."
                    show kalinth normal flip with dissolve
                    m "She pouted."
                    Kl "Well, hurry back."
                    show black with dissolve
                    m "I threw my pants and shirt on haphazardly, struggling to fit my erection beneath my waistband, then hurried to the restrooms."
                    m "A few minutes later I returned to the office."
                    hide black
                    show kalinth bangok furtive blush flip
                    with dissolve
                    Kl "Done ruining the mood?"
                    c "Sorry."
                    jump bangok_four_kalinth_c3arc_male_position_menu

            c "I didn't think you'd be into something like that. Sure."
            Kl bangok smile blush flip "Mm. Well, we don't want to make a mess on Bryce's floor. I could drink it down right now..."
            Kl "Or if you're into it you could piss it into me while you're inside, leave me even more dripping wet between the legs..."
            menu:
                "Mouth, now.":
                    $ bangok_four_kalinth.ws_position = "mouth"
                    show kalinth:
                        pause 0.5
                        yanchor 1.0
                        ease 0.5 yanchor 0.2
                        yanchor 0.2
                    with None
                    m "I rested my hand on one side of her snout, then guided it down to my erection."
                    m "She eagerly wrapped her scaly lips around me, but didn't slurp or suck as she waited for me to urinate into her mouth."
                    m "It was a strange and exciting sensation... I could feel the heat from her breath against my shaft, and the wetness of her tongue as she waited for me to let go."
                    show black with dissolve
                    m "I closed my eyes, trying to relax, and let my bladder empty into her mouth, feeling the familiar rush of relief as my member began to disgorge a steady stream of piss against the back of Kalinth's throat."
                    m "She swallowed it down eagerly, not once pulling away from me until I had finished."
                    hide black
                    show kalinth bangok smile eyesclosed blush flip
                    with dissolve
                    m "The sight of her swallowing every last drop left me with an erection that was even harder than before, and she seemed to be enjoying it as well from the way she licked her lips."
                    Kl bangok smile blush flip "Mmm... you taste interesting."
                    m "She gave my member a slow lick, from balls to tip, then stepped back with an amused smirk."
                    show kalinth:
                        yanchor 0.2
                        ease 0.5 yanchor 1.0
                        yanchor 1.0
                    with None
                    Kl "I've never tasted a human's piss before. Now I'm curious what your cum tastes like."
                    c "I'm sure you'll find out soon enough."
                "Inside.":
                    $ bangok_four_kalinth.ws_position = "inside"
                    c "Inside."
                    m "I felt my erection twitch in anticipation."
                    Kl bangok smile blush flip "Then let's get started."
            jump bangok_four_kalinth_c3arc_male_position_menu
        "Let her take charge.":
            jump bangok_four_kalinth_c3arc_male_mcbottom
        "Take charge yourself.":
            c "Actually, could you lie down? I'd like to be in control for this."
            jump bangok_four_kalinth_c3arc_male_mctop
        "Ask her to turn around.":
            jump bangok_four_kalinth_c3arc_male_doggy

label bangok_four_kalinth_c3arc_male_mcbottom:
    m "I sat back on the couch armrest, letting the assertive dragon archivist take charge."
    show kalinth bangok smile blush flip:
        zoom 1.0
        ease 0.5 zoom 1.5
        zoom 1.5
    with None
    if persistent.bangok_cloacas:
        m "She reared up, resting her forelegs over my shoulders as her spread rear legs revealed her glistening cloaca, searching with her hips for my shaft."
    else:
        m "She reared up, resting her forelegs over my shoulders as her spread rear legs revealed her glistening lower lips, searching with her hips for my shaft."
    show kalinth bangok smile blush flip:
        zoom 1.5
        ease 0.5 zoom 1.6
        zoom 1.6
        block:
            ease 1.2 ypos 1.01
            ease 1.2 ypos 1.0
            repeat
    with None
    if persistent.bangok_cloacas:
        m "Then, pressing my back against the couch's back, she began to tease her cloaca open with my tip, grinding against my erection without letting it in."
    else:
        m "Then, pressing my back against the couch's back, she began to tease her labia open with my tip, grinding against my erection without letting it in."

    m "I groaned as the dragoness rubbed herself against me."
    m "Her tail swished behind her, making a faint rustling sound with each movement."
    $ renpy.pause (0.5)
    c "Are you going to make me wait like this? I don't know how long I can take it."

    m "Kalinth chuckled with my face against her fine underbelly scales before she pushed off a little to look me in the eye."
    show kalinth bangok smile blush flip:
        zoom 1.6
        ease 0.5 zoom 1.5
        zoom 1.5
        block:
            ease 1.2 ypos 1.01
            ease 1.2 ypos 1.0
            repeat
    with None

    Kl "I'll let you inside eventually. But first I just want to feel you all over me down there before..."
    show kalinth bangok smile eyesclosed blush flip:
        ease 0.8 ypos 1.01
        ease 1.2 ypos 1.2
    with None
    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "Her breathing caught and she closed her eyes as her cloaca slid up to my tip again, then she began to lower herself down, enveloping my condom-wrapped erection with the warmth of her draconic anatomy."
        else:
            m "Her breathing caught and she closed her eyes as her labia slid up to my tip again, then she began to lower herself down, enveloping my condom-wrapped erection with the warmth of her draconic pussy."
    else:
        if persistent.bangok_cloacas:
            m "Her breathing caught and she closed her eyes as her cloaca slid up to my tip again, then she began to lower herself down, enveloping my erection with the warmth of her draconic anatomy."
        else:
            m "Her breathing caught and she closed her eyes as her labia slid up to my tip again, then she began to lower herself down, enveloping my erection with the warmth of her draconic pussy."
    c "Oh fuck."
    m "As she took every inch of me, I moaned."
    m "Her tail twitched with excitement, rubbing back and forth across the surface of the table."
    show kalinth bangok eyesclosed blush flip with dissolve
    if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        Kl "Mm. Now. Let your bladder go. Fill me up."
        m "My erection throbbed within her warm, all-encompassing depths as I struggled to relax enough to begin peeing myself inside the dragoness."
        m "I could feel the warmth of her insides around my cock, and it made it difficult to resist letting out a groan as she urged me on with gentle circling of her hips."
        m "Finally, I began to let go."
        m "The stream trickled at first, then began to jet out hard, spraying into her cloaca."
        m "Kalinth moaned in pleasure, squeezing me to try to keep it all inside her."
        Kl "Deep and warm..."
        m "I didn't stop until my bladder was empty."
    else:
        m "She paused for a moment on my lap, seemingly struggling to take things slow."
    $ renpy.pause (0.5)
    show kalinth bangok eyesclosed blush flip:
        ease 1.2 ypos 1.18
        ease 1.2 ypos 1.2
        repeat
    with None
    if bangok_four_kalinth.protection:
        m "Then she began to gently thrust herself against me, her scaly lower lips rubbing over the thin barrier between us in the most delightful way imaginable."
    else:
        m "Then she began to gently thrust herself against me, her scaly lower lips rubbing over my member in the most delightful way imaginable."

    if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        if persistent.bangok_cloacas:
            m "I grabbed onto the couch back tight as I felt Kalinth's piss-stained cloaca enveloping me, gripping me tighter with every stroke."
        else:
            m "I grabbed onto the couch back tight as I felt Kalinth's piss-stained passage enveloping me, gripping me tighter with every stroke."
    else:
        if persistent.bangok_cloacas:
            m "I grabbed onto the couch back tight as I felt Kalinth's cloaca enveloping me, gripping me tighter with every stroke."
        else:
            m "I grabbed onto the couch back tight as I felt Kalinth's passage enveloping me, gripping me tighter with every stroke."
    m "The heat radiating from her smooth scales was intoxicating."
    m "My hips twitched, desperate for more, but she seemed to enjoy this weighty but gentle slow thrusting so much that it was hard to bring myself to complain about it."

    show kalinth bangok smile eyesclosed blush flip:
        ease 1.2 ypos 1.18
        ease 1.2 ypos 1.2
        ease 1.0 ypos 1.17
        ease 1.0 ypos 1.2
        ease 0.8 ypos 1.17
        ease 0.8 ypos 1.2
        block:
            ease 0.8 ypos 1.17
            linear 0.5 ypos 1.2
            repeat
    with None

    m "It wasn't until she moaned loudly and began thrusting even faster that I finally knew the moment had come when she was ready for something more forceful."

    m "I groaned as Kalinth finally started fucking me in earnest, her tail whipping back and forth like a flag in the wind of our passion."

    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "Her cloaca leaked copious lubrication around the condom, making my shaft slide in and out with ease as our mating point gave wetter and louder slaps against my groin."
        else:
            m "Her vagina leaked copious lubrication around the condom, making my shaft slide in and out with ease as our mating point gave wetter and louder slaps against my groin."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "I couldn't tell the difference between my urine and her copious lubrication leaking from our mating point. My shaft slid in and out with ease as our groins made wetter and louder slaps against each other."
        m "The smells of urine and sex filled the air."
    else:
        if persistent.bangok_cloacas:
            m "Her cloaca leaked copious lubrication around my shaft, making it slide in and out with ease as our mating point gave wetter and louder slaps against my groin."
        else:
            m "Her vagina leaked copious lubrication around my shaft, making it slide in and out with ease as our mating point gave wetter and louder slaps against my groin."

    m "I tried to lift my hips a little, thrusting deeper into her, but I could do no better than her weight already pressing down on me."

    show kalinth bangok smile eyesclosed blush flip:
        parallel:
            ease 0.7 ypos 1.17
            linear 0.4 ypos 1.2
            repeat
        parallel:
            zoom 1.5
            ease 1.0 zoom 1.6
            zoom 1.6
    with None
    m "Still, the motion caused her to hug me to her chest again, bringing us closer together in the throes of our passion."

    Kl bangok smile eyeslidded blush flip "Don't cum just yet..."
    m "She rode me harder and faster, each stroke seeming more desperate than the one before."
    $ renpy.pause (0.5)
    Kl "I want..."
    Kl bangok eyesclosed blush flip "I need..."
    show kalinth bangok smile eyesclosed blush flip:
        linear 0.4 ypos 1.2 zoom 1.6
        ypos 1.2 zoom 1.6
    with None
    m "She moaned, then buried herself on my erection to the hilt, her tail swishing wildly behind her as her passage spasmed and clenched around my shaft."
    Kl "Now!"

    if bangok_four_kalinth.protection:
        m "I complied with a moan of my own, feeling my orgasm surge forth into the condom reservoir buried as deep in her kneading nethers."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "I complied with a moan of my own, feeling my orgasm surge forth into her urine-slickened, kneading nethers."
    else:
        m "I complied with a moan of my own, feeling my orgasm surge forth into her kneading nethers."
    m "My member throbbed within her heat and wetness as she lay her body atop mine, resting her weight on my hips to force me as deep within her as I could be."
    show kalinth bangok smile eyesclosed blush flip:
        parallel:
            ease 1.2 ypos 1.19
            ease 1.2 ypos 1.20
            repeat
        parallel:
            pause 0.6
            block:
                ease 1.2 xpos 0.51
                ease 1.2 xpos 0.5
                repeat
    $ renpy.pause(0.8)
    m "Then the dragoness began grinding herself against me in slow circles, savoring the feeling of the tail-end of my release still spurting slowly into her."
    $ renpy.pause(1.2)
    if bangok_four_kalinth.protection:
        m "Her juices dribbled down between my thighs as my erection faded, leaving us just merely lying together with soiled groins... though the condom still protected her depths from my seed.."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "The slurry of our fluids dribbled down between my thighs as my erection faded, leaving us just merely lying together with soiled groins."
    else:
        m "My cum and her juices dribbled down between my thighs as my erection faded, leaving us just merely lying together with soiled groins."

    $ renpy.pause(0.8)
    m "After a few minutes had passed, Kalinth finally took a few deeper breaths than her panting afterglow."
    Kl bangok smile eyeslidded blush flip "Oh... wow."
    show kalinth bangok smile eyeslidded blush:
        zoom 1.6
        ease 0.8 xpos 0.6 zoom 1.0
        xpos 0.6 zoom 1.0
    with None
    m "She rolled off of me to lie down on the couch properly, while I continued to splay across the armrest and seat back."
    Kl "That was... even better than I'd imagined."
    m "I nodded, panting hard myself as I sat up."

    jump bangok_four_kalinth_c3arc_male_post_intimacy


label bangok_four_kalinth_c3arc_male_mctop:
    if persistent.bangok_cloacas:
        m "Kalinth quickly agreed. She lay across the couch, her tail swishing and wings fluttering as she settled into a comfortable position and spread her legs to reveal her glistening draconic cloaca."
    else:
        m "Kalinth quickly agreed. She lay across the couch, her tail swishing and wings fluttering as she settled into a comfortable position and spread her legs to reveal her glistening wet lower lips, and her tailhole a short distance behind."
    m "I couldn't help but stare at that gorgeous sight for a moment while the dragoness watched my every move with anticipation."

    menu:
        "Finger her.":
            jump .finger
        "Lick her.":
            jump .lick
        "Enter her." if bangok_four_playerhasdick == True:
            jump .enter

    label .finger:
        m "As I approached her from behind, I couldn't help but gaze at her puffy, exposed lower lips."
        m "Wanting to make sure she was fully ready, I chose to start with my fingers."
        m "Sliding them inside her, I felt the heat of her insides and the slickness of her arousal coating my digits as they parted her labia."
        m "Kalinth gasped, breath shuddering as I touched her."
        Kl bangok smile eyeslidded blush flip "Oh, yes. So soft..."
        Kl bangok eyeslidded blush flip "Please, don't tease for too long. I want to feel more of you."
        jump todo_out_of_content_bangok_four_kalinth

    label .lick:
        jump todo_out_of_content_bangok_four_kalinth

    label .enter:
        jump todo_out_of_content_bangok_four_kalinth

        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            Kl "Don't hold back. Go ahead. Piss in me."
            m "It took me a few moments to relax as I ground my crotch against hers, feeling my member move within her warm depths."
            m "Then, at last, I felt the familiar rush of relief as I began to drain my full bladder into the dragoness below me."
            m "She moaned and purred all the while, seeming even more turned on by this degrading act than I was."
            m "As my hot jet of piss began to relax into a trickle, Kalinth's depths squeezed, soaking my member with my waste and her own fluids."
            m "Then she spoke up again."
            Kl "Keep going. Fuck me and cum inside and don't stop until you're empty."
            m "I took her words as an invitation. With renewed vigor, I began thrusting into the dragoness"
        jump todo_out_of_content_bangok_four_kalinth


label bangok_four_kalinth_c3arc_male_doggy:
    m "I patted the armrest of the couch."
    c "Do you want me to bend you over... this...?"
    m "I trailed off, realizing as she approached me on all fours that there wasn't really much bending over to be done."
    show kalinth bangok smile blush flip with dissolve
    m "She seemed to understand what I meant, though."
    Kl "That works."
    show kalinth at Position(xpos=0.6, ypos=1.1) with ease
    if persistent.bangok_cloacas:
        m "She lay down over the end of the couch with her hindlegs over the armrest. Then she lifted her tail, exposing between her spread legs her glistening cloaca already soaked with arousal and waiting for me."
        Kl "I'm ready whenever you are."
    else:
        m "She lay down over the end of the couch with her hindlegs over the armrest. Then she lifted her tail, exposing between her spread legs her glistening scaly pussy lips and tight tailhole, the former already soaked with arousal and waiting for me."
        Kl "Stay out of my tailhole, please. Otherwise I'm ready whenever you are."

    menu:
        "Finger her.":
            jump .finger
        "Lick her.":
            jump .lick
        "Enter her.":
            jump .enter

    label .finger:
        show kalinth:
            ease 0.5 zoom 1.2
            zoom 1.2
        with None
        m "As I approached her from behind, I couldn't help but gaze at her puffy, exposed lower lips."
        m "Wanting to make sure she was fully ready, I chose to start with my fingers."
        m "Sliding them inside her, I felt the heat of her insides and the slickness of her arousal coating my digits as they parted her labia."
        m "Kalinth gasped, breath shuddering as I touched her."
        Kl bangok smile eyeslidded blush flip "Oh, yes. So soft..."
        Kl bangok surprise blush flip "But please, don't tease for too long. I want you inside me."
        menu:
            # "Keep fingering her.":
            #     pass
            "Lick her.":
                jump bangok_four_kalinth_c3arc_male_doggy.lick
            "Enter her.":
                jump bangok_four_kalinth_c3arc_male_doggy.enter

        # m "I continued to finger her, feeling her insides clench and unclench around my digits as she moaned and panted."
        # Kl normal flip "A-Are you going to make me beg? Take me, please!"

        # jump todo_out_of_content_bangok_four_kalinth

    label .lick:
        show kalinth:
            ease 0.8 zoom 1.7
            zoom 1.7
        with None
        m "I couldn't help but wonder how the juices around that gorgeous hole tasted, so I knelt on the floor between her hindlegs, spreading her thighs with my hands for easier access."
        m "Parting her labia with the index finger of one hand, I found just how wet she was for me already as I inhaled the sweet scent of her arousal."
        m "It was intoxicating and only heightened the taste of her as I began to tease her entrance lightly with the tip of my tongue, lapping up her juices liberally as she shuddered beneath my hands and mouth."

        Kl bangok smile eyeslidded blush flip "I almost don't want to make you stop. But we can't spend all night here..."

        m "She shifted as I kept going a little longer."

        Kl bangok normal blush flip "Please, I want your length, not just your tongue."

        show kalinth:
            zoom 1.7
            ease 0.8 zoom 1.1
            zoom 1.1
        with None

        m "Reluctantly I got back to my feet."

    label .enter:
        m "My erection throbbed in response to the sight of the eager dragoness before me and her beautiful rear framing her wet, open passage."
        m "I ran my hands over her scaly flanks, feeling the muscle beneath as she arched her back in anticipation."
        show kalinth:
            zoom 1.1
            ease 0.5 zoom 1.2
            pause 0.5
            ease 0.5 zoom 1.3 ypos 1.2
            zoom 1.3 ypos 1.2
        if persistent.bangok_cloacas:
            m "I lined up our bodies, then slid myself into her from behind, entering her eager cloaca."
        else:
            m "I lined up our bodies, then slid myself into her from behind, entering her eager passage."

        show kalinth:
            ypos 1.2
            ease 0.8 ypos 1.25
            ease 0.8 ypos 1.2
            repeat
        m "She moaned loudly, claws digging into the couch fabric and wings rustling softly under me as I began to gently inside of her."

        m "Kalinth was panting hard even before we really got started."

        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            Kl "Mm. Now use me. Piss into me while you're fucking me."

            m "It was hard to relax enough to do so at first, but eventually the urge overcame my nerves and I felt myself starting to pee in her."
            m "Warm liquid gushing forth from my tip and spraying Kalinth inside as she gasped with pleasure."
            m "As I kept gently thrusting, some urine mixed with her copious juices squirted out around my penis, soaking my crotch and dribbling down my balls."
            m "Eventually my bladder was empty, but my desire was not at all diminished. I thrust a little harder as the scent of sex and urine filled my nostrils from our dirty coupling."


        c "Is that good?"
        m "I enjoyed the sight of her tensing and untensing her muscles under me, becoming more worked up with each thrust."
        c "Do you like feeling a human take you like this?"
        Kl bangok smile eyeslidded blush flip "I knew it would feel good..."
        show kalinth:
            ease 0.5 ypos 1.2
            block:
                ease 0.8 ypos 1.15
                ease 0.8 ypos 1.2
                repeat
        with None
        m "I hugged her tail, hiking it up a little further so that, on my next thrust, I was able to push a little deeper inside, bringing us slightly closer together and eliciting another gasp from both me and the dragoness beneath me."
        if bangok_four_kalinth.protection:
            m "The feelings of her insides clenching around my condom-wrapped length were exquisite. I couldn't help but thrust a little harder and faster, eager to feel more of her."
        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            m "The feelings of her piss-soaked insides clenching around my length were exquisite. I couldn't help but thrust a little harder and faster, eager to feel more of her."
        else:
            m "The feelings of her insides clenching around me were exquisite, and I couldn't help but thrust a little harder and faster, eager to feel more of her."
        c "You have no idea how good."
        m "Her expression was one of pure pleasure as she continued to pant, nuzzling the couch cushions while her tail writhed in my grasp with each of my thrusts."
        m "The dragoness' passage was so very warm, flushing my body with heat and arousal as I slid myself in and out of her eager depths with increasingly wet slaps."

        Kl bangok eyesclosed blush flip "Don't stop..."
        m "She clung to the couch cushions as she arched her back, pushing her rear up against me as I continued to thrust into her."
        Kl "Please don't stop. Ohhhh..."
        m "I wasn't about to stop now. I looked down, admiring the ripples each of my hard and fast thrusts made over her rear."
        m "Her cloaca tightened around me, her inner muscles clenching, and I closed my eyes as I lost myself in our lovemaking."
        show black
        with dissolvemed
        $ renpy.pause (0.5)
        if bangok_four_kalinth.protection:
            m "In moments, the sensation of her climaxing passage was too much for me to bear and with a final grunt, I came into the condom's tip, spurting white ropes of human seed into the thin barrier protecting the dragoness' eager depths."
        else:
            m "In moments, the sensation of her climaxing passage was too much for me to bear and with a final grunt, I came inside her, spurting white ropes of human seed into the dragoness' eager depths."

        m "I struggled to keep thrusting, per her request, my strength flagging as I carried us through our shared climaxes until finally I just lay on her tail, catching my breath."

        show kalinth at Position(ypos=1.2)
        hide black
        with dissolveslow

        m "Eventually, as my body began to recover its strength and the aftershocks in Kalinth's nethers subsided, I pulled out."
        if not bangok_four_kalinth.protection:
            if persistent.bangok_cloacas:
                m "It wasn't long before I could see my seed oozing from her cloaca in small droplets."
            else:
                m "It wasn't long before I could see my seed oozing from her lower lips in small droplets."
            if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
                m "I couldn't tell which of the other splatters of fluids on our crotches was my urine and which were her juices as they dribbled down our thighs."

        m "Like an overgrown cat, she stretched out on the couch, then rolled over with first her front half, then her lower body."
        show kalinth bangok smile eyeslidded blush:
            zoom 1.3
            ease 0.8 ypos 1.1 zoom 1.2
            ease 0.8 ypos 1.0 zoom 1.0
            ypos 1.0 zoom 1.0
        with None
        m "She wriggled her hips, sliding her way a little further to get her rear off the armrest so she could lie down normally."
        m "Then she sighed happily."
        Kl "That was... even better than I'd imagined."
        m "I smiled at her, still catching my breath."
        jump bangok_four_kalinth_c3arc_male_post_intimacy


label bangok_four_kalinth_c3arc_male_post_intimacy:
    c "Well, I aim to please."
    m "She dipped a dulled claw into her folds, teasing herself, before bringing it up to her scaly lips for a taste of our union."
    show kalinth bangok smile eyesclosed blush with dissolve
    m "She licked it clean, closing her eyes again."
    if bangok_four_kalinth.protection:
        Kl "Mmm... give me the condom? I'd like to taste you."
        menu:
            "Give her the condom.":
                $ renpy.pause (0.5)
                play sound "fx/chug.wav"
                m "As soon as I handed her the condom, she popped it into her mouth and lifted the reservoir over her head, driving her tongue up the condom's shaft to lick out my cum from its reservoir."
                m "I blushed as I watched her sinuous tongue work its magic."
                m "She swallowed, then licked her lips."
            "Throw it away.":
                $ renpy.pause (0.5)
                play sound "fx/clink3.ogg"
                m "I pulled the condom off, then tossed it into the trash can."
                c "Sorry, I'm not comfortable with that."
                m "Kalinth gave a small pout, but didn't seem too upset."
                Kl "Suit yourself."
    Kl "I don't think I'll be able to focus on any of my work for the rest of the night..."
    menu:
        "Help clean her up with your tongue.":
            pass
        "Part ways.":
            c "I'm sorry I was such a distraction."
            Kl bangok surprise "Don't be. I certainly enjoyed it."
            c "As did I."
            Kl bangok smile "I suppose I'd better get you my number, then. If you'd like to do this again sometime."
            c "Sure."
            jump bangok_four_kalinth_c3arc_part_ways

    show kalinth bangok surprise blush:
        zoom 1.0
        ease 0.5 zoom 1.7 ypos 1.0
        zoom 1.7 ypos 1.0
    with None
    m "With an impish grin, I knelt next to where she lay on the couch."
    Kl bangok surprise blush "Oh? Willing to help me more at no benefit to yourself? No wonder Bryce keeps asking you for help with the investigations."
    c "There's some benefit there. But in both cases, let's just say the work is its own reward."
    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "Leaning over her soaked cloaca, my tongue flicked out to lick up a first teasing droplet to sample her well-churned juices and to gauge her reaction."
        else:
            m "Leaning over her soaked pussy, my tongue flicked out to lick up a first teasing droplet to sample her well-churned juices and to gauge her reaction."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        if persistent.bangok_cloacas:
            m "Leaning over her piss-soaked and cum-filled cloaca, my tongue flicked out to lick up a first teasing droplet to sample our well-churned fluids and to gauge her reaction."
        else:
            m "Leaning over her piss-soaked and cum-filled pussy, my tongue flicked out to lick up a first teasing droplet to sample our well-churned fluids and to gauge her reaction."
    else:
        if persistent.bangok_cloacas:
            m "Leaning over her cum-filled cloaca, my tongue flicked out to lick up a first teasing droplet to sample our combined taste and to gauge her reaction."
        else:
            m "Leaning over her cum-filled pussy, my tongue flicked out to lick up a first teasing droplet to sample our combined taste and to gauge her reaction."
    Kl bangok smile eyeslidded blush "Mmm... yes."
    m "She sighed contentedly, then spread her legs a little wider with lustful eyes."
    Kl "I can't say no to help like this."
    if bangok_four_kalinth.protection:
        m "Eager to provide said help, I dove my tongue back into the dragoness' folds, tasting more of her slick arousal as she gasped and moaned beneath me."
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "Eager to provide said help, I dove my tongue back into the dragoness' folds, soiling my face and tongue with our lustful waste and fluids as she gasped and moaned beneath me."
    else:
        m "Eager to provide said help, I dove my tongue back into the dragoness' folds, tasting our mix of juices and semen as she gasped and moaned beneath me."
    m "My hands were eager too, parting her labia for easier access to those extra teasing deeper folds that caused her muscles to clench and push out more of our mixed passions."
    Kl bangok smile eyeslidded blush "Oh, yes..."
    show kalinth:
        zoom 1.7
        ease 0.5 zoom 1.8
        zoom 1.8
    with None
    m "She crossed her hindlegs behind my head."
    Kl bangok smile eyesclosed blush "You're going to make me cum again..."
    m "I continued my ministrations, eager to see if I could bring the dragoness off for a second time so soon."
    m "Her breathing was growing louder and faster as my tongue explored her insides and outside, lapping up every drop of our combined fluids and teasing all those sensitive areas that made her moan and whimper."
    Kl bangok eyesclosed blush "I think... I think I'm..."
    m "Kalinth panted heavily beneath me."
    show black with dissolve
    m "Then, abruptly, her legs clamped down, pinning my face in place as she arched her back."
    m "She wrapped her forepaws around her own muzzle, muffling her moans of passion and pleasure with a strangled cry, bucking against the couch as another climax washed over her body."

    m "Juices from her passage flooded my tongue, soaking my face, but I continued to lap them up eagerly, drinking in every last drop while she clutched me to her entrance."

    show kalinth smile eyeslidded blush
    with dissolve
    hide black
    with dissolve

    m "The dragoness eventually, seemingly reluctantly, relaxed her legs to let me breath again, though she still draped her legs over my shoulders, rubbing my back gently."

    show kalinth:
        zoom 1.8
        ease 0.5 zoom 1.7
        zoom 1.7
    m "As I finally sat back on my haunches, panting and sweaty from the hotbox held to my face, Kalinth grinned down at me."

    Kl "I have got to get you my number."

    c "I guess you do."
    m "I tried to wipe off my face with an arm, but just wound up getting that wet and sticky too."
    c "And a towel, if you know where one is?"

    scene office at Pan ((128, 250), (0, 250), 3.0) with fade
    $ bangok_four_kalinth.have_number = True

    m "After Kalinth found some towels that she could wash later, she gave me her number and left me to my work."
    jump bangok_four_kalinth_c3arc_finish_timing


label bangok_four_kalinth_c3arc_part_ways:
    show kalinth normal at center with ease
    m "Kalinth rose from the couch, then got her claws on a scrap of paper."
    play sound "fx/scribblex.ogg"
    $ renpy.pause (0.5)
    m "She wrote down her number, then handed it to me."
    $ bangok_four_kalinth.have_number = True
    Kl bangok smile blush "I'll leave you to your review of the files, then."
    hide kalinth with easeoutleft
    $ renpy.pause (0.3)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (0.5)
    jump bangok_four_kalinth_c3arc_finish_timing


label bangok_four_kalinth_c3arc_finish_timing:
    m "As I got dressed again, I took a look at the clock and realized how late it was getting."
    c "(Man, that took a lot of time. I don't think I can do too much here.)"
    $ c3arcquesx = 1
    jump c3arcques

label todo_out_of_content_bangok_four_kalinth:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")
