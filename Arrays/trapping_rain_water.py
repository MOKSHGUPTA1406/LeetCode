"""
Problem: Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/submissions/1951504948/
Difficulty: Hard
Topic: Arrays, Two Pointers
Date: 17-03-2026

Approach: We can use the two-pointer technique to solve this problem efficiently. We will initialize two pointers, one at the beginning of the array and the other at the end. We will keep track of the maximum height seen so far from both sides. For each position, we will calculate the water that can be trapped based on the minimum of the maximum heights from both sides minus the current height. We will move the pointer that points to the shorter line inward, as moving the taller line won't increase the water trapped.

Time Complexity: O(n), where n is the number of elements in the height array, since we will traverse the array at most once.
Space Complexity: O(1), since we are using only a constant amount of extra space for the pointers and variables to keep track of the maximum heights and water trapped.
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        left=0
        right=len(height)-1
        left_max=0
        right_max=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=left_max:
                    left_max=height[left]
                else:
                    water+=left_max-height[left]
                left+=1
            elif height[right]<=height[left]:
                if height[right]>=right_max:
                    right_max=height[right]
                else:
                    water+=right_max-height[right]
                right-=1
        return water

            
            