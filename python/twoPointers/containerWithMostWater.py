from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            depth = min(height[l], height[r])
            res  = max(res, depth * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res


height = [1,8,6,2,5,4,8,3,7]

print(Solution().maxArea(height))