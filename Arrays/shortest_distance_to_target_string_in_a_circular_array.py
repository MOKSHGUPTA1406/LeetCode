
"""
Problem: Shortest Distance to Target String in a Circular Array
Link: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/submissions/1979101798/
Difficulty: Easy
Topic: Arrays
Date: 15-04-2026

Approach: We can use a two-pointer approach to find the shortest distance to the target string in a circular array. We will start from the given index and move both left and right pointers simultaneously until we find the target string. We will keep track of the minimum distance found.

Time Complexity: O(n), where n is the length of the input array. In the worst case, we may have to traverse the entire array to find the target string.
Space Complexity: O(1), as we are using only a constant amount of extra space to store the pointers and the minimum distance.
"""

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        words=words[startIndex::]+words[:startIndex]
        ans=len(words)
        for x in range(len(words)):
            if words[x]==target:
                ans=min(ans,x)
        for x in range(len(words)-1,-1,-1):
            if words[x]==target:
                ans=min(ans,len(words)-x)
        if ans==len(words): return -1
        return ans
            