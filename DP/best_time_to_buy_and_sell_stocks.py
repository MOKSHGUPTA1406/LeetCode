"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1950203860/
Difficulty: Easy
Topic: Dynamic Programming, Array
Date: 16-03-2026

Approach: We can solve this problem by keeping track of the minimum price we have seen so far and the maximum profit we can achieve at each step. We initialize the minimum price to the first element of the prices array and the profit to 0. We then iterate through the prices array starting from the second element. For each price, we check if it is less than the current minimum price. If it is, we update the minimum price. Otherwise, we calculate the potential profit by subtracting the minimum price from the current price and update our maximum profit if this potential profit is greater than our current maximum profit. Finally, we return the maximum profit.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=prices[0]
        profit=0
        for x in range(1,len(prices)):
            if mn>prices[x]:
                mn=prices[x]
            else:
                profit=max(profit,prices[x]-mn)
        return profit