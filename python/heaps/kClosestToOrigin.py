from typing import List

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a minheap, but actually keep furthest point at the top
        
        distances = []
        rv = []
        for x, y in points:
            dist = -(x*x + y*y)
            
            if len(distances) == k:
                # only want the k closest (basically we want the bottom of heap)
                heapq.heappushpop(distances, (dist, x, y))
            else:
                heapq.heappush(distances, (dist, x,y))
        
        print(distances)
        rv = [(x, y) for (dist, x, y) in distances]
        
        return rv

points = [[3,3],[5,-1],[-2,4]]

print(Solution().kClosest(points, 2))