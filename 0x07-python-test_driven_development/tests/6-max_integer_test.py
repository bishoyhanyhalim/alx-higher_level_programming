#!/usr/bin/python3
"""this is an func good"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """this is an func good"""

    def test_unordered_list(self):
        """now lets test files"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """now lets test files"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """now lets test files"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ordered_list(self):
        """now lets test files"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_ints_and_floats(self):
        """now lets test files"""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_empty_string(self):
        """now lets test files"""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """now lets test files"""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """now lets test files"""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_one_element_list(self):
        """now lets test files"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)


if __name__ == '__main__':
    unittest.main()
