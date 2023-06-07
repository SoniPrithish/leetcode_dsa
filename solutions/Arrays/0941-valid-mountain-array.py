class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr))<3:
            return False
        ct_change=0
        flag="incr"
        if arr[0]>arr[1]:
            return False
        elif arr[0]==arr[1]:
            return False
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i+1] and flag=="incr":
                ct_change+=1
                flag="decr"
            if arr[i]<arr[i+1] and flag=="decr":
                ct_change+=1
                flag="incr"
            
            if arr[i]==arr[i+1]:
                return False
        if ct_change!=1:
                return False
        return True
