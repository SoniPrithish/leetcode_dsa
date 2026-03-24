# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while(fast.next.next):
            slow=slow.next
            fast=fast.next.next
        temp=slow.next.next
        slow=slow.next
        prev=None
        while(temp):
            slow.next=prev
            prev=slow
            slow=temp
            temp=temp.next
        slow.next=prev
        maxsum=0    
        while(slow):
            sum=slow.val+head.val
            head=head.next
            slow=slow.next
            if(sum>maxsum):
                maxsum=sum
        return maxsum
