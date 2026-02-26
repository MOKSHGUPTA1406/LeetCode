"""
Problem: Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/submissions/1932179357/
Difficulty: Easy
Topic: Dynamic Programming
Date: 27-02-2026

Approach:
To solve the min cost climbing stairs problem, we can use dynamic programming. The minimum cost to reach the top of the stairs can be expressed as the minimum of the cost to reach the last step plus the cost of that step, and the cost to reach the second last step plus the cost of that step. This leads to the following recurrence relation:
dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

Time Complexity: O(n) since we need to compute the minimum cost for each stair from 2 to n.
Space Complexity: O(n) since we are storing the minimum cost for each stair in a dp array.
"""


from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        for x in range(2,len(cost)+1):
            dp[x]=min(dp[x-1]+cost[x-1],dp[x-2]+cost[x-2])
        return dp[len(cost)]