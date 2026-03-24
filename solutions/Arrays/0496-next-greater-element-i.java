class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> nge=new Stack<>();
        Map<Integer,Integer> ok=new HashMap<>();
        int[] result=new int[nums1.length];
        int[] c=nums2;
        for(int i=nums2.length-1;i>=0;i--)
        {
            int temp2=nums2[i];

            if(nge.isEmpty())
            {
                nums2[i]=-1;
                ok.put(temp2,-1);
                nge.push(temp2);
                
            }
            else if(nge.peek()<=temp2)
            {
                while(!nge.isEmpty() && nge.peek()<=temp2)
                {
                    nge.pop();
                }
                if (nge.isEmpty())
                {
                    nums2[i]=-1;
                    ok.put(temp2,-1);
                    nge.push(temp2);
                
                    continue;
                }
                nums2[i]=nge.peek();
                ok.put(temp2,nge.peek());
                nge.push(temp2);
                
                
            }
            else
            {
                nums2[i]=nge.peek();
                ok.put(temp2,nge.peek());
                nge.push(temp2);
            }

        }
    for(int i=0;i<nums1.length;i++)
    {
        result[i]=ok.get(nums1[i]);
    }



    return result;

    }
}
