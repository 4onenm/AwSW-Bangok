init python:
    bangok_anoney_xemera2_set_condition = False
    bangok_anoney_xemera2_clean_arms = None
    bangok_anoney_xemera2_refuse_participate = False
    bangok_anoney_xemera2_lick_slit = None
    bangok_four_xemera2_ws_mouth_unasked = True
    bangok_anoney_xemera2_massage_only = None

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
    m "As I went past an aisle, I saw Remy with his head buried in a large box, evidently searching for a trinket of some kind to further his research."
    m "I continued toward the private area of the library where I had been before on my last visit."

    scene black with dissolvemed
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (0.5)
    scene bangok_anoney_library_corridor_night with dissolvemed

    m "Finding the now familiar door with the title Minister for Culture and Arts on it, I knocked."

    play sound "fx/knocking1.ogg"

    $ renpy.pause (2.0)

    Em "Come in."

    play sound "fx/door/door_open.wav"

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night with dissolvemed

    $ renpy.pause (0.5)

    play sound "fx/door/close2.wav"

    show emera laugh b with dissolve

    play music "mx/eveningmelody.ogg" fadein 2.0

    Em "Hello [player_name]! It's so nice to see you again. I wasn't sure if you would have the time, considering the extensive police investigation at the moment."

    c "Well I needed a break from the constant police work. It wasn't what I had intended to be my full time job when I stepped through the portal. Besides, being an ambassador means experiencing the stories of all the dragons that make up society."
    Em ques b "I see. I am pleased that you would consider me one of the dragons to experience. All too many times I feel that I am brushed off as just another high-up, pompous, dismissive dragon that needs to pretty herself up with body paint and jewelry to make herself feel important."

    menu:
        "Snicker.":
            c "(Funny, that is exactly what I think of you.)"
            Em frown b "What was that?"
            m "I coughed to try to cover up my faux pas."
            play sound "fx/throat_clear.ogg"
            c "Sorry just clearing my throat."
        "Flatter.":
            c "You are a very important politician being brought up from a well-off family and you don't work in an active lifestyle."
            c "So why should you not wear jewelry or scale paint to project your status?"
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
        c "I remember you meeting Katsuharu when he bought his cart to Tatsu Park, you both seem to have known each other for a long time."
        c "Why would he not be suitable?"
        Em ques b "Hmm, we have indeed known each other for a long while. And he does make quite artisan ice cream, his special flavor is quite exquisite if he has it in stock."
        Em laugh b "Especially if freshly prepared."
        if bangok_four_xkatsu.unplayed == False:
            c "Indeed, I helped him prepare a fresh batch just the other day. It is indeed exquisite, as you say."
        else:
            c "I see. I shall have to remember that if an opportunity comes to find out if it is as good as you say."
        Em normal b "In any case he is too old for me. Had he been twenty years younger then perhaps."
    else:
        c "(She does have a point; I have not seen many other Earth dragons about.)"

    Em "Anyway, enough of the chit chat. On to the reason why I left you that message."
    Em "I assume you can still remember the technique from last time?"
    m "I nodded."
    Em ques b "Good."

    scene black with dissolvemed

    $ renpy.pause (0.5)

    show bangok_anoney_emeramassage_night at Pan((960, 250), (960, 0), 6.0) with fade

    $ renpy.pause (1.0)
    play sound "fx/sheet.wav"
    m "As before, she produced the same mat and pillow and proceeded to lay with her back toward me."

    m "I knelt beside her on the edge of the mat and started massaging the scales on her neck, being careful to keep my arms out of the way of the spines on her head. After my close shave last time, I had no desire to experience a repeat performance."

    Em laugh b "Ah yes, yes. So good."

    m "As I moved onto her shoulder she leaned into my ministrations, reminding me of the cats that people used to keep in the old world."

    show bangok_anoney_emeramassage_night at Pan((960, 0), (960, 250), 4.0)

    c "Do you keep this mat and pillow here just for massages?"

    if (persistent.nsfwtoggle == False) or bangok_four_common.bangnokay.check():
        $ bangok_anoney_xemera2_massage_only = True
        jump bangok_anoney_xemera2_massage_only
    else:
        pass # Onward to lewds!

    Em frown b "Actually, no that is not the only use I have for them. It is a rather personal and private reason."

    c "Oh?"

    Em ques b "You are probably not one to know unless you have read a textbook on dragon biology."
    Em normal b "Female Earth dragons go into ovulation about every 3 months or so. Even if the egg is unfertilized it will stay within the egg chamber for some time after the hard shell is formed."
    Em frown b "Of course, the body will eventually pass the egg when the next cycle starts. Though, obviously, having an unscheduled egg laying could be highly embarrassing, even dangerous."

    if persistent.bangok_cervpen:
        Em "Fortunately, our creation process, whatever it may be, found a way to control the timing of the laying in us Earth dragons."
        Em "If mating occurs where the head of the male penis pushes into the egg chamber, the body will bring forwards the next cycle and it will start the laying process."
    else:
        Em "Fortunately, our creation process, whatever it may be, found a way to control the timing of the laying in us Earth dragons. If mating occurs, the body will bring forwards the next cycle and it will start the laying process."

    m "I pushed my upper body up to be able to reach the hard plates on her back and use my weight on the muscles beneath."

    show bangok_anoney_emeramassage_night at Pan((960, 250), (960, 500), 4.0)

    Em ques b "Due to the fact I currently have no male partner to take care of my needs and due to concerns anyone else I might ask may try to blackmail me or want political favors, I usually take care of things myself; having a pleasure stick that I use modeled on an Earth dragon's tool."

    Em mean b "Given your current status as an ambassador, it means you are not embedded in the usual dragon politics and your job requires you to maintain good relations with myself and others of the council."

    Em ques b "There is also a more personal reason:{w=0.2} Those hands of yours work magic on my outside, and I am intrigued if they will be just as magical working on my insides."

    menu:
        "Accept.":
            pass

        "Reject.":
            $ bangok_anoney_xemera2_refuse_participate = True
            c "I didn't expect to be performing intimate duties, I thought this was going to purely be a massage, given you admit that you take care of yourself anyway I refuse to take part."
            Em frown b "I see, I guess it was foolish on my part for thinking that you would be interested in one of the most important bonding rituals of our people."
            show bangok_anoney_emeramassage_night at Pan((960, 500), (960, 800), 6.0)
            m "I quickly moved around to her rear, now working on her hips and rump."
            m "The rest of the massage happened in silence. The words that she had said had rattled my core. What with investigating the murders and also needing to get the generators to save humanity, being asked to give pleasure to a politician was too much."
            m "(I know that this massage is not as good as my first one, I can only hope that this will not have detrimental impacts on human dragon relations.)"
            jump bangok_anoney_xemera2_conclusion

    if bangok_four_anna2.annacame == True:
        c "(Having experienced firsthand exactly what magic my hands could do for Anna, I was confident that I could please her.)"
    else:
        c "(Not having experience with a female, yet I decided to just trust in my judgment that, just as she guided me through her massage, she will let me know what feels good for her.)"

    m "I moved around to her rear, now working on her hips and rump."

    show bangok_anoney_emeramassage_night at Pan((960, 500), (960, 800), 6.0)

    Em laugh b "Yes, yes! That feels so good. Oh how I am going to miss having this performed when you eventually go back through the portal."

    m "All that was left to do was her tail. I started at the tip, then moved slowly down closer to her body. Given my hands would be seeing plenty of action tonight, this time I could massage areas that had been neglected before as my hands found themselves around the base of her tail."

    m "After finishing the massage, I got up to stretch my legs. Realizing that it would be best not to have anyone walk in on us, I went over to the door, slid the room status plate to Engaged and locked it."
    $ renpy.pause (1.0)
    play sound "fx/door/handle.wav"
    $ renpy.pause (1.0)
    play sound "fx/door/lock.ogg"

    m "I pulled the blind down over the window. The last thing Emera could want is for any of the other dragons to know that she was having intimate relations with a human."
    $ renpy.pause (0.5)
    play sound "fx/envelope.wav"
    $ renpy.pause (1.0)
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
                c "We don't have cloacae, so our genitalia and anal openings are kept separate."
            else:
                Em mean b "Fascinating you have your mating tool just dangling out like that. It looks so small and shriveled and floppy. Do you not have a slit to protect it?"
                c "No, we do not have slits for our genitals."

        "Female.":
            $ bangok_four_playerhasdick = False
            if persistent.bangok_cloacas == True:
                Em "Fascinating, but I believe I spotted two openings in between your legs?"
                c "We don't have cloacae, so our genitalia and anal openings are kept separate."

    m "I gestured to my clothes."
    c "We also wear clothing, a substitute for scales used to protect our bodies, including our genitals, from damage and to retain heat."

    c "Unlike for dragons, removing our clothing and exposing ourselves is an activity done only with those that we want to be intimate around, or for bathing."

    c "Before we begin with the more \"physical\" activities, it is common in human culture to provide stimulation for both partners, to further the bond that is shared and to get the couple prepared for intercourse."
    Em ques b "Ooh a human ritual, It has been theorized how humans could have been romantic. I had never thought to experience anything like it in reality."
    c "Would you be able to sit on your sofa with your legs apart? This should be the more comfortable position for you than doing this on the floor."
    Em laugh b "Of course. I am most curious what you intend to do. We have had plenty of physical contact already thanks to your massage, and we dragons are hardy enough to get straight to the action without needing preparation."

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emera_sofa:
        yalign 1.0
        linear 2.0 yalign 0.0
        yalign 0.0
    with dissolveslow


    m "Emera got up from off the floor and sat on her sofa."
    play sound "fx/bed.ogg"
    show bangok_anoney_emera_sofa:
        yalign 0.0
        linear 1.0 yalign 1.0
        yalign 1.0
    $ renpy.pause (2.5)
    m "I moved her pillow over and sat on it,{w=0.5}{nw}"
    play sound "fx/sheet.wav"
    m "I moved her pillow over and sat on it,{fast} facing her groin."
    play soundloop "fx/purr.ogg" fadein 1.0
    if persistent.bangok_cloacas == True:
        m "I rested my hands on her groin and started to rub the small scales surrounding her single vertical slit."
    else:
        m "I rested my hands on her groin and started to rub the small scales surrounding her slits."
    play sound ["fx/rub1.ogg", "fx/wipe.ogg", "fx/rub1.ogg", "fx/wipe.ogg", "fx/rub1.ogg"]
    Em laugh b "That tickles, but in a good way, dragon paws are not best suited due to our claws and limited dexterity, at least for those that use them for walking."
    m "Emera gently rested her front paws on my head and ran her claws through my hair."

    if bangok_four_playerhasdick == True:
        Em normal b "Your fur on your head is so strange. Although fur is present on some of the more exotic species it is normally short and stiff and stands up by itself."
    else:
        Em normal b "Your fur on your head is so strange. Although fur is present on some of the more exotic species it is normally short and stiff and stands up by itself. I did not realize humans let their hair grow so long. It is different to that of the other ambassador."

    c "What you call fur, is hair it is made of keratin similar to your claws, just obviously much thinner."
    m "I let out a chuckle. The movement of her claws through my hair made me wonder if this is what those metal head massagers that I had seen in a museum one time would have felt like."
    Em ques b "I am not hurting you am I?"
    c "No. It's fine. Back in older times on earth we used to have these many pronged, metal sticks, where the prongs would be spread over the head and the stick moved about to massage the head. I saw one in a museum some years ago."

    if persistent.bangok_cloacas == True:
        m "Emera's slit had started to spread, showing her pink insides along with a sheen of her arousal. I could feel the area around it becoming warmer due to the increased blood flow."
        m "Reaching forwards I hooked my thumbs into the walls of her slit and pulled them apart."
    else:
        m "Emera's upper slit had started to spread, showing her pink insides along with a sheen of her arousal. I could feel the area around it becoming warmer due to the increased blood flow."
        m "Reaching forwards I hooked my thumbs into the walls of her upper slit and pulled them apart."

    m "The slit spread apart easily, showing great elasticity."
    c "(I guess the male may not be in the optimal position so some flexibility would be needed to make sure he can still penetrate successfully.)"
    c "(Or perhaps the dragons were created with such elasticity to be able to accommodate other dragon species, within reason.)"
    menu:
        "Lick.":
            $ bangok_anoney_xemera2_lick_slit = True
            m "I bought my mouth close to her spread slit and started to run my tongue over what I could reach of the inner walls."
            c "(The texture of her walls were smooth as expected yet they also felt both dense and malleable, similar to a dense but compressible polymer.)"
            play sound "fx/sniff.ogg"
            c "(The smell being this close to her was pungent. I could only imagine what effect it must have on a dragon with a higher sensitivity.)"
            play sound "fx/buck.ogg"
            m "Emera's legs gave an involuntary buck at the feeling of my tongue on her inner folds."
            m "Emera moved her head around checking both sides in case her movements had injured me."
            Em frown b "Sorry about that. I am not used to feeling such a texture as your tongue on my sensitive area. You are not hurt?"
        "Finger only.":
            $ bangok_anoney_xemera2_lick_slit = False
            m "I let my fingers roam the opening of her spread slit, massaging what I could reach of the inner walls without going more than a couple knuckles deep."
            c "(The texture of her walls were smooth as expected yet they also felt both dense and malleable, similar to a dense but compressible polymer.)"
            play sound "fx/sniff.ogg"
            c "(The smell being this close to her was pungent. I could only imagine what effect it must have on a dragon with a higher sensitivity.)"
            play sound "fx/buck.ogg"
            m "Emera's legs gave an involuntary buck at the feeling of my fingers on her inner folds."
            m "She moved her head around, checking both sides in case her movements had injured me."
            Em frown b "Sorry about that. I am not used to feeling such a texture of your smooth fingers on my sensitive area. You are not hurt?"

    m "I shook my head as I continued to explore her slit."

    Em ques b "Oh, I could just sit like this with you down there forever. Have you perhaps had any more thoughts about becoming my assistant once all this ambassador business wraps up?"
    m "I pulled back from her slit to take a few breaths and answer her question."
    c "I do not think it would be wise to do that. As much as it would be fascinating to learn more of dragon culture, you have said before you wish to start a family."
    c "I can't give you a family, and I would not want to come between you and your future mate, once you have found a suitable suitor."
    if bangok_anoney_xemera2_lick_slit:
        m "I resumed my oral exploration of her slit. Her arousal was in full swing. My face was covered in her juices,{w=0.5}{nw}"
        play sound "fx/singlesplash.ogg"
        m "I resumed my oral exploration of her slit. Her arousal was in full swing. My face was covered in her juices,{fast} with the excess starting to drip and form a small puddle on the floor."
    else:
        m "I resumed my exploration of her slit. Her arousal was in full swing. My hands were almost covered in her juices,{w=0.5}{nw}"
        play sound "fx/singlesplash.ogg"
        m "I resumed my exploration of her slit. Her arousal was in full swing. My hands were almost covered in her juices,{fast} with the excess starting to drip and form a small puddle on the floor."
    $ renpy.pause (0.5)
    play sound "fx/singlesplash.ogg"
    m "Emera took a deep breath and glanced at the ceiling, analyzing my response and no doubt having an internal argument over how to reply."
    m "After a few moments she brought her head back down and exhaled with a sigh."
    Em "You are right of course. I am so used to getting what I want that I do not fully think through the consequences of my wants."
    stop soundloop fadeout 5.0      #stop purr sound, 58 seconds long, maybe change to loop if going to spend longer then min on this scene?
    if bangok_anoney_xemera2_lick_slit:
        Em bangok blush b "I think I am ready enough to proceed, a desire has built further down my tunnel out of reach of that tongue of yours."
    else:
        Em bangok blush b "I think I am ready enough to proceed, a desire has built further down my tunnel out of reach of those fingers of yours."
    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emera_presenting at Pan((960, 250), (960, 500), 4.0)

    $ renpy.pause (2.0)
    play sound "fx/sheet.wav"
    if persistent.bangok_cloacas == True:
        m "Emera returned back to the mat, laying her head on her pillow. Unlike earlier, she lifted her rear and stood on her hind legs, spread wide to show the single vertical slit between them."
        m "The scales around it had a glisten in the light that was definitely not from scale shine. Clearly my foreplay had gotten her in the mood."
    else:
        m "Emera returned back to the mat, laying her head on her pillow. Unlike earlier, she lifted her rear and stood on her hind legs, spread wide to show her slit and ass between them."
        m "The scales around the larger vent had a glisten in the light that was definitely not from scale shine. Clearly my foreplay had gotten her in the mood."

    m "Emera gestured with her paw to a cabinet behind me."
    Em normal b "You will find lube and other supplies you may need in there."
    show black with dissolvemed
    
    m "I went to the cabinet that Emera indicated and opened the door."
    play sound "fx/cabinet.ogg"
    # if persistent.havetestresults == True:
    #     Em ques b "I have seen your test results. The data said that there was no issue with our sexual compatibility, so using protection isn't strictly necessary."
    # else:
    #     Em ques b "There is protection available if you want to use it. Given I am an Earth dragon, we are meant to be tough, so I doubt I could catch anything from you."

    if bangok_four_playerhasdick == True:
        Em ques b "There is protection available if you want to use it."
    if bangok_anoney_xemera2_lick_slit:
        Em laugh b "Though, given your oral exploration of my anatomy, I think we are well past that now."

    m "I had a look at the contents of the cabinet. There was a bottle of lube as well as a pack of smaller condoms. Stuffed in the back corner I could see what looked like pack of rubbers for large dragons."

    if bangok_four_playerhasdick == True:
        menu:
            "Use protection":
                m "I opened one of the small condom packets and rolled it over my dick."
                play sound "fx/unwrap.ogg"
                $ bangok_anoney_xemera2_protection_dick = True

            "Go raw.":
                $ bangok_anoney_xemera2_protection_dick = False
    else:
        m "I saw the pleasure stick that she referred to for pleasing herself on the shelf below."
        c "(Maybe I could give that a try later...)"


    if (chap2storehealth == False) and (bangok_anoney_xemera2_lick_slit == True):
        menu:
            "Seeing the large condoms in the back reminded me of something I had thought earlier":
                    $ bangok_anoney_xemera2_clean_arms = True
                    m "I remembered seeing the size of the larger dragon condoms in the grocery store and, realizing that things will probably get messy, I dug out two of the larger sized condoms from the back of the cabinet and then put them on my arms. They were ribbed part way down and should provide Emera even more pleasure"
                    play sound "fx/unwrap.ogg"

            "Just grab the lube":
                pass

    if persistent.bangok_four_playerhasdick and (not bangok_anoney_xemera2_protection_dick) and (not bangok_anoney_xemera2_clean_arms):
        m "Ignoring the condoms, I grabbed the lube and returned to Emera to kneel before her spread legs."
    else:
        m "Grabbing the lube, I returned to Emera and knelt in front of her spread legs"

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emera_presenting at Pan((960, 250), (960, 500), 4.0)

    if persistent.bangok_cloacas == True:
        m "Using my thumb and fingers to spread her slit, I squirted some of the lube into her cave. She let out a purring sound and shivered at the sensation of the cool lube in her entrance, though it quickly warmed up to her body temperature."
    else:
        m "Using my thumb and fingers to spread her upper slit, I squirted some of the lube into her cave. She let out a purring sound and shivered at the sensation of the cool lube in her entrance, though it quickly warmed up to her body temperature."

    m "For good measure, I also squirted some lube into my hand then began to spread it around both my hands and arms."

    if bangok_anoney_xemera2_clean_arms == True:
        Em laugh b "Oh, I had forgotten that those were left in there."
        Em ques b "I am most impressed with your initiative and can't wait to feel that ribbing."
        Em laugh b "Now get that arm in me."
    else:
        Em laugh b "Well, looks like you are all prepared. Now get that arm in me."

    m "Folding my thumb into my hand and bringing my fingers to a point, I gently pushed my right arm into her lubed slit."

    if persistent.c4eggs == True:
        m "I had seen some dragon eggs before at Raza's hideout and even though I had not directly seen her own eggs I had a feeling hers would be larger than my hand."
    else:
        m "I had not seen dragon eggs before, but I had a feeling hers would be larger than my hand."
    
    m "Emera let out a snarl at the feeling of my hand entering her.{w=0.5}{nw}"
    play sound "fx/varagrowl.ogg"
    m "Emera let out a snarl at the feeling of my hand entering her.{fast} She was able to take my whole hand easily due to the size difference."
    
    if persistent.bangok_watersports == True:
        m "Just past the entrance on her upper wall I could feel an opening and guessed this was her urethra. I noted where it was to investigate it later, if both of us desired."

    m "I continued to feed my arm into her, gently rocking it in."
    play sound "fx/mud.ogg"
    m "There was plenty of lubrication from her arousal as well the extra lube I had rubbed over my arm before entering."
    m "I decided to ball my fingers into a fist to imitate the head of a dragon's cock.{w=0.1}{nw}"
    play sound "fx/purr.ogg"
    m "I decided to ball my fingers into a fist to imitate the head of a dragon's cock.{fast} Emera instantly let out a purr and shivered in pleasure."

    if bangok_anoney_xemera2_clean_arms == True:
        m "My arm slowly disappeared up to my elbow and there was still length in her tunnel yet. With the condom covering halfway up my upper arm it gave me a good indication of how much there would be to her depths. By now the ribbed texture of the condom was starting to enter her."
        Em laugh b "That feels amazing. It feels so much better to have something warm and living down there instead of awkwardly trying to push in a poor substitute, and the texture on the condom feels divine."
    else:
        m "My arm was slowly disappearing up to my elbow and there was still length in her tunnel yet."
        Em laugh b "That feels amazing. It feels so much better to have something warm and living down there instead of awkwardly trying to push in a poor substitute."

    if persistent.bangok_cervpen == True:
        m "After only another minute of slowly, gradually pushing, I finally reached the limit of her tunnel, beyond which was her egg chamber."
    else:
        m "After only another minute of slowly, gradually pushing, I finally reached the limit of her tunnel, with the majority of my arm inside her."
        Em frown b "Nngh. Yes, that is as deep as you can go."

    m "Now I knew how much length I had to work with I slowly began to withdraw my now soaked arm from her tunnel. When most of my arm was out, I pushed it in again once more and set up a rhythm."
    play soundloop "fx/massage.ogg"

    $ renpy.pause (3.0)

    if bangok_four_xipsum.unplayed == False:
        if bangok_four_xipsum.vag_and_ass == True:
            c "I understand that part of your studies in culture would also include the mating rituals of dragons. I have had the chance to have an encounter with a dragon with hemipenes. When mating happens are they both in use with one in each hole?"
            Em frown b "Do you really need to know the answer now of all times?"
            Em ques b "To satisfy your curiosity; although it is unusual to find a dragon with such an abnormality."
        else:
            c "I have had an encounter with a dragon that had hemipenes and have had both passages filled. It was quite a heavenly experience."
            Em ques b "Indeed? It is unusual to come across a dragon with such an abnormality."
        Em ques b "However, there have been records indicating that they did indeed use both passageways to enter the female and that it was highly pleasurable for both partners."
        c "How would you feel about having an experience similar to what is in your records?"
        Em bangok blush b "You can do that?"
        menu:
            "Let me work my magic.":
                stop soundloop fadeout 0.5
                jump bangok_anoney_xemera2_double_fisting
            "On second thought, maybe it is best to carry on as planned.":
                jump bangok_anoney_xemera2_vaginal_only
    else:
        jump bangok_anoney_xemera2_vaginal_only

label bangok_anoney_xemera2_vaginal_only:
    if persistent.bangok_cervpen == True:
        m "Reforming my hand into a point again, I began to put pressure at the end of my stokes onto the centre of the rear wall of her tunnel"
        Em bangok blush b "You need to go faster. Faster and harder. Put your body into it."
        stop soundloop fadeout 0.5
        play soundloop "fx/massage2.ogg" fadein 0.5
        m "Gradually I could feel the barrier yielding and a hole starting to open up."
        Em "Don't stop now, [player_name]. Give it all you got!"
        m "Over the next few minutes the hole widened even more,{w=0.5}{nw}"
        play sound "fx/varagrowl.ogg"
        m "Over the next few minutes the hole widened even more,{fast} until eventually my hand pushed through."
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I broke through into her egg chamber. I could feel the smooth hard surface of her egg held within her inner castle."
        stop soundloop fadeout 0.5
        m "I stopped moving my arm with my hand in her egg chamber, just moving around the egg."
        play sound "fx/breathing.ogg"
        $ renpy.pause (5.0)
        m "Emera panted needily."
        Em "Why did you stop?"
        m "I smoothly withdrew my arm until my fist was at her entrance and punched it through her tunnel back into her egg chamber."
        play soundloop "fx/massage2.ogg"
        Em "More, More!"
        m "I quickly picked up the pace, pushing my arm deep each time, touching the egg with my knuckles."
        $ renpy.pause(3.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{w=0.8}{nw}"
        play sound "fx/bitescr.ogg"
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{fast} I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier once there had disappeared; the entrance had dilated completely."
        $ renpy.pause(0.8)
    else:
        m "I began to move my fist around inside her, stimulating her walls around the entrance to her egg chamber"
        Em bangok blush b "You need to go faster. Faster and harder, put your body into it."
        stop soundloop fadeout 0.5
        play soundloop "fx/massage2.ogg" fadein 0.5
        m "Over the next few minutes, her tunnel gradually got looser."
        Em "Don't stop now, [player_name]. Give it all you got!"
        play sound "fx/varagrowl.ogg"
        m "I could speed up my thrusts, making sure to move my wrist each time I kissed the entrance to her egg chamber with my knuckles."
        play sound "fx/breathing.ogg"
        $ renpy.pause (5.0)
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I found a particularly sensitive area near the end of her tunnel. I angled my hand so that I would continually rub this area each time I plunged my arm back in"
        $ renpy.pause(0.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{w=0.8}{nw}"
        play sound "fx/bitescr.ogg"
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{fast} I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier that until a few moments ago was at the end of her tunnel rapidly disappeared, the entrance dilating completely."
        $ renpy.pause(0.8)
        
    m "Her tunnel clenched so tight around my arm that I could no longer move it,{w=0.8}{nw}"
    play sound "fx/spray.ogg"
    m "Her tunnel clenched so tight around my arm that I could no longer move it,{fast} her opening spraying copious amounts of lubrication all over my lower body."

    if persistent.bangok_watersports == True:
        m "I suddenly felt a much warmer and wetter fluid surrounding my arm. Given the position Emera was standing, I was glad that it was moving further inside her instead of streaming out onto the floor and embarrassing her."
        m "She didn't mention that the laying hormones also made her lose control of her bladder, though it could be an evolutionary trait to provide more lubrication for the egg."
        m "I was equally glad I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    else:
        m "I am glad that I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    m "After what felt like several minutes I felt her tunnel relaxing. Though I could still feel pulses along the sides of her tunnel, now they were going in the opposite direction."
    m "Emera was breathing heavily as she spoke to me again."
    Em bangok blush b "Thank you for that. You have done it. My egg is now going to be starting its journey out of me, and for the first time I can enjoy it."
    Em "You have already done so much for me by getting this far, but I would ask you to do more."
    Em "The hormones that are released to prepare to lay the egg severely limit any discomfort I would experience from the egg passing out."
    Em "There is something that I have always wanted to try after reading about it in our records, but have not been able to do, because of my lack of a partner or flexible enough tail."
    Em "When the egg is travelling down my tunnel, are you able to stop it before it comes out and push it back?"
    c "If that is what you want."
    m "I pulled my arm back until just my hand remained inside and I could see the muscles around her groin area working to push the egg down her tunnel."
    m "The look of rapture on the dragon's face confirmed that she was as high as a stunt-performing flyer."
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the entrance to her vagina.{w=0.8}{nw}"
    play sound "fx/mud.ogg"
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the entrance to her vagina.{fast} I held the egg for a moment whilst her contractions passed, then I drove my arm back into her slick canal."
    if persistent.bangok_cervpen == True:
        m "The copious lubrication meant it was easy to push the egg back in. I pushed it back, deep inside her, until I could feel my hand slipping it through the still-dilated entrance to her egg chamber."
    else:
        m "The copious lubrication meant it was easy to push the egg back in. I even went further  than before given the entrance to her egg chamber was still dilated."
    m "It didn't appear to cause her any discomfort.{w=0.8}{nw}"
    play sound "fx/bitescr.ogg"
    m "It didn't appear to cause her any discomfort.{fast} In fact, there was another muffled roar as another set of bite marks were added to the same cushion used before."
    m "I could feel her tunnel spasm around my arm, almost in confusion as the instinct to draw the male fluids to the egg chamber was competing with the signals from her egg chamber that is currently occupied in trying to evict the egg."
    m "Some moments later, her tunnel again went limp and I moved my hand back to the beginning to prepare to go again."
    m "I repeated the operation five more times before my arm was starting to get tired. I removed it from her and finally allowed her body to expel her egg."
    $ renpy.pause (2.5)
    m "I caught the egg in my hands as it fell from her slit.{w=0.8}{nw}"
    play sound "fx/slurp.ogg"
    $ renpy.pause(0.8)
    play sound "fx/bitescr.ogg"
    m "I caught the egg in my hands as it fell from her slit.{fast} I was surprised by its weight and size: about as large as a melon. The color was a pale yellow, nearly matching her belly."
    $ renpy.pause(0.8)
    play sound "fx/breathing.ogg"
    m "Emera panted heavily, her body still in the throes of her orgasms."
    Em bangok orgasm b "That was amazing. Those old records were not wrong when they recorded their observations."
    jump bangok_anoney_xemera2_what_will_you_do

label bangok_anoney_xemera2_what_will_you_do:
    c "What will you do with the egg now?"
    Em ques b "Usually I donate it to a charity in the city. They have an anonymous drop off box here at the library."
    Em "They extract the contents of the egg, fill it with a dense foam then paint designs on the shell, with the eggs then sold as souvenirs, presents and the like."
    Em normal b "The profits gained are then shared with orphanages and counseling for low income families all over."
    Em frown b "The level of pleasure that is had by both partners from encouraging the beginning of the cycle can fuel an addiction."
    Em "The consequences of which are seen in the large range of contraceptives. You must have seen them at the local grocery store. This is also unfortunately evident in the unwanted fertilized eggs that are sometimes also left in the donation box."
    c "Really?"
    Em normal b "Of course any eggs left in the box at the end of the day are checked by simply shining a light through them. Given the shells are slightly translucent, it is possible to tell if they are viable or not."
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
    c "Emera, there is something new I wish to try. You found the experience of one of my arms inside you was amazing. Now that you have laid your egg, how about both arms?"
    Em laugh b "I am certainly interested enough to try."
    m "I pulled the mat over to a wall, then knelt down against the wall facing her. I bought my arms together, and twined my fingers together."
    c "You will need to do the work, I can't brace against you with both my arms inside."
    m "Emera backed up slowly until my clenched hands were under her tail."
    if persistent.bangok_cloacas == True:
        m "I lined up my arms with her cloaca, which was still swollen and spread from passing the egg."
    else:
        m "I lined up my arms with her vaginal slit, which was still swollen and spread from passing the egg."
    $ renpy.pause (1.5)
    m "Emera leaned back until she forced my hands into her slit."
    Em blush b "Yes, I feel that now.{w=0.8}{nw}."
    play sound "fx/varagrowl.ogg"
    Em blush b "Yes, I feel that now.{fast} Both your arms together will be larger than any dragon cock."
    m "Emera continued to lean back, pushing more and more of my arms into her."
    play sound "fx/mud.ogg"
    Em "Gosh your arms are so big when pressed together like that."
    m "She continued to back up until my elbows had entered her slit."
    m "Emera started to rock her body back and forth,{w=0.8}{nw}"
    play soundloop "fx/massage.ogg"
    m "Emera started to rock her body back and forth,{fast} sliding my arms up and down her tunnel."
    $ renpy.pause (2.5)
    Em "So, so big, it is like the egg yet all the way along."
    m "Now that she had gotten used to my arms inside her she decided to push even harder."
    $ renpy.pause (2.5)
    m "I could feel more of my arms sliding inside,{w=0.8}{nw}"
    play sound "fx/varagrowl.ogg"
    m "I could feel more of my arms sliding inside,{fast} as her slit stretched even wider."
    stop soundloop fadeout 0.5
    play soundloop "fx/massage2.ogg" fadein 0.5
    m "Emera sped up but did not move as far, keeping my forearms within her warmth."
    Em "Almost there...., nearly at the end of my tunnel, just a little further"
    m "I can feel her passage starting to clamp down. Emera really had to put some effort into forcing me through."
    play sound "fx/breathing.ogg"
    $ renpy.pause (7.0)
    m "Finally Emera gave one last shove back and my arms reached the end of her tunnel."
    Em orgasm b "Words... so... full"
    stop soundloop fadeout 0.5
    m "Her tunnel clamped down, hard.{w=0.8}{nw}"
    play sound "fx/roar2.ogg"
    m "Her tunnel clamped down, hard.{fast} As I was trapped between her and a wall, pinned in place, I could do almost nothing but enjoy the sight of the dragon in the throes of the longest orgasm she had ever experienced."
    $ renpy.pause (1.5)
    m "I did what I could, which was to wiggle my arms to prolong her pleasure."
    $ renpy.pause (1.5)
    m "A fresh flood of juices spurted out around my arms, spattering my chest in the fresh, warm liquid."
    play sound "fx/water2.ogg"
    $ renpy.pause (2.5)
    m "Finally, after what felt twice the length of her previous orgasms, her tunnel finally relaxed,{w=0.8}{nw}."
    play sound "fx/rolldownhill.ogg"
    m "Finally, after what felt twice the length of her previous orgasms, her tunnel finally relaxed,{fast} her legs become weak, and she tumbled to the mat on her side, pulling me down too."
    play sound "fx/breathing.ogg"
    m "After minutes of laying on the mat, my arms still trapped within her passage, they were starting to ache."
    c "Emera, could you move forwards so I can pull my arms out?"
    Em blush b "Oh of course. Apologies, I don't know what came over me. The pleasure was just so, so very good and then I just felt so weak, I couldn't continue standing."
    m "She began to move forward, slowly pulling my arms out of her slit, leaving a trail of her juices on the mat beneath them."
    m "She let out a snarl as my hands finally left her now thoroughly abused slit."
    play sound "fx/varagrowl.ogg"
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
    m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until we could both take showers."
    $ renpy.pause (2.5)
    play sound "fx/rub2.ogg"
    $ renpy.pause (2.5)
    jump bangok_anoney_xemera2_conclusion

label bangok_anoney_xemera2_satisfy_male:

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night

    show emera normal b

    c "Now that I have satisfied you, I wish to take care of myself. Given how large your reproductive passage is, I would like to try your other entrance."
    Em bangok blush b "Of course ambassador. My body is yours to use after what you have done for me. It is quite fair that you should also get some pleasure out of this."

    show emera bangok blush b flip:  #Trying to do something similar to the anna lays down in anna chapter 2, rotate property is only clockwise. not sure how to do counter clockwise.
        xanchor 0.5
        ease 1.0 pos (0.8, 1.0)
    with None
    $ renpy.pause(0.7)
    show emera bangok blush b flip:
        pos (0.2, 1.0)
    with dissolve
    m "I asked Emera to roll over onto her back.{w=0.8}{nw}"
    play sound "fx/leather.ogg"
    m "I asked Emera to roll over onto her back.{fast} Then I got up from the floor and went over to the fruit bowl on one of the cabinets."
    play sound "fx/basket.ogg"
    m "Selecting three firm fruits that were slightly larger than my hand I returned to Emera."
    show emera ques b flip
    m "Emera, on her back, gave me a confused look until I spread apart the large slit that her egg had recently come out of, which was still very wet with the multiple orgasms she'd experienced earlier."
    show emera bangok blush b flip
    m "I started to push the fruits into her tunnel, until all three were in her birthing passage."

    if persistent.bangok_cloacas == True:
        m "Then I lay atop her, reached down to spread apart her cloaca, found the opening to her anal passage, then buried my lubed length within."
    else:
        m "Then I lay atop her, reached down to finding the lower slit leading to her anal passage, then buried my lubed length within."
    
    m "Our lower bodies were covered with the slippery mating fluids from her orgasms, enabling me to slide my body quickly over her scales as I thrust into her anal passage."
    play soundloop "fx/flap1.ogg"
    m "I could feel her mating muscles clamping down on the fruit in her canal, the contractions against which then also slightly contracted her anal passage."
    Em bangok blush b flip "Oh this is new, I have never thought of using food items in this way, or using my other tunnel for such..."
    m "I had been rock hard through the whole egg laying procedure, so I knew that I would not last long."
    m "I continued to thrust into her, the fruits in her tunnel moving around with the motion of my hips."
    play sound "fx/varagrowl.ogg"
    m "The pressure of the fruits against the entryway of her egg chamber caused her to moan in pleasure."
    m "I could feel my orgasm building up. I was not going to last much longer."
    stop soundloop fadeout 0.5
    if bangok_anoney_xemera2_protection_dick == True:
        m "It was only a couple more thrusts until I blew my load, the condom containing my relatively small spurts compared to what a dragon would probably produce."
    else:
        m "It was only a couple more thrusts until I blew my load, my relatively small spurts compared to what a dragon would probably produce still painting the walls of her lower passage."
    m "My last thrust, coupled with the movement from the fruits in her tunnel threw Emera into yet another orgasm.{w=0.8}{nw}"
    show emera bangok orgasm b flip
    $ renpy.pause (1.5)
    play sound "fx/bitescr.ogg"
    $ renpy.pause(0.8)
    m "My last thrust, coupled with the movement from the fruits in her tunnel threw Emera into yet another orgasm.{fast} Her lower passage tightened further around me, milking out of me a few extra spurts."
    m "Once her tunnel loosened up to allow me to pull out I got up from her underside and proceeded to reach into her vaginal passage to remove the fruit."
    show emera bangok blush b flip
    play sound "fx/varagrowl.ogg"
    m "Emera gave a moan each time her lips were stretched by their expulsion."
        
    if bangok_anoney_xemera2_clean_arms == True:

        m "I reached down and quickly removed the condoms from my arms; the rubbers had served their purpose in keeping at least some of me relatively clean."

    if (persistent.bangok_watersports == True) and (bangok_four_playerhasdick == True):

        m "Given that it had been several hours since I had visited a restroom, nature suddenly decided to make its call."
        c "(Oh crap what do I do?)"
        c "(I can't go outside the office to the washroom, not in this state.)"
        c "(The last thing I want to do is accidently leave any evidence of our activities, especially with the heightened smell of the dragons.)"
        menu:
            "Don't think about it, just get cleaned up so you can go to the restroom.":
                pass

            "Relieve yourself inside Emera.":
                jump bangok_anoney_xemera2_ws_relief

    jump bangok_anoney_xemera2_toweling_showercomment_conclusion


label bangok_anoney_xemera2_ws_relief:
    c "Emera, I'm afraid I desperately need to use the restroom. I..."
    Em bangok blush b flip "Oh, I understand. I have had to do the same thing myself after a particularly long session."
    c "No, I mean I need to use the restroom now, and I don't think I should leave your office in this state."
    Em ques b flip "Ah, I see. Well, I am aware some dragons fetishize the practice of relieving themselves in their partner, and I have immunized myself to the thought."
    Em laugh b flip "Experiencing it in practice is another matter, but I am willing to let you do so if you wish."
    if bangok_anoney_xemera2_protection_dick == True:
        m "Looking "
        menu:
            "Urinate unprotected.":
                m "I reached down and quickly removed the condom from my shaft."
                $ bangok_anoney_xemera2_protection_dick = False
            "Urinate in the condom.":
                pass
    label .ws_menu:
    menu:
        "Ass." if not persistent.bangok_cloacas:
            jump .ass
        "Vagina." if not persistent.bangok_cloacas:
            jump .vag
        "Anal vent." if persistent.bangok_cloacas:
            jump .ass
        "Cloaca." if persistent.bangok_cloacas:
            jump .vag
        "Mouth." if bangok_four_xemera2_ws_mouth_unasked:
            $ bangok_four_xemera2_ws_mouth_unasked = False
            c "May I use your mouth?"
            Em frown b flip "While I'm immunized to the thought, I highly doubt I'm immunized to the taste."
            Em ques b flip "I'd prefer if you keep this far from my face."
            jump .ws_menu
        "Urethra.":
            jump .urethra

    label .ass:
        c "May I use your ass?"
        Em ques b flip "If you so desire."
        m "Emera was still laying on her back{w=0.8}{nw}"
        play sound "fx/purr.ogg" 
        if persistent.bangok_cloacas:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her anal vent."
            m "Emera's cloaca was still spread wide from her earlier activities. I stuck my dick in the mess at her vaginal entrance, evidence from the many orgasms that Emera had." 
            m "Once my dick was thoroughly coated in her juices, I pushed it into her anal vent."

        else:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her ass"
            m "Emera's vagina was still spread wide from her earlier activities. I stuck my dick in the mess at her vaginal entrance, evidence from the many orgasms that Emera had." 
            m "Once my dick was thoroughly coated in her juices, I reached down to spread her ass and pushed my dick into her hole."
        show emera bangok blush b flip with dissolve
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        if bangok_anoney_xemera2_protection_dick == True:
            m "After adjusting my position to get both of us comfortable, I released my bladder into the reservoir of the condom, inflating it with my urine to mix with my earlier deposit in her rear."
        else:
            m "After adjusting my position to get both of us comfortable, I released my bladder into her rear, spraying away my cum with warm urine."
        $ renpy.pause (0.5)
        Em laugh b flip "Mmm. That feels... warm. Certainly far from unpleasant."
        stop soundloop fadeout 2.0
        if bangok_anoney_xemera2_protection_dick == True:
            m "When I was done, I slowly slid my penis free of the condom, leaving its overfilled reservoir within her rear, clenched shut by her anal sphincter."
        else:
            play sound "fx/uncork.ogg"
            m "When I was done, I quickly pulled out."
        stop soundloop fadeout 2.0
        jump .done

    label .vag:
        if persistent.bangok_cloacas:
            c "May I use your vagina?"
        else:
            c "May I use your cloaca?"
        show emera laugh b flip with dissolve
        m "Emera's expression changed to one both flustered and curious."
        Em bangok blush b "Well... I suppose. If you so desire."

        m "Emera was still laying on her back{w=0.8}{nw}"
        play sound "fx/purr.ogg" 
        if persistent.bangok_cloacas == True:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her cloaca."
            m "Emera's cloaca was still spread wide from her earlier activities. I stuck my dick in the mess at her vaginal entrance, evidence from the many orgasms that Emera had, and pushed inwards." 
        else:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly, and this time stuck my dick insie her vagina."
            m "Emera's vagina was still spread wide from her earlier activities. I stuck my dick in the mess at her entrance, evidence from the many orgasms that Emera had, and pushed inwards."
        show emera bangok blush b flip with dissolve
        play soundloop "fx/faucet1.ogg" fadein 2.0
        queue soundloop "fx/faucet2.ogg"
        if bangok_anoney_xemera2_protection_dick == True:
            m "After adjusting my position to get both of us comfortable, I released my bladder into the reservoir of the condom, filling it with my urine in the soft, warm confines of her canal."
        else:
            m "After adjusting my position to get both of us comfortable, I released my bladder into her vagina, spraying away my cum within her body."
        $ renpy.pause (0.5)
        Em laugh b flip "That is a... unique feeling. Warm and rather pleasurable."
        stop soundloop fadeout 2.0
        if bangok_anoney_xemera2_protection_dick == True:
            m "When I was done, I slowly slid my penis free of the condom, leaving its reservoir filled with warm urine within her vagina."
        else:
            m "When I was done, I held my position for a few moments, savoring the feeling of Emera's insides' wet embrace."
            m "Then I slowly pulled out, wiping my tip on her outer lips to clean myself off as best as possible given our circumstances."
        jump .done


    label .urethra:
        m "Remembering the discovery of where Emera's urethra was, I hoped that her hormones would still prevent any discomfort as came up with my idea."
        c "Maybe... since you're so much larger than I am, I could urinate into your bladder?"
        Em laugh b flip "Why... I have never heard of such a thing."
        Em bangok blush b flip "I cannot say I am displeased with the idea... I am curious to see how it would feel."
        Em ques b flip "Proceed."
        m "Emera was still laying on her back{w=0.8}{nw}"
        play sound "fx/purr.ogg" 
        if persistent.bangok_cloacas == True:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her cloaca."
            m "Emera's cloaca was still spread wide from her earlier activities. Reaching back I spread her slit easily and found her urethra exactly where I had remembered it."
        else:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her vagina."
            m "Emera's vagina was still spread wide from her earlier activities. Reaching back I spread her slit easily and found her urethra exactly where I had remembered it."
        show emera ques b flip
        if bangok_anoney_xemera2_protection_dick == True:
            m "Emera had a bemused look on her face as I reached down with my other hand and pushed my condom-wrapped dick into her urethra."
        else:
            m "Emera had a bemused look on her face as I reached down with my other hand and pushed my dick into her urethra."
        m "I was dreading her reaction in case she faced too much discomfort, however after waiting a few moments without her expressing being in pain I felt relieved that her hormones must still be working."
        Em normal b flip "That feels... odd. I have never come across records that have shown that place to be penetrated, however given the larger size of dragons and not wanting to cause pain to a mate it is obvious why."
        c "It doesn't hurt?"
        Em bangok blush b flip "No. As I said it just feels odd. I would not like to be mated down there; even Earth dragons are not completely resistant in areas not expected to be mated. However I do want you to continue."
        m "I continued to press further in, the lube from her vagina helping to quicken the journey."
        m "I came to her sphincter seperating the entrance to her bladder. I gently put pressure until the head of my dick pushed through."
        show emera normal b flip
        $ renpy.pause (0.5)
        show emera frown b flip with dissolve
        m "Emera let out a gasp. I could tell from her face this was at least mildly uncomfortable for her."
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        if bangok_anoney_xemera2_protection_dick == True:
            m "I quickly released my bladder into the reservoir of the condom, inflating it within her bladder, rushing to finish my business."
        else:
            m "I quickly released my own bladder inside her, rushing to finish my business."
        $ renpy.pause (1.5)
        stop soundloop fadeout 2.0

        if bangok_anoney_xemera2_protection_dick == True:
            m "When I was done, I quickly began to slide my penis free of the condom, leaving its overfilled reservoir within her bladder, clenched shut by her muscles."
        else:
            play sound "fx/uncork.ogg"
            m "When I was done, I quickly pulled out."
        show emera normal b flip with dissolve
        jump .done

    label .done:
        $ renpy.pause (0.5)
        show emera laugh b flip with dissolve
        m "I felt her rest one of her front paws pat me on my shoulder and I just laid a while, enjoying the warmth of her body heat."
        Em normal b flip "If everything is done, then we ought to clean up. It is already very late and you will probably be wanting to return to your apartment."
        play sound "fx/cabinet.ogg"
        $ renpy.pause (0.5)
        play sound "fx/rub2.ogg"
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

    c "Emera, now that you are satisfied, would I be able to borrow your pleasure stick to help satisfy my own needs?"
    Em bangok blush b "Of course. Though are you sure you would be able to take it?"

    if bangok_four_malepartners > 1:
        c "As I have said, I have had other encounters with male dragons and have been able to take them. A dildo of the same size will be manageable."

    else:
        c "I used to have 'toys' for my own pleasure back in the human world. I had quite a nice collection of what I believe to be draconic size with which to state my desires when wanting to get a little rough."

    m "I went to the cupboard {w=0.8}{nw}."
    play sound "fx/cabinet.ogg"
    m "I went to the cupboard.{fast} And retrieved the dildo from the lower shelf."
    m "Examining the dildo, I found it was made out of a hard rubber and nearly the length of my arm, with a rounded tip. The head bulged out slightly about the size of my fist."
    m "The rest of the shaft, starting out at the base, was the thickness of my bicep decreasing to the diameter of my wrist just below the head. There was a length of wood sticking out of the base, evidently to make it easier to hold when in use."

    show emera normal b flip:  #Trying to do something similar to the anna lays down in anna chapter 2, probably got this wrong.
        xanchor 0.5
        ease 1.0 pos (0.8, 1.0)
    with None
    $ renpy.pause(0.7)
    show emera normal b flip:
        pos (0.2, 1.0)
    with dissolve
    play sound "fx/leather.ogg"
    m "Emera had rolled onto her back"
    Em laugh b flip "Come over here and lay on me whilst you have your fun."
    m "I sat on her lower belly and bent forwards to her groin."
    m "I pressed the dildo to Emera's vagina and pushed it in.{w=0.8}{nw}"
    play sound "fx/mud.ogg"
    m "I pressed the dildo to Emera's vagina and pushed it in.{fast} It slid in easily due to her tunnel being lubricated and still stretched from passing the egg."
    m "I then pulled the stick out of her, ensuring it was thoroughly coated in her fluids before placing the tip at my entrance and gently easing it in."
    m "I let out a low moan as I could feel the head stretch my outer lips."
    m "I continued to push it in slowly until the thickest part was inside, then all it took was a light clench to pull the rest of the head inside."
    c "Yes, I was ready for this..."
    m "It was amazing to feel this full, and it was only the head."
    m "I continued to gently push it in further. After about half of the way down I felt the head of the toy kiss my cervix."

    if persistent.bangok_cervpen == True:
        m "Knowing that I could take it further I continued to put pressure on my cervix, twisting the toy slightly to dilate it."
        m "I could feel my cervix loosening up as I started to lightly thrust the toy a few inches back and forth."
        m "A few moments later and I felt the head pop through and into my womb."

    else:
        m "This is as much as I can take, given the size of the toy."
        m "I started to lightly thrust the toy a few inches back and forth, getting used to the dildo."

    m "Emera put her hand on my belly and could feel the progress of the toy inside me."
    Em bangok blush b flip "I am impressed, it seems you have indeed had experience enough to take it."
    c "Thank you"
    m "Now that my vagina had conformed to the dildo safely I laid fully on my back on Emera."
    play soundloop "fx/massage.ogg"
    m "The dragon continued to rub her hand over my belly, feeling the toy through my body."
    play sound ["fx/rub1.ogg", "fx/wipe.ogg", "fx/rub1.ogg", "fx/wipe.ogg", "fx/rub1.ogg"]
    $ renpy.pause (5.5)
    stop soundloop fadeout 0.5
    m "After what felt like an age, but was probably only about five minutes my orgasm washed over me, I went limp as my body was consumed by euphoria."
    m "I decided to just lay there for a while, toy still hanging out of my vagina and bask in the afterglow on the warm belly of Emera."
    Em "If everything is done, then we ought to clean up. It is already very late and you will probably be wanting to back to your apartment"
    if persistent.bangok_cervpen == True:
        m "I gave a nod and reached down to gently tug the toy out of me, giving a shudder of pleasure as the head of the toy first left my womb, then stretched my lips."
    else:
        m "I gave a nod and reached down to gently tug the toy out of me, giving a shudder of pleasure as the head of the toy stretched my lips."
    play sound "fx/uncork.ogg"
    m "Emera took her toy off of me and stuck it in her mouth, licking it clean. afterwards she gave it back to me and I put it back into the cupboard"
    play sound "fx/cabinet.ogg"
    m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until showering."
    $ renpy.pause (0.5)
    play sound "fx/rub2.ogg"
    jump bangok_anoney_xemera2_conclusion

label bangok_anoney_xemera2_double_fisting:

    if persistent.bangok_cloacas == True:
        m "Spreading her cloaca wide with one hand, I slowly withdrew my arm from her vaginal tunnel until it was out completely. It was coated in a slick mixture of lube and her plentiful arousal."
        m "I moved my arm slightly lower, the target being her anal passage towards the bottom of her slit. Once again I formed my fingers to a point and pushed at her anal entrance."
        m "Now that one arm was in the right place, I pushed my other arm back into her vacated vaginal canal, stretching her cloaca wide around both my arms."
    else:
        m "Spreading her scales around her anus with one hand, I slowly withdrew my arm from her vaginal slit until it was out completely. It was coated in a slick mixture of lube and her plentiful arousal."
        m "I moved my arm slightly lower, the target being her anal passage in her spread lower slit. Once again I formed my fingers to a point and pushed at her anal entrance."
        m "Now that one arm was in the right place, I removed the other from holding open her anal slit and moved it up to push back into her vacated vaginal canal, stretching both entrances wide around my arms."

    m "I started to push both my arms into her.{w=0.1}{nw}"
    play sound "fx/mud.ogg"
    m "I started to push both my arms into her.{fast} There was not much resistance due to the lube."
    c "How does that feel?"
    Em bangok blush b "MMmm! Having both my passages stretched at the same time is not something I had ever thought about before. I did once take my pleasure stick up there, but the feeling in isolation was not as pleasant as from my vagina."
    Em "But having both at once is just adding to the pleasure."
    if bangok_anoney_xemera2_clean_arms == True:
        m "By now my elbows are sinking in and the ribbed texture of the condoms on my arms was entering her."
    else:
        m "By now my elbows are sinking into her."
    play soundloop "fx/massage.ogg" fadein 0.5
    m "I pulled back both my arms and began alternating them in a piston motion pushing one in as the other was pulled almost out."
    m "Gradually I could feel her tunnels loosening,{w=0.1}{nw}"
    play sound "fx/water1.ogg"
    m "Gradually I could feel her tunnels loosening,{fast} her outer lips becoming more relaxed and her arousal flowing in a small trickle, keeping both arms topped up with fresh juices."
    m "By now I was able to push both arms halfway up my biceps into her and in her vagina, I could feel the entrance to her egg chamber once again."
    if persistent.bangok_cervpen == True:
        m "Reforming my hand into a point again, I began to put pressure at the end of my stokes onto the centre of the rear wall of her tunnel"
        Em bangok blush b "You need to go faster. Faster and harder. Put your body into it!"
        stop soundloop fadeout 0.5
        play soundloop "fx/massage2.ogg" fadein 0.5
        m "Gradually I could feel the barrier yielding and a hole starting to open up."
        Em "Don't stop now, [player_name]. Give it all you got!"
        m "Over the next few minutes the hole widened even more{w=0.5}{nw}"
        play sound "fx/varagrowl.ogg"
        m "Over the next few minutes the hole widened even more{fast} until eventually my hand pushed through."
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I broke through into her egg chamber. I could feel the smooth hard surface of her egg held within her inner castle."
        stop soundloop fadeout 0.5
        m "I stopped moving my arm with my hand in her egg chamber, just moving around the egg."
        play sound "fx/breathing.ogg"
        $ renpy.pause (5.0)
        m "Emera panted needily."
        Em "Why did you stop?"
        m "I smoothly withdrew both my arms until my fists were at her entrances, then punched both through her tunnels, with one sinking back into her egg chamber."
        play soundloop "fx/massage2.ogg"
        Em "More, More!"
        m "I quickly picked up the pace, pushing my arms deep each time, touching the egg with my knuckles."
        $ renpy.pause(3.5)
        Em bangok orgasm b "I am almost there... I just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{w=0.8}{nw}"
        play sound "fx/bitescr.ogg"
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{fast} I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier once there had disappeared; the entrance had dilated completely."
        $ renpy.pause(0.8)
    else:
        m "I began to move my fists around inside her, stimulating her walls around the entrance to her egg chamber and the wall of her colon closer to her reproductive center."
        Em bangok blush b "You need to go faster. Faster and harder. Put your body into it!"
        stop soundloop fadeout 0.5
        play soundloop "fx/massage2.ogg" fadein 0.5
        m "Over the next few minutes, her tunnel gradually got looser."
        Em "Don't stop now, [player_name]. Give it all you got!"
        play sound "fx/varagrowl.ogg"
        m "I could speed up my thrusts, making sure to move my wrist each time I kissed the entrance to her egg chamber with my knuckles."
        play sound "fx/breathing.ogg"
        $ renpy.pause (5.0)
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I found a particularly sensitive area near the end of her tunnel. I angled my hand so that I would continually rub this area each time I plunged both arms back in"
        $ renpy.pause(0.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{w=0.8}{nw}"
        play sound "fx/bitescr.ogg"
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{fast} I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier that until a few moments ago was at the end of her tunnel rapidly disappeared, the entrance dilating completely."
        $ renpy.pause(0.8)

    m "Her tunnel clenched so tight around my arms that I could no longer move them,{w=0.8}{nw}"
    play sound "fx/spray.ogg"
    m "Her tunnel clenched so tight around my arms that I could no longer move them,{fast} her vagina spurt copious amounts of lubrication all over my lower body and genitals."

    if persistent.bangok_watersports == True:
        m "I suddenly felt a much warmer and wetter fluid surrounding the arm in her birthing passage. Given the position Emera was standing, I was glad that it was moving further inside her."
        m "She didn't mention that the laying hormones also made her lose control of her bladder, though it could be an evolutionary trait to provide more lubrication for the egg."
        m "I found myself glad I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    else:
        m "I found myself glad that I had removed my clothing and now appreciated why she performed this on an easy to clean mat."

    m "After what felt like minutes I felt her passageways relaxing, though I could still feel pulses along the sides of her birthing tunnel, now going in an outward direction."
    m "Emera was breathing heavily as she spoke to me again."
    Em bangok blush b "Thank you for that. You have done it. My egg is now going to be starting its journey out of me, and for the first time I can enjoy it."
    Em "You have already done so much for me by getting this far, but I would ask you to do more."
    Em "The hormones that are released to prepare to lay the egg severely limit any discomfort I would experience from the egg passing out."
    Em "There is something that I have always wanted to try after reading about it in our records, but have not been able to do, because of my lack of a partner and of a flexible enough tail."
    Em "When the egg is travelling down my tunnel, are you able to stop it before it comes out and push it back?"
    m "I started to pull my arm out of her anal passage When I felt her muscles clamp down hard on my arm."
    Em "Please can you leave it in? I want to see how it feels expeling the egg with my lower passage filled. If I like it in the future, maybe I shall leave my pleasure stick in there whilst I lay my egg."
    c "If that is what you want."
    m "I pulled back my arm that was in her vagina until just my hand remained inside, and I could see and feel the muscles around her groin area working to push the egg down her tunnel."
    m "I could feel those same contractions mirrored in her anal passage as her muscles squeezed my arm."
    m "The look of rapture on the dragon's face confirmed that she was as high as a stunt-performing flyer."
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the entrance to her vagina.{w=0.8}{nw}"
    play sound "fx/mud.ogg"
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the entrance to her vagina.{fast} I held the egg for a moment whilst her contractions passed, then I drove my arm back into her slick canal."
    if persistent.bangok_cervpen == True:
        m "The copious lubrication meant it was easy to push the egg back in. I pushed it back, deep inside her, until I could feel my hand slipping it through the still-dilated entrance to her egg chamber."
    else:
        m "The copious lubrication meant it was easy to push the egg back in. I even went further than before given the entrance to her egg chamber was still dilated."
    m "It didn't appear to cause her any discomfort.{w=0.8}{nw}"
    play sound "fx/bitescr.ogg"
    m "It didn't appear to cause her any discomfort.{fast} In fact, there was another muffled roar as another set of bite marks were added to the same cushion she had abused before."
    m "I could feel her tunnels spasm around my arms, almost in confusion as the instinct to draw the male fluids to the egg chamber was competing with the signals from her egg chamber that is currently occupied and trying to evict the egg."
    m "Some moments later, her tunnels again went limp and I moved my hand back to the beginning of her birthing passage to prepare to go again."
    m "I repeated the operation five more times before my arms were starting to get tired. I removed them from her finally, allowing her body to expel her egg."
    $ renpy.pause (2.5)
    m "I caught the egg in my hands as it fell from her slit.{w=0.8}{nw}"
    play sound "fx/slurp.ogg"
    $ renpy.pause(0.8)
    play sound "fx/bitescr.ogg"
    m "I caught the egg in my hands as it fell from her slit.{fast} I was surprised by its weight and size: about as large as a melon. The color was a pale yellow, nearly matching her belly."
    $ renpy.pause(0.8)
    m "Emera panted heavily as she came down from her high."
    play sound "fx/breathing.ogg"
    Em bangok orgasm b "That was amazing. I had no idea that having something in my lower passage could feel so good. Those old records were not wrong when they recorded their observations."
    jump bangok_anoney_xemera2_what_will_you_do

label bangok_anoney_xemera2_massage_only:
    $ bangok_anoney_xemera2_massage_only = True
    Em normal b "Yes, it is just more comfortable to lay on the mat than the floor, plus allows all around access without having to move once the process is started."
    m "I nodded."
    m "I pushed my upper body up to be able to reach the hard plates on her back and as before used my weight on the muscles beneath."
    Em mean b "Oh, I could just lay like this with you massaging my back forever. Have you perhaps had any more thoughts about becoming my assistant once all this ambassador business wraps up?"
    m "I looked up from digging my palm into her back to answer her question."
    c "I do not think it would be wise to do that, as much as it would be fascinating to learn more of dragon culture, you have said before you wish to start a family."
    c "I can't give you a family, and I would not want to come between you and your future mate, once you have found a suitable suitor."
    m "I moved to her rear, kneading her thighs and rump."
    m "Emera took a deep breath and glanced at the ceiling, analyzing my response no doubt having an internal argument over how to reply."
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
    show emera normal b with dissolve
    $ renpy.pause (3.3)

    if bangok_anoney_xemera2_massage_only == True:
        Em laugh b "Thank you again for your wonderful massage. I feel great and the tension that had been building up is gone."
        Em ques b "I assume you can find your way back to your apartment?"
        c "Yes I can. I am glad to have helped. I do hope that you will chill out a bit more, and think about the outcomes of what you want for yourself."
        Em normal b "I shall try [player_name]."
        c "Goodnight."
        Em "Goodnight."
    elif bangok_anoney_xemera2_refuse_participate == True:
        Em frown b "I am disappointed that you would not help me, however I did still appreciate the massage. I assume you can find your way back to your apartment?"
        m "I nodded in reply."
        c "Goodbye."
        Em normal b "Goodbye."
    else:
        Em bangok blush b "Thank you again for your wonderful massage and for making tonight my best evening in a long time."
        Em laugh b "I feel great. The tension that had been building up is gone and I have been able to live one of my dreams."
        m "Bending down to the floor to pick up her egg, a movement she must be well practiced with by her motions, she held out her front paw, offering it to me."
        Em normal b"As a token of gratitude for providing your exquisite service, please accept my egg as a reminder of this wonderful evening and the time we shared."
        menu:
            "Accept.":
                m "I reached forward with my hands and wrapped them around the egg, carefully taking and hugging it to my chest."
                c "Thank you for this unique gift, I shall make sure to look after it well."
                c "(How would I even go about preserving it without raising questions?)"
                # So, yeah, how _would_ the player not raise a bunch of questions preserving it?
                # c "(I shall have to take it to the lab in order for it to be preserved properly.)"
            "Reject.":
                c "Sorry but I can't accept this gift. If it were to come to notice by either dragons or the humans back home, then I could be in serious trouble as to how I had gotten it."
                m "I saw Emera's head droop as she heard my refusal of her gift."
                Em frown b "Of course. I understand that it could cause trouble going forwards. The negotiations are still ongoing and, as you said, if it is discovered by the humans then it could lead to difficult questions."
                m "Seeing her crestfallen look, I stepped closer and put my hand on her other shoulder."
                c "I wish that times were better and that I could accept your gift, really I do."
        Em ques b "I assume you can find your way back to your apartment?"
        c "Yes I can. I am glad to have helped. I do hope that you will chill out a bit more and think about the outcomes of what you want for yourself."
        Em normal b "I shall try [player_name]."
        c "Goodnight."
        Em "Goodnight."


    stop music fadeout 2.0
    scene black with dissolvemed

    $ renpy.pause (1.0)
    play sound "fx/door/lock.ogg"
    $ renpy.pause (1.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.0)
    play sound "fx/door/close2.wav"
 
    scene bangok_anoney_library_corridor_night with dissolvemed

    $ renpy.pause (0.5)

    if (persistent.remy1played == True) and (remystatus == "good") or (remystatus == "neutral"):
        m "As I left Emera's office and walked down the corridor I could see that the light was on Remy's office was on and faint sounds of a computer game could be made out."
        m "I paused briefly outside the door and wondered if he is making progress on that RPG I accidentally broke."
    else:
        m "As I left Emera's office and walked down the corridor I could see that there was a light on in the next office down."
        m "I paused briefly outside the door to read the door plaque:"
        m "{size=+10}Head Archivist{/size}"
        m "I guessed this was probably Remy's office."
    play sound "fx/steps/clean2.wav"
    scene black with dissolvemed

    $ renpy.pause (0.5)
    play sound "fx/door/door_open.wav"
    scene o3
    play music "mx/campfire.ogg" fadein 2.0

    $ renpy.pause (3.3)
    play sound "fx/door/close2.wav"
    m "Soon I had returned home."

    if bangok_anoney_xemera2_refuse_participate == True:
        m "After cooling off during the walk home, I thought maybe I had made the wrong choice in refusing her offer."
        c "(Emera did seem heartbroken when I had refused. If only my head wasn't so much of a mess with the police investigation and the responsibility I feel being an ambassador. What could have happened?)"
        c "(Ah well, it would be extremely irresponsible of me to go back in time for this non-emergency, even if I did know the coordinates to before this evening's events.)"
        c "(Well, time for bed. Hopefully tomorrow will be a better day.)"
    elif bangok_anoney_xemera2_massage_only == True:
        c "(I hadn't thought I would be paying Emera a return visit, but the evening was pleasant enough.)"
        c "(It was nice to get to know her private side and to know that she can confide in me given my unique position as ambassador.)"
        c "(Well, time for bed. Let's see what tomorrow brings.)"
    else:
        c "(I hadn't even thought I would be paying Emera a return visit. Not only did I give her a massage, but I allowed her to experience pleasure she thought she would only be able to dream of.)"
        c "(It was nice to get to know her private side and to know she can confide in me given my unique position as ambassador.)"
        c "(Well, time for bed, Let's see what tomorrow brings.)"
    stop music fadeout 2.0
    scene black with dissolvemed
    call _mod_incc from bangok_anoney_xemera2_mod_incc
    jump _mod_fixjmp
