from typing import List, Dict, Set

from exceptions import *


def form_map(data: List[Dict]):
    result = dict()
    for task in data:
        result[task.get('name')] = task.get('dependencies')
    return result


def get_dependencies_for_target_task(task_map: Dict[str, List[str]], target_task: str, previous_tasks=None)\
        -> List[str]:
    if previous_tasks is None:
        previous_tasks = set()  # сет для проверки цикличности, каждый раз при "прогулке" по дереву тасок мы добавляем
        # по одной с каждого уровня родства. Если встретили ту, что уже была, значит у нас цикличность (строка ниже)
    if target_task in previous_tasks:
        raise CircularDependencyException
    previous_tasks.add(target_task)
    local_dep = set()  # Здесь хранятся все предки одной таски, чтобы избежать случайного
    # повторного интегрирования одной и той же зависимости
    all_dependencies = []
    try:
        target_task_dependencies = task_map[target_task]
    except KeyError:
        raise UndefinedDependencyException(target_task)
    if not target_task_dependencies:
        return []
    for dep in target_task_dependencies:
        if dep == target_task:
            raise SelfDependencyException
        if dep in local_dep:
            continue
        local_dep.add(dep)
        all_dependencies.append(dep)
        under_deps = get_dependencies_for_target_task(task_map, dep, previous_tasks)
        previous_tasks.remove(dep)  # изменяемый тип данных на рекурсию не влияет, поэтому ручками подчищаем
        for under_dep in under_deps:
            if under_dep in local_dep:
                continue
            local_dep.add(under_dep)
            all_dependencies.append(under_dep)
    return all_dependencies


def upload_dependencies_for_all_tasks(task_map: Dict[str, List[str]]):
    for task in task_map:
        task_map[task] = get_dependencies_for_target_task(task_map, task)
    return task_map
