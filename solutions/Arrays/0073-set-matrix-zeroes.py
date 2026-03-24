class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])

        row=set()
        col=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

        for ind in row:
            for i in range(n):

                matrix[ind][i]=0

        for ind in col:
            for i in range(m):
                matrix[i][ind]=0
