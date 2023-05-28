class Solution:
    def arrayPairSum(self, array: List[int]) -> int:
        max=0
        array=sorted(array)
        for i in range(0,len(array),2):
            max=max+array[i]
        return(max)
