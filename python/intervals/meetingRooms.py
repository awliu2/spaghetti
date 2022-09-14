from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start, end = [], []

        rv = 0

        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        
        start.sort()
        end.sort()

        ep = 0
        
        for sp in range(1, len(start)):
            if start[sp] < end[ep]:
                return False
            else:
                ep += 1
        return True

    def soln2(intervals):
        intervals.sort()
        
        for i in range(len(intervals)):
            if i > 0:
                if intervals[i][0] < intervals[i-1][1]:
                    return False
        return True