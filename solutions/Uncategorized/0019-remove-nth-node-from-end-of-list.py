# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        curr=head
        z=0
        if head.next==None:
            return None
        while(curr!=None):
            z+=1
            curr=curr.next
        curr=head
        print(curr)
        print(z)
        print(head)
        print(z-n)
        prev=None
        for i in range(z-n-1):
            print(i)
        
            curr=curr.next
        if z-n==0:
            head=head.next
        curr.next=curr.next.next
        return head
