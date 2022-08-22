# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        s2Count = {}
        for c in s1:
            s1Count[c] = 1 + s1Count.get(c, 0)
        
        l = 0
        for r in range(len(s2)):
            # print(f"s2Count: {s2Count}")
            # print(f"s1Count: {s1Count}")
            
            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)
            if r >= len(s1):
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    s2Count.pop(s2[l])
                l += 1
            if s1Count == s2Count:
                    return True
        return False

print(Solution().checkInclusion("lle", "hello"))

        