"""
Problem: House Robber
Link: https://leetcode.com/problems/house-robber/submissions/1932190204/
Difficulty: Medium
Topic: Dynamic Programming
Date: 27-02-2026

Approach:
To solve the house robber problem, we can use dynamic programming. The maximum amount of money that can be robbed up to the i-th house can be expressed as the maximum of the money robbed up to the (i-1)-th house and the money robbed up to the (i-2)-th house plus the money in the i-th house. This leads to the following recurrence relation:
dp[i] = max(dp[i-1], nums[i] + dp[i-2])

Time Complexity: O(n) since we need to compute the maximum money for each house from 1 to n.
Space Complexity: O(n) since we are storing the maximum money for each house in a dp array.
"""


from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        dp=[0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for x in range(2,len(nums)):
            dp[x]=max(dp[x-1],nums[x]+dp[x-2])
        return dp[-1]
