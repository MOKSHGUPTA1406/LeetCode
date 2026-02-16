"""
Problem: How Many Numbers Are Smaller Than the Current Number
Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/1921199584/
Difficulty: Easy
Topic: Arrays
Date: 16-02-2026

Approach: We can create a list of size n to store the count of numbers smaller than each element in the input list. We use two nested loops to compare each element with every other element in the list. If we find an element that is smaller than the current element, we increment the count for that element in our result list. Finally, we return the result list.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[0 for _ in range(len(nums))]
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[y]<nums[x]:
                    l[x]+=1
        return l