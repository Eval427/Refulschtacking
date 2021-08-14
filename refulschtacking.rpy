init:
    find label splashscreen
    search if
    branch 'persistent.lang == "Jp"':
        add option "Refulschtacking" to eval_add_refulschtacking
    branch else:
        add option "Refulschtacking" to eval_add_refulschtacking
    search show
    link eval_refulschtacking_enable_return


label eval_add_refulschtacking:
    $ renpy.change_language("gamer") #Don't ask why it's gamer

label eval_refulschtacking_enable_return:
    pass