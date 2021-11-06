init python in bangok_four_xipsum:
    unplayed = True
    mood = 0
    clothesoff = False

    loremfirst = False

    loremin = False
    fuckertarget = None
    fuckeraction = None
    suckingipsum = False
    
    playercame = False

    depth = None

    playerpiss = False



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
            Ip normal "Of course. Whatever you're comfortable with."
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
    if bangok_four_playerhasdick is not None:
        if bangok_four_playerhasdick == True:
            c "I have a penis."
        else:
            c "I have a vagina."
    else:
        menu:
            "Male.":
                $ bangok_four_playerhasdick = True
            "Female.":
                $ bangok_four_playerhasdick = False
            "That's actually somewhat of an awkward question...":
                $ renpy.pause (0.5)
                $ lorem2mood += 1
                Ip sad "Oh, is it?"
                Ip think "Then how should I phrase it..."
                Ip normal "What's between your legs?"
                menu:
                    "Show him your dick.":
                        $ bangok_four_playerhasdick = True
                    "Show him your lack of dick.":
                        $ bangok_four_playerhasdick = False

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
                renpy.pause(0.5)
                mood += 1
            Ip "You could certainly say that."
    show ipsum think with dissolve
    show ipsum:
        ease 1.5 xanchor 0.5 xpos 0.6 zoom 1.25 ypos 1.1
    with None
    $ renpy.pause(1.2)
    m "Ipsum strolled closer, inspecting me."
    if bangok_four_playerhasdick == True:
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
            label bangok_four_xipsum_donewithclothed_notouch:
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
            if bangok_four_playerhasdick == True:
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
                menu:
                    "Accept.":
                        $ renpy.pause (0.9)
                        $ bangok_four_xipsum.unplayed = False
                        c "Okay, I have to admit I'm curious."
                        Ip "Curious enough to try?"
                        c "... Yes."
                    "Reject.":
                        $ renpy.pause (0.5)
                        c "Yes, I'm sure."

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
    $ bangok_four_xipsum.unplayed = True
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
                    $ renpy.pause (3.0)
                    c "Well. This is taking a little while."
                    $ renpy.pause (3.0)
                    c "..."
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
        "You want to keep my sperm in a freezer?" if bangok_four_playerhasdick == True:
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
        if bangok_four_playerhasdick:
            m "He tossed a condom packet across the bed to Lorem with a flick of the wrist, then proffered one to me."
        else:
            m "He tossed a condom packet across the bed to Lorem with a flick of the wrist."

        Ip think bangok "Now, how you're okay with Lorem interacting with you is going to limit exactly what positions we can do."
        Ip normal bangok "What do you think?"
        show lorem think flip with dissolve
        menu:
            "Sucking me?" if bangok_four_playerhasdick:
                python in bangok_four_xipsum:
                    renpy.pause(0.5)
                    fuckeraction = "oral"
                    fuckertarget = "cock"
                Lo think flip "Alright, I can do that."
                Ip happy bangok "I can confirm that statement."
                Lo shy flip "H-Hey!"
            "Eating me out?":
                python:
                    renpy.pause(0.5)
                    bangok_four_xipsum.fuckeraction = "oral"
                    if bangok_four_playerhasdick == True:
                        bangok_four_xipsum.fuckertarget = "ass"
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
                        c "Sounds like I'm good practice, then."
                    "Sounds like I'm good practice, then.":
                        pass
                label bangok_four_xipsum_loremin_eatout_loremstart:
                $ renpy.pause(0.5)
                $ bangok_four_xipsum.mood += 1
                Lo shy flip "Oh. Okay."
                Ip think bangok flip "Let me get you two a dental dam."
                play sound "fx/rumamge.ogg"
                $ renpy.pause(0.5)
                Ip normal bangok "Here."
                m "He held up a small, limp apparatus consisting of three small bags of near-transparent barrier. It definitely wasn't the flat sheet design I knew from my world."
                c "What{w=0.5} is that?"
                Ip happy bangok "A dental dam."
                Ip normal bangok "Lorem, since you'll be the one using it, care to demonstrate?"
                Lo relieved flip "Okay."
                m "Ipsum tossed the dental dam across the bed to Lorem. The small dragon picked it up so that the three barrier bags hung vertically, then slid the top and bottom bags over his snout and jaw, respectively."
                m "Breathing through the sides of his mouth, as his nostrils were now covered, he poked his tongue into the third bag."
                Lo shy flip "That's it, I think."
                Ip normal bangok "Remember not to bite down, or you could puncture it."
                Lo relieved flip "I know how it works."
                Ip sad bangok "Then stop saying hard \"t\"s with your teeth. Your tongue against the roof of your mouth can provide a similar glottal without risking the barrier."
            "First fuck?":
                $ bangok_four_xipsum.fuckeraction = "fuck"
                $ bangok_four_xipsum.fuckertarget = "ass" if bangok_four_playerhasdick else "vag"
                $ renpy.pause (0.5)
                if bangok_four_malepartners + bangok_four_femalepartners < 1:
                    c "What do you think, Lorem? Want to be the very first dragon to fuck a human?"
                    show lorem shy flip with dissolve
                    Ip think bangok "You mean you haven't done this with other dragons, yet?"
                    Ip happy bangok "Intriguing."
                    $ renpy.pause(0.5)
                    Lo happy flip "You'd let me do that?"
                    Lo shy flip "Nobody will believe me."
                    Ip normal bangok "You will have two witnesses able to attest to the fact."
                    Lo normal flip "W-Wow. Okay."
                    $ bangok_four_xipsum.loremfirst = True
                else:
                    c "What do you think, Lorem? Want to fuck a human before Ipsum does, for the bragging rights?"
                    Lo shy flip "O-Oh?"
                    Lo normal flip "Okay."
                jump bangok_four_xipsum_loremin_firstfuck
            "Train?":
                python:
                    renpy.pause(0.5)
                    bangok_four_xipsum.fuckeraction = "fuck"
                    bangok_four_xipsum.fuckertarget = "ass" if bangok_four_playerhasdick else "vag"
                    train = True
                c "You both want a piece of me, right? Why don't I just lie back and let the two of you have at it? Whatever order you'd like?"
                if bangok_four_malepartners + bangok_four_femalepartners < 1:
                    c "Either way, you two are about to be the first two dragons to fuck a human."
                    show lorem shy flip with dissolve
                    Ip think bangok "You mean you haven't done this with other dragons, yet?"
                    Ip happy bangok "Intriguing."
                    $ bangok_four_xipsum.loremfirst = True
                Ip happy bangok "Works for me."
                scene bangok_four_xipsum_bedroom ceiling:
                    alignaround (0,0)
                    pos (0, -456)
                    ease 3.0 pos (-128,0)
                with dissolve
                $ renpy.pause(2.0)
                Ip normal bangok "Lorem, would you like to do the honors?"
                Lo shy "M-Me?"
                Ip happy bangok "Of course. I wouldn't want to stand in the way of one of your rare instances of sexual conquest."
                Ip think bangok "I am also larger than you, so if we want to ease [player_name] into this..."
                Lo think "Alright."
                jump bangok_four_xipsum_loremin_firstfuck_loremclimbs
            "Shouldn't Lorem choose?":
                python in bangok_four_xipsum:
                    renpy.pause(0.5)
                    fuckeraction = "fuck"
                $ bangok_four_xipsum.mood += 1
                c "I'm just saying. Of the three of us, he's the most nervous. So... whatever makes him comfortable, right?"
                Lo shy flip "I..."
                Ip happy bangok "Whatever you want, Lorem."
                Ip normal bangok "Within reason, of course."
                show lorem sad flip with dissolve
                $ renpy.pause(0.8)
                Lo think flip "I guess... if you're offering..."
                Lo shy flip "Can I... your, ah..."
                if bangok_four_playerhasdick == True:
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
            $ bangok_four_malepartners += 2
            show lorem shy at Position(yanchor='top',ypos=1080-195):
                yanchor 0.0
                ypos (1080-200)
                zoom 1.5
            with easeinbottom
            m "I felt Lorem's warm scales and leathery wings as he scaled the bed between my legs. Even with me on the bed, thighs spread for him, he still seemed to hesitate."
            if bangok_four_playerhasdick == True:
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
                if bangok_four_xipsum.fuckertarget == "cock" or (bangok_four_xipsum.fuckeraction == "both" and bangok_four_playerhasdick == True):
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

            if bangok_four_xipsum.fuckeraction == "fuck" and bangok_four_xipsum.fuckertarget == "ass" and bangok_four_playerhasdick == True:
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

                show lorem shy at Position(yanchor='top',ypos=1080):
                    yanchor 0.0
                    ypos (1080-200)
                    zoom 1.5
                with ease
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

                if bangok_four_playerhasdick == True:
                    m "In an impressive display of flexibility, Lorem engulfed my cock in his muzzle again, then curled to stick his cock into my ass."
                else:
                    m "In an impressive display of flexibility, Lorem drove his tongue back into my cunt, then curled to stick his cock into my ass."
                show lorem shy at Position(yanchor='top',ypos=1080):
                    yanchor 0.0
                    ypos (1080-200)
                    zoom 1.5
                with ease

            label bangok_four_xipsum_loremin_firstfuck_stagethree:

            if bangok_four_xipsum.suckingipsum == True:
                m "I switched to Ipsum's other cock, heady with the sensations Lorem was eliciting from my groin."
            else:
                m "The sensations Lorem elicited from my groin were heady."

            if bangok_four_xipsum.fuckeraction == "both":
                play soundloop "fx/rub2.ogg" fadein 1.0
                if bangok_four_playerhasdick == True:
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
                    if bangok_four_playerhasdick == True:
                        m "Lorem dug deeper, jaw wide open against my rear, snout shoving my balls up out of his way as his teeth ghosted over my taint."
                    else:
                        m "Lorem dug deeper, jaw wide open against my rear, teeth ghosting against my outer lips."
                    if bangok_four_xipsum.suckingipsum == True:
                        m "I let go of Ipsum's cocks for a moment to give him a warning, my saliva smearing on my face."
                    c "G-Getting close!"
                else:
                    jump bangok_four_xipsum_impossible_loremin
            else:
                jump bangok_four_xipsum_impossible_loremin


            if bangok_four_xipsum.fuckeraction == "oral" and bangok_four_xipsum.fuckertarget in ["vag","ass"]:
                if bangok_four_xipsum.fuckertarget == "vag":
                    $ renpy.pause(0.8)
                    m "His gentler ministrations of my clit ran the maddening borderline between teasing and stimulating."
                elif bangok_four_xipsum.fuckertarget == "ass":
                    $ renpy.pause(0.8)
                    m "Lorem made a confused noise, hot breath coming from the sides of his mouth, around the barrier, to wash over my thighs."
                    m "That, atop the slight thrill of danger of his teeth at my groin, pushed me over the edge."
                c "Mmph!"
                show black with fadequick
                if bangok_four_playerhasdick == True:
                    play sound "fx/extinguish.ogg"
                    m "Before I could think through whether it was a good idea, my legs wrapped around Lorem's head and pulled him in tight as I shot my load into my condom, spasming around his tongue."
                else:
                    m "Before I could think through whether it was a good idea, my legs wrapped around Lorem's head and pulled him in tight as I came, spasming around his tongue."
                $ bangok_four_xipsum.playercame = True
                if bangok_four_xipsum.suckingipsum == True:
                    show ipsum think flip
                hide black
                with dissolveslow
                c "Sh- Shoot. Lorem, are you okay?"
                Lo sad "Yeah. But that was... that was a bit much."
                $ renpy.pause(0.8)
                c "..."
                $ renpy.pause(0.8)
                if bangok_four_xipsum.loremfirst == True:
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
                    if bangok_four_xipsum.fuckertarget == "ass" and bangok_four_playerhasdick == False:
                        Lo think "The same spot?"
                        menu:
                            "You went to all that trouble preparing it.":
                                $ renpy.pause(0.5)
                                Lo shy "True."
                            "Whichever you'd like.":
                                $ renpy.pause(0.5)
                                $ bangok_four_xipsum.fuckertarget = "vag"
                                show lorem think with dissolve
                            "Mm. Nah, go for my pussy instead.":
                                $ renpy.pause(0.5)
                                $ bangok_four_xipsum.fuckertarget = "vag"

                    if bangok_four_xipsum.fuckertarget == "vag":
                        m "Lorem shifted around, prodding his small tip at the entrance of my soaked passage."
                    else:
                        m "Lorem shifted around, prodding his small tip at my rear entrance."
                    Lo shy "Can I just... go at it?"
                    c "Probably, yeah."
                    $ renpy.pause (0.3)
                    play soundloop "fx/rub2.ogg" fadein 1.0
                    if bangok_four_xipsum.fuckertarget == "vag":
                        m "As lubricated as I was, Lorem's cock slipped inside me without the slightest resistance."
                    else:
                        m "Lorem's shaft tugged slightly at my sphincter as he entered, but he was small enough and the condom pre-lubricated enough that the resistance disappeared within a single cycle of his length."
                    m "He pistoned in and out, plowing my passage right up to his hips with every thrust."
                    if bangok_four_xipsum.suckingipsum == True:
                        show black with dissolvemed
                        m "I tapped Ipsum's side to bring him closer to me again, then took one of his cocks in my mouth, losing myself in the spitroast at both ends."
                    jump bangok_four_xipsum_loremin_premature



            if bangok_four_xipsum.fuckeraction == "fuck" or (bangok_four_xipsum.fuckeraction == "both" and bangok_four_xipsum.suckingipsum == False):
                label bangok_four_xipsum_loremin_premature:
                $ renpy.pause (2.0)
                show lorem shy at Position(yanchor='top',ypos=1080-195):
                    yanchor 0.0
                    ypos (1080-200)
                    zoom 1.5
                with ease
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
                if bangok_four_xipsum.loremfirst == True:
                    c "Well, with that you're officially the first dragon to fuck a human."
                    Lo shy "... Wow."
                    $ renpy.pause (1.0)
                    show lorem think with dissolve
                $ renpy.pause (0.8)
                Lo "I think I'm going to go start dinner before we forget to make it."
            else:
                m "Ipsum shifted his position, tugging me sideways by my shoulders so my head went over the edge of the bed. Then he tugged my mouth off of his cocks."
                Ip happy "Would you like to try that again? And, if so, how hard?"
                if bangok_four_playerhasdick == True:
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
                
                if bangok_four_playerhasdick == True:
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

                scene bangok_four_xipsum_afterglow at Pan((0,400),(0,400),0.0) with dissolve
                Lo relieved "Wow."
                scene bangok_four_xipsum_afterglow at Pan((0,400),(640,0),8.0) with None
                Ip think "That was... most excellent."
                c "I think I'm going to need a while to recover from that."
                c "Mind if I stay for dinner?"
                Ip happy "We would be delighted."
                Lo relieved "Says the person who doesn't have to cook it after that."
                Ip sad "True."
                stop music fadeout 2.0
                $ renpy.pause (0.8)
                scene black with dissolveslow
                $ renpy.pause (0.8)
                nvl clear
                window show
                n "Ipsum took all the barriers and packed them away in a freezer with little paper labels while Lorem and I recovered."
                n "Then he said something about a large lunch and left me and Lorem to make and consume our own dinner, while he returned to his previous experiment."
                window hide
                nvl clear
                if renpy.has_label('loremEX2kitchen'):
                    jump loremEX2kitchen
                $ renpy.pause(1.0)
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
        $ loremstatus = "good"
        $ loremscenesfinished = 2
        $ persistent.lorem2skip = True
        play sound "fx/door/close2.wav"
        m "When Ipsum returned, he had on two fresh condoms."
    else:
        if bangok_four_playerhasdick:
            m "He handed me a condom packet of my own."
        Ip normal bangok "I know you've been standing a while. Why not lie down? I still have to get a tray set up for barrier disposal."
        c "Sure."
        $ bangok_four_malepartners += 1
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

    if bangok_four_playerhasdick == False:
        Ip happy "You have two holes, I have two penises. What say we keep things simple?"
        c "I'm in."
        hide ipsum with easeoutbottom
        $ renpy.pause(0.8)
        m "He stepped away a moment, getting a healthy dollop of lube to stroke over the lower of his shafts."
        show ipsum normal:
            zoom 1.8
            alignaround (0.5,0)
            xpos 0.18
            ypos 0.6
        with easeinbottom
        m "Then he returned. He parted my cheeks, then hiked my legs a little wider around him. Two cold tips prodded at my taint, sending shivers through my lower body."
        c "Uh. Up and down from there."
        Ip normal "I am aware. Just getting positioned."
        m "One warm cockhead prodded my slick folds, while his other, colder, lubricated tip pressed against my pucker."
        show ipsum think with dissolve
        m "There, he paused a moment. I felt his fingers of one hand prodding around my perenium and both his cocks."
        $ renpy.pause(0.8)
        c "Something wrong?"
        Ip think "I'm estimating how deep I can safely go."
        c "I mean, I saw your cocks. I don't think you're {i}that{/i} different from a human size-wise."
        c "(Just a little smaller.)"
        c "We can always give it a go and just back off if we go too far, somehow."
        Ip happy "Encouraging to hear."
        Ip think "But not quite what I meant. I meant safely for me; my penises can only bend so far apart before it poses some danger to the ligaments attached to my dual baculum."
        $ renpy.pause(0.3)
        Ip happy "But practical experimentation does yield better results than theorizing."
        m "Abruptly, he pressed his tips inside."
        show ipsum normal:
            ease 2.0 ypos 0.575
        with None
        m "My lower body spread for him, both holes admitting inch after inch of cockflesh. He took things slowly enough that the lube had its chance to ease his passage into my ass, leaving both my holes with nothing but the sensation of stimulation and fullness."
        show ipsum sad with dissolve
        m "As I felt his thighs almost ghosting over mine, I realized what he'd meant about his shafts only spreading so far. The separation between my ass and vagina had his cock in my ass tugging upward, while the one in my pussy tugged down."
        $ renpy.pause(0.8)
        m "Ipsum panted as he came to a stop."
        $ renpy.pause(0.4)
        Ip happy "Well, now we know what's too far."
        show ipsum sad with dissolve
        $ renpy.pause(0.4)
        c "Are you okay?"
        show ipsum normal:
            ypos 0.58
        with ease
        m "He backed out a little ways."
        Ip think "Yes. Still just figuring this out.{w=0.5} I think I'll just need a moment."
        $ renpy.pause(1.5)
        show ipsum normal:
            ease 1.0 ypos 0.575
        with None
        m "After another few moments, Ipsum began to move again, this time leaning upward to press deeper into my vagina, while backing slightly out of my ass."
        show ipsum normal:
            ease 1.0 ypos 0.578
        with None
        m "Then he rocked his hips back the other way, going deeper in my ass while sliding from my vaginal lips. My breath caught as the head of his upper cock ran over my front wall, approaching but not quite reaching my clit."
        Ip happy "Something good there?"
        c "Y-Yeah. You're close."
        m "Rather than keep exploring with his cocks, Ipsum reached down, slipping a single claw past my lips."
        if persistent.bangok_watersports == True:
            m "He didn't quite find my vagina stuffed with his cock, though."
            c "Ah!"
            m "Brushing under my clit, the point of his claw slipped into my urethra."
            Ip sad "Oh. Apologies for--"
            m "I caught his hand."
            c "Th-That was good."
            Ip normal "It was?"
            Ip "I see. Let me see what I can do."
        else:
            m "I gasped as the tip of his claw brushed my clit, then began to gently circle it."
            Ip normal "There?"
            c "O-Oh yes!"
            Ip "I'll see what I can do."
        m "Despite an uninteligible protest from my lips, he removed his hand from my nethers and instead used it to adjust his own."
        show ipsum normal:
            ease 1.0 ypos 0.59
        with None
        m "I changed my tune a moment later as he began to pull out, keeping deeper in my ass to make the angle better for him, while also lifting up his cock in my pussy to rub his head against my front wall."
        if persistent.bangok_watersports == True:
            m "His cock popped free of my lips with my ass still half full, his head dragging a drop of golden liquid from my urethra as he dragged it over the upper part of my lips."
            m "He poked and prodded his head all around my upper hole, rubbing the small dribble of pee into my clit before returning to my urethra for more."
            c "I- I don't think you'll fit in there!"
            Ip normal "I'm aware."
            show ipsum normal:
                ease 0.5 ypos 0.58
            with None
            m "He returned his head to my love passage, pressing inside at an angle until both his cocks were as deep as he could press them. Then he tugged his upper cock back up against the front of my inner walls, dragging back along the tube from my bladder through my clenching muscles."
            c "Ipsum, i-if you play with that, I don't think I can hold it."
            Ip happy "I don't mind if you don't."
            menu:
                "[[Release.]":
                    $ bangok_four_xipsum.playerpiss = True
                "I don't want to piss on your bed and floor.":
                    $ renpy.pause(0.5)
                    Ip think "I have waterproof sheets, due to a previous accident with an acid. Really, this is up to what you're comfortable with."
                    menu:
                        "[[Release.]":
                            $ bangok_four_xipsum.playerpiss = True
                        "I'd rather not.":
                            $ renpy.pause(0.5)
                            Ip normal "Your choice."
                            jump bangok_four_xipsum_f_normalfuck
            play sound ["fx/faucet1.ogg","fx/faucet2.ogg","fx/faucet2.ogg","fx/faucet2.ogg","fx/faucet2.ogg","fx/faucet2.ogg"] fadein 1.0 fadeout 2.0
            m "Taking Ipsum's acceptance, I let go of my hold on my bladder."
            show ipsum happy:
                ease 0.5 ypos 0.59
                ease 0.15 ypos 0.58
                repeat
            with None
            play soundloop "fx/rub2.ogg" fadein 0.5
            m "Feeling the stream of liquid flowing around his cocks, Ipsum grinned and pressed in, eagerly fucking into me with wet thrusts that spattered my piss across both our lower bodies."
            m "The feeling of his smooth cockhead fucking my passage wall just below my urethra as I pissed was almost too much to bear. I tried to find something else to focus on, to anchor on, and felt some of my urine entering my own ass, shoved inside by his cock and slight wrinkles in his lower condom. The rest pooled in my lower back."
            stop sound fadeout 0.5
            m "Legs weakened by the plethora of sensation, they dropped lower, his rough, urine-slicked scales rubbing past my thighs with every thrust as I ran out of piss to give."
            $ renpy.pause(1.2)
            m "Rivulets ran down my legs, and I was sure the same could be said for his. I moaned, lost in the sensations of the urine-soaked fucking."
            $ renpy.pause(1.2)
        else:
            m "His cock popped free of my lips with my ass still half full. He dragged his free tip up, frotting against my clit for a single, maddening thrust."
            show ipsum normal:
                ease 1.5 ypos 0.58
            with None
            m "Then he slipped his tip back down, pressing in against the top of my passage."
            m "The direct focus on my most sensitive nerves was almost too much to bear. I held on to the duller sensation of his cock in my ass, using that as an anchor keeping me from being swept away by what was happening in my pussy."
            label bangok_four_xipsum_f_normalfuck:
            show ipsum normal:
                ease 0.5 ypos 0.59
                ease 0.15 ypos 0.58
                repeat
            with None
            play soundloop "fx/rub2.ogg"

            m "Now that we had a position comfortable for him (and maddening for me) Ipsum began to pick up the pace, sliding straight in and out of my ass while more carefully managing his length in my love passage."
            $ renpy.pause(1.2)
            m "Legs weakened by the plethora of sensation, they dropped lower, his rough scales rubbing past my thighs with every thrust."
            $ renpy.pause(1.2)

        m "I couldn't hold out for long, as I clenched around him both front and back."
        show black with fadequick
        $ bangok_four_xipsum.playercame = True
        $ renpy.pause(1.0)
        show ipsum happy
        hide black
        with dissolvemed
        m "Ipsum barely slowed, lubrication both natural and artificial leaving him sliding smoothly despite the clenching in my ass and passage."
        m "He released his upper cock, letting it press more against the bottom of my pussy as he focused on getting as deep as he safely could." 
        stop soundloop fadeout 0.5
        play sound "fx/snarl.ogg" fadein 0.5
        show ipsum happy:
            ypos 0.7
        with ease
        m "Then he stopped, curling over, hands moving from my legs to my hips to pull me close as a warmer sensation blossomed inside my passage and gut."
        if persistent.bangok_inflation == True:
            m "Both condoms stretched, each filling with more than a human could produce. I let out a small gasp as they pushed deeper into my colon, pressing back against Ipsum's thumb claws."
            m "I felt stuffed, and wondered a little how it would feel without the condoms, to have two shafts going off inside me at the same time."
        m "I lay back, basking in coital afterglow as Ipsum came in me."
        show ipsum sad:
            ypos 0.58
        with ease
        m "Then he tugged back with a gasp and a grimace."
        c "Are you okay?"
        Ip sad "Just experiencing the downside of practical experimentation. Mistakes."
        c "Ipsum, I--"
        if persistent.bangok_cloacas == True:
            Ip think "It's my fault for thinking your separation was easily manageable."
        else:
            Ip think "It's my fault for trying. Rarely is the separation between vagina and ass easily manageable, even with most dragons, making my condition both a blessing and a curse."
        Ip normal "But don't let that tarnish that experience. I'll be fine."
        if persistent.bangok_watersports == True and bangok_four_xipsum.playerpiss == True:
            c "In that case, since I pissed all over you, do you want to piss in me?"
            Ip sad "I'm afraid I don't have much, if any, to give. Haven't had enough to drink recently."
            c "Ah."
        else:
            c "If you say so."
        m "Ipsum tugged the rest of the way out of me, reservoirs of cum bobbing at the ends of his shafts."
    else:
        if bangok_four_xipsum.playercame == False:
            Ip think "You have a penis and I have two. Would you like me to try to fit both of mine in you, one of mine in you, or just take you inside me?"
        else:
            Ip think "Your penis appears to be limpening, which would indicate you have a similar refractory period to our kind, enforced by ability to maintain bloodflow to remain hard."
            c "Yeah, something like that."
            Ip sad "I wouldn't want to hurt you by attempting to do something while your body is not ready."
            Ip think "But, at the same time, you offered to Lorem."
            Ip happy "Was that the last of your arousal talking, or does that offer extend to me as well?"
            menu:
                "Get over here.":
                    pass
                "Yeah, sure.":
                    pass
                "I think I'm tapped out.":
                    $ renpy.pause(0.5)
                    Ip sad "Oh."
                    Ip think "A shame, but I can't overrule biology."
                    Ip normal "Yet."
                    Ip think "Let me take your condom and help you retrieve your vestments."
                    Ip normal "Then I suppose Lorem and I will see you on your way."
                    c "Sure. Thanks."
                    $ renpy.pause(0.5)
                    stop music fadeout 1.0
                    scene black with dissolvemed
                    $ renpy.pause(1.0)
                    jump _mod_fixjmp

            $ renpy.pause(0.5)
            Ip happy "As you wish."
            jump bangok_four_xipsum_one_cock_ass_fuck_getlube
        menu:
            "Both.":
                $ renpy.pause(0.5)
                Ip happy "If you think you can manage."
                hide ipsum with easeoutbottom
                $ renpy.pause(0.8)
                m "He stepped away a moment, getting a healthy dollop of lube to stroke over both his shafts."
                show ipsum normal:
                    zoom 1.8
                    alignaround (0.5,0)
                    xpos 0.18
                    ypos 0.6
                with easeinbottom
                m "Then he returned. He parted my cheeks, then hiked my legs a little wider around him. Then I felt two cold tips prodding at the muscle around my hole."
                $ renpy.pause(0.5)
                Ip think "You're sure you want to try both? I'm not familiar with your level of experience, but I doubt this will be easy."
                menu:
                    "That's what I asked for, isn't it?":
                        $ renpy.pause(0.5)
                    "Okay, maybe that's too much.":
                        $ renpy.pause(0.5)
                        Ip sad "That's what I think as well."
                        show ipsum normal with dissolve
                        jump bangok_four_xipsum_one_cock_ass_fuck
                show ipsum happy with dissolve
                $ renpy.pause(0.5)
                m "He adjusted his position, squeezing his tips together closer to my hole."
                m "Then he pressed."
                show ipsum normal:
                    ease 2.0 ypos 0.58
                with None
                m "My asshole spread, admitting both tips, then slowly even more. It felt bizzare, having hy hole spread by two bulges rather than one. The elongation of my ass was unlike any other fucking I'd had, size irregardless."
                $ renpy.pause(1.0)
                c "Ha. Oh. W-Wow."
                $ renpy.pause(0.5)
                c "Is- Is that all of it?"
                Ip think "That's a little over halfway."
                if persistent.bangok_knot == True:
                    Ip "Like almost all dragons, I have a knotting instinct during climax. I had thought it would be best to have this conversation before giving you the false assumption my full depth would be safe."
                    c "L-Little late!"
                    m "I gasped for air, finding it hard to think with the strange, unfamiliar stretching in my ass."
                    menu:
                        "Knot me.":
                            $ renpy.pause (0.5)
                            $ bangok_four_xipsum.mood += 1
                            $ bangok_four_xipsum.fuckertarget = "deep"
                            Ip sad "Are you sure? It could be some time before it releases."
                            c "Y-Yes!"
                        "S-So this is as deep as we'll go?":
                            $ renpy.pause (0.5)
                            Ip sad "Well, with both knots expanding just outside my genital slit, adjacent to one another, there is some risk to me as well as to you if you're too tight, as you feel now."
                            Ip think "Inside is a different situation; you feel less tight past that initial sphincter."
                            Ip sad "But then it may be some time before the knots release."
                            menu:
                                "Knot me.":
                                    $ renpy.pause(0.5)
                                    $ bangok_four_xipsum.mood += 1
                                    $ bangok_four_xipsum.fuckertarget = "deep"
                                    Ip think "You're sure?"
                                    c "Yeah. Let's not half-ass it now that we're this far."
                                    Ip happy "Fair enough."
                                "D-Don't knot me.":
                                    $ renpy.pause(0.5)
                                    $ bangok_four_xipsum.fuckertarget = "shallow"
                                    Ip normal "Of course."
                else:
                    Ip "Like almost all dragons, I have slight taper to my penises, meaning both are wider at my base. I had thought it would be best to have this conversation before assuming my full depth would be safe."
                    m "I gasped for air, finding it hard to think with the strange, unfamiliar stretching in my ass."
                    menu:
                        "All the way.":
                            $ renpy.pause (0.5)
                            Ip think "You're sure? I would like to avoid damaging you."
                            c "I- I can take it."
                            $ bangok_four_xipsum.mood += 1
                            $ bangok_four_xipsum.fuckertarget = "deep"
                        "S-So this is as deep as we'll go?":
                            $ renpy.pause (0.5)
                            Ip think "Well, I believe this is sufficiently deep for me. And from the sounds you're making, it is more than deep enough for you as well."
                            menu:
                                "Deeper.":
                                    $ renpy.pause(0.5)
                                    $ bangok_four_xipsum.mood += 1
                                    $ bangok_four_xipsum.fuckertarget = "deep"
                                    Ip think "You're sure?"
                                    c "Yeah. Let's not half-ass it now that we're this far."
                                    Ip happy "Fair enough."
                                "Yeah. Th-This is too new.":
                                    $ renpy.pause(0.5)
                                    $ bangok_four_xipsum.fuckertarget = "shallow"
                                    Ip normal "Of course."

                if bangok_four_xipsum.fuckertarget == "deep":
                    show ipsum happy:
                        ease 2.0 ypos 0.56
                    with None
                    m "Leaning forward, Ipsum applied more pressure to his shafts in my ass, easing deeper inside."
                    $ renpy.pause(1.0)
                    m "I squirmed, feeling him spread me a little wider with every millimeter we got further down."
                    $ renpy.pause(0.3)
                    show ipsum happy:
                        ease 0.3 ypos 0.55
                    with None
                    m "He picked my balls up out of the way, then pressed the last little distance, bringing his genital slit right up against my hole."
                    show ipsum happy:
                        ease 1.0 zoom 2.2 ypos 0.3
                    with None
                    m "Then he leaned in closer to me, my cock rubbing across the plates on his belly."
                    $ renpy.pause(0.5)
                    Ip "{cps=*0.4}Feel good?{/cps}"
                    m "His voice was low and seductive, a different tone from his usual clinical talk. I moaned, cock twitching against his chest in response. He'd clearly practiced being sexy with someone."
                    show ipsum normal with dissolve
                    play soundloop "fx/rub2.ogg" fadein 0.5
                    m "He took my shaft in one hand, rough scales and short, dulled claws closing around my hardened cock. Then he began to pump, the condom protecting me from the worst of the scraping and leaving me with just the handjob and the mind-numbing sensation of my hilted, double-dicked ass."
                    $ renpy.pause(2.0)
                    m "After a few long seconds, I felt his ministrations on my arousal beginning to relax my hole."
                    show ipsum happy:
                        ease 2.0 ypos 0.35
                    with None
                    $ renpy.pause(0.5)
                    m "He eased out extremely slowly, with full awareness I was still adjusting to his strange penetration. My legs were weak, crotch afire with need as he stroked me toward my inevitable peak."
                    show ipsum happy:
                        ease 2.0 ypos 0.30
                    with None
                    m "Letting go of my leg with his other hand, he switched direction, filling me again with wide pressure. Then I felt his hand on my belly, under my cock and his handjob, massaging my skin and that electric need in my groin."
                    $ renpy.pause(1.12)
                    m "I couldn't help it."
                    stop soundloop fadeout 0.5
                    play sound "fx/extinguish.ogg"
                    show black with fadequick
                    m "My ass clenching with all the strength it had left, Ipsum's caresses threw me over my peak."
                    m "Blissed out, I thrust into his hands as much as I could move with most of his weight on me and his cocks in my ass pinning my hips."
                    show ipsum happy:
                        ypos 0.7
                    with None
                    play sound "fx/snarl.ogg" fadein 0.5
                    hide black with dissolveslow
                    $ renpy.pause (0.5)
                    $ bangok_four_xipsum.playercame = True
                    m "When I came back from my climax, I found Ipsum with his head down, hot breath washing over my chest as he made tiny thrusts into my ass."
                    if persistent.bangok_knot == True:
                        m "Then I felt the twitching of his shafts, the pool of warmth in my gut, and the reason he couldn't pull out very far."
                    else:
                        m "Then I felt the twitching of his shafts and the pool of warmth in my gut."
                    if persistent.bangok_inflation == True:
                        m "Both condoms stretched, each filling with more than a human could produce. I let out a small gasp as they pushed deeper into my colon, pressing back against Ipsum's hand on my belly."
                        m "I felt stuffed, and wondered a little how it would feel without the condoms, to have two shafts going off inside me at the same time."
                    m "I lay back, basking in coital afterglow as Ipsum came in me."
                else: # bangok_four_xipsum.fuckertarget == "shallow":
                    show ipsum normal:
                        ease 2.0 ypos 0.59
                    with None
                    $ renpy.pause(0.3)
                    m "Ipsum pulled back slowly, twin cocks tugging at my elongated sphincter. His heads brought him to a stop, the tiny ridge of flesh that had felt so much smaller on the way in now an impediment to Ipsum's teasing retreat."
                    $ renpy.pause(0.5)
                    show ipsum normal:
                        ease 0.2 ypos 0.591
                        pause 0.5
                        ease 0.2 ypos 0.59
                    with None
                    $ renpy.pause(0.9)
                    m "Getting a better grip on my waist, Ipsum used the lubrication on his condoms to tug his his heads out. He switched direction, pushing back inside before his tips popped completely free."
                    show ipsum happy:
                        ease 1.0 zoom 2.2 ypos 0.4
                    with None
                    m "Then he leaned in closer to me, my cock rubbing across the plates on his belly."
                    $ renpy.pause(0.5)
                    Ip "{cps=*0.4}Feel good?{/cps}"
                    m "His voice was low and seductive, a different tone from his usual clinical talk. I moaned, cock twitching against his chest in response. He'd clearly practiced being sexy with someone."
                    show ipsum normal with dissolve
                    play soundloop "fx/rub2.ogg" fadein 0.5
                    m "He took my shaft in one hand, rough scales and short, dulled claws closing around my hardened cock. Then he began to pump, the condom protecting me from the worst of the scraping and leaving me with just the handjob and the mind-numbing sensation of my spread, double-dicked ass."
                    $ renpy.pause(2.0)
                    m "After a few long seconds, I felt his ministrations on my arousal beginning to relax my hole."
                    show ipsum happy:
                        ease 2.0 ypos 0.41
                    with None
                    $ renpy.pause(0.5)
                    m "He tugged his heads out again extremely slowly, with full awareness I was still adjusting to his strange penetration. My legs were weak, crotch afire with need as he stroked me toward my inevitable peak."
                    show ipsum happy:
                        ease 0.3 ypos 0.40
                        block:
                            ease 0.15 ypos 0.41
                            ease 0.5 ypos 0.40
                            repeat
                    with None
                    m "Then he began to move again, fucking back and forth, inside and outside my rosebud with his twin cockheads at the same rate he pumped me."
                    $ renpy.pause(1.12)
                    m "I couldn't help it."
                    stop soundloop fadeout 0.5
                    play sound "fx/extinguish.ogg"
                    show black with fadequick
                    m "As my ass clenched with all the strength it had left, Ipsum's caresses threw me over my peak."
                    m "Blissed out, I thrust into his hands as much as I could move with most of his weight on me. His cockheads popped free, then one alone pressed back inside while the other ran along my crack."
                    label bangok_four_xipsum_one_merge:
                    show ipsum happy:
                        ypos 0.7
                    with None
                    play sound "fx/snarl.ogg" fadein 0.5
                    $ renpy.pause(0.6)
                    hide black with dissolveslow
                    $ renpy.pause (0.5)
                    $ bangok_four_xipsum.playercame = True
                    m "When I came back from my climax, I found Ipsum with his head down, hot breath washing over my chest as he made tiny thrusts with the one cock in my ass."
                    m "Then I felt the twitching of his shafts and the pool of warmth in my gut."
                    m "I lay back, basking in coital afterglow as Ipsum came in me, and in the condom reservoir in the small of my back."

                $ renpy.pause (0.5)
                show ipsum happy:
                    ease 0.5 zoom 2.0 ypos 0.4
                with None
                m "Then he popped his head up with a grin."
                Ip "Does that satisfy our arrangement, ambassador?"
                menu:
                    "I could go for another round...":
                        $ renpy.pause (0.5)
                        if bangok_four_xipsum.fuckertarget=="deep" and persistent.bangok_knot == True:
                            Ip sad "I'm afraid that could be rather difficult. I did warn you I'd be knotting you when I came, didn't I?"
                            c "You did. I was making a joke."
                        else:
                            Ip sad "I'm afraid that could be rather difficult. Us dragons have a refractory period of--"
                            c "I'm kidding. I was making a joke."
                        Ip think "Ah."
                    "Very much so.":
                        $ renpy.pause (0.5)
                        Ip normal "Good."


                if bangok_four_xipsum.fuckertarget == "deep":
                    hide ipsum with easeoutbottom
                    if bangok_four_xipsum.loremin == True:
                        m "Ipsum leaned back with a remarkable display of his thin body's flexibility, swiping a metal tray with Lorem's condom off a table next to his fume hood without disturbing his cocks in my ass."
                    else:
                        m "Ipsum leaned back with a remarkable display of his thin body's flexibility, swiping an empty metal tray off a table next to his fume hood without disturbing his cocks in my ass."
                else:
                    $ renpy.pause(0.5)
                    show ipsum think with dissolve
                    show ipsum think at Position(ypos=0.56) with ease
                    $ renpy.pause(0.3)
                    hide ipsum with easeoutbottom
                    m "Ipsum tugged out of me, taking a step back."
                    if bangok_four_xipsum.loremin == True:
                        m "Then he turned to fetch a metal tray with Lorem's condom off a table next to his fume hood."
                    else:
                        m "Then he turned to fetch an empty metal tray off a table next to his fume hood."

                show ipsum normal:
                    zoom 1.8
                    alignaround (0.5,0)
                    xpos 0.18
                    ypos 0.55
                with easeinbottom
                m "He set it next to me on the bed. Then he stripped off my condom in one smooth motion, tying it off with what looked like practiced ease. He set my load on the tray."
                if persistent.bangok_knot == True and bangok_four_xipsum.fuckertarget == "deep":
                    m "Finally, he set the tray aside."
                    hide ipsum with dissolvemed
                    m "Hiking my hips up a little higher, Ipsum lay across one of my legs, all along my body. My ass clenched, put on edge by the slight force his new position applied to my hole via his cocks, even as the warmth of his body relaxed the rest of me."
                    c "So... how long?"
                    Ip think "Twenty, maybe thirty minutes."
                    Ip normal "I believe you'll be staying for dinner, now. And don't worry; Lorem will have factored our delay into the cooking time for his choice of dish."
                    c "That's nice of him."
                    Ip normal "Indeed."
                    stop music fadeout 1.0
                    scene black with dissolveslow
                    $ renpy.pause(1.0)
                    jump _mod_fixjmp
                elif bangok_four_xipsum.fuckertarget == "deep":
                    m "Finally he set the tray aside, before bracing against my legs and beginning to pull slowly out of my ass."
                    c "A-hah!"
                    show ipsum normal:
                        zoom 1.8
                        alignaround (0.5,0)
                        xpos 0.18
                        ease 2.5 ypos 0.59
                    with None
                    m "It was painfully slow going, my ass hypersensitive after the unusual spreading."
                    $ renpy.pause(2.3)
                    play sound "fx/uncork.ogg"
                    show ipsum normal:
                        zoom 1.8
                        alignaround (0.5,0)
                        xpos 0.18
                        ease 0.3 ypos 0.6
                    with None
                    m "Eventually he popped free, condom-enwrapped loads going with him."
                else: # "shallow":
                    pass
            "One.":
                $ bangok_four_xipsum.fuckertarget = "shallow"
                $ renpy.pause(0.5)
                Ip normal "Of course."
                label bangok_four_xipsum_one_cock_ass_fuck_getlube:
                hide ipsum with easeoutbottom
                $ renpy.pause(0.8)
                m "He stepped away a moment, getting a healthy dollop of lube to stroke over both his shafts."
                show ipsum normal:
                    zoom 1.8
                    alignaround (0.5,0)
                    xpos 0.18
                    ypos 0.6
                with easeinbottom
                m "Then he returned. He parted my cheeks, then hiked my legs a little wider around him. I felt two cold tips prodding at the muscle around my hole."
                c "Uh."
                Ip normal "Just getting positioned."
                label bangok_four_xipsum_one_cock_ass_fuck:
                m "One of his cold, lubricated shafts he pushed down, into the small gap between my crack and his bedcovers. The other he pressed right up against my pucker."
                show ipsum think with dissolve
                m "There, he paused a moment. I felt his fingers of one hand prodding around my perenium and both of his cocks."
                $ renpy.pause(0.8)
                c "Something wrong?"
                Ip think "I'm estimating how deep I can safely go."
                c "I mean, I saw your cocks. I don't think you're {i}that{/i} different from a human size-wise."
                c "(Just a little smaller.)"
                c "We can always give it a go and just back off if we go too far, somehow."
                Ip happy "Encouraging to hear."
                Ip think "But not quite what I meant. I meant safely for me; my penises can only bend so far apart."
                Ip happy "But practical experimentation does yield better results than theorizing."

                show ipsum normal:
                    ease 2.0 ypos 0.58
                with None
                m "Ipsum began to push. My asshole spread, admitting Ipsum's cockhead while his other shaft rubbed up into the small of my back."
                $ renpy.pause(1.4)
                m "He stopped a moment, pulling my cheeks a little wider, then pushed more inside me."
                show ipsum normal:
                    ease 2.0 ypos 0.56
                with None
                $ renpy.pause(2.0)
                show ipsum happy:
                    ease 0.3 ypos 0.57
                with None
                $ renpy.pause(0.3)
                m "Picking my balls up out of the way, he pressed the last little distance, to the point I could feel the separation of his cocks squeezing both sides of the base of my spine."
                show ipsum happy:
                    ease 1.0 zoom 2.2 ypos 0.3
                with None
                m "Then he leaned in closer to me, my cock rubbing across the plates on his belly."
                $ renpy.pause(0.5)
                Ip "{cps=*0.4}Feel good?{/cps}"
                m "His voice was low and seductive, a different tone from his usual clinical talk. I moaned, cock twitching against his chest in response. He'd clearly practiced being sexy with someone."
                show ipsum normal with dissolve
                play soundloop "fx/rub2.ogg" fadein 0.5
                m "He took my shaft in one hand, rough scales and short, dulled claws closing around my hardened cock. Then he began to pump, the condom on my dick and lube still on his hand protecting me from the worst of the scraping and leaving me with smooth sliding of the handjob."
                $ renpy.pause(2.0)
                m "After a few long seconds, I felt his ministrations on my arousal beginning to relax my hole."
                show ipsum happy:
                    ease 0.6 ypos 0.35
                    ease 0.3 ypos 0.30
                    ease 0.6 ypos 0.35
                    ease 0.3 ypos 0.30
                    block:
                        ease 0.5 ypos 0.35
                        ease 0.15 ypos 0.30
                        repeat
                with None
                $ renpy.pause(0.5)
                m "With a grin, Ipsum gave my ass a few lighter thrusts, then began to pump in and out in time to his strokes of my cock."
                $ renpy.pause(1.5)
                show ipsum normal with dissolve
                show ipsum normal:
                    ypos 0.3
                with ease
                m "Abruptly, Ipsum pulled all the way out, still stroking my shaft."
                show ipsum happy with dissolve
                show ipsum happy:
                    ypos 0.35
                with ease
                m "I barely had a moment to adjust as he lined his tip back up and thrust."
                m "It took me a moment to realize why his shaft rubbing up my crack and the small of my back felt different. {w=0.5}He'd switched to his {i}other{/i} cock in my ass!"
                show ipsum happy:
                    ease 0.3 ypos 0.30
                    block:
                        ease 0.5 ypos 0.35
                        ease 0.15 ypos 0.30
                        repeat
                with None
                m "Giving one slower thrust to make sure everything was lined up, Ipsum picked up right where he'd left off in his fast pace."
                $ renpy.pause(1.2)
                Ip happy "Feeling close?"
                menu:
                    "O-Oh god.":
                        pass
                    "Mmh.":
                        pass
                    "Swwitch again?":
                        $ renpy.pause(0.5)
                        Ip "Sure."
                        show ipsum normal with dissolve
                        show ipsum normal:
                            ypos 0.3
                        with ease
                        m "The momentary pause in the assfucking left all my attention on my shaft, now achingly close to release."
                        show ipsum happy with dissolve
                        show ipsum happy:
                            ypos 0.35
                        with ease
                        m "His press back inside with his other shaft was maddening. Once he began to move again, there was nothing I could do."
                        show ipsum happy:
                            ease 0.3 ypos 0.30
                            block:
                                ease 0.5 ypos 0.35
                                ease 0.15 ypos 0.30
                                repeat
                        with None
                $ renpy.pause(0.8)
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                m "I rocketed over my peak. My ass clenched down on his cock and I thrust a little into his hands, spurting into the reservoir of my condom."
                jump bangok_four_xipsum_one_merge
            "Your ass." if bangok_four_xipsum.playercame == False:
                $ renpy.pause(0.5)
                $ bangok_four_xipsum.position = "iass"
                if bangok_four_xipsum.loremfirst == True:
                    Ip happy "So you'd like me to be the first dragon to have a human cum in them?"
                Ip normal "I can't find any reason to say no."

                hide ipsum with easeoutbottom
                $ renpy.pause(0.8)
                m "He stepped away a moment, getting a healthy dollop of lube onto the the rough scales of his hand."
                show ipsum normal:
                    zoom 1.8
                    alignaround (0.5,0)
                    xpos 0.18
                    ypos 0.6
                with easeinbottom
                m "Then he returned, spreading the cold lube around on my tip before pumping his hand down my length."
                menu:
                    "I, ah, think I should be on top.":
                        $ renpy.pause(0.5)
                        Ip think "I'm happy to take care of things. Are you sure?"
                        menu:
                            "I'd prefer the control.":
                                $ renpy.pause(0.5)
                                $ bangok_four_xipsum.mood -= 1
                                jump bangok_four_xipsum_hisass_top
                            "If you insist...":
                                $ renpy.pause(0.5)
                                jump bangok_four_xipsum_hisass_bot
                    "Mm. You're going to do all the work?":
                        $ renpy.pause(0.5)
                        jump bangok_four_xipsum_hisass_bot

                label bangok_four_xipsum_hisass_bot:
                    Ip happy "It's no trouble at all."
                    show ipsum happy:
                        ypos 0.45
                    with ease
                    m "Giving my shaft a few more pumps, Ipsum clambered onto the bed, straddling my thighs."
                    show ipsum happy:
                        ypos 0.42
                    with ease
                    m "He shuffled forward, his twin shafts bumping mine until he took hold of mine and aimed it back at his hole."
                    m "Then Ipsum spread his knees out wider, sinking down onto me."
                    show ipsum happy:
                        ease 3.0 ypos 0.45
                    with None
                    m "He was incredibly tight, but kept sufficient control of his depth that he didn't put a worrying amount of weight on my member. Instead, he held his position, loosening slowly until my lubricated tip popped in, gradually followed by more of my member."
                    m "The slow movement of an entrance of hard plates giving way to his warm, clenching innards left me aching to pick up the pace."
                    show ipsum happy:
                        ypos 0.46
                    with ease
                    m "I gave a small thrust and Ipsum dropped with me, his twin cocks slapping down onto my belly."

                    if persistent.bangok_knot == True:
                        $ renpy.pause(0.8)
                        Ip think "Hm. Perhaps I should have considered this earlier. Humans do not form knots upon ejaculation, do they?"
                        c "Uh, what? No."
                        Ip normal "Excellent."
                    show ipsum normal with dissolve
                    $ renpy.pause(1.2)
                    m "Ipsum took a moment to rest with me hilted inside him, adjusting. His sphincter clenched around my base. The warm plates of his underbelly rested his weight on my belly, legs, and balls."






                    jump todo_out_of_content
                
                label bangok_four_xipsum_hisass_top:
                    Ip happy "Of course."
                    $ renpy.pause(0.3)
                    play sound "fx/undress.ogg"
                    scene bangok_four_xipsum_bedroom normal at Pan ((128, 228), (128, 228), 0.0)
                    show ipsum normal flip bangok:
                        rotate -42
                        pos (-0.12,0.4)
                    with dissolvemed
                    m "Ipsum stepped back to let me get up off the bed, then lay back in my place."
                    if persistent.bangok_cloacas == True:
                        m "Reaching between his shafts with his lubricated hand, he poked one claw into the lower part of his slit, sinking it inside his hole."
                    else:
                        m "Reaching between his shafts with his lubricated hand, he poked one claw between the next pair of plates down, nudging them aside to reveal a thin strip of un-scaled flesh and a tight hole."
                        m "He sank his claw inside, then grinned up at me."
                    Ip happy flip bangok "Right there."

                    m "Spreading Ipsum's legs a little wider, I stepped over his tail to get better access to his hole."
                    show ipsum sad flip bangok with dissolve
                    m "Ipsum's ass was tight, resisting anything more than the end of my tip, despite my lubrication. The dragon's breath caught, and he wiggled his hips to better take the weight I put on him."
                    menu:
                        "You alright?":
                            $ renpy.pause(0.5)
                            $ bangok_four_xipsum.mood += 1
                            Ip "I will be. Just give me a few moments."
                            Ip normal flip bangok "I'm also used to being on top. For various reasons."
                            show ipsum sad flip bangok with dissolve
                            $ renpy.pause(1.0)
                            m "I held still for a for a few seconds, keeping my weight where it was."
                            show ipsum normal flip bangok with dissolve
                            m "Ipsum's breathing raised and lowered the wave of plates down his chest as he began to relax."
                        "Need a minute?":
                            $ renpy.pause(0.5)
                            Ip "Not nearly that long. Just give me a few moments."
                            Ip normal flip bangok "I'm also used to being on top. For various reasons."
                            show ipsum sad flip bangok with dissolve
                            $ renpy.pause(1.0)
                            m "I held still for a for a few seconds, keeping my weight where it was."
                            show ipsum normal flip bangok with dissolve
                            m "Ipsum's breathing raised and lowered the wave of plates down his chest as he began to relax."
                        "[[Push harder.]":
                            $ bangok_four_xipsum.mood -= 1
                            show ipsum sad flip bangok:
                                rotate -42
                                pos (-0.13,0.4)
                            with ease
                            Ip "Urgh!"
                            m "I sunk deeper, forcing an inch of my length into Ipsum's ass, before he clenched his thighs against my hips to keep me from encroaching further."
                            Ip "Th-That's too much!"
                            show ipsum sad flip bangok:
                                rotate -42
                                pos (-0.12,0.4)
                            with ease
                            m "I pulled back, leaving Ipsum's rosebud shuddering and winking up at me, glittering with the lubrication I'd smeared on it."
                            Ip "I will need a bit more time to adjust. I'm not used to being on the bottom."
                            c "You could have mentioned that."
                            Ip think flip bangok "I had assumed you would take matters with more caution and consideration."
                            $ renpy.pause(1.0)
                            m "I gave him his few seconds to adjust, fitting my tip again to his tailhole and waiting for him to relax."
                            $ renpy.pause(1.0)
                            show ipsum normal flip bangok with dissolve
                            m "It took some moments for the rise and fall of the plates down his chest to return to a more regular cadence. Only then did his hole begin to loosen to my intrusion."

                    Ip happy flip bangok "I believe I am prepared."

                    m "I drew back slowly, enjoying Ipsum's hole tugging back to keep me inside. At my cockhead I switched directions, pushing back inside."
                    show ipsum normal flip bangok with dissolve
                    c "How's that?"
                    Ip "I'm pleased if it's sufficient for you. But I could stand you going a bit faster."
                    m "Leaning over Ipsum, I began to let more vigor into my fucking of his hole, pressing down into the bed with my hands on either side of him."
                    play soundloop "fx/rub2.ogg" fadein 2.0
                    show ipsum normal flip bangok:
                        ease 0.15 xpos -0.1225
                        ease 0.5 xpos -0.12
                        ease 0.15 xpos -0.125
                        ease 0.5 xpos -0.12
                        ease 0.15 xpos -0.1275
                        ease 0.5 xpos -0.12
                        block:
                            ease 0.15 xpos -0.13
                            ease 0.5 xpos -0.12
                            repeat
                    with None
                    m "The rough scales of his thighs rubbed mine as I pushed to the hilt each thrust, pace slowly increasing as he hadn't told me to stop, and every thrust felt better than the last."
                    $ renpy.pause(0.5)
                    m "My balls slapped lewdly into his plates now, double dicks bouncing off my belly as I plowed into his yielding rear."
                    $ renpy.pause(0.5)
                    show ipsum happy flip bangok with dissolve
                    m "Not wanting to leave him completely out of the fun, I took hold of his shafts, doing my best to pump them both one-handed while my other hand supported my hard pace."
                    m "I felt his fluff tickling my bare skin as his tail wrapped around one of my legs, pulling me into a closer, faster pace."

                    $ renpy.pause(0.5)

                    Ip normal flip bangok "I forgot how nice it could be to lie back and enjoy sometimes."

                    m "I panted, beyond words, so very close to my peak."

                    $ renpy.pause(0.5)

                    stop soundloop fadeout 0.5
                    play sound "fx/extinguish.ogg"
                    show black with fadequick
                    m "Hilting myself in Ipsum's ass, I came, spurt after spurt of my cum filling the condom's reservoir inside him."
                    $ renpy.pause(0.5)
                    hide black
                    show ipsum normal flip bangok:
                        xpos -0.14
                    with dissolvemed
                    m "When I returned to my senses, Ipsum's tail was still holding me close, keeping me buried inside him even as I began to limpen."
                    Ip happy flip bangok "If you could help me out first."
                    m "Ipsum's shafts twitched against my belly, still hard and raring to go."
                    m "I leaned back slightly, getting my balance on weak legs. Then taking one shaft in each hand, I set to pumping."
                    play soundloop "fx/rub2.ogg" fadein 0.5
                    Ip sad flip bangok "Mmh."
                    m "His tail began to loosen immediately, legs limpening around my sore thighs as I stroked his members."
                    m "He thrust his hips back against my groin, seeking out a little bit more stimulation from my spent cock."
                    m "Then he thrust upward into my hands."
                    stop soundloop fadeout 0.5
                    play sound "fx/snarl.ogg" fadein 0.5
                    show ipsum happy flip bangok with dissolve
                    m "Both of Ipsum's condoms' reservoirs bloated as he spurted through my hands, getting off on the handjob and the dick in his ass."
                    m "Once his fluffy tail slipped from my leg, I took a step backward, tugging myself free."
                    m "Then I lay on the bed next to him, giving my leg muscles a rest."

                    scene bangok_four_xipsum_bedroom ceiling:
                        alignaround (0,0)
                        pos (0, -456)
                        ease 3.0 pos (-128,0)
                    with dissolve
                    $ renpy.pause(2.0)
                    play sound "fx/dishes.wav"

                    if bangok_four_xipsum.loremin == True:
                        m "As I lay down, Ipsum got up, moving on unsteady legs to collect a metal tray with Lorem's condom off a table next to his fume hood."
                    else:
                        m "As I lay down, Ipsum got up, moving on unsteady legs to collect an empty metal tray off a table next to his fume hood."
                    stop sound fadeout 0.5

                    jump bangok_four_xipsum_hisass_done

                label bangok_four_xipsum_hisass_done:
                show ipsum normal:
                    zoom 1.8
                    alignaround (0.5,0)
                    xpos 0.18
                    ypos 0.55
                with easeinbottom
                m "He set it next to me on the bed. Then he stripped off my condom in one smooth motion, tying it off with what looked like practiced ease. He set my load on the tray."


    scene black with dissolve
    m "Then he wandered around the bed, sitting down above my head while I lay recovering."
    label bangok_four_xipsum_afterglow:
    show bangok_four_xipsum_afterglow at Pan((0,0),(640,8),6.0) with dissolve
    $ renpy.pause(5.0)
    scene bangok_four_xipsum_bedroom normal at Pan ((128, 228), (128, 228), 0.0)
    show bangok_four_xipsum_bedroom_bed:
        alignaround (0,0)
        pos (-113,866)
    show ipsum happy flip behind bangok_four_xipsum_bedroom_bed:
        zoom 0.85
        alignaround (0.0,1.0)
        pos (0,0.35)
    with Fade(0.5,1.0,0.5)

    Ip "That was excellent indeed."
    Ip normal flip "Now, as I didn't mention taking samples until after you'd agreed, I assume your interest was real and not just curiosity?"
    c "Is this your way of asking to meet up again?"
    Ip think flip "That depends, is it working?"
    if bangok_four_playerhasdick == False:
        c "After you hurt yourself?"
        Ip "Well, mistakes always happen."
        Ip happy flip "Good scientists run the experiment over again when they do."
    c "Maybe."
    Ip happy flip "If it sweetens the deal, I'm planning to use your samples to determine the risk of us copulating unprotected. Among some other activities you may want to join in on. Up to you, of course."
    Ip normal flip "I'll give you my number and leave it to you to decide when you think is appropriate."
    Ip think flip "Wouldn't want your busy ambassadorial schedule to get in the way."
    Ip sad flip "Though I may be in the lab quite a bit in the immediate near-future."
    c "I see. So at least a few days from now."
    Ip normal flip "Yes."
    c "I'll give you a call if I have time."
    Ip happy flip "Excellent."

    if bangok_four_xipsum.playerpiss == True:
        Ip sad "Now I'd better go get something to clean up the mess we've made."
    
    $ renpy.pause(1.5)

    stop music fadeout 1.0
    scene black with dissolvemed
    $ renpy.pause(1.0)
    jump _mod_fixjmp





label todo_out_of_content:
play sound "fx/system3.wav"
s "TODO: OUT OF CONTENT."
$ renpy.error("TODO: Out of content.")
