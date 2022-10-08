from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rv = []
        i = 0
        
        # append all non-overlapping intervals
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            rv.append(intervals[i])
            i += 1

        # while interval ends before new one to insert
        # move on to next interval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        rv.append(newInterval)

        while i < len(intervals):
            rv.append(intervals[i])
            i += 1
        return rv


            

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
intervals2 = [[1,3],[6,9]]
print(Solution().insert(intervals, [4,8]))
print(Solution().insert(intervals2, [2,5]))