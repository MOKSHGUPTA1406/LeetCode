"""
Problem: Coin Change
Link: https://leetcode.com/problems/coin-change/submissions/1932493582/
Difficulty: Medium
Topic: Dynamic Programming
Date: 28-02-2026

Approach: We can solve this problem using dynamic programming. We create a list `dp` where `dp[i]` represents the minimum number of coins needed to make up the amount `i`. We initialize the list with a value greater than the maximum possible coins (amount + 1) and set `dp[0]` to 0 since no coins are needed to make up the amount of 0. We then iterate through each coin and for each coin, we update the `dp` list for all amounts from the coin's value up to the target amount. The value of `dp[n]` is updated to be the minimum of its current value and `dp[n - c] + 1`, which represents using one more coin of denomination `c`.

Time Complexity: O(n * amount) where n is the number of coins and amount is the target amount, since we iterate through each coin and for each coin, we iterate through all amounts from the coin's value up to the target amount.
Space Complexity: O(amount) where amount is the target amount, since we maintain a list `dp` of at most `amount + 1` elements.
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for c in coins:
            print(c)
            for n in range(c, amount+1):
                print(c,n)
                dp[n] = min(dp[n], dp[n-c] + 1)
        print(dp)
        return dp[amount] if dp[amount] != amount + 1 else -1
