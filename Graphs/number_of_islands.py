"""
Problem: Number of Islands
Link: https://leetcode.com/problems/number-of-islands/submissions/1944248977/
Difficulty: Medium
Topic: Graph Theory
Date: 10-03-2026

Approach: We can solve this problem using Depth First Search (DFS). We will iterate through each cell in the grid. If we encounter a '1', it means we have found an island. We will then perform a DFS to mark all connected '1's as '0' to avoid counting them again. We will increment our island count for each new island we find.

Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid. We need to iterate through all the cells once.
Space Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid. In the worst case, we may need to store all cells in the visited set.
"""

from typing import List

class Solution:
    def dfs(self, grid: List[List[str]], x: int, y: int):
        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]=='0':
            return
        grid[x][y]='0'
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x, y - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]=='1':
                    self.dfs(grid,x,y)
                    count+=1
        return count
