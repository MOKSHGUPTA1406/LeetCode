"""
Problem: Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/submissions/1913856423/
Difficulty: Easy
Topic: Array, Binary Search
Date: 09-02-2026

Approach:
Find the middle element of the array and compare it with the target value. If they are equal, return the index. If the target value is less than the middle element, repeat the search on the left half of the array. If the target value is greater than the middle element, repeat the search on the right half of the array. Continue this process until the target value is found or the search space is empty then return the left pointer.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right= len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target: return mid
            elif nums[mid]<target:
                left=mid+1
            else: right=mid-1
        return left