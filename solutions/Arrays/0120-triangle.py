class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        memo={}
        
        def dfs(i,j):
            
            if (i+1==n):
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            down=dfs(i+1,j)
            diag=dfs(i+1,j+1)
            memo[(i,j)]=triangle[i][j] +min(down,diag)
            return memo[(i,j)]

        return dfs(0,0)
