"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    # Test case 1: All positive numbers
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

    # Test case 2: All negative numbers
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

    # Test case 3: Mixed numbers
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    # Test case 4: Single element
    assert max_subarray_sum([5]) == 5

    # Test case 5: Two elements
    assert max_subarray_sum([3, -1]) == 3

def test_max_subarray_sum_edge_cases():
    # Test case 6: Empty list
    with pytest.raises(ValueError, match="Input list is invalid. Please provide a valid list of integers."):
        max_subarray_sum([])

    # Test case 7: List with non-integer values
    with pytest.raises(ValueError, match="Input list is invalid. Please provide a valid list of integers."):
        max_subarray_sum([1, 2, 'a', 4])