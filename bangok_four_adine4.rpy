label bangok_four_adine4_shower_sceneselect:
    play music "mx/fireplace.ogg" fadein 2.0
    scene black with dissolve
    $ renpy.pause (0.5)
    play sound "fx/purr.ogg"
    $ renpy.pause (2.0)
    c "Is that... are you purring?"
    show adineshower at Pan ((00,608), (00,608), 0.0) with dissolvemed
    stop sound fadeout 4.0

label bangok_four_adine4_shower_purring:
    stop soundloop fadeout 2.0

    if bangok_four_common.bangnokay.check():
        show adineshower at Pan ((00, 608), (400,0), 10.0) with None
        m "Suddenly, her expression changed as she looked over her shoulder."
        Ad think "Oh, are you done? You should take a step back if you don't want to get hit by the water."
        c "I'm fine with getting wet if I take my clothes off."
        show adineshower thinkblush at Pan ((400,0), (400,0), 10.0) with dissolve
        Ad giggle "You don't have to do that, just go ahead and step out."
        c "Are you sure?"
        show adineshower annoyedblush at Pan ((400,0), (400,0), 10.0) with dissolve
        Ad annoyed "Yes, [player_name]. You're in here to help me clean off, not so that I can see you naked or something."
        c "Oh."
        $ renpy.end_replay()
        jump bangok_four_adine4_leave_the_shower

    show adineshower blush at Pan ((00, 608), (400,0), 10.0) with None
    m "Suddenly, her expression changed as she looked over her shoulder. She was visibly blushing."
    Ad think "Oh, are you done? You should... uh, strip so your clothes don't get wet."
    $ renpy.pause (0.5)
    m "It took me a moment to process what she had just asked. But then it hit me."
    c "Wait, was this shower thing an excuse to see me naked?"
    show adineshower thinkblush at Pan((400,0),(400,0),0.0) with dissolve
    Ad giggle "No! Well, not entirely. It really would be hard to wash my back with my shoulder injured."

    menu:
        "I'd rather not.":
            $ renpy.pause (0.5)
            show adineshower think at Pan((400,0),(400,0),0.0) with dissolve
            Ad disappoint "Oh."
            c "Nothing against you, it's just..."
            show adineshower at Pan((400,0),(400,0),0.0) with dissolve
            Ad disappoint "No, no, it's fine. Sorry for, ah, trying to trick you like that."
            show adineshower think at Pan((400,0),(400,0),0.0) with dissolve
            Ad think "You might want to step out if you don't want to get hit by the water."
            $ renpy.end_replay()
            jump bangok_four_adine4_leave_the_shower
        "[[Undress.]":
            $ renpy.pause (0.8)
    play sound "fx/undress.ogg"
    scene black with dissolve
    m "She looked nervous, though that was to be expected given her request."
    if bangok_four_playerhasdick is None:
        menu:
            m "To reassure her, I started removing my clothes and tossing them out of range of the shower, lettinng my..."
            "...erection pop into view.":
                $ bangok_four_playerhasdick = True
                pass
            "...damp hole slip into view.":
                $ bangok_four_playerhasdick = False
                play sound "fx/system3.wav"
                scene black with None
                s "Whoops! This scene presently only has male player content."
                s "Would you like to proceed with this scene as a male, or skip to the end?"
                menu:
                    "Yes, Let me see the scene as a male player.\n(Temporary, will revert after this scene.)":
                        play sound "fx/system3.wav"
                        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                        pass
                    "No, skip to the end.":
                        play sound "fx/system3.wav"
                        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                        stop soundloop fadeout 2.0
                        $ renpy.end_replay()
                        jump bangok_four_adine4_leave_the_shower
    # if bangok_four_playerhasdick == True
    m "To reassure her, I started removing my clothes and tossing them out of range of the shower, letting my erection pop into view in front of her."
    Ad giggle "O-oh! Well, looking good there handsome!"
    play soundloop "fx/shower.ogg" fadein 1.0
    m "I chuckled lightly at her response as she hit a button on the wall, turning the shower head on and coating us both in warm water."
    m "With the water flowing, Adine moved around a bit, quickly washing off all of the suds from my scrubbing. And yet, even when she was clean, the water continued to flow with the two of us standing there expectantly."

    menu:
        "I should step out.":
            Ad think "Are you sure? You look a little, ah, excited. To be sharing a shower with me. You know..."
            menu:
                "I'm good, thanks.":
                    stop soundloop fadeout 2.0
                    $ renpy.pause (0.8)
                    Ad disappoint "Oh."
                    $ renpy.end_replay()
                    jump bangok_four_adine4_leave_the_shower
                "Are you saying you want to do something?":
                    jump .adine_presents_rear
        "Want to taste my dick?":
            jump .oral
        "Mind lifting that rear of yours?":
            jump .adine_presents_rear

    label .oral:
    $ bangok_four_femalepartners += 1
    m "Adine turned around to face me, clearly satisfied with my offer."
    Ad think "I hope you won't be disappointed. I've read tips on how to do this from a magazine, but this would be my first time putting them in practice."
    m "I shook my head and rubbed her cheek reassuringly."
    c "Not a problem, I have full confidence you'll do wonderfully Adine."
    if persistent.bangok_four_skin_color:
        show bangok_four_adine4showerxplayer at Pan((1920, 0), (1100,550), 15.0) with dissolveslow
    m "She playfully nudged me to the ground, before quickly putting her muzzle to use, taking my erection in her mouth and letting her tongue wander along its length."
    c "That eager huh?"
    m "She glared at me in mock indignation, but kept quiet as her oversized maw worked up and down, eliciting gentle huffs and moans from my lips."
    m "I could feel small drops of lubricant leaking out of my tip, followed by the dragon greedily lapping them up."
    m "As she pleasured me with mouth, I noticed her wing go between her hind legs as she started rubbing her own slit needily."
    c "S-sorry for leaving you out dry Adine, I'll make it up to you later."
    m "She grunted in response before letting out a chorus of moans, my own joining hers soon after."
    m "As the water pattered down around us, soaking us both to the bone, I came close to climax. Whatever tips she'd been reading seemed to have paid off."
    m "I reached a hand out to gently stroke her head, letting her know I was having fun."
    m "At the same time however, I was ready to burst and Adine knew it. It was only a matter of seconds."

    menu:
        "Grab her head and cum in her mouth.":
            $ renpy.pause (0.5)
            hide bangok_four_adine4showerxplayer with dissolve
            play sound "fx/extinguish.ogg"
            m "I wrapped both arms around the dragon's head and pulled it down, drawing a shocked gasp from my partner as I flooded her mouth with seed."
            m "There was no resistance however, and she swallowed it as wave after wave of fluids coated her tongue."
            m "After I had been licked dry, Adine's efforts for herself came to fruition, as she squirted into the wall from her own climax, her head reeling back in a loud moan."
        "Lean back and enjoy it.":
            $ renpy.pause (0.5)
            hide bangok_four_adine4showerxplayer with dissolve
            play sound "fx/extinguish.ogg"
            m "I let myself fall backwards, thrusting my hips up as I came. Just before the first drop shot out however, Adine pulled her maw back to let the off-white spunk coat her face."
            m "The water from the showerhead rinsed it off as quickly as it came out, cleaning both of us of the seed as it erupted."
            m "When I'd finished, Adine threw her head back in a loud moan as she climaxed in turn, squirting her own fluids into the wall behind her."

    m "The two of us were left gasping and wet from the experience, though our faces betrayed mutual enjoyment from the experience."
    c "Thanks, that's the best dragon blowjob I've ever had."
    Ad giggle "You're welcome, that's the best dick I've ever tasted."
    m "We laughed together, easily amused by our banter in the post-orgasmic high."
    hide adineshower with dissolve
    $ renpy.pause (0.5)
    scene adineapt2 at Pan ((128, 300), (128,300), 0.0) with dissolvemed
    m "I dismissed myself to dry off, exiting the shower to find a towel to use as Adine turned back to the shower."
    stop soundloop fadeout 2.0
    $ renpy.end_replay()
    jump bangok_four_adine4_when_she_turned_off_the_water_again


    label .adine_presents_rear:
    $ bangok_four_femalepartners += 1
    m "Adine rolled her eyes, though her amused smile betrayed her mock indignation."
    Ad annoyed "Well, I suppose I owe you that much, since I so cruelly decieved you into stripping naked for me."
    m "It was a glorious sight to behold, the different colors perfectly framing a pussy and anus that were begging to be ravaged."
    m "I almost lost track of time, but after a few moments Adine's voice broke the silence."
    Ad think "Well? Are you just going to stare all day or are you going to teach me how humans do it?"

    menu:
        "Fuck her pussy.":
            jump .vaginal
        "Use her ass.":
            jump .anal

    label .vaginal:
    m "I moved in and penetrated her swiftly, drawing a cross between a moan and a purr from her chest. It was wet, and not from the shower."
    Ad giggle "Oh my, so bold of you, nnf, to just take me like that. Are all humans such savages?"
    c "Only if you let us be."
    m "Satisfied with the answer, Adine leaned further forward, pressing her rear back to brace against my thrusts. Though her slit was too large for my human shaft, she seemed more than happy to just be doing this with me."
    m "Or maybe I was bigger than I gave myself credit for. Her hole was enjoyably tight, and her haphazard moans indicated that she was getting off as much as I was."
    c "You're tighter than I thought a dragon would- nnnf, be, given your size."
    Ad think "I don't do- annh, do this often."
    m "Unable to talk through the moaning anymore, we went back to spechlessly enjoying each others' company."
    m "The steady thrusts of my hips slowly consumed my thoughts as I put all of my effort into plowing the angel in my hands."
    m "My grasp on her flank tightened as I drew closer and closer to my orgasm. I was ready far sooner than I had hoped, but the shower head was washing off all lubricant, letting both of us feel each thrust more... stickily."
    m "At least I wasn't alone. Adine was looking back at me expectantly. She was ready too."

    menu:
        "Cum inside.":
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "After a few more thrusts, I started pumping my semen into the beautiful mass of scales before me. The white juice leaked out of her slit as I stuffed her one wave at a time."
            m "Simultaneously, Adine herself came, her pussy quivering as my crotch got soaked in her juice."
            Ad giggle "Fuhh-uhck, I needed that!"
            m "I didn't respond instantly, still pumping diminishing volumes of cum into her. Once I was finally empty though, I gasped out a response."
            c "Yeah, me too. You're gorgeous, you know that?"
            m "Adine giggled, a sort of groggy, exhausted giggle."
            Ad giggle "This would be a funny way to find out humans can get dragons pregnant."
            m "I giggled in turn, equally exhausted from the effort."
        "Pull out.":
            m "I pulled out and stroked my shaft for a few moments. At the same time, Adine reached back to start masturbating with her claws."
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "Barely a second past before we climaxed together, my belly getting soaked from her squirt as ropes of jizz shot out and iced her rump. "
            m "The fluids were washed off quickly by the water, floating down the drain as if nothing had happened. Both me and Adine were gasping like we ran a marathon however, a sure sign that I hadn't just fantasized the whole interaction."
            Ad disappoint "I was kind of hoping you'd finish inside."
            c "Sorry, old habit. It's a crude and ineffective means of birth control in the human world."
            Ad normal "Still, that was fun. We need to do it again some time."
            c "Maybe next time we can try another hole."
            m "Adine quietly pondered the idea, slowly regaining her composure as if she weren't howling in lust moments prior."

    m "After I'd regained my composure, I left the shower, being sure to give Adine a teasing pat on the rump, to which she responded by swatting my own rear with her tail."
    m "I found a dragon-sized towel and dried off with it, before gathering my clothes and getting dressed."
    c "Thanks again for the fun, that was probably the best I've ever had."
    Ad giggle "I should be thanking you, I haven't had an orgasm that good in a while."

    hide adineshower with dissolve
    $ renpy.pause (0.5)
    scene adineapt2 at Pan ((128, 300), (128,300), 0.0) with dissolvemed
    m "I returned to the living room and waited for Adine to finish her business. As it turned out, it didn't take long."
    stop soundloop fadeout 2.0
    $ renpy.end_replay()
    jump bangok_four_adine4_when_she_turned_off_the_water_again

    label .anal:
    m "I moved forward and took her flank in my hands, admiring the feeling of her smooth, wet scales. After a moment, my shaft came to rest near her anus."
    Ad think "H-hang on, that's not-"
    m "I penetrated her with one swift thrust, drawing a confused moan from her jaws. It was tight, squeezing my shaft as I started thrusting in and out like a piston."
    Ad giggle "Oohh, nevermind, keep going."
    c "Enjoying yourself after all then?"
    Ad annoyed "Shut up and fuck big boy."
    m "I gave her hip a couple of gentle pats, wordlessly doing as she said. My thrusts slowly sped up, becoming more forceful as pleasure started eroding my thought processes."
    m "I knew going in that this would be the right hole. Given her size compared to me, I'd assumed her pussy would feel loose. But the way this felt made me second guess it."
    m "She squeezed my shaft with it, pleasuring me far more than I was ready for. Eventually I simply wrapped my arms around her and went crazy, like a monster with prey."
    m "Adine was loving it too however. I could occasionally feel her claws brush my legs as she reached back and feverishly masturbated."
    m "Before long, both of us were ready to cum, eager to partake in orgasmic bliss."

    menu:
        "Cum inside.":
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "After a few more thrusts I found myself pumping her ass with my seed, followed soon by Adine's own orgasm coating my legs."
            m "We were both gasping and ragged, having spent more energy than we'd noticed. After a few spurts, I'd finally emptied my full load into her."
            m "Savoring the feeling for a moment, I eventually pulled out, sitting on the floor and admiring the view."
        "Pull out.":
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "I pulled my shaft out just before I orgasmed and started stroking it, shooting ropes of white spunk around her rump just as Adine herself came, squirting my legs with her fluids."
            m "All of it washed off quickly in the active shower, leaving both of us gasping for ragged breaths."
            m "I eventually fell back, sitting on the floor to gather my stamina back up as the water washed soothingly down around us."
    Ad think "Hah, that wasn't as bad as I expected."
    c "What, have you not done that before?"
    Ad think "Nope. I'd expected it to hurt so I just avoided it."
    c "Well, good thing I'm smaller than a dragon huh?"
    Ad giggle "It's not the size that counts you know!"
    m "I stood up and gave Adine a gentle kiss on her muzzle. She was caught off guard, but quickly accepted it, returning the favor until I withdrew."
    c "Well thanks for the fun time. I'm gonna dry off quick, alright?"
    Ad normal "Go ahead, I've gotta wash myself again. Not the back this time though!"

    hide adineshower with dissolve
    $ renpy.pause (0.5)
    scene adineapt2 at Pan ((128, 300), (128,300), 0.0) with dissolvemed
    m "I took the smallest towel I could find, which was still big enough to be a blanket for me, and dried myself off before stepping aside to wait for Adine to finish up."
    stop soundloop fadeout 2.0
    $ renpy.end_replay()
    jump bangok_four_adine4_when_she_turned_off_the_water_again
