"""
Problem: Remove Outermost Parentheses
Link: https://leetcode.com/problems/remove-outermost-parentheses/
Difficulty: Easy
Topic: String, Stack
Date: 10-02-2026

Approach:
We can use a stack to keep track of the depth of the parentheses. We iterate through each character in the string, and for each opening parenthesis '(', we check if the stack is not empty before adding it to the answer string. We then push it onto the stack. For each closing parenthesis ')', we pop from the stack and check if the stack is not empty before adding it to the answer string. This way, we only add characters that are not part of the outermost parentheses.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth=0
        ans=""
        for ch in s:
            if ch=='(':
                if depth>0:
                    ans+=ch
                depth+=1
            else:
                depth-=1
                if depth>0:
                    ans+=ch        
        return ans
            