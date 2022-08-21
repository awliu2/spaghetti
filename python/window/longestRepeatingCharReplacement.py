# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.


class Solution:
    def charReplace(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        rv = 0
        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])
            # if (size of window - max freq > k, make window smaller
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            rv = max(rv, r - l + 1)
        return rv
            
                


                













    # def characterReplacement(self, s: str, k: int) -> int:
    #     count = {}
    #     rv = 0
    #     l = 0
    #     maxFreq = 0
    #     for r in range(len(s)):
    #         # add char to count dict
    #         count[s[r]] = 1 + count.get(s[r],0)
    #         # get number of counts of most frequent character, only needs to be updated when value increases
    #         maxFreq = max(maxFreq, count[s[r]])
    #         while (r - l + 1) - maxFreq > k:
    #             count[s[l]] -= 1
    #             l += 1
    #         rv = max(rv, r - l + 1)
    #     return rv

    




    # def characterReplacement(self, s: str, k: int) -> int:
    #     ls = len(s)
    #     if ls == 0:
    #         return 0
    #     if ls == 1:
    #         return 1
        
    #     # window pointers
    #     l = 0
    #     r = 0
    #     rv = 1

    #     # character counting dict
    #     maxDict = {}
    #     maxDict[s[r]] = 1

    #     while l < ls:                    
    #         while (r - l) - max(maxDict.values()) <= k:
    #             rv = max(rv, r - l)
                
    #             if s[r] not in maxDict.keys():
    #                 maxDict[s[r]] = 1
    #             else:
    #                 maxDict[s[r]] += 1
    #             r += 1
                                


    #         maxDict[s[l]] -= 1
    #         l += 1

    #     return rv
            


    # def countChars(self, ss: str) -> int:
    #     maxDict = {}
    #     lss = len(ss)
    #     if lss == 0 or lss == 1:
    #         return lss
    #     for c in ss:
    #         if c not in maxDict.keys():
    #             maxDict[c] = 1
    #         else:
    #             maxDict[c] += 1
    #     return max(maxDict.values())



print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("ABAA", 0))


# print(Solution().countChars("AABBB"))
# print(Solution().countChars("ABCDEEEEE"))
# print(Solution().countChars("A"))
# print(Solution().countChars(""))



