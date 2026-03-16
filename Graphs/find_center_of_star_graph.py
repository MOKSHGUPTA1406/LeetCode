"""
Problem: Find Center of Star Graph
Link: https://leetcode.com/problems/find-center-of-star-graph/submissions/1938805939/
Difficulty: Easy
Topic: Graph Theory
Date: 05-03-2026

Approach: We can use a set to keep track of the visited nodes. We iterate through each edge and check if either of the nodes in the edge has already been visited. If we find a node that has already been visited, that node is the center of the star graph. If not, we add both nodes to the visited set.

Time Complexity: O(n), where n is the number of edges in the graph. We need to iterate through all the edges once.
Space Complexity: O(n), where n is the number of edges in the graph. In the worst case, we may need to store all nodes in the visited set.
"""

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited=[]
        for x in edges:
            for y in range(2):
                if x[y] not in visited:
                    visited.append(x[y])
                else:
                    return x[y]
        
        