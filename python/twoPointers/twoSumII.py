from typing import List

class Solution:
    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1
        rv = []
        l = len(numbers)
        while(p1 < (l - 1)):
            while p2 < l:
                if numbers[p1] + numbers[p2] == target:
                    rv.extend([p1 + 1,p2 + 1])
                    return rv
                if numbers[p1] + numbers[p2] > target:
                    p1 = p2 - 2
                    p2 -= 1
                    continue
                p2 += 1
            p1 += 1
            p2 = p1 + 1
        return rv






numbers = [2,7,11,15]
nums2 = [2, 3, 4, 10, 12]

nums3 = []

for i in range(100000):
    nums3.append(0)
nums3.extend([2,3])
for i in range (100000):
    nums3.append(9)

print("expecting [1, 2]")
print(Solution().twoSumII(numbers, 9))
print("expecting [3, 4]")
print(Solution().twoSumII(numbers, 26))
print("expecting [2, 3]")
print(Solution().twoSumII(nums2, 7))
print("expecting [2, 4]")
print(Solution().twoSumII(nums2, 13))
print("expecting [100001,100002]")
print(Solution().twoSumII(nums3,5))
