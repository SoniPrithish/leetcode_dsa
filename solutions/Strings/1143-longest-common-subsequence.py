class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        k=len(text1)
        m=len(text2)
        d = [[0] * (m + 1) for _ in range(k + 1)]
        for i in range(1,k+1):
            for j in range(1,m+1):
                if(text1[i-1]==text2[j-1]):
                    d[i][j]=d[i-1][j-1]+1
                else:
                    d[i][j]=max(d[i-1][j],d[i][j-1])
        return d[k][m]
