class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        nodecount=len(graph)
        rev={i:[] for i in range(nodecount)}
        outdegree=[0]*nodecount

        for node in range(nodecount):
            outdegree[node]=len(graph[node])
            for nei in graph[node]:
                rev[nei].append(node)
        q=deque()
        for i in range(nodecount):
            if outdegree[i]==0:
                q.append(i)
        safe=[]
        while(q):
            curr=q.popleft()
            safe.append(curr)

            for nei in rev[curr]:
                outdegree[nei]-=1
                if outdegree[nei]==0:
                    q.append(nei)
        
        return sorted(safe)
