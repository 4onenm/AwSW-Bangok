default bangok_four_xipsum2_store.protection = False

default bangok_four_xipsum2_store.scene = None
# Scenes:
#    truedp - Ipsum takes f character's ass and pussy at the same time.
#    assdp  - Ipsum fits both cocks in the player character's ass.
#    ass    - Ipsum fits one cock in the player's ass and hotdogs with the other.
#    df     - I

default bangok_four_xipsum2_store.has_both = False
default bangok_four_xipsum2_store.shared_with = None
# This "sharing" enum covers extra use scenes.
#  0 - Not shared.
#  1 - The player only shared it with the target.
#  2 - The player shared it with the target and a small group.
#  3 - Free use for the target's friends.
default bangok_four_xipsum2_store.sharing = 0


label bangok_four_xipsum2_answ_machine:
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.5)
    Ip happy "Hello, [player_name]! It's Ipsum, Lorem's roommate."
    Ip normal bangok blush "I've just developed something that, given our last encounter, I believe you will find quite stimulating."
    $ renpy.pause (0.5)
    Ip think "Whatever fits your schedule, of course. But it {i}may{/i} no longer be available after the coming fireworks."
    Ip normal "Call me back when you get the chance."
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.8)
    c "(Stimulating, huh?)"
    jump ml_answeringmachine_end


label bangok_four_xipsum2:
    stop music fadeout 1.0
    $ c4csplayed += 1
    $ chap4picka = "ipsum"
    play sound "fx/steps/clean2.wav"
    scene black with dissolveslow

    $ save_name = (_("Chapter 4 - Bangok Ipsum 2"))

    $ renpy.pause (1.0)
    scene loremapt at Pan ((0, 0), (128,62), 5.0) with dissolveslow

    play music "mx/snowflake.ogg" fadein 2.0

    play sound "fx/door/door_open.wav"

    $ renpy.pause (2.0)

    Ip happy "[player_name], welcome back."

    show ipsum happy bangok briefs at center with dissolve

    c "Hey Ipsum."

    menu:
        "What's this about?":
            $ renpy.pause (0.5)
        "You wear clothes now?":
            show ipsum think bangok briefs with dissolve
            $ renpy.pause (0.5)
            c "Well, pants. What are those, swimming briefs?"
            Ip think bangok briefs "Well, yes. With some modifications."
    Ip normal bangok briefs "As I implied in my call, this will be another encounter of a sexual kind. Are you okay with that?"
    c "I wouldn't be here if I wasn't."
    show ipsum happy bangok briefs with dissolve
    c "The implication was pretty clear."
    Ip happy bangok briefs "Good."
    Ip think bangok briefs "And before we go any further, I should ask if you would prefer to use protection."
    Ip normal bangok briefs "According to the results I obtained from our last meeting's samples, there is no strict chemical or biological issue I can detect with us having fun unprotected."
    Ip "Still, it is up to you."

    menu:
        "Yeah, I'd prefer protection.":
            $ renpy.pause (0.5)
            Ip normal bangok briefs "One moment, then."
            $ renpy.pause (0.3)
            show ipsum normal bangok briefs flip with dissolve
            $ renpy.pause (0.3)
            hide ipsum with easeoutright
            $ renpy.pause (0.3)
            play sound "fx/door/close2.wav"
            $ renpy.pause (1.0)
            play sound "fx/door/close2.wav"
            $ renpy.pause (0.5)
            show ipsum normal bangok briefs with easeinleft
            $ renpy.pause (0.3)
            $ bangok_four_xipsum2_store.protection = True
            if bangok_four_playerhasdick == True:
                m "He handed me a condom."
            Ip happy bangok briefs "Where were we?"
        "Unprotected sounds fun.":
            $ renpy.pause (0.5)
            $ bangok_four_xipsum2_store.protection = False
            Ip normal bangok blush briefs "Excellent."

    c "What now?"
    Ip happy bangok briefs "Now, if you would, strip and put these on."
    play sound "fx/necklace.ogg"
    m "He handed me an identical-looking pair of swim briefs he'd had tucked into his waistband near his tail, which were surprisingly heavy for their size."
    m "I glanced inside. Apart from a pair of dark disks sewn in toward the bottom, likely, the source of the weight, I couldn't find anything amiss."
    menu:
        "What are these going to do?":
            $ renpy.pause (0.5)
            Ip normal bangok briefs "You'd find out relatively quickly if you put them on."
            menu:
                "I'm not a fan of surprises, Ipsum.":
                    Ip think bangok briefs "Are you sure? Part of the stimulation is in not knowing what is going to happen."
                    c "Ipsum, I swear to--"
                    Ip sad bangok briefs "Fine, fine."
                    $ renpy.pause (0.3)
                    show ipsum sad bangok briefs touch with dissolve
                    $ renpy.pause (0.3)
                    play sound "fx/flicker.ogg"
                    $ renpy.pause (0.1)
                    show ipsum sad bangok briefs touch glow with None
                    m "As Ipsum reached into his briefs and fiddled with something, abruptly the disks in the pair he'd handed me lit up. I saw three of his fingers waggling through the center of one disk."
                    c "(Cameras and screens? I don't...)"
                    m "Then I realized his fingers were actually stiking out of the disk."
                    c "Woah!"
                    Ip happy bangok briefs touch glow "\"Woah,\" indeed."
                    Ip normal bangok briefs touch glow "Would you like to put them on, now?"
                    c "Y-Yeah, sure."
                    play sound "fx/undress.ogg"
                    $ renpy.pause (0.5)
                    queue sound "fx/leather.ogg"
                    $ renpy.pause (1.0)
                    m "I stripped out of my clothes, then pulled the strange briefs most of the way up. I kept them off my waist, though, still looking down at the glowing disks."
                "Alright, fine.":
                    jump bangok_four_xipsum2_surprise
        "[[Put them on.]":
            label bangok_four_xipsum2_surprise:
            $ renpy.pause (0.5)
            show ipsum normal bangok blush briefs with dissolve
            play sound "fx/undress.ogg"
            $ renpy.pause (0.5)
            m "I stripped out of my clothes, since it was nothing Ipsum hadn't seen last time. Then I stepped into the tight pair of swim briefs and pulled them up."
            play sound "fx/leather.ogg"
            $ renpy.pause (1.0)
            c "How's that?"
            Ip "Ideal."
            $ renpy.pause (0.3)
            show ipsum happy bangok briefs touch with dissolve
            $ renpy.pause (0.3)
            m "To my confusion, he reached inside of his briefs and fiddled with something."
            play sound "fx/flicker.ogg"
            $ renpy.pause (0.1)
            show ipsum happy bangok briefs touch glow with None
            if bangok_four_playerhasdick is None:
                m "Abruptly, I felt..."
                menu:
                    m "Abruptly, I felt...{fast}"
                    "Cold claws stroking my balls.":
                        $ bangok_four_playerhasdick = True
                    "Cold claws sinking into my lower lips' folds.":
                        $ bangok_four_playerhasdick = False
            if bangok_four_playerhasdick == True:
                m "Abruptly, I felt {fast}cold claws and scaly fingers stroking down the back of my balls."
            else:
                m "Abruptly, I felt {fast}cold claws and scaly fingers sinking into the folds of my lower lips."

            show loremapt at Pan ((0, 0), (128,72), 0.0) with vpunch
            m "I yelped, dropping to my knees and grabbing at the briefs, then yanking them down to discover what Ipsum had done."
            play sound "fx/slide.ogg"
            $ renpy.pause(0.3)
            m "Three of his fingers waggled out at me from one of the disks, which were now glowing."
            c "Woah!"
            Ip happy bangok briefs touch glow "\"Woah,\" indeed."
            show loremapt at Pan ((0, 0), (128,62), 0.0) with ease
            m "Mystery sensations explained, I got back to my feet, though kept the briefs pulled down a little so I could look at the strange disks."
    c "How do these work?"
    Ip think bangok briefs "Well, during all of my idle research into the black hole, wormhole theory on the portal, I discovered the Minister of Science had launched a secret program at the production facility attempting to replicate the portal technology, and..."
    Ip happy bangok briefs "The short answer is I have no idea. I may have \"borrowed\" them from another lab during the hubub of the police coming to raid a third party."
    c "... I see."
    Ip think bangok briefs "You can keep that secret, can't you [player_name]?"
    c "Sure."
    Ip happy bangok briefs "Excellent. Then, would you like something a little more substantive than my fingers?"

    menu:
        "Can you take both my ass and pussy comfortably with this?" if bangok_four_playerhasdick == False:
            $ renpy.pause (0.5)
            Ip normal bangok briefs "That was actually somewhat my hope in making them."
            jump bangok_four_xipsum2_truedp
        "I'd prefer you stick with just my ass, if that's okay." if bangok_four_playerhasdick == False:
            $ renpy.pause (0.5)
            Ip sad bangok briefs "I had hoped to try out whether this would help me deal with the gap between your reproductive passage and anus. Two cocks, two holes."
            Ip normal bangok briefs "But if anal play is what you would prefer."
            jump bangok_four_xipsum2_ass_split
        "Can we fuck each other at the same time with this?" if bangok_four_playerhasdick == True:
            $ renpy.pause (0.5)
            Ip normal bangok briefs "It's entirely possible!"
            Ip think bangok briefs "At least, I believe so. I did try to design in the possibility."
        "You've got two cocks and I have one ass." if bangok_four_playerhasdick == True:
            $ renpy.pause (0.5)
            Ip normal bangok briefs "That is the case, yes."
            jump bangok_four_xipsum2_ass_split
    jump todo_out_of_content_bangok_four_xipsum2

label bangok_four_xipsum2_truedp:
    play sound "fx/leather.ogg"
    $ renpy.pause (0.1)
    stop sound fadeout 0.5
    m "I pulled up my briefs the rest of the way, nestling the disks against my front and rear entrances."
    m "With the disks active, I could feel his hard plates within their metal circumference, a tiny bit of his warmth radiating through into my crotch, even as he still stood a few feet away."
    $ renpy.pause (0.3)
    show ipsum happy bangok briefs touch glow with dissolve
    $ renpy.pause (0.3)
    m "Then he reached inside his briefs again, and I felt the air of the room against my lower holes. Scaly knuckles brushed over my pussy, then my ass, transferring a small amount of my lubrication."
    if bangok_four_xipsum2_store.protection == True:
        m "His condom-enwrapped tips nestled against my holes, sending electric sparks up into my center and down toward my weak knees."
    else:
        m "His tips nestled against my holes, sending electric sparks up into my center and down toward my weak knees."
    Ip "Ready?"
    m "I pressed the briefs more tightly against my holes, hoping to tease out just a taste of his lengths early."

    play sound "fx/slap1.wav"
    $ renpy.pause(0.0)
    show ipsum happy bangok blush briefs with None
    m "He let the waistband of his briefs snap back against his hips, forcing his cocks into me with startling speed."
    m "We both gasped. Even though I was prepared this time, my knees still wobbled, nearly sending me to the floor from the sensations."
    $ renpy.pause(0.8)
    Ip "That may be too fast for me. How do you feel?"
    c "I... I think I need..."
    m "I took a few steps toward the couch. As I did, my inner walls shifted around his shafts, sending yet another wave of pleasure through me."
    Ip normal bangok aheago briefs "Nnnngh."
    Ip normal bangok blush briefs "Y-Yes. I think I should join you sitting down."
    hide ipsum with dissolvemed
    $ renpy.pause(0.3)
    show loremapt at Pan((128,62),(0,42), 2.0) with ease
    $ renpy.pause(2.3)
    show ipsum happy bangok blush flip:
        xanchor 0.0
        yanchor 1.0
        xpos 0.0
        ypos 1.3
        rotate -5
    with dissolve
    m "We both reclined back on the couch. His cocks shifted inside me, held in place like dildos by the tight briefs around my waist."
    m "The inner walls of my passage kneaded and massaged his length, milking him for stimulation now that he was fully inside."
    show ipsum normal bangok blush briefs touch glow flip with dissolve
    m "Ipsum slid his hand back inside his briefs, lifting his side of the disks away from his slit."
    m "In turn, his cocks slid out of me, leaving me aching for his next thrust."
    play soundloop "fx/bangok_poundofsalt.ogg"
    m "He began to fuck me for real, casually lifting and lowering the front of his briefs."
    m "I squirmed, the lack of heat, weight, or hips between my legs confusing my senses as my pussy and ass were pressed open, again and again, in perfect time with one another."
    $ renpy.pause (0.5)
    show ipsum normal bangok blush briefs touch glow flip with dissolve
    m "He reached over, slipping a hand beneath my waistband, then began to gently circle my labia with one clawtip -- while still fucking me."
    $ renpy.pause (1.0)
    
    Ip happy bangok blush briefs touch glow flip "How do you feel about exhibitionism?"
    c "W-What?"
    Ip normal bangok blush briefs touch glow flip "Would you, say, want to get caught like this?"
    menu:
        "Yes.":
            c "W-why are you--?"
            Ip happy bangok blush briefs touch glow flip "No reason."
            
            $ renpy.pause(1.0)

            stop music fadeout 0.5
            stop soundloop fadeout 0.5
            play sound "fx/door/door_open.wav"
            show ipsum normal bangok briefs flip with dissolve
            m "Ipsum yanked his hand away from my crotch and his own as we heard the sound of the door opening. My breath caught, his two shafts stopping, hilted inside of me."

            Lo normal b "Hey Ipsum! I'm home!"
            show lorem think b at right with easeinright
            Lo "Oh, [player_name]? You're here."
            Lo shy b "A-And your clothes are..."
            Lo relieved b "Ipsum, putting [player_name] in one of your swimming briefs doesn't hide that you were doing... things in the living room."
            Ip happy bangok briefs flip "I don't know what you're talking about."
            m "I clenched my fists, left maddenningly close to my edge by his shafts, still filling me."
            Lo "I'll be in the kitchen, putting away some things, starting dinner, and not listening."
            $ renpy.pause (0.3)
            show lorem relieved b flip with None
            $ renpy.pause (0.3)
            hide lorem with easeoutright

            play music "mx/snowflake.ogg" fadein 3.0
            $ renpy.pause (1.5)
            
            Ip normal bangok blush briefs touch glow flip "What say we take this to my bedroom, now?"
            m "My breathing hitched as he gave a short thrust, daring me to make a noise."
            c "P-Probably best."

        "No.":
            stop soundloop fadeout 2.0
            m "Ipsum withdrew his hand from my crotch, then gently let his waistband down, leaving himself hilted inside me."
            Ip "Then we should probably take this elsewhere. Namely, my bedroom."
            m "I panted for breath, my body unwilling to come down from its current high with two shafts caressing my inner walls."
            c "S-Sure."

    $ renpy.pause(0.5)
    scene bangok_four_xipsum_bedroom ceiling:
        alignaround (0,0)
        # pos (0, -456)
        pos (-128,0)
    with wipeleft

    $ renpy.pause(0.3)
    m "Ipsum gathered my clothes and brought them with us as I took unsteady steps toward his room to eventually collapse on his bed."
    play sound "fx/door/close2.wav"
    m "He closed the door behind us."
    show ipsum normal bangok blush flip:
        zoom 1.8
        alignaround (0.5,0)
        xpos 0.18
        ypos 0.6
    with easeinbottom

    m "He sat on the bed next to me, reaching into his waistband again, and into mine."
    play soundloop "fx/bangok_poundofsalt.ogg"
    c "H-Hah."
    m "His shafts slid easily through my holes now, while his lone exploring finger focused on finding and sparking every nerve in my passage's entrance."
    Ip happy bangok heady flip "I'd call this experiment a complete success, wouldn't you?"
    m "He circled just shy of my clit, causing my inner walls to clench and spasm around him."
    c "Y-Yes!"
    Ip normal bangok heady flip "G-Good."
    Ip normal bangok aheago briefs flip "B-Becase I think we're about to--"
    show ipsum happy bangok aheago briefs flip:
        ypos 0.7
    with ease
    stop soundloop fadeout 0.5
    play sound "fx/slap1.wav"
    play sound2 "fx/snarl.ogg" fadein 0.5
    m "He let his waistband snap home with a slap, hilting inside of me, before doubling over and cumming."
    if bangok_four_xipsum2_store.protection == True:
        m "I felt his shafts twitch, delivering his white seed to his condoms' reservoirs deep inside my canal and my ass."
    else:
        m "I felt his shafts twitch, then ropes of warm, white seed sprayed out deep within my canal and ass."

    m "I was so close to release my body acted of its own accord. I caught his legs with mine, pulling his crotch against my nethers, even though we could get no closer than his shafts already were."

    m "His scaly, caressing finger rubbed across my clit, tugging at my stretched lips, and providing the last bit of stimulation I needed."
    show black with dissolve
    $ renpy.pause(0.3)
    c "Ah!"
    $ renpy.pause(0.5)
    hide black
    show ipsum happy bangok blush flip:
        ypos 0.6
    with dissolveslow

    $ renpy.pause(0.8)
    Ip "And there we are."

    if persistent.bangok_inflation == True:
        if bangok_four_xipsum2_store.protection == True:
            m "I placed a hand on my belly, feeling warm and full from the balloons of cum now inflated in my ass and canal."
        else:
            m "I placed a hand on my belly, feeling warm and full from the load of cum now packing my canal and colon."

    m "I let my legs fall away from behind him, and he flicked at one of my feet with his tail."
    if persistent.bangok_knot == True:
        Ip normal bangok blush flip "Now, it'll be a little while before I can pull out--"
        c "Huh?"
        m "He tugged at his waistband, pulling on his cocks, and indicating the thick knots of flesh at the base of each of his shafts that held him inside me."
        menu:
            "H-Hey!":
                c "I didn't say you could do that!"
                Ip look bangok flip "I apologize. I assumed that because it wouldn't affect your ability to leave today, it wouldn't have as great a concern for you."
                c "What do you--"
                show ipsum:
                    ypos 0.7
                with ease
                m "He stepped back, arms spread to show there was technically no direct connection between us, despite his twin cocks resting inside me."
                c "... Huh."
            "Oh.":
                pass
    else:
        Ip normal bangok blush flip "Now, there's no reason for me to pull out immediately."
    Ip normal flip "I wanted to talk briefly about what you'd like to have happen with this."
    c "What do you mean?"
    Ip think flip "Well, the normal rules don't really apply, here. You don't need to be anywhere near the other end to make use of this -- at least so far as I have tested."
    Ip happy flip "That means you could, say, leave this end with me. We could call, or schedule times to use it."
    Ip normal flip "At least until a few days after the fireworks, when I have a distraction planned to slip these back where they came from."
    c "I see."
    menu:
        "Sure, you could keep that end.":
            $ renpy.pause(0.5)
            $ bangok_four_xipsum2_store.shared_with = "ipsum"
            $ bangok_four_xipsum2_store.sharing = 1
            Ip happy flip "Thank you."
            $ renpy.pause(0.3)
            Ip think flip "And, say, what is your opinion on having anyone else have access to it? Say, Lorem?"
            c "I..."
            menu:
                "No. Please don't go lending out my genitals to your roommate.":
                    $ renpy.pause(0.5)
                    Ip happy flip "Spoilsport."
                    Ip normal flip "I jest. Of course I'll keep this just between us."
                    c "Thanks."
                    Ip normal flip "Oh no, thank you. After all, this is going to be quite a bit of fun for both of us."
                "I... suppose.":
                    $ renpy.pause(0.5)
                    $ bangok_four_xipsum2_store.sharing = 2
                    Ip happy flip "Mmhm. And, say, other members of my lab?"
                    menu:
                        "What? No!":
                            $ renpy.pause(0.5)
                            Ip sad flip "I kid, I kid."
                            if bangok_four_xipsum2_store.protection == True:
                                Ip happy flip "Lorem and I are okay, though, yes? With protection?"
                            else:
                                Ip happy flip "Lorem and I are okay, though, yes?"
                            c "I mean, yeah, I guess I said you could. Fine."
                            Ip normal flip "Excellent."
                        "Is that something you can do?":
                            $ renpy.pause(0.5)
                            c "Aren't these supposed to be a secret? And didn't you steal parts to make it?"
                            Ip think flip "Well, yes. But few even know the project exists. And I'd only share this with members of my lab who can keep a secret."
                            menu:
                                "No, thanks.":
                                    c "I'm not comfortable with people I don't even know fucking me."
                                    if bangok_four_xipsum2_store.protection == True:
                                        Ip happy flip "Lorem and I are okay, though, yes? With protection?"
                                    else:
                                        Ip happy flip "Lorem and I are okay, though, yes?"
                                    c "I mean, yeah, I guess I said you could. Fine."
                                    Ip normal flip "Excellent."
                                "Alright. Sounds fun, then.":
                                    $ bangok_four_xipsum2_store.sharing = 3
                                    Ip happy flip "Excellent."
        "I'd honestly like to have both ends.":
            $ bangok_four_xipsum2_store.has_both = True
            Ip think flip "Oh? What for?"
            c "Well, there's someone else I might like to use it with. If, you know, I could..."
            Ip "Few people even know the project exists, so I suppose as long as you're not showing it to anyone directly involved..."
            Ip normal flip "I assume you hadn't heard of it."
            c "Nope."
            Ip "Then you're probably fine to show it to this friend of yours. If you mention it's a secret, and don't mention where it came from, of course."
            c "Of course."
            Ip happy flip "I would like to have details, though, on how you end up using it."
            Ip normal flip "Once I can get some of these by, {i}ahem{/i}, more strictly intended methods, I certainly plan to toy with them frequently."
            Ip happy flip "Hearing others' use cases, you see..."
            m "He trailed off, guaging my reaction."
            c "... Maybe."
        "I... think I'm done, once I take this off.":
            Ip sad flip "Ah."
            Ip normal flip "Well, you had fun with this experiment at least. That was my goal."
            Ip think flip "I'll talk to Lorem about including you in dinner, if you'd like."
            c "Sure. That sounds good."
            Ip happy flip "Excellent."
            Ip normal flip "And, perhaps, another round after dinner?"
            c "Oh, no. I think I'm good."
            Ip "Suit yourself."

    $ renpy.pause(0.5)
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    jump _mod_fixjmp




    jump todo_out_of_content_bangok_four_xipsum2



label bangok_four_xipsum2_ass_split:
    Ip "Are you comfortable trying to fit one or both?"
    menu:
        "One.":
            $ renpy.pause (0.5)
        "Both.":
            $ renpy.pause (0.5)
    jump todo_out_of_content_bangok_four_xipsum2

label todo_out_of_content_bangok_four_xipsum2:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")

