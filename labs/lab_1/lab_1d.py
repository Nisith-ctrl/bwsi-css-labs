"""
lab_1d.py

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Derived from LeetCode problem: https://leetcode.com/problems/two-sum/ (leetcode easy)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Function that takes in a list of integers and a target integer, and returns the indices of the two numbers that add up to the target.

    Args:
        nums (list[int]): List of integers.
        target (int): Target integer.
    
    Returns:
        list[int]: Indices of the two numbers that add up to the target.
    """
    if len(nums) < 2:
        raise ValueError("Input list must contain at least two numbers.")
    
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    raise ValueError("No two numbers add up to the target.")

# Example usage:
def main():
    nums = [1]
    target = 9
    try:
        result = two_sum(nums, target)
        print(f"Indices of the two numbers that add up to {target}: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()