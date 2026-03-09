"""
Problem: Find All Possible Stable Binary Arrays I
Link: https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/submissions/1943205240/
Difficulty: Medium
Topic: Dynamic Programming
Date: 09-03-2026

Approach:
The approach is to use dynamic programming to count the number of stable binary arrays that can be formed with a given number of zeros and ones, while respecting the limit on consecutive bits. We maintain two DP tables: `dp0[i][j]` for arrays ending with '0' and `dp1[i][j]` for arrays ending with '1'. We fill these tables based on the previous states, ensuring that we do not exceed the limit of consecutive bits.

Time Complexity: O(zero * one * limit), where zero and one are the number of zeros and ones respectively, and limit is the maximum allowed consecutive bits.
Space Complexity: O(zero * one), where zero and one are the number of zeros and ones respectively, due to the DP tables used to store intermediate results.
"""
from typing import List

class Solution:

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]

        for i in range(1, min(zero, limit)+1):
            dp0[i][0] = 1

        for j in range(1, min(one, limit)+1):
            dp1[0][j] = 1

        for i in range(zero+1):
            for j in range(one+1):
                if i == 0 and j == 0:
                    continue

                if i > 0 and j > 0:
                    ways0 = 0
                    for k in range(1, limit+1):
                        if i-k < 0:
                            break
                        ways0 = (ways0 + dp1[i-k][j]) % MOD
                    dp0[i][j] = ways0

                    ways1 = 0
                    for k in range(1, limit+1):
                        if j-k < 0:
                            break
                        ways1 = (ways1 + dp0[i][j-k]) % MOD
                    dp1[i][j] = ways1

        return (dp0[zero][one] + dp1[zero][one]) % MOD