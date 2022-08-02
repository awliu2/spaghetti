from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ### list comprehension and zip transposes the matrix
        ### we want to reverse each row of M transpose
        for i, row in enumerate([list(x) for x in zip(*matrix)]):
            matrix[i] = reversed(row)