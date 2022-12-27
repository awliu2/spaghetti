class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for row in reversed(range(m)):
            for col in reversed(range(n)):
                # dp[row][col] += 1
                if row + 1 < m:
                    dp[row][col] += dp[row + 1][col]
                if col + 1 < n:
                    dp[row][col] += dp[row][col + 1]
                print(dp)
        
        
        return dp[0][0]


print(Solution().uniquePaths(2,2))
            
    