"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/submissions/1951248807/
Difficulty: Medium
Topic: Arrays
Date: 17-03-2026

Approach: We can use the two-pointer technique to solve this problem efficiently. We will initialize two pointers, one at the beginning of the array and the other at the end. We will calculate the area formed by the lines at these two pointers and keep track of the maximum area found. Then, we will move the pointer that points to the shorter line inward, as moving the taller line won't increase the area. We will repeat this process until the two pointers meet.

Time Complexity: O(n), where n is the number of elements in the input array. We traverse the array at most once with the two pointers.
Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables to store the maximum area.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left=0
        right=len(height)-1
        while left<right:
            ans=max(ans,min(height[left],height[right])*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans