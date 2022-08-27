"""
    Given two strings s and t of lengths m and n respectively, 
    return the minimum window substring of s such that 
    every character in t (including duplicates) is included in the window. 

    If there is no such substring, return an empty string.
"""

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCounts = {}
        tCounts = dict(collections.Counter(t))
        print(len(tCounts))
        l = 0
        found = False
        rv = s
        for r, c in enumerate(s):
            sCounts[c] = 1 + sCounts.get(c, 0)
            while self.checkLetter(sCounts, tCounts):
                found = True
                # current substring contains all letters in t
                if (r - l + 1) < len(rv):
                    rv = s[l:r + 1]
                sCounts[s[l]] -= 1 
                l += 1
        return rv if found else ""
        
        
    def checkLetter(self, sCounts, tCounts):
        for letter, count in tCounts.items():
            if letter not in sCounts.keys() or sCounts[letter] < count:
                return False
        return True

    def Soln2(self, s: str, t: str) -> str:
        if t == "" : return ""

        sCounts = {}
        tCounts = dict(collections.Counter(t))

        rv = s
        l = 0
        found = False
        have, need = 0, len(tCounts)

        for r, c in enumerate(s):
            sCounts[c] = 1 + sCounts.get(c, 0)

            if c in tCounts and sCounts[c] == tCounts[c]:
                have += 1
            print(have)
            while have == need:
                found = True
                if r - l + 1 < len(rv):
                    rv = s[l : r + 1]

                sCounts[s[l]] -= 1

                if s[l] in tCounts and sCounts[s[l]] < tCounts[s[l]]:
                    have -= 1

                l += 1
        
        return rv if found else ""

            



    



s, t = "ADOBECODEBANC", "ABC" # returns 'BANC'

# print(Solution().minWindow(s,t))
print(Solution().Soln2(s,t))
