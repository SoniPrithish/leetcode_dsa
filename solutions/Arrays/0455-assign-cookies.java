class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int i=0;
        int j=0;
        int result=0;

        while(i<=(g.length-1) && j<=(s.length-1) )
        {

            if(g[i]==s[j])
            {
                result+=1;
                j++;
                i++;
            }
            else if(g[i]<s[j])
            {
                result+=1;
                j++;
                i++;
            }
            else
            {
                j++;
            }
        }
    return result;

    }
}
