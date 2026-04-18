class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for x,y in points:
            d=x*x +y*y
            heapq.heappush(heap,(-d,x,y))

            if len(heap)>k:
                heapq.heappop(heap)
        ans=[]
        for i in range(k):
            a,b,c=heapq.heappop(heap)
            ans.append([b,c])
        return ans
