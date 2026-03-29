"""
Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/submissions/1918369180/
Difficulty: Medium
Topic: String, two pointers
Date: 13-02-2026

Approach:
We can use a nested loop to iterate through all possible substrings of the input string. For each substring, we can check if it is a palindrome by comparing it to its reverse. If it is a palindrome and its length is greater than the maximum length found so far, we can update our answer accordingly.

Time Complexity: O(n^3) - O(n^2) for generating substrings and O(n) for checking if each substring is a palindrome.
Space Complexity: O(1) - We are using a constant amount of extra space to store the maximum length and the answer string.
"""

class Solution:
    def palindrome(self, s:str)->bool:
        if s==s[::-1]:
            return True
        return False
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1: return s
        if len(s)==2 and s[0]!=s[1]: return s[0]
        maxlen=1
        ans=s[0]
        for left in range(len(s)-1):
            right=len(s)-1
            while left<right:
                if s[left]!=s[right]: 
                    right-=1
                    continue
                if self.palindrome(s[left:right+1]):
                    if len(s[left:right+1])>maxlen:
                        maxlen=len(s[left:right+1])
                        ans=s[left:right+1]
                right-=1
        return ans

            
            
