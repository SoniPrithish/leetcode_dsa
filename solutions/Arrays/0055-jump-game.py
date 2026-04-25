class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxjump=nums[0]

        for i in range(n):
            if i > maxjump:
                return False
            jump=nums[i]
            maxjump=max(maxjump,i+jump)
        return True
