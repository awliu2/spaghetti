from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rv = 0
        height = len(grid)
        width = len(grid[0])
        
        checked = [[False for _ in range(width)] for _ in range(height)]
        
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1' and checked[i][j] == False:
                    rv += 1
                    self.checkLand(grid,checked,i,j,height,width)
        return rv

    def checkLand(self, grid: List[List[str]], checked: List[List[bool]], i: int, j: int, height: int, width: int):
        q = deque([(i,j)])
        while q:
            i, j = q.popleft()
            if 0 <= i < height and 0 <= j < width and grid[i][j] == '1' and checked[i][j] == False:
                checked[i][j] = True
                q.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
            


map = [['1','1'],['0','0'],['0','0']]


print(Solution().numIslands(map))
    