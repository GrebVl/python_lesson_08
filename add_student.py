import group_selection as g_s


def add_student():
    group_name = g_s.group_selection()
    fail_group = open(f'{group_name}_student', 'a', encoding='utf-8')
    estimates_maths = open(f'{group_name}_estimates_maths', 'a', encoding='utf-8')
    estimates_physics = open(f'{group_name}_estimates_physics', 'a', encoding='utf-8')
    exit_add = False
    while exit_add == False:
        print('Добавление студента:\n1. Новый студент\n2. Выход')
        option_creating = str(input('Введите значение от 1 до 2 для выбора действия: '))
        if option_creating == '1':
            str_login = str(input('Введите логин студента: '))
            str_name = str(input('Введите ФИО студента: '))
            str_group = group_name
            estimates_maths.write(f'{str_login} : {str_name} -  \n')
            estimates_physics.write(f'{str_login} : {str_name} - \n')
            str_group = group_name
            fail_group.write(f'{str_login} : {str_name};\n')
        elif option_creating == '2':
            exit_add = True
        else:
            print('Введено неверное значение')
    fail_group.close()
    estimates_maths.close()
    estimates_physics.close()