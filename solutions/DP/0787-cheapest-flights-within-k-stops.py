class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF=float('inf')
        dp=[INF]*n
        dp[src]=0

        for i in range(k+1):
            
            curr=dp[:]

            for u,v,w in flights:
                if dp[u]!=INF:
                    curr[v]=min(curr[v],dp[u]+w)
            dp=curr
        return -1 if dp[dst]==INF else dp[dst]
