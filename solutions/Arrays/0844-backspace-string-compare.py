class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        new_s=""
        new_t=""
        a=0
        for i in range((len(s)-1),-1,-1):
            if s[i]=="#":
                del s[i]
                a+=1
            elif a>0:
                del s[i]
                a-=1
        a=0
        for i in range((len(t)-1),-1,-1):
            if t[i]=="#":
                del t[i]
                a+=1
            elif a>0:
                del t[i]
                a-=1
        
        if len(t)!=len(s):
            return False
        for i in range(len(t)):
            new_s+=s[i]
            new_t+=t[i]
            print(new_s,new_t)
            if new_t!=new_s:
                return False
        return True
