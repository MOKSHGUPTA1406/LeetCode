"""
Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/submissions/1918369180/
Difficulty: Medium
Topic: Dynamic Programming
Date: 28-02-2026

Approach: We can use dynamic programming to solve this problem. We will create a 2D boolean array `dp` where `dp[i][j]` will be true if the substring from index `i` to index `j` is a palindrome. We will fill this table in a bottom-up manner. We will iterate through all possible substring lengths and check if the substring is a palindrome by comparing the characters at the start and end of the substring and checking if the inner substring is also a palindrome.


Time Complexity: O(n^2) where n is the length of the input string, since we iterate through all possible substrings and check if each is a palindrome.
Space Complexity: O(n^2) where n is the length of the input string, since we maintain a 2D boolean array `dp` of size n x n.
"""

from typing import List

class Solution:
    def palindrome(self, s:str)->bool:
        if s==s[::-1]:
            return True
        return False
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1: return s
        if len(s)==2 and s[0]!=s[1]: return s[0]
        maxlen=1
        ans=s[0]
        for left in range(len(s)-1):
            right=len(s)-1
            while left<right:
                if s[left]!=s[right]: 
                    right-=1
                    continue
                if self.palindrome(s[left:right+1]):
                    if len(s[left:right+1])>maxlen:
                        maxlen=len(s[left:right+1])
                        ans=s[left:right+1]
                right-=1
        return ans