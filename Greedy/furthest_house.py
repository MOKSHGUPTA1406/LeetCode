"""
Problem: Two Furthest Houses With Different Colors
Link: https://leetcode.com/problems/two-furthest-houses-with-different-colors/submissions/1983729204/
Difficulty: easy
Topic: Array,Greedy
Date: 20-04-2026

Approach: We can use a two-pointer approach to find the two furthest houses with different colors. We start with one pointer at the beginning of the array and another pointer at the end of the array. We move the left pointer towards the right until we find a house that has a different color than the last house. Similarly, we move the right pointer towards the left until we find a house that has a different color than the first house. Finally, we return the maximum distance between these two pointers.


Time Complexity: O(n) where n is the length of the input array, since we may need to traverse the entire array once to find the two furthest houses with different colors.
Space Complexity: O(1) since we are using only a constant amount of extra space to store the pointers and the result.
"""

from typing import List

class Solution:
    def maxDistance(self, A: List[int]) -> int:
        n = len(A)
        left, right = 0, n - 1
        for i in range(n):
            if A[i] ^ A[-1]:
                left = i
                break
        for i in range(n - 1, -1, -1):
            if A[i] ^ A[0]:
                right = i
                break
        return max(n - 1 - left, right)
