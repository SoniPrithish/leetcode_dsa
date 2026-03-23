class Solution:
    def minInsertions(self, s: str) -> int:
        t=s[::-1]
        if t==s:
            return 0
        k=len(s)
        m=len(t)
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        for i in range(1,k+1):
            for j in range(1,m+1):
                if(s[i-1]==t[j-1]):
                    curr[j]=prev[j-1]+1
                else:
                    curr[j]=max(prev[j],curr[j-1])
            prev, curr = curr, [0] * (m + 1)
        return k-prev[m]
