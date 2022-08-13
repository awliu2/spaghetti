from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob(i) = max(nums[i-2] + nums[i], nums[i-1])
        if len(nums) == 1:
            return nums[0]
        lead = 0
        tail = 0
        for i, n in enumerate(nums):
            print(f"rob {n}: nums[{i}] + nums[{i - 1}] = {tail + n}")
            print(f"don't rob {n}: nums[{i - 1}] = {lead}")
            lead, tail = max(tail + n, lead), lead
            print(f"current max: {lead}")
            print()
        return lead