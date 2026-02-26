"""
Problem: Number of suggest steps to reduce a number in binary representation to one
Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/submissions/1932135962/
Difficulty: Medium
Topic: Bit Manipulation
Date: 27-02-2026

Approach: To reduce a binary number to one, we can follow these steps:
1. If the last bit of the binary number is 0, we can simply remove it
2. If the last bit is 1 and there are more than one bits, we need to add 1 to the number, which will cause a carry that may affect multiple bits. We can find the rightmost 0 bit and flip it to 1, and flip all bits to the right of it to 0.
3. If the binary number is already 1, we are done. We can repeat these steps until we reduce the number to one, counting the number of steps taken.

Time Complexity: O(n) where n is the length of the binary string, since in the worst case we may need to process each bit of the string.
Space Complexity: O(1) since we are using a constant amount of space to store the count and intermediate variables.
"""


class Solution:
    def numSteps(self, s: str) -> int:
        count=0
        while(len(s)>1):
            idx=len(s)-1
            if s[-1]=='0':
                s=s[:len(s)-1]
                count+=1
                continue
            elif s.count('0')>0:
                while(s[idx]!='0'):
                    idx-=1
                s=s[:idx]+'1'+'0'*(len(s)-idx-1)
                count+=1
                continue
            s='1'+'0'*len(s)
            count+=1
        return count
            
            