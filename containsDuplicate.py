# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i in nums:
            if i in numset:
                return True
            else:
                numset.add(i)
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       num_set = set()
       for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)
       return False
