from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range((len(text2) + 1))] for _ in range (len(text1) + 1)]
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        
        return dp[0][0]


    def doordash(self, text1, text2):
        
        subarray = set()
        
        @lru_cache(maxsize=None)
        def doordash_oa(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                subarray.add(j)
                return 1 + doordash_oa(i + 1, j + 1)
            else:
                return max(doordash_oa(i + 1, j), doordash_oa(i, j + 1))
        print(doordash_oa(0,0))
        
        removed = list(set(range(len(text2))) - subarray)
        removed.sort()
    
        return removed[-1] - removed[0] + 1

print(Solution().doordash("ACDEF", "ABCDEEEEF"))



        # def memo_LCS(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     # get index of first occurance of text1[i] in text2[j:]
        #     first_occurance = text2.find(text1[i], j)
            
        #     possibility_1 = memo_LCS(i + 1, j)
        #     possibility_2 = 0

        #     if first_occurance != -1:
        #         possibility_2 = 1 + memo_LCS(i + 1, first_occurance + 1)

        #     return max(possibility_1, possibility_2)

        # def optimized_memo(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     if text1[i] == text2[j]:
        #         return 1 + optimized_memo(i + 1, j + 1)

        #     else:
        #         return max(optimized_memo(i + 1, j), optimized_memo(i, j + 1))
        
        # #return memo_LCS(0, 0)
        # return optimized_memo(0, 0)