class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n=nums.length;
        Deque<Integer> dq= new ArrayDeque<>();
        int[] res=new int[n-k+1];
        int ok=0;
        for(int i=0;i<n;i++)
        {
            //Making sure elements in window are there in deque
            if(!dq.isEmpty() && dq.peek()==i-k)
            {
                dq.poll();
            }

            // Remove Useless elements
            while(!dq.isEmpty() && nums[dq.peekLast()]<nums[i])
            {
                dq.pollLast();
            }
            dq.offer(i);
            if (i >= k - 1) {
                res[ok++] = nums[dq.peek()];
            }
        }
    return res;
       
    }
}
