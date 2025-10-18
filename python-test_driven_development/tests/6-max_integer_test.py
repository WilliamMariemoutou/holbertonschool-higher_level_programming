#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_regular_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_negative_numbers(self):
        self.assertEqual(max_integer([-5, -9, -3, -7]), -3)

    def test_duplicate_max_value(self):
        self.assertEqual(max_integer([4, 2, 4, 1]), 4)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, 0, 3]), 5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([10**18, 10**19, 10**20]), 10**20)

    def test_all_identical_numbers(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()
