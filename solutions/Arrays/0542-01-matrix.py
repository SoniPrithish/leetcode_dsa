class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS=len(mat)
        COLS=len(mat[0])
        q=deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c]==0:
                    q.append((r,c))
                else:
                    mat[r][c]=-1
        while(q):
            r,c=q.popleft()

            if r+1<ROWS and mat[r+1][c]==-1:
                mat[r+1][c]=mat[r][c]+1
                q.append((r+1,c))
            if r-1>=0 and mat[r-1][c]==-1:
                mat[r-1][c]=mat[r][c]+1
                q.append((r-1,c))
            if c+1<COLS and mat[r][c+1]==-1:
                mat[r][c+1]=mat[r][c]+1
                q.append((r,c+1))
            if c-1>=0 and mat[r][c-1]==-1:
                mat[r][c-1]=mat[r][c]+1
                q.append((r,c-1))

        return mat
