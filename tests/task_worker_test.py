import unittest

from ..exceptions import *
from ..reader import read_file
from ..task_worker import form_map, upload_dependencies_for_all_tasks


class TestTaskWorkerOK(unittest.TestCase):

    def test_task_read(self):
        tasks_data = read_file('tasks_data/task_ok.yaml')
        self.assertEqual(tasks_data, [{'name': '1', 'dependencies': []},
                                      {'name': '2', 'dependencies': ['1']},
                                      {'name': '3', 'dependencies': ['1', '6']},
                                      {'name': '4', 'dependencies': ['3', '1']},
                                      {'name': '5', 'dependencies': ['3', '4']},
                                      {'name': '6', 'dependencies': ['2']},
                                      {'name': '7', 'dependencies': []},
                                      {'name': '8', 'dependencies': ['1', '5', '6', '7']}])

    def test_task_to_dict(self):
        tasks_data = read_file('tasks_data/task_ok.yaml')
        task_to_dict = form_map(tasks_data)
        self.assertEqual(task_to_dict, {'1': [],
                                        '2': ['1'],
                                        '3': ['1', '6'],
                                        '4': ['3', '1'],
                                        '5': ['3', '4'],
                                        '6': ['2'],
                                        '7': [],
                                        '8': ['1', '5', '6', '7']})

    def test_task_load_dependencies(self):
        tasks_data = read_file('tasks_data/task_ok.yaml')
        task_to_dict = form_map(tasks_data)
        task_uploaded_dependencies = upload_dependencies_for_all_tasks(task_to_dict)
        self.assertEqual(task_uploaded_dependencies, {'1': [],
                                                      '2': ['1'],
                                                      '3': ['1', '6', '2'],
                                                      '4': ['3', '1', '6', '2'],
                                                      '5': ['3', '1', '6', '2', '4'],
                                                      '6': ['2', '1'],
                                                      '7': [],
                                                      '8': ['1', '5', '3', '6', '2', '4', '7']})


class TestTaskWorkerSelfException(unittest.TestCase):

    def test_task_read(self):
        tasks_data = read_file('tasks_data/task_self_exception.yaml')
        self.assertEqual(tasks_data, [{'name': '1', 'dependencies': []},
                                      {'name': '2', 'dependencies': ['1']},
                                      {'name': '3', 'dependencies': ['1', '6']},
                                      {'name': '4', 'dependencies': ['3', '1', '4']},
                                      {'name': '5', 'dependencies': ['3', '4']},
                                      {'name': '6', 'dependencies': ['2']},
                                      {'name': '7', 'dependencies': []},
                                      {'name': '8', 'dependencies': ['1', '5', '6', '7']}])

    def test_task_to_dict(self):
        tasks_data = read_file('tasks_data/task_self_exception.yaml')
        task_to_dict = form_map(tasks_data)
        self.assertEqual(task_to_dict, {'1': [],
                                        '2': ['1'],
                                        '3': ['1', '6'],
                                        '4': ['3', '1', '4'],
                                        '5': ['3', '4'],
                                        '6': ['2'],
                                        '7': [],
                                        '8': ['1', '5', '6', '7']})

    def test_task_load_dependencies(self):
        tasks_data = read_file('tasks_data/task_self_exception.yaml')
        task_to_dict = form_map(tasks_data)
        with self.assertRaises(SelfDependencyException):
            upload_dependencies_for_all_tasks(task_to_dict)


class TestTaskWorkerUndefinedException(unittest.TestCase):

    def test_task_undefined_read(self):
        tasks_data = read_file('tasks_data/task_undefined.yaml')
        self.assertEqual(tasks_data, [{'name': '1', 'dependencies': []},
                                      {'name': '2', 'dependencies': ['1']},
                                      {'name': '3', 'dependencies': ['1', '6']},
                                      {'name': '4', 'dependencies': ['3', '1', '9']},
                                      {'name': '5', 'dependencies': ['3', '4']},
                                      {'name': '6', 'dependencies': ['2']},
                                      {'name': '7', 'dependencies': []},
                                      {'name': '8', 'dependencies': ['1', '5', '6', '7']}])

    def test_task_to_dict(self):
        tasks_data = read_file('tasks_data/task_undefined.yaml')
        task_to_dict = form_map(tasks_data)
        self.assertEqual(task_to_dict, {'1': [],
                                        '2': ['1'],
                                        '3': ['1', '6'],
                                        '4': ['3', '1', '9'],
                                        '5': ['3', '4'],
                                        '6': ['2'],
                                        '7': [],
                                        '8': ['1', '5', '6', '7']})

    def test_task_load_dependencies(self):
        tasks_data = read_file('tasks_data/task_undefined.yaml')
        task_to_dict = form_map(tasks_data)
        with self.assertRaises(UndefinedDependencyException):
            upload_dependencies_for_all_tasks(task_to_dict)


class TestTaskWorkerCircularException(unittest.TestCase):

    def test_task_undefined_read(self):
        tasks_data = read_file('tasks_data/task_circular.yaml')
        self.assertEqual(tasks_data, [{'name': '1', 'dependencies': []},
                                      {'name': '2', 'dependencies': ['1']},
                                      {'name': '3', 'dependencies': ['1', '6']},
                                      {'name': '4', 'dependencies': ['3', '1', '5']},
                                      {'name': '5', 'dependencies': ['3', '4']},
                                      {'name': '6', 'dependencies': ['2']},
                                      {'name': '7', 'dependencies': []},
                                      {'name': '8', 'dependencies': ['1', '5', '6', '7']}])

    def test_task_to_dict(self):
        tasks_data = read_file('tasks_data/task_circular.yaml')
        task_to_dict = form_map(tasks_data)
        self.assertEqual(task_to_dict, {'1': [],
                                        '2': ['1'],
                                        '3': ['1', '6'],
                                        '4': ['3', '1', '5'],
                                        '5': ['3', '4'],
                                        '6': ['2'],
                                        '7': [],
                                        '8': ['1', '5', '6', '7']})

    def test_task_load_dependencies(self):
        tasks_data = read_file('tasks_data/task_circular.yaml')
        task_to_dict = form_map(tasks_data)
        with self.assertRaises(CircularDependencyException):
            upload_dependencies_for_all_tasks(task_to_dict)


if __name__ == "__main__":
    unittest.main()
