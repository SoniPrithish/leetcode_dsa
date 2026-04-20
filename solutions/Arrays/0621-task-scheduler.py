class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash=Counter(tasks)
        time=0
        heap=[-cnt for cnt in hash.values()]
        heapq.heapify(heap)

        while heap:
            item_picked=[]
            cycle=n+1

            while(heap and cycle>0):
                remaining=heapq.heappop(heap)
                time+=1
                if remaining+1<0:
                    item_picked.append(remaining+1)
                cycle-=1
            for remaining in item_picked:
                heapq.heappush(heap,remaining)
            if heap:
                time+=cycle
        return time
