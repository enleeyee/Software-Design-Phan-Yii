import unittest
import sys
sys.path.append('src')
from get_all_perfect_numbers_fetch import find_perfect_numbers

class GetAllPerfectNumbersTest(unittest.TestCase):

    def test_find_perfect_numbers_exists(self):
        self.assertEqual([6, 28], find_perfect_numbers(30))

    def test_find_perfect_numbers_do_not_exists(self):
        self.assertEqual([], find_perfect_numbers(1))
