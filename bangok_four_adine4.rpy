init python in bangok_four_adine4_store:
    # Funtime memnu
    tease_available = True


    # Afterglow
    howwas_available = True
    kiss_available = True



label bangok_four_adine4_intro:
    Ad normal b "You're right. I suppose you can spend the night here then..."
    c "I guess so."

    Ad normal b "Would you...{w=0.1}{nw}"
    # TODO: Fix to blush
    Ad giggle b "Would you{fast} like to share the bed?"

    menu:
        "Accept.":
            pass
        "Reject.":
            c "It's fine, I can just sleep on the beanbag."
            Ad sad b "Oh, are you sure? Sorry for asking..."
            c "Don't worry about it."
            $ renpy.pause(1.5)
            scene black with dissolvemed
            $ renpy.pause(0.5)
            play sound "fx/undress.ogg"
            $ renpy.pause(1.5)
            Ad normal b "How does it feel?"
            c "It's alright."
            Ad normal b "Good night."
            $ renpy.pause(0.5)
            c "Sleep well."
            jump bangok_four_adine4_sceneover

label bangok_four_adine4_bedintro:
    scene adineapt2 at Pan ((20, 300), (20,300), 0.0) with dissolvemed
    $ renpy.pause(0.3)
    play sound "fx/undress.ogg"
    show adine normal flip at left with dissolve
    Ad "How does it feel?"
    c "Your bed feels nice."
    Ad "Are you comfortable sleeping like this?"

    menu:
        "Yep.":
            c "Yes. Sleep well."
            Ad "Good night."
            jump bangok_four_adine4_sceneover
        "[[Move a little closer.]":
            pass
    play sound "fx/undress.ogg"
    show adineapt2 at Pan ((0, 300), (0,300), 0.0) with ease
    c "Can I..."
    Ad think flip "Yes?"
    c "Can I hug you?"
    # TODO: Fix to adine blush
    show adine giggle flip with dissolve
    m "She nodded and started blushing while looking into my eyes."
    m "I turned to her, closing the space between us and started hugging her."
    play sound "fx/undress.ogg"
    # TODO: Fix to adine blush
    show adine giggle flip at center with ease
    m "Then she started sliding her wing under me and pulled me towards her, embracing me nicely."
    Ad "You feel so nice"
    m "I hugged her and caressed her back."
    play soundloop "fx/purr.ogg"
    m "Then I began to hear a familiar sound."
    $ renpy.pause(2.0)
    m "We enjoyed laying in each others embrace for a while. Hugging a wyvern felt better than i ever could have imagined."
    $ renpy.pause(4.0)
    Ad "...could do this for hours."
    if persistent.nsfwtoggle == True and persistent.bangok_dev == True:
        menu:
            "Sleep in your shared embrace.":
                pass
            "Go further.":
                jump bangok_four_adine4_funtimes

    c "Can we sleep like this?"
    Ad "Of course."
    c "Sleep well, Adine."
    Ad "Good night, [player_name]."
    stop soundloop fadeout 2.0
    jump bangok_four_adine4_sceneover

label bangok_four_adine4_funtimes:
    $ renpy.pause(0.8)
    c "Adine?"
    stop soundloop fadeout 1.0
    $ renpy.pause(1.0)
    Ad think flip "Yes [player_name]?"
    $ renpy.pause(0.3)
    c "Would you...{w=0.4}{nw}"
    c "Would you{fast} like to take this...{w=0.4}{nw}"
    c "Would you like to take this{fast} a step further?"
    # TODO: Fix to Adine blush
    show adine think flip with dissolve
    $ renpy.pause(2.0)
    m "I regretted my question and waited for her response until she suddenly agreed."
    Ad giggle flip "Yes. I would love to."
    play sound "fx/undress.ogg"
    scene adineapt2 at Pan ((128, 300), (128,300), 0.0)
    show adine normal flip at left
    with Fade(1.0,0.0,1.5)

    m "I slowly got out of the bed to take my clothes off while Adine repositioned herself on the bed while watching me."
    m "After I got rid of my clothes I sat down next to Adine on the bed and gently rubbed her cheek."
    m "She didn't say anything but closed her eyes and enjoyed it."
    m "After I slowly stopped rubbing her muzzle she leaned closer to me."
    Ad "What would you like to do?"

label bangok_four_adine4_funtimes_menu:
    menu:
        "Tease her." if bangok_four_adine4_store.tease_available == True:
            $ bangok_four_adine4_store.tease_available = False
            jump bangok_four_adine4_tease
        "Ride her.":
            jump todo_out_of_content_bangok_four_adine
        "Ask her to ride you.":
            jump todo_out_of_content_bangok_four_adine
        "Ask her to suck you." if bangok_four_adine4_store.tease_available == False:
            jump todo_out_of_content_bangok_four_adine

label bangok_four_adine4_tease:
    m "Adine spread her legs, revealing her slit, and started blushing."
    # TODO: Fix to blushing
    show adine think flip with dissolve
    Ad "Please be careful."
    c "Of course."
    m "Slowly, I leaned myself down to her slit and licked slowly around it."
    Ad giggle frillrubs flip "Ohhh"
    m "I kept licking and carefully licked a little inside her snatch."
    # TODO: adine pleasured
    Ad giggle frillrubs closed flip "That feels so good."
    m "I continued my motions inside her slit and noticed that she was enjoying it, already getting pretty wet."
    m "Adine got more and more pleasure by my movements inside and I started focusing more on her clit and starting to taste her sweet juice."
    Ad "You feel so good, If you continue like this I don't think I will last long."
    menu:
        "Slowly stop licking.":
            m "Adine's breathing slowed as I let up in my ministrations on her slit."
            $ renpy.pause(0.5)
            Ad think frillrubs flip "Okay, what next?"
            jump bangok_four_adine4_funtimes_menu
        "Continue.":
            pass
    m "Encouraged by her praise, I started licking faster and deeper, getting her pleasured quickly"
    #adine very pleasured
    m "As i kept pleasing her love passage, I noticed her lightly leaking her juice on my tongue as she moaned faster, telling me that she was close."
    #small pause, then growl sound and purring after
    $ renpy.pause(0.8)
    play sound "fx/varagrowl.ogg"
    play soundloop "fx/purr.ogg" fadein 4.0
    m "Suddenly she released her love juice on my tongue and in my mouth, filling it with a sweet taste as she started purring."
    c "Did you like that?"
    m "She didn't answer and only purred loudly."
    jump bangok_four_adine4_funtimes_over_menu

label bangok_four_adine4_funtimes_over_menu:
    menu:
        "How was it?" if bangok_four_adine4_store.howwas_available == True:
            $ bangok_four_adine4_store.howwas_available = False
            c "How was it?"
            Ad "It was better than I could ever dream it to be."
            show adine giggle flip with dissolve
            c "I'm glad you liked it."
            jump bangok_four_adine4_funtimes_over_menu
        "[[Kiss her.]" if bangok_four_adine4_store.kiss_available == True:
            $ bangok_four_adine4_store.kiss_available = False
            m "Slowly, I leaned myself to her muzzle and gently held her cheeks with my hands, slowly guiding her towards me to kiss her."
            m "Then I kissed her on the muzzle and closed my eyes. I was sure she did too, enjoying it."
            m "As we kept kissing we felt warm and our feelings for each other, it was amazing."
            jump bangok_four_adine4_funtimes_over_menu
        "Snuggle up and sleep.":
            m "Once more, we lied together in each others embrace, closing our eyes as we rested in each others grasp."
            c "Good night my lovely wyverness."
            Ad "Good night [player_name]"
    jump bangok_four_adine4_sceneover

        
label todo_out_of_content_bangok_four_adine:
    play sound "fx/system3.wav"
    s "TODO: Out of content. Rollback and save or prepare to crash."
    $ renpy.error("Out of content.")