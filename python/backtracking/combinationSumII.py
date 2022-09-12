from typing import List
"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if len(candidates) == 1:
            return [candidates] if candidates[1] == target else []
        
        candidates.sort()
        print(candidates)
        rv = []

        def backtrack(remain, combo, start):
            if remain == 0:
                rv.append(list(combo))
                return
            
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                
                combo.append(candidates[i])
                backtrack(remain - candidates[i], combo, i + 1)
                combo.pop()

        backtrack(target, [], 0)
        return rv
        


candidates , target = [10,1,2,7,6,1,5] , 8
print(Solution().combinationSum2(candidates, target))