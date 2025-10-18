import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 6, 7]), 10)

    def test_max_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_single(self):
        self.assertEqual(max_integer([7]), 7)

    def test_max_with_string_elements(self):
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_max_with_mixed_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "a", 4])


if __name__ == '__main__':
    unittest.main()
