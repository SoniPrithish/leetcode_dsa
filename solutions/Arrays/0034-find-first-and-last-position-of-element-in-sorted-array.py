class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearchsmall(start,end,arr,target):
            smallest=-1
            while(start<=end):
                mid=(start+end)//2
                if arr[mid]==target:
                    smallest=mid
                    end=mid-1
                elif arr[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return smallest

        def binarysearchbig(start,end,arr,target):
            biggest=-1
            while(start<=end):
                mid=(start+end)//2
                if arr[mid]==target:
                    biggest=mid
                    start=mid+1
                elif arr[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return biggest
        result=[]
        small=binarysearchsmall(0,len(nums)-1,nums,target)
        big=binarysearchbig(0,len(nums)-1,nums,target)
        result.extend([small,big])
        return result
