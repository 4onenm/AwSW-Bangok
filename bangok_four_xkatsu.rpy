init python in bangok_four_xkatsu:
    whatcum = True

label bangok_four_xkatsu:
    show black with dissolvemed
    $ renpy.pause (1.0)
    Ka excited flip "Wait a minute!" with Shake ((0, 0, 0, 0), 2, dist=10)
    hide black with dissolveslow
    $ renpy.pause (0.5)
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
    scene black with dissolvemed
    $ renpy.pause(0.8)

    nvl clear
    window show
    n "When Katsu had said an hour wait, he hadn't been kidding."
    n "It was over twenty minutes before I heard noises that indicated he might be successfully producing the key ingredient."
    n "I dozed off after that, waiting for him to call me back in about the ready ice cream."
    window hide
    nvl clear

    $ renpy.pause (1.0)

    Ka exhausted "Alright human. Come on back."

    $ renpy.error("TODO: Why would you do this to him?")

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
    menu:
        "I didn't expect to go beyond a handjob.":
            pass
        "I guess I could suck you off.":
            pass
        "I suppose I could help you with my ass.":
            pass
        "If that's what it takes, I could help you with my vagina." if bangok_four_playerhasdick == False:
            pass
        "What if I fit inside you?" if bangok_four_playerhasdick == True:
            pass

s "TODO: Out of content."
$ renpy.error ("TODO: Out of content.")