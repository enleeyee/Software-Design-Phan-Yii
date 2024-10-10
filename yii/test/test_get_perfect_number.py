import unittest
import sys
sys.path.append('src')
from get_perfect_number import is_perfect

class GetPerfectNumberTest(unittest.TestCase):

    def test_canary(self):
        self.assertTrue(True)
        
    def test_number_is_perfect_false(self):
        self.assertFalse(is_perfect(-1))
        self.assertFalse(is_perfect(10))

    def test_number_is_perfect_true(self):
        self.assertTrue(is_perfect(6))
        self.assertTrue(is_perfect(28))
