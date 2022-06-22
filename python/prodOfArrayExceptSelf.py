from typing import List
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rv = []
        for i in range(len(nums)):
            left = reduce(lambda x, y: x * y, nums[:i], 1)
            right = reduce(lambda x, y: x * y, nums[i+1:], 1)
            rv.append(left * right)
        return rv

    def v2(self, nums: List[int]) -> List[int]:
        rv = [1 for _ in nums]
        left = right = 1
        for i in range(len(nums)):
            rv[i] *= left
            rv[~i] *= right

            left *= nums[i]
            right *= nums[~i]
        return rv
print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([0,1,2,3,4]))

print(Solution().v2([1,2,3,4]))
print(Solution().v2([0,1,2,3,4]))
