"""
Problem: Triangle
Link: https://leetcode.com/problems/triangle/submissions/1932858946/
Difficulty: Medium
Topic: Dynamic Programming
Date: 28-02-2026

Approach: We can solve this problem using dynamic programming by starting from the second last row of the triangle and moving upwards. For each cell, we add the minimum of the two adjacent cells from the row below to it. This way, by the time we reach the top of the triangle, the top cell will contain the minimum path sum from the top to the bottom.

Time Complexity: O(n^2), where n is the number of rows in the triangle, since we are iterating through each cell once.
Space Complexity: O(1), since we are modifying the triangle in place and not using any additional data structures.
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for x in range(len(triangle)-2,-1,-1):
            for y in range(0,len(triangle[x])):
                triangle[x][y]+=min(triangle[x+1][y],triangle[x+1][y+1])
        return triangle[0][0]
                
        
        