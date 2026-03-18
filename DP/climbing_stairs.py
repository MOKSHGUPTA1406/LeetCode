"""
Problem: Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/submissions/1932159562/
Difficulty: Easy
Topic: Dynamic Programming
Date: 27-02-2026

Approach:
To solve the climbing stairs problem, we can use dynamic programming. The number of ways to climb n stairs can be expressed as the sum of the ways to climb n-1 stairs and n-2 stairs, since from the last step you can either take a single step or a double step. This leads to the following recurrence relation:
ways(n) = ways(n-1) + ways(n-2)

Time Complexity: O(n) since we need to compute the number of ways for each stair from 3 to n.
Space Complexity: O(1) since we are only storing a constant amount of space for the last two computed values.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        first=1
        second=2
        for x in range(n-2):
            num=first+second
            first=second
            second=num
        return num
