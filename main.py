from reader import read_builds, read_tasks
from task_worker import upload_dependencies_for_all_tasks
from task_worker import form_map as form_tasks_map
from build_worker import form_map as form_builds_map
from executor import CommandManager
from utils import form_data


def main():
    task_data = read_tasks()
    builds_data = read_builds()
    task_dict = form_tasks_map(task_data)
    build_dict = form_builds_map(builds_data)
    data_for_execute = form_data(tasks=task_dict,
                                 builds=build_dict,
                                 tasks_uploaded_dependencies=upload_dependencies_for_all_tasks(task_dict))
    command_manager = CommandManager()
    command_manager.execute_command('help')

    while True:
        data = input()
        command, *args = data.split()
        option = args[0] if args else None
        arg = args[1] if len(args) > 1 else None
        command_manager.execute_command(command, option, arg, data_for_execute)


if __name__ == '__main__':
    main()
