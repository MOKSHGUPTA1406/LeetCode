"""
Problem: Reverse Words in a String
Link: https://leetcode.com/problems/reverse-words-in-a-string/submissions/1914763476/
Difficulty: Medium
Topic: String
Date: 10-02-2026

Approach:
We can split the input string into a list of words using the split() method, which will automatically handle multiple spaces. Then, we can reverse the list of words and join them back into a single string with spaces in between.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        text=s.split()
        ans=""
        for x in range(len(text)-1):
            ans+=text[len(text)-x-1]+" "
        return ans+text[0]
            