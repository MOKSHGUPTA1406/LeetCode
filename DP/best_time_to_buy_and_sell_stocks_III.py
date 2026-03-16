"""
Problem: Best Time to Buy and Sell Stock III
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/1937038084/
Difficulty: Hard
Topic: Dynamic Programming
Date: 03-03-2026

Approach: We can solve this problem using dynamic programming by keeping track of the maximum profit at each step for two transactions. We maintain four variables: `buy1`, `sell1`, `buy2`, and `sell2`.
- `buy1` represents the maximum profit after the first buy, which is initialized to the negative of the first price.
- `sell1` represents the maximum profit after the first sell, which is initialized to 0.
- `buy2` represents the maximum profit after the second buy, which is initialized to the negative of the first price.
- `sell2` represents the maximum profit after the second sell, which is initialized to 0. We iterate through the prices and update these variables accordingly:
- For `buy1`, we take the maximum of the current `buy1` and the negative of the current price.
- For `sell1`, we take the maximum of the current `sell1` and the profit from selling the stock bought in `buy1` at the current price.
- For `buy2`, we take the maximum of the current `buy2` and the profit from selling the stock bought in `buy1` and then buying again at the current price.
- For `sell2`, we take the maximum of the current `sell2` and the profit from selling the stock bought in `buy2` at the current price. Finally, we return `sell2` as the maximum profit from at most two transactions.

Time Complexity: O(n) where n is the length of `prices`, since we iterate through each element once.
Space Complexity: O(1), since we only use a constant amount of extra space.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for i in range(1, len(prices)):
            price = prices[i]

            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        
        return sell2