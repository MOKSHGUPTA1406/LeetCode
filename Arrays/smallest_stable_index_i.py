"""
Problem: Smallest Stable Index I
Link: https://leetcode.com/problems/smallest-stable-index-i/submissions/1982256849/
Difficulty: Easy
Topic: Arrays
Date: 19-04-2026

Approach: - We will iterate through the array and for each index, we will calculate the maximum value from the left side and the minimum value from the right side. We will then check if the difference between the maximum value and the minimum value is less than or equal to k. If it is, we will update our answer with the minimum index. 

Time Complexity: O(n^2) - We are iterating through the array and for each index, we are calculating the maximum and minimum values which takes O(n) time.
Space Complexity: O(1) - We are using a constant amount of space to store the answer and the temporary variables for maximum and minimum values.
"""

from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        ans=101
        for i,x in enumerate(nums):
            v=max(nums[0:i+1])-min(nums[i:len(nums)])
            if v<=k:
                ans=min(ans,i)
        if ans==101: return -1
        return ans