"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    # Test case 1: Basic test case
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Test case 2: Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # Test case 3: Mixed numbers
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Test case 4: Multiple pairs (should return the first pair found)
    assert two_sum([1, 3, 7, 9, 2], 10) == [3, 4]

def test_two_sum_edge_cases():
    # Test case 5: Empty list
    with pytest.raises(ValueError, match="Input list must contain at least two numbers."):
        two_sum([], 0)

    # Test case 6: List with only one number
    with pytest.raises(ValueError, match="Input list must contain at least two numbers."):
        two_sum([5], 10)

    # Test case 7: No solution exists
    with pytest.raises(ValueError, match="No two numbers add up to the target."):
        two_sum([1, 2, 3], 10)