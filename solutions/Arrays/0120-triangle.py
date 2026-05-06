class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[i for i in triangle[n-1]]
        for i in range(n-2,-1,-1):
            curr=dp[:]
            for j in range(i+1):
                curr[j]=triangle[i][j]+min(dp[j],dp[j+1])
            dp=curr[:-1]
        return dp[0]
