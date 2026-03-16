"""
Problem: Remove Element
Link: https://leetcode.com/problems/remove-element/submissions/1950385456/
Difficulty: Easy
Topic: Arrays
Date: 16-03-2026

Approach: 1. Initialize a pointer k to keep track of the position of the next non-val element.
2. Iterate through the array nums using a loop.
3. If the current element is not equal to val, assign it to the position pointed by k and increment k.
4. After the loop, k will represent the new length of the array with all occurrences of val removed.

Time Complexity: O(n) where n is the length of the input array nums, since we need to iterate through all elements once.
Space Complexity: O(1) since we are modifying the array in-place and not using any additional data structures.
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for x in range(len(nums)):
            if nums[x]!=val:
                nums[k]=nums[x]
                k+=1
        return k