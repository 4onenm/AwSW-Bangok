##################### NOTICE #####################
# Per request from the artist of the work forming
#  the basis of this scene, absolutely no water-
#  -sports (nor any mention thereof) is to be
#  added to this scene.

label bangok_four_brycexsebastian:
    m "I returned to the police station, mulling over what had happened today in my head."
    play soundloop "fx/breathing.ogg" fadein 1.0
    m "Before I could enter Bryce's office, however, I heard the sound of heavy breathing from inside, along with quiet murmurs."

    menu:
        "Listen closer.":
            pass
        "Come back a little later.":
            m "Not wanting to pry into whatever I was hearing, I decided to wait back at the station entrance until the sounds stopped, or until someone came out to greet me."
            jump bangok_four_brycexsebastian_abort_merge

    m "I stepped a little closer to the slightly-open door, listening to try to figure out what was going on."

    Br pantflirt "Mmnh. There's that depth." # Co-Pilot's suggestion: "Mmm... I'm so glad you're here, Sebastian."
    # Co-pilot again: m "I heard Bryce's voice, and I could tell he was panting. I could also tell that he was aroused."
    m "A wet \"Glk\" followed his statement, like someone choking."
    stop soundloop fadeout 0.8
    $ renpy.pause (0.8)
    Br brow "You okay down there?"
    Sb shy "Y-Yeah. Just the wrong spot."

    menu:
        "Peek.":
            pass
        "Come back a little later.":
            m "Not wanting to pry into whatever I was hearing, I decided to wait back at the station entrance until Bryce and Sebastian finished up."
            jump bangok_four_brycexsebastian_abort_merge

    $ renpy.pause (0.5)
    # TODO: Show Bryce & Sebastian
    scene bangok_four_brycexsebastian frameA:
        zoom 0.9
        xpos 600
        linear 1.0 xpos 400
        xpos 400
    show white:
        alpha 1.0
        ease 1.0 alpha 0.0
        alpha 0.0
    show bangok_four_officedoor track:
        anchor (0, 0)
        pos (-800, -6600)
        zoom 9.0
        ease 1.0 zoom 10.0 xpos -1100
        zoom 10.0
        xpos -1100
    with dissolvemed
    $ renpy.pause (0.5)
    hide white with None

    Br flirty "All good now?"
    Sb smile "Mm."
    Br flirty "So I could..."
    show bangok_four_brycexsebastian frameB brycesmile bryceeyeopen with dissolve

    m "I had no question now that what they were doing was something private. Standing here in the hallway, someone might spot me and tell them about it."
    m "Then they'd know I had been watching."

    menu:
        "Stay.":
            pass
        "Come back a little later.":
            show black with dissolveslow
            m "Leaving them to their fun, I decided to wait back at the station entrance until Bryce and Sebastian finished up."
            jump bangok_four_brycexsebastian_abort_merge

    show bangok_four_brycexsebastian frameA with dissolve

    show bangok_four_officedoor track:
        zoom 10.0
        pos (-1100, -6600)
        ease 0.5 zoom 15.0 pos (-2200, -9900)
        zoom 15.0
        pos (-2200, -9900)
    show bangok_four_brycexsebastian frameA:
        xpos 400
        ease 0.5 xpos 200
        xpos 200
    with None

    m "I adjusted my position, shamelessly peeking from closer to the crack in the door."

    Br normal "That work for ya?"
    Sb smile "MmMm."
    Br smirk "Well, one other idea I had..."
    Br flirty "Think you can take my entire load in your mouth and throat? Without swallowing?"
    Sb shy "Mm?!"
    $ renpy.pause (0.8)
    Sb smile "Mmhm."
    Br laugh "We'll see."
    Br pantflirt "Now let me {i}all{/i} the way in again."

    play soundloop "fx/breathing.ogg" fadein 2.0
    show bangok_four_brycexsebastian animate bryceclosedsmile sebastianopen with None
    $ renpy.pause (6.0)
    Br laugh "Good boy."
    $ renpy.pause (6.0)
    show bangok_four_brycexsebastian animate bryceclosed with None
    $ renpy.pause(0.8)
    Br laugh "M-Man I needed this."
    Br flirty "Thanks Sebastian."
    Sb smile "Mhh..."
    $ renpy.pause (4.0)
    Br smirk "Ready to test your capacity?"
    $ renpy.pause (0.5)
    stop soundloop fadeout 0.5
    play sound "fx/snarl.ogg"
    show bangok_four_brycexsebastian frameB nocum with dissolve
    $ renpy.pause (0.8)
    show bangok_four_brycexsebastian frameB cum with dissolve
    Sb shy "Glk!"
    $ renpy.pause (0.5)
    if persistent.bangok_inflation == True:
        show bangok_four_brycexsebastian frameB sebcheekbulge sebthroatbulge sebeyeshocked morecum with dissolve
        Sb shy "Gck."
        show bangok_four_brycexsebastian frameB sebcheekbulge sebthroatbulge morecum with dissolve
        $ renpy.pause (0.5)
        Br pantflirt "Now swallow."
        play sound "fx/gulpslow2.wav" fadein 0.5
        $ renpy.pause (0.5)
        show bangok_four_brycexsebastian frameB bryceeyeroll brycesmile sebcheekbulge morecum with dissolve
        $ renpy.pause (0.5)
        show bangok_four_brycexsebastian frameB bryceeyeroll brycesmile morecum with dissolve
        $ renpy.pause (0.6)
        show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeopen morecum with dissolve
        $ renpy.pause (0.3)
        stop sound fadeout 0.5

        Br smirk "Not to be the bearer of bad news, but it looks like you're gonna need a little more practice."
        show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile morecum with dissolve
    else:
        $ renpy.pause (0.5)
        Br pantflirt "Now swallow."
        play sound "fx/gulpslow2.wav" fadein 0.5
        show bangok_four_brycexsebastian frameB bryceeyeroll brycesmile cum with dissolve
        $ renpy.pause(4.5)
        show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeopen cum with dissolve
        stop sound fadeout 0.5

        Br brow "So, how much did you spill...?"
        Br smirk "Oh."
        Br smirk "Not to be the bearer of bad news, but it looks like you're gonna need a little more practice."

    
    show bangok_four_brycexsebastian_lickpanel:
        zoom 0.9
        xpos 200
        ypos -200
        linear 2.0 ypos 0
        ypos 0
    with dissolveslow
    $ renpy.pause (1.0)
    Br smirk "Now lick it clean..."
    $ renpy.pause (2.0)

    Br brow "Uh... I'd go get you a towel, but first you have to undo those cuffs." # Co-Pilot suggestion: "Uh... I'd go easy on the food for a while."
    Br smirk "If you throat it again, that should give you some more arm length to work with."
    Sb drop "Wai--"

    hide bangok_four_brycexsebastian_lickpanel
    show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeshocked
    with dissolve

    $ renpy.pause (0.5)

    show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeopen with dissolve

    Sb disapproval "Gck."
    Br brow "What?"

    scene black with dissolve

    m "As Bryce turned around to look at Sebastian, I ducked away before his gaze swept over the door."

    Sb drop "I dropped the key to the cuffs."
    Br laugh "Where?"
    Sb drop "I don't know! It bounced off your back when you were..."
    Br smirk "Alright, alright. Keep it down. Guess you're stuck to my hips for a little longer."
    Sb disapproval "I'm sure you're enjoying that."
    Br laugh "Of course!"

    m "Using their distraction searching for the key, I quietly slunk back to the entrance of the station."
    jump bangok_four_brycexsebastian_abort_merge

label bangok_four_brycexsebastian_abort_merge:
    m "I must have dozed off in a chair, as what felt like a few minutes later, Sebastian was nudging me awake and guiding me to Bryce's office."
    jump bangok_four_brycexsebastian_return