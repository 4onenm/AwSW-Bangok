init python:
    bangok_anoney_xemera2_set_condition = False
    bangok_anoney_xemera2_clean_arms = None
    bangok_anoney_xemera2_refuse_participate = False
    bangok_anoney_xemera2_lick_slit = None
    bangok_four_xemera2_ws_mouth_unasked = True

$ mp.emeraromance == True #must have done massage in xemera to proceed.

label bangok_anoney_xemera2_set_condition:
    $ bangok_anoney_xemera2_set_condition = True
    jump bangok_anoney_xemera2_set_condition_return

label bangok_anoney_xemera2_answ_machine:
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.5)
    Em "Hello [player_name]. Excuse the late message."
    Em ques "It has been rather a long day having just had a planning meeting for the festival happening soon."
    Em laugh "That massage you gave me last time was amazing. I had never felt so good."
    Em frown "But between the festival and situation with your fellow ambassador, all this bureaucracy is taking its toll."
    Em ques "I would like to request another session with those wonderful hands of yours."
    Em normal "I will be in my office at the library late tonight and tomorrow. I do hope you can make it."
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.8)
    c "(The Minister of Culture and Arts wants an evening date with my hands. Obviously I left a good impression.)"
    jump ml_answeringmachine_end


label bangok_anoney_xemera2_emera:
    stop music fadeout 2.0
    $ renpy.pause (0.5)
    scene black with dissolvemed
    $ renpy.pause (0.5)
    play sound "fx/steps/clean2.wav"
    scene bangok_four_library night at Pan ((60, 228), (0,228), 2.0) with dissolveslow

    m "The library was quiet this evening."
    c "(I guess everyone already has their late-night reading material.)"
    m "As I went past an isle, I saw Remy with his head buried in a large box, evidently searching for a trinket of some kind to further his research."
    m "I continued toward the private area of the library where I had been before on my last visit."

    scene black with dissolvemed
    $ renpy.pause (0.5)
    scene bangok_anoney_library_corridor_night with dissolvemed

    m "Finding the door with the name Minister for Culture and Arts on it, I knocked."

    play sound "fx/knocking1.ogg"

    $ renpy.pause (2.0)

    Em "Come in."

    play sound "fx/door/door_open.wav"

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night with dissolvemed

    $ renpy.pause (3.3)

    play sound "fx/door/close2.wav"

    show emera laugh b with dissolve

    play music "mx/eveningmelody.ogg" fadein 2.0

    Em "Hello [player_name]! It's so nice to see you again. I wasn't sure if you would have the time, considering the extensive police investigation at the moment."

    c "Well I needed a break from the constant police work. It wasn't what I had intended to be my full time job when I stepped through the portal. Besides, being an ambassador means experiencing the stories of all the dragons that make up society."
    Em ques b "I see. I am pleased that you would consider me one of the dragons to experience. All too many times I feel that I am brushed off as just another high-up, pompus, dismissive dragon that needs to pretty herself up with body paint and jewlery to make herself feel important."

    menu:
        "Snicker.":
            c "(Funny, that is exactly what I think of you.)"
            Em frown b "What was that?"
            play sound "fx/throat clear.ogg"
            m "I coughed to try to cover up my faux pas."
            c "Sorry just clearing my throat."
        "Flatter.":
            c "You are a very important politician being brought up from a well-off family and you don't work in an active lifestyle."
            c "So why should you not wear jewlery or scale paint to project your status?"
            Em "Precisely. How else am I to conduct these stressful and complex negotiations without stating my authority?"
    Em ques b "If the Chief of police is able to wander around with a large badge on his chest to exemplify his authority, why am I frowned upon for flaunting my status in the same way?"
    Em "Ah Bryce, the only viable partner for me this far away from the city."
    c "What makes you think that?"
    Em normal b "Well, he is an Earth dragon, the same as me."
    Em ques b "He is loyal and copes with a large workload."
    Em normal b "It is a shame about the scar on his throat; that is something Horn Shine could never cover up. But, as with diamonds, the most exquisite stones are those with imperfections."
    if brycescenesfinished >= 1 and not leftbryce:
        c "(Obviously she has never seen Bryce staggering out of the bar at closing time.)"
    elif katsuavailable or (katsuunplayed == False):
        c "(I wonder if bringing up that dragon I met, Katsuharu, would be a bad idea.)"
    else:
        c "(She does have a point; I have not seen many other Earth dragons about.)"

    Em "Anyway, enough of the chit chat. On to the reason why I left you that message."
    Em "I assume you can still remember the technique I from last time?"
    m "I nodded."
    Em ques b "Good."

    scene black with dissolvemed

    $ renpy.pause (0.5)

    show bangok_anoney_emeramassage_night at Pan((960, 250), (960, 0), 6.0) with fade

    $ renpy.pause (3.0)
    play sound "fx/sheet.wav"
    m "As before, she produced the same mat and pillow and proceeded to lay with her back toward me."

    m "I knelt beside her on the edge of the mat and started massaging the scales on her neck, being careful to keep my arms out of the way of the spines on her head. After my close shave last time, I had no desire to experiance a repeat performance."

    Em laugh b "Ah yes, yes. So good."

    m "As I moved onto her shoulder she leaned into my ministrations, reminding me of the cats that people used to keep in the old world."

    c "Do you keep this mat and pillow here just for massages?"

    if (persistent.nsfwtoggle == False) or bangok_four_common.bangnokay.check():
        jump bangok_anoney_xemera2_massage_only
    else:
        pass # Onward to lewds!

    Em frown b "Actually, no that is not the only use I have for them. It is a rather personal and private reason."

    c "Oh?"

    Em ques b "You are probably not one to know unless you have read a textbook on dragon biology."
    Em normal b "Female Earth dragons go into ovulation about every 3 months or so. Even if the egg is unfertilized it will stay within the egg chamber for some time after the hard shell is formed."
    Em frown b "Of course, the body will eventually pass the egg when the next cycle starts. Though, obviously, having an unsceduled egg laying could be highly embarassing, even dangerous."

    if persistent.bangok_cervpen:
        Em "Fortunately, our creation process, whatever it may be, found a way to control the timing of the laying in us Earth dragons."
        Em "If mating occurs where the head of the male penis pushes into the egg chamber, the body will bring forwards the next cycle and it will start the laying process"
    else:
        Em "Fortunately, our creation process, whatever it may be, found a way to control the timing of the laying in us Earth dragons. If mating occurs, the body will bring forwards the next cycle and it will start the laying process"

    m "I pushed my upper body up to be able to reach the hard plates on her back and use my weight on the muscles beneath."

    Em ques b "Due to the fact I currently have no male partner to take care of my needs and due to concerns anyone else I might ask may try to blackmail me or want political favors, I usually take care of things myself; having a pleasure stick that I use modeled on an earth dragon's tool"

    Em mean b "Given your current status as an ambassador, it means you are not embedded in the usual dragon politics and your job requires you to maintain good relations with myself and others of the council."

    Em ques b "There is also a more personal reason:{w=0.2} Those hands of yours work magic on my outside, and I am intrigued if they will be just as magical working on my insides."

    menu:
        "Accept.":
            pass

        "Reject.":
            $ bangok_anoney_xemera2_refuse_participate = True
            c "I didn't expect to be performing intimate duties, I thought this was going to purely be a massage, given you admit that you take care of yourself anyway I refuse to take part."
            Em frown b "I see, I guess it was foolish on my part for thinking that you would be interested in one of the most important bonding ritules of our people"
            m "I quickly moved around to her rear, now working on her hips and rump."
            m "The rest of the massage happened in silence. The words that she had said had rattled my core. What with investigating the murders and also needing to get the generators to save humanity, being asked to give pleasure to a politician was too much."
            m "(I know that this massage is not as good as my first one, I can only hope that this will not have detrimental impacts on human dragon relations.)"
            jump bangok_anoney_xemera2_conclusion

    if bangok_four_anna2.annacame == True:
        c "(Having experienced firsthand exactly what magic my hands could do for Anna, I was confident that I could please her.)"
    else:
        c "(Not having experience with a female, yet I decided to just trust in my judgement that, just as she guided me through her massage, she will let me know what feels good for her.)"

    # TODO: Start pan down
    m "I moved around to her rear, now working on her hips and rump."

    Em laugh b "Yes, yes! That feels so good. Oh how I am going to miss having this performed when you eventually go back through the portal."

    m "All that was left to do was her tail. I started at the tip, then moved slowly down closer to her body. Given my hands would be seeing plenty of action tonight, this time I could massage areas that had been neglected before as my hands found themselves around the base of her tail."

    m "After finishing the massage, I got up to stretch my legs, realising that it would be best not to have anyone walk in on us, I went over to the door, slid the room status plate to Engaged and locked it."
    $ renpy.pause (3.0)
    play sound "fx/door/handle.wav"
    $ renpy.pause (1.5)
    play sound "fx/door/lock.ogg"

    m "I pulled the blind down over the window. The last thing Emera could want is for any of the other dragons to know that she was having intimate relations with a human."
    $ renpy.pause (3.0)
    play sound "fx/envelope.wav"

    m "Turning back from the door, I decided to undress, given the activities for the evening had the potential to be messy."
    play sound "fx/zip.ogg"
    $ renpy.pause (1.5)
    play sound "fx/undress.ogg"
    Em laugh b "How exotic. I always wondered what was under the cloth layers that you wear."
    Em ques b "I am sorry but we were not sent any information on gender identifying features; what form of genitalia do you...?"

    menu:
        "Male.":
            $ bangok_four_playerhasdick = True
            if persistent.bangok_cloacas == True:
                Em mean b "Fascinating you have your mating tool just dangling out like that. It looks so small and shriveled and floppy. Do you not have a slit to protect it? And I do not see your anal vent either..."
                c "We don't have cloacas, so our genetalia and anal openings are kept seperate."
            else:
                Em mean b "Fascinating you have your mating tool just dangling out like that. It looks so small and shriveled and floppy. Do you not have a slit to protect it?"
                c "No, we do not have slits for our genitals."

        "Female.":
            $ bangok_four_playerhasdick = False
            if persistent.bangok_cloacas == True:
                Em "Fascinating, but I believe I spotted two openings in between your legs?"
                c "We do not have cloacas. Our genetalia and anal openings are seperate."

    m "I gestured to my clothes."
    c "We also wear clothing, a substitute for scales used to protect our bodies, including our genitals, from damage and to retain heat."

    c "Unlike for dragons, removing our clothing and exposing ourselves is an activity done only with those that we want to be intimate around, or for bathing."

    c "Before we begin with the more \"physical\" activities, it is common in human culture to provide stimulation for both partners, to further the bond that is shared and to get the couple prepared for intercourse."
    Em ques b "Ooh a human ritual, It has been theorised how humans could have been romantic. I had never thought to experiance anything like it in reality."
    c "Would you be able to sit on your sofa with your legs apart? This should be the more comfortable position for you than doing this on the floor."
    Em laugh b "Of course. I am most curious what you intend to do. We have had plenty of physical contact already thanks to your massage, and we dragons are hardy enough to get straight to the action without needing preparation."

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emera_sofa:
        yalign 1.0
        linear 2.0 yalign 0.0
        yalign 0.0
    with dissolveslow

    play sound "fx/bed.ogg"
    m "Emera got up from off the floor and sat on her sofa."
    show bangok_anoney_emera_sofa:
        yalign 0.0
        linear 1.0 yalign 1.0
        yalign 1.0
    $ renpy.pause (0.5)
    m "I moved her pillow over and sat on it, facing her groin."
    play soundloop "fx/purr.ogg" fadein 1.0
    if persistent.bangok_cloacas == True:
        m "I rested my hands on her groin and started to rub the small scales surrounding her single vertical slit."
    else:
        m "I rested my hands on her groin and started to rub the small scales surrounding her slits."
    play sound ["fx/rub1.ogg", "fx/rub1.ogg", "fx/rub1.ogg", "fx/rub1.ogg", "fx/rub1.ogg", "fx/rub1.ogg", "fx/rub1.ogg", "fx/rub1.ogg", "fx/rub1.ogg"]
    Em laugh b "That tickles, but in a good way, dragon paws are not best suited due to our claws and limited dexterity, at least for those that use them for walking."
    m "Emera gently rested her front paws on my head and ran her claws through my hair."

    if bangok_four_playerhasdick == True:
        Em normal b "Your fur on your head is so strange. Although fur is present on some of the more exotic spcicies it is normally short and stiff and stands up by itself."
    else:
        Em normal b "Your fur on your head is so strange. Although fur is present on some of the more exotic spcicies it is normally short and stiff and stands up by itself. I did not realise humans let their hair grow so long. It is different to that of the other ambassador."

    c "What you call fur, is hair it is made of keratin similar to the your claws, just obviously much thinner."
    m "I let out a chuckle. The movement of her claws through my hair made me wonder if this is what those metal head massagers that I had seen in a museum one time would have felt like."
    Em ques b "I am not hurting you am I?"
    c "No. It's fine. Back in older times on earth we used to have these many pronged, metal sticks, where the prongs would be spread over the head and the stick moved about to massage the head. I saw one in a museum some years ago."

    if persistent.bangok_cloacas == True:
        m "Emera's slit had started to spread, showing her pink insides along with a sheen of her arousal. I could feel the area around it becoming warmer due to the increased blood flow."
        m "Reaching forwards I hooked my thumbs into the walls of her slit and pulled them apart."
    else:
        m "Emera's upper slit had started to spread, showing her pink insides along with a sheen of her arousal. I could feel the area around it becoming warmer due to the increased blood flow."
        m "Reaching forwards I hooked my thumbs into the walls of her upper slit and pulled them apart."

    m "The slit spread appart easily, showing great elasticity."
    c "(I guess the male may not be in the optimal position so some flexibility would be needed to make sure he can still penetrate successfully.)"
    c "(Or perhaps the dragons were created with such elasticity to be able to accomodate other dragon species, within reason.)"
    menu:
        "Lick.":
            $ bangok_anoney_xemera2_lick_slit = True
            m "I bought my mouth close to her spread slit and started to run my tounge over what I could reach of the inner walls."
            c "(The texture of her walls were smooth as expected yet they also felt both dense and malleable, similar to a dense but compressible polymer.)"
            c "(The smell being this close to her was pungent. I could only imagine what effect it must have on a dragon with a higher sensitivity.)"
            m "Emera's legs gave an involuntry buck at the feeling of my toungue on her inner folds."
            m "Emera moved her head around checking both sides in case her movements had injured me."
            Em frown b "Sorry about that. I am not used to feeeling such a texture of your toungue on my sensitive area. You are not hurt?"
        "Finger only.":
            $ bangok_anoney_xemera2_lick_slit = True
            m "I let my fingers roam the opening of her spread slit, massaging what I could reach of the inner walls without going more than a couple knuckles deep."
            c "(The texture of her walls were smooth as expected yet they also felt both dense and malleable, similar to a dense but compressible polymer.)"
            c "(The smell being this close to her was pungent. I could only imagine what effect it must have on a dragon with a higher sensitivity.)"
            m "Emera's legs gave an involuntry buck at the feeling of my fingers on her inner folds."
            m "She moved her head around, checking both sides in case her movements had injured me."
            Em frown b "Sorry about that. I am not used to feeeling such a texture of your smooth fingers on my sensitive area. You are not hurt?"

    m "I shook my head as I continued to explore her slit."

    Em ques b "Oh, I could just sit like this with you down there for ever. Have you perhaps had any more thoughts about becoming my assistant once all this ambassador business wraps up?"
    m "I pulled back from her slit to take a few breaths and answer her question."
    c "I do not think it would be wise to do that. As much as it would be fascinating to learn more of dragon culture, you have said before you wish to start a family."
    c "I can't give you a family, and I would not want to come between you and your future mate, once you have found a suitable suitor."
    if bangok_anoney_xemera2_lick_slit:
        m "I resumed my oral exploration of her slit. Her arousal was in full swing. My face was covered in her juices, with the excess starting to drip and form a small puddle on the floor."
    else:
        m "I resumed my exploration of her slit. Her arousal was in full swing. My hands were almost covered in her juices, with the excess starting to drip and form a small puddle on the floor."

    m "Emera took a deep breath and glanced at the ceiling, analyzing my response and no doubt having an internal argument over how to reply."
    m "After a few moments she brought her head back down and exhaled with a sigh."
    Em "You are right of course. I am so used to getting what I want that I do not fully think through the consequences of my wants."
    stop soundloop fadeout 0.5      #stop purr sound, 58 seconds long, maybe change to loop if going to spend longer then min on this scene?
    if bangok_anoney_xemera2_lick_slit:
        Em bangok blush b "I think I am ready enough to proceed, a desire has built further down my tunnel out of reach of that toungue of yours."
    else:
        Em bangok blush b "I think I am ready enough to proceed, a desire has built further down my tunnel out of reach of those fingers of yours."
    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emera_presenting

    $ renpy.pause (3.0)
    play sound "sheet.wav"
    if persistent.bangok_cloacas == True:
        m "Emera returned back to the mat, laying her head on her pillow. Unlike earlier, she lifted her rear and stood on her hind legs, spread wide to show the single vertical slit between them."
        m "The scales around it had a glisten in the light that was definitely not from scale shine. Clearly my foreplay had gotten her in the mood."
    else:
        m "Emera returned back to the mat, laying her head on her pillow. Unlike earlier, she lifted her rear and stood on her hind legs, spread wide to show her slit and ass between them."
        m "The scales around the larger vent had a glisten in the light that was definitely not from scale shine. Clearly my foreplay had gotten her in the mood."

    m "Emera gestured with her paw to a cabinet behind me."
    Em normal b "You will find lube and other supplies you may need in there."
    show black with dissolvemed
    play sound "fx/cabinet.ogg"
    m "I went to the cabinet that Emera indicated and opened the door."

    # if persistent.havetestresults == True:
    #     Em ques b "I have seen your test results. The data said that there was no issue with our sexual compatability, so using protection isn't strictly necessary."
    # else:
    #     Em ques b "There is protection available if you want to use it. Given I am an Earth dragon, we are meant to be tough, so I doubt I could catch anything from you."

    Em ques b "There is protection available if you want to use it."
    if bangok_anoney_xemera2_lick_slit:
        Em laugh b "Though, given your oral exploration of my anatomy, I think we are well past that now."

    m "I had a look at the contents of the cabinet. There was a bottle of lube as well as a pack of smaller condoms. Stuffed in the back corner I could see what looked like pack of rubbers for large dragons."

    if bangok_four_playerhasdick == True:
        menu:
            "Use protection":
                m "I opened one of the small condom packets and rolled it over my dick."
                $ bangok_anoney_xemera2_protection_dick = True

            "Go raw.":
                $ bangok_anoney_xemera2_protection_dick = False
    else:
        m "I saw the pleasure stick that she referred to for pleasing herself on the shelf below."
        c "(Maybe I could give that a try later...)"


    if chap2storehealth == True:
        menu:
            "Seeing the large condoms in the back reminded me of something I had thought earlier":
                    $ bangok_anoney_xemera2_clean_arms = True
                    play sound "fx/unwrap.ogg"
                    m "I remembered seeing the size of the larger dragon condoms in the grocery store and, realizing that things will probably get messy, I dug out two of the larger sized condoms from the back of the cabinet and then put them on my arms. They were ribbed part way down and should provide Emera even more pleasure"
                    m "Grabbing the lube, I returned to Emera and knelt in front of her spread legs."
            "Just grab the lube":
                if bangok_anoney_xemera2_protection_dick:
                    m "Grabbing the lube, I returned to Emera and knelt in front of her spread legs."

    if persistent.bangok_four_playerhasdick and (not bangok_anoney_xemera2_protection_dick) and (not bangok_anoney_xemera2_clean_arms):
        m "Ignoring the condoms, I grabbed the lube and returned to Emera to kneel before her spread legs."
    else:
        m "Grabbing the lube, I returned to Emera and knelt in front of her spread legs"


    if persistent.bangok_cloacas == True:
        m "Using my thumb and fingers to spread her slit, I squirted some of the lube into her cave. She let out a purring sound and shivered at the sensation of the cool lube in her enterence, though it quickly warmed up to her body temperature."
    else:
        m "Using my thumb and fingers to spread her upper slit, I squirted some of the lube into her cave. She let out a purring sound and shivered at the sensation of the cool lube in her enterence, though it quickly warmed up to her body temperature."

    m "For good measure, I also squirted some lube into my hand then began to spread it around both my hands and arms."

    if bangok_anoney_xemera2_clean_arms == True:
        Em laugh b "Oh, I had forgotten that those were left in there."
        Em ques b "I am most impressed with your initive and can't wait to feel that ribbing."
        Em laugh b "Now get that arm in me."
    else:
        Em laugh b "Well, looks like you are all prepared. Now get that arm in me."

    m "Folding my thumb into my hand and bringing my fingers to a point, I gently pushed my right arm into the her lubed slit."

    if persistent.c4eggs == True:
        m "I had seen some dragon eggs before at Raza's hideout and even though I had not directly seen her own eggs I had a feeling hers would be larger than my hand."
    else:
        m "I had not seen dragon eggs before, but I had a feeling hers would be larger than my hand."
    play sound "fx/varagrowl"
    m "Emera let out a snarl at the feeling of my hand entering her. She was able to take my whole hand easily due to the size difference."
    if persistent.bangok_watersports == True:
        m "Just past the enterence on her upper wall I could feel an opening and guessed this was her urethra. I noted where it was to investigate it later."

    m "I continued to feed my arm into her, gently rocking it in."
    m "There was plenty of lubrucation from her arousal as well the extra lube I had rubbed over my arm before entering."
    m "I decided to ball my fingers into a fist to immitate the head of a dragon's cock.{w=0.1}{nw}"
    play sound "fx/purr.ogg"
    m "I decided to ball my fingers into a fist to immitate the head of a dragon's cock.{fast} Emera instantly let out a purr and shivered in pleasure."

    if bangok_anoney_xemera2_clean_arms == True:
        m "My arm slowly disappeared up to my elbow and there was still length in her tunnel yet. With the condom covering halfway up my upper arm it gave me a good indication of how much there would be to her depths. By now the ribbed texture of the condom was starting to enter her."
        Em laugh b "That feels amazing, it feels so much better to have something warm and living down there instead of awkwardly trying to push in a poor substitute, and the texture on the condom feels divine."
    else:
        m "My arm was slowly disappearing up to my elbow and there was still length in her tunnel yet."
        Em laugh b "That feels amazing, it feels so much better to have something warm and living down there instead of awkwardly trying to push in a poor substitute."

    if persistent.bangok_cervpen == True:
        m "After only another minute of slowly, gradually pushing, I finally reached the limit of her tunnel, beyond which was her egg chamber."
    else:
        m "After only another minute of slowly, gradually pushing, I finally reached the limit of her tunnel, with the majority of my arm inside her."
        Em frown b "Nngh. Yes, that is as deep as you can go."

    m "Now I knew how much length I had to work with I slowly began to withdraw my now soaked arm from her tunnel. when most of my arm was out, I pushed it in again once more and set up a rhythm."
    play soundloop "massage.ogg"

    $ renpy.pause (3.0)

    if bangok_four_xipsum.unplayed == False:
        if bangok_four_xipsum_vag_and_ass:
            c "I understand that part of your studies in culture, would also include the mating rituals of dragons. I have had the chance to have an encounter with a dragon with a pair of hemipeni. When mating happens are they both in use with one in each hole?"
            Em frown b "Do you really need to know the answer now of all times?"
            Em ques b "To satisfy your curisity; although it is unusual to find a dragon with such an abnormality."
        else:
            c "I have had an encounter with a dragon that had 2 hemipeni and have had both passages filled. It was quite a heavenly experience."
            Em ques b "Indeed? It is unusual to come across a dragon with such an abnormality."
        Em ques b "However, there have been records indicating that they did indeed use both passageways to enter the female and that it was highly pleasurable for both partners."
        c "How would you feel about having an experiance similar to what is in your records?"
        Em bangok blush b "You can do that?"
        menu:
            "Let me work my magic.":
                jump bangok_anoney_xemera2_double_fisting
            "On second thought, maybe it is best to carry on as planned.":
                jump bangok_anoney_xemera2_vaginal_only
    else:
        jump bangok_anoney_xemera2_vaginal_only

label bangok_anoney_xemera2_vaginal_only:
    if persistent.bangok_cervpen == True:
        m "Reforming my hand into a point again, I began to put pressure at the end of my stokes onto the centre of the rear wall of her tunnel"
        Em bangok blush b "You need to go faster. Faster and harder. Put your body into it."
        stop soundloop
        play soundloop "fx/massage2.ogg"
        m "Gradually I could feel the barrier yielding and a hole starting to open up."
        play sound "fx/varagrowl"
        Em "Don't stop now, [player_name]. Give it all you got!"
        m "Over the next few minutes the hole widened even more, until eventually my hand pushed through."
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I broke through into her egg chamber. I could feel the smooth hard surface of her egg held within her inner castle."
        stop soundloop fadeout 0.5
        m "I stopped moving my arm with my hand in her egg chamber, just moving around the egg."
        play sound "breathing.ogg"
        m "Emera panted needily."
        Em "Why did you stop?"
        play soundloop "massage2.ogg"
        m "I smoothly withdrew my arm until my fist was at her entrance and punched it through her tunnel back into her egg chamber."
        Em "More, More!"
        m "I quickly picked up the pace, pushing my arm deep each time, touching the egg with my knuckles."
        $ renpy.pause(0.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        play sound "fx/bitescr.ogg"
        $ renpy.pause(0.8)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar as I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier once there had disappeared; the entrance had dilated completely"
    else:
        m "I began to move my fist around inside her, stimulating her walls around the entrance to her egg chamber"
        Em bangok blush b "You need to go faster. Faster and harder, put your body into it."
        stop soundloop
        play soundloop "fx/massage2.ogg"
        m "Over the next few minutes, her tunnel gradually got looser. I could speed up my thrusts, making sure to move my wrist each time I kissed the entrance to her egg chamber with my knuckles."
        play sound "breathing.ogg"
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I found a particularly sensitive area near the end of her tunnel. I angled my hand so that I would continually rub this area each time I plunged my arm back in"
        $ renpy.pause(0.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        play sound "fx/bitescr.ogg"
        $ renpy.pause(0.8)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar as I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier that until a few moments ago was at the end of her tunnel rapidly disappeared, the entrance dilating completely."

    m "Her tunnel clenched so tight around my arm that I could no longer move it, her opening spraying copious amounts of lubrication all over my lower body and genitals."

    if persistent.bangok_watersports == True:
        m "I suddenly felt a much warmer and wetter fluid surrounding my arm. Given the position Emera was standing, I was glad that it was moving further inside her instead of streaming out onto the floor and embarassing her."
        m "She didn't mention that the laying hormones also made her lose control of her bladder, though it could be an evolutionary trait to provide more lubrucation for the egg."
        m "I was equally glad I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    else:
        m "I am glad that I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    m "After what felt like several minutes I felt her tunnel relaxing. Though I could still feel pulses along the sides of her tunnel, now they were going in the opposite direction."
    m "Emera was breathing heavily as she spoke to me again."
    Em bangok blush b "Thank you for that. You have done it. My egg is now going to be starting its journey out of me, and for the first time I can enjoy it."
    Em "You have already done so much for me by getting this far, but I would ask you to do more."
    Em "The hormones that are released to prepare to lay the egg severely limit any discomfort I would experiance from the egg passing out."
    Em "There is something that I have always wanted to try after reading about it in our records, but have not been able to do, because of my lack of a partner or flexible enough tail."
    Em "When the egg is travelling down my tunnel, are you able to stop it before it comes out and push it back?"
    c "If that is what you want."
    m "I pulled my arm back until just my hand remained inside and I could see the muscles around her groin area working to push the egg down her tunnel."
    m "The look of rapture on the dragon's face confirmed that she was as high as a stunt-performing flyer."
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers. I held the egg for a moment while her contractions passed, then I drove my arm back into her slick canal."
    if persistent.bangok_cervpen == True:
        m "The copious lubrication meant it was easy to push the egg back in. I pushed it back, deep inside her, until I could feel my hand slipping it through the still-dilated entrance to her egg chamber."
    else:
        m "The copious lubrication meant it was easy to push the egg back in. I even went further then before given the enterence to her egg chamber was still dialated."
    play sound "fx/bitescr.ogg"
    m "It didn't appear to cause her any discomfort. In fact, there was another muffled roar as another set of bite marks were added to the same cushion used before."
    m "I could feel her tunnel spasm around my arm, almost in confusion as the instinct to draw the male fluids to the egg chamber was competing with the signals from her egg chamber that is currently occupied in trying to evict the egg."
    m "Some moments later, her tunnel again went limp and I moved my hand back to the beginning to prepare to go again."
    m "I repeated the operation five more times before my arm was starting to get tired. I removed it from her and finally allowed her body to expell her egg."
    $ renpy.pause (1.5)
    play sound "fx/bitescr.ogg"
    $ renpy.pause(0.8)
    play sound "breathing.ogg"
    m "Emera panted heavily, her body still in the throws of her orgasms."
    Em bangok orgasm b "That was amazing. Those old records were not wrong when they recorded their observations."
    play sound "fx/slurp.ogg"
    m "I caught the egg in my hands as it fell from her slit. I was suprised by its weight and size: about as large as a melon. The color was a pale yellow, nearly matching her belly."
    c "What will you do with the egg now?"
    Em ques b "Usually I donate it to a charity in the city. They have an anomynous drop off box here at the library."
    Em "They extract the contents of the egg, fill it with a dense foam then paint designs on the shell, with the eggs then sold as souvenirs, presents and the like."
    Em normal b "The profits gained are then shared with orphanages and counciling for low income families all over."
    Em frown b "The level of pleasure that is had by both partners from encoraging the beginning of the cycle can fuel an addiction."
    Em "The concequences of which are seen in the large range of contraceptives, you must have seen them at the local grocery store and unfortunately in the unwanted fertilized eggs that are sometimes also left in the donation box."
    c "Really?"
    Em normal b "Of course any eggs left in the box at the end of the day are checked by simply shining a light through them. Given the shells are slightly transleucent, it is possible to tell if they are viable or not."
    m "I carefully placed the egg down onto the mat before it could slip out my hands."

    menu:
        "I wonder if I can fit both my arms in...":
            pass
        "Ask to be satisfied." if bangok_four_playerhasdick == True:
            jump bangok_anoney_xemera2_satisfy_male
        "Ask to borrow Emera's pleasure stick." if bangok_four_playerhasdick == False:
            jump bangok_anoney_xemera2_satisfy_female
        "Just finish up.":
            jump bangok_anoney_xemera2_toweling_showercomment_conclusion
    c "Emera, there is something new I wish to try. You found the experiance of one of my arms inside you was amazing. Now that you have laid your egg, how about both arms?"
    Em laugh b "Let's try."
    m "I pulled the mat over to a wall, then knelt down against the wall facing her, bought my arms together, and twined my fingers together."
    c "You will need to do the work, I can't brace against you with both my arms inside."
    m "Emera backed up slowly until my clenched hands were under her tail."
    if persistent.bangok_cloacas == True:
        m "I lined up my arms with her cloaca, which was still swollen and spread from passing the egg."
    else:
        m "I lined up my arms with her vaginal slit, which was still swollen and spread from passing the egg."
    $ renpy.pause (1.5)
    play sound "fx/varagrowl.ogg"
    m "Emera leaned back until she forced my hands into her slit."
    Em blush b "Yes, I feel that now. Both your arms together will be larger then any dragon cock."
    m "Emera continued to lean back, pushing more and more of my arms into her."
    Em "Gosh your arms are so big when pressed together like that."
    m "She continued to back up until my elbows entered her slit."
    play soundloop "fx/massage.ogg"
    m "Emera started to rock her body back and forth, sliding my arms up and down her tunnel."
    Em "So, so big, it is like the egg yet all the way along."
    m "Now that she had gotten used to my arms inside her she decided to push even harder."
    play sound "fx/varagrowl.ogg"
    m "I could feel more of my arms sliding inside as her slit stretched even further."
    play soundloop "fx/massage2" fadein 0.5
    m "Emera sped up but did not move as far, keeping my forearms within her warmth."
    Em "Almost there...., nearly at the end of my tumnnel, just a little further"
    m "I can feel her tunnel starting to clamp down. Emera really had to put some effort into forcing me through her passage."
    play sound "breathing.ogg"
    $ renpy.pause (7.0)
    m "Finally Emera gave one last shove back and my arms reached the end of her tunnel."
    play sound "fx/roar2.ogg"
    Em orgasm b "Words... so... full"
    m "Her tunnel clamped down, hard. As I was trapped between her and a wall, frozen in place, I could do almost nothing but enjoy the sight of the dragon in the throes of the longest orgasm she had ever experianced."
    m "I did what I could, which was to wiggle my arms to prolong her pleasure."
    m "A fresh flood of juices spurted out around my arms, spattering my chest in the fresh, warm liquid."
    m "Finally, after what felt twice the length of her previous orgasms, her tunnel finally relaxed, her legs become weak and she tumbled to the mat on her side, pulling me down too."
    play sound "breathing.ogg"
    m "After minuites of laying on the mat, my arms still trapped within her passage, they were starting to ache."
    c "Emera, could you move forwards so I can pull my arms out?"
    Em blush b "Oh of course. Apologies, I don't know what came over me. The pleasure was just so, so very good and then I just felt so weak, I couldn't continue standing."
    m "She began to move forward, slowly pulling my arms out of her slit, leaving a trail of her juices on the mat beneath them."
    play sound "fx/varagrowl"
    m "She let out a snarl as my hands finally left her now thoughly abused slit."
    Em "Words cannot describe how good that felt."

    menu:
        "Ask to be satisfied." if bangok_four_playerhasdick == True:
            jump bangok_anoney_xemera2_satisfy_male
        "Ask to borrow Emera's pleasure stick." if bangok_four_playerhasdick == False:
            jump bangok_anoney_xemera2_satisfy_female
        "Just finish up.":
            jump bangok_anoney_xemera2_toweling_showercomment_conclusion

label bangok_anoney_xemera2_toweling_showercomment_conclusion:
    play sound "fx/cabinet.ogg"
    $ renpy.pause (0.5)
    play sound "fx/rubb2.ogg"
    m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until we could both take showers."

    jump bangok_anoney_xemera2_conclusion

label bangok_anoney_xemera2_satisfy_male:

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night

    $ renpy.pause (3.3)

    show emera normal b

    c "Now that I have satisfied you, I wish to take care of myself. Given how large your reproductive passage is, I would like to try your other entrance."
    Em bangok blush b "Of course ambasssador. My body is yours to use after what you have done for me. It is quite fair that you should also get some pleasure out of this."

    show emera bangok blush b flip:  #Trying to do something similar to the anna lays down in anna chapter 2, probably got this wrong.
        xanchor 0.5
        ease 1.0 pos (0.8, 1.0)
    with None
    $ renpy.pause(0.7)
    show emera bangok blush b flip:
        pos (0.8, 1.3)
        rotate -15
    with dissolve
    play sound "fx/leather.ogg"
    m "I asked Emera to roll over onto her back. Then I got up from the floor and went over to the fruit bowl on one of the cabinets. Selecting three firm fruits that were slightly larger then my hand I returned to Emera."
    show emera ques b flip
    m "Emera, on her back, gave me a confused look until I spread apart the large slit that her egg had recently come out of, which was still very wet with the multiple orgasms she'd experienced earlier."
    show emera bangok blush b flip
    m "I started to push the fruits into her tunnel, until all three were in her birthing passage."

    if persistent.bangok_cloacas == True:
        m "Then I lay atop her, reached down to spread appart her cloaca, found the opening to her anal passage, then buried my lubed length within."
    else:
        m "Then I lay atop her, reached down to finding the lower slit leading to her anal passage, then buried my lubed length within."
    play soundloop "fx/flap1.ogg"
    m "Our lower bodies were covered with the slippery mating fluids from her numerous orgasms, enabling me to slide my body quickly over her scales as I thrust into her anal passage."
    m "I could feel her mating muscles clamping down on the fruit in her canal, the contractions against which then also slightly contracted her anal passage."
    Em bangok blush b flip "Oh this is new, I have never thought of using food items in this way, or using my other tunnel for such..."
    m "I had been rock hard through the whole egg laying procedure, so I knew that I would not last long."
    m "I continued to thrust into her, the fruits in her tunnel moving around with the motion of my hips."
    play sound "fx/varagrowl"
    m "The pressure of the fruits against the entryway of her egg chamber caused her to moan in pleasure."
    m "I could feel my orgasm building up. I was not going to last much longer."
    stop soundloop fadeout 0.5
    if bangok_anoney_xemera2_protection_dick == True:
        m "It was only a couple more thrusts until I blew my load, the condom containing my relitively small spurts compared to what a dragon would probably produce."
    else:
        m "It was only a couple more thrusts until I blew my load, my relatively small spurts compared to what a dragon would probably produce still painting the walls of her lower passage."
    show emera bangok orgasm b flip
    $ renpy.pause (1.5)
    play sound "fx/bitescr.ogg"
    $ renpy.pause(0.8)
    m "My last thrust, coupled with the movement from the fruits in her tunnel threw Emera into yet another orgasm. her lower passage tightened further around me, milking out of me a few extra spurts."
    m "Once her tunnel loosened up to allow me to pull out I got up from her underside and proceeded to reach into her vaginal passage to remove the fruit."
    show emera bangok blush b flip
    play sound "fx/varagrowl"
    m "Emera gave a moan each time her lips were stretched by their expulsion."

    if (bangok_anoney_xemera2_protection_dick == True) and (bangok_anoney_xemera2_clean_arms == True):
        m "I reached down and quickly removed the condom from my shaft, then removed the ones on my arms; the rubbers had served their purpose in keeping at least some of me relatively clean."

    elif bangok_anoney_xemera2_protection_dick == True:

        m "I reached down and quickly removed the condom from my shaft."

    elif bangok_anoney_xemera2_clean_arms == True:

        m "I reached down and quickly removed the condoms from my arms; the rubbers had served their purpose in keeping at least some of me relatively clean."

    if (persistent.bangok_watersports == True) and (bangok_four_playerhasdick == True):

        m "Given that it had been several hours since I had visited a restroom, nature suddenly decided to make its call."
        c "(Oh crap what do I do?)"
        c "(I can't go outside the office to the washroom, not in this state.)"
        c "(The last thing I want to do is accedently leave any evidence of our activities, especially with the hightened smell of the dragons.)"
        menu:
            "Don't think about it, just get cleaned up so you can go to the restroom.":
                pass

            "Relieve yourself inside Emera.":
                jump bangok_anoney_xemera2_ws_relief

    jump bangok_anoney_xemera2_toweling_showercomment_conclusion


label bangok_anoney_xemera2_ws_relief:
    c "Emera, I'm afraid I desparately need to use the restroom. I..."
    Em bangok blush b flip "Oh, I understand. I have had to do the same thing myself after a particularly long session."
    c "No, I mean I need to use the restroom now, and I don't think I should leave your office in this state."
    Em ques b flip "Ah, I see. Well, I am awawre some dragons fetishize the practice of relieving themselves in their partner, and I have immunized myself to the thought."
    Em laugh b flip "Experiencing it in practice is another matter, but I am willing to let you do so if you wish."
    label .ws_menu:
    menu:
        "Ass." if not persistent.bangok_cloacas:
            jump todo_bangok_anoney_xemera2_out_of_content
        "Vagina." if not persistent.bangok_cloacas:
            jump todo_bangok_anoney_xemera2_out_of_content
        "Anal vent." if persistent.bangok_cloacas:
            jump todo_bangok_anoney_xemera2_out_of_content
        "Cloaca." if persistent.bangok_cloacas:
            jump todo_bangok_anoney_xemera2_out_of_content
        "Mouth." if bangok_four_xemera2_ws_mouth_unasked:
            $ bangok_four_xemera2_ws_mouth_unasked = False
            c "May I use your mouth?"
            Em frown b flip "While I'm immunized to the thought, I highly doubt I'm immunized to the taste."
            Em ques b flip "I'd prefer if you keep this far from my face."
            jump .ws_menu
        "Urethra.":
            jump .urethra

    label .urethra:
    m "Remembering the discovery of where Emera's urethra was, and hoping that her hormones would still prevent any discomfort, I decided to relieve myself inside the dragon's bladder."
    m "Emera was still laying on her back and gave a purr as I got back on to rest on her belly, and this time stuck my dick insie her vagina."
    if persistent.bangok_cloacas == True:
        m "Reaching back I spread her slit easily and found her urethra exactly where I had remembered it."
    else:
        m "Reaching back I spread her vaginal slit easily and found her urethra exactly where I had remembered it."
    show emera ques b flip
    m "Emera had a confused look on her face before I reached down with my other hand and pushed my now lubrucated dick into her urethra"
    m "I was dreading her reaction incase she had too much discomfort, however after waiting a few moments without her expressing being in pain I felt relieved that her hormones must still be working."
    Em normal b flip "That feels... odd I have never come across records that have shown that place to be penetrated, however given the larger size of dragons and not wanting to cause pain to a mate it is obvious why."
    c "I appologise, Emera. I need to use the restroom, however given the mess I did not want to leave evidence of our activities so I wanted to relive myself into your bladder."
    c "It doesn't hurt?"
    Em bangok blush b flip "No.. as I said it just feels odd. I would not like to be mated down there, even Earth dragons are not completely resistant in areas not expected to be mated. However I do understand your concern in sharing my desire to keep this private so I will allow you to proceed."
    m "I continued to press further in, the lube from her vagina helping to quicken the journey."
    m "I came to her sphincter seperating the enterence to her bladder and gently put pressure until the head of my dick pushed through."
    show emera normal b flip
    $ renpy.pause (0.5)
    show emera frown b flip with dissolve
    play sound "fx/bubbles.ogg"
    $ renpy.pause (3.5)
    play sound "fx/uncork.ogg"
    show emera normal b flip with dissolve
    m "Emera let out a gasp and i could tell this was uncomfortable for her. I quickly released my own bladder and when I was done, quickly pulled out."
    c "Sorry."
    show emera laugh b flip
    m "I felt her rest one of her front paws pat me on my shoulder and I just laid a while, enjoying the warmth of her body heat."
    Em normal b flip "If everything is done, then we ought to clean up, it is already very late and you will probably be wanting to back to your appartment"
    play sound "fx/cabinet.ogg"
    $ renpy.pause (0.5)
    play sound "fx/rubb2.ogg"
    m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until showering."
    jump bangok_anoney_xemera2_conclusion


label bangok_anoney_xemera2_satisfy_female:
    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night

    $ renpy.pause (3.3)

    show emera normal b

    if bangok_anoney_xemera2_clean_arms == True:
        m "I reached down and quickly removed the condoms from my arms, the rubbers had served their purpose in keeping my arms clean."

    c "Emera, now that you are satisfied, would I be able to borrow your pleasure stick to help satisfy my own needs."
    Em bangok blush b "Of course, Though are you sure you would be able to take it?"

    if if bangok_four_malepartners > 0:
        c "As I have said, i have had other encounters with male dragons and have been able to take them, a dildo of the same size will be managable."

    else:
        c "I used to have 'toys' for my own pleasure back in the human world, I had quite a nice collection of bad dragons, whith which to state my desires when wanting to get a little rough."

    m "I went to the cupboard and reached down to the lower shelf and retrieved the dildo from the lower shelf."
    play sound "fx/cabinet.ogg"
    m "Examining the dildo, it was made out of a hard rubber, nearly the length of my arm, with a rounded tip, the head bulged out slightly about the size of my fist."
    m "The rest of the shaft starting out at the base being the thickness of my bicep decreasing to the diamiter of my wrist just below the head. There was a length of wood sticking out the base, evidently to make it easier to hold when in use."

    show emera normal b flip:  #Trying to do something similar to the anna lays down in anna chapter 2, probably got this wrong.
        xanchor 0.5
        ease 1.0 pos (0.8, 1.0)
    with None
    $ renpy.pause(0.7)
    show emera bangok normal b flip:
        pos (0.8, 1.3)
        rotate -15
    with dissolve

    m "Emera had rolled onto her back"
    Em laugh b flip "Come over here and lay on me whilst you have your fun."
    m "I sat on her lower belly and bent forwards to her groin."
    m "I pressed the dildo to Emera's vagina and pushed it in. It slid in easily due to her tunnel being very lubricated and still stretched from passing the egg."
    m "I then pulled the stick out of her, ensuring it was thouroughly coated in her fluids before placing the tip at my enterence and gently easing it in."
    m "I let out a low moan as I could feel the head stretch my outer lips as I continued to push it in slowly until the thickest part was inside, then all it took was a light clench to pull the rest of the head inside."
    c "Yes, i was ready for this"
    m "It had been a while since I had felt this full, and it was only the head."
    m "I continued to take it in further. after about half of the way down I felt the head of the toy kiss my cervix."

    if persistent.bangok_cervpen == True:
        m "Knowing that I could take it further I continued to put pressure on my cervix, twinsting the toy slightly to dialate it."
        m "I could feel my cervix loosening up as i started to lightly thrust the toy a few inches back and forth."
        m "A few moments later and I felt the head pop therough and into my womb."

    else:
        m "This is as much as i can take, given the size of the toy."
        m "I started to lightly thrust the toy a few inches back and forth, getting used to the dildo."

    m "Emera put her hand on my belly and could feel the progress of the toy inside me."
    Em bangok blush b "I am impressed, it seems you have indeed had experiance enough to take it."
    c "Thank you"
    m "Now that my vagina had conformed to the dildo safely i laid fully on my back on Emera."
    play soundloop "fx/massage2.ogg"
    play sound "fx/rub1.ogg"
    m "The dragon continued to rub her hand over my belly being able to feel the toy through my body."
    m "After what felt like an age, but was probably only about 5 minuites my orgasm washed over me, I went limp as my body was consumed by euphoria"
    stop soundloop fadeout 0.5
    m "I decided to just lay there fora while, toy still hanging out of my vagina and bask in the afterglow on the warm belly of Emera."
    Em "If everything is done, then we ought to clean up, it is already very late and you will probably be wanting to back to your appartment"
    play sound "fx/uncork.ogg"
    if persistent.bangok_cervpen == True:
        m "I gave a nod and reached down to gently tug the toy out of me, giving a sudder of pleasure as the head of the toy first left my womb, then stretched my lips."
    else:
        m "I gave a nod and reached down to gently tug the toy out of me, giving a sudder of pleasure as the head of the toy stretched my lips."
    m "Emera took her toy off of me and stuck it in her mouth, licking it clean. afterwards she gave it back to me and I put it back into the cupboard"
    play sound "fx/cabinet.ogg"
    m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until showering."
    jump bangok_anoney_xemera2_conclusion

label bangok_anoney_xemera2_double_fisting:

    if persistent.bangok_cloacas == True:
        m "Spreading her cloaca wide with one hand, I slowly withdrew my arm from her vaginal tunnel until it was out completely, it was coated in a mixture of lube and her plentiful arousal."
        m "I moved my arm slightly lower, the target being her anal passage towards the bottom of her slit. Once again I formed my fingers to a point and pushed at her anal entrance."
        m "Now that my first arm was in the right place, I pushed my other arm back into her vacated vaginal canal, her cloaca stretched wide around both my arms."
    else:
        m "Spreading her anal vent wide with one hand, I slowly withdrew my arm from her vaginal slit until it was out completely, it was coated in a mixture of lube and her plentiful arousal."
        m "I moved my arm slightly lower, the target being her anal passage in her spread lower slit. Once again I formed my fingers to a point and pushed at her anal entrance."
        m "Now that my first arm was in the right place, I removed it from holding open her anal slit and moved it up to push back into her vacated vaginal canal, both slits stretched wide around both my arms."
    m "I started to push both my arms into her, there was not much resistance due to the lube, hopefully this was feeling good for her."
    Em bangok blush b "MMmm having both my passages stretched at the same time is not something I had ever thought about before. I did once take my pleasure stick up there, but the feeling in isolation was not as pleasant as from my vagina."
    Em "But having both at once is just adding to the pleasure."
    if bangok_anoney_xemera2_clean_arms == True:
        m "By now my elbows are sinking in and the ribbed texture of the condoms on my arms are entering her."
    else:
        m "By now my elbows are sinking into her."
    m "I pulled back both my arms and began alternating them in a piston motion pushing one in as the other was pulled almost out."
    m "Gradually I could feel her tunnels loosening, her outer lips becoming more relaxed and her arousal flowing in a small trickle, keeping both arms topped up with fresh juices."
    m "By now I was able to push both arms halfway up my biceps into her and in her vagina, I could feel the entrance to her egg chamber once again."
    if persistent.bangok_cervpen == True:
        m "Reforming my hand into a point again, I began to put pressure at the end of my stokes onto the centre of the rear wall of her tunnel"
        Em bangok blush b "You need to go faster. Faster and harder, put your body into it."
        stop soundloop
        play soundloop "fx/massage2.ogg"
        m "Gradually I could feel the barrier yielding with a hole starting to open up"
        play sound "fx/varagrowl"
        Em "Don't stop now, [player_name]. Give it all you got!"
        m "Over the next few minutes the hole widened even more, until eventually my hand pushed through."
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I broke through into her egg chamber. I could feel the smooth hard surface of her egg held within her inner castle."
        stop soundloop fadeout 0.5
        m "I stopped moving my arm with my hand in her egg chamber, just moving around the egg."
        play sound "breathing.ogg"
        Em "(panting) why did you stop?"
        play soundloop "massage2.ogg"
        m "I smoothly withdrew my arm until my fist was at her entrance and punched it through her tunnel back into her egg chamber."
        Em "More, More"
        m "I quickly pick up the pace pushing my arm deep each time, touching the egg with my knuckles."
        $ renpy.pause(0.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and....."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        play sound "fx/bitescr.ogg"
        $ renpy.pause(0.8)
        m "Emera quickly grabbed a cushion off her chair and quickly bit down to deaden her roar as I felt her tunnel tense up with pulsing waves travelling down to her egg chamber, the barrier once there had disappeared, the entrance had dilated completely"

    else:
        m "I began to move my fist around inside her, stimulating her walls around the entrance to her egg chamber"
        Em bangok blush b "You need to go faster. Faster and harder, put your body into it."
        stop soundloop
        play soundloop "fx/massage2.ogg"
        m "Over the next few minutes, her tunnel gradually got looser. I could speed up my thrusts, making sure to move my wrist each time I kissed the entrance to her egg chamber with my knuckles."
        play sound "breathing.ogg"
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I found a particularly sensitive area near the end of her tunnel. I angled my hand so that I would continually rub this area each time I plunged my arm back in"
        $ renpy.pause(0.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and....."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        play sound "bitescr.ogg"
        $ renpy.pause(0.8)
        m "Emera quickly grabbed a cushion off her chair and quickly bit down to deaden her roar as I felt her tunnel tense up with pulsing waves travelling down to her egg chamber, the barrier that until a few moments ago was at the end of her tunnel rapidly disappeared, the entrance dilating completely."

    m "Her passages clenched so tight around my arms that I could no longer move them, her vaginal opening spraying copious amounts of lubrication all over my lower body and genitals."

    if persistent.bangok_watersports == True:
        m "I suddenly felt a much warmer and wetter fluid surrounding the arm in her vagina. Given the position Emera was standing, I was glad that it was moving further inside her."
        m "She didn't mention that the laying hormones also made her lose control of her bladder, though it could be an evolutionary trait to provide more lubrucation for the egg."
        m "I am glad I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    else:
        m "I am glad that I had removed my clothing and now appreciated why she performed this on an easy to clean mat."

    m "After what felt like several minutes I felt her passageways relaxing, however I could still feel pulses along the sides of her vaginal tunnel, however now they were going in the opposite direction."
    m "Emera was breathing heavily as she spoke to me again."
    Em bangok blush b "Thank you for that. You have done it. My egg is now going to be starting its journey out of me, and for the first time I can enjoy it."
    Em "You have already done so much for me by getting this far, but I would ask you to do more."
    Em "The hormones that are released to prepare to lay the egg severely limit any discomfort I would experiance from the egg passing out."
    Em "There is something that I have always wanted to try after reading about it in our records, but have not been able to do, because of my lack of a parner and of a flexible enough tail."
    Em "When the egg is travelling down my tunnel, are you able to stop it before it comes out and push it back?"
    m "I started to pull my arm out of her anal passage When i felt her muscles clamp down hard on my arm."
    Em "Please can you leave it in? I want to see how it feels expelling the egg with my lower passage filled. If I like it in the future, maybe i shall leave my pleasure stick in there whilst i lay my egg."
    c "If that is what you want."
    m "I pulled back my arm that was in her vagina until just my hand remained inside and I could see the muscles around her groin area working to push the egg down her tunnel."
    m "I could feel those same conteatctiions mirored in her anal passage as her mucsles lightly squeesed my arm."
    m "The look of rapture on the dragon's face confirmed that she was as high as a stunt-performing flyer."
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the enterence to her vagina. I held the egg for a moment whilst her contractions passed, then i drove my arm back into her slick cannal."
    m "The copious lubrication meant it was easy to push the egg back in. I even went further then before given the enterence to her egg chamber was still dialated."
    m "It didn't appear to cause her any discomfort. In fact, there was another muffled roar as another set of bite marks were added to the same cushion used before."
    m "I could feel her tunnels spasm around my arms, almost in confusion as the instinct to draw the male fluids to the egg chamber was competing with the signals from her egg chamber that is currently occupied and trying to evict the egg."
    m "Some moments later, her tunnels again went limp and I moved my hand back to the beginning of her vagina to prepare to go again."
    m "I repeated the operation five more times before my arms was starting to get tired. I removed them from her and finally allowed her body to expell her egg."
    $ renpy.pause (1.5)
    play sound "fx/bitescr.ogg"
    $ renpy.pause(0.8)
    Em bangok orgasm b "(panting heavily) That was amazing, I had no idea that having something in my lower passage could feel so good. Those old records were not wrong when they recorded their observations."
    m "I caught the egg in my hands as it fell from her slit. I was suprised by its weight and size, about as large as a melon. The color was a pale yellow, nearly matching her belly."
    c "What will you do with the egg now?"
    Em ques b "Usually I donate it to a charity in the city. They have an anomynous drop off box here at the library."
    Em "They extract the contents of the egg, fill it with a dense foam then paint designs on the shell, with the eggs then sold as souvenirs, presents and the like."
    Em normal b "The profits gained are then shared with orphanages and counciling for low income families all over."
    Em frown b"The level of pleasure that is had by both partners from encoraging the beginning of the cycle can fuel an addiction."
    Em "The concequences of which are seen in the large range of contraceptives, you must have seen them at the local grocery store and unfortunately in the unwanted fertilized eggs that are sometimes also left in the donation box."
    c "Really?"
    Em normal b "Of course any eggs left in the box at the end of the day are checked by simply shining a light through them. Given the shells are slightly transleucent it is possible to tell if they are viable or not."
    m "I carefully placed the egg down onto the mat before it could slip out my hands."
    if bangok_four_playerhasdick == True:
        menu:
            "Ask to be satisfied.":
                jump bangok_anoney_xemera2_satisfy_male
            "Just finish up.":
                play sound "fx/cabinet.ogg"
                $ renpy.pause (0.5)
                play sound "fx/rubb2.ogg"
                m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until showering."
    else:
        menu:
            "Ask to borrow Emera's pleasure stick.":
                jump bangok_anoney_xemera2_satisfy_female
            "Just finish up.":
                play sound "fx/cabinet.ogg"
                $ renpy.pause (0.5)
                play sound "fx/rubb2.ogg"
                m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until showering."

    jump bangok_anoney_xemera2_conclusion


label bangok_anoney_xemera2_massage_only:
    Em normal b "Yes, it is just more comfortable to lay on the mat than the floor, plus allows all round access without having to move once the process is started."
    m "I nodded."
    m "I pushed my upper body up to be able to reach the hard plates on her back and as before used my weight on the muscles beneath."
    Em mean b "Oh I could just lay like this with you massaging my back forever. Have you perhaps had any more thoughts about becoming my assistant once all this ambassador business wraps up?"
    m "I looked up from digging my palm into her back to answer her question."
    c "I do not think it would be wise to do that, as much as it would be fascinating to learn more of dragon culture, you have said before you wish to start a family."
    c "I can't give you a family, and I would not want to come between you and your future mate, once you have found a suitable suitor."
    m "I moved to her rear, kneading her thighs and rump."
    m "Emera took a deep breath and glanced at the ceiling, analysing my response no doubt having an internal argument over how to reply."
    m "After a few moments she brings her head back down on the pillow and exhaled with a sigh."
    Em ques b "You are right of course, I am so used to getting what I want, that I do not fully think through the consequences of my needs."
    Em laugh b "Yes, Yes that feels so good, oh how I am going to miss having this performed when you eventually go back through the portal."
    m "All that was left to do is her tail. I started at the top, moving further up closer to her body. This time I could massage areas that had been neglected before as my hands found themselves around the base of her tail."
    m "After finishing the massage, I got up to stretch my legs"
    jump bangok_anoney_xemera2_conclusion

label bangok_anoney_xemera2_conclusion:
    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night

    $ renpy.pause (3.3)

    if (persistent.nsfwtoggle == False) or bangok_four_common.bangnokay.check():
        Em laugh b "Thank you again for your wonderful massage, I feel great, the tension that had been building up is gone."
        Em ques b "I assume you can find your way back to your appartment?"
        c "Yes I can, I was glad to have helped, I hope that you will chill out a bit more, and think about the outcomes of what you want for yourself."
        Em normal b "I shall try [player_name]"
        c "Goodnight"
        Em "Goodnight"
    elif bangok_anoney_xemera2_massage_only == True:
        Em frown b "I am disappointed that you would not help me, however I did still appreciate the massage. I assume you can find your way back to your appartment?"
        m "I nodded in reply."
        c "Goodbye."
        Em normal b "Goodbye."
    else:
        Em bangok blush b "Thank you again for your wonderful massage and for making tonight the best evening in a long time."
        Em laugh b "I feel great, the tension that had been building up is gone and I have been able to live one of my dreams."
        m "Bending down to the floor to pick up her egg, a movement she must be well practiced by now, she holds out her front paw, offering it to me."
        Em "As a token of gratitude for providing your exquisite service, please accept my egg as a reminder of this wonderful evening and the time we shared."
        menu:
            "Accept":
                m "I reached forward with my hands and wrapped them around the egg, carefully taking and hugging it to my chest."
                c "Thank you for this unique gift, I shall make sure to look after it well."
                c "(I shall have to take it to the lab in order for it to be preserved properly)"
            "Reject":
                c "Sorry but I can not accept this gift. If it were to come to notice by either dragons or the humans back home, then i could be in serious trouble as to how I had gotten it."
                m "I saw Emera's head droop as she heared my refusal of her gift."
                Em frown b "Of course, I understand that it could cause trouble going forwards, the negotiations are still ongoing and as you said if it is discovered vby the humans then it could lead to difficult questions."
                m "Seeing her crestfallen look, I stepped closer and  put my hand on her other shoulder."
                c "I wish that times were better and that i could accept your gift, really I do."
        Em ques b "I assume you can find your way back to your appartment?"
        c "Yes I can, I was glad to have helped, I hope that you will chill out a bit more, and think about the outcomes of what you want for yourself."
        Em normal b "I shall try [player_name]"
        c "Goodnight"
        Em "Goodnight"


    stop music
    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_library_corridor_night with dissolvemed

    $ renpy.pause (3.3)

    if (persistent.remy1played == True) and (remystatus == "good") or (remystatus == "neutral"):
        m "As I left Emera's Office and walked down the corridor I could see that the light was on Remy's office was on and faint sounds of a computer game could be made out."
        m "I paused briefly outside the door and wondered if he is making progress on that RPG I accedently broke."
    else:
        m "As I left Emera's Office and walked down the corridor I could see that there was a light on in the next office down."
        m "I paused briefly outside the door to read the door plaque 'Head Archavist' I guessed this was probably Remy's office."

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene o3
    play music "mx/campfire.ogg" fadein 2.0

    $ renpy.pause (3.3)

    m "Soon I had returned home."

    if bangok_anoney_xemera2_massage_only == True:
        m "After cooling off during the walk home, I thought maybe I had made the wrong choice in refusing her offer."
        c "(Emera did seem hearbroken when I had refused. If only my head wasn't so much of a mess with the police investigation and the responsibility I feel being an ambassador. What could have happened had something had gone wrong?)"
        c "(Ah well, it would be extremely irresponsible of me to go back in time for this non-emergency, even if I did know the coordinates to before this evening's events.)"
        c "(Well, time for bed. Hopefully tomorrow will be a better day.)"
    elif (persistent.nsfwtoggle == False) or bangok_four_common.bangnokay.check():
        c "(I hadn't thought I would be paying Emera a return visit, but the evening was pleasent enough.)"
        c "(It was nice to get to know her private side and to know that she can confide in me given my unique position as ammbassador.)"
        c "(Well, time for bed. Lets see what tomorrow brings.)"
    else:
        c "(I hadn't even thought I would be paying Emera a return visit. Not only did I give her a massage, but I allowed her to experience pleasure she thought she would only be able to dream of.)"
        c "(It was nice to get to know her private side and to know she can confide in me given my unique position as ammbassador.)"
        c "(Well, time for bed, Lets see what tomorrow brings.)"

    call _mod_incc from bangok_anoney_xemera2_mod_incc
    jump _mod_fixjmp

label todo_bangok_anoney_xemera2_out_of_content:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")