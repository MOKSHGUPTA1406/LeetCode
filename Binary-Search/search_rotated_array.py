"""
Problem: Find Minimum in Rotated Sorted Array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Medium
Topic: Array, Binary Search
Date: 09-02-2026

Approach:
Find the middle element of the array and compare it with the rightmost element. If the middle element is less than or equal to the rightmost element, it means the minimum value is in the left half of the array, so we move the right pointer to mid. Otherwise, the minimum value is in the right half of the array, so we move the left pointer to mid + 1. Continue this process until left and right pointers converge, at which point left will be pointing to the minimum element.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]