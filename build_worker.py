from typing import List, Dict, Set
from exceptions import UndefinedDependencyException, UndefinedBuildException


def form_map(data: List[Dict]):
    result = dict()
    for task in data:
        result[task.get('name')] = task.get('tasks')
    return result


def add_task_to_list(result_list: List, result_set: Set, task: str):
    if task not in result_set:
        result_set.add(task)
        result_list.append(task)


def form_build_tasks(task_data: Dict[str, List[str]], build_name: str, build_data: Dict[str, List[str]]):
    result_list = []
    result_set = set()
    build_tasks = build_data.get(build_name)
    if build_tasks is None:
        raise UndefinedBuildException(f'Билд {build_name} не обнаружен')
    for task in build_tasks:
        if task not in task_data:
            raise UndefinedDependencyException(f'Билд {build_name}: '
                                               f'обнаружена несуществующая таска {task}')
        add_task_to_list(result_list, result_set, task)
        for dep in task_data.get(task):
            add_task_to_list(result_list, result_set, dep)
    return {
        'name': build_name,
        'tasks': result_list,
    }

