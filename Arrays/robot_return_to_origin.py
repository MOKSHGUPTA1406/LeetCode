"""
Problem: Robot Return to Origin
Link: https://leetcode.com/problems/robot-return-to-origin/submissions/1969679326/
Difficulty: Easy
Topic: Arrays
Date: 05-04-2026

Approach: We can keep track of the robot's position using two variables, x and y. We iterate through the moves string and update the position based on the direction of each move. After processing all moves, we check if the robot has returned to the origin (0, 0).

Time Complexity: O(n), where n is the length of the moves string, since we need to iterate through all the moves once.
Space Complexity: O(1), since we are using only a constant amount of extra space to store the position of the robot.
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for m in moves:
            if m=='U':
                y+=1
            elif m=='D':
                y-=1
            elif m=='R':
                x+=1
            elif m=='L':
                x-=1
        if x==0 and y==0: return True
        return False
        