def homework_estimates(lesson, group):
    homework_ = open(f'{group}_homework_{lesson}', 'r', encoding='utf-8')
    text_ = homework_.read()
    print(text_)
    homework_.close()

def grade_estimates(lesson, group, login):
    estimates_ = open(f'{group}_estimates_{lesson}', 'r', encoding='utf-8')
    text_ = estimates_.readlines()
    for i in range(len(text_)):
        if login in text_[i]:
            print(text_[i])
    estimates_.close()

def homework_add(lesson, group):
    homework_lesson = open(f'{group}_homework_{lesson}', 'a', encoding='utf-8')
    homework_num = str(input('Введите номер задания: '))
    homework_ = str(input('Введите задание: '))
    homework_lesson.write(f'{homework_num}\n{homework_}\n')
    homework_lesson.close()