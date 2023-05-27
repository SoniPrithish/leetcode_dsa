class Solution:
    def isMonotonic(self, array: List[int]) -> bool:
        A=0
        for i in range(len(array)-1):
            if array[i]<array[i+1]:
                A=1
                break
            elif array[i]>array[i+1]:
                A=2
                break
            else:
                pass
        if A==0:
            return True
        if A==1:
            for i in range(len(array)-1):
                
                if array[i]<=array[i+1]:
                    continue
                else:
                    return False
            return True
        if A==2:
            for i in range(len(array)-1):
                if array[i]>=array[i+1]:
                    continue
                else:
                    return False
            return True
