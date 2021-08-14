import renpy
import renpy.ast as ast
import renpy.display.im as im
import renpy.parser as parser
#from link import run_linkfile

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod
from modloader.modgame import base

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Refulschtacking", "v1.0.0", "Eval")
    
    def mod_load(self):
        #languageMenuNode2 = modast.find_menu("English {image=lang-en2.png}")[0]
        
        #languageMenu2 = base.get_menu_hook(languageMenuNode2)
        
        #languageMenu2.add_item("Refulschtacking", modast.find_label("eval_add_refulschtacking"))
        pass
    
    def mod_complete(self):
        pass