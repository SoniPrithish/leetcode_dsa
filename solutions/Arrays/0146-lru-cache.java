class LRUCache {
    class Node {
        int key;
        int value;
        Node prev, next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
    Node head=new Node(-1,-1);
    Node tail=new Node(-1,-1);
    int cap;
    HashMap<Integer,Node> m=new HashMap<>();
    public LRUCache(int capacity) {
        cap=capacity;
        head.next=tail;
        tail.prev=head;
    }
    private void addNode(Node newnode)
    {
        Node temp=head.next;

        newnode.next=temp;
        newnode.prev=head;

        head.next=newnode;
        temp.prev=newnode;
    }
    private void deleteNode(Node delnode)
    {
        Node prevv=delnode.prev;
        Node nextt=delnode.next;
        prevv.next=nextt;
        nextt.prev=prevv;
    }
    
    public int get(int key) {
        if(m.containsKey(key))
        {
            Node resenode=m.get(key);
            int ans=resenode.value;
            m.remove(key);
            deleteNode(resenode);
            addNode(resenode);
            m.put(key,head.next);
            return ans;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (m.containsKey(key))
        {
            Node curr=m.get(key);
            m.remove(key);
            deleteNode(curr);

        }
        if(m.size()==cap)
        {
            m.remove(tail.prev.key);
            deleteNode(tail.prev);
        }
        addNode(new Node(key,value));
        m.put(key,head.next);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
