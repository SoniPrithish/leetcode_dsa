class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
        n=len(s)
        kount=0
        maxkount=0
        l=0
        r=k-1
        for i in range(r+1):
            if s[i] in vowels:
                vowels[s[i]]+=1
                kount+=1
        maxkount=kount
        while(r<n-1):
            if s[l] in vowels:
                vowels[s[l]]=max(0,vowels[s[l]]-1)
                kount-=1 
            l+=1
            r+=1
            if s[r] in vowels:
                vowels[s[r]]+=1
                kount+=1
            
            maxkount=max(kount,maxkount)

        return maxkount
