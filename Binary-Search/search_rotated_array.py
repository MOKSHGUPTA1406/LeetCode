"""
Problem: Search in Rotated Sorted Array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1913900745/
Difficulty: Medium
Topic: Array, Binary Search
Date: 12-02-2026

Approach:
Find the middle element of the array and compare it with the target value. If they are equal, return the index. If the left half of the array is sorted (i.e., nums[low] <= nums[mid]), check if the target value is within the range of the left half. If it is, move the high pointer to mid - 1; otherwise, move the low pointer to mid + 1. If the right half of the array is sorted, check if the target value is within the range of the right half. If it is, move the low pointer to mid + 1; otherwise, move the high pointer to mid - 1. Continue this process until the target value is found or the search space is empty.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (len(nums) == 0):
            return -1
        
        low = 0
        high = len(nums)-1
        while (low <= high):
            mid = low+ ((high-low)//2)
            if target == nums[mid]:
                return mid
            elif nums[low]<=nums[mid]:
                if nums[low]<=target and target < nums[mid]:
                    high=mid-1
                else: low=mid+1
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low=mid+1
                else: high=mid-1
        return -1