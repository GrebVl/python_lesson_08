import menu_lesson as menu_l
import group_selection as g_s


def menu_professor():
    exit_professor = False
    login_ = 'professor'
    while exit_professor == False:
        print('1. Просмотр Д/з \n'
              '2. Добавление Д/з \n'
              '3. Просмотр оценок группы \n'
              '4. Добавлеие оценок \n'
              '5. Выход')
        option_professor = str(input('Введите значение от 1 до 5 для выбора действия: '))
        if option_professor == '1':
            num_professor = 0
            group_professor = g_s.group_selection()
            menu_l.menu_lesson(group_professor, login_, num_professor)
        elif option_professor == '2':
            num_professor = 2
            group_professor = g_s.group_selection()
            menu_l.menu_lesson(group_professor, login_, num_professor)
        elif option_professor == '3':
            num_professor = 4
            group_professor = g_s.group_selection()
            menu_l.menu_lesson(group_professor, login_, num_professor)
        elif option_professor == '4':
            num_professor = 3
            group_professor = g_s.group_selection()
            menu_l.menu_lesson(group_professor, login_, num_professor)
        elif option_professor == '5':
            exit_professor = True
        else:
            print('Введено неверное значение')