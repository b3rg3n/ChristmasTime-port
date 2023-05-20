




label start:





    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer






    $ s_name = "Сайори"
    $ m_name = "Моника"
    $ n_name = "Нацуки"
    $ y_name = "Юри"


    $ quick_menu = True



    $ style.say_dialogue = style.normal



    $ in_sayori_kill = None


    $ allow_skipping = True
    $ config.allow_skipping = True




    if persistent.playthrough == 0:



        $ chapter = 0



        call story from _call_story

        call story2 from _call_story2

        call story3 from _call_story3

        call story4 from _call_story4

        call story5 from _call_story5

        call story6 from _call_story6







































        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
