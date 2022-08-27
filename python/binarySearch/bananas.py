from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def speed(piles, rate):
            rv = 0
            for p in piles:
                rv += ceil(p / rate)
            # print(rv)
            return rv
        
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            # print(f"mid{mid}")
            if speed(piles, mid) > h:
                lo = mid + 1
            else:
                hi = mid
        # print(lo,hi)
        return hi
            
        