class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        m=len(s)
        n=len(t)
        if(m==0):
            return True
        if(m>n):
            return False
        while(j<n):
            if(s[i]==t[j]):
                if(i==m-1):
                    return True
                i+=1
                j+=1
            else:
                j+=1
        if(i==(len(s)-1) and j<=(len(s)-1) ):
            print(i,j)
            return True
        return False
