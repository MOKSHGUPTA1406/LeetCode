"""
Problem: Candy
Link: https://leetcode.com/problems/candy/submissions/1946348327/
Difficulty: Hard
Topic: Greedyy
Date: 12-03-2026

Approach: We can use a greedy approach to solve this problem. We will iterate through the ratings and assign candies to each child based on their ratings. We will ensure that each child has at least one candy and that children with higher ratings than their neighbors receive more candies. We will first iterate from left to right and assign candies based on the ratings compared to the previous child. Then, we will iterate from right to left and adjust the candies based on the ratings compared to the next child. Finally, we will sum up the total number of candies assigned.


Time Complexity: O(n) where n is the length of the input array, since we iterate through the array twice.
Space Complexity: O(n) where n is the length of the input array, since we maintain an array of size n to store the number of candies for each child.
"""

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans=[1]*len(ratings)
        for x in range(len(ratings)-1):
            if ratings[x]<ratings[x+1] and ans[x]>=ans[x+1]:
                ans[x+1]=ans[x]+1
        for x in range(len(ratings)-1,0,-1):
            if ratings[x-1]>ratings[x] and ans[x-1]<=ans[x]:
                ans[x-1]=ans[x]+1
        return sum(ans)