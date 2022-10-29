def group_selection():
    group_sel = open('group_commont_list', 'r', encoding='utf-8')
    text_ = group_sel.read().split()
    group_sel.close()
    count = 0
    for i in range(len(text_)):
        print(f'{i+1}: {text_[i]}')
        count = i
    exit_sel = False
    while exit_sel == False:
        index_ = input('Выберете группу введя число: ')
        if index_.isdigit() == True and count >= int(index_) - 1:
            index_ = int(index_)
            index_ -= 1
            exit_sel = True
        else:
            print('Введено не верное значение')
    return text_[index_]

def student_selection(group):
    student_sel = open(f'{group}_student', 'r', encoding='utf-8')
    text_ = student_sel.readlines()
    student_sel.close()
    exit_select = False
    while exit_select == False:
        studen_login = str(input('Введите логин студента: '))
        for i in range(len(text_)):
            if studen_login in text_[i]:
                exit_select = True
        if exit_select == False:
            print('Логин веден не верно')
    return studen_login