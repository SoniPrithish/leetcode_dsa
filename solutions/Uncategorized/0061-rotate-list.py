# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size=0
        temp=head
        while(temp):
            size+=1
            temp=temp.next
        if size==1 or size==0:
            return head
            
        if k%size==0:
            return head
        else:
            k=k%size
            temp2=head
            temp3=ListNode(0)
            for i in range((size-1)-k):
                temp2=temp2.next
                
        temp3=temp2.next
        print(temp3.val)
        temp2.next=None
        temp4=temp3
        print(temp4.val)
        while(temp3.next):
            temp3=temp3.next
            print(temp3.val)
        temp3.next=head
        head=temp4
        return head
