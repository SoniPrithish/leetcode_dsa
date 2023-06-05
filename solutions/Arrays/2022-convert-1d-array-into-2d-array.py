class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result2=[]
        c1=0
        if (m*n)!=len(original):
            return []
        for i in range(m):
            result1=[]
            for j in range(n):
                result1.append(original[c1])
                c1+=1
            result2.append(result1)
        return result2
