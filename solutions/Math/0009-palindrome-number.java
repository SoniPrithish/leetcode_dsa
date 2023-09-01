class Solution {
    public boolean isPalindrome(int x) {
        int y=x;
        int rev=0;
    
        while(y>0){
        
            rev=10*(rev) + (y%10);
            y=(y/10);
        }
        if (rev==x){
            return true;
        }
        else{
            return false;
        }
    }
}
