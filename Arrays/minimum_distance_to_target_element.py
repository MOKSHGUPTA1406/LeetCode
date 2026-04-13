"""
Problem: Minimum Distance to the Target Element
Link: https://leetcode.com/problems/minimum-distance-to-the-target-element/submissions/1976955472/
Difficulty: Easy
Topic: Arrays
Date: 13-04-2026

Approach: We can iterate through the array and check for each element if it is equal to the target. If it is, we calculate the distance from the current index to the start index and update our answer with the minimum distance found.

Time Complexity: O(n), where n is the length of the input array, since we need to iterate through the array once to find the target elements and calculate their distances.
Space Complexity: O(1), since we are using only a constant amount of extra space to store the answer and the loop variable.
"""

from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans=10001
        for x in range(len(nums)):
            if nums[x]==target:
                ans=min(ans,abs(x-start))
        return ans