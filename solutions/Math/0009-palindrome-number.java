class Solution {
    public boolean isPalindrome(int x) {
        int y=x;
        int rev=0;
        int res;
        while(y>0){
            res=y%10;
            rev=10*(rev) + (res);
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
