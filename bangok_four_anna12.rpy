init python:
    bangok_four_anna1_discourseonmorphologicalvariations = True
    bangok_four_anna1_sexrequested = False

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
                $ annamood += 1
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
    play sound "fx/system3.wav"
    s "Uh oh! Looks like the author is running out of horny."
    $ renpy.error("TODO: 4o4 No horny found error")


label bangok_four_anna2_woods:
    $ renpy.error("TODO: bangok_four_anna2_woods. Also: Bloodsports? What are you thinking?!")