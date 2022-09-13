class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        
        for i in range(len(intervals)):
            if i > 0:
                if intervals[i][0] < intervals[i-1][1]:
                    return False
        return True