init python in bangok_four_xkatsu:
    unplayed = True
    whatcum = True
    protection = True
    playercame = False
    playerstuffed = None
    target = None

    safety = True
    flavor = 0

    # Fill
    # 0 - Haven't gotten Katsu off yet, or he (tried) to get himself off
    # 1 - Gave Katsu a raw handjob, about one bucket. Disappointing to the artisan.
    # 2 - Gave Katsu a good time, but not ideal. About one and a half buckets.
    # 3 - Blew Katsu's mind and cleared out all his pipes. Both buckets, plus maybe playerstuffed.
    fill = 0


    gethelp = True
    getcart = True

label bangok_four_xkatsu:
    show black with dissolvemed
    $ renpy.pause (1.0)
    Ka excited flip "Wait a minute!" with Shake ((0, 0, 0, 0), 2, dist=10)
    hide black with dissolveslow
    $ renpy.pause (0.5)
    play music "mx/fun.ogg" fadein 2.0
    c "What is it, Katsuharu?"
    Ka smile flip "There is a single flavor I can prepare rather quickly. It doesn't involve many ingredients."
    Ka exhausted flip "I don't often get a chance to harvest, but I feel like today will be an exception."
    c "Oh? What flavor?"
    Ka normal flip "It's a... rather special one, only for special customers."
    c "What does it taste like?"
    Ka normal flip "Mostly like its primary ingredient."
    Ka smile flip "My seed."

    label bangok_four_xkatsu_seedmenu:
    $ renpy.pause (0.8)

    menu:
        "Ew. No way.":
            Ka exhausted flip "It's all I'll have properly prepared until a day or two from now."
            c "I think I'll wait."
            c "Are there any other flavors with {i}that{/i} in it?"
            Ka "No. I don't tend to experiment with it all that often, because my mentor wasn't the right gender to produce that ingredient. It couldn't have been a part of her recipe."
            c "Well, I could have gone my whole life without knowing you cummed in any of your ice cream."
            Ka "My application is more refined than--"
            c "Have a good afternoon, Katsu."
            Ka "..."
            jump _mod_fixjmp
        "What, like cum?" if bangok_four_xkatsu.whatcum:
            $ bangok_four_xkatsu.whatcum = False
            Ka "Yes."
            c "Semen?"
            Ka "Yes."
            c "Baby batter?"
            Ka excited flip "That exactly."
            jump bangok_four_xkatsu_seedmenu
        "No, thanks.":
            c "I think I'd like to wait for a wider selection."
            Ka normal flip "Are you sure? It's all I'll have properly prepared until a day or two from now."
            # Ka normal flip "If you say so. But know that after tonight my special should be available for at least a few days."
            c "I'll keep that in mind, thanks."
            c "Have a good afternoon, Katsu."
            jump _mod_fixjmp
        "O...kay.":
            Ka normal flip "I understand that ingredient isn't for everyone."
            c "No, no. I'm interested to try it, I've just never heard of something like that."
            Ka smile flip "Well, if it didn't taste good, I wouldn't be making it."
        "Oooh.":
            Ka excited flip "Interested, eh?"
            Ka smile flip "Good."

    Ka "We'll need to return to my home. I'm afraid it needs to be prepared quite quickly, and kept quite cold."
    c "Alright. Lead on."
    scene black with dissolvemed
    play sound "fx/steps/rough_gravel.wav"
    stop sound fadeout 1.0
    scene np3x at Pan((0, 0), (0, 220), 4.0) with dissolveslow
    m "Katsuharu led me back through town, to a small hut not far from his original spot."
    m "Beckoning me through a back door, he entered an expansive kitchen."
    scene kitchen with dissolve
    c "Wow."
    c "This corner looks kinda like the kitchen at my place."
    show katsu exhausted at right with dissolve
    Ka "I'm sure it does. I needed to replace an oven and some stoves, they came in and redid the walls too with this monstrosity."
    Ka "\"Modular\" they called it. Pfah."
    $ renpy.pause (0.5)
    m "I tried to turn his attention away from the partial remodel by returning to the topic at hand."
    c "So the, uh, ice cream. How do you usually harvest the main ingredient?"
    show katsu normal with dissolve
    show katsu at center with ease
    Ka "A mix of methods. Sometimes I can do it all by myself. Sometimes I wheel out a mounting stand."
    Ka smile "Sometimes I have volunteers from the interested customer base."
    c "Volunteers, huh?"
    Ka normal "But we can't think about that yet. First we need somewhere for it to go."
    show katsu normal flip with dissolve
    $ renpy.pause (0.3)
    hide katsu with easeoutright
    $ renpy.pause (0.5)
    play sound "fx/2buckets.ogg"
    show katsu normal at right with easeinright
    $ renpy.pause(1.0)
    m "Katsu returned with two concerningly large buckets, setting them down."
    c "Wait, can you actually produce that much?"
    Ka "Hm? Oh."
    Ka smile "Of course not. This is to chill what I can make."
    Ka normal "Start filling these from that icebox there."
    m "Curious to see how this would turn out, I opened the icebox and began digging hard chunks of ice into the buckets Katsu had brought."
    play soundloop "fx/digice.ogg"
    $ renpy.pause(1.0)
    show katsu normal flip with dissolve
    $ renpy.pause (0.3)
    hide katsu with easeoutright
    $ renpy.pause (0.5)
    play sound "fx/2buckets.ogg"
    show katsu normal at right with easeinright
    m "Katsu returned with two more, smaller buckets."
    stop soundloop fadeout 0.5
    c "Do I fill those too?"
    Ka "No. You've got good layers in the bottom of those. Here, fit these inside the first two, then add ice inbetween."
    Ka exhausted "And keep the ice out of the inner buckets!"
    play sound "fx/sphereslide.ogg"
    show katsu normal with dissolve
    stop sound fadeout 1.0
    play soundloop "fx/digice.ogg"
    $ renpy.pause (2.0)
    m "Katsu inspected my actions while I worked, remaining mostly silent throughout."
    $ renpy.pause (3.3)
    stop soundloop fadeout 0.5
    Ka smile "That's enough."
    m "I set the scoop back inside, then shut the icebox."
    Ka normal "Now, do you want to keep helping? Or do you want to wait in my sitting room for an hour?"
    m "I got the feeling that by \"helping\" I'd be a \"volunteer from his interested customer base.\""
    menu:
        "I'll help.":
            jump bangok_four_xkatsu_help
        "I'll wait.":
            jump bangok_four_xkatsu_wait

label bangok_four_xkatsu_wait:
    $ bangok_four_xkatsu.unplayed = True
    $ renpy.pause(0.5)
    Ka exhausted "Ah."
    Ka normal "Well, sitting room's that way. Go take a nap or something while I get this ready."
    $ renpy.pause(0.5)
    play sound "fx/steps/clean2.wav"
    show black with dissolvemed
    $ renpy.pause(0.8)

    nvl clear
    window show
    n "When Katsu had said an hour wait, he hadn't been kidding."
    n "It was over twenty minutes before I heard noises that indicated he might be successfully producing the key ingredient."
    n "I dozed off after that, waiting for him to call me back in about the ready ice cream."
    window hide
    nvl clear

    $ renpy.pause (1.0)

    show katsu exhausted with None
    jump bangok_four_xkatsu_ready

label bangok_four_xkatsu_help:
    $ bangok_four_xkatsu.unplayed = False
    Ka smile "Thought you were the kind who might."
    show katsu at center with ease
    m "He moved over top of one of the buckets, nudging them closer together, then arranging his hindlegs on either side."
    Ka exhausted "Give me a minute to get the old baculum moving on out."
    $ renpy.pause (0.5)
    m "He strained, but it was clear whatever he was thinking and whatever he was doing together weren't going to be enough."
    m "I knelt by the buckets, inspecting the spot where the tip of something was just peeking between two of his underbelly plates, back between his legs."
    Ka normal "Well, if you want to help move things along, I won't stop you."
    m "With his tacit permission, I reached up between his legs and poked his peeking tip."
    Ka excited "That's a bit more like it!"
    m "His rod emerged quite a bit further, revealing a few inches of cockflesh. I took ahold and gave it some light pumps, finding it surprisingly soft and malleable to the touch."
    c "It's not that hard?"
    Ka exhausted "What do you think happens as you get older? Body starts doing weird things."
    Ka normal "Can tell you, still works just fine."
    Ka exhausted "Or it did about two weeks ago, when I last made this."
    c "Huh."
    Ka smile "Has some advantages. Can fit in some people'd otherwise be too small. Like you, maybe."
    if bangok_four_playerhasdick is None:
        Ka exhausted "Huh. Guess I never did ask. You have one of these?"
        c "A penis?"
        Ka normal "What else?"
        menu:
            "Yeah, I have one.":
                $ bangok_four_playerhasdick = True
            "Nope, don't have one.":
                $ bangok_four_playerhasdick = False
        c "What did you mean, though? Fit in... inside me?"
    else:
        c "Fit inside me?"
    Ka exhausted "You don't get the biggest servings from just your hands. Especially not mine."
    m "This had rapidly progressed from ice cream to outright sex. I let go of Katsu's cock, now a little over a foot long, and considered what I actually wanted."
    $ bangok_four_xkatsu.whatcum = True
    label bangok_four_xkatsu_sexmenu:
    menu:
        "I didn't expect to go beyond a handjob.":
            $ renpy.pause(0.5)
            Ka exhausted "Well, that's better than no help."
            $ renpy.pause (0.3)
            show katsu normal with dissolve
            m "I knelt back down next to Katsuharu's hindquarters, his bright hide and the shiny bucket on the floor making me feel a little like I was getting down to milk a cow."
            m "As I took hold of his shaft again, it twitched, a tiny, glinting dollop of pre peeking out of the end. I was half curious to taste it, to find out what I was getting myself into flavor-wise."
            menu:
                "Mouth.":
                    $ renpy.pause(0.5)
                    $ bangok_four_xkatsu.target = "mouth"
                    c "I, ah, I think I might help with my mouth after all."
                    jump bangok_four_xkatsu_get_underneath
                "Hands.":
                    $ renpy.pause(0.5)
            play soundloop "fx/massage.ogg" fadein 1.5
            m "Putting the droplet from my mind, I aimed Katsuharu's cockhead into the first bucket and began to pump with both hands."
            $ renpy.pause(1.0)
            Ka exhausted "You know, dry pumping tugs at my skin a lot. Would help if you spread my pre around. Or played with my tip a bit more."
            stop soundloop fadeout 1.0
            c "Do you have lube? That'd probably be an easier way to get you more slick."
            Ka "Sure, sure."
            show katsu normal flip with dissolve
            m "Katsuharu stepped back over the buckets, cock pulling free from my hand with a smear of pre across my palm."
            hide katsu with easeoutright
            m "Then he wandered off to another part of the kitchen."
            $ renpy.pause(0.8)
            c "Should I help you look, or...?"
            Ka "No, no. Should just be a moment."
            play sound "fx/rummage.wav"
            $ renpy.pause(1.0)
            m "The wet smear on my hand drew my attention, but I tried to fight the urge to take this ice cream date to weird places like sucking off the old man."
            m "We were harvesting an ice cream ingredient. Nothing more."
            show katsu normal at Position(xpos=0.8,xanchor='center') with easeinright
            play sound "fx/box.wav"
            $ renpy.pause(0.8)
            show katsu normal at Position(xpos=0.5,xanchor='center') with ease
            m "Katsuharu returned, dropping a heavy bottle of lube with a plunger head next to me before taking up his position over the buckets once more."
            m "Squirting a slippery layer over the pre-stain on my hand, I set back to work."
            play soundloop "fx/rub2.ogg" fadein 1.0
            $ renpy.pause(3.0)
            show katsu exhausted with dissolvemed
            Ka exhausted "Getting there. Closer to my tip, maybe?"
            show katsu normal at Position(xpos=0.49,xanchor='center') with ease
            m "I moved my ministrations downward. As I passed over the slight ridge to Katsuharu's head, he thrust a little in my hands and began to pant."
            $ renpy.pause(1.0)
            Ka exhausted "Almost..."
            $ renpy.pause(1.0)
            stop soundloop fadeout 0.5
            play sound "fx/snarl.ogg"
            show katsu smile at Position(xpos=0.49,ypos=1.03,xanchor='center') with ease
            m "Katsuharu thrust through my hands and began to cum, dumping thick, creamy ropes into the bottom of the bucket."
            show katsu exhausted with dissolve
            m "At first I thought he'd have a dozen shots and that'd be it, but as the cum kept coming and even began to splatter a bit inside the pint-sized inner bucket, I let go of his length and shuffled back to protect my clothing."
            $ renpy.pause(0.5)
            $ bangok_four_xkatsu.fill = 1
            m "Katsuharu's spurts came to an end before he'd filled that first bucket."
            $ renpy.pause(0.8)
            c "Wow. That..."
            $ renpy.pause(0.8)
            Ka "Eh."
            $ renpy.pause(0.3)
            jump bangok_four_xkatsu_filldone
        "I guess I could suck you off.":
            $ bangok_four_xkatsu.target = "mouth"
            jump bangok_four_xkatsu_get_underneath
        "I suppose I could help you with my ass.":
            $ bangok_four_xkatsu.target = "ass"
            jump bangok_four_xkatsu_get_underneath
        "If that's what it takes, I could help you with my vagina." if bangok_four_playerhasdick == False:
            $ bangok_four_xkatsu.target = "vag"
            jump bangok_four_xkatsu_get_underneath
        "What if I fit inside you?" if bangok_four_playerhasdick == True and bangok_four_xkatsu.playercame == False:
            Ka exhausted "Eh?"
            show katsu at Position(xpos=0.45,xanchor='center') with ease
            m "I moved around to Katsuharu's hindquarters, already unbuckling my pants to reveal my hardening shaft."
            Ka normal "Ah, one of those customers."
            Ka exhausted "Y'know, that's not always enough for me. Especially with you being all that small compared to me."
            m "Getting under his tail, I hoisted it and his hindquarters up."
            c "We have a saying in our world: It's not your size, it's how you use it."
            Ka smile "Didn't say we couldn't try it."
            if persistent.bangok_cloacas == True and bangok_four_malepartners + bangok_four_femalepartners < 1:
                $ renpy.pause (0.8)
                m "Looking down at Katsuharu's rear under his tail, I quickly realized a problem."
                c "Uh. Where {i}is{/i} your ass?"
                Ka exhausted "What are you talking about? Same place anyone else's is."
                c "I haven't exactly done this with any other dragons."
                Ka normal "I see. Well it's the same hole my rod comes out of, just a little further back."
                m "Kneeling down and tugging his horizontal slit a little wider, I saw exactly what he meant."
                c "Ah. Found it."
                show katsu smile with dissolve
                m "I stood, tugging his tail and rear back into position."
            $ renpy.pause(1.0)
            show katsu excited with dissolve
            m "Katsuharu's underbelly was pliable at his age, his plates barely impeding me as I sank my shaft into the large, warm confines of his ass."
            Ka "Ha! Been a while since I've had anything back there."
            Ka smile "You're a bit dry, though. You sure this is the way you want to do things?"
            c "D-Definitely."
            Ka normal "No scales off my back if you can't get me off."
            Ka smile "No ice cream until you do!"
            play soundloop "fx/rub2.ogg" fadein 3.0
            show katsu:
                xanchor 0.5
                ease 0.15 xpos 0.445
                ease 0.5 xpos 0.45
                repeat
            m "Rising to his challenge, I began to move, pounding into his rear to try to get him going before I got off."
            $ renpy.pause(3.0)
            Ka "You're not falling asleep back there, are you?"
            c "Seriously?"
            Ka normal "I can tell you're trying. Doesn't mean you'll get anywhere."
            $ renpy.pause(3.0)
            Ka exhausted "What's that?"
            c "I... didn't say... anything."
            Ka "Nah, fleshy bit slapping my staff each time you push. That's not part of me, is it?"
            $ renpy.pause(0.8)
            m "Looking down, I spotted my balls swinging into Katsuharu's dick every time I thrust forward."
            c "That's... me."
            Ka normal "Mm. Well if you did a bit more of that, you might have a chance."
            $ bangok_four_xkatsu.whatcum = True
            $ bangok_four_malepartners += 1
            label bangok_four_xkatsu_assfuckmenu:
            menu:
                "[[Stroke him.]":
                    pass
                "I can't grow more balls!" if bangok_four_xkatsu.whatcum == True:
                    $ bangok_four_xkatsu.whatcum = False
                    Ka exhausted "More what?"
                    Ka normal "Not my problem, is it?"
                    jump bangok_four_xkatsu_assfuckmenu
                "I... I think I'm about to...":
                    Ka smile "Don't hold back on my account. You can help some other way."
                    stop soundloop fadeout 0.5
                    play sound "fx/rub1.ogg"
                    show katsu at Position(xpos=0.45,xanchor='center') with ease
                    $ renpy.pause(1.4)
                    play sound "fx/extinguish.ogg"
                    show black with fadequick
                    $ renpy.pause(1.0)
                    hide black with dissolveslow
                    $ renpy.pause(0.5)
                    m "I slipped out of Katsuharu, limpening rapidly in the chill air of his kitchen."
                    $ bangok_four_xkatsu.playercame = True
                    $ renpy.pause(0.8)
                    show katsu at center with ease
                    Ka smile "So. Now how will you get my cream out?"
                    jump bangok_four_xkatsu_sexmenu

            stop soundloop fadeout 0.5
            show katsu at Position(xpos=0.45,xanchor='center') with ease
            m "I stopped, getting a better grip on his tail from further down."
            Ka exhausted "Eh?"
            c "Give me a second."
            m "With his tail settled on one shoulder, I was able to get my other hand under his legs, taking a grip on the lower section of his staff."
            Ka smile "That's more like it!"
            Ka normal "Can you still move like that?"

            play soundloop "fx/rub2.ogg" fadein 3.0
            show katsu:
                xanchor 0.5
                ease 0.15 xpos 0.445
                ease 0.5 xpos 0.45
                repeat
            m "I answered his question by resuming my pace, now with the added stimulation of my hand around his cock."
            show katsu smile with dissolve
            $ renpy.pause(1.5)
            Ka "Definitely getting closer."
            m "He wasn't kidding. I was maybe a few dozen thrusts away from blowing my load in him."
            m "But after his earlier teasing, I couldn't just fail."
            $ renpy.pause(1.0)
            stop soundloop fadeout 0.5
            show katsu at Position(xpos=0.45,xanchor='center') with ease
            m "I hilted in Katsuharu, holding myself in his warm interior while I focused on his shaft for a moment."
            m "Mated up against his rear, I could feel his body expand as he took a breath."
            Ka exhausted "That's not you cumming already, is it?"
            m "Only when he complained did I start moving again."
            play soundloop "fx/rub2.ogg" fadein 3.0
            show katsu excited:
                xanchor 0.5
                ease 0.15 xpos 0.445
                ease 0.5 xpos 0.45
                repeat
            with dissolve
            $ renpy.pause(0.5)
            Ka exhausted "What are you doing, playing around like that?"
            c "Depends, is it working?"
            $ renpy.pause(1.5)
            m "He didn't say, but I could see it in his face that he was closer than he'd expected."
            stop soundloop fadeout 0.5
            show katsu at Position(xpos=0.45,xanchor='center') with ease
            m "I was approaching my limits, though, so I stopped inside him again, hand pumping up and down the lower third of his pliable shaft."
            $ renpy.pause(0.5)
            Ka smile "You might just be using that thing of yours right."
            play soundloop "fx/rub2.ogg" fadein 1.0
            show katsu excited:
                xanchor 0.5
                ease 0.15 xpos 0.445
                ease 0.5 xpos 0.45
                repeat
            with dissolve
            $ renpy.pause(0.5)
            m "Bucking my hips against his, I resumed again."
            $ renpy.pause(1.5)
            Ka excited "Ha! Gettin' real close, now!"
            menu:
                "Edge him.":
                    stop soundloop fadeout 0.5
                    show katsu at Position(xpos=0.45,xanchor='center') with ease
                    m "I stopped inside, holding his shaft tightly by the base, but unmoving."
                    $ renpy.pause(0.9)
                    Ka exhausted "H-Hey! You came now? You almost had me!"
                    $ renpy.pause(2.0)
                    m "I gave it a few seconds, both of us panting."

                    play soundloop "fx/rub2.ogg" fadein 1.0
                    show katsu excited:
                        xanchor 0.5
                        ease 0.15 xpos 0.445
                        ease 0.5 xpos 0.45
                        repeat
                    with dissolve
                    m "Then I picked up right where I left off."
                    $ renpy.pause (0.5)
                    Ka "Ha! Y-Yes! Just a bit more!"
                    $ renpy.pause(0.8)
                    stop soundloop fadeout 0.5
                    show katsu at Position(xpos=0.45,xanchor='center') with ease
                    $ renpy.pause(0.9)
                    Ka exhausted "What?"
                    $ renpy.pause(0.5)
                    Ka "You're doing that on purpose!"
                    c "Got... me."
                    m "I was out of breath, fucking the large dragon taking a heavy toll on my stamina."
                    Ka normal "Why you! I've never had--"

                    play soundloop "fx/rub2.ogg" fadein 1.0
                    show katsu excited:
                        xanchor 0.5
                        ease 0.15 xpos 0.445
                        ease 0.5 xpos 0.45
                        repeat
                    with dissolve
                    $ renpy.pause(0.5)
                    Ka "Ah! Ha! J-Just keep going this time!"
                    m "Thinking about his edge and my own stamina had taken my attention off my arousal."
                    m "I realized too late that I'd just stumbled onto my own peak, and it was a matter of moments before I couldn't hold back."
                    m "I quickened my pace, trying to bring Katsuharu over the edge with me."
                    stop soundloop fadeout 0.5
                    play sound "fx/rub1.ogg"
                    show katsu at Position(xpos=0.45,xanchor='center') with ease
                    $ renpy.pause(1.4)
                    play sound "fx/extinguish.ogg"
                    play sound2 "fx/snarl.ogg"
                    show black with fadequick
                    $ renpy.pause(1.0)
                    hide black
                    show katsu smile
                    with dissolveslow
                    $ bangok_four_xkatsu.playercame = True
                    $ bangok_four_xkatsu.fill = 3
                    $ renpy.pause(0.5)
                    m "When I came back down, Katsu's shaft twitched in my hand, rope after rope of thick seed spattering into the deep pool already in the nearer inner bucket."
                    if persistent.bangok_inflation == True:
                        m "It was already almost full!"
                    Ka exhausted "Ha! G-Gotta switch, can't overfill 'em!"
                    m "Pulling free, I ducked under Katsuharu, pulling the first bucket aside and the second bucket into the line of fire."
                    label bangok_four_xkatsu_fill3:
                    m "Then I grabbed his shaft with both hands, milking for every drop of cream we could get."
                    if persistent.bangok_inflation == True:
                        m "I needn't have bothered. The inner buckets seemed to be pint-sized, and Katsuharu was putting out well over a quart!"
                        Ka "Don't overfill the inner buckets! Gotta add other ingredients!"
                        menu:
                            "Mouth.":
                                m "Lacking other containers immediately at hand under Katsuharu's body, I took a breath and shoved his still-spurting cock into my mouth."
                                show katsu excited
                                show black
                                with dissolve
                                Ka excited "Ah. Did you fill the buckets first, or...?"
                                Ka smile "Ha. Yep."
                                m "I could do nothing to respond, as all my focus had to go to swallowing Katsu's thick, creamy seed without drowning in it."
                                m "I sank more of his soft cockflesh into my mouth, finding it pliable enough to compress and bend down my throat as he directly stuffed my stomach with cum."
                                $ bangok_four_xkatsu.playerstuffed = "mouth"
                                if bangok_four_xkatsu.target is None:
                                    m "When the pulses finally stopped and I came up for air, my shirt felt noticeably tighter. I wiped off the few thick ropes stuck to my face, licking my fingers clean."
                                else:
                                    m "When the pulses finally stopped and I came up for air, my belly bulged slightly. I wiped off the few thick ropes stuck to my face, licking my fingers clean."
                                hide black with dissolvemed
                            "Ass." if bangok_four_xkatsu.target == "ass":
                                m "Lacking other containers immediately at hand under Katsuharu's body, I turned and presented my ass again, right next to the bucket."
                                c "It's almost full!"
                                Ka exhausted "Well then--"
                                show katsu smile with dissolve
                                m "Spotting what I wanted, he stepped over and obliged."
                                show katsu excited at Position(xpos=0.5, ypos=1.04) with ease
                                c "Ah!"
                                if persistent.bangok_knot == True:
                                    m "Cum flooded my ass, backing up inside me, then was abruptly shoved even deeper as Katsuharu used the added lubrication of his seed to shove his cock further in, until a bulge near his base was pressed between my cum-spattered cheeks, against my spread asshole."
                                else:
                                    m "Cum flooded my ass, backing up inside me, then was abruptly shoved even deeper as Katsuharu used the added lubrication of his seed to shove his cock further in, until his genital slit was pressed to my cum-spattered cheeks."
                                show katsu excited at Position(xpos=0.49, ypos=1.05) with ease
                                $ bangok_four_xkatsu.playerstuffed = "ass"
                                m "I dropped my face to the floor, putting hand on my belly. I could feel the pulses in my ass translating directly to my gut, flooding me with an extra dose of cream than he'd promised."
                                m "Eventually the pulses stopped, leaving me noticeably heavier than before. At first, I wasn't sure I'd be able to get up again."
                                show katsu excited at Position(xpos=0.53, ypos=1.0) with ease
                                m "Then Katsuharu lifted the weight of his hindquarters off of mine, pulling out with a dribble of cum down my taint."
                            "Vagina." if bangok_four_xkatsu.target in ["vag", "womb"]:
                                m "Lacking other containers immediately at hand under Katsuharu's body, I turned and presented my spread lips again, right next to the bucket."
                                c "It's almost full!"
                                Ka exhausted "Well then--"
                                show katsu smile with dissolve
                                m "Spotting what I wanted, he stepped over and obliged."
                                show katsu excited at Position(xpos=0.5, ypos=1.04) with ease
                                c "Ah!"
                                m "Cum flooded my love passage, packing it almost solid in a couple of spurts as Katsuharu sank deeper into me."
                                if bangok_four_xkatsu.target == "womb":
                                    m "His seed sprayed into my sacred place as his cockhead pressed at the gate, then pressed through with a wave of warmth I could feel."
                                    m "Pulses pressed down his shaft, expanding his girth at my tightest point, before spraying directly into the deepening pool in my womb."
                                else:
                                    m "He stopped just short of my innermost gate, but with my vagina blocked by his pillar of flesh, his seed had nowhere to go but through as he packed still more inside. My passage spasmed as I felt my womb defiled by a rich, viscous flood of his seed."
                                m "I dropped my face to the floor, putting hand on my belly. I could feel the pulses in my passage translating directly to an expansion, milimeters at a time, making me look over two months pregnant with his extra dose of cream."
                                $ bangok_four_xkatsu.playerstuffed = "vag"
                                m "Eventually the pulses stopped, leaving me noticeably heavier than before. At first, I wasn't sure I'd be able to get up again."
                                show katsu excited at Position(xpos=0.53, ypos=1.0) with ease
                                m "Then Katsuharu lifted the weight of his shaft out of my body, pulling out with a dribble of cum down my thighs."
                            "Bowl.":
                                m "Spotting a mixing bowl within arm's reach on a low shelf, I grabbed it and swapped it out with the bucket."
                                m "Katsu groaned, making a pool in it as deep as my hand was wide before finally running out."
                    else:
                        m "The second bucket nearly did overfill, the level inside rising all the way to the handle bolts before finally running out."
                    $ renpy.pause(1.8)
                    Ka excited "That was amazing, [player_name]!"
                    Ka smile "Haven't been that cleared out in one go since I was a youngin' like yourself!"

                "Get him off.":
                    $ renpy.pause(1.5)
                    play sound "fx/snarl.ogg"
                    show katsu exhausted with dissolvemed
                    m "Katsu's ass clenched around me as he began to cum, and that was the last I could take too."
                    stop soundloop fadeout 0.5
                    show katsu at Position(xpos=0.45,xanchor='center') with ease
                    play sound "fx/extinguish.ogg"
                    show black with fadequick
                    $ renpy.pause(1.0)
                    hide black
                    show katsu exhausted
                    with dissolveslow
                    label bangok_four_xkatsu_fill2:
                    $ bangok_four_xkatsu.playercame = True
                    $ bangok_four_xkatsu.fill = 2
                    m "Katsuharu looked between his legs, watching his progress in the first bucket, even as his legs shook."
                    Ka "Switch 'em out at three quarters. Might need a few more pumps to get the second to..."
                    m "Pulling free, I knelt under Katsuharu, then pulled the first bucket aside and the second bucket into the line of fire when they reached the specified fullness."
                    m "Then I grabbed his shaft with both hands, milking for every drop of cream we could get."
                    $ renpy.pause(2.0)
                    m "The second bucket filled halfway, before Katsu let out a big sigh and the spurts stopped."
                    $ renpy.pause(1.0)
                    Ka "That's... hah... that's it."

            label bangok_four_xkatsu_filldone:
            show katsu at left with ease
            show katsu exhausted flip with dissolve
            m "He took a few shaky steps away from the buckets, then sat down."
            Ka "I... ah... might need some help finishing up the recipe."
            if bangok_four_xkatsu.fill == 3 and persistent.bangok_inflation == True and not bangok_four_xkatsu.playerstuffed:
                Ka "First, put that bowl away in the icebox. Don't want it to spoil too fast."
            if bangok_four_xkatsu.playerstuffed:
                c "M-Might need a minute to recover first. You, ah, pumped quite a bit into me."
                Ka smile flip "Did you have fun, at least?"
                c "Oh yeah."
            else:
                c "Sure."
            
            show black with dissolvemed
            $ renpy.pause (0.5)
            nvl clear
            window show
            n "Katsu walked me through the rest of the recipe, adding a mix of other ingredients to make his cream thicken further at the right temperatures, and a small amount of finely crushed ice for that icy texture people expect in ice cream."
            if bangok_four_xkatsu.fill == 3:
                n "We even had to set some of his seed aside in the icebox, with how full the buckets became once the ingredients went in."
            n "Then he showed me how the buckets interlocked, sealing the special ice cream mix in the casing of chill ice we'd created before."
            n "When he told me to shake the heavy mixer, I stared at him, then showed him I could barely lift it."
            n "He conceded the point, dragging out a mechanical shaker he used when he was too tired to do the job himself."
            n "We took turns operating the foot pedals that provided it the energy it needed to mix and chill our creamy goodness."
            window hide
            nvl clear
            if persistent.bangok_watersports == True and (bangok_four_xkatsu.fill > 1 or bangok_four_xkatsu.target in ["mouth","throat"]):
                window show
                n "Katsuharu asked me to bring him bowls of water a few times, throughout the recipe-making."
                n "I obliged, unsurprised he needed to rehydrate after what he'd just done."
                n "Toward the end of our prep, he began to look a little uncomfortable, and I could see his man-meet peeking from his slit again."
                n "He couldn't be ready for another round, could he?"
                window hide
                nvl clear
            show katsu excited with None
            jump bangok_four_xkatsu_ready







        "Protection?" if bangok_four_xkatsu.protection == True:
            $ bangok_four_xkatsu.protection = False
            Ka exhausted "What, and get the taste of that rubber stuff into my special cream?"
            Ka normal "I don't buy the things. I get any customers of the same species as me, we just take a few more precautions."
            Ka smile "Not that that's a problem here."
            jump bangok_four_xkatsu_sexmenu
        "I'm... not so keen on helping now." if bangok_four_xkatsu.protection == False or bangok_four_xkatsu.playercame == True:
            jump bangok_four_xkatsu_wait






label bangok_four_xkatsu_get_underneath:
    show katsu smile with dissolve
    $ renpy.pause (1.4)
    Ka "What do you expect me to say? No?"
    $ renpy.pause (0.3)
    play sound "fx/undress.ogg"
    m "Feeling self-conscious, I stripped out of my clothes and set them well out of the way by the door, trying to keep them clear of our activities."
    Ka normal "Why d'you wear all that, anyway?"
    c "It's not normal among humans to expose yourself to others. It indicates, ah, sexual openness."
    Ka "So is that what you're seeing from everyone 'round these parts?"
    Ka smile "Hope I didn't get you going too much with the day-long show."
    c "No, er, it's different because none of you wear clothes in the first place."
    Ka normal "Hrm."
    $ renpy.pause(0.5)
    m "I got onto my hands and knees next to Katsuharu, reaching out to steady his shaft, estimating his height off the ground and my own."
    show katsu normal at Position(ypos=1.01) with ease
    m "Katsuharu bent his hindlegs slightly, his tip bobbing over one of the ice buckets."
    m "I hesitated, a couple more questions coming to mind."
    label bangok_four_xkatsu_underneath_questions:
    menu:
        "Safe to eat?" if bangok_four_xkatsu.safety == True:
            $ renpy.pause(0.5)
            $ bangok_four_xkatsu.safety = False
            c "We're exposing the key ingredient to my insides at your tip. Is that really safe?"
            Ka exhausted "Haven't had any health complaints yet."
            Ka normal "And I do have more than a few customers for this flavor."
            c "Huh."
            jump bangok_four_xkatsu_underneath_questions
        "Will it taste like my...?" if bangok_four_xkatsu.flavor == 0:
            $ renpy.pause(0.5)
            $ bangok_four_xkatsu.flavor = 1
            c "Is my, uh, flavor going to affect how it tastes?"
            Ka exhausted "I know how to pull out."
            jump bangok_four_xkatsu_underneath_questions
        "What if I want it inside me first?" if bangok_four_xkatsu.flavor == 1:
            $ renpy.pause(0.5)
            $ bangok_four_xkatsu.flavor = 2
            if bangok_four_xkatsu.target == "mouth":
                Ka exhausted "I'm not so sure the ice cream recipe will work if it comes back up from your stomach with any other stuff in there."
                Ka normal "Best not."
            else:
                Ka smile "Do you?"
                menu:
                    "Yes.":
                        $ renpy.pause(0.5)
                        $ bangok_four_xkatsu.flavor = 3
                        Ka normal "Been a while since I've tried it. Alright."
                    "No.":
                        $ renpy.pause(0.5)
                        Ka normal "Then I'll pull out and how you taste won't matter."
            jump bangok_four_xkatsu_underneath_questions
        "Please?" if bangok_four_xkatsu.flavor == 2 and bangok_four_xkatsu.target == "mouth":
            $ renpy.pause(1.5)
            Ka exhausted "I suppose, if that's what you really want."
            $ bangok_four_xkatsu.flavor = 3
            jump bangok_four_xkatsu_underneath_questions
        "Okay. Let's do this.":
            $ renpy.pause(0.5)
    if bangok_four_xkatsu.target == "mouth":
        jump bangok_four_xkatsu_underneath_mouth
    show katsu smile with dissolve
    play sound "fx/slide.ogg"
    m "I shoved the second bucket out of my way, then shuffled sideways over the first until I felt Katsuharu's cockflesh dragging a moist trail across one of my thighs, then bounce to the space between them."
    m "The chill air wafting off the ice bucket sent shivers up my arms and legs."
    if bangok_four_xkatsu.target == "ass":
        m "Reaching back, I guided his cockhead up to my rosebud, my arm rubbing between my back and his hard belly plates."
    elif bangok_four_xkatsu.target == "vag":
        m "Reaching back, I guided his cockhead up to my vaginal lips, my arm rubbing between my back and his hard belly plates."
    else:
        $ renpy.error("There are no third options between a human's legs.")
    m "It barely took a moment to realize his few smears of pre wouldn't be enough lubrication for him to fit inside me with any degree of comfort."
    c "Uh. Lube?"
    Ka normal "Sure I have some around here somewhere. Why? Need it?"
    c "I think it'd be safest, yeah."
    show katsu normal flip with dissolve
    m "Rather than give me a chance to shuffle out from under him, Katsuharu just stepped away, leaving me on hands and knees over the icy bucket."
    hide katsu with easeoutright
    $ renpy.pause(0.8)
    c "Should I help you look, or...?"
    Ka "No, no. Should just be a moment."
    play sound "fx/rummage.ogg"
    $ renpy.pause(1.2)
    show katsu normal at Position(xpos=0.8,xanchor='center') with easeinright
    m "Katsuharu's footsteps returned. I heard a squeeze bottle plunger, then cold gel spilled on one of my cheeks and into my crack."
    m "I shuffled forward sligthly from the sensation, my legs bumping into the freezing metal of the outer bucket."
    c "H-Hey! That's pretty cold!"
    play sound "fx/box.ogg"
    $ renpy.pause(0.5)
    Ka exhausted "Odd. Didn't keep it anywhere near the icebox."
    c "I don't think cold for me and cold for you is the same."
    Ka normal "Doesn't matter if it does its job."
    m "He inspected my backside."
    if bangok_four_playerhasdick == True:
        jump bangok_four_xkatsu_assfuck_lube_ass
    Ka normal "You've got two holes here. Which one this stuff supposed to go into?"
    if bangok_four_xkatsu.target == "ass":
        c "Top."
        label bangok_four_xkatsu_assfuck_lube_ass:
        m "Katsuharu scooped the lube that had spilled down my cheek, rubbing it deeper into my crack. He pushed it into my asshole with a single claw, cold keratin causing a hitch in my breathing."
    elif bangok_four_xkatsu.target == "vag":
        c "Bottom."
        m "Katsuharu scooped the lube that had spilled down my cheek, pushing it down past my ass and over my crotch. He pushed it past my lips with a single claw, cold keratin causing a hitch in my breathing."
    else:
        $ renpy.error("There are no third options between a human's legs.")
    menu:
        "Ooh.":
            $ renpy.pause (0.5)
            show katsu smile with dissolve
        "I-I think that's enough.":
            $ renpy.pause (0.5)
        "Are your claws clean?":
            $ renpy.pause (0.5)
            Ka "Are you going to complain about everything?"
            Ka exhausted "Hold still. Claws get brittle as I get older. Can't dull them like I used to."
    m "He withdrew his claw carefully, then stepped back overtop me."
    show katsu normal at Position(xpos=0.5,ypos=1.01) with ease
    m "I caught his cock, guiding it back toward the hole we both wanted it to fill."

    # TODO: Should lube be behind a menu option?

    Ka smile "Now. Will I push forward, or will you push back?"
    Ka normal "Can't sit here forever."

    if bangok_four_xkatsu.target == "ass":
        jump bangok_four_xkatsu_underneath_ass
    elif bangok_four_xkatsu.target == "vag":
        jump bangok_four_xkatsu_underneath_vag
    else:
        $ renpy.error("There are no third options between a human's legs.")

label bangok_four_xkatsu_underneath_ass:
    m "I pushed, taking advantage of the lube to spear myself on his massive tip."
    m "Taking that as a sign, he pushed forward, squishing his big cockhead through my sphincter and shoving my legs a little forward, into contact again with the ice bucket."
    m "The shock of cold on my legs had me clenching, halting all our movement."
    Ka excited "Ha! Really did need that lube, didn't we? You're not all that big."
    show katsu normal with dissolve
    c "You're a lot bigger than I am!"
    Ka normal "Well. I'll let you handle it until we're deep enough. Not like you need to take all of me."
    m "I shuffled back again, getting a little distance from the bucket and trying to get more pressure on, to get over my clenching."
    $ renpy.pause (0.5)
    show katsu excited at Position(ypos=1.04) with ease
    m "My ass released suddenly, a few inches of Katsuharu's cock sliding in all at once. I instantly felt full. His thick, malleable cock expanded to press against my inner walls in a soft, spongy way I'd never felt before."
    Ka smile "That's enough for me to work with. Feeling okay down there?"
    menu:
        "Y-Yeah.":
            $ renpy.pause(0.5)
        "So full...":
            $ renpy.pause(0.5)
        "This is really unusual.":
            $ renpy.pause(0.5)
            Ka normal "You know much about normal for dragons?"
            if bangok_four_malepartners < 1:
                c "I guess not..."
            elif bangok_four_malepartners < 3:
                c "A little..."
            else:
                c "You'd be surprised."
    $ renpy.pause (1.5)
    Ka normal "Best get moving, then."
    play soundloop "fx/rub2.ogg" fadein 0.5
    show katsu normal:
        ease 0.5 xpos 0.55
        ease 0.15 xpos 0.5
        repeat
    with None
    m "Without further warning, Katsuharu pulled back, cockflesh dragging on my sphincter until he plunged back inside to the same depth."
    m "I slid backward a little with his first pull before catching myself. The feeling of his soft dick compressing to squeeze back and forth through my hole was completely new to me, and maddenning in sensation."
    $ renpy.pause(1.0)
    Ka exhausted "You slid a bit. Need you to move forward if we're going to fill the bucket."
    menu:
        "B-Be careful!":
            $ renpy.pause (0.5)
            Ka exhausted "What else can I do? Not move?"
            $ renpy.pause (0.8)
            m "I opened my mouth to answer, but now that he was reaming my ass, I didn't want him to stop."
            Ka normal "Then move up a bit."
        "I-I'll t-try.":
            $ renpy.pause (0.5)
            show katsu smile with dissolve
        "[[Moan.]":
            $ renpy.pause (0.5)
            show katsu smile with dissolve
    if bangok_four_playerhasdick == True:
        Ka "And get your dick out. You get off, we don't want that in our mix."
    m "On weak knees, I shuffled forward under his fucking until my thighs bumped the freezing bucket. I clenched again, legs warmed by the fucking abruptly shocked again by the cold."
    stop soundloop fadeout 0.5
    show katsu excited at Position(xpos=0.5, ypos=1.04) with ease
    Ka "Ha! That's one way to get me closer."
    show katsu normal with dissolve
    if bangok_four_playerhasdick == True:
        m "It was doing the same for me. Sheepishly, I spread my legs a little further around the bucket so that our mating point was overtop. Then I pulled my achingly hard dick up out of the bucket, laying it over the ice so it pointed outside."
    else:
        m "It was doing the same for me. Sheepishly, I spread my legs a little further around the bucket so that our mating point was overtop. My lower belly brushed over the ice, empty lips aching as an area so nearby was stimulated."
    m "I struggled to calm my body and unclench while so wrapped around the cold bucket. The moment I had, Katsuharu began moving again."
    play soundloop "fx/rub2.ogg" fadein 0.5
    show katsu normal:
        ease 0.5 xpos 0.55
        ease 0.15 xpos 0.5
        repeat
    with None
    if bangok_four_playerhasdick == True:
        m "My cock frotted over the ice from the force of his thrusts, the harsh stimulation abrupt and mind-melting."
        m "Between the soft, warm cockflesh repeatedly filling and emptying my ass and the hard, cold metal and ice rubbing under my shaft, I barely lasted a few more thrusts."
        show katsu excited with dissolve
        play sound "fx/extinguish.ogg"
        show black with fadequick
        m "Sticky ropes spattered across my chest and the ground, forced from me by the unyielding fucking even as my ass clenched around Katsuharu."
        hide black with dissolvemed
    else:
        m "His thrusts forced me forward and downward, brushing the front of my lips against the cold metal, oh so maddenningly close to my clit."
        m "I spread my legs slightly and lowered myself still further, rutting against the inner bucket's lip with each of Katsuharu's entries into my ass."
        m "I barely lasted a few more thrusts."
        show katsu excited with dissolve
        play sound "fx/extinguish.ogg"
        show black with fadequick
        m "My love canal clenched and spasmed around nothing, but my ass grabbed hold of Katsuharu. He ignored the added force, unyielding in his fucking of my ass."
    $ bangok_four_xkatsu.playercame = True
    show katsu exhausted
    hide black with dissolvemed
    m "When I came back down, Katsuharu was panting."
    $ bangok_four_xkatsu.fill = 2
    if bangok_four_xkatsu.flavor == 3:
        $ bangok_four_xkatsu.fill = 3
        Ka "You're sure you want it in you, human?"
        menu:
            "Y-Yes!":
                stop soundloop fadeout 0.5
                show katsu smile at Position(xpos=0.50, ypos=1.05) with ease
                play sound "fx/snarl.ogg"
                m "Katsuharu plowed into my ass, shoving me down against the top of the ice bucket."
                m "Immediately pulses pressed through my sphincter, spurts of seed making their way to his tip to flood my guts."
                show katsu normal at Position(xpos=0.53, ypos=1.03) with ease
                $ renpy.pause (0.8)
                m "He backed out a moment, backing up the beginning of my colon with a thick soup of his seed."
                show katsu excited at Position(xpos=0.49, ypos=1.05) with ease
                if persistent.bangok_knot == True:
                    m "Then he pressed in hard and fast, shoving the cum deep into me fast enough that some spurted back around his cock, lubricating him as he speared me all the way to a thick bulge at his base."
                else:
                    m "Then he pressed in hard and fast, shoving the cum deep into me fast enough that some spurted back around his cock, lubricating him as he speared me all the way to his genital slit."
                m "The fluid shifted deep inside of me, pushed still deeper as more jets came to fill me up. Feeling full, I pushed the ice bucket out from under me, setting my face on the floor to better take my deep penetration."
                show katsu exhausted with dissolve
                if persistent.bangok_inflation == True:
                    m "From this new angle, I could watch as these spurts that packed me solid began to press my belly outward, inflating me with Katsuharu's creamy seed."
                    $ bangok_four_xkatsu.playerstuffed = "ass"
                    m "No matter how full I felt, still more was coming."
                m "Then, gently, the pulses came to an end, leaving me packed full of Katsuharu's cum, as I'd wanted."
                $ renpy.pause (0.8)
                show katsu exhausted at Position(xpos=0.53) with ease
                show katsu exhausted at Position(xpos=0.56, ypos=1.0) with ease
                show katsu exhausted at Position(xpos=0.65) with ease
                m "Katsuharu took a few shaky steps off of me, dick pulling free with a small river of cum from my ass."
                Ka "No time to rest with it! We need to get it into the buckets to chill!"
                play sound "fx/slide.ogg"
                $ renpy.pause(0.5)
                m "A freezing bucket was slid between my legs, then Katsuharu grabbed my shoulder and pulled me back until I was sitting on it."
                c "A-Ah! D-Damn!"
                play sound "fx/pour.ogg"
                $ renpy.pause(3.0)
                stop sound fadeout 0.5
                m "With how full I was, gravity was the only prompting our creamy end-goal needed to escape me into the bucket. Katsuharu set me back down when he decided the bucket was full enough, then dragged it away only to replace it with the second."
                play sound "fx/pour.ogg"
                $ renpy.pause(2.5)
                stop sound fadeout 0.5
                m "I didn't have quite as much to drain this time, before the stores so easily reached within me came to an end. I was sure much of my gut was still painted white, even after my draining."
                if persistent.bangok_inflation == True:
                    m "That didn't even account for what had been stuffed beyond my colon. My belly still bulged slightly, packed with cum."
                $ bangok_four_xkatsu.fill = 2 # Lost some. But did you have fun?
                jump bangok_four_xkatsu_filldone
            "Uh-":
                $ bangok_four_xkatsu.flavor = 2
    stop soundloop fadeout 0.5
    show katsu normal at Position(xpos=0.55, ypos=1.0) with ease
    m "Moving one of his forelegs under one of my arms, Katsuharu yanked his cock free of my ass, then pushed me forward to shove his cock where my crotch had been."
    play sound "fx/snarl.ogg"
    if bangok_four_xkatsu.fill == 2:
        m "I got myself turned around quickly, ready to help his aim and not waste our combined efforts. Luckily, he was well on-target."
        show katsu exhausted with dissolve
        jump bangok_four_xkatsu_fill2
    else:
        m "I got myself turned around quickly, ready to help his aim and not waste our combined efforts if he wasn't quite spurting into the bucket."
        if persistent.bangok_inflation == True:
            m "I found said bucket almost already full!"
        else:
            m "He was spot on, the inner bucket filling alarmingly quickly."
        Ka exhausted "Ha! G-Gotta switch, can't overfill 'em!"
        m "Ducking back under Katsuharu, I pulled the first bucket aside and the second bucket into the line of fire."
        jump bangok_four_xkatsu_fill3



label bangok_four_xkatsu_underneath_vag:
    m "I pushed, parting my lubed-up lips around his massive tip."
    m "Taking that as a sign, he pushed forward, soft cockfleash spreading my canal like a hand filling a glove."
    show katsu excited:
        ease 1.5 ypos 1.04
    with None
    $ renpy.pause(1.3)
    m "I gasped as I ran out of room, every inch of my inner walls pressed against by his thick, warm, malleable shaft. Leaning forward to try to get a little more room, my belly pressed against the icy rim of the layered buckets."
    show katsu smile with dissolve
    m "My canal clenched and squeezed, massaging his length for his heady warmth, to fight off the cold shock."
    Ka normal "That as deep as you can go?"
    if persistent.bangok_cervpen:
        c "(He's right up against my cervix. {i}Can{/i} I take him deeper?)"
        menu:
            c "(He's right up against my cervix. {i}Can{/i} I take him deeper?){fast}"
            "Fuck me deeper.":
                $ renpy.pause(0.5)
                $ bangok_four_xkatsu.target = "womb"
                Ka smile "If you insist."
                show katsu smile at Position(ypos=1.03) with ease
                m "Katsuharu pulled back a moment, leaving a tiny well of emptiness inside me between his tip and my inner gate."
                show katsu excited:
                    ease 0.3 xpos 0.47 ypos 1.05
                with None
                m "Then he filled that space and then some, squeezing through into my most sacred temple."
            "I-I think I can take it...":
                $ renpy.pause(0.5)
                $ bangok_four_xkatsu.target = "womb"
                Ka normal "You just let me know if it's too much."
                show katsu normal:
                    ease 1.3 xpos 0.495 ypos 1.05
                with None
                m "He applied more pressure oh-so-gradually, leaning weight on his shaft with a slow ease that spoke to countless years of experience."
                m "The pressure on my innermost gate increased, the ache increasing in step as his tip burrowed milimeters deeper, squeezed by a hole out of reach of humans."
                menu:
                    "S-Stop!":
                        $ renpy.pause(0.5)
                        $ bangok_four_xkatsu.target = "vag"
                        show katsu normal:
                            ease 0.5 xpos 0.5 ypos 1.03
                        with None
                        m "Katsuharu and I both let out panting breaths as he pulled back."
                        c "Y-You're too big. There's no way..."
                        Ka exhausted "I could tell. Are you hurt?"
                        c "I don't think so. As long as we don't try that again."
                        Ka normal "Of course."
                    "So close...":
                        $ renpy.pause(0.8)
                        show katsu excited:
                            ease 0.3 xpos 0.47 ypos 1.05
                        with None
                        m "His head popped in, squeezing through into my most sacred temple."
            "Can't fit any more.":
                $ renpy.pause(0.5)
                $ bangok_four_xkatsu.target = "vag"
                Ka "Of course."
            "I-It's already so much!":
                $ renpy.pause(0.5)
                $ bangok_four_xkatsu.target = "vag"
                show katsu exhausted with dissolve
                show katsu exhausted at Position(ypos=1.03)
                m "Katsuharu carefully slid back a little, taking the pressure off the wall at the end of my canal."
                Ka "There?"
                c "B-Better."
    else:
        menu:
            "Ngh. Obviously!":
                $ renpy.pause(0.5)
                $ bangok_four_xkatsu.target = "vag"
                Ka "Of course."
            "It already hurts...":
                $ renpy.pause(0.5)
                $ bangok_four_xkatsu.target = "vag"
                show katsu exhausted with dissolve
                show katsu exhausted at Position(ypos=1.03)
                m "Katsuharu carefully slid back a little, taking the pressure off the wall at the end of my canal."
                Ka "There?"
                c "B-Better."
    if bangok_four_xkatsu.target == "womb":
        m "I collapsed atop the bucket, knees giving out as my lower body shuddered with sparks of pain and pleasure ricocheting everywhere."
        show katsu smile:
            ease 0.6 ypos 1.055
        with None
        m "He slid deeper gradually, easing more spongy cockflesh inside. His length pressed up against my belly, sandwiching his heat right up against the freezing ice through the walls of my most hidden place."
        show katsu smile:
            ease 0.6 ypos 1.06
        with None
        m "Then I felt his thighs against mine."
        c "H-Holy fuck."
        Ka exhausted "Is that a good expression or a bad one."
        c "{i}Good.{/i}"
        $ renpy.pause(0.3)
        show katsu smile with dissolve
        $ renpy.pause(0.3)
        show katsu smile:
            ease 1.0 xpos 0.495 ypos 1.05
            ease 1.0 xpos 0.47 ypos 1.06
            repeat
        m "Katsuharu began moving gradually, taking things slowly as his cockflesh, slickened by my arousal and a healthy dose of lube, squeezed back through my inner gate and spread my canal with a massive pillar of meat and bone."
        m "Pulling back, his tugging at my lips found my clit. That, combined with his presence so deep inside, sent me catapulting over my peak."
        show black with fadequick
        $ bangok_four_xkatsu.playercame = True
        $ bangok_four_xkatsu.fill = 3
        $ renpy.pause(1.0)
        m "I couldn't move, couldn't think as he took my clenching, spasming walls as a sign of encouragement and picked up his pace."
        play soundloop "fx/rub2.ogg" fadein 0.5
        show katsu normal:
            ease 0.5 xpos 0.55
            ease 0.15 xpos 0.5
            repeat
        with None
        $ renpy.pause(0.8)
        hide black with dissolveslow
    else:
        $ renpy.pause(0.5)
        show katsu normal with dissolve
        $ renpy.pause(0.8)
        play soundloop "fx/rub2.ogg" fadein 0.5
        show katsu normal:
            ease 0.5 xpos 0.55
            ease 0.15 xpos 0.5
            repeat
        with None
        m "Katsuharu began to move, dragging his spreading cockflesh back through my canal, rubbing every nook and cranny like a million soft caresses, as rich and smooth as the ice cream I'd been promised, and the cream he'd soon deliver."
        m "His meat tugging at my lips found my clit, rubbing against it as he pushed harder on the inward thrusts, stopping short of my innermost gate so as not to hurt me, but still filling my innermost space."
        m "The stimulation of my clit and spreading of my love passage sent me catapulting over my peak."
        show black with fadequick
        $ bangok_four_xkatsu.playercame = True
        $ bangok_four_xkatsu.fill = 2
        $ renpy.pause(1.8)
        show katsu exhausted
        hide black with dissolveslow
        m "Coming back down took exquisite ages, as throughout he kept filling my vagina and dragging back out, drops of my arousal running down my legs in a stream from our mating point."
    Ka exhausted "Not long now."
    if bangok_four_xkatsu.flavor == 3:
        $ bangok_four_xkatsu.fill = 3
        Ka "You're sure you want it in you, human?"
        menu:
            "Y-Yes!":
                stop soundloop fadeout 0.5
                show katsu smile at Position(xpos=0.51, ypos=1.06) with ease
                play sound "fx/snarl.ogg"
                if bangok_four_xkatsu.target == "womb":
                    if persistent.bangok_knot == True:
                        m "Katsuharu speared me almost the way, tail slapping down between my legs as he pressed his tip and my sacred place against the bucket and stopped."
                    else:
                        m "Katsuharu speared me all the way, tail slapping down between my legs as he pressed his tip and my sacred place against the bucket and stopped."
                    m "Pulses pressed through my innermost gate, expanding his girth at my tightest point before spraying from his tip within me."
                    play sound "fx/slide.ogg"
                    m "I had to shove the ice bucket out of the way, as the contrast between warm fluid and frozen spikes became painful. Face on the floor, I moaned as he defiled my innermost place, sowing his seed within me."
                else:
                    show katsu smile at Position(xpos=0.5, ypos=1.04) with ease
                    m "Katsuharu jerked back as he began to cum, keeping himself from pressing deeper than I could take. Even still, his first spurts spattered against my innermost gate like thrusts, leaving me crying out from the overstimulation."
                    m "Rapidly, what space there was within my canal packed with his seed. With his wide girth blocking my entrance, pouring more inside, the cum had nowhere to go but through my innermost gate, pouring into my womb."
                    m "Even still, I felt rivulets running down my legs, leaking around his rod."
                    show katsu smile at Position(xpos=0.50, ypos=1.05) with ease
                    show katsu smile at Position(xpos=0.51, ypos=1.05) with ease
                    m "He pressed forward carefully, like a plunger in a syringe, injecting his seed into my deepest temple and leaving me weak enough to collapse onto the bucket beneath me."
                    play sound "fx/slide.ogg"
                    m "I shoved the bucket aside, putting my face to the floor as I moaned around his deep cream filling."

                if persistent.bangok_inflation == True:
                    m "My womb was packed solid with nothing but him. As yet more pulses poured inside, my belly was forced to acommodate, expanding past two months, then the first trimester."
                    $ bangok_four_xkatsu.playerstuffed = "vag"
                    m "By the time his fluid injection began to slow, my navel reached out to kiss the cold floor where the bucket had been."

                show katsu exhausted with dissolvemed

                if bangok_four_xkatsu.target == "womb":
                    m "As Katsuharu's pulses through my cervix slowed, he pulled back, filling the space his cock abandoned with yet more seed."
                    m "When he pulled free of my flooded womb, I could feel his liquid gift draining through the spread terminus of my love canal."
                else:
                    m "Katsuharu's pulses finally slowed, leaving me stuffed full of his liquid gift."

                $ renpy.pause (0.8)
                m "He panted heavily."
                show katsu exhausted at Position(xpos=0.53) with ease
                show katsu exhausted at Position(xpos=0.56, ypos=1.0) with ease
                show katsu exhausted at Position(xpos=0.65) with ease
                m "He took a few shaky steps off of me, dick pulling free with a small river of cum from my vagina."
                Ka "No time to rest with it! We need to get it into the buckets to chill!"
                play sound "fx/slide.ogg"
                $ renpy.pause(0.5)
                m "A freezing bucket was slid between my legs, then Katsuharu grabbed my shoulder and pulled me back until I was sitting on it."
                c "A-Ah! D-Damn!"
                play sound "fx/pour.ogg"
                $ renpy.pause(3.0)
                stop sound fadeout 0.5
                m "With how full I was, gravity was the only prompting our creamy end-goal needed to escape me into the bucket. Katsuharu set me back down when he decided the bucket was full enough, then dragged it away only to replace it with the second."
                play sound "fx/pour.ogg"
                $ renpy.pause(2.5)
                stop sound fadeout 0.5
                m "I didn't have quite as much to drain this time, before the stores so easily reached within me came to an end. I was sure much of my love passage was still painted white, even after my draining."
                if persistent.bangok_inflation == True:
                    m "That didn't even account for all of what had been stuffed into my womb. My belly still bulged slightly, a couple months pregnant with Katsuharu's gift."
                $ bangok_four_xkatsu.fill = 2 # Lost some. But did you have fun?
                jump bangok_four_xkatsu_filldone
            "Uh-":
                $ bangok_four_xkatsu.flavor = 2
    stop soundloop fadeout 0.5
    show katsu normal at Position(xpos=0.55, ypos=1.0) with ease
    m "Moving one of his forelegs under one of my arms, Katsuharu yanked his cock free of my passage, then pushed me forward to shove his cock where my crotch had previously been."
    play sound "fx/snarl.ogg"
    if bangok_four_xkatsu.fill == 2:
        if bangok_four_xkatsu.target == "womb":
            m "I struggled to turn around quickly, ready to help his aim and not waste our combined efforts. Luckily, he was well on-target."
        else:
            m "I got myself turned around quickly, ready to help his aim and not waste our combined efforts. Luckily, he was well on-target."
        show katsu exhausted with dissolve
        jump bangok_four_xkatsu_fill2
    else:
        if bangok_four_xkatsu.target == "womb":
            m "I struggled to turn around quickly, ready to help his aim and not waste our combined efforts if he wasn't quite spurting into the bucket."
        else:
            m "I got myself turned around quickly, ready to help his aim and not waste our combined efforts if he wasn't quite spurting into the bucket."
        if persistent.bangok_inflation == True:
            m "I found said bucket almost already full!"
        else:
            m "He was spot on, the inner bucket filling alarmingly quickly."
        Ka exhausted "Ha! G-Gotta switch, can't overfill 'em!"
        m "Ducking back under Katsuharu, I pulled the first bucket aside and the second bucket into the line of fire."
        jump bangok_four_xkatsu_fill3



label bangok_four_xkatsu_underneath_mouth:
    show katsu smile with dissolve
    play sound "fx/slide.ogg"
    m "I shoved the second bucket out of my way, then shuffled sideways over the first until Katsuharu's cockhead was just next to my cheek, a glistening drop of pre glinting in the corner of my vision as I peered up his shaft, toward the slit from which it emerged."
    show black with dissolvemed
    m "Cautiously, I took his tip into my mouth, licking up the pre. {w=0.5}It was delicious! Saccharine sweet, I was sure in a more viscous form, it would be an incredibly lucrative flavor of taffy."
    show katsu exhausted with dissolve
    m "Seeking out more of it, my tongue explored just inside his urethra, eliciting a small gasp from Katsuharu, a twitch from his shaft, and another dollop for me."
    m "I shuffled closer, until my knees were up against the first bucket. Bracing against his hindlegs with one hand and holding his shaft from beneath with the other, I pushed more of his head into my mouth, his spongy cockflesh compressing so I could do so without hurting my jaw."
    m "I began to pump, trying to draw more pre down his tube. Encouraging the production of more, my tongue explored around what it could reach, digging and licking behind his head."
    $ renpy.pause(0.5)
    m "Katsuharu kept himself steady, content to let me do the work in this position, and keeping himself from moving in a way that might hurt me."
    $ renpy.pause(0.5)
    m "Even despite my efforts, though, his drops of pre were few and far between. It certainly didn't sound like he was getting any closer."
    c "(Maybe there's something more I can do?)"
    menu:
        c "(Maybe there's something more I can do?){fast}"
        "Deepthroat.":
            $ bangok_four_xkatsu.target = "throat"
            $ renpy.pause(0.5)
            c "(He's so spongy. Can I fit his cock down my throat?)"
            m "Remembering his comment about a baculum, I took a moment to arrange myself, leaning my head back to get my mouth and throat in line while getting back on my knees to have control over his depth."
            $ renpy.pause(0.8)
            m "Then, with a deep breath, I took Katsuharu to the back of my mouth."
            show katsu excited with dissolve
            $ renpy.pause(0.3)
            hide black with fadequick
            show katsu exhausted with dissolve
            m "It was impossible not to gag the first time. His cock's slightly spongy nature meant it pressed against every part of my mouth and throat, leaving no way to control where he went to keep him from more sensitive parts of my gag reflex."
            m "I spent a moment recovering with just a hand on his shaft, drawing a concerned grumble from Katsuharu."
            Ka "You're not hurting yourself with it back there, are you human?"
            c "N-No. I can do this."
            Ka normal "If you say so."
            $ renpy.pause(0.8)
            show black with dissolvemed
            m "Taking things more slowly the second time, I eased his head into my mouth after his breath, sinking lower slowly, focusing on each place my gag reflex responded and telling myself that, no, I really wasn't going to choke and I was doing this on purpose."
            $ renpy.pause(0.8)
            hide black with fadequick
            m "I got him into my throat this time, just barely. When I pulled back, another drop of heady pre waited on his tip for my tongue."
            show katsu smile with dissolve
            $ renpy.pause(0.5)
            show black with dissolve
            m "I dove back down with less recovery time, eager both to prove myself and to reach the creamy treat I knew waited if I could stimulate him enough."
            m "Easing him in, once I felt his head in my throat I kept going, consuming as much cockflesh as I could this go."
            Ka smile "Ha. Halfway."
            m "Katsuharu's words vibrated through his shaft, passing his warning along to my gag reflex."
            hide black with fadequick
            m "I pulled back until his head popped free of my mouth, my breath going with it until I could suck down another lungful to cough with."
            $ renpy.pause(0.8)
            Ka exhausted "Are you sure you're not hurting yourself?"
            show black with dissolve
            m "I answered his question by taking his cock into my mouth again. Rather than brace against his hindlegs, I put both hands on his cock, hanging between it and my knees on the floor as I pumped what my throat couldn't take."
            Ka excited "Ha! Keep that up!"
            m "I hung on, telling my gag reflex I was in control and had nothing to worry about. It worked, mostly, as I kept the depth I'd gotten, even if it was less than last time."
            m "Then I paused my pumping and sank deeper, seeking out more of his thick shaft, testing my limits."
            show katsu smile
            hide black
            with dissolve
            m "When I pulled back for air, the farthest point on his shaft dampened by my saliva was still only just past halfway."
            $ renpy.pause(0.8)
            Ka "Going to take a few more of those to get what we're after."
            m "I pumped his shaft with a hand, completely catching my breath before I took him again."
            $ renpy.pause(1.2)
            Ka normal "If you need help, you could ask."
            c "Huh?"
            Ka "If you need me to move forward. I know there's only so far you can lever yourself on your knees like that. Runners have the same problem."
            c "Oh. Alright."
            $ renpy.pause(1.2)
            m "After a few more seconds of recovery, I arranged myself again, staring down his shaft."
            show katsu smile with dissolve
            show black with dissolvemed
            m "Then I took him into my mouth again, pressing directly for depth. I saw his length and I wanted it {i}all{/i}."
            m "When I couldn't press myself forward any further, I tugged on one of Katsuharu's hindlegs."
            Ka excited "Alright!"
            c "Urk!"
            m "In one step forward, he had me sitting back as if I hadn't begun taking his shaft, all of my control gone. My head was bent back, face pressed directly into his genital slit as his rod straightened and bulged my neck."
            m "My chest burned. I realized a moment later it wasn't from lack of air, but instead heartburn as his tip popped into my stomach, completely spearing my throat with malleable cockflesh."
            m "He lifted his hips, freeing my face from his genital slit, only to drop back down, fucking my mouth."
            Ka excited "Ah!{w=0.5} Not going to last long like this!"
            m "With nothing else I could do, my hands went to my neck, as if that would clear the girthy obstruction lifting to fuck my throat again. I could feel bumps and wrinkles in his cockflesh sliding by through my own skin!"
            m "I squeezed, feeling faint as he slid to mate with my mouth again, trying to get a message through to him."
            Ka smile "That's the spot!"
            m "I gestured a bit more widely, as he clearly misinterpreted my throat squeeze."
            Ka normal "Hm?"
            Ka exhausted "Oh! Air!"
            hide black with dissolve
            m "He stepped back. I collapsed against the ice bucket, lungs convulsing as they tried to get oxygen back into my system."
            m "While I recovered I stroked his shaft, not wanting to lose the progress we'd made pushing him toward his peak."
            $ renpy.pause(0.8)
            m "He panted as my saliva-slicked fingers ran over his fully-dampened length."
            $ renpy.pause(0.8)
        "Spread affection.":
            $ renpy.pause(0.5)
            m "I popped his head out of my mouth, then leaned in. Moving my knees a little to one side of the bucket, I nestled a little further into Katsuharu's crotch, angling to rub his cock with more of my arms, as well as planting sucking kisses slowly up toward his base."
            Ka excited "Ah! That-- Ha! That's very different!"
            $ renpy.pause(0.8)
            m "I paused with my mouth close to his genital slit, wondering if he could feel my breath."
            c "Keep going?"
            Ka smile "If you'd please."
            m "I dragged my hands back down my shaft, but kept my head where it was. Curiosity getting the better of me, I leaned in to taste a part of his shaft I hadn't reached yet, digging my tongue just a little bit in and around his genital slit."
            show katsu excited with dissolve
            show katsu excited at Position(xpos=0.51, xanchor='center') with ease
            m "His cock almost twitched out of my grip, as he shuffled back half a step."
            show katsu exhausted
            hide black
            with dissolvemed
            Ka exhausted "Hrm. That- That spot is a little too sensitive. Stay a little lower, alright?"
            show katsu exhausted at center with ease
            show katsu normal with dissolve
            m "As I backed off a little, he moved back into his position over the bucket. I took his shaft in hand and began to work it again, slowly planting kisses down the other side."
            show katsu smile with dissolve
            show black with dissolvemed
            $ renpy.pause(1.4)
            m "Back at his tip, I enveloped and sucked, enjoying the large beads of pre my actions had collected there. Then I popped th ehead back out of my mouth for a momentary breather, and to see if he had any more tips for treating his cock well."
            hide black with dissolvemed
    
    if bangok_four_xkatsu.flavor == 3:
        Ka "If you still want it inside you... Not sure how much more I've got before it comes out."
        menu:
            "In.":
                $ renpy.pause (0.5)
                $ bangok_four_xkatsu.playerstuffed = "mouth"
                show black with dissolve
                play sound "fx/snarl.ogg"
                m "No sooner was I stroking him into my mouth again than he twitched in my hands, his first pulse prying my jaw slightly wider before exploding against the back of my throat."
                if bangok_four_xkatsu.target == "throat":
                    if persistent.bangok_knot == True:
                        m "I leaned forward, using Katsuharu's head to push his first spurts down before I could change my mind. {w=0.5}He obliged me by stepping forward, ramming his cock down my throat, packing my neck solid with twitching meat but for a bulge at his base that wouldn't fit past my jaw."
                    else:
                        m "I leaned forward, using Katsuharu's head to push his first spurts down before I could change my mind. {w=0.5}He obliged me by stepping forward, ramming his cock down my throat, packing my neck solid with his twitching meat."
                    m "After the meat came dessert, rope after rope of warm seed injected directly into my stomach, flooding me with nutritious, creamy protein."
                    if persistent.bangok_inflation == True:
                        m "It was seconds before my belly was filled, stuffed with as much as I'd ever eaten in one go. Yet the flood continued. My guts gurgled audibly as they made room for what Katsuharu was feeding me, my stomach insufficient to contain the gift. Then I began to expand, my stuffed intestines needing somewhere to go themselves."
                    m "My hands went to my belly, knowing even when I gave some of it back for the ice cream recipe, I still wouldn't need to eat for some time."
                    m "As my neck spasmed back against his pulsing cock, the feeling of warm, stuffed contentment faded. Much as I wanted to sit back and rest, filled with his shaft, I needed to breathe. He didn't seem to be slowing down!"
                    m "I pushed against his hips, trying to get him to back off. He did, stepping back and stuffing my throat with his seed. The moment he popped free with a spurt in my face, I bent over the bucket. His cock and my mouth competed to fill it faster."
                else:
                    m "The sweet richness almost made me lose my seal as my tongue darted to seek it all out. Some small drops leaked from my lips, so I nestled his tip against my throat to force him that little bit deeper and get the drops back in."
                    m "His next spurts went directly into my throat as I basked in the rich aftertaste of his first few. Rope after rope of seed backed up in my throat, each forcing the previous down into my stomach as I stubbornly pumped his cock for more."
                    if persistent.bangok_inflation == True:
                        m "It was seconds before my belly was filled, stuffed with as much as I'd ever eaten in one go. Yet the flood continued. My guts gurgled audibly as they made room for what Katsuharu was feeding me, my stomach insufficient to contain the gift. Then I began to expand, my stuffed intestines needing somewhere to go themselves."
                    m "One hand went to my belly, knowing even when I gave some of it back for the ice cream recipe, I still wouldn't need to eat for some time with the liquid gift Katsuharu had stuffed into me."
                    m "Yet, it didn't seem to end. The feeling of warm, stuffed contentment faded with my ability to swallow, my stomach too packed to take any more. But more was coming!"
                    m "Remembering the bucket, I yanked him free with a spray of cum in my face. Then I bent over the bucket, his cock and my mouth competing to fill it faster."
                $ bangok_four_xkatsu.playerstuffed = True
                $ renpy.pause(0.8)
                show katsu exhausted with dissolve
                play sound "fx/slide.ogg"
                hide black with dissolve
                m "I won, gasping for air as I dragged the second bucket over. His spurts were already slowing, though, and left a sad puddle in the bottom of the second bucket."
                $ renpy.pause(1.0)
                $ bangok_four_xkatsu.fill = 1 # Oops. You swallowed a lot.
                Ka smile "Good meal?"
                m "I patted my belly."
                c "Oh yeah. I'm... I'm not sure I'll even be able to eat the ice cream after that."
                Ka normal "You will."
                jump bangok_four_xkatsu_filldone
            "Out.":
                $ renpy.pause (0.5)
                $ bangok_four_xkatsu.flavor = 2
                $ bangok_four_xkatsu.fill = 3
                c "Changed my mind."
                Ka "Probably best."
    Ka "I... ah. Think I'm not far from--"
    play sound "fx/snarl.ogg"
    m "He thrust through my hands and I quickly aimed him into the bucket."
    if bangok_four_xkatsu.fill == 3:
        jump bangok_four_xkatsu_fill3
    else:
        jump bangok_four_xkatsu_fill2










label bangok_four_xkatsu_ready:
    Ka "Alright human. It's ready."
    show katsu at right
    hide black
    with dissolveslow

    if bangok_four_xkatsu.fill == 0:
        Ka exhausted "It's not much. Would've been more with some more help."
        m "The buckets from before sat on the floor, along with a good amount of spilled crushed ice."
        m "The bottom half of one bucket was packed with what looked like a half pint of off-yellow, cream-substitute ice cream."
        menu:
            "You made it in the bucket you came in?":
                Ka "It's my special seed ice cream. What did you expect? Some kind of rigorous machine purification? Pah!"
                c "And why's it that nasty color?"
                Ka "Mix-in ingredients to get the texture right. You'd know something about that if you'd stayed to help."
                c "Ooo... kay."
            "Why's it that color?":
                Ka "Mix-in ingredients to get the texture right. You'd know something about that if you'd stayed to help."
            "Looks good. Thanks.":
                show katsu smile with dissolve
    elif bangok_four_xkatsu.fill == 1:
        m "The buckets from before sat on the floor. The inner buckets were a little less than half full of a  whitish off-yellow, cream-substitute ice cream."
        Ka normal "Well, not a bad batch."
        Ka exhausted "Kinda expected to put out a bit more after that dry spell."
        menu:
            "It looks good, though. Thanks.":
                pass
            "Sorry for swallowing so much." if bangok_four_xkatsu.target in ["mouth","throat"] and bangok_four_xkatsu.flavor == 3:
                pass
            "Can't wait to try it!":
                pass
        show katsu smile with dissolve
    elif bangok_four_xkatsu.fill == 2:
        m "The buckets from before sat on the floor. They were a little short of full of a rich, whitish, off-yellow, cream-substitute ice cream."
        Ka "We made so much! It's been a while since I've been able to offer it to those in the know."
        Ka smile "It's going to sell out quickly."
        c "Can't wait to try it!"
    elif bangok_four_xkatsu.fill == 3:
        m "The buckets from before sat on the floor. Both were packed solid with a rich, whitish, off-yellow, cream-substitute ice cream."
        Ka "We made so much! It's been a while since I've been able to offer it to those in the know."
        Ka smile "It's going to sell out quickly."
        Ka excited "And we even have some of the key ingredient left over for a topping."
        menu:
            "Looks good. Thanks.":
                pass
            "I think I got enough topping earlier." if bangok_four_xkatsu.playerstuffed:
                pass
            "I can't wait to try it!":
                pass
    else:
        $ renpy.error("Invalid fill value: "+str(bangok_four_xkatsu.fill))
    $ renpy.pause (0.5)
    if persistent.bangok_watersports == True and (bangok_four_xkatsu.fill > 1 or bangok_four_xkatsu.target in ["mouth","throat"]):
        show katsu exhausted with dissolve
        $ renpy.pause (0.8)
        c "Something wrong?"
        $ renpy.pause (0.3)
        Ka normal "No, no. Just that water is going straight through me."
        Ka smile "I'll be right back to serve up."
        menu:
            "I could use a palette cleanser...":
                $ renpy.pause (0.5)
                Ka "Could you, now?"
                m "Katsuharu's cock emerged a little further from his slit."
                jump bangok_four_xkatsu_ws_mouth
                # if bangok_four_xkatsu.target in ["ass","vag","womb"]:
                #     Ka "Are you sure that's where you want it?"
                #     menu:
                #         "Shower.":
                #             jump bangok_four_xkatsu_ws_shower
                #         "Mouth.":
                #             jump bangok_four_xkatsu_ws_mouth
                #         "Ass." if bangok_four_xkatsu.target == "ass":
                #             jump bangok_four_xkatsu_ws_underneath
                #         "Vagina." if bangok_four_xkatsu.target == "vag":
                #             jump bangok_four_xkatsu_ws_underneath
            "Oh, yeah, go take care of that.":
                $ renpy.pause (0.5)
                show katsu exhausted flip with dissolve
                $ renpy.pause (0.3)
                hide katsu with easeoutright
                $ renpy.pause (1.0)
                m "He headed off to another part of the house, leaving me alone in the kitchen."
                $ renpy.pause (2.0)
                c "(Been waiting all day for this ice cream. What's a few more minutes?)"
                $ renpy.pause (3.0)
                c "(Nope. Not going to do it.)"
                $ renpy.pause (4.0)
                c "(Really! I can wait. I'm definitely going to get it this time.)"
                $ renpy.pause (3.0)
                c "(Okay, maybe just a taste to--){w=0.8}{nw}"
                show katsu smile at right with easeinright
                Ka "Apologies for that."
                $ renpy.pause(0.3)

    Ka "All that's left is to serve up. Cup or cone?"
    $ renpy.pause(0.8)
    jump bangok_four_xkatsu_ending

label bangok_four_xkatsu_ws_mouth:
    # c "Doesn't cleanse my palette if it goes somewhere else."
    # Ka smile "Suppose it doesn't."
    m "Stepping away from the buckets to protect our creamy treat, I sank to my knees."
    show katsu smile at center with ease
    if bangok_four_xkatsu.target == "throat":
        Ka normal "You took me down your throat earlier. You want to go all that way again? Or just stick it in your mouth?"
        menu:
            "Deepthroat.":
                $ renpy.pause(0.5)
                c "All the way."
                show black with dissolve
                m "I ducked underneath him, coming again face-to-face with his shaft."
                Ka smile "Full service. Sounds good to me."
                m "The feel of his cockhead in my mouth was familiar now. What was less so was the fresh tang that came with it as he began to dribble a fluid less viscous than his cum."
                m "I nestled his tip down into my throat, struggling only slightly. Then Katsuharu stepped forward, ramming all the way home in my face and releasing the floodgates."
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                m "I did my best to be a full-service urinal, lapping at his genital slit with what little I could move of my tongue, but I was too overwhelmed by the sensations inside me."
                if bangok_four_xkatsu.playerstuffed == False:
                    m "My stomach filled rapidly with warmth from Katsuharu's bladder as he pissed like a hose down my throat."
                    if persistent.bangok_inflation == True:
                        m "It was beyond anything I could drink without the assistance of his shaft, my stomach filled so completely my intestines began to flood, belly expanding under the load."
                if bangok_four_xkatsu.playerstuffed == True:
                    m "My guts churned, Katsuharu's piss pushing the cum from my stomach and deeper into my intestines."
                    if persistent.bangok_inflation == True:
                        m "It was beyond anything I could drink without the assistance of his shaft. I expanded, the fluid bulge in my belly growing to a nearly painful degree, enough that I was sure I couldn't walk."


                stop soundloop fadeout 1.0
                $ renpy.pause(0.8)
                m "Katsuharu's shaft shrank slightly as he finally finished packing me with piss."
                $ renpy.pause(0.3)
                m "Then he pulled back, the space his tip had occupied in my stomach immediately replaced with urine by fluid pressure."
                hide black with dissolvemed
                m "I could barely keep it all down as he withdrew completely, leaving me gasping on my knees, flushed with the warmth of my urinal use."
                $ bangok_four_xkatsu.playerstuffed = True
            "Mouthwash.":
                $ renpy.pause(0.5)
                c "I'm in it for the taste. So, uh..."
                Ka normal "Well, it's acquired, so I hope you've got practice."
                jump bangok_four_xkatsu_ws_mouthwash
    else:
        label bangok_four_xkatsu_ws_mouthwash:
        m "I looked around, not sure where would be best to really make a mess in his kitchen. If his volume of piss was anything like that of his cum, I wasn't sure I'd be able to drink it all."
        Ka normal "Just grab a mixing bowl if you're worried about overflow. I wash 'em."
        show black with dissolve
        m "Finding a large bowl on a nearby shelf, I ducked underneath him, coming again face-to-face with his shaft, then taking him into my mouth."
        $ renpy.pause(0.5)
        Ka smile "You ready down there?"
        c "Mmm!"
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        m "My first warning was a bit of sweetness mixed with tang, some of his cum mixed in with the initial trickle of urine. Then the full stream hit the back of my throat, {i}definitely{/i} beyond what I could swallow."
        if bangok_four_playerhasdick == True:
            m "Piss leaked past my lips, dribbling down my chin and chest as I tried to keep up and not make a mess. I pulled the mixing bowl closer, under my hardening shaft and balls as the stream of golden liquid flowed down my belly, parting around my cock before dribbling down into a pool."
        else:
            m "Piss leaked past my lips, dribbling down my chin and chest as I tried to keep up and not make a mess. I pulled the mixing bowl closer, under my vaginal lips as the stream of golden liquid flowed down my belly and over my cunt, dribbling down into a pool with my own juices."
        m "I sank his cockhead a little deeper in my mouth, trying to get a better seal, trying to swallow the fast stream without choking and coughing up more."
        if bangok_four_xkatsu.playerstuffed == True:
            if bangok_four_xkatsu.target not in ["vag","womb"]:
                m "The new stream of liquid gift mixed with the cum Katsuharu had already left inside me. Almost unable to swallow, even more piss ran down my front, over my belly stuffed full of his donations."
            else:
                m "The new stream of liquid gift pooled above the cum Katsuharu had already left inside me. I felt stuffed, letting even more piss run down my front over my belly pregnant with his previous donation."
        elif persistent.bangok_inflation:
            m "His fluid load was immense, enough that even though I was sure half or more leaked from my lips and ran down my front, my stomach filled so completely my intestines began to flood, belly expanding under the load."
        else:
            m "His fluid load was immense, enough that even though I was sure half or more leaked from my lips and ran down my front, my thirst for the day was completely sated, and then some."
        stop soundloop fadeout 1.0
        $ renpy.pause(0.8)
        m "Katsuharu's shaft shrank slightly as he finally finished packing me with piss. A cascade of excess leaked between my lips as he pulled out, streaming down my soaked chest and body."
        m "He gave one last spurt onto my chest as he stepped back, then dribbled a few glimmering droplets down into the bowl between my legs."
        hide black with dissolveslow
        show katsu smile with dissolve
        $ renpy.pause (0.5)

    Ka "All that's left is to serve up. Cup or cone?"
    $ renpy.pause(0.8)
    c "H-How about a half hour rest first? That... I think my throat needs a break."
    if bangok_four_xkatsu.playerstuffed == True:
        c "And I'm so full..."
    Ka normal "If you insist."
    jump bangok_four_xkatsu_ending




label bangok_four_xkatsu_ending:
    scene black with dissolveslow
    $ renpy.pause(0.5)
    m "After serving up and putting the remainder into the icebox to stay cool, we wandered back out into the summer heat to enjoy the fruits of our labor and Katsuharu's loins."
    $ renpy.pause(0.5)
    scene extra9:
        zoom 2.0
        pos (-1000, -1080)
        linear 7.0 pos (-760,-300)
    with dissolvemed

    $ renpy.pause(3.0)
    Ka excited "How is it?"

    c "It's amazing!"

    if bangok_four_xkatsu.fill > 0:
        if persistent.c1liquid == True:
                c "..."
                c "You know, I think I've had it before."
                Ka normal "You have? How? Where?"
                c "When I moved into my apartment, there was this unlabeled container in the fridge. It was liquid, and slightly saltier."
                Ka exhausted "Oh no."
                Ka exhausted "This flavor doesn't keep in a refrigerator, and the last time I made any was before that other human arrived."
                c "You're telling me it had gone bad?"
                $ renpy.pause (0.8)
                c "That's what I get for drinking unlabeled containers, I guess."
        else:
            Ka smile "I concur."
    else:
        Ka exhausted "And this isn't even the peak of my quality for this flavor. With more volume, it always seems to blend better."

    $ renpy.pause(1.0)
    m "We enjoyed our batch of special cream, watching the sun sink lower in the sky."
    $ renpy.pause(1.0)

    label bangok_four_xkatsu_finalemenu:
    menu:
        "You gave your cart to Emera, but said you're leaving town..." if bangok_four_xkatsu.getcart == True:
            $ bangok_four_xkatsu.getcart = False
            Ka normal "Well, I'll be busy most of tonight making more of my usual flavors for whenver the minister lets me know I can retrieve my cart."
            c "Does she know how to contact you?"
            Ka exhausted "I told you she's a connoisseur, did I not?"
            c "Oh. Oh, you mean..."
            if bangok_four_xkatsu.fill > 0:
                Ka smile "I'm sure she'll be excited to know this particular flavor is back on the menu."
            else:
                Ka exhausted "I wish we'd made more for this batch."
                Ka normal "But I'm sure now that business is booming again, it's only a matter of time until I find more help."
                Ka smile "Or run into some old friendly faces."
            jump bangok_four_xkatsu_finalemenu
        "Does your \"help\" ever deposit into the mix?" if bangok_four_xkatsu.gethelp == True:
            $ bangok_four_xkatsu.gethelp = False
            Ka normal "Can't say that they have."
            c "If you let other dragons pitch in, that could help increase the volume of special you have to sell."
            Ka normal "I've trained myself over the years for quality and quantity."
            Ka exhausted "Who knows how anyone else's would compare."
            c "At the very least, you could try it for alternate flavors."
            if bangok_four_bryce1_unplayed == False:
                c "One of the customers that came by earlier today, I happen to know can produce enough for this."
                Ka smile "Eh? Which one?"
                c "Bryce."
                Ka smile "And you know this from experience, do you?"
                Ka "Hm. That chief of police. I'll have a word with him, then, next time I pass through town."
                c "Sure."
            jump bangok_four_xkatsu_finalemenu
        "Thanks for this, Katsuharu.":
            pass
    Ka smile "Don't go thanking me, now. You saved my business."
    if bangok_four_xkatsu.fill < 2 or bangok_four_xkatsu.flavor == 3:
        Ka exhausted "It was the least I could do."
    else:
        Ka excited "It was the least I could do."
    c "I think I need to head back to my apartment now, but I'll definitely keep an eye out for you on Tatsu Avenue."
    Ka smile "Sure, human."
    if bangok_four_xkatsu.fill > 1 or bangok_four_xkatsu.flavor == 3:
        Ka smile "And if you want any more special, just ask."
        c "I will."

    stop music fadeout 1.0
    scene black with dissolveslow
    $ renpy.pause (1.0)
    jump _mod_fixjmp

