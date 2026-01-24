#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test with ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([1, 4, 4, 2]), 4)

    def test_all_same(self):
        """Test with all elements same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.3, 2.1]), 3.3)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.2]), 4.2)

    def test_large_list(self):
        """Test with large list"""
        self.assertEqual(max_integer(list(range(1000))), 999)

    def test_max_at_beginning(self):
        """Test with maximum at beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_max_at_end(self):
        """Test with maximum at end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test with maximum in middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative(self):
        """Test with one negative number"""
        self.assertEqual(max_integer([-5]), -5)

    def test_string_in_list(self):
        """Test with string in list (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4])

    def test_none_as_argument(self):
        """Test with None as argument (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict_in_list(self):
        """Test with dictionary in list (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, {'a': 3}, 4])

    def test_tuple_in_list(self):
        """Test with tuple in list (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, (3, 4), 5])


if __name__ == '__main__':
    unittest.main()
