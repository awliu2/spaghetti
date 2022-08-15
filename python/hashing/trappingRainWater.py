from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or height == []:
            return 0
        


        rv = 0
        l = 0
        r = len(height) - 1
        
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                rv += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                rv += rightMax - height[r]
            

        return rv


            

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))

                    



