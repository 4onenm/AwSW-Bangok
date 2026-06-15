label bangok_four_bryce4_shower_intro:
    Br flirty "I promise you won't regret it."
    $ renpy.pause (0.5)
    hide bryce with dissolve
    play sound "fx/steps/clean2.wav"
    scene black with dissolve
    $ renpy.pause (0.5)
    scene bath with dissolve
    $ renpy.pause (0.5)
    show bryce smirk flip at left with dissolve
    m "Bryce dropped the basket on the counter next to the sink, the wine bottle clunking against the lube bottles."
    Br flirty flip "Who gets to enjoy first? You? Me? 50/50?"
    menu:
        "Your idea. You go ahead and bend over.":
            jump todo_out_of_content_bangok_four_bryce4_shower
        "Can't let you guzzle it all. I'll have it.":
            jump todo_out_of_content_bangok_four_bryce4_shower
        "Those condoms... wanna drink it outta me?":
            jump todo_out_of_content_bangok_four_bryce4_shower



label todo_out_of_content_bangok_four_bryce4_shower:
    play sound "fx/system3.wav"
    s "Bryce4 Shower Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")