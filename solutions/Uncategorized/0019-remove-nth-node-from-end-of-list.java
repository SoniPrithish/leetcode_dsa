/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int i=0;
        ListNode t=head;
        ListNode k=head;
        while(t!=null)
        {
            i++;
            
            t=t.next;
        }
        
        if(i==1)
        {
            head=null;
            k=head;
            
        }
        
        else if(i==n)
        {
            head=head.next;
            k=head;
        }
        
        else{
        for(int j=1;j<(i-n);j++)
        {
            head=head.next;
        }
           
            head.next=(head.next).next;
            
            
        }
        return k;
    }
}
