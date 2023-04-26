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
    if not data.get(task):
        print('Зависимостей не найдено')
        return
    print(f'Зависимости:')
    for dep in data.get(task):
        print(f'\t- {dep}')


def write_build_dependencies(build_data: dict):
    print(f'Информация о билде')
    print(f'Название: {build_data.get("name")}')
    print(f'Таски: ')
    for dep in build_data.get('tasks'):
        print(f'\t- {dep}')
