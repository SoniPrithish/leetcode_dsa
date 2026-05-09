class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        dp = [[0]*col for k in range(row)]
        maxpathlen=0
        def dfs(i,j):
            if dp[i][j]:
                return dp[i][j]
            
            dp[i][j]=1

            if i>0 and matrix[i-1][j]>matrix[i][j]:
                dp[i][j]=max(dfs(i-1,j)+1,dp[i][j])
            if i<row-1 and matrix[i+1][j]>matrix[i][j]:
                dp[i][j]=max(dfs(i+1,j)+1,dp[i][j])
            if j>0 and matrix[i][j-1]>matrix[i][j]:
                dp[i][j]=max(dfs(i,j-1)+1,dp[i][j])
            if j<col-1 and matrix[i][j+1]>matrix[i][j]:
                dp[i][j]=max(dfs(i,j+1)+1,dp[i][j])
            
            return dp[i][j]
        
        for i in range(row):
            for j in range(col):
                maxpathlen=max(maxpathlen,dfs(i,j))
        return maxpathlen
