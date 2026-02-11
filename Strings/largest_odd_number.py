"""
Problem: Largest Odd Number in String
Link: https://leetcode.com/problems/largest-odd-number-in-string/submissions/1914778144/
Difficulty: Easy
Topic: Math, String
Date: 10-02-2026

Approach:
We can iterate through the string from the end to the beginning and check if each character is an odd digit (1, 3, 5, 7, 9). If we find an odd digit, we can return the substring from the beginning of the string to that index (inclusive) as the largest odd number. If we finish iterating through the string without finding any odd digit, we can return an empty string.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for x in range(len(num)-1,-1,-1):
            if int(num[x])%2==1:
                return num[:x+1]
        return ""
                
            