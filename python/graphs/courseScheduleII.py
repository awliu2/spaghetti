from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = {c:[] for c in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        visitedSet, cycleSet = set(), set()
        rv = []

        def dfs(crs):
            if crs in cycleSet:
                return False
            if crs in visitedSet:
                return True

            cycleSet.add(crs)
            for prereq in prereqMap[crs]:
                if not dfs(prereq):
                    return False
            
            cycleSet.remove(crs)
            visitedSet.add(crs)
            rv.append(crs)
            return True

        for crs in range(numCourses):
            if crs not in visitedSet:
                if not dfs(crs):
                    return []
        return rv
