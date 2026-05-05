class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n

        for i in range(1,m):
            for j in range(1,n):
                top=dp[j]
                left=dp[j-1]
                dp[j]=top+left
        return dp[n-1]
