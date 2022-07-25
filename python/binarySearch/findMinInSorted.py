"""
Given the sorted rotated array nums of unique elements, 
return the minimum element of this array.
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[0] < nums[right]:
            return nums[0]
        while left < right:
            if nums[left] < nums[right]:
                right = (right // 2)
            else:
            # if nums[left] > nums[right]:
                mid = (right +  left) // 2
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                else:
                    if nums[mid + 1] < nums[mid]:
                        return nums[mid + 1]
                    else:
                        if nums[mid] > nums[right]:
                            left = mid
                        else:
                            right = mid
        return nums[left]


nums = [1,2,3,4]
nums2 = [5,6,7,1,2,3,4]
nums3 = [8,1,2,3,4,5,6,7]
nums4 = [3,1,2]
nums5 = [3,4,5,1,2]
nums6 = [2,3,4,5,1]
print(Solution().findMin(nums))
print(Solution().findMin(nums2))
print(Solution().findMin(nums3))
print(Solution().findMin(nums4))
print(Solution().findMin(nums5))
print(Solution().findMin(nums6))