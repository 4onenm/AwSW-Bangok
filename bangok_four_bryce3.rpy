init python in bangok_four_bryce3:
    unplayed = True
    maverick_in = False
    sebastian_in = False

    mc_bottom = True
    protection = False

    # Menu options
    top_mav = True




label bangok_four_bryce3_skipmenu:
    play sound "fx/system3.wav"
    s "Join the team-building exercise?"
    menu:
        "Yes. Join the team-building exercise.":
            play sound "fx/system3.wav"
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ bryce3mood = 2
            show bryce at Position(xanchor = 1.0, xpos = 1.175)
            show sebastian normal flip at left
            show maverick normal behind bryce at Position(xpos=0.825)
            show zhong normal flip at Position(xpos = 0.05)
            with Fade(0.5,0.5,1.0)
            play music "mx/hydrangea.ogg" fadein 2.0
            jump bangok_four_bryce3_intro
        "No. Have a nonsexual BBQ.":
            pass
    jump bangok_four_bryce3_skip_return





label bangok_four_bryce3_intro:
    Br laugh "Wait, you're out too? What about the best part?"
    c "Best part?"
    Br smirk "A bit of teambuilding, a bit of exercise."
    Zh shy "A bit of poor decision making in which I will not be involving myself."
    Br normal "Oh don't be like that. You don't have to sit every one of these out."
    Zh "I'd prefer to."
    Br smirk "Don't get lost in the dark, then."
    hide zhong with easeoutleft
    if bangok_four_xsebastian_unplayed == False:
        show sebastian shy flip with dissolve
    Sb "You're not actually proposing this in front of the ambassador, are you?"
    Mv angry "Really, Bryce. This is too far, even for you."
    menu:
        "What is \"this\"?":
            pass
        "Is \"this\" what I think it is?" if bangok_four_bryce1_unplayed == False:
            pass
        "I get the feeling we might still need the babysitter.":
            $ renpy.pause (0.5)
            $ bryce3mood -= 1
            Br stern "We're all adults here. We can have an adult conversation about this."
    Br normal "It's just a bit of casual sex between friends. You don't all have to make a big deal about inviting one more."
    Sb disapproval flip "It is if you didn't discuss it with anyone else first."
    Br laugh "Oh come on. We haven't started. This {i}is{/i} the discussion."
    if bangok_four_bryce1_unplayed == False:
        Br normal "What do you say, [player_name]? Up to have a bit of fun again?"
        if bangok_four_xsebastian_unplayed == False:
            show sebastian shy flip with dissolve
        Sb "Again?"
    else:
        Br normal "What do you say, [player_name]? Up to get a little closer to the rest of the team?"
    menu:
        "No thanks.":
            Mv "Even [player_name] doesn't want it."
            Mv normal "The least discussion you could have had was with the person you were surprising us with."
            Mv angry "But instead you--"
            Br stern "I get it, fine. None of you are interested."
            Br brow "I'm sorry for trying to keep some semblance of normality around here."
            Sb normal flip "I'd say the BBQ went well enough. And there's always next year."
            Br stern "True enough I suppose."
            Sb disapproval flip "With that, I'm off. See you all tomorrow."
            hide sebastian with dissolve
            Br brow "Maverick?"
            Mv normal "..."
            Mv normal "Thanks for inviting me, Bryce."
            Br normal "Of course. Wouldn't be the same without you."
            m "Maverick gave me one more look before slinking off into the night."
            $ renpy.pause (0.3)
            hide maverick with dissolve
            $ renpy.pause (0.5)
            show bryce at center with ease
            $ renpy.pause (0.3)
            Br brow "Sorry for springing that on you. I didn't want it to look to Maverick like I was coaching you before you came over."
            if bangok_four_bryce1_unplayed == False:
                Br "I thought after last time you'd be interested in..."
                Br flirty "I thought after last time you'd be interested in{fast} further expanding your horizons."
            menu:
                "I was drunk last time." if bangok_four_bryce1_unplayed == False:
                    Br sad "..."
                "I don't do groups.":
                    Br sad "Ah. Sorry. I really messed that up, then."
                "Don't worry about it.":
                    show bryce sad with dissolve
                    c "Just wasn't feeling it, especially because they weren't."
                    Br sad "Still. It's my fault for assuming all this would just work out."
            $ renpy.pause(1.2)
            jump bangok_four_bryce3_playershouldleave
        "I don't want to get in the way of you all...":
            $ bryce3mood -= 1
            Mv "There is no getting in the way. Nothing is happening."
            Mv normal "Naomi is the only one as interested in the exercise as you. She's not here."
            Mv angry "And I'm not even part of your team right now. Thanks to--"
        "I would if they want to.":
            Mv normal "Then it's settled, because we are not."
            Br brow "Aren't you kinda speaking for Sebastian there?"
            Mv angry "No member of our police force should be proposing something like this with one of {i}them{/i}. Especially not--"
        "Sounds fun.":
            $ bryce3mood -= 1
            Mv angry "We're not here for your enjoyment. Can't--"
    
    show sebastian disapproval flip with dissolve
    Br stern "I thought you agreed to keep this civil. Getting angry about things we're trying to leave out of tonight doesn't qualify in my book."
    if bryce3mood < 2:
        Mv "They are the only known associate of the lone suspect in three murders."
        Mv "Sleeping with a suspect's associate doesn't qualify as proper police work in my book."
        $ renpy.pause (1.2)
        Sb "Let's just call it a night and all go home."
        Sb "Mavers?"
        Mv normal "..."
        Mv "Fine."
        hide maverick with dissolve
        Sb "Until next year."
        Br sad "Yeah, yeah."
        hide sebastian with dissolve
        $ renpy.pause (0.5)
        show bryce at center with ease
        $ renpy.pause (0.3)
        Br brow "Sorry for springing that on you. I didn't want it to look to Maverick like I was coaching you before you came over."
        Br sad "It's my fault for assuming all this would just work out like normal."
        c "Hey, it's not so bad. Most of the BBQ went well."
        Br normal "'Spose that's true."
        $ renpy.pause (1.2)
        jump bangok_four_bryce3_playershouldleave

    Br normal "[player_name] has done their best to fit in and participate tonight. The least you could do is the same."
    $ renpy.pause(0.8)
    $ bangok_four_bryce3.maverick_in = True
    Mv normal "..."
    $ renpy.pause(0.4)
    Mv "Sebastian, where do you sit with this?"
    if bangok_four_xsebastian_unplayed == False:
        $ bangok_four_bryce3.sebastian_in = True
        Sb shy flip "I, ah. I'm for this."
        Sb drop flip "Though I can't bottom like normal for you two if I'll be on shift tomorrow morning."
    else:
        Sb drop flip "I'm not going to take sides on what you three should be doing."
        Sb disapproval flip "I know my shift starts early tomorrow morning, and that's my excuse to bow out."
        Br normal "That's fair. Get a good night's rest in."
        Sb normal flip "Thanks. Until next year."
        hide sebastian with dissolve
        $ renpy.pause(0.5)
        Mv "Bryce, if you're offering, you're bottoming."

    Br normal "I can do that."
    if bangok_four_bryce1_unplayed == False:
        show bryce flirty with dissolve
    else:
        show bryce smirk with dissolve
    Br "I can do that. {fast}Unless [player_name] would like to?"

    $ bangok_four_bryce3.mc_bottom = True # Used temporarily for a conversation option
    $ bangok_four_bryce3.top_mav = True
    label bangok_four_bryce3_bottom_choice:
    menu:
        "Wait, bottom all three of you?" if (bangok_four_bryce3.mc_bottom == True) and (bangok_four_bryce3.sebastian_in == True):
            show sebastian normal flip with dissolve
            $ bangok_four_bryce3.bottom_choice_clarification = False
            if bangok_four_bryce1_unplayed == False:
                Br smirk "I think you can manage it."
            else:
                Br normal "It's just a thought. You don't have to take it seriously."
            jump bangok_four_bryce3_bottom_choice
        "Wait, bottom both of you?" if (bangok_four_bryce3.mc_bottom == True) and (bangok_four_bryce3.sebastian_in == False):
            $ bangok_four_bryce3.bottom_choice_clarification = False
            if bangok_four_bryce1_unplayed == False:
                Br smirk "I think you can manage it."
            else:
                Br normal "It's just a thought. You don't have to take it seriously."
            jump bangok_four_bryce3_bottom_choice
        "Why isn't Maverick...?" if bangok_four_bryce3.top_mav == True:
            $ bangok_four_bryce3.top_mav = False
            Mv angry "I won't be beneath you."
            Sb disapproval flip "Don't ask Maverick to bottom. He's not a fan."
            Br brow "Understatement."
            jump bangok_four_bryce3_bottom_choice
        "I'll bottom.":
            $ bangok_four_bryce3.mc_bottom = True
            show maverick nice
            if bangok_four_bryce3.sebastian_in == True:
                show sebastian shy flip
                show bryce flirty
                with dissolve
                $ renpy.pause(0.3)
                Br "Oh?"
                Sb "You sure, [player_name]? That's not a statement to be made lightly."
                Sb drop flip "At least Bryce is in the size class to take Maverick."
                Sb shy flip "You're, ah..."
                Br smirk flip "[player_name] will be fine. I stashed some supplies up here in the rocks. And if it's too much, I'll take over."
                hide bryce with easeoutright
            else:
                show bryce flirty
                with dissolve
                Br "Oh?"
                $ renpy.pause (0.5)
                Br smirk flip "Alright. Let me go get the supplies I stashed."
        "Don't let me stop you, Bryce.":
            $ bangok_four_bryce3.mc_bottom = False
            show maverick normal
            show bryce laugh
            Br "It's not my usual thing."
            Br normal "But I don't mind."
            Br normal flip "Alright. Let me go get the supplies I stashed."


    hide bryce with easeoutright
    $ renpy.pause (0.5)
    Sb drop flip "Of course you brought supplies, even without talking it over with any of us."
    menu:
        "Maverick, are you okay with this?":
            Mv angry "It changes nothing."
            Mv normal "But Bryce has asked us to leave those concerns out of tonight. I will if you will."
            c "Consider it done, then."
        "Does he do that a lot?":
            c "You know, stash stuff in advance?"
            Mv normal "Yes."
            $ renpy.pause(1.2)
            m "I waited, but Maverick did not elaborate."


    show bryce normal at Position(xanchor = 1.0, xpos = 1.175) with easeinright
    m "Bryce returned with an open-top wicker basket, handle clenched in his teeth. A sizeable bottle of lube and four open boxes of condoms peeked out."
    Br "So. We've got condoms and lube. Should fit everyone."
    if bangok_four_bryce3.sebastian_in == True:
        if bangok_four_bryce3.mc_bottom == False:
            Br laugh "Personally I don't care, but Seb, if you want to skip cleaning yourself up later."
        else:
            Br "Seb, if you want to use one and skip most of the cleanup from ass and sloppy seconds..."
        Br smirk "Or you could take a dip in the ocean."
        Sb disapproval flip "I'd rather use protection than have sand up there, thanks."
    else:
        if bangok_four_bryce3.mc_bottom == False:
            Br "I don't give a damn about the condoms tonight."
            Br laugh "Gotta clean myself up later anyway."
            Br normal "But if either of you want 'em."
            
    if bangok_four_bryce3.mc_bottom == False:
        menu:
            "Take a condom.":
                $ bangok_four_bryce3.protection = True
            "Go without.":
                $ bangok_four_bryce3.protection = False
    else:
        Br normal "So [player_name], normally we'd just go at it without protection. But I'm guessing you weren't expecting two dragonloads tonight, so if you'd like us to use them..."
        menu:
            "I'd prefer if you used condoms.":
                $ bangok_four_bryce3.protection = True
                Br normal "Sure."
            "I'm fine going unprotected.":
                $ bangok_four_bryce3.protection = False
                Br smirk "Alright."

    c "I should go strip, then."
    Br smirk "Go strip? Why not do that here?"
    if bangok_four_bryce3.sebastian_in == True:
        Sb normal flip "We're going to see you without your clothes before the night is over anyway."
    Mv normal "You may as well show us what you're hiding now."
    Br stern "Maverick."

    m "Swallowing my hesitation, I stripped out of my upper clothes before I could think about it, then dropped my drawers into the sand."

    if bangok_four_playerhasdick is None:
        menu:
            "The cool night air tickled my dick.":
                $ bangok_four_playerhasdick = True
            "The cool night air teased my lower lips.":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick:
        m "The cool night air tickled my dick, eliciting a small rush of blood and a twitch."
        if bangok_four_bryce1_unplayed == True:
            Br smirk "Guessing you're a guy, then."
    else:
        m "The cool night air teased my lower lips, eliciting a small rush of blood that left my groin flushed and warm."
        if bangok_four_bryce1_unplayed == True:
            Br brow "Does something come out of that, or...?"
            c "No. It's not a slit for a penis."
            Br flirty "Oh."

    if bangok_four_bryce3.mc_bottom == True:
        jump bangok_four_bryce3_mcbottom
    else:
        jump bangok_four_bryce3_mctop


label bangok_four_bryce3_mcbottom:
    $ renpy.pause(0.5)
    if bangok_four_bryce3.protection == True:
        Br stern "Do have to say, if you want me and Maverick wearing protection, you're going to have to get it on."
        c "Shouldn't it have been designed with your species putting it on in mind?"
        Br brow "It sorta was. But they didn't design it to also deal with sand on our paws."
        Br laugh "Oh the rare curses of four feet."
        c "Alright."
        scene beachx at Pan ((300, 0), (300, 0), 0.0) with dissolve
        m "I knelt in the sand next to the basket, briefly searching through the condom boxes in the moonlight "


label bangok_four_bryce3_mctop:
    jump todo_out_of_content_bangok_four_bryce3

label todo_out_of_content_bangok_four_bryce3:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")