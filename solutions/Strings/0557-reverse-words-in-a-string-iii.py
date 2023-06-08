class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        result=""
        for i,st in enumerate(s):
            result=result+st[::-1]
        
            if i!=(len(s)-1):
                result=result+" "
        return result
