from typing import List
from collections import deque
class Solution:
    def soln2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= ROW or 
                c < 0 or c >= COL or
                grid[r][c] == 0 or
                (r,c) in visited):
                return 0
            visited.add((r,c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        
        visited = set()
        rv = 0
        for r in range(ROW):
            for c in range(COL):
                rv = max(rv, dfs(r,c))
        return rv



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        rv = 0
        visited = set()


        def getSize(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            size = 1

            while q:
                row, col = q.popleft()
                directions = [[1,0] , [-1,0] , [0,1] , [0,-1]]
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if ((newRow) in range(rows) and 
                        (newCol) in range(cols) and
                        grid[newRow][newCol] == 1 and 
                        (newRow, newCol) not in visited):

                        visited.add((newRow, newCol))
                        q.append((newRow, newCol))
                        size += 1

            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    rv = max(rv, getSize(r,c))
        
        return rv