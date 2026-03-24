class Solution {
    public boolean isValid(String s) {
        Stack<Character> st= new Stack<>();
        for(int i=0;i<s.length();i++)
        {   char   currentchar=s.charAt(i);
            if(currentchar=='[' )
            {
                st.push(']');
            }
            else if(currentchar=='{' )
            {
                st.push('}');
            }
            else if(currentchar=='(')
            {
                st.push(')');
            }
            else
            {
                if(st.empty() || st.pop()!=currentchar)
                {
                    return false;
                }
               
            }
        }
        return st.empty();
    }
}
