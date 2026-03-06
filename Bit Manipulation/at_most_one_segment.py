"""
Problem: Check if Binary String Has at Most One Segment of Ones
Link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/submissions/1939671280/
Difficulty: Easy
Topic: Bit Manipulation
Date: 06-03-2026

Approach:
To check if a binary string has at most one segment of ones, we can split the string by '0' and count the number of non-empty segments. If there is more than one such segment, it means there are multiple segments of ones, which violates the condition.

Time Complexity: O(n) where n is the length of the string.
Space Complexity: O(n) for storing the split segments.
"""

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s)==1 and s[0]=='1': return True
        if s.count('1')==0 or s.count('1')==len(s): return True
        l=s.split('0')
        while '' in l: l.remove('')
        if len(l)>1: return False
        return True