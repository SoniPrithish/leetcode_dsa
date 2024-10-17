# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=0
        l2=0

        currA=headA
        currB=headB        
        while(headA or headB):
            if headA:
                l1+=1
                headA=headA.next
            if headB:
                
                l2+=1

                headB=headB.next

        for i in range(int(abs(l2-l1))):
            if(l2>l1):
                currB=currB.next
            elif (l1>l2):
                currA=currA.next
        while(currA or currB):
            if currA==currB:
                return currA
            else:
                currA=currA.next
                currB=currB.next
        return None
