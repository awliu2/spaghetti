from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def search(r, c):

            if (r,c in visited): 
                return 0
            visited.add((r,c))


            if (r < 0 or r >= ROW or 
                c < 0 or c >= COL or 
                grid[r][c] == 0):
                return 1

            if grid[r][c] == 1:
                return (search(r + 1, c) +
                        search(r - 1, c) +
                        search(r, c + 1) +
                        search(r, c - 1))



        if not grid:
            return 0
        
        rv = 0
        visited = set()
        ROW, COL =  len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in visited:
                    rv += search(r,c)
        return rv


        

