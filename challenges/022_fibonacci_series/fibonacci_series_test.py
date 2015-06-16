import unittest

from fibonacci_series import fib


class TestFibonacci(unittest.TestCase):

    def test_fib(self):
        results = ((0, 0), (1, 1), (5, 5), (12, 144))
        for x, y in results:
            self.assertEqual(y, fib(x))
