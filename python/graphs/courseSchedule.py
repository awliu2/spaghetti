from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        checked = set()
        classMap = collections.defaultdict(list)

        def dfs(course):
            if course in checked:
                return False
            if course not in classMap or classMap[course] == []:
                return True
            
            checked.add(course)
            for prereqs in classMap[course]:
                if not dfs(prereqs):
                    return False
            
            checked.remove(course)
            classMap[course] = []
            return True


        for course, prereq in prerequisites:
            classMap[course].append(prereq)
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True





        # def dfs(course):
        #     if course in checked:
        #         # we already visited it, so this must be cyclic
        #         return False
        #     if course not in classMap:
        #         # course has no prerequisites
        #         return True
        #     checked.add(course)
        #     for prereq in classMap[course]:
        #         # check all of courses prereqs
        #         if not dfs(prereq):
        #             return False
            
        #     # remove course from checked after checking all dfs all of its prereqs
        #     checked.remove(course)
        #     classMap[course] = []
        #     return True
        
        # checked = set()
        # classMap = collections.defaultdict(list)

        # for course, req in prerequisites:
        #     classMap[course].append(req) 
            
        # for course in range(numCourses):
        #     if not dfs(course): 
        #         return False
        
        # return True

        
                


            
        
        

classList = [[0,1],[1,0]]

print(Solution().canFinish(2, classList))