#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""
    
    def test_max_integer(self):
        """Test with regular integer lists"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)  # Maximum is 4
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)  # Maximum is 4
        self.assertEqual(max_integer([10, 5, 6, 7]), 10)  # Maximum is 10
    
    def test_max_empty(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)  # Empty list returns None
    
    def test_max_single(self):
        """Test with a list containing only one element"""
        self.assertEqual(max_integer([7]), 7)  # Single element, returns itself
    
    def test_max_negative(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)  # Maximum is -1
    
    def test_max_with_strings(self):
        """Test with a list containing strings"""
        # The function will not raise a TypeError, and will return the maximum value
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")  # Lexicographical comparison
    
    def test_max_with_mixed_elements(self):
        """Test with a list containing mixed types"""
        # The function will still try to compare elements lexicographically and will return the maximum value
        self.assertEqual(max_integer([10, "apple", 30]), 30)  # Maximum integer is 30
    
    def test_max_with_empty_strings(self):
        """Test with a list containing empty strings"""
        self.assertEqual(max_integer(["", "apple", "banana"]), "banana")  # Lexicographical comparison
    
if __name__ == '__main__':
    unittest.main()
