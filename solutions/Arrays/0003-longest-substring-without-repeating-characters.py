class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        n=len(s)
        l,r=0,0
        maxl=0
        while(r<n):
            if s[r] in d and d.get(s[r]) >= l:
                l = d.get(s[r]) + 1

            d[s[r]] = r  

            maxl=max(maxl,(r-l+1))
            r+=1

        return maxl
