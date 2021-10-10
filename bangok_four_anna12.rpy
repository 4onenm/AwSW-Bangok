init python:
    bangok_four_anna1_discourseonmorphologicalvariations = True
    bangok_four_anna1_sexrequested = False

init python in bangok_four_anna2:
    havecondoms = False


    waitvert = True
    finger = True
    lick = True

    fist = False


    annacame = False

label bangok_four_anna1_skipmenu:
    play sound "fx/system3.wav"
    s "Bet with Anna for sex?"
    menu:
        "Yes. Bet with Anna for sex.":
            $ bangok_four_anna1_sexrequested = True
        "No. Not that far.":
            pass
    jump bangok_four_anna1_skipmenu_return

label bangok_four_anna1_winmenu:
    $ bangok_four_anna1_sexrequested = False
    menu:
        c "Let's say if I win..."
        "Real date.":
            jump bangok_four_anna1_winmenu_return
        "Sex.":
            $ bangok_four_anna1_sexrequested = True
            c "Let's say if I win{fast} you'll have sex with me."
            An face flip "And I suppose you expect me to respond with, \"and if I win, I get to have sex with you\"?"
            c "Well, I can't say I'd be opposed to that."
            An smirk flip "Too bad. If I win, I'll have you come in sometime so I can run more tests on you."
            if blood == False:
                An "I won't even need your blood anymore."
            jump bangok_four_anna1_winmenu_afterannablood
        "A discourse on the morphological variations of dragon species, including factors cerebral, physical, and societal, with special interest toward understanding the apparently equivalent levels of intelligence despite clearly divergent evolutionary pathways." if bangok_four_anna1_discourseonmorphologicalvariations:
            c "Let's say if I win{fast} you'll help me understand how all these dragon species came about with the same level of intelligence? A bit of a biology trade-off."
            python:
                bangok_four_anna1_discourseonmorphologicalvariations = False
                annamood -= 1
            An face flip "Are you kidding me?"
            An sad flip "Do I look like I have time to go over dragon biology 101 with you?"
            An face flip "Just pick up a textbook from the library."
            An sad flip "If you have advanced questions, then maybe. But teaching you the basics isn't worth a kid's game."
            c "Oh. Okay then. Something that takes less time..."
            jump bangok_four_anna1_winmenu

label bangok_four_anna1_goodending:
    An normal flip "I won't have a spot in the facility to do the tests for a while, though, so I suppose next time we meet, it'll be for sex."
    jump bangok_four_anna1_goodending_thankyou

label bangok_four_anna1_goodending_nvl:
    n "Even though my bet of forcing her to have sex with me with me was more to get back at her for her earlier rudeness, I had not expected this outcome. I was not even sure what I expected from this meeting in the first place, but now I was locked into sex with her and being her own, personal guinea pig."
    if bangok_four_firsttime == True:
        n "I hadn't tried anything with a dragon before. Would I even be able to get it up when the time came?"
    else:
        n "I had bed a dragon before, but Anna seemed like a whole new experience."
    jump bangok_four_anna1_goodending_nvl_end

label bangok_four_anna1_medending:
    An normal flip "But you know what, this wasn't so bad after all. Maybe I'll let you have your sex."
    jump bangok_four_anna1_medending_really

label bangok_four_anna1_medending_nvl:
    n "After all, proposing a sex was my way of sticking it to her for being rude."
    n "Even though I lost the bet, she didn't seem to mind having sex with me, as long as she got what she wanted. Whether I would follow up on it was up to me, though."
    if bangok_four_firsttime == True:
        n "I hadn't tried anything with a dragon before. Would I even be able to get it up when the time came?"
    else:
        n "I had bed a dragon before, but Anna seemed like a whole new experience."
    jump bangok_four_anna1_medending_nvl_end

label bangok_four_anna1_badending:
    An normal flip "I think you're just experiencing acute posterior pain, because you don't get to have sex with me now."
    menu:
        "I didn't want to have sex with you in the first place.":
            c "I didn't want to have sex with you in the first place. I just wanted to teach you some manners."
            An disgust flip "Like I'd ever have sex with a mammal like you."
            c "Oh, am I not good enough for you, now?"
            An normal flip "Frankly, if you're an ambassador, a shining example of humanity, I'd say your entire species isn't good enough for anyone."
            An sad flip "It's something in the way you just exude virtues such as civility and humbleness, trying to force someone into sex with you on a bet."
        "I didn't expect to lose.":
            c "This was a kid's game. It wasn't supposed to be this hard."
            An disgust flip "You actually expected to force me into sex on a bet? And, what, leave me with nothing?"
            c "I could say the same to you, trying to force me into a bunch of experiments. What were you going to do, cut me open?"
            An normal flip "Of course not. When do you think we live, {i}The First War{/i}? I have much better ways of looking inside you."
            An sad flip "Not that I'm sure I'll even want to see that, with the twisted versions of civility and humbleness you pretend to exude."
    jump bangok_four_anna1_badending_end









label bangok_four_chap2storehealth_anna12:
    m "Remembering my arrangement with Anna, I picked up one of the boxes of smaller sizes, labeled for runners, to purchase."
    c "(Hope this doesn't seem too strange to the store clerk.)"
    jump bangok_four_chap2storehealth_anna12_return

label bangok_four_chap2storehealth_checkout_anna12:
    play sound "fx/register.ogg"
    $ renpy.pause (5.0)
    stop sound fadeout 1.0
    m "The store clerk checked out what I'd picked up without comment."
    jump bangok_four_chap2storehealth_checkout_anna12_return















label bangok_four_anna2_nomorewaiting:
    m "In the end, I decided that enough was enough. Not wanting to wait any longer, I left, even though she still owed me sex."
    jump bangok_four_anna2_nomorewaiting_end

label bangok_four_anna2_wantthisornot:
    An disgust "I just told you that I am, so get off my back. Do you want to fuck me or not?"
    jump bangok_four_anna2_wantthisornot_end

label bangok_four_anna2_whatnow:
    An "Well, we're not doing this here in the lab. I suppose we could go back to your government-funded apartment."
    menu:
        "Why not?":
            $ anna2mood -= 1
            An face "Because it's virtually guaranteed we'll break something."
            An sad "Not to mention the sanitary issues."
            c "Alright, alright. My place it is."
        "Sure.":
            $ anna2mood += 1
        "All that waiting left me kinda hungry...":
            An face "Was that supposed to be an \"eating out\" joke? Because I have bad news for you."
            menu:
                "That's exactly what it was.":
                    c "What do you mean by bad news?"
                    An normal "I don't like dental dams. And you, in particular, aren't putting your mouth on my genitals without one."
                    c "Oh."
                    An "Forget about it. Let's go do this."
                "No, I meant that literally.":
                    An sad "What do you expect me to do about that, magic up food for you?"
                    c "It's not that crazy to go out for dinner, especially since I assume you haven't eaten either."
                    An "Fine. Maybe the coffee place is still open. I don't know."
                    jump bangok_four_anna2_alley
    $ renpy.pause(0.9)
    jump bangok_four_anna2_apartment

label bangok_four_anna2_romanticdate_alley:
    An sad "Excuse me?"
    c "I mean, going to get dinner, that's basically what this turned into."
    An face "This is not what I agreed to."
    c "But you are hungry too, right? I'm not going to make you skip dinner to have sex with me."
    An "..."
    c "My apartment is stocked with some food supplies. I'll figure out something I can cook for us."
    An normal "Actually, I know a place that should still be open."
    An smirk "I suspect it'll be better cooking than whatever you're planning."
    c "Sure."
    jump bangok_four_anna2_romanticdate_alley_end

label bangok_four_anna2_romanticdate_unusualbutfun:
    if anna2mood > 4:
        An smirk c "Was fun? Who said the fun stops after dinner?"
        if bangok_four_anna1_sexrequested == True:
            c "Oh, right. I almost forgot."
        else:
            c "Oh?"
    elif anna2mood > 0 and bangok_four_anna1_sexrequested == True:
        An normal c "It isn't the end of the evening, either."
        c "Oh, right. I almost forgot."
    else:
        An sad c "Well. One of us is enjoying it, at least."
    jump bangok_four_anna2_romanticdate_unusualbutfun_return

label bangok_four_anna2_romanticdate_conclusion:
    if bangok_four_anna1_sexrequested == False:
        if anna2mood > 4:
            An sad c "I have to say, I'm surprised how well this evening went, considering."
            c "Well, I can't take all the credit."
            An normal c "You can take enough of it."
            An sad c "I know the movie we had planned didn't work out, but..."
            An smirk c "If we consider my hunting prowess to be a show, that makes dinner and a movie."
            c "Oh?"
            An "Do you want to do anything else before we call it a night?"
            menu:
                "Accept.":
                    pass
                "Reject.":
                    c "No, thank you. You've more than fulfilled your end of our bet."
                    $ anna2mood += 1
                    An normal c "Your loss."
                    An "That's enough talking, then. Back to the facility so I can clean up and finish some things."
                    jump bangok_four_anna2_romanticdate_conclusion_return
        else:
            menu:
                "Is that really our whole date?":
                    c "You know, humans have a saying: \"Dinner and a movie.\""
                    An normal c "We have that saying too."
                    c "Well, we just ate, and your hunting prowess was quite the show..."
                    An face c "Was that really supposed to be a pickup line?"
                    if anna2mood < 1:
                        c "You bet it was."
                        An disgust c "Fuck off."
                        An normal c "I agreed to a date, not anything more."
                        An "If you want a chance at more, you'll have to sit through my experiments, and find something else I'd be willing to trade it for."
                        $ renpy.pause(0.8)
                        c "..."
                        $ renpy.pause(0.8)
                        An sad c "Just follow me back to the facility. I need to clean this off, and I have a thing or two more to finish up."
                    else:
                        c "Depends, are you interested?"
                        if anna2mood > 2:
                            An normal c "..."
                            An smirk c "I might be."
                        else:
                            An sad c "..."
                            An normal c "No."
                            c "Alright then. Forget I said anything."
                            An "Already done."
                            jump bangok_four_anna2_romanticdate_conclusion_end
                "[[Agree and follow her.]":
                    jump bangok_four_anna2_romanticdate_conclusion_return

    if bangok_four_anna1_sexrequested == True:
        if anna2mood > 2:
            An smirk c "Now, about your reward."
            c "My place, right?"
        else:
            if anna2mood > 0:
                c "So, about that bet reward."
                An face c "Not in the mood."
                c "I... see. Should we reschedule?"
                An sad c "That won't work. At least not for me."
                An face c "Today was the only day I could leave early. I won't have another chance any time soon."
                menu:
                    "I understand.":
                        c "I mean, that's not what I was hoping, but I'm not going to force the issue."
                        $ renpy.pause(0.8)
                        $ anna2mood += 1
                        An normal c "Thanks. I'm glad you can be reasonable."
                        c "What else is an ambassador for?"
                        An smirk c "Good point."
                        c "Anyway, you said we should probably go."
                        An normal c "Right."
                        jump bangok_four_anna2_romanticdate_conclusion_end
                    "That's not what we agreed on.":
                        pass
            else:
                An sad c "Back to the facility, then. I think I've wasted enough time on this."
                c "What about my reward?"
                An normal c "Oh, I'm sorry. You decided to be hungry instead."
                An sad c "Besides, I thought you didn't like the wild side. You wouldn't want to fuck someone covered in blood, would you?"
                menu:
                    "You bet I would.":
                        if nofood == True:
                            An "Blood makes you lose your apetite, but not your sex drive? Creep."
                        else:
                            An "Too bad."
                    "Okay, maybe not...":
                        An normal c "Good."
            c "We agreed on sex, though."
            An sad c "And you chose to co-opt it into a romantic date. That's your problem, not mine."
            An normal c "I'm not going to stand here arguing about it all night."
            c "..."
            scene black with dissolve
            $ renpy.pause(0.5)
            m "The walk back to the facility gave me a chance to cool down about the bait-and-switch, though I couldn't read the emotions going through Anna's head."
            jump bangok_four_anna2_romanticdate_conclusion_end
    else:
        An smirk c "Now, the question of where."
        c "I guess my apartment?"

    if False: # nofood == False: # Disabled until I write the woods scene
        An "Actually, since you so enjoyed nature's bounty out here..."
        c "Oh?"
        An smirk c "Once we get some distance, we could find a quiet spot in the woods and see what happens."
        menu:
            "Don't you need to wash the blood off?":
                An sad c "I actually thought that would be part of the fun."
                menu:
                    "Not for me.":
                        c "I, uh, I don't do blood in sex."
                        An normal c "I suppose I can see why, given your fragility."
                        An smirk c "Then in the interest of not breaking you somehow, let's head back to your apartment."
                    "Sounds interesting.":
                        c "I, ah, suppose I could see what you have in mind."
                        show anna smirk c
                        $ renpy.pause (0.8)
                        jump bangok_four_anna2_woods
            "I'd prefer to be inside.":
                An normal c "In that case, your apartment it is."
            "Sounds fun.":
                $ anna2mood += 1
                c "I'm in."
                An smirk c "Thought you would be."
                jump bangok_four_anna2_woods
    else:
        An normal c "Sounds good."
    An sad c "I'd rather not leave evidence all over your living room, though, so I may need to ruin a towel or two to get this blood off."
    c "Alright."
    jump bangok_four_anna2_apartment

label bangok_four_anna2_apartment:
    scene black with dissolve
    $ renpy.pause (1.0)
    scene o2 at Pan((0, 250), (0, 250), 0.1)
    show anna normal
    with dissolvemed

    $ renpy.pause (0.5)
    if anna2mood > 0:
        An smirk "I suppose now we see what's under all those layers."
    else:
        An sad "I suppose now we see what's under all those layers."
    if bangok_four_playerhasdick is None:
        menu:
            "Show her your dick.":
                $ bangok_four_playerhasdick = True
            "Show her your lack of dick.":
                label bangok_four_anna2_apartment_nodick:
                show black with None
                play sound "fx/system3.wav"
                s "Apologies, but the author of this mod leans more toward the gay male side of things, and does not intend to attempt to write F/F."
                play sound "fx/system3.wav"
                s "You may feel free to contribute an F/F script to the mod's development if that is your preference."
                play sound "fx/system3.wav"
                s "Meanwhile, would you like to skip to the end? Or can you accept continuing this scene as a male?"
                menu:
                    "Yes. I'd like to skip ahead.":
                        play sound "fx/system3.wav"
                        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                        jump bangok_four_anna2_apartment_skip
                    "No. Don't skip ahead.":
                        play sound "fx/system3.wav"
                        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                        hide black with dissolvemed
    elif bangok_four_playerhasdick == False:
        jump bangok_four_anna2_apartment_nodick

    play sound "fx/undress.ogg"
    $ renpy.pause (1.5)

    An normal "Definitely a mammal. Definitely a male."
    menu:
        "Actually, I prefer a different set of pronouns...":
            An "Fine. We don't need pronouns to use that thing of yours."
        "[[Say nothing.]":
            pass

    if bangok_four_anna1_sexrequested == True:
        An "Now, you did buy condoms for the occasion, right?"
        if chap2storehealth == False:
            $ bangok_four_anna2.havecondoms = True
            c "Of course."
            m "I retrieved the box I'd purchased during my visit to the store, removing one small foil-wrapped barrier device."
        else:
            c "Uh..."
            An face "Oh for crying out loud."
            menu:
                "I thought you would bring something.":
                    c "I'm the visitor from another world, after all."
                    An sad "That's why it was your responsibility to pick one that's safe for you."
                    c "Let's look around. I'm sure some are stocked."
                "I thought this place would be stocked.":
                    c "It's had everything else I've needed."
                    An "And did you look for them?"
                    c "..."
                    An "I see."
                "Let's look around. I'm sure some are stocked.":
                    pass
    else:
        An face "Damnit."
        c "What?"
        An sad "I didn't expect to do anything like this, so I didn't bring any condoms."
        An normal "And before you ask, no, I won't be having sex outside my phylogenic group without one."
        $ renpy.pause (0.8)
        c "Well, let's look around. I'm sure some are stocked."

    if bangok_four_anna2.havecondoms == False:
        An normal "Fine. I'll check the bathroom, you check the bedroom."
        hide anna with dissolve
        $ renpy.pause (0.5)
        play sound "fx/rummage.ogg"
        m "A box of condoms was in the first drawer I checked in the nightstand next to my bed, shoved near the back."
        m "I returned, holding it aloft, only to find Anna already seated on the couch with one next to her."
        show anna normal at center with dissolve
        c "Wait, you found some in there, too?"
        An smirk "Of course. I'm sure they have them all over the apartment. Better to avoid a health incident with an ambassador from another world, right?"
        c "Oh."
        An "Here. Use this brand instead of that one."
        m "Setting the box I'd found aside, I took the single condom she offered."

    m "It took a couple pumps by hand to get going enough to put the condom on."
    show anna sad with dissolve
    m "Anna looked on with some concern."
    An "Is it supposed to start limp like that? Most dragons -- most species in general -- have a baculum to keep it from being too soft for insertion."
    menu:
        "What's a baculum?":
            $ anna2mood -= 1
            An face "Nevermind."
            An sad "I suppose as long as you go in hard, it doesn't matter."
        "Yeah, that's normal for us.":
            An normal "I see."
        "It gets hard when we see someone or something sexually stimulating.":
            if anna2mood > 2:
                An smirk "I see."
            else:
                An "I see."
    c "What about for you?"
    An normal "Haven't you looked in a science textbook yet?"
    c "Not really. I'd prefer to get to know these things from people, make connections."
    if anna2mood > 3:
        An smirk "Connections like this?"
        c "I have to say it's unexpected, but I think it'll be a good thing."
    else:
        An face "Connections like this?"
        c "Absolutely."
        if bangok_four_anna1_sexrequested == True:
            An sad "Let's just get it over with."
        else:
            show anna normal with dissolve

    # hide anna with dissolve
    # $ renpy.pause(0.3)
    show anna:
        xanchor 0.5
        ease 1.0 pos (0.8, 1.0)
    with None
    $ renpy.pause(0.7)
    show anna:
        pos (0.8, 1.3)
        rotate 15
    with dissolve
    m "Anna stepped back up to the couch, then sat back, swinging her tail between her legs to sit on it and exposing her underside."
    m "Now in this position, I could clearly make out her single vertical slit, hidden on a slight mound between her legs."
    if persistent.bangok_cloacas == False:
        m "A small rosebud winked up at me from an inch or two further down."
    label bangok_four_anna2_apartment_startingmenu:
    menu:
        "Finger." if bangok_four_anna2.finger == True:
            $ bangok_four_anna2.finger = False
            m "I stepped in closer, reaching out to caress her opening."
            An sad "Are those hands of yours clean?"
            menu:
                "Clean enough.":
                    pass
                "I've washed them!":
                    pass
                "Do you want me to go find gloves?":
                    An face "No."
            An normal "Just be careful with your claws. I don't want you to cut me in there."
            c "Unless you're way more delicate than a human, I doubt that will be a problem."
            m "Slowly, I pressed two fingers inside, continuing my small, gentle circles with the rest of my hand. Anna's legs shuddered slightly, where they were sticking up in the air."
            $ renpy.pause (0.8)
            if anna2mood > -1:
                An smirk "You can keep going with that."
            else:
                show anna sad with dissolve
            $ renpy.pause (0.5)
            m "After giving her another moment with this gentle teasing, I added a third finger, finding it slipping in even more easily than the first two as lubrication began to slicken her lips."
            $ renpy.pause (0.8)
            if anna2mood < 1:
                An face "Okay, stop."
                c "Huh? I thought you liked this."
                An sad "We're here to fuck. Just fuck me already."
                menu:
                    "[[Add a fourth finger.]":
                        if anna2mood > -2:
                            $ anna2mood += 1
                            m "Anna shivered, but I felt her squeeze around my fingers, and she made no move to stop me."
                            $ renpy.pause(0.8)
                            An smirk "Fine. Have it your way. But you'd better get me off."
                            c "I intend to."
                        else:
                            $ anna2mood -= 2
                            $ bangok_four_anna2.lick = False
                            show anna disgust with dissolve
                            play sound "fx/impact3.ogg"
                            # play sound2 "fx/chair.wav"
                            $ renpy.pause(0.1)
                            hide anna with None
                            $ renpy.pause(0.0)
                            show o2 at Pan((0,150),(0,150),0.0)
                            show anna disgust at Position(xpos=0.8,ypos=1.0, xanchor='center')
                            with vpunch
                            m "Anna kicked me off of her, hard, leaving pinpricks from her claws in my chest. I stumbled into the armchair next to the couch."
                            An rage "The terms of our deal were pretty fucking clear. Sex. Not fingerfucking, sex."
                            An sad "I've had it up to here with you. But I'm going to honor the terms of our deal. So get over here and stick it in me already. No more of whatever the fuck that was."
                            c "..."
                            $ renpy.pause(0.8)
                            show o2 at Pan((0,250),(0,250),0.0) with ease
                            m "I got back to my feet, a little more wary of what she could do to me if I pissed her off."
                            show anna disgust:
                                pos (0.8, 1.3)
                                rotate 15
                            with dissolve
                            m "Anna lay back down, still looking like she'd tear me open if I angered her again."
                            jump bangok_four_anna2_apartment_startingmenu
                    "If you insist.":
                        jump bangok_four_anna2_apartment_startingmenu
            else:
                An smirk "You were right. Your claws aren't a problem."
                An blush "And your skin is much softer than any dragon's scales."
                menu:
                    "[[Add a fourth finger.]":
                        m "This finger resisted slightly more. But with her natural lubrication it fit, followed by most of my palm."
                        $ anna2mood += 1
                        An lipbite "Mm. Now you're in for it."
                        c "Huh?"
                    "[[Move on to something else.]":
                        show anna sad with dissolve
                        $ renpy.pause(0.3)
                        show anna normal with dissolve
                        m "Anna's folds tugged at my fingers as I withdrew, but she made no comment on my decision."
                        jump bangok_four_anna2_apartment_startingmenu
            An smirk "I want your arm. Let's see what the rest of that soft flesh feels like."
            menu:
                "What, like, detached from my body?":
                    c "I'd like to keep my arms, thanks."
                    An blush "Fine, you can have it back."
                    An smirk "But first I want it as deep inside me as you can push it."
                    c "O-Oh."
                "No way.":
                    $ anna2mood -= 2
                    c "I was just exploring. I didn't think you'd..."
                    show anna sad with dissolve
                    $ renpy.pause(1.2)
                    An blushpalm "Seriously?"
                    An sad "Fine. Take your hand out and fuck me, if that's all you want."
                    jump bangok_four_anna2_apartment_startingmenu
                "Okay.":
                    An smirk "Good little human."

            show anna blush with dissolve
            m "I slid in and out the four fingers I had so far, getting her used to the size until my hand was soaked and buried right up to the base of my thumb."
            $ renpy.pause(0.5)
            c "You're sure?"
            An blushpalm "Would I be asking you to do it if I wasn't?"
            m "I pulled back out to the tips of my fingers, then folded my thumb into my palm and pressed my whole hand inside of her."
            An lipbite "Ngh..."
            m "Her slit clenched around my wrist, insides undulating as they milked my hand for a substance it could not provide."
            c "You okay?"
            An blush "Could you stop asking me that and push deeper already?"
            c "What should I do when I do run out of room?"
            An blushpalm "I'll tell you when you get there."
            show anna blush with dissolve
            m "Heeding her instructions, I sank more of my arm inside of her. Very quickly, the section that had been lubricated by her fluids thus far ended, and resistance to my force increased dramatically."
            An blushpalm "Should've thought about lube."
            An blush "Doesn't matter. Pull out."
            show anna lipbite with dissolve
            m "I did so, retrieving the small part of my wrist and entirety of my hand I'd gotten in. Anna bit her lip the whole way out, then sighed with relief."
            hide anna with None
            $ renpy.pause(0.0)
            show anna blush at Position(xpos=0.8,ypos=1.0, xanchor='center')
            m "Then she stood up."
            An normal "Kneel here, brace your elbow on the table, here."
            menu:
                "I thought we were going to have sex.":
                    An smirk "You're the one who got me going. Now it will be first me, then you."
                "This is a lot of orders you're giving me...":
                    $ anna2mood -= 1
                    An face "Boo-hoo. Want me to write them down for you?"
                    An normal "Just put your elbow on the table and stick your hand up."
                "Yes, Anna.":
                    $ anna2mood += 1
                    show anna smirk with dissolve
                    $ renpy.pause (0.5)
                    An "You. I like you."
            m "Once my hand was in place, Anna made sure my fingers were in the shape I'd used when penetrating her, and that I was keeping them that way."
            show anna blush flip at Position(xpos=0.7) with dissolve
            m "Then she turned around and lined her slick slit back up, one of her legs coming down right in front of me."
            $ renpy.pause(0.3)
            show anna lipbite flip at Position(xpos=0.7,ypos=1.02) with ease
            An "Nnh!"
            m "The muscles in Anna's passage pressed in lewdly around my hand, squeezing more of her natural lubricant around my wrist and sending it running in small rivulets down my arm."
            $ renpy.pause (0.4)
            An blush flip "Spread that around."
            m "I did as ordered, trying to more evenly distribute her juices on the next part of my arm. Anna shivered as the fingers of my other hand brushed her slit."
            An smirk flip "You're still braced against the table, right?"
            c "Yeah."
            An blush flip "Good."
            show anna lipbite flip at Position(xpos=0.7,ypos=1.0) with ease
            show anna lipbite flip at Position(xpos=0.7,ypos=1.04) with ease
            m "Anna lifted herself up, her clenching almost tugging my arm with her. Just before my fingers were about to leave, she reversed direction and pressed back down, fucking herself onto my hand as if it were a dildo."
            An "Ah!"
            m "We came up against resistance almost immediately, but this one came from within her."
            show anna smirk flip with dissolve
            m "A glance back from her showed in her face. Whatever this felt like for her, it was a good feeling."
            menu:
                "[[Form a fist.]":
                    $ anna2mood += 1
                    $ renpy.pause (0.5)
                    An sad flip "What are you...?"
                    m "Shifting around me, Anna felt the additional room I'd bought her to take my arm."
                    An blush flip "Hm."
                    show anna lipbite flip:
                        ease 1.0 ypos 1.02
                    with None
                    m "She lifted up, walls shifting and spreading around the ball of my fist inside her."
                    m "Then she switched direction, pressing down fast."
                    show anna lipbite flip:
                        ease 0.4 ypos 1.06
                    with None
                    c "Anna, w-wait--"
                    show anna orgasm flip with dissolve
                    An "F-Fuck! Yes!"
                    m "I froze."
                    c "(Yes?)"
                    show anna lipbite flip with dissolve
                    $ bangok_four_anna2.fist = True
                "[[Spread your fingers.]":
                    $ renpy.pause (0.5)
                    $ anna2mood -= 3
                    An sad flip "What are you...?"
                    m "As her walls shifted around me, my fingers dug into her passage."
                    An disgust flip "Ah! Ow! [player_name], for fuck's sake!"
                    show anna at Position(xpos=0.8, ypos=1.0) with ease
                    show anna sad with dissolve
                    m "She stepped away, yanking my hand free, glaring at me as I worked out the jarring my fingers had experienced from her innards pressing back."
                    c "Sorry..."
                    An disgust "Don't say \"sorry.\" Don't play games with my fucking genitals!"
                    An sad "Put your fingers back the way they were."
                    m "I did so. After inspecting me and my hand for a long moment, Anna turned her tail back toward me, then sank back down."
                    show anna sad flip with dissolve
                    show anna at Position(xpos=0.7, ypos=1.0) with ease
                    show anna at Position(xpos=0.7, ypos=1.02) with ease
                    show anna at Position(xpos=0.7, ypos=1.04) with ease
                    An sad flip "D-Damnit. Still hurts a little."
                "[[Don't get any ideas.]":
                    pass

            show anna:
                ease 1.0 ypos 1.02
                ease 1.0 ypos 1.04
                ease 0.7 ypos 1.02
                ease 0.5 ypos 1.04
                block:
                    ease 0.40 ypos 1.02
                    ease 0.25 ypos 1.04
                    repeat
            with None
            play soundloop "fx/rub2.ogg" fadein 4.0
            m "Anna began to fuck my wrist and hand, gently at first, then with increasing vigor."
            show anna lipbite flip with dissolve
            m "Each time, she thrust my hand against the resistance inside of her harder."
            An "A-Almost..."
            menu:
                "Anna, don't hurt yourself!":
                    $ anna2mood += 1
                    An "I've gone far harder than this."
                "Hey, don't break my hand!":
                    $ anna2mood -= 1
                    An blushpalm flip "Are... you humans... really... so fragile...?"
                    show anna lipbite flip with dissolve
                "[[Say nothing.]":
                    pass
            $ renpy.pause(0.5)
            stop soundloop fadeout 0.5
            play sound "fx/tableslap.wav"
            play sound2 "fx/snarl.ogg"
            $ bangok_four_anna2.annacame = True 
            show anna orgasm flip:
                ease 0.3 ypos 1.07
            with None
            $ renpy.pause(0.8)
            m "Abruptly, Anna thrust herself down hard enough to finally punch through the resistance. Her tail slapped the table as a few more inches of my arm disappeared inside of her. The pressure on my hand lessened and the undulating pressure on my arm mounted, a wider section now stuffed into her tight passage."
            $ renpy.pause(0.5)
            show anna lipbite flip with dissolve
            m "Anna remained there for several long moments, just catching her breath after the quiet roar and whatever she'd done."
            $ renpy.pause(0.8)
            menu:
                "Are you okay?":
                    $ renpy.pause (0.9)
                    $ anna2mood += 1
                    An smirk flip "Excellent, actually."
                "What just happened?":
                    $ renpy.pause (0.6)
                    An "I pushed your hand through my cervix."
                "Is my hand in your womb right now?":
                    $ renpy.pause (0.5)
                    An smirk flip "Yes. Yes it is."
            if bangok_four_playerhasdick == True:
                An "Most of my previous partners have been... larger than you are."
                An smirk flip "But your arm? Now that's something."
            An blush flip "This wouldn't be safe to do with any dragon. Not without a protective cover, because of the scales and sharp claws."
            An smirk flip "Now, though?"
            show anna orgasm flip:
                ease 1.5 ypos 1.1
            with None
            $ renpy.pause(1.5)
            show anna lipbite flip with dissolve
            m "Anna sank further down my arm now soaked with her juices, until she all but sat on my forearm. There was another resistance inside of her, one I assumed she wouldn't be trying to batter through."
            $ renpy.pause(1.5)
            An smirk flip "Well, I'm not going to do all the work here."
            c "I can't move my arm like this."
            An "I expected as much. Let me get back on the couch."
            show anna lipbite flip:
                ease 1.5 ypos 1.04
            with None
            $ renpy.pause(1.5)
            show anna orgasm flip:
                ease 0.25 ypos 1.07
            with None
            $ renpy.pause(0.8)
            show anna blush flip with dissolve
            m "Anna began to pick herself up, legs shuddering. She faltered when I felt her cervix close above my hand, her bodyweight falling back on that tight inner gate and punching me back through, though not all the way."
            menu:
                "[[Pull out.]":
                    show anna lipbite flip with dissolve
                    $ renpy.pause(2.0)
                    play sound "fx/uncork.ogg"
                    show anna blushpalm flip at Position(ypos=1.08) with ease
                    $ anna2mood += 1
                    An "Thanks."
                "[[Let her handle it.]":
                    show anna lipbite flip:
                        ease 1.5 ypos 1.04
                    with None
                    $ renpy.pause(1.5)
                    show anna lipbite flip:
                        ease 1.5 ypos 1.00
                    with None
                    $ renpy.pause(1.5)
                    play sound "fx/uncork.ogg"
            show anna at Position(xpos=0.75, ypos=1.0) with ease
            show anna at Position(xpos=0.8, ypos=1.0) with ease
            show anna blush with dissolve
            $ renpy.pause(0.3)
            show anna blush:
                pos (0.8, 1.3)
                rotate 15
            with dissolve
            m "Taking some faltering steps over to the couch, Anna fell back onto it. Her slit was still slightly open, glistening inside from her arousal."
            An smirk "Stick your arm back in."
            show anna lipbite with dissolve
            if bangok_four_anna2.fist == True:
                m "I obliged, reforming my fist (being careful to keep my fingernails in) and working it back into her. Once through her outer opening, it spread her walls, rubbing every which way until I reached her inner gate."
            else:
                m "I obliged, working my hand through her outer opening, then sliding the short distance through her passage to her inner gate."
            An smirk "Batter through."
            menu:
                "Just punch it?":
                    $ anna2mood += 1
                    An blush "How do you think I just did it?"
                    An smirk "I've done this a few times with big-dicked lovers. They're a lot less gentle than you try to be."
                    m "I drew back a little, then shoved."
                    show anna lipbite with dissolve
                    $ renpy.pause(0.3)
                    An "Harder. Obviously."
                    $ renpy.pause(0.8)
                    m "I tried again, pushing harder. Even with all the natural lubricant she'd spread on my arm, moving at speed was difficult with all the friction in her tight passage. Still, when I pressed up against her cervix, I felt a little spot of something different, and some small give."
                    An smirk "What's wrong? The weak human ambassador isn't strong enough?"
                    c "(That's it!)"
                    m "Adusting myself forward a little, I pulled my dragon-wrapped hand back, then pushed again, transferring the force between my shoulders to pull my arm up into her crotch. With the new angle, I was applying more force at her cervix."
                    show anna orgasm with dissolve
                    m "It spread around my hand like her outermost opening had."
                "I'll try pushing first...":
                    m "I leaned more of the weight of my upper body onto my arm, pressing on her gate."
                    An blush "Seriously, [player_name]. Repeated force is more effective than--"
                    show anna orgasm with dissolve
                    $ renpy.pause (0.4)
                    show anna blushpalm with dissolve
                    An "Nevermind."


            An lipbite "Well done. Now fuck me."
            m "I started moving, pushing my arm almost to the elbow, then pulling back out until her cervix was about to let go of me, popping my knuckles through."
            m "Anna writhed in ecstacy."
            $ renpy.pause(0.5)
            An "D-Do not stop!"
            m "I was about to ask why I would when her outer passage clamped down hard, the friction quadrupling. I could barely even manage to move. Not that it mattered, as one of her legs pulled me against her belly a moment later."
            show anna orgasm with dissolve
            show black with fadequick
            play sound "fx/snarl.ogg"
            $ bangok_four_anna2.annacame = True 
            m "Anna let out another muffled roar, shoving her own hand into her mouth to try to keep from being too loud."
            $ renpy.pause (0.8)
            hide black
            show anna lipbite 
            with dissolvemed
            m "After a long moment, Anna's canal relaxed its grip and she dropped her arms to her sides, releasing me."
            $ renpy.pause (0.5)
            An smirk "Holy fuckeroly. That... that was good. Twice in one night."
            menu:
                "You came earlier?":
                    $ renpy.pause (0.5)
                    An smirk "The first time you were through my cervix."
                "My turn, now?":
                    $ renpy.pause (0.6)
                    An smirk "Yes. Your turn."
                "Hey! What about me?":
                    $ anna2mood -= 1
                    An blush "Yes. Your turn."
            m "I withdrew my sopping wet arm from her now-loosened passage, considering my next move."
            jump bangok_four_anna2_apartment_startingmenu
        "Lick." if bangok_four_anna2.lick == True:
            $ anna2mood -= 1
            $ bangok_four_anna2.lick = False
            m "I knelt down next to Anna, bringing my face closer."
            An disgust "Hey!"
            m "I had to dodge back as she crossed her legs over her privates, nearly slashing me in the face as she blocked my path."
            An face "I agreed to sex, not just any kind."
            An sad "None of your mouth until I know more about what's in it."
            if anna2mood < 1:
                c "Are you going to use this as an excuse for anything I try to do?"
                An face "What do you think the condom is for?"
            m "I got back to my feet."
            jump bangok_four_anna2_apartment_startingmenu
        "Straight into her ass.":
            pass
        "Straight into her pussy.":
            if bangok_four_anna2.annacame == True:
                m "Anna's slit remained slightly parted after my arm-fucking, and like my arm still glistening with her arousal. I gave my dick a pump with the same arm I'd fucked her with, lubricating the condom, then got between her legs."
                m "As I slipped inside, I realized my gusto had spread her out to the point where there was disappointingly little resistance."
            else:
                if anna2mood > 2:
                    show anna blush with dissolve
                    m "Her slit was a thin glistening line. I got between her legs, aiming my condom-wrapped dick directly into it."
                    m "Entering her had disappointingly little resistance, her slit clearly meant to take larger partners."
                else:
                    show anna sad with dissolve
                    m "Her slit was a thin line, I got between her legs, aiming my condom-wrapped dick directly into it."
                    m "She tensed up, fighting my entry for a moment as I pressed all the way in. Once inside, though, the pressure disappeared, her passage clearly made for larger mates."
            m "I paused, hilted, as I felt her passage moving around me, muscles massaging my shaft like an all-around warm caress even if not squeezing tightly."
        "Wait, it's vertical?" if bangok_four_anna2.waitvert == True and bangok_four_malepartners > 0:
            $ bangok_four_anna2.waitvert = False
            An sad "Obviously."
            An face "Oh. You must have been with a male before me."
            An normal "That's one of the few gender dimorphisms we have, aside from voice, some eye structure, and the obvious difference in reproductive equipment."
            if anna2mood < 2:
                An sad "Now will we get on with this?"
            else:
                An smirk "Now, could you get on with this?"






label bangok_four_anna2_apartment_skip:
s "TODO: Out of content."
$ renpy.error("TODO: Out of content.")