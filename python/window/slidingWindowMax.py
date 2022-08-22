from collections import deque
from typing import List

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        currMax = max(nums[0:k])
        rv = [currMax]
        l = 0
        for i in range(k, len(nums)):
            # print(i)
            # print(l)
            if nums[l] == currMax:
                currMax = max(nums[l + 1: i + 1])
            else:
                currMax = max(currMax, nums[i])
            l += 1
            rv.append(currMax)
        return rv

    def dequeSoln(self, nums: List[int], k: int) -> List[int]:
        rv = []
        indexQ = deque()
        l = 0
        for r, n in enumerate(nums):
            while indexQ and n > nums[indexQ[-1]]:
                # remove tail of queue if it is smaller than n
                indexQ.pop()
            
            indexQ.append(r)

            if l > indexQ[0]:
                # if current greatest value is out of bounds, remove it from queue
                indexQ.popleft()
                
            
            if r + 1 >= k:
                # slide the window over once we go thru the first k elements
                # also append currMax to rv
                l += 1
                rv.append(nums[indexQ[0]])
        return rv
            



            
            



nums1 , k1 = [1,3,-1,-3,5,3,6,7] , 3
nums2, k2 = [1, -1], 1
nums3, k3 = [1], 1
nums4, k4 = [1,3,1,2,0,5], 3
nums5, k5 = [5,3,4], 1

print(Solution().dequeSoln(nums1, k1))
print(Solution().dequeSoln(nums2, k2)) # expect [1, -1]
print(Solution().dequeSoln(nums3, k3))
print(Solution().dequeSoln(nums4, k4))
print(Solution().dequeSoln(nums5, k5))
            
