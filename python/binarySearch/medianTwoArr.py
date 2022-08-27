from typing import List
from math import inf

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalSize = len(nums1) + len(nums2)
        totalMid= totalSize // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums1, nums2

        l1 = 0
        r1 = len(nums1) - 1
        while True:
            mid1 = (l1 + r1) // 2
            mid2 = totalMid - mid1 - 2
            
            maxLeft1 = nums1[mid1] if mid1 >= 0 else float("-infinity")

            minRight1 = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float("infinity")

            maxLeft2 = nums2[mid2] if mid2 >= 0 else float("-infinity")

            minRight2 = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float("infinity")
            
            if maxLeft1 < minRight2 and maxLeft2 < minRight1:
                if totalSize % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return min(minRight1, minRight2)
            
            elif maxLeft1 > minRight2:
                r1 = mid1 - 1
            if maxLeft2 > minRight1:
                l1 = mid1 + 1

            

            