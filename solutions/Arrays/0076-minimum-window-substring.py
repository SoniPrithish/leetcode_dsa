class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or (not s or not t ) :
            return ""
        m=len(s)
        n=len(t)
        need=Counter(t)
        formed=0
        window=defaultdict(int)
        minlen=float('inf')
        beststart=0
        left=0
        required=len(need)

        for right in range(m):
            window[s[right]]+=1
            if (s[right] in need and window[s[right]]==need[s[right]]):
                formed+=1
            
            while(formed==required):
                if right-left+1<minlen:
                    minlen=right-left+1
                    beststart=left
                
                window[s[left]]-=1
                if(s[left] in need and window[s[left]]<need[s[left]]):
                    formed-=1
                left+=1
        if minlen == float("inf"):
            return ""
        return s[beststart:beststart+minlen]
