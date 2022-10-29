import menu_lesson as menu_l
import group_selection as g_s


def menu_studen():
    exit_studen = False
    studen_group = g_s.group_selection()
    studen_login = g_s.student_selection(studen_group)
    while exit_studen == False:
        print('1. Просмотр Д/з \n'
              '2. Просмотр оценок \n'
              '3. Выход')
        option_studen = str(input('Введите значение от 1 до 3 для выбора действия: '))
        if option_studen == '1':
            num_studen = 0
            menu_l.menu_lesson(studen_group, studen_login, num_studen)
        elif option_studen == '2':
            num_studen = 1
            menu_l.menu_lesson(studen_group, studen_login, num_studen)
        elif option_studen == '3':
            exit_studen = True
        else:
            print('Введено неверное значение')