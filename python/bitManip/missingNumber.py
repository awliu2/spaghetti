class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        expectedSum = l * (l + 1) // 2
        for i in nums:
            expectedSum -= i
        return expectedSum