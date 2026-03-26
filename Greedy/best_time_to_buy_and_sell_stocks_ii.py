"""
Problem: Best Time to Buy and Sell Stock II
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1950207817/
Difficulty: Medium
Topic: Greedy
Date: 17-03-2026

Approach: To solve this problem, we can use a greedy approach. The idea is to iterate through the list of prices and whenever we find a price that is higher than the previous day's price, we can consider it as a profitable transaction. We can simply add the difference between the current price and the previous price to our total profit. This way, we are effectively buying at the previous day's price and selling at the current day's price whenever it is profitable to do so. Finally, we return the total profit.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for x in range(len(prices)-1):
            if prices[x+1]>prices[x]:
                profit+=prices[x+1]-prices[x]
        return profit