from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            # print(maxSum)
        return maxSum
            



nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [-2, 1]
print(Solution().maxSubArray(nums1))
print(Solution().maxSubArray(nums2))
print(Solution().maxSubArray([-1, -2]))
