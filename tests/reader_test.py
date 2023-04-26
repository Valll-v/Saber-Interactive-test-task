import unittest
from reader import read_file


class TestReader1(unittest.TestCase):
    def test_first_read(self):
        self.assertEqual(read_file('tasks1.yaml'), [{'name': 'bring_black_leprechauns', 'dependencies': []},
                                                    {'name': 'bring_gray_cyclops', 'dependencies': []}])


if __name__ == "__main__":
    unittest.main()
