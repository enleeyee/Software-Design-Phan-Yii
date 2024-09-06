import time
import unittest
from test_fibonacci import BaseFibonacciTests
from src.recursive_fibonacci import recursive_fibonacci
from src.memorized_fibonacci import memorized_fibonacci

class MemorizedFibonacciTests(unittest.TestCase, BaseFibonacciTests):    
    def get_fibonacci_function(self):
        return memorized_fibonacci
    
    def getSpeed(self, function, position): 
        startTime = time.time()
        function(position)
        endTime = time.time()

        return endTime - startTime

    def test_memoized_faster_than_recursive_fibonacci_call_big_position(self):
        memoizedTime = self.getSpeed(memorized_fibonacci, 30)

        recursiveTime = self.getSpeed(recursive_fibonacci, 30)

        self.assertGreater(recursiveTime, memoizedTime * 10, "recursive time: " + str(recursiveTime) + " memoizedTime: " + str(memoizedTime)) 
        
    def test_memoized_faster_than_recursive_fibonacci_call_small_position(self):
        memoizedTime = self.getSpeed(memorized_fibonacci, 3)

        recursiveTime = self.getSpeed(recursive_fibonacci, 3)

        self.assertLessEqual(recursiveTime, memoizedTime, "recursive time: " + str(recursiveTime) + " memoizedTime: " + str(memoizedTime))
        