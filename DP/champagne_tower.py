"""
Problem: Champagne Tower
Link: https://leetcode.com/problems/champagne-tower/submissions/1919117727/
Difficulty: Medium
Topic: Dynamic Programming
Date: 14-02-2026

Approach:
We can use a 2D array (dp) to represent the amount of champagne in each glass. We start by pouring the champagne into the top glass (dp[0][0]). For each glass, if it contains more than 1 unit of champagne, we calculate the excess amount and distribute it equally to the two glasses below it. We repeat this process until we have filled all the glasses up to the query row. Finally, we return the amount of champagne in the queried glass.

Time Complexity: O(query_row^2) - We need to fill the dp array up to the query row, which involves iterating through each glass in that row.
Space Complexity: O(query_row^2) - We are using a 2D array to store the amount of champagne in each glass up to the query row.
"""

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * 102 for _ in range(102)]
        dp[0][0] = poured
        
        for glrow in range(query_row + 1):
            for glcol in range(glrow + 1):
                if dp[glrow][glcol] > 1:
                    excess = (dp[glrow][glcol] - 1.0) / 2.0
                    dp[glrow][glcol] = 1
                    dp[glrow+1][glcol] += excess
                    dp[glrow+1][glcol+1] += excess
                    
        return dp[query_row][query_glass]