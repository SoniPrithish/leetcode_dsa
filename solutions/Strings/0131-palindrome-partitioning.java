class Solution {
    public List<List<String>> partition(String s) {
     List<List<String>> result=new ArrayList<>();
     List<String> path =new ArrayList<>();
     part(s,0,path,result);  
     return result; 
    }
    private void part(String s,int index,List<String> path,List<List<String>> result)
    {
        if(index==s.length())
        {
            result.add(new ArrayList(path));
            return;
        }
        for(int end=index;end<s.length();end++)
        {
            String substring=s.substring(index,end+1);
            if(isPalindrome(substring))
            {
                path.add(substring);
                part(s,end+1,path,result);
                path.remove(path.size()-1);
            }
        }
    }
    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) return false;
        }
        return true;
    }
}
