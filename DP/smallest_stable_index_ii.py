"""
Problem: Smallest Stable Index II
Link: https://leetcode.com/problems/smallest-stable-index-ii/submissions/1982271863/
Difficulty: Medium
Topic: Arrays, Dynamic Programming
Date: 19-04-2026

Approach: - We can use two arrays, maxdp and mindp, to store the maximum and minimum values from the left and right sides of the array respectively. We can iterate through the array and fill these two arrays. Then we can iterate through the array again and check if the difference between the maximum and minimum values at each index is less than or equal to k. If it is, we return that index as the answer. If we finish iterating through the array without finding such an index, we return -1. 

Time Complexity: O(n) - We iterate through the array three times, which gives us a linear time complexity.
Space Complexity: O(n) - We use two additional arrays of size n to store the maximum and minimum values.
"""

from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n=len(nums)
        maxdp=[0]*n
        mindp=[0]*n
        maxdp[0]=nums[0]
        mindp[-1]=nums[-1]
        for x in range(1,n):
            maxdp[x]=max(maxdp[x-1],nums[x])
            mindp[n-x-1]=min(mindp[n-x],nums[n-x-1])
        for x in range(n):
            if maxdp[x]-mindp[x]<=k:
                return x
        return -1