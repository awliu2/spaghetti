from os import lseek


from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # order is prev2 -> prev1 -> next
        prev2, prev1 = 0, 0
        # rv = 0
        for i, n in enumerate(cost):
            print(f"i: {i}")
            print(f"prev2, prev1, n: {prev2}, {prev1}, {n}")
            if i == len(cost) - 1:
                return min(prev1, prev2 + n)
            prev2, prev1 = prev1, min(prev2 + n, prev1 + n)
        return prev1


cost = [10,15,20] # answer is 6
cost2 = [1,100,1,1,1,100,1,1,100,1] # answer is 6

print(Solution().minCostClimbingStairs(cost))
print(Solution().minCostClimbingStairs(cost2))
