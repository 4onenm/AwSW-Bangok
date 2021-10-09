init python in bangok_four_xipsum:
    unplayed = True
    mood = 0
    clothesoff = False
    
    # Player has a dick or a vagina. Sorry Lorems of the world.
    playerhasdick = None

    loremin = False
    fuckertarget = None
    fuckeraction = None
    suckingipsum = False
    
    playercame = False



label bangok_four_xipsum_takeemoff:
    $ renpy.pause (0.5)
    Ip normal "I'm just saying it would be hard to study an insect if there was a piece of cloth draped over it. Wearing that much just seems odd to me."
    Lo normal flip "If humans wear clothes like this, it's only appropriate to depict them as such."
    Ip think "Well [player_name], you did propose taking them off. What are the circumstances under which humans wear clothes versus not?"
    c "Exposing yourself around around other people is generally taboo, unless those other people are family or intended sexual partners."
    Ip happy "If that's all you need, I'd be quite interested in arranging that for you."
    Lo think flip "I don't think any members of [player_name]'s family are able to come over to our--"
    Lo shy flip "Oh."
    Lo relieved flip "Ipsum. Really? {w=0.9}I'm sorry [player_name]. He didn't mean it like that."
    Ip "Didn't I?"
    menu:
        "Accept.":
            python in bangok_four_xipsum:
                unplayed = False
                clothesoff = True
                mood += 1
                renpy.pause (0.5)
            c "I'd be interested in that arrangement as well."
            Lo shy flip "Not you too..."
        "Reject.":
            $ renpy.pause (0.5)
            c "Yeah, that's not for me."
            jump bangok_four_xipsum_unsatisfied
        "Clothes off, nothing more.":
            python in bangok_four_xipsum:
                clothesoff = True
                renpy.pause (0.5)
            Ip normal "I'll take what I can get."
    Lo "Just let me finish drawing you with your \"vestments\" {i}on{/i} first, alright?"
    c "Am I going to have to stand like this again once they're off?"
    Lo think flip "I guess that depends on how different you look."
    jump bangok_four_xipsum_vestment_variety

label bangok_four_xipsum_cute:
    $ renpy.pause(0.5)
    Ip sad "Cute? You must be joking."
    Lo normal flip "You are never going to live that description down."
    Ip "Oh dear..."
    jump bangok_four_xipsum_cute_end

label bangok_four_xipsum_donewithclothed:
    menu:
        "Really? But staring at the wall was so much fun.":
            $ renpy.pause (0.5)
            $ lorem2mood += 1
        "Sure.":
            $ renpy.pause (0.5)
    c "So does this mean I take off my clothes now?"
    Ip happy "That would be the main event, yes."
    Lo shy flip "I mean, if you're still comfortable with that. I don't want you breaking any taboos if you don't want to."
    menu:
        "Here goes.":
            pass
        "Uh...":
            $ renpy.pause(0.5)
            Lo relieved flip "Really, [player_name]. Don't let him pressure you into this."
            Ip "Or do. It's really all up to you where things go from here."
            show lorem sad flip with dissolve
            if annadead == False:
                Lo "Wouldn't Anna consider this an experiment you're running on [player_name]?"
                Ip normal "What she doesn't know can't hurt her."
            menu:
                "[[Undress.]":
                    pass
                "I think I've changed my mind.":
                    show lorem normal flip with dissolve
                    python in bangok_four_xipsum:
                        renpy.pause (0.5)
                        clothesoff = False
                        unplayed = True
                    Ip sad "And my scientific curiosity shall remain unsatisfied."
                    Lo "Whatever you feel comfortable with."
                    Lo think flip "Let's make one more drawing. Something dynamic."
                    jump bangok_four_xipsum_dynamicdrawing
    m "I took off my shirt first, exposing my upper body."
    play sound "fx/undress.ogg"
    $ renpy.pause (0.5)
    show lorem shy flip with dissolve
    show ipsum think with dissolve
    $ renpy.pause (0.8)
    Ip "So those dots hanging off your upper chest, I take it those are nipples, for milk feeding in mammals like yourself. And that divot in your belly would then be your navel."
    Ip normal "Excuse my confusion, but are you male or female?"
    menu:
        "Male.":
            $ bangok_four_xipsum.playerhasdick = True
        "Female.":
            $ bangok_four_xipsum.playerhasdick = False
        "That's actually somewhat of an awkward question...":
            $ renpy.pause (0.5)
            $ lorem2mood += 1
            $ bangok_four_xipsum.mood -= 1
            Ip sad "Oh, is it?"
            Ip think "Then how should I phrase it..."
            Ip normal "What's between your legs?"
            menu:
                "Show him your dick.":
                    $ bangok_four_xipsum.playerhasdick = True
                "Show him your lack of dick.":
                    $ bangok_four_xipsum.playerhasdick = False

    play sound "fx/undress.ogg"
    $ renpy.pause (0.5)
    m "Kicking off my shoes, I undid my belt and dropped my drawers."
    show lorem bangok shy with dissolve
    play soundloop "fx/scribbles.ogg"
    m "Lorem began scribbling, though turned away as if trying to pretend he wasn't looking."
    Ip happy "So that's what you're working with."
    menu:
        "Are my genitals about to end up in your game, Lorem?":
            $ renpy.pause (0.5)
            Lo bangok shy "You are the one who agreed to this."
            Lo bangok relieved "But I haven't even decided if I want that kind of content."
            Ip normal "I think a lot of people would be interested to know how mythical species get it on."
            Lo bangok think "True, but at the same time there's pushback for showing any kind of sexual content to younger dragons."
            Lo bangok relieved "Putting anything like that in could limit the reach of my game."
            Lo bangok shy "Plus, I don't want my game to be {i}about{/i} that."
        "See something you like, Ipsum?":
            python in bangok_four_xipsum:
                mood += 1
            Ip "You could certainly say that."
    show ipsum think with dissolve
    show ipsum:
        ease 1.5 xanchor 0.5 xpos 0.6 zoom 1.25 ypos 1.1
    with None
    $ renpy.pause(1.2)
    m "Ipsum strolled closer, inspecting me."
    if bangok_four_xipsum.playerhasdick == True:
        Ip "Based on what's between your legs, then, I assume your nipples don't actually produce milk."
        Ip normal "A shame. I would have liked to get samples as to what young humans find nutritious."
        Ip think "What about this? I'm not seeing any sort of slitting around your penis; does it always hang unprotected like this?"
        show ipsum at Position(ypos=1.5) with ease
        show ipsum normal with dissolve
        m "He reached out, as if to run a finger along it."
    else:
        Ip "So is that a slit, or a vaginal opening?"
        Ip normal "Actually, let me guess. Based on the size of your chest, the latter. Then your nipples would produce milk to feed the young that result from your live births."
        Ip think "I wonder if I might take a sample?"
        c "Humans actually only lactate in the period after birth, to feed the newborn or newborns."
        c "I, uh, haven't exactly had any kids recently."
        Ip sad "Oh, I see."
        Ip think "So that is a vaginal opening, then?"
        show ipsum at Position(ypos=1.5) with ease
        show ipsum normal with dissolve
        m "He reached out, as if to prod it open."
    menu:
        "No touching, please.":
            jump bangok_four_xipsum_donewithclothed_notouch
            show ipsum think with dissolve
            $ renpy.pause (0.5)
            show ipsum at Position(ypos=1.1) with ease
            if bangok_four_xipsum.unplayed == False:
                Ip normal "That could make the sex later much less enjoyable for both of us."
                c "Just hold on. I'm not sure I want to go that far yet."
                Ip sad "Ah, I see."
            else:
                Ip normal "Ah, of course. As you said, clothes off and nothing more."
                c "Yeah."
        "Hey!":
            $ lorem2mood -= 1
            $ bangok_four_xipsum.mood -= 1
            jump bangok_four_xipsum_donewithclothed_notouch
        "[[Let him.]":
            if bangok_four_xipsum.playerhasdick == True:
                m "Ipsum nudged my shaft aside with smooth tops of his cold claws."
                Ip happy "That {i}is{/i} an external scrotum."
                Ip think "It looks so strange without fur."
                m "Ipsum's cold analysis and inspection of my body led to a welling of heat in my groin, and a twitch from my shaft."
            else:
                m "Ipsum just teased my vaginal lips apart, looking past the first folds."
                if persistent.bangok_cloacas == True:
                    Ip sad "So humans really don't have cloacas. Where is your rectal opening?"
                    c "Um. Further back."
                else:
                    Ip "Not all that different from that on a dragon."
                    Ip "I assume, then, your rectal opening is further back?"
                    m "I nodded."
                Ip think "Interesting."
                m "Ipsum's cold analysis and inspection of my body led to a welling of heat in my groin. Ipsum noticed."

            Ip normal "Bloodflow arousal. Not uncommon among mammals, as I understand."
            if bangok_four_xipsum.unplayed == True:
                Ip happy "Are you sure about \"nothing more\"?"

    stop soundloop fadeout 1.0
    Lo relieved flip "Ipsum, I'm trying to draw [player_name], not you."
    show ipsum normal with dissolve
    show ipsum normal at Position(ypos=1.1) with ease
    Ip "Yes, I suppose you are."
    show lorem shy flip
    show ipsum normal flip with dissolve
    show ipsum:
        ease 1.5 xanchor 0.5 xpos 0.8 zoom 1.0 ypos 1.0
    with None
    $ renpy.pause(1.5)
    show ipsum normal with dissolve
    play soundloop "fx/scribbles.ogg"

    jump bangok_four_xipsum_donewithclothed_end

label bangok_four_xipsum_awkward:
    m "It was awkward, trying to resume a conversation so completely exposed, but the dragons seemed to treat it as just every other day for them."
    m "The more comfort I showed, the less uncomfortable Lorem seemed to be."
    c "(I guess it is every day for them. Other than Lorem's post office uniform, I don't think they wear clothes.)"
    jump bangok_four_xipsum_awkward_return

label bangok_four_xipsum_littlelong:
    menu:
        "You probably don't have to change it.":
            $ renpy.pause(0.5)
            Lo think flip "Really? I'm not sure. I think it's getting a little shorter."
            c "Uh."
            Ip "As I said, I'm sure. To get the most accurate pose..."
            pass
        "[[Say nothing.]":
            $ renpy.pause(0.5)
    jump bangok_four_xipsum_littlelong_return

label bangok_four_xipsum_whataboutour:
    $ renpy.pause (0.5)
    $ lorem2mood += 1
    Lo shy flip "Oh, right."
    Lo relieved flip "He'll probably be back out in a minute or two, once he makes sure nothing is going to explode."
    jump bangok_four_xipsum_whataboutour_end

label bangok_four_xipsum_lorembad:
    c "If Ipsum's going to make me wait here naked, maybe I don't need the sex after all."
    m "I stomped over to my clothes, fed up with the mess Lorem had talked me into."
    jump bangok_four_xipsum_lorembad_return

label bangok_four_xipsum_loremdone:
    Lo normal flip "Would you like to stay for dinner? I don't know how long you and Ipsum are going to.{cps=2}..{/cps}{w=0.5}{nw}"
    Lo bangok shy flip "Would you like to stay for dinner? I don't know how long you and Ipsum are going to...{fast} take."
    c "Let me see. What time is it?"
    c "It's getting late and I probably shouldn't stay out this long. Looks like I'll have to decline for now."
    Lo think flip "I see. Well, I gotta do something for you, at least."
    c "Isn't Ipsum already doing something?"
    Lo bangok shy flip "O-Oh, I guess you're right."
    m "I had thought I had imagined it the first time, when he'd turned away while drawing. Now that I was seeing it again, I was sure."
    m "Every time I brought up me and Ipsum being about to get it on, since I got naked, something poked out of a slit on Lorem's lower body."
    menu:
        "Are you interested in joining us?":
            $ renpy.pause(0.5)
            Lo bangok sad flip "What? N- No."
            m "He seemed to finally notice what I'd picked up on."
            Lo bangok hidepeek flip "No. No I--"
            show lorem at Position(ypos=1.1) with ease
            hide lorem with easeoutright
            play sound ["fx/run.ogg","fx/door/close2.wav"]
            m "Lorem dropped off the couch to all fours, then scampered off into Ipsum's room, slamming the sliding door behind himself."
            $ renpy.pause(0.5)
            c "(That was a weird response.)"
            menu:
                "[[Listen at the door.]":
                    $ renpy.pause (0.5)
                    m "The door was made of a pretty light paper with wood reinforcement. The voices of the room's two occupants were pretty clearly audible."
                    Lo shy "H- How do I say no?"
                    Ip sad "You just say \"no\", Lorem. This isn't difficult."
                    Lo shy "But [player_name] {i}saw{/i} that I'm... you know. Interested."
                    Ip think "If you are, then what's the problem? Why not say \"yes\"?"
                    Lo relieved "You know why!"
                    Ip think "You don't have to tell [player_name] that. A human wouldn't even have a frame of reference to know. Don't get in front of or under [player_name] and there's nothing to see."
                    $ renpy.pause (0.5)
                    Ip think "Do you want to do something with [player_name] or not? That whole situation aside?"
                    $ renpy.pause (1.3)
                    Ip normal "Then I'll let them know."
                    m "I hurried back away from the door, but it was still a few seconds before Ipsum emerged."
                "[[Wait.]":
                    pass
            $ renpy.pause (2.0)
            show ipsum normal at right with easeinright

            if lorem2mood >= 7:
                $ bangok_four_xipsum.loremin = True
                Ip happy "Lorem's in."
                c "Cool."
                Ip think "But, ground rules: Lorem is a lot more picky than I am. You can't put your mouth on him anywhere, and he doesn't like receiving anally."
                c "So basically all we can do there is his dick between my legs? Or your legs, I guess, but I assume you both want a piece of me."
                Ip happy "Well, his mouth will also be free."
                c "What about you?"
            else:
                Ip sad "Lorem's a bit shy. I apologize on his behalf, but your question spooked him."
                c "Oh. Oh no, I didn't mean--"
                Ip think "He's fine, just not interested."
                m "Behind Ipsum, I saw Lorem slip out of Ipsum's room and run off to the kitchen."
                c "Sorry Lorem..."
                $ loremstatus = "neutral"
                $ loremscenesfinished = 2
                $ persistent.lorem2skip = True
                $ renpy.pause (0.5)
                c "So I guess that leaves you and me. What are you comfortable with?"
        "Don't mention it.":
            show lorem bangok normal flip with dissolve
            $ renpy.pause (0.5)
            c "Honestly, this whole thing has been my pleasure. Minus having to stand still for as long as I did, this was actually quite fun."
            c "And, of course, there's a little left to come."
            Lo bangok shy flip "Yep."
            Lo bangok normal flip "How about I invite you again, sometime?"
            c "For Ipsum's benefit, or...?"
            Lo bangok shy flip "If you two wanted to meet again, I suppose you'd work that out with him."
            Lo normal flip "But I was thinking something that wouldn't force you to take your clothes off."
            c "Sure. Works for me."
            $ loremstatus = "good"
            $ loremscenesfinished = 2
            $ persistent.lorem2skip = True
            $ renpy.pause (0.8)
            Lo happy "Oh, right! I should go start dinner!"
            hide lorem with easeoutleft

            $ renpy.pause (0.8)
            m "I took a seat on the couch, waiting for Ipsum to come back out."
            $ renpy.pause (0.6)
            m "Lorem's nude drawing of me lay on the table in front of me. Unlike in human media, none of my assets had been overemphasized."
            $ renpy.pause (0.6)
            c "(I wonder what dragon pornography looks like...)"
            show ipsum happy at right with easeinright
            Ip "That should be stable enough to sit. Where were we?"
            c "I mean, we should probably start with what you're comfortable with."

    Ip happy "I'm comfortable with just about every position."
    Ip think "Although, I do prefer my bed be involved, as the top is just a little under my waist height."
    c "Got it."
    Ip "I'm also specifically interested in sampling you."
    c "Oral?"
    Ip normal "No. Fluid samples. Whatever we produce, I want to freeze and hold onto for analysis. That means condoms."
    menu:
        "I've had weirder reasons to have condoms.":
            $ bangok_four_xipsum.mood += 1
            $ renpy.pause (0.5)
            Ip happy "I'd be curious to hear those sometime."
        "You want to keep my sperm in a freezer?" if bangok_four_xipsum.playerhasdick == True:
            $ bangok_four_xipsum.mood -= 1
            $ renpy.pause (0.5)
            c "I better not find out years from now you cloned kids of me."
            Ip sad "We're not much past artifical eggs. I don't think an artifical womb for a live-birth mammal is within our technology."
            Ip think "How long would the gestation period even be?"
            c "Nine months."
            Ip normal "Much too long for our technologies. So no; you won't be hearing about any cloned humans."
            c "But you're saying that if it was within your technological capability..."
            Ip happy "No promises."
            c "Uh..."
        "Are you sure I can't take you bareback?":
            $ bangok_four_xipsum.mood -= 1
            $ renpy.pause (0.5)
            Ip sad "I'd really rather not."
            c "Fine..."
        "Sure. Fine by me.":
            $ renpy.pause (0.5)
    m "Ipsum gestured to his room."
    Ip happy "Shall we?"

    scene bangok_four_xipsum_bedroom normal at Pan ((128, 228), (128, 228), 0.0)
    if bangok_four_xipsum.loremin == True:
        show bangok_four_xipsum_bedroom_bed:
            alignaround (0,0)
            pos (-113,866)

        show lorem shy flip at left behind bangok_four_xipsum_bedroom_bed:
            xoffset 100
            yoffset -20
            zoom 0.7
    with wipeleft

    show ipsum happy at right:
        yanchor 1.0
        ypos 1.0
        xanchor 1.0
        xpos 1.5
        ease 1.5 xpos 1.0 zoom 1.25 ypos 1.1
    with None
    if bangok_four_xipsum.loremin == True:
        m "Lorem hid behind Ipsum's bed, while Ipsum shut the bedroom door."
    else:
        m "Ipsum shut the bedroom door behind us."
    Ip "Stand forward of the line there, unless you want your bare backside exposed to some dangerous chemicals."
    m "Turning around, I recognized the large, humming piece of equipment behind me as a fume hood, full of dozens of beakers and flasks."
    c "Oh, oops."
    show ipsum normal flip with dissolve
    show ipsum:
        ease 1.0 xpos 0.9 zoom 1.0 ypos 1.0
    m "As Ipsum went over to his desk, I looked around the rest of the room."
    c "Quite the aesthetic."
    Ip happy "Like it? {w=0.5}Blackout curtains and an RGB bulb let me switch things up whenver I feel like. It's also extremely useful for more photosensitive experiments."
    c "And today you're feeling purple?"
    Ip think flip "Yes. Is that a problem?"
    m "I shrugged."
    c "You do you."
    $ renpy.pause(0.8)
    show ipsum happy bangok with dissolve
    Ip "Actually, I believe now I do you."
    m "Ipsum had turned around from his desk, revealing twin penises now sheathed in condoms."
    menu:
        "Oh my.":
            python in bangok_four_xipsum:
                renpy.pause(0.5)
                mood += 1
        "You have {i}two{/i}?!":
            $ renpy.pause(0.5)
            Ip think bangok "Oh. I take it this is uncommon among mammals?"
            c "Yeah, I think it's pretty much unheard of."
            Ip normal bangok "Well, in dragon society it's a little rare, but hardly uncommon."

    if bangok_four_xipsum.loremin:
        show lorem sad flip with dissolve
        if bangok_four_xipsum.playerhasdick:
            m "He tossed a condom packet across the bed to Lorem with a flick of the wrist, then proffered one to me."
        else:
            m "He tossed a condom packet across the bed to Lorem with a flick of the wrist."

        Ip think bangok "Now, how you're okay with Lorem interacting with you is going to limit exactly what positions we can do."
        Ip normal bangok "What do you think?"
        show lorem think flip with dissolve
        menu:
            "Sucking me?" if bangok_four_xipsum.playerhasdick:
                python in bangok_four_xipsum:
                    renpy.pause(0.5)
                    fuckeraction = "oral"
                    fuckertarget = "cock"
                Lo think flip "Alright, I can do that."
                Ip happy bangok "I can confirm that statement."
                Lo shy flip "H-Hey!"
            "Eating me out?":
                python in bangok_four_xipsum:
                    renpy.pause(0.5)
                    fuckeraction = "oral"
                    if playerhasdick == True:
                        fuckertarget = "ass"
                Lo "I'm relatively inexperienced at that, but I can try. Are you sure?"
                Lo normal flip "Ipsum's a lot better at it."
                $ renpy.pause(0.5)
                Lo shy flip "Er, I mean..."
                menu:
                    "How would you know, Lorem?":
                        $ renpy.pause(0.5)
                        $ bangok_four_xipsum.mood -= 1
                        Ip happy bangok "We're roommates. He's merely heard the reviews from my other satisfied customers."
                        c "Wait, you sell yourself out as a business?"
                        Lo relieved flip "That was a joke, [player_name]."
                        c "Oh."
                        menu:
                            "Sounds like I'm good practice, then.":
                                jump bangok_four_xipsum_loremin_eatout_loremstart
                            "In that case, maybe Ipsum should start there.":
                                jump bangok_four_xipsum_loremin_eatout_ipsumstart
                    "Sounds like I'm good practice, then.":
                        label bangok_four_xipsum_loremin_eatout_loremstart:
                        $ renpy.pause(0.5)
                        $ bangok_four_xipsum.mood += 1
                        Lo shy flip "Oh. Okay."
                        Ip think bangok flip "Let me get you two a dental dam, then."
                    "In that case, maybe Ipsum should start there.":
                        label bangok_four_xipsum_loremin_eatout_ipsumstart:
                        $ renpy.pause(0.5)
                        Lo sad flip "Oh. Alright."
                        Ip think bangok flip "Let me get out a dental dam, then."
                        jump todo_out_of_content
                play sound "fx/rumamge.ogg"
                $ renpy.pause(0.5)
                Ip normal bangok "Here."
                m "He held up a small, limp apparatus consisting of three small bags of near-transparent barrier. It definitely wasn't the flat sheet design I knew from my world."
                c "What{w=0.5} is that?"
                Ip happy bangok "A dental dam."
                Ip normal bangok "Lorem, since you'll be the one using it, care to demonstrate?"
                Lo relieved flip "Okay."
                m "Ipsum tossed the dental dam across the bed to Lorem. The small dragon picked it up so that the three barrier bags hung vertically, then slid the top and bottom bags over his snout and jaw, respectively."
                m "Breathing through his mouth, as his nostrils were now covered, he poked his tongue into the third bag."
                Lo shy flip "That's it, I think."
                Ip normal bangok "Remember not to bite down, or you could puncture it."
                Lo relieved flip "I know how it works."
                Ip sad bangok "Then stop saying hard \"t\"s with your teeth. Your tongue against the roof of your mouth can provide a similar glottal without risking the barrier."
            "First fuck?":
                $ bangok_four_xipsum.fuckeraction = "fuck"
                $ bangok_four_xipsum.fuckertarget = "ass" if bangok_four_xipsum.playerhasdick else "vag"
                $ renpy.pause (0.5)
                if bangok_four_firsttime == True:
                    c "What do you think, Lorem? Want to be the very first dragon to fuck a human?"
                    show lorem shy flip with dissolve
                    Ip think bangok "You mean you haven't done this with other dragons, yet?"
                    Ip happy bangok "Intriguing."
                    $ renpy.pause(0.5)
                    Lo happy flip "You'd let me do that?"
                    Lo shy flip "Nobody will believe me."
                    Ip normal bangok "You will have two witnesses able to attest to the fact."
                    Lo normal flip "W-Wow. Okay."
                else:
                    c "What do you think, Lorem? Want to fuck a human before Ipsum does, for the bragging rights?"
                    Lo shy flip "O-Oh?"
                    Lo normal flip "Okay."
                jump bangok_four_xipsum_loremin_firstfuck
            "Train?":
                python in bangok_four_xipsum:
                    renpy.pause(0.5)
                    fuckeraction = "fuck"
                    fuckertarget = "ass" if playerhasdick else "vag"
                    train = True
                c "You both want a piece of me, right? Why don't I just lie back and let the two of you have at it? Whatever order you'd like?"
                if bangok_four_firsttime == True:
                    c "Either way, you two are about to be the first two dragons to fuck a human."
                    show lorem shy flip with dissolve
                    Ip think bangok "You mean you haven't done this with other dragons, yet?"
                    Ip happy bangok "Intriguing."
                Ip happy bangok "Works for me."
                scene bangok_four_xipsum_bedroom ceiling:
                    alignaround (0,0)
                    pos (0, -456)
                    ease 3.0 pos (-128,0)
                with dissolve
                $ renpy.pause(2.0)
                Ip normal "Lorem, would you like to do the honors?"
                Lo shy "M-Me?"
                Ip happy "Of course. I wouldn't want to stand in the way of one of your rare instances of sexual conquest."
                Ip think "I am also larger than you, so if we want to ease [player_name] into this..."
                Lo think "Alright."
                jump bangok_four_xipsum_loremin_firstfuck_loremclimbs
            "Shouldn't Lorem choose?":
                python in bangok_four_xipsum:
                    renpy.pause(0.5)
                    fuckeraction = "fuck"
                $ bangok_four_xipsum.mood += 1
                c "I'm just saying. Of the three of us, he's the most nervous. So... whatever makes him comfortable, right?"
                Lo shy flip "I..."
                Ip happy "Whatever you want, Lorem."
                Ip normal "Within reason, of course."
                show lorem sad flip with dissolve
                $ renpy.pause(0.8)
                Lo think flip "I guess... if you're offering..."
                Lo shy flip "Can I... your, ah..."
                if bangok_four_xipsum.playerhasdick == True:
                    $ bangok_four_xipsum.fuckertarget = "ass"
                    Lo "... ass?"
                else:
                    $ bangok_four_xipsum.fuckertarget = "vag"
                    Lo "... vagina?"
                c "Sure."

        label bangok_four_xipsum_loremin_firstfuck:
            scene bangok_four_xipsum_bedroom ceiling:
                alignaround (0,0)
                pos (0, -456)
                ease 3.0 pos (-128,0)
            with dissolve
            $ renpy.pause(2.0)
        label bangok_four_xipsum_loremin_firstfuck_loremclimbs:
            show lorem shy at Position(yanchor='top',ypos=1080-195):
                yanchor 0.0
                ypos (1080-200)
                zoom 1.5
            with easeinbottom
            m "I felt Lorem's warm scales and leathery wings as he scaled the bed between my legs. Even with me on the bed, thighs spread for him, he still seemed to hesitate."
            if bangok_four_xipsum.playerhasdick == True:
                if persistent.bangok_cloacas == True:
                    Lo "W-wait, your penis doesn't come out of a hole where your..."
                    Ip "That was implied by the external scrotum, yes."
                    Lo "Huh."
                else:
                    $ renpy.pause(0.8)
                    c "I wouldn't be lying on the bed if I didn't want this."
                    show lorem sad with dissolve
                    $ renpy.pause(0.5)
                    Lo normal "Okay."
            else:
                Lo "W-wait, you have two holes down here. Which one should I be...?"
                if bangok_four_xipsum.fuckertarget == "vag":
                    c "My vagina is the one in front."
                    Lo "O-Oh."
                else:
                    menu:
                        "Lady bits.":
                            python in bangok_four_xipsum:
                                renpy.pause(0.5)
                                fuckertarget = "vag"
                            c "The one toward my front."
                        "Ass.":
                            python in bangok_four_xipsum:
                                renpy.pause(0.5)
                                fuckertarget = "ass"
                            c "The one toward my back."
                Lo "O-Okay."
            m "Lorem's stubby claws were much colder than his hands, like icy pinpricks on my thighs."
            play sound "fx/slide.ogg"
            show bangok_four_xipsum_bedroom:
                alignaround (0,0)
                pos (-128, 0)
                easeout 0.4 pos (-128,-50)
            with None
            m "Before he could begin, Ipsum tugged the bed away from the wall."
            show ipsum normal flip:
                zoom 1.8
                alignaround (0.5,0.5)
                rotate 90
                ypos -0.5
                xpos -1000
            with easeinleft
            Ip "Your mouth won't be occupied while he's down there, will it?"
            menu:
                "One at a time, please.":
                    python in bangok_four_xipsum:
                        renpy.pause(0.5)
                        mood -= 1
                        suckingipsum = False
                    Ip think "If you insist."
                    hide ipsum with easeoutleft
                "I suppose you might occupy it...":
                    python in bangok_four_xipsum:
                        renpy.pause(0.5)
                        suckingipsum = True
                    show ipsum happy flip with dissolve
                    $ renpy.pause(0.5)
                    show black with dissolvemed
                    $ renpy.pause(0.3)
                    m "It was impossible to fit both of Ipsum's cocks in my mouth, so I gave up and focused my efforts on one. The other slapped lewdly against my cheek, slickening it with the thin layer of condom lubricant."

            if bangok_four_xipsum.fuckeraction == "oral":
                if bangok_four_xipsum.fuckertarget == "cock":
                    m "Hesitantly, Lorem's tongue teased around the head of my cock, as if the wrong move might make me explode."
                elif bangok_four_xipsum.fuckertarget == "vag":
                    m "Hesitantly, Lorem's barrier-wrapped tongue teased my outermost folds, as if the wrong move might make me explode."
                elif bangok_four_xipsum.fuckertarget == "ass":
                    m "Hesitantly, Lorem's barrier-wrapped tongue played around my rosebud, as if entering might risk me exploding."
                else:
                    label bangok_four_xipsum_impossible_loremin:
                        $ renpy.error("Loremin=True, but fuckeraction=%s and fuckertarget=%s. This was not expected."%(bangok_four_xipsum.fuckeraction, bangok_four_xipsum.fuckertarget))
            elif bangok_four_xipsum.fuckeraction == "fuck":
                if bangok_four_xipsum.fuckertarget == "vag":
                    m "Hesitantly, Lorem teased my outermost folds with something, as if entering might make me explode."
                elif bangok_four_xipsum.fuckertarget == "ass":
                    m "Hesitantly, Lorem prodded my rosebud with something, as if entering might risk me exploding."
                else:
                    jump bangok_four_xipsum_impossible_loremin
            else:
                jump bangok_four_xipsum_impossible_loremin


            if bangok_four_xipsum.suckingipsum == True:
                m "The teasing action was still plenty of stimulation. I moaned around Ipsum's cock in my mouth."
            else:
                m "The teasing action was still plenty of stimulation. I moaned appreciatively."

            Lo shy "W-Wait, am I doing it wrong?"
            Ip happy "I think you're doing it exactly right, and [player_name] wants you to keep going."
            Lo shy "..."

            label bangok_four_xipsum_loremin_firstfuck_stagetwo:

            if bangok_four_xipsum.fuckeraction == "oral" or bangok_four_xipsum.fuckeraction == "both":
                if bangok_four_xipsum.fuckertarget == "cock" or (bangok_four_xipsum.fuckeraction == "both" and bangok_four_xipsum.playerhasdick == True):
                    m "Lorem engulfed my cock in his mouth, tongue and scaly lips sliding downward without resistance."
                else:
                    m "More of the barrier rubbed against my thighs as Lorem pressed his tongue inside me, exploring."
            elif bangok_four_xipsum.fuckeraction == "fuck":
                if bangok_four_xipsum.fuckertarget == "vag":
                    m "Lorem pressed forward, penetrating my cunt with his small shaft."
                elif bangok_four_xipsum.fuckertarget == "ass":
                    m "Lorem pressed forward, his small size letting him enter my ass with nothing but a smooth slide."
                else:
                    jump bangok_four_xipsum_impossible_loremin
            
            if bangok_four_xipsum.fuckertarget == "ass" and bangok_four_xipsum.fuckeraction != "both":
                m "My sphincter clenched around him, surprised and excited by the entry."
            elif bangok_four_xipsum.fuckertarget == "vag":
                m "The slow pace left me drenched in anticipation of the real fucking."

            if bangok_four_xipsum.fuckeraction == "fuck" and bangok_four_xipsum.fuckertarget == "ass" and bangok_four_xipsum.playerhasdick == True:
                Lo shy "Would you mind if I a-also licked your cock? It's just right there."
                if bangok_four_xipsum.suckingipsum == True:
                    m "I let go of Ipsum's shaft I'd been suckling on, both of his cocks slapping against my face."
                menu:
                    "Go ahead.":
                        python in bangok_four_xipsum:
                            renpy.pause(0.5)
                            fuckeraction = "both"
                        jump bangok_four_xipsum_loremin_firstfuck_stagetwo
                    "If you finally start moving.":
                        python in bangok_four_xipsum:
                            renpy.pause(0.5)
                            mood -= 1
                            fuckeraction = "both"
                        jump bangok_four_xipsum_loremin_firstfuck_stagetwo
                    "Just fuck me.":
                        python in bangok_four_xipsum:
                            renpy.pause(0.5)
                            mood -= 1
            elif bangok_four_xipsum.fuckeraction == "oral" and (bangok_four_xipsum.fuckertarget == "vag" or bangok_four_xipsum.fuckertarget == "cock"):
                m "Lorem pulled back a moment."
                Lo shy "C-can I fuck your ass while I...?"
                if bangok_four_xipsum.suckingipsum == True:
                    m "I let go of Ipsum's shaft I'd been suckling on, both of his cocks slapping against my face."
                menu:
                    "Go ahead.":
                        python in bangok_four_xipsum:
                            renpy.pause(0.5)
                            fuckeraction = "both"
                    "If you pick up the pace.":
                        python in bangok_four_xipsum:
                            renpy.pause(0.5)
                            mood -= 1
                            fuckeraction = "both"
                    "Just lick me.":
                        python in bangok_four_xipsum:
                            renpy.pause(0.5)
                            mood -= 1
                        jump bangok_four_xipsum_loremin_firstfuck_stagethree

                if bangok_four_xipsum.playerhasdick == True:
                    m "In an impressive display of flexibility, Lorem engulfed my cock in his muzzle again, then curled to stick his cock into my ass."
                else:
                    m "In an impressive display of flexibility, Lorem drove his tongue back into my cunt, then curled to stick his cock into my ass."

            label bangok_four_xipsum_loremin_firstfuck_stagethree:

            if bangok_four_xipsum.suckingipsum == True:
                m "I switched to Ipsum's other cock, heady with the sensations Lorem was eliciting from my groin."
            else:
                m "The sensations Lorem elicited from my groin were heady."

            if bangok_four_xipsum.fuckeraction == "both":
                play soundloop "fx/rub2.ogg" fadein 1.0
                if bangok_four_xipsum.playerhasdick == True:
                    m "As he began to move in my ass, I felt undulations around my cockhead and realized the small dragon must have taken me all the way to his throat!"
                    m "He nuzzled his snout into my groin as if he didn't need to breathe, tongue now dancing around my base."
                    if bangok_four_xipsum.suckingipsum == True:
                        m "Spurred on by Lorem's enthusiasm, I tried to take Ipsum deeper, but gagged on the position that was all wrong for him to enter my less-flexible pipes."
                else:
                    m "As he began to move in my ass, his tightly curled position forced his tongue against the front of my vaginal canal, barrier-protected tastebud after tastebud sliding maddeningly past my clit."
                m "I wasn't sure how long I could hold out."
            elif bangok_four_xipsum.fuckeraction == "fuck":
                play soundloop "fx/rub2.ogg" fadein 1.0
                if bangok_four_xipsum.fuckertarget == "vag":
                    m "Lorem pulled back, then began to slide in and out of my cunt with vigor."
                elif bangok_four_xipsum.fuckertarget == "ass":
                    m "Lorem pulled back, then began to slide in and out of my ass with vigor."
                else:
                    jump bangok_four_xipsum_impossible_loremin
            elif bangok_four_xipsum.fuckeraction == "oral":
                if bangok_four_xipsum.fuckertarget == "vag":
                    m "Lorem prodded around my vagina, searching for soemthing to provide me more stimulation."
                    m "He found it in my front wall, sliding back over my clit. I arched my back in response."
                    if bangok_four_xipsum.suckingipsum == True:
                        m "I let go of Ipsum's cocks for a moment to give him a warning, my saliva smearing on my face."
                    c "G-Gentle with that!"
                elif bangok_four_xipsum.fuckertarget == "ass":
                    # m "Lorem dug "
                    $ renpy.error("TODO: Sorry, do people actually get off from just rimming?")
                else:
                    jump bangok_four_xipsum_impossible_loremin
            else:
                jump bangok_four_xipsum_impossible_loremin


            if bangok_four_xipsum.fuckeraction == "oral" and bangok_four_xipsum.fuckertarget == "vag":
                $ renpy.pause(0.8)
                m "His gentler ministrations of my clit ran the maddening borderline between teasing and stimulating."
                c "Mmph!"
                show black with fadequick
                m "Before I could think through whether it was a good idea, my legs wrapped around Lorem's head and pulled him in tight as I came, spasming around his tongue."
                $ bangok_four_xipsum.playercame = True
                if bangok_four_xipsum.suckingipsum == True:
                    show ipsum think flip
                hide black
                with dissolveslow
                c "Sh- Shoot. Lorem, are you okay?"
                Lo sad "Yeah. But that was... that was a bit much."
                c "..."
                if bangok_four_firsttime == True:
                    c "Well, congratulations on being the first dragon to tonguefuck a human to orgasm."
                    Lo shy "O- Oh?"
                    Lo "I don't know if that's a title I needed in my life."
                    Lo normal "But thanks."
                c "Want to actually fuck me now?"
                if bangok_four_xipsum.mood < 3:
                    Lo think "Mmm."
                    Lo relieved "No. I think I'm going to go start on dinner."
                else:
                    Lo shy "O- Okay."
                    if bangok_four_xipsum.suckingipsum == True:
                        show ipsum happy flip with dissolve
                    m "Lorem shifted around, prodding his small tip at the entrance of my soaked passage."
                    Lo "Can I just... go at it?"
                    c "Probably, yeah."
                    $ renpy.pause (0.3)
                    play soundloop "fx/rub2.ogg" fadein 1.0
                    m "As lubricated as I was, Lorem's cock slipped inside me without the slightest resistance."
                    m "He pistoned in and out, plowing my passage right up to his hips with every thrust."
                    if bangok_four_xipsum.suckingipsum == True:
                        show black with dissolvemed
                        m "I tapped Ipsum's side to bring him closer to me again, then took one of his cocks in my mouth, losing myself in the spitroast at both ends."
                    jump bangok_four_xipsum_loremin_premature


            if bangok_four_xipsum.fuckeraction == "fuck" or (bangok_four_xipsum.fuckeraction == "both" and bangok_four_xipsum.suckingipsum == False):
                label bangok_four_xipsum_loremin_premature:
                $ renpy.pause (2.0)
                m "Lorem's head abruptly snapped up."
                Lo shy "W-Wai--"
                stop soundloop fadeout 1.0
                play sound "fx/extinguish.ogg"
                $ renpy.pause(0.8)
                if bangok_four_xipsum.suckingipsum == True:
                    show ipsum think flip
                    hide black
                    with dissolvemed
                    m "I let Ipsum's cock out of my mouth, looking down at an embarrassed Lorem."
                Lo shy "... I..."
                menu:
                    "Nothing to be embarassed about.":
                        python in bangok_four_xipsum:
                            renpy.pause(0.5)
                        c "Premature ejaculation happens. It's not a big deal."
                        c "Did you have fun, at least?"
                        $ renpy.pause (0.8)
                        Lo normal "Yep."
                    "Really?":
                        python in bangok_four_xipsum:
                            renpy.pause(0.5)
                            mood -= 2
                        Lo relieved "Sorry."
                        Lo sad "I don't often..."
                        Lo relieved "..."
                if bangok_four_firsttime == True:
                    c "Well, with that you're officially the first dragon to fuck a human."
                    Lo shy "... Wow."
                    $ renpy.pause (1.0)
                    show lorem think with dissolve
                $ renpy.pause (0.8)
                Lo "I think I'm going to go start dinner before we forget to make it."
            else:
                m "Ipsum shifted his position, tugging me sideways by my shoulders so my head went over the edge of the bed. Then he tugged my mouth off of his cocks."
                Ip happy "Would you like to try that again? And, if so, how hard?"
                if bangok_four_xipsum.playerhasdick == True:
                    m "It was hard to think with Lorem going at my ass and so deeply taking my own shaft."
                else:
                    m "It was hard to think with Lorem going at my ass and so thoroughly working my cunt with his tongue."
                menu:
                    "Suck both.":
                        $ renpy.pause(0.5)
                        m "I answered his question by grabbing both his cocks together and tugging them into my mouth."
                        m "My cheeks bulged trying to contain both dongs, but I wasn't about to give up now."
                        m "Sealing my lips, I began to suck."
                        Ip sad "O-oh. That's different."
                        Ip happy "Very different."
                        m "Ipsum let me take over completely as I bobbed my head up and down what little of his twin shafts I could manage."
                        $ renpy.pause(0.8)
                        m "I could barely think beyond what Lorem was doing to my crotch. My pacing on Ipsum was all over the place."
                        $ renpy.pause(1.0)
                    "Throatfuck me with one.":
                        $ bangok_four_xipsum.suckingipsum = False # Technically true now, no longer sucking :bryce_laugh:
                        $ renpy.pause (0.5)
                        Ip happy "If you say so."
                        m "He stuck one of his shafts back into my mouth, his other slapping against my chin and throat as he sank inside."
                        m "Utterly lost in the sensations of fucking at my other end, I didn't notice enough to gag as my nose pressed into his crotch, Ipsum bottoming out in my throat."
                        m "He pulled back out a moment later, picking up Lorem's rapid pace."
                        $ renpy.pause(0.8)
                        m "I swooned, the double-ended fucking and Lorem's tounging more than my brain could take. Each thrust of Ipsum's hips sent his other cock bouncing lewdly off my face or throat."
                        $ renpy.pause(1.0)
                
                if bangok_four_xipsum.playerhasdick == True:
                    play sound "fx/extinguish.ogg"
                    m "I came first, blasting my load into the condom deep in the undulating depths of Lorem's throat."
                    m "Even still, the sensations kept coming as Lorem held on until I was completely done, and starting to limpen."
                else:
                    m "I came first, utterly limp from the mind-shattering orgasm of the triple penetration."
                    m "Even still, the sensations kept coming as Lorem kept tonguefucking my pussy until my orgasmic aftershocks had stopped."

                m "The moment his mouth left my crotch, he made a strangled noise."
                stop soundloop fadeout 1.0
                play sound "fx/extinguish.ogg"
                Lo shy "Ah-!"

                if bangok_four_xipsum.suckingipsum == False:
                    m "That seemed to push Ipsum over the edge as well, as he grabbed my throat and hilted himself in my mouth."
                    play sound "fx/extinguish.ogg"
                    m "I could feel every little twitch of Ipsum's cockflesh as he squeezed his dick through my throat, spurting into the condom."
                    m "His other shaft twitched against my face, reservoir bloating against my neck."
                    m "He let go well before I had worries about my air supply, pulling out even as I suckled to try to get a drop or two through the protective barrier separating me from his seed."
                else:
                    m "That seemed to push Ipsum over the edge, as his shafts twitched and their reservoirs began to bloat in my mouth."
                    m "I tugged him free, finishing him with pumps of my hands."

                play sound "fx/undress.ogg"
                m "Lorem clambered over my leg, then collapsed onto his back against the bed's pillows."
                m "Ipsum took a moment longer to take a seat, pulling his legs up, then tugging off one of his condoms."

                scene black with None
                show bangok_four_xipsum_afterglow at Pan((0,400),(640,0),8.0) with dissolve
                Lo relieved "Wow."
                Ip think "That was... most excellent."
                c "I think I'm going to need a while to recover from that."
                c "Mind if I stay for dinner?"
                Ip happy "We would be delighted."
                Lo relieved "Says the person who doesn't have to cook it after that."
                Ip sad "True."
                stop music fadeout 2.0
                $ renpy.pause (0.8)
                scene black with dissolveslow
                $ loremstatus = "good"
                $ loremscenesfinished = 2
                $ persistent.lorem2skip = True
                jump _mod_fixjmp


        Ip normal flip "Let me get out a tray for barrier disposal."
        hide ipsum with easeoutleft
        play sound "fx/dishes.wav"
        Lo relieved "Really, Ipsum?"
        stop sound fadeout 0.5
        hide lorem with easeoutbottom

        $ renpy.pause (1.5)
        m "When Ipsum returned, he had on two fresh condoms."
    else:
        if bangok_four_xipsum.playerhasdick:
            m "He handed me a condom packet of my own."
        Ip normal bangok "I know you've been standing a while. Why not lie down? I still have to get a tray set up for barrier disposal."
        c "Sure."
        scene bangok_four_xipsum_bedroom ceiling:
            alignaround (0,0)
            pos (0, -456)
            ease 3.0 pos (-128,0)
        with dissolve
        $ renpy.pause(2.0)
        play sound "fx/dishes.wav"
        $ renpy.pause (1.0)
        stop sound fadeout 0.5


        
    show ipsum normal:
        zoom 1.8
        alignaround (0.5,0)
        xpos 0.18
        ypos 0.6
    with easeinbottom

    if bangok_four_xipsum.playerhasdick == False:
        Ip happy "You have two holes, I have two penises. What say we keep things simple?"
        c "I'm in."
    else:
        Ip think "You have a penis and I have two. Would you like me to try to fit both of mine in you, one of mine in you, or just take you inside me?"
        menu:
            "Both.":
                pass
            "One.":
                pass
            "Your ass.":
                pass






label todo_out_of_content:
s "TODO: OUT OF CONTENT."
$ renpy.error("TODO: Out of content.")
