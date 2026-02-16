"""
Problem: Find All Numbers Disappeared in an Array
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1921214198/
Difficulty: Easy
Topic: Arrays
Date: 16-02-2026

Approach: We can create a set from the input list to store the unique numbers. Then, we iterate through the numbers from 1 to n (where n is the length of the input list) and check if each number is present in the set. If a number is not present in the set, it means it has disappeared from the array, and we add it to our result list. Finally, we return the result list.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        num_set=set(nums)
        for x in range(1,len(nums)+1):
            if x not in num_set:
                ans.append(x)
        return ans
