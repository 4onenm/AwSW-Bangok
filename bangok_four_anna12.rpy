init python:
    bangok_four_anna1_discourseonmorphologicalvariations = True
    bangok_four_anna1_sexrequested = False

init python in bangok_four_anna2:
    boughtcondoms = False
    havecondoms = False

    havestrapon = False

    havefauxcum = False

    waitvert = True
    finger = True
    lick = True

    position = None
    hornsgrabbed = None

    annacame = False

    tail = False

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

label bangok_four_anna1_medending:
    An normal flip "But you know what, this wasn't so bad after all. Maybe I'll let you have your sex."
label bangok_four_anna1_ending_merge:
    c "Really? I'm surprised you're okay with that."
    An normal flip "It's not unreasonable, and I certainly won't be letting you go back on your part of the bet."
    An sad flip "Why? Do you {i}not{/i} want to have sex with me?"
    menu:
        "I didn't say that.":
            An smirk flip "Then there's no problem."
            An normal flip "I won't have a spot in the facility to do the tests for a while, though, so I suppose next time we meet, it'll be for sex."
        "Humans have this saying, \"dinner and a movie...\"":
            $ bangok_four_anna1_sexrequested = False
            An normal flip "Fine. Then we can scale your end of the bet back to just a date."
            An smirk flip "Unless things go really well."
            c "That sounds fair to me."
            An normal flip "I won't have a spot in the facility to do the tests for a while, though, so I suppose next time we meet, it'll be for that date."
        "I kinda said it to get back at you for being rude.":
            $ bangok_four_anna1_sexrequested = False
            $ annamood -= 2
            An face flip "I can't believe this."
            c "Look, I'm sorry. What if we, I don't know, went to see a movie instead?"
            An sad flip "What, like a date?"
            An face flip "I seriously hope you're not abruptly trying to twist this into something longer-term."
            $ renpy.pause(0.8)
            An normal flip "Fine. I won't have a spot in the facility to do the tests for a while, so I suppose next time we meet, it'll be for this date of yours."
    c "Sure."
    if annaanswers == 3:
        jump bangok_four_anna1_goodending_after_thankyou
    else:
        jump bangok_four_anna1_medending_uptoyou

label bangok_four_anna1_goodending_nvl:
    n "Even though my bet of forcing her to have sex with me with me was more to get back at her for her earlier rudeness, I had not expected this outcome. I was not even sure what I expected from this meeting in the first place, but now I was locked into sex with her and being her own, personal guinea pig."
    if bangok_four_malepartners + bangok_four_femalepartners < 1:
        n "I hadn't tried anything with a dragon before. Would I even be able to get it up when the time came?"
    else:
        n "I had bed a dragon before, but Anna seemed like a whole new experience."
    jump bangok_four_anna1_goodending_nvl_end

label bangok_four_anna1_medending_nvl:
    n "After all, proposing a sex was my way of sticking it to her for being rude."
    n "Even though I lost the bet, she didn't seem to mind having sex with me, as long as she got what she wanted. Whether I would follow up on it was up to me, though."
    if bangok_four_malepartners + bangok_four_femalepartners < 1:
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
    if bangok_four_playerhasdick == True:
        m "Remembering my arrangement with Anna, I realized I should probably get some protection. I was dealing with an entirely different species, after all."
    else:
        m "Remembering my arrangement with Anna, an intrusive thought popped into my head about her tail."
    menu:
        "Get condoms.":
            $ bangok_four_anna2.boughtcondoms = True
            "I picked up one of the boxes of smaller sizes, labeled for runners, to purchase."
            c "(Hope this doesn't seem too strange to the store clerk.)"
        "Don't.":
            $ bangok_four_anna2.boughtcondoms = False
            c "(They probably have some in the apartment somewhere. Or we won't need them.)"
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
            $ renpy.pause(0.5)
            $ anna2mood -= 1
            An face "Because it's virtually guaranteed we'll break something."
            An sad "Not to mention the sanitary issues."
            c "Alright, alright. My place it is."
            if anna2mood >= 0 and persistent.bangok_dev == True:
                An normal "That said, I would like to get something I stashed in my lab for this."
        "Sure.":
            $ renpy.pause(0.5)
            $ anna2mood += 1
            if anna2mood >= 0 and persistent.bangok_dev == True:
                An smirk "Ah, almost forgot. I left something in my lab for this."
        "All that waiting left me kinda hungry...":
            $ renpy.pause(0.5)
            An face "Was that supposed to be an \"eating out\" joke? Because I have bad news for you."
            menu:
                "That's exactly what it was.":
                    $ renpy.pause(0.5)
                    c "What do you mean by bad news?"
                    An normal "I don't like dental dams. And you, in particular, aren't putting your mouth on my genitals without one."
                    c "Oh."
                    An "Forget about it. Let's go do this."
                    if anna2mood >= 0 and persistent.bangok_dev == True:
                        An face "Oh, damnit. Almost forgot. I put something in my lab for this."
                "No, I meant that literally.":
                    An sad "What do you expect me to do about that, magic up food for you?"
                    c "It's not that crazy to go out for dinner, especially since I assume you haven't eaten either."
                    An "Fine. Maybe the coffee place is still open. I don't know."
                    jump bangok_four_anna2_alley

    if anna2mood >= 0 and persistent.bangok_dev == True:
        c "Oh?"
        hide anna with dissolve
        play sound "fx/door/door_open.wav"
        $ renpy.pause (3.0)
        show anna normal with dissolve
        m "She returned with a leather hand-satchel, closing the lab door behind herself."
        $ bangok_four_anna2.havestrapon = True
        menu:
            "What's in that?":
                $ renpy.pause(0.5)
                $ anna2mood += 1
                An smirk "I'll show you in private."
            "Ready?":
                $ renpy.pause(0.5)
                An normal "Yes."
            "Is that your purse?":
                $ renpy.pause(0.5)
                $ anna2mood -= 1
                c "Does the big famous scientist carry around a little lady purse?"
                An sad "It's not a purse."
                c "Then what's in it?"
                An normal "Keep making annoying comments like that and maybe I won't show you."

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

    if bangok_four_anna2.havestrapon == True:
        $ renpy.pause(0.5)
        c "So. What's in the bag?"
        show anna smirk with dissolve
        play sound "fx/undress.ogg"
        show anna smirk dildohand with dissolve

        $ renpy.pause(0.8)

        menu:
            "Is that a double-ended dildo?":
                $ renpy.pause(0.5)
                c "What's all that extra strapping for?"
            "Is that a strapon?":
                $ renpy.pause(0.5)
                An smirk dildohand "It is."
            "Oh my.":
                $ renpy.pause(0.5)
            "No.":
                $ renpy.pause(0.5)
                show anna sad dildohand with dissolve
                c "Whatever that is, we're not using it."
                label bangok_four_anna2_apartment_nostrapon:
                An sad dildohand "I see. Would you mind telling me why?"
                menu:
                    "Not my thing.":
                        $ renpy.pause(0.5)
                        An normal dildohand "Fair enough."
                        play sound "fx/undress.ogg"
                        show anna normal with dissolve
                    "It's huge!":
                        $ renpy.pause(0.5)
                        An sad dildohand "The larger end wouldn't be going in {i}you{/i}."
                        c "Even still."
                        An normal dildohand "Fair enough."
                        play sound "fx/undress.ogg"
                        show anna normal with dissolve
                    "Why did you go and make this weird?":
                        $ renpy.pause(0.5)
                        $ anna2mood -= 1
                        play sound "fx/undress.ogg"
                        An face "Fine, I'll put it away."
                    "No.":
                        $ renpy.pause(0.5)
                        $ anna2mood -= 1
                        play sound "fx/undress.ogg"
                        An face "Fine, I'll put it away."

                m "Anna put the toy away in the satchel and set it aside."
                $ bangok_four_anna2.havestrapon = False
                jump bangok_four_anna2_apartment_under_layers

        An normal dildohand "I bought this to use with an ex, but I never could talk him into it."
        An smirk dildohand "It's intended to be used as a strapon for pegging, but there's a few other ways I'm sure we could use it."
        menu:
            "Sounds like fun.":
                $ renpy.pause(0.5)
                $ anna2mood += 1
            "I... guess we could try it.":
                $ renpy.pause(0.5)
            "I'm not sure about that thing.":
                $ renpy.pause(0.5)
                jump bangok_four_anna2_apartment_nostrapon
            "Okay, no way.":
                $ renpy.pause(0.5)
                $ anna2mood -= 1
                jump bangok_four_anna2_apartment_nostrapon
        show anna normal with dissolve
        m "Anna set the toy aside on the coffee table."

    label bangok_four_anna2_apartment_under_layers:
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
                $ bangok_four_playerhasdick = False

    play sound "fx/undress.ogg"
    $ renpy.pause (1.5)

    if bangok_four_playerhasdick == True:
        label bangok_four_anna2_apartment_maleshow:
        An normal "Definitely a mammal. Definitely a male."
        menu:
            "Actually, I prefer a different set of pronouns...":
                An "Fine. We don't need pronouns to use that thing of yours."
            "[[Say nothing.]":
                pass

        if bangok_four_anna1_sexrequested == True:
            An "Now, you did buy condoms for the occasion, right?"
            menu:
                "Wait, why?":
                    c "We're different species. I'm pretty sure I can't get you pregnant."
                    An sad "Until I have a chance to go over your genital biofauna in a lab, I'd rather not discover the hard way your species has some kind of dragon-compatible bacteria that becomes an STD."
                    c "Ah. Fair enough."
                "Of course." if bangok_four_anna2.boughtcondoms == True:
                    pass
                "Uh..." if bangok_four_anna2.boughtcondoms == False:
                    pass
            if bangok_four_anna2.boughtcondoms == True:
                $ bangok_four_anna2.havecondoms = True
                show anna normal with dissolve
                c "Of course I got some."
                m "I retrieved the box I'd purchased during my visit to the store, removing one small foil-wrapped barrier device."
            else:
                c "Uh..."
                An face "Oh for crying out loud."
                menu:
                    "You didn't bring any in your bag?" if bangok_four_anna2.havestrapon == True:
                        $ renpy.pause(0.5)
                        $ bangok_four_anna2.havecondoms = True
                        An normal "I did, but I assumed you'd do some shopping around to determine what's safe for you to use."
                        c "Oh. Well, how hard is it to make a safe condom? I'm sure it'll be fine."
                        An "Your choice."
                        m "She handed one over."
                    "I thought you would bring something.":
                        $ renpy.pause(0.5)
                        c "I'm the visitor from another world, after all."
                        An sad "That's why it was your responsibility to pick one that's safe for you."
                        c "Let's look around. I'm sure some are stocked."
                    "I thought this place would be stocked.":
                        $ renpy.pause(0.5)
                        c "It's had everything else I've needed."
                        An "And did you look for them?"
                        c "..."
                        An "I see."
                    "Let's look around. I'm sure some are stocked.":
                        $ renpy.pause(0.5)
        else:
            An face "Damnit."
            c "What?"
            An sad "I didn't expect to do anything like this, so I didn't bring any condoms."
            An normal "And before you ask, no, I won't be having sex outside my phylogenic group without one."
            An normal "Until I have a chance to go over your biofauna in a lab, I'd rather not discover the hard way your species has some kind of dragon-compatible bacteria that becomes an STD."
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


        if bangok_four_anna2.havestrapon == True:
            An smirk dildohand "Or do you want to be receiving first?"
    else:
        An normal "Definitely a mammal. I'm guessing female, as I'm sure as a male your dick would already be visible at the prospect of sex."
        menu:
            "Actually, I prefer a different set of pronouns...":
                An "Fine. We don't need pronouns to enjoy what you have attached to you."
            "[[Say nothing.]":
                pass

        if bangok_four_anna2.havestrapon == False:
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
                    hide black with dissolveslow
                    jump bangok_four_anna2_apartment_done
                "No. Don't skip ahead.":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                    hide black with dissolvemed
                    jump bangok_four_anna2_apartment_maleshow

        An normal "Well, I doubt the strapon's strapping will work with your pelvic structure."
        An smirk dildohand "I suppose that means you'll have to be receiving."



    if bangok_four_anna2.havestrapon == True:
        label bangok_four_anna2_apartment_strapon_consideringmenu:
        menu:
            "I think I'd like that.":
                $ renpy.pause(0.5)
                $ bangok_four_anna2.position == "strapon"
                An bangok blush "Excellent."
            "I can try, I guess.":
                $ renpy.pause(0.5)
                $ bangok_four_anna2.position = "strapon"
                An bangok blush "Excellent."
            "How about we just use it as a dildo?":
                $ renpy.pause(0.5)
                $ bangok_four_anna2.position = "dildo"
                c "I'm not so sure about having that inside me, but it sounds like you want to use it."
                An bangok blush "I can work with that."
            "I'm actually not so sure about using that now...":
                $ renpy.pause(0.5)
                $ anna2mood -= 1
                An face "Oh for--"
                An normal "Fine."
                if bangok_four_playerhasdick == False:
                    jump bangok_four_anna2_apartment_nodick
                jump bangok_four_anna2_apartment_annaliesdown

        
        An bangok blush "There's another fun feature this has, if you're interested. Faux cum."
        if bangok_four_anna2.position == "strapon":
            c "For in me or for in you?"
            An "No reason it can't be both. It comes in a powder form, so we can make basically as much as we want. It's also configurable, so we can choose later who gets the load."
            An smirk "Even while inside people."
        c "I see."

        An normal dildohand "I should go fill the faux cum now if we're going to use it later."
        menu:
            "Let's not.":
                $ renpy.pause(0.5)
                $ bangok_four_anna2.havefauxcum = False
                c "I'm not sure I want to play with that. Plus, what's the cleanup like?"
                An "Fair enough."
            "Sure.":
                $ renpy.pause(0.5)
                $ bangok_four_anna2.havefauxcum = True
                show anna normal with dissolve
                play sound "fx/rummage.ogg"
                $ renpy.pause(0.8)
                stop sound fadeout 1.0
                $ renpy.pause(0.8)
                hide anna with dissolve
                m "Anna rummaged through the satchel, grabbing a large bladder, thin hose, and a couple unmarked packets.{w=0.3} Then she disappeared into the bathroom."
                $ renpy.pause(0.5)
                play soundloop "fx/faucet1.ogg"
                queue soundloop "fx/faucet2.ogg"
                $ renpy.pause(1.0)
                menu:
                    "How much are you making?":
                        $ renpy.pause(0.5)
                        An normal "A fun amount."
                    "[[Wait.]":
                        pass
                $ renpy.pause(1.0)
                stop soundloop fadeout 0.5
                show anna bangok blush with dissolve
                An bangok blush "Shall we?"



label bangok_four_anna2_apartment_annaliesdown:
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
    m "Anna stepped back up to the couch, then sat back, swinging her tail between her legs to sit on it, exposing her underside."
    m "Now in this position, I could clearly make out her single vertical slit, hidden on a slight mound between her legs."
    if persistent.bangok_cloacas == False:
        m "A small rosebud winked up at me from an inch or two further down."
    $ bangok_four_femalepartners += 1

    if bangok_four_anna2.havestrapon == False:
        jump bangok_four_anna2_apartment_male_nostrapon_startingmenu
    else:
        An normal "Do you want to put a condom on it first? I have a few for fitting its larger end in my bag."
        c "Why?"
        An bangok blush "In case you want to cum through it, if you're feeling inadequate about your size."
        if persistent.bangok_watersports == True:
            An smirk "Or play with other fluids."
        An normal "Changes basically nothing about the feel of it, so I don't care either way. We just aren't playing with your output without a barrier."
        # The player has put his personal condom on already if he's male, so reusing this variable is fine.
        menu:
            "Put a condom on the toy.":
                $ bangok_four_anna2.havecondoms = True
            "Don't.":
                $ bangok_four_anna2.havecondoms = False

    show anna bangok blush with dissolve
    m "Anna spread her legs a little wider as I approached with the toy."
    An "Now, get me ready with your fingers. But watch your claws. I don't want you to cut me in there."
    menu:
        "I doubt that will be a problem.":
            c "Unless you're way more delicate than a human in there..."
            An normal "Unlikely. Still, don't do anything too stupid."
        "Do you want it lubed first?":
            An normal "I didn't bring any, and I didn't see any in your restroom."
            c "Oh."
        "Pussy or your ass?":
            An "Vagina. Let's not regress to slang terminology around here."
            An bangok blush "And I'm sorry to say it doesn't fit in my anus without lube, which I didn't bring, nor did I see in your restroom."
            c "Oh."
    
    $ bangok_four_anna2.finger = False
    m "I stepped in closer, reaching out to caress her opening."
    m "After a few moments, I slowly pressed two fingers inside, continuing my small, gentle circles with the rest of my hand. Anna's legs shuddered slightly, where they were sticking up in the air."
    $ renpy.pause (0.8)
    if anna2mood > -1:
        An smirk "You can keep going with that."
    else:
        show anna sad with dissolve
    $ renpy.pause (0.5)
    m "After giving her another moment with this gentle teasing, I added a third finger, finding it slipping in even more easily than the first two as her natural lubrication began to slicken her lips."
    if anna2mood < 1:
        An face "Okay, stop."
        c "Huh? I thought you liked this."
        An sad "Just move on to the strapon."
    else:
        An smirk "You were right. Your claws aren't a problem."
        An bangok blush "And your skin is much softer than any dragon's scales."
        menu:
            "[[Add a fourth finger.]":
                m "This finger resisted slightly more. But with her natural lubrication it fit, followed by most of my palm."
                $ anna2mood += 1
                An bangok lipbite "Mm."
                c "Keep going with this?"
                if anna2mood > 2:
                    $ renpy.pause(0.5)
                    An "Yes."
                    m "Gently, I worked my hand in and out, drawing Anna's breath slightly faster with each motion."
                    $ renpy.pause(0.8)
                    An bangok lipbite "Mm. Now you're in for it."
                    c "Huh?"
                    call bangok_four_anna2_apartment_yourarm from bangok_four_anna2_apartment_strapon_fourthfinger
                else:
                    An bangok blush "Let's move on to getting the strapon in."
            "[[Move on to the strapon.]":
                pass

    m "Taking the toy from the coffee table, I spread some of her wetness from my fingers to the tip of the larger end."
    if bangok_four_anna2.position == "dildo":
        c "You're sure you can take this larger end?"
        An bangok blush "I have plenty of practice in my free time. I can't see why that would have changed."
        if bangok_four_anna2.annacame == True:
            An smirk "Especially after you stretched me out that much."

    if bangok_four_anna2.annacame == True:
        m "Anna's slit remained slightly parted after my arm-fucking, and like my arm still glistened with her arousal."
        if bangok_four_anna2.position == "dildo":
            m "Sliding off the strapping meant to keep it in her and leaving just the double-ended shaft, I fit the tip of the larger end of the toy to her lips."
        else:
            m "Holding the strapping meant to keep it in her out of the way, I fit the tip of the larger end of the toy to her lips."
        show anna bangok lipbite with dissolve
        m "It slid in smoothly, despite the fact I could see it stretching her almost as much as my arm had."
        show anna bangok orgasm with dissolve
        m "Anna gasped as her resistance to the intrusion abruptly increased, though not quite to the point of body-shuddering shake I'd observed before. Then the shaft was through her inner gate, her outer lips wrapping around where the toy decreased in width. My fingers brushed against her filled slit as I held the toy steady."
        c "Did you get off on just it going in?"
        An bangok lipbite "N-Not quite. But it won't take me long."
    else:
        m "Anna's slit glistened with arousal from my finger-fucking."
        if bangok_four_anna2.position == "dildo":
            m "Sliding off the strapping meant to keep it in her and leaving just the double-ended shaft, I fit the tip of the larger end of the toy to her lips."
        else:
            m "Holding the strapping meant to keep it in her out of the way, I fit the tip of the larger end of the toy to her lips."
        show anna bangok lipbite with dissolve
        m "It speared her open wide, taking a bit of force to slide, but Anna seemed only further aroused by stretching to accomodate it."
        m "Even still, she ran out of lubrication around the halfway point on the toy's larger end, her scaly lips tugging inward with it as I failed to slide it any deeper."
        An bangok blush "In and out. Obviously."
        c "You're completely {i}sure{/i} this thing fits in you?"
        An normal "Would I be asking you to put it in me if I thought it didn't?"
        An bangok blush "Just pump it."

        m "Doing as she'd asked, I slid the toy back out until the tip tugged past her lips. It was almost dripping with her wet, dollops running down the head to slick her lips."
        An bangok lipbite "And back in..."
        m "I pushed it back inside her, watching with fascination as the slickness on her lips spread further up the toy, from her tightness."
        m "The toy stopped abruptly with three quarters of the larger end inside her, and not because she was out of lubrication."
        An "Keep going."
        menu:
            "What's stopping it?":
                pass
            "If you're out of room, Anna, you're out of room!":
                $ anna2mood -= 1
            "If you say so...":
                $ renpy.pause(0.5)
                m "I leaned more weight on the toy, assuming it would give with just a little more pressure. It didn't seem to."
        $ renpy.pause(0.5)
        An bangok blushpalm "Oh for fuck's sake."
        show anna bangok lipbite with dissolve
        m "Taking my wrist, she pushed back against the toy, indicating I should pull it out of her."
        m "Then she reversed her tug, stopping me."
        An bangok lipbite "Now shove in. Hard."
        menu:
            "Didn't you want me to not hurt you in there?":
                $ renpy.pause(0.5)
                $ anna2mood -= 1
                An bangok blushpalm "I'll be fine. For crying out loud, fuck me with it already!"
            "[[Obey.]":
                pass
        $ renpy.pause(0.5)
        m "I shoved the toy in, hard, up to the resistance inside of her, but still hesitated."
        An bangok blushpalm "Again. Follow through!"
        m "Withdrawing a little, I shoved at the resistance again."
        show anna bangok orgasm with dissolve
        m "I wasn't sure if it was my imagination, but the toy felt about half the length of the tip further inside."
        show anna bangok lipbite with dissolve
        An "Deeper. Come on, [player_name]."
        m "Taking her words as encouragement, I tugged the toy back slightly and pushed inside over again, all-but leaning my bodyweight on it."
        An bangok blushpalm "C-Closer."
        show anna bangok lipbite:
            ease 0.8 xpos 0.8
            ease 0.15 xpos 0.81
            repeat
        with None
        m "I pulled and pushed another time, then again. The toy sank ever-so-slightly deeper, but it apparently still wasn't enough for the insatiable dragonness."
        $ renpy.pause(0.8)
        play sound "fx/tableslap.wav"
        play sound2 "fx/snarl.ogg"
        $ bangok_four_anna2.annacame = True 
        show anna bangok orgasm:
            xpos 0.8
        with hpunch
        m "Then, abruptly, the toy kept sinking inside and Anna became a snarling, shuddering mess, her tail slapping the table."
        m "I almost let go from my surprise, but I kept my grip as I held her legs apart, trying to keep the dangerous-looking claws on her feet away from my body."
        show anna smirk with dissolve
        $ renpy.pause(0.5)
        m "Anna came down from her orgasm with a grin."
        $ renpy.pause(0.5)
        An "Finally. So hard to get that force when I'm on my own."
        menu:
            "Are you okay?":
                $ renpy.pause (0.9)
                $ anna2mood += 1
                An smirk flip "Excellent, actually."
            "What just happened?":
                $ renpy.pause (0.6)
                An "You finally worked that toy through my cervix."
            "Is that toy sticking into your womb right now?":
                $ renpy.pause (0.5)
                An smirk flip "Yes. Yes it is."
        An bangok blush "I tend toward larger partners. Why do you think that strapon is so big?"
        An normal "Technically it's designed to be worn the other way, for someone my size to please a quadrupedal dragon. But it was trivial enough to make it reversible."
        show anna bangok lipbite with dissolve
        m "She tugged on my hand, bringing the toy just a little deeper, until her outer lips wrapped around where the toy decreased in width. My fingers brushed against her filled slit as I held the toy steady."

    if bangok_four_anna2.position == "dildo":
        m "With it up inside her, it looked a little like I was holding onto a penis emerging from her slit, apart from it being a grey, flexible material"
        An smirk "I think I could use getting off one more time."
    else:
        m "With it up inside her, it looked a little like I was holding onto a penis emerging from her slit, apart from it being a grey, flexible material and ringed by the straps that would hold it in place."

    play sound "fx/system3.wav"
    s "Out of content. Load a save or prepare to crash."
    $ renpy.error("TODO: ")


label bangok_four_anna2_apartment_male_nostrapon_startingmenu:
    menu:
        "[[Finger her.]" if bangok_four_anna2.finger == True:
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
            m "After giving her another moment with this gentle teasing, I added a third finger, finding it slipping in even more easily than the first two as her natural lubrication began to slicken her lips."
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
                            jump bangok_four_anna2_apartment_male_nostrapon_startingmenu
                    "If you insist.":
                        jump bangok_four_anna2_apartment_male_nostrapon_startingmenu
            else:
                An smirk "You were right. Your claws aren't a problem."
                An bangok blush "And your skin is much softer than any dragon's scales."
                menu:
                    "[[Add a fourth finger.]":
                        m "This finger resisted slightly more. But with her natural lubrication it fit, followed by most of my palm."
                        $ anna2mood += 1
                        An bangok lipbite "Mm. Now you're in for it."
                        c "Huh?"
                    "[[Move on to something else.]":
                        show anna sad with dissolve
                        $ renpy.pause(0.3)
                        show anna normal with dissolve
                        m "Anna's folds tugged at my fingers as I withdrew, but she made no comment on my decision."
                        jump bangok_four_anna2_apartment_male_nostrapon_startingmenu

            call bangok_four_anna2_apartment_yourarm from bangok_four_anna2_apartment_male_nostrapon_startingmenu_finger
            jump bangok_four_anna2_apartment_male_nostrapon_startingmenu

            label bangok_four_anna2_apartment_yourarm:
            An smirk "I want your arm. Let's see what the rest of that soft flesh feels like."
            menu:
                "What, like, detached from my body?":
                    c "I'd like to keep my arms, thanks."
                    An bangok blush "Fine, you can have it back."
                    An smirk "But first I want it as deep inside me as you can push it."
                    c "O-Oh."
                "No way." if bangok_four_anna2.position not in ["dildo","strapon"]:
                    $ anna2mood -= 2
                    c "I was just exploring. I didn't think you'd..."
                    show anna sad with dissolve
                    $ renpy.pause(1.2)
                    An bangok blushpalm "Seriously?"
                    An sad "Fine. Take your hand out and fuck me, if that's all you want."
                    return
                "I'd rather move on to the strapon." if bangok_four_anna2.position in ["dildo","strapon"]:
                    $ anna2mood -= 1
                    c "I was just exploring. I didn't think you'd..."
                    show anna sad with dissolve
                    $ renpy.pause(1.2)
                    An bangok blushpalm "Seriously?"
                    An sad "Fine. Take your hand out stick the strapon in, if that's all you want."
                    return
                "Okay.":
                    An smirk "Good little human."

            show anna bangok blush with dissolve
            m "I slid in and out the four fingers I had so far, getting her used to the size until my hand was soaked and buried right up to the base of my thumb."
            $ renpy.pause(0.5)
            c "You're sure?"
            An bangok blushpalm "Would I be asking you to do it if I wasn't?"
            m "I pulled back out to the tips of my fingers, then folded my thumb into my palm and pressed my whole hand inside of her."
            An bangok lipbite "Ngh..."
            m "Her slit clenched around my wrist, insides undulating as they milked my hand for a substance it could not provide."
            c "You okay?"
            An bangok blush "Could you stop asking me that and push deeper already?"
            c "What should I do when I do run out of room?"
            An bangok blushpalm "I'll tell you when you get there."
            show anna bangok blush with dissolve
            m "Heeding her instructions, I sank more of my arm inside of her. Very quickly, the section that had been lubricated by her fluids thus far ended, and resistance to my force increased dramatically."
            An bangok blushpalm "Should've thought about lube."
            An bangok blush "Doesn't matter. Pull out."
            show anna bangok lipbite with dissolve
            m "I did so, retrieving the small part of my wrist and entirety of my hand I'd gotten in. Anna bit her lip the whole way out, then sighed with relief."
            hide anna with None
            $ renpy.pause(0.0)
            show anna bangok blush at Position(xpos=0.8,ypos=1.0, xanchor='center')
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
            show anna bangok blush flip at Position(xpos=0.7) with dissolve
            m "Then she turned around and lined her slick slit back up, one of her legs coming down right in front of me."
            $ renpy.pause(0.3)
            show anna bangok lipbite flip at Position(xpos=0.7,ypos=1.02) with ease
            An "Nnh!"
            m "The muscles in Anna's passage pressed in lewdly around my hand, squeezing more of her natural lubricant around my wrist and sending it running in small rivulets down my arm."
            $ renpy.pause (0.4)
            An bangok blush flip "Spread that around."
            m "I did as ordered, trying to more evenly distribute her juices on the next part of my arm. Anna shivered as the fingers of my other hand brushed her slit."
            An smirk flip "You're still braced against the table, right?"
            c "Yeah."
            An bangok blush flip "Good."
            show anna bangok lipbite flip at Position(xpos=0.7,ypos=1.0) with ease
            show anna bangok lipbite flip at Position(xpos=0.7,ypos=1.04) with ease
            m "Anna lifted herself up, her clenching almost tugging my arm with her. Just before my fingers were about to leave, she reversed direction and pressed back down, fucking herself onto my hand as if it were a dildo."
            An "Ah!"
            if persistent.bangok_cervpen:
                m "We came up against resistance almost immediately, but this one came from within her."
                show anna smirk flip with dissolve
                m "A glance back from her showed in her face. Whatever this felt like for her, it was a good feeling."
            else:
                show anna smirk flip with dissolve
                m "She clenched up intentionally, bringing herself to a stop partway down and squeezing my arm and hand tightly."
                c "(I wonder if I can make things even more interesting for her...)"
            menu:
                "[[Form a fist.]":
                    $ anna2mood += 1
                    $ renpy.pause (0.5)
                    An sad flip "What are you...?"
                    m "Shifting around me, Anna felt the additional room I'd bought her to take my arm."
                    An bangok blush flip "Hm."
                    show anna bangok lipbite flip:
                        ease 1.0 ypos 1.02
                    with None
                    m "She lifted up, walls shifting and spreading around the ball of my fist inside her."
                    m "Then she switched direction, pressing down fast."
                    show anna bangok lipbite flip:
                        ease 0.4 ypos 1.06
                    with None
                    c "Anna, w-wait--"
                    show anna bangok orgasm flip with dissolve
                    An "F-Fuck! Yes!"
                    m "I froze."
                    c "(Yes?)"
                    show anna bangok lipbite flip with dissolve
                    $ bangok_four_anna2.position = "fist"
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
            show anna bangok lipbite flip with dissolve
            if persistent.bangok_cervpen:
                m "Each time, she thrust my hand against the resistance inside of her harder."
            else:
                m "Each time, she thrust my hand a little deeper inside of her, squeezing tighter as more of her juices dribbled down my arm."
            An "A-Almost..."
            menu:
                "Anna, don't hurt yourself!":
                    $ anna2mood += 1
                    An "I've gone far harder than this."
                "Hey, don't break my hand!":
                    $ anna2mood -= 1
                    An bangok blushpalm flip "Are... you humans... really... so fragile...?"
                    show anna bangok lipbite flip with dissolve
                "[[Say nothing.]":
                    pass
            $ renpy.pause(0.5)
            stop soundloop fadeout 0.5
            play sound "fx/tableslap.wav"
            play sound2 "fx/snarl.ogg"
            $ bangok_four_anna2.annacame = True 
            show anna bangok orgasm flip:
                ease 0.3 ypos 1.07
            with None
            $ renpy.pause(0.8)
            if persistent.bangok_cervpen:
                m "Abruptly, Anna thrust herself down hard enough to finally punch through the resistance. Her tail slapped the table as a few more inches of my arm disappeared inside of her. The pressure on my hand lessened and the undulating pressure on my arm mounted, a wider section now stuffed into her tight passage."
            else:
                m "Abruptly, Anna thrust herself all the way down. I gasped, feeling the tight grip of her outer lips almost down to my elbow. The undulating pressure on my arm mounted and spasmed, a wider section now stuffed into her deep, tight passage."
            $ renpy.pause(0.5)
            show anna bangok lipbite flip with dissolve
            m "Anna remained there for several long moments, just catching her breath after the quiet roar and whatever she'd done."
            $ renpy.pause(0.8)
            menu:
                "Are you okay?":
                    $ renpy.pause (0.9)
                    $ anna2mood += 1
                    An smirk flip "Excellent, actually."
                "What just happened?":
                    $ renpy.pause (0.6)
                    if persistent.bangok_cervpen:
                        An "I pushed your hand through my cervix."
                    else:
                        An "I took your arm, like I said I would."
                "Is my hand in your womb right now?" if persistent.bangok_cervpen:
                    $ renpy.pause (0.5)
                    An smirk flip "Yes. Yes it is."
            if bangok_four_playerhasdick == True:
                An "Most of my previous partners have been... larger than you are."
                An smirk flip "But your arm? Now that's something."
            An bangok blush flip "This wouldn't be safe to do with any dragon. Not without a protective cover, because of the scales and sharp claws."
            An smirk flip "Now, though?"
            show anna bangok orgasm flip:
                ease 1.5 ypos 1.1
            with None
            $ renpy.pause(1.5)
            show anna bangok lipbite flip with dissolve
            if persistent.bangok_cervpen:
                m "Anna sank further down my arm now soaked with her juices, until she all but sat on my forearm. There was another resistance inside of her, one I assumed she wouldn't be trying to batter through."
            else:
                m "Anna sank further down my arm now soaked with her juices, until she all but sat on my forearm. There was a resistance deep inside of her, one I assumed she wouldn't be trying to play with."
            $ renpy.pause(1.5)
            An smirk flip "Well, I'm not going to do all the work here."
            c "I can't move my arm like this."
            An "I expected as much. Let me get back on the couch."
            show anna bangok lipbite flip:
                ease 1.5 ypos 1.04
            with None
            $ renpy.pause(1.5)
            show anna bangok orgasm flip:
                ease 0.25 ypos 1.07
            with None
            $ renpy.pause(0.8)
            show anna bangok blush flip with dissolve
            if persistent.bangok_cervpen:
                m "Anna began to pick herself up, legs shuddering. She faltered when I felt her cervix close above my hand, her bodyweight falling back on that tight inner gate and punching me back through, though not all the way."
            else:
                m "Anna began to pick herself up, legs shuddering. She faltered most of the way up, her bodyweight falling back on my arm as she clamped down, and let out a small gasp."
            menu:
                "[[Pull out.]":
                    show anna bangok lipbite flip with dissolve
                    $ renpy.pause(2.0)
                    play sound "fx/uncork.ogg"
                    show anna bangok blushpalm flip at Position(ypos=1.08) with ease
                    $ anna2mood += 1
                    An "Thanks."
                "[[Let her handle it.]":
                    show anna bangok lipbite flip:
                        ease 1.5 ypos 1.04
                    with None
                    $ renpy.pause(1.5)
                    show anna bangok lipbite flip:
                        ease 1.5 ypos 1.00
                    with None
                    $ renpy.pause(1.5)
                    play sound "fx/uncork.ogg"
            show anna at Position(xpos=0.75, ypos=1.0) with ease
            show anna at Position(xpos=0.8, ypos=1.0) with ease
            show anna bangok blush with dissolve
            $ renpy.pause(0.3)
            show anna bangok blush:
                pos (0.8, 1.3)
                rotate 15
            with dissolve
            m "Taking some faltering steps over to the couch, Anna fell back onto it. Her slit was still slightly open, glistening inside from her arousal."
            An smirk "Stick your arm back in."
            show anna bangok lipbite with dissolve
            if persistent.bangok_cervpen:
                if bangok_four_anna2.position == "fist":
                    m "I obliged, reforming my fist (being careful to keep my fingernails in) and working it back into her. Once through her outer opening, it spread her walls, rubbing every which way until I reached her inner gate."
                else:
                    m "I obliged, working my hand through her outer opening, then sliding the short distance through her passage to her inner gate."
            else:
                if bangok_four_anna2.position == "fist":
                    m "I obliged, reforming my fist (being careful to keep my fingernails in) and working it back into her. Once through her outer opening, it spread her walls, rubbing every which way until she clenched down to stop my progress."
                else:
                    m "I obliged, working my hand through her outer opening, then sliding deeper until she clenched down to stop my progress."

            An smirk "Batter through."
            menu:
                "Are you sure that's safe?":
                    $ anna2mood -= 1
                    jump bangok_four_anna2_finger_punch
                "Just punch it?":
                    label bangok_four_anna2_finger_punch:
                    $ anna2mood += 1
                    An bangok blush "How do you think I just did it?"
                    An smirk "I've done this a few times with big-dicked lovers. They're a lot less gentle than you try to be."
                    m "I drew back a little, then shoved."
                    show anna bangok lipbite with dissolve
                    $ renpy.pause(0.3)
                    An "Harder. Obviously."
                    $ renpy.pause(0.8)
                    if persistent.bangok_cervpen:
                        m "I tried again, pushing harder. Even with all the natural lubricant she'd spread on my arm, moving at speed was difficult with all the friction in her tight passage. Still, when I pressed up against her cervix, I felt a little spot of something different, and some small give."
                    else:
                        m "I tried again, pushing harder. Even with all the natural lubricant she'd spread on my arm, moving at speed was difficult with all the friction in her tight passage. Still, when I lined up just right, there was a way to slip deeper."
                    An smirk "What's wrong? The weak human ambassador isn't strong enough?"
                    c "(That's it!)"
                    if persistent.bangok_cervpen:
                        m "Adusting myself forward a little, I pulled my dragon-wrapped hand back, then pushed again, transferring the force between my shoulders to pull my arm up into her crotch. With the new angle, I was applying more force at her cervix."
                        show anna bangok orgasm with dissolve
                        m "It spread around my hand like her outermost opening had."
                    else:
                        m "Adusting myself forward a little, I pulled my dragon-wrapped hand back, then pushed again, transferring the force between my shoulders to pull my arm up into her crotch. With the new angle, I took her to my elbow."
                        show anna bangok orgasm with dissolve
                "I'll try pushing first...":
                    m "I leaned more of the weight of my upper body onto my arm, pressing on her gate."
                    An bangok blush "Seriously, [player_name]. Repeated force is more effective than--"
                    if not persistent.bangok_cervpen:
                        m "Finding the right angle, I slid all the way in, despite her clenching down."
                    show anna bangok orgasm with dissolve
                    $ renpy.pause (0.4)
                    show anna bangok blushpalm with dissolve
                    An "Nevermind."

            An bangok lipbite "Well done. Now fuck me."
            if persistent.bangok_cervpen:
                m "I started moving, pushing my arm almost to the elbow, then pulling back out until her cervix was about to let go of me, popping my knuckles through."
            else:
                m "I started moving, pulling back, then pushing my arm almost to the elbow, then pulling back out until her outer lips were about to let go of me."
            m "Anna writhed in ecstacy."
            $ renpy.pause(0.5)
            An "D-Do not stop!"
            m "I was about to ask why I would when her passage clamped down hard, the friction quadrupling. I could barely even manage to move. Not that it mattered, as one of her legs pulled me against her belly a moment later."
            show anna bangok orgasm with dissolve
            show black with fadequick
            play sound "fx/snarl.ogg"
            $ bangok_four_anna2.annacame = True 
            m "Anna let out another muffled roar, shoving her own hand into her mouth to try to keep from being too loud."
            $ renpy.pause (0.8)
            hide black
            show anna bangok lipbite 
            with dissolvemed
            m "After a long moment, Anna's canal relaxed its grip and she dropped her arms to her sides, releasing me."
            $ renpy.pause (0.5)
            An smirk "Holy fuckeroly. That... that was good.{w=0.8} Twice in one night."
            menu:
                "You came earlier?":
                    $ renpy.pause (0.5)
                    if persistent.bangok_cervpen:
                        An smirk "The first time you were through my cervix."
                    else:
                        An smirk "The first time I hilted your forearm."
                "My turn, now?":
                    $ renpy.pause (0.6)
                    An smirk "Yes. Your turn."
                "Hey! What about me?":
                    $ anna2mood -= 1
                    An bangok blush "Yes. Your turn."
            m "I withdrew my sopping wet arm from her now-loosened passage, considering my next move."
            return



        "[[Lick her.]" if bangok_four_anna2.lick == True:
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
            jump bangok_four_anna2_apartment_male_nostrapon_startingmenu



        "[[Use her mouth.]":
            c "Actually..."
            m "I sat on the couch, spreading my legs."
            c "Why don't you use that mouth of yours on me?"
            if bangok_four_anna2.annacame == True:
                show anna smirk with dissolve
                An "I suppose fair's fair after your arm."
                hide anna with None
                $ renpy.pause(0.0)
                show anna bangok blush at Position(xpos=0.8,ypos=1.0, xanchor='center')
            else:
                show anna sad with dissolve
                $ renpy.pause(0.9)
                if anna2mood < 4:
                    show anna face with dissolve
                An "Fine."
                hide anna with None
                $ renpy.pause(0.0)
                show anna sad at Position(xpos=0.8,ypos=1.0, xanchor='center')
            show anna normal at Position(xpos=0.7) with ease
            show anna normal at Position(xpos=0.6, ypos=1.1) with ease
            show anna normal at Position(ypos=1.3) with ease
            m "Anna got back off the couch, then sank to her knees in front of me."
            $ renpy.pause(0.3)
            show anna normal with dissolve
            m "She stroked one hand down my shaft, pressing the condom's ring all the way to the base. The rough scales of her hand and cold claws were an exciting and new sensation, bringing my shaft to twitching readiness."
            $ renpy.pause (0.8)
            show anna bangok orgasm at Position(ypos=1.5) with ease
            m "Then she descended on my crotch with an open maw, the brief flash of teeth giving me a thrill of danger deep in my gut."
            menu:
                "C-Careful with the teeth!":
                    $ anna2mood -= 1
                    show anna face with dissolve
                    show anna at Position(ypos=1.4) with ease
                    m "Before she'd even really begun anything, Anna retreated with claws over her face."
                    An "You've had ample opportunity to see what my mouth looks like. What did you think I was going to do? Bite into you? Cause an incident with your blood all over my face?"
                    An sad "Do you want this blowjob or not?"
                    $ renpy.pause(0.8)
                    c "I mean, I do--"
                    An normal "Then no buts about it. I know what I'm doing."
                    show anna bangok orgasm at Position(ypos=1.5) with ease
                    m "She didn't give me another chance to protest, diving back down."
                "O-hoohh...":
                    pass
            m "Anna's tongue slithered around my shaft, tugging and milking it toward the back of her maw."
            m "She closed her lips, teeth ghosting over the lower portion of my shaft as her scaly lips slid downward."
            m "Her rough tastebuds held my length hostage, twisting and tugging like she was sucking, but without any vacuum seal."
            $ renpy.pause(0.6)
            m "I threw my head back, momentarily lost in the brand new sensations."
            $ renpy.pause(0.6)
            show anna bangok blush at Position(ypos=1.49) with ease
            m "The tip of her tongue pulled back from my base, the windings tightening as she pulled back toward my cockhead. Her lips went with it, and for a moment I was worried she was pulling away."
            m "Then I felt her tongue tighten just beneath my tip, forming a squeezing ring around the condom."
            show anna bangok blush at Position(ypos=1.52) with ease
            m "She pushed her head back down, lips and teeth ghosting over my length before the tongue ring squeezed in their absence."
            m "I almost lost my hold right there. But Anna uncoiled her tongue at my base, pulling back with parted lips as she arranged her tongue for a second thrust."
            show anna bangok blush at Position(ypos=1.5) with ease
            menu:
                "[[Grab her horns.]" if bangok_four_hornincident == False:
                    if anna2mood < 1:
                        m "This pushing-only pace wasn't going to work for me. Luckily, nature had given me the perfect pair of handles to explain what I want to Anna."
                    else:
                        m "What Anna was doing to my shaft was incredible, but I wanted a slightly more active role."
                    m "I clasped Anna's horns with both hands when her tongue was formed into a ring again, tugging her back into my groin faster."
                    $ anna2mood -= 1
                    $ bangok_four_anna2.hornsgrabbed = True
                    show anna disgust at Position(ypos=1.52) with ease
                    m "Her teeth were quite a bit tighter on this descent, enough that I almost couldn't focus on her tongue as the thrill of danger returned, the worry I was sticking my thing someplace dangerous."
                "M-May I use your horns to...?":
                    $ anna2mood += 1
                    $ bangok_four_anna2.hornsgrabbed = False
                    m "Anna nodded, causing my cock to bob as she slurped at my tip."
                    m "I gave her a moment to reform her tight tongue ring, then pulled her head down my shaft by both horns."
                    show anna bangok orgasm at Position(ypos=1.52) with ease
                "[[Moan.]":
                    pass
            m "I thrust into her face a little as she came down. It felt like fucking some kind of exotic, teeth-ringed pussy, the sensation unlike anything I'd felt before."
            $ renpy.pause (0.5)
            m "Anna braced her forearms against my thighs, keeping me in place against the couch."
            $ renpy.pause(0.3)
            if bangok_four_anna2.hornsgrabbed is not None:
                m "I held Anna against my crotch a moment, enjoying as she lashed her tongue around my shaft. Then I drew her back, feeling her tongue uncoiling around my tip."
                show anna sad at Position(ypos=1.50) with ease
                m "I tugged her horns, indicating that I'd be picking up the pace. After giving her a moment to prepare her tongue, I dragged her back down."
                play soundloop "fx/rub2.ogg" fadein 0.5
                show anna:
                    ease 0.25 ypos 1.51
                    ease 0.4 ypos 1.50
                    repeat
                with None
            else:
                show anna bangok lipbite at Position(ypos=1.50) with ease
                m "Anna drew back again, keeping the ring with her tongue this time, milking me through the condom."
                play soundloop "fx/rub2.ogg" fadein 0.5
                show anna:
                    ease 0.25 ypos 1.51
                    ease 0.4 ypos 1.50
                    repeat
                with None
                m "Confident now in her control over my member, she started up a faster pace, facefucking herself onto my cock."
            $ renpy.pause(2.0)
            menu:
                "I-I'm about to...":
                    pass
                "[[Cum.]":
                    pass
            if bangok_four_anna2.hornsgrabbed is not None:
                show anna bangok blush at Position(ypos=1.53) with ease
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                m "I pulled Anna deep into my crotch, sheathing my shaft between her scaly lips."
                m "Her tongue kept moving, searching and tugging against our rubber barrier."
                $ renpy.pause(0.5)
                hide black with dissolveslow
                $ renpy.pause(0.5)
                m "I released Anna's horns, leaving her free to let my cock fall from her lips"
                show anna normal at Position(ypos=1.4) with ease
                m "Anna flicked the condom's reservoir with her tongue as she moved back."
            else:
                show anna bangok blush at Position(ypos=1.4) with ease
                m "Anna pulled off immediately, using a hand to finish pushing me to climax."
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                $ renpy.pause(0.5)
                hide black with dissolveslow
                $ renpy.pause(0.5)
                m "She kept pumping until my shaft began to soften, my liquid load expended. Then she flicked the condom's reservoir with her thumb."

            call bangok_four_anna2_apartment_harvest from bangok_four_anna2_apartment_bjdone

            if bangok_four_anna2.hornsgrabbed is None:
                show anna at center with ease
            else:
                if bangok_four_anna2.hornsgrabbed == True:
                    show anna normal at center with ease
                    An normal "I should note, you're lucky I get around as much as I do. Grabbing my horns like that could have resulted in a painful surprise with someone less experienced."
                    label bangok_four_anna2_apartment_hornincident_description:
                    c "What do you mean?"
                    An sad "It's a sensitive area. There's a biological drive to keep them from getting ripped off our heads, so using them to control our head's motion is... undesireable."
                    An bangok blush "Unless we see it coming. But that's not for everybody."
                    c "I see."
                else:
                    show anna bangok blush at center with ease
                    An "Thank you for {i}asking{/i} to grab my horns. I've had one asshole grab them without warning, and..."
                    if bangok_four_hornincident == True:
                        c "Of course. No problem."
                    else:
                        jump bangok_four_anna2_apartment_hornincident_description
                $ bangok_four_hornincident = True

            jump bangok_four_anna2_apartment_done



        "[[Use her ass.]":
            $ bangok_four_anna2.position = "ass"
            if persistent.bangok_cloacas == True:
                if bangok_four_anna2.annacame == True:
                    m "Anna's slit remained slightly parted after my arm-fucking, and like my arm still glistened with her arousal. I gave my dick a pump with the same arm I'd fucked her with, lubricating the condom, then got between her legs."
                    c "During the, ah, arm fucking, you said you usually take larger partners."
                    c "Could I try your ass, then? Since I assume it's going to be less..."
                    An smirk "Fine by me."
                else:
                    if anna2mood > 0:
                        show anna bangok blush with dissolve
                        m "Her slit was a thin, glistening line. I got between her legs, aiming my condom-wrapped dick directly into it."
                        c "I assume your ass is further back in your slit, here? Since you're a reptile and..."
                        An "Yes. And yes, you can go there."
                    else:
                        show anna sad with dissolve
                        m "Her slit was a thin line. I got between her legs, aiming my condom-wrapped dick toward the bottom of it, where I assumed her ass would be."
            else:
                if bangok_four_anna2.annacame == True:
                    m "Anna's slit remained slightly parted after my arm-fucking, and like my arm still glistened with her arousal. I gave my dick a pump with the same arm I'd fucked her with, lubricating the condom, in preparation to enter the smaller hole slightly further back between her legs."
                    c "During the, ah, arm fucking, you said you usually take larger partners."
                    c "Could I try your ass, then? Since I assume it's going to be less..."
                    An smirk "Fine by me."
                else:
                    if anna2mood > 0:
                        show anna bangok blush with dissolve
                        m "Her pucker was denoted by a few small rings of scales, an inch or two below the thin, glistening line of her slit. I got between her legs, aiming my condom-wrapped dick directly into it."
                        m "I just tapped my tip against it first, looking up at her in question."
                        An "Oh, you..."
                        An smirk "Fine by me."
                    else:
                        show anna sad with dissolve
                        m "Her pucker was denoted by a few small rings of scales, an inch or two below the thin line of her slit, I got between her legs, aiming my condom-wrapped dick directly into it."

            if anna2mood < 1:
                $ anna2mood -= 1
                show anna disgust with dissolve
                m "She clenched up hard the moment I pushed inside, anger flashing across her features."
                An "For fuck's sake. Can't you {i}ask{/i} first?"
                if bangok_four_anna2.lick == True:
                    c "Oh, are you going to tell me I can't do this either?"
                    An sad "Normally sex is between a penis and a vagina, in case you can't remember biology 101. Other holes get involved after discussing it."
                    c "We're discussing it now. Yes or no?"
                else:
                    c "Okay, I'll ask now. Yes or no?"
                $ renpy.pause (0.8)
                An sad "Fine. Go ahead."
                m "Even after she conceded the point, it took her a few moments to relax enough to let my dick move again, sliding with aching slowness into her warm, enveloping rectum."
            else:
                show anna bangok blush with dissolve
                m "Her ass clenched and tugged at my shaft as I entered, but in a way that spoke of experience, rather than spasms or pain."
                m "Her motions caused me to slow my entry, sliding with aching tingles of need into her warm, enveloping rectum."

            $ renpy.pause (0.8)

            m "I paused, hilted, enjoying her ass squeezing my base in a tight ring."

            $ renpy.pause (0.8)
            if anna2mood < 1:
                An sad "You're not cumming already, are you?"
            else:
                c "Do you need time to adjust?"
                An smirk "Not in the least. I've done anal before, [player_name]. With people larger than you, even."
                if anna2mood < 2:
                    An normal "Now do your thing."
                else:
                    An bangok blush "Now, start moving."
            jump bangok_four_anna2_apartment_vaganal_merge



        "[[Use her pussy.]":
            $ bangok_four_anna2.position = "vag"
            if bangok_four_anna2.annacame == True:
                m "Anna's slit remained slightly parted after my arm-fucking, and like my arm still glistened with her arousal. I gave my dick a pump with the same arm I'd fucked her with, lubricating the condom, then got between her legs."
                m "As I slipped inside, I realized my gusto had spread her out to the point where there was disappointingly little resistance."
            else:
                if anna2mood > 2:
                    show anna bangok blush with dissolve
                    m "Her slit was a thin glistening line. I got between her legs, aiming my condom-wrapped dick directly into it."
                    m "Entering her had disappointingly little resistance, her slit clearly meant to take larger partners."
                else:
                    show anna sad with dissolve
                    m "Her slit was a thin line. I got between her legs, aiming my condom-wrapped dick directly into it."
                    m "She tensed up, fighting my entry for a moment as I pressed all the way in. Once inside, though, the pressure disappeared, her passage clearly made for larger mates."
            m "I paused, hilted, as I felt her passage moving around me, muscles massaging my shaft like an all-around warm caress even if not squeezing tightly."
            $ renpy.pause(0.8)
            c "Can you feel me in there?"
            if anna2mood < 0:
                An disgust "What kind of question is that, \"can I feel it?\" It's in my body, isn't it?"
                An face "Just do your thing and cum already."
                c "Geez. Fine."
            elif anna2mood < 3:
                An sad "Yes. But you're rather small."
                c "Ah. Well, I'll do what I can."
            else:
                An smirk "You're adorable. But there's simply no way you'll get me off with just that thing."
                c "Is that a challenge?"
                An bangok blush "A statement of fact."

            label bangok_four_anna2_apartment_vaganal_merge:
            play soundloop "fx/rub2.ogg" fadein 2.0
            
            if anna2mood < 0:
                show anna sad with dissolve
            else:
                show anna bangok blush with dissolve
            $ renpy.pause(1.2)
            m "Taking her words as a challenge, I began to pump my hips, pulling out just beyond my tip before sliding back home."
            $ renpy.pause(0.8)
            if annamood >= 0:
                show anna smirk with dissolve
            m "As we fucked, I felt Anna's tail curling up between my legs, caressing my rear and encouraging my pace."
            m "Then the tip of her tail prodded into my crack, between my cheeks."
            menu:
                "O-Oh!":
                    $ renpy.pause(0.5)
                    $ bangok_four_anna2.tail = True
                "Uh. Please don't.":
                    $ renpy.pause(0.5)
                    show anna bangok blush with dissolve
                "[[Smack it away.]":
                    $ renpy.pause(0.5)
                    $ anna2mood -= 1
                    show anna sad with dissolve
                    c "What the hell was that?"
                    An "I take it you're not interested, then."
                    c "No. No I'm not."

            if bangok_four_anna2.tail == True:
                $ anna2mood += 1
                show anna bangok blush with dissolve
                m "Her tail rode against my rosebud for a few thrusts, in and out, before holding in place abruptly when I was in her."
                c "Ah!"
                m "My breath caught, pulling back out of her fucking her tail into my ass, and vice versa when I pressed forward."
                $ renpy.pause(0.8)
                c "Wh-Where did you-- How did you find out your tail could...?"
                An smirk "Practice."
            else:
                m "Retreating from my back, her tail followed the curve of one of my thighs, down my leg, just riding along while I filled its owner's hole."

            $ renpy.pause(2.0)

            m "As the combination of sensations pushed me toward my peak, Anna crossed her ankles behind my back, reducing the depth of my thrusts as she pulled me closer."

            if bangok_four_anna2.tail == True:
                m "Then her tail explored a little deeper."
                c "W--"
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                m "Finding that pleasure button within me, she pressed, pushing me over my edge inside her."
                $ renpy.pause(0.5)
                hide black with dissolvemed
                $ renpy.pause(0.5)
                m "She withdrew her tail from my ass and uncrossed her legs, leaving me free to rise on shaky legs."
            else:
                show anna bangok blush with dissolve
                m "I leaned in closer to her smooth scales, breath coming hot and heavy as her warmth increased, hide flushing in a clear blush."
                m "Then she tightened her legs against my back, pulling me in, and I couldn't hold off my climax any longer."
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                $ renpy.pause(1.0)
                hide black with dissolvemed
                $ renpy.pause(0.5)
                m "Once I'd come down from my peak, she uncrossed her legs, leaving me free to rise on slightly unsteady legs."

            hide anna with None
            $ renpy.pause(0.0)
            show anna bangok blush at Position(xpos=0.8,ypos=1.2, xanchor='center')
            m "Then she rose from the couch, giving the condom's filled reservoir a poke with the flat top of one of her claws."
            call bangok_four_anna2_apartment_harvest from bangok_four_anna2_apartment_vaganaldone
            jump bangok_four_anna2_apartment_done



        "Wait, it's vertical?" if bangok_four_anna2.waitvert == True and bangok_four_malepartners > 0:
            $ bangok_four_anna2.waitvert = False
            An sad "Obviously."
            An face "Oh. You must have been with a male before me."
            An normal "That's one of the few gender dimorphisms we have, aside from voice, some eye structure, and the obvious difference in reproductive equipment."
            if anna2mood < 2:
                An sad "Now will we get on with this?"
            else:
                An smirk "Now, could you get on with this?"
            jump bangok_four_anna2_apartment_male_nostrapon_startingmenu





label bangok_four_anna2_apartment_harvest:
    if blood == False:
        An "Well. With this sample, I suppose I don't need your blood anymore, do I?"
        m "She pinched just at my cock's tip and the ring, then began to tug it off."
        menu:
            "I didn't agree to that!":
                $ anna2mood -= 1
                An sad "No. You agreed to far more detailed procedures a few days from now. This is basically nothing."
                menu:
                    "Take her hands off.":
                        $ anna2mood -= 2
                        m "Grabbing her wrists, I yanked her hands off of my cock."
                        c "It's my DNA. That's not \"nothing\" to me!"
                        An face "Are you kidding me?"
                        An sad "It's a few kilometers of basic molecules chained together, replicated over and over. There's literally no point to protecting it. I can probably get most of it from skin cells you've shed on my arms tonight."
                        c "You're just doing this to get the information to clone me?"
                        An disgust "Why the fuck would I even want to do that?"
                        An face "No. This is all about figuring out how you work. And I don't need this to do it, but it makes it a lot easier to know what to expect and do when I bring you into my lab."
                        menu:
                            "Concede the point.":
                                $ renpy.pause(0.5)
                                $ anna2mood += 2
                                c "Okay. Look, I'm sorry. Giving samples of ourselves away isn't really normal among humans."
                                An sad "That's not what I'd expect from the liberal opinion on sex."
                                c "If you're just going to take it another way anyway, I guess there's no point to forcing you to do all that work. Go ahead and take it."
                                show anna normal with dissolve
                                $ renpy.pause(0.8)
                                An "Thank you."
                            "Refuse.":
                                $ anna2mood -= 1
                                stop music fadeout 2.0
                                c "I don't care. You're not keeping samples of my cum like some sick souveneir."
                                An disgust "Fine."
                                An sad "In that case, I've fulfilled my end completely. Expect a call from me when I have a spot in the lab."
                                label bangok_four_anna2_apartment_abruptdeparture:
                                stop music fadeout 0.5
                                if anna2mood > -2:
                                    c "Anna..."
                                hide anna with dissolvemed
                                $ renpy.pause(0.3)
                                play sound "fx/door/doorclose.ogg"
                                $ renpy.pause(1.0)
                                m "Without another word, Anna left."
                                $ renpy.pause(1.0)
                                scene black with dissolvemed
                                $ renpy.pause(0.5)
                                $ annastatus = "bad"
                                $ annascenesfinished = 2
                                jump _mod_fixjmp
                    "Puncture the condom.":
                        $ anna2mood -= 1
                        m "Grabbing her wrists, I forced her hands together, driving her claws through the condom's walls to puncture the sample she was after."
                        An disgust "What the fuck?!"
                        c "It's my DNA. That's not \"nothing\" to me!"
                        An "So you're going to spill it all over my hands?"
                        An sad "You do know that's exactly the same as just handing it to me, don't you? I need a few cells, not the whole sample."
                        An sad "It's a few kilometers of basic molecules chained together, replicated over and over. There's literally no point to protecting it."
                        c "You're just doing this to get the information to clone me?"
                        An disgust "Why the fuck would I even want to do that?"
                        An sad "No. This is all about figuring out how you work. And I don't need this to do it, but it makes it a lot easier to know what to expect and do when I bring you into my lab."
                        menu:
                            "Apologize.":
                                $ renpy.pause(0.5)
                                $ anna2mood += 1
                                c "Okay. Look, I'm sorry. Giving samples of ourselves away isn't really normal among humans."
                                An sad "That's not what I'd expect from the liberal opinion on sex."
                                c "If you're just going to take it another way anyway, I guess there's no point to forcing you to do all that work. Go ahead and take it."
                                show anna normal with dissolve
                                $ renpy.pause(0.8)
                                An "Thank you."
                                m "She tugged off the condom's remains, balling it in one hand."
                            "Threaten.":
                                $ anna2mood -= 2
                                stop music fadeout 2.0
                                c "Take that sample and I won't come into your lab."
                                An disgust "Fine."
                                m "She wiped my cum on my bare legs."
                                An "There. Happy now? Or do you want me to wash my hands to prove myself to you?"
                                $ renpy.pause(1.5)
                                An sad "Then I've fulfilled my end completely. Expect a call from me when I have a spot in the lab."
                                stop music fadeout 0.5
                                if anna2mood > -2:
                                    c "Anna..."
                                hide anna with dissolvemed
                                $ renpy.pause(0.3)
                                play sound "fx/door/doorclose.ogg"
                                $ renpy.pause(1.0)
                                m "Without another word, Anna left."
                                $ renpy.pause(1.0)
                                scene black with dissolvemed
                                $ renpy.pause(0.5)
                                $ annastatus = "bad"
                                $ annascenesfinished = 2
                                jump _mod_fixjmp
                    "Piss in the condom." if persistent.bangok_watersports:
                        $ anna2mood -= 2
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        $ renpy.pause(0.5)
                        show anna disgust with dissolve
                        An disgust "What the fuck are you...?"
                        m "She dropped the condom's bloating reservoir against the couch."
                        An rage "You {i}know{/i} the PH difference will destroy the sample! How {i}dare{/i} you!"
                        c "How dare {i}I{/i}? You were trying to take my DNA. That's not \"nothing\" to me!"
                        stop soundloop fadeout 0.5
                        An rage "It's a few kilometers of basic molecules chained together, replicated over and over. There's literally no point to protecting it!"
                        c "Well it's done now. What are you going to do about it?"
                        $ renpy.pause(0.8)
                        show anna sad with dissolve
                        $ renpy.pause(0.5)
                        An sad "Then I've fulfilled my end completely. Expect a call from me when I have a spot in the lab."
                        stop music fadeout 0.5
                        hide anna with dissolvemed
                        $ renpy.pause(0.3)
                        play sound "fx/door/doorclose.ogg"
                        $ renpy.pause(1.0)
                        m "Without another word, Anna left."
                        $ renpy.pause(1.0)
                        scene black with dissolvemed
                        $ renpy.pause(0.5)
                        $ annastatus = "bad"
                        $ annascenesfinished = 2
                        jump _mod_fixjmp
                    "Let her.":
                        pass
            "[[Let her.]":
                pass
        m "Pulling the condom completely free, she tied it off and palmed it."
    else:
        c "So are you going to take a sample of this, too?"
        An normal "No point. Sequencing your full DNA from sexual gametes would be a bunch of extra work with no benefit after you gave me your blood sample. At least if your chromosomes behave at all like ours."
        c "I see."
        m "She pinched at my cock's tip and the ring, then tugged my condom off of my limpening shaft, tying it off to set it aside."
    return





label bangok_four_anna2_apartment_done:
    show anna at center with ease
    if bangok_four_anna2.annacame == False:
        An sad "That's that, then. Are you satisfied?"
        if anna2mood > 2:
            c "Are you? I haven't done anything for you yet."
            An "I suppose not, but there are really some things I need to take care of back at the lab."
        else:
            c "More than."
            An normal "Glad to hear it. In that case, I should get back to the lab. I have a few more things to finish up."
    else:
        An smirk "I suppose that's that, then. Are you satisfied?"
        c "Yeah. You?"
        An "Yeah."
        $ renpy.pause(0.8)
        An bangok blush "I should get back to the lab. I have a few more things to finish up."
    c "At this time of night?"
    $ renpy.pause(0.8)
    An normal "If you're so worried about me, walk me there."
    $ renpy.pause(0.8)
    c "Just give me a second to put my clothes back on."
    An sad "That was a joke. Are you actually serious?"
    c "Sure. Why not? It's good chivalry not to make you take a walk of shame after a night like that."
    $ renpy.pause(0.8)
    if persistent.bangok_watersports == True:
        An face "Fine. While you do that, I'll borrow your government-funded restroom."
        menu:
            "I might not need to put my clothes back on for that...":
                $ renpy.pause (0.5)
                An sad "What exactly are you...?"
                An bangok blush "Oh."
                An smirk "If you say so."
                scene black with dissolvemed
                $ renpy.pause (0.5)
                play sound "fx/door/doorclose3.wav"
                $ renpy.pause (1.5)
            "Okay.":
                hide anna with dissolve
                $ renpy.pause (0.5)
                play sound "fx/door/doorclose3.wav"
    else:
        An face "Fine."
    $ renpy.pause(0.5)
    scene facin3 at Pan ((128, 250), (128, 250), 0.0)
    show anna normal
    with Fade(0.5,1.0,0.5)
    jump anna2skip

label bangok_four_anna2_lab_good_hookupover:
    An smirk "Speaking of which, now that our hookup is officially over, we should talk about your end of the deal."
    jump bangok_four_anna2_lab_good_hookupover_end

label bangok_four_anna2_lab_normal_hookupover:
    An smirk "You know, now that this hookup is officially over, if I don't work overtime every single day, I could fit you in for your end of the deal."
    jump bangok_four_anna2_lab_normal_hookupover_end