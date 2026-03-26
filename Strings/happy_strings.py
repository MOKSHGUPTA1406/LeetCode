
"""
Problem: The k-th Lexicographical String of All Happy Strings of Length n
Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/submissions/1948290150/
Difficulty: Medium
Topic: String
Date: 14-03-2026

Approach:
1. Calculate the total number of happy strings of length n, which is 3 * (2^(n-1)). If k is greater than this total, return an empty string.
2. Decrease k by 1 to convert it to a zero-based index.
3. Initialize an empty list to store the characters of the resulting happy string and a variable to keep track of the last character added to ensure no two adjacent characters are the same.
4. Iterate through each position from 0 to n-1:
    a. Calculate the number of happy strings that can be formed with the remaining positions (branch) as 2^(n - pos - 1).
    b. Determine the choices for the current position, which are the characters 'a', 'b', and 'c' excluding the last character added.
    c. Calculate the index of the character to add based on k and branch, and append it to the result list.
    d. Update the last character and reduce k by taking the modulus with branch to prepare for the next iteration.


Time Complexity: O(n) - We iterate through each position of the string once.
Space Complexity: O(n) - The space used to store the resulting happy string is proportional to the length of the string n.
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""

        k -= 1
        result = []
        last = ""

        for pos in range(n):

            branch = 2 ** (n - pos - 1)
            choices = [c for c in "abc" if c != last]

            idx = k // branch
            result.append(choices[idx])

            last = choices[idx]
            k %= branch

        return "".join(result)

            
            
