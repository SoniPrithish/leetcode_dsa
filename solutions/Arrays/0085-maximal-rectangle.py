class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row=len(matrix)
        col=len(matrix[0])
        heights=[0]*col
        ans=0
        def maxtriangle(heights):

            stack=[]
            maxarea=0

            for i in range(len(heights)):
                curr=heights[i]
                while(stack and heights[stack[-1]]>curr):
                    element=heights[stack.pop()]
                    nse=i
                    pse=stack[-1] if stack else -1
                    maxarea=max(maxarea,element*(nse-pse-1))
                stack.append(i)
            while stack:
                nse=len(heights)
                element=heights[stack.pop()]
                pse=stack[-1] if stack else -1
                maxarea=max(maxarea,element*(nse-pse-1))
            
            return maxarea
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c]=="1":
                    heights[c]+=1
                else:
                    heights[c]=0
            ans=max(ans,maxtriangle(heights))
        return ans
