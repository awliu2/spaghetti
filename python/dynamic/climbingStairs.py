p = print
""" You are climbing a staircase. 
It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
 In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev1 = 2
        prev2 = 1  
        for i in range(3, n + 1):
            prev2 , prev1 = prev1, prev1 + prev2
            p(f"prev1: {prev1}")
            p(f"prev2: {prev2}")
        return prev1

p("n = 2, Expecting 2: "  + str(Solution().climbStairs(2)))
p("n = 3, Expecting 3: "  + str(Solution().climbStairs(3)))
p("n = 4, Expecting 5: "  + str(Solution().climbStairs(4)))



