from typing import List

"""
Given an integer n, return an array ans of length 
n + 1 such that 
for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        rv = []
        for i in range(n + 1):
            rv.append(self.hammingWeight(i))
        return rv

    def hammingWeight(self, n: int) -> int:
        rv = 0
        while n:
            rv += 1
            n = n & (n - 1)
        return rv
    
    def dpCountBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        print(dp)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

            
            
print(Solution().countBits(64))
print(Solution().dpCountBits(64))