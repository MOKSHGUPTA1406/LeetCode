"""
Problem: Coin Change II
Link: https://leetcode.com/problems/coin-change-ii/submissions/1946321774/
Difficulty: Medium
Topic: Dynamic Programming
Date: 12-03-2026

Approach: We can use a dynamic programming approach to solve this problem. We will create a list `dp` where `dp[i]` represents the number of ways to make change for the amount `i` using the given coins. We initialize `dp[0]` to 1 because there is one way to make change for the amount 0 (using no coins). We then iterate through each coin and for each coin, we update the `dp` list for all amounts from the coin's value up to the target amount. The number of ways to make change for the current amount `y` can be calculated by adding the number of ways to make change for the amount `y` without using the current coin (which is `dp[y]`) and the number of ways to make change for the amount `y - x` (which is `dp[y - x]`).

Time Complexity: O(n*m), where n is the amount and m is the number of coins. We iterate through each coin and for each coin, we iterate through the amounts up to the target amount.
Space Complexity: O(n), where n is the amount. We use a list of size `amount + 1` to store the number of ways to make change for each amount up to the target amount.
"""

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]* (amount+1)
        dp[0]=1
        for x in coins:
            for y in range(x, amount+1):
                dp[y]=dp[y]+dp[y-x]
        return dp[-1]
