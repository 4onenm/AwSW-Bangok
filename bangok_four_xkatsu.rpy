init python in bangok_four_xkatsu:
    whatcum = True
    protection = True
    playercame = False
    playerstuffed = False

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
    Ka smile "Thought you were the kind who might."
    show katsu at center with ease
    m "He moved over top of one of the buckets, nudging them closer together, then arranging his hindlegs on either side."
    Ka exhausted "Give me a minute to get the old baculum moving on out."
    $ renpy.pause (0.5)
    m "He strained, but it was clear whatever he was thinking and whatever he was doing together weren't going to be enough."
    m "I knelt by the buckets, inspecing the spot where the tip of something was just peeking between two of his underbelly plates, back between his legs."
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
            pass
        "I guess I could suck you off.":
            pass
        "I suppose I could help you with my ass.":
            pass
        "If that's what it takes, I could help you with my vagina." if bangok_four_playerhasdick == False:
            pass
        "What if I fit inside you?" if bangok_four_playerhasdick == True and bangok_four_xkatsu.playercame == False:
            Ka exhausted "Eh?"
            show katsu at Position(xpos=0.45,xanchor='center') with ease
            m "I moved around to Katsuharu's hindquarters, already unbuckling my pants to reveal my hardening shaft."
            Ka normal "Ah, one of those customers."
            Ka exhausted "Y'know, that's not always enough for me. Especially with you being all that small compared to me."
            m "Getting under his tail, I hoisted it and his hindquarters up."
            c "We have a saying in our world: It's not your size, it's how you use it."
            Ka smile "Didn't say we couldn't try it."
            if persistent.bangok_cloacas == True and bangok_four_firsttime == True:
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
                                $ bangok_four_xkatsu.playerstuffed = True
                                m "When the pulses finally stopped and I came up for air, my shirt felt noticeably tighter. I wiped off the few thick ropes stuck to my face, licking my fingers clean."
                                hide black with dissolvemed
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

            show katsu at left with ease
            show katsu exhausted flip with dissolve
            m "He took a few shaky steps away from the buckets, then sat down."
            Ka "I... ah... might need some help finishing up the recipe."
            if bangok_four_xkatsu.fill == 3 and persistent.bangok_inflation == True and bangok_four_xkatsu.playerstuffed == False:
                Ka "First, put that bowl away in the icebox. Don't want it to spoil too fast."
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
            show katsu excited with None
            jump bangok_four_xkatsu_ready







        "Protection?" if bangok_four_xkatsu.protection == True:
            $ bangok_four_xkatsu.protection = False
            Ka exhausted "What, and get the taste of that rubber stuff into my special cream?"
            Ka normal "I don't buy the things. I get any customers of the same species as me, we just take a few more precautions."
            Ka smile "Not that that's a problem here."
            jump bangok_four_xkatsu_sexmenu
        "I'm... not so keen on helping now." if bangok_four_xkatsu.protection == False:
            jump bangok_four_xkatsu_wait


label bangok_four_xkatsu_outofcontent:
play sound "fx/system3.wav"
s "TODO: Out of content."
$ renpy.error ("TODO: Out of content.")

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
            "I think I got enough topping earlier." if bangok_four_xkatsu.playerstuffed == True:
                pass
            "I can't wait to try it!":
                pass
    else:
        jump bangok_four_xkatsu_outofcontent
    $ renpy.pause (0.5)
    Ka "All that's left is to serve up. Cup or cone?"

    $ renpy.pause(0.8)

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

    if bangok_four_xkatsu.fill > 1:
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
    if bangok_four_xkatsu.fill < 2:
        Ka exhausted "It was the least I could do."
    else:
        Ka excited "It was the least I could do."
    c "I think I need to head back to my apartment now, but I'll definitely keep an eye out for you on Tatsu Avenue."
    Ka smile "Sure, human."
    if bangok_four_xkatsu.fill > 1:
        Ka smile "And if you want any more special, just ask."
        c "I will."

    stop music fadeout 1.0
    scene black with dissolveslow
    $ renpy.pause (1.0)
    jump _mod_fixjmp

