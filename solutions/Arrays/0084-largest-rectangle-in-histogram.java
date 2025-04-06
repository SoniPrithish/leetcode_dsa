class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> st=new Stack<>();
        int maxA=0;
        int n=heights.length;
        for(int i=0;i<=n;i++)
        {
            while(!st.isEmpty() && (i==n || heights[st.peek()]>heights[i]))
            {   
                int height=heights[st.peek()];
                st.pop();
                int width;
                if(st.empty())
                {
                    width=i;
                }
                else
                {
                    width=i-st.peek()-1;
                }
                maxA=Math.max(maxA,height*width);
            }
            st.push(i);
        }
        return maxA;
    }
}
