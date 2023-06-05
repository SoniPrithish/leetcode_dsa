class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=dict()
        ct=-1
        for i in s:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d[i]==1:
                ct=s.index(i)
                break
            
        return ct
