from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        currEnd = intervals[0][1]
        count = 0
        for i in intervals[1:]:
            if i[0] < currEnd:
                count += 1
                currEnd = min(currEnd, i[1])
            else:
                currEnd = i[1]

            return count





intervals = [[1,2],[2,3],[3,4],[1,3]]
print(Solution().eraseOverlapIntervals(intervals))