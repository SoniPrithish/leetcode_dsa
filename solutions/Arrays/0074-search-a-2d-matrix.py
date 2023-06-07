class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col=len(matrix[0])-1
        row=0
        for i in range(len(matrix)):
            if (matrix[i][col]==target):
                return True
            if matrix[i][col]>target:
                row=i
                break
        start=0
        end=len(matrix[0])-1
        while(start<=end):
            mid=(start+end)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                end=mid-1
            elif matrix[row][mid]<target:
                start=mid+1
        return False
