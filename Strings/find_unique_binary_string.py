
"""
Problem: Find Unique Binary String
Link: https://leetcode.com/problems/find-unique-binary-string/submissions/1942180138/
Difficulty: Medium
Topic: Strings
Date: 08-03-2026

Approach:
The approach is to use diagonalization. For each string in the list, we flip the bit at the diagonal position (i.e., if the bit is '0', we make it '1' and vice versa). This ensures that the resulting string is different from every string in the list.

Time Complexity: O(n), where n is the number of strings in the input list.
Space Complexity: O(n), where n is the length of the resulting string (which is equal to the number of strings in the input list).
"""
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res=""
        for x in range(len(nums)):
            if nums[x][x]=='0':
                res+='1'
            else:
                res+='0'
        return res