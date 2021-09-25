from modloader import modinfo
from modloader.modclass import Mod, loadable_mod

def anna12(ml):
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
        .search_say("That's fine with me.") \
        .hook_to('bangok_four_anna1_goodending', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("Thank you.") \
        .link_from('bangok_four_anna1_goodending_thankyou') \
        .search_say("Despite all odds, I managed to match her perfect score in the game we played.") \
        .hook_to('bangok_four_anna1_goodending_nvl',condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("Whether anything good would come of this, I wasn't sure, either.") \
        .link_from('bangok_four_anna1_goodending_nvl_end')
        
    ml.find_label('anna1skip') \
        .search_say("I'm quite sure you will.") \
        .hook_to('bangok_four_anna1_medending', condition='bangok_four_anna1_sexrequested == True and persistent.nsfwtoggle == True', return_link=False) \
        .search_say("Really?") \
        .link_from('bangok_four_anna1_medending_really') \
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
    



def bryce1_afterparty(ml):
    ml.find_label('_call_skiptut_8') \
        .search_menu("Yes. I want to skip ahead.") \
        .branch() \
        .hook_to('bangok_four_bryce1_skipmenu')

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

@loadable_mod
class BangOkMod(Mod):
    @staticmethod
    def mod_info():
        name = "BangOk?"
        version = "v0.0"
        author = "4onen"
        nsfw = True
        return (name,version,author,nsfw)

    @staticmethod
    def mod_load():
        ml = modinfo.get_mods()["MagmaLink"].import_ml()
        anna12(ml)
        bryce1_afterparty(ml)

    @staticmethod
    def mod_complete():
        pass