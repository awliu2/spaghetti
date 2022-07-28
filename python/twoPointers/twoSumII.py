from typing import List

class Solution:
    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 0
        rv = []
        l = len(numbers)
        while(p1 < (l - 1)):
            while p2 < l:
                if numbers[p1] + numbers[p2] == target:
                    rv.extend([p1,p2])
                    return rv
                p2 += 1
            p1 += 1
            p2 = p1 + 1
        return rv






numbers = [2,7,11,15]
nums2 = [2, 3, 4, 10, 12]

print("expecting [0, 1]")
print(Solution().twoSumII(numbers, 9))
print("expecting [2, 3]")
print(Solution().twoSumII(numbers, 26))
print("expecting [1, 2]")
print(Solution().twoSumII(nums2, 7))
print("expecting [1, 3]")
print(Solution().twoSumII(nums2, 13))