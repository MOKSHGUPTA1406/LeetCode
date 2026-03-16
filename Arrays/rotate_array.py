"""
Problem: Rotate Array
Link: https://leetcode.com/problems/rotate-array/submissions/1950233074/
Difficulty: Medium
Topic: Arrays
Date: 16-03-2026

Approach: To rotate the array to the right by k steps, we can use slicing to rearrange the elements. We first calculate the effective rotation by taking k modulo the length of the array. Then we can slice the array into two parts: the last 'rotate' elements and the first 'len(nums) - rotate' elements. Finally, we concatenate these two parts in reverse order to achieve the rotated array.

Time Complexity: O(n), where n is the length of the array, since we are slicing and concatenating the array.
Space Complexity: O(1), since we are modifying the array in-place without using any additional data structures.
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate = k % len(nums)
        print(len(nums)-rotate,rotate)
        nums[:rotate],nums[rotate:] = nums[len(nums)-rotate:],nums[:len(nums)-rotate]