"""
Problem: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1945680369/
Difficulty: Easy
Topic: Arrays
Date: 12-03-2026

Approach: 1. Initialize a pointer k to keep track of the position of the next unique element.
2. Iterate through the array nums using a loop.
3. If the current element is not equal to the next element, assign it to the position pointed by k and increment k.
4. After the loop, k will represent the new length of the array with all duplicates removed

Time Complexity: O(n) where n is the length of the input array nums, since we need to iterate through all elements once.
Space Complexity: O(1) since we are modifying the array in-place and not using any additional data structures.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for x in range(len(nums)-1):
            if nums[x]!=nums[x+1]:
                nums[k]=nums[x+1]
                k+=1
        return k