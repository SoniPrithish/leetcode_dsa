class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i in range(len(heights)):
            while(stack and heights[stack[-1]]>heights[i]):
                element=stack.pop()
                nse=i
                pse= stack[-1] if stack else -1
                maxarea=max(maxarea,heights[element]*(nse-pse-1))

            stack.append(i)
        while stack:
                element=stack.pop()
                nse=len(heights)
                pse=stack[-1] if stack else -1
                maxarea=max(maxarea,heights[element]*(nse-pse-1))
        return maxarea
