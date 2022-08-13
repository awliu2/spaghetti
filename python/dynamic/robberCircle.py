from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == [] or nums is None:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self.simple_rob(nums[1:]), self.simple_rob(nums[:-1]))
    
    def simple_rob(self, nums: List[int]) -> int:
        # order goes prev2 -> prev1 -> next
        if len(nums) == 1:
            return nums[0]

        prev2 = prev1 = 0


        for n in nums:
            prev2, prev1 = prev1, max(prev2 + n, prev1)
        return prev1

        