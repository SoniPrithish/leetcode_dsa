class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.heap=[]
        for i in range(len(nums)):
            heapq.heappush(self.heap,nums[i])
            if (len(self.heap)>k):
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif self.heap[0]>val:
            return self.heap[0]
            
        else:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
