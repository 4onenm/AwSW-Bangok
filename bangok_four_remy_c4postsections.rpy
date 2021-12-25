init python in bangok_four_remy_c4postsections_store:
    remy_top = False
    remy_tail_player = None
    remy_tail_remy = None

    protection_agreed = False

    tail_protection = False
    shaft_protection = False
    mc_protection = False

    tail_lube = False
    shaft_lube = False
    ass_lube = False

    tail_in_remy = False
    tail_in_player = None

    remy_kissed = False

    knot_pos = None




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
    play music "mx/bangok_quiet_campfire.ogg" fadein 5.0
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
                stop music fadeout 8.0
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
                        python:
                            if remystatus == "good":
                                remystatus = "neutral"
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
                stop music fadeout 5.0
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

    show remy look dk with dissolve
    m "Considering the question, Remy led the way outside."
    hide remy with dissolve

    scene bangok_four_library outside night with dissolvemed
    $ renpy.pause(0.3)
    play sound "fx/door/lock.ogg"
    $ renpy.pause(0.8)
    show remy look dk with dissolve

    $ renpy.pause (0.5)
    Ry look dk "Simple anatomy could very well get in the way of us taking that step. I-I'm not sure if you've done research on the matter."
    Ry shy dk "My species is, ah, {size=+8}larger{/size} than most in that area. To, erm, help... {i}directly{/i}... could be dangerous for your health. I don't..."

    menu:
        "That's not necessary.":
            c "I don't need that to make this work. And I'm sure we can find some other way to satisfy you."
            Ry shy dk "Ah. Okay."
        "I've had large partners." if ((bangok_four_bryce1_unplayed == False and (bangok_four_bryce1_position_picka in ["vag","analbot"] or bangok_four_bryce1_position_pickb in ["vag","analbot"]))
            or (bangok_four_bryce3_store.unplayed == False and bangok_four_bryce3_store.mc_bottom == True)
            or (bangok_four_xipsum.unplayed == False and bangok_four_xipsum.took_ipsum_both == True)
            or (bangok_four_xkatsu.unplayed == False and bangok_four_xkatsu.target in ["throat","vag","womb","ass"])):
            $ bangok_four_remy_c4postsections_store.remy_top = True
            Ry look dk "[player_name], I'm not sure you understand..."
            
            if (bangok_four_bryce3_store.unplayed == False and bangok_four_bryce3_store.mc_bottom == True):
                c "No, Remy, I mean {size=+8}large{/size}. And of your species."
            elif (bangok_four_bryce1_unplayed == False and (bangok_four_bryce1_position_picka in ["vag","analbot"] or bangok_four_bryce1_position_pickb in ["vag","analbot"])):
                c "No, Remy, I mean another quadrupedal dragon."
            elif (bangok_four_xkatsu.unplayed == False and bangok_four_xkatsu.target in ["throat","vag","womb","ass"]):
                c "No, Remy, I mean another quadrupedal dragon."
            elif (bangok_four_xipsum.unplayed == False and bangok_four_xipsum.took_ipsum_both == True):
                c "No, Remy, I mean a dragon with two penises. And I took both in one hole."
            else:
                play sound "fx/system3.wav"
                s "Missing case for player banging previous large partner. (Ignore this to continue.)"
                $ renpy.error("Missing case for player banging previous large partner. (Ignore this to continue.)")
            Ry shy dk "Oh. Oh my."
            Ry shy dk "Well, perhaps I should take your word on that point. I'm not sure I want the details."
            Ry shy dk "Would you actually want me to... to... inside you?"
            c "Yeah. At least, we can consider it an option."
        "I've done some research.":
            if bangok_four_malepartners > 0:
                c "Some of it of an intimate variety."
            c "I don't think it'll be unreasonable, size-wise. Humans are pretty stretchy if you take it slow."
            Ry shy dk "I... I don't think that's sufficient, [player_name]."
            Ry look dk "I think whatever we end up doing, if we end up doing anything, you should take full control and pay close attention to your limits."
            c "That's fair enough."

    $ renpy.pause(0.5)

    c "Where do we go from here?"
    Ry shy dk "I-In terms of act, or?"
    c "Not quite. I assume you don't want to do this out in the open in town, or in the wilderness, so..."
    Ry look dk "Your apartment or my house."
    $ renpy.pause(0.5)
    show remy sad dk with dissolve
    $ renpy.pause(0.5)
    c "Let's go to my apartment. I'm sure you don't want to think about bringing anyone over to your house for... this sort of thing."
    Ry "Right."
    $ renpy.pause(0.8)
    Ry look dk "Hold on. What if the guard assigned to your apartment sees us?"
    c "What guard? The police have been stretched too thin to have one since the first victim."
    Ry shy dk "Ah. I had forgotten."
    Ry look dk "Then... then your apartment is fine."

    $ renpy.pause(0.3)
    play sound "fx/steps/rough_gravel.wav"
    scene np4 with dissolveslow
    $ renpy.pause(0.5)
    m "As we walked, Remy seemed more and more reluctant to remain close to me, perhaps having second thoughts about our night."
    show remy sad flip dk at left with dissolve
    $ renpy.pause(0.3)
    m "Trying to keep his mind off Amelia, I changed the subject to looking ahead."
    c "So, ah, what usually gets you going?"
    Ry look flip dk "Going?"
    c "Aroused. Excited. Like... what were you imagining earlier in the library?"
    Ry shy flip dk "Oh. Oh I--"
    m "His tail flicked sharply."
    Ry look flip dk "[player_name], I think we should be focused on what's safe and enjoyable for both of us."
    m "His long, smooth, tapered tail kept swaying, then stiffened abruptly when I looked back at it."
    Ry shy flip dk "Er, [player_name]..."
    stop sound fadeout 0.5
    m "I hadn't noticed, but I'd stopped walking."
    c "So, you're a fan of putting that tail to good use, I'm guessing?"
    $ renpy.pause(0.7)
    m "Remy's blush glowed brighter in the moonlight."

    python in bangok_four_remy_c4postsections_store:
        remy_tail_player = None
        remy_tail_remy = None
    label bangok_four_remy_c4postsections_tailmenu:
    menu:
        "What about putting it in me?" if bangok_four_remy_c4postsections_store.remy_tail_player is None and bangok_four_remy_c4postsections_store.remy_tail_remy == True:
            jump bangok_four_remy_c4postsections_tailmenu_tail_player
        "I'm up for it." if bangok_four_remy_c4postsections_store.remy_tail_player is None and bangok_four_remy_c4postsections_store.remy_tail_remy is None:
            label bangok_four_remy_c4postsections_tailmenu_tail_player:
            Ry "W-We couldn't possibly. [player_name], it's {i}much{/i} larger than... than my..."
            c "We could take it only as far as it's safe. I trust you, Remy, and we'll feel out my limits."
            if bangok_four_remy_c4postsections_store.remy_top == True:
                $ bangok_four_remy_c4postsections_store.remy_tail_player = True
                Ry "I... I suppose we might try."
            else:
                $ bangok_four_remy_c4postsections_store.remy_tail_player = False
                show remy look flip dk
                m "He flicked his tail aside, then held it further away from me."
                Ry look flip dk "\"Feeling out limits\" does not seem safe."
                c "Remy..."
                Ry "No. My tail will not be involved with your body. Not... not right now."
                c "Okay."
            if bangok_four_remy_c4postsections_store.remy_tail_remy is None:
                jump bangok_four_remy_c4postsections_tailmenu
        "What about with your body?" if bangok_four_remy_c4postsections_store.remy_tail_player is not None and bangok_four_remy_c4postsections_store.remy_tail_remy is None:
            c "Do you like having it inside you?"
            jump bangok_four_remy_c4postsections_tailmenu_tail_remy
        "Do you like having it inside you?" if bangok_four_remy_c4postsections_store.remy_tail_remy is None and bangok_four_remy_c4postsections_store.remy_tail_player is None:
            label bangok_four_remy_c4postsections_tailmenu_tail_remy:
            Ry shy flip dk "I..."
            Ry "[player_name]..."
            $ renpy.pause(0.8)
            Ry "Yes. A little. I mean--"
            c "Say no more."
            menu:
                "Happy to help.":
                    $ renpy.pause(0.8)
                    $ bangok_four_remy_c4postsections_store.remy_tail_remy = True
                    if bangok_four_remy_c4postsections_store.remy_tail_player is None:
                        jump bangok_four_remy_c4postsections_tailmenu
                "That's too weird for me.":
                    c "So let's just forget I asked that."
                    $ bangok_four_remy_c4postsections_store.remy_tail_remy = False
                    show remy look flip dk with dissolve
                    $ renpy.pause(0.8)
        "Sorry, forget I asked.":
            Ry shy flip dk "Th-Thank you."

    m "We resumed walking toward my apartment."
    play sound "fx/steps/rough_gravel.wav"
    scene black with dissolvemed
    $ renpy.pause(1.0)
    scene np5e with dissolvemed
    $ renpy.pause(1.0)
    play sound "fx/door/handle.wav"
    $ renpy.pause(0.3)
    scene o2 at Pan((0, 150), (0, 250), 1.5) with dissolve
    $ renpy.pause(1.2)
    show remy normal at center with dissolve
    c "You know, this is a little like when you brought me here my first night."
    Ry shy "I... I suppose."
    Ry shy "I-I'm going to retrieve some things your apartment is stocked with."
    c "Oh?"
    hide remy with dissolve
    $ renpy.pause(0.3)
    play sound "fx/rummage.wav"
    m "Remy disappeared into the bathroom. I heard some light boxes falling from inside my bathroom cabinet's low shelves, plus something heavier."
    $ renpy.pause(1.0)
    play sound "fx/slide.ogg"
    show remy shy at center with dissolve
    m "Remy returned nosing three boxes of condoms and a bottle of lube along the floor."

    c "Protection?"
    Ry "It's not strictly necessary, with us being not just different species but of wildly differing taxonomic classes. But I'm not sure if you..."
    menu:
        "Probably a good idea.":
            $ bangok_four_remy_c4postsections_store.protection_agreed = True
        "Nah, don't worry about it.":
            $ bangok_four_remy_c4postsections_store.protection_agreed = False

    Ry normal "The, ah, lube is strictly necessary. No question."
    c "Alright."

    $ renpy.pause (0.8)
    m "We stood, staring at each other for a few moments."
    $ renpy.pause (0.8)

    Ry shy "..."
    if bangok_four_remy_c4postsections_store.remy_top == False:
        show remy sad with dissolve
        m "Remy looked down at his tie. His face fell, attention swallowed by the strip of fabric."
        $ renpy.pause(0.8)
        c "Remy?"
        Ry "I-I can't."
        Ry "I can't do this, [player_name]. I'm sorry, I..."
        menu:
            "I understand.":
                Ry look "You do?"
                c "Yeah. We don't have to take this any faster than you're comfortable with, or anywhere at all if you're not comfortable sharing what you were thinking in the library."
                label bangok_four_remy_c4postsections_reshirt:
                $ renpy.pause(0.8)
                Ry normal "Thank you, [player_name]."
                Ry shy "I think, then, I'll, ah, bid you good night and be on my way."
                c "Sure."
                $ renpy.pause(0.5)
                hide remy with dissolve
                $ renpy.pause(0.3)
                play sound "fx/door/handle.wav"
                $ renpy.pause(1.0)
            "Are you sure?":
                c "You seemed pretty into whatever you were thinking at the library. If you--"
                Ry shy "[player_name], {i}please.{/i}"
                Ry look "I-I'm just not comfortable with... that right now. Not like this. Not..."
                c "Alright, alright."
                jump bangok_four_remy_c4postsections_reshirt
            "[[Undress.]":
                stop music fadeout 2.0
                play sound "fx/undress.ogg"
                show remy shy with dissolve
                $ renpy.pause(0.5)
                m "I toyed with my genitalia, showing it off."
                c "C'mon, Remy. I heard you at the library. You can't tell me you weren't thinking about this."
                hide remy with dissolve
                c "Remy?"
                play sound "fx/door/handle.wav"
                $ renpy.pause(1.0)
                python:
                    remystatus = "bad"
                    if persistent.remygoodending == False:
                        remydead = True
                if bangok_four_playerhasdick == True:
                    m "Remy left abruptly, leaving me literally dick-in-hand."
                else:
                    m "Remy left abruptly, leaving me figuratively with my dick in my hand."
                play sound "fx/undress.ogg"
                m "Annoyed, I shrugged back into my clothes."
                $ renpy.pause(1.0)
        stop music fadeout 2.0
        $ renpy.pause (0.5)
        m "After this fateful day, I was glad to finally have some sort of respite. I wandered into the kitchen as I considered tonight's dinner."
        c "(It's too late to order out. Should I cook something? Or just go to sleep?)"
        m "When I returned to the living room, I suddenly found my strength leaving me and collapsed to the floor."
        jump bangok_four_remy_c4postsections_epilogue_admin

    hide remy with dissolve
    $ renpy.pause(0.5)
    play sound "fx/undress.ogg"
    $ renpy.pause(1.5)
    show remy normal b with dissolve
    m "Remy removed his tie, setting it aside on the couch."

    menu:
        "Want any help with the collar or glasses?":
            Ry shy b "No, I..."
            $ renpy.pause(1.8)
            Ry "Yes."
            hide remy with dissolve
            $ renpy.pause(0.5)
            play sound "fx/undress.ogg"
            $ renpy.pause(1.5)
            show remy shy ud with dissolve
        "[[Say nothing.]":
            $ renpy.pause(0.8)
            hide remy with dissolve
            play sound "fx/undress.ogg"
            $ renpy.pause(1.5)
            show remy normal ud with dissolve
            m "His collar and glasses joined it, glasses falling over the back and onto the seat."
    $ renpy.pause(0.3)
    menu:
        "You are pretty cute, you know that?":
            Ry shy ud "Th-Thank you."
        "That's a lot of neck.":
            Ry look ud "I'll have to return some of it to the shop."

    Ry normal ud "And you, [player_name]?"
    $ renpy.pause(0.3)
    play sound "fx/undress.ogg"
    $ renpy.pause(2.0)

    show remy shy ud with dissolve
    $ renpy.pause(0.5)
    Ry shy ud "My, ah, eyesight isn't ideal without my glasses. Between your legs, i-is that a...?"
    if bangok_four_playerhasdick is None:
        menu:
            "Penis.":
                $ bangok_four_playerhasdick = True
            "Vagina.":
                $ bangok_four_playerhasdick = False
    elif bangok_four_playerhasdick == True:
        c "Penis."
    else:
        c "Vagina."

    if bangok_four_playerhasdick == True:
        Ry look ud "Ah. That... seems below the average for runners."
        Ry shy ud "And I, ah, think the runner average is a little small to do... th-things for me. And I can't say I have much experience with oral on small males--"
        if bangok_four_remy_c4postsections_store.remy_tail_remy == True:
            c "Well, we have your tail for satisfying your, ah, hole."
            Ry "Er..."
            Ry normal ud "I suppose that is true."
        else:
            menu:
                "I want you in me, so don't worry about it.":
                    Ry "Er..."
                    Ry normal ud "I suppose that makes sense."
                "We'll figure something out.":
                    Ry "I..."
                    Ry normal ud "Okay. Of course."
    else:
        Ry shy ud "Ah. Th-That... I see."

    $ renpy.pause(0.5)
    c "And you? From what you said earlier..."
    Ry normal ud "Ah. Let me... I'll just get positioned first and then..."
    $ renpy.pause(0.3)
    hide remy with dissolve
    scene o2:
        ypos -250
        ease 1.5 xpos -128
    with None
    $ renpy.pause(1.8)
    scene o2:
        ypos -250 xpos -128
    with None
    show remy shy ud:
        xanchor 0.5
        yanchor 1.0
        transform_anchor True
        rotate 30
        xpos 0.7
        ypos 1.36
    with dissolve
    $ renpy.pause(0.5)
    if persistent.bangok_cloacas == True:
        m "With Remy lying on his back, I could see a single horizontal slit, exposed between his hindlegs. The scales rimming the hole looked ever so slightly damp and shiny."
    else:
        m "With Remy lying on his back, I could see a single large horizontal slit, and a smaller one further down, exposed between his hindlegs. The scales rimming the upper looked ever so slightly damp and shiny."

    if bangok_four_malepartners < 1 and (persistent.bangok_cloacas == False or bangok_four_femalepartners < 1):
        c "Wait, I thought you were male. Do you not have a penis?"
        Ry normal ud "I do. It's just..."

    m "After a few moments, Remy clenched some muscles in his lower body. A {size=+8}large{/size}, pinkish shaft slid out into the light of the room."
    show remy normal ud with dissolve
    $ renpy.pause(0.5)
    c "Oh my."
    Ry look ud "If that's too large, we really should call this off now."
    c "No, no, I think I'll be fine."
    Ry shy ud "Then... what would you like to do? I, ah, believe we should probably get any prep work done before we... go further."
    m "Moving the bottle of lube and boxes of condoms closer by, I considered our options."
    jump bangok_four_remy_c4postsections_keymenu

label bangok_four_remy_c4postsections_keymenu:
    menu:
        "Put a condom on myself." if bangok_four_remy_c4postsections_store.mc_protection == False and bangok_four_playerhasdick == True and bangok_four_remy_c4postsections_store.protection_agreed == True:
            $ bangok_four_remy_c4postsections_store.mc_protection = True
            show remy shy ud with dissolve
            call bangok_four_remy_c4postsections_keymenu_getcondom
            jump bangok_four_remy_c4postsections_keymenu
        "Put a condom on his cock." if bangok_four_remy_c4postsections_store.shaft_protection == False and bangok_four_remy_c4postsections_store.shaft_lube == False and bangok_four_remy_c4postsections_store.protection_agreed == True:
            $ bangok_four_remy_c4postsections_store.shaft_protection = True
            show remy shy ud with dissolve
            call bangok_four_remy_c4postsections_keymenu_getcondom
            jump bangok_four_remy_c4postsections_keymenu
        "Lube his cock." if bangok_four_remy_c4postsections_store.shaft_lube == False:
            $ bangok_four_remy_c4postsections_store.shaft_lube = True
            if bangok_four_remy_c4postsections_store.protection_agreed == True and bangok_four_remy_c4postsections_store.shaft_protection == False:
                show remy look ud with dissolve
                m "As I lifted the bottle of lube over Remy's shaft, he gave me a look."
                Ry "[player_name], you, ah, said protection was probably a good idea. Lube underneath it can make it slip easily, making it unsafe."
                Ry shy ud "Did you change your mind about using a condom?"
                menu:
                    "Yeah. I changed my mind.":
                        $ bangok_four_remy_c4postsections_store.protection_agreed = False
                        if bangok_four_remy_c4postsections_store.mc_protection == True:
                            Ry normal ud "Then I'm fine with taking your shaft unprotected as well."
                            Ry shy ud "I mean, it would be a little odd for you to be protected and me unprotected."
                            m "Agreeing with his logic, I tugged off my own condom as well."
                            $ bangok_four_remy_c4postsections_store.mc_protection = False
                        else:
                            Ry normal ud "Whatever you prefer."
                    "I'll put a condom on you.":
                        call bangok_four_remy_c4postsections_keymenu_getcondom
                        $ bangok_four_remy_c4postsections_store.shaft_protection = True

            m "I squirted a big dollop of lube onto his shaft, then set the bottle aside and began to spread it with my hands."
            play soundloop "fx/massage2.ogg"
            show remy shy ud closed with dissolve
            $ renpy.pause(2.0)
            stop soundloop fadeout 0.3
            $ renpy.pause(0.5)
            Ry shy ud "Ah. Th-That's... well applied."

            menu:
                "Keep going with your hands and mouth.":
                    jump bangok_four_remy_c4postsections_oral
                "Do something else.":
                    pass
            jump bangok_four_remy_c4postsections_keymenu
        "Lube his ass." if bangok_four_remy_c4postsections_store.ass_lube == False and (bangok_four_playerhasdick == True or bangok_four_remy_c4postsections_store.remy_tail_remy == True) and bangok_four_remy_c4postsections_store.tail_in_remy == False:
            $ bangok_four_remy_c4postsections_store.ass_lube = True
            if persistent.bangok_cloacas == True:
                c "Rear of your cloaca is your ass, right?"
                show remy shy ud with dissolve
                m "I squeezed out a large dollop of lube onto Remy's slit, sliding some of it down the bottom of his cock, then set the bottle aside and reached to work my fingers in, to make sure it permeated his rear entrance."
            else:
                show remy shy ud with dissolve
                m "I squeezed out a large dollop of lube onto Remy's ass, then set the bottle aside and reached to work my fingers in, to make sure it permeated his rear entrance."
            Ry shy ud closed "O-Ohhhh."
            m "It didn't take long to spread the lube in, but just prodding at the outside of Remy's hole seemed to get him going a little more, his cock twitching."
            menu:
                "Push a few fingers in.":
                    jump bangok_four_remy_c4postsections_fisting
                "Put Remy's tail in." if bangok_four_remy_c4postsections_store.remy_tail_remy == True:
                    jump bangok_four_remy_c4postsections_keymenu_tailinsert
                "Do something else.":
                    show remy shy ud with dissolve
                    m "I withdrew my fingers and Remy sighed."
            jump bangok_four_remy_c4postsections_keymenu
        "Lube his tail." if bangok_four_remy_c4postsections_store.tail_lube == False and bangok_four_remy_c4postsections_store.tail_in_remy == False and (bangok_four_remy_c4postsections_store.remy_tail_remy == True or bangok_four_remy_c4postsections_store.remy_tail_player == True):
            $ bangok_four_remy_c4postsections_store.tail_lube = True
            if bangok_four_remy_c4postsections_store.remy_tail_remy == True and bangok_four_remy_c4postsections_store.remy_tail_player == True:
                m "As I moved down toward Remy's tail with the lube, he spoke up."
                Ry look ud "Are you doing that for putting it into me or into you?"
                menu:
                    "Me.":
                        label bangok_four_remy_c4postsections_keymenu_tailcondom_check:
                        Ry look ud "I'm... I'm unsure of your durability in that... area. My scales are far from perfectly smooth. If you want to do that, it will be far safer for you to use a condom over my tail. And to use a condom, you can't really have lube underneath it, especially with the way my tail tapers..."
                        menu:
                            "I want you as you are.":
                                Ry shy ud "Er... I-if you insist."
                            "I'll put a condom on your tail.":
                                call bangok_four_remy_c4postsections_keymenu_getcondom
                                $ bangok_four_remy_c4postsections_store.tail_protection = True
                    "You.":
                        Ry shy ud "I... Oh."
            elif bangok_four_remy_c4postsections_store.remy_tail_player == True:
                jump bangok_four_remy_c4postsections_keymenu_tailcondom_check

            show remy shy ud with dissolve
            $ renpy.pause(0.3)
            play soundloop "fx/massage2.ogg"
            $ renpy.pause(2.0)
            stop soundloop fadeout 0.3
            if bangok_four_remy_c4postsections_store.tail_protection == True:
                m "The condom over half of Remy's tail glistened with globs of lube, the entire surface coated."
            else:
                m "Remy's tail glistened with lube as far as halfway down, coating over every scale and flowing down inbetween."
            Ry smile ud "Looks good."
            Ry normal ud "Er. I think. Again, glasses."
            if bangok_four_remy_c4postsections_store.remy_tail_remy == True:
                menu:
                    "Put Remy's tail in his ass.":
                        label bangok_four_remy_c4postsections_keymenu_tailinsert:
                        Ry shy ud "What are you...?"
                        $ renpy.pause(0.3)
                        Ry shy ud closed "Mmnh."
                        $ bangok_four_remy_c4postsections_store.tail_in_remy = True
                        $ renpy.pause(0.3)
                        m "When he realized what I was doing, Remy's tail stopped resisting my attempt to move it, curling over and almost guiding itself to his rear entrance before burrowing in, sliding easily enough with the lubrication I'd added."
                        if bangok_four_remy_c4postsections_store.tail_lube == True and bangok_four_remy_c4postsections_store.ass_lube == True:
                            m "The double layer of lube from his tail and ass squished and spattered over his backside in glistening droplets."
                        Ry shy ud "Could you... Would you mind pushing on it? My own muscles can only bend it over so far, and when it gets wider..."
                        if bangok_four_remy_c4postsections_store.tail_protection == True:
                            m "I took hold of Remy's tail where it curved over, just before the condom began, then gently began to push, feeding more into his spreading asshole."
                        else:
                            m "I took hold of Remy's tail where it curved over, then gently began to push, feeding more into his spreading asshole."
                        Ry shy ud closed "Nnh..."
                        if bangok_four_remy_c4postsections_store.shaft_protection == True:
                            m "His cock twitched noticeably as I felt his tail move inside him."
                        else:
                            m "His cock twitched noticeably, a small dribble of pre leaking from the tip as I felt his tail move inside him."
                        Ry shy ud "I... think that's as far as I'll take it, u-unless you plan to push me over my peak this way."
                        m "I let go, considering my remaining options."
                        jump bangok_four_remy_c4postsections_keymenu
                    "Later.":
                        pass
            jump bangok_four_remy_c4postsections_keymenu
        "Take his shaft between my legs." if bangok_four_remy_c4postsections_store.shaft_lube == True:
            show remy shy ud with dissolve
            m "As I straddled Remy's chest just in front of his hindlegs, he blushed."
            Ry "I, ah, are you ready?"
            if bangok_four_remy_c4postsections_store.tail_lube == False and bangok_four_remy_c4postsections_store.tail_in_remy == False and bangok_four_remy_c4postsections_store.remy_tail_player == True:
                menu:
                    "Wait, I want to prep your tail." if bangok_four_remy_c4postsections_store.tail_lube == False and bangok_four_remy_c4postsections_store.tail_in_remy == False and bangok_four_remy_c4postsections_store.remy_tail_player == True:
                        jump bangok_four_remy_c4postsections_keymenu_tailcondom_check
                    "Yeah.":
                        pass
            else:
                c "Yeah."
            Ry "B-Before you start..."
            Ry look ud "I'm... I'm not small compared to you. Please don't feel obligated to keep going if this is too much."
            c "Remy, would I be here on top of you if I didn't think I could handle this?"
            Ry shy ud "Just k-keep that in mind."
            if bangok_four_playerhasdick == False:
                if bangok_four_remy_c4postsections_store.tail_lube == True and bangok_four_remy_c4postsections_store.remy_tail_player == True:
                    Ry shy ud "I know you wanted to play into my, ah, tail... interests. With dragons, it's the reproductive entrance that is more, er, malleable and damage resistant. It's also slightly dangerous to change openings, if you understand what I mean."
                    c "Oh. What you're saying is, if your tail is going anywhere in me, it's going in my pussy."
                    Ry normal ud "That would be safest. And would mean you need to take my penis in your... alimentary canal. Anus."
                    c "Right."

                menu:
                    m "Take Remy's shaft..."
                    "Anally.":
                        jump bangok_four_remy_c4postsections_mcpowerbottom_anal
                    "Vaginally.":
                        jump bangok_four_remy_c4postsections_mctop_vag
            else:
                jump bangok_four_remy_c4postsections_mcpowerbottom_anal


    jump todo_out_of_content_bangok_four_remy_c4postsections

label bangok_four_remy_c4postsections_keymenu_getcondom:
    play sound "fx/rummage.wav"
    $ renpy.pause(0.6)
    stop sound fadeout 0.5
    $ renpy.pause(0.5)
    return

label bangok_four_remy_c4postsections_fisting:
    jump todo_out_of_content_bangok_four_remy_c4postsections

label bangok_four_remy_c4postsections_oral:
    jump todo_out_of_content_bangok_four_remy_c4postsections

label bangok_four_remy_c4postsections_mcpowerbottom_anal:
    if bangok_four_remy_c4postsections_store.shaft_protection == True:
        m "I turned around, facing Remy's condom-wrapped, lubed-up, glistening shaft."
    else:
        m "I turned around, facing Remy's lubed-up, glistening shaft."
    
    m "Stepping over it and his hindlegs, I straddled his tail, then backed up until I felt the cold lube touch the cleft between my cheeks."

    show remy shy ud:
        xanchor 0.5
        yanchor 1.0
        transform_anchor True
        rotate 30
        xpos 0.7
        ypos 1.36
    with dissolve

    Ry shy ud leye "I-I'm really not sure y-you {i}can{/i} do this, [player_name]. M-Maybe--"
    m "Not about to give up, I lifted my ass higher, until I was able to spread my cheeks around his tip."
    Ry shy ud closed "H-Hahhh."
    m "I applied pressure gently, moving my hips and spreading my cheeks with a hand to try to give him room for entry."
    m "Even still, Remy was {size=+8}large{/size}. his head flared wide enough that even its gradual sloping wasn't quite enough to spread my ass for him."
    m "I sat for a moment, spread open but not yet penetrated, trying to catch my breath and relax further."
    show remy shy ud leye with dissolve
    menu:
        "Ask for some oral preparation.":
            c "M-Maybe you're right."
            m "Breathing heavily, I lifted myself off of his shaft, my ass recovering all too quickly from the failed penetration."
            Ry look ud "I'm s--"
            c "I think I need to ease into this with something smaller."
            show remy shy ud with dissolve
            $ renpy.pause(0.5)
            Ry "D-Do you have any, er, toys of that nature? I don't believe any were provided for you."
            if bangok_four_remy_c4postsections_store.tail_lube == True and bangok_four_remy_c4postsections_store.remy_tail_player == True:
                c "Well, no. And since you're worried about having your tail there, we can't use that to prepare. But you do have something else that's larger than most species'."
            else:
                c "Well, no. But you do have something else that's larger than most species'."
            Ry look ud "What are you talking about?"
            c "Could you prepare me a little with your tongue?"
            $ renpy.pause(0.5)
            Ry shy ud "O-Oh."
            $ renpy.pause(1.2)
            Ry shy ud "I'm... not exactly... experienced in that department."
            $ renpy.pause(0.3)
            Ry look ud "Let me go get a dental dam."
            menu:
                "A what?":
                    Ry look ud "A dental dam. It's... effectively a condom for oral intercourse."
                    Ry shy ud "I sincerely doubt I'd want to continue if I had to taste... you know."
                "Why?":
                    Ry shy ud "I sincerely doubt I'd want to continue if I had to taste... you know."
                "Sure.":
                    pass
            hide remy with dissolve
            $ renpy.pause(1.5)
            play sound "fx/slide.ogg"
            $ renpy.pause(1.5)
            show remy normal ud at center with dissolve
            m "Remy returned on three feet, carrying a what looked like a condom packet, but was even larger than the largest size condoms he'd brought out earlier."
            Ry normal ud "Ah, if you'd open this. The lighter blue bag fits over the top of my muzzle -- it has holes for me to breathe through my nostrils -- while the darker blue goes over the bottom. Try to shake it out a little first."
            m "I shook out the contents of the packet. It seemed to be three sort of bags of the same material as condoms, with the center bag shaped a little like a tongue."
            Ry shy ud "With our size difference and your lack of natural lubrication, I expect the pre-lubrication will not be sufficient either, so you might have to... apply some lube to my tongue once it's on. I think that's everything."
            c "Will you be able to talk with it on?"
            Ry look ud "Not well."
            Ry shy ud "But, ah, it's unlikely you will be able to hurt my mouth, and I will be the one in control of depth, so really it's more important that you communicate with me."
            c "Okay. Ready?"
            hide remy with dissolve
            $ renpy.pause(0.3)
            play sound "fx/undress.ogg" fadein 0.3
            m "I fit the draconic dental dam over Remy's snout and jaw. He worked his tongue into the middle tongue cover, then nodded at the bottle of lube."
            menu:
                "Squirt the lube on his tongue.":
                    m "Sticking the bottle a little into Remy's mouth, I squirted a good dollop onto his tongue. When I withdrew, Remy closed his mouth most of the way and rolled his tongue around, spreading the lube until the material of the dental dam sparkled through his lips."
                "Spread the lube with your hand.":
                    # TODO: Definitely a --mood
                    m "I squirted a large dollop of lube into my hand. Remy's eyes widened as I reached into his mouth, and he shook his head slightly, shying back."
                    m "Claws digging into the floorboards, Remy struggled to hold his position while I spread the lube around his tongue, hand immediately slipping and sliding over the dental dam material until it sparkled."
                    m "When I withdrew my hand, Remy closed his mouth and shook his head a few times, then gave me a lopsided look."
                    c "More?"
                    m "After a shake of his head, Remy nodded to the floor."
            m "I got onto my hands and knees, presenting my ass to Remy."
            m "He approached slowly, then cupped one cheek in his large paw to tug aside and expose my ass."

            m "When Remy's tongue entered me it was lukewarm, thanks to the cool temperature of the lube. But between the heat of my rear and Remy's breathing, it quickly warmed further as he pushed deeper."
            m "His tongue was tapered, the first few inches small and easily wormed into me after my attempt to take his shaft."
            m "Then Remy paused to open his mouth further over my ass, before pushing deeper at a slower pace."
            m "I spread, the smooth increase in size and the liberal application of lube a boon, only surpassed by Remy beginning to work his tongue side to side."
            m "Then his teeth ghosted over my ass, causing me to clench down."
            m "Remy tugged, fighting my ass to pull his tongue back out, working both his muscle and mine."
            m "After a moment longer with the struggling intrusion, the lube and a small amount of relaxation of my sphincter let him withdraw."
            $ renpy.pause(0.5)
            menu:
                "I-I think I'm ready to try you again.":
                    m "I heard a wet plap on the floor, then Remy coughed."
                    Ry normal ud "Thank you. I... don't think I'm a fan of that action. At least, not on someone so, ah, small."
                    c "Yeah, I could kinda feel that."
                    jump bangok_four_remy_c4postsections_mcpowerbottom_anal_rimprep
                "Could you keep going? Deeper?":
                    $ renpy.pause(0.8)
            Ry look ud "..."
            m "Remy shifted his feet, then hesitantly leaned back down to my rear."
            $ renpy.pause(0.5)
            m "This time he dove in harder and faster, maw already spread around my cheeks. Leaning down to the floor, I grabbed my ass and pulled wider, wanting to give him the best access possible, to get as much practice as I could from his tongue, in preparation for his cock."
            m "As the barest ghost of his teeth touched my skin, Remy stopped and pulled back a little, trying to avoid making that contact again."
            m "Then, experimentally, he began to thrust his tongue, forcing me wide before retreating to near his tip, only to repeat the process."
            m "The tonguefucking began to elicit soft sounds of pleasure from me. Spurred on, Remy began to explore a little more, rubbing my inner walls and tugging on my ring with his tip."
            m "I clenched down involuntarily as his tongue tugged my sphincter from the inside, rather than the center. That proved to be too much for Remy, and he pulled his tongue back out again."
            Ry look ud "Ah. No, er, grabbing."
            m "His words were heavily muffled by the draconic dental dam, the syllables blending together as he seemed to avoid hard consonants that might close his teeth on it."
            c "I don't have that much control. It's an involuntary reaction."
            m "I heard a wet plap on the floor, then Remy coughed."
            Ry look ud "Well, I'm afraid I'm having difficulty with the feeling something is grabbing my tongue like its next move is to pull it out of me."
            c "You're done?"
            Ry shy ud "If you'd please. This... this really isn't working for me."
            c "Alright."

            label bangok_four_remy_c4postsections_mcpowerbottom_anal_rimprep:
            $ renpy.pause(0.3)
            m "Remy and I switched places, with Remy lying back down where he'd begun."
            show remy normal ud:
                xanchor 0.5
                yanchor 1.0
                transform_anchor True
                rotate 30
                xpos 0.7
                ypos 1.36
            with dissolve
            m "Taking a fresh squirt of lube with me for his cock, I spread it around on his tip."
            show remy shy ud with dissolve
            m "Then I again straddled his tail, facing away."
            Ry "Whenever you're ready."
            Ry normal ud "And if it's too much, just stop and let me know."
            $ renpy.pause(0.3)
            show remy shy ud with dissolve
            $ renpy.pause(0.5)
            m "I slowly eased back onto Remy's shaft, keeping my breathing even and my rear as relaxed as I could as the new lube pressed inside, joining what Remy had deposited with his tongue."
            show remy shy ud leye with dissolve
            m "Then, my legs shaking a little from exertion, I felt the widest point on his head slip through my pucker."

        "Keep pushing.":
            m "Then, my legs shaking a little from exertion, I eased some more weight down and felt the widest point on his head slip through my pucker."

    Ry shy ud closed "Ohhhh..."
    m "Not wanting to lose the momentum, I slid down Remy's length, inch after inch of wide, thick shaft entering to spread my colon around him."
    m "The way I could feel his head pushing deeper, it was almost like having a fist up inside me, though no human arm was so smooth, so able to mold my insides to its shape."
    m "I almost didn't notice the slight taper to Remy's shaft, until I was sitting speared upon it, the smallest distance remaining between my stretched hole and taking him completely."

    Ry shy ud leye "Ngh... [player_name]?"
    c "C-Can't... quite..."
    m "I fought my breathing, the pain of the stretch telling me to hyperventilate and tense up. I raised myself slightly, feeling Remy's warm length retreat, then switched direction and pushed back down, agonizingly slowly, but keeping a steady rate."
    show remy shy ud closed with dissolve
    $ renpy.pause(0.8)
    if bangok_four_playerhasdick == True:
        if bangok_four_remy_c4postsections_store.tail_in_remy == True:
            m "It took me a moment to realize it was over, that I was sitting on Remy's hips. My balls rested on his tail, my cock rubbing against it while it twitched in Remy's ass."
        elif bangok_four_remy_c4postsections_store.ass_lube == True:
            m "It took me a moment to realize it was over, that I was sitting on Remy's hips. My balls rested in the glistening lube I'd applied to his ass."
        else:
            m "It took me a moment to realize it was over, that I was sitting on Remy's hips. My balls rested on his scales, my skin against shades of white."
    else:
        if bangok_four_remy_c4postsections_store.tail_in_remy == True:
            m "It took me a moment to realize it was over, that I was sitting on Remy's hips. My outer lips wrapped around the side of his tail, dribbling juices down to where it disappeared into his ass."
        elif bangok_four_remy_c4postsections_store.ass_lube == True:
            m "It took me a moment to realize it was over, that I was sitting on Remy's hips. My empty cunt dribbled juices into the glistening lube I'd applied to his ass."
        else:
            m "It took me a moment to realize it was over, that I was sitting on Remy's hips. My empty cunt dribbled juices onto the scales of his crotch, leaving them glistening."

    show remy shy ud with dissolve
    $ renpy.pause(0.8)


    if bangok_four_remy_c4postsections_store.tail_in_remy == True:
        jump bangok_four_remy_c4postsections_mcpowerbottom_anal_tailinremy_decision
    elif bangok_four_remy_c4postsections_store.remy_tail_player == True and bangok_four_remy_c4postsections_store.tail_lube == True and bangok_four_playerhasdick == False:
        c "Any-- Ngh. A-Any more questions about my capacity?"
        $ renpy.pause(0.5)
        menu:
            "H-Hand me your tail?":
                pass
            "I... I don't w-want to risk the tail too.":
                Ry shy ud "O-Of course. Whatever's safe, first."
                if bangok_four_remy_c4postsections_store.remy_tail_remy == True:
                    menu:
                        "Put his tail in him.":
                            jump bangok_four_remy_c4postsections_mcpowerbottom_anal_puttailinremy
                        "Continue without tailplay.":
                            pass
                jump bangok_four_remy_c4postsections_mcpowerbottom_anal_notail

        Ry shy ud leye "B-Be careful. Hold onto me as I go in."
        if bangok_four_remy_c4postsections_store.tail_protection == True:
            m "The condom-wrapped, lubricated, tapered tip of Remy's tail curled back toward me, until I could catch it and guide it down to my front entrance."
            m "The cold lubricant and smooth surface of the condom squished into my outer folds, the excess material around his tapered tip folding in."
            m "I held him there a long moment, rubbing his tip through my folds, teasing myself as I prepared my body for what was next."
        else:
            m "The lubricated, sparkling, tapered tip of Remy's tail curled back toward me, until I could catch it and guide it down to my front entrance."
            m "The lube was cold as it squished into my outer folds, insulated from his heat by his scales. The slightly rough surface of his tip was already electrifying."
            m "I held him there a long moment, rubbing his scaly tip through my folds, teasing myself as I prepared my body for what was next."

        show remy shy ud with dissolve
        m "Then, gradually, like a snake slowly sneaking away beneath a rock, his tail began to slide between my guiding hands and into me."
        $ bangok_four_remy_c4postsections_store.tail_in_player = "vag"

        if bangok_four_remy_c4postsections_store.tail_protection == True:
            m "I arched my back, tensing up, pulling in my knees and sliding a little ways up his cock as his tail entered, doubly penetrating me."
            m "The smoothing effect of the lube and condom let him slide into me easily while he remained smaller than a human penis, but he had far more tail beyond that point."
        else:
            m "I arched my back, tensing up, pulling in my knees and sliding a little ways up his cock as his rough scales entered, doubly penetrating me."
            m "The smoothing effect of the lube let him slide into me easily while he remained smaller than a human penis, but he had far more tail beyond that point."

        m "When he brushed the end of my canal I gasped and tugged, pulling him slightly back out as my legs shuddered, and I dropped back to sitting fully sheathed on his cock."
        Ry shy ud closed "Ah-!"
        Ry shy ud "[player_name], are you hurt?! I-I knew I shouldn't have--"
        menu:
            "Th-That's too deep.":
                Ry look ud "That's not much at all. If that's too deep, we might want to reconsider using my tail inside you..."
                menu:
                    "Yeah. T-Take it out.":
                        $ bangok_four_remy_c4postsections_store.tail_in_player = None
                        m "I panted as Remy slid his tail back out of me, the surface pulling out of me over my clit, even as I tried to guide it to a less over-stimulating angle."
                        m "Then he was out."
                        if bangok_four_remy_c4postsections_store.remy_tail_remy == True:
                            menu:
                                "Guide the tip to his ass.":
                                    $ bangok_four_remy_c4postsections_store.tail_in_remy = True
                                    jump todo_out_of_content_bangok_four_remy_c4postsections
                                "Let go.":
                                    m "Remy's tail flicked away, landing back on the hardwood floor with a wet splat."
                        else:
                            m "When I released it, Remy's tail flicked away, landing back on the hardwood floor with a wet splat."
                    "Keep it in.":
                        pass
            "Just didn't expect it, is all.":
                Ry shy ud "I obviously don't have direct experience, but I'm aware the cervix is... extremely sensitive. You're, ah, not deep enough to do this with safely."
                menu:
                    "Just push through it.":
                        Ry look ud "J-Just-- Th-Through?! [player_name], what part of extremely sensitive are you not understanding?"
                        Ry shy ud "I thought you just felt what happened when I barely flicked it."
                        Ry look ud "I haven't ever... I know some {i}extremely rare{/i}..."
                        menu:
                            "I can take it.":
                                Ry look ud "[player_name], I... I don't..."
                                m "Hesitantly, his tail began to slither deeper inside me again, before his tip prodded my inner gate."
                                m "I hissed, arching my back again from the small explosion of pain and pleasure."
                                Ry shy ud "Are you sure?"
                                menu:
                                    "I'll be fine.":
                                        $ bangok_four_remy_c4postsections_store.tail_in_player = "womb"
                                    "O-Okay. No. K-Keep it where it is.":
                                        pass
                            "Nevermind. Keep it where it is.":
                                pass
                    "Keep it in anyway.":
                        pass

        if bangok_four_remy_c4postsections_store.tail_in_player == "vag":
            c "Just, ah, we'll control its depth."
            label bangok_four_remy_c4postsections_mcpowerbottom_anal_taildepthcontrol:
            m "I looked over at the couch."
            c "Can I borrow your shirt collar?"
            Ry shy ud "I suppose..."
            m "Taking his shirt collar from the couch, I bound his tail against its base with his shirt collar, keeping him from getting any more tail to slip into me."
            Ry shy ud leye "O-Oh. Th-That works. Very tight, though."
        elif bangok_four_remy_c4postsections_store.tail_in_player == "womb":
            m "I doubled over, holding my belly, legs limp as I sat with Remy's cock in my ass and his tail tip deep in my canal, prodding my deepest gate as he sought the entryway yet deeper."
            m "Then he found the tiny opening, his poke spreading it wider around his tapered tip."
            if bangok_four_remy_c4postsections_store.tail_protection == True:
                m "I grabbed his tail and pulled, swooning as his condom-wrapped, lubed taper smoothly spread my cervix. He resisted slightly, worried, but I encouraged him onward as the thickening slide through my outer lips and inner gate drove me up toward my peak."
            else:
                m "I grabbed his tail and pulled, swooning as his rough, lubed scales speared my cervix. He resisted slightly, worried, but I encouraged him onward as the thickening friction through my outer lips and inner gate drove me rapidly toward my peak."
            show remy shy ud closed
            show black
            with fadequick
            m "Then I came, my spread passage and ass spasming as they tried and failed to clench down on the large insertions filling me."
            $ renpy.pause(1.0)
            hide black with dissolveslow
            m "I came back down lying on Remy's belly, his cock and tail both twitching inside me ever so slightly as he struggled to hold his position."
            Ry look ud "A-Are you ok?"
            menu:
                "Fine.":
                    show remy normal ud with dissolve
                "Never better.":
                    show remy shy ud with dissolve
                "[[Kiss him.]":
                    m "Reaching up, I tugged on his chin with a few fingers, guiding his head closer. Then, when he was in range, I lifted my head to kiss him."
                    show remy shy ud with dissolve
                    $ bangok_four_remy_c4postsections_store.remy_kissed = True
                    m "It turned into a brief peck as he abruptly pulled away, blushing furiously."
            m "I picked myself up on his chest, sheathing back inside me the small bit of cock and tail that had slid out when I'd cum."
            m "Then, abruptly, I ran out of womb for his almost ramrod-straight tail inside me."
            c "Ngh!"
            Ry look ud "[player_name]?"
            if bangok_four_remy_c4postsections_store.tail_protection == True:
                m "I guided a little tail out of myself, but stopped before he could get the wrong idea and pull the smooth, tapered length out of me completely."
            else:
                m "I guided a little tail out of myself, but stopped before he could get the wrong idea and pull the rough scales out of me completely."

            if persistent.bangok_inflation == True:
                menu:
                    "We, ah, need some way to control your depth.":
                        jump bangok_four_remy_c4postsections_mcpowerbottom_anal_taildepthcontrol
                    "Can you relax your tail? Coil it inside me?":
                        Ry shy ud leye "I... I can try..."
                        $ bangok_four_remy_c4postsections_store.tail_in_player = "wombfold"
                        jump bangok_four_remy_c4postsections_mcpowerbottom_anal_wombfoldtail
            else:
                c "We, ah, need some way to control your depth."
                jump bangok_four_remy_c4postsections_mcpowerbottom_anal_taildepthcontrol
        else:
            $ renpy.error("How did you get bangok_four_remy_c4postsections_store.tail_in_player = \"%s\"?"%bangok_four_remy_c4postsections_store.tail_in_player)







        jump todo_out_of_content_bangok_four_remy_c4postsections
    elif bangok_four_remy_c4postsections_store.remy_tail_remy == True:
        label bangok_four_remy_c4postsections_mcpowerbottom_anal_notail_choice:
            menu:
                "Put his tail in him.":
                    jump bangok_four_remy_c4postsections_mcpowerbottom_anal_puttailinremy
                "Continue without tailplay.":
                    pass
        jump bangok_four_remy_c4postsections_mcpowerbottom_anal_notail
    else:
        jump bangok_four_remy_c4postsections_mcpowerbottom_anal_notail

label bangok_four_remy_c4postsections_mcpowerbottom_anal_notail:
    Ry shy ud leye "Y-You're so t-tight. A-Are you okay?"
    c "Y-Yeah. I think."
    Ry shy ud ud "O-Once you start moving I... I don't think I'll last very long."
    Ry shy ud leye "S-Sorry."


    jump todo_out_of_content_bangok_four_remy_c4postsections


label bangok_four_remy_c4postsections_mcpowerbottom_anal_puttailinremy:
    c "Do you want your tail in you, now?"
    Ry shy ud leye "I..."
    Ry shy ud closed "Very much so."
    if bangok_four_remy_c4postsections_store.tail_protection == True:
        m "Remy flicked his tail up off the floor. I had to lean forward slightly to grab the slick, rubbery muscle's condom-wrapped surface to guide down to his hole. It tugged slightly through my grip, already anticipating what was to come."
    else:
        m "Remy flicked his tail up off the floor. I had to lean forward slightly to grab the muscle's slick, but also rough surface to guide down to his hole. It tugged slightly through my grip, already anticipating what was to come."
    $ renpy.pause(0.3)
    Ry shy ud closed "Mmnh."
    $ bangok_four_remy_c4postsections_store.tail_in_remy = True
    $ renpy.pause(0.3)
    m "Remy's tail burrowed inside him, inch after inch disappearing, sliding easily enough with the lubrication I'd added."
    if bangok_four_remy_c4postsections_store.tail_lube == True and bangok_four_remy_c4postsections_store.ass_lube == True:
        m "The double layer of lube from his tail and ass squished and spattered over his backside in glistening droplets."
    Ry shy ud leye "Could you... Would you mind pulling on it? My own muscles can only bend it over so far, and when it gets wider..."
    m "I gave his lubricated tail a squeeze."
    c "I'll try. Hard for me to bend over with- Ah--! ... with you being so big."
    if bangok_four_remy_c4postsections_store.tail_protection == True:
        m "I took hold of Remy's tail where it curved over, just before the condom began, then gently began to pull, feeding more into his spreading asshole."
        if bangok_four_playerhasdick == True:
            m "As his tail entered deeper into him, it widened enough for its slick surface to rub past my balls and tip, giving back to me a fraction of what Remy had to be feeling."
        else:
            m "As his tail entered deeper into him, it widened enough for its slick surface to tickle past my outer folds and, as I leaned into it, my clit, giving me a fraction of what Remy had to be feeling."
    else:
        m "I took hold of Remy's tail where it curved over, then gently began to pull, feeding more into his spreading asshole."
        if bangok_four_playerhasdick == True:
            m "As his tail entered deeper into him, it widened enough for his rough scales to rub past my balls and tip, giving back to me a fraction of what Remy had to be feeling."
        else:
            m "As his tail entered deeper into him, it widened enough for his rough scales to tickle past my outer folds and, as I leaned into it, my clit, giving me a fraction of what Remy had to be feeling."
    Ry shy ud closed "Nnh..."
    c "Ohhh..."
    m "His cock twitched noticeably inside me as I felt his tail move inside him."
    Ry shy ud "I... think that's as far as I'll take it, u-unless you plan to push me over my peak this way. I-I don't know how much you can feel, or want me to..."
    jump bangok_four_remy_c4postsections_mcpowerbottom_anal_tailinremy_decision


label bangok_four_remy_c4postsections_mcpowerbottom_anal_tailinremy_decision:
    m "I considered playing with Remy's tail."
    jump todo_out_of_content_bangok_four_remy_c4postsections


label bangok_four_remy_c4postsections_mcpowerbottom_anal_wombfoldtail:
    m "After a moment, I felt his tail twist a little, then rub against the walls of my deepest center. My spread cervix felt every motion, electric sparks dancing through my lower body."
    if bangok_four_remy_c4postsections_store.tail_protection == False:
        m "I winced, his scales not gentle so deep inside of me. But the pain only served to feed the pleasure, like fuel to the fire, hieghtening the experience."
    show remy shy ud closed with dissolve
    m "With a little more confidence he could safely navigate my womb, Remy began to gently sink more tail into me, his taper spreading my outer folds now larger than any human shaft."
    m "My inner gate widened further, forced open by the inevitable taper of his tail. What he had inside me began to circle back, pressing outward on my womb's walls."
    if bangok_four_remy_c4postsections_store.tail_protection == True:
        m "My channel spread, a sleeve for his tail, slipped on like the condom had been as he spread my innermost center with his long, prehensile limb of smooth, protected meat."
    else:
        m "My channel spread, a sleeve for his tail, slipped on like any other article of clothing as he spread my innermost center with a long, prehensile limb of scaly meat."
    m "I felt myself forced to expand, belly pressed outward by the long, sinuous muscle slithering into my womb. Looking down, I could see my belly bulging slightly, pregnant with Remy's tail as it snaked inside me."
    m "Finally, he stopped, leaving me stuffed with tail. Between my legs, it spread me wider than his shaft spread my ass, wide enough I couldn't close my legs if I'd wanted to."
    if bangok_four_remy_c4postsections_store.tail_protection == True:
        m "I could barely make out the ring of the condom, under an inch from disappearing within me."

    m "I rested a hand on my belly."
    Ry shy ud "H-How's that?"
    m "With his shaft in my ass twitching against my new pregnancy of dragon tail, I wasn't sure how long I could hold off another orgasm."
    $ renpy.pause(0.5)
    c "I... ah... don't think I can move enough to help you..."
    $ renpy.pause(0.8)
    Ry look ud "..."
    c "Little help?"
    m "Maneuvering his hindlegs, Remy awkwardly got a grip on my sides."
    Ry normal ud "Tell me if I need to stop, please."
    m "Then he began to lift me a little off his manhood."
    show remy shy ud closed with dissolve
    m "His tail had to slide a little out of my widened pussy to give him the slack to lift me, the coils inside twisting and tightening as a few inches pulled back through my cervix."
    show black with fadequick
    m "When he stopped to switch directions, I came again, my spread cunt trying with spasming muscles to squeeze off the pregnancy of dragon tail and keep it inside."
    $ renpy.pause(1.0)
    hide black
    show remy shy ud leye
    with dissolvemed
    $ renpy.pause(0.5)
    m "I came back to Remy holding me carefully in place, riding out my orgasm and clenched ass."
    c "S-Sorry."
    m "I struggled to relax. Then, gradually, Remy let me sink back down his length, spreading my cheeks and spearing my sphincter with a log of cock."
    m "The knot of tail in my womb held its place, not getting any deeper, denying me the sliding motion of tailfucking that might get me to another orgasm."
    m "Remy lifted me again, then let me back down, this thrust easier on my ass than the last as my muscle grew weaker and more tired."
    m "Then his tail shifted a little, coils shifting toward my back, pressing against his shaft for his next thrust."
    play soundloop "fx/bangok_panting_1dot8.ogg" fadein 8.0
    show remy shy ud closed with dissolve
    m "The fucking increased slightly in tempo, as much as Remy could manage having to lift me bodily with each thrust. He panted, those same noises I'd heard back in the library, now undeniably because of me and my body."
    m "He began to move his tail again, coiling and uncoiling just a little bit deep inside me, slack sliding through my cervix and canal, dragging me toward another peak whether I was ready or not."
    if persistent.bangok_knot == True:
        Ry "K-Knot inside?"
        menu:
            "Fill me.":
                $ bangok_four_remy_c4postsections_store.knot_pos = True
            "W-Wait, don't--!":
                $ bangok_four_remy_c4postsections_store.knot_pos = False
    stop soundloop fadeout 0.5
    show black with fadequick
    m "I came, conscious thought abandoning me as I tugged on his tail, trying to fit yet more inside my expanded belly."
    play sound "fx/snarl.ogg" fadein 0.3
    if (persistent.bangok_knot == True and bangok_four_remy_c4postsections_store.knot_pos == True) or persistent.bangok_knot == False:
        m "Two faster thrusts, his tail twitching inside me, then Remy pulled me all the way down to the base of his shaft, spreading me as wide as my ass could possibly go."
    else:
        m "Two faster thrusts, his tail twitching inside me, then Remy stopped abruptly only halfway in."

    if bangok_four_remy_c4postsections_store.shaft_protection == True:
        m "His length twitched, then began delivering spurt after hot spurt into the condom tip, deeper than any human could ever cum."
    else:
        m "His length twitched, then began delivering spurt after hot spurt into my guts, deeper than any human could ever cum."
    m "The load was huge, pulses pressing my sphincter just that little bit wider as each jet worked its way up from Remy and into me."
    if bangok_four_remy_c4postsections_store.shaft_protection == True:
        m "The balloon of cum bloated, spreading my inner walls outward and stretching down my colon as he kept cumming, until the pressure was pressing his tail in my womb away from his shaft, forcing my belly to expand to appear even more pregnant with dragon."
    else:
        m "The cum flooded me, pouring deep into my colon until my ass was stuffed, then continuing to spurt in until the pressure on my innards was pressing his tail in my womb away from his shaft, forcing my belly to expand to appear even more pregnant with dragon."

    if (persistent.bangok_knot == True and bangok_four_remy_c4postsections_store.knot_pos == True) or persistent.bangok_knot == False:
        if persistent.bangok_knot == True:
            m "I could feel the cum flowing, pressing, seeking any way out of me, even back along Remy's shaft. But my ass was no escape, as a massive knot of flesh wider than my rear could ever spread held me fast against Remy."
        else:
            m "I could feel the cum flowing, pressing, seeking any way out of me, even back along Remy's shaft. But my ass was no escape, as my stretched pucker held fast, spread already to its limit against his thick length."
        hide black with dissolveslow
    else:
        m "I could feel the cum flowing, pressing, seeking any way out of me, even back along Remy's shaft. Ropes of white dribbled from my spread rear, not as spread as it could have been had I been fully filled with his shaft."
        hide black with dissolveslow
        m "Then Remy let me down, gently, onto a knot of flesh so wide it hardly fit between my cheeks, and would never fit inside me."

    $ renpy.pause(0.8)
    m "A few moments of silence passed between us, panting and gasping from the incredible fuck."
    m "Then Remy tugged in his wing, spread on the floor, and with his other, tipped us over onto his side."
    hide remy with dissolve
    play sound "fx/bed.ogg"
    scene o2:
        ypos -400 xpos -128
    with vpunch
    c "Oof!"

    m "The cum inside me sloshed and flowed, liquid weight now resting on my side instead of my pelvis causing my belly to bloat a little bit further."
    play sound "fx/craphug.mp3"
    m "Then Remy tugged me closer to him with his forelegs, hugging me."
    Ry smile ud "Thank you."
    menu:
        "Th-Thank me when you're out of me.":
            # TODO: Mood--
            pass
        "Same to you.":
            c "That... That was incredible."
        "[[Kiss him.]":
            show black with dissolvemed
            if bangok_four_remy_c4postsections_store.remy_kissed == True:
                m "Unlike last time, when I tugged on Remy's chin, he wasn't confused about what I wanted."
                label bangok_four_remy_c4postsections_mcpowerbottom_anal_wombfoldtail_kiss:
                m "Our lips met, then his parted, offering tongue."
                m "For a few seconds, with him stuffing two of my holes full, I accepted him into a third."
                m "Just after we parted, he finished by giving me a small lick on the cheek."
                hide black with dissolvemed
                if remystatus == "neutral":
                    Ry shy ud "That's... that's the second time you've done that. You..."
                    Ry shy ud "[player_name], I-I thought you wanted this casually. I thought you wanted just to be friends."
                    menu:
                        "I didn't know you were so interested.":
                            c "Now that I do, though, I'll admit it too: I like you as more than just a friend."
                            $ remystatus = "good"
                            m "Remy nuzzled my head, planting a few more licks."
                            Ry shy ud "I wasn't sure when you did it the first time, but I'd hoped..."
                        "Friends can't share some kisses during a good fuck?":
                            Ry look ud "Oh. That... that's all it meant to you?"
                            $ renpy.pause(0.5)
                            c "Did it mean something more to you?"
                            Ry look ud "Nevermind."
                            $ renpy.pause(0.8)
                else: # good
                    c "Guess that seals the deal."
                    Ry normal ud "I suppose it does."
            else:
                $ bangok_four_remy_c4postsections_store.remy_kissed = True
                m "Reaching up, I tugged on his chin with a few fingers, guiding his head closer. Then, when he was in range, I lifted my head to kiss him."
                if remystatus == "good":
                    jump bangok_four_remy_c4postsections_mcpowerbottom_anal_wombfoldtail_kiss
                else:
                    m "It turned into a brief peck as he abruptly pulled away, blushing furiously."
                    hide black with dissolve
                    Ry shy ud "[player_name], I-I thought you wanted this casually. I thought you wanted just to be friends."
                    menu:
                        "I didn't know you were so interested.":
                            c "Now that I do, though, I'll admit it too: I like you as more than just a friend."
                            $ remystatus = "good"
                            m "Remy hesitated, then leaned back down."
                            show black with dissolvemed
                            jump bangok_four_remy_c4postsections_mcpowerbottom_anal_wombfoldtail_kiss
                        "Friends can't share a kiss after a good fuck?":
                            Ry shy ud "N-No that... I..."
                            $ renpy.pause(0.5)
                            Ry normal ud "That's a little too strange for me."
                            c "Fine."

    
    m "His tail twitched inside my womb, and I hissed."
    Ry normal ud "R-Right. Apologies."
    jump todo_out_of_content_bangok_four_remy_c4postsections




label bangok_four_remy_c4postsections_mctop_vag:
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
    scene o3 at Pan((0, 100), (0, 250), 3.0) with dissolveslow
    $ renpy.pause (1.3)

    m "I returned home utterly spent after the long night. After this fateful day, I was glad to finally have some sort of respite."
    # TODO: Add alternates of this line
    m "My stomach rumbled quietly, the lack of lunch or dinner weighing heavy on my energy."
    m "Then, I suddenly found my remaining strength leaving me and collapsed to the floor."
    jump bangok_four_remy_c4postsections_epilogue_admin