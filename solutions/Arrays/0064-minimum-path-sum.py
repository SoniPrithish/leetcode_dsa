class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        inf=float('inf')
        minpathsum=inf
        m,n=len(grid),len(grid[0])
        next=[inf]*n
        curr=[inf]*n
        curr[0]=grid[0][0]

        for i in range(m):
            for j in range(n):
                if j+1<n:
                    curr[j+1]=min(curr[j+1],curr[j]+grid[i][j+1])
                if i+1<m:
                    next[j]=curr[j]+grid[i+1][j]
            minpathsum=curr[n-1]
            curr=next
            next=[inf]*n
        return minpathsum
