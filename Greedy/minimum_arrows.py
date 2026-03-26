"""
Problem: Minimum Number of Arrows to Burst Balloons
Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/1951424646/
Difficulty: Medium
Topic: Greedy
Date: 17-03-2026

Approach: 1. We first sort the list of points (balloons) based on their end coordinates. This allows us to efficiently determine how many balloons can be burst with a single arrow.
2. We initialize a variable `arrow` to count the number of arrows needed, starting with 1, since we will need at least one arrow to burst the first balloon.
3. We also initialize `curr_end` to the end coordinate of the first balloon, which represents the position where we will shoot the first arrow.
4. We iterate through the sorted list of balloons starting from the second balloon. For each balloon, we check if its start coordinate is less than or equal to `curr_end`. If it is, it means that the current arrow can burst this balloon as well, so we continue to the next balloon.
5. If the start coordinate of the current balloon is greater than `curr_end`, it means that the current arrow cannot burst this balloon, and we need to shoot another arrow. We increment the `arrow` count and update `curr_end` to the end coordinate of the current balloon.
6. After iterating through all the balloons, we return the total number of arrows needed.

Time Complexity: O(n log n), where n is the number of balloons. This is due to the sorting step. The rest of the operations are O(n).
Space Complexity: O(1), as we are using only a constant amount of extra space for the variables.
"""

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow=1
        curr_end=points[0][1]
        for x in range(1,len(points)):
            if points[x][0]<=curr_end:
                continue
            arrow+=1
            curr_end=points[x][1]
        return arrow