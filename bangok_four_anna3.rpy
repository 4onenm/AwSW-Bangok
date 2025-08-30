label bangok_four_anna3_orifices:
    An "I'd reconsider whether I want to get close enough to examine mucosa and orifices."
    if bangok_four_anna2.annacame == True:
        show anna smirk b with dissolve
    else:
        show anna sad b with dissolve
    An "I suppose that's not relevant after the other night."
    menu:
        "Not relevant?":
            pass
        "I wouldn't stop you from examining that.":
            $ renpy.pause (0.5)
            An face b "Is that what you're into? Good to know."
            $ anna3mood -= 1
    show anna normal b with dissolve
    An "We quarantined Reza when he initially arrived here, but skipped the procedure with you. After examining Reza, we didn't think humans by themselves posed any danger."
    An "That's why I was willing to get that close to you at all."
    c "Does that mean your procedures are going to get a lot more invasive?"
    An "No. It was the other night that told me there's not much to learn there, anyway. You're already largely exposed to our baseline."
    jump bangok_four_anna3_orifices_end

label bangok_four_anna3_intimately_close:
    # Right after:
    #    An "Sure, but then I'd have to ask you if any of those actually got close enough to you."
    #    An "As in... intimately close."
    # 
    menu:
        "Nope. None. Nobody.":
            if bangok_four_anna2.unplayed == False:
                show anna smirk b with dissolve
            else:
                show anna normal b with dissolve
            An "Now why didn't that sound convincing?"
        "Just you." if bangok_four_anna2.unplayed == False:
            An "Hmm. I suppose I'll just have to believe you there."
        "At least one." if bangok_four_malepartners + bangok_four_femalepartners > 0:
            if bangok_four_anna2.unplayed == False:
                show anna smirk b with dissolve
            else:
                show anna normal b with dissolve
            An "Hmm. I suppose I'll just have to believe you there."
        "Uh... a few." if bangok_four_malepartners + bangok_four_femalepartners >= 3:
            An smirk b "Oh really? Well, tell me later."
        "Plenty. I didn't even count.":
            An normal b "Well, that's either a slightly sad lie or a very concerning public health situation."
            An "Good for you, I suppose."
    An "The point is, I don't think sticking swabs into you will get anything out of you beyond what I've already gleaned."
    jump bangok_four_anna3_intimately_close_return