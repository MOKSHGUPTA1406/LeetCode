"""
Problem: Reverse Bits
Link: https://leetcode.com/problems/reverse-bits/submissions/1921103416/
Difficulty: Easy
Topic: Bit Manipulation
Date: 16-02-2026

Approach:
To reverse the bits of a given 32-bit unsigned integer, we can follow these steps:
1. Convert the integer `n` to its binary representation as a string.
2. Pad the binary string with leading zeros to ensure it is 32 bits long.
3. Reverse the binary string.
4. Convert the reversed binary string back to an integer.

Time Complexity: O(1) since we are always processing a fixed number of bits (32).
Space Complexity: O(1) since we are using a constant amount of space to store the result.
"""

class Solution:
    def binary(self, n:int)-> str:
        ans=0
        x=1
        y=0
        while(x<=n):
            x*=2
        x//=2
        while(x>0):
            lastDigit=n//x
            n-=lastDigit*x
            x//=2
            ans=ans*10+lastDigit
        return str(ans)
    def reverseBits(self, n: int) -> int:
        strn=self.binary(n)
        strn=(32-len(strn))*'0'+strn
        strn=strn[::-1]
        ans=0
        for x in range(len(strn)):
            ans+=(2**(31-x))*int(strn[x])
        return ans