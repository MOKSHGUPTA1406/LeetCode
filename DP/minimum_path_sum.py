"""
Problem: Minimum Path Sum
Link: https://leetcode.com/problems/minimum-path-sum/submissions/1932881994/
Difficulty: Medium
Topic: Dynamic Programming
Date: 28-02-2026

Approach: To solve the minimum path sum problem, we can use dynamic programming. We modify the input grid in-place to store cumulative sums. We initialize the first row and first column by accumulating values from the previous cells. For each remaining cell, we update its value by adding the minimum of the cumulative sum from the top and left cells.

Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid, since we need to iterate through each cell once.
Space Complexity: O(1) since we modify the input grid in-place.
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for x in range(1,len(grid)):
            grid[x][0]+=grid[x-1][0]
        for x in range(1,len(grid[0])):
            grid[0][x]+=grid[0][x-1]
        for x in range(1,len(grid)):
            for y in range(1,len(grid[0])):
                grid[x][y]+=min(grid[x-1][y],grid[x][y-1])
        return grid[-1][-1]
        
        