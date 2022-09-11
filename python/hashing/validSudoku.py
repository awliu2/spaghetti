from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for i in range(9)]
        colSet = [set() for i in range(9)]
        squareSet = [set() for i in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                if val in rowSet[r]:
                    return False
                rowSet[r].add(val)

                if val in colSet[c]:
                    return False
                colSet[c].add(val)

                if val in squareSet[(r//3) * 3 + (c //3)]:
                    return False
                squareSet[(r // 3) * 3 + (c // 3)].add(val)
        # print(rowSet)
        # print(colSet)
        # print(squareSet)
        
        return True


board = [
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]


print(Solution().isValidSudoku(board))