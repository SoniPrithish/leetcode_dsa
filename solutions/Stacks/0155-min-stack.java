class MinStack {
    Stack<Long> s = new Stack<>();
    long mini;

    public MinStack() {
        mini = Long.MAX_VALUE;
    }

    public void push(int val) {
        if (s.isEmpty()) {
            mini = val;
            s.push((long) val);
        } else {
            if (val < mini) {
                s.push(2L * val - mini);
                mini = val;
            } else {
                s.push((long) val);
            }
        }
    }

    public void pop() {
        if (s.peek() < mini) {
            mini = 2 * mini - s.peek();
        }
        s.pop();
    }

    public int top() {
        if (s.peek() < mini) {
            return (int) mini;
        }
        return s.peek().intValue();
    }

    public int getMin() {
        return (int) mini;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
