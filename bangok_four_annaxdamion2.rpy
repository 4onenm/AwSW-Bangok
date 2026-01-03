##################### NOTICE #####################
# Per request from the commissioner of the artwork
#  forming the basis of this scene, absolutely no
#  watersports (nor any mention thereof) is to be
#  added to this scene.
init python in bangok_four_xdamion_store:
    annaxdamion2_seen = False

label bangok_four_annaxdamion2_sceneselect:
    scene black with dissolve
    $ renpy.pause (0.5)
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (0.5)

label bangok_four_annaxdamion2:
    c "(The facility isn't {i}that{/i} big. She must be around here somewhere, right?)"
    play sound "fx/steps/clean2.wav"
    scene black with dissolvemed
    $ renpy.pause (1.0)
    m "It quickly became apparent that nearly all of the dragons working here had already gone home for the day."
    scene bangok_four_facin3_wall:
        yalign 0.8
        xalign 0.0
        linear 3.0 xalign 1.0
        xalign 1.0
    with dissolvemed
    m "The sun set as I walk, and the facility's lights dimmed to nearly nothing, leaving me alone and frustrated."
    c "(I'm not sure who the world record holder for \"most patient person\" is, but now I feel like a contender.)"
    if (bangok_four_common.bangnokay.check()):
        c "(It'd be wild if I caught a glimpse of her through a floor-height vent, wouldn't it?)"
        c "(Or if I heard her voice echoing through the halls?)"
        c "(Oh well. At this point I might as well go back to the lab.)"
        jump bangok_four_annaxdamion2_abort_fade
    c "(Still no sign of--)"
    scene bangok_four_facin3_wall:
        yalign 0.8
        xalign 1.0
        ease 1.0 xalign 0.5
        xalign 0.5
    with None
    m "As I'm thinking of turning back to the lab, or giving up entirely, I hear the murmur of a voice from a nearby floor-height vent."
    m "Looking up and down the hallway, I saw no doors around. With the maze-like layout of the facility, I wasn't sure I'd be able to find the entrance to the room before those dragons went home too."
    menu:
        "Try to look inside.":
            $ renpy.pause (0.5)
        "Go back to Anna's lab.":
            $ renpy.pause (0.5)
            m "Deciding there was nothing more to be gained from useless wandering, I turned to go back to Anna's lab door."
            label bangok_four_annaxdamion2_abort_fade:
                scene black with dissolve
                play sound "fx/steps/clean2.wav"
                $ renpy.pause (1.0)
                scene facin3 at Pan ((128, 250), (128, 250), 0.0) with dissolvemed
                jump bangok_four_annaxdamion2_nosign_return
    scene bangok_four_facin3_wall:
        align (0.5,0.8)
        zoom 1.0
        linear 1.0 zoom 2.0
        zoom 2.0
    show black:
        alpha 0.0
        linear 1.0 alpha 1.0
        alpha 1.0
    with None
    m "Leaning down to the vent, I tried to look inside, at the same time as I heard a wet slurping."
    scene bangok_four_annaxdamion2 track stage1
    show bangok_grey
    show bangok_four_facin3_wall_vent track:
        zoom 3.0
        linear 1.0 zoom 4.0
        zoom 4.0
    with dissolvemed
    Dm "Fuck, there's a good bitch who knows her place."
    "???" "Gck!"
    menu:
        "Look closer.":
            $ renpy.pause (0.5)
        "Go back to Anna's lab.":
            $ renpy.pause (0.5)
            m "Deciding not to be involved in whatever was happening on the vent's far side, I rose and turned to go back to Anna's lab door."
            jump bangok_four_annaxdamion2_abort_fade
    show bangok_four_facin3_wall_vent track:
        zoom 4.0
        linear 1.0 zoom 5.0
        zoom 5.0
    show bangok_grey:
        alpha 1.0
        linear 1.0 alpha 0.0
        alpha 0.0
    with None
    $ bangok_four_xdamion_store.annaxdamion2_seen = True
    $ renpy.pause (1.5)
    m "As soon as my eyes adjusted to the light on the far side of the vent, I spotted Anna's tongue snaking around another dragon's shaft while he held her head into his crotch."
    An disgust b "Nnnglk..."
    Dm arrogant "Was that a moan? I thought you wanted us to keep this quiet."
    m "I stared, dumbfounded that Anna kept me waiting so she could suck this dragon's dick instead of honoring our agreement."
    menu:
        "Go home.":
            m "In the end, I decided that enough was enough. Not willing to wait for her to finish her sucking, I left, even though she still owed me that date."
            $ annastatus = "bad"
            $ annascenesfinished = 2
            stop music fadeout 2.0
            jump _mod_fixjmp
        "Go back to the lab.":
            m "I had seen enough. Though I still hadn't made up my mind about what to say to her, I did still want to see if she'd even remember to meet me at the lab, late as it was now."
            m "I decided to go back to the lab door and wait until she finished her sucking and showed her cum-stained face, or until I decided to give up on her."
            play sound "fx/steps/clean2.wav"
            scene black with dissolvemed
            $ renpy.pause (1.0)
            scene facin3 at Pan ((128, 250), (128, 250), 0.0) with dissolvemed
            jump bangok_four_annaxdamion2_nosign_return
        "Watch.":
            $ renpy.pause (0.5)
    show bangok_four_annaxdamion2 track stage2 with dissolve
    m "I kept my face nearly pressed to the vent, mesmerized by the sights in front of me as Anna closed her eyes and, of her own accord, took Damion a little deeper."
    Dm arrogant "Nngh. That's how you should treat me."
    Dm arrogant "Are you sure you want to stay in genetics and facility management? Maybe I should hire you as my full-time cocksleeve instead."
    if persistent.bangok_cloacas == True:
        m "Despite Damion's demeaning words as Anna's head bobbed up and he pushed it down, I could see when I was closer to the lower left of the vent hints of wetness dripping from Anna's puffy cloaca, on display beneath her lifted tail."
    else:
        m "Despite Damion's demeaning words as Anna's head bobbed up and he pushed it down, I could see when I was closer to the lower left of the vent hints of wetness dripping from Anna's puffy pussy, on display beneath her lifted tail."
    m "Damion let out a sigh of contentment as Anna's head bobbed up and down, her tongue working his shaft with a practiced ease."
    Dm arrogant "That's it, Anna. You're almost there."
    Dm arrogant "I almost like your mouth more than your other end."
    show bangok_four_annaxdamion2 track stage1 with dissolve
    m "He pulled on her head a little harder as Anna's eyes opened, and she looked up at him."
    Dm face "What do you think? You rushing to a bathroom with it all running down your legs, or...? Nngh..."
    m "Anna's eyes widened as Damion yanked her head down, then held her there."
    if persistent.bangok_inflation == True:
        show bangok_four_annaxdamion2 track stage3 bulge1 with dissolve
        m "The first sign of Damion's climax was a shudder that ran through his body, then a bulge forming in Anna's throat as he flooded it with his seed."
        show bangok_four_annaxdamion2 track stage3 bulge2 with dissolve
        m "Anna's eyes rolled back, then closed. Her throat bulged with the sheer volume of his load, which was now leaking from her mouth."
        show bangok_four_annaxdamion2 track stage3 bulge3 with dissolve
        m "He tugged on Anna's head again, eliciting a gagging sound from her as a small drop of cum even escaped her nose."
        show bangok_four_annaxdamion2 track stage4 postbulge with dissolve
    else:
        show bangok_four_annaxdamion2 track stage3 with dissolve
        if persistent.bangok_balls == True:
            m "The first sign of Damion's climax was a shudder that ran through his body, then rivulets of cum began to spill from Anna's mouth, running down her tongue and Damion's balls."
        else:
            m "The first sign of Damion's climax was a shudder that ran through his body, then rivulets of cum began to spill from Anna's mouth, running down her tongue and Damion's member."
        m "Anna's eyes rolled as she gagged on Damion's load."
        show bangok_four_annaxdamion2 track stage4 with dissolve
    m "Then, finally, Damion let up the pressure on Anna's head, allowing her to swallow his cum and a bit of air, though he kept his cock in her mouth."
    $ renpy.pause (0.8)
    Dm arrogant "Well, what do you think?"
    m "Anna's tail lashed angrily as she choked on his cock."
    An sad b "Grck."
    if persistent.bangok_cloacas == True:
        Dm arrogant "If that's what you want. I'll stuff your cloaca again next time."
    else:
        Dm arrogant "If that's what you want. I'll stuff your pussy again next time."
    show bangok_four_facin3_wall_vent track:
        zoom 5.0
        linear 1.0 zoom 4.0
        zoom 4.0
    show bangok_grey:
        alpha 0.0
        linear 1.0 alpha 1.0
        alpha 1.0
    with None
    m "With a shove, he pushed her off his groin, and Anna coughed wetly on the floor."
    $ renpy.pause (0.5)
    m "A few seconds passed before she could speak again."
    An disgust b "Where is it, Damion?"
    Dm arrogant "On top of the lockers, around the corner from your lab."
    Dm arrogant "I bet you walked past it two or three times to the mailroom looking for it, too."
    An disgust b "Bastard."
    Dm arrogant "You wouldn't keep working with me if you didn't love it."
    Dm normal "Now go on. I need to clean myself up because you can't keep it all down."
    An sad b "..."
    scene black with dissolve
    scene bangok_four_facin3_wall at Transform(xalign=0.5, yalign=0.8, xpos=0.5, ypos=0.8) with dissolve
    m "Realizing that Anna would be returning to the lab soon, I quickly left the vent and made my way back to the lab door, still not certain what I would say, if anything, when she finally did appear."
    play sound "fx/steps/clean2.wav"
    scene black with dissolvemed
    $ renpy.pause (1.0)
    scene facin3 at Pan ((128, 250), (128, 250), 0.0) with dissolvemed
    jump bangok_four_annaxdamion2_nosign_return

label bangok_four_annaxdamion2_confrontation_choice:
    menu:
        "But was sucking that Damion so much more important?":
            jump bangok_four_annaxdamion2_confrontation
        "[[Let it go.]":
            jump bangok_four_anna2_wantthisornot_end

label bangok_four_annaxdamion2_confrontation:
    stop music fadeout 2.0
    show anna disgust with dissolve
    m "I couldn't believe that Anna had kept me waiting so she could suck Damion off."
    m "Yet here she was, acting like it was just work as usual."
    An "How the fuck could you know about that?"
    c "What part of leaving me waiting for two hours did you miss?"
    c "I got bored, started looking for you, and heard you two going at it through a vent!"
    if bangok_four_anna1_sexrequested == True:
        c "I'm not even sure I want to fuck you anymore, if you have guys queueing up so long the line takes {i}two hours{/i}!"
    else:
        c "In my world, it's generally impolite to make a suitor wait {i}two hours{/i} while you suck another guy off!"
    An face "I'm doing what I have to do!"
    c "Sucking off guys in the breakroom? Is that what you have to do?"
    An disgust "My work is my business, not yours. Keep your nose out of it and get back to whatever it is you're supposed to be doing here."
    c "Like you kept your nose out of Damion's crotch?"
    An rage "How about you get your nose out of my fucking building!"
    c "Maybe I will!"
    An face "Good!"
    if bangok_four_anna1_sexrequested == True:
        c "Good luck finding another fuckable human like me!"
    else:
        c "Good luck finding another human to poke and prod!"
    An despair "I don't need one!"
    play sound "fx/steps/clean2.wav"
    show anna cry with dissolveslow
    scene black with dissolveslow
    $ annastatus = "bad"
    $ annascenesfinished = 2
    stop music fadeout 2.0
    jump _mod_fixjmp
