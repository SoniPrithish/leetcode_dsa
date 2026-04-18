class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[(-stone) for stone in stones]
        heapq.heapify(heap)
        while(len(heap)>1):
            big1=-(heapq.heappop(heap))
            big2=-(heapq.heappop(heap))
            if big1 == big2:
                continue
            else:
                heapq.heappush(heap,-(big1-big2))
        return -heapq.heappop(heap) if len(heap)>0 else 0
