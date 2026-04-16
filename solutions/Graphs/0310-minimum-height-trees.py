class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj={i:[] for i in range(n)}
        degree=[0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1
        q=deque()
        for node in range(n):
            if degree[node]==1:
                q.append(node)
        remaining=n
        while(remaining>2):
            size=len(q)
            remaining-=size

            for _ in range(size):
                node=q.popleft()

                for nei in adj[node]:
                    degree[nei]-=1
                    if degree[nei]==1:
                        q.append(nei)
        return list(q)
