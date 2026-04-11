class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf=0
        d=defaultdict(int)
        l,r=0,0
        n=len(s)
        ans=0
        while(r<n):
            d[s[r]]+=1
            maxf=max(maxf,d[s[r]])
            while (r-l+1-maxf>k):
                d[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1            
        return ans
