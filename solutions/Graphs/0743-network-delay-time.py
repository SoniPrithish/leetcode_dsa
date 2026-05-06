class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[float('inf')]*(n+1)
        dist[k]=0
        pq=[]
        heapq.heappush(pq,(0,k)) 
        al=defaultdict(list)
        for u,v,w in times:
            al[u].append((v,w))
        while pq:
            d,u=heapq.heappop(pq)
            if dist[u]<d:
                continue
            for v,w in al[u]:
                if dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w
                    heapq.heappush(pq,(dist[v],v))
        return max(dist[1:]) if max(dist[1:])<float('inf') else -1
