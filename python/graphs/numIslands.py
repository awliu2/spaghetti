from typing import List
from collections import deque
class Solution:
    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        rv = 0
        visited = set()


        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0] , [-1,0] , [0,1] , [0,-1]]
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if ((newRow) in range(rows) and 
                        (newCol) in range(cols) and
                        grid[newRow][newCol] == '1' and 
                        (newRow, newCol) not in visited):

                        visited.add((newRow, newCol))
                        q.append((newRow, newCol))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r,c)
                    rv += 1
        
        return rv

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
    