"""
Problem: Find if Path Exists in Graph
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/1939026507/
Difficulty: Easy
Topic: Graph Theory
Date: 05-03-2026

Approach: We can use a breadth-first search (BFS) approach to determine if there is a path from the source node to the destination node. We first build an adjacency list representation of the graph from the given edges. Then, we initialize a queue for BFS and a set to keep track of visited nodes. We start from the source node and explore its neighbors. If we reach the destination node during our exploration, we return True. If we exhaust all possible nodes without finding the destination, we return False.

Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. We need to build the graph and perform BFS, which takes linear time relative to the number of vertices and edges.
Space Complexity: O(V + E), where V is the number of vertices and E is the number of edges. The adjacency list representation of the graph takes O(V + E) space, and the visited set and queue can also take up to O(V) space in the worst case.
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set([source])
        q=deque([source])
        while q:
            node=q.pop()
            if node==destination:
                return True
            for x in graph[node]:
                if x not in visited:
                    visited.add(x)
                    q.append(x)
        return False
        