class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need=Counter(p)
        left=0
        
        formed=0
        d=defaultdict(int)
        m=len(s)
        reqd=len(p)
        ans=[]
        for i in range(m):
            ch=s[i]
            if ch in need:
                d[ch] += 1
                formed += 1
                while d[ch] > need[ch]:
                    leftchar = s[left]
                    d[leftchar] -= 1
                    if d[leftchar] == 0:
                        del d[leftchar]
                    left += 1
                    formed -= 1
                
            else:
                formed=0
                left=i+1
                d=defaultdict(int)
            if formed==reqd and need==d:
                
                ans.append(left)
                leftchar=s[left]
                d[leftchar]-=1
                if d[leftchar] == 0:
                    del d[leftchar]
                left+=1
                formed-=1
        return ans
