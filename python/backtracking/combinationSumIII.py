from typing import List

"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.

Return a list of all possible valid combinations. 
The list must not contain the same combination twice, and the combinations may be returned in any order.
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        rv = []
        def backtrack(remain, combo, next):
            if remain == 0 and len(combo) == k:
                # we've summed to 9
                rv.append(list(combo))
                return
            elif remain < 0 or len(combo) == k:
                # do nothing
                return
            
            for i in range(next, 10):
                combo.append(i) 
                backtrack(remain - i, combo, next + i)

                combo.pop()

        backtrack(n, [], 1)

        return rv            

print(Solution().combinationSum3(3, 7))
