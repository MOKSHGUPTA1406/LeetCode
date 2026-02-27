"""
Problem: Unique Paths II
Link: https://leetcode.com/problems/unique-paths-ii/submissions/1933028636/
Difficulty: Medium
Topic: Dynamic Programming
Date: 28-02-2026

Approach: To solve the unique paths with obstacles problem, we can use dynamic programming. We create a 2D dp array where dp[i][j] represents the number of unique paths to reach cell (i, j). We initialize the first row and first column based on the presence of obstacles. For each cell, if there is an obstacle, we set dp[i][j] to 0. Otherwise, we calculate dp[i][j] as the sum of dp[i-1][j] and dp[i][j-1], which represent the paths from the top and left cells respectively.

Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the obstacleGrid.
Space Complexity: O(m*n) where m is the number of rows and n is the number of columns in the obstacleGrid.
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1: return 0
        dp=[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[0][0]=1
        for x in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][x]==1:
                break
            dp[0][x]=1
        for x in range(1,len(obstacleGrid)):
            if obstacleGrid[x][0]==1:
                break
            dp[x][0]=1
        for x in range(1,len(obstacleGrid)):
            for y in range(1,len(obstacleGrid[0])):
                if obstacleGrid[x][y]==1:
                    dp[x][y]=0
                    continue
                dp[x][y]+=dp[x-1][y]+dp[x][y-1]
        return dp[-1][-1]
        
        