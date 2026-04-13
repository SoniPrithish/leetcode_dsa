class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        fresh=0
        time=0
        q=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        while(q and fresh>=1):
            for _ in range(len(q)):    
                r,c=q.popleft()

                if c-1>=0 and grid[r][c-1]==1:
                    fresh-=1
                    grid[r][c-1]=2
                    q.append((r,c-1))
                if c+1<col and grid[r][c+1]==1:
                    fresh-=1
                    grid[r][c+1]=2
                    q.append((r,c+1))
                if r-1>=0 and grid[r-1][c]==1:
                    fresh-=1
                    grid[r-1][c]=2
                    q.append((r-1,c))
                if r+1<row and grid[r+1][c]==1:
                    fresh-=1
                    grid[r+1][c]=2
                    q.append((r+1,c))
            time+=1
        return time if fresh==0 else -1
