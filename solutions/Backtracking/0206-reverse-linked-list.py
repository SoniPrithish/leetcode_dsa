# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nex=head
        prev=None       
        while nex is not None:
            nex=head.next
            head.next=prev
            prev=head
            head=nex
        return prev
