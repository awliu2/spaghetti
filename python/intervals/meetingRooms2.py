from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:   
        start, end = [], []
        rv = 0
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        
        start.sort()
        end.sort()
        ep = 0
        for sp in range(len(start)):
            if start[sp] < end[ep]:
                rv += 1
            else:
                ep += 1
        return rv

            
                







intervals = [[0,30],[5,10],[15,20]]
intervals2 = [[1,5],[8,9],[8,9]]
print(Solution().minMeetingRooms(intervals))
print(Solution().minMeetingRooms(intervals2))
