"""
There is an integer array nums sorted in ascending order
(with distinct values).

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums,
or -1 if it is not in nums.



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

class Solution:
    def search(self, nums: List[int], targt: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2

            if target = nums[mid]:
                return mid

            elif target > nums[mid]:
                low = mid

            else:
                high = mid
"""