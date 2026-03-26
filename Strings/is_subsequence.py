"""
Problem: Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/submissions/1951512484/
Difficulty: Easy
Topic: String, Two Pointers
Date: 17-03-2026

Approach:
We can use the two-pointer technique to solve this problem efficiently. We will initialize two pointers, one for the subsequence string `s` and the other for the main string `t`. We will iterate through both strings, and if we find a character in `t` that matches the current character in `s`, we will move the pointer for `s` forward. If we successfully match all characters in `s`, then it is a subsequence of `t`.

Time Complexity: O(n), where n is the length of string `t`.
Space Complexity: O(1), since we are using only a constant amount of extra space for the pointers and variables.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0: return True
        if len(s)>len(t): return False
        dp=[False for _ in range(len(s))]
        left=0
        right=0
        while left<len(s) and right<len(t):
            if s[left] not in t:
                return False
            if s[left]==t[right]:
                dp[left]=True
                left+=1
            right+=1
        return dp[-1]