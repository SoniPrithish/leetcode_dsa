class MyQueue {

    private Stack<Integer> q1;
    private Stack<Integer> q2;
    public MyQueue() {
        q1=new Stack<>();
        q2=new Stack<>();
    }
    
    public void push(int x) {
        while (q1.empty() == false) {
            q2.push(q1.peek());
            q1.pop();
        }
       
        q1.push(x);

        while (q2.empty() == false) {
            q1.push(q2.peek());
            q2.pop();
        }
    }
    
    public int pop() {
        return q1.pop();
    }
    
    public int peek() {
        return q1.peek();
    }
    
    public boolean empty() {
        return q1.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
