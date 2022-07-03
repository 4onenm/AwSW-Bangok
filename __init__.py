import renpy.exports
import renpy.display.im as im
from renpy.display.image import ImageReference

from modloader import modinfo
from modloader.modclass import Mod, loadable_mod

import jz_magmalink as ml

def make_dev(cond):
    return '('+cond+') and (persistent.bangok_dev == True)'


def anna12():
    # Anna1
    ml.find_label('_call_skiptut_7') \
        .search_menu("Yes. I want to skip ahead.") \
        .branch() \
        .hook_to('bangok_four_anna1_skipmenu', condition='persistent.nsfwtoggle == True')
    
    ml.find_label('_call_skiptut_7') \
        .search_menu("I see.") \
        .search_menu("What a lucky coincidence.") \
        .search_menu("It would be my pleasure.") \
        .search_menu("I'll also take a coffee, please.") \
        .search_menu("I know, she can be pretty annoying.") \
        .search_menu("I've only seen glimpses, but it already sounds like a fascinating place.") \
        .search_menu("Yes, totally. You can call your lawyer if you like.") \
        .search_menu("Alright, I'll finish my drink quietly, then, if that's what you'd prefer.") \
        .search_menu("I'm being cute and spontaneous?") \
        .search_say("What do you have in mind?") \
        .hook_to('bangok_four_anna1_winmenu') \
        .search_menu("If that's what you want, so be it.") \
        .link_from('bangok_four_anna1_winmenu_afterannablood')

    ml.find_label('_call_syscheck_36') \
        .search_say("I say we both get our rewards. After all, we each made a good effort to get them.") \
        .hook_to('bangok_four_anna1_ending_merge', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("Thank you.") \
        .search_show("anna normal flip") \
        .link_from('bangok_four_anna1_goodending_after_thankyou') \
        .search_say("Despite all odds, I managed to match her perfect score in the game we played.") \
        .hook_to('bangok_four_anna1_goodending_nvl',condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("Whether anything good would come of this, I wasn't sure, either.") \
        .link_from('bangok_four_anna1_goodending_nvl_end')
        
    ml.find_label('anna1skip') \
        .search_say("I'm quite sure you will.") \
        .hook_to('bangok_four_anna1_medending', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("Well, it's up to you. Call me if you're interested.") \
        .link_from('bangok_four_anna1_medending_uptoyou') \
        .search_say("I was not sure what I had expected out of this encounter, but it certainly wasn't this.") \
        .hook_to('bangok_four_anna1_medending_nvl', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True') \
        .search_say("Even though I lost the bet, she didn't seem to mind going on a date with me, as long as she got what she wanted. Whether I would follow up on it was up to me, though.") \
        .link_behind_from('bangok_four_anna1_medending_nvl_end')

    ml.find_label('cont4') \
        .search_if() \
        .branch_else() \
        .search_say("And you're about the worst winner I've ever met.") \
        .hook_to('bangok_four_anna1_badending', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("Maybe you should step down from your high horse for once.") \
        .link_from('bangok_four_anna1_badending_end')

    # Chap2store
    ( ml.find_label('chap2storebrowsemenu')
        .search_menu("Look at the health aisle.")
        .branch()
        .search_say("(I think these ones could fit on my arm.)")
        .hook_to('bangok_four_chap2storehealth_anna12', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True')
    )

    ( ml.find_label('chap2storeques')
        .search_menu("[[Leave.]")
        .branch()
        .search_say("(I suppose that's all I can do here.)")
        .hook_to('bangok_four_chap2storehealth_checkout_anna12', condition='bangok_four_anna1_sexrequested == True and bangok_four_anna2.boughtcondoms == True and persistent.nsfwtoggle == True')
    )

    # Anna2
    sorrymenu = ml.find_label('anna2') \
        .search_menu("Go home.") \
        .branch() \
        .hook_to('bangok_four_anna2_nomorewaiting', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_python('annastatus = "bad"') \
        .link_from('bangok_four_anna2_nomorewaiting_end') \
        .search_menu("Go home.") \
        .branch() \
        .hook_to('bangok_four_anna2_nomorewaiting', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_menu("You better be.")
    
    sorrymenu.branch("You better be.") \
        .search_python('renpy.pause (0.5)') \
        .hook_to('bangok_four_anna2_wantthisornot', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("I suppose so.") \
        .link_from('bangok_four_anna2_wantthisornot_end')
    
    eveningmenu = sorrymenu \
        .hook_to('bangok_four_anna2_whatnow', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("I guess that's better than nothing.") \
        .link_from('bangok_four_anna2_alley') \
        .search_say("Let's just enjoy our romantic date in the back alley of a coffee shop.") \
        .hook_to('bangok_four_anna2_romanticdate_alley', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_menu("I already have my own dirt.") \
        .link_behind_from('bangok_four_anna2_romanticdate_alley_end') \
        .search_menu("You're a bad girl, Anna.") \
        .search_menu("Offal.") \
        .search_menu("I have no idea.") \
        .search_menu("That'd be wicked cool.") \
        .search_menu("You're a wild one, Anna.") \
        .search_menu("I can see your point. This was unusual, but fun.")
    
    eveningmenu.branch("I can see your point. This was unusual, but fun.") \
        .search_say("I can see your point. This certainly isn't how I thought the evening would go, but it was pretty fun.") \
        .hook_to('bangok_four_anna2_romanticdate_unusualbutfun', condition='persistent.nsfwtoggle == True')

    eveningmenu.search_say("We should probably leave before that senile has-been wakes up from his evening nap.") \
        .hook_to('bangok_four_anna2_romanticdate_conclusion', condition='persistent.nsfwtoggle == True') \
        .search_say("Yeah, let's go.") \
        .link_behind_from('bangok_four_anna2_romanticdate_conclusion_end')

    anna2endings = ml.find_label('anna2skip').search_if('anna2mood > 6')
    ( anna2endings
        .branch('anna2mood > 6')
        .search_say("Today was kinda fun, so maybe I should make the effort to get out every once in a while.")
        .hook_to('bangok_four_anna2_lab_good_hookupover', condition='persistent.nsfwtoggle == True and bangok_four_anna2.position is not None', return_link=False)
        .search_say("Of course.")
        .link_from('bangok_four_anna2_lab_good_hookupover_end')
    )
    ( anna2endings
        .branch('anna2mood > 1')
        .search_say("I'll think about it.")
        .hook_to('bangok_four_anna2_lab_normal_hookupover', condition='persistent.nsfwtoggle == True and bangok_four_anna2.position is not None', return_link=False)
        .search_say("Of course you didn't forget about that.")
        .link_from('bangok_four_anna2_lab_normal_hookupover_end')
    )

def anna4():
    ml.find_label("a4romance") \
        .search_menu("If you say so.").branch() \
        .search_say("Alright, alright. So fussy.") \
        .hook_to("bangok_anon_anna4_skipmenu", condition="persistent.nsfwtoggle == True")

def anna_x_damion():
    ( ml.find_label('chap2facility')
        .search_say("(Reza was allegedly here at some point. Maybe I should ask Anna.)")
        .hook_to('bangok_four_annaxdamion', condition=("(persistent.bangok_voyeurism == True) and (persistent.nsfwtoggle == True)"))
        .search_say("What exactly did you want, again?")
        .link_behind_from('bangok_four_annaxdamion_canon_questions')
    )

def bryce1_afterparty():
    ml.find_label('_call_skiptut_8') \
        .search_menu("Yes. I want to skip ahead.") \
        .branch() \
        .hook_to('bangok_four_bryce1_skipmenu', condition='persistent.nsfwtoggle == True')

    wake_menu = ml.find_label('waitmenu') \
        .search_menu("I would, but I don't think I can beat someone like you.") \
        .search_menu("I'm not buzzed.") \
        .search_menu("I'm having a drinking contest with a dragon. How could I not love this?") \
        .search_menu("That's my tactic, make you think that I'm struggling so you'll let your guard down.") \
        .search_menu("Maybe. Having a lil' fun doesn't hurt, right?") \
        .search_menu("Why are you so damn attractive?") \
        .search_menu("Mine.") \
        .search_menu("S-Suck on this, you ssscaly bastard.") \
        .search_menu("If you think I'm giving up, you're mistaken. This isn't over.") \
        .search_menu("I know when I've had enough, and it's now.") \
        .search_menu("Fine...") \
        .search_menu("Put some pepper on his nose.")

    wake_menu.add_choice("Poke him someplace special.",jump='bangok_four_bryce1_poke',condition='persistent.nsfwtoggle == True')

    wake_menu.link_behind_from('bangok_four_bryce1_nevermind')

    ml.find_label('bryce2cont2') \
        .search_say("Good question. If you're just talking about my species, some of us can. At least a little.") \
        .search_say("The runners lean forward and use their big tails for balance, whereas you have yours tucked into whatever that is you are wearing.") \
        .search_say("Are you kidding me?") \
        .hook_to('bangok_four_bryce1_bryce2fix',condition='bangok_four_bryce1_unplayed == False', return_link=False) \
        .search_menu("That's just the way we are.") \
        .link_from('bangok_four_bryce1_bryce2fix_end')



def bryce3_afterparty():
    ( ml.find_label('_call_skiptut_26')
        .search_menu("Yes. I want to skip ahead.")
        .branch()
        .hook_to('bangok_four_bryce3_skipmenu', condition=make_dev('persistent.nsfwtoggle == True'))
    )

    ( ml.find_label('bryce3')
        .search_say("Yeah, I should also be heading off. You know I'm starting early tomorrow.", depth=1800)
        .hook_to('bangok_four_bryce3_intro', condition=make_dev('persistent.nsfwtoggle == True'))
        .search_say("I suppose I should be heading off as well.")
        .link_from('bangok_four_bryce3_playershouldleave')
        .search_say("Damn, now everyone left without cleaning up. At least you're still here to help me.")
        .link_from('bangok_four_bryce3_canon_trash')
        .search_say("Hey, do you want to know where I got these scars? I bet you're curious.")
        .link_from('bangok_four_bryce3_wannaknowscars')
        .search_python('renpy.pause (1.5)')
        .hook_to('bangok_four_bryce3_mcbottom_mav_bryce_mp_bryce_knotted_speech_continue', return_link=False, condition=make_dev('(persistent.nsfwtoggle==True) and (bangok_four_bryce3_store.unplayed == False) and (bangok_four_bryce3_store.knotted == True)'))
        .search_with()
        .link_behind_from('bangok_four_bryce3_mcbottom_mav_bryce_mp_bryce_knotted_speech_continue_end')
        .search_say("Having been saved by police sure did a lot to make me want to follow the same path. Turns out, I was good enough to even become chief.")
        .hook_to('bangok_four_bryce3_mcbottom_mav_bryce_mp_bryce_knotted_epilogue', return_link=False, condition=make_dev('(persistent.nsfwtoggle == True) and (bangok_four_bryce3_store.unplayed == False) and (bangok_four_bryce3_store.knotted == True)'))
        .search_say("Guess that's all of the trash. Thanks for the help.")
        .hook_to('bangok_four_bryce3_mcbottom_train_epilogue', return_link=False, condition=make_dev('(persistent.nsfwtoggle == True) and (bangok_four_bryce3_store.unplayed == False) and (bangok_four_bryce3_store.mc_bottom == True and bangok_four_bryce3_store.mavbackout == False)'))
    )

    clothes_fix = ( ml.find_label('bryce3skip')
        .search_menu("There's no need for you to sleep on the floor.")
        .branch()
        .search_menu("The couch is big enough for both of us.")
        .branch()
        .search_say("There we go.")
    )

    clothes_fix.search_say("Is it okay for you to sleep like this?") \
        .link_from('bangok_four_bryce3_oktosleep') \
    
    clothes_fix.hook_to('bangok_four_bryce3_oktosleep', return_link=False, condition=make_dev('(persistent.nsfwtoggle == True) and (bangok_four_bryce3_store.unplayed == False) and (bangok_four_bryce3_store.mc_bottom == True)'))


def lorem4():
    ( ml.find_label('lorem4skip')
        .search_say("You've made me feel a lot better, though.")
        .hook_to('bangok_four_lorem4_feelbetter', condition=make_dev('(persistent.nsfwtoggle==True)'))
        .search_say("Hey, do you still want to see the fireworks show together?")
        .link_from('bangok_four_lorem4_canon_fireworks')
    )

    ( ml.find_label('lorem4skip')
        .search_menu("I'm not sure what to say.")
        .branch()
        .search_say("You can give me a call in a few days when you've had the time to mull it over or want to talk.")
        .link_from('bangok_four_lorem4_canon_callmelater')
    )


def remy_c4postsections():
    ( ml.find_label('c4postsections')
        .search_say("I'll take care of the remaining tasks, so you can take the rest of the day off. I'm sure you have things to do other than helping the police department.")
        .hook_to('bangok_four_remy_c4postsections_sebintro', condition=make_dev('(persistent.nsfwtoggle == True) and (c4libraryavailable == True) and (remy3unplayed == False) and (remystatus == "good" or remystatus == "neutral")'))
        .search_say("When I returned to the living room, I suddenly found my strength leaving me and collapsed to the floor.")
        .link_behind_from('bangok_four_remy_c4postsections_epilogue_admin')
    )


def xdamion():
    ( ml.find_label('chap2facility')
        .search_say("And you are?")
        .hook_to('bangok_four_xdamion', condition=('(persistent.nsfwtoggle==True)'))
        .search_say("What exactly did you want, again?")
        .link_from('bangok_four_xdamion_canon_whatdidyouwant')
        # ml.find_label('chap2facques') # We're literally right here.
        .search_menu("That's all.")
        .add_choice("[[Attempt to stand.]", jump='bangok_four_xdamion_questions_getup', condition=('(persistent.nsfwtoggle==True) and (bangok_four_xdamion_store.position) and (bangok_four_xdamion_store.standing_unattempted == True)'), before="That's all.")
        .branch("That's all.").search_say("Thanks for your help.")
        .hook_to('bangok_four_xdamion_cleanup', condition=('(persistent.nsfwtoggle==True) and (bangok_four_xdamion_store.position)'))
        .search_hide('damion').search_with()
        .link_behind_from('bangok_four_xdamion_canon_interrogation_over')
    )


def xipsum():
    ( ml.find_label('lorem2')
        .search_if('persistent.lorem2skip == True')
        .branch()
        .search_menu("Yes. I want to skip ahead.")
        .branch()
        .hook_to('bangok_four_xipsum_lorem2_skipmenu', condition='persistent.nsfwtoggle==True')
    )

    ( ml.find_label('lorem2')
        .search_hide('meetingipsum', depth=400)
        .search_menu("I see how it is.")
        .add_choice("I could take them off...", condition='persistent.nsfwtoggle == True', jump='bangok_four_xipsum_takeemoff')
        .search_say("And my scientific curiosity shall remain unsatisfied.")
        .link_from('bangok_four_xipsum_unsatisfied')
        .search_say("We actually have a pretty big variety of \"vestments\". I could tell you about it.")
        .link_from('bangok_four_xipsum_vestment_variety')
        .search_menu("Sounds interesting.")
        .search_menu("Same as mine, then.")
        .add_choice("Cute.", jump='bangok_four_xipsum_cute', condition='bangok_four_xipsum.unplayed == False')
        .link_behind_from('bangok_four_xipsum_cute_end')
        .search_say("Alright, I'm done with this one. You can turn around.")
        .hook_to('bangok_four_xipsum_donewithclothed',condition='bangok_four_xipsum.clothesoff == True and persistent.nsfwtoggle == True')
        .search_say("How dynamic are we talking about?")
        .link_from('bangok_four_xipsum_dynamicdrawing')
        .search_say("By the way, did you get the groceries when you came home from work?")
        .link_from('bangok_four_xipsum_donewithclothed_end')
        .search_say("I'm not even going to deny that. When I'm not working on something at the office, I do so here.")
        .hook_to('bangok_four_xipsum_awkward',condition='bangok_four_xipsum.clothesoff == True and persistent.nsfwtoggle == True')
        .search_say("If I wasn't sure, I wouldn't have said it.",depth=400)
        .hook_to('bangok_four_xipsum_littlelong', condition='bangok_four_xipsum.clothesoff == True and persistent.nsfwtoggle == True and bangok_four_playerhasdick == True')
        .search_menu("He sounds fun.")
        .add_choice("What about our...?", condition='bangok_four_xipsum.unplayed == False and persistent.nsfwtoggle == True', jump='bangok_four_xipsum_whataboutour')
        .link_behind_from('bangok_four_xipsum_whataboutour_end')
        .search_say("Anyway, looks like we're done here.")
        .hook_to('bangok_four_xipsum_loremdone', condition='bangok_four_xipsum.unplayed == False and persistent.nsfwtoggle == True')
        .search_if('lorem2mood >= 9')
        .branch_else()
        .search_say("I should be going now, anyway. It's getting late.")
        .hook_to('bangok_four_xipsum_lorembad', condition='bangok_four_xipsum.unplayed == False and persistent.nsfwtoggle == True')
    )


def xipsum2():
    ml.add_answ_machine_message('bangok_four_xipsum2_answ_machine', condition=make_dev('persistent.nsfwtoggle == True and bangok_four_xipsum.unplayed == False and (loremstatus == "good" or loremstatus == "neutral")'), chapters=[4])

    ( ml.find_label('chapter4chars2')
        .search_menu("Meet with Remy.")
        .add_choice("Meet Ipsum for something stimulating.", condition=make_dev('persistent.nsfwtoggle == True and bangok_four_xipsum.unplayed == False and (loremstatus == "good" or loremstatus == "neutral")'), jump='bangok_four_xipsum2')
    )

    ( ml.find_label('chapter5')
        .search_say("After a night of turbulent dreams, my consciousness returned to the shores of the waking world.")
        .hook_to('bangok_four_xipsum2_ipsum_sharing3', condition=make_dev('persistent.nsfwtoggle == True and bangok_four_xipsum2_store.shared_with == "ipsum" and bangok_four_xipsum2_store.sharing == 3'))
    )


def xkatsu():
    ( ml.find_label('katsuskip')
        .search_if('persistent.playedkatsu == False')
        .hook_to('bangok_four_xkatsu', condition='persistent.nsfwtoggle == True', return_link = False)
    )



def xsebastian():
    ( ml.find_label('sebastianskip')
        .search_menu("It's pretty cold.")
        .branch()
        .search_menu("I'll take it.")
        .branch()
        .search_say("Sure.")
        .hook_to('bangok_four_xsebastian_todaywasgreat', condition='persistent.nsfwtoggle == True')
    )


def modsettings_firstboot():
    ( ml.find_label('splashscreen')
        .search_python("renpy.pause(1.6, hard=True)")
        .hook_to('bangok_four_mod_firstboot', condition='persistent.bangok_four_menu_firstboot_complete != True')
    )


def link_scenes():
    anna12()
    anna4()
    anna_x_damion()
    bryce1_afterparty()
    bryce3_afterparty()
    lorem4()
    remy_c4postsections()
    xdamion()
    xipsum()
    xipsum2()
    xkatsu()
    xsebastian()
    modsettings_firstboot()


def add_side_images():
    def clip_anna_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile,(30,35,500,600)),250,300),horizontal=True)

    for expression in ["blush","orgasm","blushpalm","lipbite"]:
        renpy.exports.image('side anna bangok %s'%expression, clip_anna_side_image('cr/anna_%s.png'%expression))

    def clip_sebastian_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile,(70,0,500,600)),250,300),horizontal=True)
    
    renpy.exports.image('side sebastian shy b sleep', clip_sebastian_side_image('cr/sebastian_shy_b_sleep.png'))

    def clip_ipsum_side_image(composite):
        return im.Flip(im.Scale(im.Crop(composite, (100,40,500,600)), 250,300), horizontal=True)

    renpy.exports.image('side ipsum normal bangok blush', clip_ipsum_side_image(im.Composite((650,800),(0,0),"cr/ipsum_sad.png",(0,0),"cr/bangok/ipsum_normal_blush.png")))
    renpy.exports.image('side ipsum happy bangok blush', clip_ipsum_side_image(im.Composite((650,800),(0,0),"cr/ipsum_sad.png",(0,0),"cr/bangok/ipsum_happy_blush.png")))
    renpy.exports.image('side ipsum normal bangok heady', clip_ipsum_side_image(im.Composite((650,800),(0,0),"cr/ipsum_sad.png",(0,0),"cr/bangok/ipsum_heady.png")))
    renpy.exports.image('side ipsum happy bangok heady', clip_ipsum_side_image(im.Composite((650,800),(0,0),"cr/ipsum_sad.png",(0,0),"cr/bangok/ipsum_heady_grin.png")))

def add_scene_select():
    import four_scene_select as fss

    bangok="BangOk"

    fss.register_scene_select_cateogry(bangok, nsfw=True)

    # Anna2
    fss.register_scene_select(bangok, "Anna at Night", 'bangok_four_anna2_apartment',
        replay_scope=fss.extend_scope_by_dict({
            'blood': True,
            'annamood': 1,
            'anna2mood': 4,
            'bangok_four_anna2.boughtcondoms': True,
        }))

    # Anna4
    fss.register_scene_select(bangok, "Anna4: A Very Anna Afternoon", 'bangok_four_anna4_replay_start',
        locked=lambda: not renpy.exports.seen_label('a4romance'))

    # Bryce1
    fss.register_scene_select(bangok, "Drunk with Bryce", 'bangok_four_bryce1_apartment_decided', replay_scope=fss.extend_scope(
                        brycemood = 4,))

    # Bryce3
    fss.register_scene_select(bangok, "Bryce and Maverick at the BBQ", 'bangok_four_bryce3_replaylabel',
                                locked=lambda: (not renpy.store.persistent.bryce3skip) or (not renpy.store.persistent.bangok_dev),
                                replay_scope=fss.extend_scope_by_dict({
                                    'bangok_four_malepartners': 1,
                                }))

    fss.register_scene_select(bangok, "Bryce, Maverick, and Sebastian at the BBQ", 'bangok_four_bryce3_replaylabel',
                                locked=lambda: (not renpy.store.persistent.bryce3skip) or (not renpy.store.persistent.bangok_dev),
                                replay_scope=fss.extend_scope_by_dict({
                                    'bangok_four_malepartners': 1,
                                    'bangok_four_bryce1_unplayed': False,
                                    'bangok_four_xsebastian_unplayed': False,
                                    'bangok_four_bryce3_store.sebastian_in': True,
                                }))

    # Lorem2
    fss.register_scene_select(bangok, "Arrangement with Ipsum", 'bangok_four_xipsum_replay_start',
        locked=lambda: not renpy.store.persistent.lorem2skip)
    fss.register_scene_select(bangok, "Arrangement with Lorem and Ipsum", 'bangok_four_xipsum_replay_start',
        locked=lambda: not renpy.store.persistent.lorem2skip,
        replay_scope=fss.extend_scope_by_dict({
            'lorem2mood': 8,
            'bangok_four_xipsum.loremin': True,
        }))

    # Remyc4postsections
    fss.register_scene_select(bangok, "Remy's Tailplay Adventure", 'bangok_four_remy_c4postsections_replaystart',
        locked=lambda: (not renpy.store.persistent.remy3skip) or (not renpy.store.persistent.bangok_dev),
        replay_scope=fss.extend_scope_by_dict({
            'bangok_four_remy_c4postsections_store.remy_tail_player': True,
            'bangok_four_remy_c4postsections_store.remy_tail_remy': True,
            'bangok_four_remy_c4postsections_store.remy_top': True,
        }))

    # xDamion
    fss.register_scene_select(bangok, "Improving Damion's Mood", 'bangok_four_xdamion_replay_start',
        locked=lambda: (not renpy.store.persistent.metdamion))

    # xIpsum2
    fss.register_scene_select(bangok, "Something Stimulating with Ipsum", 'bangok_four_xipsum2_replay_start',
        locked=lambda: (not renpy.store.persistent.bangok_four_xipsum2_skip) or (not renpy.store.persistent.bangok_dev))

    # xKatsu
    fss.register_scene_select(bangok, "Katsuharu's Special", 'bangok_four_xkatsu_replay_start',
        locked=lambda: not renpy.store.persistent.playedkatsu)

    # xSebastian
    fss.register_scene_select(bangok, "Sebastian Cave Night", 'bangok_four_xsebastian_replay_start',
        locked=lambda: not renpy.store.persistent.sebastianplayed,
        replay_scope=fss.extend_scope(mcwon=False))
    fss.end_replay_at_ml_node(ml.find_label('bangok_four_xsebastian_todaywasgreat_return'))


@loadable_mod
class BangOkMod(Mod):
    name = "BangOk"
    version = "v0.0"
    author = "4onen"
    nsfw = True
    dependencies = ["MagmaLink", "?Side Images", "?CRAP", "?Scene Select"] # TODO: Make CRAP mandatory when Bryce and Ipsum assets move.

    @classmethod
    def mod_load(cls):
        if modinfo.has_mod("Side Images"):
            add_side_images()

        ml.register_mod_settings(cls, screen='bangok_modsettings')

        link_scenes()

        if modinfo.has_mod("Scene Select"):
            add_scene_select()

    @staticmethod
    def mod_complete():
        pass
