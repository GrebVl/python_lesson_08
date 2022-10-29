import creating_group as c_g
import group_list as g_l
import add_student as a_s
import menu_lesson as menu_l
import group_selection as g_s


def menu_curator():
    login_ = 'curator'
    exit_curator = False
    while exit_curator == False:
        print('1. Создать новую группу \n'
              '2. Добавить студеннта \n'
              '3. Просмотр списка группы \n'
              '4. Просмотр оценнок группы \n'
              '5. Выход')
        option_lesson = str(input('Введите значение от 1 до 5 для выбора действия: '))
        if option_lesson == '1':
            c_g.creating_group()
        elif option_lesson == '2':
            a_s.add_student()
        elif option_lesson == '3':
            g_l.group_list()
        elif option_lesson == '4':
            num_curator = 4
            group_curator = g_s.group_selection()
            menu_l.menu_lesson(group_curator, login_, num_curator)
        elif option_lesson == '5':
            exit_curator = True
        else:
            print('Введено неверное значение')