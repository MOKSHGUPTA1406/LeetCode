"""
Problem: Majority Element
Link: https://leetcode.com/problems/majority-element/submissions/1950223540/
Difficulty: Easy
Topic: Arrays
Date: 16-03-2026

Approach: To find the majority element, we can sort the array and return the element at the middle index. This works because the majority element appears more than n/2 times, so it will always be at the middle index after sorting.

Time Complexity: O(n log n) due to the sorting step.
Space Complexity: O(1) if we ignore the space used by the sorting algorithm, otherwise O(n) if the sorting algorithm uses additional space.
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]