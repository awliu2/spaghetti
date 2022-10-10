from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        ROW, COL = len(heights), len(heights[0])

        drains_to_pacific = set()
        drains_to_atlantic = set()

        pacific_coast = [[0,c] for c in range(COL)] + [[r, 0] for r in range(ROW)]
        atlantic_coast = ([[ROW - 1, c] for c in range(COL)] + 
                          [[r, COL - 1] for r in range(ROW)])

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, h_prev, ocean_set):
            if (r < 0 or r >= ROW or
                c < 0 or c >= COL or 
                heights[r][c] < h_prev or 
                (r,c) in ocean_set):
                return

            ocean_set.add((r,c))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], ocean_set)
            
        for r, c in pacific_coast:
            dfs(r, c, heights[r][c], drains_to_pacific)
        # print(drains_to_pacific)

        for r, c in atlantic_coast:
            dfs(r,c, heights[r][c], drains_to_atlantic)
        
        both_oceans = drains_to_pacific.intersection(drains_to_atlantic)
        # print(both_oceans)

        return [list(coord) for coord in list(both_oceans)]
heights = [[1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]]

print(Solution().pacificAtlantic(heights))
            
