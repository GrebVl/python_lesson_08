def creating_group():
    group_name = str(input('Введите название группы: '))
    homework_maths = open(f'{group_name}_homework_maths', 'w', encoding='utf-8')
    homework_maths.close()
    homework_physics = open(f'{group_name}_homework_physics', 'w', encoding='utf-8')
    homework_physics.close()
    estimates_maths = open(f'{group_name}_estimates_maths', 'w', encoding='utf-8')
    estimates_physics = open(f'{group_name}_estimates_physics', 'w', encoding='utf-8')
    fail_group = open(f'{group_name}_student', 'w', encoding='utf-8')
    exit_creating = False
    while exit_creating == False:
        print('Добавление студента:\n1. Новый студент\n2. Выход')
        option_creating = str(input('Введите значение от 1 до 2 для выбора действия: '))
        if option_creating == '1':
            str_login = str(input('Введите логин студента: '))
            str_name = str(input('Введите ФИО студента: '))
            estimates_maths.write(f'{str_login} : {str_name} -  \n')
            estimates_physics.write(f'{str_login} : {str_name} - \n')
            str_group = group_name
            fail_group.write(f'{str_login} : {str_name};\n')
        elif option_creating == '2':
            exit_creating = True
        else:
            print('Введено неверное значение')
    fail_group.close()
    estimates_maths.close()
    estimates_physics.close()
    fail_group_commont = open(f'group_commont_list', 'a', encoding='utf-8')
    fail_group_commont.write(f'{group_name} \n')
    fail_group_commont.close()

