"""
Problem: Gas Station
Link: https://leetcode.com/problems/gas-station/submissions/1951241141/
Difficulty: Medium
Topic: Greedy
Date: 17-03-2026

Approach: 1. First, we check if the total amount of gas is less than the total cost. If it is, then it's impossible to complete the circuit, and we return -1.
2. We initialize two variables: `start` to keep track of the starting gas station index, and `curr` to keep track of the current amount of gas in the tank.
3. We iterate through each gas station, calculating the net gas (gas[i] - cost[i]) at each station and adding it to `curr`.
4. If at any point `curr` becomes negative, it means we cannot reach the next station from the current starting point. Therefore, we reset `curr` to 0 and update `start` to the next station index (x + 1).
5. After the loop, we return the `start` index, which will be the starting gas station from which we can complete the circuit.

Time Complexity: O(n), where n is the number of gas stations. We traverse the list of gas stations once.
Space Complexity: O(1), as we are using only a constant amount of extra space for the variables.
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        start=0
        curr=0
        for x in range(len(gas)):
            curr+=gas[x]-cost[x]
            if curr<0:
               curr=0
               start=x+1 
        return start


