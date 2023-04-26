from typing import List, Dict


def form_map(data: List[Dict]):
    result = dict()
    for task in data:
        result[task.get('name')] = task.get('tasks')
    return result
