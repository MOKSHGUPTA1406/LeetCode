"""
Problem: Set Mismatch
Link: https://leetcode.com/problems/set-mismatch/submissions/1921168139/
Difficulty: Easy
Topic: Arrays, Hash Table
Date: 16-02-2026

Approach: We can create a list of size n+1 to count the occurrences of each number in the input list. We iterate through the input list and increment the count for each number. After that, we iterate through the counting list to find the number that appears twice (the one with a count of 2) and the number that is missing (the one with a count of 0). Finally, we return these two numbers as a list.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[0 for _ in range(len(nums)+1)]
        twice=-1
        missing=-1
        for x in nums:
            l[x]+=1
        for x in range(1,len(l)):
            if l[x]==2:
                twice=x
            if l[x]==0:
                missing=x
        return [twice,missing]

