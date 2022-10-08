from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]
        for i in range(1, len(nums)):
            print(jumps)
            if jumps == 0: return False
            jumps = max(nums[i], jumps - 1)
        
        return True
                    

        # def recursive(index):
        #     maxJump = nums[index]
        #     # if maxJump == 0:
        #     #     return False
        #     if index + maxJump >= len(nums) - 1:
        #         return True
            

        #     for jump in range(maxJump):
        #         if recursive(index + jump + 1):
        #             return True
            
        #     return False
        
        # return recursive(0)

    
lst2 = [2,3,1,1,0]
lst = [3,2,1,0,4]
# print(Solution().canJump(lst))
print(Solution().canJump(lst2))
# print(Solution().canJump([0]))
# print(Solution().canJump([1,2,3]))