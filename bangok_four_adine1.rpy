label bangok_four_adine1_angercheck:
    if adinemood < 0:
        $ renpy.pop_call()
        jump bangok_four_adine1_abruptexit
    return

label bangok_four_adine1_abruptexit:
    stop music fadeout 1.0
    Ad frustrated b "You know what? I think I've had it with you, and this game."
    c "But--"
    Ad "I'd rather deal with this rain than with any more of your perversion."
    hide adine with dissolve
    m "Before I could get a word in edgewise, Adine was already headed for the door."
    c "Hey!"
    play sound "fx/door/doorclose3.wav"

    $ adinestatus = "bad"
    $ adinescenesfinished = 1
    jump _mod_fixjmp

label bangok_four_adine1_ToD_refused:
    Ad think b "Honestly I kinda hate you. Is it still raining outside?"
    m "The storm hadn't stopped, though it had lessened slightly."
    c "Not really, so you should stay--"
    Ad disappoint b "Nah, good enough. I'll be leaving now."
    hide adine with dissolve
    $ renpy.pause (0.3)
    play sound "fx/door/doorclose3.wav"
    m "Before I could get another word in, she was gone, flying through a thin sheet of rain."

    $ adinestatus = "bad"
    $ adinescenesfinished = 1
    jump _mod_fixjmp

label bangok_four_adine1:
    if bool(bangok_four_bangnokay) != bool(persistent.bangok_four_bangnokay):
        jump bangok_four_adine1_return

    m "As I brought the topic up, I had in mind some..."
    $ headgear = True
    menu:
        m "As I brought the topic up, I had in mind some...{fast}"
        "...silly ideas for questions and dares.":
            jump bangok_four_adine1_return
        "...lascivious ideas for questions and dares.":
            $ adinemood = 2 if adinemood > 0 else 2 + adinemood // 5
            if adinemood < 0:
                jump bangok_four_adine1_ToD_refused
    

    Ad normal b "What's that?"
    c "We keep asking each other questions, but if you don't want to answer one, you have to do whatever I tell you to, and vice versa."
    Ad disappoint b "I can't think of anything to tell you to do. At least, not anything I want to say out loud."
    c "I'd do anything you dared me to as long as it stayed in this house."
    Ad think b "Really? Anything at all?"
    c "Well, keep in mind that immediately afterwards, I get a turn as well, so be wary of an equally fun comeback."
    Ad normal b "Alright then, who goes first?"
    c "You asked the last few questions, so it's only fair if I start."
    Ad annoyed b "Fair's fair I guess."

    show adine normal b with dissolve
    m "I took a moment to think carefully about what I wanted to ask."
    menu:
        "What part of your body is most ticklish?":
            $ adinemood += 1
            $ renpy.pause (0.5)
            Ad think b "Probably my sides, though they're not my most sensitive area."
            c "Good to know. For research, of course."
            Ad sad b "You wouldn't abuse this knowledge to bring me down, would you?"
            c "Of course not. Unless you asked me to."
            show adine think b with dissolve

        "How tight are you, and how often do you fuck?":
            $ adinemood -= 1
            Ad frustrated b "What the fuck? What kind of question is that?"
            c "A direct one. Is it well worn, or are you still-"
            Ad annoyed b "Fuck you, I don't think that's even worthy of a response."
            c "I think you're over--{w=0.5}{nw}"
            call bangok_four_adine1_angercheck
            Ad frustrated b "I'll take a dare."
            call .dare_table_1
            
        "What's the smallest delivery you've ever had to make?":
            Ad think b "I was at a college party once. As the only flier, I was tasked with getting the condoms."
            c "Smallest delivery? Was it just the one box or were their dicks that small?"
            Ad annoyed b "There were only five of them, plus me. I don't know about their size though."
            c "Weren't they lining up to... y'know."
            Ad think b "Nah, there was this other girl there, plus four guys. They were all having fun with her while I waited my turn, but I got bored and left after a bit."
            c "Ah, fair enough."

    Ad normal b "Anyways, it's my turn now. What's your greatest wish?"

    menu:
        "World peace.":
            c "More than anything, I'd want there to be peace on Earth"
            Ad "A noble wish, albeit a bit generic."
            c "Generic as it may be, I think it'd just feel a lot better."
            Ad think b "True, conflict brings nothing but pain for everyone involved."
        "I want to fuck as many dragons as I can before I go back.":
            $ adinemood -= 1
            $ renpy.pause (0.5)
            Ad think b "Seriously, of all the things you could have, you want to just fuck?"
            c "Yeah, it's a load of fun!"
            call bangok_four_adine1_angercheck
            Ad disappoint b "I'm not going to judge, as long as you're doing it safely."
            c "Honestly, I think I'm slacking at the moment, if you get what I mean."
            Ad annoyed b "I'd rather not, to be honest. Let's just move on."
        "To live here.":
            $ adinemood += 1
            c "Honestly, I'd choose to live here forever, never go back to Earth for anything more than a visit."
            Ad think b "Really? I get that you don't have anyone to miss you, but wouldn't you miss home?"
            c "Not really. This place is actually really comfortable for a human."
            Ad "Do you really not know anyone at all that would miss you?"
            c "No, everyone I did know has gone their own way. On the other hand, there are plenty plenty of dragons I'd like to know better."
            Ad giggle b "Fair enoough. Let's move on."

    menu:
        "Do the goggles stay on in the bedroom?":
            Ad think b "Why are you asking that of all things?"
            c "I'm just curious, I haven't seen you without them on."
            Ad annoyed b "I don't think it's any of your business really."
            Ad think b "Though, come to think of it, I guess I've never thought to take them off for sex..."
            menu:
                "Give me a demonstration, now.":
                    $ adinemood -= 1
                    c "Well that's an offer I can accept, go ahead and give me a demonstration right now hot stuff. Lift that tail nice and high."
                    Ad frustrated b "What the hell is wrong with you? That wasn't an offer."
                    c "Right, but it could-"
                    call bangok_four_adine1_angercheck
                    Ad "No, it couldn't."
                "Would you be willing to do a demonstration for me?":
                    $ adinemood += 1
                    Ad giggle b "Maybe some time, but not right now."
                    c "Thanks for considering it, beautiful."
                    Ad giggle b "Hey, flattery is cheating!"
                "Just one of those things, huh?":
                    c "I guess that's just one of the things you never think about, huh?"
                    Ad think b "Yeah, I guess so."
            Ad normal b "It's my turn now. What do you like most about dragons?"
        "What would you do if you were invisible for a day?":
            Ad think b "Invisible, huh?"
            Ad think b "That's not easy to answer. My main hobby is flying, and I want people to be able to see that."
            c "Well, with this question it's more about what kind of mischief you'd get up to if you couldn't get caught, like a crime or public masturbation."
            Ad "Pretending I didn't hear that last one, {nw}"
            Ad normal b "Pretending I didn't hear that last one, {fast}I actually know what I'd do. I would check out the building they found along with the portal."
            c "Wait, building?"
            Ad "You didn't hear? They found a whole structure, mostly intact, along with the portal."
            Ad "It's actually underground, and nobody's allowed in except for a team of archaeologists. I think it may have a lot of secrets and answers about the portal and what it's doing here."
            c "Interesting. I'd actually want to check that out myself."
            $ renpy.pause (0.5)
            Ad normal b "What do you like most about dragons?"
        "Are you a top, or a bottom?":
            Ad think b "You mean in the bedroom? Why would you be interested in that?"
            c "Was just curious, I don't think I could figure it out just by watching you casually."
            Ad giggle b "Well if you insist, I'm actually a switch. I think."
            c "You think?"
            Ad think b "I've only ever been on the bottom, but that's because I've only ever been with tops. I'm actually interested in at least trying to take charge."

            menu:
                "Top me right here, right now.":
                    $ adinemood -= 1
                    c "Hey, I'm here, you can take charge right now."
                    Ad annoyed b "If I wanted to fuck you I would've asked already, asshole."
                    c "Don't take that tone with me, I was just making an offer."
                    call bangok_four_adine1_angercheck
                    Ad annoyed b "Well it was awfully pushy. Let's just keep going."
                "I can give you the opportunity to if you'd like.":
                    $ adinemood += 1
                    $ renpy.pause (0.5)
                    Ad giggle b "Well, I didn't take you to be so flirtatious. Maybe I will, but not right now."
                    c "The offer's open whenever you're ready."
                    Ad "We get there when we get there. For now it's my turn."
                "Maybe one day.":
                    c "Maybe you'll get a chance one day."
                    Ad "Indeed. Until then, it's my turn."
            Ad normal b "What do you like most about dragons?"

    menu:
        "I've done nothing but stare at dragon ass since I got here.":
            $ adinemood -= 1
            $ renpy.pause (0.5)
            Ad "Seriously? That's all you've done? That's disgusting."
            c "Can you really blame me?"
            call bangok_four_adine1_angercheck
            Ad "Have you been staring at mine?"
            menu:
                "Yes, and it's gorgeous.":
                    $ adinemood += 1
                    $ renpy.pause (0.5)
                    Ad giggle b "Well at least you're honest, pervert."
                "Yes, and it's very fat.":
                    $ adinemood -= 2
                    c "I have, and it's one of the fattest dragon asses I've seen."
                    $ renpy.pause (0.5)
                    Ad sad "Wh-what? Why would you-"
                    c "No no that's not a bad thing! I like it fat!"
                    Ad sad "I- let's just move on."
                "Nope.":
                    $ renpy.pause (0.5)
                    Ad annoyed "I may not like perverts, but I still prefer an honest pervert."

        "You're all graceful in their own way.":
            $ adinemood += 1
            Ad think b "How so?"
            c "Well, look at winged dragons such as yourself. You can swiftly soar through the air, rising high as you deftly ride the currents."
            c "And big four-legged dragons like the police chief are built like beasts, like they could easily drag a solid steel block as big as themselves."
            c "Then the bipeds, though not as nimble as humans, are still able to gently move things around with their hands."
            Ad "Well, I guess I never thought about it, but you're right."
            c "Not to mention their beautiful scale patterns, like yours."
            Ad giggle b "Not my nose rings though."
            c "Yes your nose rings, I love those."
            Ad giggle b "Okay okay, that's enough flattery."
        "Nothing really.":
            $ adinemood -= 1
            c "Not much about them honestly. Humans are more agile, and I just really like how they look."
            Ad "Fair enough, I guess you'd prefer your own species. Still, some dragons have wings to fly, right?"
            c "Yeah, but I always found wings a bit ugly, they remind me of bats."
            Ad sad "Geez, you didn't have to say it like that."
            c "Shit, right, I'm sorry, I didn't-"
            call bangok_four_adine1_angercheck
            Ad sad "it's your turn, right?"
            c "Yeah, it is."

    c "Alright, my question."
    show adine think b with dissolve

    menu:
        "If I asked you to fuck me would you?":
            $ renpy.pause (0.5)
            if adinemood >= 2:
                show adine giggle b with dissolve
            else:
                show adine annoyed b with dissolve
            Ad "That's a very good question. Which you won't get an answer to; I'll take a dare on this one."
            call .dare_table_2
        "What is the highest you've flown?":
            Ad think b "I'm not sure. Pretty high, I think. Turns out you lose confidence quickly when everything below you looks like an ant farm and have nothing to focus on except how fast you can drop."
            c "Imagine that, I can't see why anyone would be scared of terminal velocity."
            Ad giggle b "You just reminded me of how hard it can be to convey tone through text. I've had to re-read lines in a few of my books because the author didn't tell me a character was being sarcastic."
        "Have you ever tried sleeping upside down?":
            $ adinemood += 1
            Ad think b "That sounds ridiculous. Why would I ever do that?"
            c "There's a flying mammal species on Earth that does that. You kinda remind me of them."
            Ad normal b "Well I'm not a mammal last I checked, but fair enough. That sounds an awful lot like bats though."
            c "Wait, that's what they're called on Earth too. Weird."
            Ad giggle b "Well I'm glad I remind you of them then, they're pretty cute."
        "Have you ever peed mid-flight?" if persistent.bangok_watersports:
            Ad annoyed b"Ugh, don't remind me. Yeah, once. Thankfully I was far from town and there was nobody below me."
            c "So you have. What was it like?"
            Ad think b "Less messy than doing it on the ground, but it just didn't feel right. Like \"Hey you should be doing this down there\" and all."
            c "Yeah, fair enough."

    Ad normal b "Okay, from the dragons you've met here so far, who do you fancy the most?"

    menu:
        "You":
            $ adinemood += 1
            Ad giggle b "Me? S-sorry, but isn't it a bit early for that?"
            c "Maybe, but you're the one who's left the best impression so far."
            Ad normal b "Well thanks. Maybe one day."
        "Remy" if remyscenesfinished > 0 and remystatus in ["neutral","good"] and not remydead:
            $ adinemood += 1
            Ad think b "Him huh? Thanks actually. He needs someone to look out for him."
            c "What makes you say that exactly?"
            Ad normal b "Nothing in particular, I'm just worried about him is all."
        "Bryce" if brycescenesfinished > 0 and brycestatus in ["neutral","good"] and not brycedead:
            Ad giggle b "He really is quite the pick, huh?"
            c "So strong, so loyal, and so charming."
            Ad normal b "And with the strongest liver for miles, I hear." ## Did you do that on purpose? "Miles"?
        "Anna" if annascenesfinished > 0 and annastatus in ["neutral","good"] and not annadead:
            $ adinemood -= 1
            Ad annoyed b "I don't know what you see in her if I'm being honest."
            c "What do you mean?"
            Ad think b "That bitch from the other day? The one who was rude to everyone at every possible turn?"
            c "I know, she's rough around the edges, but I just think there's more to her than that."
            Ad frustrated b "What's that supposed to-- {w=0.5}{nw}"
            Ad annoyed b "What's that supposed to-- {fast}Nevermind. I don't want to talk about this."
        "Lorem" if loremscenesfinished > 0 and loremstatus in ["neutral","good"] and not loremdead:
            Ad think b "Sorry, I don't know that name. Who is it?"
            c "Cute delivery flyer, blue scales."
            Ad "Actually I think I've run into him a few times, never got his name though."
        "Too early to tell":
            Ad normal b "Yeah, that makes sense. You haven't been here that long."
            c "I just want to wait until it feels right."
            Ad think b "Honestly, I feel the same way. You can't really force these things."
        "Take dare":
            Ad giggle b "About time!"
            Ad think b "Hmm, what am I going to do with you?"
            if adinemood < 3:
                c "Anything you want."
                Ad disappoint b "I really have no clue"
                c "Should put a pin in this?"
                Ad think b "Yeah, let's do your turn next."
            else:
                c "Anything you ask."
                Ad think b "Well, I have been curious about something."
                c "And what would that be?"
                Ad normal b "Would you mind taking your clothes off? I've never seen humans without all those on."
                menu:
                    "Strip naked.":
                        m "I remove my clothing without hesitating, baring my naked body for Adine."
                        Ad think b "Much smoother than I expected. It looks kinda cute actually."
                        c "Thanks. I'll just set these aside for now."
                    "Explain that humans see nudity as sexual.":
                        Ad sad b "O-oh! Sorry, I didn't mean to. I mean, I didn't know, it's just--"
                        menu:
                            "Strip naked.":
                                $ adinemood += 1
                                m "I start removing my clothes, ignoring Adine's sudden silence. She blushed, seeming to enjoy the show."
                                Ad giggle b "Thanks! I think. Jeez, now I feel like I owe you something."
                                c "Maybe I'll call it in later. Or maybe your next dare's gonna sting."
                                Ad normal b "Don't push me too hard! Thanks though. I really was curious about that."
                            "Comfort her.":
                                c "Don't worry, I doubt you've had many humans telling you how important clothes are."
                                Ad giggle b "Right? I just wanted to know what you looked like. I didn't know how forward I sounded."
                                c "Any idea what your backup dare is?"
                                Ad think b "Sadly no, that was all I had."
                                c "Let's put a pin in that for later then."

    menu:
        "If I dared you to fuck me, would you?":
            Ad giggle b "Well that's awful forward of you."
            c "Perhaps, but definitely something I'd like to know."
            Ad normal b "Why don't you try it and find out?"
        "Turn the tables. Who are you most interested in?":
            Ad giggle b "Oh no you don't. I'm taking a dare on this one."
            c "Works just fine for me."
        "Do you use your tail as a phone often?":
            Ad think b "I-- What? What's that supposed to mean?"
            c "You know, it's vaguely phone-shaped. Do you ever just use it as a phone?"
            Ad disappoint b "I genuinely have no idea how to answer that. I'll take a dare."
    jump .dare_table_3

    label .dare_table_1:
        menu:
            "Lift that rump so I can test it.":
                $ adinemood -= 2
                $ renpy.pause (0.5)
                Ad frustrated b "Seriously? Is that all you think about?"
                c "You're really--"
                Ad frustrated b "Fuck you, and fuck this place."
                if adinemood < 0:
                    $ renpy.pop_call()
                    call bangok_four_adine1_angercheck
            "I dare you to accept my apology.":
                $ adinemood += 1
                $ renpy.pause (0.5)
                Ad annoyed b "Is that really your way of saying sorry?"
                c "It is, because I am. I thought we were... y'know..."
                Ad disappoint b "Fine, I guess I'll overlook this misunderstanding, but only because your apology was a bit clever."
            "Strip naked!":
                $ headgear = False
                $ renpy.pause (0.5)
                show adine normal b with dissolve
                Ad "Just that? Alright I guess."
                stop music fadeout 1.0
                show black with fade
                play sound "fx/undress.ogg"
                $ renpy.pause(2.5)
                show adine giggle
                hide black
                with fade
                play music "mx/serene.ogg"
                Ad "There. Satisfied?"
                c "Absolutely, you have a nice face."
                Ad frustrated "If you think flattery's going to make me forgive you for being so rude, you're wrong."
                if persistent.c1disrobement == False:
                    $ mp.disrobement = True
                    $ mp.save()
                    $ persistent.c1disrobement = True
                    $ achievement.grant("Disrobement")
                    $ persistent.achievements += 1
                    call syscheck from _call_bangok_four_syscheck_48
                    play sound "fx/system.wav"
                    if system == "normal":
                        s "You got Adine to strip naked!"
                    elif system == "advanced":
                        s "You got Adine to strip naked. Wow."
                    elif True:
                        s "You got Adine to strip naked. Interesting way of asking her to take off her headgear."
                Ad normal "Anyways, let me just put these back on quick, I've grown so used to their weight I notice when they're off instead of the other way around."
                show black with fade
                play sound "fx/undress.ogg"
                $ renpy.pause(1.0)
                show adine normal b
                hide black
                with fade
                $ renpy.pause (0.5)
        return

    label .dare_table_2:
        menu:
            "Kiss me!":
                $ renpy.pause (0.5)
                Ad think b "Is that your dare?"
                c "Yup."
                Ad annoyed b "Alright, fine, I'll do it."
                stop music fadeout 1.0
                scene black with fade
                play sound "fx/kiss.wav"
                $ renpy.pause(1.0)
                scene o2 at Pan((0, 250), (0, 250), 0.1)
                show adine giggle b
                with fade
                play music "mx/serene.ogg"
                Ad giggle b "There we go, happy?"
                show adine normal b with dissolve
                c "Definitely."
            "Eat a raw potato.":
                $ adinemood -= 1
                Ad "I didn't know you were evil."
                c "Well, are you going to do it?"
                show adine annoyed b with dissolve
                Ad "Alright."
                c "You can find one in the pantry."
                hide adine with dissolve
                play sound "fx/drmg.wav"
                $ renpy.pause(4.0)
                show adine normal b with dissolve
                m "Adine left to the pantry and came back with a potato in hand."
                Ad "Ugh, you couldn't have chosen a more mildly annoying dare."
                c "That's the fun of this, eh?"
                Ad "I swear if I get a good idea I'm getting revenge."
                stop music fadeout 1.0
                show black with fade
                play sound "fx/bite.wav"
                $ renpy.pause(1.0)
                m "Adine put the potato in her mouth and took a chomp. With how small it was compared to her jaw, half of it was gone in a single bite, though the shape of her face made it hard to fit in."
                m "Adine chewed the thing rapidly, evidently not enjoying the sensation of the bitter, starchy tuber."
                m "After a bit, she swallowed it, then put the other half in her mouth, downing it more quickly than the other."
                show adine normal b
                hide black
                with fade
                play music "mx/serene.ogg"
                Ad "There you go. I'll be taking my turn now, thank you very much."
            "Slide two claws into your vagina.":
                $ adinemood -= 1
                Ad annoyed b "You want me to masturbate?"
                c "Well, not completely."
                call bangok_four_adine1_angercheck
                Ad disappoint b "Alright, give me a moment. I'm not used to having an audience."
                stop music fadeout 1.0
                show black with fade
                $ renpy.pause (1.5)
                $ adinemood += 2
                Ad giggle b "Mnnf, there we-- gosh, am I that wet already?"
                Ad "Oh yeah, that's more like it! I-- W-wait!"
                hide black with fade
                Ad "Sorry, I guess I got a bit carried away."
                c "I'm not complaining. Feeling a bit pent up?"
                Ad "Just a bit, I'll take care of that when I get home."
        return

    label .dare_table_3:
        menu:
            "Let me see that butt of yours.":
                jump .ending
            "I'd like to see your rump, if that's not too much.":
                jump .ending
            "Go streaking naked outside!":
                Ad think b "Wait, but for my headgear, I'm already naked..."
                c "I didn't think this through."
                Ad "Oh! I just noticed, it stopped raining!"
                c "I guess it's time for you to head out then, huh?"
                Ad "I suppose so."
                Ad giggle b "By the way, you don't have to order anything if you want me to come over again. Here's my private number."
                c "Thanks, I'll keep that in mind."
                Ad "Bye!"


    label .ending:
        if adinemood < 2:
            jump .poor_ending
        elif adinemood < 5:
            jump .med_ending
        elif adinemood < 7:
            jump .good_ending
        else:
            jump .best_ending

    label .poor_ending:
        Ad annoyed b "That's your dare? Seriously?"
        c "Well, will you?"
        Ad annoyed b "Looks like it's stopped raining. I'll be heading home then."
        c "Sorry. Still friends?"
        Ad "We'll see. I'll leave you my number."
        hide adine with dissolve
        m "Adine scribbled some numbers on a piece of scrap paper, then left without saying anything else." 
        stop music fadeout 2.0
        m "On her way out though, she looked back and shot me an exasperated look before lifting her tail, showing me her heavenly rear in full."
        play sound "fx/door/doorclose3.wav"
        $ renpy.pause(0.5)
        m "Then, just like that, she was gone. I was just relieved that she had seemingly forgiven me, at least a little bit."
        $ persistent.adine1skip = True
        $ adinestatus = "neutral"
        $ adinescenesfinished = 1
        jump _mod_fixjmp

    label .med_ending:
        Ad think b "Hmm, is that your dare?"
        c "It is. I'd like to see it."
        Ad giggle b "You really are a perverted one huh?"
        c "I'd be lying if I said no."
        Ad annoyed b "Alright then."
        hide adine with dissolve
        m "Without anotehr word, Adine turned around and lifted her tail high as can be, showing me her gorgeous posterior in all its glory."
        Ad giggle b "Enjoying the view?"
        c "I most certainly am, thank you."
        Ad normal b "Good, because it looks like the rain has stopped, which means it's time for me to go."
        show adine normal b with dissolve
        m "Adine wrote a string of numbers on a scrap of paper and slid it to me."
        Ad "Here, no need to order food if you want to stare at me again."
        hide adine with dissolve
        play sound "fx/door/doorclose3.wav"
        $ renpy.pause(2.0)
        stop music fadeout 1.0
        $ persistent.adine1skip = True
        $ adinestatus = "neutral"
        $ adinescenesfinished = 1
        m "We exchanged goodbyes, and just like that she left the building, leaving me aroused."
        jump _mod_fixjmp

    label .good_ending:
        Ad giggle b "My, such a forward demand. I like it."
        c "So?"
        hide adine with dissolve
        m "Adine answered my question by turning around and curling her tail upwards, bringing the crescent at the end back to spread her visibly damp slit."
        Ad disappoint b "I'll admit, I got a bit horny hanging around here. Just a shame this is the first date."
        c "I wouldn't mind helping you out, you know."
        Ad giggle b "That's a tempting offer. And I mean that, I want to."
        Ad disappoint b "But this is the first date, I have to tease you with something!"
        c "True. Maybe another day, then."
        Ad normal b "In the mean time, do you have this memorized? You'll need that to masturbate to."
        c "Oh absolutely, I'd never forgot that."
        Ad giggle b "Good, because it looks like it's stopped raining. I have to go home and also masturbate."
        $ renpy.pause (1.0)
        m "Finally, she let her tail down, the top dripping slightly on my floor as she grabbed some paper and scrawled her phone number on." ## The "top" of what?
        stop music fadeout 1.0
        m "After exchanging goodbyes with me, Adine started heading out the door. Though, on her way out, she moved her tail out of the way again and smirked back at me, teasing me further."
        play sound "fx/door/doorclose3.wav"
        $ renpy.pause(2.0)
        $ persistent.adine1skip = True
        $ persistent.headgear = headgear
        $ adinestatus = "good"
        $ adinescenesfinished = 1
        jump _mod_fixjmp
    
    label .best_ending:
        Ad think b "You really are horny, aren't you?"
        c "More than a little."
        Ad giggle b "You and me both, you really got me worked up."
        c "So?"
        Ad normal b "I'll do you one better. Lay down and let me do my thing, no effort needed on your part."
        ## Implement the eject sequence here for if the player doesn't want to fuck Adine, unless the opening counted as the eject sequence.
        stop music fadeout 2.0
        play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/undress.ogg"]
        show black with dissolve
        $ renpy.pause(0.4)
        m "Without thinking about it, I obediently got on my back and waited patiently for Adine to approach."
        m "As promised, she offered more than just flashing me her rear. She sat on my chest and looked down into my eyes, her wet slit rubbing against me."
        m "As our gazes met, and a blush covered her face, she spoke in a low, gentle tone."
        Ad think b "So, how good are you with your tongue?"
        c "Good enough."
        c "Why, thinking of teaching me what dragon tastes like?"
        Ad giggle b "You owe me that much for getting me worked up like this."
        m "She stood up and turned around. I had plenty of chance to protest if I so chose, but I opted not to. Instead, I closed my eyes and opened my arms as she plopped her rump on my nose, her soaking wet dragon snatch within reach of my tongue."
        m "I didn't hesitate to hug her rump, letting my tongue out to lap at her."
        Ad giggle b "Ooooh yeah, just like that [player_name]."
        m "Her lustful moans repeated the sentiment as I gorged myself on her fluids."
        m "I felt my own arousal grow from the intoxicating mix of proximity and scent."
        Ad think b "I hope you're enjoying yourself-- Nnf... As much as I'm enjoying you."
        m "I couldn't respond through the dragon ass in my face, but a couple of reassuring pats on her hips gave all the assurance needed."
        m "After a few moments passing all too soon, Adine began to buck her hips on impulse, seemingly close to orgasm."
        play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/varagrowl.ogg"]
        m "And after a few moments more, she came, splashing my tongue with her juices as I continued licking."
        m "As she started to wind down, she slowly rolled off of me, letting me sit up and meet her gaze."
        $ renpy.pause (0.3)
        play sound "fx/undress.ogg"
        hide black
        show adine giggle b
        with dissolvemed
        Ad "Thanks, I really needed that."
        c "No problem. Now, about my turn?"
        Ad normal b "Another time. It looks like the rain's stopped."
        c "You owe me one, understand?"
        Ad giggle b "Yeah, agreed. Here's my personal number. Let's meet again."
        m "Adine scribbled her number down on some scrap paper and left it on the table."
        hide adine with dissolve
        play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/door/doorclose3.wav"]
        m "After exchanging some final goodbyes, she went out the door, leaving me horny with no dragon to satisfy me."
        $ renpy.pause(1.0)
        $ persistent.adine1skip = True
        $ persistent.headgear = headgear
        $ adinestatus = "good"
        $ adinescenesfinished = 1
        jump _mod_fixjmp