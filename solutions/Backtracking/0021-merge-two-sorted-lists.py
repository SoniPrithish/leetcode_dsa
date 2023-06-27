# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=list1
        q=list2
        if p and not q:
            return p
        if not p and q:
            return q
        if not p and not q:
            return p    
        head=None
        while(p or q):
            result=ListNode(0)
            if p.val<q.val:
                result.val=p.val
                p=p.next
            else:
                result.val=q.val
                q=q.next
            if not head:
                head=result
                ptr=result
            else:
                ptr.next=result
                ptr=result
            if p==None and q!=None:
                ptr.next=q
                return head
            if p!=None and q==None:
                ptr.next=p
                return head
        return head
