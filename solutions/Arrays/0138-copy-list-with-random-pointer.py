"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        d={}
        if(head==None):
            return None
        else:
            d[temp]=Node(temp.val)
        while(temp.next):
            temp=temp.next
            d[temp]=Node(temp.val)
        temp2=head
        pre=Node(0)
        while(temp2):
            if(temp2.next!=None):
                d[temp2].next=d[temp2.next]
            if(temp2.random!=None):
                d[temp2].random=d[temp2.random]
            
            temp2=temp2.next 

                 
        return d[head]
