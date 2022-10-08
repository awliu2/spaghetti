from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_curr = nums[0]
        min_curr = nums[0]
        rv = nums[0]
        for n in nums[1:]:
                        
            temp_max = max(n, max_curr * n, min_curr * n)
            min_curr = min(n, min_curr * n, max_curr * n)
            max_curr = temp_max
            
            rv = max(rv, max_curr)
        return rv
