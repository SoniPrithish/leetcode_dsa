class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        for i in range(len(temperatures)-1,-1,-1):
            curr=temperatures[i]
            while stack and curr>=stack[-1][0]:
                p,ind=stack.pop()
           # print(stack)
            if not stack:
                stack.append([curr,i])
                temperatures[i]=0
                continue
            
            temperatures[i]=stack[-1][1]-i
            stack.append([curr,i])
        return temperatures
