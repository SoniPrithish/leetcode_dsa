class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand(left,right):
            count=0
            while(left>=0 and right<n and s[left]==s[right]):
                left-=1
                right+=1
            
            return right-left-1,left+1,right

        longest=0
        l1,r1=0,0
        for i in range(n):
            pl,l2,r2=expand(i,i)
            if pl>longest:
                l1,r1=l2,r2
                longest=pl
            pl,l2,r2=expand(i,i+1)
            if pl>longest:
                l1,r1=l2,r2
                longest=pl
        return s[l1:r1]
