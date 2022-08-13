"""
There is an integer array nums sorted in ascending order
(with distinct values).

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums,
or -1 if it is not in nums.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max = len(nums) - 1
        i = 0
        visited = []
        while i not in visited:
            visited.append(i)

            if nums[i] > target:
                i = i - 1
                if i < 0:
                    i = max

            elif nums[i] < target:
                i = i + 1
                if i > max:
                    i = 0

            else:
                return i
        return -1

    
    
    def search2(self, nums: List[int], target: int) -> int:
        max_i = len(nums) - 1
        l = 0
        r = max_i
        while nums[l] > nums[r]:
            mid = l + r // 2
            if nums[mid] > nums[l]:
                l = mid
            if nums[mid] < nums[l]:
                r = mid
        pivot = r

        if nums[pivot] == target:
            return pivot

        if nums[0] > target:
            l2 = pivot
            r2 = max_i
        else:
            l2 = 0
            r2 = pivot
        
        while nums[l2] < nums[r2]:
            mid = l2 + r2 // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r2 = mid
            else:
                l2 = mid
        return -1

    