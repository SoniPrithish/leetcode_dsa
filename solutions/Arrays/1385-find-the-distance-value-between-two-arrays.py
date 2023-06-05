class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ct=0
        for i in arr1:
            ct2=0
            for j in arr2:
                if abs(i-j)>d:
                    ct2+=1
                if ct2==len(arr2):
                    ct+=1
        return ct
