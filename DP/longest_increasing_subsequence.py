"""
Problem: Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/submissions/1933051634/
Difficulty: Medium
Topic: Dynamic Programming
Date: 28-02-2026

Approach: We can solve this problem using dynamic programming with binary search. We maintain a list `dp` where `dp[i]` represents the smallest tail of all increasing subsequences with length `i+1`. For each number in the input list, we use binary search to find the appropriate position in `dp` to either replace an existing value or append a new value. The length of the `dp` list at the end will give us the length of the longest increasing subsequence.

Time Complexity: O(n log n) where n is the length of the input list, since we iterate through each element once and perform binary search operations.
Space Complexity: O(n) where n is the length of the input list, since we maintain a list `dp` of at most n elements.
"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for x in nums:
            if len(dp) == 0 or dp[-1] < x:
                dp.append(x)
            else:
                left=0
                right= len(dp)-1
                while left <= right:
                    mid = (left + right) // 2
                    if dp[mid] < x:
                        left = mid + 1
                    else:
                        right = mid - 1
                dp[left] = x
        return len(dp)