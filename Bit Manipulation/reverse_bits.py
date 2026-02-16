"""
Problem: Reverse Bits
Link: https://leetcode.com/problems/reverse-bits/submissions/1921105421/
Difficulty: Easy
Topic: Bit Manipulation
Date: 16-02-2026

Approach:
To reverse the bits of a given 32-bit unsigned integer, we can follow these steps:
1. Initialize a variable `ans` to store the reversed bits.
2. Iterate through each of the 32 bits of the input integer `n`.
3. In each iteration, left shift `ans` by 1 to make room for the next bit, and then use a bitwise OR operation to add the least significant bit of `n` to `ans`.
4. Right shift `n` by 1 to process the next bit in the next iteration.

Time Complexity: O(1) since we are always processing a fixed number of bits (32).
Space Complexity: O(1) since we are using a constant amount of space to store the result.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        
        return ans