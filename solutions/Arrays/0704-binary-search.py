class Solution:
    k=-1
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)-1
        self.solve(0,n,nums,target)
        return self.k
    def solve(self,start,end,nums,target):
        mid=(start+(end-start)//2)
        print(mid)
        if(start>end):
            return -1
        if(nums[mid]==target):
            self.k=mid
            return mid
        elif(target>nums[mid]):
            self.solve(mid+1,end,nums,target)
        else:
            self.solve(start,mid-1,nums,target)
