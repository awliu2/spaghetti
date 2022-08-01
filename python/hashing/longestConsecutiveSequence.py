"""
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.
Must run in O(n) time
"""
from calendar import c
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lnums = len(nums)
        if lnums == 0 or lnums == 1:
            return lnums
        nums.sort()
        print(nums)
        currStreak = maxStreak = 1
        for i in range(lnums):
            if nums[i] == nums[i - 1] + 1:
                currStreak += 1
                maxStreak = max(currStreak,maxStreak)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                currStreak = 1
        return maxStreak

 
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     num_set = set(nums)
    #     streak = 0

    #     for n in num_set:
    #         if n - 1 not in num_set:
    #             current = n
    #             current_streak = 1
            
    #             while current + 1 in num_set:
    #                 current += 1
    #                 current_streak += 1

    #             streak = max(streak, current_streak)
    #     return streak
    
    # def sorted(self, nums: List[int]) ->  int:
    #     if not nums:
    #         return 0
    #     nums.sort()
    #     longest_streak = 0
    #     for i, n in enumerate(nums):
    #         if i == 0:
    #             current_streak = 1
    #         elif nums[i - 1] == n - 1:
    #             current_streak += 1
    #         elif nums[i - 1] == n:
    #             continue
    #         else:
    #             current_streak = 1
            
    #         longest_streak = max(longest_streak, current_streak)
        
    #     return longest_streak

    

nums = [100,4,200,1,3,2]
nums2 = [1,2,0,1]
print(Solution().sorted(nums))
print(Solution().sorted(nums2))
