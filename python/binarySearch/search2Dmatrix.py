from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        indexM = 0
        num_col = len(matrix[0]) - 1
        num_row = len(matrix) - 1
        while matrix[indexM][num_col] < target:
            indexM += 1
            if indexM > num_row:
                return False

        print(indexM)

        left = 0
        right = num_col + 1
        
        if left == (right - 1):
            return matrix[indexM][left] == target
        
        mid = right // 2

        while left < right:
            if matrix[indexM][mid] == target:
                return True

            if matrix[indexM][mid] > target:
                right = mid

            if matrix[indexM][mid] < target:
                left = mid

            if (left + right) // 2 == mid:
                return False
            else:
                mid = (left + right) // 2
        return False


        


matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix2 = [[1]]
matrix3 = [[1,3]]
matrix4 = [[-10,-10],[-9,-9],[-8,-6],[-4,-2],[0,1],[3,3],[5,5],[6,8]]


print(Solution().searchMatrix(matrix1, 11))
print(Solution().searchMatrix(matrix2, 1))
print(Solution().searchMatrix(matrix3, 3))
print(Solution().searchMatrix(matrix4, 0))
