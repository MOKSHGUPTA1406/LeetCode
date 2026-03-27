"""
Problem: Count Submatrices With Top Left Element and Sum Less Than K
Link: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/submissions/1952304484/
Difficulty: Medium
Topic: Arrays
Date: 18-03-2026

Approach: We can use a prefix sum approach to calculate the sum of submatrices efficiently. We iterate through the grid and update the prefix sums in place. For each cell, we check if the sum of the submatrix from the top-left corner to that cell is less than or equal to k. If it is, we increment our count. We also keep track of the last column where the sum exceeded k to optimize our inner loop.

Time Complexity: O(n log n) due to the sorting step.
Space Complexity: O(1) since we are modifying the input grid in place.
"""

from typing import List
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r, c=len(grid), len(grid[0])
        cnt, brCol=0, c
        if grid[0][0]>k:
            return 0
        cnt+=1
        for j in range(1, c):
            grid[0][j]+=grid[0][j-1]
            if grid[0][j]>k:
                brCol=j
                break
            cnt+=1
        for i in range(1, r):
            grid[i][0]+=grid[i-1][0]
            if grid[i][0]>k:
                break
            cnt+=1
            for j in range(1, brCol):
                grid[i][j]+=grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1]
                if grid[i][j]>k:
                    brCol=j
                    break
                cnt+=1
        return cnt