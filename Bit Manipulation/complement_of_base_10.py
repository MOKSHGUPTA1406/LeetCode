"""
Problem: Complement of Base 10 Integer
Link: https://leetcode.com/problems/complement-of-base-10-integer/submissions/1945340660/
Difficulty: Easy
Topic: Bit Manipulation
Date: 11-03-2026

Approach:
1. Convert the given integer `n` to its binary representation using the `bin()` function and remove the '0b' prefix.
2. Initialize an empty string `res` to store the complement of the binary representation.
3. Iterate through each character `x` in the binary string:
   - If `x` is '1', append '0' to `res`.
   - If `x` is '0', append '1' to `res`.
4. Finally, convert the resulting binary string `res` back to an integer using `int(res, 2)` and return it.

Time Complexity: O(k), where k is the number of bits in the binary representation of `n`.
Space Complexity: O(k), where k is the number of bits in the binary representation of `n` (for storing the complement string).
"""

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res=""
        n=bin(n)[2:]
        print(n)
        for x in str(n):
            if x=='1':
                res+='0'
            else:
                res+='1'
        return int(res,2)