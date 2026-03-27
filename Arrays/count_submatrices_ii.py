"""
Problem: Count Submatrices With Equal Frequency of X and Y
Link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/submissions/1953312983/
Difficulty: Medium
Topic: Arrays
Date: 19-03-2026

Approach: We can iterate through each row of the grid and maintain two cumulative sums: one for 'X' and one for 'Y'. For each cell, we update these cumulative sums based on whether the cell contains 'X' or 'Y'. If at any point the cumulative sums are equal, it means we have found a submatrix with an equal frequency of 'X' and 'Y', and we can increment our result counter.

Time Complexity: O(rows * cols), where rows is the number of rows in the grid and cols is the number of columns. We iterate through each cell once.
Space Complexity: O(cols), as we are using two arrays to store the cumulative sums for 'X' and 'Y' for each column.
"""

from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        sumX = [0] * cols
        sumY = [0] * cols
        res = 0

        for i in range(rows):
            rx = 0
            ry = 0
            for j in range(cols):
                if grid[i][j] == 'X':
                    rx += 1
                elif grid[i][j] == 'Y':
                    ry += 1
                
                sumX[j] += rx
                sumY[j] += ry
                
                if sumX[j] > 0 and sumX[j] == sumY[j]:
                    res += 1

        return res