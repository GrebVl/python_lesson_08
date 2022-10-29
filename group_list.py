import group_selection as g_s

def group_list():
    group_name = g_s.group_selection()
    fail_group = open(f'{group_name}_student', 'r', encoding='utf-8')
    print(*fail_group)
    fail_group.close()