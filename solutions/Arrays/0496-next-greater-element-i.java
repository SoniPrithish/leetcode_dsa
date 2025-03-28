class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] result=new int[(nums1.length)];
        int ct=0;
    for(int i:nums1)
    {
        int ok=i;
        boolean flag=false;
        int op=-1;
        for(int j:nums2)
        {

            if(i==j)
            {
                flag=true;
            }
            if(flag==true && j>ok)
            {
                op=j;
                break;
            }
            
            

        }
        result[ct]=op;
        ct++;
    }
    return result;
    }
}
