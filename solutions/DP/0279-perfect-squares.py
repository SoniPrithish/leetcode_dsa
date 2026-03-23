class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0

        for i in range(1,n+1):
            for j in range(1,n+1):
                jj=j*j
                if i-jj<0:
                    break
                dp[i]=min(dp[i],1+dp[i-jj])
        return dp[n]
