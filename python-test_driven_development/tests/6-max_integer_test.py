#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_max_positive_integers(self):
        """Test case for a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_negative_integers(self):
        """Test case for a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_mixed_integers(self):
        """Test case for a list with both positive and negative integers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_single_element(self):
        """Test case for a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test case for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_with_duplicates(self):
        """Test case for a list with duplicate values"""
        self.assertEqual(max_integer([3, 2, 3, 1]), 3)

    def test_max_with_string_elements(self):
        """Test case for invalid data type"""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
