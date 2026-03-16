"""
Problem: Maximal Square
Link: https://leetcode.com/problems/maximal-square/submissions/1937996582/
Difficulty: Medium
Topic: Dynamic Programming
Date: 04-03-2026

Approach: We can use dynamic programming to solve this problem. We create a 2D array `dp` where `dp[i][j]` represents the side length of the largest square that can be formed with the bottom-right corner at position `(i-1, j-1)` in the original matrix. We iterate through each cell in the original matrix, and if we encounter a '1', we update our `dp` array based on the minimum of the three neighboring cells (top, left, and top-left) plus one. We also keep track of the maximum side length found during the iteration.

Time Complexity: O(m * n) where m and n are the dimensions of the matrix, since we iterate through each element once.
Space Complexity: O(m * n), since we create a 2D array `dp` to store the side lengths of squares.
"""

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]=='1':
                    dp[r+1][c+1]=min(dp[r][c],dp[r+1][c],dp[r][c+1])+1
                    max_side = max(max_side, dp[r+1][c+1])
        return max_side * max_side
                