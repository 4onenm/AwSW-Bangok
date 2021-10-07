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
        "What, like cum?" if whatcum:
            bangok_four_xkatsu.whatcum = False
            Ka "Yes."
            c "Semen?"
            Ka "Yes."
            c "Baby batter?"
            Ka excited flip "That exactly."
            jump bangok_four_xkatsu_seedmenu
        "No, thanks.":
            c "I think I'd like to wait for a wider selection."
            Ka normal flip "If you say so. But know that after tonight my special should be available for at least a few days."
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





s "TODO: Out of content."
$ renpy.error ("TODO: Out of content.")