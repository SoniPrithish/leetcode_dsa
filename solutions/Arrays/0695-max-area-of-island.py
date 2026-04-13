class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        maxarea_island=0
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0:
                return 0
            grid[r][c]=0

            return 1 + dfs(r,c-1) + dfs(r,c+1) + dfs(r-1,c) + dfs(r+1,c)

        for i in range(row):
            for j in range(col):
                if (grid[i][j]==1):
                    c=dfs(i,j)
                    maxarea_island=max(maxarea_island,c)
                    
        return maxarea_island
