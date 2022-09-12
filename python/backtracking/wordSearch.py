from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        checked = [[False for col in board[0]] for row in board]

        def backtrack(index, row, col):
            # if grid spot has alr been visited: return
            if checked[row][col] == True:
                return
            # if we are at last character:
            if board[row][col] != word[index]:
                return

            if index == len(word) - 1:
                # return true if last character matches grid else return
                if board[row][col] == word[index]: 
                    return True
                else:
                    return False
            
            
            
            checked[row][col] = True
            
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for dr, dc in directions:
                if 0 <= row + dr < len(board) and 0 <= col + dc < len(board[0]):
                    if backtrack(index + 1, row + dr, col + dc):
                        return True
            # if nothing found in any direction, we set checked to false in order to be able to come back to it
            checked[row][col] = False

            return False
            
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                print(row, col)
                if backtrack(0, row, col):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
board2 = ["a", "a"]
word2 = "aaa"
word = "ABCCED"
print(Solution().exist(board, word))

print(Solution().exist(board2, word2))

            

            
            