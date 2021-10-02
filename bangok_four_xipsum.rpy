init python in bangok_four_xipsum:
    unplayed = True
    mood = 0
    clothesoff = False
    
    # Player has a dick or a vagina. Sorry Lorems of the world.
    playerhasdick = None

    loremin = False

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

    scene bangok_four_xipsum_bedroom at Pan ((128, 228), (128, 228), 0.0)
    if bangok_four_xipsum.loremin == True:
        show lorem bangok bedcut:
            alignaround (0.0,0.0)
            pos (423, 653)
            size (620, 325)
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
    Ip "Stand forward from there, unless you want your bare backside exposed to some dangerous chemicals."
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
    show ipsum happy bangok with dissolve
    Ip "Actually, I believe now I do you."
    m "Ipsum had turned around from his desk, revealing twin penises already sheathed in condoms."
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



s "TODO: OUT OF CONTENT."
$ renpy.error("TODO: Out of content.")
