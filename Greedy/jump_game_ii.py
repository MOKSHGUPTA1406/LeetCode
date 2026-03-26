"""
Problem: Jump Game II
Link: https://leetcode.com/problems/jump-game-ii/submissions/1951225332/
Difficulty: Medium
Topic: Greedy
Date: 17-03-2026

Approach: To solve the Jump Game II problem, we can use a greedy approach. The idea is to keep track of the farthest reachable index at each step and count the number of jumps needed to reach the end of the array. We initialize three variables: `jumps` to count the number of jumps, `curr` to keep track of the current end of the jump, and `farthest` to keep track of the farthest reachable index. We iterate through the array, updating `farthest` with the maximum reachable index at each step. When we reach the end of the current jump (`curr`), we increment the `jumps` counter and update `curr` to `farthest`. This process continues until we reach or exceed the last index of the array.

Time Complexity: O(n), where n is the length of the input array. We traverse the array once to determine the minimum number of jumps.
Space Complexity: O(1), as we are using only a constant amount of extra space for the variables.
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        jumps=0
        curr=0
        farthest=0
        for x in range(len(nums)-1):
            farthest=max(farthest,x+nums[x])
            if x==curr:
                jumps+=1
                curr=farthest
        return jumps
