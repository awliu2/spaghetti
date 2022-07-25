from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = right // 2
        
        while left < right:
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid
                
            if nums[mid] > target:
                right = mid
                
            if (left + right) // 2 == mid:
                return -1
            else:
                mid = (left + right) // 2
            
        return -1

nums = [-1,0,3,5,9,12]
nums2 = [1,3]
print(Solution().search(nums, 2))
print(Solution().search(nums2, 3))