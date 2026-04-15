class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]!=1:
                return
            grid[r][c]=2

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for c in range(COLS):
            if grid[0][c]==1:
                dfs(0,c)
            if grid[ROWS-1][c]==1:
                dfs(ROWS-1,c)
        for r in range(1,ROWS-1):
            if grid[r][0]==1:
                dfs(r,0)
            if grid[r][COLS-1]==1:
                dfs(r,COLS-1)
        
        kount=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    kount+=1
        return kount
