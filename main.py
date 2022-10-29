import menu

action_ = True
while action_ == True:
    action_main = menu.menu_titles()
    if action_main == 1:
        menu.menu_professor()
    elif action_main == 2:
        menu.menu_studen()
    elif action_main == 3:
        menu.menu_curator()
    elif action_main == 4:
        action_ = False
        break