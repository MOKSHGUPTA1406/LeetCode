"""
Problem: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/submissions/1945664923/
Difficulty: Easy
Topic: Arrays
Date: 12-03-2026

Approach: 1. Remove the last n elements from nums1 (which are placeholders).
2. Append all elements of nums2 to nums1.
3. Sort nums1 to get the merged sorted array.

Time Complexity: O((m+n) log(m+n)) due to the sorting step.
Space Complexity: O(1) since we are modifying nums1 in-place and not using any additional data structures.
"""

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(n):
            nums1.pop()
        nums1+=nums2
        nums1.sort()
        