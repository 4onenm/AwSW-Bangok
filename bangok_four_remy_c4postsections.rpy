label bangok_four_remy_c4postsections_sebintro:
    menu:
        "Offer to bring a PDA to Remy.":
            pass
        "Excuse yourself.":
            jump bangok_four_remy_c4postsections_sebintro_return

    c "Happy to help."
    c "Actually, you still have the PDAs here, right?"
    c "The library is between here and home. I can bring a PDA there."
    Sb disapproval b "The library would be closed by this time of night."
    c "Well, I know Remy. If he's not still working at the library, I can get it to him at his home, and he can take it to the archives first thing in the morning."
    Sb normal b "I suppose as long as it gets to the archives. Thanks."
    Sb "Here you go. But once you've delivered it, get home and be safe."
    c "Sure. See you."
    stop music fadeout 2.0
    $ renpy.pause (0.5)
    scene black with dissolvemed
    $ renpy.pause (0.5)
    play sound "fx/steps/clean2.wav"
    scene bangok_four_library night at Pan ((60, 228), (0,228), 2.0) with dissolveslow

    c "(Yep, definitely closed. Lights are off and nobody's home.)"
    play sound "fx/door/handle.wav"
    $ renpy.pause(0.5)
    c "(What? The door's unlocked.)"

    m "I went inside and closed the door behind me."
    play soundloop "fx/bangok_panting_1dot8.ogg" fadein 15.0
    m "Though I thought to call out for Remy immediately, I heard something that gave me pause. As I moved deeper in the stacks of bookshelves, I identified it as some sort of animalistic grunting."
    m "A few words mixed in with the noises."
    "???" "[player_name]... oh..."
    m "I turned a corner."
    stop soundloop fadeout 1.5
    # TODO: Go get real photo of real library to import
    show remy shy dk:
        xanchor 0.5
        yanchor 1.0
        xpos 0.5
        ypos 1.1
    with dissolve
    c "Remy?"
    Ry "Wh- [player_name]?! What are you doing here? H-How did you get in?!"
    m "Remy's legs splayed awkwardly as he struggled to arrange them under himself, as if he'd just fallen from his side. The noises also stopped upon him spotting me and me spotting him."
    c "The front door to the library was unlocked."
    Ry "O-Oh it was?"
    Ry sad dk "That must have been my fault, then. I-I missed most of my shift today and so Emera left closing completely to me, as a punishment."
    c "I see."
    Ry shy dk "W-Why are you here? Y-You didn't happen to see anything untoward through the shelves, did you?"
    menu:
        "Didn't see a thing. I'm just here to give you this.":
            Ry smile dk "A-Ah! It's one of your PDAs. I told you one would find its way to me eventually."
            c "Yep, and now you can look at all the human knowledge you want."
            Ry normal dk "You have no idea how much I'm looking forward to that."
            Ry sad dk "It's a little late to go digging through it tonight, however, even with the library resources here at my disposal."
            c "Not if I help you close up."
            Ry normal dk "Oh, would you? That would be most helpful."
            c "Of course."
            jump bangok_four_remy_c4postsections_epilogue
        "I, ah, heard a bit.":
            Ry sad dk "O-Oh? Oh no."
            menu:
                "I think I should give you this and leave.":
                    stop music fadeout 1.0
                    Ry sad dk "Oh, it's one of your PDAs. I was really looking forward to this."
                    c "Well, here you go."
                    Ry sad dk "[player_name]..."
                    c "Enjoy."
                    python:
                        remystatus = "abandoned"
                        if persistent.remygoodending == False:
                            remydead = True
                    jump bangok_four_remy_c4postsections_epilogue
                "Do you want any \"help\" with that?":
                    pass

    $ renpy.pause(0.8)
    Ry shy dk "H-Help?!"
    $ renpy.pause(1.2)
    Ry "Y-you'd want to..."
    $ renpy.pause(1.2)

    Ry sad dk "I can't. I still have closing up to do here."
    c "I can always help you close up, too."
    Ry look dk "I sincerely hope that is not further innuendo."
    c "No, no, I mean that seriously."
    Ry normal dk "I see. That help I would appreciate very much."
    Ry shy dk "But, ah, why are you here at this time of night?"
    c "Oh, right. I came to give you this."
    Ry smile dk "Hey, it's one of your PDAs. I told you one would find its way to me eventually."
    c "Yep, and now you can look at all the human knowledge you want."
    Ry normal dk "You have no idea how much I'm looking forward to that."
    c "Well, look forward a little more. As you said, we have closing up to do."
    Ry normal dk "Thank you."

    $ renpy.pause(0.3)
    hide remy with dissolve
    $ renpy.pause(0.5)
    nvl clear
    window show
    n "With Remy's guidance, I was able to quickly accomplish some of the closing tasks requiring more dexterity at which he'd been struggling."
    n "This, in turn, left Remy free to finish the labor tasks of moving book carts that his poor mental state had been putting off."
    n "In under half an hour, we met back at the doors."
    window hide
    nvl clear
    $ renpy.pause(0.3)
    show remy shy dk with dissolve
    Ry "You said earlier you wanted to... \"help\" with what you'd heard as well."
    Ry "Were you making a joke in poor taste? Or would you actually want to, with my kind, have a..."
    m "He trailed off."
    if bangok_four_malepartners > 0 or bangok_four_femalepartners > 0:
        if bangok_four_malepartners + bangok_four_femalepartners < 2:
            c "I already have, once."
        else:
            c "I already have, multiple times."
        c "I really wasn't joking, Remy."
    else:
        menu:
            "No, never." if remystatus == "neutral":
                c "No offense Remy, but you're built like a horse. I can't imagine fucking you."
                Ry look dk "What... is a horse?"
                c "Well, you have the PDA now. Look it up."
                Ry sad dk "Ah, yes. I had forgotten."
                $ renpy.pause(1.2)
                Ry shy dk "I truly am sorry that--"
                c "That you were imagining having sex with me? And masturbating to that?"
                $ renpy.pause(0.5)
                Ry shy dk "..."
                $ renpy.pause(0.5)
                menu:
                    "You're disgusting.":
                        c "I could get over that you had the thoughts. Hell, I made a joke about it."
                        c "But to pretend you're sorry about it? Try to get back into my good graces in the hope you might get to act on those sick thoughts someday?"
                        Ry sad dk "[player_name] I--"
                        c "Just don't."
                        python:
                            remystatus = "abandoned"
                            if persistent.remygoodending == False:
                                remydead = True
                        jump bangok_four_remy_c4postsections_epilogue
                    "Let's just forget about it.":
                        c "People can't control their urges. Just know I don't remotely see you that way."
                        Ry sad dk "I see."
                        Ry shy dk "Then if it's not too much trouble, I'd like for tonight to be over as soon as possible."
                        c "Sure. Have a good night's sleep."
                        $ renpy.pause(0.8)
                        c "And don't think about me that way."
                        jump bangok_four_remy_c4postsections_epilogue
            "I... I don't know.":
                c "Maybe going all the way there this fast is too soon."
                Ry "Y-Yes of course."
                Ry normal dk "Could we, perhaps, ignore what you heard? At least until, or, if you become comfortable with..."
                c "Sure."
                Ry smile dk "Thank you."
                $ renpy.pause(0.5)
                Ry normal dk "I suppose I'm headed home, then."
                Ry shy dk "Unless I should walk you, or you should walk me, or..."
                c "I think we both need some more sleep."
                Ry normal dk "Right."
                c "Goodnight, Remy."
                Ry shy dk "And to you as well."
                jump bangok_four_remy_c4postsections_epilogue
            "Yes.":
                pass
            "Been fucking waiting!":
                c "I'll be honest: I've wanted to get under your tail since I first saw you."
                c "Now to find out that you've been wanting to get in my pants?"
                Ry look dk "I..."
                c "It's not even a question. In fact, we can lock the library doors properly now, and you had a good spot back there. How about we just give it a go right now?"
                Ry look dk "Please stop."
                c "You sure sounded like you wanted this over there. Why would you want me to stop?"
                Ry look dk "Is that all you wanted from me this whole time? Sex?"
                $ renpy.pause(0.8)
                c "I mean..."
                show remy sad dk with dissolve
                m "My answer set a stricken look across Remy's face."
                c "What? You wanted this."
                Ry "Please get out."
                c "..."
                Ry "Now."
                c "For fuck's sake, Remy--"
                Ry "Please don't talk to me again."
                c "Remy!"
                play sound "fx/door/lock.ogg"
                m "Remy locked me outside the library."
                python:
                    remystatus = "bad"
                    if persistent.remygoodending == False:
                        remydead = True
                jump bangok_four_remy_c4postsections_epilogue
        c "I'm not averse to it. And it sounds like you're not either."

    if remystatus == "neutral":
        c "Why not make it friends with benefits? If it makes both of us happier."
    else:
        c "Why wait to take that step? If it makes both of us happier."


    jump todo_out_of_content_bangok_four_remy_c4postsections


label todo_out_of_content_bangok_four_remy_c4postsections:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")

label bangok_four_remy_c4postsections_epilogue:
    stop music fadeout 2.0
    $ renpy.pause (0.5)
    scene black with dissolvemed
    $ renpy.pause (0.5)
    scene o at Pan((0, 100), (0, 250), 3.0) with dissolveslow
    $ renpy.pause (1.3)

    m "I returned home utterly spent after the long night. After this fateful day, I was glad to finally have some sort of respite."
    # TODO: Add alternates of this line
    m "My stomach rumbled quietly, the lack of lunch or dinner weighing heavy on my energy."
    m "Then, I suddenly found my remaining strength leaving me and collapsed to the floor."
    jump bangok_four_remy_c4postsections_epilogue_admin