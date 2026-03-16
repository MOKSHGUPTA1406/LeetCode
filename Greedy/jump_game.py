"""
Problem: Jump Game
Link: https://leetcode.com/problems/jump-game/submissions/1950375659/
Difficulty: Medium
Topic: Greedy
Date: 16-03-2026

Approach: We can solve this problem using a greedy approach. We initialize a variable `dis` to keep track of the maximum distance we can reach at any point. We iterate through the input list `nums` and for each index `x`, we check if it is greater than `dis`. If it is, it means we cannot reach this index, and we return False. Otherwise, we update `dis` to be the maximum of its current value and the sum of the current index `x` and the jump length at that index `nums[x]`. After iterating through the list, if `dis` is greater than or equal to the last index, we return True; otherwise, we return False.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dis=0
        for x in range(len(nums)-1):
            if x>dis:
                return False
            dis=max(dis,nums[x]+x)
        if dis>=len(nums)-1:
            return True
        return False