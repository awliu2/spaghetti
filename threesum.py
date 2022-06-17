from operator import index


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        if len(nums) < 3:
            return ans
        for i in range(len(nums)-2):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                lo=i+1
                hi=len(nums)-1
                s=0-nums[i]
                while lo<hi:
                    if nums[lo]+nums[hi]==s:
                        ans.append([nums[i], nums[lo], nums[hi]])
                        while lo<hi and nums[lo]==nums[lo+1]:
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi-1]:
                            hi-=1
                        lo+=1
                        hi-=1
                    else:
                        if nums[lo]+nums[hi]<s:
                            lo+=1
                        else:
                            hi-=1
        return ans

lst1 = [-1,0,1,2,-1,-4]
lst2 = [0,0,0]

print(Solution().threeSum(lst1))
print(Solution().threeSum(lst2))