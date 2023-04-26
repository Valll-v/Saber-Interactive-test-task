from abc import ABC

from build_worker import form_build_tasks
from exceptions import CustomAppException
from writer import write_list, write_task_dependencies, write_build_dependencies

help_text = """
Команды:
help: дублирует это сообщение
list option: Вывод загруженных имен (option=builds) и задач (option=tasks)
get option arg: Вывод детальной информации билда (option=build) и задачи (option=task)
exit: Отключение программы
"""

valid_list_option = ('builds', 'tasks')
valid_get_option = ('build', 'task')


class Command(ABC):

    def execute(self, option=None, arg=None, data=None):
        pass


class HelpCommand(Command):

    def execute(self, option=None, arg=None, data=None):
        print(help_text)


class GetCommand(Command):

    def execute(self, option=None, arg=None, data=None):
        if option not in valid_get_option:
            print(f'Аргумент {option} неприемлем для команды list')
            return
        elif option == 'task':
            write_task_dependencies(arg, data.get('tasks_uploaded_dependencies'))
        else:
            try:
                build_data = form_build_tasks(data.get('tasks_uploaded_dependencies'), arg, data.get('builds'))
            except CustomAppException as ex:
                print(ex)
                return
            write_build_dependencies(build_data)


class ListCommand(Command):

    def execute(self, option=None, arg=None, data=None):
        if option not in valid_list_option:
            print(f'Аргумент {option} неприемлем для команды list')
            return
        write_list(option, data.get(option))


class ExitCommand(Command):

    def execute(self, option=None, arg=None, data=None):
        exit(0)
