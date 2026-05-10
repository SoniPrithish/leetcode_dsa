class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left=1
        right=len(nums)-1
        print(nums)
        while(left<right):
            mid=(left+right)//2
            ct=0
            for num in nums:
                if num<=mid:
                    ct+=1
            if ct>mid:
                right=mid
            else:
                left=mid+1
        return left
