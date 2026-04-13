class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row=len(isConnected)
        col=len(isConnected[0])
        cities={i:[] for i in range(row)}
        visited=set()
        output=0
        def dfs(city):
            for j in range(col):
                if  isConnected[city][j]==1 and j not in visited :
                    visited.add(j)
                    dfs(j)
        for i in range(row):
            if i not in visited:
                visited.add(i)
                dfs(i)
                output+=1
            
                
        return output
