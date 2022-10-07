from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in word_set:
                    dp[i] = True

        return dp[-1]
                        
        
        # def recurse(s : str) -> bool:
        #     if s == "" or s in wordDict:
        #         return True

        #     for i in range(len(s)):
        #         if s[0:i] in wordDict:
        #             if recurse(s[i:]):
        #                 return True
        #     return False

        # return recurse(s)

        


s = "leetcode"
word_dict = ["leet","code"]

s2 = "applepenapple"
word_dict2 = ["apple","pen"]

s3 = "catsandog"
word_dict3 = ["cats","dog","sand","and","cat"]


print(Solution().wordBreak(s3, word_dict3))
