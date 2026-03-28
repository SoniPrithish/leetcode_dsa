class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxr=nums[0]
        n=len(nums)
        
        for i in range(n):
            if(i>maxr):
                print("I",i,"MAxr",maxr)
                return False
            jump=nums[i]
            maxr=max(maxr,i+jump)
        return True
