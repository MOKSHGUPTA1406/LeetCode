"""
Problem: Binary Watch
Link: https://leetcode.com/problems/binary-watch/submissions/1922501622/
Difficulty: Easy
Topic: Bit Manipulation
Date: 16-02-2026

Approach:
To generate all possible times on a binary watch given a number of LEDs that are on, we can use a bit manipulation technique to iterate through all combinations of LEDs. The binary watch has 10 LEDs, where the first 4 represent the hours (0-11) and the next 6 represent the minutes (0-59). We can use a bitmask to represent the state of the LEDs, and we can generate combinations of LEDs that are on by using a loop to iterate through possible values of the bitmask. For each combination, we can extract the hour and minute values and check if they are valid (hour < 12 and minute < 60). If they are valid, we can format the time as a string and add it to the result list.

Time Complexity: O(1) since we are generating a fixed number of combinations (2^10 = 1024).
Space Complexity: O(1) since we are using a constant amount of space to store the result list and intermediate variables.
"""

from typing import List

class Solution:
    def readBinaryWatch(self, k: int) -> List[str]:
        if k == 0:
            return ['0:00']
        mask = (1 << 6) - 1
        q = (1 << k) - 1
        limit = q << (10 - k)
        res = []
        while q <= limit:
            min = q & mask
            hour = q >> 6
            if hour < 12 and min < 60:
                res.append(f'{hour}:{min:0>2}')
            r = q & -q
            n = q + r 
            q = (((q ^ n) // r) >> 2) | n
        return res
