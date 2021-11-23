init python in bangok_four_remy_c4postsections_store:
    remy_top = False
    remy_tail_player = None
    remy_tail_remy = None

    protection = None



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
            or (bangok_four_bryce3.unplayed == False and bangok_four_bryce3.mc_bottom == True)
            or (bangok_four_xipsum.unplayed == False and bangok_four_xipsum.took_ipsum_both == True)
            or (bangok_four_xkatsu.unplayed == False and bangok_four_xkatsu.target in ["throat","vag","womb","ass"])):
            $ bangok_four_remy_c4postsections_store.remy_top = True
            Ry look dk "[player_name], I'm not sure you understand..."
            
            if (bangok_four_bryce3.unplayed == False and bangok_four_bryce3.mc_bottom == True):
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
    c "So, you’re a fan of putting that tail to good use, I'm guessing?"
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
    play sound "fx/rummage.ogg"
    m "Remy disappeared into the bathroom. I heard some light boxes falling from inside my bathroom cabinet's low shelves, plus something heavier."
    $ renpy.pause(1.0)
    play sound "fx/slide.ogg"
    show remy shy at center with dissolve
    m "Remy returned nosing three boxes of condoms and a bottle of lube along the floor."

    c "Protection?"
    Ry "It's not strictly necessary, with us being not just different species but of wildly differing taxonomic classes. But I'm not sure if you..."
    menu:
        "Probably a good idea.":
            $ bangok_four_remy_c4postsections_store.protection = True
        "Nah, don't worry about it.":
            $ bangok_four_remy_c4postsections_store.protection = False

    Ry "The, ah, lube is strictly necessary. No question."
    c "Alright."

    $ renpy.pause (0.8)
    m "We stood, staring at each other for a few moments."
    $ renpy.pause (0.8)

    c "I guess I'll undress first?"
    Ry "Th-That would be an instrumental step in--"
    play sound "fx/undress.ogg"
    show remy look with dissolve
    m "I lifted my shirt up over my head, setting it aside on a couch."
    Ry shy "..."
    Ry "... Er..."
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
                play sound "fx/undress.ogg"
                m "I shrugged back into my shirt, in an effort to make Remy more comfortable."
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
            "[[Keep undressing.]":
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

    c "I'd ask you to take off your shirt too, but you're just wearing a shirt collar."
    c "Speaking of which, I've never actually seen you without your tie."
    Ry "Well..."
    hide remy with dissolve
    $ renpy.pause(0.3)
    play sound "fx/undress.ogg"
    $ renpy.pause(2.0)
    show remy normal b with dissolve
    m "Heaving a sigh, Remy undid his tie and draped it on the couch next to my shirt."

    menu:
        "You are pretty cute, you know that?":
            pass
        "That's a lot of neck.":
            pass
    Ry shy b "I... suppose."





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