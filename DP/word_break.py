"""
Problem: Word Break
Link: https://leetcode.com/problems/word-break/submissions/1932212706/
Difficulty: Medium
Topic: Dynamic Programming
Date: 27-02-2026

Approach:
To solve the word break problem, we can use dynamic programming. The idea is to check if a string can be broken down into words from a given dictionary. We use a boolean array dp where dp[i] represents whether the substring s[0:i] can be segmented into words from the dictionary. For each position i, we check all words in the dictionary to see if any of them matches the substring ending at position i and if dp[i - len(word)] is True.

Time Complexity: O(n * m * k) where n is the length of the string, m is the number of words in the dictionary, and k is the average length of each word.
Space Complexity: O(n) since we are storing a boolean value for each position in the string.
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True
        for x in range(1,len(s)+1):
            for w in wordDict:
                start = x - len(w)
                if start >= 0 and dp[start] and s[start:x] == w:
                    dp[x] = True
                    break
        return dp[-1]