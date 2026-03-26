"""
Problem: Get Biggest Three Rhombus Sums in a Grid
Link: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/submissions/1950455219/
Difficulty: Medium
Topic: Heap
Date: 16-02-2026

Approach:
To solve this problem, we can use a min-heap to keep track of the three largest rhombus sums. We will iterate through each cell in the grid and calculate the rhombus sums for different sizes of rhombuses centered at that cell. The rhombus sum can be calculated by summing the values of the cells that form the rhombus shape. We will ensure that we only consider valid rhombuses that fit within the grid boundaries. As we calculate each rhombus sum, we will add it to the min-heap if it is not already present. If the size of the heap exceeds three, we will remove the smallest element from the heap. Finally, we will return the three largest rhombus sums in descending order.

Time Complexity: O(m * n * k), where m and n are the dimensions of the grid and k is the maximum size of the rhombus. In the worst case, k can be O(min(m, n)).
Space Complexity: O(1) for the heap, as we are only storing three elements at any time, and O(m * n) for the grid itself.
"""

from typing import List
from heapq import heapify, heappush, heappop
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        max_length = min((m - 1) // 2, (n - 1) // 2)
        best = []
        heapify(best)
        def rhombusSum(r, c, k):
            result = grid[r][c]
            for s in range(k):
                r += 1
                result += grid[r][c + s + 1]
                result += grid[r][c - s - 1]
            for s in range(k - 1, -1, -1):
                r += 1
                result += grid[r][c + s]
                if s > 0:
                    result += grid[r][c - s]
            return result
        for r in range(m):
            for c in range(n):
                for k in range(max_length + 1):
                    if c >= k and c + k < n and r + 2 * k < m:
                        candidate = rhombusSum(r, c, k)
                        if candidate not in set(best):
                            heappush(best, candidate)
                        if len(best) > 3:
                            heappop(best)
        return sorted(best, reverse = True)