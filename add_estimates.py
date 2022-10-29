import group_selection as g_s

def add_estimates(lesson, group):
    estimates_ = open(f'{group}_estimates_{lesson}', 'r', encoding='utf-8')
    text_ = estimates_.readlines()
    estimates_.close()
    str_login = g_s.student_selection(group)
    for i in range(len(text_)):
        if str_login in text_[i]:
            str_estimates = str(input('Введите оценку: '))
            text_[i] = text_[i][:-1] + ' ' + str_estimates + '\n'
    estimates_ = open(f'{group}_estimates_{lesson}', 'w', encoding='utf-8')
    for i in range(len(text_)):
        estimates_.write(f'{text_[i]}')
    estimates_.close()

def grade_estimates_group(lesson, group):
    estimates_ = open(f'{group}_estimates_{lesson}', 'r', encoding='utf-8')
    text_ = estimates_.readlines()
    print(*text_)
    estimates_.close()
