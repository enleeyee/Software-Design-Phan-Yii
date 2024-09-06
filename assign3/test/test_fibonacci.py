from parameterized import parameterized

class BaseFibonacciTests:
    @parameterized.expand([
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 8),
        (8, 34),
        (10, 89),
    ])
    def test_fibonacci_for_valid_position(self, position, expected):
        self.assertEqual(expected, self.get_fibonacci_function()(position))
        
    def test_fibonacci_for_invalid_position(self):
        self.assertRaisesRegex(ValueError, "The number should be non-negative", self.get_fibonacci_function(), -1)
        