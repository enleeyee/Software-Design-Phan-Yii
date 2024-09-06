import unittest
from test_fibonacci import BaseFibonacciTests
from src.imperative_fibonacci import imperative_fibonacci

class ImperativeFibonacciTests(unittest.TestCase, BaseFibonacciTests):
    def test_canary(self):
        self.assertTrue(True)
        
    def get_fibonacci_function(self):
        return imperative_fibonacci
    