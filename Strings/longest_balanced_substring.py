"""
Problem: Longest Balanced Substring I
Link: https://leetcode.com/problems/longest-balanced-substring-i/submissions/1917346244/
Difficulty: Medium
Topic: String, hashtable
Date: 12-02-2026

Approach:
We can use a nested loop to iterate through all possible substrings of the input string. For each substring, we can maintain a frequency count of each character using a list of size 26 (for lowercase letters). We also keep track of the number of distinct characters and the maximum frequency of any character in the current substring. If the length of the substring is equal to the product of the number of distinct characters and the maximum frequency, then it is a balanced substring. We can update our maximum length accordingly.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestBalanced(self, s: str) -> int:
        maxlen=0
        for x in range(len(s)):
            l=[0 for _ in range(26)]
            dis=0
            maxf=0
            for y in range(x,len(s)):
                i=ord(s[y])-ord('a')
                if l[i]==0: 
                    dis+=1
                l[i]+=1
                if l[i]>maxf: 
                    maxf=l[i]
                if (y-x+1)==dis*maxf:
                    maxlen=max(maxlen,y-x+1)
        return maxlen