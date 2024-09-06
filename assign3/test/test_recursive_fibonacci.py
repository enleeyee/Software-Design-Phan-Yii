import unittest
from test_fibonacci import BaseFibonacciTests
from src.recursive_fibonacci import recursive_fibonacci

class RecursiveFibonacciTests(unittest.TestCase, BaseFibonacciTests):
    def get_fibonacci_function(self):
        return recursive_fibonacci
    