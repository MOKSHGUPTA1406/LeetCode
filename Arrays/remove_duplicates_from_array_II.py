"""
Problem: Remove Duplicates from Sorted Array II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/1950219803/
Difficulty: Medium
Topic: Arrays
Date: 16-03-2026

Approach: We can use a two-pointer approach to solve this problem. We maintain a pointer `k` that keeps track of the position where the next unique element should be placed. We iterate through the array starting from the third element (index 2) and compare it with the element at position `k-2`. If they are different, it means we have found a new unique element, and we can place it at position `k` and increment `k`. This way, we ensure that each element can appear at most twice in the modified array.

Time Complexity: O(n), where n is the length of the input array. We traverse the array once.
Space Complexity: O(1), since we are modifying the array in place and using only a constant amount of extra space.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        for x in range(2,len(nums)):
            if nums[x]!=nums[k-2]:
                nums[k]=nums[x]
                k+=1
        return k