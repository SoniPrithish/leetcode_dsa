# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(pq,(node.val,i,node))
        Node=ListNode(-1)
        tail=Node
        while(pq):
            a,i,node=heapq.heappop(pq)
            tail.next=node
            tail=tail.next
            if node.next:
                heapq.heappush(pq,(tail.next.val,i,tail.next))
        return Node.next
