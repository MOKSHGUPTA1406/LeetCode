"""
Problem: Fancy Sequence
Link: https://leetcode.com/problems/fancy-sequence/submissions/1949390438/
Difficulty: Hard
Topic: Math
Date: 15-03-2026

Approach: We can maintain two variables `a` and `b` to represent the linear transformation applied to the sequence. When we append a value, we store it in a way that allows us to retrieve the original value before any transformations. When we add or multiply all values, we update `a` and `b` accordingly. To get the value at a specific index, we apply the inverse of the transformations to retrieve the original value.

Time Complexity: - append: O(1)
                 - addAll: O(1)
                 - multAll: O(1)
                 - getIndex: O(1)
Space Complexity: O(n) for storing the values in the sequence.
"""

class Fancy:

    def __init__(self):
        self.mod = 10**9+7  
        self.val = []  
        self.a = 1  
        self.b = 0 
    def append(self, val: int) -> None:
        x=(val-self.b+self.mod)%self.mod
        self.val.append(x*pow(self.a,self.mod-2,self.mod)%self.mod)

    def addAll(self, inc: int) -> None:
        self.b=(self.b+inc)%self.mod

    def multAll(self, m: int) -> None:
        self.a=(self.a*m)%self.mod
        self.b=(self.b*m)%self.mod

    def getIndex(self, idx: int) -> int:
        if idx>=len(self.val):
            return -1
        return (self.a*self.val[idx]+self.b)%self.mod