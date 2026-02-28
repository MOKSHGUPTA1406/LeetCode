"""
Problem: Interleaving String
Link: https://leetcode.com/problems/interleaving-string/submissions/1933994816/
Difficulty: Medium
Topic: Dynamic Programming
Date: 29-02-2026

Approach: We can use dynamic programming to solve this problem. We create a 2D boolean array `dp` where `dp[i][j]` indicates whether the first `i` characters of `s1` and the first `j` characters of `s2` can interleave to form the first `i + j` characters of `s3`. We initialize the base cases for when one of the strings is empty. Then, we fill the `dp` table based on whether the current characters of `s1` and `s2` match the corresponding character in `s3` and whether the previous states in the `dp` table are true.

Time Complexity: O(m * n) where m and n are the lengths of `s1` and `s2` respectively, since we iterate through each element once.
Space Complexity: O(m * n) where m and n are the lengths of `s1` and `s2` respectively, since we maintain a 2D boolean array `dp`.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[m][n]