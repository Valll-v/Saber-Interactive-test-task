import unittest

from exceptions import *
from reader import read_file
from build_worker import form_map as build_form_map, form_build_tasks
from task_worker import form_map as task_form_map, upload_dependencies_for_all_tasks


class TestBuildWorkerOK(unittest.TestCase):

    def test_build_read(self):
        build_data = read_file('builds_data/build_ok.yaml')
        self.assertEqual(build_data, [{'name': 'build1', 'tasks': ['8']},
                                      {'name': 'build2', 'tasks': ['6', '1', '4']}])

    def test_build_to_dict(self):
        build_data = read_file('builds_data/build_ok.yaml')
        build_to_dict = build_form_map(build_data)
        self.assertEqual(build_to_dict, {'build1': ['8'],
                                         'build2': ['6', '1', '4']})

    def test_build_load_dependencies1(self):
        build_data = read_file('builds_data/build_ok.yaml')
        build_to_dict = build_form_map(build_data)
        tasks_data = read_file('tasks_data/task_ok.yaml')
        task_to_dict = task_form_map(tasks_data)
        task_uploaded_dependencies = upload_dependencies_for_all_tasks(task_to_dict)
        build_uploaded_tasks = form_build_tasks(task_uploaded_dependencies, 'build1', build_to_dict)
        self.assertEqual(build_uploaded_tasks, {'name': 'build1',
                                                'tasks': ['8', '1', '5', '3', '6', '2', '4', '7']})

    def test_build_load_dependencies2(self):
        build_data = read_file('builds_data/build_ok.yaml')
        build_to_dict = build_form_map(build_data)
        tasks_data = read_file('tasks_data/task_ok.yaml')
        task_to_dict = task_form_map(tasks_data)
        task_uploaded_dependencies = upload_dependencies_for_all_tasks(task_to_dict)
        build_uploaded_tasks = form_build_tasks(task_uploaded_dependencies, 'build2', build_to_dict)
        self.assertEqual(build_uploaded_tasks, {'name': 'build2',
                                                'tasks': ['6', '2', '1', '4', '3']})


class TestBuildWorkerUndefined(unittest.TestCase):

    def test_build_read(self):
        build_data = read_file('builds_data/build_undefined.yaml')
        self.assertEqual(build_data, [{'name': 'build1', 'tasks': ['8']},
                                      {'name': 'build2', 'tasks': ['9']}])

    def test_build_to_dict(self):
        build_data = read_file('builds_data/build_undefined.yaml')
        build_to_dict = build_form_map(build_data)
        self.assertEqual(build_to_dict, {'build1': ['8'],
                                         'build2': ['9']})

    def test_build_load_dependencies1(self):
        build_data = read_file('builds_data/build_undefined.yaml')
        build_to_dict = build_form_map(build_data)
        tasks_data = read_file('tasks_data/task_ok.yaml')
        task_to_dict = task_form_map(tasks_data)
        task_uploaded_dependencies = upload_dependencies_for_all_tasks(task_to_dict)
        with self.assertRaises(UndefinedDependencyException):
            form_build_tasks(task_uploaded_dependencies, 'build2', build_to_dict)

    def test_build_load_dependencies2(self):
        build_data = read_file('builds_data/build_undefined.yaml')
        build_to_dict = build_form_map(build_data)
        tasks_data = read_file('tasks_data/task_ok.yaml')
        task_to_dict = task_form_map(tasks_data)
        task_uploaded_dependencies = upload_dependencies_for_all_tasks(task_to_dict)
        with self.assertRaises(UndefinedBuildException):
            form_build_tasks(task_uploaded_dependencies, 'build3', build_to_dict)


if __name__ == "__main__":
    unittest.main()
