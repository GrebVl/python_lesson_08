import subject_lesson as sub_l
import add_estimates as a_e

def menu_lesson(group, login, num_option):
    exit_lesson = False
    while exit_lesson == False:
        print('1. Математика \n'
              '2. Физика \n'
              '3. Выход')
        option_lesson = str(input('Введите значение от 1 до 3 для выбора действия: '))
        if option_lesson == '1':
            lesson_ = 'maths'
            if num_option == 0:
                sub_l.homework_estimates(lesson_, group)
            elif num_option == 1:
                sub_l.grade_estimates(lesson_, group, login)
            elif num_option == 2:
                sub_l.homework_add(lesson_, group)
            elif num_option == 3:
                a_e.add_estimates(lesson_, group)
            elif num_option == 4:
                a_e.grade_estimates_group(lesson_, group)
        elif option_lesson == '2':
            lesson_ = 'physics'
            if num_option == 0:
                sub_l.homework_estimates(lesson_, group)
            elif num_option == 1:
                sub_l.grade_estimates(lesson_, group, login)
            elif num_option == 2:
                sub_l.homework_add(lesson_, group)
            elif num_option == 3:
                a_e.add_estimates(lesson_, group)
            elif num_option == 4:
                a_e.grade_estimates_group(lesson_, group)
        elif option_lesson == '3':
            exit_lesson = True
        else:
            print('Введено неверное значение')