from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        rv = []
        for i in intervals:
            if not rv or rv[-1][1] < i[0]:
                rv.append(i)

            else:
                rv[-1][1] = max(rv[-1][1], i[1])
        
        return rv


interval1 = [[1,3],[2,6],[8,10],[15,18]]
interval2 = [[1,4],[2,3]]
        
print(Solution().merge(interval1))
print(Solution().merge(interval2))