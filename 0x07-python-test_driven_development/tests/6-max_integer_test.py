#!/usr/bin/python3
"""
    Unit Test for max integer
    """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test a max integer function
    """

    def test_empty_list(self):
        """
        Tests an empty list
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """
        Tests a single element
        """
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """
        Tests positive numbers
        """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        """
        Tests negative numbers
        """
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """
        Tests negative and positive numbers
        """
        result = max_integer([-1, 2, -3, 4])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        """
        Tests duplicate numbers
        """
        result = max_integer([1, 1, 1, 1])
        self.assertEqual(result, 1)

    def test_large_numbers(self):
        """
        Tests large numbers
        """
        result = max_integer([9999999999, 10000000000, 5000000000])
        self.assertEqual(result, 10000000000)

if __name__ == '__main__':
    unittest.main()
