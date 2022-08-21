from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
    
    def quickSelectSoln(self, nums: List[int], k: int) -> int:
        index = len(nums) - k

        def quickSelect(l,r):
            p, pivot = l, nums[r]
            for i in range(l , r):
                if nums[i] <= pivot:
                    nums[p] , nums[i] = nums[i] , nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > index:   return quickSelect(l, p - 1)
            elif p < k:     return quickSelect(p + 1, r)
            else:           return nums[p]
        
        quickSelect(0, len(nums))
