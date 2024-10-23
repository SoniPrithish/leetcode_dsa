# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        if head==None:
            return False

        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next

        prev=None
        curr=slow
        nxt=slow

        
        while(nxt):
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt

        while(prev):
            if(head.val!=prev.val):
                return False
            else:
                head=head.next
                prev=prev.next
        return True
