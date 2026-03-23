class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        k=len(text1)
        m=len(text2)
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        for i in range(1,k+1):
            for j in range(1,m+1):
                if(text1[i-1]==text2[j-1]):
                    curr[j]=prev[j-1]+1
                else:
                    curr[j]=max(prev[j],curr[j-1])
            prev, curr = curr, [0] * (m + 1)
        return prev[m]
