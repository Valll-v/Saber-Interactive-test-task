def write_list(what, data):
    print(f'Список доступных {what}')
    for name in data:
        print(f'\t- {name}')


def write_task_dependencies(task, data: dict):
    if task not in data:
        print(f'Таска {task} не найдена. Посмотрить список доступных тасок можно командой (list tasks)')
        return
    print(f'Информация о таске')
    print(f'Название: {task}')
    print(f'Зависимости:')
    for dep in data.get(task):
        print(f'\t- {dep}')
