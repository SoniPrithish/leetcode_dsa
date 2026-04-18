class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feq=Counter(nums)
        heap=[(-kount,num) for num,kount in feq.items()]
        heapq.heapify(heap)
        ans=[]
        for i in range(k):
            kount,element=heapq.heappop(heap)
            ans.append(element)
        return ans
