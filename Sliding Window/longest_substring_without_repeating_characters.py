"""
Problem: Remove Outermost ParenthesesLongest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1915970993/
Difficulty: Medium
Topic: String, Sliding Window
Date: 11-02-2026

Approach:
Use a sliding window technique with two pointers (start and end) to maintain a window of unique characters. Expand the window by moving the end pointer and shrink it when a duplicate character is encountered. Keep track of the maximum length of such windows.

Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is the size of the character set and n is the length of the string.
"""

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1: return len(s)
        ans=0
        st=0
        end=1
        i=1
        while(i<len(s)):
            if s[i] not in s[st:end]:
                i+=1
                end+=1
            else:
                st+=1
                end=st
                i=end
            ans=max(ans,len(s[st:end]))
        return ans
            