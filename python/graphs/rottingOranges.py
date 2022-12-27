from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        n_rows, n_cols = len(grid), len(grid[0])
        fresh_oranges = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh_oranges += 1
        
        q.append((-1, -1))
        rv = 0
        print(q)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            orange = q.popleft()
            r = orange[0]
            c = orange[1]
            # if we find a divider between search layers, append to rv
            if orange == (-1, -1):
                    rv += 1
                    # add another "divider" into the queue if not empty
                    # avoids infinite loop
                    if q:
                        q.append((-1,-1))
            else:
                for d_r, d_c in directions:
                    # if out of bounds, do nothing
                    if (0 <= r + d_r < n_rows) and (0 <= c + d_c < n_cols):
                        # if fresh, change to rotting, and add to queue
                        if grid[r + d_r][c + d_c] == 1:
                            grid[r + d_r][c + d_c] = 2
                            fresh_oranges -= 1
                            q.append((r + d_r, c + d_c))
                            
        return rv
                    
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))

