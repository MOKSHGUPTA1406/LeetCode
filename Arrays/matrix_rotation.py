"""
Problem: Determine Whether Matrix Can Be Obtained By Rotation
Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/submissions/1955858384/
Difficulty: Easy
Topic: Arrays
Date: 22-03-2026

Approach: 1. We define a helper function `rotate` that rotates the matrix 90 degrees clockwise. This is done by first transposing the matrix and then reversing each row.
2. In the `findRotation` function, we check if the original matrix `mat` is equal to the target matrix. If it is, we return True.
3. If not, we rotate the matrix and check again. We repeat this process up to 4 times (since rotating 4 times will bring the matrix back to its original orientation).  

Time Complexity: O(n^2) for the rotation operation, and we perform it at most 4 times, so the overall time complexity is O(n^2).
Space Complexity: O(1) since we are modifying the matrix in place and not using any additional data structures.
"""

class Solution:
    def rotate(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(n):
            mat[i].reverse()

    def findRotation(self, mat, target):
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
        return False