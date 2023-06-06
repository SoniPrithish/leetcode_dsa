class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ab=list(i for i in range(len(s)+1))
        result=[]

        for i in range(len(s)):
            if s[i]=="I":
                var=ab[0]
                result.append(var)
                ab.remove(var)
            else:
                var=ab[len(ab)-1]
                result.append(var)
                ab.remove(var)
        result.append(ab[0])
        return result
