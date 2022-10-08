from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        rv = 1
        memo = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[j] + 1, memo[i])
            rv = max(memo[i], rv)
        return rv

nums = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]

print(Solution().lengthOfLIS(nums2))
            



