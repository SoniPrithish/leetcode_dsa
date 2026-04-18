class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[((((x**2)+(y**2))**0.5),x,y) for x,y in points]
        
        heapq.heapify(dist)
        ans=[]
        for i in range(k):
            dista,x,y=heapq.heappop(dist)
            ans.append([x,y])
        return ans
