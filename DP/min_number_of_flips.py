"""
Problem: Minimum Number of Flips to Make the Binary String Alternating
Link: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/submissions/1941033879/
Difficulty: Medium
Topic: Dynamic Programming
Date: 27-02-2026

Approach:
1. We can use a dynamic programming approach to solve this problem. We will maintain two counts, `op[0]` and `op[1]`, which represent the number of flips needed to make the string alternating starting with '0' and '1' respectively.
2. We will iterate through the string and update these counts based on the current character and its position.
3. After processing the string, we will iterate through it again to calculate the minimum flips needed to make the string alternating by considering the flips needed for both starting with '0' and '1'.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(1), as we are using a constant amount of extra space for the counts.
"""


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        res = n
        op = [0, 0]

        for i in range(n):
            op[(ord(s[i]) ^ i) & 1] += 1

        for i in range(n):
            c = ord(s[i])
            op[(c ^ i) & 1] -= 1
            op[(c ^ (n + i)) & 1] += 1
            res = min(res, min(op))

        return res
