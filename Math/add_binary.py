"""
Problem: Add Binary
Link: https://leetcode.com/problems/add-binary/submissions/1920278849/
Difficulty: Easy
Topic: String, Math
Date: 10-02-2026

Approach:
To solve the problem of adding two binary numbers represented as strings, we can follow these steps:
1. Convert the binary strings to decimal integers.
2. Add the two decimal integers together.
3. Convert the resulting sum back to a binary string.

Time Complexity: O(n) where n is the length of the longer binary string.
Space Complexity: O(n) for storing the resulting binary string.
"""

class Solution:
    def dec(self, n:int)-> int:
        ans=0
        i=0
        while (n>0):
            ans+=(2**i)*(n%10)
            n//=10
            i+=1
        return ans
    def binary(self, n:int)-> int:
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
        return ans
    def addBinary(self, a: str, b: str) -> str:
        return str(self.binary(self.dec(int(a))+self.dec(int(b))))
            