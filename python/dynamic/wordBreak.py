from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len,wordDict+['']))
        
        
        words = set(wordDict)
        
    
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range (1, len(s) + 1):
            for j in range(max(0, i - max_len), i):
                dp[i] = (dp[j] and s[j:i] in words)
                if dp[i] : break
                    
        return dp[len(s)]
                
                