import menu_professor as m_p
import menu_studen as m_s
import menu_curator as m_c


def menu_titles():
    exit_titles = False
    while exit_titles == False:
        print('1. Преподаватель\n2. Студент \n3. Куратор \n4. Выход')
        option_titles = str(input('Введите значение от 1 до 4 для выбора действия: '))
        if option_titles == '1':
            m_p.menu_professor()
        elif option_titles == '2':
            m_s.menu_studen()
        elif option_titles == '3':
            m_c.menu_curator()
        elif option_titles == '4':
            return 4
        else:
            print('Введено неверное значение')
