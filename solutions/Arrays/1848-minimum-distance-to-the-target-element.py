class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n=len(nums)
        ans=1001+start
        l=0
        r=n-1
        while(l<=r):
            if nums[l]==target:
                ans=min(abs(l-start),ans)
            if nums[r]==target:
                ans=min(abs(r-start),ans)
            l+=1
            r-=1
        return ans
